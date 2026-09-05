# One Biology Book 2 — Dutch (`nl`) edition: self-score

**Date:** 2026-09-05
**Scope:** `one_biology_book_2_high_school_nl.tex` — 36 chapters + 36 solutions
files (grades 10–12), 72 files, 395 pages.
**Quality bar:** *native academic*. The question is not "is this a correct
rendering of the English?" but "would a Dutch biology teacher writing a
`havo`/`vwo` upper-school volume from scratch have written these sentences?"
The register reference is this repository's own Book 1 `nl` edition
(`parts/grade-1..9/nl/`) — same series, same exercise machinery, one school
stage younger.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | informal `je` / `jouw`, 0 `u`/`uw`, 0 `men`; imperative exercise stems, as in the Book 1 `nl` twin |
| Terminology | high | 96 | Dutch school-biology vocabulary; Latin binomials, DNA/RNA/ATP/NADP untouched; one cross-volume inconsistency found and normalised |
| MT-artifact freedom | high | 96 | twin-comparison gate clean of multi-word findings on all three years; 21 one-word advisories, all real Dutch cognates |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 72 files; log 0 errors / 0 undefined / 0 overfull / 0 `nullfont` |
| Cross-references | gated | 100 | 0 undefined references, label sets identical to English file by file |
| Figures and captions | — | 97 | 136 `tikzpicture`s, 184 `omfigure`s, 56 image paths, 23 `\legend` sites, 12 `symbolic coords` lists and every `\foreach` label list translated |
| Solutions | — | 96 | all 36 solutions twins translated; exercise/solution key parity gated |
| Defined-term links | — | 95 | 4,971 links on 103 targets (English 5,547 on 103) — 90 % of English density, against 85 % for the Book 1 `nl` edition |

## Measured state

```
files on disk             72   (36 chapters + 36 solutions)     = English
.fls files inputted       72                                    = English
pages                    395                                    (English 379)
LaTeX errors               0
undefined references       0
Overfull boxes             0
nullfont warnings          0                                    = English
"invalid in math mode"     0
TeX accent escapes         0
\qty occurrences       1,184                                    = English
\text{...}                 9, all translated                    = English
\includegraphics          56                                    = English
\index{} occurrences     182                                    = English
distinct \index keys     175   (English 171) — every key Dutch
\omterm links          4,971   (English 5,547)
distinct link targets    103   (English 103)
check_translation.sh   PASSED for grade-10, grade-11, grade-12 (gates 1–10)
check_orphan_lines.py  0 orphan English lines
check_latin_prose.py   no multi-word findings in any of the three years
```

## Censuses run, and what each found

* **`\index{}` key-set diff against the English twin — the highest-value
  sweep, run after the last file landed.** 182 occurrences on both sides, and
  all 175 distinct Dutch keys are Dutch words. 21 keys are byte-identical to
  their English twin and every one of them is a true cognate or an
  international term: `ATP, DNA, RNA, adrenaline, base (DNA), clade, codon,
  crossing-over, diabetes, dominant, doping, genotype, glucagon, intron,
  karyotype, mitochondrion, neuron, neurotransmitter, nucleotide, reflex,
  vacuole`. Zero English residue.
* **`\omterm` per-target frequency diff against English.** This is what found
  the single largest defect of the run: `def:g10:cells-common-unit:cell`
  carried 908 links in English and only 318 in Dutch. The cause is
  `lang_nl.py`'s `WORD_TAIL = (?:e?[ns])?`, which cannot double the *l* of
  *cel* → *cellen*, so the commonest plural in the whole volume — 411
  standalone uses — was invisible while the singular linked 285 times. An
  `EXTRA` closes it (672 links now). The same diff found `hormonen`,
  `antibiotica`, `organellen`, `carcinogenen`, `antigenen`, `pezen`,
  `centromeren`, `mutagenen` and `neurotransmitters`, all plurals the `-en/-s`
  tail cannot build, and `bloedglucose`, which the boundary keeps out of the
  harvested compound `bloedglucosespiegel`.
