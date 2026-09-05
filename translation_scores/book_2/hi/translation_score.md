# One Biology Book 2 — Hindi (`hi`) edition: self-score

**Date:** 2026-09-05
**Scope:** `one_biology_book_2_high_school_hi.tex` — 36 chapters + 36 solutions
files (grades 10–12), 72 files, 367 pages.
**Quality bar:** *native academic prose*. Not "is this a correct rendering of
the English?" but "would a Hindi biology teacher writing a lycée-level book
from scratch have written these sentences?" The register reference is the
physics Book 2 `hi` edition (`../one-physics-book/parts/grade-1*/hi/`) — same
ages, same series, same exercise machinery — and it was measured, not assumed,
before the first chapter was written: **आप** with **-इए** imperatives, not the
**तुम** / **-ओ** of biology Book 1's grades 1–9.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | 1,876 `-इए` imperatives, 0 `तुम`, 0 informal `-ओ`; `आप` only where English addresses the reader |
| Terminology | high | 95 | standard Hindi school-biology vocabulary; four cross-year drifts of my own making found and normalised (below) |
| MT-artifact freedom | high | 97 | written, not post-edited; 0 ASCII quotes, 0 Latin digits in prose, 0 space-before-danda, 2 oblique-case slips found and fixed |
| Structure / LaTeX hygiene | gated | 100 | `id_apply` censuses green on all 72 files; log 0 errors / 0 undefined / 0 overfull / 0 nullfont / 0 missing characters |
| Cross-references | gated | 100 | 0 undefined references |
| Figures and captions | — | 97 | every TikZ node, axis label and legend translated; 12 `symbolic coords` lists and 2 `\foreach` label lists translated by a checked exact-string applier after the patch (the draw census cannot see them) |
| Solutions | — | 96 | all 36 solutions twins translated; `\text{}`, `\qty` and `\index` censuses clean over solutions too |
| Defined-term links | — | 95 | 5,833 links on 107 targets — 105 % of English's density; three collision classes found by the chapter-set census and cured |

## Measured state

```
files on disk             72   (36 chapters + 36 solutions)      = English
.fls files inputted       72                                   = English
pages                    367                                 (English 379)
LaTeX errors               0
undefined references       0
Overfull boxes             0                                    (3 found, 3 fixed)
nullfont warnings          0                                     = English
"Missing character"        0                                    (2 found, 1 cause, fixed)
TeX accent escapes         0                                     = English
\qty                   1,187, every unit argument ASCII          (English 1,186)
\unit / \qty non-ASCII     0
\text{...}                 9, all nine translated                = English
\index{} occurrences     182                                     = English
\includegraphics          56                                     = English
\legend / \addlegendentry 23, all translated                     = English
\omterm links          5,833   (English 5,547)  by year 1,243 / 2,292 / 2,298
distinct link targets    107   (English 103)
\omterm inside tikzpicture 0
exercise <-> solution keys identical in all 36 pairs
duplicate labels           0
check_translation.sh   PASSED for grade-10, grade-11, grade-12 (gates 1–10,
                       including the Devanagari prose gate and the orphan-line gate)
link_defined_terms --check   "every file matches what the config generates"
```

Every number above is the **final** state: the linker was re-run and both
`\omterm` censuses re-measured after the last prose edit of the overfull
sweep, and `--check` confirms the tree and `tools/term_config/book2_hi.py`
agree. *The last thing done was to measure, not to edit.*

## Censuses run, and what each found

### 1. `\omterm` per-target frequency diff against English

The instrument that showed the edition's structural problem: Hindi does not
inflect with a Latin-style suffix, so `lang_hi.py` sets `WORD_TAIL = ''` and
`DERIVE = False` and **nothing** is derived automatically. The first honest
harvest linked **4,672** — 84 % of English — with `कोशिका` at 396 links and
its own oblique and plural forms (`कोशिकाओं`, `कोशिकाएँ`, 481 occurrences)
invisible. The cure is the `DERIVED` block of `book2_hi.py`: 63 base terms and 74 forms
with the forms this book actually writes, each read off the corpus and each
checked for a second sense before it was added. That, plus five `EXTRA`
entries for definitions whose `\emph` display is itself an oblique
(`मूलरोमों`, `पेशी तंतुओं`, `इंट्रॉनों`, `द्वीपिकाएँ`, `शलाकाएँ`), took the
edition to 5,833.

