# Translation score: One Biology Book 2, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 2 (High School, grades 10–12), `one_biology_book_2_high_school_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages, seed 1 (7 from grade 10, 7 from grade 11, 6 from grade 12), plus three chapter openings; not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script (all) and on contact sheets (57 drawn figures) |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 374 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit. One open English defect is listed below. |
| **Tokens** | Haiku: 374 calls, about $2.7 list price (per year in `draft/pilot-grade-1*-zh/post.log`). Weekly plan (all models): 22 % at the run's start, 24 % at this book's close. |
| **Scope** | 36 chapters + 36 solution files under `parts/grade-{10..12}/zh/` and `parts/grade-{10..12}/solutions/zh/`; credits `frontmatter/image-credits-book2.zh.tex` |

## Verdict

Plain, accurate high-school Chinese with the standard biology vocabulary (有丝分裂, 等位基因, 复制叉, 视交叉). Sentences are reordered
as Chinese needs, and large numbers are converted correctly into 万 and 亿. Weak point: some long sentences keep the English
clause order. No sentence in the sample was wrong in sense.

## Build and gates

- `build/one_biology_book_2_high_school_zh.pdf`: 345 pp (English 379). XeLaTeX + xeCJK, Fandol, TeX Live 2026. Errors 0,
  undefined 0, overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 72 translated
  files. Pinyin index (upmendex): 175 entries.
- `tools/check_translation.sh grade-N zh`: PASSED for N = 10, 11, 12, the Chinese prose gate included.
- `link_defined_terms.py --book 2 --lang zh --check`: every file matches; a dry run inserts 0. 6,699 links to 102 targets
  (English 5,547 to 103). The surplus is real occurrences: Chinese repeats 细胞, 染色体 and 突变 where English uses a pronoun.
- Targets English reaches and this edition does not: `prop:g12:adaptive-immunity:tcells` (10 English links),
  `prop:g11:becoming-male-female:hormones` (6), `def:g11:dna-replication:replication` (3), and two antibiotic-resistance
  propositions (2 each). 睾酮 and 耐药 are stopped on purpose: unstopped they made 54 and 112 links against 6 and 2 in English.
  `T 细胞` and `DNA 复制` did not link when tried as `EXTRA` entries, so those two targets stay unlinked.
- Every exercise and problem has one solution, in order; no duplicate label.
- `pdfsweep.py` against the French PDF: only *mRNA*, *tRNA*, *Escherichia*, the licence URL and a credit's *Museum* remain.
- `figcheck.py lint`: 0 label collisions after one fix.

## What was read

- Text: 20 passages (seed 1), three chapter openings (g10/06, g11/05, g12/08), the sweep, number and PDF-sweep reports, every gate hit, four contact sheets.
- Numbers: every NUMDIFF line traced. Differences are million-scale numbers converted to 万 and 亿 (320 million → 3.2 亿) and
  number words written as digits; none lost.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Chart keys and labels left in English | 11 tick-label lists, plus `\foreach` lists and one table | `symbolic x coords={human, yeast, …}`, `{0/{generation 0}, …}` | Keys kept, Chinese printed through `xticklabels`/`yticklabels`, lists and one table translated |
| Last English line left after the sentence was finished above it | not counted | `holds glycogen.` | Sentence re-split over the two lines |
| Glyphs missing from Fandol | 9 | 腘绳肌, 葇荑花序 | 股后肌群, 柔荑花序 |
| Label collision in a figure | 1 | 促卵泡激素、黄体生成素 over 雌激素 | FSH、LH, GnRH, as English |
| English left in prose or math | 6 | `10^6$ bacteria`, `F_{\text{muscle}}` | Translated |
| Year axis printed with a thousands comma | 2 charts | 1,900 | Separator removed in this edition |

Two sections stayed rejected after three passes (g11 ch. 12, g12 ch. 14) and were finished by hand with `fixsec.py`.

## Open

- **English canon, year axes:** two grade-12 charts print years with a comma in English (1,900, 1,925 …): ch. 3 (peppered moth) and
  ch. 7 (wheat yield). This edition is fixed; the English source is unchanged, and the other editions were not checked.
