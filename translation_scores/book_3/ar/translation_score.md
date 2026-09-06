# Translation score — Biology Book 3 · Arabic (`ar`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 3 (University Biology, Year 1) |
| **Language** | Arabic (`ar`) |
| **Quality bar** | **native academic prose** — a first-year university biology course as an Arabic-language faculty of science actually writes one. English is the source of truth for content, structure and labels. Two references were measured before drafting, not assumed: the shipped `ar` edition of **Biology Book 2** (`parts/grade-1[012]/ar/`, the volume this one continues) and the `ar` university volumes of the physics series (`parts/bachelor-*/ar/`) for exercise register |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-06 (re-synced the same day to the corrected English canon) |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 29 chapters + 29 solution twins = **58 files**, a curated `tools/term_config/book3_ar.py`, the defined-term link layer, the overfull sweep, the index sort-order question, and this score |

## Verdict in one line

An Arabic Book 3 that reads as a university biology course written in Arabic —
the vocabulary an Arabic-language science faculty uses in lecture, the
imperative-singular exercise register the shipped Arabic volumes already use,
Arabic punctuation and guillemets throughout — with every structural, build,
prose and collision gate green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 58 files against their 58 twins: **348 `exercise` / 348**, **29 `problem` / 29**, **377 `\begin{solution}` / 377**, **87 `[resume]` / 87**, **185 `omfigure` / 185**, **122 `tikzpicture` / 122**, **36 `axis` / 36**, **633 `\node` / 633**, **86 `\addplot` / 86**, **58 `\addlegendentry` / 58**, **85 `\includegraphics` / 85**, **2977 `\qty` / 2977**, **56 `\qtyrange` / 56**, **353 `\num` / 353**, **42 `\unit` / 42**, **3 `\qtylist` / 3**, **992 `\emph` / 992**, **568 `\index` / 568**, **130 `\cref` / 130**, **819 `\label` / 819**, per environment **141 `definition`, 18 `theorem`, 117 `proposition`, 33 `method`, 96 `example`, 8 `remark`, 64 `proof`**, and **725 `\textbf{N.}` weekend-problem answer numbers / 725** with the same sequence in both editions. `\label` **set** diff = **0 in both directions**. Every file was written through `tools/id_apply.py`, so every unnamed line is byte-identical to English |
| Terminology | **96** | Standard Arabic university biology, chosen for continuity with the shipped `ar` volumes: *الاستتباب*، *التغذية الراجعة السالبة*، *الجوف العام*، *النسيج الضام*، *الطبقة الدهنية المضاعفة*، *الفسيفساء المائعة*، *الكمون المائي*، *النقل المشترك*، *الرابطة الغليكوزيدية*، *الرابطة الفوسفوديإسترية*، *الحموض الدسمة*، *الألوستيرية*، *التعاونية*، *أثر بور / هالدين*، *أنهيدراز الكربونيك*، *استحداث السكر*، *مسلك البنتوز فوسفات*، *النويد*، *الالتفاف الفائق*، *شوكة التضاعف*، *قطعة أوكازاكي*، *القسيمات الطرفية*، *التقسم الخيطي*، *القلنسوة*، *ذيل عديد الأدنين*، *التشذيب*، *إطار القراءة*، *كبت الهدم*، *النمو الثنائي الطور*، *التوهين*، *التبادل بتيار معاكس*، *أكل البراز الأعوري*، *الأحماض الدهنية الطيارة → الحموض الدسمة الطيارة*، *شريط كاسباري*، *الأبوبلاست / السمبلاست*، *الضغط الجذري*، *العقيدة الجذرية*، *الميكوريزا*، *التماسك والتوتر*، *التجوّف*، *الأنبوب الغربالي*، *المصدر / المصرف*، *جدول الحياة*، *السعة الحمولية*، *التعلق بالكثافة*، *معادلة الأقراص*، *النوع المفتاح*، *الشلال الغذائي*، *الإنتاجية الأولية الصافية*، *دليل شانون*، *دين الانقراض*، *علاقة الأنواع بالمساحة*، *الصفة المشتقة المشتركة*، *المجموعة الخارجية*، *الاقتصاد*، *شبه عرقية*. **0 non-ASCII characters inside `\qty` / `\qtyrange` / `\unit` / `\num` / `\qtylist`** (machine-checked over all 58 files, because siunitx typesets those arguments in math mode) |
| Register / tone | **97** | Measured against the shipped twins before drafting. The Arabic university volumes (physics `bachelor-*/ar`) and Book 2 `ar` use the **imperative singular** for exercise stems; this edition does the same — *احسب*، *فسّر*، *اذكر*، *عرّف*، *أعطِ*، *بيّن*، *قارن*، *سمّ*، *اسرد*، *اكتب*، *ارسم*، *تنبأ*، *استنتج*، *صنّف*، *ناقش*. Audited by script: **0 plural-imperative stems** (*احسبوا*, *اذكروا*, …), **0 second-person-plural address**. Course text is impersonal lecture register |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes, `nullfont` 0** — the English baseline is also 0/0/0/0 — all measured with `grep -a`. **0 TeX accent escapes**, **0 tatweel (U+0640)**, **0 bidi control characters (U+200E/200F)**, **0 Arabic presentation forms (U+FB50–FDFF, U+FE70–FEFF)**, **0 Arabic-Indic digits** (the edition uses ASCII digits throughout, so gate 11 can read its answer numbers) |
| Cross-refs / rule compliance | **98** | `\label`, `\cref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English. No curriculum, programme or country name in visible text. `\bookline` left as given. No git commit made |
| Figures | **96** | All TikZ / pgfplots drawing code byte-identical — coordinates, styles, axis options, colours untouched; only node text, `\addlegendentry`, axis labels, `symbolic coords` and `{\small …}` captions localized. **No file used a `!draw` opt-out**: where a construct the `draw` census does not blank had to change (`\foreach` label lists in ch15/18/19, `symbolic x/y coords` with their `\addplot coordinates` names in ch1/2/6/21/23/26/29, and the book's one `(axis cs:<symbolic name>)` reference in ch23) the English text was kept inside the patch and translated in a recorded post-write edit, so the drawing census stayed fully strict for every file |
| Solutions | **97** | All 348 exercise solutions and all 29 weekend-problem solutions present and native; headers `\section*{الفصل \ref{ch:…} --- <عنوان>}` with the `ch:…` slug unchanged. Every multi-line math span reproduced with its exact internal line break, which `id_apply`'s `math` census requires byte-for-byte (a helper, `mathws.py`, re-imposed English's internal newlines after each re-flow) |
| Defined-term links (`\omterm`) | **95** | **5036 links over 186 distinct targets** against English's **5495 over 179**. 92 % density on a text that runs 10 % SHORTER than English (305 pp vs 339), which is the expected Arabic figure: `lang_ar.py` has `WORD_TAIL = ''` and `DERIVE = False`, so a broken plural is unreachable unless declared — 47 `EXTRA` keys were declared from measured occurrence counts. Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ drawing bodies. `link_defined_terms.py --check` reports **every file matches what the config generates**. Both collision censuses and the per-target display census re-run **after** the last edit |
| MT-artifact freedom | **97** | `check_orphan_lines.py` (gate 10): **0 orphan English lines**. `check_arabic_prose.py` (gate 7), all nine classes: **0 findings over 58 files** — no residual Latin in visible text, no ASCII punctuation where Arabic punctuation belongs, no Latin digits misuse, no math spacing defects, no bidi controls, no presentation forms, no tatweel, no split numbers. `\text{…}` census over course **and** solutions directories: **81 / 81**, every translatable one translated (*خارج*، *داخل*، *حفز*، *ظاهري*، *كلي*، *توازن*، *الرطوبة النسبية*، *الميل*، *الخلية*، *أساس*، *حمض*، *ماء*، *الدم*، *الخشب*، *كرة*، *ثابت*), with `ATP`, `G3P` left as international symbols |

**Overall: 96** (weighted toward terminology, register and MT-artifact freedom;
structure and build are already gated mechanically).

## Structural / build gates

Measurement note: the build log carries non-UTF-8 bytes, so a plain
`grep -c '^!'` treats it as binary, prints nothing and exits 1 — which reads
exactly like a pass. Every figure below was taken with `grep -a`.

| Gate | Result |
|------|--------|
| `latexmk -g one_biology_book_3_university_year_1_ar.tex` | exit 0 (forced `-g`; a plain build would not have recorded the newly created files) |
| `grep -ac '^!'` | **0** |
| `grep -aci 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (6 found and cleared — see below) |
| `grep -ac 'nullfont'` | **0** — same as the English build |
| `.fls` `parts/bachelor-1/` count | **60 distinct paths** = the 58 translated bodies + the two shared structure files (`part.tex`, `solutions/solutions.tex`), matching the English baseline. All **58** are the `ar/` and `solutions/ar/` files, so `\ominput` fell back to English **nowhere** |
| PDF | `build/one_biology_book_3_university_year_1_ar.pdf`, **305 pp** (EN 339 — Arabic sets ~10 % shorter, as it does in Books 1 and 2) |
| Canon re-sync | Four files mirrored after the coordinator's three corrections: `19-gene-expression` questions 14 and 20 (السؤال 11→12، السؤال 10→11); `solutions/21-gas-exchange` answer 16 (the "five times the oxygen" defect → *جزء من عشرين من الكتلة، مقابل ثلاث مئة مثل من الأكسجين* with the two figures); `27-species-interactions` l. 526 `$\alpha = 1.6$` → `$\alpha = 1.4$`, with `solutions/27` answers 1 and 2 rewritten to the new intercepts (143) and the new crossing ($N_A = -69$, outside the quadrant). Math-span parity re-verified span-by-span against the new twins in all four files; **gate 10 re-run first and separately: 0 orphan English lines**, the class the Spanish agent hit when a lengthened canon file pushed a patch range past its tail. Linker, all eleven gates and a forced build re-run afterwards |
| `bash tools/check_translation.sh bachelor-1 ar` | **PASSED** (gates 1–11), re-run after the canon re-sync |
| `python3 tools/check_problem_numbering.py parts/bachelor-1/ar` (gate 11, run separately) | **OK (29 chapters)**. The edition writes answer numbers with **ASCII digits** (725 of them), so the gate can see them; there are **0 Arabic-Indic digits** anywhere in the tree |
| `python3 tools/link_defined_terms.py --book 3 --lang ar --check` | **every file matches what the config generates** |
| `\index{}` parity | **568 / 568** |
| Engine | LuaLaTeX with babel `bidi=basic`, dispatched per source filename in `latexmkrc`. Nothing in this pass touched the font setup: the bundled Arabic faces remain **static instances**, never a variable font instanced at run time |
| Post-final sweeps, re-run **after the last edit** | tatweel **0**; bidi controls / presentation forms **0**; `\begin{proof}[…]` titles **42 شواهد + 5 برهان جزئي = 47**, matching English's 42 `[Evidence]` + 5 `[Partial proof]`; ASCII `,` `;` `?` in visible Arabic prose **0** (the only ASCII commas left are inside `symbolic coords` / `\foreach` / `xtick=`, i.e. pgfplots syntax); Arabic punctuation actually used: **6135 `،`, 1694 `؛`, 387 `؟`** |