* **`\omterm` per-target frequency diff, re-run against the NEW English twin
  after the `species` canon fix.** The English baseline moved 5,275 → 5,547
  links and 102 → 103 targets when `\emph{species}\index{species}` was moved
  onto the Species definition; the Dutch was re-curated against the new
  baseline, not the old one. `def:g10:biodiversity-scales:species` now carries
  259 Dutch links in 16 chapters against 272 English links in 15 — the one
  extra Dutch chapter is `g11-09`, where "de soort die elk hoofdstuk van dit
  jaar heeft beschreven" is the species, correctly.
* **`\omterm` chapter-set diff against English.** Every target that reaches
  more than six chapters is core vocabulary that reaches the same chapters in
  English (`gene, cell, DNA, molecule families, organelle, mutation,
  chromosome, enzyme, protein, muscle, nucleotide`). Confirmed that the three
  `STOP`ped words survive only as **chapter-local** links, which is exactly
  what they should do: `oog` links 12 times and only inside the eye chapter,
  `frequenties` 5 times and only inside the drift chapter.
* **`\omterm` per-target surface-form census.** Confirmed the
  `nearest-preceding` splits are the intended ones (`eiwit` 44× to the
  molecule families and 73× to the gene-expression protein; `enzym` 16× to
  metabolism and 72× to the enzyme definition), and that no wrong-sense form
  survives.
* **`\legend` / `\addlegendentry` census.** 23 sites, matching English's 23,
  every one Dutch.
* **`symbolic x/y coords` + `\addplot coordinates` census.** 12 symbolic
  lists, all Dutch, and each one verified against the coordinate names of its
  own `\addplot` lines (these are *not* blanked by the `draw` census and must
  be edited together or the plot silently drops its bars).
* **`\foreach` label-list census.** Every `\foreach` whose body contains a
  visible label was read by eye; 10 lists carried text and all are Dutch.
* **Three line-end sweeps** (`['’]$` excluding `''`; a line opening on
  punctuation; a word-final hyphen at end of line): 0 hits each.
* **`\text{...}` census over the chapters *and* the solutions:** 9 sites,
  matching English, all translated (`\text{spier}`, `\text{last}`,
  `\text{energie}`, `\text{licht, bladgroen}`).
* **Register measurement against the Book 1 `nl` twin:** 80 `je`, 5 `jouw`,
  **0** `u`, **0** `uw`, **0** `men`; exercise stems are bare imperatives
  (`Bereken` 109, `Leg uit` 105, `Vergelijk` 43, `Noem` 32, `Verklaar` 31).

## Curation decisions in `tools/term_config/book2_nl.py`

Every entry was decided on the Dutch word, in context; nothing was translated
mechanically from `book2_en.py`, and nothing was seeded from `book1_nl.py`.

* `STOP = {oog, bestand, frequenties}` — the three words whose technical sense
  is honest in one chapter and ordinary Dutch everywhere else. `oog` is the
  book's own "onder het oog van de alvleesklier"; `bestand` is both *resistant*
  and an ordinary noun; `frequenties` is allele frequencies in one chapter and
  the firing rate of a muscle spindle in two others.
* `DROP = {drager, soorten, basen, base (DNA), cultuur, cultuur (dier)}`.
  Two of these are Dutch-only collisions:
  * **`drager`** is the carrier of a recessive allele *and* the NAD/electron
    carriers of photosynthesis and respiration *and* the pollen carrier of the
    flower chapter — one Dutch word for four English ones. Dropping it costs
    the disease chapter ~117 of its own links; keeping it would have shipped
    ~27 links from the respiration and photosynthesis chapters into a genetics
    definition. The wrong link is the more expensive error, and English DROPs
    `carrier` for the same reason.
* **`soort` is NOT dropped — the homograph was resolved in the prose.**
  Dutch `soort(en)` is both *species* and *kinds/sorts*, and after the canon
  fix that made `species` a live English term (272 links across 23 files), the
  cost of dropping it rose to 272 links. But `EXTRA_PROTECT` had nothing to
  key on: most of the *kinds* uses are a bare numeral plus `soorten`, which is
  exactly how the species chapters count species. So all **51** *kinds* sites
  were rewritten to `type / typen` instead — "twee typen fotoreceptoren",
  "twintig typen aminozuur", "de drie typen puntmutatie", "wat voor type
  indringer", "twee typen bewijs" — which is what a Dutch biology text says
  for a cell or receptor **type** anyway, so the prose improved rather than
  merely became linkable. `soort` now means *species* everywhere in the
  volume; it links 259 times, and every one of the 34 links outside the six
  species chapters was read back and is the species sense.
