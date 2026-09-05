# One Biology Book 2 — Spanish (`es`) edition: translation score

**Date:** 2026-09-05
**Scope:** `one_biology_book_2_high_school_es.tex` — 36 chapters and 36
solutions files across grades 10–12 (`parts/grade-10`, `parts/grade-11`,
`parts/grade-12`), 72 files in all, plus the curated term configuration
`tools/term_config/book2_es.py`.
**Quality bar:** native *lycée/bachillerato* prose — what a Spanish
upper-secondary biology textbook writer would have written for a 15–18 year
old reader, not what a careful translator would have produced from the
English. English is the source of truth for content, labels, figures and
structure; native Spanish is the source of truth for how it reads.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (age band, instruction voice) | high | 97 |
| Terminology (consistency, disambiguation) | high | 96 |
| MT-artifact freedom (idiom, calques, word order) | high | 96 |
| Term links (`\omterm` density and sense) | high | 95 |
| Solutions (parity, voice, self-containment) | medium | 97 |
| Figures (TikZ node prose, captions, frozen code) | medium | 95 |
| Cross-references | medium | 99 |
| LaTeX hygiene | medium | 99 |
| Structure and fidelity | low (already gated) | 99 |

## Measured evidence

* Build (`latexmk -g`, then incremental): **395 pp; 0 errors, 0 undefined
  references, 0 overfull boxes, `nullfont` 0** — the English baseline for this
  volume is also `nullfont` 0, so no accent ever entered a `\qty{}` or
  `\unit{}` argument. English builds at 379 pp with the same four zeros.
* Underfull boxes are not a gated metric for this volume and its English
  baseline is not zero: English 41 `\hbox` / 126 `\vbox`, Spanish 44 / 143 —
  the ordinary cost of 16 more pages of the same material.
* `.fls` lists **72** distinct translated bodies — every file on disk was
  really read, with no `\IfFileExists` fallback to English.
* `tools/id_apply.py` accepted all **72** files: labels, environments,
  solution keys, `\emph`/`\index` adjacency and counts, math spans, drawing
  code, image paths, delimiter counts and brace balance all agree with the
  English twin, by construction and re-verified per file.
* `bash tools/check_translation.sh grade-10 es`, `grade-11 es`, `grade-12 es`:
  **all three PASSED** (gates 1–10, including gate 9 `check_latin_prose.py`
  and gate 10 `check_orphan_lines.py`).
* Gate 9 residue is advisory only: 7 one-word hits, every one a word that is
  genuinely identical in Spanish — `aorta`, `tibia`, `retina`, `lumbar`, and
  the italic binomials `H. heidelbergensis` and `A. africanus`. Zero
  multi-word findings.
* `\index{}` census: **182 entries in Spanish, 182 in English**, and every
  file matches its twin's count individually (occurrence-level, not
  line-level).
* `\text{...}` census over chapters **and** solutions: 9 occurrences in
  English, 9 in Spanish, 4 distinct, all translated — `\text{músculo}`,
  `\text{carga}`, `\text{energía}`, `\text{luz, clorofila}`.
* Unit hygiene: every `\qty{}`, `\qtyrange{}`, `\unit{}`, `\num{}` and
  `\numrange{}` argument in the 72 files is **pure ASCII**, and none contains
  a word of any language: an audit for `[A-Za-z]{4,}` in a unit argument
  returns **148 hits in Spanish and 148 in English — the same eight kinds in
  the same counts** (`\micro m` ×63, `\celsius` ×48, `\micro m^3` ×13,
  `\micro m^2` ×7, `\percent` ×7, `mmol/L` ×6, `\micro mol/L` ×3,
  `\micro L` ×1). All eight are legitimate siunitx units; the audit matches
  the *names* of the macros once the backslash is stripped. The Spanish unit
  vocabulary is therefore byte-for-byte the canon's, with nothing added.
  Where a unit needed a Spanish word it was written outside the macro
  (`\qty{-40}{dB} por década`, never `\qty{-40}{dB/década}`).
