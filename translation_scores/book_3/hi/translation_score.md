# One Biology Book 3 — Hindi (`hi`) edition: self-score

**Date:** 2026-09-06 (re-synced the same day to three canon fixes; see the
last section)
**Scope:** `one_biology_book_3_university_year_1_hi.tex` — 29 chapters + 29
solutions files (University Biology, Year 1), 58 files.
**Quality bar:** *native academic prose*. Not "is this a correct rendering of
the English?" but "would a Hindi biologist writing a first-year university
book from scratch have written these sentences?" The register reference is the
physics Book 3 `hi` edition (`../one-physics-book/parts/bachelor-1/hi/`) —
same year, same series, same exercise machinery — and it was measured, not
assumed, before the first chapter was written: **आप** with **-इए**
imperatives (705 such forms in the physics twin), never **तुम**.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | 295 `-इए` imperatives, 0 `तुम`, 0 informal `-ओ`; `आप` only where the English addresses the reader; `\begin{proof}[साक्ष्य]` ×42 and `[आंशिक उपपत्ति]` ×5, matching English's 42 + 5 |
| Terminology | high | 95 | harmonised with the shipped Books 1–2 `hi` index-key pairs; eight self-inflicted drifts found by a doublet census and normalised (below) |
| MT-artifact freedom | high | 97 | written, not post-edited; 0 ASCII quotes, 0 space-before-danda, 0 TeX accent escapes, 0 Latin-word residue |
| Structure / LaTeX hygiene | gated | 100 | `id_apply` censuses green on all 58 files; log 0 errors / 0 undefined / 0 nullfont / 0 "invalid in math mode" / 0 "Missing character" |
| Cross-references | gated | 100 | label sequence byte-identical to English in all 58 files; 0 undefined references |
| Figures and captions | — | 96 | every TikZ node, axis label and legend translated; 6 `symbolic coords` axes and 3 `\foreach` label lists translated under a checked `!draw` opt-out |
| Solutions | — | 96 | all 29 solutions twins translated; gate 11 (problem numbering) OK on 29 chapters |
| Defined-term links | — | 95 | 5,404 links on 186 targets = 98 % of English's 5,495 on 179; two collision censuses run, 30 terms dropped, 6 protected, 3 cured in the prose |

## Measured state

```
files on disk              58   (29 chapters + 29 solutions)       = English
.fls parts/bachelor-1      60   (58 + part.tex + solutions.tex)    = English
LaTeX errors                0                                      = English
undefined references        0                                      = English
nullfont warnings           0                                      = English
"invalid in math mode"      0                                      = English
"Missing character"         0                                      = English
Overfull boxes              0   (5 found, all "in paragraph", all 5 cured
                                 by adding or removing a short word BEFORE
                                 the break point)                  = English
pages                     325                                 (English 339)
TeX accent escapes          0                                      = English
\index{} occurrences      568                                      = English
\qty{}                  2,977, every unit argument ASCII            = English
\includegraphics           85                                      = English
\addlegendentry / \legend  58, all translated                      = English
\text{} + \mathrm{}       706 (50 + 656; English 81 + 625)          = English
\omterm links           5,404  (English 5,495) — chapters 4,216 vs 4,185,
                                                solutions 1,188 vs 1,310
distinct link targets     186  (English 179)
\omterm inside tikzpicture  0
label sequence          identical to English, file by file
exercise <-> solution keys identical in all 29 pairs
check_translation.sh    PASSED (gates 1–11, including gate 7 check_hindi_prose
                        and gate 11 check_problem_numbering)
link_defined_terms --check  "every file matches what the config generates"
```

Every number above is the **final** state: the linker was re-run and both
`\omterm` censuses re-measured after the last prose edit, `--check` confirms
the tree and `tools/term_config/book3_hi.py` agree, and the last build was
started after the last edit. *The last thing done was to measure, not to edit.*

## The index sort-order question, answered

The French agent added 164 ASCII `@` sort keys because makeindex sorts
accent-initial entries after Z. **Devanagari does not need them, and I added
none.** The reason and the check:

