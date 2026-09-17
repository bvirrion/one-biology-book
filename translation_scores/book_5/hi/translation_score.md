# Translation self-score — One Biology Book 5 (University Year 3), Hindi (`hi`)

**Date:** 2026-09-17
**Scope:** 54 body files (`parts/bachelor-3/hi/`, `parts/bachelor-3/solutions/hi/`)
and the curated term configuration `tools/term_config/book5_hi.py`.

**Overall: 96 / 100**

## Quality bar

The bar of `translation_instruction.md` and `hindi_style_card.md`: native academic
prose at the register of a university Year-3 lecture, not a gloss of the English. The
text must read as though a biologist teaching the course had written it in Hindi,
while every `\label{}`, `\cref` target, solution key, `\omterm` first argument, math
span, drawing body and image path stays byte-identical to the English twin.

## Sense and register reference

* **`parts/bachelor-2/hi/`** (Book 4 Hindi, shipped 2026-09-16 at 96/100) for settled
  terminology, measured and not assumed: `समष्टि` (population), `व्यष्टि`,
  `युग्मविकल्पी`, `आनुवंशिक अपवाह` (drift), `प्रभावी समष्टि आकार`, `विषमयुग्मजता`,
  `अंतःप्रजनन गुणांक` / `अंतःप्रजनन अवसाद`, `विलोपन` / `विलोपन-ऋण`,
  `जाति--क्षेत्रफल संबंध`, `आवास`, `आक्रामक जाति`, `अड़चन` (bottleneck), `प्रसरण`
  (variance) against `विविधता` (variation), and — changed late in this run for the
  series' sake — `सुयोग्यता` for *fitness*, which Book 4 Hindi uses and which this
  edition had first written as `फिटनेस` (24 occurrences, all converted, the whole
  book re-linked and rebuilt afterwards).
* **`parts/bachelor-1/hi/`** (Book 3 Hindi) and Book 1 Hindi for `पोषी अनुप्रपात`
  (trophic cascade) and `आधार जाति`.
* **`parts/bachelor-3/fr/`** and **`/nl/`** (the finished wave-1 Book 5 editions) as a
  sense reference wherever an English sentence could be read two ways.

## Dimension scores

| Dimension | Score | Note |
|---|---:|---|
| Fidelity of sense | 97 | Every number, unit, sign and cross-reference read against the English twin. One answer (ch. 27 no. 20) is deliberately NOT a translation: the English number is arithmetically impossible and the corrected sense was written instead, on the coordinator's instruction. |
| Naturalness / register | 95 | Postpositional word order throughout, `यानी` / `इसलिए` / `ताकि` for the logical joints, `कोई` for the English indefinite where Hindi wants it and nowhere else. The heaviest passages are the eight-line definition environments, where the English sentence is itself three clauses deep and the `id_apply` range structure keeps its boundaries. |
| Terminological consistency | 96 | One vocabulary per notion across 27 chapters, measured by a corpus scan for every harvested term plus its inflections; `check_term_display_drift.py` flags 81 targets, every one of them either a target English itself reaches through several distinct terms or a Hindi inflection pair (`प्रतिजैविक`/`प्रतिजैविकों`); no notion is spelled two ways. |
| Structural integrity | 100 | Every `id_apply` census green on all 54 files: labels, environments, solution keys, `\emph`/`\index` adjacency and count, ordered math spans byte-for-byte *including their internal line breaks*, drawing bodies, delimiters, braces, image paths. `\index` 911, `\emph` 1,328 and `\qty` 2,249 — identical to English in every case, file by file. |
| Typography (Devanagari) | 96 | 0 overfull, 0 underfull-blocking, `nullfont` 0, 349 pages, no hyphenation patterns needed. Five overfull boxes were cleared by rewording, all of them `in paragraph` (prose) and none a fixed-width box. |
| Term links | 96 | **2,672 links on 192 targets against English's 2,672 on 188** — every English target reached, and four more. 15 STOP, 0 DROP, 15 EXTRA, 113 DERIVED bases (133 forms), 2 EXTRA_PROTECT, all derived from this edition's own harvest. |

## Samples

