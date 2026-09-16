# One Biology Book 4 — Portuguese (`pt`) edition — self-score

**Date:** 2026-09-16
**Volume:** Book 4, *Biologia universitária — 2.º ano*, 27 chapters
+ 27 solutions files, **54 translated bodies**.
**Variety:** Brazilian Portuguese, one variety throughout. Targeted census
over the 54 bodies: `oxigênio` 132 / `oxigénio` **0**; `cromossomo` 91 /
`cromossoma` **0**; `elétr-` 39 / `electr-` **0**; `úmido` 6 / `húmido`
**0**; `registro` 18 / `registo` **0**; `projeto` 2 / `projecto` **0**;
`atual` 8 / `actual` **0**; `fenômeno`/`fenómeno` **0** each; `ecrã`,
`comboio`, `autocarro` **0**. No European progressive: 0 `está a …-r`
(the 5 hits of `está a` are all "is at *a value*", e.g. *o cálcio está a
\qty{10}{nM}*). Reader address is the university-register impersonal —
4 `você`, 0 `tu`, 0 `vós` — the same level as the Book 3 `pt` twin (6).
`\bookline` and the coordinator-owned entry file were left exactly as
delivered.

## Quality bar

The bar is **native academic prose**: a Brazilian professor of *biologia*
in the second year of a *bacharelado* should read every page as something
written in Portuguese for Brazilian students, not as English seen through
glass. English is the source of truth for content, labels, structure,
figures and numbers; native Brazilian academic register is the source of
truth for how it reads.

**Sense and register reference:** this repository's own **Book 3 `pt`
edition** (`parts/bachelor-1/pt/`) — same series, same exercise machinery,
one year below — read before drafting and again before scoring. Everything
that carries across was taken from it: bare imperative stems in exercises
(*Calcule* 278, *Explique* 102, *Dê* 41, *Preveja* 39, *Compare* 34,
*Enuncie* 32, *Discuta* 23, *Recalcule* 19, *Defina* 16, *Liste* 14 —
662 stems in all, every one of them attested in the Book 3 `pt` twin),
`\begin{proof}[Evidências]` for the classic experiments (64 of them),
*Demonstração* for the rest, `---` em dashes, ` ``…'' ` quotes, decimal
points kept as in the English twin (as Book 3 `pt` does), *volume do Ano 1
/ Ano 3* for the cross-volume pointers, and *Problema de fim de semana ---
…* / *Parte I --- …* for the weekend problems. Terminology follows
Brazilian university usage: *aptidão* (fitness), *deriva genética*,
*efeito fundador*, *endogamia*, *herdabilidade*, *equação do melhorista*,
*pool gênico*, *relógio molecular*, *parcimônia*, *agrupamento de vizinhos*,
*serapilheira*, *húmus*, *plantio direto*, *intemperismo*, *leghemoglobina*,
*graus-dia*, *branqueamento dos corais*, *dívida de extinção*,
*débito cardíaco*, *quinase*, *axônio*, *hemácia*, *samambaia*,
*anterozoide*, *oosfera*.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (academic voice, one variety) | high | 96 |
| Terminology (consistency, Brazilian university usage) | high | 96 |
| MT-artifact freedom (idiom, word order, false friends) | high | 96 |
| Cross-references and defined-term links | medium | 96 |
| Solutions (answer voice, parity with stems) | medium | 97 |
| Structure (labels, environments, exercise/solution keying) | gated | 100 |
| LaTeX hygiene (build log, boxes, index, math) | gated | 100 |
| Figures (TikZ node text, captions, image paths) | gated | 97 |

## Machine evidence

- **Build:** `latexmk -g one_biology_book_4_university_year_2_pt.tex` —
  **338 pp** (English 321; +5 %, the normal Portuguese expansion).
  **0 errors**, **0 undefined references**, **0 Overfull boxes**,
  **0 `nullfont`** (the English twin is 0 too), **0 "invalid in math mode"**.
- **`.fls` file count:** **54** distinct
  `parts/bachelor-2/{,solutions/}pt/*.tex` — every chapter and every
  solutions file is really being read; nothing falls back to English.
- **Gates:** `bash tools/check_translation.sh bachelor-2 pt` — gates
  **1–8, 10 and 11 PASS** (labels, `\cref` targets, solution keys,
  environment counts, `\index` count, duplicate labels, line-broken
  `\index` keys, TeX accent escapes, orphan English lines **0**, weekend
  problem answer numbering OK over 27 problems). **Gate 9 fails on six
  false positives only** — see "Tooling" below; every genuine residue it
  found was fixed, and a patched copy of the gate (three-line fix, diff in
  the report) passes with the text unchanged.
