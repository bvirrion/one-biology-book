# One Biology Book 1 — Dutch (`nl`) edition: self-score

**Date:** 2026-09-04
**Scope:** `one_biology_book_1_primary_middle_school_nl.tex` — 71 chapters +
71 solutions files (grades 1–9), 142 files, 453 pages.
**Quality bar:** *native school prose*. The question is not "is this a correct
rendering of the English?" but "would a Dutch biology teacher writing this book
from scratch, for these ages, have written these sentences?" The register
reference is the physics Book 1 `nl` edition
(`../one-physics-book/parts/grade-*/nl/`) — same ages, same series, same
exercise machinery.

## Overall: **96 / 100**

| Dimension | Weight | Score | Notes |
|---|---|---|---|
| Register and voice | high | 96 | informal `je` / `jouw` throughout, 0 `u`/`uw`; imperative exercise stems |
| Terminology | high | 96 | Dutch school-biology vocabulary; Latin binomials and DNA/RNA/ATP/pH untouched |
| MT-artifact freedom | high | 96 | no calques left in the sampled reading; two mistranslations found and fixed |
| Structure / LaTeX hygiene | gated | 100 | `id_apply` censuses green on all 142 files; log 0/0/0 |
| Cross-references | gated | 100 | 0 undefined references |
| Figures and captions | — | 97 | all 254 TikZ node sites and 3 `\foreach` label lists translated; 132 image paths byte-identical |
| Solutions | — | 96 | all 71 solutions twins translated; `\text{}` census clean over solutions too |
| Defined-term links | — | 93 | 6,451 links on 151 of English's 152 targets |

## Measured state

```
files on disk            142   (71 chapters + 71 solutions)     = English
.fls files inputted      142                                    = English
pages                    453                                   (English 422)
LaTeX errors               0
undefined references       0
Overfull boxes             0
nullfont warnings         20                                    = English
"invalid in math mode"     0
TeX accent escapes         0                                    = English
\qty                      57, every unit argument ASCII         = English
\text{...}                 4, all four translated               = English
\index{} occurrences     331                                    = English
distinct \index keys     303   (English 298)
\omterm links          6,451   (English 7,609)
distinct link targets    151   (English 152)
check_translation.sh   PASSED for grade-1 … grade-9 (gates 1–10)
check_orphan_lines.py  0 orphan English lines
check_latin_prose.py   OK, 142 files
```

## Censuses run, and what each found

* **`\omterm` per-target frequency diff vs English.** Caught the two
  collisions the Dutch plural rule manufactures: `lang_nl.py`'s
  `WORD_TAIL = (?:e?[ns])?` makes the term **lever** (liver) also match
  **leveren** — the verb *to supply* — which had linked 15 times, and the term
  **spore** also match **sporen**, which in Dutch is equally *tracks, traces,
  op te sporen*: 17 wrong links across grades 6, 7 and 9. Neither is reachable
  by `DROP` (the plural is not a term key), so both wrong **senses** are masked
  in `EXTRA_PROTECT`, phrase by phrase, and the 21 correct *lever* and 24
  correct *spore(n)* links survive.