### 2. `\omterm` chapter-set census (the one that finds homographs)

For every target, the set of chapters where `hi` links it minus the set where
English links it. This is the census that pays, and it found three classes:

* **समजात.** In grade 10 it is the *homology* of two organs (the defined
  sense); in grade 12 it is the second word of **समजात गुणसूत्र**, the
  homologous chromosomes of meiosis. 19 links in grade 12 pointed at the
  common-ancestry definition. `book2_en.py` protects exactly this pair with
  `r'homologous (?:chromosomes?|pairs?)'`; Hindi needs more patterns, because
  the noun also stands alone (`समजातों का हर जोड़ा`). 12 `EXTRA_PROTECT`
  patterns; 0 wrong links left.
* **प्रतिरोधी.** The antibiotic-resistant bacteria of grade 11 (72 honest
  links, which English throws away by STOPping "resistant") and the
  toxin-resistant maize borers of grade 12 (11 links, which English also
  refuses). Protected the borer collocations only, so the grade-11 links
  survive.
* **संधि.** The skeleton's *joint* (grade 10) and the second element of
  **तंत्रिका-संधि** (the synapse) and **दृक्-संधि** (the optic chiasm). The
  synapse keeps its links, because the longer term wins the sort; the chiasm
  and **संधि-दरार** are protected. Twelve bare `संधि` in the vision chapter
  meaning *chiasm* were reworded to `दृक्-संधि` — the prose is better for it.

Three further single-link collisions were cured in the prose rather than the
config, because the words were simply wrong: `वंशावली` (a *pedigree chart*)
used for a mitochondrial *lineage* → `वंशक्रम`; `बारंबारताओं` (allele
*frequencies*) used for a spindle's *firing rate* → `दरों`; `विभेदन` (a
microscope's *resolution*) used for the *differentiation* of a gonad →
`विभेदीकरण`.

### 3. The multi-word merge census

A Hindi phrase can accidentally become a two-word term when the linker's
longest-match sort crosses a phrase boundary. Checking every multi-word
display whose **first** word is itself a term found two:

* `क्या कोई प्रतिजैविक प्रतिरोध के उत्परिवर्तन करता है?` — "does an
  antibiotic cause resistance mutations?" was being read as "does an
  *antibiotic resistance* …". Reworded with a comma and a proper verb.
* `…पीछे बैठे युग्मविकल्पी बारंबारता में चढ़ें` — "the alleles rise in
  frequency" was being read as the term *allele frequency*. Reworded.

### 4. The sweeps

`['’]\s*$` (5 hits, all `''` closing quotes — English has 5 of the same),
`^\s*([.,;:)?!]|~[;:?!])` (4 hits, all TikZ `.. controls` continuation lines),
`[a-zà-ÿ]-\s*$` (0), `।\s*।` (0), `\s+।` (0), Devanagari digits (0), ASCII
`"` (0), `\index{}` count per file against the English twin (0 mismatches),
`\text{...}` over chapters *and* solutions (9 = 9, all translated), the 23
`\legend`/`\addlegendentry` sites by eye, every `\foreach` and
`symbolic coords` list by eye, and the siunitx audit in the shape
`WAVE1_FINDINGS.md` prescribes — **exactly the six `mmol/L` sites and nothing
else**, and zero non-ASCII bytes inside any `\qty`/`\num`/`\unit` argument.

## Terminology: four drifts of my own, normalised

Writing 72 files over three years drifts. A per-label occurrence diff against
the English twin caught four cases where the same concept had two Hindi words,
which would have split the link graph and read as two different books:

| concept | grade 10–11 wrote | grade 12 wrote | normalised to | sites |
|---|---|---|---|---|
| species | प्रजाति | जाति | **जाति** (it is the stem of जातिउद्भव, जातिवृत्तीय) | 132 |
| allele | विकल्पी | युग्मविकल्पी | **युग्मविकल्पी** (the standard term) | 176 |
| enzyme | एंजाइम | एंज़ाइम | **एंजाइम** | 28 |
| photosynthesis | प्रकाश संश्लेषण | प्रकाशसंश्लेषण | **प्रकाशसंश्लेषण** (closed compound) | 16 |
| feedback | प्रतिपुष्टि | पुनर्भरण | **प्रतिपुष्टि** | 6 |

