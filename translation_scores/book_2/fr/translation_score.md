# Translation score — Biology Book 2 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 2 (High School, grades 10–12) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic prose** — French *lycée* SVT as it is actually written. English is the source of truth for content and labels. Two references were measured before drafting, not assumed: the shipped `fr` edition of **Biology Book 1** in this repo (`parts/grade-*/fr/`, the volume this one continues) for terminology, and the shipped `fr` edition of **Physics Book 2/3** (`../one-physics-book/parts/grade-1[12]/fr/`) for the exercise register of this age band |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-05 |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 36 chapters + 36 solution twins = **72 files**, a curated `tools/term_config/book2_fr.py`, the defined-term link layer, the overfull sweep, and this score |

## Verdict in one line

A French Book 2 that reads as a *lycée* SVT course written in French — the
vocabulary a *première*/*terminale* pupil meets in class, the infinitive
exercise register of the French high-school tradition, the typography of
French printing — with every structural, build, link-hygiene and
collision gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 72 files against their 72 twins: **540 `exercise` / 540**, **36 `problem` / 36**, **576 `\begin{solution}` / 576**, **108 `[resume]` / 108**, **184 `omfigure` / 184**, **136 `tikzpicture` / 136**, **48 `axis` / 48**, **668 `\node` / 668**, **56 `\includegraphics` / 56**, **1184 `\qty` / 1184**, **8 `\qtyrange` / 8**, **165 `\num` / 165**, **30 `\unit` / 30**, **543 `\emph` / 543**, **182 `\index` / 182**, **148 `\cref` / 148**, **1013 `\label` / 1013**. `\label` **set** diff = **0 lines**. Every file was written through `tools/id_apply.py`, so every unnamed line is byte-identical to English |
| Terminology | **96** | Standard French SVT, chosen for continuity with the *collège* volume below and the *licence* volume above: *arbre phylogénétique*, *groupe externe*, *état dérivé partagé*, *clade*, *horloge moléculaire*, *fuseau neuromusculaire*, *appareil racinaire / aérien*, *poil absorbant*, *sève brute / élaborée*, *xylème*, *phloème*, *phase photochimique / phase chimique*, *cycle de Calvin*, *crêtes*, *chaîne respiratoire*, *glycémie*, *îlots du pancréas*, *insulinorésistance*, *réaction inflammatoire*, *cellules sentinelles*, *sélection clonale*, *lymphocyte T auxiliaire*, *immunité collective*, *réflexe myotatique*, *motoneurone*, *voie finale commune*, *faisceau corticospinal*. **0 non-ASCII characters inside `\qty` / `\qtyrange` / `\unit` / `\num`** (machine-checked over all 72 files) |
| Register / tone | **96** | Measured, not assumed. Book 1 `fr` at its own top year (`parts/grade-9/fr/`) uses imperative *tu* — «~Définis~», «~Classe~», «~Énonce~» — which is a children's-book register and was deliberately **not** carried up. Book 2 `fr` uses the French high-school **infinitive** stem, exactly as the shipped physics `fr` editions of the same ages do («~Donner~», «~Calculer~», «~Classer~»): «~Définir un état dérivé partagé~», «~Énoncer le résultat~:~», «~Calculer la dose d'insuline rapide~». Course text is impersonal (*on*, passive) with occasional *vous* addressed to the reader. **Zero occurrences of *tu / ton / ta / tes*** in the 72 files |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes, `nullfont` 0** — the English baseline is also 0/0/0/0 — all measured with `grep -a`. **0 TeX accent escapes** (`\'e`, `` \`e ``, `\^e`, `\c c`), **0 `\oe`** against **370 raw `œ`**, 0 backtick quotes, **133 `«` / 133 `»`**, French spaced punctuation (`~:` `~;` `~?` `~!`) throughout, **0 lines ended with a trailing `%`** |
| Cross-refs / rule compliance | **98** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English; French articles supplied before the capitalised `\cref` names («~du \cref{ch:…}~», «~la \cref{met:…}~», «~de l'\cref{ex:…}~»). No curriculum, programme or country name in visible text (one pre-existing exception in a coordinator-owned file is reported below, not edited) |
| Figures | **97** | All TikZ / pgfplots drawing code byte-identical — coordinates, styles, axis options, colours untouched; only node text, `\legend{}`, axis label strings and `{\small …}` captions localized. The `draw` census compares `\foreach` label lists and `symbolic coords` **byte-for-byte**, so those five sites were kept English inside the patch and localized by a single targeted post-write edit each — **never** a `!draw` opt-out (listed under *Deliberate divergences*) |
| Solutions | **96** | All 540 exercise solutions and all 36 weekend-problem solutions present and native; headers `\section*{Chapitre \ref{ch:…} --- <titre>}` with the `ch:…` slug unchanged. All multi-line math spans reproduced with their exact internal line break, which `id_apply`'s `math` census requires |
| Defined-term links (`\omterm`) | **95** | **5789 links over 106 distinct targets** against English's **5547 over 103** — 104 % density on a text that runs 5 % longer. Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles. Both collision censuses run **after** the last edit; the one real collision found is documented below |
| MT-artifact freedom | **97** | `check_orphan_lines.py` (gate 10): **0 orphan English lines**. `check_latin_prose.py` (gate 9): **49 findings, 0 multi-word**, and all 49 one-word hits are true French words identical to English — *stroma*, *glucagon*, *cytokines*, *synapse*, *muscle*, *pyruvate*, *glucose*, *macaque*, *duplication*, *population*, plus Latin binomials (`\emph{A. africanus}`). `\text{…}` census over course **and** solutions directories: **4 of 4 translated** (*charge*, *muscle*, *énergie*, *lumière, chlorophylle*) |

**Overall: 96** (weighted toward terminology, register and MT-artifact freedom;
structure and build are already gated mechanically).

## Structural / build gates

Measurement note: pdfTeX writes `build/*.log` with non-UTF-8 bytes, so a plain
`grep -c '^!'` treats the file as binary, prints nothing and exits 1 — which
reads exactly like a pass. Every figure below was taken with `grep -a`.

| Gate | Result |
|------|--------|
| `latexmk -g one_biology_book_2_high_school_fr.tex` | exit 0 (forced `-g`: 72 files were **created** during this run, and a plain build would not have recorded them) |
| `grep -ac '^!'` | **0** |
| `grep -ac 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (11 found and cleared — see below) |
| `grep -ac 'nullfont'` | **0** — same as the English build; a rise would be the accent-inside-`\qty` failure |
| `.fls` translated-file count | **72** — every chapter and every solution twin really compiled. `\ominput` falls back to English silently, so a green log alone proves nothing |
| PDF | `build/one_biology_book_2_high_school_fr.pdf`, **399 pp** (EN 379 — French runs ~5 % longer) |
| `bash tools/check_translation.sh grade-10 fr` | **PASSED** |
| `bash tools/check_translation.sh grade-11 fr` | **PASSED** |
| `bash tools/check_translation.sh grade-12 fr` | **PASSED** |
| Line-end sweeps, re-run **after the last edit** | `['’]\s*$` → **0**; `^\s*([.,;:)?!]\|~[;:?!])` → **0** in prose (the only hits are TikZ `.. controls` continuations, byte-identical to English); `[a-zà-ÿ]-\s*$` → **0**. Every one was cured by re-wrapping the line; **no line was ever "fixed" with a trailing `%`** |
| `\index{}` parity | **182 / 182**, per grade 63 / 51 / 68 — exact |
| Decimal marker | `styles/onebiology.sty` sets `output-decimal-marker={.}`, so the printed page uses a decimal **point**; prose was written to match (0 decimal commas outside TikZ coordinates), as the shipped physics `fr` editions do |

### The eleven overfull boxes, and how each was cleared

The cure for a too-wide `tikzpicture` is shorter **node text**, never a change
to the drawing code; the cure for a prose box is to **add** short words so TeX
gets a legal break earlier, not to shorten the sentence.

| File | Box | Cure |
|------|----:|------|
| `grade-11/fr/11-the-eye.tex` | 54.6 pt | «~opsine des bâtonnets (rhodopsine)~» → «~rhodopsine (bâtonnets)~»; «~gène d'opsine ancestral~» → «~gène ancestral~» |
| `grade-12/fr/05-human-evolution.tex` | 36.7 pt | four skeleton labels shortened («~humain~: ouverture de la moelle~» → «~humain~: ouverture~») |
| `grade-11/fr/08-antibiotic-resistance.tex` | 26.6 pt | three-column `\legend{}` shortened to English width |
| `grade-12/fr/04-phylogenetic-trees.tex` | 15.2 pt | the seven-column character table (French headers are 12 characters wider): `\small` → `\footnotesize` |
| `grade-12/fr/12-adaptive-immunity.tex` | 14.6 pt | two right-hand labels wrapped onto a third line |
| `grade-12/solutions/fr/14-brain-and-movement.tex` | 12.8 pt | «~(et chez des volontaires~» → «~(et même chez des volontaires,~» — words **added** |
| `grade-12/fr/06-plant-rooted-life.tex` | 10.6 pt | the two left-hand leaf labels wrapped onto three lines |
| `grade-11/solutions/fr/05-enzymes-and-phenotype.tex` | 9.2 pt | «~a fixé l'enzyme (…)~» → «~a fixé l'enzyme elle-même (…)~» |
| `grade-12/solutions/fr/03-selection-drift-speciation.tex` | 7.0 pt | «~entre porteurs~» → «~entre les porteurs~» |
| `grade-10/solutions/fr/08-heart-lungs-effort.tex` | 5.8 pt | «~Débit cardiaque multiplié par 5.3~» → «~Le débit cardiaque est multiplié par 5.3~» |
| `grade-10/fr/02-cells-common-unit.tex` | 3.8 pt | «~membrane plasmique~» wrapped onto two lines |

The linker and both collision censuses were re-run **after** this sweep, and
the build re-run after that: the last thing done was a measurement, not an edit.

## Defined-term links — what the curation actually needed

The uncurated harvest inserted **6053** links. Curation removed 277 of them,
restored the missing singulars and plurals, and landed at **5789 over 106
targets** against English's **5547 over 103**. Every entry in
`tools/term_config/book2_fr.py` is a French fact, and none of it was copied
from `book1_fr.py` or mechanically translated from `book2_en.py`.

| Cause | Effect | Cure |
|-------|--------|------|
| **`espèce`** — dropped in the first curation, then restored | Both editions had the `\emph`/`\index` marker on the *biodiversity* definition's bullet rather than on the Species definition, so 165 French links landed on a definition of biodiversity and English linked the word not at all. **The canon was corrected mid-run in both editions** (marker moved onto the Species definition), and the word now points at a definition **of a species**: 274 French links against English's 272 | drop reverted; no suppression needed — French has no «~une espèce de X~» = *a sort of X* idiom in this volume (its single «~une espèce de petite taille~» is the biological sense) |
| Definitions that emphasise only a **plural** — *anti-inflammatoires*, *médiateurs*, *tropismes*, *proto-oncogènes*, *sels minéraux* | `WORD_TAIL` can only **add** `-s`/`-es`, so the singular the prose actually uses (*un anti-inflammatoire*, *son médiateur*, *un tropisme*) was unreachable: 14 links missing, one of them a whole target French had zero of | `EXTRA` for each singular |
| **`paroi`** is *any* wall in French — of a vessel, of the gut, of an alveolus, of a bronchus — as well as the plant/bacterial cell wall | 33 links, **12 of them the anatomical sense** (the inflammation chapter is built on vessel walls). English is safe because its term is the two-word *cell wall* | `DROP "paroi"`, with *paroi de cellulose / cellulaire / bactérienne* restored in `EXTRA` |
| **`homologues`** is the homology of the common-ancestry chapter **and** the paired chromosomes of meiosis | **16 links** in three chapters English never links, e.g. «~les \emph{chromosomes homologues}~» pointing at *homology* | `EXTRA_PROTECT` (five patterns), mirroring English's `homologous chromosomes/pairs` |
| **`culture`** — transmitted animal behaviour, a bacterial culture on a plate, a growing crop, human culture. French collides harder than English: a cultivated plant *is* «~une culture~» | four senses on one target | `DROP` (as English does) |
| **`fréquences`** — allele frequencies vs the firing frequency of a spindle and cardiac/respiratory rates | wrong sense in three chapters | `STOP` |
| **`résistante`** — antibiotic resistance vs toxin-resistant borers vs insulin-resistant tissue | wrong mechanism, same adjective | `STOP` (the multi-word *résistance aux antibiotiques* still links) |
| French idioms built on **`œil`**: «~à l'œil nu~», «~sous l'œil du pancréas~», «~avec un œil humain à la place du milieu~» | three wrong-sense links | `EXTRA_PROTECT` (four patterns) |
| `WORD_TAIL` is `(?:e?s)?`, which cannot make an irregular plural | *œil→yeux*, *noyau→noyaux* unreachable | `EXTRA` |

Three deliberate divergences from `book2_en.py`, each because the collision it
guards against does not exist in French:

* **`bases` is kept.** English `DROP`s it because of *acids and bases*; this
  volume's French has no such phrase — all 66 occurrences are «~paires de
  bases~», the DNA sense, on the right target.
* **`œil` is kept** (English `STOP`s *eye*): the sense is right in 100 of 104
  places, and the four idioms are protected individually.
* **`porteur` is kept** (English `DROP`s *carrier*): French says
  *transporteur* for the NAD/glucose carriers, so the collision English feared
  cannot arise. `HEAD` reaches *non-porteur*, which is the same sense; it
  cannot reach *transporteur*, which has no word boundary.

### Both collision censuses, run after the last edit

`CHAPTER` (target linked in a chapter English never links there) and `FREQ`
(≥ 6 links and ≥ 2× English) both ran on the final tree. Ten chapter flags and
six frequency flags remain; **all sixteen were read site by site and are
correct**, and the reasons are worth recording because a later agent will see
them again:

* `def:g10:biodiversity-scales:species` **274 vs 272** — no longer a flag at
  all; before the canon fix it was the largest anomaly in the edition.
* `def:g11:the-eye:parts` 100 vs 12 and `prop:g11:becoming-male-female:hormones`
  50 vs 6 and `prop:g11:gene-expression:translation` 6 vs 1 — the English side
  of these three is an artefact of **capitalisation**: English links only
  *Testosterone*, *Translation*, and 12 of its *eye*s. French links the
  lower-case forms too, on the same, correct targets.
* `def:g10:universal-dna:nucleotide` 121 vs 54 — the kept `bases`, above.
* `def:g11:genes-and-disease:genetic` 128 vs 46 — the kept `porteur`, above.
* `def:g10:chemistry-of-life:families` in seven extra chapters — French
  harvests *protéine* (ambiguous, resolved nearest-preceding) and *protéines*
  (unambiguous) as two keys where English folds them into one; both targets are
  real definitions of the word.
* Three targets are French-only and one English-only, all small and all
  correct: French links *voie métabolique* (2) and *proto-oncogène* (3+1)
  where English's surface differs; English's *anti-inflammatory drug* (2) is
  now matched by the French `EXTRA` above.
* Five display strings map to two targets each — *protéine*, *chloroplaste*,
  *chromosome*, *enzyme*, *enzymes* — which is exactly the
  `AMBIG_POLICY = "nearest-preceding"` set the English edition also carries.

The per-target display census additionally caught a **cross-chapter spelling
drift I had created myself**: ch. 7 wrote *transgénèse* while `grade-10/fr`
writes *transgenèse*, which split one notion across two targets. Normalized to
*transgenèse* (the standard spelling) in both files before the final link run.
Nothing else in the toolchain can see that class of defect.

## Deliberate divergences from a byte-for-byte patch

Five figures could not be localized inside `id_apply.py`'s `draw` census, which
compares `\foreach` label lists and `symbolic coords` **byte-for-byte**. In each
case the English text was kept in the patch — so the census passed on the whole
file — and one targeted post-write edit was applied. No file ever took a
`!draw` opt-out.

| File | Site |
|------|------|
| `grade-12/fr/04-phylogenetic-trees.tex` | the `\matrix` character table (6 rows) and the `\foreach \x/\y/\t` character labels |
| `grade-12/fr/05-human-evolution.tex` | `symbolic x coords` + its two `\addplot coordinates` |
| `grade-12/fr/09-respiration-fermentation.tex` | `symbolic x coords` + its `\addplot coordinates` |
| `grade-12/fr/13-stretch-reflex.tex` | the `\foreach \row/\y/\lab/\n` stretch labels |
| `grade-12/fr/14-brain-and-movement.tex` | `symbolic y coords` + its `\addplot coordinates` |

One further divergence: ch. 13's synapse definition was first written with the
gap spelled out («~une vingtaine de nanomètres~»). It was restored to
`\qty{20}{nm}` when a per-file `\qty` count against the twin showed 31 vs 32 —
the only structural drift the whole run produced, and it is now 1184 / 1184.

## Sentences the English left open, and how French read them

French is the sense reference for the other six editions, so every place the
English admits two readings is recorded here.

1. `grade-12/solutions/14` ¶18 — "*and* `H. erectus` *only through populations
   that fed into it*". "It" is not bound. Read as the surviving lineage:
   «~et \emph{H. erectus} seulement par les populations qui ont alimenté cette
   lignée~».
2. `grade-12/09` Part IV q. 3 — "*Which of the three stages, then, can fat not
   use*", whose own solution names glycolysis **and** its fermentation.
   Rendered as a single question, «~Laquelle des trois étapes la graisse
   ne peut-elle donc pas emprunter~», leaving the two-part answer to the
   solution, as the English does.
3. `grade-12/08` solution 7 — "*about* $5/1.47$" uses an unexplained
   CO₂-to-sugar mass ratio. Kept verbatim rather than invented.
4. `grade-12/12` opening — English *cowpox*. French's own name for that
   disease, *la vaccine*, is a near-homograph of *le vaccin*, the word the
   chapter is about. Rendered as «~une pustule de vaccine~» in the narrative
   and «~l'inoculation de la vaccine protégeait de la variole~» in the Jenner
   caption, where the contrast with *variole* disambiguates it.
5. `grade-12/13`/`14` — the knee jerk. English uses *kick* and *jerk* for the
   same event; French distinguishes «~la jambe se tend~» (the movement) from
   «~le réflexe rotulien~» (the test) and «~se détend~» (the observed jerk).

## Samples

**Native.** `grade-12/fr/09-respiration-fermentation.tex`, the mirror remark:

> La photosynthèse charge sur des transporteurs, grâce à la lumière, les
> électrons pris à l'eau et s'en sert pour réduire le dioxyde de carbone en
> sucre, en libérant de l'oxygène~; la respiration décharge du sucre les
> électrons sur des transporteurs et les remet à l'oxygène, en produisant de
> l'eau et en libérant du dioxyde de carbone, et emploie l'énergie à fabriquer
> de l'ATP.

Two long balanced clauses on a semicolon, gerund adjuncts carrying the
subordinate action — the shape of French scientific exposition, not of a
rendered English sentence.

**Native.** `grade-12/fr/06-plant-rooted-life.tex`, the opening:

> Un chêne ne peut pas marcher jusqu'à l'eau, fuir une chenille ni partir en
> quête d'un partenaire. Il se tient trois siècles durant là où son gland est
> tombé…

«~ni~» after a negation and the fronted «~trois siècles durant~» are choices a
translator makes and a machine does not.

**Native.** `grade-12/fr/11-innate-immunity.tex`, caption:

> Le pus, ce sont les phagocytes venus, qui ont combattu et qui sont morts.

The dislocated «~ce sont~» is the ordinary French way to gloss a noun; a
literal rendering would have produced *Le pus est les phagocytes*.

**Near-native.** `grade-12/fr/10-glucose-and-diabetes.tex`, exercise 12:

> Poser le diagnostic pour chacun, et dire ce que font les îlots de chaque
> patient.

Correct and idiomatic, but «~pour chacun~» then «~de chaque patient~» repeats
the distributive twice in one sentence; a French author would probably have
dropped one. Kept because the English does the same and the exercise is a
two-part instruction.

**No MT anywhere.** The prose gate reports zero multi-word English fragments in
72 files, and the twin comparison zero orphan lines.

## Why not 100

* **Link density is 104 % of English on a 5 % longer text**, and three of the
  targets are 8×–10× — correctly, for the capitalisation reason above, but a
  French reader will meet «~testostérone~» linked more often than an English
  reader meets *testosterone*. Nothing is wrong; the calibration is not equal.
* **Five figures are not byte-provable.** The `\foreach` and `symbolic coords`
  post-write edits are correct and were re-read, but they are the one class of
  change in this edition that no census guards.
* **Two figures were re-laid-out, not just re-worded.** The character table
  dropped to `\footnotesize` and four labels gained a line break; French is
  simply wider than English there, and the page is fractionally less like the
  English one.
* **`fuseau` remains a two-sense word in the book** — the mitotic spindle
  (`fuseau de division`) and the muscle spindle (`fuseau neuromusculaire`).
  Neither is a linked term, so no census can see it; the qualifier is written
  out at every first use in a section, but a reader who meets a bare «~fuseau~»
  in ch. 13 must take it from context.
* **Register is a judgement, not a measurement.** The infinitive stem is right
  for a French *lycée* textbook and matches the physics editions of the same
  ages, but it is one convention among two (the imperative *vous* is the other),
  and a French publisher might have chosen differently.

## Defects found in the ENGLISH canon (reported, not fixed)

1. `parts/grade-12/06-plant-rooted-life.tex`, problem Part IV q. 20 — asks for
   "*the two **animals** that do its moving for it*", but its own solution
   answers "*the wind for its pollen and the jay for its acorns*". The wind is
   not an animal. Rendered faithfully in French, so the same mismatch ships.
2. `parts/grade-12/07-domesticated-plants.tex`, the *Brassica* figure —
   labelled the common ancestor of kale, cabbage, Brussels sprout, kohlrabi,
   broccoli and cauliflower "*wild mustard (one species)*"; those six are
   cultivars of *Brassica oleracea*, the wild **cabbage**. **Reported and
   fixed in the canon during this run** (`wild cabbage`); the French node now
   reads «~chou sauvage~». The *wild mustard* of exercise 12 in the same
   chapter is a different and correct use, and was left as «~moutarde
   sauvage~».
3. `parts/grade-11/02-cell-cycle-mitosis.tex` — colchicine is "*a drug
   extracted from crocuses*". It comes from *Colchicum autumnale*
   (Colchicaceae), not from a true crocus (Iridaceae). French has the exact
   word and uses it: «~colchique~».
4. `parts/grade-12/solutions/10-glucose-and-diabetes.tex`, `\textbf{1.}` —
   writes `$1/180 = \qty{5.55}{mmol/L}$`. The number is right but the equation
   is not: 1 g/L ÷ 180 g/mol = 0.00555 mol/L. Rendered faithfully.
5. `one_biology_book_2_high_school_fr.tex` (coordinator-owned) — `\bookline`
   reads «~Livre 2~: Biologie du lycée~». *Lycée* is a school-system name, and
   hard rule 7 of `translation_instruction.md` forbids naming a curriculum in
   visible text. This is a pre-existing series decision (Book 1 `fr` ships
   «~collège~»), so it is reported rather than changed.

## Gate bugs hit

None new. The two known traps both fired and both were handled as
`translation_instruction.md` prescribes:

* `id_apply.py`'s `draw` census refuses a translated `\foreach` list or
  `symbolic coords`; the documented post-write route was used five times
  rather than a file-wide `!draw`.
* A range that swallows `\begin{enumerate}`, drops a closing `\end{...}`, or
  re-wraps a multi-line math span is rejected by the `envs` / `math` censuses.
  Nine such rejections occurred across the run and all nine were real defects
  in my patch, not false alarms — the censuses earned their keep.

Three canon changes arrived mid-run from the coordinator and were mirrored:
the orphan `def:g10:biodiversity-scales:species` target (marker moved from the
Biodiversity bullet to the Species definition — same two edits made in
`parts/grade-10/fr/05-biodiversity-scales.tex`, restoring `\emph` 11/11 and
`\index` 5/5 for that file); the *wild cabbage* correction above; and
`parts/grade-11/01-dna-replication.tex` lines 290 and 399, where an `\omterm`
inside a `\qty` unit argument became prose. The French file still carried the
old form `\qty{50}{nucleotides/s}`, so both sites were rewritten as prose
(«~à 50 nucléotides par seconde~»). The linker, both collision censuses, all
three gates, the three line-end sweeps and the full `-g` build were re-run
**after** the last of these edits, in that order.

`tools/check_latin_prose.py`'s hyphenated-compound bug (a hyphenated loanword
counted as two words and so hit the blocking multi-word tier) never blocked
this edition: *crossing-over* is the only such term here, and it passed both
before and after the fix.
