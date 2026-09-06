#!/usr/bin/env python3
"""Hindi-specific hygiene gate for a translated tree.

check_translation.sh proves *structure*: same files, same labels, same
environment census. Its two prose gates are Latin-oriented and score nothing
on Devanagari -- gate 6 looks for TeX accent escapes (\\'e), which Hindi never
writes, and the drafty-"..." gate is script-agnostic. So a Hindi tree can be
structurally perfect and still be raw machine translation.

These are the failure classes the 2026-07-24 Hindi machine translation left
behind, each of which this script detects:

  1. residual English in visible text  -- \\text{ thousands}, TikZ nodes
     reading {tens} {units}, English chapter titles, English \\index keys.
     137 of 177 math bodies and 29 of 35 physics bodies carried these.
  2. transliterated English function words -- "द" for *the*, "ए" for *a*,
     "ऑफ", "एंड". A Hindi sentence never needs an article.
  3. Latin full stop where Hindi ends a sentence with a danda (।). The MT
     output mixed both, sometimes inside one paragraph.
  4. MT-injected spaces inside inline math -- "$P $ और $ Q $", which changes
     spacing in the output and is never what the English source wrote.
  5. a thin space splitting a number away from its noun -- the MT produced
     \\chapter{10 तक की संख्या\\,000} from "Numbers up to 10\\,000".

Usage:
    python3 tools/check_hindi_prose.py parts/grade-3/hi parts/grade-3/solutions/hi
    python3 tools/check_hindi_prose.py --quiet <dir> ...

Exit status is 1 if anything was flagged. Called by check_translation.sh for
lang == hi; safe to run by hand on a single directory while translating.
"""

from __future__ import annotations

import argparse
import pathlib
import re
import sys

DEVANAGARI = r"\u0900-\u097F"
DEV_CHAR = re.compile(f"[{DEVANAGARI}]")

# ---------------------------------------------------------------------------
# What is allowed to stay in Latin script inside visible Hindi text.
# ---------------------------------------------------------------------------
# Brand, markup names the prose legitimately mentions, and SI/unit symbols
# that Hindi textbooks print in Latin. Proper nouns are deliberately NOT
# whitelisted: a Hindi edition transliterates them (Fourier -> फूरिये).
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
}

# --- appended 2026-09-05 by the Biology Book 2 `hi` agent -------------------
# REASON: the block above says outright to grep the English bodies again when a
# later book adds species, and Book 2 (grades 10-12) adds these. Every one is a
# genus or species epithet the canon prints in italic Latin, which a Devanagari
# edition keeps in Latin exactly as the Latin-script editions do -- they are
# international nomenclature, not residual English. `sry` is the mouse gene
# symbol \emph{Sry}: gene symbols are Latin in every edition too, and the
# lowercase-with-capital form falls through the <= 4-letter acronym escape.
ALLOWED_WORDS |= {
    "heidelbergensis", "paranthropus", "africanus",
    "euglena", "chlorella", "archaeopteryx", "sry",
    # RNA species abbreviations, the same three letters in every edition and
    # exactly the kind of token "dna"/"rna"/"atp" are already whitelisted for.
    # Their mixed case (mRNA) defeats both the <= 4-letter acronym escape and
    # CHEM_FORMULA.
    "mrna", "trna", "rrna",
}

# 2026-09-05, biology Book 2 `hi`: the title of a CC BY work must be reproduced
# as published for the licence's attribution to be valid, so the image credit
# in parts/grade-12 keeps the Latin title *Anatomy & Physiology* (OpenStax).
# These two words are only ever the title of that book in this edition.
ALLOWED_WORDS |= {"anatomy", "physiology"}