* No `\omterm` — and so no `\hyperref` — is nested inside any `\qty`,
  `\qtyrange`, `\qtylist`, `\num`, `\numlist`, `\numrange` or `\unit`
  argument anywhere in the 72 files: **0 hits** on a brace-aware scan. That
  matters because siunitx typesets a unit argument in math mode, where an
  accented character expands to an invalid escape, drops characters from the
  page and still exits 0.
* Decimal separator: comma in prose, ASCII dot inside `$…$`, `\qty{}` and
  `\num{}`. A scripted sweep that strips math spans, `\qty`/`\num`
  arguments and TikZ bodies finds **0** prose decimal points.
* Line-end greps over all 72 files: **0** hits for `[a-zà-ÿ]-\s*$` (split
  hyphen), **0** for a trailing `%` after a letter, **0** orphan punctuation
  lines outside TikZ `.. controls` path continuations, and the 4 hits for
  `['’]\s*$` are all a closing `''` at end of line, not an elision.
* Quotes: **129** `` `` … '' `` pairs, **0** straight ASCII `"` — see the
  English-canon note below.
* Term links: **5 893 `\omterm` links on 105 distinct targets**, against
  English's **5 547 on 103** — 106.2 % density, no missing target, two extra.
* `python3 tools/link_defined_terms.py --book 2 --lang es --check`:
  *every file matches what the config generates* — the shipped links are
  exactly what `book2_es.py` produces, with no hand edits.

## Register: measured against this repo's own twins, not assumed

The instruction voice was fixed **before** any exercise stem was written, by
counting the stems of the two nearest Spanish twins in this workspace:
`one-physics-book/parts/grade-1[012]/es` (30 `Calcula`, 0 `Calcule`) and this
repo's own `parts/grade-9/es` (Nombra 10, Enuncia 9, Explica 8, Define 3,
Enumera 2, Describe 1, Calcula 1, Compara 1 — all *tú*).

Book 2 `es` therefore uses **tú imperatives throughout**: Explica 54, Define
21, Nombra 17, Enumera 12, Da 11, Describe 10, Compara 8, Calcula 6, Predice
4, Enuncia 3, Discute 2, Clasifica 2, plus singletons (Toma, Interpreta,
Estima, Dibuja). **`usted` forms: 0.** The only line-initial `Lea` in the
volume is the given name of a person in a pedigree exercise, not the *usted*
imperative of *leer*.

This was a reviewed conversion, never a regex, and the six Spanish nouns that
are spelled exactly like a *tú* imperative — *nombre, cierre, cruce,
contraste, ajuste, apunte* — were checked by hand in every place they occur;
none of them was produced by, or mistaken for, an imperative. The impersonal
`-se` passive of the experimental sections agrees in number with its object
throughout (*se recogen los ovocitos*, *se secciona la raíz dorsal*, *se
cortan los estomas*, *se añaden dos entradas*).

## Terminology

The technical vocabulary follows Spanish school usage, not the English
morphology: *reflejo miotático* (not *reflejo de estiramiento*), *huso
neuromuscular*, *células oclusivas*, *savia bruta / savia elaborada*,
*pelos absorbentes*, *línea pura* for *inbred line*, *síndrome de
domesticación*, *desgranarse* for *shattering*, *linfocitos T colaboradores*,
*inmunidad de grupo*, *vía final común*, *unidad motora*, *sustancia gris*,
*hendidura sináptica*, *consigna* for a regulated set point, *retroalimentación
negativa*, *sida* (lower case, per RAE) for *AIDS*, *ictus* for *stroke*,
*barrenador* for *borer*, *arrendajo* for *jay*, *teosinte / zuro / brácteas*
for the maize ear.

`styles/lang/es.tex` was used as-is for every UI string; it was not edited.

## babel-spanish

`styles/onebiology.sty:160` already calls `\spanishplainpercent`, so `\%`
keeps its ordinary meaning under `babel`-`spanish`. Nothing here undoes it and
no spacing trick was added around any `\%`; the 60-odd percentages of the
volume typeset exactly as in English.

