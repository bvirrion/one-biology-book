# Translation score: One Biology Book 4, Simplified Chinese (`zh`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 4 (University Year 2), `one_biology_book_4_university_year_2_zh.tex` |
| **Language** | Simplified Chinese (`zh`), mainland textbook usage |
| **Overall score** | **88 / 100**, sampled: 20 passages (seed 1) and three chapter openings (ch. 1, 12, 22), not read in full |
| **Ship status** | **Pilot tier**: gates green; not read sentence by sentence; figures checked by script and on contact sheets; solutions not recomputed |
| **Date** | 2026-11-19 |
| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section, 439 calls (translation, retries and repairs); glossary, infrastructure and coordinator `claude-opus-5-5` (Opus 5.5) |
| **Canon** | English as committed; no English edit |
| **Tokens** | Haiku: 439 calls, about $4.24 list price (`draft/pilot-bachelor-2-zh/post.log`). Weekly plan (all models): 25 % at this book's close. |
| **Scope** | 27 chapters + 27 solution files under `parts/bachelor-2/zh/` and `parts/bachelor-2/solutions/zh/` |

## Verdict

Accurate university-level Chinese with the standard vocabulary (减数分裂, 每搏输出量, 动作电位, 遗传漂变). Some long sentences keep the
English clause order. The sample found two faults of sense, both fixed: *soma* written 胞体 (cell body) for 体细胞, and an exercise whose
question had absorbed its premise (ch. 12).

## Build and gates

- `build/one_biology_book_4_university_year_2_zh.pdf`: 290 pp (English 321). XeLaTeX + xeCJK, Fandol, TeX Live 2026. Errors 0, undefined 0,
  overfull 0, nullfont 0, missing character 0, invalid-in-math 0, zero-height 0. The `.fls` lists all 54 translated files.
- `tools/check_translation.sh bachelor-2 zh`: PASSED, the Chinese prose gate included.
- Term links: a dry run inserts 0. 4,502 links to 180 targets (English 3,093 to 155). Chinese links more because one short word covers
  what English spreads over several forms (动脉, 突变, 等位基因).
- Nine targets English reaches are not linked here, 17 English links in all. The largest is `thm:b2:blood-circulation:poiseuille` (4).
- 351 exercises and problems, 351 solutions; no duplicate label.
- `pdfsweep.py` against the French PDF: only *cAMP*, *mRNA*, *cDNA*, *FGFs*, *kisspeptin*, the subscript *cal*, the title *One Physics Book* and the licence URL remain.
- `figcheck.py lint`: 0 label collisions. 63 figures seen on five contact sheets.

## Numbers

Every line of the number trace was read. The differences are number words written as digits, lines shifted within a paragraph, decades
written 20 世纪 60 年代, and millions written 万 or 亿. Seven figures written *N 百万* were converted and checked against the English.
*百万年* stays as a unit after a computed result in the solutions of ch. 24 (`$35 \pm 5$ 百万年`).

## Defects found and fixed, by class

| Class | Count | Example | Fix |
|---|---:|---|---|
| `\foreach` label lists in English | 24 lists | meiosis stages, sliding-filament steps, tropism experiments | Translated |
| Chart key printed in English | 1 chart | `symbolic x coords={brain, heart, …}` | Keys kept, Chinese printed through `xticklabels` |
| Last English line left after the sentence | 2 | `destabilised?`, `question 4 is kept?` | Sentence re-split |
| English left in prose or subscripts | about 40 | `\text{in}`, `stylopod`, `xenia` | Translated |
| Wrong or missing species name | 1 pair | pied flycatcher written 领姬鹟 | 斑捕蝇鸟, 白领捕蝇鸟 |
| Glyphs missing from Fandol | 8 | 鹟, 鼩鼱, 貒 | 捕蝇鸟, 尖鼠, 美洲野猪 |
| ASCII dash left in Chinese lines | 16 lines | ` --- ` | —— |
| Doubled word across a line break | 2 | 舒张压为 / 为 | One removed |
| ASCII brackets in figure labels | 6 | `时间 (s)` | Full width |

Seven sections stayed rejected after three passes (ch. 3, 4, 5, 13, 18, 21 and 24) and were finished by hand or by one more call.
