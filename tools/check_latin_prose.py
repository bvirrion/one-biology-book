#!/usr/bin/env python3
"""Gate 9 -- the twin-comparison prose gate, for editions written in the Latin
alphabet (fr, nl, es, pt, id).

WHY THIS EXISTS. Gates 5 and 6 are Latin-oriented but score nothing about
whether a fragment was translated; gate 7 (Devanagari, Arabic) works because
residual English is *visibly foreign* in a non-Latin script; gate 8
(Indonesian) works because a curated list of English words that are not
Indonesian words can be built. Neither trick is available for French, Dutch,
Spanish or Portuguese: an English word is spelled with the same letters as a
French one, and no word list can separate them cheaply.

So this gate does not ask "is this English?". It asks a question that needs no
per-language knowledge at all:

    IS THIS FRAGMENT BYTE-IDENTICAL TO ITS ENGLISH TWIN, AND DOES IT CONTAIN
    A LOWERCASE WORD?

A translated fragment that still equals the English one either was never
touched or is a proper noun. Proper nouns (Gauss, Thevenin, Bolzano--
Weierstrass, RLC) carry no lowercase word once math and macros are stripped,
so requiring one removes nearly every false positive without knowing a word of
the target language. The comparison is positional: the Nth fragment of the
translated file against the Nth fragment of its English twin, and it is
skipped entirely when the counts differ, because then check_translation.sh
owns the divergence.

WHAT IT COVERS -- exactly the classes that shipped green in real editions:

  title     environment optional titles (\\begin{definition}[Physical quantity])
            and \\chapter/\\section headings
  text      \\text{...} inside math, including the subscripts that no reader of
            the source ever looks at (S_{\\text{created}})
  node      TikZ/pgfplots node text, node[...] {...}, and axis labels
  dup       a line repeated verbatim from the English twin sitting immediately
            above or below its own translation (an applier misuse: the
            English line was kept AND translated)

Each class was a real defect in a shipped or nearly-shipped edition. The
Portuguese Book 3 edition carried three untranslated environment titles, one
duplicated English line, fourteen English \\text{} subscripts and one English
TikZ node -- all of them through a green check_translation.sh and a clean PDF.

DELIBERATE BLIND SPOTS. \\mathrm{} is mathematics and stays English across
every edition by series convention (S_{\\mathrm{created}}), so it is never
compared. Unit arguments (\\qty, \\unit, \\num) are mathematics too. A fragment
whose lowercase words are all in ALLOWED_IDENTICAL is skipped: those are
strings a Latin-script edition legitimately leaves alone.

Usage:
    python3 tools/check_latin_prose.py parts/bachelor-1/fr parts/bachelor-1/solutions/fr
    python3 tools/check_latin_prose.py --quiet <dirs...>

The English twin is found by dropping the /<lang>/ path component, the same way
check_indonesian_prose.py does it.
"""
import argparse
import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from check_hindi_prose import strip_comments          # noqa: E402

# --------------------------------------------------------------------------
# Fragment extractors. Each returns a LIST in document order, so the Nth
# fragment of a translation can be compared with the Nth of its twin.
# --------------------------------------------------------------------------
TITLE_ENVS = ("definition", "theorem", "proposition", "lemma", "corollary",
              "example", "remark", "method", "notation", "exercise",
              "problem", "proof", "omfigure", "figure", "table")
TITLE_RE = re.compile(
    r"\\begin\{(?:" + "|".join(TITLE_ENVS) + r")\}"
    r"\[((?:[^\[\]]|\[[^\]]*\])*)\]"
    r"|\\(?:chapter|section|subsection)\*?\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")

# \text{...} but NOT \mathrm{...}: the first is prose, the second mathematics.
TEXT_RE = re.compile(r"\\text\{([^{}]*)\}")

