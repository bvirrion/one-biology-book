# One Biology Book 3 — Portuguese (`pt`) edition — self-score

**Date:** 2026-09-06 (re-synced twice to the corrected English canon the same day)
**Volume:** Book 3, *Biologia universitária — 1.º ano*, 29 chapters
+ 29 solutions files, **58 translated bodies**.
**Variety:** Brazilian Portuguese, one variety throughout. Targeted census
over the 58 bodies: `oxigênio` 210 / `oxigénio` **0**; `cromossomo` 110 /
`cromossoma` **0**; `elétr-` 109 / `electr-` **0**; `úmido` 9 / `húmido`
**0**; `registro` 7 / `registo` **0**; `projeto` 17 / `projecto` **0**;
`atual` / `actual` **0**; `fenômeno`/`fenómeno` **0** each; `ecrã`,
`equipa`, `comboio` **0**. No European progressive: 0 `está a …-r` (the 19
hits of `está a` are all "is at *a value*", e.g. *o ATP está a
\qty{8}{mmol/L}*). Reader address is the university-register impersonal —
6 `você`, 0 `tu`, 0 `vós` — against Book 2's school-register 38, which is
the intended difference of level, not a drift of variety. `\bookline`
(`Livro 3: Biologia universitária — 1.\textsuperscript{o} ano`) and the two
coordinator-owned entry files were left exactly as delivered.

## Quality bar

The bar is **native academic prose**: a Brazilian professor of *biologia* in
the first year of a *bacharelado* should read every page as something
written in Portuguese for Brazilian first-year students, not as English seen
through glass. English is the source of truth for content, labels,
structure, figures and numbers; native Brazilian academic register is the
source of truth for how it reads.

Register was calibrated against **this repository's own Book 2 `pt` twin**
(`parts/grade-1{0,1,2}/pt/`) before drafting and again before scoring — same
series, same exercise machinery, one level below — and deliberately raised
from it: the school edition's `você` address gives way to the impersonal and
to the bare imperative-singular stem, which is what a Brazilian university
text does. The stems themselves are the twin's: *Calcule* (388),
*Explique* (108), *Compare* (35), *Preveja* (34), *Enuncie* (33),
*Discuta* (27), *Escreva* (16), *Liste* (16), *Defina* (15), *Dê* (15),
*Trace* (10), *Nomeie* (10) — every one of them attested in the Book 2 `pt`
edition. `---` em dashes and ` ``…'' ` quotes as in the twin.
*dele/dela* runs at **4.2** per 1000 words against **5.9** in the Book 2
`pt` twin: the same Brazilian habit of avoiding the ambiguity of *seu/sua*,
a little lighter because university prose repeats the head noun more.

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (academic voice, one variety) | high | 96 |
| Terminology (consistency, Brazilian university usage) | high | 96 |
| MT-artifact freedom (idiom, word order, false friends) | high | 96 |
| Cross-references and defined-term links | medium | 95 |
| Solutions (answer voice, parity with stems) | medium | 97 |
| Structure (labels, environments, exercise/solution keying) | gated | 100 |
| LaTeX hygiene (build log, boxes, index, math) | gated | 100 |
| Figures (TikZ node text, captions, image paths) | gated | 97 |

## Machine evidence

- **Build:** `latexmk -g one_biology_book_3_university_year_1_pt.tex` —
  **351 pp** (English 339; +3.5 %, the normal Portuguese expansion).
  **0 errors**, **0 undefined references**, **0 Overfull boxes**,
  **0 `nullfont`**, **0 "invalid in math mode"**.
- **`.fls` file count:** **58** distinct `parts/bachelor-1/{,solutions/}pt/*.tex`
  — every chapter and every solutions file is really being read; nothing is
  silently falling back to English.
