# Translation score — Biology Book 1 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | French (`fr`) |
| **Quality bar** | **native school prose** (English is the source of truth for content and labels; there is no French twin of this book, so the register exemplar is the shipped `fr` edition of **Physics Book 1** — same ages, same series, same apparatus — and the terminology reference is ordinary French SVT usage) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-04 |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 71 chapters + 71 solution twins + the two front-matter files + a curated `tools/term_config/book1_fr.py`, then the defined-term link layer, then this score. **144 files written.** |

## Verdict in one line

A French Book 1 that reads as though it had been written in French — for
French seven-year-olds in Année 1 and for French fifteen-year-olds in
Année 9 — with the SVT vocabulary a *collège* pupil will meet again in the
*lycée* volume, and with every structural, build and link-hygiene gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, measured file by file: **796 exercises EN / 796 FR**, **35 `problem` environments / 35**, **831 `\begin{solution}` / 831**, **70 `[resume]` / 70**, **99 `omfigure` / 99**, **43 `tikzpicture` / 43**, **169 `\node` / 169**, **76 `\includegraphics` / 76**, **57 `\qty` / 57**. `\label` set diff = **0 lines** across all 142 files |
| Terminology | **96** | Ordinary French SVT, chosen for continuity upward into the *lycée* volume: *être vivant*, *milieu de vie*, *chaîne alimentaire*, *décomposeur*, *matière organique*, *villosités*, *alvéoles*, *oreillette / ventricule*, *nidation*, *délivrance*, *règles*, *neurone*, *synapse*, *rétrocontrôle*, *caryotype*, *allèle*, *sélection naturelle*, *flore résidente*, *agent pathogène*, *anticorps*. Unit symbols and all `siunitx` markup byte-identical to English; **0 non-ASCII characters inside `\qty` / `\unit` / `\num`** |
| Register / tone | **96** | Measured against `../one-physics-book/parts/grade-*/fr/` before drafting: *tutoiement* with second-person-singular imperatives in the exercise stems from Année 1 to Année 9 (*Nomme*, *Range*, *Applique*, *Énonce*, *Rédige*), course text impersonal from Année 6 on. The four *vous* forms in the book are all correct — two are quoted speech to a class, one is a four-item plural subject («~la truite, le ver, la libellule et toi… dans votre milieu~»), one is the noun *rendez-vous* |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes**, `nullfont` **20** (the English baseline exactly), 0 `invalid in math mode` — all measured with `grep -a`. **0 TeX accent escapes**, 0 backtick quotes, 352/352 balanced `«~…~»`, French double punctuation (`~:` `~;` `~?` `~!`) throughout, raw UTF-8 accents and `œ` |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English. No curriculum, programme or country name anywhere in visible text |
| Figures | **97** | All TikZ / pgfplots drawing code byte-identical — coordinates, `\foreach` lists, axis options, colours untouched; only node text and `{\small …}` captions localized. Three `\foreach` label lists (grades 2, 3, 4) could not be localized inside a patch without a file-wide `!draw` opt-out, so the English line was kept in the patch and a single targeted post-write edit applied instead — never an opt-out |
| Solutions | **96** | All 796 exercise solutions and all 35 weekend-problem solutions present and native; headers `\section*{Chapitre \ref{ch:…} --- <titre>}` with the `ch:…` slug unchanged. Open-answer models rewritten as French, not glossed (the closing line of the book — «~L'escargot et toi avez été bâtis par les mêmes quatre lettres~: prends soin de toute la famille.~») |
| Defined-term links (`\omterm`) | **95** | **7 532 links over 152 distinct targets**, against English's **7 609 over 152** — 99.0 % density, and the *same target set* (see the two divergences below). Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles |
| MT-artifact freedom | **97** | `check_orphan_lines.py`: **0 orphan English lines**. `check_latin_prose.py`: 17 findings, **all of them the same false positive** (see *Shared-file bug* below) — zero multi-word identical fragments, zero one-word cognate hits in prose. `\text{…}` census over course **and** solutions: 4 of 4 translated (*herbe*, *sauterelle*, *lézard*, *buse*) |

**Overall: 96** (weighted toward terminology + register + MT-artifact freedom; structure is already gated mechanically).

## Structural / build gates

Measurement note: pdfTeX writes `build/*.log` as ISO-8859 text, so a plain
`grep -c '^!'` treats the file as binary, prints nothing and exits 1 — which
reads exactly like a pass. Every figure below was taken with `grep -a`.

| Gate | Result |
|------|--------|
| `latexmk -g one_biology_book_1_primary_middle_school_fr.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -ac 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (one found and fixed — see below) |
| `grep -ac 'nullfont'` | **20** — the English baseline; a rise would be the accent-inside-`\qty` failure |
| `grep -ac 'invalid in math mode'` | **0** |
| `.fls` translated-file count | **142** — every one of the 71 chapters and 71 solution twins really compiled (a failed `\IfFileExists` records nothing and ships English bodies inside a green log) |
| PDF | `build/one_biology_book_1_primary_middle_school_fr.pdf`, **457 pp** (EN 422 — French runs ~8 % longer) |
| `tools/check_translation.sh grade-N fr` | gates 1–8 and 10 **PASSED × 9**; gate 9 fails only on the false positive documented below |
| Elision sweep, re-run **after the last file landed** | `['’]\s*$` → **0**; `^\s*([.,;:)?!]|~[;:?!])` → 0 in prose (only TikZ Bézier `..` continuations, inherited from English); `[a-zà-ÿ]-\s*$` → **0**; trailing `%` → **0**. **No line was ever "fixed" with a trailing `%`** |
| `\index{}` key-set diff | **331 entries over 303 keys, in both editions** — exact parity. The 38 keys spelled identically in the two languages are all true French–English homographs (*adaptation*, *carnivore*, *chromosome*, *synapse*, *virus*…), not survivals |

The single overfull box was `parts/grade-9/fr/03-genes-and-dna.tex`, lines
45–51, 1.41 pt: cured by **adding** a short word before the break point
(«~chacun des parents~» → «~chacun des deux parents~»), not by shortening
the sentence.

## Defined-term links — what the curation actually needed

The uncurated harvest inserted **9 128** links, **20 % more than English
carries on the same text**. Every cause is French, and each is recorded in
`tools/term_config/book1_fr.py`:

| Cause | Effect | Cure |
|-------|--------|------|
| **`paroi`** is *any* wall in French — of a vessel, of the gut, of a capillary | 72 links onto the plant **cell wall** against the twin's 4 | `DROP`; the compound *paroi cellulaire* survives as a term |
| **`règles`** = menstrual periods **and** «~les règles de l'usage durable~» | ~20 rules of method pointing at the ovarian cycle | `STOP` (chapter-local) |
| **`témoin`** = the fair test's control **and** «~les témoins indépendants~» of the evidence chapter | evidence-weighing prose pointing at a plant experiment | `STOP` |
| **`battement`** = heartbeat **and** «~les battements du moteur~» of the selection chapter | engine ticks pointing at the heart | `STOP` |
| **`maillon`**, **`langue`**, **`réserves`** | the audit's "named link", the shared genetic *language*, every metaphorical reserve | `DROP` |
| `équilibre`, `nature`, `arbre`, `mouvement`, `étape(s)`, `adulte`, `champs`, `trier`/`classer`, `contracter` | the same collisions the English config already names | `STOP`, mirroring `book1_en.py` |

Under-linking had two causes worth recording, because both are invisible
without the frequency diff:

* **`animaux`.** French `WORD_TAIL` is `(?:e?s)?`, so the irregular plural of
  the book's commonest term is invisible to the deriver — **124 links** of
  `def:g1:animals-around-us:animal` simply did not exist. Restored via `EXTRA`.
* **The English `DROP` of "arms"/"legs"/"eyes"/"branches" is a no-op**, because
  the harvested key is the singular and the tail regex matches the plural at
  link time. Translating that list literally into French *does* bite, and cost
  **158 links** on `def:g1:my-body:parts`, **93** on the five-senses definition
  and **52** on the grade-1 tree. Restored by dropping only the four the twin
  really suppresses (*tête*, *cou*, *bouche*, *queue*).

### Homograph collisions found and fixed

The frequency diff and the chapter-set diff were run **both ways** and
**after** the overfull sweep, exactly because the frequency test goes blind
when a wrong sense lands on a heavily-linked target. Nine collision classes
surfaced; **84 individually verified wrong links** were removed, plus the
suppressions above:

| Collision | Sites | Cure |
|-----------|------:|------|
| `paroi` (cell wall vs. any wall) | 71 | config `DROP` |
| **`reines`** — `rein` + the tail `(?:e?s)?` matched *les reines*, so the queens blamed for their kingdoms' daughters were linked to the **kidneys** | 2 | `EXTRA_PROTECT` |
| `membres` — "toute paire à un ou trois membres", "les membres de la liste", "les trois membres de phrase" linked to the **limbs** | 4 | reworded (*éléments*, *segments de phrase*, *un élève*) |
| `récupération` — the kidney's reclaiming linked to **exercise recovery** | 3 | reworded to *réabsorption* |
| `branche sur` — the verb *se brancher* linked to a **bough of the grade-1 tree** | 3 | `EXTRA_PROTECT` |
| `éteinte` — "l'épidémie s'est éteinte" linked to **species extinction** | 1 | reworded to *arrêtée* |
| `règles`, `témoin`, `battement` | prevented | `STOP` |

### The two remaining target-set divergences

* `prop:g2:caring-for-nature:recycle` (EN 2 links, FR 0) — the phrase *tri des
  déchets* happens not to recur in the French text outside its own definition.
* `prop:g6:decomposers-and-soil:decomposition` (FR 9, EN 0) — French *décomposition*
  is harvested as a display term where English's *decomposition* is not; the
  sense is correct at all nine sites.

Both are ≤ 9 links and semantically sound; neither is a defect.

## Deliberate divergences from the English wording

Recorded here because a reviewer will otherwise read them as errors:

1. **`ventilation`.** Grade 7 chapter 1 contrasts *respiration* (gas exchange)
   with *breathing* (the chest movements). French SVT reserves **respiration**
   for the exchange and **ventilation** for the movements, so grade 4 keeps the
   everyday *respiration* and grade 7 refines it with
   `\emph{ventilation}\index{ventilation}`. This adds **one French index key
   with no English twin** — the only such key in the book.
2. **Gametes: `cellule œuf` / `cellule mâle`, not `ovule` / `spermatozoïde`.**
   English deliberately uses the plain compounds (*egg cell*, *sperm cell*),
   and in grade 5 *ovule* already denotes the **plant** structure — "les ovules,
   chacun contenant une cellule œuf" would become "ovules containing an ovule".
   A 51-site retrofit was considered and rejected; instead grade 8 glosses them
   in text: «~des \emph{cellules mâles} --- les spermatozoïdes ---~» and
   «~futures \emph{cellules œufs} --- les ovules ---~». This is why
   `def:g8:reproductive-systems:male` carries 51 links against the twin's 23.
3. **`poum-tac`** for *lub-dub*, **`eau de chaux`** for *limewater*,
   **`nidation`** for *implantation*, **`délivrance`** for *afterbirth*,
   **`respiration cutanée`** for *skin breathing* — standard French SVT, chosen
   over calques.

## Sampled fragments, judged

| # | Fragment | Verdict |
|---|----------|---------|
| 1 | *(g1-01)* «~Un escargot glisse lentement sur le chemin mouillé. À côté de lui repose un caillou gris, aussi petit, aussi rond. L'escargot et le caillou reçoivent la même pluie --- pourtant l'un est vivant et l'autre non.~» | **native** — the rhythm and the *pourtant* inversion are French, not carried over |
| 2 | *(g8-07)* «~Électrique le long du fil, chimique à chaque jonction~: tout le système alterne les deux.~» | **native** — nominal-clause parallelism, the natural French form of the English gerund pair |
| 3 | *(g9-06)* «~Les girafes n'ont pas allongé leur cou à force de tirer --- des variantes à cou plus long se sont mieux nourries et ont laissé plus de descendants que les variantes à cou plus court.~» | **native** — «~à force de~» is the idiom a French textbook uses to retire Lamarck |
| 4 | *(g9-02, solutions)* «~La série semble porter un sens~; le mécanisme, lui, ne garde aucune mémoire.~» | **native** — the resumptive «~lui~» is a French move with no English source token |
| 5 | *(g5-08)* «~La dépendance est un piège à entrée facile et à sortie difficile~» | **near-native** — faithful and idiomatic, but the English "easy entrance, hard exit" is punchier than any French rendering found |

No fragment in the sample reads as machine translation.

## Shared-file bug (reported, not edited)

`tools/check_latin_prose.py` fails every Latin-script edition of this book on
a false positive. 18 figures are a label-free image annotated by TikZ overlay
nodes, e.g.

```
\node[anchor=south west, inner sep=0]
  {\includegraphics[width=0.6\linewidth]{images/book1/ai/fig-cat-side.png}};
```

`id_apply.py`'s `img` census **requires** the image path to stay byte-identical,
so these nodes are identical to English *by design*. Inside the checker,
`_word_count()` strips `\includegraphics{…}` — which is why the finding lands
in the low-confidence `node-1word` tier — but `_has_lowercase_word()` does
**not** strip it, so the node fires anyway; and `main()` returns 1 on *any*
finding, including that tier, although the module docstring says only the
multi-word tier is worth blocking on. Result: **17 hits in 14 files**, and
`check_translation.sh grade-1…7 fr` reports FAILED with nothing wrong in the
text. Suggested fix (shared file — not applied here): give
`_has_lowercase_word()` the same `\includegraphics` strip, or have `main()`
return non-zero only for the multi-word tier.

## Why not 100

* Gate 9 cannot be made green from inside the `fr` files (above).
* Density is 99.0 % of English, not 100 %: the residue is real prose choice,
  chiefly `def:g2:where-animals-live:habitat` (EN 79 links, FR 15) because the
  French text says *milieu de vie* / *milieu* where English says *habitat*, and
  `def:g1:plants-around-us:plant` (EN 296 / FR 248).
* One link points at the wrong one of two adjacent targets — *micro-habitats*
  in g6-01 resolved to `where-animals-live:habitat` rather than
  `exploring-our-environment:microhabitat`. One site, correct sense, wrong
  granularity; left in place rather than reworded around the linker.
* `def:g6:exploring-our-environment:conditions` carries 225 FR links against
  176 EN — *lumière*, *humidité*, *température* are commoner in French prose
  than their English counterparts. The sense is right at every site, but the
  density is 28 % above the twin.
