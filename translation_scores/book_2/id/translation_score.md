# One Biology Book 2 — Indonesian (`id`) edition: self-score

**Date:** 2026-09-05
**Scope:** `one_biology_book_2_high_school_id.tex` — 36 chapters + 36 solutions
files (grades 10–12), 72 files, 401 pages.
**Quality bar:** *native academic*. Not "is this a correct rendering of the
English?" but "would an Indonesian biology teacher writing an upper-secondary
(SMA) volume from scratch have written these sentences?" The register
reference is this repository's own Book 1 `id` edition
(`parts/grade-1..9/id/`) — same series, same exercise machinery, one school
stage younger — measured before the first chapter was written, not after.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | bare imperatives throughout (`Jelaskan` 219, `Hitung` 80, `Sebutkan` 66, `Bandingkan` 52, `Nyatakan` 47, `Ramalkan` 36); `kamu`/`-mu` where the English addresses the reader, **0 `Anda`** — the Book 1 `id` twin's ruling, held |
| Terminology | high | 96 | Indonesian school-biology vocabulary; Latin binomials, DNA/RNA/ATP/NADP/HIV untouched; every `\index` key Indonesian |
| MT-artifact freedom | high | 96 | twin-comparison gate clean of multi-word findings on all three years; 27 one-word advisories across the three years, all international or anatomical Latin (`humerus`, `tibia`, `femur`, `aorta`, `plasmid`, `globin`, `orangutan`) |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 72 files; log 0 errors / 0 undefined / 0 overfull / 0 `nullfont` |
| Cross-references | gated | 100 | 0 undefined references; label sets identical to the English file by file |
| Figures and captions | — | 97 | 136 `tikzpicture`s, 184 `omfigure`s, 56 image paths, 23 `\legend` sites, 12 `symbolic coords` lists and all 98 `\foreach` label lists handled |
| Solutions | — | 96 | all 36 solutions twins translated; exercise/solution key parity gated |
| Defined-term links | — | 96 | 6,264 links on 105 targets (English 5,547 on 103) — 113 % of English density, matching the Book 1 `id` edition's 110 % |

## Measured state

```
files on disk             72   (36 chapters + 36 solutions)     = English
.fls files inputted       72                                    = English
pages                    401                                    (English 379)
LaTeX errors               0
undefined references       0
Overfull boxes             0
nullfont warnings          0                                    = English
"invalid in math mode"     0
TeX accent escapes         0                                    (Indonesian is plain ASCII)
\qty occurrences       1,186                                    = English
\text{...}                 9, all translated                    = English
\includegraphics          56                                    = English
\begin{tikzpicture}      136                                    = English
\begin{omfigure}         184                                    = English
\legend/\addlegendentry   23                                    = English
symbolic x/y coords       12                                    = English
\foreach                  98                                    = English
\index{} occurrences     182                                    = English
distinct \index keys     170   (English 171) — every key Indonesian
\omterm links          6,264   (English 5,547)
distinct link targets    105   (English 103)
check_translation.sh   PASSED for grade-10, grade-11, grade-12 (gates 1–10)
check_indonesian_prose.py  OK on all 72 files (gate 8)
check_latin_prose.py   no multi-word findings in any of the three years (gate 9)
check_orphan_lines.py  0 orphan English lines (gate 10)
decimal separator      point everywhere: 0 "\d,\d" in prose, 0 in \qty/\num
hyphen at line end     0 hits for [a-z]-\s*$  (the Indonesian-specific sweep)
siunitx unit audit     exactly 6 sites, all mmol/L               = English
```

## Censuses run, and what each found

* **`\index{}` key-set diff against the English twin, run after the last file
  landed.** 182 occurrences on both sides and identical per file. 22 of the
  170 distinct keys are byte-identical to English and every one is an
  international term or an ordinary Indonesian word: `AIDS, ATP, DNA, RNA,
  alveolus, antigen, diabetes, diploid, doping, haploid, insulin, intron,
  lipid, meiosis, mitosis, mutagen, neuron, opsin, protein, stoma, tendon,
  transgenesis`. Zero English residue.
* **`\omterm` per-target frequency diff against English.** Eleven targets sit
  well above their English count. Each was read site by site; the honest ones
  were kept and the dishonest ones removed (below). The largest honest
  divergences are `def:g10:universal-dna:nucleotide` (142 vs 54, because
  Indonesian never writes "asam dan basa" so `basa` is single-sense here and
  English has to DROP it) and `prop:g11:antibiotic-resistance:mechanisms`
  (85 vs 2, because English STOPs `resistant` for insulin-resistant tissues,
  which Indonesian calls `resistansi insulin` — a different word).