- **Gates:** `bash tools/check_translation.sh bachelor-1 pt` — **PASSED**
  (gates 1–11, including gate 9's twin-comparison prose gate, gate 10's
  orphan-line gate — **0 orphan English lines**, checked explicitly after
  the canon edits that lengthened two solutions files — and the new gate 11,
  `check_problem_numbering.py`: OK over 58 chapters). Gate 9 reports 53 one-word advisory hits, all read: they
  are cognates and international nomenclature (*genital*, *submucosa*,
  *serosa*, *pili*, *ribose*, *helicase*, *repressor*, *basal*, *gene*,
  *Bacteria*/*Archaea*/*Eukarya*), math subscripts (`\text{cat}` ×25) and
  three proper-name titles (*Turgor*, *Henderson--Hasselbalch*,
  *Michaelis--Menten*). The five genuine residues gate 9 did find were
  fixed: an `ATP\\ synthase` TikZ node, `cyt $c$` / `cyt $b_6f$` →
  `cit`, and `\text{glucose}`, `\text{pyruvate}`, `\text{photons}`,
  `\text{sphere}`, `c_{\text{out}}`/`c_{\text{in}}`.
- **Structural parity with the English twin:** 348 `exercise` / 377
  `solution` / 185 `omfigure` — identical counts; **0** chapters and **0**
  solutions files with a differing environment count; `\index` entries
  **568 = 568**, chapter by chapter; 42 `\begin{proof}[Evidências]` and 5
  `[Demonstração parcial]` against English's 42 `[Evidence]` and 5
  `[Partial proof]`.
- **Defined-term links:** **5352** `\omterm` links over **181** distinct
  targets, measured against the corrected English canon (English: 5495 over
  179). **No target that English links is unlinked here.** `--check`
  reports every file matches what the config generates. A span-by-span
  comparison of every `pt` file against its English twin (`math_spans`
  after `unwrap_omterm`) reports **0 files** whose math differs, and the
  `\textbf{N.}` answer sequences match English file by file.
- **Two collision censuses** against the English twin (per-target frequency
  and per-target chapter set) after the final link pass. Frequency: only two
  targets differ by more than 10 upward — `water-small-molecules:water`
  (+15, the *polar* links English drops and Portuguese keeps honestly) and
  `classifying-biodiversity:nomenclature` (+14, *táxons*: English never
  links its own irregular plural *taxa*). The three downward outliers are
  morphological, not lost meaning: Portuguese says *foliar*, *celular*,
  *peptídico* where English repeats *leaf*, *cell*, *peptide*
  (`organs` −83, `cell` −66, `peptide` −11). Chapter set: 9 targets have a
  pt-only chapter, every one of them read and honest (a *folha* in the
  carbohydrate chapter, *osmose* in the digestion chapter, *micorriza* in
  the interactions chapter).
- **Hygiene sweeps:** line-ending elision (`['’]\s*$`, `^\s*[.,;:)?!]`,
  `[a-zà-ÿ]-\s*$`) — 0 real hits (the four apostrophe hits are closing
  ` '' ` quotes, as in English); `\text{}` census over both directories —
  every remaining string is an abbreviation Portuguese shares (`cat`,
  `int`, `ext`, `tot`, `eq`, `ap`, `const`) or already Portuguese
  (`água`, `ácido`, `íon`, `sangue`, `xilema`, `cél`, `inclinação`, `UR`).

## Terminology

Term configuration `tools/term_config/book3_pt.py` was curated from **this
edition's own harvest**, never seeded. It carries 23 `EXTRA`, 35 `DROP` and
7 `EXTRA_PROTECT` entries, each justified in the file, and every `EXTRA`
value is machine-checked against the labels actually defined in
`parts/bachelor-1/` — 0 dangling targets, prefixes included. The two Portuguese
facts that shaped it:

1. `WORD_TAIL = (?:e?s)?` cannot build the `-ão → -ões` and `-al → -ais`
   plurals, nor agree an adjective after a pluralised head. Left alone that
   cost **54** links on *pulmões*, 38 on *órgãos*, 19 on *populações*, 10 on
   *tampões*, and every *ligações covalentes / peptídicas / glicosídicas*.
