# One Biology Book 5 — Indonesian (`id`) edition: self-score

**Date:** 2026-09-17
**Scope:** `one_biology_book_5_university_year_3_id.tex` — 27 chapters + 27
solutions files (University Year 3), 54 files, 400 pages.
**Quality bar:** *native academic*. Not "is this a faithful rendering of the
English?" but "would an Indonesian biologist writing a third-year university
volume from scratch have written these sentences?" The sense reference is the
French (`fr`) Book 5 edition of wave 1 wherever a passage was ambiguous in
English, and this repository's own Book 4 `id` edition for continuity of
vocabulary: a reader moving from Year 2 to Year 3 meets the same words
(`silang dalam`, `koefisien silang dalam`, `hanyutan genetik`, `ukuran
populasi efektif`, `keheterozigotan`, `hubungan spesies--luas`, `utang
kepunahan`, `serpihan habitat`, `kebugaran`, `lungkang gen`, `terpancang`).

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | university-lecture register; `-lah` imperatives in exercise stems (`Jelaskanlah` 28, `Sebutkanlah` 14, `Ramalkanlah` 11, `Nyatakanlah` 10, `Hitunglah` 10, `Tunjukkanlah` 7, `Definisikanlah` 11, `Turunkanlah` 5, `Namailah` 5, `Ringkaslah`); **0 `kamu`**; `Anda` 32 times, every one where the English addresses the reader directly ("your kidneys filter…", "what further test would you run?") |
| Terminology | high | 96 | Indonesian university-biology vocabulary throughout (`hanyutan`, `pemancangan`, `pemfungsian baru`, `ceruk`, `kripta`, `pelipat ganda arus balik`, `bersihan`, `penghindaran naungan`, `gen senjang`, `gen aturan pasangan`, `kekutuban segmen`, `pematrian`, `kebugaran inklusif`, `tarian goyang`, `pusaran kepunahan`, `populasi layak minimum`); Latin binomials, gene symbols (`Xist`, `hunchback`, `Per`, `Cry`, `FoxP3`) and DNA/RNA/ATP/cAMP untouched; **898 distinct `\index` keys, one-to-one with English's 898** |
| MT-artifact freedom | high | 96 | twin-comparison gate (gate 9) clean of multi-word findings; 57 one-word advisories, every one a cognate (`Apoptosis`, `Virus`, `Sepsis`, `Insulin`), a proper name (`Needleman--Wunsch`, `CRISPR--Cas9`, `Dicer`, `Drosha`, `Argonaute`, `MutS/MutL`, `xeroderma pigmentosum`), a gene symbol (`\emph{Igf2}`), a math subscript (`osm`, 8×) or the Hox-cluster `\foreach` gene list |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 54 files (labels, envs, solution keys, `\emph`/`\index` adjacency, math spans, drawing code, delimiters, braces, image paths); log 0 errors / 0 undefined / 0 overfull / 0 `nullfont`; 0 "invalid in math mode"; `.fls` inputs 54 of 54 |
| Cross-references | gated | 100 | 0 undefined references; label set identical to the English twin file by file; 104 `\cref` calls, same targets |
| Figures and captions | — | 95 | 116 `tikzpicture`s, 177 `omfigure`s, 105 image paths, 116 `\foreach` lists and 4 pgfplots `symbolic coords` keys translated by hand; **16 figures re-flowed** after the first linked build because Indonesian labels run 15–25 % longer than English ones |
| Solutions | — | 96 | all 27 solutions twins translated; 351 `\begin{solution}` keys, exercise/solution parity gated; weekend-problem answer numbering gated (gate 11, 27 chapters OK) |
| Defined-term links | — | 96 | 2,934 links on **197** targets (English 2,672 on 188) — 110 % of English density, and **every one of English's 188 targets is reached** |

## Measured state