## The two collision censuses, and what they caught

Both censuses were run **last**, over the finished edition, and both were run:
a per-target *frequency* diff against `--lang en`, and a per-target
*chapter-set* diff. A third, per-target *display* census (which distinct
strings each target collects) was run alongside them, because the frequency
census alone is blind to a target that collects a large number of wrongly
sensed links from a single word.

**The display census found the one real defect, and the frequency census
confirmed it.** `def:g10:biodiversity-scales:biodiversity` was collecting
**170** links whose displayed word was `especies`. Both editions wrote
*the diversity of `\emph{species}`* inside the **Biodiversity** definition and
*a `\emph{species}` is …* in the **Species** definition immediately after it.
English spelled the two the same, so its harvest saw one term defined twice
and dropped it: `--lang en` linked "species" **zero** times. Spanish spells
them `especie` and `especies`, so the harvest saw two different terms, kept
both, and pointed 170 links from the commonest noun in the volume at a
definition of *biodiversity* — which is not what the word means. A `DROP` was
the right call against that canon, and removed all 170.

**The canon has since been fixed at the source, and the term restored.** The
marker moved off the Biodiversity bullet onto the Species definition itself,
in English and in the Spanish body alike, so there is now exactly one
`especie` term pointing at `def:g10:biodiversity-scales:species` — the
definition those 170 links were reaching for. The `DROP` is gone and nothing
replaces it: `WORD_TAIL` derives *especies* from the singular key for free.

Before restoring it, every `especie de` in the volume was censused for the
ordinary Spanish *a sort of / a kind of* idiom, which English's *species*
cannot produce and which would have needed `EXTRA_PROTECT`. There are two,
and **both are taxonomic** — *el ciclo de toda especie de reproducción
sexual* (g12/01) and *una especie de cuerpo pequeño en una isla* (g12/05);
English links `species` at both twins. Spanish has no independent homograph
here and needs no protection.

The result is the tightest parity in the volume: `especie`/`especies` now
carries **272 links in Spanish and 272 in English**, over the same chapter
set, from 171 *especies* and 101 *especie*; and
`def:g10:biodiversity-scales:biodiversity` settles at **37 = 37**. Neither
target appears in the frequency census any more, and neither appears in the
chapter-set census. The only residue is one extra *file* on the Spanish side:
`grade-12/solutions/es/06-plant-rooted-life` renders English's *flowers of
their own kind* as *flores de su misma especie*, which is what the sentence
means biologically and which the linker therefore picks up.

The same censuses caught three wrong-sense links on *portador*: “los
portadores de cepas resistentes” of the hospital-hygiene section are people
carrying an **infection**, not heterozygotes carrying an allele. English
writes "carriers" in the same three places and links none of them.
`EXTRA_PROTECT` now guards both phrasings.

Watch-list words that were censused and came back **clean** (every occurrence
in the defined sense, or no occurrence at all): *cultivo* vs *cultura*
(Spanish splits the English collision into two different words — only
*cultura* collides, and it is dropped), *núcleo* (55 + 8, all the cell
nucleus), *sustrato* (29, all the enzyme/metabolic substrate), *tallo*,
*cadena*, *marco*, *placa*, *vaso*, *presión*, *medio*, *carácter*,
*disolución*, *huso* (none of these is a term in this volume), *bastón*
(the walking stick of the rehabilitation chapter is singular, and the term key
is the plural *bastones*, so it never matched), *islote* (9 of its 13 uses are
a small **island** in the drift chapter — this is why `islote` was deliberately
**not** added to `EXTRA` even though the pancreatic islet term is plural-only).

### Deliberate, measured divergences from the English link placement

Each of these was checked against the criterion *does the displayed word
denote the subject of the definition it points at?* Each answers yes, and each
is recorded here because the frequency census flags it:

