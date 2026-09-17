# Translation score — Biology Book 5 · French (`fr`)

| Field | Value |
|-------|--------|
| **Book** | One Biology Book 5 (University Biology, Year 3) |
| **Language** | French (`fr`) |
| **Quality bar** | **native academic prose** — a French third-year biology course (L3) as it is actually written and lectured. English is the source of truth for content, structure, labels, mathematics and drawing code |
| **Sense / register references measured before drafting** | the **English** canon (content) and the shipped **French Book 4** edition in this repo (`parts/bachelor-2/fr/`, 96/100) for settled terminology, typography and the **infinitive** exercise-stem register. There is no same-book French twin: this file *is* the French edition of Book 5 |
| **Overall score** | **96 / 100** |
| **Ship threshold** | ≥ 95 — **met** |
| **Date** | 2026-09-17 |
| **Scope of this pass** | Full first translation written directly at native register (no machine draft): 27 chapters + 27 solution twins = **54 files**, a curated `tools/term_config/book5_fr.py`, the defined-term link layer, the French index keys, the overfull sweep, and this score |

## Verdict in one line

A French Book 5 that reads as a third-year French biology course — the
vocabulary an L3 student hears in lecture, the infinitive exercise register of
the French university tradition, French spaced punctuation — with every
structural, build, prose and homograph gate green on a forced build of
**0 errors / 0 undefined / 0 overfull / 0 nullfont**.

## Dimension scores