1. **Ch. 27, the opening** (`27-conservation-biology.tex`).
   EN: *“The species was not rare when its decline began; it was harvested by the
   trainload, and its forests were cut, and a bird that bred only in immense colonies
   could not breed once the colonies had thinned below some size no one measured.”*
   HI: «जब उस जाति का ह्रास शुरू हुआ तब वह दुर्लभ नहीं थी; उसे रेलगाड़ी भर-भर कर काटा
   जाता था, और उसके वन काटे जा रहे थे, और जो पक्षी केवल विशाल बस्तियों में प्रजनन करता
   था वह उन बस्तियों के किसी ऐसे आकार से नीचे विरल हो जाने पर प्रजनन कर ही नहीं सका
   जिसे किसी ने मापा नहीं था।»
   **Verdict: native.** The English relative clause “below some size no one measured”
   is split the way Hindi splits it — the correlative `जिसे … मापा नहीं था` is pushed
   to the end rather than embedded — and `रेलगाड़ी भर-भर कर` carries “by the
   trainload” as an adverbial reduplication, which is the idiom, not a calque.

2. **Ch. 27, weekend problem answer 20** (`solutions/hi/27-conservation-biology.tex`).
   EN: *“The observed 100 is closer to the exponential 124 than to the logistic 63.”*
   HI: «देखा गया 100 वही चरघातांकी मान है, क्योंकि वृद्धि-दर इन्हीं दो बिंदुओं पर फिट
   की गई थी, न कि संभार्य 63…»
   **Verdict: native, and deliberately not faithful.** Question 19 fits $r$ from the
   two observed points, so the exponential prediction at eight years *is* the observed
   100 and the English 124 cannot exist. Written as the corrected sense on the
   coordinator's instruction. The causal clause names the growth rate in words rather
   than as `$r$`, because an added math span would have broken the ordered math-span
   census against a twin that has none there.

3. **Ch. 21, the insulin–glucose loop** (`21-endocrinology.tex`, theorem).
   EN: *“so the feedback divides the disturbance an unregulated body would suffer by
   $1 + L$, the \emph{loop gain} plus one.”*
   HI: «इसलिए वह पुनर्भरण उस विक्षोभ को, जो किसी अनियंत्रित शरीर को झेलना पड़ता,
   $1 + L$ से, यानी \emph{पाश-लाभ} जमा एक से, भाग देता है।»
   **Verdict: native.** The English counterfactual “would suffer” becomes the Hindi
   contrary-to-fact `झेलना पड़ता` without a conditional particle, and the instrumental
   `से … भाग देता है` puts the divisor before the verb where Hindi needs it — the
   English order would have produced an unreadable `भाग देता है $1+L$ से`.

4. **Ch. 26, Hamilton's rule** (`26-behavioural-ecology.tex`, theorem).
   EN: *“\emph{Altruism} --- behaviour that lowers the actor's reproduction and raises
   another's --- thus evolves toward kin, in proportion to relatedness”*
   HI: «इस तरह \emph{परोपकारिता} --- यानी ऐसा व्यवहार जो कर्ता का जनन घटाए और किसी
   दूसरे का बढ़ाए --- बंधुओं की ओर, संबंधिता के अनुपात में विकसित होती है»
   **Verdict: native.** `यानी` opens the em-dash gloss the way Hindi opens an
   apposition, and the two subjunctive verbs `घटाए … बढ़ाए` give the defining relative
   clause its generic reading, which the indicative would have turned into a report
   about one particular act.

5. **Ch. 02, the ping-pong cycle** (`02-rna-regulation.tex`, definition).
   EN: *“the cleaved fragment becomes a new sense piRNA, which in turn cuts cluster
   transcripts to make more antisense piRNAs --- the \emph{ping-pong} cycle”*
   HI: «कटा खंड नया संवेदी piRNA बन जाता है, जो बदले में गुच्छा-अनुलेखों को काटकर और
   प्रतिसंवेदी piRNA बनाता है --- यही \emph{पिंग-पॉन्ग} चक्र है»
   **Verdict: near-native.** Accurate, and the conjunctive participle `काटकर` is the
   right way to chain the two actions; but Hindi does not mark the plural on the
   English loan, so “more antisense piRNAs” becomes `और प्रतिसंवेदी piRNA`, where the
   quantifier alone carries the plural. Readable and standard in Indian molecular
   biology writing, and it is exactly this missing plural that cost the edition a link
   target (see below) — but an English reader would notice the flattening.

## Why not 100

* **Register in the deepest definitions.** Book 5's definition environments run to
  eight lines with three embedded qualifications. Hindi would rather break such a
  sentence in two, but the `id_apply` range structure keeps the English sentence
  boundaries, so a handful of definitions (ch. 03 lesions, ch. 15 complement, ch. 20
  countercurrent) read as accurate lecture Hindi rather than as elegant Hindi. A
  deliberate trade against the byte-level censuses, not an oversight.