* `makeindex` compares UTF-8 bytes. For the Devanagari block, byte order is
  code-point order, and the Unicode Devanagari block is laid out in the
  traditional varnamala order. So byte sorting *is* Hindi alphabetical
  sorting — the opposite of the Latin-1 accent problem, where `é` (0xC3 0xA9)
  sorts after `z`.
* Verified on the generated `build/one_biology_book_3_university_year_1_hi.ind`:
  469 entries, **0 out-of-order adjacent pairs** among the Devanagari ones, and
  the first-letter sequence reads
  `अ आ इ उ ऊ ऋ ए ऐ ऑ ओ क ख ग घ च ज झ ट ड त थ द ध न प फ ब भ म य र ल व श स ह`.
* The one trap that *could* have bitten: the precomposed nukta letters
  (क़ U+0958 … य़ U+095F, ड़ U+095C, ढ़ U+095D) sit at the END of the block and
  would sort after ह. I checked every one of the 543 index keys: **none begins
  with a precomposed nukta letter** — this edition stores nukta decomposed
  (फ़ = फ U+092B + ़ U+093C), so फ़ॉस्फ़ोलिपिड files under फ, where a reader
  looks for it. A future Hindi edition that pastes precomposed nukta from
  another source WOULD need `@` keys for those entries; this one does not.
* The five keys that already carry `@` sort keys (`3' end@`, `5' end@`,
  `alpha helix@`, `beta sheet@`, `beta-oxidation@`, `pKa@`) are inherited
  from the English canon and were kept: their display halves are translated,
  their ASCII sort halves are not.

## Censuses run, and what each found

**1. `id_apply` structural censuses (every file, every range).** labels, envs,
solutions, emph adjacency, index count, ordered math spans, drawing bodies,
image paths, delimiters, braces, `\omterm` absence, prose. 58 of 58 written
only after all twelve passed. The math-span census was by far the most
frequent objection (~35 rejects): Hindi postpositions reverse "A against B"
into "B के सापेक्ष A", and the census requires the ordered span sequence to be
byte-identical, so every such sentence had to be re-worded rather than
re-ordered. Newlines *inside* a math span (`$T_b =\n\qty{37}{\celsius}$`) had
to be reproduced exactly, indentation included.

**2. `\text{}` / `\mathrm{}` census, chapters and solutions.** 706 occurrences,
the same total as English. 31 `\text{cat}` / `\text{app}` subscripts were moved
to `\mathrm{}` — legal, because the math census blanks both — because gate 7
reads `\text{}` as visible prose and would otherwise have reported `cat` and
`app` as residual English. Nothing readable is left in math: the survivors are
`FADH_2`, `NAD^+`, `ATP`, `ADP`, `HCO_3^-`, `C_\alpha`, `NADPH`, `COOH`,
`mol/L`.

**3. Per-target link-frequency census (Hindi vs English).** Ran three times.
The first run showed 13 targets where Hindi linked far more than English;
every one was a Hindi word doing double duty. Largest: `water-small-molecules:ph`
EN 89 / HI 181 (अम्ल 97, almost all inside वसा अम्ल / ऐमीनो अम्ल);
`membranes-transport:transporters` EN 28 / HI 109 (पंप 60, वाहक 31);
`mammal-organization:compartments` EN 13 / HI 64 (प्लाज़्मा 48, of which ~30
are प्लाज़्मा झिल्ली, the plasma MEMBRANE);
`classifying-biodiversity:characters` EN 28 / HI 75 (लक्षण 49, symptoms
outside ch. 29). After curation the largest surviving ratio is
`cell-unit-of-life:prokeuk` (EN 54 / HI 113) and every one of those displays
was read: सुकेंद्रकी, सुकेंद्रकियों, कोशिकांग, केंद्रक — all correct sense,
Hindi simply writes the standalone noun where English writes an adjective.

