# One Biology Book 1 — Spanish (`es`) edition: translation score

**Date:** 2026-09-04
**Scope:** `one_biology_book_1_primary_middle_school_es.tex` — 71 chapters and
71 solutions files across grades 1–9, plus `frontmatter/preface.es.tex` and
`frontmatter/image-credits.es.tex`.
**Quality bar:** native *school* prose — what a Spanish primary/secondary
science textbook writer would have written for this age band, not what a
careful translator would have produced from the English. English is the source
of truth for content, labels and structure; native Spanish is the source of
truth for how it reads.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (age band, instruction voice) | high | 97 |
| Terminology (consistency, disambiguation) | high | 96 |
| MT-artifact freedom (idiom, calques, word order) | high | 96 |
| Term links (`\omterm` density and sense) | high | 96 |
| Solutions (parity, voice, self-containment) | medium | 97 |
| Figures (TikZ node prose, captions, frozen paths) | medium | 97 |
| Cross-references | medium | 99 |
| LaTeX hygiene | medium | 99 |
| Structure and fidelity | low (already gated) | 99 |

## Measured evidence

* Build: 453 pp, **0 errors, 0 undefined references, 0 overfull boxes,
  0 underfull hboxes, `nullfont` 20** (the English baseline exactly — no
  accent ever entered a `\qty{}` argument), **0** `invalid in math mode`.
  `.fls` lists **142** translated bodies, i.e. every file on disk was really
  read (no `\IfFileExists` fallback to English).
* `tools/id_apply.py` accepted all 142 files: labels, environments, solution
  keys, `\emph`/`\index` adjacency and counts, math spans, drawing code, image
  paths, delimiter counts and brace balance all agree with the English twin.
* `tools/check_translation.sh grade-1..9 es`: **all nine years PASS** (gates
  1–10, including the two prose gates, gate 9 `check_latin_prose.py` and
  gate 10 `check_orphan_lines.py`).
* `tools/check_latin_prose.py` over all 142 files: **OK, zero findings in
  either tier** — no identical multi-word fragment, and not even a one-word
  advisory hit.
* `tools/check_orphan_lines.py`: **0** orphan English lines.
* Line-end greps: **0** prose hits for `['’]\s*$`, `[a-zà-ÿ]-\s*$`; the 21 hits
  for `^\s*([.,;:)?!])` are all TikZ `.. controls` path continuations, which
  `id_apply` requires to stay byte-identical to English.
* `\index{}` census: **331 entries in Spanish, 331 in English**, and every file
  matches its twin's count individually. The 9 keys spelled identically in both
  editions (`animal`, `bacteria`, `diabetes`, `humus`, `molar`, `placenta`,
  `saliva`, `urea`, `virus`) are true Spanish cognates, not survivals.
* `\text{...}` census over chapters **and** solutions: 4 in English, 4 in
  Spanish, all translated (`hierba`, `saltamontes`, `lagartija`, `ratonero`).
* Term links: **7 748 `\omterm` links on 151 distinct targets**, against
  English's 7 609 on 152 — 101.8 % density.

## Register: measured, not assumed

The reference for a grades 1–9 Spanish voice is the physics Book 1 `es`
edition. Its exercise stems were counted before a single biology stem was
written: **339 tú-imperatives** (Nombra 55, Explica 54, Da 41, Calcula 39,
Escribe 27, Dibuja 26, Enuncia 22, …) against **3** apparent *usted* forms, all
three of which turned out to be the girl's name *Lea*. Ruling: Book 1 `es` uses
**tú imperatives** in exercise stems, unlike the university volumes' impersonal
`-se` forms.

The finished edition was then counted the same way: **275 line-initial
tú-imperatives** (Nombra 52, Da 29, Explica 25, Enuncia 23, Enumera 16, …) and
**0** *usted* imperatives. The single `^Lea` hit is again the character's name,
mirroring the English twin. The six Spanish nouns that are spelled exactly like
an *usted* imperative (*nombre, cierre, cruce, contraste, ajuste, apunte*) were
checked by hand rather than by regex; none is a stem.

## Terminology decisions worth recording

Deliberate splits, made so that one English word does not become one
over-loaded Spanish word:

* **respiración / ventilación** — grade 4's *breathing* is `respiración`;
  grade 7 introduces `ventilación` for the movement so that `respiración` can
  carry the cellular sense the chapter defines.
* **tráquea / tráquea (insecto)** — the human windpipe and the insect trachea
  are indexed apart, exactly as English separates *windpipe* from *tracheae*.
* **tierra / suelo** — grade 1's growing medium is `tierra`, grade 6's studied
  soil is `suelo`, so the young chapter never forward-links to a definition
  five years away.
* **menstruación** over *regla*, and **oviducto** over *trompa*, to keep the
  reproductive chapters free of the *rule* / *tube* homographs.
* **cabello / pelo** — human head hair vs. animal covering, so the grade-9
  cold-case problem does not link a forensic hair to the grade-1 definition of
  fur, feathers and shells.
* **sala del hospital** — never *planta*, which is also the book's word for a
  plant.

## Homograph collisions: 16 classes found and fixed

The frequency census alone cannot see these — a wrong sense landing on a
heavily-linked target is invisible in a total — so the **chapter-set** census
(which chapters link a target that English never links there) was run as well,
and it is what found most of the list.

Fixed by rewriting the Spanish (24 sites): `pelo` → `cabello` (human hair, 11
sites); `planta` → `sala` (hospital ward, 8 sites); `suelo` → `fondo` / `piso`
/ `mínimo` (floor and lower-bound senses, 5 sites).