# --- appended 2026-09-06 by the Biology Book 3 `hi` agent ---------------------
# REASON: the block above says outright to grep the English bodies again when a
# later book adds species, and Book 3 (university year 1) adds these. Every one
# is a genus or species epithet the canon prints in italic Latin, which a
# Devanagari edition keeps in Latin exactly as the Latin-script editions do:
# international nomenclature, not residual English. Enumerated from the canon,
# word by word (the gate tokenises), and only the ones it actually uses:
#   Escherichia coli, Paramecium aurelia, Paris japonica, Quercus robur,
#   Felis catus, Canis lupus (abbreviated F.~catus / C.~lupus), Dryas,
#   Mytilus, Pisaster, Rhizobium, Trypanosoma, Lynx (as a genus in ch. 25).
ALLOWED_WORDS |= {
    "aurelia", "japonica", "robur", "catus", "lupus",
    "paramecium", "paris", "quercus", "felis", "canis", "dryas",
    "mytilus", "pisaster", "rhizobium", "trypanosoma",
    "caudatum", "bursaria",
    # ch. 29 prints the type binomial of our own species, \emph{Homo sapiens},
    # in the same italic Latin as every other binomial in the book.
    "homo", "sapiens",
    # `lac` and `trp` are OPERON/GENE symbols, printed lowercase italic Latin in
    # every edition of every language -- the same case `sry` was whitelisted for
    # by the Book 2 agent. Their three lowercase letters defeat the <= 4-letter
    # UPPERCASE acronym escape. 12 sites in ch. 20 and its solutions.
    "lac", "trp", "laci", "lacz", "lacy", "laca",
    # `RuBisCO` and `cyt` are international abbreviations printed the same
    # way in every edition: the enzyme ribulose-bisphosphate
    # carboxylase/oxygenase, and the standard short form of cytochrome
    # (cyt $b_6f$, cyt $c$). Wave 1 of this run ruled explicitly that `cyt`
    # is not an English residue. Their mixed case defeats both the
    # uppercase-acronym escape and CHEM_FORMULA.
    "rubisco", "cyt",
    # `Alu` is the name of the human repeat element (after the AluI site),
    # a Latin-script symbol in every edition; mixed case, three letters.
    "alu",
    # `X-gal` is the trade name of the chromogenic galactoside used as the
    # lacZ reporter; the same string in every edition.
    "x-gal",
    # Two Latin quotations the canon prints as such: Virchow's dictum
    # `omnis cellula e cellula` (ch. 5) and the title of Hooke's
    # *Micrographia* (ch. 5). A title and a quotation are reproduced, not
    # translated, in every edition.
    "omnis", "cellula", "micrographia",
}

# Unit and symbol strings that may appear bare in a table cell or node.
ALLOWED_UNITS = {
    "m", "s", "kg", "g", "mg", "km", "cm", "mm", "nm", "um",
    "dm", "dam", "hm",
    "n", "j", "w", "hz", "pa", "mol", "cd", "k", "a", "v", "c", "t",
    "wb", "f", "ev", "min", "h", "l", "ml", "rad", "sr", "bq", "gy", "sv",
    "kwh", "kj", "mj", "gpa", "mpa", "kpa", "khz", "mhz", "ghz",
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
    # 2026-09-06, biology Book 3 `hi`: the siunitx FAMILY, not just \qty.
    # \qtylist{1;2;5;10;20}{mmol/L} left "mmol" in visible text and was
    # reported as residual English -- a defect no translator can remove,
    # because the unit argument is mathematics in every language. Invisible
    # until now because the gate fires on the English canon anyway. The
    # whole family takes fixed argument counts: qtyrange/SIrange 3,
    # qtylist/numrange 2, numlist 1.
    "qtyrange": 3, "qtylist": 2, "numlist": 1, "numrange": 2,
    "SIrange": 3, "SIlist": 2, "unitlist": 1,
    "newcommand": 2, "renewcommand": 2, "providecommand": 2,
    "color": 1, "textcolor": 1, "definecolor": 3, "pgfplotsset": 1,
    "hypersetup": 1, "setlength": 2, "addtolength": 2, "url": 1,
}

# \omterm{def:label}{visible display} -- first arg technical, second is prose.
# \href{url}{text} likewise.
SPLIT_MACROS = {"omterm": (1, 1), "href": (1, 1), "hyperref": (1, 1)}

# The mirror image: \texorpdfstring{<typeset>}{<PDF bookmark>} keeps its FIRST
# argument and drops its second. The bookmark is a plain-text fallback that no
# reader sees on the page, and it is deliberately ASCII -- PDF outlines cannot
# carry math. Reading it as prose makes \texorpdfstring{$SO(3)$}{SO(3)} report
# "SO" as residual English. Used in 11 chapters, in every language edition.
KEEP_DROP_MACROS = {"texorpdfstring": (1, 1)}

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

