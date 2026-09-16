# One Biology Book 4 — Dutch (`nl`) edition: self-score

**Date:** 2026-09-16
**Scope:** `one_biology_book_4_university_year_2_nl.tex` — 27 chapters + 27
solutions files (University Biology, Year 2), 54 files, plus
`frontmatter/image-credits-book4.nl.tex` and
`tools/term_config/book4_nl.py`.
**Quality bar:** *native academic*. Not "is this a correct rendering of the
English?" but "would a Dutch biologist writing a second-year university volume
from scratch have written these sentences?" The register reference is this
repository's own Book 3 `nl` edition (`parts/bachelor-1/nl/`) — same series,
same exercise machinery, one year younger; Book 4 keeps its voice and raises
the technical level. The French Book 3 edition (`parts/bachelor-1/fr/`) was
used only as a sense check on two proofs.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | 0 `u` / `uw` / `jouw`; 8 second-person stems use `je`, exactly the Book 3 `nl` distribution; 0 `we` (the proofs use `men`/impersonal, as Book 3 `nl` does); exercise stems imperative (`Bereken`, `Leg uit`, `Noem`, `Formuleer`, `Voorspel`) |
| Terminology | high | 96 | Dutch university-biology vocabulary throughout: `atrium`/`ventrikel` (never `boezem`/`kamer`), `haarvat`, `slagvolume`, `rustpotentiaal`, `knopen van Ranvier`, `saltatoire geleiding`, `dwarsbruggencyclus`, `spaarzaamheid` for parsimony (the Book 3 `nl` choice), `erfelijkheidsgraad`, `soorten-oppervlakterelatie`, `keelingcurve`, `haber-boschproces` |
| MT-artifact freedom | high | 95 | twin-comparison gate: 7 multi-word findings, every one a correct Dutch/Latin fragment (see *Gate results*); the 56 one-word advisories are real Dutch cognates (`water`, `pilus`, `chiasma`, `zygote`, `arteriole`, `systole`, `axon`, `plateau`) |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 54 files (labels, environments, solution keys, `\emph`/`\index` adjacency, index count, math spans, drawing code, delimiters, braces, image paths) |
| Cross-references | gated | 100 | 0 undefined references; exercise/solution key sets identical chapter by chapter; gate 11 (`check_problem_numbering.py`) green on all 27 weekend problems |
| Figures and captions | — | 96 | 122 `tikzpicture`s, 181 `omfigure`s, 79 image paths, 57 `\addlegendentry`, the one `symbolic x coords` list and 39 `\foreach` label lists translated by hand after the write; figure pages read on the rendered PDF |
| Solutions | — | 96 | all 27 solutions twins translated; every numeric answer re-derived (which is how the ten canon defects below were found) |
| Defined-term links | — | 95 | 2,666 links on 157 targets against English 3,092 on 155 — 86 % of English density with full target parity plus two targets English leaves orphaned (`nervus vagus`, `principe van Fick`) |

## Measured state

```
files on disk             54   (27 chapters + 27 solutions)       = English
parts/bachelor-2/**/nl paths in the .fls                     54   = English
pages                    339                                       (English 321)
LaTeX errors               0
undefined references       0
Overfull boxes             0                                       = English
nullfont warnings          0                                       = English
"invalid in math mode"     0
TeX accent escapes         0
\index entries           621  (611 distinct keys)                  = English (611 distinct)
\qty occurrences       2,454                                       = English
\includegraphics          79                                       = English
\begin{tikzpicture}      122                                       = English
\addlegendentry           57, 51 translated, 6 identical by right  = English
\text{...} fragments      96, all translated or international      = English
\omterm links          2,666 on 157 distinct targets                (English 3,092 on 155)
```

`bash tools/check_translation.sh bachelor-2 nl`: gates 1–8 and 10–11 **PASS**;
gate 9 reports 7 multi-word findings, all false positives on correct Dutch
(listed below, with the one-line fix the shared tool needs).

## What this edition had to solve

**Dutch welds its compounds, and `harvest.py` only accepts an `\index` key
outside a definition when the key contains a space.** English `stroke volume`,
`length constant`, `pollen tube`, `species--area relation` all pass that test;
`slagvolume`, `lengteconstante`, `stuifmeelbuis`, `soorten-oppervlakterelatie`
do not. The first link run produced 103 targets against English's 155 — 54
targets missing, not one of them because the notion was absent from the Dutch
prose. They were found by a `comm` of the two `\omterm` target sets, never by
eye, and every one is restored by an `EXTRA` in `tools/term_config/book4_nl.py`
whose value is a label of *this* book and whose key is the surface the English
edition actually links.

**Two homographs.** `schors` is the root cortex, the bark of a tree and the
brain's motor cortex at once, and the linker put four wrong-sense links into
chapters 18 and 22; English links `cortex` nowhere, so `DROP` mirrors it.
`bloeden` — the verb "to bleed" — is manufactured by `WORD_TAIL` out of
`bloed`, and linked the heading `Deel III --- Bloeden.` to the definition of
blood; `DROP` cannot reach a form `WORD_TAIL` invents, so it is masked in
`EXTRA_PROTECT`. One more collision was fixed in the prose instead: chapter
19's `benoem de koppeling` (the metabolic-electrical coupling of the β cell)
would have linked to genetic *linkage*, and now reads `benoem de schakel
tussen beide`.

