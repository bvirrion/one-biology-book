# Contributing to One Biology Book

Thank you for contributing! This document describes the structure of the
project and the conventions that keep the book coherent.

## Project structure

The project is a **series of books** sharing one style and one `parts/`
tree. Each book has its own entry file at the repository root:

- `one_biology_book_1_primary_middle_school.tex` — Book 1, Grades 1–9;
- `one_biology_book_2_high_school.tex` — Book 2, Grades 10–12;
- `one_biology_book_3_university_year_1.tex` — Book 3, Bachelor Year 1;
- `one_biology_book_4_university_year_2.tex` — Book 4, Bachelor Year 2;
- `one_biology_book_5_university_year_3.tex` — Book 5, Bachelor Year 3.

Naming: `one_biology_book_<N>_<slug>[_<lang>].tex` → PDF
`build/one_biology_book_<N>_<slug>[_<lang>].pdf`. The English edition is
canonical; translated editions can be added later with the same mechanism
as in `one-math-book`.

The shared files:

- `styles/onebiology.sty` — **the only place** where packages are loaded and
  macros/environments are defined. Chapter files must not use `\usepackage`
  or define commands.
- `styles/lang/<lang>.tex` — UI strings for each language (`en` for now).
- `frontmatter/` — title page, colophon, preface.
- `parts/<year>/part.tex` — `\part` via `\omstr{...}` and `\ominput`s.
- `parts/<year>/NN-slug.tex` — English chapter (canonical).
- `parts/<year>/solutions/NN-slug.tex` — English solutions.

**Cross-volume references:** `\cref` only works within one book. Never
reference a label that lives in another book; name the volume in prose
instead.

## Building

```sh
make          # runs latexmk (pdflatex), builds every book into build/
```

A single book: `latexmk one_biology_book_2_high_school.tex`.

A pull request must build with **zero errors** and introduce no undefined
references.

## Environments

| Environment | Use for |
|---|---|
| `definition` | new notions; put the defined term in `\emph{...}` and `\index{...}` it |
| `theorem` / `proposition` / `lemma` / `corollary` | laws and results (prefer proposition in biology) |
| `method` | step-by-step recipes |
| `example`, `remark`, `notation` | worked examples, comments |
| `proof` | derivations when useful; otherwise `\admitted` |
| `exercise` | end-of-chapter exercises, difficulty `[$\star$]` to `[$\star\star\star$]` |
| `problem` | weekend multi-part problem set; label `pb:<year>:<slug>:1` |
| `solution` | `\begin{solution}{exo:...}` keyed to the exercise label |

## Style rules

1. **Rigor**: state precisely; mark admitted results with `\admitted`.
2. **Concision**: no filler. An example after each substantial definition;
   a `method` box for each standard technique; **many diagrams**.
3. **Exercises**: 8–12 per chapter, graded; **every exercise must have a
   full solution**. Prefer a weekend `problem` on substantive chapters.
4. **English text** for an international audience; no curriculum jargon
   (no “BAC”, “AP”, “SVT”) in student-facing text.
5. Equations only when they clarify; never as decoration.

## Labels

All labels are namespaced: `<type>:<year>:<chapter-slug>:<name>`.

- Chapters: `ch:g12:immunity`
- Statements: `def:g10:the-cell:organelle`, `prop:...`, `met:...`, `ex:...`
- Exercises: `exo:g12:immunity:3`
- Weekend problems: `pb:g10:scientific-biology:1`

Year prefixes: `g1`–`g12`, `b1`–`b3`.

Cross-reference with `\cref{...}`, never bare `\ref`.

## Workflow

1. Fork / branch.
2. Write or edit chapter + solutions files.
3. `make` and check the log for errors and undefined references.
4. Open a pull request.

## Licensing of contributions

One Biology Book is free for everyone under the licences in the [README](README.md#license). Contributing
means agreeing to the following.

1. **Same licence in as out.** Your contribution is licensed under the same terms as the part of the
   repository it changes: CC BY-NC-SA 4.0 for book content ([`LICENSE`](LICENSE)), MIT for the
   software — `tools/`, `.github/`, the `Makefile` and the build scripts ([`LICENSE-CODE`](LICENSE-CODE)).
2. **Sign off every commit** with `git commit -s`, which adds a line such as
   `Signed-off-by: Your Name <you@example.com>`. It certifies the
   [Developer Certificate of Origin 1.1](https://developercertificate.org): you wrote the change or
   have the right to submit it. For this project, "the open source license indicated in the file"
   in the certificate means the licences named in point 1.
3. **Relicensing grant.** You grant Benjamin Virrion a perpetual, worldwide, non-exclusive,
   royalty-free and irrevocable right to use, modify and relicense your contribution under other
   terms, including commercial ones (print editions, licences for schools, publishers or companies,
   paid app versions). You keep the copyright in your contribution and may use it as you wish.

**By signing off your commits you certify the DCO and agree to this whole section, including the
relicensing grant in point 3.** Why the grant exists: the books stay free under CC BY-NC-SA for
every reader; the grant only lets the author fund the project through commercial editions without
having to trace and ask every past contributor. Commits without a sign-off cannot be merged.
