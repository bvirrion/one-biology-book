#!/usr/bin/env python3
"""Arabic-specific hygiene gate for a translated tree.

check_translation.sh proves *structure*: same files, same labels, same
environment census. Its two prose gates are Latin-oriented and score nothing
on Arabic -- gate 6 looks for TeX accent escapes (\\'e), which Arabic never
writes, and the drafty-"..." gate is script-agnostic. So an Arabic tree can be
structurally perfect and still be raw machine translation.

The LaTeX reduction below is shared with tools/check_hindi_prose.py: it drops
technical macro arguments, keeps \\text{...} inside math, pulls the visible
strings out of tikz/pgfplots/circuitikz drawing code, and reports MT spacing
damage inside inline math. Only the language-specific classes differ.

Failure classes this script detects:

  1. residual English in visible text -- \\text{ metres}, TikZ nodes still
     reading {time (s)}, English chapter titles, English \\index keys.
  2. transliterated English function words written in Arabic letters.
  3. Latin , ; ? closing an Arabic clause, where Arabic writes ، ؛ ؟.
     (The full stop is NOT in this class: Modern Standard Arabic ends a
     sentence with the ordinary Latin '.', unlike Hindi's danda.)
  4. Arabic-Indic digits ٠-٩ in the sources. This edition writes ASCII
     digits so that a number in a sentence matches the same number in the
     mathematics beside it -- see arabic_style_card.md.
  5. MT-injected spaces inside inline math -- "$P $ و $ Q $".
  6. bidi control characters (LRM/RLM/LRE..PDI). Machine translation emits
     these constantly; they are invisible on the page, survive every other
     gate, and corrupt the term linker's word boundaries.
  7. Arabic presentation forms (U+FB50-FDFF, U+FE70-FEFF). Copy-paste from
     some sources yields pre-shaped glyphs instead of the standard block;
     they render acceptably and then break search, the index and \\omterm
     matching.
  8. tatweel (U+0640) used as padding.
  9. a thin space splitting a number away from its noun.

Usage:
    python3 tools/check_arabic_prose.py parts/grade-3/ar parts/grade-3/solutions/ar
    python3 tools/check_arabic_prose.py --quiet <dir> ...

Exit status is 1 if anything was flagged. Called by check_translation.sh for
lang == ar; safe to run by hand on a single directory while translating.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

# Letters only: the Arabic block also holds ، ؛ ؟ and the Arabic-Indic digits,
# which must not count as "an Arabic letter" in the punctuation rule below.
ARABIC_LETTER = r"ؠ-يٮ-ۓۺ-ۿ"
ARABIC_MARK = r"ً-ٰٟۖ-ۭ"
ARABIC = ARABIC_LETTER + ARABIC_MARK
AR_CHAR = re.compile(f"[{ARABIC_LETTER}]")

ALLOWED_WORDS = {
    "one", "course", "com", "www", "http", "https",
    "tex", "latex", "pdf", "html",
    "si", "iso", "atp", "dna", "rna", "led", "usb", "gps", "ph",
    # Latin binomials. Scientific nomenclature is international: a Devanagari
    # or Arabic biology text writes "Homo sapiens" in Latin script exactly as
    # every other edition does, so these are correct visible Latin, not
    # residual English. Listed word by word (the gate tokenises), and only the
    # ones the canon actually uses -- grep the English bodies again if a later
    # book adds species.
    "homo", "sapiens", "habilis", "erectus", "australopithecus", "afarensis",
    "escherichia", "coli", "staphylococcus", "aureus", "aequorea", "victoria",
    # Biology Book 3's own binomials and higher taxa, grepped from the
    # English bodies as the note above instructs. A Linnaean name is Latin
    # in every script -- an Arabic biology textbook italicises
    # \emph{Quercus robur} exactly as an English one does -- and the
    # domain and supergroup names of a classification chapter are the same
    # kind of thing. Added by the Arabic Biology Book 3 agent, 2026-09-06.
    "quercus", "robur", "felis", "catus", "canis", "lupus", "familiaris",
    "paramecium", "aurelia", "caudatum", "bursaria", "trypanosoma", "euglena",
    "mytilus", "pisaster", "rhizobium", "dryas", "paris", "japonica",
    "bacteria", "archaea", "eukarya", "amoebozoa", "excavata",
    "archaeplastida", "opisthokonta", "sar",
    # The Linnaean higher taxa the classification chapter prints as formal
    # names -- "kingdom Animalia", "family Felidae". A formal taxon name is
    # Latin in every language and is italicised or capitalised exactly as
    # here in the French, Dutch, Spanish and Portuguese twins; only the RANK
    # word beside it ("kingdom", "family") is translated, and this edition
    # translates it. Added by the Arabic Biology Book 3 agent, 2026-09-06.
    "animalia", "chordata", "mammalia", "carnivora", "felidae", "canidae",
    "reptilia", "aves",
    # "Alu" is the name of a repeated element (after the AluI enzyme that
    # cuts it), not an English word; it keeps its published capitalisation
    # in every language, like a gene symbol.
    "alu",
    # Bacterial gene symbols and reagent/protein acronyms of the
    # gene-regulation chapter. A gene symbol is an international identifier,
    # not an English word: the French, Dutch, Spanish and Portuguese twins of
    # parts/bachelor-1/20-expression-control.tex all print \emph{lacZ},
    # \emph{lacY}, \emph{lacA} and \emph{lacI} verbatim, exactly as the
    # English canon does, and so does the figure that labels the operon map.
    # "X-gal" is the trade name of a chromogenic substrate and "PaJaMo" the
    # published name of the Pardee--Jacob--Monod experiment; both are kept in
    # Latin by every other edition. Added by the Arabic Biology Book 3 agent,
    # 2026-09-06.
    "lacz", "lacy", "laca", "laci", "x-gal", "pajamo",
}

# Image attribution that EVERY edition must keep verbatim: a CC licence
# identifier is the licence's NAME, and the repository holding a photograph is
# an institution's. The French, Dutch, Hindi and Indonesian editions all keep
# "Wellcome Collection" and "Wikimedia Commons" in Latin, and so does this
# edition's own frontmatter/image-credits.ar.tex -- but the gate rejected
# "Wellcome" and "Collection" in a chapter, so the Arabic agent transliterated
# them there and the book ended up carrying TWO spellings of one institution.
# Blanked here, the way the Indonesian gate does it, so the surrounding Arabic
# stays fully gated. Note the DESCRIPTION is not exempt: "Oil painting" is
# ordinary prose and Arabic rightly writes تصوير زيتي.
# Reported by the Arabic Book 1 agent, 2026-09-04.
ATTRIBUTION = re.compile(
    r"Wikimedia\s+Commons|Wellcome\s+Collection|Creative\s+Commons"
    r"|\bCC[~\s]?(?:BY(?:[~\s-](?:SA|NC|ND))*(?:[~\s]?\d+(?:\.\d+)?)?|0)")


# pgfmath function names. These appear inside tikz/pgfplots COORDINATE groups
# -- \node[...] at ({cos(72)},{sin(72)}) -- which the node-text regex captures
# along with real node text. Listing them here rather than tightening the regex
# is deliberate: a tighter pattern that skipped a group after "(" also stopped
# matching the genuine node text later on the same line, trading a false
# positive for a false negative, which is the worse failure for this gate.
PGFMATH_FUNCTIONS = {
    "cos", "sin", "tan", "acos", "asin", "atan", "atan2", "cot", "sec", "csc",
    "sqrt", "exp", "ln", "log10", "log2", "abs", "mod", "div", "floor", "ceil",
    "round", "int", "frac", "pow", "rnd", "rand", "random", "deg", "rad",
    "veclen", "max", "min", "sign", "factorial", "pi", "width", "height",
    "depth", "scalar", "true", "false",
}

# Unit and symbol strings that may appear bare in a table cell or node.
ALLOWED_UNITS = {
    "m", "s", "kg", "g", "mg", "km", "cm", "mm", "nm", "um",
    "dm", "dam", "hm",
    "n", "j", "w", "hz", "pa", "mol", "cd", "k", "a", "v", "c", "t",
    "wb", "f", "ev", "min", "h", "l", "ml", "rad", "sr", "bq", "gy", "sv",
    "kwh", "kj", "mj", "gpa", "mpa", "kpa", "khz", "mhz", "ghz",
    # Units that Biology Book 3 prints bare inside a tikz node, where
    # \unit{} is not available: an energy budget labelled
    # "\num{8800} kcal\,m$^{-2}$\,yr$^{-1}$". A unit symbol is the same in
    # every language. Added by the Arabic Biology Book 3 agent, 2026-09-06.
    "cal", "kcal", "yr", "ha",
}

LATIN_WORD = re.compile(r"[A-Za-z][A-Za-z'\-]{1,}")

# Short English that the >=3-letter rule below cannot see. A blanket lower
# threshold is not an option: one- and two-letter Latin tokens are usually
# legitimate symbols (x_{\text{m}}, R_{\text{s}}, the dioptre \text{D}), so
# only a named list is safe. The Physics 2 agent found 19 of these hiding
# under the threshold after the 100 visible ones were fixed.
SHORT_ENGLISH = {
    "so", "in", "of", "to", "is", "at", "by", "an", "or", "if", "no",
    "we", "it", "as", "be", "do", "on", "up", "and", "the", "for",
    "ie", "eg", "cf", "vs", "eq", "nc", "wrt", "resp",
}
# "th" is deliberately absent: it collides with the element symbol Th
# (thorium) and with coin-outcome labels like TH. Matched lowercase-only for
# the same reason -- capitalised short tokens are symbols, not words.

# "i.e." / "e.g." never match LATIN_WORD: the dot splits them into single
# letters, which are skipped as symbols.
DOTTED_ABBREV = re.compile(r"\b(?:i\.e\.|e\.g\.|etc\.|cf\.|viz\.)")

# ---------------------------------------------------------------------------
# Macros whose arguments are technical and must not be read as prose.
# ---------------------------------------------------------------------------
# name -> number of braced arguments to drop wholesale.
TECHNICAL_MACROS = {
    "label": 1, "ref": 1, "cref": 1, "Cref": 1, "crefrange": 2,
    "Crefrange": 2, "eqref": 1, "pageref": 1, "nameref": 1, "autoref": 1,
    "input": 1, "include": 1, "includegraphics": 1, "usepackage": 1,
    "documentclass": 1, "bibliography": 1, "bibliographystyle": 1,
    "ominput": 2, "ominputsol": 2, "omsollink": 1,
    "qty": 2, "unit": 1, "num": 1, "ang": 1, "SI": 2, "si": 1,
    # 2026-09-06, biology Book 3 `ar`: the siunitx FAMILY, not just \qty.
    # \qtylist{1;2;5;10;20}{mmol/L} left "mmol" in visible text and was
    # reported as residual English -- a defect no translator can remove,
    # because the unit argument is mathematics in every language. This gate
    # is an independent COPY of check_hindi_prose.py's reduction rather than
    # an import, so the identical fix made there the same day did not reach
    # it; ported verbatim. The whole family takes fixed argument counts:
    # qtyrange/SIrange 3, qtylist/numrange 2, numlist 1.
    "qtyrange": 3, "qtylist": 2, "numlist": 1, "numrange": 2,
    "SIrange": 3, "SIlist": 2, "unitlist": 1,
    "newcommand": 2, "renewcommand": 2, "providecommand": 2,
    "color": 1, "textcolor": 1, "definecolor": 3, "pgfplotsset": 1,
    "hypersetup": 1, "setlength": 2, "addtolength": 2, "url": 1,
}

# \omterm{def:label}{visible display} -- first arg technical, second is prose.
# \href{url}{text} likewise.
SPLIT_MACROS = {"omterm": (1, 1), "href": (1, 1), "hyperref": (1, 1)}

# Environments whose optional argument is a visible title (so it IS prose).
TITLED_ENVS = {
    "definition", "theorem", "proposition", "lemma", "corollary", "example",
    "remark", "method", "notation", "exercise", "problem", "proof",
    "omfigure", "figure", "table", "solution",
}

# Environments whose body is drawing code, not prose. Node text and axis
# labels are pulled out of them separately.
DRAWING_ENVS = {"tikzpicture", "axis", "semilogxaxis", "semilogyaxis",
                "loglogaxis", "groupplot", "scope", "circuitikz"}

MATH_ENVS = {"equation", "equation*", "align", "align*", "gather", "gather*",
             "multline", "multline*", "eqnarray", "eqnarray*", "array",
             "cases", "split", "aligned", "gathered", "pmatrix", "bmatrix",
             "vmatrix", "matrix", "smallmatrix"}

MATH_PLACEHOLDER = "\x00"

# A chemical formula's letters: two or more element symbols run together, each
# a capital optionally followed by one lower-case letter (MgF, NaCl, GaAs, AsH).
# Mixed case means the acronym rule above cannot catch them, and they are not
# English in any script -- without this the Book 4 Hindi agent had to write
# "Mg{}F" with an empty group to silence the gate, which is a source wart of
# exactly the kind this project refuses elsewhere.
CHEM_FORMULA = re.compile(r"(?:[A-Z][a-z]?){2,}")

# The same thing written as a STRUCTURAL formula: element symbols joined by
# bond dashes. "O--H" and "S--S" already pass (the hyphen-splitting rule
# below sees two one-letter parts), but a chain of three or more --
# "H--O--H", the bond angle of the water molecule, and "C--C--C" -- reaches
# no rule and was reported as residual English. It is a formula in every
# language and every script; rewording the Arabic around it would be the
# gate driving the translation. Each link is a capital plus at most one
# lower-case letter, so no English word and no surname pair (Michaelis--
# Menten) can match. Added by the Arabic Biology Book 3 agent, 2026-09-06.
CHEM_CHAIN = re.compile(r"(?:[A-Z][a-z]?)(?:-{1,2}(?:[A-Z][a-z]?))+")


# Environments taking a column specification ({c|ccc}) before their body.
COLSPEC_ENVS = {"tabular", "tabular*", "tabularx", "array", "longtable"}

# Text-bearing keys inside a drawing environment.
TIKZ_TEXT_KEYS = re.compile(
    r"\b(?:xlabel|ylabel|zlabel|title|legend\s+entries|label)\s*=\s*"
    r"(\{[^{}]*\}|[^,\]\n]+)"
)
# A node's braced group is its visible label -- but "node" also occurs inside
# pgfplots STYLE KEYS, as in "every node near coord/.append style={font=\small}",
# where the following group is formatting, not text. Exclude a "node" preceded
# by "every", or with a "/." key path before its group.
TIKZ_NODE = re.compile(
    r"(?<!every\s)\bnode\b(?![^{;]*/\.)[^{;]*?(\{(?:[^{}]|\{[^{}]*\})*\})"
)

# pgfplots' \legend{...} and \addlegendentry{...} MACROS. The key form, "legend entries={...}", is
# matched by TIKZ_TEXT_KEYS above; the macro form has no "=" and was therefore
# invisible to every prose gate in the project. Book 4 carries 18 of them and
# the SHIPPED Hindi and Arabic Book 2 editions each ship six untranslated
# English legends ("without friction, with friction", "undamped, damped", ...)
# behind a green gate run. Two levels of nesting are allowed: a legend entry
# may hold $\operatorname{Re}(...)$.
TIKZ_LEGEND = re.compile(
    r"\\(?:legend|addlegendentry)\s*(\{(?:[^{}]|\{(?:[^{}]|\{[^{}]*\})*\})*\})"
)


def strip_comments(text: str) -> str:
    out = []
    for line in text.split("\n"):
        i, esc = 0, False
        cut = len(line)
        while i < len(line):
            ch = line[i]
            if esc:
                esc = False
            elif ch == "\\":
                esc = True
            elif ch == "%":
                cut = i
                break
            i += 1
        out.append(line[:cut])
    return "\n".join(out)


def match_group(text: str, start: int, open_ch: str, close_ch: str):
    """Return (inner, end_index) for a balanced group starting at text[start]."""
    if start >= len(text) or text[start] != open_ch:
        return None, start
    depth, i, esc = 0, start, False
    while i < len(text):
        ch = text[i]
        if esc:
            esc = False
        elif ch == "\\":
            esc = True
        elif ch == open_ch:
            depth += 1
        elif ch == close_ch:
            depth -= 1
            if depth == 0:
                return text[start + 1:i], i + 1
        i += 1
    return None, start


# Text-mode macros used INSIDE math. Their argument is prose a reader sees, so
# it must be Hindi -- "$x \text{ metres}$" is as much residual English as a bare
# sentence. Blanking math wholesale hid 19 of these across 7 files that every
# other gate called finished. \operatorname and \mathrm are deliberately absent:
# their arguments are operator names (sin, det, d) and stay Latin.
MATH_TEXT_MACRO = re.compile(
    r"\\(?:text|textrm|textbf|textit|textsf|textnormal|mbox|hbox)\s*\{")


def extract_math_text(body: str) -> str:
    """Pull \\text{...} arguments out of a math span so they get scanned."""
    out = []
    for m in MATH_TEXT_MACRO.finditer(body):
        inner, _ = match_group(body, m.end() - 1, "{", "}")
        if inner:
            out.append(inner)
    return " ".join(out)


def blank_math(text: str, findings: list, path: str) -> str:
    """Replace math spans with a placeholder, flagging MT spacing damage.

    The argument of a text-mode macro inside the span is kept: it is prose.
    """
    out, i = [], 0
    n = len(text)
    while i < n:
        ch = text[i]
        if ch == "\\" and i + 1 < n:
            nxt = text[i + 1]
            if nxt in "[(":
                closer = "\\]" if nxt == "[" else "\\)"
                j = text.find(closer, i + 2)
                j = n if j < 0 else j + 2
                out.append(MATH_PLACEHOLDER)
                out.append(" " + extract_math_text(text[i + 2:j]) + " " + MATH_PLACEHOLDER)
                i = j
                continue
            out.append(text[i:i + 2])
            i += 2
            continue
        if ch == "$":
            dollars = 2 if text.startswith("$$", i) else 1
            delim = "$" * dollars
            j = i + dollars
            while j < n:
                if text[j] == "\\":
                    j += 2
                    continue
                if text.startswith(delim, j):
                    break
                j += 1
            body = text[i + dollars:j]
            # A trailing space that terminates a control word ("$\star $") is
            # ordinary TeX and appears in the English sources too; only a
            # leading space, or a trailing one after an ordinary token, is the
            # MT fingerprint we are after ("$P $ और $ Q $").
            #
            # A trailing RELATION or BINARY OPERATOR is the same exemption and
            # was missing here as it was in check_hindi_prose.py. The canon's
            # idiom closes the math on the operator and lets the operand
            # follow outside as text or a macro -- "$\lambda_{\max}T = $ const",
            # "$\Delta^{++} = $ uuu". Six such spans exist in the Book 5
            # ENGLISH source, so the rule fired on prose no translator may
            # touch: id_apply's math census requires the span byte-identical
            # to English, and this gate demanded it change. Predicted from the
            # Hindi fix and confirmed by the Arabic Book 5 agent, 2026-09-03,
            # which had worked around it by post-editing an empty group
            # ("= {}$") into six spans.
            #
            # It cannot mask the fingerprint it exists to catch: MT spacing
            # damage leaves the space after an ordinary TOKEN ("$P $"), never
            # after a dangling relation.
            bad_lead = bool(body) and body[0] == " "
            bad_trail = (bool(body) and body[-1] == " "
                         and not re.search(r"\\[A-Za-z]+\s*$", body)
                         and not re.search(r"[=+\-<>*/~]\s*$", body))
            if dollars == 1 and (bad_lead or bad_trail):
                findings.append(
                    (path, line_of(text, i), "math-space",
                     f"MT space inside inline math: ${body[:40]}$"))
            out.append(MATH_PLACEHOLDER)
            out.append(" " + extract_math_text(body) + " " + MATH_PLACEHOLDER)
            i = min(j + dollars, n)
            continue
        out.append(ch)
        i += 1
    return "".join(out)


def line_of(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


MAX_NESTING = 4


def nested_text(fragment: str, depth: int) -> str:
    """Reduce a fragment that is itself LaTeX.

    A node label, an environment's optional title and an \\omterm display are
    all markup, not plain strings: "{size (\\unit{m})}" must not report *unit*
    as residual English, and a generated \\omterm inside a weekend-problem
    title must not leak its label into the prose stream. Findings are
    discarded here -- the caller's own scan of the reduced text reports them,
    with the line numbers of the enclosing file.
    """
    if depth >= MAX_NESTING or not fragment or "\\" not in fragment:
        return fragment
    return visible_text(fragment, [], "<nested>", depth + 1)


def _unwrap_braces(s: str) -> str:
    """Strip ONE outer brace pair, and only when it is genuinely balanced.

    `s.strip("{}")` is wrong and cost two editions a workaround in their
    SOURCES: a node whose whole body is one macro, `node {\\qty{1}{atm}}`, is
    captured as `\\qty{1}{atm}` and strip() eats the macro's own closing brace,
    leaving `\\qty{1}{atm` -- so the unit leaked out of the macro and was
    reported as residual English. Both the Hindi and the Arabic Book 3 agents
    hit it on the same figure and patched the .tex rather than the tool.
    """
    s = s.strip()
    while len(s) >= 2 and s[0] == "{" and s[-1] == "}":
        depth = 0
        for i, ch in enumerate(s):
            if ch == "{":
                depth += 1
            elif ch == "}":
                depth -= 1
                if depth == 0 and i != len(s) - 1:
                    return s          # the leading brace closes early: keep all
        s = s[1:-1].strip()
    return s


def extract_drawing_text(body: str, depth: int = 0) -> str:
    """Pull the visible strings out of tikz/pgfplots/circuitikz drawing code."""
    pieces = [m.group(1) for m in TIKZ_NODE.finditer(body)]
    pieces += [m.group(1) for m in TIKZ_TEXT_KEYS.finditer(body)]
    pieces += [m.group(1) for m in TIKZ_LEGEND.finditer(body)]
    return " \n ".join(nested_text(_unwrap_braces(p), depth) for p in pieces)


def visible_text(text: str, findings: list, path: str, depth: int = 0) -> str:
    """Reduce a LaTeX body to the text a reader actually sees."""
    text = blank_math(text, findings, path)
    out, i, n = [], 0, len(text)

    while i < n:
        ch = text[i]

        if ch != "\\":
            if ch in "{}":
                out.append(" ")
            else:
                out.append(ch)
            i += 1
            continue

        m = re.match(r"\\([A-Za-z@]+)\*?", text[i:])
        if not m:
            # A control SYMBOL, not a control word. The spacing ones are
            # visible white space, and dropping them silently GLUES the words
            # on either side into one token: the canon's
            # "kcal\\,m$^{-2}$\\,yr$^{-1}$" was reported as the English word
            # "kcalm", which no translator can remove without breaking the
            # unit. Emit a space for them so the tokeniser sees two words.
            # Found by the Arabic Biology Book 3 agent, 2026-09-06.
            if text[i + 1:i + 2] in {",", ";", ":", "!", " ", "/"}:
                out.append(" ")
            i += 2 if i + 1 < n else 1
            continue
        name = m.group(1)
        j = i + m.end()

        if name == "begin":
            env, j = match_group(text, skip_ws(text, j), "{", "}")
            env = (env or "").strip()
            if env in DRAWING_ENVS or env in MATH_ENVS:
                end_tag = "\\end{" + env + "}"
                k = text.find(end_tag, j)
                k = n if k < 0 else k
                if env in DRAWING_ENVS:
                    out.append(" " + extract_drawing_text(text[j:k], depth) + " ")
                else:
                    out.append(MATH_PLACEHOLDER)
                    out.append(" " + extract_math_text(text[j:k]) + " " + MATH_PLACEHOLDER)
                i = min(k + len(end_tag), n)
                continue
            j = skip_ws(text, j)
            if text[j:j + 1] == "[":
                inner, j = match_group(text, j, "[", "]")
                if env in TITLED_ENVS and inner:
                    out.append(" " + nested_text(inner, depth) + " ")
            # solution's {key} and tabular's {c|ccc} arguments are technical
            j2 = skip_ws(text, j)
            if (env == "solution" or env in COLSPEC_ENVS) and text[j2:j2 + 1] == "{":
                _, j = match_group(text, j2, "{", "}")
            i = j
            continue

        if name == "end":
            _, j = match_group(text, skip_ws(text, j), "{", "}")
            i = j
            continue

        if name in SPLIT_MACROS:
            drop, keep = SPLIT_MACROS[name]
            for _ in range(drop):
                _, j = match_group(text, skip_ws(text, j), "{", "}")
            for _ in range(keep):
                inner, j = match_group(text, skip_ws(text, j), "{", "}")
                if inner:
                    out.append(" " + nested_text(inner, depth) + " ")
            i = j
            continue

        if name in TECHNICAL_MACROS:
            j = skip_ws(text, j)
            if text[j:j + 1] == "[":
                _, j = match_group(text, j, "[", "]")
            for _ in range(TECHNICAL_MACROS[name]):
                _, j = match_group(text, skip_ws(text, j), "{", "}")
            i = j
            continue

        if name == "index":
            inner, j = match_group(text, skip_ws(text, j), "{", "}")
            if inner:
                # makeindex syntax: "sortkey@visible", and "!" separates the
                # levels of a subentry. The sort key is NEVER printed, so
                # reading it as visible text reports residual English that no
                # translator can remove: the canon's \index{pKa@p$K_a$} was
                # flagged as "pKa". It matters more than one site -- the
                # French edition of this book added 164 ASCII sort keys so
                # that makeindex would not file every accent-initial entry
                # after Z, and an Arabic edition needing the same would have
                # been flagged 164 times. Keep only what is printed, per
                # level. Fixed by the Arabic Biology Book 3 agent, 2026-09-06.
                visible = " ".join(
                    lvl.split("@", 1)[1] if "@" in lvl else lvl
                    for lvl in inner.split("!"))
                out.append(" " + nested_text(visible, depth) + " ")
            i = j
            continue

        if name == "item":
            j = skip_ws(text, j)
            if text[j:j + 1] == "[":
                _, j = match_group(text, j, "[", "]")
            out.append(" ")
            i = j
            continue

        # Any other macro: drop the control word and the bracket options it
        # may carry (those are keys, not prose), keep braced groups as text.
        j = skip_ws(text, j)
        if text[j:j + 1] == "[":
            _, j = match_group(text, j, "[", "]")
        out.append(" ")
        i = j

    return "".join(out)


def skip_ws(text: str, i: int) -> int:
    while i < len(text) and text[i] in " \t":
        i += 1
    return i


def _locate(body: str, token: str, seen_before: dict) -> int:
    """Line of `token` in the ORIGINAL file.

    Findings are detected in the reduced stream, whose line numbers do not
    survive the reduction: a multi-line math span collapses to one placeholder
    character, so every later line number drifts. Map back by finding the
    n-th occurrence of the token in the source, n being how many times this
    token has already been reported for this file.
    """
    n = seen_before.get(token, 0)
    seen_before[token] = n + 1
    start = 0
    for _ in range(n + 1):
        idx = body.find(token, start)
        if idx < 0:
            break
        start = idx + 1
    else:
        return body.count("\n", 0, idx) + 1
    return body.count("\n", 0, max(idx, 0)) + 1 if idx >= 0 else 1


# Transliterated English function words, written in Arabic letters.
#
# This list is deliberately short. Arabic is full of short particles that a
# naive list would collide with, and a gate that cries wolf gets switched off:
#   "ذا"  is Arabic (demonstrative, and ذو/ذا "possessor of"), not *the*;
#   "إن"  is Arabic (that / indeed) and one of the commonest words in the book;
#   "فور" is Arabic ("immediately upon"), not *four*;
#   "ذي"  is Arabic (genitive of ذو).
# Only tokens with no Arabic reading at all are listed, the same principle
# that keeps "इन" out of the Hindi gate.
TRANSLITERATED_ARTICLES = {
    "أوف": "of", "إند": "and", "آند": "and", "أند": "and",
    "إز": "is", "ويذ": "with", "ويز": "with", "أور": "or",
}

# Invisible bidi controls. LRM/RLM, the deprecated embedding/override set, and
# the isolates. babel's bidi=basic resolves direction from the characters
# themselves, so none of these is ever needed in a source file.
BIDI_CONTROLS = {
    "‎": "LRM", "‏": "RLM",
    "‪": "LRE", "‫": "RLE", "‬": "PDF",
    "‭": "LRO", "‮": "RLO",
    "⁦": "LRI", "⁧": "RLI", "⁨": "FSI", "⁩": "PDI",
}
BIDI_CTRL_RE = re.compile("[" + "".join(BIDI_CONTROLS) + "]")

# Pre-shaped glyphs from Presentation Forms A and B, plus the lam-alef
# ligatures. The standard Arabic block is the only correct encoding here.
PRESENTATION_FORMS = re.compile(r"[ﭐ-﷿ﹰ-﻿]")

TATWEEL = "ـ"

ARABIC_INDIC_DIGITS = re.compile(r"[٠-٩۰-۹]")

# A nucleotide sequence printed with its 5'/3' ends, e.g. the biology canon's
# \texttt{5'-ATGGCTTAC-3'} and \texttt{5'-GTAAGCCAT-3'}. CHEM_FORMULA already
# clears a bare run of bases (ATGGCTTAC fullmatches (?:[A-Z][a-z]?){2,}), but
# LATIN_WORD swallows the trailing hyphen of the 3' end, so the token reaching
# the loop is "ATGGCTTAC-" and no rule can see it. Verified against the
# UNTRANSLATED English canon, where the gate reports these two sites and no
# other edition can avoid inheriting them: a base sequence is not English, it
# is data, and it must stay byte-identical in every language.
# Added by the Arabic Biology Book 2 agent, 2026-09-05.
NUCLEOTIDE_SEQ = re.compile(r"[ACGTU]{4,}[-']*")

# Latin genus and species names this BIOLOGY volume uses that the original
# ALLOWED_WORDS list (written for Book 1) does not carry. Scientific
# nomenclature is international: an Arabic biology text prints
# \emph{Chlorella} in Latin exactly as the French, Dutch and Indonesian
# editions do, and the English canon italicises them for that reason. Found by
# grepping the Book 2 canon for \emph{...}/\textit{...} whose content is a
# capitalised Latin word, which is what the ALLOWED_WORDS comment asks a later
# book to do. Common-noun forms (paramecium, neanderthal) are NOT listed --
# those are ordinary prose and are written in Arabic.
# Added by the Arabic Biology Book 2 agent, 2026-09-05.
ALLOWED_WORDS |= {
    "chlorella", "euglena", "archaeopteryx", "paranthropus",
    "africanus", "heidelbergensis",
}

# The IUPAC three-letter abbreviations for the twenty amino acids. Book 2's
# genetic-code table prints all twenty of them, and so does every other
# edition: the French twin keeps "UUU Phe / UCU Ser / UAU Tyr" verbatim and
# translates only "deuxieme lettre" and "arret" around them. They are
# international nomenclature, like the Latin binomials above, not English
# words -- and they are unreachable by the existing rules, since "Phe" is
# neither all-caps (the acronym exemption) nor a chemical formula.
# Added by the Arabic Biology Book 2 agent, 2026-09-05.
ALLOWED_WORDS |= {
    "ala", "arg", "asn", "asp", "cys", "gln", "glu", "gly", "his", "ile",
    "leu", "lys", "met", "phe", "pro", "ser", "thr", "trp", "tyr", "val",
}

# Nucleic-acid abbreviations. The Arabic edition keeps DNA and RNA in Latin --
# the choice Book 1 `ar` already shipped (\emph{DNA}\index{DNA}) and the one
# an Arabic biology textbook makes -- so the derived forms mRNA, tRNA and rRNA
# are Latin too. "DNA" and "RNA" pass already as all-caps acronyms; the mixed
# case of "mRNA" reaches no existing rule.
# Added by the Arabic Biology Book 2 agent, 2026-09-05.
ALLOWED_WORDS |= {"mrna", "trna", "rrna"}

# One more institution that every edition keeps in Latin, for the same reason
# as "Wikimedia Commons" and "Wellcome Collection" above: this edition's own
# frontmatter/image-credits-book2.ar.tex already prints "Imperial War
# Museums" unchanged, so a chapter caption that transliterated it would give
# the book two spellings of one institution -- the exact defect the Arabic
# Book 1 agent reported. Kept as a separate pattern rather than folded into
# ATTRIBUTION so the original stays untouched; the words "war" and "museums"
# are deliberately NOT added to ALLOWED_WORDS, which would blind the gate.
# Added by the Arabic Biology Book 2 agent, 2026-09-05.
ATTRIBUTION_EXTRA = re.compile(
    r"Imperial\s+War\s+Museums"
    # The publisher and the title of the textbook a figure is reused from,
    # for exactly the same reason: frontmatter/image-credits-book2.ar.tex
    # prints "OpenStax \\emph{Anatomy and Physiology}" in Latin, so a
    # chapter caption that translated the title would give the book two
    # names for one source. A work's title and its publisher are names, not
    # prose. "anatomy" and "physiology" are again deliberately NOT added to
    # ALLOWED_WORDS -- only this exact phrase is blanked.
    # Added by the Arabic Biology Book 2 agent, 2026-09-05.
    r"|OpenStax|Anatomy\s+and\s+Physiology"
    # Book 3's own frontmatter/image-credits-book3.ar.tex prints "National
    # Cancer Institute" in Latin (the coordinator wrote it that way, following
    # the ruling that an attribution string is the legally required credit and
    # stays verbatim). A chapter caption crediting the same photograph must
    # therefore print it identically, or the book carries two spellings of one
    # institution -- the defect the Arabic Book 1 agent reported. As above,
    # "national", "cancer" and "institute" are deliberately NOT added to
    # ALLOWED_WORDS; only this exact phrase is blanked.
    # Added by the Arabic Biology Book 3 agent, 2026-09-06.
    r"|National\s+Cancer\s+Institute"
    # The two portrait subjects of the classification chapter and the two
    # works its captions name. The personal-name ruling for this edition is
    # that the SUBJECT of a portrait is transliterated with the Latin form in
    # parentheses on first mention -- which is exactly what
    # frontmatter/image-credits-book3.ar.tex prints ("كارل لينيوس (Carl
    # Linnaeus)"), so the caption must print it identically or the book
    # carries two spellings of one person. A work's TITLE is a name too, like
    # \emph{Micrographia} below. Exact phrases only: "carl", "species" and
    # "naturae" stay out of ALLOWED_WORDS.
    # Added by the Arabic Biology Book 3 agent, 2026-09-06.
    r"|Carl\s+Linnaeus|Carl\s+Woese|Ernst\s+Haeckel"
    r"|Species\s+Plantarum|Systema\s+Naturae"
    # Same rule, same book: frontmatter/image-credits-book3.ar.tex prints
    # "Nobel Foundation" in Latin for the two portrait photographs it
    # credits, so the chapter captions crediting them must print it
    # identically. "nobel" and "foundation" stay out of ALLOWED_WORDS.
    # Added by the Arabic Biology Book 3 agent, 2026-09-06.
    r"|Nobel\s+Foundation"
    # The rest of the attribution strings that Book 3's own
    # frontmatter/image-credits-book3.ar.tex prints in Latin: the
    # institutions and repositories that hold the photographs, the
    # photographers and painters who made them, and the titles of the two
    # published works a plate is reproduced from. A chapter caption
    # crediting the same image must print the same string, or the book
    # carries two spellings of one credit -- the defect the Arabic Book 1
    # agent reported. The SUBJECT of a portrait is a different case and is
    # transliterated, so no subject name is listed here. None of these
    # words is added to ALLOWED_WORDS; only these exact phrases are
    # blanked. Added by the Arabic Biology Book 3 agent, 2026-09-06.
    r"|Lawrence\s+Berkeley\s+Laboratory"
    r"|National\s+Human\s+Genome\s+Research\s+Institute"
    r"|Electron\s+Microscopy\s+Facility"
    r"|Jan\s+Verkolje|Alexander\s+Roslin|Don\s+Hamerman"
    r"|Nationalmuseum|Rijksmuseum"
    r"|Micrographia|Kunstformen\s+der\s+Natur")

# Gene symbols keep their published capitalisation in every language, and the
# mouse/human convention (mouse \emph{Sry}, human SRY) is part of the name.
# All-caps symbols (SRY, CFTR, ATP) already pass as acronyms; the mixed-case
# mouse form does not, and it is the only one Book 2 prints.
# Added by the Arabic Biology Book 2 agent, 2026-09-05.
ALLOWED_WORDS |= {"sry"}

# Biology Book 4's own Latin binomials, higher taxa and gene/strain symbols,
# grepped from parts/bachelor-2/*.tex as the ALLOWED_WORDS comment at the top
# of this file instructs ("grep the English bodies again if a later book adds
# species"). A Linnaean name is Latin in every script -- an Arabic biology
# textbook italicises \emph{Volvox carteri} exactly as an English one does --
# and a gene symbol or a strain designation is an international identifier,
# not an English word. Listed word by word, because the gate tokenises. No
# ordinary English word is added here: a definition headword such as
# "Adaptation" or "Budding" is translated by this edition and must keep
# firing the gate.
# Added by the Arabic Biology Book 4 agent, 2026-09-16.
ALLOWED_WORDS |= {
    # genera and species epithets
    "acetabularia", "aegilops", "tauschii", "urartu", "amoeba", "proteus",
    "anabaena", "arabidopsis", "archaeopteryx", "azotobacter", "bacillus",
    "beggiatoa", "chlamydomonas", "clostridium", "daphnia", "desulfovibrio",
    "drosophila", "melanogaster", "eudorina", "frankia", "fucus", "gonium",
    "kalanchoe", "neurospora", "nitrobacter", "nitrosomonas", "ophioglossum",
    "reticulatum", "pandorina", "paracoccus", "phytophthora", "infestans",
    "plasmodium", "pleodorina", "posidonia", "pseudomonas", "sordaria",
    "thiobacillus", "thiomargarita", "namibiensis", "tiktaalik",
    "trichoderma", "vibrio", "fischeri", "volvox", "carteri",
    # gene, locus, hormone and strain symbols printed in Latin by every edition
    "myod", "wuschel", "constans", "hox", "mads", "pax3", "pax6", "pax7",
    "shh", "sox9", "tbx4", "tbx5", "wnt", "lac", "gal", "thr", "ndm", "hfr",
    "hcg", "igg", "iga", "fsh", "gnrh",
    "sonic", "hedgehog", "tbx", "hoxa", "hoxd", "wnt", "fgf", "fgfs",
    "bmp", "aer", "zpa", "gremlin", "kisspeptin",
    "pax", "sox", "myf", "myod", "mrf", "cdna", "dystrophin",
    "clavata", "clv", "wus", "pin", "expansin", "expansins",
    "pfr", "flc", "constans", "florigen",
}


def check_file(path: pathlib.Path, findings: list) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = str(path)
    body = strip_comments(raw)
    seen = visible_text(body, findings, rel)
    _occ: dict = {}

    # 1. residual English in visible text
    for m in ATTRIBUTION.finditer(seen):
        seen = seen[:m.start()] + " " * (m.end() - m.start()) + seen[m.end():]
    for m in ATTRIBUTION_EXTRA.finditer(seen):
        seen = seen[:m.start()] + " " * (m.end() - m.start()) + seen[m.end():]
    for m in LATIN_WORD.finditer(seen):
        word = m.group(0)
        low = word.lower()
        if low in ALLOWED_WORDS or low in ALLOWED_UNITS:
            continue
        if low in PGFMATH_FUNCTIONS:
            continue
        if word.islower() and low in SHORT_ENGLISH:
            findings.append((rel, _locate(body, word, _occ),
                             "english", f"English in visible text: {word!r}"))
            continue
        if word.isupper() and len(word) <= 4:
            continue        # acronyms printed in Latin (SI, ATP)
        if CHEM_FORMULA.fullmatch(word):
            continue        # MgF(2), NaCl, GaAs, AsH(3): element symbols, not
                            # English, and they stay Latin in every script
        if CHEM_CHAIN.fullmatch(word):
            continue        # H--O--H, C--C, S--S: a structural formula
        if NUCLEOTIDE_SEQ.fullmatch(word):
            continue        # 5'-ATGGCTTAC-3': a DNA sequence, see above
        if "-" in word and all(
                part.lower() in ALLOWED_WORDS
                for part in word.split("-") if part):
            continue        # Met--Pro--Glu--Phe: LATIN_WORD swallows the
                            # hyphens, so an amino-acid chain arrives as ONE
                            # token and no per-word rule can see it. Accepted
                            # only when EVERY component is separately allowed,
                            # so an ordinary English compound still fires.
                            # Added by the Arabic Biology Book 2 agent.
        if len(word) < 3:
            continue        # stray single symbols
        findings.append((rel, _locate(body, word, _occ),
                         "english", f"English in visible text: {word!r}"))

    for m in DOTTED_ABBREV.finditer(seen):
        findings.append((rel, _locate(body, m.group(0), _occ),
                         "english",
                         f"English abbreviation in visible text: {m.group(0)!r}"))

    # 2. transliterated English function words
    for token, gloss in TRANSLITERATED_ARTICLES.items():
        for _ in re.finditer(rf"(?<![{ARABIC}]){token}(?![{ARABIC}])", seen):
            findings.append((rel, _locate(body, token, _occ),
                             "translit",
                             f"transliterated English {gloss!r}: {token!r}"))

    # 3. Latin comma / semicolon / question mark closing an Arabic clause.
    #    The full stop is correct in Arabic and is deliberately not checked.
    for sym, want in ((",", "،"), (";", "؛"), ("?", "؟")):
        for m in re.finditer(
                rf"[{ARABIC_LETTER}][{ARABIC_MARK}]*[)\"'\s]*\{sym}", seen):
            findings.append((rel, seen[:m.start()].count("\n") + 1,
                             "punct",
                             f"Latin {sym!r} after Arabic (use {want!r})"))

    # 4. Arabic-Indic digits: this edition writes ASCII so prose matches math.
    for m in ARABIC_INDIC_DIGITS.finditer(body):
        findings.append((rel, body[:m.start()].count("\n") + 1,
                         "digits",
                         f"Arabic-Indic digit {m.group(0)!r} (use ASCII 0-9)"))

    # 6. invisible bidi control characters
    for m in BIDI_CTRL_RE.finditer(raw):
        findings.append((rel, raw[:m.start()].count("\n") + 1,
                         "bidi-ctrl",
                         f"bidi control character {BIDI_CONTROLS[m.group(0)]}"))

    # 7. Arabic presentation forms instead of the standard block
    for m in PRESENTATION_FORMS.finditer(raw):
        findings.append((rel, raw[:m.start()].count("\n") + 1,
                         "presform",
                         f"presentation form U+{ord(m.group(0)):04X} "
                         f"(use the standard Arabic block)"))

    # 8. tatweel padding
    for m in re.finditer(TATWEEL, raw):
        findings.append((rel, raw[:m.start()].count("\n") + 1,
                         "tatweel", "tatweel U+0640 (kashida padding)"))

    # 9. thin space splitting a number from its noun
    for m in re.finditer(rf"[{ARABIC_LETTER}]\s*\\,\s*\d", body):
        findings.append((rel, body[:m.start()].count("\n") + 1,
                         "split-number",
                         "\\, between Arabic and digits (split number?)"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("dirs", nargs="+", help="directories of .tex files")
    ap.add_argument("--quiet", action="store_true",
                    help="print only the per-class summary")
    ap.add_argument("--max-detail", type=int, default=8,
                    help="detail lines to show per class (default 8)")
    args = ap.parse_args()

    findings: list = []
    files = 0
    for d in args.dirs:
        p = pathlib.Path(d)
        # A PATH THAT IS NOT A DIRECTORY USED TO BE SKIPPED IN SILENCE, so the
        # gate handed a single .tex file printed "OK (0 files)" and exited 0 --
        # a clean pass that had checked nothing. That is how 561 residual-English
        # hits survived per-file checking during the Biology Book 5 run. Accept a
        # file, and refuse a path that is neither. Found by the Arabic Book 5
        # agent, 2026-09-17; fixed in all three script gates at once.
        if p.is_file():
            files += 1
            check_file(p, findings)
            continue
        if not p.is_dir():
            sys.stderr.write("  ERROR: not a file or directory: %s\n" % d)
            return 2
        for f in sorted(p.glob("*.tex")):
            files += 1
            check_file(f, findings)

    if not findings:
        print(f"  arabic prose gate: OK ({files} files)")
        return 0

    by_class: dict = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))

    print(f"  arabic prose gate: {len(findings)} issue(s) in {files} files")
    for cls in sorted(by_class):
        hits = by_class[cls]
        bad_files = len({h[0] for h in hits})
        print(f"    {cls:<14} {len(hits):>5} hit(s) in {bad_files} file(s)")
        if not args.quiet:
            for rel, line, msg in hits[:args.max_detail]:
                print(f"        {rel}:{line}: {msg}")
            if len(hits) > args.max_detail:
                print(f"        ... {len(hits) - args.max_detail} more")
    return 1


# NOTE: every block below was appended by a translation agent AFTER the
# module body but BEFORE the __main__ guard, which now stays last. An
# earlier append put them after the guard, where sys.exit(main()) had
# already run and the additions were dead code: the module imported fine
# (so a harness that imports check_file saw them) while the command-line
# gate did not. Keep the guard at the very end of this file.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.


# Biology Book 5's own Latin binomials, higher taxa, gene/protein symbols and
# method names, collected from parts/bachelor-3/ exactly as the ALLOWED_WORDS
# comment at the top of this file instructs a later book to do ("grep the
# English bodies again if a later book adds species"). Book 5 spans twenty-seven
# molecular and organismal fields, so it prints many more gene symbols than any
# earlier volume. The rule applied here is the one the Book 2 and Book 4 blocks
# above use: a Linnaean name is Latin in every script, and an italicised gene
# symbol or a method acronym is an international identifier, not an English
# word. Ordinary English words are NOT added -- a definition headword such as
# "Adhesion" or "Memory" is translated by this edition and must keep firing the
# gate -- and neither are surnames, which this edition transliterates
# (هويش، كورنبرغ، لوغر).
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {
    # genera, species epithets and higher taxa
    "agrobacterium", "tumefaciens", "aplysia", "californica", "aspergillus",
    "anthracis", "botrytis", "buchnera", "burkholderia", "caenorhabditis",
    "ciona", "clostridioides", "difficile", "dscam", "haemophilus",
    "influenzae", "helicobacter", "pylori", "hydra", "klebsiella", "listeria",
    "monocytogenes", "neisseria", "nocardia", "paulinella", "philanthus",
    "aeruginosa", "riftia", "salmonella", "sclerotinia", "serratia",
    "pyogenes", "symbiodiniaceae", "aquaticus", "wolbachia", "petunia",
    "glomeromycete", "zooxanthellae",
    # gene, protein, complex and allele symbols printed in Latin
    "xist", "igf", "peg", "cdkn", "agouti", "var", "snrpn", "ube",
    "antennapedia", "ultrabithorax", "trithorax", "argonaute", "dicer",
    "drosha", "bicoid", "nanos", "hunchback", "knirps", "giant", "caudal",
    "eve", "engrailed", "wingless", "oskar", "gurken", "sxl", "msl", "dsx",
    "abi", "akt", "apaf", "arf", "arp", "bcl", "camkii", "cas", "caspase",
    "cdc", "cdk", "ced", "cgas", "cgmp", "chk", "clock", "bmal", "dectin",
    "ecori", "egl", "eif", "enac", "exportin", "fasl", "flg", "fls", "foxp",
    "groel", "groes", "hnrnp", "hoxb", "hoxc", "hoxa", "hoxd", "hsp",
    "igd", "ige", "igm", "iga", "igg", "inos", "klf", "lexa", "lgr", "lin",
    "loxp", "luxi", "luxr", "macroh", "mad", "mcl", "mecp", "msh", "mlh",
    "muth", "mutl", "muts", "myd", "mtor", "oct", "nanog", "piezo", "pitx",
    "prp", "psc", "reca", "rhoa", "rpos", "ruvc", "shieldin", "snrk",
    "sting", "sula", "tdt", "tric", "unc", "uvra", "uvrb", "wee", "wus",
    "notch", "shh", "noggin", "chordin", "follistatin", "dnmt", "tet",
    "polycomb", "myc", "kras", "ras", "raf", "rab", "rac", "cdna",
    "let", "pri", "pre", "shrna", "sirna", "sirnas", "mirna", "mirnas",
    "pirna", "pirnas", "lncrna", "lncrnas", "ncrna", "snrnas", "microrna",
    "micrornas", "mrnas", "sema", "cre", "flp", "frt", "tra",
    "vhl", "brca", "apc", "atm", "atr", "rad", "kdm", "shox", "src", "vegf",
    "glut", "creb", "ampa", "nmda", "pam", "pin", "della", "pif", "pifs",
    "cry", "phy", "pfr", "sec", "copi", "copii", "clathrin",
    # methods, databases and scoring matrices, which are proper names
    "chip", "seq", "blast", "blosum", "pfam", "qpcr", "nanopore", "sanger",
    "taq", "crispr", "rnai", "bruijn", "cryo", "sem", "tem", "pcr",
    "alphafold", "hmms", "hmm", "otus", "sloss", "iucn", "snps",
    # units and instrument abbreviations reduced to letters by the tokeniser
    "mosm", "mmhg", "hba", "nacl", "kda", "gfp", "camp", "dgtp",
}

# Two more tokens the tokeniser cannot reach on its own. LATIN_WORD splits at
# a digit, so the antisense-transcript symbol UBE3A-ATS arrives as "UBE" and
# then as the single token "A-ATS"; the hyphen rule accepts a compound only
# when EVERY component is separately allowed, so the stray one-letter "a" has
# to be listed beside "ats". Listing "a" costs the gate nothing: a standalone
# "a" is already below the three-character floor, and the only other effect is
# on a hyphenated compound whose other half is itself an allowed identifier.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"a", "t", "ats"}

# Book 5 prints three Drosophila gene names that ARE ordinary English words,
# so they cannot go into ALLOWED_WORDS without blinding the gate for the word
# itself. A gene symbol is a name: \emph{Sex-lethal}, \emph{transformer} and
# \emph{doublesex} stay Latin in the French, Dutch and Indonesian editions too.
# They are blanked as exact phrases, the way "Imperial War Museums" is above,
# rather than token by token -- "sex" and "lethal" deliberately stay out of
# ALLOWED_WORDS. Appended to the existing pattern so the original stays intact.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern + r"|Sex-lethal|transformer|doublesex"
)

# Lowercase gene symbols and nomenclature fragments that are not English words.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {
    "elegans", "piwi", "rnase", "snrna", "snrnas", "poly", "dsx", "sxl",
    "tra", "lin", "unc", "egl", "ced", "abd", "dfd", "scr", "antp", "ubx",
    "gcn", "atf", "pcsk", "dgcr", "drm", "suv", "ezh", "prc", "hdac", "hat",
    "hats", "hdacs", "mbd", "mecp", "tet", "cpg", "cpgs", "tpg", "cpa",
}

# More Book 5 identifiers: polymerase and recombinase symbols, and the names of
# two recombination systems. "Pol" is the printed abbreviation of a polymerase
# (Pol~$\beta$, Pol~IV), "lox" and "frt" are the recognition-site names of the
# Cre-lox and Flp-FRT systems, "pkcs" is the catalytic subunit of DNA-PK.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"pol", "lox", "frt", "pkcs", "rev", "flp", "xpa", "xpc",
                  "xpf", "xpg", "brca", "parp", "chk", "atm", "atr", "mrn",
                  "rpa", "dam", "muth", "okazaki"}

# "LINE-1" is the name of a retrotransposon family (long interspersed nuclear
# element), printed in Latin in every edition. It cannot go token by token into
# ALLOWED_WORDS, because "line" is an ordinary English word the gate must keep
# catching; blanked as an exact phrase instead, like the gene names above.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(ATTRIBUTION_EXTRA.pattern + r"|LINE-1|Bcl-xL"
    r"|(?<![A-Za-z])(?:Bad|Puma)(?![A-Za-z0-9])")

# An ALIGNED nucleotide or peptide row contains gap characters, so the existing
# NUCLEOTIDE_SEQ (which allows only trailing hyphens, for the 3' end) cannot see
# \texttt{G-AT} / \texttt{A-CAT}: the tokeniser hands it "A-CAT", and the hyphen
# rule then asks for "cat" in ALLOWED_WORDS, which must not be added. Alignment
# rows are data, byte-identical in every edition. Widened to accept internal
# gaps; the four-character floor is kept, so an ordinary word is still reported.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
NUCLEOTIDE_SEQ = re.compile(r"[ACGTU](?:[ACGTU-]{2,})[ACGTU][-']*")

# Two more genus names Book 5 prints in Latin, and the components of "T-DNA",
# the transferred segment of the Agrobacterium Ti plasmid. "dna" is already
# exempt as an acronym on its own; it has to be listed for the hyphen rule,
# which accepts a compound only when every component is separately allowed.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"thermus", "streptococcus", "staphylococcus", "aureus",
                  "escherichia", "coli", "dna", "rna", "bacillus",
                  "clostridium", "pseudomonas", "vibrio", "arabidopsis",
                  "drosophila", "caenorhabditis", "neurospora", "xenopus",
                  "danio", "rerio", "saccharomyces", "cerevisiae"}

# Enzyme-class suffixes and the SNARE families. "GTPase", "ATPase", "v-SNARE"
# and "t-SNARE" are international nomenclature printed in Latin in every
# edition; the glycosylation consensus "Asn-X-Ser/Thr" is a sequence written in
# the three-letter amino-acid code, whose components must each be listed for
# the hyphen rule ("asn" and "ser" are already allowed; "x" and "thr" are not).
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"gtpase", "gtpases", "atpase", "atpases", "snare", "snares",
                  "v", "x", "thr", "sar", "arf", "ku", "nsf", "kdel", "skl",
                  "ldl", "hdl", "cftr", "erad"}

# ---------------------------------------------------------------------------
# Standard math SUBSCRIPTS written with \text{}, which no translator can touch.
# ---------------------------------------------------------------------------
# Book 5 writes rate constants as k_{\text{on}}, k_{\text{off}} and the
# steady-state concentration as C_{\text{ss}} -- and it writes them inside
# \[...\] displays, which tools/id_apply.py's math census compares BYTE FOR
# BYTE. So the applier requires those three fragments to stay English while
# this gate, which reads \text{} inside math, requires them to be Arabic: the
# two gates demand opposite things and no edition can satisfy both. They are
# symbol subscripts, not prose -- the same class the SHORT_ENGLISH comment
# above already exempts for x_{\text{m}} and R_{\text{s}} -- so they are
# skipped at extraction rather than added to ALLOWED_WORDS, which would blind
# the gate to the ordinary English words "on" and "off" in running prose.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
MATH_SUBSCRIPTS = {"on", "off", "ss", "max", "min", "NHEJ", "HR",
                   # R_{\text{eff}}, the effective reproduction number of the
                   # herd-immunity chapter, is frozen inside displays the same way.
                   # Added by the Arabic Biology Book 5 agent, 2026-09-17.
                   "eff",
                   # M_{\text{brain}} \propto M_{\text{body}}^{0.75}, the
                   # allometric law of the nervous-systems chapter.
                   "brain", "body",
                   # P_{\text{see}}, the frequency-of-seeing function of the
                   # sensory-systems chapter.
                   "see",
                   # t_{\text{pre}} - t_{\text{post}}, the spike-timing axis of
                   # the learning-and-memory chapter.
                   "pre", "post",
                   # The renal chapter's frozen symbols: P_{\text{GC}},
                   # P_{\text{BS}}, \pi_{\text{GC}}, \text{GFR}, \text{RPF},
                   # U_{\text{osm}}, P_{\text{osm}}.
                   "GC", "BS", "GFR", "RPF", "osm",
                   # The endocrinology chapter: \text{EC}_{50}, \text{TSH},
                   # \text{PTH}, \text{Ca}, \text{Ca}_{0}.
                   "EC", "TSH", "PTH", "Ca",
                   # The plant chapter: [\text{Pfr}], [\text{Pr}],
                   # [\text{IAA}]_{\text{in}}/[\text{IAA}]_{\text{out}},
                   # \mathrm{pH}_{\text{in}}. "in"/"out" are blinded only
                   # inside a math \text{} group, never in prose.
                   "Pfr", "Pr", "IAA", "IAAH", "in", "out",
                   # The developmental chapter: D_{\text{inh}},
                   # k_{\text{inh}} of the Turing wavelength.
                   "inh",
                   # The stem-cell chapter: L_{\text{crit}}.
                   "crit",
                   # The molecular-evolution chapter: P_{\text{discord}},
                   # d_{\text{true}}.
                   "discord", "true",
                   # The behavioural-ecology chapter: the Hawk--Dove payoff
                   # matrix inside \[...\], whose \text{} row and column
                   # heads id_apply compares byte for byte.
                   "Hawk", "Dove", "vs Hawk", "vs Dove"}
_extract_math_text_all = extract_math_text


def extract_math_text(body: str) -> str:            # noqa: F811
    out = []
    for m in MATH_TEXT_MACRO.finditer(body):
        inner, _ = match_group(body, m.end() - 1, "{", "}")
        if inner and inner.strip() not in MATH_SUBSCRIPTS:
            out.append(inner)
    return " ".join(out)

# Two more Book 5 protein symbols: the Rho family of small GTPases (Rac, Rho,
# Cdc42 -- "rac" and "cdc" are already allowed) and Listeria's surface protein
# ActA, which recruits the host Arp2/3 complex.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"rho", "acta", "arp", "cdc", "rac", "tau", "map",
                  "katanin", "profilin", "cofilin", "dynactin", "nexin"}

# Single letters, for the hyphen rule only. A cyclin--CDK pair prints as
# "cyclin D--Cdk4/6", which LATIN_WORD swallows whole as "D--Cdk"; the hyphen
# rule then wants every component listed. Single letters never match
# LATIN_WORD on their own (it requires two characters), so listing them here
# costs the gate nothing at all.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= set("abcdefghijklmnopqrstuvwxyz")

# The apoptosis gene/protein symbols of Book 5's Bcl-2 chapter, plus the
# cell-cycle and death-receptor names. All are published protein symbols kept
# in Latin by every edition. "bad" and "puma" are ordinary English words, so
# they are matched here only in their Latin symbol spelling; the gate keeps
# catching the lowercase English words, which are not in this set.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"bax", "bak", "bim", "bid", "noxa", "mcl", "flip", "iap",
                  "iaps", "fas", "fasl", "trail", "tnf", "apaf", "mad",
                  "securin", "separase", "cohesin", "condensin", "mcm",
                  "wee", "ripk", "mlkl", "gasdermin", "venetoclax",
                  "anoikis", "myc", "scf", "apc", "cdk", "cdks"}

# The signalling-cascade names of the cancer chapter, printed as chains of
# protein symbols (Ras--MAPK, Raf--MEK--ERK, PI3K--Akt--mTOR, BCR--ABL) which
# the tokeniser hands over as one hyphenated token.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"mapk", "raf", "mek", "erk", "akt", "bcr", "abl", "egfr",
                  "her", "pten", "vegf", "hif", "vhl", "smad", "kras",
                  "braf", "imatinib", "trastuzumab", "apobec", "ctla",
                  "cadherin", "microglobulin", "src", "wnt", "notch",
                  "gtp", "gdp", "atp", "adp", "amp", "nadh", "fadh"}

# Bacteriology names: the species epithet of Bacillus subtilis and the
# D-lactate terminus that replaces D-Ala in vancomycin-resistant cell walls.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"subtilis", "lactate", "ala", "lux", "rpos", "mrsa",
                  "integron", "integrons", "pangenome", "teichoic"}

# Nucleic-acid strand abbreviations (dsDNA, ssRNA, ...) and the Latin phrase
# Beijerinck coined for the tobacco-mosaic agent, which every edition prints
# in Latin as a historical quotation.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"dsdna", "ssdna", "dsrna", "ssrna", "contagium", "vivum",
                  "fluidum", "aciclovir", "remdesivir", "molnupiravir",
                  "tenofovir", "lamivudine", "azt", "nirmatrelvir",
                  "maraviroc", "pleconaril", "lenacapavir", "ribavirin",
                  "ccr", "ace", "sars", "cov", "hiv", "pfu"}

# "Nod factor" (nodulation factor): the lipochitooligosaccharide signal a
# rhizobium answers a legume's flavonoids with. Every edition prints the
# symbol "Nod" unchanged, so the Arabic reads "عوامل Nod". Matched
# case-sensitively rather than added to ALLOWED_WORDS so that the ordinary
# English word "nod" stays gated; \b would not work here, because an Arabic
# letter is a word character and "وNod" therefore has no boundary before N.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern + r"|(?<![A-Za-z])Nod(?![A-Za-z])")


# Innate-immunity symbols: the Drosophila gene "Toll" that named the Toll-like
# receptors, the cytosolic RNA sensor RIG-I and the JAK--STAT pathway. "Toll"
# is matched case-sensitively so that the ordinary English noun "toll" stays
# gated; the other two are ordinary protein-family acronyms.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"rig", "jak", "stat", "jaks", "stats"}
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern + r"|(?<![A-Za-z])Toll(?![A-Za-z])")


# CAR-T: chimaeric antigen receptor T cells. Matched case-sensitively as a
# whole token so that the English noun "car" stays gated.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern + r"|(?<![A-Za-z])CAR-T(?![A-Za-z])")


# "L-dopa", the drug name printed unchanged in every edition (the levorotatory
# prefix is part of the name). Matched case-sensitively so that the English
# word "dopa" alone, and the letter-plus-word pattern generally, stay gated.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern + r"|(?<![A-Za-z])L-dopa(?![A-Za-z])")


# A TikZ *label* key was read as if its whole braced value were prose. A label
# is written "label={[font=\tiny]right:hormone}": the option group and the
# anchor word are syntax, only what follows the colon is visible text. Both
# TIKZ_NODE (which grabs the first braced group after "node", i.e. the label's)
# and TIKZ_TEXT_KEYS therefore reported "font" and "right" as residual English
# on every such node, and no edition could clear them without rewriting the
# picture. Normalised here, before extraction, to "label={hormone}", so the
# visible text is still gated and the syntax is not. A label with no anchor is
# left untouched, so nothing becomes invisible.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
_extract_drawing_text_with_label_syntax = extract_drawing_text
LABEL_SYNTAX = re.compile(
    r"(\blabel\s*=\s*)\{\s*(?:\[[^\]]*\]\s*)?"
    r"(?:(?:above|below|left|right|north|south|east|west|centre|center)"
    r"(?:\s+(?:above|below|left|right|north|south|east|west))?\s*:\s*)?"
    r"((?:[^{}]|\{[^{}]*\})*)\}")


def extract_drawing_text(body: str, depth: int = 0) -> str:   # noqa: F811
    return _extract_drawing_text_with_label_syntax(
        LABEL_SYNTAX.sub(lambda m: m.group(1) + "{" + m.group(2) + "}", body),
        depth)


# Clock-gene symbols, printed italic and unchanged in every edition: the
# Drosophila gene "period" and its mammalian orthologues Per and Cry. Matched
# as whole tokens; "period" is thereby also blinded as an ordinary English
# noun, which is the accepted cost -- this edition writes "دور" for the period
# of an oscillation everywhere and never leaves the English word standing.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern
    + r"|(?<![A-Za-z])(?:Per|Cry|period)(?![A-Za-z])")


# Plant-molecular names: the Aux/IAA repressor family, the F-box class of
# ubiquitin-ligase subunits, and the species epithet of Arabidopsis thaliana.
# "F-box" is matched case-sensitively as a whole token so that the English noun
# "box" stays gated.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"aux", "thaliana"}
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern + r"|(?<![A-Za-z])F-box(?![A-Za-z])")


# Drosophila gene symbols printed italic and unchanged in every edition:
# even-skipped, fushi tarazu, hairy, knirps (kni), bithorax, Distal-less,
# yellow, and the "ppel" fragment that a tokeniser leaves when it splits
# "Krueppel" at its u-umlaut. The lowercase English words "hairy" and "yellow"
# are blinded as a documented cost: this edition writes أشعر / أصفر and never
# leaves either English word standing.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"ppel", "fushi", "tarazu", "kni", "bithorax"}
ATTRIBUTION_EXTRA = re.compile(
    ATTRIBUTION_EXTRA.pattern
    + r"|(?<![A-Za-z])(?:even-skipped|Distal-less|hairy|yellow)(?![A-Za-z])")


# Cre-ER, the tamoxifen-inducible recombinase of lineage tracing, and nAG, the
# newt anterior-gradient protein. Both are protein names printed unchanged.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ALLOWED_WORDS |= {"cre", "er", "nag"}


# "Anefo", the Dutch national photo agency whose archive supplies several
# public-domain portraits; part of a photo credit, like Wikimedia Commons.
# Added by the Arabic Biology Book 5 agent, 2026-09-17.
ATTRIBUTION_EXTRA = re.compile(ATTRIBUTION_EXTRA.pattern + r"|Anefo")


if __name__ == "__main__":
    sys.exit(main())