**4. Per-target chapter-set census (Hindi vs English).** This is the one that
finds a homograph the frequency census misses. It found six single-occurrence
wrong-sense links no other gate could see:
`flowering-plant-organization:organs` reaching ch. 11 (तिपतिया पत्ती — the
cloverleaf of a tRNA, a shape, not an organ); `mammal-organization:organ`
reaching ch. 29 (अंग उपस्थित या अनुपस्थित — the cladogram's "limb present or
absent"); `lipids:triglyceride` reaching ch. 29 (ईथर-बद्ध वसाएँ, where the
word should have been लिपिड); `eukaryotic-cell:mitochondrion` reaching ch. 10
(आधात्री, the extracellular matrix); `membranes-transport:proteins` reaching
ch. 17 and 19 (अंतर्वेशी used for INTRON); `organism-environment:trophy`
reaching ch. 6, 11 and 17 (परपोषी used for the phage's HOST).

**5. Per-target display census.** Every display string per target, which is
how the प्लाज़्मा-झिल्ली and वसा-अम्ल cases were identified rather than
guessed.

**6. Index-key diff.** 568 `\index{}` in Hindi against 568 in English, key for
key. Three keys are deliberately pure Latin (`NADPH`, `Rhizobium`, `RuBisCO`).

**7. Doublet census over the whole corpus.** Eight terminology drifts of my
own making, found by scanning for known spelling pairs and normalised:
प्रकाशसंश्लेषण → प्रकाश-संश्लेषण (18 sites), थाइलैकॉइड → थाइलेकॉइड (4),
अर्धगुणसूत्र → क्रोमैटिड (6), जीवद्रव्य-तंतु → जीवद्रव्यतंतु (2),
रिक्तिका → रसधानी (4), and the nucleotide-base sense of क्षार → क्षारक
(11), leaving क्षार for the acid–base sense only.

**8. Register census against the physics Book 3 `hi` twin.** 705 `-इए` forms
there, 295 here (this book has fewer imperative exercises); 0 `तुम` in either.

## Defects found in the ENGLISH canon

**1. `solutions/27-species-interactions.tex`, answer 2 — a sign error and the
wrong conclusion.** The printed text said: *"solving $N_A = 200 - 1.6 N_B$
with $N_B = 130 - 0.9 N_A$ gives $N_B = -114$: the lines meet outside the
positive quadrant … A wins from any starting point."*
Substituting gives $N_B = 130 - 0.9(200 - 1.6N_B) = -50 + 1.44N_B$, so
$-0.44 N_B = -50$ and $N_B = +113.6$, $N_A = +18.2$ — **both positive**; the
slip was dividing $-50$ by $+0.44$. The conclusion was wrong in the opposite
direction too: with $\alpha = 1.6 > K_A/K_B = 1.538$ and
$\beta = 0.9 > K_B/K_A = 0.65$, each species limits the other more than
itself, so the crossing was an *unstable*, founder-controlled equilibrium —
which also contradicted question 2's own wording.

**Resolved in the canon, and this edition re-synced.** The coordinator's
diagnosis went one step further than my report: since the question and the
answer agree with each other that A wins unconditionally, and Part I is built
as a contrast (Q1–Q3 exclusion against Q4–Q6 coexistence), the *number* was
the error, not the question. $\alpha$ is now **1.4**, which puts A's
$N_B$-intercept at 143 > $K_B = 130$ and moves the crossing to $N_A = -69$,
outside the positive quadrant, so A does win unconditionally as both the
question and the answer say. I re-checked the new arithmetic before
translating it: $200/1.4 = 142.9$, $130/0.9 = 144.4$, and
$N_A = 200 - 1.4(130 - 0.9N_A)$ gives $-0.26 N_A = 18$, $N_A = -69.2$.
Re-synced here in `hi/27-…` (the problem statement's $\alpha$) and in
`solutions/hi/27-…` (answers 1 and 2). Answers 3–6 are unaffected and were
already correct.

**2. `solutions/21-gas-exchange.tex`, answer 16 — "five times the oxygen".**
Confirmed here from the problem's own data (300× by oxygen uptake, 21× by
mass; "five times" is reachable only per kilogram of body mass, which the
problem never gives). Fixed in the canon — now "a twentieth of the mass, for
three hundred times the oxygen ($15\,000$ against \qty{50}{mL} an hour)" —
and re-synced here.

**3. `19-gene-expression.tex` — two stale cross-references** (found by the
Arabic agent, both one too low): "the proteins of question 12" and "(each
yielding the number of question 11)". Re-synced here.

