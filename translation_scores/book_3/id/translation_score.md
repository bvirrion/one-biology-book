# One Biology Book 3 — Indonesian (`id`) edition: self-score

**Date:** 2026-09-06
**Scope:** `one_biology_book_3_university_year_1_id.tex` — 29 chapters + 29
solutions files (University Year 1), 58 files, 361 pages.
**Quality bar:** *native academic*. Not "is this a correct rendering of the
English?" but "would an Indonesian biologist writing a first-year university
volume from scratch have written these sentences?" The register reference is
this workspace's own physics `bachelor-1` `id` edition — same stage, same
exercise machinery — measured before the first chapter was written: **0
`kamu`**, formal `Anda` only where the English addresses the reader directly.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | university lecture register: bare imperatives (`Hitunglah` 404, `Jelaskan` 108, `Sebutkan` 46, `Nyatakan` 41, `Ramalkan` 34, `Bandingkan` 32, `Bahaslah` 27), **0 `kamu`**, `Anda` only 3 times (the three exercises whose English says "would you") — the physics `bachelor-1` `id` ruling, held |
| Terminology | high | 96 | Indonesian university-biology vocabulary throughout (`relung`, `kesintasan`, `daya dukung`, `tabung tapis`, `arus lawan`, `pita Kaspari`, `riam trofik`, `utang kepunahan`); Latin binomials, domain names, DNA/RNA/ATP/NADPH untouched; every `\index` key Indonesian |
| MT-artifact freedom | high | 96 | twin-comparison gate clean of multi-word findings; 79 one-word advisories, all true cognates (`epidermis`, `endodermis`, `stoma`, `mesoderm`, `lumen`, `plasma`, `mitosis`, `turgor`, `virus`, `nitrogen`), proper names (`Michaelis--Menten`, `Henderson--Hasselbalch`, `lynx`) or the `k_{\text{cat}}` subscript |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 58 files; log 0 errors / 0 undefined / 0 overfull / 0 `nullfont`; no "invalid in math mode" |
| Cross-references | gated | 100 | 0 undefined references; label sets identical to the English file by file |
| Figures and captions | — | 96 | 122 `tikzpicture`s, 185 `omfigure`s, 85 image paths, 58 `\addlegendentry`, 7 `symbolic coords` lists and all 69 `\foreach` label lists handled; 12 figures re-flowed to clear Indonesian-length overfulls |
| Solutions | — | 96 | all 29 solutions twins translated; 377 `\begin{solution}` keys, exercise/solution parity gated; weekend-problem answer numbering gated (gate 11) |
| Defined-term links | — | 95 | 5,827 links on 185 targets (English 5,495 on 179) — 106 % of English density; 26 homograph families found by the two censuses and stopped |

## Measured state

```
files on disk             58   (29 chapters + 29 solutions)     = English
.fls files inputted       58                                    = English
pages                    361                                    (English 339)
LaTeX errors               0                                    = English
undefined references       0                                    = English
Overfull boxes             0                                    = English
nullfont warnings          0                                    = English
"invalid in math mode"     0                                    = English
TeX accent escapes         0                                    (Indonesian is plain ASCII)
\qty occurrences       2,977                                    = English
\text{...}                81, all translated                    = English
\includegraphics          85                                    = English
\begin{tikzpicture}      122                                    = English
\begin{omfigure}         185                                    = English
\addlegendentry           58                                    = English
symbolic x/y coords        7                                    = English
\foreach                  69                                    = English
\index{} occurrences     568                                    = English
distinct \index keys     544   (English 544) — every key Indonesian
\begin{exercise}         348                                    = English
\begin{solution}         377                                    = English
\omterm links          5,827   (English 5,495)
distinct link targets    185   (English 179)
check_translation.sh   PASSED (gates 1-11)
```

## What the two collision censuses found

The per-target frequency census and the per-target chapter-set census were run
against the English twin after every link pass. The first pass shipped 7,142
links on 189 targets — 30 % above English — and the excess was almost entirely
one defect class: an Indonesian index key that is also an ordinary word.

