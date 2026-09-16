# One Biology Book 4 — Indonesian (`id`) edition: self-score

**Date:** 2026-09-16
**Scope:** `one_biology_book_4_university_year_2_id.tex` — 27 chapters + 27
solutions files (University Year 2), 54 files, 350 pages.
**Quality bar:** *native academic*. Not "is this a correct rendering of the
English?" but "would an Indonesian biologist writing a second-year university
volume from scratch have written these sentences?" The sense reference is this
repository's own Book 3 `id` edition (self-scored 96/100, shipped 2026-09-06):
its terminology was mined key-by-key from the shipped `\index{}` pairs and
re-used wherever Book 4 re-uses the concept, so a reader moving from Year 1 to
Year 2 meets the same words (`relung`, `daya dukung`, `hanyutan genetik`,
`waktu tinggal`, `tandon`, `kebugaran`, `lungkang gen`).

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | university lecture register: bare imperatives (`Hitunglah` 285, `Jelaskan` 102, `Berikan` 38, `Nyatakan` 34, `Sebutkan` 29, `Bandingkan` 28, `Bahaslah` 23, `Definisikan` 16), **0 `kamu`**, `Anda` only 10 times — every one of them where the English addresses the reader directly ("what would you disable?", "how long does it take you?") |
| Terminology | high | 96 | Indonesian university-biology vocabulary throughout (`lungkang gen`, `keplastisan fenotipe`, `penghindaran naungan`, `jembatan silang`, `kurir kedua`, `keselanjaran`, `waktu tinggal`, `bagian yang mengudara`, `utang kepunahan`, `tarikan cabang panjang`, `hidup berdampingan`); Latin binomials, gene names (`MyoD`, `FLOWERING LOCUS T`, `Sonic hedgehog`), and ATP/DNA/RNA/cAMP untouched; all 611 distinct `\index` keys Indonesian and in one-to-one correspondence with English's 611 |
| MT-artifact freedom | high | 96 | twin-comparison gate (gate 9) clean of multi-word findings; 39 one-word advisories, every one a true cognate (`meiosis`, `mitosis`, `diatom`, `pilus`, `protonema`, `blastula`, `aorta`, `insulin`, `endometrium`, `stele`, `haploid`, `diploid`, `oogenesis`, `spermatogenesis`, `biofilm`, `florigen`, `normal`, `total`, `data`), a unit (`mol/L`, `nmol`), a proper name (`Hardy--Weinberg`, `Haldane`, `Aegilops`, `lac`/`gal`) or a math-mode subscript (`art`, `ven`) |
| Structure / LaTeX hygiene | gated | 100 | every `id_apply` census green on all 54 files (labels, envs, solution keys, `\emph`/`\index` adjacency, math spans, drawing code, delimiters, braces, image paths); log 0 errors / 0 undefined / 0 overfull / 0 `nullfont`; no "invalid in math mode" |
| Cross-references | gated | 100 | 0 undefined references; label sets identical to the English file by file; 79 `\cref` calls, same targets |
| Figures and captions | — | 96 | 122 `tikzpicture`s, 181 `omfigure`s, 79 image paths, 57 `\addlegendentry`, 1 `symbolic x coords` list and all 132 `\foreach` label lists translated by hand (the `draw` census does **not** see a `\foreach` list, so each was checked by eye); 9 figures re-flowed after the first build because Indonesian labels are longer than English ones |
| Solutions | — | 96 | all 27 solutions twins translated; 351 `\begin{solution}` keys, exercise/solution parity gated; weekend-problem answer numbering gated (gate 11) |
| Defined-term links | — | 96 | 3,572 links on 164 targets (English 3,093 on 155) — 115 % of English density, and 164 of the 155 English targets reached but one, which is a stale link in the English canon (below) |

## Measured state

```
files on disk             54   (27 chapters + 27 solutions)     = English
.fls files inputted       54                                    = English
pages                    350                                    (English 321)
LaTeX errors               0                                    = English
undefined references       0                                    = English
Overfull boxes             0                                    = English
nullfont warnings          0                                    = English
"invalid in math mode"     0                                    = English
TeX accent escapes         0                                    (Indonesian is plain ASCII)
\qty occurrences       2,456                                    = English
\qtyrange                 33                                    = English
\num                     175                                    = English
\text{...}                96, all translated                    = English
\includegraphics          79                                    = English
\begin{tikzpicture}      122                                    = English
\begin{omfigure}         181                                    = English
\addlegendentry           57                                    = English
symbolic x coords          1                                    = English
\foreach                 132                                    = English
\emph{}                  997                                    = English
\index{} occurrences     621                                    = English
distinct \index keys     611   (English 611) — every key Indonesian
\begin{exercise}         324                                    = English
\begin{solution}         351                                    = English
\begin{definition/proposition/theorem/method/example/problem}
                        61/101/59/6/41/27                       = English
\omterm links          3,572   (English 3,093)
distinct link targets    164   (English 155)
check_translation.sh   PASSED (gates 1-11)
link_defined_terms --check   green; --apply twice inserts 0
```