| target | en | es | why |
|---|---:|---:|---|
| `def:g11:genes-and-disease:genetic` | 46 | 163 | English `DROP`s "carrier" because of the NAD **carriers** of respiration and photosynthesis. Spanish carries those on *transportador*, so the collision does not exist; *portador/portadora/portadores/portadoras* is the heterozygote everywhere but the three protected places. |
| `def:g11:the-eye:parts` | 12 | 98 | English `STOP`s "eye" for "the naked eye" / "under the eye of". Spanish has exactly one such metaphor (*con un ojo humano en lugar del ambiente*), which `EXTRA_PROTECT` guards; the other 98 are the organ. |
| `prop:g11:antibiotic-resistance:mechanisms` | 2 | 85 | English `STOP`s "resistant". Spanish has three uses of *resistente* meaning *tough* (the tough stalk of the first cultivated wheats, the tough tissue of a ligament); those are protected, and the rest are the evolved resistance of bacteria, borers and weeds. |
| `def:g10:universal-dna:nucleotide` | 54 | 120 | English `DROP`s "bases" for "acids and bases". Spanish's 66 *bases* are the four DNA bases; the single skull *base de cráneo* is protected. |
| `prop:g11:becoming-male-female:hormones` | 6 | 50 | English harvests "testosterone" in a way that leaves it linked in only two files; the Spanish *testosterona* is the same hormone in all 50 places, in the two chapters that discuss it plus one back-reference. |
| `def:g10:chemistry-of-life:families` | 247 | 289 | An ambiguity-resolution difference, not a sense difference: English has "protein"/"proteins" both ambiguous between the chemistry and the gene-expression definitions, while Spanish's plural *proteínas* was harvested unambiguously by the chemistry definition. Both targets are correct definitions of *protein*; `def:g11:gene-expression:protein` correspondingly drops from 129 to 80. |
| `def:g10:common-ancestry:homology` | 11 | 2 | The reverse: **Spanish links fewer.** English writes "homologous chromosomes" and can protect that phrase; Spanish uses *los homólogos* as a bare noun through meiosis and polyploidy, and 24 of the 28 occurrences of the word are the meiosis homologue. `DROP {"homólogos"}` costs 8 same-chapter links and prevents 24 wrong ones; *homología* keeps the sense linked where it is meant. |
| `prop:g11:cancer:genes`, `prop:g11:enzymes-and-phenotype:pathway` | 0, 0 | 1, 1 | Two targets English leaves orphaned. Spanish writes *protooncogenes* without the hyphen and *vía metabólica* recurs once outside its definition, so each collects one honest link. |

`prop:g12:innate-immunity:drugs` was, at first, the mirror-image loss: the
harvest saw only the plural *antiinflamatorios* of the definition display,
while every later mention is singular, so the target fell to zero links
against English's two. `EXTRA {"antiinflamatorio"}` restored it — the missing
target was found by diffing the target **sets**, which is why that diff is
worth running even when the totals look healthy.

### On `STOP`

Nothing in `book2_es.py` relies on `STOP`, and the brief's warning is
confirmed on the English canon itself: `book2_en.py` lists `"eye"` in `STOP`,
yet `--lang en` still emits **12** `\omterm` links whose display is *eye*.
Every suppression in the Spanish config is therefore either a `DROP` of a
harvested key or an `EXTRA_PROTECT` regex, and each one was verified by
re-running the per-target frequency diff before and after.

## `book2_es.py` provenance

Curated from **this** edition's own harvest (153 terms → 226 linkable
spellings), term by term. It was **not** seeded from `book1_es.py`, and
`book2_en.py` was read for the *senses* that collide in this volume, not
transposed: three of English's five collisions (culture, carrier, bases) do
not exist in Spanish, and Spanish has two English never had (*especies*,
*homólogos*).