```
files on disk             54   (27 chapters + 27 solutions)     = English
.fls files inputted       54                                    = English
pages                    400                                    (English 365)
LaTeX errors               0                                    = English
undefined references       0                                    = English
Overfull boxes             0                                    = English
nullfont warnings          0                                    = English
"invalid in math mode"     0                                    = English
decimal commas in prose    0   (2,524 "d,d" matches, all TikZ/pgfplots
                                coordinates, byte-identical to English)
\qty occurrences       2,249                                    = English
\qtyrange                 36                                    = English
\num                     232                                    = English
\text{...}               210, all translated or kept as symbols = English
\includegraphics         105                                    = English
\begin{tikzpicture}      116                                    = English
\begin{omfigure}         177                                    = English
\foreach                 116                                    = English
\emph{}                1,328                                    = English
\index{} occurrences     911                                    = English
distinct \index keys     898   (English 898) — every key Indonesian
\begin{exercise}         324                                    = English
\begin{solution}         351                                    = English
\cref{}                  104                                    = English
\admitted                  8                                    = English
proof[Bukti eksperimental] 53   (English proof[Evidence] 53)    = English
definition/proposition/theorem/method/example/problem
                   127/59/34/26/54/27                           = English
\omterm links          2,934   (English 2,672)
distinct link targets    197   (English 188; all 188 reached)
check_translation.sh   PASSED (gates 1-11)
link_defined_terms --check    green
link_defined_terms (plain)    links to insert: 0 across 0 files
```

## What the two collision censuses found

Both censuses were run against the English twin after the final link pass: the
per-target **frequency** census (`|id|` vs `|en|` per target) and the per-target
**chapter-set** census (which chapters link a target in `id` but not in `en`).
The first pass shipped 3,023 links on 196 targets; the censuses raised 26
chapter flags and 7 frequency flags, and **thirteen of them were real
homographs**, every one minted by Indonesian rather than inherited from
English. All are handled by `STOP` (per-chapter fall-through) except six that
needed a narrow `EXTRA_PROTECT`:

* **`primer` — the one with no English counterpart.** Indonesian spells the PCR
  *primer* and the adjective *primary* alike, so `def:b3:genetic-engineering:pcr`
  had collected `struktur primer` (primary structure, ch. 7), `silium primer`
  (primary cilium, ch. 9) and `tanggapan primer` (primary response, ch. 16).
* **`perancah`** is a genome *scaffold* in ch. 4 and a *wading bird* (`burung
  perancah`) in ch. 20's countercurrent exchangers. English cannot collide there.
* **`laju kematian`** is Gompertz's *mortality rate* (ch. 24) and an ordinary
  population *death rate* (ch. 27, the first sentence of the definition of
  smallness). English writes "mortality rate" and "death rate" and never collides.
  `EXTRA_PROTECT`.
* **`vektor`** — the cloning vector of ch. 6 against the **eigenvector** of
  ch. 19's Oja rule (13 wrong links, the largest single family).
* **`perakitan`** — genome *assembly* against polymer, spindle and capsid assembly.
* **`bencana`** — microtubule *catastrophe* against `bencana galat` (error
  catastrophe), systemic catastrophe and `gangguan bencana` (catastrophic
  interference).
* **`lesi`** — the DNA lesion of ch. 3 against tissue, brain and endocrine lesions
  (41 links, most of them wrong before the fix).
* **`benih`** — the BLAST seed against plant seeds, seed banks, the prion seed and
  Paget's "seed and soil".
* **`toleransi`** — immunological tolerance against the glucose *tolerance* test.
* **`transduksi`** — phage transduction against sensory transduction.
* **`penghadang`** — the innate barrier against a leaky glomerular barrier.
* **`salut`** — the vesicle coat against the complement coat of ch. 15.
* **`daya pisah`** — crystallographic resolution against optical, angular and
  phylogenetic resolution.
* **`penyusunan ulang`** — viral *reassortment* against antibody class switching.
* `EXTRA_PROTECT` also covers **`domain publik`** (the *public domain* of eight
  photograph credits, not a protein domain), **`lipatan kepala`** (the embryo's
  head fold, not a protein fold), **`sintesis, konjugasi`** (hormone conjugation,
  the same collocation `book5_en.py` protects), **`pemencaran kurva`** (the spread
  of a titration curve, not neural divergence) and **`selubung, gerak,
  pengaturan`** (the bacterial cell envelope, not the viral one).

Flags that were **deliberately left alone**, because the target is right and the
extra links are worth having: `bacaan` (a sequencing *read*, 98 links in
chapters 5 and 14 that English cannot have, because English STOPs "read" for
being also a verb — the Indonesian noun is not), `profil`, `pembaca`/`penulis`
(chromatin readers and writers), `silium`, `antibodi`, `antigen`, `uji baca`,
`luar sasaran`, `kaidah Oja`, `pemusatan`.

