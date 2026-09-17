# One Biology Book 5 — Dutch (`nl`) edition: self-score

**Date:** 2026-09-17
**Scope:** `one_biology_book_5_university_year_3_nl.tex` — 27 chapters + 27
solutions files (University Biology, Year 3), 54 files, plus
`frontmatter/image-credits-book5.nl.tex` and
`tools/term_config/book5_nl.py`.
**Quality bar:** *native academic*. Not "is this a correct rendering of the
English?" but "would a Dutch biologist writing a third-year university volume
from scratch have written these sentences?" The register reference is this
repository's own `parts/bachelor-2/nl/` (Book 4 `nl`, one year younger, same
exercise machinery); Book 5 keeps that voice and raises the technical level.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | **0** second-person pronouns anywhere (`je`/`jij`/`jouw`/`jullie`/`uw`/`u`; the only `u` tokens in the tree are mathematical variables). Course text is impersonal (`de mens`, `men`, passive); exercise stems are bare imperatives and match the Book 4 `nl` distribution almost exactly (`Bereken` 22, `Noem` 21, `Definieer` 11, `Voorspel` 10, `Leg … uit` 25, `Formuleer` 7) |
| Terminology | high | 96 | Dutch university-biology vocabulary throughout: `uitstervingsdraaikolk`, `effectieve populatiegrootte`, `inteeltcoëfficiënt`, `tegenstroomvermenigvuldiging`, `vrijwaterklaring`, `kabelvergelijking`, `lengteconstante`, `soort--oppervlakteverband`, `foto-evenwicht`, `trofische cascade`, `weefselvocht` for *interstitium*, `doorgangsversterkende cel` for *transit-amplifying cell*. The English loanwords Dutch genomics actually writes (`read`, `reads`, `contig`, `scaffold`, `seed`) are kept, as a Dutch bioinformatics text keeps them |
| MT-artifact freedom | high | 95 | twin-comparison gate 9: **0** multi-word findings; the 103 one-word advisories are gene and protein symbols (`Dicer`, `Drosha`, `Argonaute`, `MutS/MutL`, `Igf2`), amino-acid abbreviations (`thr`) and math subscript labels (`\Delta G_{\text{fold}}`, `A^{*}_{\text{high}}`) that are notation, not prose |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 54 files (labels, environments, solution keys, `\emph`/`\index` adjacency, index count, math spans, drawing code, image paths, delimiters, braces); 0 TeX accent escapes — the tree is UTF-8 throughout |
| Cross-references | gated | 100 | 0 undefined references; exercise/solution key sets identical chapter by chapter; gate 11 green on all 27 weekend problems (27 `problem`s, 324 `exercise`s, 351 `solution`s — all equal to English) |
| Figures and captions | — | 96 | 116 `tikzpicture`s, 116 `\foreach` lists, 105 `\includegraphics`, 210 `\text{}` fragments — every node label, axis label, `\foreach` label field and `\text{}` string translated by hand after the write, then the figure pages read on the rendered PDF |
| Solutions | — | 96 | all 27 solutions twins translated; every numeric answer re-derived against the chapter (which is how the canon defect below surfaced) |
| Defined-term links | — | 95 | 2,510 links on **191** distinct targets against English's 2,670 on 188 — 94 % of English's density with **full target parity** (`comm` of the two target sets is empty in the English→Dutch direction) plus three targets English leaves orphaned |

## Measured state

```
files on disk             54   (27 chapters + 27 solutions)       = English
parts/bachelor-3/**/nl paths in the .fls                     54   = English
pages                    384                                       (English 365)
LaTeX errors               0
undefined references       0
Overfull boxes             0                                       = English
Underfull boxes          144                                       (cosmetic, English has them too)
nullfont warnings          0                                       = English
"invalid in math mode"     0
TeX accent escapes         0
\index entries           913  (898 distinct keys)                  = English 913 (900 distinct)
\qty occurrences       2,283                                       = English
\includegraphics         105                                       = English
\begin{tikzpicture}      116                                       = English
\foreach                 116                                       = English
\text{...} fragments     210                                       = English
\begin{exercise}         324   \begin{solution} 351   \begin{problem} 27   = English
\omterm links          2,510 on 191 distinct targets                (English 2,670 on 188)
```

`bash tools/check_translation.sh bachelor-3 nl` → **TRANSLATION GATE: PASSED**
(gates 1–8 and 10–11 silent; gate 9 reports 0 multi-word findings and 103
advisory one-word findings).

## What this edition had to solve