# --- appended 2026-09-05 by the Biology Book 2 `hi` agent -------------------
# REASON: a biology book prints nucleotide strands and residue chains, and
# both reach the `english` class as false positives that no translator can
# remove, because they are data and are identical in every language edition.
#
#   \texttt{5'-ATGGCTTAC-3'}  ->  LATIN_WORD is greedy over "-", so the token
#       tested is 'ATGGCTTAC-', which no longer fullmatches CHEM_FORMULA (the
#       bare 'ATGGCTTAC' does). 8 sites in parts/grade-10/03-universal-dna.
#   Met--Lys--Gly--Trp        ->  a chain of three-letter amino-acid codes; the
#       hyphens defeat CHEM_FORMULA. 20+ sites in grade-11/04-gene-expression.
#
# Deliberately narrow, so nothing English can hide behind either rule:
#   * the strand rule is UPPERCASE-only and needs 5+ letters, so the ordinary
#     words spelled from A/C/G/T/U (cat, act, tag, tact, gut) stay gated, and
#     the existing "uppercase and <= 4 chars" acronym escape already covers
#     the three-letter codon spellings;
#   * the residue rule needs at least TWO codes joined by hyphens and matches
#     the exact Xxx casing, so a lone 'His' or 'Met' -- and lowercase 'his',
#     'met', 'leu' -- are still reported. A chain that still contains an
#     English word (Met--Pro--stop) is still reported, which is the point.
AMINO_CODES = {"ala", "arg", "asn", "asp", "cys", "gln", "glu", "gly", "his",
               "ile", "leu", "lys", "met", "phe", "pro", "ser", "thr", "trp",
               "tyr", "val"}
NUCLEOTIDE_STRAND = re.compile(r"[ACGTU]{5,}")
AMINO_CHAIN = re.compile(r"[A-Z][a-z]{2}(?:-+[A-Z][a-z]{2})+")


SINGLE_RESIDUE = re.compile(r"[A-Z][a-z]{2}")

# A bond drawn between element symbols in running prose: H--O--H, C--C,
# Ca--O, N--H. Deliberately narrow -- every part must be a bare element
# symbol (a capital, optionally one lower-case letter), there must be at
# least two parts and at most four, so no English hyphenated compound can
# hide behind it. 2026-09-06, biology Book 3 `hi`.
ELEMENT_CHAIN = re.compile(r"[A-Z][a-z]?(?:-{1,2}[A-Z][a-z]?){1,3}")


def is_biochemical_token(word: str) -> bool:
    """A printed nucleotide strand or amino-acid residue chain -- not prose."""
    core = word.strip("-'")
    if NUCLEOTIDE_STRAND.fullmatch(core):
        return True
    # A LONE three-letter residue code, in its exact Xxx casing. The genetic
    # code table of parts/grade-11/04-gene-expression prints all twenty of
    # them, one per cell (64 sites), and every Hindi biology textbook keeps
    # them in Latin exactly as this one does. Cost of the escape: capitalised
    # 'His', 'Met' and 'Pro' can no longer be reported on their own -- an
    # acceptable blind spot, because an untranslated English sentence
    # containing one of them carries several other words this class still
    # catches, and the lowercase forms stay gated.
    if SINGLE_RESIDUE.fullmatch(core) and core.lower() in AMINO_CODES:
        return True
    if not AMINO_CHAIN.fullmatch(core):
        return False
    return all(p.lower() in AMINO_CODES for p in re.split(r"-+", core) if p)


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
            # A trailing RELATION or BINARY OPERATOR is the same kind of
            # exemption, and it was missing. The canon's own idiom closes the
            # math on the operator and lets the operand follow outside it as
            # text or a macro -- "$\lambda_{\max}T = $ const",
            # "$k_BT\ln n(h) + mgh = $ const", "$\Delta^{++} = $ uuu". Six
            # such spans exist in the Book 5 ENGLISH source (four files), so
            # the rule fired on prose no translator may touch: id_apply's math
            # census requires the span byte-identical to English, and gate 7
            # demanded it change. That is a hard conflict between two gates,
            # not a defect -- found by the Hindi Book 5 agent, 2026-09-03,
            # and confirmed by running this gate over the English canon
            # (6 hits in 4 files, 0 after this change).
            #
            # It cannot mask the fingerprint it is looking for: MT spacing
            # damage leaves the space after an ordinary TOKEN ("$P $"), never
            # after a dangling relation, which no machine translator emits.
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
            # A non-alphabetic control sequence. The SPACING ones -- \, \; \:
            # \! \<space> \/ and \\ -- separate two words on the page, so
            # deleting them WELDS the words together and the welded token is
            # then reported as residual English: `\num{8800} kcal\,m$^{-2}$`
            # in a tikz node became the single word "kcalm" and fired the
            # `english` rule on a unit no translator may touch (Hindi Book 3,
            # 2026-09-06). Emit a space for them; every other escape
            # (\%, \&, \_, \$, \#) is a literal character and is dropped
            # as before.
            if i + 1 < n and text[i + 1] in ",;:! /\\":
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

        if name in KEEP_DROP_MACROS:
            keep, drop = KEEP_DROP_MACROS[name]
            for _ in range(keep):
                inner, j = match_group(text, skip_ws(text, j), "{", "}")
                if inner:
                    out.append(" " + nested_text(inner, depth) + " ")
            for _ in range(drop):
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
                # `key@display` is makeindex's SORT KEY followed by what is
                # actually printed. The sort key is deliberately ASCII -- it is
                # how a non-Latin or accent-initial entry is filed in the right
                # place -- and no reader ever sees it, so reading it as visible
                # text reports the canon's own `\index{pKa@p$K_a$}` as residual
                # English. Keep the display half of every `!` level.
                # 2026-09-06, biology Book 3 `hi`.
                levels = [lvl.split("@", 1)[-1] for lvl in inner.split("!")]
                out.append(" " + nested_text(" ".join(levels), depth) + " ")
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


