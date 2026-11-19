# Run file — One Biology Book 1–5 in Simplified Chinese (`zh`), pilot method

Scope: Books 1–5 (15 years: grade-1 … grade-12, bachelor-1 … bachelor-3) into Simplified Chinese (mainland), by the pilot method (`../pilot_translation_instruction.md`).
Started 2026-11-18, one run with biology Books 1–5 and Earth Books 1–5 (run 1 of 2 (biology first, then Earth)).

| **Model** | `claude-haiku-5-5` (Haiku 5.5, effort medium), pilot method: one headless call per section; glossary and coordinator `claude-opus-5-5` (Opus 5.5) |
|---|---|

Shape (user, 2026-11-18): one coordinator (the main session), no subagents, one session for both series; at most three
years (`run.py` jobs) at once and at most 9 Haiku calls in flight. **Pause rule for this run: pause and report at +25
points of the weekly plan** from the run's start (22 %, so at 47 %; points before and after a weekly reset are added).
Order: biology Books 1–5, then Earth Books 1–5.

## Usage readings (`claude -p /usage`, all models, current week)

| When | Week used |
|---|---:|
| Run start, 2026-11-18 22:03 | 22 % |
| After the trials, 2026-11-18 23:33 | 23 % |
| Biology Book 1 closed, 2026-11-19 | 23 % |
| Biology Book 2 closed, 2026-11-19 | 24 % |
| Biology Book 3 closed, 2026-11-19 | 24 % |
| Biology Book 4 closed, 2026-11-19 | 25 % |
| Biology Book 5 closed, 2026-11-19 | 26 % |
| Earth Book 1 closed, 2026-11-19 | 26 % |
| Earth Book 2 closed, 2026-11-19 | 27 % |
| Earth Book 3 closed, 2026-11-19 11:00 | 30 % |
| Earth Book 4 closed, 2026-11-19 | 30 % |
| Earth Book 5 closed, 2026-11-19 13:20 | 31 % |

## Decisions

- Glossaries: `sources/GLOSSARY_BOOK_{1..5}_ZH.md` (new lines only), `sources/GLOSSARY_OVERRIDES_ZH.md` read last. The inherited
  physics and chemistry lines gave *cell* 晶胞, *nucleus* 原子核, *translation* 平动, *base* 碱, *population* 布居数: the override
  file restores the biology sense and drops the words whose sense depends on the sentence.
- Scientific names and gene symbols stay in Latin (series card).

## Trials (2026-11-18, before the queue)

Four chapters, Haiku 5.5 at effort medium, two passes each: biology g7/04 and b1/13, Earth g8/03 and b3/01.

| Chapter | sections | call files | rejected after pass 1 | after pass 2 |
|---|---:|---:|---:|---:|
| biology g7/04 | 5 | 8 | 0 | 0 |
| biology b1/13 | 7 | 16 | 0 | 0 |
| Earth g8/03 | 5 | 18 | 1 | 1 |
| Earth b3/01 | 12 | 28 | 1 | 0 |

29 sections, 70 call files (2.4 per section), 2 rejected at pass 1 (7 %), 1 left at pass 2 (3 %). The one left (Earth g8/03, section 3,
lines 230–340) is a reply that stops at line 313: Haiku truncates a long section. It goes to `fixsec.py` with the year's other leftovers.
Fandol covers all 1,169 distinct characters used. No wrong-sense inherited term appears (极板, 纤芯, 晶胞, 布居数, 平动 and others: 0).
Weekly plan after the trials: 23 %.

## Books closed

### Book 1 (grades 1–9), closed 2026-11-19

Pilot tier 88; 396 pp; 0/0/0; missing character 0; gates green for all nine grades; 8,161 links to 150 targets (English 7,607 to 151);
448 Haiku calls, about $2.3 list price. Score file: `translation_scores/book_1/zh/translation_score.md`.

Found on the way, for the later books:
- **`tools/check_translation.sh` had the zh block pasted inside the Arabic `if`** (a fuzzy patch), a shell syntax error for every language
  in the working tree. Fixed here; Earth's copy was checked and is sound.
- **New sweep rule `trailingeq`**: Haiku glued the blank-line marker to line ends in one section.
- **`sites.py` misses a multi-line `\foreach` list**: `pdfsweep.py` found the grade 3 figure.

### Book 2 (grades 10–12), closed 2026-11-19

Pilot tier 88; 345 pp; 0/0/0; missing character 0; gates green for all three grades; 6,699 links to 102 targets (English 5,547 to 103);
374 Haiku calls, about $2.7 list price. Score file: `translation_scores/book_2/zh/translation_score.md`.