# TikZ node text: "node {...}", "node[opt] {...}", "node[opt] (name) {...}",
# plus pgfplots xlabel=/ylabel=/title= values in braces.
#
# The option bracket must be consumed as a UNIT, not with a lazy [^{;]*?: a
# lazy run stops at the first "{" it can, which inside "node[lab/.style={font=
# \small}]" is the *style* group, so the gate reported "font=\small" as node
# text. Match an optional [...] (allowing one nested brace group inside it),
# then an optional (name), then the real body.
NODE_RE = re.compile(
    r"\\?node\b\s*"
    r"(?:\[(?:[^\[\]{}]|\{[^{}]*\})*\]\s*)?"
    r"(?:\([^()]*\)\s*)?"
    r"(?:at\s*\([^()]*\)\s*)?"
    r"\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}"
    r"|(?:xlabel|ylabel|zlabel|title)\s*=\s*\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")

# pgfplots' \legend{...} and \addlegendentry{...} MACROS -- the one piece of visible figure text that
# no gate in this project could see. The KEY form, "legend entries={...}", is
# covered by the sibling gates' TIKZ_TEXT_KEYS; the macro form carries no "=",
# and check_duplicated_lines below cannot help either, because a \legend is
# always INSIDE an axis environment and everything inside one is skipped by
# design. Book 4 carries 18 of them, several with real English ("disk, , no
# friction", "lost, pressure recovered", "copper, sea water"). Two levels of
# nesting are allowed: an entry may hold $\operatorname{Re}(\dots)$.
LEGEND_RE = re.compile(
    r"\\(?:legend|addlegendentry)\s*\{((?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*)\}")

# Environments whose bodies are drawing code, copied byte-identically by
# design. A "duplicated English line" inside one of these is not a defect --
# it is the applier doing exactly what it promises.
DRAW_ENV_OPEN = re.compile(
    r"\\begin\{(?:tikzpicture|axis|semilogxaxis|semilogyaxis|loglogaxis|"
    r"scope|circuitikz|groupplot|pgfonlayer)\}")
DRAW_ENV_CLOSE = re.compile(
    r"\\end\{(?:tikzpicture|axis|semilogxaxis|semilogyaxis|loglogaxis|"
    r"scope|circuitikz|groupplot|pgfonlayer)\}")
# A DISPLAYED-MATH body is copied byte-identically by design too, and the
# "$" guard below cannot see it: an align* line carries no $ delimiters at all.
# Translating the \text{} label on one line of an align* therefore made the
# NEXT line -- pure mathematics, identical by construction and enforced as such
# by id_apply's math census -- report as a duplicated English line. Found on the
# Spanish Book 4 edition (11-maxwell-equations), where every edition that
# translates that label would have seen it.
MATH_ENV_OPEN = re.compile(
    r"\\begin\{(?:align|alignat|equation|gather|multline|eqnarray|split|aligned|gathered|cases|array|[pbvVB]matrix|smallmatrix|dmath)\*?\}|\\\[")
MATH_ENV_CLOSE = re.compile(
    r"\\end\{(?:align|alignat|equation|gather|multline|eqnarray|split|aligned|gathered|cases|array|[pbvVB]matrix|smallmatrix|dmath)\*?\}|\\\]")

# A continuation line of drawing code carries no leading macro to key on:
# "xmin=0, xmax=4.3, ymin=0, ymax=21, xtick={0,1,2,3,4},". Key on the shape.
DRAW_OPTION_LINE = re.compile(
    r"^[^a-zA-Z]*(?:[a-z][a-z ]*\s*=\s*[^=]*,?\s*)+$|^[-\d.,()\s{}\[\]+*/]+;?$")

LOWER_WORD = re.compile(r"(?<![A-Za-z])[a-z]{3,}(?![A-Za-z])")