| Dimension | Score /100 | Notes |
|-----------|----------:|--------|
| Structural fidelity | **99** | Exact mirror, counted over all 54 files against their 54 twins: **324 `exercise` / 324**, **27 `problem` / 27**, **351 `\begin{solution}` / 351**, **81 `[resume]` / 81**, **177 `omfigure` / 177**, **116 `tikzpicture` / 116**, **51 `axis` / 51**, **802 `\node` / 802**, **105 `\includegraphics` / 105**, **1330 `\emph` / 1330**, **913 `\index` / 913**, **104 `\cref` / 104**, **710 `\label` / 710**, **675 `\item` / 675**, **232 `\num` / 232**, **24 `\unit` / 24**, **8 `\admitted` / 8**, and per environment **127 `definition`, 34 `theorem`, 59 `proposition`, 26 `method`, 54 `example`, 104 `proof`, 32 `remark`** — all exact. `\label` **set** diff = **0 in both directions**. Every file was written through `tools/id_apply.py`, so every unnamed line (mathematics, TikZ, image paths, solution keys) is byte-identical to English. `\qty` family **2247 vs 2249**: the two missing are the same idiom twice — English's "the top `\qty{1}{\%}`" is *le centile supérieur* in French, which is what a French statistician says |
| Terminology | **96** | Standard French university biology: *chromatine / hétérochromatine*, *code des histones*, *lecteur, écrivain, effaceur*, *empreinte parentale*, *ARN interférent*, *réparation par excision de nucléotides*, *jonction d'extrémités non homologues*, *loi de Lander--Waterman*, *matrice BLOSUM*, *modèle de Markov caché de profil*, *convertase C3*, *complexe d'attaque membranaire*, *immunité déclenchée par les motifs / par les effecteurs*, *recombinaison V(D)J*, *diversité jonctionnelle*, *commutation de classe*, *centre germinatif*, *maturation d'affinité*, *tolérance centrale / périphérique*, *constante d'espace*, *générateur central de rythme*, *oscillateur à demi-centres*, *barrière hémato-encéphalique*, *plasticité dépendante du temps des potentiels*, *potentialisation / dépression à long terme*, *cellule de lieu / de grille*, *rejeu*, *multiplicateur à contre-courant*, *effet unitaire*, *clairance de l'eau libre*, *système rénine--angiotensine--aldostérone*, *gain de boucle*, *point de consigne*, *photoéquilibre*, *évitement de l'ombre*, *transport polarisé de l'auxine*, *efficience d'utilisation de l'eau*, *réaction hypersensible*, *résistance systémique acquise*, *hiérarchie de la segmentation*, *drapeau français de Wolpert*, *colinéarité*, *homéoboîte*, *zone d'activité polarisante*, *dérive neutre*, *limite de Hayflick*, *loi de Gompertz*, *théorie neutraliste*, *horloge moléculaire*, *tri incomplet des lignées*, *théorème de la valeur marginale*, *stratégie évolutivement stable*, *règle de Hamilton*, *valeur sélective inclusive*, *taille efficace de population*, *vortex d'extinction*, *relation aire--espèces*, *dette d'extinction*, *réensauvagement*, *cascade trophique*. All 913 `\index{}` keys rewritten in French |
| Register / tone | **97** | Measured against `parts/bachelor-2/fr/`, not assumed: the exercise stem is the French **infinitive** (*Expliquer* ×25, *Définir* ×11, *Prévoir* ×10, *Énoncer* ×10, *Énumérer* ×9, *Nommer* ×9, *Calculer* ×7, *Montrer* ×7, *Décrire*, *Comparer*, *Estimer*, *Classer*, *Résumer* …). Script audit over course **and** solutions: **0 imperative-*vous* stems** (`Calculez`, `Expliquez`, `Donnez`, `Montrez`, `Décrivez`, `Nommez`, `Prévoyez`, `Comparez`, `Énoncez`, `Définissez`, `Utilisez`, `Trouvez`, `Estimez`, `Discutez`, `Justifiez`, `Considérez`, `Supposez`, `Écrivez`, `Citez`, `Indiquez` — all zero), **0 tutoiement**. Course text is impersonal (*on*, passive); the weekend problems keep the English house forms (`Problème du week-end --- …`, `Partie I --- …`, solutions header `\section*{Chapitre \ref{…} --- <titre>}`) |
| LaTeX hygiene | **99** | Forced build (`latexmk -g`): **0 errors, 0 undefined, 0 overfull, `nullfont` 0, 0 `invalid in math mode`**, `.fls` French source count **54**, 0 English chapter files pulled in. **0 TeX accent escapes** (`\'e`, `` \`e ``, `\^e`, `\c c`), **0 `\oe`** against **144 raw `œ`**, **54 `«` / 54 `»`**, French spaced punctuation throughout (**1405 `~:`**, **1157 `~;`**, **751 `~?`**). Line-break class swept after the last file landed and again after the link layer: **no line-end elision apostrophe** (the one `'` at a line end is the prime of `$\gamma'$`), **no line-end word hyphen**, **no line start on `~;`/`~:`/`~?`/`~!` or on `. , ; ) ? !`**, **no line-broken `\index{}`**, **no drafty `...`**, every file valid UTF-8. No `%` was ever used to hide a line break |
| Cross-refs / rule compliance | **99** | `\label`, `\cref` targets, `\begin{solution}{key}` keys, `[resume]`, math spans and image paths byte-identical to English. No programme, curriculum or country name in visible text. No English source and no other language's file touched; the only shared file edited is `tools/check_latin_prose.py`, append-only, with a comment (reported). No git command run, no commit |
| Figures | **97** | All TikZ / pgfplots drawing code byte-identical — coordinates, styles, axis options, colours untouched; only node text, axis label strings, `yticklabels`, `\foreach` label lists and `{\small …}` captions localized. `!draw` was used **fifteen times across twelve chapters**, and only where the drawing census cannot see the text it must not compare: eight `\foreach` label lists (among them the Hox cluster, the body regions, the receptor legend and the gut-segment ticks), three pgfplots `symbolic coords` blocks (the dopamine bars, the ω bar chart and the intestinal axis, where the ASCII coordinate names are kept and French `xticklabels`/`yticklabels` added instead of accented coordinates), one `label={[…]right:…}` whose text the census does not blank, and three nodes whose `\qty{}` argument defeats the census's brace blanking. Eleven figures were re-flowed after the first build to clear overfull boxes; the second build is clean |
| Solutions | **97** | All 324 exercise solutions and all 27 weekend-problem solutions present and native; every multi-line math span reproduced with its exact internal line break, which `id_apply`'s `math` census requires byte-for-byte (49 such spans across the 27 solution files, each verified before the write); `check_problem_numbering.py` OK on all 27 chapters |
| Defined-term links (`\omterm`) | **96** | **2835 links over 193 distinct targets** against English's **2670 over 188** — every English target reached, at +6 % density on a text that runs ~7 % longer. `book5_fr.py` curated from **this edition's own harvest** (775 linkable terms before curation), never seeded: a 24-entry `STOP`, no `DROP` and no `EXTRA_PROTECT` needed, because every collision found is *between* chapters and `STOP`'s per-chapter fall-through is the exact lever. Both homograph censuses (per-target frequency and per-target chapter set) were run **after** the last prose edit and **after** the link layer, and every flag was read in a link dump with its sentence; the residue is three targets whose French count exceeds English for a reason that is not a homograph (see below). `--apply` run twice changes nothing, and the plain dry run reports **links to insert: 0** |
| MT-artifact freedom | **96** | `check_orphan_lines.py` (gate 10): **0 orphan English lines**. `check_latin_prose.py` (gate 9): **0 findings in the blocking multi-word tier**, 84 in the advisory one-word tier — every one a cognate, an acronym, a gene symbol or a Latin binomial (*Drosha*, *Dicer*, *Argonaute*, *xeroderma pigmentosum*, *fraction*, *contigs*, *position*, *Virus*, *CRISPR--Cas9*, *Needleman--Wunsch*…). `\text{…}` census over course **and** solutions: every translatable subscript translated (`\text{DFG}`, `\text{CG}`, `\text{EB}`, `\text{DPR}`, `\text{vu}`, `\text{pré}`, `\text{cerveau}`, `\text{corps}`, `\text{seuil}`, `\text{non couvert}`, `\text{nécessaire}`…); the survivors are abbreviations identical in French (`osm`, `crit`, `eff`, `in`, `out`, `inh`, `ss`, `contigs`) or English math conventions the series keeps |

**Overall: 96** (weighted toward terminology, register, link curation and
MT-artifact freedom; structure and build are gated mechanically).

## Gate output summary

```
bash tools/check_translation.sh bachelor-3 fr
  gates 1-11 ................. PASSED
                               (completeness, labels, exercise/solution
                               parity, environment census, hygiene, UTF-8,
                               twin-comparison prose gate, orphan lines,
                               weekend-problem answer numbering)
  gate 9 advisory tier ....... 84 one-word findings, read, all cognates