### Overfull boxes: six found, six cleared

All five were cured by re-wording, never by a trailing `%` (which would blind
the only detector) and never by `\sloppy`:

| File | Cause | Fix |
|------|-------|-----|
| `ar/07-membranes-transport.tex` (tikz, 7.5 pt) | the two left-hand legend nodes of the five-routes figure are longer in Arabic than in English and hang past the picture's box | split each onto three lines with `\\` |
| `ar/11-nucleic-acids.tex` (14.9 pt) | two `$5'$-ATGGCATTC-$3'$` sequences are single unbreakable LTR boxes in one short paragraph | re-worded to add break opportunities around them |
| `ar/23-plant-water-minerals.tex` (12.6 pt) | `\qtyrange{0.1}{0.3}{MPa}` in a short proof paragraph | shortened the clause carrying it |
| `solutions/ar/01-organism-environment.tex` (2.3 pt) | dense run of `\qty` boxes | two connective words added |
| `solutions/ar/08-water-small-molecules.tex` (4.4 pt) | long unbroken Arabic clause | re-worded |
| `solutions/ar/13-enzymes.tex` (0.4 pt) | `و` -separated numeral list ending in a `\qty` | list re-joined with `ثم` and re-wrapped |

## Defined-term links: what the censuses found

`tools/term_config/book3_ar.py` was curated from **this edition's own harvest**
(734 candidate displays), never by translating `book3_en.py` and never by
seeding from the Book 2 Arabic twin.