# Strings a Latin-script edition legitimately leaves byte-identical.
ALLOWED_IDENTICAL = {
    # brand, markup and file names
    "one", "course", "com", "www", "http", "https", "tex", "latex", "pdf",
    "github", "book", "md",
    # internationalisms and symbols that are the same word in the targets
    "min", "max", "log", "exp", "sin", "cos", "tan", "arg", "det", "lim",
    "sup", "inf", "abs", "mod", "rad", "deg", "cte", "const",
    "in", "out", "on", "off", "up", "down",          # circuit port labels
    "gaz", "gas", "air", "ion", "bar", "net", "cm", "mm", "km", "kg",
    "obscura", "camera",                              # camera obscura
    "et", "al",                                       # et al.
    # Spectroscopy series labels. "Lyman (ultraviolet)" and "Balmer
    # (visible)" are byte-identical in French, Spanish, Portuguese and Dutch
    # because BOTH words are the same in all of them -- the parenthesis is
    # not untranslated English. Verified in the fr and es Book 3 editions.
    "ultraviolet", "visible", "infrarood", "infrarouge",
    # Same word in Dutch as in English, verified in the nl Book 3 edition:
    # a guitar "fret" and a "pseudo-integrator" op-amp stage.
    "fret", "pseudo", "integrator",
    # Conventional subscript abbreviations. These are the SAME abbreviation in
    # French, Spanish, Portuguese, Dutch and Indonesian (ext = extérieur /
    # exterior / externo / extern; tot = total; cons = conservatives /
    # conservativas), so an identical \text{ext} is correct, not untranslated.
    # Verified against the shipped Book 2 editions before being listed.
    "ext", "int", "tot", "cons", "max", "min", "eff", "abs", "rel", "gen",
    "th", "eq", "crit", "ref", "res", "init", "fin", "moy", "med", "num",
    "den", "obs", "src", "det", "acc", "rms", "emf", "dc", "ac", "pp",
    # ---- biology -----------------------------------------------------------
    # Latin binomials are international scientific nomenclature: "Homo
    # sapiens" is written exactly so in French, Dutch, Spanish, Portuguese and
    # Indonesian, and leaving it byte-identical is CORRECT, not untranslated.
    # A binomial is two words, so without this it lands in the gate's
    # high-confidence multi-word tier and fires on every Latin edition at
    # once. Only the species epithet needs listing: the genus is capitalised
    # and the gate counts lowercase words. These are the epithets the canon
    # actually uses -- grep the English bodies again if a later book adds
    # species, rather than opening the rule to any "Capitalised lowercase"
    # pair, which would swallow "Simple sugars" and "Natural selection".
    "sapiens", "habilis", "erectus", "afarensis", "coli", "aureus",
    "victoria",
    # Book 3 (University Year 1) adds these five: Paris japonica,
    # Paramecium aurelia, Quercus robur, Felis catus, Canis lupus.
    # "lupus" was first added per-language by the Indonesian agent, which
    # noted in its own comment that it belonged here instead -- correctly: a
    # binomial epithet is identical in EVERY Latin-script target, which is the
    # criterion for this global set. Moved. Its three companions (domain,
    # genus, monomer) stay per-language, because French says domaine, genre
    # and monomere.
    "japonica", "aurelia", "robur", "catus", "lupus",
}

# A fragment of a single word is reported in a SEPARATE, lower-confidence
# class. In the Latin-script targets a one-word fragment is very often a true
# cognate -- French "distance", "signal", "amplitude", "absorption", "visible"
# and Spanish "amplitud"-class words are correct prose, and firing on them
# would make the gate useless. A multi-word fragment left byte-identical is
# the high-confidence defect: no two languages agree on a whole phrase by
# accident. Both tiers are reported; only the multi-word tier is worth
# blocking on.
def _word_count(s):
    s = re.sub(r"\$[^$]*\$", " ", s)
    # A graphics path is never prose, in any language. The overlay-label
    # figures put \includegraphics INSIDE a tikz node, so the node-text
    # extractor hands the whole include to this gate -- and it is
    # byte-identical between English and every translation BY DESIGN. Left in,
    # "images/book1/ai/fig-frog-cycle.png" counts as several words and the
    # fragment lands in the high-confidence multi-word tier, firing on every
    # Latin edition for every annotated figure in the book.
    s = re.sub(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}", " ", s)
    s = re.sub(r"\\omimg\s*\{[^{}]*\}", " ", s)
    s = re.sub(r"\\(?:qty|unit|num|SI|si)\s*(?:\{[^{}]*\})?\{[^{}]*\}", " ", s)
    # A label argument is not prose: "def:b1:kinetic-theory:temperature" would
    # otherwise count as four words and make a bare \omterm line look like a
    # duplicated English sentence. It fired on three shipped editions at once.
    s = re.sub(r"\{[^{}]*:[^{}]*\}", " ", s)
    s = re.sub(r"\\[A-Za-z@]+", " ", s)
    # A HYPHENATED COMPOUND IS ONE WORD, not two. Counting the parts put the
    # international loanword "Crossing-over" -- correct, unchanged prose in
    # Dutch, French, Spanish and Portuguese -- into the blocking multi-word
    # tier, and a legitimate environment title FAILED a whole year until it
    # was retitled to satisfy the gate. That is the gate driving the
    # translation, which is backwards. A single lexical item, hyphens and
    # elision apostrophes included, is exactly the true-cognate case the
    # one-word tier exists for. Found by the Dutch Book 2 agent, 2026-09-05.
    return len(re.findall(r"[A-Za-z]{2,}(?:[-'\u2019][A-Za-z]{2,})*", s))