I looked for, and did **not** find, arithmetic errors in the other solutions I
checked line by line while translating: ch. 25 answers 16–18 (the permutation
the coordinator warned about) are correct in the canon I inherited, and
ch. 22 Q10/Q20, ch. 24 Q17/Q19, ch. 26 Q14/Q15, ch. 28 Q8/Q23, ch. 27 Q12
and ch. 19 Q22 all recompute to the printed values.

## Bugs found in the SHARED tooling, and what I did

All six are in `tools/check_hindi_prose.py`, which is the Hindi-only gate and
which I own; each is documented in the file at the point of change, each was
validated against the English canon (still fires, `english` class only), the
seven shipped `hi` grade trees (all still OK) and a negative-control file
(every rule still fires).

1. **A spacing control sequence welded two words together.** `\,` `\;` `\:`
   `\!` `\ ` `\/` and `\\` were deleted rather than turned into a space, so
   `\num{8800} kcal\,m$^{-2}$` in a tikz node became the single token
   `kcalm` and was reported as residual English — on a unit no translator may
   touch. Fixed: those escapes now emit a space; every other escape
   (`\%`, `\&`, `\_`, `\$`, `\#`) is still dropped. *This is the one that
   would bite any future Devanagari or Arabic edition with a unit in a node.*
2. **The siunitx family was missing from `TECHNICAL_MACROS`.** `\qtylist`,
   `\qtyrange`, `\numlist`, `\numrange`, `\SIrange`, `\SIlist`, `\unitlist`
   left their unit arguments in the visible-text stream, so `mmol` in
   `\qtylist{1;2;5;10;20}{mmol/L}` was reported as English.
3. **The makeindex sort key was being read as prose.** `\index{a@b}` was
   flattened by replacing `@` with a space, so the ASCII *sort* half was
   scanned. It now keeps only the display half — which is exactly what a
   reader sees, and what an edition with `@` keys needs.
4. **Outer punctuation was not stripped from a token**, so `cell''` (a LaTeX
   closing quote), `ACGT-` and `DNA--` were reported as unknown words.
5. **Element chains were not recognised**: `H--O--H`, `C--C`, `Ca--O`.
6. **Species, gene and quotation whitelist** extended for this book's Latin:
   `aurelia`, `caudatum`, `bursaria`, `japonica`, `robur`, `catus`, `lupus`,
   `paramecium`, `paris`, `quercus`, `felis`, `canis`, `dryas`, `mytilus`,
   `pisaster`, `rhizobium`, `trypanosoma`, `homo`, `sapiens`, the `lac`/`trp`
   operon symbols, `rubisco`, `cyt`, `alu`, `x-gal`, and Virchow's
   *omnis cellula e cellula* / Hooke's *Micrographia*.

Two further tooling facts, measured rather than assumed, that cost me time and
are worth writing down:

* **`!draw` is applied per FILE, not per range** (already known from wave 1).
  Confirmed again here: one `@@ N !draw` in a patch silently disables the
  drawing census for the whole file, so the other figures in that file are
  unchecked. I compensated by reading every figure body by hand in the six
  files that needed the opt-out.
* **`STOP` does not stop a homograph; only `DROP` does.** Taken from the
  coordinator's message and honoured: `STOP` is empty in
  `tools/term_config/book3_hi.py` and the 30 suppressed words are all in
  `DROP`. Each was diffed against English afterwards, as instructed.

## What is Hindi-specific in `tools/term_config/book3_hi.py`

Four of English's `DROP`s do **not** collide in Hindi and are therefore kept,
which is where this edition links where English cannot: **क्रियाधार**
(enzyme substrate in all 69 places — the succession's rock substrate is आधार
here), **अभिज्ञान** (molecular recognition in all 5), **स्तरण** (base stacking
in all 5), **प्रचालक** (the lac operator in all 18). **ध्रुवीय** likewise
keeps its links, because cell polarity is ध्रुवता and the verb is ध्रुवित.