**`DROP`, not `STOP`.** `harvest.py` excludes a stop-listed word from the
global `terms` table but still feeds it to the per-chapter `local` map, so a
`STOP`ped homograph is linked anyway in any chapter with exactly one candidate
definition. `DROP` is applied to `terms`, `local`, `nearest` and `primary`
alike. Every suppression below is a `DROP`.

**23 `DROP` entries.** Eleven re-check English's own cross-sense list in Arabic
(*الطاقة*, *ماء / مائي*, *بلازما*, *وعاء / الأوعية*, *البشرة / بشرة*,
*الساق / ساق*, *مُشغِّل*, *المشبع*, *الأملس / الخشن*, *الصفة*, *مقاومة*,
*ركيزة*) — and *ركيزة* is the one English merely `STOP`s, which does not work.
Four are collisions Arabic has and English does not, each measured before it
was suppressed:

* **فصل / يفصل** — "to separate/resolve" (the microscopy definition) is also
  the word for *chapter*: **«هذا الفصل» occurs 33 times**, once in every
  chapter opening and again in each solutions header.
* **معدل** — the enzyme *rate* against *معدل النمو / معدل الخطأ / معدل
  الهجوم / معدل الوفاة*: the same shape as the Indonesian agent's `laju`.
* **التعرف** — molecular *recognition* against *جسيم تعرف الإشارة* and
  ordinary recognising.
