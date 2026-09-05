# Translation score — Biology Book 1 · Indonesian (`id`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 1 (Primary & Middle School, grades 1–9) |
| **Language** | Indonesian (`id`) |
| **Quality bar** | **native school prose** (English is the source of truth for content and labels; there is no Indonesian twin of this book, so the register exemplar is the shipped `id` edition of **Physics Book 1** — same ages, same series, same exercise apparatus — and the terminology reference is ordinary Indonesian IPA/biologi usage) |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-04 |
| **Scope of this pass** | Full first translation, written directly at native register (no machine draft). 71 chapters + 71 solution twins + the two front-matter files + a curated `tools/term_config/book1_id.py`, then the defined-term link layer, then the overfull sweep, then a full re-measurement, then this score. **144 files written.** |

## Verdict in one line

An Indonesian Book 1 that reads as though it had been written in Indonesian —
for seven-year-olds in Kelas 1 and for fifteen-year-olds in Kelas 9 — with the
biology vocabulary a *SMP* pupil will meet again in the *SMA* volume, and with
every structural, build, gate and link-hygiene measurement green.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted file by file: **796 exercises EN / 796 ID**, **35 `problem` / 35**, **831 `\begin{solution}` / 831**, **142 `\admitted` / 142**, **70 `[resume]` / 70**, **99 `omfigure` / 99**, **43 `tikzpicture` / 43**, **169 `\node` / 169**, **3 `axis` / 3**, **8 `\foreach` / 8**, **71 chapters / 71**, **304 sections / 304**, **76 `\includegraphics` / 76**, **57 `\qty` / 57**. `\label` set diff, `\qty` span diff and `\includegraphics` span diff are all **byte-identical** |
| Terminology | **95** | Ordinary Indonesian school biology, chosen for continuity upward: *makhluk hidup*, *daur hidup*, *perkecambahan*, *penyerbukan*, *rantai makanan*, *pengurai*, *materi organik*, *jonjot usus*, *alveolus*, *serambi / bilik*, *penanaman*, *ari-ari*, *haid*, *neuron*, *sinapsis*, *umpan balik*, *kariotipe*, *alel*, *seleksi alam*, *flora penetap*, *patogen*, *antibodi*, *sel ingatan*. Unit symbols and all `siunitx` markup byte-identical; **0 non-ASCII characters inside `\qty` / `\unit` / `\num`**; **0 TeX accent escapes**. One real inconsistency was found by the frequency census and fixed — see *populasi* below |
| Register / tone | **96** | Measured against `../one-physics-book/parts/grade-*/id/` before drafting and again before scoring. Bare imperatives dominate the exercise stems exactly as they do there (*Sebutkan* 75, *Jelaskan* 22, *Nyatakan* 23, *Berikan* 18, *Ceritakan* 9, *Jalankan* 25) with `-lah` reserved for the softened, invitational commands (*Cobalah* 33, *Tutuplah* 22, *Bacalah* 14, *Susunlah* 13) — 115 `-lah` imperatives over 71 chapters, a leaner rate than physics's 601 over 106, and on the side the style card prefers. `kamu` address throughout, EYD spelling, decimal **point** never comma, `-nya` attached, reduplication with a bare hyphen |
| LaTeX hygiene | **99** | **0 errors, 0 undefined references, 0 overfull boxes**, `nullfont` **20** (the English baseline exactly), 0 `invalid in math mode` — all measured with `grep -a`. 329/329 balanced `` `` ``/`''` pairs, raw UTF-8 throughout |
| Cross-refs / rule compliance | **99** | `\label`, `\cref`/`\ref` targets, `\begin{solution}{key}` keys and `[resume]` options byte-identical to English. No curriculum, programme or country name anywhere in visible text |
| Figures | **96** | All TikZ / pgfplots drawing code byte-identical — coordinates, `\foreach` lists, axis options, colours untouched; only node text and `{\small …}` captions localized. Three `\foreach` visible-label lists (grades 2, 3, 4) are not blanked by `id_apply`'s `draw` census, so the English line was kept outside the patch ranges and a single targeted post-write edit applied instead — never a file-wide `!draw` opt-out |
| Solutions | **97** | All 796 exercise solutions and all 35 weekend-problem solutions present and native; headers `\section*{Bab \ref{ch:…} --- <judul>}` with the `ch:…` slug unchanged. Open-answer models rewritten as Indonesian, not glossed (the closing line of the book — ``Siput itu dan kamu dibangun oleh empat huruf yang sama: jagalah seluruh keluarganya.'') |
| Defined-term links (`\omterm`) | **95** | **8 390 links over 151 distinct targets**, against English's **7 608 over 151** — 110.3 % density on the *same target set* but for two ≤ 7-link divergences (below). Zero links inside `\qty` / `\unit` / `\num` / math / `\label` / solution keys / TikZ bodies / titles |
| MT-artifact freedom | **95** | `check_indonesian_prose.py`: **silent across all 142 files**. `check_latin_prose.py`: **0 findings across 142 files** (both tiers). `check_orphan_lines.py`: **0 orphan English lines**. `\text{…}` census over course **and** solutions: 4 of 4 translated (*rumput*, *belalang*, *kadal*, *elang*) |

