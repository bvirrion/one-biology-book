# One Biology Book 3 — Spanish (`es`) edition: translation score

**Date:** 2026-09-06 (re-synced twice the same day to the corrected English canon)
**Scope:** `one_biology_book_3_university_year_1_es.tex` — 29 chapters and 29
solutions files of University Biology Year 1 (`parts/bachelor-1/es`,
`parts/bachelor-1/solutions/es`), 58 files in all, plus the curated term
configuration `tools/term_config/book3_es.py`.
**Quality bar:** native *licenciatura / grado* prose — what a Spanish
university biology lecturer would have written for a first-year reader, not
what a careful translator would have produced from the English. English is the
source of truth for content, labels, figures, numbers and structure; native
peninsular Spanish is the source of truth for how it reads.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (level band, instruction voice) | high | 97 |
| Terminology (consistency, disambiguation) | high | 96 |
| MT-artifact freedom (idiom, calques, word order) | high | 96 |
| Term links (`\omterm` density and sense) | high | 96 |
| Solutions (parity, voice, self-containment) | medium | 97 |
| Figures (TikZ node prose, captions, frozen code) | medium | 95 |
| Cross-references | medium | 99 |
| LaTeX hygiene | medium | 98 |
| Structure and fidelity | low (already gated) | 99 |

## Measured evidence

* Build (`latexmk -g`, forced, after the re-sync): **353 pp; 0 errors, 0
  undefined references, 0 overfull boxes, `nullfont` 0**, and 0 `invalid in
  math mode`. The English baseline for this volume is 339 pp with the same
  four zeros; `nullfont` 0 means no accent
  ever entered a `\qty{}` or `\unit{}` argument.
* Underfull boxes are not a gated metric and the English baseline is not zero:
  English 33 `\hbox` / 130 `\vbox`, Spanish 36 / 128 — the ordinary cost of 14
  more pages of the same material.
* The `.fls` lists **60** distinct `parts/bachelor-1/` sources: the 58
  translated bodies plus the two shared structure files (`part.tex`,
  `solutions/solutions.tex`). **No `\IfFileExists` fell back to English** —
  every one of the 58 files on disk was really read.
* `tools/id_apply.py` accepted all **58** files, and every one was re-applied
  from its patch at the end of the run and re-verified: labels, environments,
  solution keys, `\emph`/`\index` adjacency and counts, math spans, drawing
  code, image paths, delimiter counts and brace balance all agree with the
  English twin by construction.
* `bash tools/check_translation.sh bachelor-1 es`: **PASSED** (gates 1–11,
  including gate 9 `check_latin_prose.py`, gate 10 `check_orphan_lines.py` and
  the new gate 11 `check_problem_numbering.py`, which reports
  `OK (58 chapters)`).
  Gate 10 is at **0 orphan English lines** (it found one, in ch. 28's last
  problem item, and the patch range was widened rather than the line patched).
* Gate 9 residue is advisory only — **0 multi-word findings**. The 14 `node`
  and 26 `text` one-word hits are words that are genuinely identical in
  Spanish (`epidermis`, `endodermis`, `submucosa`, `serosa`, `plasma`,
  `genital`, `virus`, `pili`, `basal`, `base`), pure math node labels, `pol`
  for polymerase, and the internationally standard subscript `\text{cat}`
  of $k_{\text{cat}}$.
* `\label{}` sets are **byte-identical** to English (whole edition, sorted
  diff is empty), and every chapter's `exo:`/`pb:` labels match its solutions
  file's `\begin{solution}{}` keys one for one, in order. No duplicate labels.
* `\index{}` census: **568 entries in Spanish, 568 in English**, and every one
  of the 58 files matches its twin's count individually.
* `\text{…}` census over chapters **and** solutions: **22 distinct forms in
  each edition**, and every Spanish one is Spanish or international —
  `\text{agua}`, `\text{sangre}`, `\text{glucosa}`, `\text{piruvato}`,
  `\text{ácido}`, `\text{base}`, `\text{cél}`, `\text{esfera}`,
  `\text{xilema}`, `\text{fotones}`, `\text{pendiente}`, `\text{cte}`,
  `\text{HR}`, `\text{int}`, `\text{ext}`, `\text{ap}`, `\text{eq}`,
  `\text{tot}`, `\text{ion}`, `\text{cat}`, `\text{ATP}`, `\text{G3P}`.
  Six of them (`water`, `blood`, `glucose`, `pyruvate`, `in`, `out`) and the
  two TikZ labels `cyt $b_6f$` / `cyt $c$` had survived in English and were
  found only by this census: gate 9 files a capitalised or single-word
  fragment in its **advisory** tier, so nothing would have failed on them.
