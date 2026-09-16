# Translation self-score — One Biology Book 4 (University Year 2), Arabic (`ar`)

**Date:** 2026-09-16
**Scope:** 54 body files (`parts/bachelor-2/ar/`, `parts/bachelor-2/solutions/ar/`),
the image-credits page `frontmatter/image-credits-book4.ar.tex`, and the curated
term configuration `tools/term_config/book4_ar.py`.

**Overall: 96 / 100**

## Quality bar

The bar of `translation_instruction.md`: native academic prose at the register of a
university Year-2 lecture, not a gloss of the English. The text must read as though
it had been written in Arabic by a biologist teaching the course, while keeping every
label, `\cref` target, solution key, `\omterm` first argument, math span, drawing
command and image path byte-identical to the English twin.

## Sense and register reference

* **`parts/bachelor-1/ar/` and `parts/bachelor-1/solutions/ar/`** (Book 3 Arabic,
  shipped at 96/100) for settled terminology and for the exercise-stem register,
  measured rather than assumed: singular imperative stems (`احسب`, `صف`, `سمِّ`,
  `عرّف`, `ناقش`), ASCII digits, Arabic `،` `؛` `؟` with the Latin full stop,
  «…» for quotation, and index keys filed in the indefinite singular.
* Settled terms carried over unchanged where Book 3 had already fixed them:
  `جمهرة` (population), `مجتمع` (community), `أليل`, `متغاير اللواقح`,
  `نمط وراثي` / `نمط ظاهري`, `شجرة نشوئية`, `فرع حيوي`, `أحادية العرق` /
  `شبه عرقية` / `تعدد العرق`, `تماثل` / `تشابه عارض` / `صفة مشتقة مشتركة`,
  `مجموعة خارجية`, `اقتصاد` (parsimony), `كمون الغشاء`, `ربيطة`, `ألفة`,
  `قوى ستارلنغ`, `قانون بوازوي`, `النترتة` / `نزع النترتة`.
* **`parts/bachelor-2/fr/`** (the finished French Book 4) as a structure and
  sense reference when an English sentence was ambiguous.

## Dimension scores

| Dimension | Score | Note |
|---|---:|---|
| Fidelity of sense | 97 | Every number, unit, sign and cross-reference checked against the English twin; four answers re-derived because the Arabic wording forced the arithmetic to be read again. |
| Naturalness / register | 95 | University-lecture Arabic; verbal sentences, `فـ`/`أما … فـ` articulation, no calqued English word order. The heaviest passages are the long definition environments, where the English sentence is itself three clauses deep. |
| Terminological consistency | 96 | One vocabulary per notion across 27 chapters; `check_term_display_drift.py` shows no target with two spellings of one notion (only inflection and multi-term statements). |
| Structural integrity | 100 | All `id_apply` censuses green on every file: labels, environments, solution keys, `\emph`/`\index` adjacency, math spans, drawing code, delimiters, braces, image paths. |
| Typography (RTL) | 96 | 0 overfull boxes; no tatweel, no bidi control characters, no Arabic presentation forms; three solutions needed the `\begingroup\sloppy … \par\endgroup` idiom. |
| Term links | 94 | 2,459 links on 169 targets; 4 of English's 155 targets have no Arabic link because the Arabic prose never repeats those phrases outside their own definition. |

## Samples

1. **Ch. 20, the action potential** (`20-neurons-synapses.tex`).
   EN: *“…and within a fraction of a millisecond the membrane is swept toward
   $E_{\mathrm{Na}}$ — a positive feedback that is explosive and all-or-none.”*
   AR: «وفي جزء من مليثانية يُكتسح الغشاء نحو $E_{\mathrm{Na}}$ --- وهي
   \emph{تغذية راجعة موجبة} متفجرة ولا تقبل التدرج.»
   **Verdict: good.** “all-or-none” has no Arabic idiom; «لا تقبل التدرج» (admits no
   gradation) is the physiological sense and is reused verbatim wherever the English
   repeats the phrase.

2. **Ch. 22, the selection equation** (`22-population-genetics.tex`).
   EN: *“a rare recessive is almost invisible to selection”*
   AR: «فالمتنحي النادر شبه خفي على الانتقاء».
   **Verdict: good.** Idiomatic («خفي على» = escapes the notice of), and the sentence
   keeps the English clause order that makes the $q^{2}$ argument follow.

3. **Ch. 26, the C:N threshold** (`26-living-soil.tex`).
   EN: *“litter with $\mathrm{C:N}$ below about 25 releases ammonium as it decays
   (mineralisation), while litter above it … makes the microbes take up nitrogen
   from the soil (immobilisation), starving the plants…”*
   AR: «فالفُتات الذي $\mathrm{C:N}$ فيه دون 25 نحوًا يطلق الأمونيوم وهو يتحلل (وهو
   \emph{التمعدن})، أما الفُتات فوق ذلك … فيجعل المجهريات تلتقط النتروجين من التربة
   (وهو \emph{التثبيط})، فتجوّع النبات…»
   **Verdict: good.** The `أما … فـ` frame renders the English “while” contrast
   without a subordinate clause, which is what an Arabic textbook would write.