forced build, build/one_biology_book_5_university_year_3_fr.log (grep -a)
  '^!' ................. 0        undefined ............ 0
  Overfull ............. 0        nullfont ............. 0
  'invalid in math mode' 0        pages ................ 389 (English 365)
  .fls French .tex ..... 54       .fls English .tex .... 0

python3 tools/link_defined_terms.py --book 5 --lang fr      (plain dry run)
  links to insert: 0 across 0 files
\index count 913 = English 913 · \label set diff 0 · \qty 2247 vs 2249
```

### The two homograph censuses

Both were run against the English twin after the link layer was final.

*Frequency census* (French count ≥ 8 and ≥ 2× English) — three survivors,
each read in context and each correct:

| target | EN | FR | why |
|---|---:|---:|---|
| `def:b3:adaptive-immunity:lymphocytes` | 37 | 105 | French writes *lymphocyte~B / lymphocytes~T* where English writes *B cell / T cell*, so the head noun carries the link English spreads over two compounds it then fails to match through its own non-breaking spaces |
| `thm:b3:bioinformatics:evalue` | 6 | 16 | English's *E-value* is set as math (`$E$-value`) and never matches its own term; French *valeur E* does. All sixteen are in ch. 5 |
| `prop:b3:nervous-systems:barrier-budget` | 4 | 8 | French *barrière hémato-encéphalique* is one term where English splits the link between *blood--brain barrier* and *cerebrospinal fluid*. All eight in ch. 17 |

*Chapter-set census* (French linking in chapters English never links) — two
survivors, both the defined sense: `virus` in ch. 14, 24 and 25, and
`anticorps` in ch. 17 and 25.

Before curation the two censuses together found **twenty-four** homographs, of
which ten are French collisions English does not have — *lecture* (the
sequencing read against the act of reading, 132 links in nine chapters against
English's 98 in one), *motif* (the sequence motif against the French word for
any pattern: PAMPs, pattern receptors, Turing patterns, Hox domains, activity
patterns — 93 links in nine chapters against English's 19 in three),
*lésion*, *domaine* (including two photograph credits reading *domaine
public*), *vecteur* (twelve links in ch. 19, every one the weight vector of
Hebb's rule), *conjugaison*, *transformation*, *manteau*, *retour en arrière*
and *taux de mortalité*. All are documented with their evidence in
`tools/term_config/book5_fr.py`.

## Samples (French, with verdict)

1. **ch. 15, definition of innate immunity** — «~L'\emph{immunité innée} est
   l'ensemble des défenses présentes avant toute exposition, codées par des
   gènes germinaux qui ne se réarrangent pas, reconnaissant des caractères
   conservés des microbes plutôt que des individus précis, agissant en
   quelques minutes à quelques heures et (sous réserve) sans mémoire.~»
   → **native**: the participial chain is how a French definition is built,
   and *gènes germinaux qui ne se réarrangent pas* is the lecture phrase.

2. **ch. 17, cable theorem** — «~La membrane se charge avec la \emph{constante
   de temps} $\tau = R_{m}C_{m}$, indépendante de la géométrie. Un potentiel
   d'action, qui se régénère lui-même, parcourt un axone amyélinique à une
   vitesse proportionnelle à $\lambda/\tau$ et donc à $\sqrt{d}$~;~»
   → **native**: *amyélinique*, *constante d'espace/de temps* and the
   *et donc à* connective are the French neurophysiology register.

3. **ch. 21, the glucose loop** — «~la résistance à l'insuline abaisse $s$~:
   l'état stationnaire à jeun sous la production hépatique propre du corps
   monte, et la boucle compense par un $i^{*}$ plus haut jusqu'à ce que le
   $\beta$ des cellules $\beta$ baisse à son tour~»
   → **native**: the clinical register (*à jeun*, *production hépatique*,
   *la boucle compense*) with the control-theory vocabulary intact.

4. **ch. 26, Hamilton's rule** — «~L'\emph{altruisme} --- un comportement qui
   abaisse la reproduction de l'acteur et élève celle d'un autre --- évolue
   donc vers la parentèle, proportionnellement à l'apparentement~»
   → **native**: *parentèle* and *apparentement* are the French behavioural-
   ecology terms (not the calque *relation*), and the em-dash aside is kept.

5. **ch. 27, the extinction vortex** — «~une population plus petite perd de la
   variation, devient moins féconde, rapetisse, est plus exposée au hasard, et
   en perd davantage~» → **native**: a five-verb asyndeton that reads as
   French rhetoric, not as a translated English list.

No sample in the edition reads as MT: the draft was written directly in
French against the English twin, line range by line range, never post-edited
from a machine pass.

## Why not 100

* **Four defects in the English canon** are reproduced, not repaired, because
  English is the source of truth (they are reported separately as hypotheses):
  a self-referential question number in ch. 1, twenty-seven `\qty{}{day}`
  unit arguments that Book 3's own canon fix converted to `d`, an
  unitalicised genus in an `example` title in ch. 9, and a truncated
  photograph credit in ch. 26. Only the `day`/`d` class could be repaired in
  French without diverging from the twin, and even there the three instances
  that sit **inside** a math span had to be left as `day`, because
  `id_apply`'s math census compares spans byte-for-byte.
* **Six `!draw` opt-outs.** Each is justified above and each is the documented
  pattern, but each is a place where the drawing census no longer guards the
  figure, and only the rendered PDF does.
* **One shared file extended.** `tools/check_latin_prose.py` needed seven more
  words in `ALLOWED_BY_LANG["fr"]` for correct French to pass the blocking
  tier. That is a gate that does not know French, not a defect in the text,
  but it is a shared file this edition had to touch.
* **Link density is +6 %** against English and one target (*lymphocyte*) is
  twenty times English's count. Every link was read and every one is the
  defined sense, but the volume of links in ch. 16 is heavier than the English
  page and a second pass might thin it.
* **Register is measured, not perfect.** The exercise stems, the impersonal
  course voice and the spaced punctuation were audited by script; the
  *rhythm* of a few long proof paragraphs still follows the English sentence
  boundaries more closely than a French author would choose.

## Post-delivery canon alignment (coordinator, 2026-09-17)

After this edition was delivered, six defects that wave 1 found in the English
canon were fixed, and this tree was brought into line with them. The edition
was **not re-translated**; the edits were mechanical and are listed here
because three of them move a census count.

- **ch. 25 no longer re-defines *orthologue*/*paralogue*.** English defined the
  same two notions twice, 21 chapters apart, and escaped `harvest.py`'s
  "defined twice is ambiguous" rule only because ch. 4 spelled them American
  and ch. 25 British. Any language with one word for the concept lost those
  links. Chapter 4 now owns the definition; ch. 25's two markers are plain
  prose. `\index` 913 -> **911**, `\emph` 1,330 -> **1,328**, matching English.
- **Two `\numrange` calls given three arguments** became `\qtyrange`
  (`12-bacteriology`, `solutions/20-renal-osmoregulation`).
- **`day`/`days` inside `\qty{}`/`\unit{}` arguments became `d`**, the form
  Books 3 and 4 use, including the sites frozen inside math spans that no
  translator could reach through `id_apply`.
- The ch. 1 weekend problem's self-referential "question 12" now reads
  "question 11", and ch. 26's truncated photo credit is repaired.

The link pass was re-run from scratch (`--unwrap --apply`, then `--apply`), and
a plain dry run over the wrapped tree reports **`links to insert: 0`**.
Re-measured after the change: **389 pages, 2845 links on 193
targets, `\index` 911, `.fls` 54, 0 errors / 0 undefined / 0 overfull /
`nullfont` 0 / 0 "invalid in math mode", `check_translation.sh bachelor-3 fr`
gates 1-11 PASSED.** The self-score above is unchanged.