- **Structural parity with the English twin:** 324 `exercise`,
  351 `solution`, 181 `omfigure`, 61 `definition`, 59 `theorem`,
  101 `proposition`, 6 `method`, 41 `example`, 27 `problem` — identical
  counts, file by file; `\index` **621 = 621**; `\qty` **2487 = 2487**;
  the `\index` key sets differ everywhere except 23 international keys
  (*plasma*, *placenta*, *clone*, *glia*, *bootstrap*, *UPGMA*,
  *anammox*, *centimorgan*, *protonema*, gene names…).
- **Term links:** 3,240 `\omterm` over **157 distinct targets**, against
  English's 3,092 over 155 — every English target reached except two that
  English links once each (`prop:b2:living-soil:humus`,
  `thm:b2:living-soil:decay`, where the Portuguese sentence says the thing
  without the noun phrase), plus four targets English never links
  (`prop:b2:living-soil:erosion`, `prop:b2:plant-meristems:sam`,
  `prop:b2:unicellular-diversity:gram`, `thm:b2:blood-pressure:fick`), each
  checked and correct. `--apply` twice changes nothing; `--check` reports
  every file matching what the config generates.
- **Homograph censuses (both, against the English twin):** clean except two
  read-and-cleared flags — `def:b2:plant-life-cycles:moss` 37 vs 14
  (Portuguese says *musgos*, *anterídios*, *arquegônios* where English
  varies its wording; every site is the moss concept) and one
  `unicelular` in ch. 7 (correct sense, a chapter English happens not to
  link). The censuses drove the whole of `tools/term_config/book4_pt.py`:
  `STOP` for *potência* (potency vs power) and *ovário* (flower vs mammal,
  as English STOPs "ovary"), 40 `EXTRA_PROTECT` masks (the animal-egg sense
  of *óvulo*, non-genetic *dominante*, *sangue quente*, floral and
  mathematical *indução*, *fluxo de massa*, *em flor*), and 18 `EXTRA`
  entries for the plurals `WORD_TAIL = (?:e?s)?` cannot build
  (*mutações* alone was 52 lost links, *células-tronco* 11).
- **`\text{…}` census (bodies *and* solutions):** no English left. The
  subscripts were localised where Portuguese has its own abbreviation —
  `\text{in}/\text{out}` → `\text{int}/\text{ext}` (membrane sides, the
  Book 3 `pt` convention), → `\text{ent}/\text{sai}` (box-model inflow and
  outflow), `\text{rest}` → `\text{repouso}`, `\text{low}/\text{high}` →
  `\text{baixo}/\text{alto}`, `\text{cum}` → `\text{acum}`; *art*, *ven*,
  *tot*, *red*, *ox*, *cal* are the same abbreviations in Portuguese.
- **Figure text:** every TikZ node, `\foreach` label list, axis label,
  `\legend`/`\addlegendentry`, `symbolic x coords` and `coordinates`
  string was read against the English twin (a fragment-by-fragment diff of
  all 54 files, not only the gate's view: it found four nodes the gate's
  allow-list hides, e.g. `$\mathrm{N_2}$ in air`, `cm to m`, `10\% at
  $K_d/10$`). Rendered pages were inspected for overlap and three labels
  were re-wrapped or shortened after seeing them on the page (the carbon
  cycle's `10 fósseis / + 1 uso da terra`, the sarcomere caption, the
  Keeling annotation).
- **Sweeps after the last file was written:** line-end elision apostrophe
  **0**, line-start punctuation **0** (two ratio colons re-wrapped),
  line-end hyphen **0**, line-broken `\index` **0**, `IU/L` **0**
  (→ `UI/L`), `yr` units **0** (→ `/ano`).

## Samples read against the English twin