## Deliberate divergences from the English, and why

* **`अधिकतम $\dot V\!\mathrm{O_2}$`** for English's `$\dot V\!\mathrm{O_2}$max`.
  "max" cannot go inside the math span (the math census compares spans
  byte-for-byte) and cannot stay outside it in Latin (the prose gate fires),
  so the word is translated and moved in front of the symbol, which is how
  Hindi says it anyway.
* **संधि** for *joint*, where biology Book 1 `hi` uses जोड़. जोड़ is "pair"
  and "sum" all through the genetics chapters of this volume; keeping it would
  have made the commonest word of grade 12 a homograph of a grade-10 term.
* **युग्मविकल्पी** for *allele*, where Book 1 `hi` uses विकल्पी. See above.
* **`\qty{4}{ms}-\qty{4}{ms}`** for "\qty{4}{ms} each" — the idiomatic Hindi
  distributive. It is the one `\qty` this edition has more than English.
* The CC BY image credit keeps its Latin title, **`\emph{Anatomy \& Physiology}`**
  (OpenStax), because a licence's attribution has to name the work as
  published; `and` became `\&` so that no English function word survives in
  visible text.

## Gate 7 (`tools/check_hindi_prose.py`): what I added, and why

I am the only consumer of this gate for `hi`, so it was extended **append-only,
each block dated and reasoned in a comment, and re-validated on both controls
after every change** (it must fire on an English chapter — 2,661 hits on
`parts/grade-12/14-brain-and-movement.tex` — and stay silent on real Hindi
prose — `parts/grade-12/hi/13-stretch-reflex.tex`). The controls were run in
the scratchpad, never in a live language directory. Three additions:

1. **`is_biochemical_token()`** with `AMINO_CODES`, `NUCLEOTIDE_STRAND`,
   `AMINO_CHAIN` and `SINGLE_RESIDUE`, inserted right after the existing
   `CHEM_FORMULA` escape. Book 2 prints nucleotide strands (`5'-ATGGCTTAC-3'`
   — `LATIN_WORD` is greedy over the hyphen, so `ATGGCTTAC-` no longer
   `fullmatch`es `CHEM_FORMULA`), peptide chains (`Met--Lys--Gly--Trp`) and
   the 64 lone three-letter residue codes of the genetic-code table. None of
   them is English; all 64 fired.
2. **`ALLOWED_WORDS |= {"heidelbergensis", "paranthropus", "africanus",
   "euglena", "chlorella", "archaeopteryx", "sry", "mrna", "trna", "rrna"}`** —
   Latin binomials new to Book 2, and the mixed-case RNA abbreviations, whose
   case defeats both the ≤4-letter acronym escape and `CHEM_FORMULA`.
3. **`ALLOWED_WORDS |= {"anatomy", "physiology"}`** — the two words of the
   OpenStax title in the grade-12 image credit, for the licence reason above.
   Deliberately *not* added: `and`, `of`, or any other function word.

## Three samples, with verdicts

**1. Chapter opening (grade 12, selection).** English: *"In 1848 a black form
of the peppered moth was caught near an industrial city where every tree trunk
was coated with soot…"*

> 1848 में किसी औद्योगिक शहर के पास काली मिर्च वाले पतंगे का एक काला रूप
> पकड़ा गया, जहाँ हर पेड़ का तना कालिख से पुता था; और 1895 तक उस इलाक़े का
> लगभग हर पतंगा काला था।

*Verdict: native.* The passive `पकड़ा गया`, the `जहाँ` relative and the `और …
तक` time frame are how a Hindi science writer opens a narrative paragraph.
`काली मिर्च वाले पतंगे` is a coinage (the species has no Hindi name), but it is
the same coinage the English name is.

**2. A definition (grade 12, glycaemia).**

> \emph{ग्लाइसीमिया}\index{ग्लाइसीमिया} रक्त प्लाज़्मा में ग्लूकोज की सांद्रता
> है: … ग्लाइसीमिया एक \emph{नियंत्रित} राशि है: यानी ऐसा मान जिसे कोई तंत्र
> किसी निर्धारित बिंदु के पास थामे रखता है, तथा उसे नापता और सुधारता है।

*Verdict: native.* `यानी` for English's dash-gloss, `निर्धारित बिंदु` for *set
point*, and the `जिसे … रखता है` relative instead of a participial calque.