def _fragments(text):
    """[(class, string, char-offset)] for every comparable fragment."""
    out = []
    for m in TITLE_RE.finditer(text):
        out.append(("title",
                    m.group(1) if m.group(1) is not None else m.group(2),
                    m.start()))
    for m in TEXT_RE.finditer(text):
        out.append(("text", m.group(1), m.start()))
    for m in NODE_RE.finditer(text):
        out.append(("node",
                    m.group(1) if m.group(1) is not None else m.group(2),
                    m.start()))
    for m in LEGEND_RE.finditer(text):
        out.append(("legend", m.group(1), m.start()))
    return out


# Per-LANGUAGE allow-lists. The global set above is for words identical in
# EVERY target; these are for words identical in ONE of them, which a global
# entry would blind the other six to. Amino-acid names are the clearest case:
# Dutch and French keep the English -ine forms (alanine, glycine), but Spanish
# and Portuguese say alanina and glicina, so listing them globally would hide a
# genuine Spanish defect.
#
# EVERY entry here is evidence: it comes from an agent reporting that the gate
# made it reword CORRECT prose. That report is a gate bug, not a workaround --
# a gate that drives the translation is worse than no gate (the Book 2 Dutch
# `Crossing-over` incident). Add to this list rather than letting the next
# agent reword around it, and say which edition supplied the evidence.
ALLOWED_BY_LANG = {
    # Reported by the Dutch Book 3 agent, 2026-09-06: 11 multi-word fragments
    # failed the BLOCKING tier although every one is correct Dutch.
    "nl": {
        # Latin anatomical nomenclature, unchanged in Dutch.
        "muscularis", "mucosae", "propria", "lamina", "serosa", "submucosa",
        # Amino acids and sugars keep the English -ine/-ose form in Dutch.
        "alanine", "serine", "glycine", "valine", "leucine", "proline",
        "lysine", "cysteine", "histidine", "arginine", "glutamine",
        "asparagine", "threonine", "methionine", "tyrosine", "fructose",
        "glucose", "sucrose", "lactose", "ribose", "gyrase",
        # Second round, reported by the same agent after the first fix: four
        # fragments still blocked, each for ONE word, each in a family already
        # here. -ose sugars beside ribose/glucose/lactose; an -ase enzyme
        # beside gyrase; and "carrier", which is the loanword Dutch membrane
        # physiology actually uses -- this edition's term config deliberately
        # keeps "carrier" (the transporter) linked and distinct from "drager"
        # (the NAD carrier). Adding them cleared gate 9 with NO change to the
        # text, which is the whole point.
        "galactose", "deoxyribose", "hexokinase", "carrier",
        # "per" is an ordinary Dutch preposition (4 H+ per ATP).
        "per",
    },
    # French keeps the same -ine forms; accented ones (sérine) differ and are
    # deliberately absent, because there the identical spelling WOULD be a
    # defect.
    "fr": {"muscularis", "mucosae", "propria", "lamina", "alanine", "glycine",
           "valine", "leucine", "proline", "lysine", "arginine", "glutamine",
           "asparagine", "gyrase", "fructose", "glucose", "lactose", "ribose"},
    # Indonesian absorbs Latin anatomical nomenclature verbatim.
    "id": {"muscularis", "mucosae", "propria", "lamina", "serosa", "submucosa",
           # Reported by the Indonesian Book 3 agent, 2026-09-06: three
           # multi-word fragments blocked although each is correct Indonesian.
           # "domain" and "genus" are the Indonesian rank names themselves
           # (the figure translates the ranks around them: filum, kelas, ordo,
           # famili), and "monomer" is the Indonesian word for a monomer. The
           # fourth fragment the agent found, "kingdom Animalia", WAS a real
           # defect and was translated to "kerajaan Animalia" instead of being
           # exempted here.
           "domain", "genus", "monomer",
           },
}


