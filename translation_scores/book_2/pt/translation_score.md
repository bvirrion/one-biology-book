# One Biology Book 2 — Portuguese (`pt`) edition — self-score

**Date:** 2026-09-05
**Volume:** Book 2, *Biologia do ensino médio* (grades 10–12), 36 chapters
+ 36 solutions files, **72 translated bodies**.
**Variety:** Brazilian Portuguese, one variety throughout — 38 `você`,
0 `tu`, 0 `vós`, 0 `está a …-r` against 33 gerund progressives, and **zero**
European-Portuguese tells in a targeted census (`facto`, `oxigénio`,
`fenómeno`, `género`, `húmido`, `cromossoma`, `actu-`, `electr-`, `registo`,
`projecto`, `ecrã`, `equipa`: 0 hits each; `oxigênio` 259, `cromossomo` 251,
`atu-` 125, `elétr-` 29, `íons` 9, `registro` 32). The frontmatter written by
the coordinator (`frontmatter/preface.pt.tex`,
`frontmatter/image-credits-book2.pt.tex`) is the same variety and was matched,
not re-decided.

## Quality bar

The bar is **native academic school prose**: a Brazilian teacher of *biologia*
in the *ensino médio* should read every page as something written in
Portuguese for Brazilian sixteen-to-eighteen-year-olds, not as English seen
through glass. English is the source of truth for content, labels, structure,
figures and numbers; native Brazilian register is the source of truth for how
it reads.

Register was calibrated against **this repository's own Book 1 `pt` twin**
(`parts/grade-9/pt/`) before drafting and again before scoring — same series,
same exercise machinery, one grade below. The two editions are
stem-for-stem indistinguishable: imperative-singular stems (*Nomeie*,
*Explique*, *Calcule*, *Dê*, *Enuncie*, *Liste*, *Compare*, *Preveja*),
`você` as the reader pronoun, `---` em dashes, ` ``…'' ` quotes, and the same
possessive habit — *dele/dela* at **6.6** per 1000 words here against **6.3**
in the Book 1 `pt` twin, the Brazilian pattern that avoids the ambiguity of
*seu/sua*.

Sense was checked against the French twin where the English was terse, but
never copied: `fr` and `pt` diverge in exercise-stem mood and in how much of
the English participle chain survives.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (academic school voice, one variety) | high | 96 |
| Terminology (consistency, Brazilian school usage) | high | 96 |
| MT-artifact freedom (idiom, word order, false friends) | high | 96 |
| Cross-references and links | medium | 95 |
| Solutions (answer voice, parity with stems) | medium | 97 |
| Structure (labels, environments, exercise/solution keying) | gated | 100 |
| LaTeX hygiene (build log, boxes, index, math) | gated | 100 |
| Figures (TikZ node text, captions, image paths) | gated | 98 |

## Machine evidence

- **Build:** `latexmk -g one_biology_book_2_high_school_pt.tex` —
  **392 pp** (English 379; +3.4 %, the normal Portuguese expansion).
  **0 errors**, **0 undefined references**, **0 Overfull boxes**,
  **0 `nullfont`**. The one box that survived my own sweep was in a
  coordinator-owned file (`frontmatter/image-credits-book2.pt.tex`, 62.3 pt);
  it was reported and has since been fixed for every language.
- **`.fls` file count:** **72** distinct `parts/grade-1{0,1,2}/…/pt/*.tex`
  read by the build, and **0** English chapter bodies — no silent fallback
  through `\ominput`.
- **`check_translation.sh grade-10|grade-11|grade-12 pt`:** **PASSED** for all
  three years (labels, environments, solution keys, `\emph`/`\index`
  adjacency, `\index` count, math spans, drawing code, image paths,
  delimiters, braces, residual `\omterm`, twin-comparison prose gate, orphan
  English lines). The only residual gate output is the advisory one-word tier:
  8 hits, all correct Portuguese — `aorta`, `splicing`, `retina`, `cone`,
  `glucagon` and three Latin binomials (`\emph{A. africanus}`,
  `\emph{H. heidelbergensis}` twice).
- **`\index{}` census:** **182** entries in Portuguese against **182** in
  English, per-file identical in all 72 files; the `.idx` files agree line for
  line. No English index key survives.
- **`\text{…}` census (chapters *and* solutions):** 4 in English, 4 in
  Portuguese, all translated — `carga`, `energia`, `luz, clorofila`, `músculo`.
- **`\qty{}`/`\unit{}` audit:** every argument in the edition is ASCII
  (`kJ`, `g/L`, `t/ha`, `\micro m`, `\celsius`, …). No accented character
  reaches a siunitx argument, which is the silent page-dropping failure.
