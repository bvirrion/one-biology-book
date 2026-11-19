# Translation score: One Biology Book 3, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 3 (University Year 1), `one_biology_book_3_university_year_1_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages (seed 1) and three chapter openings (ch. 4, 13, 26), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 374 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 374 calls, about $3.2 list price (`draft/pilot-bachelor-1-zh/post.log`). Weekly plan (all models): 24 % at this book's close. |
| **Scope** | 29 chapters + 29 solution files under `parts/bachelor-1/zh/` and `parts/bachelor-1/solutions/zh/` |

## Verdict

Accurate university-level Chinese with the standard vocabulary (糖酵解, 克雷布斯循环, 过渡态, 环境容纳量). The prose follows Chinese order
in most sentences; some long ones keep the English clause order. No sentence in the sample was wrong in sense. One chapter opening
had a stray 但, now removed.

## Build and gates

- `build/one_biology_book_3_university_year_1_zh.pdf`: 303 pp (English 339). XeLaTeX + xeCJK, Fandol, TeX Live 2026. Errors 0, undefined 0,
  overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 58 translated files.
- `tools/check_translation.sh bachelor-1 zh`: PASSED, the Chinese prose gate included.
- Term links: a dry run inserts 0. 6,605 links to 173 targets (English 5,495 to 179).
- Eleven targets English reaches are not linked here. The largest are `def:b1:respiration-fermentation:pdh` (*acetyl-CoA*, 26 English links)
  and `def:b1:nucleic-acids:rnas` (14). No `EXTRA` was added for them.
- Every exercise and problem has one solution, in order; no duplicate label.
- `pdfsweep.py` against the French PDF: only *tRNA*, *mRNA*, *rRNA*, *cAMP*, *omega* and the licence URL remain.
- `figcheck.py lint`: 0 label collisions after one fix. 57 figures seen on five contact sheets.

## Numbers

Every NUMDIFF line was traced. The differences are number words written as digits, lines shifted within a paragraph, and *Year 2 volume*
written 二年级. Ten figures written *N 百万* were converted to 万 and checked one by one against the English.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| Chart keys left in English | 7 charts | `symbolic y coords={heart muscle, …}` | Keys kept, Chinese printed through `xticklabels`/`yticklabels` |
| `\foreach` label lists in English | 3 figures | Krebs intermediates, mitosis phases, ribosome steps | Translated |
| Chinese inserted into the codon table | 6 cells | `亮 Leu`, `\textbf{甲硫}` | Three-letter codes restored |
| Millions in English word order | 10 | `\num{9} 百万种` | 900 万种 |
| Glyphs missing from Fandol | 11 | 鼩鼱, 鲀 | 尖鼠, 豚 |
| Label collision in a figure | 1 | operon gene names | *lacI*, *lacZ*, *lacY*, *lacA*, as English |
| English left in prose | about 15 | `cell wall`, `creosote bushes`, `pin cherry` | Translated |

Three sections stayed rejected after three passes (ch. 4, 15 and 21). One was translated again by one more call; two were finished by hand.
