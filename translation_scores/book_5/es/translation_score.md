# One Biology Book 5 — Spanish (`es`) edition: translation score

**Date:** 2026-09-17
**Scope:** `one_biology_book_5_university_year_3_es.tex` — 27 chapters and 27
solutions files of University Biology Year 3 (`parts/bachelor-3/es`,
`parts/bachelor-3/solutions/es`), 54 files in all, plus the curated term
configuration `tools/term_config/book5_es.py`.
**Quality bar:** native *grado / licenciatura* prose — what a Spanish
university biology lecturer would have written for a third-year reader, not
what a careful translator would have produced from the English. English is the
source of truth for content, labels, figures, numbers and structure; native
peninsular Spanish is the source of truth for how it reads.
**Sense reference:** the Spanish Book 4 edition (`parts/bachelor-2/es`,
96/100) for register, instruction voice and house vocabulary — in particular
its impersonal *-se* instruction voice, which this edition matches stem for
stem. The French Book 5 edition was **not** used: it was being written in
parallel by another agent.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (level band, instruction voice) | high | 98 |
| Terminology (consistency, disambiguation) | high | 96 |
| MT-artifact freedom (idiom, calques, word order) | high | 96 |
| Term links (`\omterm` density and sense) | high | 95 |
| Solutions (parity, voice, self-containment) | medium | 97 |
| Figures (TikZ node prose, captions, frozen code) | medium | 94 |
| Cross-references | medium | 99 |
| LaTeX hygiene | medium | 99 |
| Structure and fidelity | low (already gated) | 99 |

## Measured evidence

* Build (`latexmk -g`, forced, after the last prose edit and the last link
  pass): **387 pp; 0 errors, 0 undefined references, 0 overfull boxes,
  `nullfont` 0, 0 `invalid in math mode`**. English baseline: 365 pp with the
  same zeros. `nullfont` 0 and the math-mode count 0 together certify that no
  accent ever entered a `\qty{}`, `\unit{}` or `\num{}` argument — one did
  (`\qty{0.67}{mm/día}`, solutions ch. 24) and was caught by the
  `invalid in math mode` grep and fixed to `mm/d`.
* Underfull boxes are not gated and the English baseline is not zero: English
  **160**, Spanish **144**.
* The `.fls` lists **54** distinct `parts/bachelor-3/…/es/` sources: every
  translated file on disk was really read; no `\IfFileExists` fell back to
  English.
* `tools/id_apply.py` accepted all **54** files. Its censuses (labels,
  environments, solution keys, `\emph`/`\index` counts, math spans byte for
  byte, drawing code, image paths, delimiter counts, brace balance) therefore
  agree with the English twin by construction.
* Counts against English, whole edition: `\index` **913 = 913**, `\qty`
  **2249 = 2249**, `\qtyrange` **34 = 34**, `\num` **232 = 232**, `\emph`
  **1330 = 1330**. Distinct index keys: English 900, Spanish 898 — exactly the two
  English spelling pairs that Spanish has one word for:
  `ortholog`/`orthologue` and `paralog`/`paralogue` each become a single
  `\index{ortólogo}` / `\index{parálogo}`.
* `\omterm`: **2,737 links on 195 distinct targets**, against English's
  **2,670 on 188** — 2.5 % more links, 7 more targets reached.
  `link_defined_terms.py --book 5 --lang es --check` reports "every file
  matches what the config generates", and a plain dry run inserts **0** links.
* **Both homograph censuses** were run against the English twin after the last
  prose edit — per-target frequency *and* per-target chapter set — and re-run
  after every curation change. The first pass flagged eighteen targets; each
  was read in context, and twenty-seven Spanish homograph families went into
  `STOP` (below). The residue is eleven frequency flags and nineteen
  chapter-set flags, every one read in context and every one a correct sense:
  `virus` and `cápside` in the microbiome, stem-cell and molecular-evolution
  chapters; `anticuerpos` in the nervous-system and molecular-evolution
  chapters; `cilios` in innate immunity (the same organelle); `roturas de
  doble hebra` in V(D)J recombination. The four negative flags
  (`def:…:lesions` −24, `def:…:ngs` −14, `def:…:comparative` −9,
  `def:…:retina` −9) are links Spanish *declines* to make, never wrong ones.
