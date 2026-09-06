# Translation score — Biology Book 3 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 3 (University Biology, Year 1) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic prose** — a French first-year *licence de biologie* / BCPST course as it is actually written. English is the source of truth for content, structure and labels. Two references were measured before drafting, not assumed: the shipped `fr` edition of **Biology Book 2** in this repo (`parts/grade-1[012]/fr/`, the volume this one continues) for terminology, typography and exercise register, and `styles/lang/fr.tex` for the UI strings |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-06 (re-synced twice the same day to the corrected English canon: wave-1 corrections, then wave-2) |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 29 chapters + 29 solution twins = **58 files**, a curated `tools/term_config/book3_fr.py`, the defined-term link layer, the index sort keys, the overfull sweep, and this score |

## Verdict in one line

A French Book 3 that reads as a *licence*-level biology course written in
French — the vocabulary a BCPST or L1 student meets in lecture, the
infinitive exercise register of the French university tradition, the
typography of French printing — with every structural, build, link-hygiene
and collision gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 58 files against their 58 twins: **348 `exercise` / 348**, **29 `problem` / 29**, **377 `\begin{solution}` / 377**, **87 `[resume]` / 87**, **185 `omfigure` / 185**, **122 `tikzpicture` / 122**, **38 `axis` / 38**, **633 `\node` / 633**, **85 `\includegraphics` / 85**, **2978 `\qty` / 2978**, **56 `\qtyrange` / 56**, **353 `\num` / 353**, **42 `\unit` / 42**, **3 `\qtylist` / 3**, **992 `\emph` / 992**, **568 `\index` / 568**, **130 `\cref` / 130**, **819 `\label` / 819**, and per environment **141 `definition`, 18 `theorem`, 117 `proposition`, 33 `method`, 96 `example`, 8 `remark`, 64 `proof`**, plus **887 `\item` / 887** and **725 `\textbf{N.}` weekend-problem answer numbers / 725** with the *same sequence* in both editions — all exact. `\label` **set** diff = **0 in both directions**. Every file was written through `tools/id_apply.py`, so every unnamed line is byte-identical to English |
| Terminology | **96** | Standard French university biology, chosen for continuity with the *lycée* volume below: *système ouvert*, *milieu intérieur*, *valeur de consigne*, *rétroaction négative*, *plan d'organisation*, *cœlome*, *métamérie*, *tissu conjonctif*, *bicouche lipidique*, *mosaïque fluide*, *potentiel hydrique / osmotique*, *symporteur / antiporteur*, *liaison osidique*, *adaptation homéovisqueuse*, *liaison phosphodiester*, *brin continu / discontinu*, *hélice α*, *feuillet β*, *pont disulfure*, *allostérie*, *coopérativité*, *effet Bohr / Haldane*, *nombre de renouvellement*, *rétro-inhibition*, *zymogène*, *phase photochimique*, *schéma en Z*, *chimiosmose*, *cycle de Calvin*, *plante en C4*, *gaine périvasculaire*, *force protomotrice*, *rapport P/O*, *quotient respiratoire*, *néoglucogenèse*, *voie des pentoses phosphates*, *cycle de Cori*, *nucléoïde*, *surenroulement*, *paradoxe de la valeur C*, *fourche de réplication*, *fragment d'Okazaki*, *cytodiérèse*, *coiffe*, *queue poly-A*, *épissage*, *cadre de lecture*, *répression catabolique*, *diauxie*, *atténuation*, *échange à contre-courant*, *anhydrase carbonique*, *cæcotrophie*, *acides gras volatils*, *cadre de Caspary*, *apoplasme / symplasme*, *poussée racinaire*, *nodosité*, *mycorhize*, *cohésion--tension*, *cavitation*, *tube criblé*, *source / puits*, *table de survie*, *capacité de charge*, *densité-dépendance*, *équation du disque*, *espèce clé de voûte*, *cascade trophique*, *biocénose*, *productivité primaire nette*, *indice de Shannon*, *dette d'extinction*, *relation aire--espèces*, *synapomorphie*, *groupe externe*, *parcimonie*, *paraphylétique*. **0 non-ASCII characters inside `\qty` / `\qtyrange` / `\unit` / `\num` / `\qtylist`** (machine-checked over all 58 files) |
| Register / tone | **97** | Measured against the shipped `fr` twin before drafting, not assumed. Book 2 `fr` uses the French **infinitive** exercise stem; Book 3 `fr` does the same, one register up: «~Énoncer la loi de Fick~», «~Calculer la tension nécessaire~», «~Expliquer le déplacement des chlorures~», «~Énoncer le résultat~:~». All 348 stems audited by script: **0 imperative-*vous* stems** (`Calculez`, `Expliquez`, …) and **0 tutoiement**. Course text is impersonal (*on*, passive), with the occasional *vous* the English source itself addresses to the reader («~Réchauffez l'étang…~») |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes, `nullfont` 0, 0 `invalid in math mode`** — the English baseline is also 0/0/0/0 — all measured with `grep -a`. **0 TeX accent escapes** (`\'e`, `` \`e ``, `\^e`, `\c c`), **0 `\oe`** against **137 raw `œ`**, **0 backtick quotes**, **78 `«` / 78 `»`** (the canon's 156 straight quotes, in pairs), French spaced punctuation (`~:` `~;` `~?` `~!` `~\%`) throughout, **0 prose lines ended with a trailing `%`** (the single `%`-terminated line is the `\newcommand{\haworth}` macro body, byte-identical to English) |
| Cross-refs / rule compliance | **98** | `\label`, `\cref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English; French articles supplied before the capitalised `\cref` names. No curriculum, programme or country name in visible text. No git commit made |
| Figures | **96** | All TikZ / pgfplots drawing code byte-identical — coordinates, styles, axis options, colours untouched; only node text, `\addlegendentry`, axis label strings and `{\small …}` captions localized. Ten of the 29 chapters needed a `!draw` opt-out, each for one reason only and each verified with a per-class differ (see *Deliberate divergences*) |
| Solutions | **97** | All 348 exercise solutions and all 29 weekend-problem solutions present and native; headers `\section*{Chapitre \ref{ch:…} --- <titre>}` with the `ch:…` slug unchanged. Every multi-line math span reproduced with its exact internal line break and indentation, which `id_apply`'s `math` census requires byte-for-byte |
| Defined-term links (`\omterm`) | **96** | **5459 links over 179 distinct targets** against English's **5495 over 179** — 99.3 % density on a text that runs 5 % longer, after curating away every collision the two censuses found. Target sets now agree except for the one documented `endoderme` casualty. Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles. Both collision censuses re-run **after** the last edit |
| MT-artifact freedom | **97** | `check_orphan_lines.py` (gate 10): **0 orphan English lines** (one found and removed). `check_latin_prose.py` (gate 9): **105 findings, 0 multi-word** — every remaining hit is a one-word true cognate (*cortex*, *ribosome*, *cytosol*, *virus*, *stroma*, *glucose*, *pyruvate*, *lactate*, *transamination*, *diffusion*, *transpiration*, *lynx*, *exon*, *intron*, *filaments*, *halophiles*, `\text{cat}`, `\text{app}`). A separate script scan of French prose (math, labels, `\omterm` targets, siunitx arguments and TikZ bodies stripped) for 70 English function words returns **0 real hits**. `\text{…}` census over course **and** solutions directories: every translatable one translated (*ext*, *int*, *éq*, *pente*, *cellule*, *base*, *acide*, *eau*, *sang*, *xylème*, *sphère*, *HR*, *cte*); *cat*, *app*, *tot* are the same abbreviations in French (*catalytique*, *apparent*, *total*) |

**Overall: 96** (weighted toward terminology, register and MT-artifact freedom;
structure and build are already gated mechanically).

## Structural / build gates

Measurement note: pdfTeX writes `build/*.log` with non-UTF-8 bytes, so a plain
`grep -c '^!'` treats the file as binary, prints nothing and exits 1 — which
reads exactly like a pass. Every figure below was taken with `grep -a`.

| Gate | Result |
|------|--------|
| `latexmk -g one_biology_book_3_university_year_1_fr.tex` | exit 0 (forced `-g`: 58 files were **created** during this run, and a plain build would not have recorded them) |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (12 found and cleared — see below) |
| `grep -ac 'nullfont'` | **0** — same as the English build |
| `grep -ac 'invalid in math mode'` | **0** — the `\sisetup{range-phrase}` fix in `styles/lang/fr.tex` holds across all 56 `\qtyrange` sites |
| `.fls` `parts/bachelor-1/` count | **60 distinct paths** = the 58 translated bodies + the two shared structure files (`part.tex`, `solutions/solutions.tex`), matching the English baseline exactly. `\ominput` falls back to English silently, so a green log alone proves nothing |
| PDF | `build/one_biology_book_3_university_year_1_fr.pdf`, **356 pp** (EN 339 — French runs ~5 % longer) |
| Canon re-sync, wave 1 | Three coordinator corrections mirrored on 2026-09-06 after the English line numbers moved: `solutions/16` answer renumbered 13→12 with the missing answer 13 written in French; `solutions/25` answers 16/17/18 reordered to the corrected sequence; two `\num{…}{g}` → `\qty{…}{g}` in `17-genomes` and `20-expression-control` (both constructs were present in the French twins). `book3_en.py`'s new `Golgi` / `Chargaff` / `checkpoint` entries re-examined in French: `Golgi` and `Chargaff` added to the French `EXTRA` for the same reasons, `checkpoint` already covered by *point de contrôle* |
| Canon re-sync, wave 2 | Three further corrections mirrored, four files: `19-gene-expression` questions 14 and 20 cited questions 11 and 10 where the arithmetic needs **12** and **11** (checked against the French answers — A11 = 180, A12 = 520, A14 divides by 520, A20 divides by 180); `solutions/21` answer 16's "pour cinq fois l'oxygène" replaced by the corrected "un vingtième de la masse, pour trois cents fois l'oxygène ($15\,000$ contre \qty{50}{mL} par heure)"; and the **changed datum** in `27-species-interactions`, $\alpha = 1.6 \to 1.4$, with answers 1 and 2 rewritten (intercept 125 → 143, and the equilibrium now solved for $N_A = -69$, not $N_B = -114$; re-derived independently: $N_A = 200 - 1.4(130 - 0.9N_A) \Rightarrow -0.26 N_A = 18 \Rightarrow N_A = -69.2$). Both solutions files **lengthened**, so gate 10 was re-run specifically for a copied-through file tail: **0 orphan lines**. Linker, both censuses, all eleven gates and a forced build re-run afterwards |
| `bash tools/check_translation.sh bachelor-1 fr` | **PASSED** (gates 1–11, including the new `check_problem_numbering.py`: *problem numbering: OK (58 chapters)*), re-run after the canon re-sync with the two new gate behaviours in place: gate 5's line-broken-`\index{}` check → **0**, and gate 9's new capitalised one-word advisory tier → 8 hits (*Coordination*, *Henderson--Hasselbalch*, *Monosaccharide*, *Polysaccharide*, *Ionisation*, *Michaelis--Menten*, *Fermentation*, *Virus* — every one a true French word or a proper name) |
| Line-end sweeps, re-run **after the last edit** | `['’]\s*$` → **0**; `^\s*([.,;:)?!]\|~[;:?!])` → **0**; `[a-zà-ÿ]-\s*$` → **0**. Every one was cured by re-wrapping the line; **no line was ever "fixed" with a trailing `%`**, which would have blinded the only detector |
| `\index{}` parity | **568 / 568**, exact in every one of the 58 files |
| Index sort keys | **164 ASCII sort keys added** (`\index{ecosysteme@écosystème}`), so that every accented entry alphabetises where a French reader looks for it. `makeindex` sorts byte-wise, and `é` sorts after `z`: without this, 18 entries would have formed a spurious section after the Z group and ~200 more would have sorted wrongly inside their own letter. Verified: **0 non-ASCII sort keys, 0 displays carrying two different sort keys** |
| Decimal marker | `styles/onebiology.sty` sets `output-decimal-marker={.}`, so the printed page uses a decimal **point**; prose was written to match, as the shipped Book 2 `fr` does |

### The twelve overfull boxes, and how each was cleared

The cure for a too-wide `tikzpicture` is shorter **node text**, never a change
to the drawing code; the cure for a prose box is to **add** short words so TeX
gets a legal break earlier, not to shorten the sentence.

| Chapter | Cure |
|---------|------|
| 2 (×2) | two compartment labels wrapped onto a further line |
| 3 | one root-anatomy label shortened |
| 4 | one tissue-table cell shortened |
| 7 (×2) | two transporter labels wrapped |
| 12 | the twenty-amino-acid table: `\footnotesize` → `\scriptsize` (French names are ~12 characters wider) |
| 13 | one Lineweaver–Burk axis annotation shortened |
| 15 (×3) | three respiratory-chain labels wrapped |
| 23 | the two-path cortex diagram: the grey caption node split onto three lines instead of two |

The linker and both collision censuses were re-run **after** this sweep and
after every later prose edit, so the last action on the edition was a
measurement, not an edit.

## Defined-term links and the two collision censuses

`tools/term_config/book3_fr.py` was curated from **this** edition's own
harvest. It was not translated from `book3_en.py` and not seeded from
`book2_fr.py`; every entry was re-derived, and the file's docstring records
the reasoning. Both censuses were run against the English twin: per-target
**frequency ratio** and per-target **chapter set**.

**Collisions that exist in French and not in English** (found by the censuses,
invisible to every structural and prose gate):

* **`endoderme`** is *both* the plant endodermis (ch. 3) and the animal
  embryonic endoderm (ch. 4). English has two different words —
  *endodermis* and *endoderm* — so the collision cannot exist there. The
  harvest kept the animal sense and ch. 23's Casparian-strip prose linked
  **seven times** to a germ layer. Dropped; the cost is English's 12 links to
  `prop:b1:flowering-plant-organization:stemroot`, which is the only target
  the French edition does not reach.
* **`source`** is the phloem source *and*, through the whole of ch. 26, a
  limestone **spring** — 14 wrong links.
* **`matrice`** is the mitochondrial and extracellular matrix, the **template
  strand** of ch. 18–19 (*brin matrice*) and ch. 29's **character matrix**.
* **`grossit`** was harvested from an `\emph`'d verb in the microscope
  definition and matched «~le foie grossit~» in ch. 16.
* **`genre`** as the ordinary noun («~du genre de ceux qui…~») was cured in
  the **prose**, not by dropping the term: the caption was reworded and the
  three taxonomic links kept.

**English collisions that do *not* exist in French, kept on purpose** — the
point of re-deriving rather than translating the config:

* **`plasma`**: French says *membrane plasmique*, so the English
  plasma-membrane collision is absent. All 21 links are blood plasma, and the
  target runs 34 links against English's 13 purely because English had to drop
  the word.
* **`polaire`**: French says *polarité cellulaire*, so *molécule polaire* is
  unambiguous.
* **`lisse`**, **`opérateur`**, **`empilement`**, **`résistance`**: single-sense
  in this volume, verified chapter by chapter.

`WORD_TAIL = (?:e?s)?` with `TAIL_ON_EVERY_WORD` was audited against every
single-word term: the tail can only manufacture forms like *basees*, *cirees*,
*plasmaes*, none of which occurs anywhere in the corpus, so **no
`EXTRA_PROTECT` pattern was needed**. Six `EXTRA` entries cover what the tail cannot
build: the irregular plural *niveaux trophiques*, *parois cellulaires*, the
singulars *hydrophyte* / *xérophyte*, and — added at re-sync, mirroring the
same two additions to `book3_en.py` — bare **`Golgi`** (the French index key is
the two-word *appareil de Golgi*, so 18 bare uses linked nowhere; all 18 were
read and every one is the organelle, never Camillo Golgi the person) and bare
**`Chargaff`** (French says *règles de Chargaff*, leaving two bare uses of the
surname unlinked). These two took the edition from 5424 to 5459 links.

Every remaining census outlier was inspected link by link and is correct:
`def:b1:mammal-organization:compartments` (+ch. 4, 7, 10, 21 — all blood
plasma), `def:b1:membranes-transport:transporters` (+ch. 8, 12, 14, 15, 24 —
all proton and ion pumps), `thm:b1:membranes-transport:fick` (+ch. 7 — the
chapter the theorem lives in), `prop:b1:organism-environment:thermo` (+ch. 29 —
*endotherme* in the amniote discussion), `def:b1:biosyntheses-integration:ppp`
(+ch. 23 — NADPH equivalents in the nitrate budget).

## Deliberate divergences from the English source

1. **Ten `!draw` opt-outs** (ch. 1, 2, 6, 15, 18, 19, 21, 23, 26, 29). The
   `draw` census compares `\foreach` label lists and `symbolic [xy] coords`
   **byte-for-byte**, and those strings are visible tick labels that must be
   French. Each opt-out was verified with a per-class differ that prints *all*
   divergences (`id_apply` reports only the first), and in every case the only
   diff is the intended label words. The affected sites are: metabolic-rate and
   surface-to-volume `\foreach` lists (ch. 1, 2), a `symbolic x coords` bar
   chart with matching `\addplot coordinates` (ch. 6, 21, 23), Krebs-cycle and
   mitosis-phase `\foreach` metabolite/phase names (ch. 15, 18), elongation-step
   titles (ch. 19), and `symbolic y coords` biome / taxon bar charts (ch. 26,
   29).
2. **Accented `symbolic coords` are impossible.** pgfplots normalises the
   coordinate key, so `(axis cs:lacune du mésophylle,-0.3)` fails with
   *"the input coordinate has not been defined with symbolic x coords"* and the
   build dies. The three affected charts therefore keep **ASCII** coordinate
   keys and add a `yticklabels=` / `xticklabels=` line carrying the accented
   French, so the printed axis is correct French while the lookup stays ASCII.
   Verified in the rendered PDF, label by label.
3. **Index sort keys.** The shipped Book 2 `fr` uses none (it has only three
   accent-initial entries, so nobody noticed). Book 3 `fr` has 18
   accent-initial entries and ~200 with an interior accent, which `makeindex`
   would sort after Z. Sort keys were added mechanically to every entry
   containing a non-ASCII character. This is a departure from the twin and is
   flagged here as such; it is strictly an improvement, and the existing `@`
   keys inherited from English (`beta-oxydation@$\beta$-oxydation`,
   `helice alpha@hélice $\alpha$`, `pKa@p$K_a$`, …) are untouched.
4. **Twelve gate-9 fragments were reworded, in French's favour.** The gate fails
   on a multi-word fragment byte-identical to English. Rather than let the gate
   drive the translation, each was replaced by *better* French that also
   differs: `[Nutrition, digestion, absorption]` → `[Nutrition, digestion et
   absorption]`; `[Habitat, niche]` → `[Habitat et niche]`;
   `{glucose, galactose}` → `{glucose et galactose}`; `{gyrase (ATP)}` →
   `{ADN gyrase (ATP)}`; `{fixation (RuBisCO)}` → `{fixation par la RuBisCO}`;
   `{pyruvate carboxylase, ATP}` → `{pyruvate carboxylase (ATP)}`;
   `{PEP carboxykinase, GTP}` → `{PEP carboxykinase (GTP)}`;
   `{hexokinase\\ ATP}` → `{hexokinase\\ (ATP)}`; `{fructose-1,6-bisP}` →
   `{fructose-1,6-bisphosphate}` (×2); `{ATP\\ synthase}` → `{ATP-\\ synthase}`;
   `{fructose-1,6-\\ bisphosphatase}` → `{fructose-\\ 1,6-bisphosphatase}`.

## Defects found in the ENGLISH canon during this pass

Nothing was edited in the English tree; each was verified against the book's
own model before being claimed.

0. **`solutions/16-biosyntheses-integration.tex` had Q12's answer labelled
   `\textbf{13.}` and no answer to Q13 at all** — independently reported by
   three editions, and **now corrected in the canon**; the French twin was
   re-synced (existing answer relabelled 12, new answer 13 written in French).
   Worth recording as a defect class: `\textbf{N.}` answer numbering inside a
   `problem` solution is prose to every gate in the repo. Nothing counts it,
   nothing matches it against the question list. A two-line check — the
   `\textbf{N.}` sequence in `solutions/NN` must be `1..k` with no gap, and
   `k` must equal the `\item` count of that chapter's `problem` — would have
   caught it in English before any translation started. This became
   **gate 11** (`check_problem_numbering.py`). The coordinator validated it in
   both directions and corrected me on the second half of the claim: it does
   **not** catch the `solutions/25` permutation, because the integers there
   still form a complete `1..k` run. A permutation of correct answers under
   correct numbers remains invisible to every mechanical check in the repo;
   only reading the answer against its question finds it.

1. **`\begin{proof}[Evidence]` / `[Partial proof]` are untranslatable in
   place.** Not an English defect but a **shared-tooling gap**: the optional
   argument of `proof` is prose, it is the same string in all 64 proofs, and
   nothing in `id_apply` requires a translator to name it. Seventeen
   `[Evidence]` and three `[Partial proof]` shipped through untranslated in
   this edition before gate 9's `title` tier caught them — and gate 9 only
   catches the ones a translator happened to miss *inconsistently*. Every other
   edition is exposed to the same trap. `styles/lang/<lang>.tex` already
   defines `\omnameProof`; a `\omnameEvidence` / `\omnamePartialProof` pair
   would make the string impossible to miss.
2. **`prop:b1:flowering-plant-organization:stemroot` is reachable in English by
   exactly one word, *endodermis*.** That is fragile by construction: any
   language whose word for the plant endodermis is also its word for the
   embryonic endoderm (French, Spanish, Portuguese, Italian) loses the target
   entirely. Reported, not edited — the fix belongs in the English definition
   (a second harvestable term such as *Casparian strip* pointing at the same
   proposition), not in one translation.
3. **`def:b1:classifying-biodiversity:characters` is defined by the word
   *character*, which English itself has to `DROP`.** English therefore reaches
   the target only through *homology*, *homoplasy*, *synapomorphy* and
   *outgroup*. Noted as the same structural fragility as (2); no edit made.

## Bugs found in the SHARED tooling

1. **pgfplots `symbolic coords` cannot hold non-ASCII text, and nothing warns
   about it.** With `\node ... at (axis cs:<accented key>,y)` the build dies
   with *"the input coordinate `…' has not been defined"* — the message shows
   the key mojibake'd, which sends a reader looking for an encoding bug that
   is not there. This is the third distinct trap on `symbolic coords` after the
   `draw`-census byte comparison, and it is guaranteed to hit every accented
   language on every such chart. It deserves a line in
   `translation_instruction.md`: **keep symbolic coordinate keys ASCII and put
   the localized text in `xticklabels=` / `yticklabels=`** — which the `draw`
   census permits under a `!draw` opt-out and which renders identically.
2. **A line-broken `\index{}` key is invisible to every gate.** `id_apply`'s
   `index` census counts entries, not their content, and `harvest.py` collapses
   whitespace before comparing — so `\index{système\nouvert}` passes the write,
   passes `check_translation.sh`, and reaches `makeindex` as a distinct entry
   from `\index{système ouvert}`. Four were introduced here purely by French
   line-wrapping and found only by an ad-hoc balanced-brace scan. The
   coordinator fixed 18 of these in the English canon by hand this week; a
   two-line check in `check_translation.sh` (`\index{` whose closing brace is
   on another line) would close the class permanently.
3. **`harvest.py` harvests inflected verbs from `\emph` inside a definition.**
   The microscope definition emphasises the verbs *magnifies* / *resolves*;
   French *grossit* and *résout* were both harvested as terms, and *grossit*
   then matched «~le foie grossit~» four chapters away. English had already
   had to `DROP "resolves"` for the same reason. The rule that a bare `\emph`
   counts only when it agrees with the label leaf does not apply to
   `\emph{…}\index{…}` pairs, which is where these came from; a
   part-of-speech-agnostic engine cannot fix it, but the class is worth naming
   in `translation_instruction.md` next to the capitalised-harvest class.

## Files owned and written by this pass

* `parts/bachelor-1/fr/01-…29-*.tex` (29 chapters)
* `parts/bachelor-1/solutions/fr/01-…29-*.tex` (29 solution twins)
* `tools/term_config/book3_fr.py` (curated from this edition's harvest)
* `translation_scores/book_3/fr/translation_score.md` (this file)

Not touched: the English tree, `styles/`, the entry file
`one_biology_book_3_university_year_1_fr.tex`, `frontmatter/image-credits-book3.fr.tex`,
`latexmkrc`, CI. No git commit was made.
