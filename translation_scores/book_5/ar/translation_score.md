# Translation self-score — One Biology Book 5 (University Year 3), Arabic (`ar`)

**Date:** 2026-09-17
**Scope:** 54 body files (`parts/bachelor-3/ar/`, `parts/bachelor-3/solutions/ar/`)
and the curated term configuration `tools/term_config/book5_ar.py`.

**Overall: 96 / 100**

## Quality bar

The bar of `translation_instruction.md` and `arabic_style_card.md`: native academic
prose at the register of a university Year-3 lecture, not a gloss of the English. The
text must read as though a biologist teaching the course had written it in Arabic,
while every `\label{}`, `\cref` target, solution key, `\omterm` first argument, math
span, drawing body and image path stays byte-identical to the English twin.

## Sense and register reference

* **`parts/bachelor-2/ar/`** (Book 4 Arabic, shipped 2026-09-16 at 96/100) and
  **`parts/bachelor-1/ar/`** (Book 3 Arabic) for settled terminology, measured and
  not assumed: `جمهرة` (population), `أليل`, `نمط وراثي`/`نمط ظاهري`, `كمون الغشاء`,
  `ربيطة`, `ألفة`, `الصادات` (antibiotics), `مورّثة`, `صبغين` (chromatin),
  `تغايرية زيجية` (heterozygosity), `انجراف` (drift), ASCII digits, Arabic `،` `؛` `؟`
  with the Latin full stop, ``…'' for quotation, index keys in the indefinite singular.
* **`parts/bachelor-3/fr/`** (the finished French Book 5, the wave-1 twin) as a sense
  reference wherever an English sentence could be read two ways — the loop-gain
  argument of ch. 21, the auxin-trapping derivation of ch. 22, and the marginal-value
  theorem of ch. 26 were each checked against it before being written in Arabic.

## Dimension scores

| Dimension | Score | Note |
|---|---:|---|
| Fidelity of sense | 97 | Every number, unit, sign and cross-reference read against the English twin. One answer (ch. 27 no. 20) is deliberately NOT a translation: the English number is arithmetically impossible and the corrected sense was written instead, on the coordinator's instruction. |
| Naturalness / register | 95 | Verbal sentences, `أما … فـ` articulation, `إذ`/`ولذلك` for the causal joints; no calqued English word order. The long definition environments are the heaviest passages, because the English sentence is itself three clauses deep. |
| Terminological consistency | 96 | One vocabulary per notion across 27 chapters; `check_term_display_drift.py` reports no target with two lexical spellings of one notion — only inflection (`المحاذاة`/`محاذاة`) and multi-term statements. |
| Structural integrity | 100 | Every `id_apply` census green on all 54 files: labels, environments, solution keys, `\emph`/`\index` adjacency and count, math spans byte-for-byte including their internal line breaks, drawing bodies, delimiters, braces, image paths. `\index` 911 and `\emph` 1,328, identical to English. |
| Typography (RTL) | 96 | 0 overfull boxes, 0 `nullfont`; no tatweel, no bidi control characters, no Arabic presentation forms, no split numerals. `\emergencystretch` lives in the entry file, never in a chapter body. |
| Term links | 95 | 2,155 links on 199 targets; **every one of English's 188 targets is reached**, and 11 more besides. 19 STOP entries, 0 DROP, 8 EXTRA, all derived from this edition's own harvest. |

## Samples

1. **Ch. 27, the risks of smallness** (`27-conservation-biology.tex`, definition).
   EN: *“A large population declines when its death rate exceeds its birth rate; a
   small one can vanish without any change in either.”*
   AR: «تتراجع الجمهرة الكبيرة حين يتجاوز معدل وفاتها معدل مواليدها؛ وأما الصغيرة
   فتقدر على الزوال بلا أي تغيّر في أيهما.»
   **Verdict: native.** The verbal opening (`تتراجع` before its subject) and the
   `وأما … فـ` contrast are how Arabic joins two clauses of unequal weight; the
   English semicolon would have produced a limp `و` in a literal rendering.

2. **Ch. 27, weekend problem answer 20** (`solutions/ar/27-conservation-biology.tex`).
   EN: *“The observed 100 is closer to the exponential 124 than to the logistic 63.”*
   AR: «والمرصود 100 هو بعينه قيمة النموذج الأسّي --- إذ حُسب معدل النمو من هاتين
   النقطتين نفسيهما --- في مقابل 63 في اللوجستي.»
   **Verdict: native, and deliberately not faithful.** Question 19 fits $r$ from the
   two observed points, so the exponential prediction at eight years IS the observed
   100 and the English 124 cannot exist. Written as the corrected sense on the
   coordinator's instruction; the interpolated clause avoids a `$r$` span the English
   does not have, so the math census still matches.

3. **Ch. 21, the linear insulin–glucose loop** (`21-endocrinology.tex`, theorem).
   EN: *“so the feedback divides the disturbance an unregulated body would suffer by
   $1 + L$, the \emph{loop gain} plus one.”*
   AR: «فتقسم التغذية الراجعة الاضطراب الذي كان سيعانيه جسم غير منظَّم على $1 + L$،
   أي \emph{كسب العروة} زائدًا واحدًا.»
   **Verdict: native.** `كسب العروة` is the control-theory term an Arabic physiology
   course uses, and the relative clause `الذي كان سيعانيه` carries the English
   counterfactual ("would suffer") without the conditional particle a gloss would add.

