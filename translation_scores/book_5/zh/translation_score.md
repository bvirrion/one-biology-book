# Translation score: One Biology Book 5, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 5 (University Year 3), `one_biology_book_5_university_year_3_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages (seed 1) and three chapter openings (ch. 4, 12, 26), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 557 calls (translation, retries and repairs); glossary, infrastructure, hand-finished sections and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 557 calls, about $5.27 list price (`draft/pilot-bachelor-3-zh/post.log`). Weekly plan (all models): 26 % at this book's close. |
| **Scope** | 27 chapters + 27 solution files under `parts/bachelor-3/zh/` and `parts/bachelor-3/solutions/zh/` |

## Verdict

Accurate university-level Chinese with the standard vocabulary (表观遗传, 剪接体, 适应性免疫, 广义适合度). Some long sentences keep the
English clause order. The sample found one fault of sense, now fixed: a caption read *geometric approach* as a method (几何方法) instead of
a curve that approaches its limit. Two more were found outside the sample and fixed: exercise 4.6 asked why the *standard deviation* is
30× where English asks why 30× coverage is the standard, and one sentence repeated *per division*.

## Build and gates

- `build/one_biology_book_5_university_year_3_zh.pdf`: 325 pp (English 365). XeLaTeX + xeCJK, Fandol, TeX Live 2026. Errors 0, undefined 0,
  overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 54 translated files.
- `tools/check_translation.sh bachelor-3 zh`: PASSED, the Chinese prose gate included.
- Term links: a dry run inserts 0. 3,847 links to 208 targets (English 2,672 to 188).
- Five targets English reaches are not linked here, 8 English links in all. The largest have 2 each.
- 351 exercises and problems, 351 solutions; no duplicate label.
- `pdfsweep.py` against the French PDF: only RNA and DNA abbreviations (*mRNA*, *siRNA*, *piRNA*), *IUCN*, *cAMP*, gene, protein and drug
  names, and the licence URL remain.
- `figcheck.py lint`: 0 label collisions after one fix. 70 figures seen on five contact sheets.

## Numbers

Every file of the number trace was read. The differences are number words written as digits, decades written 20 世纪 70 年代, and millions
or billions written 万 or 亿. Six figures written *N 百万* or *N 十亿* were converted and checked against the English.

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| `\foreach` label lists in English | 13 lists | repair steps, Drosophila segmentation, olfactory receptors | Translated |
| Chart keys printed in English | 3 charts | `symbolic y coords={histone H4, …}` | Keys kept, Chinese printed through `xticklabels`/`yticklabels` |
| Figure labels too long for their boxes | 7 | `\emph{胎儿生长因子}` for *Igf2*, `Dicer 酶` | Gene and protein names as in English |
| English left in prose, index or subscripts | about 40 | `\index{beta 折叠}`, `（washout）`, `A_{\text{thr}}` | Translated; rate-constant subscripts *on*, *off*, *crit*, *inh* set upright |
| Glyphs missing from Fandol | 13 | 鸮, 獴 | 卡卡坡鹦鹉, 猫鼬 |
| Millions and billions in English word order | 6 | `\num{3.2} 十亿个碱基对` | 32 亿个碱基对 |
| ASCII dash left in Chinese lines | 66 lines | ` --- ` | —— |
| ASCII brackets in figure labels | 3 | `\\(\qty{150}{mV} 驱动)` | Full width |
| Doubled word across a line break | 1 | 其 / 其 | One removed |

Seven sections stayed rejected after three passes (ch. 2 ×2, 4 ×2, 9, 19 and 21). Two passed with one more call. Five were finished by
hand: in three of them Haiku had written whole paragraphs on one line and left the rest in English.