* **عرف** — a mitochondrial *crista* against the perfect of "to know".

**18 `EXTRA_PROTECT` masks**, each for a phrase where a term worth keeping is
used in its other sense; all written with `\s+`, never a literal space, because
the source wraps: `RNA\s+الناقل` / `RNA\s+ناقل` (24 occurrences of *transfer
RNA*, which is not a membrane *carrier*), `قناة\s+البنكرياس` (a duct, not an
ion channel), `الخشب\s+الميت` (dead wood, not xylem), `قصيبات\s+موازية` (a
bird's parabronchi, not xylem tracheids), `ورقة\s+معشبة` (a herbarium sheet,
not a leaf), `كابح\s+تحرره` (a brake the kidneys release, not a repressor),
`المراتب\s+أعراف` (ranks are conventions, not cristae), `قاعدة\s+العشرة`
and `قاعدة\s+عريضة` (a rule and a pyramid's broad base, not a nucleotide
base), `التغذية\s+الراجعة` (feedback, not nutrition), `المحيط\s+الهادئ` /
`المحيط\s+الحيوي` / `عرض\s+المحيط` (the Pacific, the biosphere and the open
ocean, not *environment*), `مجمع\s+مصدر` (a source pool of species, not a
phloem source), `الفجوة\s+بينهما` (a gap, not a vacuole), `كل\s+عقدة` (a tree
node, not a stem node), `(?:ال)?مقطع\s+(?:ال)?ناقل` (a conducting
cross-section, not a carrier).

**47 `EXTRA` keys.** Arabic pluralises by internal vowel change, which
`lang_ar.py`'s empty `WORD_TAIL` cannot reach, so every plural the book
actually writes has to be declared: *خلايا* (286 occurrences), *أنواع* (164),
*بروتينات* (150), *أوراق* (107), *إنزيمات* (99), *مورّثات* (75), … down to
*طفيليات* (2). Four more fix a head-word collision the census exposed: the
bare *النواة* was swallowing every *حقيقيات النواة* and *بدائيات النواة* in
the book — **92 links to the nucleus definition against English's 14** — so
*حقيقيات النواة* (36), *حقيقية النواة* (31), *بدائيات النواة* (8) and *بدائية
النواة* (4) were declared as terms of their own and the longest-match rule now
reaches the prokaryote/eukaryote definition instead. A dangling-`EXTRA` audit
(every value must be a `\label` that exists) returns **0** before and after.

**Per-target frequency census** (Arabic against English, after the last edit):
186 targets against 179, 7 English-only and 14 Arabic-only. The largest
remaining Arabic excesses were each inspected: *pH* (163 vs 89) and
*prokeuk* (101 vs 54) are correct links to correct definitions that Arabic
simply writes more often; *transporters* (75 vs 28) and *membrane* (46 vs 16)
are the declared plurals *قنوات / نواقل / أغشية* doing their job. The largest
deficits are the DROPped homographs (*organs* 291 vs 399 because *الساق* is
dropped, exactly as English drops *stem*).

**Per-target chapter-set census**: 28 targets appear in an Arabic chapter where
English does not link them; each was read and each is the plural or definite
form of the same concept, not a second sense.

**Per-target display census**: run over all 186 targets. It found the two real
defects listed under *Consistency defects found by measurement* below.

## Consistency defects found by measurement, and fixed

