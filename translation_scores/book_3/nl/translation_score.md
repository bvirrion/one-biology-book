# One Biology Book 3 — Dutch (`nl`) edition: self-score

**Date:** 2026-09-06 (re-synced twice to the corrected English canon the same day)
**Scope:** `one_biology_book_3_university_year_1_nl.tex` — 29 chapters + 29
solutions files (University Biology, Year 1), 58 files.
**Quality bar:** *native academic*. The question is not "is this a correct
rendering of the English?" but "would a Dutch biologist writing a first-year
university volume from scratch have written these sentences?" The register
reference is this repository's own Book 2 `nl` edition
(`parts/grade-10..12/nl/`) — same series, same exercise machinery, one stage
younger; Book 3 lifts it to a university lecture without becoming stiff.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | 0 `u` / `uw` anywhere; the few second-person stems use `je`, as the Book 2 `nl` twin does; exercise stems imperative (`Bereken`, `Leg uit`, `Noem`, `Omschrijf`), matching the twin's distribution with `Bereken` promoted for the university level |
| Terminology | high | 96 | Dutch university-biology vocabulary; Latin binomials, taxon names, DNA/RNA/ATP/NADPH untouched; `bron`/`put` for phloem source/sink, `sluitcel`, `chylvat`, `band van Caspary`, `spaarzaamheid` for parsimony |
| MT-artifact freedom | high | 96 | twin-comparison gate clean of multi-word findings on all 58 files; the one-word advisories are real Dutch cognates (`apoplast`, `codon`, `taxon`, `mesoderm`, `plasma`) |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 58 files (labels, environments, solution keys, `\emph`/`\index` adjacency, math spans, drawing code, delimiters, braces, image paths) |
| Cross-references | gated | 100 | 0 undefined references; exercise/solution key sets identical chapter by chapter; 0 duplicate labels |
| Figures and captions | — | 96 | 122 `tikzpicture`s, 185 `omfigure`s, 85 image paths, 58 `\addlegendentry`, 7 `symbolic coords` lists and all 69 `\foreach` label lists translated by hand after the write |
| Solutions | — | 96 | all 29 solutions twins translated; gate 11 (`check_problem_numbering.py`) green on all 29 chapters, 1..k complete |
| Defined-term links | — | 95 | 5,040 links on 188 targets against English 5,495 on 179 — 92 % of English density, with full target parity plus 9 targets English still leaves orphaned |

## Measured state

```
files on disk             58   (29 chapters + 29 solutions)      = English
parts/bachelor-1 paths in the .fls                          58   = English
pages                    350                                      (English 339)
LaTeX errors               0
undefined references       0
Overfull boxes             0
nullfont warnings          0                                      = English
"invalid in math mode"     0
TeX accent escapes         0
\index entries           568                                      = English
\qty occurrences       2,969                                      = English
\includegraphics          85                                      = English
\text{...} fragments      22, all translated or international     = English
\omterm links          5,040 on 188 distinct targets               (English 5,495 on 179)
```

`check_translation.sh bachelor-1 nl`: **PASSED** (gates 1–11, including the new
`check_problem_numbering.py`), with all ten of this edition's gate-9 wordings
restored to the translator's own choice.

## What the Dutch edition had to solve that no other edition does

**Dutch welds its compounds, and `harvest.py` skips any `\index` key without a
space.** Thirty-three targets of the English twin were missing from the Dutch
harvest outright — not because the term was absent from the prose, but because
`water-use efficiency` is `watergebruiksefficiëntie` and
`Michaelis–Menten equation` is `michaelis-mentenvergelijking`. They were found
by a `comm` of the two target sets, never by eye, and every one is restored by
an `EXTRA` in `tools/term_config/book3_nl.py`. Six more (`peroxisoom`,
`wassen`, `xerofyt`, `signaalpeptide`, `uitwisselingsoppervlak`, `integrale
eiwitten`) were found by the same `comm` run against the *linked* target sets
after the first pass.