* `EXTRA` — 21 entries, each counted in the bodies first, each single-sense.
* `EXTRA_PROTECT = [vergroting van de hersenen]` — `vergroting` is the
  microscope's magnification in 13 of its 14 uses; the fourteenth is the
  enlargement of the brain in the human-evolution solutions. `STOP` would have
  cost the other thirteen, so the one phrase is masked instead.
* `NOT_A_TERM` deliberately left unset, so the English default applies.

## Samples read back, with verdicts

1. **Chapter 8 (grade 12), opening.** "Zet een takje waterpest ondersteboven
   in een pot water onder een lamp, en er stijgt een stroom belletjes op uit
   de afgesneden steel: zuurstof, om de paar seconden een belletje, sneller
   als de lamp dichterbij wordt gebracht, en gestopt zodra hij uitgaat."
   *Verdict: native.* `waterpest` is the Dutch name of *Elodea*, the
   verb-second inversion after the opening imperative is Dutch word order, not
   an English clause order carried over.
2. **Chapter 13 (grade 12), opening.** "Dertig milliseconden liggen er tussen
   de tik en de schop: te weinig voor de hersenen, te weinig zelfs voor een
   beslissing." *Verdict: native.* The expletive `er` and the fronted subject
   are what Dutch does with this sentence; a literal rendering would have
   produced "Dertig milliseconden scheiden…", which is a calque.
3. **Chapter 10 (grade 12), definition.** "De bloedglucosespiegel is een
   *geregelde* grootheid: een waarde die bij een streefwaarde wordt gehouden
   door een stelsel dat haar meet en bijstuurt." *Verdict: native.*
   `streefwaarde` is the Dutch control-theory word a school text uses for a
   set point; `set point` and `instelpunt` would both have read as translation.
4. **Chapter 12 (grade 12), exercise stem.** "Leg uit waarom alleen al de
   vernietiging van de helper-T-cellen zowel de arm van de antistoffen als die
   van de dodende cellen uitschakelt, met de figuur van de organisatie."
   *Verdict: native, and in the Book 1 register* — bare imperative, `zowel …
   als`, no `u`.
5. **Chapter 7 (grade 12), solution 15.** "Elk veld met een hybridevariëteit
   is genetisch identiek, en streken telen enkele hybriden: de
   verscheidenheid is versmald. De boer maakt geen zaad meer en hangt elk jaar
   van de leverancier af." *Verdict: native.* `hangt … af` with the separable
   prefix at the clause end is the Dutch the sentence needs.

## Divergences from the English source, deliberate and recorded

Every one is drawing code that the `id_apply` `draw` census cannot blank, so
it was written by a targeted post-write edit rather than through a range-level
`!draw` opt-out (which would have disabled the census for the whole file).

* `\foreach` label lists (they carry visible text but are not `node {...}`):
  g10-02, g11-01 (two), g11-06, g10-05, g12-04, g12-13.
* `symbolic x/y coords` **together with** the coordinate names of their
  `\addplot ... coordinates {(name,value)}` lines, which must match:
  g10-03, g10-05, g10-08, g10-10, g11-06, g11-12, g12-05, g12-09, g12-14.
* g12-04: the `\matrix of nodes` character table (species rows and character
  header) — matrix cells are not `node` text and are compared byte for byte.
* Five overfull boxes introduced by longer Dutch strings were removed by
  shortening figure labels, never by a trailing `%`: g11-05 (`hemoglobineketen`
  → `keten van hemoglobine`, an unbreakable 16-letter compound), g11-11 (five
  opsin-tree labels), g12-05 (two skeleton labels), g12-06 (one leaf label),
  g12-09 (`text width` of one flow-chart box widened 2.8 cm → 3.2 cm).
* g12-09: `mitochondrium` normalised to `mitochondrion` (16 sites) to match
  the spelling grade-10 and grade-12/02 already used, and the `\index` key with
  it. Both are correct Dutch; using two of them split one term in the harvest.

## Defects found in the ENGLISH canon (both reported; one now fixed upstream)