The per-target display census is the only thing in the pipeline that can see
these: every one of them passes `id_apply`, every prose gate and the build,
because the Arabic is correct Arabic — it is simply a *second* Arabic word for
a concept the book already named.

1. **Fatty acid had two names.** Chapters 6, 8, 9, 10, 15 and 16 use the
   definition's own term *الحموض الدسمة / حمض دسم* (40 occurrences); chapter
   22 and its solutions had *الأحماض الدهنية / حمض دهني* (17). Unified on the
   definition's term.
2. **Cytosol had two names.** Chapters 1–16 use *العصارة الخلوية*; chapters
   19, 20 and 23 had *السيتوسول*. Unified (5 sites).
3. **Endoplasmic reticulum** — chapter 19 had *الشبكة الهيولية الباطنة* /
   *الشبكة الباطنة* against the book's *الشبكة الإندوبلازمية* (2 sites).
4. **Peroxisome** — chapter 19 had *الجسيمات البيروكسية* against the book's
   *البيروكسيسومات* (1 site).
5. **Chaperone** — chapters 19 and 20 had *المرافقات* against chapter 12's
   *البروتينات المرافقة* (2 sites).
6. **Plasmodesmata** — chapters 23 and 24 had *الوصلات الهيولية* against
   chapter 6's *الروابط السيتوبلازمية* (3 sites).
7. **Gluconeogenesis** — chapters 20 and 22 had *استحداث الغلوكوز* against
   chapter 16's defined *استحداث السكر* (2 sites).
8. **Two `\qty` macros lost.** A structural census of siunitx macros (which
   `id_apply`'s `math` census does not cover, because `\qty{1000}{}` is a
   macro and not a math span) found `ar/18-replication-mitosis.tex` with
   **34 `\qty` against English's 36**: two numbers had been spelled out in
   words (*بألف*, *بخمسين*) instead of kept as `\qty{1000}{}` and
   `\qty{50}{}`. Restored. *This is a census worth adding to the shared
   toolchain — see the requests below.*
9. **Two quotation conventions in one book.** Chapters 1–18 used TeX
   `` `` … '' `` (41 pairs, which render as English curly quotes); chapters
   19–29 used Arabic guillemets « … » (37 pairs). Unified on « … » — the
   convention the shipped Book 2 `ar` uses (81 guillemets, 0 backticks);
   Book 1 `ar` uses the other one (334 backticks, 0 guillemets), so the two
   shipped Arabic volumes disagree with each other and Book 3 follows the
   nearer neighbour. **78 « / 78 »**, matching English's 78 quote pairs.

## Index sort order — the question asked, and what Arabic answered

The French agent added 164 ASCII `@` sort keys because `makeindex` sorts
byte-wise and `é` sorts after `z`, which scattered French entries. **Arabic
does not have that problem, and needs no sort keys for ordering.** UTF-8 byte
order over the Arabic block is Unicode code-point order, and Unicode's Arabic
block is laid out in the conventional alphabet: ء آ أ ؤ إ ئ ا ب ة ت ث ج ح خ د
ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ى ي. Arabic entries therefore form one
contiguous, correctly ordered block after the Latin ones (DNA, RNA, ATP, pH,
`p$K_a$`), which is where an Arabic reader expects Latin-script headwords.

Two residual imperfections were measured and deliberately **not** papered over:

* **65 of the 568 keys begin with the definite article ال** and so file under
  ا rather than under their head letter, which is the convention an Arabic
  dictionary uses. Fixing it needs 65 `@` sort keys.
* **17 keys carry a diacritic** (mostly shadda, U+0651), which sorts after ي
  and displaces the word by one letter relative to its undiacritised
  neighbours.

The edition therefore ships with **6 `@` sort keys**, all inherited from the
English canon (`pKa@p$K_a$` and its kin) — the same 6 the `nl`, `es` and `pt`
editions carry — because the two shipped Arabic volumes of this series carry
**0** hand-added sort keys and adding 65 here would make Book 3 the only
Arabic volume with a different index convention. See the requests below.

## Deliberate divergences from English

* **`\qty{}` / `\unit{}` / `\num{}` arguments hold no Arabic.** siunitx
  typesets them in math mode, where an Arabic glyph raises `nullfont` at best.
  Where English writes a bare unit inside a node the Arabic node names the
  quantity in Arabic and keeps the unit in Latin.