* **`\omterm` chapter-set census — the one that actually finds collisions.**
  It flagged `def:g11:the-eye:parts` reaching ten grade-12 chapters. Reading
  every one found four genuine homographs, now protected:
  `mata uang` (currency — ATP is the cell's currency, chapters 8 and 9),
  `air mata` (tears, chapter 11), `semata-mata` (solely, chapter 3, reached
  through the `HEAD` hyphen rule) and the figurative `mata manusia` of
  chapter 7. The same census found `tahannya` in the grade-12 meiosis caption
  meaning *the wait*, not *resistant*; the sentence was reworded, and two
  `pembawa` in the plant chapter meaning *pollinator*, not *allele carrier*,
  reworded to `pengantar`. **Nine wrong-sense links removed in all.**
* **`\text{...}` census over chapters and solutions.** 9 sites, all
  Indonesian (`\text{otot}`, `\text{beban}`, `\text{energi}`,
  `\text{cahaya, klorofil}`).
* **`\legend` / `\addlegendentry` and every `\foreach` label list by eye.**
  23 legends and 12 `symbolic coords` lists translated, each with its matching
  `coordinates {(...)}` line rewritten in the same edit — never with a
  file-wide `!draw` opt-out.
* **The hyphen sweep, run after the last file landed.** `[a-z]-\s*$`: zero
  hits, so no split hyphen can be read as a reduplication mark.
* **siunitx argument audit** (macro names blanked first): exactly the six
  `mmol/L` sites the English canon has, and nothing else.

## What the register measurement decided

Measured against `parts/grade-1..9/id/` before writing: 0 `Anda`, 127 `kamu`,
bare imperative exercise stems. Book 2 holds the same line — 0 `Anda`, 33
`kamu` plus 100 `-mu` enclitics, and 599 bare imperatives — but with the
adult, experiment-driven vocabulary the volume asks for: `Bukti percobaan`
for `[Evidence]`, `Soal akhir pekan` for the weekend problem, `Bagian I–IV`
for its parts, and the modern-lecture register (`pengamatan`, `penyandian`,
`pemaduan`) rather than the primary-school one.

## What was found in the shared tooling

* **`tools/termlink/morphology.py` denied `WORD_TAIL` to any term ending in
  `s`** (`NO_TAIL_END = ("s", "$", "]", ")")`). That entry is correct for
  English, whose tail is the PLURAL `(?:e?s)?` — *species* + *s* would be
  *specieses*. Indonesian's tail is not a plural at all: it is the ENCLITIC
  `-nya`, which attaches after `s` exactly as after any other letter. Every
  term of this volume ending in `s` therefore lost its commonest Indonesian
  form. **Reported, and now fixed generally**: `morphology.py` reads an opt-in
  `TAIL_AFTER_S` (default off, so en/fr/nl/es/pt/hi/ar patterns are
  byte-identical), and `tools/term_config/lang_id.py` sets it to `True` with
  the enclitic-vs-plural reason beside it. `"$"`, `"]"` and `")"` stay
  suppressed for everyone, since those end mathematics, not a word.

  The flag replaced eleven hand-declared `EXTRA` forms with none, and reached
  **more** than the hand list did: 6,253 → 6,264 links, 220 → 209 linkable
  terms. Three forms the enumeration had missed:
  - `pulau pankreasnya` (4) — a MULTI-word term whose last word ends in `s`,
    which is easy to overlook when enumerating single words by eye;
  - `plastisitasnya` (1) — the `EXTRA` term declared for the affix gap below
    itself ends in `s`, so the hand list could not have inflected it;
  - `kloroplasnya` (4) — **the case a hand list cannot express at all.**
    `kloroplas` is one of the four ambiguous terms; `EXTRA` can name only one
    label, so this form was deliberately left unlinked. The derived tail sends
    it through `AMBIG_POLICY` instead, and it resolves 3 → the grade-10
    organelle definition (the three sites that precede the grade-12 one) and
    1 → the grade-12 photosynthesis definition. Exactly right, and only
    reachable by derivation.

  Every one of the 14 `-nya` forms the flag now reaches was read in context
  before the flag was switched on; all are the intended sense, and no
  Indonesian word in this corpus is a term-ending-in-`s` plus `nya` by
  accident. Both censuses were re-run after the switch: the chapter-set census
  is unchanged — the 11 new links all landed in chapters that already linked
  those targets, so the flag introduced no new collision.

* **A definition whose display opens its sentence is harvested capitalised
  only.** `\emph{Xilem}` and `\emph{Floem}` open their bullets, so
  `prop:g12:plant-rooted-life:saps` collected 1 link where English collects
  15; the fifteen lowercase uses in the surrounding prose matched nothing.
  Declared in `EXTRA`, which is the right local fix. This is the same shape as
  the `Fermentation` orphan in this volume and the `Sorting` orphan in Book 1
  — **a general property of `harvest.py`, not an Indonesian one.**

## Defects found in the ENGLISH canon (reported, not fixed)

None new. The four wave-1 canon fixes (the `species` orphan target, the
colchicine crocus, the "two agents" of the plant problem, and the
`mmol/L` conversion) were already in the tree when this edition started and
are inherited clean. The 258 straight ASCII `"` quotations remain in the
English files and are harmless here: this edition uses LaTeX ``…'' pairs
throughout and copies none of them.

## What was added to `tools/check_indonesian_prose.py`

One append-only pattern, with its reason in a comment beside it, and the loop
at the residual-English stage extended to run it:

```python
WORK_TITLE = re.compile(r"Anatomy\s+and\s+Physiology")
```

**Why it is unreachable otherwise.** The grade-12 chapter 14 image credit
names its source work exactly as it is published — "Ilustrasi dari OpenStax
\emph{Anatomy and Physiology}, CC~BY~3.0." — and a bibliographic title is not
translatable prose: the fr, es, pt and nl editions all keep it verbatim, and
the licence identifier beside it is already exempted by the existing
`ATTRIBUTION` pattern. Left ungated, the conjunction `and` fires on
`ENGLISH_WORDS` and there is no way to reword a title. It is blanked exactly
the way `ATTRIBUTION` is, so the surrounding credit prose stays fully gated.

Re-validated on both controls **inside the scratchpad, never in a live
language directory**: the English control (`grade-12/14`, `grade-11/04`) still
fires 2,917 issues in 2 files, and the live Indonesian tree is silent on all
72 files.

Earlier in the run, the same file gained two other append-only entries, also
documented in place: `AMINO_ACID` (the twenty three-letter symbols, needed by
the grade-11 genetic-code table, where `His` lower-cases into the English
possessive) and `"minimal"` in `NOT_GATED` (ordinary Indonesian per KBBI —
*medium minimal*, *suhu minimal* — which fired on the correct grade-11
sentence about Beadle and Tatum's minimal medium).

## Why not higher than 96

* The link graph is 13 % denser than English. Every link was audited by the
  two censuses and each surviving one is honest, but a denser graph is a
  different reading experience from the English volume's, and two targets
  (`def:g11:the-eye:parts` at 104 against 12, `prop:g11:antibiotic-resistance:
  mechanisms` at 85 against 2) exist only because English chose to STOP a word
  whose Indonesian translation does not collide. A reviewer could reasonably
  prefer parity over honesty here.
* `prop:g12:respiration-fermentation:fermentation` is an orphan target, as it
  is in English and for the same recorded reason (`Fermentasi` / `Fermentation`
  in `STOP`). It is left orphaned rather than fixed unilaterally, so the
  editions stay comparable.
* Five figures needed their node text re-broken to fit the Indonesian, which
  is longer than the English at every one of them; the layouts are correct but
  are not identical to the English ones.
* Switching `TAIL_AFTER_S` on in `tools/term_config/lang_id.py` is a change to
  the shared Indonesian language config, and Biology **Book 1 `id` reads the
  same file**. Its link pass has not been re-run, so
  `link_defined_terms.py --book 1 --lang id --check` is red until it is: it
  would go 8,390 → 8,486 links across 38 files. All 96 are the same enclitic
  class and were verified honest (`alveolusnya` 16, `spesiesnya` 20,
  `jonjot ususnya` 16, `sinapsisnya` 14, `virusnya` 11, `usus halusnya` 6,
  `pubertasnya` 8, `diabetesnya` 3, `metamorfosisnya` 2, `penisnya` 2), but
  Book 1 `id` is a delivered edition whose own self-score quotes 8,390, so its
  numbers were not changed unilaterally from here.
