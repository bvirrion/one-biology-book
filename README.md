# One Biology Book

<p align="center">
  <a href="https://www.one-course.com">
    <img src="assets/one-course-logo.svg" alt="One Course — one-course.com" width="420">
  </a>
</p>

*The One Biology Book to Rule Them All.*

> **One Biology Book** is part of the **One Course** project — one coherent
> course covering each subject from kindergarten to the end of the bachelor's
> degree. Discover the whole project at
> **[www.one-course.com](https://www.one-course.com)**.

A series of biology books, written in English for readers anywhere in the
world, with the ambition of covering everything **from kindergarten to
the end of the bachelor's degree** — as one coherent course, published in
several volumes:

1. **Primary & Middle School Biology** — Grades 1–9;
2. **High School Biology** — Grades 10–12;
3. **University Biology — Year 1**;
4. **University Biology — Year 2**;
5. **University Biology — Year 3**.

The course is **pure biology** (life sciences only: cell, genetics,
evolution, physiology, ecology, immunity, and so on — no geology or Earth
science). The first two volumes are fully written; the university
volumes exist as titled chapter placeholders, with the full five-book
architecture in place.

The style is concise and rigorous: courses built from **definitions,
examples, propositions, methods and diagrams**, with careful reasoning
whenever it is accessible at the given level (results admitted without
derivation are explicitly marked), followed by graded **exercises with full
solutions** collected at the end of each book. Biology chapters are rich
in **TikZ figures**; equations stay sparse.

## Current status

| Book | Level | Status |
|------|-------|--------|
| Primary & Middle School | Grades 1–9 | ✅ written in English (71 chapters, exercises, solutions, figures) |
| High School | Grades 10–12 | ✅ written in English (36 chapters, exercises, weekend problems, solutions, figures) |
| University Year 1–3 | Bachelor | 🚧 structure (29 + 27 + 27 chapter placeholders) |

## Building the books

Requirements: a TeX Live installation with `latexmk` (packages used:
`tcolorbox`, `pgfplots`, `amsthm`, `cleveref`, `imakeidx`, `siunitx`, …).

```sh
make            # or just: latexmk — builds all books
```

The PDFs are produced at

```
build/one_biology_book_1_primary_middle_school.pdf
build/one_biology_book_2_high_school.pdf
build/one_biology_book_3_university_year_1.pdf
build/one_biology_book_4_university_year_2.pdf
build/one_biology_book_5_university_year_3.pdf
```

`make clean` removes auxiliary files, `make distclean` removes the whole
`build/` directory. To build a single book, e.g.\
`latexmk one_biology_book_2_high_school.tex`.

## Repository layout

```
one_biology_book_<N>_*.tex   entry file per book (N = series number)
styles/onebiology.sty        packages, theorem environments, macros
styles/lang/<lang>.tex       UI strings (en for now)
frontmatter/                 title page, preface (shared layout)
parts/<year>/part.tex        shared structure for a school year
parts/<year>/NN-*.tex        English chapter
parts/<year>/solutions/      solutions, one file per chapter
```

## Contributing

Contributions are welcome — new chapters and years, corrections, better
diagrams, additional exercises. Please read
[CONTRIBUTING.md](CONTRIBUTING.md) for the structure, environments and
style conventions of the project.

## Contributors

- Benjamin Virrion
- Fable 5 (Anthropic's Claude)

## License

Not yet decided.