* **Attribution strings stay in Latin, verbatim** — photographer, painter,
  institution, repository, licence — because they are the legally required
  credit and the credits page prints them that way. The **subject** of a
  portrait is transliterated with the Latin form in parentheses on first
  mention, exactly as `frontmatter/image-credits-book3.ar.tex` does: كارل
  لينيوس (Carl Linnaeus), كارل ويزي (Carl Woese), إرنست هيكل (Ernst Haeckel).
  Scientists named in running prose (شارب وروبرتس, كريك وبرينر, نيرنبرغ
  وماتاي, جاكوب ومونو, بافلوف, غوز, باين, هولينغ, لينديمان, أودوم, مونش,
  ديكسون وجولي, شولاندر, سيمبرلوف وويلسون) are transliterated without the
  Latin, as Books 1 and 2 `ar` do.
* **Formal taxon names, gene symbols and binomials stay in Latin** —
  *Homo sapiens*, *Quercus robur*, *Paramecium aurelia*, *Pisaster*,
  *Mytilus*, *Rhizobium*, *Dryas*, kingdom *Animalia*, phylum *Chordata*,
  family *Felidae*, and the gene symbols *lacZ*, *lacY*, *lacA*, *lacI* —
  with only the rank word beside them translated. This is what the `fr`, `nl`,
  `es` and `pt` twins do.
* **No tatweel, ever.** Arabic prose habitually joins a one-letter proclitic
  to a following Latin token with a tatweel (بـ$h$, لـNADPH, الـDNA). That
  character is invisible, corrupts the term linker and is banned here, so
  every such site names the object instead: بمعامل $h$، لمركب NADPH، فجزيء
  DNA، بمقدار \qty{…}. A pre-apply grep guard rejected any patch containing
  U+0640 before `id_apply` ever ran.

## Defects found in the ENGLISH canon

**One, verified against the book's own model before claiming it.**

* `parts/bachelor-1/19-gene-expression.tex`, weekend problem
  `pb:b1:gene-expression:1`: **two internal cross-references are off by one.**
  Question 14 says "sharing the transcript's cost among the proteins of
  **question 11**", but question 11 is "how many protein molecules does one
  messenger yield per hour?" (180) while the solution's answer 14 computes
  `60 000/520`, i.e. it uses **question 12**'s number (520, the yield over the
  message's whole half-life) — which is also the only number that makes the
  physics right. Question 20 says "each yielding the number of **question
  10**", but question 10 is "how many ribosomes read one messenger at once?"
  (25) while answer 20 computes `3000/180`, i.e. **question 11**'s number.
  Both references are exactly one too low, and both become correct if Part I
  is read as having seven questions instead of eight — so the questions were
  numbered before an eighth question was added to Part I. Diagnosis: two
  stale cross-references, not two wrong answers. Reported rather than edited
  while Hindi and Indonesian were still writing against these line numbers;
  the coordinator verified it the same way, corrected English to "question
  12" and "question 11", and this edition re-synced both.
* The `solutions/21-gas-exchange.tex` answer-16 defect the coordinator
  reported ("for five times the oxygen") was translated faithfully as it
  stood, per instruction, and **re-synced** when English was corrected: the
  human moves a twentieth of the mass for three hundred times the oxygen
  (15 000 against \qty{50}{mL} an hour).