Found on the way, for the later books:
- **Symbolic chart keys stay ASCII.** A section that translates them is rejected for ever: keep the English keys and print Chinese with
  `xticklabels`/`yticklabels` after install (11 lists in this book).
- **Gate additions** in `tools/check_chinese_prose.py`: DNA and RNA sequences, genome formulas, amino-acid codes and chains, *poly-U*.
- **Fandol lacks** 鵟, 腘, 葇: write 鹰, 股后肌群, 柔荑花序.

### Book 3 (University Year 1), closed 2026-11-19

Pilot tier 88; 303 pp; 0/0/0; missing character 0; gate green; 6,605 links to 173 targets (English 5,495 to 179); 374 Haiku calls, about
$3.2 list price. Score file: `translation_scores/book_3/zh/translation_score.md`.

Found on the way, for the later books:
- **`draft/zh/baiwan.py --fix <year>`** turns *N 百万* into 万 or 亿. Run it on every university book, then check each number against the English.
- **Tables of codes:** the codon table gained Chinese amino-acid names beside the three-letter codes. Read every code table against English.
- **Fandol lacks** 鼩, 鼱, 鲀: write 尖鼠, 河豚.

### Book 4 (University Year 2), closed 2026-11-19

Pilot tier 88; 290 pp; 0/0/0; missing character 0; gate green; 4,502 links to 180 targets (English 3,093 to 155); 439 Haiku calls, about
$4.24 list price. Score file: `translation_scores/book_4/zh/translation_score.md`.

Found on the way, for the later books:
- **Most propositions here index their terms at the head of the statement:** set `INDEX_CJK = True`, then `DROP` everyday words and any key
  English links twice or less against 10 or more here (`tools/term_config/book4_zh.py`).
- **` --- ` survives in lines edited after the sweep:** run `zh_sweeps.py --fix` again after the hand fixes, on unwrapped files.
- **Fandol lacks** 鹟, 貒: write 捕蝇鸟, 美洲野猪.

### Book 5 (University Year 3), closed 2026-11-19

Pilot tier 88; 325 pp; 0/0/0; missing character 0; gate green; 3,847 links to 208 targets (English 2,672 to 188); 557 Haiku calls, about
$5.27 list price. Score file: `translation_scores/book_5/zh/translation_score.md`. **The biology series is closed: five books in `zh`.**

Found on the way, for the Earth books:
- **Merged paragraphs.** Haiku wrote a whole paragraph on one line and stopped ("lines missing"); one more call did the same.
  `draft/zh/redistribute.py HANDFIX A B TEXT` spreads a Chinese paragraph back over its English lines, never inside math or braces.
- **Labels inside drawn boxes** must stay as short as English: keep gene and protein names (*Igf2*, *Dicer*, *MutS/MutL*).
- **十亿 too:** `\num{3.2} 十亿` → 32 亿. Three sites over Books 3–5, fixed and rebuilt.
- **Fandol lacks** 鸮, 獴: write 卡卡坡鹦鹉, 猫鼬.
- The Chinese keys of a definition with a space (`非编码 RNA`, `微 RNA`) cannot link: give `EXTRA` the unspaced abbreviations (miRNA, siRNA).

## Open defects (kept on disk, cleared as fixed)

- **English canon, not fixed (no English edit in this run):** grade 12, ch. 3 and ch. 7 charts print years with a comma (1,900).
- **English canon, not fixed:** two unit-less quantities print a number with a stray unit slot: `\qty{14}{} billion hairs`
  (bachelor-1 ch. 3, line 282) and `\qty{160}{} million dollars` (bachelor-3 solutions ch. 27, line 143). Both should be `\num`.
- **Fixed 2026-11-19, after Book 4 closed:** bachelor-2 ch. 1 line 485 named the physics series in English (`One Physics Book`);
  now 物理各册. Book 4 rebuilt, 290 pp, 0/0/0.
- **Fixed 2026-11-19, after Books 1 and 5 closed; both rebuilt 11:20 (396 and 325 pp, 0/0/0):** two bare `%` signs after a number, which LaTeX
  reads as a comment. Grade 9 ch. 4 line 203 (`在 99% 共享的位点上能确立什么？`) lost the rest of its question in print, and
  bachelor-3 ch. 13 line 450 (`的 8%` at a line's end) printed 8 without its sign. Both are now `\%`. `zh_sweeps.py` only caught
  a `%` directly before Chinese text; it now also allows a space before it, or the end of the line.

## Per-book log