- **Line-end hygiene:** 0 lines ending on an apostrophe, 0 ending on a
  word-final hyphen, 0 prose lines opening on punctuation (the five hits are
  TikZ Bézier `..` operators, byte-identical to English).
- **Term links:** **5 501** `\omterm` links on **103** distinct targets against
  English's **5 547** on **103** — **99.2 %** density parity, same target set
  but one either way (below). `tools/term_config/book2_pt.py` was curated from **this
  edition's own harvest**; `NOT_A_TERM` was left unset as instructed, `EXTRA`
  has exactly **two** entries and both were checked against the labels
  actually defined in `parts/grade-1{0,1,2}/`.

## Homograph collisions found and fixed

Both `\omterm` censuses were run — per-target **frequency** against the
English twin **and** per-target **chapter set** — and re-run after the last
edit, because each is blind where the other sees. Portuguese collides where
English does not, and vice versa: English's `carrier` collides with the
NAD/NADP carriers, but Portuguese says *transportador* for those, so *portador*
is honest; conversely *aumento* is at once *magnification* and the ordinary
word for *an increase*, and *cultura* is at once the animal culture, a
bacterial culture and a crop.

**211 wrong-sense links were removed, in five classes.** A sixth class,
*espécies*, was `DROP`ped on the first pass and **restored** on the second —
see *The `species` target* below.

1. **`olho` — 99 links against 12**, 50 of them in the vision chapter alone,
   plus *a olho nu* and *com um olho humano no lugar do ambiente*. English
   `STOP`s `eye`; `DROP`ped here, at the documented cost below.
2. **`resistente` — 85 links against 2.** English `STOP`s `resistant`. The
   Portuguese excess includes the eleven *eixo resistente* of the domestication
   chapter — a **tough wheat stalk**, not antibiotic resistance.
3. **`bases` / `base (DNA)` — 120 links against 54.** English `DROP`s both.
   The Portuguese excess includes *Bases de crânio* — the **base of a fossil
   skull** in the human-evolution chapter.
4. **`proteínas` — 8 chapters English never links.** The English harvest
   yields the capitalised `Proteins` and therefore routes the lowercase plural
   through the **ambiguous** `protein` key; the Portuguese harvest yields
   lowercase *proteínas*, which bypassed `AMBIG_POLICY` and sent immunology and
   respiration chapters to the grade-10 families definition instead of the
   grade-11 protein one. `DROP`ped so the singular key (plus the `(?:e?s)?`
   tail) carries the plurals under the nearest-preceding rule.
5. **`homólogos` — the meiosis sense.** *Cromossomos homólogos*, *pares de
   homólogos*, *sem homólogo*: ~25 chromosome sites against 6 organ ones.
   `DROP`ped, and `EXTRA` recovers the organ sense through the feminine forms
   (*estruturas homólogas*, *homóloga ao*), which are never chromosomes —
   the Portuguese equivalent of English's `EXTRA_PROTECT` on
   `homologous chromosomes`.

### The `species` target — a canon defect, not a Portuguese collision

On the first pass *espécies* carried **206** links against English's **37**,
in seven chapters English never touched, and was `DROP`ped for parity. The
coordinator then found the cause in the canon: `\emph{species}\index{species}`
sat in the Biodiversity definition's bullet list **and** a bare
`\emph{species}` was the Species definition's own display two paragraphs
later, so the English harvest lost the key to the defined-twice rule and
`def:g10:biodiversity-scales:species` was an orphan. Portuguese did not
collide, because *espécie* and *espécies* are different strings — which is why
the Portuguese excess was real and the English deficit was the bug.

With the marker moved onto the definition, English links *species* **272**
times in 15 chapters and this edition links *espécie* **271** times in the
**same 15 chapters**; the chapter-set census flags nothing at all. Portuguese
has no independent homograph here — every *espécie de* in the volume is
*species of* — so no `EXTRA_PROTECT` is needed for the term. The only two
sites that read *kind of* were mistranslations of mine, reworded rather than
protected (divergence 4 below).

Seven `EXTRA_PROTECT` patterns cover the collisions too small to justify
losing a key: *aumento do cérebro*, *fator médio de aumento*, *aumento de 225*
(three ordinary "increase" uses against fourteen honest magnifications),
*portadores de linhagens* and *a partir dos portadores* (people carrying
resistant bacteria, not carriers of a recessive allele), *dominante reduzem*
(the dominant ovarian follicle) and *o torna dominante*.

One coverage **gain**: `prop:g12:innate-immunity:drugs` shipped with **zero**
links because the Portuguese prose says *um anti-inflamatório* where English
says *an anti-inflammatory drug*; `EXTRA` now maps the short form, and the
target links like its twin.

## Residual deviations, all audited and all right-sense