* The `27-species-interactions` weekend-problem datum the Hindi agent found
  ($\alpha = 1.6$ made the case founder-controlled, contradicting question
  2's own wording) was corrected in English to $\alpha = 1.4$ and
  **re-synced** here, question and both affected answers together.
* No permutation of answers was found in any of the 29 weekend problems. Each
  answer was read against its question while the file was being written, and
  the 29 answer runs are complete 1..k (gate 11 green, and 725 `\textbf{N.}`
  against English's 725 in the same sequence).

## Bugs found in the SHARED tooling

Three, all in `tools/check_arabic_prose.py`, all fixed in place with a comment
naming this agent and the date (the precedent is the Arabic Book 1 and Book 2
agents, who added their own `ATTRIBUTION_EXTRA` entries to the same file).

1. **A control symbol was dropped instead of spaced, gluing two words into
   one.** `visible_text()` matched only control *words* (`\\[A-Za-z@]+`) and
   skipped anything else two characters at a time, emitting nothing. The
   canon's `\num{8800} kcal\,m$^{-2}$\,yr$^{-1}$` therefore reached the
   tokeniser as **`kcalm`**, reported as residual English that no translator
   can remove without breaking the unit. Fixed: a spacing control symbol
   (`\,` `\;` `\:` `\!` `\ ` `\/`) now emits a space. **This is the class the
   `translation_instruction.md` rule names — a gate driving the translation
   instead of checking it — and it would fire in every language whose gate
   shares this function.**
2. **`makeindex` sort keys were read as visible text.** `\index{pKa@p$K_a$}`
   was reported as the English word `pKa`, though `makeindex` never prints the
   part before `@`. An edition that needed 164 sort keys (as `fr` did) would
   have been flagged 164 times. Fixed: only the printed part of each level is
   read.
3. **The siunitx family was incomplete** in `TECHNICAL_MACROS`
   (`\qtyrange`, `\qtylist`, `\numlist`, `\numrange`, `\SIrange`, `\SIlist`,
   `\unitlist` were missing), so unit strings inside them were read as prose.
   Fixed.

Two further changes to the same file are curation rather than bug fixes, and
follow the invitation in its own docstring ("only the ones the canon actually
uses — grep the English bodies again if a later book adds species"):
a structural-formula rule (`H--O--H`, `C--C`, `S--S` are formulae, not words);
Book 3's binomials, higher taxa and domain names in `ALLOWED_WORDS`
(*quercus robur*, *felis catus*, *paramecium aurelia / caudatum / bursaria*,
*bacteria*, *archaea*, *eukarya*, *opisthokonta*, *animalia*, *chordata*,
*mammalia*, *carnivora*, *felidae*, *canidae*, *reptilia*, *aves*, *alu*,
plus the gene symbols *lacZ / lacY / lacA / lacI*, *X-gal* and *PaJaMo*); the
units `cal`, `kcal`, `yr`, `ha` in `ALLOWED_UNITS`; and the attribution
strings this book's own credits page prints in Latin
(`National Cancer Institute`, `Nobel Foundation`, `Lawrence Berkeley
Laboratory`, `National Human Genome Research Institute`, `Electron Microscopy
Facility`, `Jan Verkolje`, `Alexander Roslin`, `Don Hamerman`,
`Nationalmuseum`, `Rijksmuseum`, `Micrographia`, `Kunstformen der Natur`,
`Carl Linnaeus`, `Carl Woese`, `Ernst Haeckel`, `Species Plantarum`,
`Systema Naturae`) in `ATTRIBUTION_EXTRA`.

## Requests to the orchestrator

1. **Add a siunitx-macro census to `id_apply.py`.** Its `math` census compares
   `$…$` spans, and `\qty{1000}{}` is a macro, not a math span — so a
   translator who spells a number out in words (*بألف* for `\qty{1000}{}`)
   passes every gate. This edition lost two that way and they were only found
   by a hand-written count of `\qty` per file against the English twin. A
   count of `\qty` / `\qtyrange` / `\num` / `\unit` / `\qtylist` per range,
   alongside the existing `index` count, would catch the whole class in every
   language.
2. **Add a per-target display census to the shared toolchain.** Seven of the
   nine consistency defects above are one concept with two correct Arabic
   names, and nothing in the repository can see them: `id_apply` compares a
   translation against its twin, the prose gates ask whether words are
   foreign, and the link censuses count links. Grouping every `\omterm`
   display by target and printing the ones with more than one lexical root
   found all seven in a minute.
3. **Decide the Arabic quotation convention for the series.** Book 1 `ar`
   ships 334 `` `` … '' `` pairs and 0 guillemets; Book 2 `ar` ships 81
   guillemets and 0 backticks. Book 3 followed Book 2. One of the two shipped
   volumes should be re-synced.
4. **Decide whether Arabic index entries should file under the article.** 65
   of this book's 568 keys begin with ال and therefore file under ا. Adding 65
   ASCII `@` sort keys fixes it, but would make Book 3 the only Arabic volume
   in the series that does so; the change belongs at series level, applied to
   Books 1 and 2 as well.
5. **`tools/check_translation.sh` runs gate 11 on the chapter directory
   only** (`check_problem_numbering.py --quiet "$tdir"`). The script reads the
   sibling solutions tree itself, so the result is right — but the call reads
   as if solutions were not checked. Worth a comment or an explicit second
   path.
6. ~~`solutions/21-gas-exchange.tex` answer 16~~ — done: re-synced with the
   corrected English on 2026-09-06, together with `19-gene-expression` and the
   `27-species-interactions` α datum.
