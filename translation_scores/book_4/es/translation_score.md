# One Biology Book 4 — Spanish (`es`) edition: translation score

**Date:** 2026-09-16
**Scope:** `one_biology_book_4_university_year_2_es.tex` — 27 chapters and 27
solutions files of University Biology Year 2 (`parts/bachelor-2/es`,
`parts/bachelor-2/solutions/es`), 54 files in all, plus
`frontmatter/image-credits-book4.es.tex` and the curated term configuration
`tools/term_config/book4_es.py`.
**Quality bar:** native *licenciatura / grado* prose — what a Spanish
university biology lecturer would have written for a second-year reader, not
what a careful translator would have produced from the English. English is the
source of truth for content, labels, figures, numbers and structure; native
peninsular Spanish is the source of truth for how it reads.
**Sense reference:** the Spanish Book 3 edition (`parts/bachelor-1/es`,
96/100) for register, instruction voice and house vocabulary; the French Book 4
edition was NOT used (it was being written in parallel).

## Overall: **96 / 100**

| Dimension | Weight | Score |
|---|---|---|
| Register (level band, instruction voice) | high | 97 |
| Terminology (consistency, disambiguation) | high | 96 |
| MT-artifact freedom (idiom, calques, word order) | high | 96 |
| Term links (`\omterm` density and sense) | high | 96 |
| Solutions (parity, voice, self-containment) | medium | 97 |
| Figures (TikZ node prose, captions, frozen code) | medium | 95 |
| Cross-references | medium | 99 |
| LaTeX hygiene | medium | 98 |
| Structure and fidelity | low (already gated) | 99 |

## Measured evidence

* Build (`latexmk -g`, forced, after the last prose edit and the last link
  pass): **344 pp; 0 errors, 0 undefined references, 0 overfull boxes,
  `nullfont` 0**, 0 `invalid in math mode`. English baseline: 321 pp with the
  same four zeros. `nullfont` 0 means no accent ever entered a `\qty{}`,
  `\unit{}` or `\num{}` argument.
* Underfull boxes are not gated and the English baseline is not zero: English
  147, Spanish 159 — the ordinary cost of 23 more pages of the same material.
* The `.fls` lists **54** distinct `parts/bachelor-2/…/es/` sources: every
  translated file on disk was really read, no `\IfFileExists` fell back to
  English.
* `tools/id_apply.py` accepted all **54** files, and all 54 patches were
  re-verified with `--dry-run` at the end of the run (54 ok, 0 rejected):
  labels, environments, solution keys, `\emph`/`\index` adjacency and counts,
  math spans, drawing code, image paths, delimiter counts and brace balance
  agree with the English twin by construction.
* Counts against English, whole edition: `\index` **621 = 621** (and equal
  file by file; 611 distinct keys on both sides), `\qty` **2454 = 2454**,
  `\qtyrange` 33 = 33, `\num` 175 = 175, `\emph` 997 = 997.