1. **Fixed in the canon after this report.**
   `parts/grade-12/07-domesticated-plants.tex`, the artificial-selection
   figure: the ancestor node read **"wild mustard (one species)"**, but the
   six crops drawn from it — kale, cabbage, Brussels sprout, kohlrabi,
   broccoli, cauliflower — are all *Brassica oleracea*, i.e. wild **cabbage**.
   The Dutch edition had already written `wilde kool`, because `wilde mosterd`
   producing broccoli would read as an error to a Dutch pupil; the English now
   reads `wild cabbage`, so the Dutch is a faithful rendering and not a
   divergence. Exercise 12 of the same chapter separately, and correctly, uses
   a real wild mustard as the herbicide-tolerance recipient — the two uses are
   not the same plant.
2. **Held for cross-edition reconciliation.** The proposition
   `prop:g12:respiration-fermentation:fermentation` is reachable in English
   **only** through the capitalised string `Fermentation`, a sentence-initial
   `\emph` that the harvest keeps as a term of its own; no `\omterm` actually
   points at it, so it is an orphan target. Any language whose word for
   *fermentation* is not capitalised there loses it. A `NO_CAPITAL` entry in
   `book2_en.py` is the lever; the fix changes the English target set, so it
   waits until all seven editions can be relinked together.

## Gate bugs hit

1. **Fixed in the gate after this report.** `check_latin_prose.py`'s
   `_word_count()` counted `[A-Za-z]{2,}` runs, so a hyphenated compound scored
   as two words and `Crossing-over` — a legitimate Dutch environment title —
   landed in the *blocking* multi-word tier and failed the whole year. It was
   retitled `De crossing-over` as a workaround; with the gate now counting a
   hyphenated compound as one word, the title is **restored to
   `Crossing-over`**, which is this edition's own convention for a title that
   is nothing but the term being introduced (`ATP`, `Fagocytose`, `Neuron`,
   `Reflex`, `Symbiose`, `Vaccin`). It now sits in the `title-1word` advisory
   tier and grade-12 still passes.
2. **Left as a reword, by agreement.** The `dup` class fires on a line that is
   byte-identical to its English twin *because the differing word wrapped to
   the next line* (`grade-12/solutions/05`, item 6). That is inherent to a
   line-based comparison and loosening it would blind the gate to genuinely
   absorbed lines, so the resolution is the reword, not a gate change.

## Why not 100

* **Link density is 90 % of English, not 100 %.** This is structural, not a
  defect: Dutch welds compounds and `tools/termlink/morphology.py`
  deliberately refuses to match inside one, so `spiercellen`, `bloedcellen`,
  `kankercellen` and `zenuwcellen` cannot carry the `cel` link that English's
  two-word "muscle cells" gets for free. 89 % is above the 85 % this
  repository's Book 1 `nl` edition reached, and the `EXTRA` list closes every
  gap that a countable surface form could close.
* **One English target has no Dutch counterpart.**
  `def:g10:exercise-and-energy:vo2max` is linked once in English, on the
  spelled-out phrase "maximal oxygen consumption"; the Dutch chapter writes
  the symbol `$\dot V\!\mathrm{O_2}$max` in all eight of its uses, which is
  what a Dutch sports-physiology text does, and a symbol cannot carry a link.
* **`drager` is dropped, not disambiguated.** It is a genuine
  one-word-for-four-senses collision in Dutch (allele carrier / NAD carrier /
  electron carrier / pollen carrier). `EXTRA_PROTECT` could in principle mask
  the wrong sense phrase by phrase, but the carrier-molecule uses have no
  stable lexical neighbourhood to key on, so ~117 correct links in the disease
  chapter are given up to avoid ~27 wrong ones. `soort` had the same shape and
  was solved the other way, by rewriting the prose — that route was open
  because *kind* has a good Dutch word of its own (`type`) and *carrier* does
  not.
* **The 21 one-word advisories of the twin-comparison gate.** Each was read;
  each is a real Dutch word (`mitochondrion, vacuole, product, aorta,
  meniscus, codon, tyrosine, hypothalamus, thalamus, python, gorilla, stroma`,
  plus Latin binomials). They are correct, but they are also the class in which
  a genuine residue would hide, so the score is not a perfect one.