* Unit hygiene: every `\qty{}`, `\qtyrange{}`, `\qtylist{}`, `\unit{}`,
  `\num{}`, `\numlist{}` and `\numrange{}` argument in the 58 files is **pure
  ASCII**, and a brace-aware scan finds **0** `\omterm` (and so 0 `\hyperref`)
  inside any of them. The only alphabetic tokens inside unit arguments are the
  siunitx macro names themselves (`\micro`, `\celsius`) and the standard unit
  words `mmol`, `kcal`, `nmol`, `osmol`, `pmol`, `mmHg`, `NADPH`.
* Decimal separator: **comma in prose, ASCII point inside `$…$`, `\qty{}`,
  `\num{}`, TikZ/pgfplots bodies and LaTeX dimensions**. A masked sweep
  converted 157 prose points and now returns **0** remaining; the mask
  protects `0.46\linewidth`, `p{2.6cm}` and every tikz coordinate, which was
  verified by rebuilding (a first, buggier mask let a `(0.09)` circle radius
  through and pgfmath refused it — caught by the build, then fixed).
* Quotes: **78** `` `` … '' `` pairs, **0** straight ASCII `"`. Accents are
  UTF-8 throughout: **0** hits for `\'e`, `` \`a ``, `\~n`.
* Line-end greps over all 58 files: **0** for `[a-zà-ÿ]-\s*$` (a hyphen split
  across lines), **0** orphan punctuation lines, and the 4 hits for
  `['’]\s*$` are all a closing `''` at end of line, not an elision.
* `styles/onebiology.sty` was **read and not touched**: it already calls
  `\spanishplainpercent` inside the `es` branch, guarded by
  `\IfFileExists{spanish.ldf}`, so babel-spanish's redefinition of `\%` never
  meets a `\lastskip` probe after math mu-glue. No percent construct broke.

## Register

* **Impersonal *-se* throughout**, the voice this project uses for its Spanish
  university volumes and not the *tú* of its school volumes. The choice was
  **measured, not assumed**: the shipped Spanish physics bachelor volumes carry
  360 / 264 / 515 *-se* forms and **zero** *tú* and *usted* imperatives, while
  the Spanish grade-10–12 volumes of both physics and biology carry 684 and 594
  *tú* imperatives. Level, not subject, sets the register.
* This edition: **1,739** *-se* forms; **0** *tú* imperatives and **0** *usted*
  imperatives (the two `compare` hits an automatic scan returns are the label
  fragments `ex:b1:enzymes:compare` and `prop:b1:eukaryotic-cell:compare`).
* The *-se* passive agrees in number with its object throughout —
  *calcúlense los electrones*, *calcúlese la tensión*, *enumérense las
  regiones*, *enúnciese el resultado* — and every exercise stem was measured
  against the shipped `parts/grade-1[012]/es/` register before it was written.
* The six Spanish nouns spelled exactly like an *usted* imperative
  (*nombre, cierre, cruce, contraste, ajuste, apunte*) were censused: **40
  occurrences, every one a noun** (*el nombre binomial*, *el cierre de
  mediodía*, *el cruce de las isoclinas*, *contraste de fases*, *el ajuste
  inducido*), plus one subjunctive (*cuando la sombra de un busardo cruce el
  charco*). None is a stray *usted* imperative.
* Peninsular variety, consistent with the other Spanish volumes of the series.

## Terminology

Glossary decisions, all held consistent across the 58 files: *medio interno*,
*valor de consigna*, *retroalimentación negativa*, *tasa metabólica (basal)*,
*zona de neutralidad térmica*, *superficie de intercambio*, *plan de
organización*, *hojas embrionarias*, *celoma*, *unión estrecha/adherente/
comunicante*, *tejido conjuntivo*, *parénquima en empalizada/lagunar*, *índice
de área foliar*, *meristemo*, *cofia*, *orgánulo*, *sistema endomembranoso*,
*glúcidos*, *enlace glucosídico*, *tampón*, *potencial hídrico/osmótico/de
presión*, *difusión facilitada*, *simportador/antiportador*, *cociente
respiratorio*, *gluconeogénesis*, *cuerpos cetónicos*, *corte y empalme*,
*espliceosoma*, *caperuza*, *cola de poli-A*, *potenciador*, *gen de
mantenimiento*, *hebra conductora/retardada*, *cebador*, *horquilla de
replicación*, *punto de control*, *banda de Caspary*, *apoplasto/simplasto*,
*cohesión--tensión*, *tubo criboso*, *fuente/sumidero*, *capacidad de carga*,
*tasa intrínseca de crecimiento*, *especie clave*, *cascada trófica*,
*deuda de extinción*, *sinapomorfía*, *parafilético*, *grupo externo*.

## Term links

* **5,441 `\omterm` links across 181 distinct targets**, against English's
  **5,495 across 179** — 99.0 % of the canon's density.
* `tools/term_config/book3_es.py` was curated **from this edition's own
  harvest**: nothing was translated from `book3_en.py` and nothing was seeded
  from `book2_es.py`. The uncurated harvest inserted 6,436 links; 24 DROP
  entries, 2 EXTRA entries and 13 EXTRA_PROTECT patterns brought it to 5,403,
  and **every entry was read in its own link contexts before it was written**.
* Both collision censuses were run against the English twin, before and after
  curation, and re-run as the last measurement of the edition:
  * **per-target frequency** — after curation only four targets differ by 25
    links or more. Three are Spanish being *less* verbose than English
    (`cell` −76, `organs` −101, `gene` −28: Spanish drops the repeated noun
    where English repeats it). The fourth, `transporters` +61, is Spanish
    keeping *bomba* (23 links) and *transportador* (22) where English DROPs
    "pump" and "carrier"; all 45 were read and all 45 are the membrane sense.
  * **per-target chapter set** — only two targets reach three or more chapters
    English does not (`transporters`, `compartments`); all of those links were
    read individually and are the defined sense (membrane pumps in ch. 8, 9,
    12, 15, 24; blood plasma in ch. 4, 7, 10, 21).
  * **EN-only targets: none.** Two English targets were initially missing and
    both were restored by EXTRA — `xerófito` (the harvest keys only the
    emphasised plural, and `WORD_TAIL` can add an *s* but never remove one) and
    `nitrato-reductasa` (the harvest loses the hyphenated `\emph{}`).
  * **ES-only targets: two**, both correct-sense links English happens not to
    make (`apilamiento` → base stacking, which English DROPs as "stacking";
    `corrección de pruebas` → proofreading). The third, `punto de control`,
    is now in both editions: English added `"checkpoint(s)"` in the same
    round.
* `WORD_TAIL` in `lang_es.py` is `(?:e?s)?` on every word. Every single-word
  term was checked for a false derived form: `canal` → *canales* and `gen` →
  *genes* are the wanted plurals, and the terms whose *+s* form is a different
  Spanish word are already gone through DROP.
* The curation is documented sense by sense in the config, including the
  eleven English DROP entries that were **checked and deliberately not
  copied** because the Spanish word has no second sense here (*plasma*,
  *tallo*, *carácter*, *operador*, *fuente*, *sumidero*, *polar*,
  *apilamiento*, *absorción*, *resistencia*, *hidrostático*).

## Defects found in the ENGLISH canon (reported, not edited — all now fixed upstream)

1. **`parts/bachelor-1/solutions/16-biosyntheses-integration.tex` was missing a
   numbered solution.** The weekend problem has **25** `\item`s; the solution
   had **24** `\textbf{N.}` entries, numbered 1–11 and 13–25 — `\textbf{12.}`
   was simply absent, so one question had no answer and from 12 on the numbers
   no longer lined up (`\textbf{13.}` gave the protein needed for the day's
   glucose, which is what question 12 asks). Verified by counting the problem's
   `\item`s against the solution's numbers and reading the pairs, before
   claiming it. **The canon now carries 12 (the protein) and a new 13 (the ATP
   cost of the gluconeogenesis, ≈ 265 kJ, some 3 % of the day); Spanish
   mirrors both, the new one written in the edition's impersonal register.**
2. **`parts/bachelor-1/solutions/25-populations.tex` answered three Part III
   questions in the wrong order** — 16 = doubling time, 17 = fixed-fraction
   harvest, 18 = maximum sustainable yield, a three-cycle permutation of what
   questions 16–18 ask. The three answers were individually correct, so no
   gate could see it. Verified against the problem's own item list.
   **Reordered upstream to MSY / doubling time / fixed fraction, and Spanish
   reordered to match.**
3. **`\num{}` used with a stray unit argument.** `parts/bachelor-1/17-genomes.tex`
   wrote `$\num{1.66e-24}{g}$` and `parts/bachelor-1/20-expression-control.tex`
   wrote `$\num{1.5e-13}{g}$`: the unit passed as a second argument to `\num`,
   where `\qty` was meant, so the `{g}` was typeset as ordinary mathematics.
   **Both are `\qty` upstream now, and both Spanish twins carry `\qty`.**
4. **The two `\text{}` labels `cyt $b_6f$` and `cyt $c$`** were reported as
   English residue and the coordinator **checked and correctly declined**:
   *cyt* is the international abbreviation for cytochrome. Spanish nonetheless
   writes *cit*, which is the Spanish spelling of the same abbreviation, so
   this edition keeps *cit* and the canon keeps *cyt*.
5. **`19-gene-expression.tex` cited two stale question numbers** (found by the
   Arabic agent in wave 2; this edition mirrored both faithfully, and neither
   is visible to any structural census because a question number is prose).
   Now question **12** and question **11**; Spanish follows.
6. **`solutions/21-gas-exchange.tex` answer 16 claimed "five times the
   oxygen"** (found by the Indonesian agent): it is 300× by oxygen and 21× by
   mass. Now "a twentieth of the mass, for three hundred times the oxygen";
   Spanish reads *una veinteava parte de la masa, para trescientas veces el
   oxígeno*.
7. **`27-species-interactions.tex` carried a datum that contradicted its own
   question** (found by the Hindi agent): with $\alpha = 1.6$ the isoclines
   cross inside the positive quadrant and the case is founder-controlled, not
   the exclusion the question asserts. $\alpha$ is now **1.4**; the chapter,
   answer 1 and answer 2 were re-translated to match.

## Bugs and blind spots found in the SHARED tooling (reported, not edited)

1. **`tools/id_apply.py`: `!draw` is documented per range and implemented per
   file.** The docstring describes the opt-out as belonging to a range;
   `main()` unions the option over every range of a file, so one `!draw`
   silently disarms the drawing census for the whole file. Not used here.
2. **`tools/check_latin_prose.py` could not see an untranslated capitalised
   one-word optional title.** `_has_lowercase_word()` decided whether a
   fragment was reported in *either* tier, so `\begin{proof}[Evidence]` — 12
   of them, plus two `[Partial proof]` — passed the gate untranslated in this
   edition and had to be found by an independent census of every environment
   title against its twin. **Fixed upstream**: such fragments now land in the
   advisory `-1word` tier, and it caught 20 untranslated titles in another
   edition. This edition's five (`Homeostasis`, `Virus`, `Mitosis`,
   `Henderson--Hasselbalch`, `Michaelis--Menten`) are all correct Spanish.
