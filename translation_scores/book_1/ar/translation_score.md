# Translation score — Biology Book 1 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Modern Standard Arabic (`ar`) |
| **Quality bar** | **native school prose** (English is the source of truth for content and labels; there is no Arabic twin of this book, so the register exemplar is the shipped `ar` edition of **Physics Book 1** — same ages, same series, same apparatus — and the terminology reference is ordinary Arabic SVT/علوم الحياة usage) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-04 |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 71 chapters + 71 solution twins (**142 bodies**), the two front-matter files reviewed against English (`preface.ar.tex` kept as drafted, `image-credits.ar.tex` corrected), and a curated `tools/term_config/book1_ar.py`, then the defined-term link layer, then this score. |

## Verdict in one line

An Arabic Book 1 that reads as though it had been written in Arabic — for
Arabic seven-year-olds in الصف الأول and for Arabic fifteen-year-olds in
الصف التاسع — with the vocabulary a middle-school pupil will meet again in
the high-school volume, and with every structural, build and link-hygiene
gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, measured across all 142 files: **796 `exercise` EN / 796 AR**, **35 `problem` / 35**, **831 `\begin{solution}` / 831**, **70 `[resume]` / 70**, **99 `omfigure` / 99**, **43 `tikzpicture` / 43**, **169 `\node` / 169**, **76 `\includegraphics` / 76**, **57 `\qty` / 57**, **142 `\admitted` / 142**, **895 `\emph{` / 895**, **331 `\index{` / 331**. `\label` set diff = **0 lines**; `\cref`/`\ref` target set diff = **0 lines** |
| Terminology | **96** | Ordinary Arabic school biology, chosen for continuity upward: *كائن حي، موئل، سلسلة غذائية، محلِّل، مادة عضوية، زغابات، أسناخ، أذين/بطين، مشيمة، حيض، عصبون، مشبك، تغذية راجعة، نمط صبغي، أليل، انتقاء طبيعي، نبيت مقيم، ممرض، جسم مضاد، مستضد*. Two deliberate near-homograph splits were held for the whole book: *بدن* (body trunk) vs *جذع* (tree trunk), and *بويضة* (egg cell) vs *بييضة* (plant ovule). Unit symbols and all `siunitx` markup byte-identical to English; **0 non-ASCII characters inside `\qty` / `\unit` / `\num`** |
| Register / tone | **96** | Measured against `../one-physics-book/parts/grade-*/ar/` before drafting: MSA throughout, second-person-singular imperatives in the exercise stems from grade 1 to grade 9 (*سمّ، ارسم، اذكر، فسّر، طبّق، برهن، اكتب*), course text impersonal from grade 6 on. Arabic comma `،`, semicolon `؛` and question mark `؟` used throughout; Latin full stop, as the style card requires |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes**, `nullfont` **20** (the English baseline exactly), 0 `invalid in math mode`, 20 `Missing character` lines (all of them the nullfont ones) — all measured with `grep -a`. **0 tatweel (U+0640)**, 0 bidi control characters (U+200E/200F), 0 Arabic presentation forms (U+FB50–FDFF, U+FE70–FEFF), 0 Arabic-Indic digits, 0 wrong-order accusative tanween |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English. No curriculum, programme or country name anywhere in visible text |
| Figures | **97** | All TikZ / pgfplots drawing code byte-identical — coordinates, axis options, colours untouched; only node text and `{\small …}` captions localized. Two classes of change the `draw` census cannot see were made as targeted post-write edits, never as a file-wide `!draw` opt-out (see *Deliberate divergences*): three `\foreach` visible-label lists, and the direction of all 56 inline arrows |
| Solutions | **96** | All 796 exercise solutions and all 35 weekend-problem solutions present and native; headers `\section*{الفصل \ref{ch:…} --- <العنوان>}` with the `ch:…` slug unchanged. Open-answer models rewritten as Arabic, not glossed (the closing line of the book — «الحلزون وأنت بنيتما بالأحرف الأربعة نفسها: فاعتن بالعائلة كلها.») |
| Defined-term links (`\omterm`) | **95** | **6 781 links over 152 distinct targets**, against English's **7 607 over 151** — 89.1 % density, and a **superset** of English's target set. Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles |
| MT-artifact freedom | **97** | `check_arabic_prose.py`: **PASSED for all nine years**, 142 files, 0 findings in any of its nine classes. `check_orphan_lines.py`: **0 orphan English lines**. `\text{…}` census over course **and** solutions: 4 of 4 translated (*عشب، جندب، سحلية، صقر*). The three line-end greps: 0 hits (the only `^\s*[.,;:)?!]` matches are TikZ Bézier `..` continuations, byte-identical to English) |

