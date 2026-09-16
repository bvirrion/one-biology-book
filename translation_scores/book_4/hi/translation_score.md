# Biology Book 4 (University Year 2) — Hindi edition, self-score

**Date:** 2026-09-16
**Scope:** `parts/bachelor-2/hi/` (27 chapters) and `parts/bachelor-2/solutions/hi/`
(27 solution files), `frontmatter/image-credits-book4.hi.tex`,
`tools/term_config/book4_hi.py`.

## Overall: 96 / 100

| Dimension | Score | Note |
|---|---:|---|
| Accuracy of content (numbers, biology, argument) | 98 | Every figure, unit and inference re-derived against the English twin; the `id_apply.py` math census proves the equations are byte-identical. |
| Terminology and consistency | 95 | Base vocabulary harvested from the Book 3 `hi` edition (544 index-key pairs); two terminology splits of my own were found by the link census and repaired (see below). |
| Register and fluency (standard technical Hindi, lecture voice) | 96 | `मान लीजिए` / `निकालिए` / `समझाइए` throughout, danda sentence ends, ASCII digits, Latin binomials and gene symbols kept. |
| Structural fidelity (labels, environments, math, figures) | 100 | Gate 1–11 PASSED; labels, `\cref` targets, solution keys, math spans, drawing code and image paths byte-identical to English. |
| Typography and build | 97 | 0 errors / 0 undefined / 0 overfull / 0 `nullfont`; one solution needed a local `\sloppy` group. |
| Term links | 95 | 3,014 links on 157 targets against English's 3,093 on 155; every English target reached, no wrong-sense chapter. |

**Quality bar used:** the native-academic bar of `translation_instruction.md` — a
Hindi-speaking BCPST/L2 lecturer reading this volume should not be able to tell
it was translated, and should never have to reconstruct the English to
understand a sentence. Ship threshold 95/100.

**Sense reference used:** the English canon in `parts/bachelor-2/` (read line by
line), plus the Book 3 Hindi edition (`parts/bachelor-1/hi/`) as the
terminological base, `hindi_style_card.md` for the variety and mechanics, and
`translation_instruction.md` for the defect classes and the two collision
censuses.

## Samples read against the English twin

1. **ch. 20, chapter opening (the knee jerk).** EN "a signal has travelled a
   metre to the spinal cord, crossed one junction to a second cell" →
   "कोई संकेत मेरुरज्जु तक मीटर भर चल चुका है, किसी दूसरी कोशिका तक एक जोड़ पार कर
   चुका है". **Verdict: pass.** The perfective chain (`चल चुका है` … `पार कर चुका
   है` … `सिकोड़ चुका है`) carries the English "in that time … has happened"
   construction naturally; no calque.

2. **ch. 22, `thm:b2:population-genetics:selection`.** The selection equation and
   its two consequences. **Verdict: pass.** Display and every inline span are
   byte-identical; the prose around them was re-ordered so the spans occur in the
   English order (`$\Delta p$ $pq$ के समानुपाती है`), which is what the math
   census enforces. Reads as ordinary Hindi, not as a gloss.

3. **ch. 17, `prop:b2:heart:cycle` (the cardiac cycle).** EN "the ventricle
   squeezes a closed chamber --- isovolumetric contraction --- until its pressure
   passes the arterial pressure" → "वह निलय किसी बंद कक्ष को भींचता है ---
   समआयतनी संकुचन --- जब तक उसका दाब धमनीय दाब को पार न कर ले". **Verdict:
   pass.** `भींचना` is the right verb for a muscular squeeze; the em-dash
   apposition survives.

4. **ch. 26, `thm:b2:living-soil:decay` (C:N and immobilisation).** EN "litter
   with C:N below about 25 releases ammonium as it decays (mineralisation), while
   litter above it … makes the microbes take up nitrogen from the soil
   (immobilisation)". **Verdict: pass.** `खनिजीकरण` / `स्थिरीकरण` are the
   standard pair; `स्थिरीकरण (नाइट्रोजन)` is used in the index so it does not
   collide with the nitrogen-fixation sense.

5. **ch. 27, `ex:b2:global-change:scenarios` (three futures).** Re-read after the
   coordinator's canon repair: "ranges … move \qty{200}{km} beyond today's in the
   first case and \qty{60}{km} in the second" → "परास पहली स्थिति में आज के परे
   \qty{200}{km} चलते हैं और दूसरी में \qty{60}{km}". **Verdict: pass** — both
   figures hang off the same "आज के परे", as the repaired English intends.

## Why not 100

* **Two terminology splits were mine, not the canon's**, and only the link census
  found them: *sarcomere* was `पेशीखंडिका` in ch. 12 and `सार्कोमियर` in ch. 21
  (unified to `सार्कोमियर`, 41 occurrences), and *stem cell* / *palisade cell*
  were both `स्तंभ कोशिका` (palisade is now `खंभ कोशिका` / `खंभ-परत` in ch. 15).
  A translation that needed a census to catch its own homographs is not a 100.
* **Four wrong-sense words had to be repaired in the prose after the fact**:
  `प्रभावी` used for "effective" where it is the genetics term *dominant* (ch. 14,
  19), `भरती` used for "fill" where it is *recruitment* (ch. 23), `द्विगुणित`
  used for "duplicated" where it is *diploid* (ch. 11 solutions), and
  `रसायन-शिलापोषी` vs `रसशिलापोषी` (ch. 25).
* **157 targets against English's 155 and 3,014 links against 3,093.** The two
  extra targets are right-sense (see below); the 79 fewer links are mostly Hindi
  compounds that the English pattern reaches with a plural `-s` and Hindi cannot
  (`lang_hi.py` has `WORD_TAIL = ''`), plus adjectival derivations
  (`धमनीय` = arterial, `पुष्पन` = flowering) that I deliberately did **not**
  declare, because English does not link its own adjectives either.
* **One solution needed a local `\sloppy` group** (`solutions/hi/02`, answer 1):
  the chain of five trophic compounds (`प्रकाश-शिला-स्वपोषी`,
  `रस-कार्बनिक-परपोषी`, …) has no hyphenation and no feasible break within
  `\tolerance`. `\allowbreak` after the hyphens did not help; the paragraph is
  now wrapped in `\begingroup\sloppy … \par\endgroup`, the same remedy the
  credits page uses.
* `\text{बाहर}` / `\text{भीतर}` are twice the width of `\text{out}` / `\text{in}`,
  so one Nernst answer (`solutions/hi/20`, answer 5) had to be reworded
  (`से ये मान मिलते हैं।`) to give TeX a break point. Correct, but a divergence
  from the English sentence shape.

## Gate output

```
bash tools/check_translation.sh bachelor-2 hi
  == bachelor-2 / hi ==
    hindi prose gate: OK (54 files)
  TRANSLATION GATE: PASSED            (gates 1–11)