1. **Ch. 26 opening (Darwin's worms).** EN: "Charles Darwin's last book,
   published the year before he died, was about earthworms. … ten tonnes of
   soil per acre per year passing through their bodies". PT: "O último livro
   de Charles Darwin, publicado um ano antes de sua morte, tratava das
   minhocas. … dez toneladas de solo por acre por ano passando por seus
   corpos". **Verdict: native.** The quotation inside it was re-rendered as
   Portuguese prose (*"toda a terra vegetal superficial … passou, e voltará
   a passar, a cada poucos anos, pelo corpo das minhocas"*), not
   transliterated.
2. **Ch. 22, Hardy–Weinberg theorem.** "Numa população grande com
   cruzamentos ao acaso, sem seleção, mutação ou migração, as frequências
   alélicas não mudam de uma geração para a seguinte" — the standard
   Brazilian statement of the law, *cruzamento ao acaso* rather than a
   calque of "random mating". **Verdict: native.**
3. **Ch. 24, Jukes–Cantor.** "À medida que $d$ cresce, $p$ satura em $3/4$
   --- duas sequências aleatórias coincidem em um quarto de seus sítios ---
   e, além de $p \approx 0.5$, a correção amplia todo erro de amostragem: um
   gene que mudou tanto deixou de marcar o tempo." *sítio* is the
   Brazilian term for a sequence position, *marcar o tempo* keeps the
   chapter's clock metaphor. **Verdict: native.**
4. **Solutions 21, answer 5 (the jump).** "…bem aquém dos \qty{1370}{N}
   necessários. Só o encurtamento muscular não consegue realizar esse salto.
   O contramovimento fornece o restante: quando quem salta se agacha, os
   tendões estirados armazenam energia elástica…". The answer voice is the
   twin's: verbless title, direct arithmetic, explanation after the number.
   **Verdict: native.**
5. **Ch. 27, exercise stem.** "Calcule o orçamento de carbono restante para
   \qty{1.5}{\celsius} e para \qty{2}{\celsius} … ; converta ambos em anos a
   \qty{10}{GtC/ano}." Bare imperative, *orçamento de carbono* as the
   climate literature in Portuguese writes it. **Verdict: native.**

## Why not 100

- Six gate-9 false positives remain on disk (they are gate bugs, not prose
  defects, and the rule is to report rather than reword), so the edition
  ships with one gate red.
- Three targets of the English link set are reached by a different route
  (two not at all, four extra): the Portuguese sentence sometimes carries
  the concept without the exact noun phrase the harvest keys on. That is
  style, but it is a 2-link divergence from the twin.
- Register in the weekend problems is very slightly more explicit than the
  English ("Calcule … e diga o que isso significa") because Portuguese
  imperatives need an object more often than English ones; a native author
  might have cut a few of those objects.
- The 18 canon defects listed in the report were carried through unchanged
  in 14 cases (the fix is a judgement call, not arithmetic); an edition
  that shipped with every one of them resolved would read better than this
  one.

## Deliberate divergences from the English span

Each is a correction of an arithmetic or naming defect in the English
canon, reported separately; the English files were not touched.

| File (pt) | Divergence |
|---|---|
| `solutions/pt/17-heart.tex` (Q19) | `+12.9` → `$+7.7$`, and the parenthetical rewritten as the exact sum `($4.9 + 7.7 + 3.6 + 5.4 = 21.6$)` |
| `solutions/pt/18-blood-pressure.tex` (Q14) | `0.630`/`1.59` → `0.727`/`1.38` |
| `pt/21-muscle-movement.tex` | `\qty{80}{g}` of ATP in the race → `\qty{800}{g}` |
| `pt/05-plant-life-cycles.tex` | "third autumn" → *segundo outono* (the chapter's own figure and caption say the second) |
| `pt/05-plant-life-cycles.tex` (problem Q11) | "A moss sperm swims" inside a fern question → *Um anterozoide nada … (como o de um musgo)* |
| `pt/25-biogeochemical-cycles.tex` | "Hutchinson Forest at Hubbard Brook" → *Floresta Experimental de Hubbard Brook* |
| `solutions/pt/25-biogeochemical-cycles.tex` (Q24) | `4 g/m^2` over the lake surface → `\qty{20}{g/m^2}` (4 is the per-volume figure) |

Non-canon divergences, all of them localisation rather than content:
`IU/L` → `UI/L`; the `\text{}` subscripts listed above; `/yr` units →
`/ano`; every `\foreach` label list, axis label and legend entry
translated (the drawing census does not blank those, so they were written
as post-edits after `id_apply`).

## How it was written

Every one of the 54 bodies was produced with `tools/id_apply.py` from
line-range patches over the English twin, so labels, `\cref` targets,
solution keys, math spans, drawing code, image paths, delimiters and braces
are byte-identical to English by construction; only prose was written.
Figure label lists and the handful of canon corrections above were applied
as post-edits, and the link pass, the censuses and the build were re-run
afterwards — the last action on the edition was to measure, not to edit.