**Overall: 96** (weighted toward terminology + register + MT-artifact freedom;
structure is already gated mechanically).

## Structural / build gates

Measurement note: the LuaLaTeX log carries non-UTF-8 bytes, so a plain
`grep -c '^!'` treats the file as binary, prints nothing and exits 1 — which
reads exactly like a pass. Every figure below was taken with `grep -a`.

```
build/one_biology_book_1_primary_middle_school_ar.log
  errors            0
  undefined         0
  Overfull          0
  nullfont         20   (the English number; a rise is the accent-in-\qty failure)
  invalid in math   0
  Missing character 20   (identical set to the nullfont lines)
  pages           396   (English 422)
build/one_biology_book_1_primary_middle_school_ar.fls
  parts/grade-*/ar files   142  (= the 142 on disk)
```

`tools/check_translation.sh grade-1 … grade-9 ar`: **TRANSLATION GATE:
PASSED** for all nine years.

`python3 tools/link_defined_terms.py --book 1 --lang ar --check`:
*every file matches what the config generates* — i.e. the shipped link layer
was regenerated after the last prose edit, not before it.

## The two `\omterm` censuses

**Frequency diff, per target, against English.** All 151 English targets are
present in the Arabic edition; the Arabic edition carries **one target
English does not**, `prop:g6:decomposers-and-soil:decomposition` (4 links).
That is not an Arabic invention: the English definition emphasises
*Decomposition* capitalised, so the harvest registered only the capitalised
display and the lowercase word in later chapters never matched — the same
`\emph{Sorting}` trap the Dutch agent found. Arabic's *التحلل* has no case,
so the links are simply there.

The density gap is 826 links, and it is concentrated in four targets whose
Arabic word is morphologically poorer than the English one, not in any
missed prose:

| Target | EN | AR | why |
|---|---:|---:|---|
| `prop:g3:flowers-fruits-seeds:transform` | 168 | 52 | English's plural *seeds* is ambiguous (grade-2 seed vs grade-3 fruit-and-seed) and nearest-preceding sends 98 of them here. Arabic's *بذور* is a **broken** plural declared in `DERIVED`, and `DERIVED` can only extend an **unambiguous** base, so all of them stay on the grade-2 target. Combined, EN 276 / AR 261 across the two targets — the words are linked, the attribution differs |
| `def:g1:plants-around-us:parts` | 316 | 226 | *leaves* + *leaf* + *roots* + *stem* + *root* is five English forms; Arabic has *أوراق/ورقة/جذور/جذر/ساق/سيقان* and the same prose simply says «النبتة» more often |
| `def:g3:flowers-fruits-seeds:parts` | 173 | 113 | same shape, one level down (*petal/petals*, *stamen/stamens*) |
| `def:g4:breathing:organs` | 43 | 2 | the honest one. English's *lungs* is ambiguous grade-4/grade-7 and nearest-preceding gives grade 4 its share. Arabic writes the dual *الرئتان/رئتين*, which the harvest saw only as the grade-7 display, and `wrap_file` links a term only from its own chapter on — so grades 4–6 get nothing. Fixing it needs one string mapped to two labels, which the config format cannot express |

**Chapter-set diff, per target, against English.** 37 targets differ in the
set of grades they are linked from. Every one was read in context. The
ar-only appearances are all correct-sense re-uses of a word Arabic happens to
spell the same way (*أطراف* limbs in grades 3–9, *محك* criterion in grade 9,
*الشيخوخة* old age in grade 9, *الأغصان* branches in grade 8, *العرق* sweat in
grade 8, *شجرة العائلة* in grade 9); the en-only appearances are the
morphological gaps tabulated above.

### Homograph collisions found and fixed

Reading the **display/target pairs** the linker actually produced — not the
frequency counts, which stayed green throughout — found **seven Arabic
homograph classes shipping wrong-sense links**, and seven more that were
pre-empted before they could fire. They cost 33 links to remove; every one is
recorded, with its evidence, in `tools/term_config/book1_ar.py`:

