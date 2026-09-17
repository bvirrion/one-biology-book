# One Biology Book 5 — Portuguese (`pt`) edition — self-score

**Date:** 2026-09-17
**Volume:** Book 5, *Biologia universitária — 3.º ano*, 27 chapters
+ 27 solutions files, **54 translated bodies**.
**Variety:** Brazilian Portuguese, one variety throughout. Targeted census
over the 54 bodies: `oxigênio` 64 / `oxigénio` **0**; `cromossomo` 66 /
`cromossoma` **0**; `elétr-` 11 / `electr-` **0**; `úmido` 2 / `húmido`
**0**; `registro` 6 / `registo` **0**; `projeto` 9 / `projecto` **0**;
`atual` 7 / `actual` **0**; `fenômeno`/`fenómeno` **0** each. No European
progressive: the 10 hits of `está a` are all "is at *a value*" or "lies"
(*a actina livre está a \qty{100}{\micro M}*, *entre 20 % e 35 % está a
zona crepuscular*), 0 `está a …-r`. Reader address is the direct
você-form imperative of `parts/bachelor-2/pt/` — 15 `você`, 0 `tu`,
0 `vós`. `\bookline` and the coordinator-owned entry file were left
exactly as delivered.

## Quality bar

The bar is **native academic prose**: a Brazilian professor of *biologia*
in the third year of a *bacharelado* should read every page as something
written in Portuguese for Brazilian students, not as English seen through
glass. English is the source of truth for content, labels, structure,
figures and numbers; native Brazilian academic register is the source of
truth for how it reads.