Fixed by curation in `tools/term_config/book1_es.py`: `testigo` (experiment
control **vs. witness** — grade 9 uses *testigos independientes* on almost
every page; STOPped, as English STOPs *control*); `anuales` (annual plant vs.
*vacunas anuales*); `eslabón` (food-chain link vs. the method chapters' *nombra
su eslabón*); `tierra` (soil vs. *la Tierra*); `vaso` (blood vessel vs. the
grade-7 *vaso de agua* — only the plural is linked, and the singular phrase is
protected); `hoja de puntuación` (sheet, not leaf); `la yema de la …` (yolk,
not bud); plus `árbol`, `naturaleza`, `equilibrio`, `movimiento`, `clasificar`
and the five sense names, each STOPped or DROPped exactly where `book1_en.py`
does the same for the same reason.

One collision is **not** fixable and is documented instead: Spanish `óvulo`
covers both the animal egg cell (grade 4) and the plant ovule (grade 5), where
English has two words (*egg cell*, *ovule*). The engine keeps the grade-4
target, so grade 5's ovules link to the definition of the female reproductive
cell — which is precisely the analogy that chapter opens with ("la reproducción
de las plantas con flores es reproducción sexual, exactamente en el sentido de
la \cref{def:g4:animal-reproduction:sexual}"). It costs 8 links on
`prop:g5:flower-to-fruit:roles` and is the one target English has that this
edition does not.

## Link-density divergences, and why each is honest

Every remaining per-target difference of 6 links or more was inspected:

* `+70 def:g6:exploring-our-environment:conditions` — Spanish must say
  `humedad` where English says *damp*, *dampness* and *moisture*; all three are
  the same environmental condition the definition names.
* `+51 def:g4:animal-reproduction:sexual` — Spanish inflects for gender
  (`femenina`, `masculino`) where English reuses *male* / *female*; the extra
  links are the same sense, and without them Spanish adjective phrases went
  unlinked entirely.
* `−45 def:g1:plants-around-us:plant` and `+37 def:g5:…:cell` — `célula
  vegetal` is one noun plus one adjective where English writes *plant cell*,
  two nouns.
* `−37 def:g1:my-body:parts` — Spanish splits English *leg* into `pierna`
  (human) and `pata` (animal). Only the human word is linked, which is arguably
  more accurate than the canon: the definition is of *my* body. Linking `pata`
  as well was measured at +86 links and rejected.
* `−30 def:g3:bones-and-muscles:skeleton` — English has *spine* (grade 3) and
  *backbone* (grade 4) as separate words; Spanish has one, `columna vertebral`,
  which the nearest-preceding policy routes to whichever definition the reader
  has most recently met.

## Sampled fragments

1. *Grade 1, definition* — “Un **ser vivo** es algo que está **vivo**: nace, se
   alimenta, crece, puede tener crías y un día muere.” — **native**. The
   asyndetic verb list is exactly how a Spanish infant-school text lists the
   signs of life; no English word order survives.
2. *Grade 1, example* — “El caracol nació de un huevo diminuto. Come hojas de
   lechuga. Crece --- su concha crece con él. Puede haber caracoles bebés.” —
   **native**. Short sentences, present tense, the dash used as Spanish uses
   it.
3. *Grade 7, digestion* — “las unidades pequeñas de la **materia de
   construcción**, de la carne, el pescado, los huevos, los lácteos y las
   legumbres --- los ladrillos de la construcción” — **native**. `los
   lácteos` and `las legumbres` are the register's own words, not glosses of
   *dairy* and *pulses*.
4. *Grade 9, evolution* — “las variantes de cuello más largo comieron y
   criaron más que las de cuello más corto.” — **native**. The comparative is
   restructured away from English's *out-fed and out-bred*, which has no
   Spanish shape.
5. *Grade 9, immunity* — “la memoria entrenada y puesta en común es la única
   arma que ha exterminado jamás una enfermedad humana.” — **near-native**.
   `puesta en común` for *pooled* is idiomatic and consistent across the
   chapter, but it is a two-word rendering of a one-word English term and reads
   very slightly heavier than a Spanish original would.

No fragment in the sample reads as machine output: there are no calqued
possessives, no English comma habits, no *-ing* participial chains, and the
`check_latin_prose.py` gate reports zero identical multi-word fragments.

## A shared-file defect, found and fixed during this run

`tools/check_latin_prose.py` was reporting `node-1word` on the 18 figures whose
TikZ overlay wraps a label-free image: the node's content is
`\includegraphics[...]{images/book1/ai/fig-*.png}` — an image path, not prose,
and byte-identical to English **by design**, because `id_apply`'s `img` census
requires exactly that. It produced 16 such hits here (grades 1–7) and failed
gate 9 for every Latin-script edition of this book, with nothing actually
wrong. It was reported rather than edited (the file is shared) and the
coordinator has since fixed both the `\includegraphics` stripping and the exit
code, which previously blocked on the advisory one-word tier as well. All nine
years now pass, and the gate reports zero findings on this tree.

## Why not 100

* The `óvulo` merger costs one link target and 8 links, and Spanish offers no
  school-register way to split it.
* `pata` vs. `pierna` leaves ~37 animal-leg mentions unlinked where English
  links them; the alternative over-linked by 86.
* `puesta en común` (pooled immunity) and `engullidores` (engulfers) are
  correct and consistent but are coinages of this edition rather than settled
  Spanish school terms — a Spanish curriculum author might have reached for
  `inmunidad de grupo` and `fagocitos`, which would have been more standard and
  less faithful to the book's deliberately plain register.
* One figure had to be trimmed to fit its frozen picture width: the plant-cell
  overlay's `pared celular` became `pared`, and its inner caption dropped two
  articles. Both are correct and the full wording survives in the figure's main
  caption, but they are terser than their English twins.