| word | the two senses | wrong links | fix |
|---|---|---:|---|
| حمل | *pregnancy* / the perfect verb *carried* | 12 | `DROP`, restored as the definite «الحمل» in `EXTRA` |
| تحول | *metamorphosis* / the verb *turns X into Y* | 3 | `DROP`, the definite «التحول» stays |
| الصمامات | the heart's valves / the male tract's valve arrangement | 3 | `EXTRA_PROTECT` |
| بول | *urine* / **Paul** Nadar, the photographer | 1 | `EXTRA_PROTECT` |
| مضغ | plural of *embryo* / the verbal noun for *chewing* | 1 | `EXTRA_PROTECT` |
| جذر / ساق | a plant's root and stem / a **hair's** root and shaft | 1 | `EXTRA_PROTECT` |
| بصلة | grade-4's *bulb* / the **onion** mashed in the DNA extraction | 1 | `EXTRA_PROTECT` |

Pre-empted before they fired, by `STOP`/`DROP`/`EXTRA_PROTECT`: **شاهد**
(experimental control / **witness** — chapter g9-05 argues from four
independent witnesses), **حلقة** (a food chain's link / the report-decide-order
**loop** / a seminar), **الفطور** (plural of *fungus* / **breakfast**, eaten
repeatedly in grades 8–9), **رجل** (*leg* / **man**), **طرف** (*limb* /
*party, end*), **نوع** (*species* / *a kind of*), **واقي** (grade-8's condom /
the pigment that is the body's **sunscreen** in grade 9).

### One terminology drift found and unified

The `\omterm` display census also exposed a drift the structural gates cannot
see: **two different broken plurals of مشيج** were in use for *gametes* —
*مشائج* (44 sites) and *أمشاج* (21). Both are correct Arabic and both linked
to the same target, so no count moved; only reading the displays showed it.
Unified to **أمشاج** (the standard plural, and the one the grade-8 definition
emphasises) across all 65 sites, and the link layer regenerated afterwards.

## `\index{}` key-set diff

**331 entries in both editions**, 303 distinct keys in English against 298 in
Arabic (the difference is five keys Arabic spells identically where English
spells them apart). **Exactly one Arabic key contains Latin characters —
`DNA`** — and it is the only key shared with English, by design.

## Sampled fragments

| # | Fragment | Judgement |
|---|---|---|
| 1 | grade 1, `def:g1:living-or-not:living` — «الكائن الحي شيء حي: يولد، ويتغذى، وينمو، ويمكن أن يكون له صغار، ويموت يومًا ما.» | **native** — the enumerative *و…و…و* rhythm of Arabic primary science, no copied English clause order |
| 2 | grade 5, `rem:g5:brain-in-command:training` — «التمرين يقصّر الحلقة ويشحذها --- لا سرعة الأعصاب، بل توجيه الدماغ. فالمشعوذ المبتدئ يُسقط كل شيء؛ وبعد شهر يأمر الدماغ نفسه اليدين نفسيهما بثلاث كرات بلا جهد ظاهر.» | **native** — «لا … بل …» carries the English em-dash contrast without importing the dash grammar |
| 3 | grade 9, `ex:g9:how-species-change:resistance` — «أضعف الكابح على نحو مهلهل، تربّ ما أردت قتله.» | **native** — a conditional jussive pair, the Arabic idiom for *do X and you breed Y*; a machine draft would have produced «إذا أضعفت… فإنك ستربي» |
| 4 | grade 9 solutions, `exo:g9:immune-defenses:8` — «فسلالات كل شتاء تلبس أوصافًا لا تحملها الذاكرة، فيكون كل زكام هبوطًا أول.» | **native** — *تلبس أوصافًا* keeps the English "wear descriptions" image inside an Arabic collocation that exists |
| 5 | grade 8, `prop:g8:contraception:principle` — «وكل طريقة على رف الصيدلي هجوم على حلقة مسماة واحدة، وترتيبها بحسب حلقتها هو النظرية كلها.» | **near-native** — correct and idiomatic, but «هو النظرية كلها» is a shade more literal than an Arabic textbook's «وفي هذا الترتيب تكمن النظرية كلها» |

## Deliberate divergences from the English source

1. **All 56 inline arrows flipped.** English's 53 `\rightarrow` and 3
   `\longrightarrow` became `\leftarrow` / `\longleftarrow` in 8 files. Under
   babel `bidi=basic` an inline `$\to$` between two Arabic words renders
   pointing at the word that comes **first** in the sentence, so «عشب
   $\rightarrow$ جندب» reads *grasshopper eats grass*. Verified empirically:
   a single-chapter probe was built with LuaLaTeX, rasterised with
   `pdftoppm`, and the page read; the flipped version reads correctly.
   The English math spans were kept byte-identical inside the patch and the
   flip applied as a targeted post-write edit — never a `!math` opt-out.
2. **Three `\foreach` visible-label lists translated** (`grade-2/01`,
   `grade-3/01`, `grade-4/01`). The `draw` census blanks node text and legend
   strings but not a `\foreach` value list, so these could not be localized
   inside a patch without a file-wide `!draw` opt-out; a single targeted
   post-write edit was applied instead.
3. **The wall-map instruction in `pb:g9:how-species-change:1` reads «من
   اليمين إلى اليسار»** where English says *left to right*. A chain diagram
   drawn on an Arabic classroom wall is drawn right to left; keeping the
   English direction would have made the instruction wrong.
4. ***Archaeopteryx* transliterated to الأركيوبتيريكس** at 6 sites in
   `grade-9/05` and its solutions twin (and once in the image credits).
   Forced, not chosen — see *Requests to the orchestrator* below.
5. **The Jenner photo credit inside `grade-9/08`** reads «تصوير زيتي، مجموعة
   ويلكم، CC~BY~4.0.» The licence identifier is verbatim, as instructed; the
   medium is translated; the **institution name could not be kept in Latin**
   — again forced, see below. `frontmatter/image-credits.ar.tex` is outside
   the prose gate's scan path and does keep «Wellcome Collection» in Latin,
   as `fr`, `nl`, `hi` and `id` do, so the two spellings differ. That is a
   consequence of the gate gap, not an editorial decision.
6. **Blood groups kept as Latin `A` / `B` / `O` / `AB`**, which is what
   Arabic school textbooks and donation registers print. Tested against
   `check_arabic_prose.py` first: it accepts them.

## Requests to the orchestrator (shared files — reported, not edited)

1. **`tools/check_arabic_prose.py`, `ALLOWED_WORDS` is missing five words the
   English canon uses in visible text**, and the Arabic edition is the only
   one it blocks:
   * `archaeopteryx` — the genus name in `parts/grade-9/05-evidence-of-evolution.tex`
     and its solutions twin, italicised as a Latin binomial exactly like
     *Homo sapiens*, which **is** allowed. Six sites.
   * `oil`, `painting`, `wellcome`, `collection` — the Jenner photo credit
     `Oil painting, Wellcome Collection, CC~BY~4.0.` in
     `parts/grade-9/08-immune-defenses.tex`. `CC~BY~4.0` itself passes; the
     institution name does not.

   Both were checked against the live gate before writing the chapters, per
   the instruction not to reach for a workaround silently. With no way to
   edit a shared file, the minimal reversible choice was Arabic script;
   adding the five words and reverting the six + one sites is a two-line
   change, and I would prefer it.

2. **`\setlength{\emergencystretch}{3em}` is absent** from
   `one_biology_book_1_primary_middle_school_ar.tex`, from
   `styles/onebiology.sty` and from `styles/lang/ar.tex`, although
   `../arabic_style_card.md` says it "belongs in the ENTRY file": under
   `bidi=basic` every inline `$…$` is a box, interword glue barely stretches,
   and a formula-dense Arabic paragraph can have no legal break point at all.
   This edition reached **0 overfull boxes** without it — the two it did have
   were cured by rewording, which is the better fix — so nothing is broken
   today. It is worth adding as insurance before the next Arabic book, not
   as a repair.

3. **`def:g4:breathing:organs` is structurally unreachable in Arabic**
   (2 links against English's 43), for the reason tabulated above: Arabic
   spells *lungs* as one dual noun that the harvest can only attach to one
   of the two definitions, and `wrap_file` will not link a term before its
   own chapter. Solving it needs either an ambiguity-aware `EXTRA`
   (one display, two labels, resolved by nearest-preceding) or a
   `DERIVED` that is allowed to extend an ambiguous base. Neither exists;
   both would help every language with broken plurals.

## Why not higher

* The link density is 89 % of English, not 99 %, and four targets carry
  almost all of the gap. Three of the four are pure Arabic morphology —
  broken plurals that `DERIVE = False` cannot reach and `DERIVED` cannot
  attach to an ambiguous base — and I declared 106 plural and dual
  forms across 85 bases by hand to recover what could be recovered. The fourth,
  `def:g4:breathing:organs`, is a genuine hole in the tooling.
* Sampled fragment 5 is near-native rather than native: a handful of
  aphoristic closing sentences follow the English clause order more closely
  than an Arabic textbook would, because breaking them would have cost the
  parallelism the English deliberately builds across chapters.
* Two spellings of the Jenner credit now exist in the book (Arabic in the
  chapter, Latin in the credits page) because the prose gate scans one and
  not the other. It is a one-line fix once request 1 lands, but it is in the
  shipped PDF today.