**Sense and register reference:** this repository's own **Book 4 `pt`
edition** (`parts/bachelor-2/pt/`) — same series, same exercise
machinery, one year below — read before drafting and again before
scoring, together with the 1,199-entry EN→PT glossary mined by positional
`\index{}` matching from the seven shipped Book 1–4 `pt` editions (129 of
this volume's index keys already had a settled translation there, and all
129 were reused). Everything that carries across was taken from it: bare
você-form imperative stems in exercises (*Explique* 26, *Defina* 11,
*Preveja* 10, *Enuncie* 10, *Liste* 9, *Nomeie* 9, *Calcule* 7,
*Mostre* 7, *Descreva* 6, *Distinga* 5, *Deduza* 5, *Dê* 3,
*Classifique* 3, *Contraste* 3, *Argumente* 2, *Ordene* 2 — every stem
attested in the Book 4 `pt` twin), `\begin{proof}[Evidência]` for the
classic experiments (**53 = 53** with the English twin), `---` em dashes,
` ``…'' ` quotes, **decimal points** kept as in the English twin (the
series sets siunitx `output-decimal-marker={.}`), *volume do Ano~1 /
Ano~2* for the cross-volume pointers, and *Problema de fim de semana ---
…* / *Parte I --- …* for the 27 weekend problems. Terminology follows
Brazilian university usage: *neutrófilo*, *macrófago*, *linfonodo*,
*plasmócito*, *imunidade coletiva*, *paratormônio*, *hipófise*,
*tronco encefálico*, *medula espinal*, *barreira hematoencefálica*,
*líquido cefalorraquidiano*, *célula-guarda*, *estômato*,
*eficiência do uso da água*, *aptidão inclusiva*, *deriva neutra*,
*células-tronco*, *limite de Hayflick*, *espécies--área*,
*vórtice de extinção*, *relógio molecular*, *seleção purificadora*,
*parálogo*/*ortólogo*, *fuga da sombra*, *dança do requebrado*.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (academic voice, one variety) | high | 96 |
| Terminology (consistency, Brazilian university usage) | high | 96 |
| MT-artifact freedom (idiom, word order, false friends) | high | 96 |
| Cross-references and defined-term links | medium | 96 |
| Solutions (answer voice, parity with stems) | medium | 96 |
| Structure (labels, environments, exercise/solution keying) | gated | 100 |
| LaTeX hygiene (build log, boxes, index, math) | gated | 100 |
| Figures (TikZ node text, captions, axis labels) | gated | 97 |

## Machine evidence

- **Build:** `latexmk -g one_biology_book_5_university_year_3_pt.tex` —
  **382 pp** (English 365; +4.7 %, the normal Portuguese expansion).
  **0 errors**, **0 undefined references**, **0 Overfull boxes**,
  **0 `nullfont`** (the English twin is 0 too), **0 "invalid in math
  mode"** (`grep -a`, the log carries non-UTF8 bytes).
- **`.fls` file count:** **54** distinct
  `parts/bachelor-3/{,solutions/}pt/*.tex` — every chapter and every
  solutions file is really being read; nothing falls back to English.
- **Gates:** `bash tools/check_translation.sh bachelor-3 pt` —
  **TRANSLATION GATE: PASSED**, gates **1–11** (labels, `\cref` targets,
  solution keys, environment counts, `\index` count, duplicate labels,
  line-broken `\index` keys, TeX accent escapes, the twin-comparison
  prose gate with **no multi-word findings**, orphan English lines **0**,
  weekend-problem answer numbering OK over 27 problems).
- **Structural parity with the English twin**, file by file:
  `exercise` **324 = 324**, `solution` **351 = 351**, `omfigure`
  **177 = 177**, `definition` **127 = 127**, `theorem` **34 = 34**,
  `proposition` **59 = 59**, `method` **26 = 26**, `example` **54 = 54**,
  `remark` **32 = 32**, `problem` **27 = 27**, `proof` **104 = 104**,
  `\index` **913 = 913**, `\qty` **2249 = 2249**. Every one of the 54
  files was written through `tools/id_apply.py`, so the `labels`, `envs`,
  `solutions`, `emph`, `index`, `math`, `draw`, `img`, `delims`,
  `braces`, `omterm` and `prose` censuses all passed per range.
- **Defined-term links:** `tools/link_defined_terms.py --book 5 --lang pt`
  inserts **2,794 links** over **193 targets** (English 2,670 / 188);
  the plain dry run over the wrapped tree reports **`links to insert: 0`**,
  so no `EXTRA_PROTECT` pattern has silently stopped protecting.
  `tools/term_config/book5_pt.py` was curated from this edition's own
  harvest: **18 STOP entries**, **6 EXTRA** plurals the `(?:e?s)?` tail
  cannot build, **9 EXTRA_PROTECT** spans, and a **translated
  `NOT_A_TERM`** (single words only — `lei de` deliberately absent, so
  Portuguese keeps the five named-law targets English keeps).
- **Homograph censuses** (both, against the English twin): per-target
  frequency and per-target chapter set. After curation the frequency
  census leaves three flags, all verified correct in context
  (`adaptive-immunity:lymphocytes`, because English writes `T~cell` with
  a tie that its own matcher skips and Portuguese writes *célula T*;
  `cytoskeleton-motility:cilia`, the airway cilia of ch. 15;
  `bioinformatics:evalue`, entirely inside its own chapter), and the
  chapter-set census leaves two (`virology:virus` and
  `adaptive-immunity:antibody`, both the same concept in the extra
  chapters).
- **Line-break hygiene** over both trees: 0 lines beginning with
  punctuation, 0 lines ending on a hyphen, 0 elision apostrophes at
  end of line (the single `'`-at-EOL hit is a math prime, `\gamma'`,
  byte-identical to the English twin).
- **Decimal separators:** a `\d[.,]\d` Counter diff against the English
  twin, file by file, outside TikZ — **identical in all 54 files**.
- **Residual English:** a 70-word function-word scan over both trees
  (prose only, math/TikZ/macro arguments stripped) returns **41 hits,
  all Portuguese**: the future-subjunctive *for*, the verb *some*, and
  *cross-β* / *Distal-less*.

## Samples

Marked against the bar: native / near-native / MT-flavoured.

1. **native** — ch. 24 opening: «Corte a perna de um axolote e em dois
   meses ele terá feito crescer uma nova, com osso, músculo, nervo e pele
   nos lugares certos, e voltará a fazê-lo tantas vezes quantas você
   cortar.» The *tantas vezes quantas* correlative and the future perfect
   are Portuguese moves, not English ones.
2. **native** — ch. 21: «Pouco demais (doença de Addison, a destruição do
   córtex da adrenal) dá fraqueza, pressão arterial baixa, glicose baixa
   e, sob estresse, colapso e morte se não houver reposição.» The
   *pouco demais / demais* pair carries English's *too little / too much*
   with no calque.
3. **native** — ch. 26: «O chapim não deriva $g(t)/(\tau + t)$, o
   suricato não calcula $r$, e a pavoa nunca ouviu falar de handicap.»
4. **near-native** — ch. 15: «a distinção entre o próprio e o não próprio
   não é feita pelo reconhecimento, mas pelo sinal de $a - d$.» *o próprio
   / o não próprio* for *self / non-self* is the standard Brazilian
   immunology rendering but still reads as terminology rather than prose;
   a native monograph would often keep *self* in italics.
5. **near-native** — ch. 25: «a esmagadora maioria é neutra». Correct and
   idiomatic, but *esmagadora* is the obvious first choice for
   *overwhelming*; a Brazilian author might write *a imensa maioria*.

## Why not 100

- Three chapters (14, 19, 25) carry a pgfplots axis whose
  `symbolic x/y coords` are kept in English on purpose — they are internal
  keys referenced by `\addplot coordinates {...}`, which `id_apply`'s
  `draw` census compares byte-for-byte — with the visible text supplied by
  a Portuguese `xticklabels=`/`yticklabels=` added as a post-write edit.
  The reader sees only Portuguese (verified in the PDF text layer), but
  the source is not monolingual, and the extra key makes gate 9 skip those
  three files entirely (see "Tooling" in the report).
- Link density is **+4.7 %** over English, concentrated in one target
  (*célula T* / *célula B*, where English's `T~cell` tie hides the term
  from its own matcher). Every extra link is correct, but the page is
  slightly busier than the English twin's.
- Two English link targets (`def:b3:rna-regulation:pirna`,
  `met:b3:microbiomes:16s`) receive links in English only through the
  ambiguity resolver's per-site choice between two definitions of
  *piRNA*; in Portuguese every *piRNA* resolves to the `ncrna`
  definition, so those two definitions are defined but never linked to.
  No undefined reference, no build consequence.
- Five figures needed their node text rebalanced over more lines
  (ch. 6, 13, 16, 18, 21, 23, 27) because Portuguese is longer than
  English; the wording is native, but the line breaks are the
  translator's, not the author's.

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
Re-measured after the change: **382 pages, 2797 links on 194
targets, `\index` 911, `.fls` 54, 0 errors / 0 undefined / 0 overfull /
`nullfont` 0 / 0 "invalid in math mode", `check_translation.sh bachelor-3 pt`
gates 1-11 PASSED.** The self-score above is unchanged.