**Overall: 96** (weighted toward terminology + register + MT-artifact freedom; structure is already gated mechanically).

## Structural / build gates

Measurement note: pdfTeX writes `build/*.log` as ISO-8859 text, so a plain
`grep -c '^!'` treats the file as binary, prints nothing and exits 1 — which
reads exactly like a pass. Every figure below was taken with `grep -a`.

| Gate | Result |
|------|--------|
| `latexmk -g one_biology_book_1_primary_middle_school_id.tex` | exit 0 |
| `grep -ac '^!'` | **0** |
| `grep -ac 'undefined'` | **0** |
| `grep -ac 'Overfull'` | **0** (two found and fixed — see below) |
| `grep -ac 'nullfont'` | **20** — the English baseline; a rise would be the accent-inside-`\qty` failure |
| `grep -ac 'invalid in math mode'` | **0** |
| `.fls` translated-file count | **142** — every one of the 71 chapters and 71 solution twins really compiled (a failed `\IfFileExists` records nothing and ships English bodies inside a green log) |
| PDF | `build/one_biology_book_1_primary_middle_school_id.pdf`, **467 pp** (EN 422 — Indonesian runs ~11 % longer, chiefly because it spells possession with the enclitic *-nya* where English uses a bare noun) |
| `tools/check_translation.sh grade-N id` | gates 1–10 **PASSED × 9** |
| Line-end sweep, re-run **after the last file landed** | `['’]\s*$` → **0**; `[a-zà-ÿ]-\s*$` → **0** (so no reduplication is split across a line break — the failure mode that would silently break the term linker); `^\s*([.,;:)?!]|~[;:?!])` → 9, **all of them TikZ Bézier `..` continuations, and English has the identical 9**; trailing `%` → **0**. **No line was ever "fixed" with a trailing `%`** |
| `\index{}` key-set diff | **331 entries in both editions.** 301 distinct id keys against 303 en — two English pairs collapse because Indonesian has one word for both members. The **11** keys spelled identically to English (*DNA*, *alveolus*, *antigen*, *diabetes*, *habitat*, *humus*, *neuron*, *penis*, *urea*, *urine*, *virus*) are all genuine Indonesian forms, not survivals; **0 untranslated English index entries** |

The two overfull boxes:

* `frontmatter/image-credits.id.tex` — an unbreakable `\texttt{images/book1/CREDITS.md}`.
  English keeps a two-letter word (*in*) in front of it; the Indonesian first
  draft had a long one. Cured by ending the line on the two-letter *di*, i.e.
  by **shortening the word before the break point**, which is the fixed-width-box
  cure, not the prose one.