* **Latin nomenclature in a Devanagari line.** Gene, protein and species names stay
  Latin (`Cdk1`, `Su(var)`, `Bicoid`, `Clostridioides difficile`), which is what an
  Indian university course does, but a sentence sometimes carries three Latin tokens
  inside Devanagari and the mixed line is busy. 219 such tokens are now declared in
  `check_hindi_prose.py`'s allow-list.
* **Plural flattening.** Hindi does not mark the plural on a Latin loan, which is
  invisible in the prose but not in the linker: English reaches
  `def:b3:rna-regulation:pirna` only through the PLURAL key *piRNAs* (the singular
  harvests to the ncRNA definition instead), so this edition reaches it through an
  `EXTRA` on `piRNA गुच्छों` — one link where English has seven. The same flattening
  costs a few links on `प्रतिजैविक`, `विक्षति` and `शलाका`, each restored form by
  form in `DERIVED`.
* **The STOP list costs correct links.** 15 Hindi words are a technical term in one
  chapter and an ordinary noun in six others — `विभेदन` is X-ray *resolution* in ch. 7
  and sensory *discrimination* in ch. 17–18 and cell *differentiation* in ch. 24;
  `प्रांत` is a protein *domain* in ch. 7 and a Hox *expression domain* in ch. 23;
  `प्रसुप्ति` is viral *latency* in ch. 13 and seed *dormancy* in ch. 22. Each STOP
  removes wrong links in several chapters at the price of correct ones in its own.
* **Four marginal senses knowingly left in,** each read in context and judged right:
  `विषाणु` links the virus definition in ch. 14, 24 and 25 where English's own
  `virus`/`viruses` does not; `वाचन` links the sequencing-read definition in ch. 5 and
  ch. 14, which English STOPs wholesale because *read* is also a verb (Hindi's `वाचन`
  is only the noun, and the one verbal use, `गलत वाचन` = misreading, is protected);
  `प्रतिरक्षी` links *antibody* in ch. 17 and 25, where English silently misses its
  own plural (see below); and `ओया का नियम` links the Hebb theorem in ch. 19, which
  English drops because `NOT_A_TERM` contains the English word *rule*.

## Requests to the orchestrator

1. **English canon, `solutions/27-conservation-biology.tex` answer 20** — confirmed
   defect, already known: “the exponential 124” is impossible, because question 19
   derives $r$ from $31 \to 100$ over eight years, so the exponential prediction at
   eight years is $31\,\mathrm{e}^{1.17} = 99.9$, the observed 100 itself. This
   edition ships the corrected sense; English and the wave-1 editions still carry 124.
2. **`morphology.pattern` cannot form an English `-y → -ies` plural.** The English
   tail is `(?:e?s)?`, so `antibody` + `es` would be *antibodyes*: Book 5's English
   canon contains 31 occurrences of **“antibodies”** and links **none** of them. This
   is not a Hindi defect — the Hindi edition links its 51 — but it silently lowers the
   English baseline every other edition is measured against, in this book and
   presumably in the whole series.
3. **`id_apply.py`'s `NODE_TEXT` cannot match a node whose `at` coordinate contains
   parentheses.** `at\s*\([^)]*\)` stops at the first `)`, so
   `\node[...] at ({2.4*sin(40)},{2.4*cos(40)}) {food, \qty{1}{km}}` is compared
   BYTE-FOR-BYTE as drawing code and a translated node label is refused. Same file,
   `label={[font=\tiny]right:hormone}` is not covered by `NODE_TEXT` at all. Both
   forced a whole-file `!draw` opt-out (ch. 21 and ch. 26), which is the only lever
   available and is far blunter than the defect.
4. **`check_hindi_prose.py`'s reduction lets a TikZ node's OPTION list through as
   prose**: `node[right, font=\tiny]`, `label={[font=\tiny]right:…}` and
   `at ({2.4*sin(40)},…)` are reported as the English words *right*, *font*, *log*,
   *sin*. The reduction is the part `check_indonesian_prose.py` imports, so it was not
   touched; the four tokens are parked in the data block instead. It should drop a
   node's bracketed option list the way it already drops a macro's.
5. **Appended to shared files** (reported in full in the handback):
   `tools/check_hindi_prose.py` gained one `ALLOWED_WORDS |= {...}` data block (219
   biology symbols, commented with its evidence) and one four-character change to the
   transliterated-article scan, excluding a hyphen on either side of the token so that
   `आर-पार` — an ordinary Hindi word — stops being reported 18 times as English *are*.
   Neither touches the imported reduction; both Indonesian and Hindi control runs over
   `bachelor-1`, `bachelor-2` and `grade-10` are unchanged and green.
