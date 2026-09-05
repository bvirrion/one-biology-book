# One Biology Book 1 — Portuguese (`pt`) edition — self-score

**Date:** 2026-09-04
**Volume:** Book 1, *Biologia do ensino fundamental* (grades 1–9), 71 chapters
+ 71 solutions files, 142 translated bodies.
**Variety:** Brazilian Portuguese, one variety throughout (0 `tu`, 0 `vós`,
0 European-Portuguese lexical tells; 132 `você`, progressive built with the
gerund only — 60 `está …-ndo`, 0 `está a …-r`).

## Quality bar

The bar is **native school prose**: a Brazilian teacher of *ciências* /
*biologia* should read every page as something written in Portuguese for
Portuguese-speaking children of that age, not as English seen through glass.
English is the source of truth for content, labels, structure and figures;
native Portuguese school register is the source of truth for how it reads.

The register was calibrated against the physics Book 1 `pt` edition
(`../one-physics-book/parts/grade-*/pt/`) — same ages, same series, same
exercise machinery — before drafting and again before scoring: imperative
singular exercise stems (*Diga* 57, *Faça* 42, *Explique* 26, *Dê* 26,
*Enuncie* 22, *Liste* 16, …), `você` as the reader pronoun, `---` em dashes,
` ``…'' ` quotes. The two editions are stem-for-stem indistinguishable in
register.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (school voice, age-graded, one variety) | high | 96 |
| Terminology (consistency, Brazilian school usage) | high | 96 |
| MT-artifact freedom (idiom, word order, false friends) | high | 96 |
| Cross-references and links | medium | 95 |
| Solutions (answer voice, parity with stems) | medium | 97 |
| Structure (labels, environments, exercise/solution keying) | gated | 100 |
| LaTeX hygiene (build log, boxes, index, math) | gated | 100 |
| Figures (TikZ node text, captions, image paths) | gated | 99 |

## Machine evidence

- **Build:** `latexmk -g one_biology_book_1_primary_middle_school_pt.tex` —
  453 pp (English 422; +7.3 %, the normal Portuguese expansion).
  `0` errors, `0` undefined references, `0` Overfull boxes,
  `nullfont` **20** (the English number, the shared style file's systemic
  artifact), `0` `invalid in math mode`.
- **`.fls` file count:** **142** — every translated body actually read by the
  build; no silent English fallback.
- **`check_translation.sh` grades 1–9:** PASSED for all nine years
  (labels, environments, solution keys, `\emph`/`\index` adjacency, `\index`
  count, math spans, drawing code, image paths, delimiters, braces, residual
  `\omterm`, twin-comparison prose gate, orphan English lines).
- **`\index{}` census:** 331 entries in Portuguese against 331 in English, and
  the per-file counts are identical in all 142 files — 0 English index keys
  survive.
- **`\text{...}` census (chapters *and* solutions):** 4 in English, 4 in
  Portuguese, all translated (`grass/grasshopper/lizard/buzzard` →
  `capim/gafanhoto/lagarto/gavião`).
- **Line-end hygiene:** 0 lines ending on an apostrophe, 0 lines ending on a
  word-final hyphen, 0 prose lines opening on punctuation (the only hits are
  TikZ Bézier `..` operators, byte-identical to English).