Six collisions Hindi has and English does not were repaired with
`EXTRA_PROTECT` rather than by dropping a productive term: अंग (organ / limb),
वंश (genus / lineage), अधिचर्म (plant epidermis / skin's), चिकना (smooth ER /
smooth cartilage), ध्रुवित (polarised cell / to polarise a bond), स्पर्धा
(ecological competition / competitive inhibition).

Three more were repaired in the **prose**, because the word itself was the
wrong choice and no config entry would have made the sentence right:
परपोषी (heterotroph) was being used for the phage's HOST in ch. 6, 11 and 17
and is now पोषी; अंतर्वेशी / बहिर्वेशी (integral protein) were being used for
intron / exon in the ch. 17 and 19 solutions and are now इंट्रॉन / एक्सॉन;
and जड़ (root) was being used for "inert" in ch. 1, 10 and 17.

Because `lang_hi.py` sets `WORD_TAIL = ''` and `DERIVE = False`, nothing is
derived automatically. The `DERIVED` block (72 forms over 55 terms) was built
by scanning this book's own corpus for term+ending forms occurring at least
three times and reading each one; without it the edition linked 4,644 times
against English's 5,495.

## Deliberate divergences from the shipped Books 1–2 `hi` glossary

* `litter` is कर्कट here, not the glossary's अपरद, because this volume already
  spends अपरद on **detritus** in the food-web figure of ch. 26 and on
  अपरदभक्षी for the detritivores; two senses on one word inside one volume is
  exactly the collision the censuses exist to find.
* `species` is जाति, following Book 2, not Book 1's प्रजाति.
* `apoplast` / `symplast` are अपप्रवेश्य पथ / जीवद्रव्य पथ, as the Books 1–2
  glossary has them, even though they read as calques: a university reader
  meets both terms in their own definition and the pair is self-explaining.

## Where the remaining 4 points went

* **Register (−4 in that column).** The `-इए` polite imperative is right for
  the exercises, and the expository voice is impersonal, but a Hindi reviewer
  would probably tighten a dozen long relative clauses that follow English's
  clause order more closely than a Hindi writer would choose — the
  "जो … है, वह …" pattern appears more often than it needs to.
* **Terminology (−5).** Eight drifts were found and fixed; I do not claim
  there is no ninth. Some renderings are defensible rather than settled:
  निकेत for *niche*, ग्राही for *sink* (dropped from the linker for exactly
  this reason), सुसाधन for *facilitation*.
* **Links (−5).** 98 % of English's density, not 100 %: the deficit is
  concentrated in `flowering-plant-organization:organs` (−51), where English
  links "root"/"leaf"/"stem" in nine chapters in which the Hindi sentence
  uses a different word, and in the solutions generally (1,188 vs 1,310),
  where the Hindi prose is terser than the English.
* **Figures (−4).** Six axes keep ASCII `symbolic coords` with a Hindi
  `xticklabels` / `yticklabels` overlay rather than Devanagari coordinates,
  because pgfplots' `symbolic coords` cannot hold non-ASCII; the printed page
  is right, but the source is one indirection away from the English.

## Re-sync, 2026-09-06

Four files re-synced to the three canon fixes above: `hi/27-species-interactions.tex`,
`hi/19-gene-expression.tex`, `solutions/hi/27-species-interactions.tex`,
`solutions/hi/21-gas-exchange.tex`. Two of the four English edits LENGTHEN the
file, which is the case the Spanish agent showed can push a trailing patch
range past the file tail and leave English lines copied through, so gate 10
was run explicitly as well as through `check_translation.sh`:
**`orphan English lines: 0`**. Every other structural comparison was re-run
and is unchanged (labels identical file by file, solution keys identical in
all 29 pairs, 5,404 links on 186 targets, `--check` clean), and the numbers in
*Measured state* above are from the build made after this re-sync.