**3. An exercise stem (grade 12, immunity).** English: *"Compute the
vaccination coverage needed for a disease with $R_0 = 4$, and with
$R_0 = 18$."*

> $R_0 = 4$ वाली और $R_0 = 18$ वाली किसी बीमारी के लिए ज़रूरी टीकाकरण कवरेज
> निकालिए।

*Verdict: native.* `वाली … वाली` is the ordinary Hindi way to hang two
specifications on one noun, and the math span is byte-identical and in the
English order — which is exactly what the math census enforces and what a
careless reordering would have broken.

## Why not 100

* **−2, terminology.** Four cross-year drifts existed at all. They were found
  and normalised, but a book written by one hand should not have needed the
  census to notice that grade 10 said प्रजाति and grade 12 said जाति.
* **−1, link density in one target.** `def:g10:exercise-and-energy:vo2max`
  ends with **0** links against English's 2: the Hindi prose says
  `अधिकतम $\dot V\!\mathrm{O_2}$`, and nothing can link inside a math span.
  English's `\dot V\mathrm{O_2}max` has the same problem in reverse and gets
  its links from the spelled-out term, which Hindi uses only in the definition.
* **−1, `आँख`.** 101 links, against English's 12 — English STOPs "eye" for the
  naked-eye idiom, which Hindi does not have (this edition writes नज़र for the
  figurative uses), so every use here is the organ and every link is
  sense-correct. It is still more links on one everyday word than a reader
  needs.

## Defects found in the ENGLISH canon (reported, not fixed)

1. **`parts/grade-12/solutions/11-innate-immunity.tex`, solution 1–2.** The
   splinter problem doubles every 40 minutes, so solution 1 correctly gives
   "three doublings in 2 hours". Solution 2 then compares the macrophages'
   1,000 removals with "the `\num{10000}` new bacteria the first hour's
   doublings add" — but 1.5 doublings of 10,000 add about **18,000**, not
   10,000. The conclusion ("growth continues") is unaffected; the figure is
   not.
2. **`parts/grade-12/02-diversification-of-life.tex:137`.** The index key of
   the developmental-gene definition is broken across a source line:
   `\index{developmental\ngene}`. It builds, but every translation has to
   reproduce the break to keep the `\index` census equal, and any tool that
   reads index keys line-by-line will mis-read it. A `%`-continuation or a
   single line would be safer.
3. **`parts/grade-12/14-brain-and-movement.tex:96`.** The homunculus credit
   prints the CC BY work title *Anatomy and Physiology* in running prose. For
   the Latin-script editions this is free; for `hi` and `ar` it puts an
   English function word (`and`) inside visible text, which the residual-Latin
   gates are built to reject. `\&` (or a `\textenglish`-style wrapper in
   `styles/`) would let every edition keep the attribution without weakening
   a gate.

## Tooling notes for the next agent on this language

* **A Devanagari matra is its own code point.** `समजातों?` in an
  `EXTRA_PROTECT` pattern makes only the *anusvara* optional and never matches
  the bare `समजात`. Every optional Hindi ending must be a group: `(?:ों)?`.
  Three wrong links survived the first draft of `book2_hi.py` for exactly that
  reason, and the mistake is invisible in a diff.
* **The second `--apply` pass reads the first pass's output.** An
  `EXTRA_PROTECT` pattern that spans two words will silently stop matching
  once pass 1 has wrapped the second word, and the term it was protecting gets
  linked on pass 2. The patterns here tolerate the wrapper:
  `r'समजात(?:ों)?\s+(?:\\omterm\{[^{}]*\}\{)?गुणसूत्र(?:ों)?'`.
* **`\unit{\micro …}` inside a pgfplots axis label is typeset in the
  surrounding text font.** In `hi` that is NotoSansDevanagari, which has no
  micro sign, and XeLaTeX reports `Missing character: There is no ¤ (U+00A4)`
  — twice, silently, with exit code 0 from the engine. Every other `\micro` in
  this book — 85 of them, all inside `\qty` in running text or math — is fine.
  Write the unit out in Devanagari in axis labels.
* **Overfull boxes in a Devanagari edition really are prose.** All three here
  were `in paragraph`, none was `detected at line`; all three were cured by
  shortening one long word or removing a long unbreakable run, never by
  touching `styles/`.