`lang_es.py`'s `WORD_TAIL = r'(?:e?s)?'` with `TAIL_ON_EVERY_WORD = True` was
read first and its consequences worked out before curating. It builds plurals
and never strips them, and it never rewrites an accent: *cáncer* reaches
*cánceres*, but *población* only reaches *poblaciónes*, which is not a Spanish
word. Every `-ción`/`-ón` term therefore needed its real plural in `EXTRA`
(*poblaciones*, *mutaciones*, *articulaciones*, *tendones*), and Spanish
gender needed the other form (*recesiva*, *portadora*, *autótrofo*,
*heterótrofo*). Between them those eight entries are worth about 300 links
that would otherwise have gone missing.

## Figure text: what the `draw` census freezes, and how it was translated

`id_apply.py`'s `draw` census blanks node text, `\legend{}`, `\addlegendentry{}`,
the `AXIS_STR` keys and `\text{}` — but it does **not** blank `\foreach` value
lists, `matrix of nodes` cells, or the coordinate names of a
`symbolic x/y coords=` list that an `addplot` also names. Rather than opt a
whole file out of the census, every such string was translated by a recorded
post-edit applied after `id_apply` (`postedits.tsv`, 49 entries over 13
files): the size-ladder, gel-ladder, pond-species and cladogram `\foreach`
label lists of g10/02, g10/05, g11/01, g11/06 and g12/04, the
`matrix of nodes` rows of g12/04, and the paired `symbolic coords` +
`addplot` coordinate names of g10/03, g10/05, g10/08, g10/10, g11/06, g11/12,
g12/05, g12/09 and g12/14. Accented coordinate names (*fermentación*, *glucólisis +
Krebs*, *respiración completa*, *África subsahariana*, *pie y dedos del pie*)
build cleanly under pdfTeX; the 0/0/0/0 log is the check.

### Figure text that had to diverge from English to fit the page

Spanish runs 15–20 % longer than English, and seven labels overflowed the text
block. Each was shortened or rewrapped — never fixed with a spacing trick,
never by resizing the image:

* `grade-10/es/02-cells-common-unit`: the plant-cell node
  `{membrana plasmática}` → `{membrana}` (the full term stays in the caption).
* `grade-11/es/08-antibiotic-resistance`: the pgfplots `\legend` shortened to
  `células sensibles, resistentes (una de cada $10^5$), total si se corta el
  día 3`.
* `grade-11/es/11-the-eye`: opsin-tree labels
  `{opsina de los bastones (rodopsina)}` → `{rodopsina (bastones)}` and
  `{gen ancestral de opsina}` → `{gen ancestral}`.
* `grade-12/es/05-human-evolution`: six overlay labels rewrapped onto two
  lines or trimmed — `humano: abertura` for *human: cord opening*,
  `pelvis en cuenco` for *short bowl-shaped pelvis*, `columna oblicua,\\
  cabeza colgada` for *oblique spine, head hung forward*.
* `grade-12/es/06-plant-rooted-life`: the stoma label dropped its trailing
  `(epidermis inferior)`, which the label beside it already carries, and
  `{epidermis inferior}` was wrapped onto two lines.

One further divergence is typographic rather than spatial: the pgfplots nodes
`{meiosis I}` / `{meiosis II}` of `grade-12/es/01-meiosis-genetic-shuffling`
are written `{meiosis~I}` / `{meiosis~II}`. The phrase is genuinely identical
in Spanish, and gate 9's multi-word tier — correctly, by its own rule — refused
a two-word fragment byte-identical to English. The non-breaking space is
standard Spanish typography for a roman numeral after a noun and clears the
gate honestly, without pretending the words differ.

## Late canon change, re-synchronised

`parts/grade-11/01-dna-replication.tex` changed under this run: lines 290 and
399 had wrapped an `\omterm` **inside** a siunitx unit
(`\qty{50}{\omterm{...}{nucleotides}/s}`) and were rewritten as prose,
matching the idiom line 171 already used. The line count stayed 408 and no
other line moved.

The Spanish file had rendered those two sites as `\qty{50}{nucleotides/s}` —
no nested link, but an English noun typeset in math italic inside a Spanish
book, and the same trap one accent away. Both are now prose in the register
line 178 already used (*añade unos 1000 nucleótidos por segundo*):