Nine flags survive both censuses. Every one was read in context:

- **`def:g11:the-eye:parts` 0 against English's 12** — the only target the
  edition does not reach, and the price of class 2 above. Portuguese *olho*
  cannot be linked twelve times and not ninety-nine; the honest choice was to
  lose twelve rather than ship eighty-seven wrong-density links on the
  commonest noun of two chapters.
- **`genes-and-disease:genetic` 109 vs 46** — *portador/portadores* (75 of the
  109). English drops `carrier` because of its NAD carriers; Portuguese has no
  such collision, and every site is a carrier of an allele. Right sense, denser
  than the twin.
- **`becoming-male-female:hormones` 50 vs 6** — English harvests the
  capitalised `Testosterone` and so links only sentence-initial occurrences;
  *testosterona* is one word in every position. Right target every time.
- **`sport-and-health:training` 15 vs 7** — *treinamento* against English's
  alternation of *training* / *physical activity*.
- **`prop:g11:cancer:genes` 1 against English's 0** — the same capitalisation
  artifact in the other direction: English harvests `Proto-oncogenes` from a
  sentence-initial `\emph`, so its own caption's *Proto-oncogene proteins* does
  not link; the Portuguese key is lowercase and the caption links once, on the
  right target.
- Four single-link chapter-set flags (*resolução* in the eye chapter,
  *treinamento* in the doping chapter, *replicação do DNA* in the meiosis
  chapter, *tradução* in the antibiotic chapter): each is the right definition
  reached one chapter earlier than English reaches it.

## Deliberate divergences from the English canon

1. **`\qty{50}{nucleotides/s}`** (English `parts/grade-11/01-dna-replication.tex`,
   lines 290 and 399) is an English noun inside a siunitx unit argument. It
   cannot be translated in place: an accent inside `\qty{}` silently drops
   characters from the page and still exits 0. Both sites were rewritten as
   prose — *a 50 nucleotídeos por segundo* — which keeps the number, the unit
   and the reading, and keeps the argument ASCII.
2. **A dozen figure labels and two table settings were adjusted** to clear Overfull
   boxes that Portuguese length created and English never had: *membrana
   plasmática* → *membrana* in the plant-cell drawing; *gene ancestral da
   opsina*, *opsina dos bastonetes (rodopsina)*, *grupo externo: lampreia*,
   *bacia curta em forma de tigela*, *células efetoras: combatem agora, depois
   morrem*, three skeleton labels and one antibiotic legend split onto extra
   lines; one tree scope shifted 6 mm and one character table given
   `\tabcolsep 4.5pt`. No number, no term and no arrow moved.
3. **`\foreach` label lists and `symbolic x coords`** are frozen byte-for-byte
   by `id_apply.py`'s drawing census, which cannot see that they are prose.
   Rather than take the file-wide `!draw` opt-out, thirteen such lists (the
   size ladders, species and population coordinates, the character bars of the
   phylogeny figure, the motor-cortex bar chart, the stretch bands) were
   translated **after** the patch, in place, with a checked exact-string
   applier.
4. **Two of my own sentences were reworded to remove a *kind of* reading of
   *espécie***, once the target existed: the section title *uma árvore, duas
   espécies de evidência* → *dois tipos de evidência* (English: *Two Kinds of
   Evidence*), and the meiosis definition's *o ciclo de toda espécie de
   reprodução sexuada* → *o ciclo de toda espécie que se reproduz
   sexuadamente* (English: *the cycle of every sexually reproducing species*).
   The second was a genuine sense error, not only a link hazard.
5. **`ótico` was normalised across the volume** (47 sites): the edition had
   drifted between *óptico* and *ótico*, both valid in Brazil, and the Book 1
   `pt` twin uses *ótico* throughout. One spelling now, in all four grades.

## Defects found in the ENGLISH canon (reported, not fixed)

- **`parts/grade-11/01-dna-replication.tex:290` and `:399`** —
  `\qty{50}{nucleotides/s}` puts an English noun inside a siunitx unit
  argument. It renders in math italic in English (*nucleotides* set as a
  product of variables), and it is untranslatable in every accented language
  without a silent failure. It should be prose, or `\unit{nucleotides/s}`
  should become a `\text`-wrapped compound.

## Defect found in a coordinator-owned file (reported, since fixed)

- **`frontmatter/image-credits-book2.pt.tex` lines 36–39** — Overfull hbox
  **62.3 pt**. Two adjacent `\texttt{images/book2/CREDITS.md}` /
  `\texttt{images/book1/CREDITS.md}` paths gave TeX no break point in a
  Portuguese sentence longer than its English original. It was the single
  Overfull box in the edition and would have hit every language's 0-box
  target; the coordinator has fixed it for all of them, and this build is now
  **0 Overfull**.

