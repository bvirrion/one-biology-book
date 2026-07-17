# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A series of five LaTeX biology books (Grades 1–9, Grades 10–12, University
Year 1, University Year 2, University Year 3) built from **one shared
`parts/` tree**, one entry file per book at the repo root, and a single
style file. The structure, theme and tooling mirror the sibling
`one-math-book` / `one-physics-book` projects (same One Course brand, same
environments, same label conventions, same term-link tooling).

Contents are **pure biology** (life sciences only). High school (Book 2)
is written in full; other volumes have titled placeholders.

`CONTRIBUTING.md` holds the authoritative style/structure conventions;
`THEME.md` documents the One Course cover brand. Read both before writing
chapters.

## Build

```sh
make                                     # latexmk builds all books into build/
latexmk one_biology_book_2_high_school.tex   # a single book
```

The build is pdflatex via `latexmkrc` (which also raises pdfTeX memory
limits — don't bypass it). PDFs land in
`build/one_biology_book_<N>_<slug>.pdf`. There are no tests; the quality
gate is the log:

```sh
L=build/one_biology_book_<N>_<slug>.log
grep -c '^!' $L                 # errors — must be 0
grep -ci 'undefined' $L         # undefined references — must be 0
grep -c 'Overfull' $L           # overfull boxes — keep at 0
```

## Architecture

- `one_biology_book_<N>_<slug>.tex` — entry file per book (series number N):
  loads `styles/onebiology.sty`, calls `\ombrandheader` and
  `\omsolutionlinks`, defines `\bookline` ("Book N: ..." shown on the
  shared cover), inputs `parts/<year>/part.tex` for its years, then a
  Solutions appendix inputting `parts/<year>/solutions/solutions.tex`.
- `styles/onebiology.sty` — **the only place** packages are loaded and
  macros/environments defined. Chapter files never `\usepackage` or
  `\newcommand`. Language UI strings live in `styles/lang/<lang>.tex`.
- `parts/<year>/part.tex` — shared structure: `\part{\omstr{...}}` and
  `\ominput{<year>}{NN-slug}` lines; `solutions/solutions.tex` likewise
  with `\ominputsol`.
- Books → years: Book 1 → `grade-1`…`grade-9`; Book 2 → `grade-10`…
  `grade-12`; Books 3–5 → `bachelor-1`…`bachelor-3`.
- Year label prefixes: `g1`–`g12`, `b1`–`b3`. All labels are namespaced
  `<type>:<year>:<chapter-slug>:<name>`, e.g. `def:g10:the-cell:organelle`,
  exercises `exo:g12:immunity:3`, weekend problems `pb:g10:...`.
  Reference with `\cref`, never bare `\ref`.
- **Cross-volume references are prose-only** ("the Year 2 volume") —
  `\cref` to another book's label will build locally by accident and
  break that book.

## Invariants (once content is written)

Every exercise (and every weekend `problem`, label `pb:...`) has exactly
one solution, keyed by label. Per chapter:

```sh
diff <(grep -o 'label{\(exo\|pb\):[^}]*}' parts/<year>/NN-slug.tex | sed 's/label{//;s/}//') \
     <(grep -o 'begin{solution}{[^}]*}' parts/<year>/solutions/NN-slug.tex | sed 's/begin{solution}{//;s/}//')
grep -rho 'label{[^}]*}' parts/<year>/ | sort | uniq -d   # duplicate labels
```

Defined-term links (`\omterm`) are generated, not hand-written — the
engine lives in `tools/termlink/` and
`tools/term_config/book<N>_en.py`. After chapters and definitions land:

```sh
python3 tools/link_defined_terms.py --book N          # dry run
python3 tools/link_defined_terms.py --book N --apply
```

Content rules (from CONTRIBUTING.md): 8–12 exercises per chapter, graded
`[$\star$]` to `[$\star\star\star$]`, each with a full solution;
new terms introduced as `\emph{...}\index{...}` in a `definition`;
prefer diagrams over equations; SI units where relevant.

## Style notes for biology

- Prefer `proposition` / `method` / `definition` over theorem-heavy prose.
- Use `\begin{omfigure}...\end{omfigure}` around TikZ diagrams.
- Semantic colors: `omDef`, `omThm`, `omProp`, `omMeth`, `omExo`.
- Brand `oc*` colors and `\ocRosette`/`\ocQuadLine` are cover-only
  (see THEME.md).