* **`\omterm` chapter-set diff vs English.** Caught what frequency could not:
  `eis` (a *demand*) linking to the egg definition — the same tail rule, since
  the real Dutch plural of *ei* is *eieren*; and `kamer` (heart chamber)
  linking *the room* in two places. Also surfaced the one genuine
  **mistranslation** of the run: `pols` = *wrist*, but I had written "pols en
  druk" where English reads "pulse and pressure" — the Dutch is `polsslag en
  bloeddruk`, now fixed in the chapter and its solution.
* **`\index{}` key-set diff vs English.** 331 occurrences on both sides, and
  every one of the 18 keys that is byte-identical to English is a real Dutch
  word (`DNA, arm, baby, diabetes, embryo, glucose, humus, insect, karyotype,
  microhabitat, penis, placenta, plant, rib, spore, urine, virus, zygote`).
  No English index entry survives.
* **`\text{...}` census over chapters *and* solutions**: 4 in each tree,
  `buzzard/grasshopper/grass/lizard` → `buizerd/sprinkhaan/gras/hagedis`.
* **Line-end greps** (`['’]\s*$`, `^\s*([.,;:)?!]|~[;:?!])`, `[a-zà-ÿ]-\s*$`):
  one real hit — a line ending on `` `gedoe' `` — fixed by **rewrapping**, not
  by a trailing `%`. The remaining `^\s*\.` hits are TikZ `..` path syntax,
  byte-identical to English.
* **Overfull sweep**, run before the final linker pass: 3 boxes, all
  `in paragraph`, all cured by adding short words before the break point
  (two prose rewrites in grades 2 and 6, one in the image-credits page).
  The linker and both `\omterm` censuses were then re-run *after* the sweep,
  and the sweep's own rewrites were re-checked.

**Homograph collisions found and fixed: 38** (15 `leveren`, 17 `sporen`,
2 `eis`, 2 `kamer`) plus 2 genuine mistranslations (`pols` → `polsslag`).

## Register

Verified against physics Book 1 `nl`, not inferred:

```
biology  nl:  je 388   jij 31   jouw 38   u 0   uw 0
physics  nl:  je 992   jij 41   jouw 72   u 6   uw 2
```

Second-person density tracks the English source (biology English uses
*you/your* 328 times to physics English's 904). Exercise stems are bare
imperatives and interrogatives in both books — *Waarom…, Wat…, Noem…, Geef…,
Beschrijf…, Leg uit…, Probeer het:* — never `u`-imperatives and never
infinitive stems. Chapter titles, `definition`/`proposition`/`method` titles
and problem titles are Dutch noun phrases, as in the physics twin.

## Sampled fragments, judged

1. **grade 1, ch. 2 opening** — *"Een merel huppelt over het gazon, een kat
   kijkt vanaf de muur toe, een mier sleept een kruimel groter dan zichzelf
   over de drempel."* — **native**. Verb choice (*huppelt*, *sleept*), the
   `vanaf … toe` split particle and the rhythm are Dutch, not English word
   order carried over.
2. **grade 7, ch. 5 opening** — *"Dit jaar zetten we de deuren van de
   werkplaats open: wat doen die sappen precies … en hoe klaart de wand van de
   dunne darm de grootste grensovergang van het lichaam?"* — **native**.
   *de deuren openzetten* and *een grensovergang klaren* are idiomatic; the
   English "throws the workshop doors open" is not calqued.
3. **grade 9, ch. 6 opening** — *"Samengebouwd lopen ze vanzelf --- dat vanzelf
   lopen is de natuurlijke selectie, en het is het eenvoudige idee met de
   grootste gevolgen uit de hele biologie."* — **native**. The nominalised
   *dat vanzelf lopen* is the Dutch way to do what English does with
   "that self-running".
4. **grade 9, ch. 2 solutions, #9** — *"Er is niets verkeerd gedaan: de extra
   21 ontstaat bij een ongeluk in het halveren --- de partners van een paar die
   niet uit elkaar gaan --- een pech van het mechanisme, niet van de daden of
   de waarde van de ouders."* — **near-native**. Correct and warm, but *een
   pech van het mechanisme* is a shade unusual; *een pech van de machinerie*
   or *een misser van het mechanisme* would read fractionally better.
5. **grade 2, ch. 6, example** — *"Als tussendoortje A: een appel, een boterham
   en wat water."* — **native**; this sentence is also the overfull-box rewrite,
   and adding *Als … En als …* both fixed the box and improved the rhythm.

## Why not 100

* **Link density is 85 % of English (6,451 vs 7,609).** This is structural, not
  sloppy: Dutch writes compounds solid, and `lang_nl.py` deliberately refuses to
  match inside one, so *huidcellen*, *lichaamscellen* and *bekledingscellen* are
  three words English spells as two and links as one. I recovered what could
  honestly be recovered (`EXTRA` for *witte bloedcellen*, *geslachtscel(len)*),
  and declined to invent a long EXTRA list of arbitrary compounds, which would
  trade a measured deficit for unmeasured noise.
* **One English target has no Dutch counterpart**
  (`prop:g2:caring-for-nature:recycle`). Its two English links are themselves
  wrong-sense — English links the *waste-sorting* proposition from "Sorting by
  body features" (grade 3) and "Part I --- Sorting the ledger" (grade 9). The
  Dutch `DROP` of *sorteren* correctly refuses to reproduce them; the target
  simply has nothing left to link. This is a defect in the English edition, not
  in the Dutch.
* **Three `sporen` and one `huiden` link are judgement calls** left in place:
  bacterial spores pointed at the fern-spore definition (English does the same),
  and a plant's waxy *huiden* pointed at the skin definition.
* **453 pages against English's 422.** Dutch runs about 9 % longer in words;
  nothing was padded, but the volume is physically bigger.