* `a 50 nucleótidos por segundo` (exercise 9)
* `con horquillas de 50 nucleótidos por segundo` (weekend problem, part II)

The English twin cache was re-unwrapped, the patch regenerated and re-verified
by `id_apply`, the linker re-run over the whole edition (5 619 → **5 621**
links: exactly the two new occurrences of *nucleótidos*, which is what the
canon now links there too), and the build, the three gates, `--check` and both
censuses re-run afterwards. All still green.

## Two late canon changes, re-synchronised

Besides the `\qty` fix above, two content changes landed in the English canon
after this edition was first delivered. Both were re-checked in Spanish and
the whole pipeline was re-run after each.

**1. The Species definition got its marker back** (see the census section):
the `DROP` on *especies* was retired, the linker re-run over all 72 files, and
the count went 5 621 → **5 893**, i.e. **+272** — the exact figure English
gained. Build, three gates, `--check` and both censuses all re-run against the
**new** English twin, not the stale baseline.

**2. `wild mustard` → `wild cabbage`** in the six-crops figure of
`grade-12/07-domesticated-plants` (all six are *Brassica oleracea*). The
Spanish node is now `col silvestre`, which is both the right plant and the
right word: it restores the naming pattern the whole figure depends on, since
every one of its six descendants is a *col* — col rizada, repollo, col de
Bruselas, colinabo, brócoli, coliflor. The old *mostaza silvestre* was wrong
twice over in Spanish. *Mostaza silvestre* correctly survives in exercise 12,
where the canon still says *wild mustard*, because there it is a true and
different statement about rapeseed crossing with a wild brassica.

## Samples

**1 — Chapter opening (g12/13, `El reflejo miotático`). Native.**
> Un médico te golpea con un martillito de goma el tendón que hay justo
> debajo de la rótula, y tu pie da una patada hacia delante antes de que hayas
> sentido nada. Treinta milisegundos separan el golpe de la patada: demasiado
> poco para el cerebro, demasiado poco incluso para una decisión.

Verdict: **native**. The dative-of-interest `te golpea … el tendón` is how a
Spanish writer says *taps your tendon*; a translator would have written
*golpea tu tendón*. `martillito` carries the English diminutive *small rubber
hammer* in one word, and `antes de que hayas sentido nada` takes the
subjunctive Spanish requires after `antes de que`.

**2 — Evidence paragraph (g12/10, insulin). Native.**
> Quitarle el páncreas a un perro (1889) lo vuelve diabético en un día: su
> glucemia se triplica y aparece glucosa en su orina; ligar el conducto que
> lleva las enzimas digestivas no lo hace, así que el efecto no es digestivo.

Verdict: **native**. `Quitarle … a un perro` is the obligatory Spanish clitic
doubling that an MT pipeline drops; `volver + adjective` for *makes it* rather
than the calque `hacer diabético`; `no lo hace` as the pro-verb English gets
from *does not*.

**3 — Exercise stem (g12/07, ★★★). Native.**
> ``La domesticación es lo contrario de la selección natural.'' Discútelo en
> un párrafo, con la aritmética de las frecuencias alélicas, el agente de la
> selección y el destino de la planta seleccionada.

Verdict: **native**. *tú* imperative with an enclitic pronoun (`Discútelo`,
accented as the enclisis requires), Spanish `` `` '' `` quotes, and
`lo contrario de` rather than the calque `el opuesto de`.

**4 — Solution (g12/09, question 14). Near-native.**
> Respiración: $1/30$ de glucosa por ATP; fermentación: $1/2$ --- quince veces
> más glucosa. El músculo lo acepta porque el ATP hace falta ahora y el
> glucógeno está ahí; la deuda se paga después.

Verdict: **near-native**. Idiomatic and correctly clipped for a solutions
register, but `el glucógeno está ahí` is a shade closer to the English *the
glycogen is there* than a Spanish writer's `hay glucógeno de sobra`. Kept
because the parallel with `el ATP hace falta ahora` is the point of the
sentence.