2. The homographs are not the English ones. *água*, *energia*, *matéria*,
   *informação*, *ácido*, *velocidade*, *ambiente*, *fonte*, *dreno*,
   *plasma*, *matriz*, *caráter*, *esqueleto*, *vaso*, *bomba*,
   *carreador*, *relação*, *reprodução*, *nutrição* were dropped after
   counting them target by target against English; conversely *substrato*
   stays linked (eleven enzyme senses against two succession ones, masked
   individually) and *canal* stays linked where English needed an EXTRA.

Vocabulary was fixed once and held: one drift was found and repaired —
chapters 23–24 had written *turgescência* where chapters 6–10 had defined
*turgor* (24 sites, rewritten with the gender agreement fixed).

## What keeps this at 96 and not higher

- Portuguese needs a preposition where English compounds two nouns
  (*balanço de calor*, *tempo de manipulação*, *taxa de ataque*), so some
  sentences carry one more *de* than a Brazilian author writing freely
  would; they are correct and idiomatic, but a native drafting from scratch
  would occasionally reach for a different construction.
- A handful of figure labels were shortened or re-broken to fit the page,
  so three or four of them are terser than their English twins.
- The English-canon items listed below were mirrored faithfully rather than
  silently repaired; the two that the coordinator has since fixed at source
  have been re-synced here, and the rest are link-coverage gaps that leave
  nothing wrong on the printed page.

## Defects found in the English canon (reported; two now fixed at source)

1. **A missing answer and a shifted numbering — FIXED at source and
   re-synced here.** `parts/bachelor-1/solutions/16-biosyntheses-integration.tex`,
   weekend problem `pb:b1:biosyntheses-integration:1`: the answer to
   question 13 was absent and question 12's answer carried the label
   `\textbf{13.}` — 24 answers for 25 questions. Reported rather than
   edited during the run, because editing the English canon would have
   shifted line numbers under the six other language agents. The
   coordinator has since corrected it; the Portuguese twin now carries the
   relabelled 12 and a Brazilian-Portuguese 13, and both files show 25
   numbered answers.

2. **A three-cycle permutation of answers 16/17/18** in
   `parts/bachelor-1/solutions/25-populations.tex` (found by the Spanish
   agent, not by me — my own numbered-answer audit compared counts and
   labels, not the arithmetic behind each label; a permutation under
   identical labels is invisible to it). **FIXED at source and re-synced
   here**: 16 is the maximum sustainable yield, 17 the doubling time, 18
   the fixed-fraction harvest.

3. **Two `\num{…}{g}` written where `\qty{…}{g}` was meant**, in
   `17-genomes.tex` and `20-expression-control.tex`. Fixed at source; the
   Portuguese twins carried the same construct and are fixed too. A census
   of `\num{…}{unit}` over both Portuguese directories now returns zero.

