# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A series of five LaTeX biology books (Grades 1–9, Grades 10–12, University
Year 1, University Year 2, University Year 3) built from **one shared
`parts/` tree**, one entry file per book at the repo root, and a single
style file. The structure, theme and tooling mirror the sibling
`one-math-book` / `one-physics-book` projects (same One Course brand, same
environments, same label conventions, same term-link tooling).

Contents are **pure biology** (life sciences only), following the old
French programmes (never named in visible text): Book 1 the primaire +
collège SVT biology parts, Book 2 the lycée S SVT biology parts, Books
3–4 the two years of the BCPST classe préparatoire (biology part, union
of old and current programmes), Book 5 the rest of a licence de biologie
(L3 + L1/L2 gaps).

**Current state: Books 1, 2 and 3 written in English (2026-08-28,
2026-09-02 and 2026-09-04); Books 4–5 are titled placeholders** (chapter
architecture in place, no chapter written).

- **Book 1** (Primary & Middle School, grades 1–9): 71 chapters + 71
  solutions files. Grades 1–5 carry 10–11 exercises (★-heavy, ★★/★★★
  tail) and no weekend problem; grades 6–9 carry 12 exercises plus one
  ~12-question weekend `problem` (Parts I–III with `[resume]`), every
  exercise and problem with a keyed solution. TikZ schematics
  throughout, plus 51 AI illustrations (`images/book1/ai/`, prompts in
  `PROMPTS.md`) and 4 free-license photographs (`images/book1/`,
  records in `CREDITS.md`, credited in `frontmatter/image-credits.tex`,
  inputted by the entry file). ~7,600 generated `\omterm` links;
  `tools/term_config/book1_en.py` is curated (young-register STOP/DROP
  philosophy — regenerate with `--unwrap --apply` then `--apply` after
  editing definitions or prose). Math level guard: whole numbers only
  in grades 1–3, fractions from grade 4, percentages from grades 6–7,
  powers grade 8, chance only as "one in two/four" in grade 9.

- **Book 2** (High School, grades 10–12): 36 chapters + 36 solutions
  files, ~378 pp. Physics high-school calibration: every chapter carries
  exactly 15 exercises ramped 5×★, 6×★★, 4×★★★ in order, plus one
  ~20-question weekend `problem` (Parts I–IV with `[resume]`) ending on a
  named quantified result; every exercise and problem has a keyed
  solution. Adult, experiment-driven register: classic experiments are
  given as `\begin{proof}[Evidence]`, the rest `\admitted`. 184
  figures: TikZ/pgfplots schematics, 47 AI illustrations
  (`images/book2/ai/`, prompts in `PROMPTS.md`, overlay-label bases named
  `fig-*`) and 5 free-license photographs (`images/book2/`, records in
  `CREDITS.md`) plus 3 reused from `images/book1/`, all credited in
  `frontmatter/image-credits-book2.tex`. ~5,300 generated `\omterm`
  links; `tools/term_config/book2_en.py` is curated (STOP/DROP for the
  few ordinary-English collisions, EXTRA plurals, a protect pattern for
  "homologous chromosomes"). Math level guard: percentages, ratios,
  Punnett squares and $p^2+2pq+q^2$; no derivatives or logarithms. The
  entry file redefines `\indexspace` with more shrink — without it the
  multicol index reports two overfull columns on its last page.

- **Book 3** (University Biology, Year 1): 29 chapters + 29 solutions
  files, ~340 pp. Physics/math Year-1 calibration: every chapter carries
  exactly 12 exercises ramped 4×★, 5×★★, 3×★★★ in order, plus one
  ~25-question weekend `problem` (Parts I–IV with `[resume]`) ending on a
  named quantified result (a $K_m$, a P/O ratio, a xylem tension, a
  carrying capacity, a tree length); every exercise and problem has a
  keyed solution. University-lecture register: the quantitative laws are
  `theorem`s with Year-1 derivations (Michaelis–Menten, Nernst, logistic
  growth, the disc equation, island biogeography), classic experiments
  are `\begin{proof}[Evidence]`, the rest `\admitted`. 185 figures:
  TikZ/pgfplots schematics, 69 AI illustrations (`images/book3/ai/`,
  prompts in `PROMPTS.md`, 14 overlay-label bases named `fig-*`) and 13
  free-license photographs (`images/book3/`, records in `CREDITS.md`),
  all credited in `frontmatter/image-credits-book3.tex`. ~5,450
  generated `\omterm` links; `tools/term_config/book3_en.py` is curated
  (DROP for the cross-sense words — energy, water, plasma, matrix,
  vessel, smooth/rough, saturated, operator, resistance, epidermis, stem,
  character — STOP for "substrate", EXTRA plurals). Math level guard:
  derivatives, exp/ln, first-order ODEs, log axes; no partial
  differential equations, no matrices, no statistics beyond a mean.

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

## Language editions

**Book 1 ships in eight languages** — English plus `fr`, `nl`, `es`, `pt`,
`hi`, `ar` and `id`, all seven translated 2026-09-04, one agent per edition,
**each self-scored 96/100** under the native-academic bar. Books 2–5 are
English only.

Per-edition figures, all from forced (`-g`) builds so they are comparable:

| | pages | `\omterm` links | distinct targets |
|---|------:|-----:|-----:|
| `en` | 422 | 7,607 | 151 |
| `fr` | 457 | 7,532 | 152 |
| `es` | 453 | 7,748 | 151 |
| `pt` | 453 | 7,531 | 153 |
| `nl` | 453 | 6,451 | 151 |
| `hi` | 419 | 7,923 | 150 |
| `ar` | 396 | 6,781 | 152 |
| `id` | 467 | 8,390 | 151 |