def _allowed(lang):
    return ALLOWED_IDENTICAL | ALLOWED_BY_LANG.get(lang or "", set())


def _lang_of(path):
    """parts/<year>[/solutions]/<lang>/NN-slug.tex -> <lang>."""
    m = re.search(r"/([a-z]{2})/[^/]*$", str(path).replace("\\", "/"))
    return m.group(1) if m else None


def _has_lowercase_word(s, lang=None):
    """A lowercase word that is not an allowed internationalism."""
    # Strip math and macros first: [$\arcsin$] and [Gram--Schmidt] must not fire.
    s = re.sub(r"\$[^$]*\$", " ", s)
    # A graphics path is not prose, and it is byte-identical to English BY
    # DESIGN -- id_apply's `img` census requires exactly that. The overlay-label
    # figures put \includegraphics inside a tikz node, so the node-text
    # extractor hands the whole include to this gate; without stripping it here
    # too, "images/book1/ai/fig-frog-cycle.png" supplies the lowercase word that
    # makes the fragment a finding at all. _word_count() already strips it, but
    # that only chooses the TIER -- this is what decides whether it is reported.
    # Found by the French Book 1 agent, 2026-09-04: 17 hits in 14 files, and a
    # FAILED check_translation.sh with nothing wrong in the text.
    s = re.sub(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}", " ", s)
    s = re.sub(r"\\omimg\s*\{[^{}]*\}", " ", s)
    s = re.sub(r"\\[A-Za-z@]+", " ", s)
    return any(w not in _allowed(lang) for w in LOWER_WORD.findall(s))


CAP_WORD = re.compile(r"(?<![A-Za-z])[A-Z][a-z]{2,}(?![a-z])")


def _capitalised_only(s):
    """Capitalised word(s) and no lowercase word at all.

    _has_lowercase_word() decides whether a fragment is reported AT ALL, so a
    fragment made only of capitalised words was invisible in BOTH tiers. The
    English canon of Biology Book 3 has 42 \begin{proof}[Evidence] titles and
    ~30 one-word capitalised definition titles; every one of them could ship
    untranslated behind a green gate. The Spanish Book 3 agent found its 42 by
    writing an independent title census after this gate stayed silent, which is
    the gate failing at its one job.

    Reported in the LOW-CONFIDENCE tier only, never blocking: a capitalised
    one-word title is very often a true cognate (Mitosis, Virus, Turgor,
    Plasmid) or a proper noun (Michaelis--Menten, Hardy--Weinberg), and a gate
    that blocks on those would drive the translation instead of checking it --
    exactly the failure the hyphenated-compound bug caused on Book 2.
    """
    s = re.sub(r"\$[^$]*\$", " ", s)
    s = re.sub(r"\\includegraphics\s*(?:\[[^\]]*\])?\s*\{[^{}]*\}", " ", s)
    s = re.sub(r"\\omimg\s*\{[^{}]*\}", " ", s)
    s = re.sub(r"\\[A-Za-z@]+", " ", s)
    return bool(CAP_WORD.search(s)) and not LOWER_WORD.search(s)


def _line_of(text, offset):
    return text.count("\n", 0, offset) + 1