* `parts/grade-6/id/09-cell-unit-of-life.tex` — the two side-by-side cell
  minipages, 3.38 pt. Isolated by probing the chapter alone into the book's own
  preamble and shortening one overlay label at a time: the culprit was
  `dinding sel` at *x* = 0.08 of the image, overhanging the minipage on the
  left (English's `cell wall` is two characters shorter). The **coordinates were
  left untouched**; only the node text changed, to `dinding` — which the caption
  immediately below already glosses, exactly as English's caption glosses
  *cell wall* as *plus wall*.

## Defined-term links — what the curation actually needed

The uncurated harvest inserted **10 829** links, **42 % more than English
carries on the same text**. Nearly every cause is one fact about Indonesian:
**the language marks no number**, so a word English harvests only in the
plural — or only in the singular — is reached by *every* mention here. That
cuts both ways, and each direction had to be re-taken rather than translated
out of `book1_en.py`:

| Cause | Effect | Cure |
|-------|--------|------|
| **`makan` / `tumbuh`** — the book's two commonest verbs, defined gently in grade 1 | **400** links onto `prop:g1:living-or-not:signs`, which English does not link at all | `DROP` |
| **`hidup`** = *alive*, *living*, and the ordinary verb *to live* | 214 of the 326 links on the grade-1 living-things definition | `DROP`; *makhluk hidup* survives |
| **`air`** = water, in *air minum*, *air liur*, *air kapur*, and every ordinary sentence | **298** links onto a target English links **3** times | `DROP`; the compounds survive as terms of their own |
| **`tahap` / `mati` / `tua` / `muda` / `lahir` / `kematian`** | 370 links onto the grade-2 life-cycle definition against English's 65 | `DROP` (`kelahiran`, `daur hidup` survive) |
| **`anak` / `bayi`** = child, baby, *and* the young of any animal | 321 of the 408 links on the stages-of-life definition | `DROP` |
| **`indra`, `penglihatan`, `pendengaran`, `penciuman`, `pengecapan`, `perabaan`, `hidung`, `lidah`** | mirror of the English sense-word `DROP` | `DROP` |
| **`cadangan`** = the winter food store *and* any reserve (of oxygen, of a species) | 45 links onto a 15-link target | `DROP`; *cadangan makanan* survives |
| **`mata rantai`** = a chain's link, *and* the linker's own noise word | see the collision table — this one was **wrong**, not merely noisy | `DROP` + `EXTRA_PROTECT` |
| `dewasa`, `tahap`, `keseimbangan`, `kontrol`, `hutan`, `ladang`, `gerak`, `mengelompokkan`, `mengklasifikasikan`, `pemilahan`, `pohon`, `alam` | the same collisions `book1_en.py` already names, in their Indonesian forms | `STOP` (chapter-local) |

Two of English's `DROP` decisions had to be **refused**, and refusing them is
worth 200 links:

* **`mata` / `telinga`.** English drops *eyes*/*ears* but keeps the singulars
  *eye*/*ear*, which carry **93** of that target's 215 links. Indonesian has one
  form each; dropping them would have cost every one.
* **`lengan` / `tungkai`.** Same shape: English's `DROP` of *arms*/*legs* leaves
  *arm*, *leg*, *limb*, *limbs* linking **148** of 158 times. Restoring the two
  Indonesian singulars recovered 72 links.
* Conversely **`sisik`** (fish scale) and **`lembaga`** (the germ of a seed) are
  kept, where English must drop *scale*/*scales* and *germ*: Indonesian says
  *skala* for the measure and *kuman* for the microbe, so neither collides.

## Homograph collisions found and fixed

The frequency diff and the chapter-set diff were run **both ways** and again
**after** the overfull sweep, precisely because the frequency test goes blind
when a wrong sense lands on a heavily-linked target — the chapter-set test is
what caught most of these. Seventeen collision classes surfaced. Measured
directly (relink with `EXTRA_PROTECT` emptied, then restored): the protections
alone suppress **151 wrong links**; six more sites were reworded in the source,
and one terminology inconsistency restored 26 links that were missing.

Indonesian's dominant collision shape is not English's: compounds are written
**open**, so a two-word compound whose head is a defined term fires on the head.
English gets these for free from word boundaries (*milkmaid*, *eyebrow*); here
every one had to be named.

| Collision | Literally | Wrongly linked to | Sites | Cure |
|-----------|-----------|-------------------|------:|------|
| **`mata rantai`** | *eye of chain* = a link of a food chain | the grade-1 **sense organ** | **59** | `EXTRA_PROTECT` (the single largest wrong-sense class in this edition) |
| `batang tubuh` | *stalk of body* = torso | the plant **stem** | 12 | `EXTRA_PROTECT` |
| `suasana hati` | *atmosphere of liver* = mood | the **liver** | 11 | `EXTRA_PROTECT` |
| `batang kayu / rokok / kapur / rambut` | rod, cigarette, chalk stick, hair shaft — *batang* is also the counter word for long thin things | the plant **stem** | 11 | `EXTRA_PROTECT` |
| `buah zakar` | *fruit of the scrotum* = testis | **fruit** | 10 | `EXTRA_PROTECT` |
| `kulit kayu` | *skin of wood* = bark | the **skin**/sense organ | 10 | `EXTRA_PROTECT` |
| `kuning telur` | *yellow of egg* = yolk | the grade-2 **egg** | 7 | `EXTRA_PROTECT` |
| `kulit sayuran / wortel / pelindung / sebutir biji` | peel, seed coat | the **skin** | 6 | reworded to *kulit biji* + `EXTRA_PROTECT` |
| `keruh seperti susu` | *cloudy like milk* = milky limewater | the grade-2 **milk** | 5 | `EXTRA_PROTECT` (English guards the same pair with `\bmilk-white\b`) |
| `kaki seribu` | *thousand feet* = millipede | the grade-1 **limb** | 3 | `EXTRA_PROTECT` |
| `Batang-batang kaku`, `satu batang yang kaku`, `memotong batangnya` | rigid rods; a puppet's stick | the plant **stem** | 3 | reworded to *tiang* / *tongkat* |
| `mata uang` | *eye of money* = currency | the **eye** | 2 | `EXTRA_PROTECT` |
| `pemerah susu` | milkmaid | the **milk** | 1 | `EXTRA_PROTECT` |
| `kulit mentah` | *raw skin* = hide | the **skin** | 1 | reworded + `EXTRA_PROTECT` |
| `kulit` of a ripening cheese | rind | the **skin** | 1 | reworded to *kerak* |
| `tanah pembiakannya` | *soil of its breeding* = breeding ground | the grade-6 **soil** | 1 | reworded to *lahan* |
| `bahasa batangnya` | the trunk of the family tree | the plant **stem** | 1 | reworded to *batang pokok* |

### And one terminology inconsistency, caught only by the frequency census

`def:g8:reproduction-and-environment:population` carried **3** links against
English's **29**. The cause was mine: I had translated *population* as
**`populasi`** where grade 8 defines it and as **`penduduk`** through the whole
of grade 9 — a word that in Indonesian means the *inhabitants of a place*, not
a biological population. Eight files were corrected with a
`\bpenduduk(nya)?\b` rewrite (guarded against *pendudukan*, "occupation",
which is a different word and correct where it stands), restoring 26 links and,
more importantly, making the book say one thing.

### Two under-links repaired at source, not in the config

* **`prop:g2:from-seed-to-plant:cycle`** (EN 20, ID 2). The definition opened
  `\emph{Kecambah}\index{kecambah}` — capitalised, so only the capitalised
  display was harvested and every later lowercase *kecambah* went unlinked.
  Rewritten as `Sebuah \emph{kecambah}\index{kecambah} …`. This is the failure
  the brief warned about, and the census is the only thing that sees it.
* **`def:g1:healthy-habits:hygiene`** (EN 6, ID 0). The Indonesian text said
  *kebersihan* where it should have said the defined *kebersihan diri*; four of
  the six sites were rewritten.

### The two remaining target-set divergences

* `prop:g3:bones-and-muscles:joints` (EN 6, ID 0) and
  `rem:g7:removing-wastes:sweat` (EN 1, ID 0) — both are English
  singular/plural splits. English harvests *joint* at grade 1 and *joints* at
  grade 3 and routes each separately; Indonesian *sendi* is one word, so
  nearest-preceding sends all of them to the grade-1 definition. The links
  exist and are correct; only the granularity differs.
* `def:g2:animals-grow-up:direct` (ID 2, EN 0) and
  `prop:g6:decomposers-and-soil:decomposition` (ID 7, EN 0) — Indonesian
  *penguraian* and *tiruan kecil induk* are harvested as displays where the
  English config suppresses theirs. The sense is correct at all nine sites.

## Sampled fragments, judged

| # | Fragment | Verdict |
|---|----------|---------|
| 1 | *(g1-01)* ``Seekor siput merayap pelan di jalan setapak yang basah. Di sebelahnya tergeletak sebutir kerikil kelabu, sama kecilnya, sama bulatnya. Siput dan kerikil itu berada di bawah hujan yang sama --- namun yang satu hidup dan yang lain tidak.'' | **native** — *sebutir*, *tergeletak* and the *sama …-nya, sama …-nya* parallel are Indonesian moves with no English source token |
| 2 | *(g8-07)* ``Listrik di sepanjang kabelnya, kimia di setiap simpangnya: seluruh sistemnya menyelang-nyelingkan keduanya.'' | **native** — the reduplicated verb *menyelang-nyelingkan* is the natural rendering of *alternates the two*, and carries the English gerund pair as two bare nominals |
| 3 | *(g9-06)* ``Jerapah tidak memanjangkan lehernya dengan meregang --- ragam yang berleher lebih panjanglah yang makan dan berbiak lebih baik daripada yang pendek.'' | **native** — the focus enclitic *-lah* on *panjanglah* is exactly how Indonesian retires Lamarck, and has no English counterpart |
| 4 | *(g9-02, solutions)* ``Deretannya terasa bermakna; mekanismenya tidak menyimpan ingatan.'' | **native** — two clauses, one semicolon, no copula; the English *the run feels meaningful; the mechanism keeps no memory* would be flabby if rendered word for word |
| 5 | *(g5-08)* ``Kecanduan adalah perangkap dengan pintu masuk yang mudah dan pintu keluar yang sulit: memulai adalah satu pilihan, berhenti adalah pertarungan yang diulang bertahun-tahun.'' | **near-native** — faithful and idiomatic, but English's *easy entrance, hard exit* is tighter than any Indonesian rendering I found; the two *yang* relatives are the price of the language |

No fragment in the sample reads as machine translation.

## Shared-file findings (reported, never edited)

Four gate defects were reported to the coordinator during this run rather than
worked around, and all four were fixed in the shared tools:

1. **`tools/check_latin_prose.py`** failed every Latin-script edition on the 18
   overlay-label figures, whose `\includegraphics` path `id_apply`'s `img`
   census *requires* to stay byte-identical: `_has_lowercase_word()` did not
   strip it, and `main()` returned non-zero for the low-confidence one-word
   tier against its own docstring. Both fixed; this edition now reports 0
   findings over 142 files.
2. **`tools/check_indonesian_prose.py`** rejected `Wellcome Collection,
   CC~BY~4.0.` — the Wellcome image's licence attribution, which the French
   edition rightly keeps verbatim and which has no translatable form. Fixed
   with an `ATTRIBUTION` blank; the Jenner credit now ships verbatim.
3. The same gate read the standard EYD decade suffix `1840-an` as the English
   article *an*, and
4. read the eponym in `sindrom Down` as the preposition *down*. Both fixed;
   both forms are restored in the text.

## Why not 100

* **Density is 110 % of English, not 100 %.** The residue is one structural
  fact and one prose fact. Structural: `prop:g3:sorting-living-things:groups`
  carries **461** links against English's **182**, because English harvests only
  the plurals (*fish*, *birds*, *insects*, *mammals*) and leaves every singular
  mention unlinked, while Indonesian *ikan*, *burung*, *serangga*, *mamalia*
  have one form that matches everywhere. Every one of those links points at the
  right definition — it is noise, not error — but I could not remove it without
  `STOP`ping the four group words into their own chapter and falling far *below*
  English. Prose: `def:g6:exploring-our-environment:conditions` (221 vs 176) and
  `def:g2:from-seed-to-plant:seed` (237 vs 108) are the same effect on
  *kondisi*/*cahaya* and *biji*.
* **`def:g8:nervous-communication:synapse` runs 19 against English's 36**, and
  `def:g1:my-body:parts` 116 against 158. Both are honest prose choices — I
  wrote *simpang* for *junction* where English repeats *synapse* — but they are
  choices, not parity.
* **`tulang belakang` cannot split the way English's *spine*/*backbone* does.**
  Indonesian has one word, so the ~8 grade-5-and-later mentions that English
  routes to the skeleton definition go to the grade-4 vertebrate criterion
  instead. Correct sense, coarser granularity; left rather than reworded around
  the linker.
* **The enclitic *-nya* is this edition's one stylistic tic.** Indonesian marks
  definiteness where English uses a bare noun, so long expository chains
  (*permesinannya*, *penahannya*, *pembukuannya*) accumulate. I pruned them
  where a sentence could carry a demonstrative instead, but a native editor
  would still thin a handful further.