One `EXTRA` entry was needed. English splits piRNA between two definitions **by
number**: the singular *piRNA* is one of the ncRNA classes and the plural
*piRNAs* opens the transposon-silencing definition. Indonesian has no plural
`-s`, so both collapse onto one key and `def:b3:rna-regulation:pirna` became
unreachable; `"gugus piRNA"` (English's other key for that target, *piRNA
clusters*) restores it. That is the difference between 196 and 197 targets.

`lang_id.py`'s `TAIL_AFTER_S` earned its keep with no configuration: **497** of
the 2,934 link displays end in the enclitic `-nya`.

## The four `--force-classes prose` uses, and why

`id_apply.py`'s `prose` census (gate 8 minus the `title` class) was overridden
on exactly four chapters, and in every case for the same structural reason: the
file still held **English** at apply time, in a string the applier refuses to
let a patch change, and which `postedit.py` rewrites immediately afterwards.

* **ch. 21 `endocrinology`** — two TikZ `label={[font=\tiny]right:hormone}`
  options. The `draw` census byte-compares the whole `label=` value, so the text
  cannot be translated in the patch; gate 8 then reads the *anchor keyword*
  `right` as English. The post-edit rewrites the anchor as the degree form `0:`
  and translates the text (`hormon`, `hormon pada pengusung`).
* **ch. 23 `developmental-genetics`** — the four-tier segmentation `\foreach`
  label list and the body-region `\foreach {0.6/head, …}`. `id_apply` compares a
  `\foreach` list byte-for-byte *on purpose*, so the only form that passes the
  applier is the untranslated one; the post-edit translates both lists.
* **ch. 25 `molecular-evolution`** — a pgfplots `symbolic y coords={histone H4,
  …}` key together with its `coordinates {…}` and `axis cs:` references, which
  must be rewritten as one unit.
* **ch. 26 `behavioural-ecology`** — a node whose coordinate carries inner
  parentheses, `at ({2.4*sin(40)},{2.4*cos(40)}) {food, \qty{1}{km}}`;
  `id_apply`'s `NODE_TEXT` stops at the inner `)`, so the node text is invisible
  to the patch and is post-edited.

Every one of those strings is translated in the shipped tree, and gate 9 (the
twin comparison, which *does* own `\foreach` lists and pgfplots string keys)
reports no multi-word finding on any of the four chapters.

## Samples, with verdicts

1. **Chapter 27, opening** — *"Spesiesnya tidak langka ketika kemerosotannya
   bermula; ia dipanen dengan muatan kereta api, dan hutannya ditebang, lalu
   seekor burung yang hanya berbiak di dalam koloni raksasa tidak dapat lagi
   berbiak begitu koloninya menipis di bawah suatu ukuran yang tidak seorang pun
   mengukurnya."* — **native**: `dipanen dengan muatan kereta api` for "harvested
   by the trainload", the temporal `begitu` for "once", and the enclitic chain
   (`spesiesnya`, `kemerosotannya`, `hutannya`, `koloninya`) that Indonesian uses
   where English uses "its".