- **Term links:** **7 531** `\omterm` links on **153** distinct targets,
  against English's **7 609** on **152** — 99.0 % density parity.
  `tools/term_config/book1_pt.py` was curated from this edition's own harvest
  (`EXTRA` started empty and gained exactly one entry, verified against this
  book's own labels) and then diffed target-by-target against the English
  twin.

## Homograph collisions found and fixed

Both `\omterm` censuses were run — per-target **frequency** against English
**and** per-target **chapter-set** — because each is blind where the other
sees. Four collision classes were found and fixed; **300 wrong-sense links
removed in total**:

1. **`pelo` / `pelos` — 298 links.** The largest single defect of this
   edition, and invisible to every gate. `pelo` is both *fur* and the
   contraction `por` + `o`: `def:g1:animals-around-us:covering` carried
   **388** links against English's 141, spread over eleven chapters English
   never touches (*carregado **pelos** insetos*, *o sangue **pelos** vasos*).
   The frequency census raised the alarm, the chapter-set census proved it.
   Both forms are now in `DROP`; Portuguese simply cannot link *fur*, which
   is why that target now sits at 82 against 141 — an honest, documented loss
   rather than 298 lies.
2. **`óvulos` — 2 links.** The plural is the flower's *ovules*
   (`prop:g5:flower-to-fruit:roles`) **and** the animal egg cell. Two
   animal-context uses (grade-9 chromosomes, grade-8 sexual reproduction) were
   pointing at the botany definition; both were reworded so the sense — and
   the link — is right. Found only by the chapter-set census: the frequency
   was within tolerance.
3. **`anuais` — 2 links.** *Annual plants* versus the ordinary adjective:
   *as vacinas **anuais** de gripe* and *as renovações **anuais*** were
   pointing at `prop:g6:life-through-seasons:herbs`. Reworded, so the botanical
   links survive.
4. **Register collisions retired before they became links** — `pelo`,
   `sentido` (*meaning*), `elo`, `terra`, `escama`, `movimento`, `equilíbrio`,
   `batida`, `controle`, `natureza`, `árvore`, `classificar`, `adulto`,
   `lavouras`: each STOPped or DROPped exactly where `book1_en.py` suppresses
   its English counterpart, never by guesswork.

Two link gaps were also found and closed, both caused by Portuguese
morphology the shared `lang_pt.py` tail `(?:e?s)?` cannot produce:
a hand-measured `DERIVED` table for the irregular plurals
(`animal→animais` alone recovered **119** links lost to `-al → -ais`, plus
`raiz→raízes`, `coração→corações`, `fóssil→fósseis`, `embrião→embriões`,
`-ão → -ões` on four abstract nouns), and one `EXTRA` (`vasos →
def:g4:heart-and-blood:vessels`) mirroring English's bare *vessels*.

## Residual frequency deviations, all audited and all right-sense

Nine targets deviate by more than 30 links or 2×. Each was read in context;
none is a wrong sense.

- `covering` −59: *fur* is unlinkable in Portuguese (above).
- `conditions` +59: Portuguese says *as condições*, *a regra das condições*
  where English writes `conditions-rule` (hyphenated, and English's own
  pattern refuses it).
- `food-webs:roles` −53 and `plants-around-us:plant` −47: English *plant cell*,
  *producer plants* are adjectives; Portuguese uses *célula vegetal*,
  *plantas produtoras* — different words, no link.
- `animal-reproduction:sexual` −48 / `reproductive-systems:male` +32: one
  Portuguese word *espermatozoide* against English's *sperm* / *sperm cell*;
  nearest-preceding sends the later grades to the grade-8 definition, which is
  where they belong. Net ≈ −16.
- `breathing:organs` −41: English *lung* pluralises for free; Portuguese
  *pulmão → pulmões* does not, and *pulmões* is the grade-7 index key. Checked
  per grade: **0 forward links** — the grades 4–6 uses are simply unlinked,
  never mislinked.
- `plants-around-us:tree` −36, `human-reproduction:plan` +28: vocabulary
  spread, right sense in every sampled instance.

## Sampled fragments

1. **Grade 1, chapter 1, opening** — *"Um caracol desliza devagar pelo caminho
   molhado. Do lado dele está uma pedrinha cinza, do mesmo tamanho e igualmente
   redonda. […] Como é que a gente sabe?"* — **native.** The diminutives
   (*pedrinha*), the impersonal *a gente*, the rhythm are all how a Brazilian
   textbook opens for six-year-olds; nothing survives of the English clause
   order.
2. **Grade 7, chapter 5, opening** — *"Neste ano abrimos as portas da oficina:
   o que exatamente os sucos fazem […] e como a parede do intestino delgado dá
   conta da maior travessia de fronteira do corpo?"* — **native.** *Dá conta
   de* is idiomatic where a literal *lida com* would have been the MT reflex.
3. **Grade 9, chapter 6, the selection proposition** — *"Essa deriva da
   constituição herdada de uma população, impulsionada por nada além da
   variedade encontrando os freios, é a seleção natural."* — **near-native.**
   Accurate and readable; *impulsionada por nada além de* is a shade more
   formal than the surrounding grade-9 prose.
4. **Grade 6, exercise stem** — *"Como uma planta anual passa o inverno? E uma
   perene como o narciso?"* — **native**, and stem-for-stem the register of
   the physics Book 1 `pt` twin.
5. **Grade 9, solutions, weekend problem** — *"Os surtos são mais baratos de
   parar na transmissão --- o sabonete, o ar, a distância e uma caixa térmica
   fechada ganham de qualquer remédio que espera a multiplicação."* —
   **native.** *Ganham de* is the spoken-Brazilian comparative a translator
   reaching for *superam* would have missed.

No fragment in the five sampled — and none found in the twin-comparison gate
over all 142 files — reads as machine translation.

## Why not 100

- **Three link classes cannot be reproduced in Portuguese at all.** *Fur*
  (`pelo`), *plant* as an adjective (*célula vegetal*) and *lungs* in grades
  4–6 (*pulmões* against an index key of *pulmão*) lose ~150 links between
  them. The Portuguese reader loses nothing in meaning, but the edition is 1 %
  below the English link density and there is no honest way to close it.
- **`conditions` is over-linked by 59** relative to English, because
  Portuguese has one noun where English alternates between *conditions* and a
  hyphenated compound the English pattern itself refuses. Right sense every
  time, but denser than the twin.
- **Two chapter-level idioms remain a compromise.** *Engulfers* became
  *devoradoras* and *deck* became *baralho*: both carry the metaphor and both
  are consistent across every chapter that uses them, but neither is a term a
  Brazilian textbook would have coined unprompted.
- **A handful of grade-9 abstractions** (*o carregar sem mostrar*, *a
  contabilidade do motor*) are faithful and clear but slightly more nominal
  than a Brazilian ninth-grade text would naturally be.

None of these is a defect a reader would call an error; all four are the
distance between *excellent* and *indistinguishable from originally written*.