Twenty-six words were stopped, each verified against its own occurrences first:

* `air` (water) — 370 links; English links `hydrogen bonds`, never `water`.
* `laju` (rate) — 143 links to the enzyme-kinetics definition from
  `laju alir`, `laju pertumbuhan`, `laju kelahiran`, `laju serangan`.
* `energi`, `materi`, `informasi` — 238 links to "an organism exchanges
  matter, energy and information"; each is an everyday noun.
* `saluran` (channel / duct / tract) — linked the ion-channel definition from
  `saluran pencernaan`, `saluran udara`, `saluran xilem`. The 20 legitimate
  ion-channel links were given up rather than ship ten wrong-sense ones:
  Indonesian has one word where English has three.
* `halus` and `kasar` (smooth / rough ER) — 62 links, nearly all from
  `usus halus`, `akar halus`, `produksi kasar`, `asupan kasar`.
* `bersaing` (to compete) — 23 links to *competitive inhibition* from
  `asas penyisihan bersaing` and `spesies bersaing`.
* `asam`, `polar`, `ciri`, `pembawa`, `pompa`, `sumber`, `penampung`,
  `rangka`, `hidrostatik`, `memisahkan`, `nutrisi`, `reproduksi`, `relasi`,
  `penumpukan`, `plasma` — same shape, each documented in
  `tools/term_config/book3_id.py`.

Two further collisions could not be reached by a word list and are masked with
`EXTRA_PROTECT`: `batang otak` (brainstem — `batang` is a plant stem) and
`akar nyata` (a real root of a quadratic — `akar` is a plant root). One was
better fixed in the prose: the core of a villus was renamed `teras`, because
`inti` is the cell nucleus.

**A tooling finding worth recording:** `STOP` alone did *not* stop them.
`harvest.py` removes a stop-listed word from the global term table but still
feeds it to the per-chapter "local sense" table, so a chapter with only one
candidate definition links it anyway — `laju` still reached the rate
definition 38 times after `STOP`. Only `DROP`, which empties `terms`, `local`,
`nearest` and `primary`, actually removes a homograph. Both sets are populated
in this book's config, with that reason written down.

## Canon re-sync (2026-09-06, after the English fixes landed)

Four files were re-synced against three corrections to the English canon, and
the edition was re-linked, re-gated and rebuilt with no change to any measured
number:

* `solutions/21-gas-exchange.tex` answer 16 — this edition's own finding: the
  human moves a twentieth of the mass for three hundred times the oxygen, not
  "five times".
* `19-gene-expression.tex` — two stale cross-references (questions 12 and 11,
  found by the Arabic agent).
* `27-species-interactions.tex` and its solutions — the competition
  coefficient $\alpha$ changed from 1.6 to 1.4 (found by the Hindi agent), so
  answers 1 and 2 were retranslated: the isoclines now meet at $N_A = -69$,
  outside the positive quadrant, and A wins from any starting point.

The two solutions files were checked for the lengthening-edit trap the Spanish
agent found: whole-file math-span sequences are identical to their English
twins, `check_orphan_lines.py` reports 0 orphan English lines, and both files
still carry 13 `\begin{solution}` keys ending on `\end{solution}`.

## Where the remaining four points are

* The Indonesian edition still carries 6 % more links than English on 6 more
  targets. Every one was read; the excess is real usage (`inti`, `prokariot`,
  `takson`, `alveolus` are simply commoner words in Indonesian than their
  English twins), not a wrong sense — but it is not English parity either.
* Three targets are under-linked against English: the nucleus (5 vs 14),
  because Indonesian's bare `inti` was harvested onto the prokaryote/eukaryote
  definition rather than the nucleus one, and the transporters (14 vs 28),
  the price of dropping `saluran`.
* `parts/bachelor-1/id/01..19` were drafted before the collision censuses
  existed and were only audited by them, not written against them.