## What the two collision censuses found

Both censuses were run against the English twin after every link pass: the
per-target **frequency** census (`|id| vs |en|` per target) and the per-target
**chapter-set** census (which chapters link a target in `id` but not in `en`).
The first pass shipped 3,654 links on 164 targets; five families came out of
the censuses and one of them was a real homograph.

* **`pembelahan` — the one that mattered.** English's *cleavage* is a word of
  embryology only. Indonesian `pembelahan` is the ordinary noun for *any*
  division: of a cell, of a lineage, of a data set. Harvested from
  `def:b2:vertebrate-development:egg` it linked **67** times — 34 inside
  chapter 10 itself (where the definition stands three lines away and the link
  is worth least) and **33 of them wrong**: `pembelahan sel` in the muscle,
  limb, meristem and signalling chapters, and the lineage `pembelahan` of
  every divergence date in the phylogeny chapter, all pointing at the cleavage
  of a zygote. The chapter-set census is what found it: eight chapters that
  English never links. `STOP` would not have helped (the term falls through to
  the per-chapter map and keeps every chapter that pins a sense); only `DROP`
  removes it. The target is still reached, by its other term `kuning telur`.
* **`lumut kerak`** is a *lichen*, not a moss: two occurrences in the peppered-moth
  chapter linked their first word to `def:b2:plant-life-cycles:moss`. `EXTRA_PROTECT`.
* **`pengatur`** is the embryologist's *organiser* in chapter 10 and the
  ordinary adjective *regulatory/regulating* in `daerah pengatur` (chapters 3
  and 12) and `pusat pengatur tekanan` (chapter 17). `EXTRA_PROTECT` on the
  two collocations.
* **`bunga matahari`** is a sunflower, not a flower organ. `EXTRA_PROTECT`.
* **`folikel dominan`** is not a dominant allele — the same collision
  `book4_en.py` protects as "dominant follicle". `EXTRA_PROTECT`.

One `EXTRA` block was needed, for exactly the reason English needed one:
`def:b2:microbial-metabolism:trophic` indexes only the four bare roots
(`fototrof`, `kemotrof`, `litotrof`, `organotrof`) and every later use in the
prose is a compound (`kemolitotrof`, `kemolitotrofik`, `kemolitoautotrof`,
`kemoorganoheterotrof`). Without it the target carried **zero** links.

`lang_id.py`'s `TAIL_AFTER_S` earned its keep without any configuration: the
enclitic `-nya` tail is what links `meristemnya`, `stomanya`, `auksinnya`,
`sarkomernya`, `tandonnya` — 988 of the 3,572 link displays end in the enclitic `-nya`.

## Samples, with verdicts

1. **Chapter 17, opening** — *"Keluarkan jantung seekor katak lalu jatuhkan ia
   ke dalam larutan garam, maka ia terus berdenyut selama berjam-jam --- tanpa
   saraf, tanpa otak, tanpa darah, hanya sebuah otot yang berkerut dengan
   sendirinya kira-kira sekali tiap detik karena sepetak kecil selnya tidak
   sanggup diam."* — **native**: the imperative-then-`maka` construction is the
   ordinary Indonesian way to render an English "do X and Y happens"; a
   translation would have produced `dan ia terus berdenyut`.
2. **Chapter 22, the selection theorem** — *"seleksinya paling cepat pada
   frekuensi menengah dan paling lambat ketika sebuah alel jarang atau nyaris
   terpancang --- hanya ada sedikit keragaman untuk dikenainya."* —
   **native**: `terpancang` for *fixed* (not the calque `tetap`), and the
   passive `untuk dikenainya` where English writes "to act on".
3. **Chapter 25, the reservoir definition** — *"Sebuah tandon bermassa $M$
   dengan aliran keluar total $F$ memiliki waktu tinggal $\tau = M/F$, yaitu
   waktu rerata sebuah atom berada di dalamnya."* — **native**: `tandon`,
   `aliran keluar`, `waktu tinggal` are the terms an Indonesian
   biogeochemistry lecture uses; the apposition with `yaitu` is the standard
   definitional move.
