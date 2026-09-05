"""Book 2 -- es. Curation only; the rules live in tools/termlink/.

Curated on 2026-09-05 from THIS edition's own harvest (153 terms, 219
linkable spellings), term by term, never seeded from book1_es.py. The
English twin, tools/term_config/book2_en.py, was read for the SENSE
collisions of the volume, not transposed: three of its five collisions
(culture, carrier, bases) simply do not exist in Spanish, and Spanish has
two the English canon never had.

  python3 tools/link_defined_terms.py --book 2 --lang es --terms
  python3 tools/link_defined_terms.py --book 2 --lang es --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang es --apply

Facts about the engine that drove the choices below:

  * lang_es.py sets WORD_TAIL `(?:e?s)?` with TAIL_ON_EVERY_WORD, so every
    word of a phrase may gain "s" or "es". It BUILDS plurals and never
    strips them, and it never rewrites an accent: "cáncer" reaches
    "cánceres" but "población" only reaches "poblaciónes", which is not a
    Spanish word. Every -ción/-ón term therefore needs its real plural in
    EXTRA, and DROPping a plural while keeping its singular changes nothing.
  * Spanish inflects adjectives for gender; the harvest only ever sees the
    form the definition happened to use ("recesivo", "portador",
    "autótrofa"). The missing gender goes in EXTRA.
  * a display carrying a parenthesis ("base (ADN)", "cono (retina)",
    "cultura (animal)") can never match running prose, so listing one in
    DROP is a no-op. They are left alone; the bare spelling is what has to
    be dropped.
  * STOP is applied before derivation and is easy to get wrong, so nothing
    below relies on it: every suppression here is a DROP of a harvested key
    or an EXTRA_PROTECT regex, both of which were verified by diffing the
    per-target link counts against the English twin.

Terms are spelled as the bodies spell them: raw UTF-8, no TeX escapes.
"""

STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # -- real plurals the accent rule puts out of WORD_TAIL's reach.
    # "población" -> "poblaciónes" is not a word, so 58 occurrences of the
    # population of the selection/drift chapter went unlinked; likewise the
    # 83 "mutaciones", which English links through its regular plural.
    "poblaciones": "def:g12:selection-drift-speciation:population",
    "mutaciones": "def:g11:mutations:mutation",
    "articulaciones": "def:g10:muscles-and-joints:joint",
    "tendones": "def:g10:muscles-and-joints:muscle",
    # the harvest saw only the plural of the definition display; every
    # later mention is singular ("un antiinflamatorio", "el tratamiento
    # antiinflamatorio"), so the target lost the two links the English
    # canon gives it.
    "antiinflamatorio": "prop:g12:innate-immunity:drugs",
    # -- the other gender. English has one form for each of these.
    "recesiva": "def:g11:genes-and-disease:genetic",
    "portadora": "def:g11:genes-and-disease:genetic",
    "autótrofo": "def:g10:cell-metabolism:autotrophy",
    "heterótrofo": "def:g10:cell-metabolism:autotrophy",
}

DROP = {
    # The English collision, and the same one here: "cultura" is the
    # transmitted behaviour of the diversification chapter, but it is also
    # human culture in the human-evolution and hormones chapters (6 of its
    # 10 uses). Unlike English, Spanish does NOT also carry the bacterial
    # or agricultural sense on this word -- that is "cultivo" -- so the
    # parenthesised display "cultura (animal)" is left to print the index
    # entry, and only the bare spelling is dropped.
    "cultura",
    # A collision Spanish has and English does not. English writes
    # "homologous chromosomes" and can protect that phrase; Spanish uses
    # "los homólogos" as a bare NOUN throughout meiosis and polyploidy --
    # 24 of the 28 occurrences of the word are the meiosis homologue, not
    # the homology of the common-ancestry chapter. Dropping the adjective
    # costs 8 same-chapter links and prevents 24 wrong ones; "homología"
    # keeps the sense linked where it is meant.
    "homólogos",
}

# -- especie / especies: DROPPED on 2026-09-05, RESTORED the same day.
#
# The first curation dropped "especies" because both editions marked
# "\emph{species}" inside the BIODIVERSITY definition as well as in the
# SPECIES definition just after it. English spelled the two the same, so its
# harvest saw one term defined twice and dropped it -- `--lang en` linked
# "species" zero times -- while Spanish spelled them "especies" and
# "especie", kept both, and pointed 170 links from the commonest noun in the
# volume at a definition of BIODIVERSITY, which is not what the word means.
#
# The canon has since been fixed: the marker moved off the Biodiversity
# bullet onto the Species definition itself, in English and in the Spanish
# body alike. There is now exactly one "especie" term and it points at
# `def:g10:biodiversity-scales:species`, which is the definition those 170
# links were reaching for, so the DROP is gone and nothing replaces it.
#
# Before restoring, every occurrence of "especie de" was censused for the
# ordinary Spanish "a sort of / a kind of" idiom, which English's "species"
# cannot produce and which would have needed EXTRA_PROTECT. There are two in
# the volume and BOTH are taxonomic: "el ciclo de toda especie de
# reproducción sexual" (g12/01) and "una especie de cuerpo pequeño en una
# isla" (g12/05) -- English links `species` at both twins. So Spanish has no
# independent homograph here and needs no protection.
#
# WORD_TAIL derives the plural for free: the harvest key is the singular
# "especie" and "(?:e?s)?" reaches "especies", so no EXTRA is needed either.

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across
# a source line break must still be protected. Each pattern below was found
# by a per-word frequency census of the whole edition, not guessed.
EXTRA_PROTECT = [
    # "aumento" is the microscope's magnification in 15 of its 17 uses; the
    # other two are the ordinary Spanish noun for an increase.
    r'\bfactor\s+medio\s+de\s+aumento\b',
    r'\baumento\s+de\s+\d',
    # "resistente" is antibiotic/toxin resistance everywhere except three
    # places where it is the ordinary adjective for tough: the tough stalk
    # of the first cultivated wheats and the tough tissue of a ligament.
    r'\b(?:tallos?|tejidos?)\s+resistentes?\b',
    # "frecuencias" is the allele frequency of the population chapter in 26
    # of 27 uses; the odd one is the firing rate of a muscle spindle.
    r'\bfrecuencias\s+más\s+altas\b',
    # "un ojo humano en lugar del ambiente": the selecting eye of the
    # domestication chapter, not the organ of the eye chapter.
    r'\bun\s+ojo\s+humano\b',
    # "la portadora del rasgo heredable" is the DNA carrying the trait, not
    # the heterozygous carrier of a recessive allele.
    r'\bla\s+portadora\s+del\s+rasgo\b',
    # "los portadores de cepas resistentes" of the hospital-hygiene section
    # are people carrying an INFECTION, not heterozygotes carrying an
    # allele; English writes "carriers" in the same three places and links
    # none of them, because book2_en.py DROPs the word outright.
    r'\bportadores?\s+de\s+cepas\b',
    r'\bdesde\s+los\s+portadores\b',
    # "el folículo dominante" of the ovarian cycle: the ordinary adjective,
    # not the dominant allele.
    r'\bfolículos?\s+dominantes?\b',
    # "las bases de cráneo" of the fossil skulls, not the bases of DNA.
    r'\bbases?\s+de\s+cráneo\b',
]

AMBIG_POLICY = "nearest-preceding"   # school book; matches book2_en.py
