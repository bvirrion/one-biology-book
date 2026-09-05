# One Biology Book 1 — Hindi (`hi`) edition: self-score

**Date:** 2026-09-04
**Scope:** `one_biology_book_1_primary_middle_school_hi.tex` — 71 chapters +
71 solutions files (grades 1–9), 142 files, 419 pages.
**Quality bar:** *native school prose*. The question is not "is this a correct
rendering of the English?" but "would a Hindi biology teacher writing this book
from scratch, for these ages, have written these sentences?" The register
reference is the physics Book 1 `hi` edition
(`../one-physics-book/parts/grade-*/hi/`) — same ages, same series, same
exercise machinery.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | `तुम` throughout, 0 formal `आप`; `-ओ` imperatives in every exercise stem |
| Terminology | high | 96 | standard Hindi school-biology vocabulary; `DNA` and Latin binomials left in Latin script, as Hindi textbooks print them |
| MT-artifact freedom | high | 97 | written, not post-edited: no calques found in the sampled reading |
| Structure / LaTeX hygiene | gated | 100 | `id_apply` censuses green on all 142 files; log 0 errors / 0 undefined / 0 overfull |
| Cross-references | gated | 100 | 0 undefined references |
| Figures and captions | — | 97 | every TikZ node and axis label translated; 3 `\foreach` label lists translated by hand (the draw census cannot see them); image paths byte-identical |
| Solutions | — | 96 | all 71 solutions twins translated; `\text{}` and `\qty` censuses clean over solutions too |
| Defined-term links | — | 95 | 7,923 links on 150 of English's 151 targets — 104 % of English's density; 12 collision classes found and cured |

## Measured state

```
files on disk            142   (71 chapters + 71 solutions)     = English
.fls files inputted      142                                    = English
pages                    419                                   (English 422)
LaTeX errors               0
undefined references       0
Overfull boxes             0                                   (7 found, 7 fixed)
nullfont warnings         20                                    = English
"invalid in math mode"     0
TeX accent escapes         0                                    = English
\qty                      57, every unit argument ASCII         = English
\text{...}                 4, all four translated               = English
\index{} occurrences     331                                    = English
distinct \index keys     303                                    = English
\omterm links          7,923   (English 7,608)
distinct link targets    150   (English 151)
check_translation.sh   PASSED for grade-1 … grade-9 (gates 1–10, incl. the
                       Devanagari prose gate)
check_orphan_lines.py  0 orphan English lines
link_defined_terms --check   "every file matches what the config generates"
```

All of the above are the numbers of the **final** state: the linker was
re-run and both `\omterm` censuses re-measured after the last prose edit of
the overfull sweep, and `--check` confirms the tree and the config agree.

## Censuses run, and what each found

* **`\omterm` per-target frequency diff vs English.** The instrument that
  showed the edition's central structural problem: Hindi inflects, and
  `lang_hi.py` sets `WORD_TAIL = ''` with `DERIVE = False`, so *every* oblique
  and plural form is invisible to the harvester. The first honest pass linked
  6,289 — 83 % of English — with `पौधा` at 89 links against English's 296
  for **plant**, because the book says `पौधे`/`पौधों` on nearly every page.
  Fixed by generating a `DERIVED` table from this book's own corpus (a variant
  is listed only where it actually occurs) and reading all 152 entries one by
  one: +1,838 occurrences recovered, and the same diff then showed the
  remaining gaps are structural, not sloppy (below).
* **`\omterm` chapter-set diff vs English.** Caught what frequency could not —
  four wrong **senses**, none of which changes a link count enough to notice:
  `सूक्ष्मदर्शी` (a *microscope*) used adjectivally for *microscopic* in
  grades 7 and 8 — bad Hindi as well as a bad link, now `सूक्ष्म`; `झिल्ली`
  (a cell *membrane*) used for the pond's *surface film* in grade 7, now
  `सतह की परत`; `खोल` (a *shell*) matching the verb *खोलना*, "to open", in
  four places; and `जड़` (a plant *root*) matching *अँगूठे की जड़*, the base
  of the thumb, in the grade-4 pulse method.