Every edition: 0 errors, 0 undefined, 0 overfull, `nullfont` 20, 142 files in
the `.fls`, `\index` 331 in all eight, and `check_translation.sh` green for
all nine years.

**Translation found three defects in the ENGLISH canon**, which is the most
useful thing about running seven editions at once — nothing compares English
to anything, so these were invisible until a translator asked why its numbers
disagreed:
- `\emph{Sorting}` harvested CAPITALISED, so the config's lowercase
  `"sorting"` in `STOP` never reached it and
  `prop:g2:caring-for-nature:recycle` collected its only two links from the
  wrong sense (taxonomy in grade 3, a problem heading in grade 9). Found via
  the Dutch edition being one target short. English went 152 → 151 targets.
- The grade-7 double-circulation caption read "the oxygen-rich
  `\omterm{def:g1:my-body:parts}{legs}`" — legs of a *journey*, correctly read
  by six translators, but linked to the grade-1 body-parts definition and
  mistranslated as the anatomical leg by the seventh. Reworded to "stretches".
- Both are instances of the same rule: **a homograph collision can live in the
  source.** See `../translation_instruction.md`. Read the workspace-root
`translation_instruction.md` before touching any of this; it is the
authoritative procedure and it records, generically, every defect class the
math and physics runs paid for.

- **Bodies** live under `parts/<year>/<lang>/` and
  `parts/<year>/solutions/<lang>/`; `\ominput` prefers the `<lang>` file and
  falls back to English when it is missing. **A green build therefore does
  NOT prove a translation is complete** — and a *failed* `\IfFileExists`
  records nothing in the `.fls`, so latexmk cannot even see the new file.
  Build with `-g` whenever a translated file has been CREATED since the last
  build, and check the `.fls` file count against the files on disk.
- **UI strings** are in `styles/lang/<lang>.tex`; **entry files** are
  `one_biology_book_1_primary_middle_school_<lang>.tex`, each setting
  `\booklang` *before* `\usepackage{styles/onebiology}`. All are registered
  in `latexmkrc` and `.github/workflows/release.yml`.
- **Engines differ per file.** `_hi.tex` builds with XeLaTeX (OpenType
  Devanagari), `_ar.tex` with LuaLaTeX (babel `bidi=basic`), everything else
  with pdfTeX. `latexmkrc` dispatches on the source filename, not on
  `$pdf_mode` — a command-line engine flag would otherwise beat the rc file.
  Fonts are bundled under `assets/fonts/`; the Arabic faces are **static
  instances**, and nothing may go back to instancing the variable font at run
  time (it segfaults LuaHBTeX on musl, which is what CI runs).
- **`tools/id_apply.py` is how a translated body should be written.** The
  translator writes only prose, as replacements for named line ranges of the
  English twin; every unnamed line is copied byte-identically, and the write
  is refused unless labels, environments, solution keys, `\emph`/`\index`
  adjacency, math spans, drawing code, delimiters, braces and **image paths**
  all match English. The `img` census is this repo's addition: Book 1 carries
  132 raster figures, most of them outside any drawing environment where the
  `draw` census would have seen them.
- **The prose gates.** `check_translation.sh` runs them per year and language:
  gate 7 `check_hindi_prose.py` / `check_arabic_prose.py` (residual Latin in a
  non-Latin script), gate 8 `check_indonesian_prose.py` (the inverse — a
  curated list of English words that are not Indonesian words; **the list is
  subject-specific and was re-tuned for biology**, since `organ`, `protein`,
  `virus`, `vitamin`, `habitat`, `predator` and `larva` are ordinary
  Indonesian), gate 9 `check_latin_prose.py` (is this fragment byte-identical
  to its English twin?) and gate 10 `check_orphan_lines.py` (an English line
  the translation absorbed and left behind).
- **Term links are per language**: `tools/term_config/book1_<lang>.py` is
  **curated**, never a translation of `book1_en.py`, and never seeded from
  another book — a seeded `EXTRA` points at the other book's labels and ships
  as undefined references, and a seeded `EXTRA_PROTECT` masks the links you
  wanted.
- **Self-scores** live in `translation_scores/book_<N>/<lang>/translation_score.md`;
  the ship threshold is **95/100** under the native-academic bar.

Build-log gate for a language edition (`nullfont` is **20** in a healthy Book 1
build — it is a systemic artifact of the shared style file, identical in every
edition, so gate on that number and not on zero):

```sh
L=build/one_biology_book_1_primary_middle_school_<lang>.log
grep -ac '^!' $L        # 0   -- and grep -a: these logs carry non-UTF8 bytes,
grep -aci undefined $L  # 0      so a plain grep prints NOTHING instead of 0
grep -ac Overfull $L    # 0
grep -ac nullfont $L    # 20  -- a RISE above this is an accent inside \qty{}
```

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
- **Visuals follow the Visuals section of `../book_style.md`, and biology is in scope for
  all three kinds.** A TikZ schematic only where the explanation needs
  labels, structure or measured geometry; an **AI-generated illustration
  wherever the thing can simply be seen** (and alongside a schematic when
  both help); a **free-of-rights photograph** for a specific real thing a
  reader would want to see as it is — a named scientist, a landmark
  specimen, a famous organism or landscape. None of the supporting
  infrastructure exists in this repo yet: it needs `images/book<N>/` with
  `CREDITS.md`, `images/book<N>/ai/PROMPTS.md`, and an Image Credits page
  in `frontmatter/` inputted by each entry file. Copy the shape from
  `one-physics-book` (`images/book1/`, `frontmatter/image-credits*.tex`).
- Semantic colors: `omDef`, `omThm`, `omProp`, `omMeth`, `omExo`.
- Brand `oc*` colors and `\ocRosette`/`\ocQuadLine` are cover-only
  (see THEME.md).