**Dutch welds its compounds, and `harvest.py` accepts an `\index` key outside a
`definition` only when the key contains a space.** English `genome size`,
`cable equation`, `gene drive`, `bit score`, `packing ratio`, `folding funnel`
all pass that test; `genoomgrootte`, `kabelvergelijking`, `gendrive`,
`bitscore`, `pakkingsgraad`, `vouwtrechter` do not. The first link run reached
152 targets against English's 188 — 36 missing, not one because the notion was
absent from the Dutch prose. They were found by a `comm` of the two `\omterm`
target sets, never by eye, and every one is restored by an `EXTRA` in
`tools/term_config/book5_nl.py` whose value is a label of *this* book.

**Dutch inflection the linker cannot manufacture.** `WORD_TAIL` for `nl` is
`(?:e?[ns])?`, which cannot double a consonant (`stamcel` → `stamcellen`),
shorten a vowel (`hormoon` → `hormonen`, `macrofaag` → `macrofagen`), form a
Latin plural (`microtubulus` → `microtubuli`) or write the apostrophe plural of
an abbreviation (`siRNA` → `siRNA's`). That silently cost ~250 links against
the English twin; each is recovered by an `EXTRA` whose key is the inflected
Dutch surface. `EXTRA` ended at 91 entries.

**Eight homograph families, all found by the two censuses, none by eye.** The
per-target *chapter-set* census is the one that finds them; the frequency
census alone would have missed every one of them except `domein`:

| Dutch term | right sense | wrong sense it reached |
|---|---|---|
| `domein` | protein domain (ch. 7) | domains of life, expression domains, TADs — eight other chapters |
| `laesie` | DNA lesion (ch. 3) | the clinical lesion of chs. 17, 19, 21 |
| `mantel` | vesicle coat (ch. 8) | endospore coat (ch. 12), phage coat (ch. 13) |
| `assemblage` | genome assembly (ch. 4) | virus assembly (chs. 13, 15) |
| `divergentie`, `convergentie` | neural (ch. 17) | sequence divergence (ch. 25) |
| `latentie` | viral latency (ch. 13) | the latency of a spinal reflex (ch. 17) |
| `transformatie` | bacterial (ch. 12) | the homeotic transformation of a vertebra (ch. 23) |
| `conjugatie` | bacterial (ch. 12) | auxin conjugation (ch. 22) |
| `tolerantie` | immunological (ch. 16) | the glucose tolerance test (ch. 21) |
| `profiel` | HMM profile (ch. 5) | a concentration profile (ch. 23) |
| `barrière` | innate barriers (ch. 15) | the glomerular filtration barrier (ch. 20) |
| `herschikking` | viral reassortment (ch. 13) | rearrangement of the antibody locus (ch. 16) |

All twelve are `STOP` (21 keys with their capitalised and plural forms), which
is what English does with the same collisions (`domain`, `lesion`, `coat`,
`assembly`, `convergence`, `divergence`, `tolerance`, `profile`, `barrier`).
`DROP` and `EXTRA_PROTECT` stayed empty: no Dutch collision this volume needed
a form `WORD_TAIL` invents.

**Six over-reaches were read in context and kept**, because the Dutch link is
the *right* sense where the English edition simply declines to link: `reads`
(chs. 5, 14 — sequencing reads), `lezer`/`schrijver` (chs. 2, 11 — chromatin
and m6A readers and writers), `envelop` (ch. 25 — the HIV envelope), and the
three targets English leaves orphaned (`regel van Oja` → Hebb, the marginal-value
theorem, the viability-analysis method).

**One EXTRA was deliberately withdrawn.** `golgiapparaat` reached its own
chapter 29 times where English links `Golgi apparatus` once; `cisternerijping`
alone reaches the same target, so the bare compound is commented out with the
reason.

## Samples

1. ch. 27, opening — *In 1813 Audubon watched a flock of passenger pigeons…*

   > In 1813 zag Audubon drie dagen lang een zwerm trekduiven over Kentucky
   > trekken die de hemel verduisterde; er waren er misschien vijf miljard,
   > een kwart van alle vogels van Noord-Amerika.

   **Native.** `zag … trekken` splits the perception verb the way Dutch does,
   `er waren er misschien` is the idiomatic existential with the partitive
   `er`, and the semicolon carries the apposition without a relative clause.
   Machine translation produces `Audubon keek naar een zwerm … vliegen` and
   `er waren misschien vijf miljard van hen`.

2. ch. 17, opening — the nervous-system budget.

   > De mens heeft er zesentachtig miljard, verbonden door honderd biljoen
   > synapsen, draaiend op twintig watt --- een vijfde van zijn energie voor
   > twee procent van zijn massa.

   **Native.** `De mens heeft er …` is the impersonal subject this series uses
   instead of a second person; `honderd biljoen` is the Dutch long-scale
   value of English *hundred trillion* (a real trap: MT writes `triljoen`);
   `draaiend op twintig watt` is the ordinary Dutch participle for a running
   machine.