4. **Ch. 25, the opening of molecular evolution** (`25-molecular-evolution.tex`).
   EN: *“The neutral theory became the null hypothesis of molecular evolution, the
   baseline against which selection is detected.”*
   AR: «وصارت \emph{النظرية المحايدة} فرضية العدم في التطور الجزيئي، وخط الأساس الذي
   يُكشف الانتخاب في مواجهته.»
   **Verdict: native.** `فرضية العدم` is the statistical term, not a calque of "null";
   `في مواجهته` gives "against which" its comparative sense rather than its
   adversarial one, which is the reading a literal `ضد` would have forced.

5. **Ch. 07, the prion paragraph** (`07-structural-biology.tex`).
   EN: *“the misfolded form of the prion protein PrP converts the normal form on
   contact into more of itself, so that the ``infection'' carries no nucleic acid but
   only a shape”*
   AR: «فالصورة السيئة الطي من البروتين البريوني PrP تحوّل الصورة السوية عند التماس
   إلى مزيد من نفسها، فلا تحمل ``العدوى'' حمضًا نوويًا بل شكلًا فقط».
   **Verdict: near-native.** Accurate and readable, and `سيئة الطي` / `السوية` are the
   right pair; but `إلى مزيد من نفسها` is one remove from idiomatic Arabic, which
   would rather say `تستنسخ صورتها فيما يلامسها`. Kept because the English deliberately
   reuses "itself" from the sentence before and the parallel carries the argument.

## Why not 100

* **Register in the deepest definitions.** Book 5's definition environments routinely
  run to eight lines with three embedded qualifications. Arabic prefers to break such
  a sentence in two, but the `id_apply` range structure keeps the English sentence
  boundaries, so a handful of definitions (ch. 03 `lesions`, ch. 10 `checkpoints`,
  ch. 20 `countercurrent`) read as accurate lecture Arabic rather than as elegant
  Arabic. That is a deliberate trade against the byte-level censuses, not an oversight.
* **Transliterated nomenclature.** Protein and gene names stay Latin (`Pitx1`, `GroEL`,
  `FoxP3`, `Cas9`), which is what an Arabic university course does — but it means a
  sentence sometimes carries three Latin tokens, and Arabic type sets those as
  directional islands. Legible, occasionally busy.
* **Link density.** 2,155 links against English's 2,672 on 199 targets against 188.
  The gap is not a miss — every English target is reached — it is the STOP list: 19
  Arabic masdars (`قراءة`, `تحول`, `إعادة`, `تمييز`, `نطاق`, `ناقل`, …) that are both
  a technical term in one chapter and an ordinary noun everywhere else. Each STOP
  costs correct links in its own field to remove wrong ones in six others.
* **Two marginal senses knowingly left in.** `الغلاف` links to the virus envelope in
  ch. 14 and ch. 25 where the bacterial envelope is at least as good a reading (2
  links), and `البادئة` links the replication primer of ch. 10 to the PCR definition
  (1 link). Both are defensible readings of the Arabic; protecting them would have
  cost more than it bought.

## Requests to the orchestrator

1. **English canon, `solutions/27-conservation-biology.tex` answer 20** — confirmed
   defect, already known to the coordinator: "the exponential 124" is impossible
   because question 19 derives $r$ from the two points $31 \to 100$ over eight years,
   so the exponential prediction at eight years is $31\,\mathrm{e}^{1.17} = 99.9$, i.e.
   the observed 100 itself. The logistic 63 and the pedagogical point are both right;
   only the number is wrong. This edition ships the corrected sense; English and the
   five wave-1 editions still carry 124.
2. **`harvest.py` cannot harvest an Arabic display from a statement environment.**
   In `harvest.py` the emph-to-label match inside a definition falls back to
   `re.sub(r'[^a-z]', '', to_text(term).lower())` and requires that key to share a
   prefix with the label's leaf. For an Arabic (or Hindi) display that key is the
   empty string, so the match can never succeed and the term is recovered only if it
   also carries an adjacent `\index{}`. Seven of this edition's targets were
   unreachable for that reason alone and had to be restored by hand in `EXTRA`. A
   non-Latin-script fallback (accept the emph when the environment has exactly one
   emph, as the ordinal path already does) would remove that whole class.
3. **`tools/check_arabic_prose.py` silently passes a file argument.** The gate only
   walks directories; handed a single `.tex` path it reports `OK (0 files)` and exits
   0. That is how 561 residual-English hits survived a per-file check earlier in this
   run. It should either accept files or exit non-zero on an argument it ignores.
4. **Appended to a shared file** (reported in full in the handback): the
   `LABEL_SYNTAX` normaliser and the `MATH_SUBSCRIPTS` / `ALLOWED_WORDS` /
   `ATTRIBUTION_EXTRA` blocks in `tools/check_arabic_prose.py`, all append-only and
   commented with their reason, plus the move of an earlier agent's dead code back
   above the `__main__` guard.