def check_duplicated_lines(path, body, en_body, findings, lang=None):
    """An English line kept AND translated: the twin's line sits verbatim in
    the translation, adjacent to a line that is not in the twin at all."""
    en_lines = {ln.strip() for ln in en_body.split("\n") if len(ln.strip()) > 40}
    lines = body.split("\n")
    depth = 0
    for i, ln in enumerate(lines):
        s = ln.strip()
        # Track drawing AND displayed-math environments: everything inside one
        # is copied byte-identically on purpose, so a "duplicate" there means
        # nothing.
        opens = len(DRAW_ENV_OPEN.findall(ln)) + len(MATH_ENV_OPEN.findall(ln))
        closes = len(DRAW_ENV_CLOSE.findall(ln)) + len(MATH_ENV_CLOSE.findall(ln))
        was_inside = depth > 0
        depth = max(0, depth + opens - closes)
        if was_inside or opens:
            continue
        if len(s) <= 40 or s not in en_lines:
            continue
        if not _has_lowercase_word(s, lang) or _word_count(s) < 4:
            continue
        # Prose only: drawing code and math are copied verbatim by design.
        if re.search(r"\\(?:draw|fill|path|node|addplot|foreach|coordinate|"
                     r"begin|end|label|cref|ref|index|input|item|omterm)\b", s) or "$" in s:
            continue
        if DRAW_OPTION_LINE.match(s):
            continue
        neighbours = [lines[j].strip() for j in (i - 1, i + 1)
                      if 0 <= j < len(lines)]
        if any(n and len(n) > 40 and n not in en_lines for n in neighbours):
            findings.append((str(path), i + 1, "dup",
                             "English line kept beside its translation: "
                             f"{s[:70]!r}"))


def check_file(path, findings):
    twin = pathlib.Path(re.sub(r"/[a-z]{2}/(?=[^/]*$)", "/", str(path)))
    if not twin.is_file() or twin == path:
        return
    lang = _lang_of(path)
    body = strip_comments(path.read_text(encoding="utf-8"))
    en_body = strip_comments(twin.read_text(encoding="utf-8"))

    mine, theirs = _fragments(body), _fragments(en_body)
    by_class = {}
    for cls, s, off in mine:
        by_class.setdefault(cls, []).append((s, off))
    en_by_class = {}
    for cls, s, off in theirs:
        en_by_class.setdefault(cls, []).append((s, off))

    for cls, items in by_class.items():
        en_items = en_by_class.get(cls, [])
        if len(items) != len(en_items):
            # A structural divergence; check_translation.sh owns it.
            continue
        for (s, off), (e, _) in zip(items, en_items):
            if s.strip() != e.strip():
                continue
            if _has_lowercase_word(s, lang):
                tier = cls if _word_count(s) >= 2 else cls + "-1word"
            elif _capitalised_only(s):
                # No lowercase word: always the low-confidence tier. See
                # _capitalised_only() -- without this branch the fragment was
                # reported in NEITHER tier.
                tier = cls + "-1word"
            else:
                continue
            findings.append((str(path), _line_of(body, off), tier,
                             f"identical to English ({cls}): {s.strip()[:70]!r}"))

    check_duplicated_lines(path, body, en_body, findings, lang)


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--quiet", action="store_true")
    ap.add_argument("--max-detail", type=int, default=8)
    args = ap.parse_args()

    findings, files = [], 0
    for d in args.dirs:
        p = pathlib.Path(d)
        if not p.is_dir():
            continue
        for f in sorted(p.glob("*.tex")):
            files += 1
            check_file(f, findings)

    if not findings:
        print(f"  latin prose gate: OK ({files} files)")
        return 0

    by_class = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))
    print(f"  latin prose gate: {len(findings)} issue(s) in {files} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        print(f"    {cls:<8} {len(hits):>5} hit(s) in "
              f"{len({h[0] for h in hits})} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")

    # Exit non-zero ONLY for the multi-word tiers. The module docstring has
    # always said "both tiers are reported; only the multi-word tier is worth
    # blocking on", but main() returned 1 for any finding at all -- so gate 9
    # in check_translation.sh failed on the one-word tier, which in these
    # editions is overwhelmingly TRUE COGNATES (French "distance", "signal",
    # "amplitude"; Dutch "fret"). A gate that fires on correct prose gets
    # ignored, which is worse than not having it. The one-word hits are still
    # printed, because they are worth a human's eye; they are just not a
    # failure. Reported by the French Book 1 agent, 2026-09-04.
    blocking = sum(len(h) for c, h in by_class.items() if not c.endswith("-1word"))
    if blocking:
        return 1
    print("  latin prose gate: no multi-word findings "
          "(the one-word tier above is advisory -- read it, it is usually cognates)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