python3 tools/check_problem_numbering.py parts/bachelor-2/hi parts/bachelor-2/solutions/hi
  problem numbering: OK (27 chapters)

python3 tools/link_defined_terms.py --book 4 --lang hi --check
  LINKABLE TERMS : 516
  links to insert: 3014 across 54 files
  CHECK: every file matches what the config generates

latexmk -g one_biology_book_4_university_year_2_hi.tex
  Output written on build/one_biology_book_4_university_year_2_hi.pdf (307 pages)
  ^!          0
  undefined   0
  Overfull    0
  nullfont    0
  invalid in math mode 0
  "detected at line"   0        (no ToC page-number box overflow)
  .fls files under parts/bachelor-2/{,solutions/}hi : 54   (= files on disk)

counts, this edition vs the English twin (identical in every one)
  \index 621   \qty 2458   \qtyrange 33   \num 175   \unit 56
```

Collision censuses (both run after the last file landed, against the English
twin): per-target frequency and per-target chapter set.
**No chapter-set anomaly remains** — every target is linked in exactly the
chapters English links it in, or fewer. Two targets are linked here that English
does not link, both right-sense:

* `prop:b2:plant-meristems:sam` — `पर्ण प्राथमिकांग` (leaf primordium). English's
  own index entry there is single-word, so `harvest.py` drops it.
* `thm:b2:blood-pressure:fick` — `फ़िक सिद्धांत` (Fick principle). English drops
  "Fick principle" because `NOT_A_TERM` contains "principle", which is an English
  word list and cannot fire on Hindi.

## Deliberate divergences from the English

* **Word order around mathematics.** Hindi postpositions force the text macro to
  move; the mathematics never does. Roughly twenty-five sentences were re-ordered
  so the math spans occur in the English sequence (the `math` census in
  `id_apply.py` rejects anything else). Example: EN "with $R = \qty{1}{mmHg.s/mL}$
  and $C = \qty{2}{mL/mmHg}$, compute …" → "$R = …$ और $C = …$ के साथ, … निकालिए".
* **`\text{…}` inside mathematics is Hindi**, following the Book 3 `hi`
  convention (`\text{भीतर}`, `\text{बाहर}`, `\text{कुल}`): `c_{\text{बाहर}}`,
  `P_{\text{शिरा}}`, `C_{\text{संचयी}}`, `\bar P_{\text{निष्कासन}}`. The
  exceptions are unit strings (`\text{mol/L}`, `\text{nmol}`), which stay Latin.
* **`\foreach` label lists, `symbolic x coords` and the `coordinates` that index
  them are translated** by a post-write edit, because the `draw` census does not
  blank them (ch. 1, 4, 5, 6, 8, 10, 11, 13, 14, 15, 18, 19, 21, 23, 24).
* **"Million years" is written `मिलियन वर्ष`** in ch. 24, where the numeral sits
  inside a frozen math span (`$t = d/2k = 35$ मिलियन वर्ष`) and `करोड़` would
  contradict it; `करोड़`/`लाख` are used elsewhere. Book 3 `hi` mixes the two the
  same way.
* **Initials expanded.** `A.~F.~Huxley` and `H.~E.~Huxley` are written
  `एंड्रयू हक्सली` and `ह्यू हक्सली`: a bare transliterated `ए.` is flagged by the
  `translit` rule of `check_hindi_prose.py` (it is the article *a*), and
  expanding the names is better Hindi than inventing a spelling that dodges the
  gate.
* **`आरपार`, not `आर-पार`** — the Book 3 `hi` spelling (39 occurrences there),
  chosen for the same reason.