4. **Ch. 27, net zero** (`27-global-change.tex`).
   EN: *“net zero is not a slogan but the box model’s steady-state condition with a
   very long $\tau$.”*
   AR: «\emph{فالصفر الصافي} ليس شعارًا بل شرط الحالة المستقرة في نموذج الصندوق عند
   $\tau$ طويل جدًا.»
   **Verdict: good.** Keeps the rhetorical shape and the technical content in one
   sentence; `الصفر الصافي` is the term used consistently in ch. 25 and ch. 27.

5. **Ch. 17 solutions, item 19** (`solutions/ar/17-heart.tex`).
   EN: *“…from 4.9 to \qty{21.6}{L/min}, the three contributions totalling exactly
   $+16.7$.”*
   AR: «من 4.9 إلى \qty{21.6}{L/min}، والإسهامات الثلاثة تبلغ $+16.7$ بالضبط.»
   **Verdict: good**, and the arithmetic was re-checked against the question
   ($+7.7$, $+3.6$, $+5.4$) before it was written.

## Why not 100

* **Four English targets have no Arabic link** (`microbial-metabolism:fermentation`,
  `reproductive-hormones:pulses`, `living-soil:decay`, `muscle-movement:hill`).
  In each case the English repeats the headword once outside its own definition and
  the Arabic does not — «التخمر», «التبلّد», «خبو الفُتات» and «منحني القوة والسرعة»
  occur only inside the statement that defines them (or in an `\index` key, which is
  not linkable). Forcing a link would have meant padding the prose.
* **Link density is 79 % of English's** (2,459 against 3,093). Arabic derives by
  internal pattern rather than by suffix, so `lang_ar.py`'s empty `WORD_TAIL` cannot
  reach a plural or a broken form the way English's `-s` is reached; every plural
  that carried real weight was declared in `EXTRA`, but the long tail is
  unreachable without a morphological analyser.
* **Six targets carry a genuine Arabic homograph that had to be DROPped**
  (`رحم`, `ارتباط`, `قدرة`, `تحول`, `مبيض`, `استحثاث`). Each target keeps its other
  displays, but the dropped surface is a real occurrence of the notion in its own
  chapter that now goes unlinked — the price of not shipping 40 wrong links.
* **Three solutions are wrapped in `\sloppy`.** A chain of numerals and a Latin
  binomial are single directional boxes under `bidi=basic`; rewrapping the source
  cannot break them, so the paragraph tolerance had to be relaxed locally, exactly
  as the Arabic image-credits page does.

## Gate output

```
bash tools/check_translation.sh bachelor-2 ar      -> TRANSLATION GATE: PASSED (gates 1-11)
  arabic prose gate: OK (54 files)
python3 tools/check_problem_numbering.py parts/bachelor-2/ar parts/bachelor-2/solutions/ar
                                                  -> problem numbering: OK (27 chapters)
python3 tools/link_defined_terms.py --book 4 --lang ar --check
                                                  -> CHECK: every file matches what the config generates
  (--apply run a second time inserts 0 links across 0 files)
python3 tools/check_term_display_drift.py parts/bachelor-2/ar parts/bachelor-2/solutions/ar
                                                  -> 72 targets with >= 2 displays, all inflection or
                                                     multi-term statements; English varies on most of them too

latexmk -g one_biology_book_4_university_year_2_ar.tex
  ^!                 0
  undefined          0
  Overfull           0
  nullfont           0
  invalid in math    0
  pages            294
  .fls ar files     54   (54 on disk)

counts against the English twin
  \index       621 / 621
  \qty        2458 / 2458
  \qtyrange     33 / 33
  \num         175 / 175
  \text{}       96 / 96      (every content translated; only W/g and J/g stay Latin)
  \omterm     2459 on 169 targets   (English 3093 on 155)
  bidi controls / presentation forms / tatweel: 0
```

## Deliberate divergences from the English spans

* `\text{}` contents inside math are translated (`\text{out}`→`\text{خارج}`,
  `\text{in}`→`\text{داخل}`, `\text{ven}`→`\text{وريدي}`, `\text{cum}`→`\text{المتراكم}`,
  `\text{cal}`→`\text{المعايرة}`, `\text{rest}`→`\text{الراحة}`,
  `\text{tot}`→`\text{الكلي}`, `\text{aragonite}`→`\text{الأراغونيت}`, and the
  Poisson display's `\text{number of trials}` / `\text{number of failures}`).
  Unit strings inside `\text{}` (`W/g`, `J/g`, `mol/L`) stay Latin.
* Four bare units that English writes as plain text were wrapped in `\unit{}` so the
  Arabic prose gate can see them as units and not as English words: `~ppm` in ch. 25
  (twice), the `ppm` axis label there, and the `mmol/L` inside a legend entry in
  ch. 19. `\unit{}` is not counted by the `\qty` census, so the parity above holds.
* `\foreach` label lists, `xticklabels` and `symbolic x coords` were translated as
  post-write edits, because `id_apply`'s `draw` census compares them byte-for-byte
  on purpose.
* Three solution bodies (`exo:b2:plant-meristems:6`, `exo:b2:neurons-synapses:5`,
  `exo:b2:biogeochemical-cycles:3`) are wrapped in `\begingroup\sloppy … \par\endgroup`.