## Samples

1. ch. 17, opening — *Cut out a frog's heart and drop it into salt solution,
   and it goes on beating for hours.*
   → **Snijd het hart uit een kikker, leg het in een zoutoplossing, en het
   blijft urenlang kloppen** — the English imperative chain keeps its rhythm;
   Dutch needs the separable order `snijd … uit` and a comma splice the
   language actually uses.
2. ch. 26, opening — *He had put a chalk marker on a field … and dug it up in
   1871: it lay eighteen centimetres down.*
   → **Hij had in 1842 op een veld bij zijn huis een krijtmarkering gelegd en
   die in 1871 opgegraven: ze lag achttien centimeter diep** — time–place–
   object order, `krijtmarkering` for the chalk marker, and the resumptive
   `die` that Dutch prefers to a repeated noun.
3. ch. 20, theorem — *A membrane permeable to one ion … settles at the
   equilibrium potential at which the electrical force on the ion balances its
   diffusion.*
   → **komt tot rust op de evenwichtspotentiaal, waarbij de elektrische kracht
   op het ion zijn diffusie in evenwicht houdt** — `nernstpotentiaal` and
   `evenwichtspotentiaal` are the two names Dutch physiology uses, and both
   index keys carry them.
4. ch. 22, exercise 12 — *"Selection is blind to what it cannot see."*
   → **``Selectie is blind voor wat ze niet kan zien.''** — `selectie` is
   feminine in this register, so `ze`, not `het`; the quotation marks are the
   `` … '' pair the Dutch tree uses everywhere.
5. ch. 25, proposition — *the atmosphere has kept about 45 % of it (the
   airborne fraction).*
   → **de atmosfeer heeft er ongeveer \qty{45}{\%} van gehouden (de
   atmosferische fractie)** — `er … van` is the Dutch pronominal adverb the
   sentence needs; `atmosferische fractie` is the term Dutch climate texts use
   and is now a link target of its own.

## Why not 100

* Gate 9 still reports seven fragments (the tool cannot know that
  `megasporangium (nucellus)`, `zygote → embryo`, `recombinant`,
  `Ae.~tauschii`, `Quorum sensing` and a bare distance-matrix `tabular` are
  Dutch); a translator reading the report must check them by hand.
* Link density is 86 % of English. Full target parity is restored, but a
  welded Dutch compound is one word where English has two, so a sentence that
  gives English two chances to link gives Dutch one.
* Ten defects of the English canon had to be judged one at a time (below); two
  of them are corrected *inside math spans*, which is a deliberate divergence
  from a tree the gates otherwise keep byte-identical.
* Three figures needed a manual line break or a shorter label to keep the
  page free of overfull boxes (`04` tetrad captions, `14` ABC-model legends,
  `21` sarcomere labels): the Dutch words are simply longer.

## Deliberate divergences from the English tree

| Where | English | Dutch | Why |
|---|---|---|---|
| `solutions/17-heart.tex`, pb answer 19 | `$+12.9$`, `$21.9$` + "the parts interact" | `$+7.7$`, and "de drie bijdragen … tellen precies op tot het verschil van $16.7$" | 12.9 is the *output* at 180 beats, not the increment; the four contributions sum exactly, so the interaction remark is false |
| `solutions/18-blood-pressure.tex`, pb answer 14 | `= 0.630`, `R = 1.59` | `= 0.727`, `R = 1.38` | the five listed terms sum to 0.727 |
| `21-muscle-movement.tex`, sprint example | `\qty{80}{g}` of ATP, "a few grams" held | `\qty{800}{g}`, "enkele tientallen grammen" | 160 mmol/s × 10 s × 507 g/mol = 811 g; the store is 0.1 mol = 50 g |
| `solutions/21`, pb answer 15 | "a hundred times the free rise" | "tien keer" | 0.1 mmol/L against a 9.9 µmol/L rise is ten times |
| `solutions/25`, pb answer 24 | `\qty{4}{g/m^2}` | `\qty{20}{g/m^2}` | 205 t over 10⁷ m² |
| `25-biogeochemical-cycles.tex`, Evidence | "Hutchinson Forest at Hubbard Brook" | "Het proefbos van Hubbard Brook" | the site is the Hubbard Brook Experimental Forest |
| six more (ch. 1, 5, 6, 11, 14, 22) | see the report | corrected content translated | arithmetic or internal contradiction, each re-derived |

Every divergence keeps the `\qty`, `\index` and math-span *counts* the censuses
compare; only the numerals inside change.

## Gate results

```
tools/check_translation.sh bachelor-2 nl
  1-4  label / environment / solution-key / emph-index censuses   PASS
  5    line-broken \index keys                                    PASS (0)
  6    UTF-8, no TeX accent escapes                               PASS
  9    twin-comparison prose gate                                 7 findings, all false positives
  10   orphan English lines                                       PASS (0)
  11   weekend-problem answer numbering                           PASS (27/27)
tools/check_term_display_drift.py                                 59 targets with >1 display,
                                                                  each inflection, English varies too
tools/link_defined_terms.py --book 4 --lang nl --check            every file matches the config
latexmk -g (forced)   0 errors, 0 undefined, 0 overfull, 0 nullfont, 339 pp
```