**`WORD_TAIL = (?:e?[ns])?` manufactures ordinary Dutch words**, and neither
`STOP` nor `DROP` can reach a derived form. The one that mattered:
`blad` + `-en` = **`bladen`**, which in this volume is never a plant leaf (that
plural is `bladeren`) but always the two *leaflets* of a lipid bilayer and the
leaves of a cow's omasum — nine links pointing at the leaf definition of
chapter 3, invisible to every gate. `EXTRA_PROTECT` is the only lever, and it
is what removed them.

**The tail also cannot build the plurals Dutch really uses.** `cel → cellen`,
`eiwit → eiwitten`, `aminozuur → aminozuren`, `orgaan → organen`,
`chromosoom → chromosomen`, `lysosoom → lysosomen`, `blad → bladeren`,
`taxon → taxa`: 34 `EXTRA` entries, each counted as an unlinked surface form in
the bodies first. Note what is deliberately **absent**: `genoom → genomen`,
because `genomen` is also the past participle of *nemen*.

**Nine homograph collisions were resolved in this file and one in the prose.**
The worst was Dutch-only: **`was`** is the wax of chapter 9 *and* the past tense
of *zijn* — 48 of its 49 occurrences are the verb. Also dropped: `vat` (xylem
vessel / blood vessel / Pasteur's flask / the hundred-litre vat of a rumen),
`bron` and `put` (the phloem's source and sink, but `bron` is also the limestone
*spring* that the whole of chapter 26 is built on), `knoop` (plant node / rope
knot / cladogram node), `kenmerk` (systematic character / ordinary feature),
`matrix`, `pomp` (the verb *pompen*), `snelheid` (reaction rate / plain speed,
57 wrong links), `scheidt` (resolves / separates / secretes, 12 wrong links).
The tenth, **`soort`** — species *and* "kind" — was resolved the way the Book 2
`nl` edition resolved it: the fourteen sites that meant *kind* were rewritten to
`type` / `typen`, which is what a Dutch biology text says anyway, so `soort`
now means species everywhere and links freely.

**Two collisions were resolved in the prose rather than the config**, because
the Dutch word was simply wrong: `vaten` in the animal chapters (chapters 1, 2,
4 and 12) is *blood* vessels, and now reads `bloedvaten`, so the word boundary
protects it and the plant sense keeps its links; and `de vaten van Pasteur`
(chapter 15) are flasks, now `de kolven van Pasteur`.

**Every suppression in this edition uses `DROP`, and `STOP` is empty.** The
Indonesian Book 3 agent measured that `STOP` does not suppress a homograph at
all — its word kept 38 links after being stopped — so this was checked here on
the re-sync: `book3_nl.py` has `STOP = set()` and 30 `DROP` entries, and each
dropped surface form was then counted in the linked bodies and carries 0 links.
The one apparent survivor, `vaten` (11 links), is not a leak: only the singular
`vat` is dropped, and the 11 are the plant xylem vessels of chapters 23 and 24,
the blood vessels having been rewritten to `bloedvaten` in the prose.

**Several English `DROP`s were deliberately not repeated**, because Dutch welds
the compound that made the English word ambiguous: `plasma` (Dutch has
`plasmamembraan`, `cytoplasma`), `zuur` (`aminozuur`, `nucleïnezuur`),
`substraat` (chapter 28's substrate is `ondergrond`), `carrier` (the NAD
carriers are `dragers`), `operator` (only the *lac* operator), `stengel` (the
stem cell is a `stamcel`). Each of those is a Dutch gain over English, and each
was checked against every occurrence in the volume before it was kept.

## Verification actually run

- `tools/id_apply.py` on all 58 files; four rejects during the run
  (a math span rewrapped across a line, an `\emph` count, an extra `$\Psi$`, a
  swallowed `\end{proof}`) all fixed at the source, never worked around.
- `bash tools/check_translation.sh bachelor-1 nl` — PASSED, after fixing the
  20 untranslated `\begin{proof}[Evidence]` / `[Partial proof]` titles the gate
  caught in chapters 21–29 and four untranslated environment titles the gate
  caught in chapters 4, 13 and 20.
- Hygiene sweep (elision apostrophe at end of line, line starting with
  punctuation, hyphen at end of line, TeX accent escapes, non-ASCII inside
  `\qty`/`\unit`/`\num`, zero-width and bidi controls, drafty ellipses) — clean,
  re-run after the last file landed and again after the overfull sweep.
- `\text{…}` census over chapters **and solutions**: `\text{blood}`,
  `\text{cell}` and eleven `\text{out}` were still English; all fixed.
- `\index` key-set diff against English: 568 = 568, and the 82 identical keys
  are international terms that are identical in Dutch.
- **Both collision censuses**: per-target frequency against English and
  per-target chapter set. The chapter-set census is what caught `bladen`,
  `vaten`, `snelheid` and `scheidt`; the frequency census caught two
  mis-targeted `EXTRA`s of my own (`membranen` pointing at the integral-protein
  definition, `bacteriën` at the prokaryote/eukaryote one, where English links
  neither) and two more (`organellen`, `wortelharen`) pointing at a different
  definition from the one English chose.
- Per-target display census: no target renders one notion two unrelated ways.
- Forced `latexmk -g` after every file creation and after the link pass;
  `.fls` count checked each time.

## Three samples, with verdicts

**1 — chapter 21, opening (native, rhythm kept):**

> Een liter lucht bevat dertig keer meer zuurstof dan een liter water, weegt
> achthonderd keer minder, en laat zuurstof er tienduizend keer sneller
> doorheen diffunderen. Een forel moet voor elke milligram zuurstof die zij
> opneemt honderdvijftig gram water over haar kieuwen laten stromen […]

Verdict: **pass**. The three-clause opening survives intact; `laat … doorheen
diffunderen` is the natural Dutch separable-verb construction, not a calque of
"lets oxygen diffuse through it".

**2 — chapter 13, opening (imperative, then the argument):**

> Giet waterstofperoxide op een doorgesneden aardappel en het schuimt: één
> enkel molecuul katalase in de cellen van de aardappel splitst elke seconde
> veertig miljoen moleculen peroxide, een reactie die aan zichzelf overgelaten
> jaren zou duren.

Verdict: **pass**. `aan zichzelf overgelaten` is the idiom; the English "left
to itself" would have produced `alleen gelaten`, which is what a machine gives.

**3 — chapter 24, the cohesion–tension theorem:**

> Water stijgt in het xyleem omdat het van boven wordt *getrokken*, niet van
> onder geduwd. […] Om een kolom van hoogte $h$ tegen de zwaartekracht in te
> houden is een spanning $\rho g h$ nodig […]

Verdict: **pass**. `tegen de zwaartekracht in te houden` uses the Dutch
circumposition; the emphasis contrast *getrokken / geduwd* is preserved where a
literal rendering would have flattened it.

## Why not 100

- **Link density is 92 % of English (5,040 against 5,495), and it cannot reach
  100 %.** Dutch welds `celmembraan`, `bladoppervlak`, `eiwitsynthese`, and the
  word boundary deliberately refuses to link inside a compound — correctly, but
  it costs `def:b1:cell-unit-of-life:cell` 114 links and
  `def:b1:flowering-plant-organization:organs` 100 against their English twins.
  Loosening the boundary would link `lengte` inside `golflengte`; the deficit is
  the right side of that trade, not a defect, but it is a real difference from
  the English reading experience. −2
- **Three drops cost correct links.** `kenmerk`, `weerstand` and `matrix` each
  carry the defined sense in perhaps half their uses, and `DROP` is all-or-
  nothing; a per-phrase `EXTRA_PROTECT` list would have recovered some, at the
  cost of a config nobody can maintain. −1
- **The `\legend`/`node` one-word advisories were read, not silenced.** 74 of
  them are genuine Dutch cognates (`epidermis`, `mesoderm`, `plasma`,
  `endodermis`, `codon`); none is residual English, but a reader who wanted a
  fully Dutch figure would still see Latin anatomical labels such as
  `lamina muscularis mucosae`, which Dutch anatomy does use. −1

## Defects found in the ENGLISH canon (all now fixed by the coordinator)

1. **`solutions/16-biosyntheses-integration.tex` skipped `\textbf{12.}`** — 25
   questions, 24 answers. Checked against the problem's own model: question 12
   asks where the 160 g of glucose must come from (protein) and question 13 asks
   for the ATP the liver spends making it; the answer labelled **13** was
   question 12's, and question 13's was missing. Reported, not edited. English
   now carries both, and this edition has been re-synced: the Dutch answer was
   relabelled 12 and a Dutch answer 13 written to match.
2. **`def:b1:eukaryotic-cell:endomembrane` was badly under-linked in English.**
   The English prose writes `Golgi` 40 times but `Golgi apparatus` 6, and the
   harvested key was the two-word form, so the commonest name of one of the
   book's basic organelles linked **once** in the whole volume — while the Dutch
   edition, which writes `golgi-apparaat` throughout, linked it 30 times.
   `"Golgi"` is now in `book3_en.py` and the target went 30 → 63 links in
   English (Dutch 67).
3. **Targets the English edition left orphaned.** Ten collected 0 links in
   English and 2–39 in Dutch, because the English key is `\index`ed twice (so
   `AMBIG_POLICY = "drop"` drops it) or the phrase never recurs in the English
   prose. Two have since been picked up in English (`Chargaff`,
   `checkpoint(s)`) — the second added a target the Dutch harvest did not have
   either, now reached through `controlepunt(en)`. Nine remain Dutch-only:
   `def:b1:enzymes:rate`, `def:b1:organism-environment:levels`,
   `prop:b1:nucleic-acids:stability`, `prop:b1:body-plans-tissues:gutwall`,
   `prop:b1:digestion-absorption:routes`, `prop:b1:digestion-absorption:cellulose`,
   `prop:b1:ecosystem-organization:biomes`, `prop:b1:gene-expression:dogma`,
   `prop:b1:populations:densitydependence` and
   `thm:b1:plant-transport:cohesiontension`.

Two further English corrections landed in the same pass and are mirrored here:
the three-cycle permutation of answers 16/17/18 in
`solutions/25-populations.tex`, and two `\num{…}{g}` → `\qty{…}{g}` in
`17-genomes.tex` and `20-expression-control.tex`.

## Bugs found in the SHARED tooling

1. **`check_latin_prose.py` blocked fragments that are correct Dutch — fixed,
   and this edition's wording is fully restored.** Eleven multi-word fragments
   failed the blocking tier although every one is right Dutch (`muscularis
   mucosae`, `fructose-1,6-bisP`, `alanine, serine, glycine`, `gyrase (ATP)`,
   `$\approx 4\,\mathrm{H^+}$ per ATP` — whose only word, `per`, is Dutch).
   I had reworded each *for the gate* and said so. The gate now carries a
   per-language `ALLOWED_BY_LANG` set; after its first round and the four
   further words I supplied on evidence (`carrier`, `deoxyribose`,
   `hexokinase`, `galactose` — two -ose sugars, one -ase enzyme and the
   loanword Dutch membrane physiology uses), **all ten reworded fragments now
   carry the wording I preferred and gate 9 is green.** The eleventh,
   `type II: …, **met** plateau …`, I chose to keep with the preposition,
   because it is better Dutch there than the English apposition — so `type`
   and `plateau` were deliberately not requested for the list.

2. **Retracted: the applier does not break `\index{}` across lines.** I reported
   that `link_defined_terms.py --apply` had pushed four `\index{}` keys across a
   line break; the coordinator points out that `wrap_file()` is a pure in-place
   substitution with no wrapping code, and I could not reproduce it on the
   re-sync run either (`\index\{[^}]*$` = 0 after two further link cycles). The
   four broken keys were in my own written source and the earlier gate runs
   simply had not reached that file set. The symptom was real, the diagnosis was
   wrong, and gate 4 catches it either way.
3. **`harvest.py`'s "no space in the `\index` key" rule is a systematic tax on
   every compounding language.** It cost this edition 33 targets outright — and
   a 34th on the re-sync, `prop:b1:replication-mitosis:checkpoints`, whose Dutch
   key is the solid `controlepunt` — and it will cost the German or Danish
   edition the same. The Dutch and Indonesian configs both carry long `EXTRA`
   blocks that exist only to undo it. **Suggested fix:** make the rule opt-out
   per language (`ALLOW_SOLID_INDEX_KEYS = True` in `lang_nl.py`), the way
   `TAIL_AFTER_S` was made opt-in for Indonesian after Book 2.