4. **Chapter 15, phytochrome** — *"Nilai $\varphi$ yang rendah memberi tahu
   sebatang tumbuhan bahwa ia berada di bawah atau di samping tumbuhan lain
   sebelum ia benar-benar ternaung."* — **native**: the classifier `sebatang`
   for a plant, `ternaung` for *shaded*, and `memberi tahu ... bahwa` rather
   than a nominalisation.
5. **Chapter 26, the C:N threshold** — *"seresah dengan $\mathrm{C:N}$ di bawah
   kira-kira 25 melepaskan amonium ketika ia terurai (mineralisasi), sedangkan
   seresah di atasnya --- jerami pada 80, kayu pada 400 --- membuat mikrobanya
   menyerap nitrogen dari tanahnya (imobilisasi), sehingga tumbuhannya
   kelaparan sampai karbonnya telah direspirasikan habis."* — **native**:
   `seresah` (litter), `sedangkan` for the contrastive "while", and the
   consecutive `sehingga`.

## Deliberate divergences from the English

* **`\emph{quality}` → `\emph{mutu}`, `\emph{texture}` → `\emph{teksturnya}`**
  and similar: Indonesian marks definiteness with the enclitic `-nya`, so a
  defined term that English leaves bare is often possessed in Indonesian. The
  `\emph` adjacency census is satisfied because the count and neighbourhood are
  unchanged.
* **Nine figures re-flowed.** Indonesian noun phrases run 15–25 % longer than
  English ones, so nine TikZ labels were shortened or re-broken (`04`, `06`,
  `14`, `21`, `25`, `26`, `27`, and the `solutions/08` paragraph) to clear
  overfull boxes. No coordinate was touched: the drawing code is byte-identical
  to English everywhere, as the `draw` census requires.
* **`2~ons` → `2~auns`** in the Harvey problem: Indonesian `ons` is a
  *hectogram* (100 g), not the imperial ounce (28.35 g), so using it would have
  made the arithmetic of the problem false. (`ons` also trips gate 8 — see the
  report below.)
* **`\index{synapsis}` → `\index{sinapsis kromosom}`** in chapter 4: Indonesian
  renders both English *synapse* and *synapsis* as `sinapsis`, which would have
  merged two index entries and created a homograph across chapters 4 and 20.
  Qualifying the meiotic one keeps 611 distinct keys, exactly English's count.

## Why not 100

* Three of the 39 one-word gate-9 advisories are *choices* rather than
  cognates: `pilus`, `stele` and `protonema` are the international terms and an
  Indonesian textbook would use them, but a stricter editor might prefer
  `benang lekat`, `silinder pusat` and `protonema` respectively; only the
  middle one has a settled Indonesian form, and using it in one place and the
  Latin elsewhere would be worse.
* The link density is 115 % of English. Every surplus link was checked by the
  two censuses and none is a homograph, but a density that far above the twin
  is a standing invitation to re-check after any future edit to the prose.
* The volume's register is uniformly formal, which is right for Year 2 — but
  the English original allows itself a few conversational turns (*"a bet on the
  cue's honesty"*, *"the soil is the slowest organism on the farm"*) whose
  Indonesian renderings (`sebuah taruhan atas kejujuran isyaratnya`, `jasad
  yang paling lambat di sebuah ladang`) are faithful but a shade flatter.

## Gate output

```
$ bash tools/check_translation.sh bachelor-2 id
== bachelor-2 / id ==
  indonesian prose gate: OK (54 files)
  latin prose gate: 39 issue(s) in 54 files
    legend-1word     6 hit(s) in 4 file(s)
    node-1word      21 hit(s) in 9 file(s)
    text-1word       6 hit(s) in 4 file(s)
    title-1word      6 hit(s) in 5 file(s)
  latin prose gate: no multi-word findings (the one-word tier above is advisory)

TRANSLATION GATE: PASSED

$ L=build/one_biology_book_4_university_year_2_id.log
$ grep -ac '^!' $L        -> 0
$ grep -aci undefined $L  -> 0
$ grep -ac Overfull $L    -> 0
$ grep -ac nullfont $L    -> 0
$ grep -ac 'invalid in math mode' $L -> 0
Output written on build/one_biology_book_4_university_year_2_id.pdf (350 pages)
```