3. **`NOT_A_TERM` in `tools/link_defined_terms.py` is an English word list**
   (`"paradox"`, `"rule"`, `"law of"`, `"principle"`, …) applied to every
   language, so it silently fails to exclude the translated names of the same
   results. Spanish harvested *paradoja del valor C* and *reglas de Chargaff*
   as terms where English excludes "C-value paradox" and "Chargaff's rules";
   `paradoja del valor C` stays DROPped to keep the two editions carrying the
   same targets; `reglas de Chargaff` stays DROPped and the bare surname
   `Chargaff` now carries the link, which is exactly how English reaches that
   target.

## Where the 4 points went

* Register (−3): the *-se* voice is right and uniform, but a Spanish lecturer
  writing from scratch would vary it more — this edition keeps English's
  one-clause-per-instruction rhythm because `id_apply` verifies structure line
  range by line range.
* Terminology (−4): a handful of terms have two defensible Spanish forms
  (*glúcido/carbohidrato*, *dipnoo/pez pulmonado*, *tráqueida/traqueida*); one
  was chosen and held, but the choice is a judgement, not a fact.
* MT-artifact freedom (−4): long English appositive chains
  ("a vat of a hundred litres in a cow, where food is fermented for a day or
  two, regurgitated and chewed again") were re-cut for Spanish, but the
  sentence *boundaries* are the canon's, because the applier verifies ranges.
* Term links (−4): 99.0 % of the canon's density with two Spanish-only
  targets and no missing ones, but `transporters` carries 61 links English
  does not, and a Spanish reader may find *bomba* linked more often than they
  need.
* Figures (−5): TikZ geometry is frozen, so a Spanish label that wants more
  room gets a shorter word instead of a wider box; a dozen figure labels,
  legend entries and one table header were shortened for that reason
  (ch. 2, 4, 7, 13, 15, 20, 23), each verified by rebuilding the chapter to
  0 overfull boxes.
* LaTeX hygiene (−2): the volume inherits the canon's `\num{…}{g}` construct
  in two places rather than correcting it in one edition only.
