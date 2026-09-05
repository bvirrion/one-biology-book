# Translation score — Biology Book 2 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 2 (High School, grades 10–12) |
| **Language** | Modern Standard Arabic (`ar`) |
| **Quality bar** | **native academic prose** (English is the source of truth for content and labels; the register exemplar is this repo's own shipped `ar` edition of **Biology Book 1** — same series, same apparatus, one school level below — and the terminology reference is ordinary Arabic SVT / علوم الحياة والأرض usage at lycée level) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-05 |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 36 chapters + 36 solution twins (**72 bodies**) for grades 10, 11 and 12; a curated `tools/term_config/book2_ar.py`; the defined-term link layer; six append-only extensions to `tools/check_arabic_prose.py`; then this score. |

## Verdict in one line

An Arabic high-school biology volume that reads as though it had been written
in Arabic for الصف العاشر إلى الثاني عشر — experiment-driven, impersonal in the
course text and imperative in the exercises — with terminology continuous with
the `ar` edition of Book 1, and with every structural, build and link-hygiene
gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, measured across all 72 files: **540 `exercise` EN / 540 AR**, **36 `problem` / 36**, **576 `\begin{solution}` / 576**, **108 `[resume]` / 108**, **184 `omfigure` / 184**, **136 `tikzpicture` / 136**, **720 `\node` / 720**, **56 `\includegraphics` / 56**, **1 186 `\qty` / 1 186**, **94 `\admitted` / 94**, **543 `\emph{` / 543**, **182 `\index{` / 182**, **23 `\legend{` / 23**, **1 013 `\label{` / 1 013**, **148 `\cref{` / 148**. `\label` set diff = **0 lines**; per-file `\index` count diff = **0 files** |
| Terminology | **96** | Lycée-level Arabic biology, chosen for continuity with the `ar` Book 1: *مورّثة، أليل، صبغي، صبغيد، الانقسام المتساوي/المنصّف، التصالب، التوزع المستقل، جمهرة، الانتقاء الطبيعي، الانسياق الوراثي، الانتواع، الفرع الحيوي، الشجرة التطورية، النسغ الناقص/الكامل، الخشب واللحاء، الثغر، الانتحاء، البلاستيدة الخضراء، التيلاكويد، الحشوة، دورة كالفن، المتقدرة، المادة الأساسية، دورة كريبس، السلسلة التنفسية، سكر الدم، الأنسولين، الغلوكاغون، جزر البنكرياس، المناعة الفطرية/التكيّفية، البلعمة، البالعة، المستضد، اللمفاوية، الجسم المضاد، مناعة القطيع، العصبون، المشبك، كمون العمل، الناقل العصبي، القشرة الحركية، السبيل القشري النخاعي*. Four homograph splits were held for the whole volume (see below). DNA / RNA / ATP / NADP / HIV kept in Latin, as Book 1 `ar` ships them. Unit symbols and all `siunitx` markup byte-identical to English; **0 non-ASCII characters inside `\qty` / `\qtyrange` / `\unit` / `\num`** |
| Register / tone | **96** | MSA throughout; course text impersonal and experiment-driven (`\begin{proof}[شواهد]` for the classic experiments), exercise stems in the singular masculine imperative (*عرّف، صنّف، احسب، فسّر، قارن، اذكر، تنبأ، برهن، طبّق*), weekend problems in the same voice as Book 1's. Arabic comma `،`, semicolon `؛` and question mark `؟` throughout; Latin full stop, as `arabic_style_card.md` §6 requires |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, `nullfont` 0, 0 `invalid in math mode`, 0 `Missing character`** — all measured with `grep -a`. **3 overfull boxes remain, all three in `frontmatter/image-credits-book2.ar.tex`, which this edition does not own** (see *Requests to the orchestrator*); every overfull box in the 72 owned bodies was cleared, 13 → 0. **0 tatweel (U+0640)**, 0 bidi control characters, 0 Arabic presentation forms, 0 Arabic-Indic digits |
| Cross-refs / rule compliance | **99** | `\label`, `\cref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English. No curriculum, programme or country name anywhere in visible text |
| Figures | **97** | All TikZ / pgfplots drawing code byte-identical — coordinates, axis options, colours untouched; only node text, axis labels, `\legend{}` entries and `{\small …}` captions localized. The two classes the `draw` census freezes by design were translated as targeted post-write edits, never as a file-wide `!draw` opt-out: **8 `symbolic x/y coords` + matching `addplot coordinates` pairs** and **2 `\foreach` visible-label lists**. Every `\legend{}` entry is individually braced, so the ASCII comma stays a separator |
| Solutions | **96** | All 540 exercise solutions and all 36 weekend-problem solutions present and native; headers `\section*{الفصل \ref{ch:…} --- <العنوان>}` with the `ch:…` slug unchanged. Numeric answers, unit strings and math spans byte-identical to English |
| Defined-term links (`\omterm`) | **95** | **4 831 links over 103 distinct targets**, against English's **5 547 over 103** — 87.1 % density on an identical target count. Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies. Both homograph censuses run after the last prose edit (below) |
| MT-artifact freedom | **97** | `check_arabic_prose.py`: **0 findings in any of its nine classes** across all 72 files. `check_orphan_lines.py` and the eight other structural gates: clean for grade-10, grade-11 and grade-12. `\text{…}` census over course **and** solutions: 9 of 9 translated (*عضلة، حمل، طاقة، ضوء، يخضور*). Line-end elision, orphan-punctuation and split-hyphen greps: 0 hits |

**Overall: 96** (weighted toward terminology + register + MT-artifact freedom;
structure is already gated mechanically).

## Structural / build gates

Measurement note: the LuaLaTeX log carries non-UTF-8 bytes, so a plain
`grep -c '^!'` treats the file as binary, prints nothing and exits 1 — which
reads exactly like a pass. Every figure below was taken with `grep -a`.

```
build/one_biology_book_2_high_school_ar.log
  errors            0
  undefined         0
  Overfull          3   (all three in frontmatter/image-credits-book2.ar.tex)
  nullfont          0
  invalid in math   0
  Missing character 0
  pages           344   (English 379)
build/one_biology_book_2_high_school_ar.fls
  parts/grade-1*/ar files   72   (= the 72 on disk)
```

`bash tools/check_translation.sh grade-10 ar`, `grade-11 ar`, `grade-12 ar`:
**TRANSLATION GATE: PASSED** for all three years.

The build was forced (`latexmk -g`) on every pass in which a translated file
had been created, and the `.fls` count checked against the files on disk each
time — a plain build cannot see a file that `\IfFileExists` did not find on the
previous run, so a green build is not evidence of a complete translation.

## How the bodies were written

Every one of the 72 bodies was written through `tools/id_apply.py` as named
line-range replacements on the English twin, so that all twelve refusal
censuses (`labels envs solutions emph index math draw img delims braces omterm
prose`) ran on every file. **No file used `!math`, `!draw` or any other
whole-file opt-out.** The two classes of visible text the `draw` census freezes
by design — `symbolic x/y coords` together with the `addplot coordinates` that
must match them, and `\foreach` label lists — were translated afterwards with a
checked exact-string replacer that refuses unless each old string occurs exactly
once.

A single-chapter probe build (`lualatex` on one chapter plus the book preamble)
was run before drafting to confirm that **Arabic strings work as pgfplots
`symbolic x coords` and inside `addplot coordinates`** under `bidi=basic`; that
de-risked eight figures before the prose was written.

`styles/onebiology.sty` and `styles/lang/ar.tex` were not touched.

## Terminology decisions worth recording

Four homograph splits held across the whole volume:

- **لقاح = vaccine only.** Pollen is **غبار الطلع** everywhere (chapters 6, 7,
  11 and 12 and their solutions), because *لقاح* is the ordinary Arabic word
  for both and chapter 12 defines it as the vaccine. The one occurrence of
  *حبوب لقاح* already shipped in grade-11's solutions was changed to *حبوب طلع*
  for the same reason.
- **الحشوة = the chloroplast stroma; المادة الأساسية = the mitochondrial
  matrix.** Both are *الحشوة* in ordinary Arabic usage; keeping them apart
  keeps chapters 8 and 9 legible side by side.
- **الجسم المضاد = antibody**, never *ضد* — which is also the preposition
  *against*, and would have produced sentences reading "antibody antibody".
  Four occurrences of the synonym *أضداد* introduced in an early draft were
  normalised.
- **جزر غالاباغوس rewritten as a genitive** in chapter 3, so that *الجزر*
  (islands) never collides with *الجزر* (the islets of the pancreas), which
  chapter 10 defines.

One spelling was normalised across the whole edition after the fact: **إنزيم**
(112 occurrences) against **أنزيم** (28), which had crept into the grade-12
files; the shipped grade-10/11 spelling won.

## Defined-term links

`tools/term_config/book2_ar.py` was curated from **this edition's own harvest**
(228 terms, 312 keys) and never seeded from `book1_ar.py`; `NOT_A_TERM` is left
unset, as the brief requires. `tools/termlink/morphology.py`'s
`HEAD_ON_EVERY_WORD` is on for Arabic (`lang_ar.py`), so the article and the
one-letter proclitics are supplied automatically and only the *stems* are
declared.

The five sense collisions `book2_en.py` documents all recur in Arabic and are
handled the same way — `عين`/`العين` and `مقاومة` and `تواترات` in `STOP`,
`ثقافة` and `حامل` and `قواعد` in `DROP`, and `الصبغيات المتماثلة` in
`EXTRA_PROTECT` — plus one Arabic-only entry, `دهن`, which is the lipid family
in chapter 1 and the *fuel* "fat" in chapter 9, where English writes "fat" and
links nothing.

Because Arabic pluralises by internal vowel change, which `lang_ar.py`'s empty
`WORD_TAIL` cannot reach, **19 plural and dual stems were declared in `EXTRA`**
(خلايا، مورّثات، أنواع، أليلات، أليلين، طفرات، عصبونات، إنزيمات، جمهرات،
مضادات حيوية، هرمونات، أجسام مضادة، صبغيدان/صبغيدين/صبغيدات، ثغور، مشابك،
عضيات، منعكسات، تهوية). They lift the edition from 3 767 links to 4 831 — from
68 % to 87 % of English's density — and every one of them was counted in this
edition's own prose before being declared.

Both homograph censuses were run **after** the last prose edit and the linker
re-run afterwards. The remaining flags were each read and judged benign:

| Flag | Reading |
|------|---------|
| `def:g10:sport-and-health:training` 22 vs EN 7 | *التدريب / النشاط البدني* — the right concept every time; English's own count is low because it writes the unlinked word "exercise" |
| `prop:g12:respiration-fermentation:mitochondrion` 21 vs EN 8 | an artefact of the definite/indefinite split: *المتقدرة* was harvested to the chapter-9 proposition and *متقدرة/المتقدرات* to the organelle definition. Both targets are about mitochondria |
| `prop:g12:diversification-of-life:polyploidy` 8 vs EN 3 | same split (*تعدد الصيغ الصبغية* / *متعدد الصيغة الصبغية*) |
| six CHAPTER flags of 1–2 links each | verified one by one: *التنوع الوراثي*, *الترجمة*, *الصبغي X*, *عضية*, *التدريب*, one *البروتينات* and one *الدهون* — all the right sense |

Three genuine wrong-sense links **were** found this way and fixed in the prose,
not by protecting them: *برباط* (a warming **strap**, not a ligament) in
grade-11 ch. 5, *البلوغ* (a sapling **reaching** adulthood, not puberty) in the
grade-12 ch. 6 solutions, and *تحت عين البنكرياس* (idiomatic "under the eye
of", rewritten as *تحت رقابة*) in grade-12 ch. 14.

Two targets English links and Arabic does not:
`prop:g11:becoming-male-female:hormones` (English 6) and
`def:g10:exercise-and-energy:vo2max` (English 1). The first is an artefact of
English's own harvest — its only key is the **capitalised** `Testosterone`, so
it collects six sentence-initial links and nothing else; Arabic has no case, so
the analogous key would have taken all 62 occurrences of *التستوستيرون* and
pointed them at a proposition about the *foetal* testis. Left as an orphan
deliberately. Arabic in exchange links two targets English does not
(`prop:g11:cancer:genes`, 5, and `prop:g12:domesticated-plants:transgenic`, 2).

## Prose-gate extensions (append-only, `tools/check_arabic_prose.py`)

Six extensions, each with a dated comment naming the reason, each re-validated
on **both** controls (an untranslated English chapter copied into the private
scratchpad, which still reports its 2 177 `english` hits; and the live `ar`
tree, which reports OK). Gate controls were never run in a live language
directory.

1. `NUCLEOTIDE_SEQ` — `5'-ATGGCTTAC-3'`: `LATIN_WORD` swallows the trailing
   hyphen, so no per-word rule could see it. A base sequence is data, not
   English, and stays byte-identical in every language.
2. `ALLOWED_WORDS` += the six Latin binomial words this volume adds
   (`chlorella`, `euglena`, `archaeopteryx`, `paranthropus`, `africanus`,
   `heidelbergensis`).
3. `ALLOWED_WORDS` += the twenty IUPAC three-letter amino-acid abbreviations,
   which the genetic-code table prints in full.
4. A guarded `continue` for hyphen-joined chains (`Met--Pro--Glu--Phe`), which
   arrive as **one** token and are accepted only when **every** component is
   separately allowed, so an ordinary English compound still fires.
5. `ALLOWED_WORDS` += `mrna`, `trna`, `rrna`, and += `sry` (the mixed-case
   mouse gene symbol; all-caps symbols already passed as acronyms).
6. `ATTRIBUTION_EXTRA` — `Imperial War Museums`, then `OpenStax` and
   `Anatomy and Physiology`. All three are printed **in Latin** by the
   orchestrator's own `frontmatter/image-credits-book2.ar.tex`; translating
   them in a chapter caption would have given the book two names for one
   source. Only the exact phrases are blanked; the component words are
   deliberately **not** added to `ALLOWED_WORDS`.

## Deliberate divergences from a literal rendering

- Personal names in chapter captions are transliterated (*غريغور مندل، تشارلز
  داروين، إدوارد جينر، جون غولد، هنري مول وجون فوكس، غولدسميث*), following the
  `ar` Book 1 precedent; institutions and licence identifiers stay Latin.
- `meiosis I / II` is rendered *المنصّف الأول / الثاني* rather than with a Latin
  numeral, which reads as an ordinal in Arabic and avoids a bare Latin glyph in
  a figure label.
- `\emph{Beagle}` is transliterated *بيغل*: it is a ship's name in running
  prose, not a bibliographic credit.
- Ten paragraphs were reworded to clear overfull boxes, following the
  "add short words around the wide material" rule; two long Latin runs
  (`Pro وThr وAla…` and `Met--Ala--Leu…`) needed Arabic separators inserted,
  because under `bidi=basic` a Latin run is one directional box and
  `\allowbreak` inside it does not take.

## Why not 100

- **Link density is 87 % of English's** on an identical target count. The gap
  is structural: Arabic broken plurals are unreachable by any suffix rule, so
  coverage is exactly as good as the hand-declared `EXTRA` list, and a longer
  list buys links at rising risk of wrong-sense matches.
- **Two plural keys were surrendered for correctness.** *بروتينات* and
  *الدهون*/*دهن* would have put ~30 links on the chemistry-families definition
  in chapters where English points the same words at
  `def:g11:gene-expression:protein` or links nothing; `AMBIG_POLICY` cannot
  reach an `EXTRA` entry, so the choice was coverage or the right target.
- **Three overfull boxes remain in a file this edition does not own.**
- The definite/indefinite split of two targets (mitochondrion, polyploidy) is
  cosmetically different from English's link graph, though every link is on a
  target about the same thing.

## Requests to the orchestrator

1. **`frontmatter/image-credits-book2.ar.tex` carries the only three overfull
   boxes in the book** (6.93 pt, 10.04 pt, 8.40 pt, at its lines 16–20, 22–25
   and 25–28). All three are long unbreakable Latin runs inside Arabic list
   items — `C.~Goldsmith, Centers for Disease Control and Prevention`,
   `OpenStax \emph{Anatomy and Physiology}, عبر Wikimedia Commons`, and
   `Henry Maull و John Fox، نحو 1854، Wikimedia Commons`. Inserting a short
   Arabic word before each run (or `\sloppy` around the `itemize`) clears them;
   this edition did not edit the file because it is outside its ownership.
2. **The same file spells six personal names in Latin** (`Gregor Mendel`,
   `Alexander Fleming`, `Charles Darwin`, `Edward Jenner`, `John Gould`,
   `Henry Maull و John Fox`) while the chapter captions transliterate them, as
   Book 1 `ar` does. That is defensible — a credit line is a bibliographic
   record — but it does mean the book prints two spellings of *داروين* and of
   *جون غولد*. Worth a ruling for the series.

## Defects found in the ENGLISH canon

None that changes a fact. Two observations, reported rather than fixed:

1. **`prop:g11:becoming-male-female:hormones` collects its six links from the
   capitalised `Testosterone` only.** The lowercase word is never linked, so
   the target's link set is decided by sentence position rather than by sense —
   the same class of defect as the `\emph{Sorting}` case recorded in
   `CLAUDE.md`. A `NO_CAPITAL` entry in `book2_en.py` would fix it, but it
   would also multiply the target's links by ten, so it needs an editorial
   decision rather than a config edit.
2. **Chapter 8 says photosynthesis fixes "about a seventh of the carbon in the
   atmosphere" a year**, while the same chapter's weekend problem gives
   \qty{1e11}{t} fixed against \qty{8.5e11}{t} in the atmosphere — one eighth
   and a half, and its own solution 16 computes 8.5 years. "A seventh" is loose
   rather than wrong; the Arabic keeps the English wording.

## Samples

Three passages, with the verdict a native reader would give.

**1 — Chapter 12 (adaptive immunity), opening.** *Native.*

> في سنة 1796 خدش طبيب ريفي مادةً من بثرة جدري البقر عند حالبة إلى ذراع صبي،
> وانتظر ستة أسابيع، ثم لقّحه بالجدري. فلم يمرض الصبي. ولم يكن في عالم الطبيب
> ما يفسر ذلك؛ فقد بدا أن الجسم قد علّم.

Narrative past with `ف`-chaining, the way an Arabic science book opens a
chapter; no calque of the English participial clauses.

**2 — Chapter 1 (meiosis), definition.** *Native.*

> الخلية الحاملة نسختين من كل صبغي --- واحدة من كل والد، ويكوّن الاثنان زوجًا من
> الصبغيات المتماثلة --- هي خلية ثنائية الصيغة الصبغية، ويكتب طقمها $2n$.

The technical noun phrase is built with a genitive construct
(*ثنائية الصيغة الصبغية*), not with a borrowed adjective; the em-dash aside
survives because Arabic uses it in the same way.

**3 — Chapter 13 (stretch reflex), exercise 15.** *Near-native.*

> "النخاع الشوكي ليس إلا كبلًا بين الدماغ والجسم." أعد الكتابة على الصواب في
> فقرة، مستعينًا بالمنعكس، وبالعصبون البيني، وبالحيوان الذي قطع نخاعه عن دماغه.

*كبل* is the standard loan for *cable* and reads naturally, but a purist would
prefer *سلك ناقل*; the imperative chain is idiomatic.

**4 — Chapter 9 (respiration), solution 20.** *Native.*

> نحو \qty{0.6}{mol} من ATP في الدقيقة؛ ونحو \qty{3}{L} من الأكسجين في الدقيقة
> تدفع ثمنها؛ والسلسلة التنفسية في الغشاء الداخلي للمتقدرة تصنع نحو تسعة
> أعشارها.

The result line of a weekend problem, in the same clipped register as the
English, with the units untouched.