3. ch. 24, opening — regeneration.

   > Snijd een axolotl een poot af en binnen twee maanden heeft hij een nieuwe
   > laten groeien, met bot, spier, zenuw en huid op de juiste plaatsen.

   **Native.** The separable verb `afsnijden` is split correctly across the
   indirect object (`snijd een axolotl een poot af`), which no MT system gets
   right, and `heeft … laten groeien` is the Dutch causative perfect.

4. ch. 20, solutions, item 6 — renal arithmetic.

   > De gefiltreerde vracht is $\qty{40}{mL/min}\times\qty{0.14}{mmol/mL} =
   > \qty{5.6}{mmol/min}$. Uitscheiding: …

   **Near-native.** `gefiltreerde vracht` for *filtered load* is the standard
   Dutch physiology term and the telegraphic solution style matches the rest
   of the series, but the sentence is a little flatter than a Dutch textbook
   would write it; a native author would more often drop the copula entirely
   (`Gefiltreerde vracht: …`), which is what the other 26 solution files do.

5. ch. 1, opening — epigenetics.

   > Twee muizen uit hetzelfde nest, genetisch identiek tot aan de laatste
   > base, zitten naast elkaar: de ene is slank en bruin, de andere dik en
   > geel, en zij zal diabetes krijgen.

   **Native.** `de ene … de andere` is the Dutch correlative (MT writes `een
   is … de andere is`), and the forward-looking `en zij zal diabetes krijgen`
   keeps the English sentence's sting without a relative clause.

No sample in the book reads as machine translation; the residual weakness is
the flatness noted in sample 4, which recurs in perhaps a dozen solution
sentences where a numeric chain leaves little room to vary the syntax.

## Why not 100

* **The solutions are terser than the course text.** They are correct,
  idiomatic Dutch, but a native author writing them from scratch would vary
  the sentence openings more; the arithmetic chains constrain word order and
  perhaps a dozen of them read as a list rather than as prose (sample 4).
* **Link density is 94 % of English's, not 100 %.** Target parity is complete
  and the deficit is now almost entirely one class: Dutch says a thing once
  where the English sentence says it twice (`de boom van een gen … de boom van
  de soorten` against `the gene tree … the species tree`), so there is simply
  one fewer surface to link. Recovering the last 160 links would mean
  paraphrasing correct Dutch toward English, which is the wrong trade.
* **Twelve homograph families had to be `STOP`ped.** Each decision was read in
  context, but `STOP` is a blunt instrument: it also removes the *correct*
  links that term would have made in a later chapter (`convergentie` in the
  sensory chapter is genuinely the neural convergence of chapter 17). English
  pays the same price for the same words, so parity is preserved, but a
  hand-curated per-chapter map would do better than either edition does.
* **Three `\text{}` subscript labels stay English** (`\Delta G_{\text{fold}}`,
  `A^{*}_{\text{high}}`). They are notation shared with every other edition and
  with the formula the student will meet in the literature; translating them
  would desynchronise the mathematics between editions for no reader's gain.

## Post-delivery canon alignment (coordinator, 2026-09-17)

After this edition was delivered, six defects that wave 1 found in the English
canon were fixed, and this tree was brought into line with them. The edition
was **not re-translated**; the edits were mechanical and are listed here
because three of them move a census count.

- **ch. 25 no longer re-defines *orthologue*/*paralogue*.** English defined the
  same two notions twice, 21 chapters apart, and escaped `harvest.py`'s
  "defined twice is ambiguous" rule only because ch. 4 spelled them American
  and ch. 25 British. Any language with one word for the concept lost those
  links. Chapter 4 now owns the definition; ch. 25's two markers are plain
  prose. `\index` 913 -> **911**, `\emph` 1,330 -> **1,328**, matching English.
- **Two `\numrange` calls given three arguments** became `\qtyrange`
  (`12-bacteriology`, `solutions/20-renal-osmoregulation`).
- **`day`/`days` inside `\qty{}`/`\unit{}` arguments became `d`**, the form
  Books 3 and 4 use, including the sites frozen inside math spans that no
  translator could reach through `id_apply`.
- The ch. 1 weekend problem's self-referential "question 12" now reads
  "question 11", and ch. 26's truncated photo credit is repaired.

The link pass was re-run from scratch (`--unwrap --apply`, then `--apply`), and
a plain dry run over the wrapped tree reports **`links to insert: 0`**.
Re-measured after the change: **384 pages, 2511 links on 191
targets, `\index` 911, `.fls` 54, 0 errors / 0 undefined / 0 overfull /
`nullfont` 0 / 0 "invalid in math mode", `check_translation.sh bachelor-3 nl`
gates 1-11 PASSED.** The self-score above is unchanged.