## Canon changes absorbed after the first pass

Three edits landed in the English canon after this edition was first
measured, and every number above is from the rebuild that followed them:

- **`def:g10:biodiversity-scales:species` un-orphaned** — the change that
  restored 271 links here (above).
- **`tools/termlink/protect.py` now masks siunitx arguments.** The root cause
  of my `\qty{50}{nucleotides/s}` finding was the linker itself, which was
  wrapping `\omterm` inside a unit argument; the prose rewrite of divergence 1
  stands, because the English noun in the unit was a defect independently of
  the linker.
- **`parts/grade-12/07-domesticated-plants.tex:61` "wild mustard" →
  "wild cabbage"** — all six crops in that figure are *Brassica oleracea*.
  The Portuguese node is now **couve silvestre**, which is the right name and
  sits correctly with the six *couve*-family crop names it feeds; the
  *mostarda* of exercise 12 and its solution is a different plant (the wild
  mustard a herbicide-tolerant rapeseed crosses with) and is unchanged.

## Gate bugs hit

None. `id_apply.py` rejected a patch range on some fifteen occasions during
the run and was right every time — off-by-one ends that would have swallowed an `\end{…}`, a
math span whose internal newline had moved, a `matrix of nodes` body that the
drawing census (correctly) treats as drawing code. The only friction is the
one recorded above as divergence 3: `\foreach` lists are prose the drawing
census must keep frozen, so the translation has to happen outside the patch.

## Sampled fragments

1. **Grade 10, chapter 1, opening** — *"Deixe uma fatia de pão tempo demais na
   grelha e ela fica preta: o que sobra é quase só carbono. Pese uma fatia de
   maçã fresca, seque-a por um dia num forno morno, pese-a de novo…"* —
   **native.** The imperative chain with enclitic pronouns (*seque-a*,
   *pese-a*) is exactly how a Brazilian textbook addresses the student; the
   MT reflex would have been *seque ela*.
2. **Grade 12, chapter 6, opening** — *"Um carvalho não consegue caminhar até
   a água, fugir de uma lagarta nem sair à procura de um parceiro. Ele fica
   onde a bolota dele caiu por três séculos…"* — **native.** *Não … nem* for
   the English triple negation, and *sair à procura de* where a literal
   *ir procurar* would have been flatter.
3. **Grade 12, chapter 13, opening** — *"Um médico bate com um martelinho de
   borracha no tendão logo abaixo da sua rótula, e o seu pé chuta para a
   frente antes que você tenha sentido qualquer coisa."* — **native**, and the
   subjunctive after *antes que* is the tell that this was written, not
   converted.
4. **Grade 12, solutions, exercise 15 of the selection chapter** — *"A seleção
   faz os portadores de alguns alelos se reproduzirem mais aqui e agora:
   melhores em deixar descendentes neste ambiente… A evolução não tem direção
   de melhora, apenas separação local."* — **native.** The personal infinitive
   (*se reproduzirem*) is a construction no machine reaches for and no other
   Romance language offers.
5. **Grade 11, chapter 7, opening** — *"…uma célula que, alguns anos antes,
   adquiriu uma mutação que a deixou se dividir quando não deveria — e depois,
   ao longo dos anos, mais algumas."* — **near-native.** Accurate and
   idiomatic; *a deixou se dividir* is spoken-Brazilian where a textbook might
   have written *que a levou a se dividir*.

No fragment in the five sampled — and none in the twin-comparison gate over
all 72 files — reads as machine translation.

## Why not 100

- **One target is unreachable.** *Olho* cannot be linked at English's density
  without linking it at nine times English's density; the edition loses twelve
  canon links rather than ship eighty-seven noisy ones. There is no lever
  between "every occurrence" and "none".
- **Two targets are denser than the twin** (*portador* 75 links, *testosterona*
  50) because Portuguese has one word where English has two, or one case where
  English has two. Right sense every time, but the density profile is not the
  English one.
- **Thirteen `\foreach` and `symbolic coords` label lists live outside the
  patch discipline.** They are correct and were re-checked by eye and by the
  leftover-line census, but they are the one part of the edition whose
  structural equivalence to English rests on a second pass rather than on
  `id_apply.py`.
- **A handful of high-register passages are a shade more nominal than a
  Brazilian *ensino médio* text would naturally be** — *a passagem de bastão*
  for the hand-over to adaptive immunity, *a alça* for the regulation loop:
  both carry the metaphor, both are consistent across every chapter that uses
  them, but neither is a phrase a Brazilian author would have coined unprompted.

None of these is a defect a reader would call an error; all four are the
distance between *excellent* and *indistinguishable from originally written*.