2. **Chapter 26, opening** — *"Seekor merak menyeret sebuah ekor yang berongkos
   seperlima anggaran tenaganya lalu memperlambat pelariannya dari harimau."* —
   **native**: `berongkos` as a verb ("costs"), and `pelariannya dari` for "its
   escape from"; a machine would have produced `biaya seperlima dari anggaran
   energinya`.
3. **Chapter 24, the crypt** — *"Sel puncanya membelah secara setangkup, sekitar
   sekali sehari, lalu bersaing memperebutkan ruang ceruknya yang terbatas."* —
   **native**: `setangkup` for *symmetric* (not the calque `simetris`),
   `memperebutkan` for competing *for* something, `ceruk` for the niche.
4. **Chapter 25, the neutral rate** — *"yakni \emph{hanyutan netral} pada skala
   sebuah kripta, yaitu sebuah jalan acak dengan batas yang menyerap."* —
   **near-native**: correct and idiomatic, but `jalan acak` for *random walk* sits
   beside `pengembaraan acak` in chapter 27; both are used in Indonesian
   textbooks and neither is wrong, but one volume should have picked one.
5. **Chapter 27, the effective-size theorem** — *"Laju sebuah populasi kehilangan
   keragaman dan menimbun silang dalam ditentukan bukan oleh cacah jiwanya $N$
   melainkan oleh \emph{ukuran efektifnya} $N_{e}$."* — **native**: `cacah jiwa`
   is the demographer's word for a census count, and the `bukan … melainkan`
   correlative is exactly the Indonesian contrastive English gets with "not …
   but".

## Deliberate divergences from the English

* **`\begin{proof}[Evidence]` → `\begin{proof}[Bukti eksperimental]`** (53×).
  A bare `Bukti` would read as *proof*, which is what the surrounding
  environment already says.
* **Decimals keep a POINT**, not the comma an Indonesian newspaper would use:
  every number in the book lives beside a `\qty`, an axis tick or a formula, and
  mixing separators inside one document is worse than following the scientific
  convention. (`3.14`, never `3,14`.)
* **Sixteen figures re-flowed.** Indonesian noun phrases run 15–25 % longer than
  English ones, so sixteen TikZ labels were shortened or re-broken (chapters 6,
  7, 11, 13 ×2, 14, 16 ×2, 18, 19, 21 ×2, 25, 26, 27, and two solutions
  paragraphs) to clear overfull boxes. **No coordinate was touched** except one
  `xshift` in chapter 18, and no drawing primitive changed: the drawing code is
  otherwise byte-identical to English, as the `draw` census requires.
* **`\emph{period}` → `\emph{per}`** in chapter 21: the *Drosophila* gene, whose
  standard symbol is `per`; the English spelling is also an ordinary English word
  and fired gate 8 for that reason.
* **Math `\text{}` subscripts translated** where they are words
  (`on→ikat`, `off→lepas`, `thr→amb`, `fold→lipat`, `needed→perlu`,
  `brain→otak`, `body→tubuh`, `pre→pra`, `post→pasca`, `GFR→LFG`, `true→sejati`)
  and **kept** where they are symbols (`ss`, `crit`, `osm`, `eff`, `inh`, `max`,
  `min`).
* **`Evo-devo` → `Evo-devo: perkakas dan sakelar`** (chapter 23 remark title):
  the bare form is byte-identical to English and gate 8's `title` class reads an
  identical title as untranslated, correctly — the subtitle is what an
  Indonesian lecture would put there anyway.

## Why not 100

* **Link density is 110 % of English.** Every surplus family was read in context
  through the two censuses and none is a homograph, but a density that far above
  the twin is a standing invitation to re-run both censuses after any future
  edit to the prose.
* **Two spellings of one concept survive**: `jalan acak` (ch. 24) and
  `pengembaraan acak` (ch. 27) for *random walk*, and `pelipatgandaan arus balik`
  (the process) beside `pelipat ganda arus balik` (the device) in chapter 20.
  The second pair is a real distinction English also makes; the first is simply
  two good words for one thing.
* **Eight of the 57 gate-9 advisories are the subscript `osm`**, which is right,
  but the remaining one-word advisories include three that are *choices* rather
  than cognates: `pre-miRNA` (against `pra-miRNA`), `Sepsis` (against
  `sepsis`/`renjatan septik`, both of which the chapter uses elsewhere) and
  `normal`. All three are what an Indonesian journal prints; a stricter editor
  might disagree about the first.
* **The English original allows itself a few conversational turns** — "a bet on
  the cue's honesty", "the experiment is being run once, without a control" —
  whose Indonesian renderings are faithful but a shade flatter than the English,
  because the register of an Indonesian Year-3 volume is uniformly formal.

## Gate output

```
$ bash tools/check_translation.sh bachelor-3 id
== bachelor-3 / id ==
  indonesian prose gate: OK (54 files)
  latin prose gate: 57 issue(s) in 54 files
    foreach-1word    1 hit(s) in 1 file(s)
    node-1word      29 hit(s) in 13 file(s)
    text-1word      20 hit(s) in 5 file(s)
    title-1word      7 hit(s) in 5 file(s)
  latin prose gate: no multi-word findings (the one-word tier above is advisory)

TRANSLATION GATE: PASSED

$ L=build/one_biology_book_5_university_year_3_id.log
$ grep -ac '^!' $L                    -> 0
$ grep -aci undefined $L              -> 0
$ grep -ac Overfull $L                -> 0
$ grep -ac nullfont $L                -> 0
$ grep -ac 'invalid in math mode' $L  -> 0
Output written on build/one_biology_book_5_university_year_3_id.pdf (400 pages)

$ python3 tools/link_defined_terms.py --book 5 --lang id
links to insert: 0 across 0 files
```