* `\omterm`: **3,159 links on 156 distinct targets**, against English's 3,092
  on 155. Every English target but four is reached; the four are targets
  English itself links once or twice (`prop:…:ps` "dimethyl sulfide",
  `prop:…:humus` "soil respiration", `prop:…:pulses` "receptor
  desensitisation", `thm:…:decay` "litter decays"), where the Spanish phrase
  the sentence needs is not the harvested index phrase.
  `link_defined_terms.py --check` reports "every file matches what the config
  generates", and a second `--apply` inserts 0 links.
* Both homograph censuses (per-target frequency vs the English twin, and
  per-target chapter set) were run after the last prose edit. The residue is
  five flags, each read in context and each correct: `flor` in the ch. 27
  cherry-orchard caption, `sistema nervioso autónomo` in ch. 20, `helecho
  común` in ch. 7, `unicelular` in the ch. 7 solutions, and the density flag
  on the moss definition (37 links vs English's 14 — Spanish repeats *musgo*
  where English writes "it").
* `python3 tools/check_term_display_drift.py` over both `es` directories: 66
  multi-display targets, all of them ordinary inflection (`semilla`/`semillas`,
  `capilar`/`capilares`) or the same two-display pattern English shows.
* Register census: **775** impersonal `-se` stems (`Calcúlese` 93,
  `Calcúlense` 78, `Explíquese` 40, `Enúnciese` 27, `Compárese` 10 …) and
  **zero** *usted* imperatives, matching the two earlier Spanish volumes.
* Hygiene sweeps after the last file was written: 0 line-end hyphens, 0
  line-broken `\index{}`, 0 line-initial punctuation that English does not
  also have, 0 typographic apostrophes; the `\text{…}` census (chapters **and**
  solutions) is down to Spanish abbreviations (`\text{int}`, `\text{ext}`,
  `\text{ent}`, `\text{sal}`, `\text{rep}`, `\text{cél}`, `\text{aire}`,
  `\text{alto}`, `\text{bajo}`, `\text{inest}`, `\text{acum}`) plus the
  international `ox`/`red`/`art`/`ven`/`tot`.
* A drawing sweep compared every tikz/pgfplots line still byte-identical to
  English: it caught nine node/legend strings the `show.py` view had collapsed
  (`Ca$^{2+}$ enters`, `$\sim 10^{2}$ G proteins`, `fused tetanus`, the
  species–area annotation, the Keeling decade labels …). All are translated.

## Gates

`bash tools/check_translation.sh bachelor-2 es` → gates 1–8, 10 and 11 **pass**
(completeness, label sets, exercise/solution parity, environment and figure
census, `\index`/`\qty` counts, orphan English lines **0**, problem numbering
`OK (27 chapters)`).

**Gate 9 (`check_latin_prose.py`) FAILS on six multi-word findings, and all six
are false positives** — correct Spanish that happens to be byte-identical to
English. The gate has no `"es"` key in `ALLOWED_BY_LANG`. Nothing was reworded
to get around it (per `translation_instruction.md`: "an agent reporting that it
reworded around a gate is a gate bug report"). The six:

| file:line | fragment | why it is correct |
|---|---|---|
| `es/03:516` | `\emph{Ae.~tauschii}\\DD, $2n = 14$` | species epithet |
| `es/04:331`, `es/04:334` | `\textcolor{omDef}{A\,B} \quad parental` | *parental* is the Spanish adjective |
| `es/11:59` | `proximal $\to$ distal` | both words identical in Spanish |
| `es/11:198` | `posterior $\to$ anterior` | both words identical in Spanish |
| `es/24:178` | `\begin{tabular}{c|ccc} & $B$ & $C$ & $D$ \\ \hline …` | a table of letters and numbers; the lowercase "word" the gate sees is the environment name `tabular` |

Proposed fix (in `tools/check_latin_prose.py`, which this edition must not
edit): add an `"es"` entry to `ALLOWED_BY_LANG` with
`{"parental", "proximal", "distal", "posterior", "anterior", "tauschii",
"urartu"}`, and strip `\begin{…}`/`\end{…}` environment names in
`_has_lowercase_word` (argument included, so the column spec `{c|ccc}` goes
with it) so a numeric `tabular` node can never reach either tier. **Verified
by monkey-patching those two changes into the module and re-running the gate
over both `es` directories: `no multi-word findings`, exit 0** — i.e. with
that patch `check_translation.sh bachelor-2 es` passes gates 1-11 with no
change to the translation.
The one-word (advisory) residue — 38 hits — is cognates and math labels:
`meiosis`, `mitosis`, `protonema`, `pilus`, `aorta`, `normal`, `total`,
`red`/`ox`, `art`/`ven`, `Apomixis`, `Hardy--Weinberg`.

## Samples (self-review)

1. **ch. 16, definition of blood** — "La sangre es un tejido en suspensión:
   unos \qty{5}{L} en un adulto, el \qty{7}{\%} de la masa corporal.
   Centrifugada, se separa en *plasma* … y células (\qty{45}{\%}, el
   *hematocrito*)". *Verdict: native.* The participial opening
   ("Centrifugada, se separa") is Spanish scientific prose, not a calque of
   "Spun down, it separates".
2. **ch. 22, chapter opener** — "En 1848 se capturó cerca de Mánchester una
   polilla del abedul negra… Las polillas no cambiaron: cambiaron las
   proporciones de dos alelos en una población de millones, bajo la mirada de
   las aves". *Verdict: native.* Impersonal *se* for the capture, the
   colon-contrast kept, the city name in its Spanish form.
3. **solutions ch. 21, problem q5** — "muy lejos de los \qty{1370}{N}
   necesarios. El acortamiento muscular por sí solo no puede realizar este
   salto. El contramovimiento aporta el resto: cuando el saltador se agacha,
   los tendones estirados almacenan energía elástica…". *Verdict: native and
   self-contained*: a reader who has the question can follow the answer
   without the English.
4. **ch. 26, soil horizons** — "el horizonte \emph{A}, oscuro, de suelo
   mineral mezclado con \emph{humus}, el residuo estable, oscuro y coloidal de
   la descomposición". *Verdict: native*, and the horizon letters, being
   international, are left alone.
5. **Exercise stems** — "Calcúlense el flujo hacia cada órgano y la fracción
   del gasto que recibe"; "Predígase el efecto sobre la contracción de: …".
   *Verdict: correct register* — impersonal `-se`, never *usted*, matching
   Books 2 and 3 in Spanish.

## Why not 100

* Gate 9 does not pass on this repository as it stands (six false positives,
  above). An edition that needs a tooling change before its own gate is green
  cannot claim a perfect score.
* Two Spanish homographs cost links rather than being resolved: `óvulo`
  (plant ovule / animal egg) and `ovario` (flower / mammal) are `STOP`ped, so
  they link only in the chapter that defines them; English links *ovule* in
  chapters 5 **and** 6, Spanish only in 5. `EXTRA_PROTECT` cannot separate the
  two senses, which share every collocation ("el óvulo", "del óvulo").
* Figures: five node strings had to be shortened or broken (`duración
  crítica`, the photoperiod row labels, the cross-bridge cycle captions)
  because Spanish is longer than English and the drawing geometry is frozen.
  The information is intact, but the Spanish labels are terser than the prose
  around them.
* Nine canon defects were translated faithfully rather than corrected, because
  the arithmetic lives inside frozen math spans (listed in the final report);
  four more were corrected where the wrong value sat outside math. A reader of
  the Spanish edition meets the same defects as a reader of the English one.
* 344 pp against English's 321: 7 % longer, the usual Spanish expansion, which
  moves a handful of figures away from the paragraph that introduces them.

## Deliberate divergences from the English

* **Index keys are translated** (`\index{sinapsis cromosómica}` for
  *synapsis*, distinct from `\index{sinapsis}` for *synapse*, which Spanish
  would otherwise merge into one index entry — the only such collision in the
  book).
* **Decimal commas in prose, decimal points in mathematics**: `22,8` in a
  sentence, `$0.875$` and `\qty{2.13}{GtC}` in math and siunitx, per the house
  rule that no non-ASCII and no comma may enter a `\qty{}` argument.
* **`\text{}` subscripts are Spanish** where they are words (`int`/`ext` for
  in/out, `ent`/`sal` for inflow/outflow, `rep` for rest, `cél` for cell,
  `aire`, `alto`, `bajo`, `inest`, `acum`, `cal`), international where they are
  not (`ox`, `red`, `art`, `ven`, `tot`).
* **Plant vs animal gametes**: *anterozoide* and *oosfera* for the moss and
  fern gametes, *óvulo* for the mammalian egg and the plant ovule, *células
  espermáticas* for the angiosperm sperm cells — the distinction Spanish
  botany makes and English blurs under "sperm" and "egg".
* Two numbers were corrected in place because they are unambiguous arithmetic
  errors lying outside a frozen math span: the sprinter's ATP mass
  (`\qty{80}{g}` → `\qty{800}{g}`, ch. 21) and the lake's plankton carbon
  (`4 g/m^2` → `20 g/m^2`, solutions ch. 25); "unos pocos miles de
  generaciones" became "unos pocos cientos" in ch. 23, and one solutions
  sentence in ch. 22 says "una frecuencia alélica del 5 %" where English says
  "5 % melanic". All four are listed in the final report with the English
  file:line.