**5 — Figure caption (g12/12, herd immunity). Native.**
> La fracción de una población que tiene que ser inmune para detener la
> propagación de una enfermedad, frente al $R_0$ de esa enfermedad. Cuanto más
> contagiosa es la enfermedad, más cerca de todo el mundo tiene que estar la
> cobertura.

Verdict: **native**. `Cuanto más … más …` is the Spanish correlative
comparative, not a rendering of *the more … the closer*; `frente al` is the
standard caption preposition for *against* on an axis.

**No sample in the volume reads as MT.** The one MT-shaped sentence that did
survive the first pass — a g11/03 remark that had become *al antibiótico no lo
hizo resistentes a las bacterias* — was caught on review and rewritten as
*el antibiótico no volvió resistentes a las bacterias*.

## Defects found in the ENGLISH canon (reported, not fixed)

1. **264 straight ASCII `"` double quotes across 41 English source files**, and
   **zero** `` `` … '' `` pairs. In OT1/T1 a straight `"` typesets as `”`, so
   every quoted phrase in the English Book 2 opens with a *closing* quotation
   mark: `”Domestication is the opposite of natural selection.”`. The Spanish
   edition uses `` `` … '' `` (129 pairs, 0 straight quotes) and therefore does
   **not** reproduce the artefact.
2. **`def:g10:biodiversity-scales:species` is an orphan target in English.**
   Because `\emph{species}` occurs both inside the Biodiversity definition
   (`parts/grade-10/05-biodiversity-scales.tex:23`) and as the Species
   definition's own display (line 52), the harvest drops the term as "defined
   twice" and the Species definition collects **zero** `\omterm` links in the
   English edition. Disambiguating one of the two displays (English does this
   elsewhere with a parenthesis, e.g. `trunk (body)`) would give the
   definition its links back — and would have prevented the Spanish
   mis-targeting described above, which is the same source defect seen from
   the other side.
3. **A split hyphen at a line end in the English canon:**
   `parts/grade-12/solutions/07-domesticated-plants.tex:88` ends a line with
   `Non-` and continues `biological:` on the next. That is exactly the pattern
   the repository's own translation procedure forbids (fix by rewrapping,
   never with a trailing `%`), and it is the only one in the volume.
4. **`STOP` does not suppress what it claims to.** `book2_en.py` lists
   `"eye"` in `STOP`, yet the English edition still ships 12 `\omterm` links
   whose display is *eye*; `"frequencies"` and `"resolution"` behave the same
   way. This is the documented caveat, confirmed on the canon itself, and is
   why nothing in `book2_es.py` depends on `STOP`.

## Gate bugs hit

None that misfired. Gate 9 (`check_latin_prose.py`) blocked once, on
`{meiosis II}` — and it was **right** to: a two-word TikZ node byte-identical
to English is exactly what it is looking for, and no gate can know that
*meiosis II* is also correct Spanish. The fix was made in the translation
(`meiosis~II`), not in the gate. The remaining seven one-word hits are
correctly reported as advisory.

## Why not 100

* **−1, term-link density.** At 106.5 % of the English link count the edition
  is honest but not identical in placement; six targets diverge by more than
  40 links, each for a reason argued above, and a Spanish editor reading the
  eye chapter would probably still find *ojo* linked more often than the
  reading eye wants.
* **−1, the protein ambiguity.** 42 links point at
  `def:g10:chemistry-of-life:families` where English points at
  `def:g11:gene-expression:protein`, because the Spanish plural *proteínas*
  was harvested unambiguously. Both destinations define *protein*, so no
  reader is misled, but the two editions are not interchangeable here.
* **−1, seven figure labels shortened.** The overlay labels of g12/05 and
  g12/06 and the legend of g11/08 carry slightly less information than their
  English twins, because Spanish needed the width. Nothing false was written,
  but a reader comparing editions would notice.
* **−1, residual translator's rhythm.** A handful of solution sentences
  (sample 4) keep the English clause order where a Spanish writer would have
  reordered. They read as good Spanish, not as MT, but they read as *written
  from* something.