* Register census: **zero** *usted* imperatives anywhere in the 54 files, and
  **524** impersonal `-se` instruction stems (`Explíquese` 117, `Calcúlese`
  46, `Calcúlense` 45, `Compárese` 41, `Estímese` 15, `Muéstrese` 14,
  `Nómbrense` 11, `Enumérense` 10, `Arguméntese` 9, `Predíganse` 8,
  `Interprétese` 8 …), matching `parts/bachelor-2/es` stem for stem. The one
  narrative *usted* that survived the first draft (ch. 14 opener, "Usted lleva
  unos treinta y ocho billones de bacterias") was rewritten impersonally
  ("El cuerpo humano lleva …").
* Hygiene sweeps after the last file was written, over **both** directories:
  0 line-end hyphens, 0 line-initial punctuation, 0 line-broken `\index{}`,
  and one line-end apostrophe — a math prime inside a `$…$` span that English
  breaks in exactly the same place (`es/02:210`). The `\text{…}` census is
  down to Spanish abbreviations (`int`, `ext`, `umbr`, `ef`, `pleg`, `media`,
  `alto`, `ambos`, `nec`, `disc`, `real`, `cerebro`, `cuerpo`, `ver`,
  `plegada`, `desplegada`, `sin cubrir`, `sin sitio`, `contra Halcón`,
  `contra Paloma`, `TFG`, `FPR`, `CG`, `EB`) plus the international `on`,
  `off`, `ss`, `crit`, `osm`, `inh`, `pre`, `post`, `contigs`, `nm`, `pN`,
  the codons and the protein names.
* A drawing sweep compared every tikz/pgfplots line still byte-identical to
  English: seven survive and all seven are pure `\addplot` expressions
  (`2*(exp(-0.05*x)-exp(-0.1*x))` and the like). No node string, axis label,
  legend entry or `symbolic coords` list is left in English.
* Non-ASCII audit of every `\qty`/`\qtyrange`/`\unit`/`\num`/`\numrange`
  argument in both directories: **0** offenders after the `mm/día` fix.

## Gates

`bash tools/check_translation.sh bachelor-3 es` → **gates 1–11 PASS**
(completeness, label sets, exercise/solution parity, environment and figure
census, `\index`/`\qty` counts, gate 9 `check_latin_prose.py` with **no
multi-word findings**, gate 10 orphan English lines **0**, gate 11 problem
numbering).

The advisory one-word tier (56 hits) was read line by line and is entirely
cognates and proper names: gene and protein symbols in figure nodes
(`Igf2`, `Drosha`, `Dicer`, `MutS/MutL`, `EcoRI`, `Alu`), the international
subscripts above, and seven statement titles that are the same word in
Spanish (`Apoptosis`, `Virus`, `Evo-devo`) or a person's name
(`Needleman--Wunsch`, `CRISPR--Cas9`). Two of those title hits were real
misses on the first pass — `\begin{proof}[Evidence]` left untranslated in
ch. 18 and ch. 24 — and are now `[Evidencia]`.

### Shared file appended (reported to the coordinator)

`tools/check_latin_prose.py`, `ALLOWED_BY_LANG["es"]`: three lowercase
*Drosophila* Hox gene symbols (`lab`, `pb`, `abd`) added, append-only, with a
comment naming this edition as the evidence. The Hox-cluster figure of ch. 23
carries a `\foreach` whose label field is the canonical gene-symbol list
(`lab, pb, Dfd, Scr, Antp, Ubx, abd-A, Abd-B`); gene symbols are identical in
every edition by design, but the list has slash fields, so it landed in the
**blocking** `foreach` tier. Nothing in the translation was reworded around
the gate.

## Samples (self-review)

1. **ch. 17, chapter opener** — "Una medusa tiene unos pocos miles de neuronas
   en una red sin centro y es capaz de nadar, alimentarse y enderezarse. Un
   pulpo tiene quinientos millones, dos tercios de ellas en los brazos, cada
   uno de los cuales resuelve problemas de los que al cerebro no se le ha
   informado." *Verdict: native.* The English "a problem the brain has not been
   told about" becomes a Spanish impersonal passive with the dative clitic
   ("al cerebro no se le ha informado"), which is how Spanish says it; a
   translator would have written "*sobre los que al cerebro no se le ha
   dicho nada*".
2. **ch. 25, chapter opener** — "En 1968 Motoo Kimura hizo una cuenta que
   inquietó a todo un campo. Al comparar las hemoglobinas, los citocromos y
   otras proteínas de mamíferos cuyos antepasados comunes databan los
   fósiles…" *Verdict: native.* "Al + infinitivo" for the English gerund, and
   the inverted "cuyos antepasados comunes databan los fósiles" (object before
   subject) is ordinary Spanish scientific word order, not a calque of
   "whose common ancestors were dated by fossils".
3. **ch. 20, figure caption** — "por encima del umbral, hacia
   \qty{180}{mg/dL} (\qty{10}{mmol/L}), la glucosa se derrama a la orina ---el
   azúcar en la orina de la diabetes no tratada." *Verdict: native.*
   "Se derrama" for "spills", the em-dash apposition kept, and the units left
   in siunitx with no comma and no accent.
4. **solutions ch. 22, problem q15** — "CO$_{2}$, $28\times 10^{-6}\times
   0.002\times\num{43200} = \qty{2.4e-3}{mol}$, es decir, … \qty{0.073}{g} de
   glucosa ---cien gramos de agua por un gramo de azúcar." *Verdict: native and
   self-contained*: a reader who has the question can follow the answer
   without the English, and the closing image ("cien gramos de agua por un
   gramo de azúcar") reads as a Spanish sentence, not as a gloss.
5. **Exercise stems, all 27 chapters** — "Calcúlese la constante de longitud
   de un axón de \qty{1}{\micro m}…"; "Explíquese por qué un oscilador de
   semicentros necesita fatiga…"; "Predíganse el volumen y la osmolaridad de
   la orina…"; "Resúmase: la ganancia de bucle sana (pregunta~5)…".
   *Verdict: correct register* — impersonal `-se` throughout, never *usted*,
   matching Books 2, 3 and 4 in Spanish.

## Why not 100

* **Four homograph families cost links rather than being resolved.** Spanish
  has one word where English has two, so `AMBIG_POLICY = "drop"` removes the
  link: *ortólogo* and *parálogo* are defined twice (ch. 4 comparative
  genomics and ch. 25 molecular evolution), which English avoids only because
  it spells them *ortholog*/*orthologue* in the two chapters; and *ARNpi* is
  the display of both the non-coding-RNA definition and the piRNA definition,
  where English separates them by number (*piRNA* vs *piRNAs*). Nine and seven
  English links respectively have no Spanish counterpart.
* **Twenty-seven `STOP` families are blunter than English's curation.**
  English protects *conjugation* and *transformation* with collocation
  regexes; in Spanish both are ordinary high-frequency nouns (hormone
  conjugation, homeotic transformation, a mathematical transformation) and a
  regex would have had to enumerate every context, so they are `STOP`ped and
  link only in ch. 12.
* **Figures.** Spanish is 6 % longer than English and the drawing geometry is
  frozen, so eleven pictures overflowed the text block on the first build.
  Fifteen node strings had to be re-broken or shortened (the extinction
  vortex, the sticky-ends detail, the germinal-centre output box, the hair
  bundle, the clock's degradation note, the Hamilton pedigree). The
  information is intact, but those labels are terser than the prose around
  them.
* **387 pp against English's 365**: 6 % longer, the usual Spanish expansion,
  which moves a handful of figures away from the paragraph that introduces
  them.
* **Nine English-canon defects were translated faithfully rather than
  corrected** (they are listed in the final report with file and line): seven
  `\qty{N}{days}` unit arguments, one broken photo credit in ch. 26, and the
  ortholog/orthologue spelling split. Where the defect would have produced a
  silent `nullfont` in Spanish — an accented `días` inside a unit argument —
  the SI symbol `d` was used instead, which is what the rest of the book does.

## Deliberate divergences from the English

* **Index keys are translated** (`\index{neurona!tipos}`, `\index{glía}`,
  `\index{tasa de filtración glomerular}`), so the Spanish index is a Spanish
  index; the count is identical file by file.
* **`\text{}` subscripts are Spanish where they are words** (`umbr` for
  *thr*, `ef` for *eff*, `int`/`ext` for *in*/*out*, `pleg` for *fold*,
  `media`, `alto`, `ambos`, `nec`, `real`, `disc`, `cerebro`, `cuerpo`,
  `ver`), **international where they are not** (`on`, `off`, `ss`, `osm`,
  `inh`, `crit`, `pre`, `post`, `contigs`, the codons).
* **Clinical acronyms follow Spanish usage**: `TFG` for the glomerular
  filtration rate, `FPR` for the renal plasma flow, `P_{CG}` and `P_{EB}` for
  the glomerular-capillary and Bowman's-space pressures; `LTP`/`LTD`,
  `MHC`, `TSH`, `PTH`, `HbA1c`, `ATP` stay international, as Spanish
  textbooks keep them.
* **Game-theory strategies are named in Spanish** — *Halcón*, *Paloma*,
  *Burgués*, *Represalia*, and `EEE` for the evolutionarily stable strategy —
  and the payoff matrix's `\text{}` labels with them.
* **`symbolic coords` keys are ASCII, tick labels are accented.** pgfplots
  cannot take a non-ASCII symbolic coordinate (it aborted the build once, on
  `estómago`), so the keys are `estomago`, `ileon`, `gen tipico`, `seudogen`
  and an explicit `xticklabels=`/`yticklabels=` carries the accented Spanish
  the reader sees.
* **`days` in a unit argument becomes `d`.** `\qty{60}{días}` would put an
  accent in math mode; every such site uses the SI symbol, which is also what
  the English book does everywhere except the seven sites listed above.

## Post-delivery canon alignment (coordinator, 2026-09-17)

After this edition was delivered, six defects that wave 1 found in the English
canon were fixed, and this tree was brought into line with them. The edition
was **not re-translated**; the edits were mechanical and are listed here
because three of them move a census count.

- **ch. 25 no longer re-defines *orthologue*/*paralogue*.** English defined the
  same two notions twice, 21 chapters apart, and escaped `harvest.py`'s
  "defined twice is ambiguous" rule only because ch. 4 spelled them American
  and ch. 25 British. Any language with one word for the concept lost those
  links. Chapter 4 now owns the definition; ch. 25's two markers are plain
  prose. `\index` 913 -> **911**, `\emph` 1,330 -> **1,328**, matching English.
- **Two `\numrange` calls given three arguments** became `\qtyrange`
  (`12-bacteriology`, `solutions/20-renal-osmoregulation`).
- **`day`/`days` inside `\qty{}`/`\unit{}` arguments became `d`**, the form
  Books 3 and 4 use, including the sites frozen inside math spans that no
  translator could reach through `id_apply`.
- The ch. 1 weekend problem's self-referential "question 12" now reads
  "question 11", and ch. 26's truncated photo credit is repaired.

The link pass was re-run from scratch (`--unwrap --apply`, then `--apply`), and
a plain dry run over the wrapped tree reports **`links to insert: 0`**.
Re-measured after the change: **387 pages, 2746 links on 195
targets, `\index` 911, `.fls` 54, 0 errors / 0 undefined / 0 overfull /
`nullfont` 0 / 0 "invalid in math mode", `check_translation.sh bachelor-3 es`
gates 1-11 PASSED.** The self-score above is unchanged.
