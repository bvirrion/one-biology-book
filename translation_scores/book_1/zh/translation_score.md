# Translation score: One Biology Book 1, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 1 (Primary / Middle, grades 1–9), `one_biology_book_1_primary_middle_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (6 from grade 2, 7 from grade 5, 7 from grade 8), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all) and on one contact sheet (the 6 drawn figures the script detects) |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 448 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit. |
| **Tokens** | Haiku: 448 calls, about $2.3 list price (per year in `draft/pilot-grade-*-zh/post.log`). Weekly plan (all models): 22 % at the run's start, 23 % at this book's close. |
| **Scope** | 71 chapters + 71 solution files under `parts/grade-{1..9}/zh/` and `parts/grade-{1..9}/solutions/zh/`; preface `frontmatter/preface.zh.tex`; credits `frontmatter/image-credits.zh.tex` |

## Verdict

Natural mainland schoolbook Chinese: short, warm sentences in the young grades, a plain textbook register from grade 6.
Clauses are reordered across lines as Chinese needs. Biology terms are the standard ones. Weak points: a few images kept
too literally from English (the "checks" that collect a fish's eggs, 检查几乎将其全部收走) and some long sentences in
English clause order. No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_biology_book_1_primary_middle_school_zh.pdf`: 396 pp (English 422). XeLaTeX + xeCJK, Fandol, TeX Live 2026.
  Errors 0, undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all
  142 translated files. Pinyin index (upmendex): 297 entries.
- `tools/check_translation.sh grade-N zh`: PASSED for N = 1…9, the Chinese prose gate included.
- `link_defined_terms.py --book 1 --lang zh --check`: every file matches; a dry run inserts 0. 8,161 links to 150 targets
  (English 7,607 to 151).
- Targets English reaches and this edition does not: `prop:g3:bones-and-muscles:joints` (6 English links; 关节 is harvested
  for the grade 1 definition) and `prop:g5:people-and-nature:managed` (2 English links; 森林 and 田地 are stopped).
- Every exercise and problem has one solution, in order; no duplicate label.
- `pdfsweep.py` against the French PDF: 1 English-only word type left, intended (*licenses* in the licence URL).
- `figcheck.py lint`: 0 label collisions.

## What was read

- Text: 20 passages (seed 1), the sweep, number and PDF-sweep reports, every gate hit.
- Numbers: every NUMDIFF line traced. Number words written as digits or moved between lines; one real sense error fixed (below).

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Last English line left after the sentence was finished above it | 9 | `grown-ups.`, `magnifications` | Sentence re-split over the two lines |
| Blank-line marker glued to a line end | 26 | `\end{exercise}=` (one section; killed the build) | New `zh_sweeps.py` rule `trailingeq` |
| Figure labels left in English in a `\foreach` list | 3 figures | `0/insects/{6 legs}` | Translated |
| Headings left in English | 3 | `[How fast, how slow]`, `Part II --- The consumers' floor` | Translated |
| Glyph missing from Fandol | 9 | 鵟 (buzzard) | 鹰, as the course text; noted in the series card |
| Index key lost its sense | 3 | `\emph{溶解}\index{溶解}` for *dissolved oxygen* | Key restored (溶解氧, 作物, 家畜) |
| Wrong sense | 1 | *five points* (of oxygen) as 5 分 | 5 个百分点 |
| Doubled word over a line break | 1 | 请将 / 将每项 | Removed |
| Onomatopoeia left in Latin | 6 | *lub-dub* | “咚—嗒” |

One section (grade 3, chapter 7, section 2) stayed rejected after three passes, the reply cut off; it was finished by hand.