# Transliterated English function words. Hindi has no articles, so "द"/"ए"
# standing alone are always the MT leaving *the*/*a* behind.
#
# "इन" is deliberately NOT here: it is the ordinary Hindi oblique demonstrative
# ("इन संख्याओं में" = among these numbers), not transliterated English *in*.
# Listing it forced agents to write "उन" instead and shift the meaning.
TRANSLITERATED_ARTICLES = {
    "द": "the", "ए": "a/an", "ऑफ": "of", "एंड": "and", "इज": "is",
    "आर": "are", "फॉर": "for", "विद": "with", "टू": "to",
}


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


def check_file(path: pathlib.Path, findings: list) -> None:
    raw = path.read_text(encoding="utf-8")
    rel = str(path)
    body = strip_comments(raw)
    seen = visible_text(body, findings, rel)
    _occ: dict = {}

    # 1. residual English in visible text
    for m in LATIN_WORD.finditer(seen):
        word = m.group(0)
        # LATIN_WORD accepts an apostrophe inside a token so that English
        # possessives ("Gauss's") are still caught -- but the sources quote with
        # LaTeX's ``...'' , and the closing pair welds itself to the last word
        # ("the pH of a cell''"). Strip only the OUTER apostrophes, so an
        # internal one is still tested. 2026-09-06, biology Book 3 `hi`.
        # The OUTER hyphens go the same way, and for the same reason: the
        # sources write `$5'$-ACGT-$3'$` and `DNA--protein`, where blanking the
        # math leaves the token `ACGT-` / `DNA--`. An internal hyphen is kept,
        # so `Well-Being` is still reported.
        word = word.strip("-'") or m.group(0)
        low = word.lower()
        if low in ALLOWED_WORDS or low in ALLOWED_UNITS:
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
        if is_biochemical_token(word):
            continue        # 5'-ATGGCTTAC-3', Met--Lys--Gly--Trp: see the
                            # note beside is_biochemical_token above
        if ELEMENT_CHAIN.fullmatch(word):
            continue        # H--O--H, C--C, Ca--O: a bond drawn between element
                            # symbols. Identical in every edition, and the
                            # <= 4-character uppercase escape above already
                            # passes the two-symbol forms (O--H, S--S), so
                            # only the longer chains were being reported.
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
        for m in re.finditer(rf"(?<![{DEVANAGARI}]){token}(?![{DEVANAGARI}])", seen):
            findings.append((rel, _locate(body, token, _occ),
                             "translit",
                             f"transliterated English {gloss!r}: {token!r}"))

    # 3. Latin full stop closing a Devanagari sentence (use danda ।)
    for m in re.finditer(rf"[{DEVANAGARI}][)\"'\s]*\.(?=\s|$)", seen):
        findings.append((rel, seen[:m.start()].count("\n") + 1,
                         "danda",
                         "sentence ends with '.' after Devanagari (use ।)"))

    # 5. thin space splitting a number from its noun
    for m in re.finditer(rf"[{DEVANAGARI}]\s*\\,\s*\d", body):
        findings.append((rel, body[:m.start()].count("\n") + 1,
                         "split-number",
                         "\\, between Devanagari and digits (split number?)"))


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
        if not p.is_dir():
            continue
        for f in sorted(p.glob("*.tex")):
            files += 1
            check_file(f, findings)

    if not findings:
        print(f"  hindi prose gate: OK ({files} files)")
        return 0

    by_class: dict = {}
    for rel, line, cls, msg in findings:
        by_class.setdefault(cls, []).append((rel, line, msg))

    print(f"  hindi prose gate: {len(findings)} issue(s) in {files} files")
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


if __name__ == "__main__":
    sys.exit(main())