4. **Three further canon defects found by wave 2 and re-synced here**,
   none of which my own review caught: two stale cross-references in
   `19-gene-expression.tex` (A14 divides by question 12's answer and A20 by
   question 11's, while the questions cited 11 and 10 — Arabic agent);
   "for five times the oxygen" in answer 16 of `solutions/21-gas-exchange.tex`,
   which is 21× by mass and 300× by oxygen (Indonesian agent); and a wrong
   datum in `27-species-interactions.tex`, where $\alpha = 1.6$ made the
   equilibrium founder-controlled and contradicted the question's own
   wording — now $\alpha = 1.4$, with answers 1 and 2 rewritten (Hindi
   agent). All four Portuguese twins are re-synced, and the math-span
   sequence of every file still matches its English twin exactly.

5. **Defined terms that carry zero links in the English edition** although
   the phrase occurs in its prose. Four of the five I reported were real
   and are now linked in English: `prop:b1:nucleic-acids:chargaff` (+4),
   `prop:b1:replication-mitosis:checkpoints` (+6),
   `prop:b1:body-plans-tissues:gutwall`, and
   `def:b1:classifying-biodiversity:nomenclature`, whose plural *taxa* is
   unreachable from the singular key. `def:b1:cell-unit-of-life:culture`
   was my error of inference: in English the phrase occurs only inside its
   own definition, so the target is legitimately unlinkable. (Portuguese
   repeats *cultura de células* once in the prose after the definition, so
   the pt edition links it honestly, and `gutwall` likewise.)
   **I also mis-typed two of the labels in my own report** —
   `def:b1:nucleic-acids:chargaff` and
   `def:b1:replication-mitosis:checkpoints` are `prop:`, not `def:`; entered
   verbatim they would have been dangling `EXTRA` values, silent and
   link-free. My own `book3_pt.py` never pointed at them, and all 23 EXTRA
   values re-audited clean against the label set, prefixes included.

6. **A `pt` defect in the already-shipped Book 2 edition** (out of my scope,
   not edited): 26 of the 61 `\begin{proof}[...]` optional titles under
   `parts/grade-1{0,1,2}/pt/` are still the English `[Evidence]`; 35 are
   `[Evidências]`. It renders as an English word on 26 printed pages of a
   shipped edition and no gate sees it, because the string is a legal
   optional argument. `fr` has a different version of the same problem
   (38 `[Faits expérimentaux]` against 23 `[Preuves]` — one notion rendered
   two ways); `nl`, `es` and `id` are uniform. This Book 3 `pt` edition is
   uniform: 42 `[Evidências]`, 5 `[Demonstração parcial]`.

## Findings in the shared tooling

0. **`STOP` does not stop a homograph; only `DROP` does** (measured by the
   Indonesian agent: a stopped term kept 38 links, because `harvest.py`
   feeds it into the per-chapter map anyway). Checked against my own
   config: `book3_pt.py` has `STOP = set()` and suppresses every homograph
   through `DROP` or `EXTRA_PROTECT`, so nothing here relied on the broken
   mechanism. Worth noting that `book3_en.py` *does* use `STOP` for
   *substrate*/*substrates* — which, if the measurement generalises, is not
   actually suppressing them.

1. **`lang_pt.py`'s `WORD_TAIL` cannot build a Portuguese plural in
   `-ões`/`-ais`, and the cost is large in a university volume.** Every
   `-ão` and `-al` head silently loses its plural: 54 links on *pulmões*,
   38 on *órgãos*, 19 on *populações*, 10 on *tampões*, 5 on *perturbações*,
   plus every phrase whose head pluralises and whose adjective must agree
   (*ligações covalentes*, *ligações peptídicas*, *níveis tróficos*,
   *potenciais hídricos*). Twelve `EXTRA` entries here are nothing but that.
   A morphology rule (`-ão → -ões`, `-al/-el/-ol → -ais/-éis/-óis`) in
   `lang_pt.py`, or a shared `DERIVED` table, would remove the hand work
   from every Portuguese book at once; the same gap will be in Books 4 and 5.

2. **An `EXTRA_PROTECT` pattern with a literal space silently fails on a
   hard-wrapped source.** `r"aumento(?= das presas)"` matched nothing
   because the source reads `aumento das\n        presas`; the mask
   reported no error and the wrong link simply stayed. Any multi-word
   `EXTRA_PROTECT` pattern must join its words with `\s+`. Worth a line in
   `protect.py`'s docstring next to the "never consume a `$`" warning.

3. **Three hyphenated Portuguese defined terms were absent from the
   harvest** although their English twins were harvested and although other
   hyphenated keys (*DNA-polimerase*, *espécime-tipo*, *sequência-sinal*,
   *célula-guarda*) were picked up normally: *ATP-sintase*,
   *nitrato-redutase*, *peptídeo-sinal*. Each left a defined target with
   **zero** links until an `EXTRA` restored it, and each is indexed and
   `\emph`-marked exactly as its English twin
   (`\index{quimiosmose}\index{ATP-sintase}` against
   `\index{chemiosmosis}\index{ATP synthase}`). I did not find the
   mechanism; the reproducer is small and worth one look before the Book 4
   and Book 5 Portuguese runs.