* **`\index{}` key-set diff vs English.** 331 occurrences and 303 distinct
  keys on both sides — a one-to-one map, including the ten keys English writes
  twice (`head`, `limb`, `skin`, `living thing`, `flower`, `soil`, `joint`,
  `brain`, `adult`, `old age`), each of which is written twice in Hindi too
  (`सिर`, `उपांग`, `त्वचा`, `सजीव`, `फूल`, `मिट्टी`, `जोड़`, `मस्तिष्क`,
  `वयस्क`, `बुढ़ापा`). No English index key survives anywhere in the tree.
* **`\text{...}` census over chapters *and* solutions**: 4 in each tree, all in
  the grade-3 food-chain display, `grass/grasshopper/lizard/buzzard` →
  `घास/टिड्डा/छिपकली/बाज़`. The display's trailing `.` is kept byte-identical:
  replacing it with a danda breaks the math-span census.
* **Line-end greps** (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`,
  and a Devanagari-hyphen variant): 0 real hits. The 66 lines ending in `''`
  are closing quotes (English has 94 of the same); the 21 `^\s*\.` hits are
  TikZ `..` path syntax, byte-identical to English.
* **Overfull sweep**, run before the final linker pass: 7 boxes, every one
  `in paragraph`, all cleared. Six were cured by **adding** short words
  before the break point — never by shortening, which the Physics Book 4 Hindi
  agent measured going 2 pt → 54 → 19 → 69 as it cut. The sixth was not prose
  at all: the plant-cell TikZ overlay in grade 6 chapter 9, whose Hindi labels
  `कोशिका भित्ति` and `पानी की थैली` are wider than their English originals
  and pushed the picture past its `0.48\linewidth` minipage; fixed with
  `align=center` and a `\\` inside each label. The linker and both `\omterm`
  censuses were then re-run **after** the sweep, and the sweep's own rewrites
  re-checked — measure last, do not edit last. One box also taught the limit
  of a single-chapter probe: a paragraph containing `\cref` sets differently
  alone (the reference prints `??`) than in the book, so the last box, which
  the probe called clean, had to be cured against a full rebuild — the
  offending line was the remark's run-in header plus a `\cref`, and the cure
  was two short words inserted before the reference.

**Homograph collisions found and fixed: 12 classes.** Four were live wrong
links, removed by editing the prose or by `EXTRA_PROTECT` (above). Eight more
were caught before they could be minted, by curating the term config against
this corpus rather than translating the English config:

| Word | Wrong sense it would have linked | Occurrences at risk | Cure |
|---|---|---|---|
| `जोड़` / `जोड़ों` | the body's *joints* (grades 1, 3) vs the **synapses' junctions** (grades 8–9) | 104 | `STOP` |
| `कड़ी` | the food chain's *link* vs any link of any chain, argument or hormone cascade | 100 | `DROP` |
| `पानी` | the drink of the balanced-diet families vs water everywhere | 395 | `DROP` |
| `जीवित` | the grade-1 *living* vs the ordinary adjective | 104 | `DROP` |
| `वर्ग` | the vertebrate *classes* vs school classes and `आहार-वर्ग` | 58 | `DROP` |
| `छाँटना` / `छँटाई` | the sorting *criterion* vs the imperative of half the exercises | 35 | `DROP` |
| `सूक्ष्मजीवों` | the oblique plural harvested from **grade 6's bakery** microbes, pointing every grade-9 use back at the bread | 8 | `STOP` |
| `घुटने` | the knee's oblique vs the verb of `दम घुटने`, *to suffocate* | 15 | excluded from `DERIVED` |

(`शाखा`/`तना`, `मृत्यु`, `वृद्धि`, `जन्म` and the sense words are `DROP`ped on
the same reasoning English uses for *branches*, *trunk*, *death*, *grows* and
*sight/hearing/touch*; they are not counted above because English refuses them
too, so they cost this edition nothing English does not also decline.)

The mirror finding is worth recording too: several English collisions **do not
exist in Hindi**, and suppressing them would have thrown links away. `control`
splits into `नियंत्रण` (the fair test's control) and `क़ाबू` (self-control);
`contract` into `संकुचन` (a muscle) and `इक़रारनामा` (the daily contract);
`scale` into `शल्क` (a fish's) only; `tree` into `पेड़` (the plant) and
`वृक्ष` (the kinship tree), each with its own definition. Those four are *not*
stopped, and `met:g4:what-plants-need:fairtest` consequently carries 16 links
where English carries 0. `खेत` (farmland) is the one word I stopped for a
reason English does not have either: it has no wrong sense here, but 28 links
to "managed land" on every mention of a farm is noise, and English's own
judgement on *fields* is the same.

## Register

Verified against physics Book 1 `hi`, not inferred:

```
biology  hi:  तुम 213   तुम्हारा 26   तुम्हारी 52   तुम्हारे 46   तुम्हें 22   formal आप 0
physics  hi:  तुम 605   तुम्हारा 90   तुम्हारी 123  तुम्हारे 160  तुम्हें 65   formal आप ~13
```

(The 80 raw hits for `आप` in the biology tree are all `अपने आप`, "by itself",
and `आपूर्ति`, "supply" — there is no formal second person anywhere.)
Second-person density tracks the English source, which uses *you/your* 328
times to physics English's 1,057. Exercise stems are bare `तुम`-imperatives —
*बताओ, गिनाओ, समझाओ, लिखो, चलाओ, जोड़ो, जाँचो* — never `आप`-imperatives and
never infinitive stems, matching the physics twin. 5,605 sentences end in a
danda; 0 Devanagari digits anywhere in the tree — ASCII throughout, as the
physics `hi` edition prints them.

## Sampled fragments, judged

1. **grade 1, ch. 1 opening** — *"गीली पगडंडी पर एक घोंघा धीरे-धीरे सरक रहा
   है। उसके बग़ल में एक भूरा कंकड़ पड़ा है, उतना ही छोटा, उतना ही गोल।"* —
   **native**. `सरक रहा है` for a snail's slide and the bare `उतना ही छोटा,
   उतना ही गोल` apposition are Hindi rhythm, not English word order carried
   over; a translation would have produced `जितना छोटा … उतना ही`.
2. **grade 5, ch. 1 opening** — *"वह अटूट सतह घुलकर नन्हे-नन्हे कक्षों की एक
   फ़र्शबंदी बन जाएगी, फ़र्श के पत्थरों की तरह आपस में जुड़े हुए।"* —
   **native**. `फ़र्शबंदी` is the right register for *pavement* here, and the
   reduplicated `नन्हे-नन्हे` does the work English does with "tiny".
3. **grade 7, ch. 1 opening** — *"किसी बंद मरतबान में एक कठ-जूँ रखो और घंटों
   बाद उस मरतबान की हवा बदल चुकी होती है।"* — **native**. `मरतबान` (a
   wide-mouthed storage jar) is the concrete word a Hindi science teacher
   would use for a bell jar; `कठ-जूँ` is the standard name for a woodlouse.
4. **grade 8, ch. 9 opening** — *"नींद की कमी, शोर, परदे और मन पर असर करने
   वाले पदार्थ, उस मशीन के साथ --- जो तुम ख़ुद हो --- जोड़-दर-जोड़ असल में
   करते क्या हैं?"* — **native**. The interposed `--- जो तुम ख़ुद हो ---` and
   the sentence-final `करते क्या हैं?` reproduce the English's emphasis with
   Hindi's own means; `जोड़-दर-जोड़` is the idiomatic `X-दर-X` distributive.
5. **grade 9, ch. 1 solutions, #5** — *"वह पहुँचा सकता है जो वह ख़ुद दिखाता
   नहीं: उस लक्षण का निर्धारक उसमें से छिपा हुआ गुज़र गया, और एक पीढ़ी बाद
   ऊपर आ गया।"* — **near-native**. Correct and compact, but `ऊपर आ गया` for
   *surfaced* is a shade plain; `सतह पर आ गया` would carry the English's
   metaphor better. Left as is because the plainer verb suits a grade-9
   answer key.

## What is wrong in a shared (English) file

`parts/grade-7/07-heart-and-circulation.tex`, the double-circulation figure
caption, reads:

> Red arrows carry the oxygen-rich `\omterm{def:g1:my-body:parts}{legs}`, blue
> the returning ones.

"legs" is not a word that belongs in that sentence — it should be *blood* (or
*routes*) — and because the wrong word happens to be a linked term, the
English edition also carries a link from a circulation caption to the grade-1
body-parts definition. It is an English canon defect, not a translation one,
and every edition inherits the sentence; the Hindi caption says
`लाल तीर ऑक्सीजन से भरपूर रास्ते दिखाते हैं, और नीले लौटते हुए रास्ते`
("red arrows show the oxygen-rich routes, blue the returning ones"), which is
what the figure means. Reported rather than fixed: the English tree is not
mine to edit.

## Why not 100

* **Four English targets have no Hindi counterpart, and two more are thinner
  than English**, each for a reason the language forces:
  * `def:g4:breathing:movements` (English 26 links, Hindi 0). English links the
    everyday word *breathing*; Hindi's everyday word is `साँस`, while the
    grade-4 definition's display is the Sanskritic `श्वासोच्छ्वास`, which the
    chapters then use twice. Linking `साँस` globally would have sent every
    grade-7 respiration mention to the wrong chapter, so I left the target
    empty rather than mint 200 plausible-looking wrong links.
  * `prop:g3:bones-and-muscles:joints` (English 6, Hindi 0) — the price of
    `STOP`ping `जोड़`, which was worth 104 wrong links in grades 8–9.
  * `prop:g5:people-and-nature:managed` (English 2, Hindi 0) and
    `def:g6:matter-from-food:production` (English 1, Hindi 0) — three links
    between them: the first is `खेत`, `STOP`ped for noise, whose definition
    chapter contains no other bare `खेत`; the second is the phrase
    `पदार्थ का निर्माण`, which the chapters only ever write inside its own
    definition, where the linker correctly refuses to link it.
  * `prop:g3:flowers-fruits-seeds:transform` carries 71 links against English's
    168, and `def:g2:from-seed-to-plant:seed` 231 against 108. English splits
    *seed* (grade 2) from *seeds* (grade 3) by number; Hindi's `बीज` is both,
    so the whole class lands on the grade-2 definition. The links are right;
    the split is not reproducible.
* **The `DERIVED` table is a hand-curated list, not a morphology.** It covers
  the forms this book actually uses, so a future chapter added to Book 1 will
  need it extended. The alternative — teaching `lang_hi.py` real Hindi
  morphology — is a shared-rules change, and `tools/check_book5_golden.sh`
  exists precisely to stop a language agent from making one.
* **Ambiguous terms cannot take `DERIVED` entries at all** (`harvest.py`
  applies them only to unambiguous terms), so the oblique forms of `त्वचा`,
  `फेफड़ा`, `पोषक तत्व`, `हॉर्मोन`, `सजीव` and `शुक्राणु` stay unlinked —
  roughly 150 further occurrences that English links. Recovering them would
  need a per-chapter `EXTRA`, which the config format does not have.
* **Terminology has one place I would still argue about.** `बहाली` for
  *recovery* (grade 7's pulse-recovery time) is defensible and consistent, but
  a sports-physiology text would more likely write `रिकवरी` — which the
  Devanagari prose gate correctly refuses as a transliteration. `उबराव` was
  the alternative and is not a real word. I kept `बहाली`.
* **Page count is 419 against English's 422**, i.e. Devanagari sets slightly
  tighter here than English at the same measure; nothing about the layout was
  tuned to reach it.
