"""Book 2 -- fr. Curation only; the rules live in tools/termlink/.

Curated on 2026-09-05, from THIS edition's own harvest (153 terms, 220
linkable forms), never seeded from book1_fr.py.

  python3 tools/link_defined_terms.py --book 2 --lang fr --terms
  python3 tools/link_defined_terms.py --book 2 --lang fr --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang fr --apply

lang_fr.py's WORD_TAIL is (?:e?s)?, applied to EVERY word of a term, with
HEAD allowing one hyphenated prefix. What that manufactures here was checked
term by term:
  * "porteur" also matches "non-porteur" (the hyphenated head) -- correct
    sense both times -- but NOT "transporteur" (no word boundary), which is
    the collision that would have mattered: this volume is full of NAD and
    glucose "transporteurs".
  * "résistante" matches only the feminine forms, so g10's "tissu résistant"
    (tough) is out of reach; the antibiotic sense is still stopped below.
  * "entraînement" cannot reach the verb "entraîner"/"entraînée" ("la
    photosynthèse est entraînée par..."), which occurs dozens of times in
    the photosynthesis and respiration chapters.
  * irregular plurals the tail cannot make ("œil" -> "yeux", "noyau" ->
    "noyaux") are declared in EXTRA.

The English twin is tools/term_config/book2_en.py. Its DROP of "bases" does
NOT apply here: French has no "acids and bases" in this volume, every
occurrence of "bases" is "paires de bases" -- so the term is kept. Its STOP
of "eye" is likewise replaced by two protected phrases, since French "œil"
collides in exactly two idioms and is honest in the hundred other places.
"""

STOP = {
    # allele frequencies in the population chapter; the firing frequencies of
    # a muscle spindle (ch. 13) and cardiac/respiratory rates (g10) elsewhere.
    # Only the plural is harvested, but that is the form the collisions take.
    "fréquences",
    # bacteria resistant to an antibiotic in its own chapter; borers resistant
    # to a plant toxin (ch. 7) and tissues resistant to insulin (ch. 10)
    # elsewhere -- different mechanisms, same adjective. The multi-word
    # "résistance aux antibiotiques" still links.
    "résistante",
}

NO_CAPITAL = set()

EXTRA = {
    # irregular plurals: WORD_TAIL can only append -s / -es
    "yeux": "def:g11:the-eye:parts",
    "noyaux": "def:g10:cells-common-unit:organelle",
    # feminine/agreement forms of terms harvested in one gender only
    "résistantes aux antibiotiques": "prop:g11:antibiotic-resistance:mechanisms",
    # the cell-wall sense of the dropped "paroi", spelled out
    "paroi de cellulose": "def:g10:cells-common-unit:organelle",
    "paroi cellulaire": "def:g10:cells-common-unit:organelle",
    "paroi bactérienne": "def:g10:cells-common-unit:organelle",
    # singulars of terms whose definition emphasises only the plural, so the
    # harvest keyed the plural and WORD_TAIL (which can only ADD -s/-es)
    # cannot walk back to the singular the prose actually uses
    "anti-inflammatoire": "prop:g12:innate-immunity:drugs",
    "médiateur": "prop:g12:innate-immunity:inflammation",
    "tropisme": "prop:g12:plant-rooted-life:tropisms",
    "proto-oncogène": "prop:g11:cancer:genes",
    "sel minéral": "def:g10:chemistry-of-life:mineral-organic",
}

DROP = {
    # transmitted animal behaviour in one chapter; bacterial cultures on a
    # plate (g11), the crop being grown (ch. 7) and human culture (ch. 5)
    # everywhere else -- French collides harder here than English does,
    # because a cultivated plant is itself "une culture".
    "culture", "culture (animale)",
    # NOT dropped: "espèce". The first curation of this edition dropped it,
    # because the harvest sent all 165 of its links to the BIODIVERSITY
    # definition (French emphasised "espèces" in that definition's bullet
    # list) while English linked the word zero times. The canon was then
    # fixed -- the marker moved onto the Species definition itself, in both
    # editions -- and the reason evaporated: the word now points at a
    # definition OF a species, which is right everywhere. French has no
    # "une espèce de X" = "a sort of X" idiom in this volume (one occurrence
    # of "une espèce de petite taille", the biological sense), so no
    # EXTRA_PROTECT is needed either.
    # the plant/bacterial cell wall of g10 -- but French says "paroi" for the
    # wall of a blood vessel, of the gut, of an alveolus and of a bronchus
    # too, and the inflammation chapter is built on those (12 of 33 links
    # were the anatomical sense). English is safe because its term is the
    # two-word "cell wall". The unambiguous phrases are restored in EXTRA.
    "paroi",
}

EXTRA_PROTECT = [
    # "à l'œil nu" (naked eye) and "sous l'œil de" (under the watch of) are
    # idioms, not the organ of g11. Every pattern uses \s+ rather than a
    # literal space: the prose is hard-wrapped at 72 columns, and a literal
    # space silently misses the half of the sites that straddle a line break
    # (that is how "la\nparoi des vaisseaux" survived the first pass).
    r"à\s+l'œil\s+nu",
    r"L'œil\s+nu",
    r"sous\s+l'œil\s+d[eu]",
    r"un\s+œil\s+humain",
    # THE collision of this edition: "homologues" is the homology of the
    # common-ancestry chapter (organes homologues) AND the paired chromosomes
    # of meiosis -- 16 links in three chapters English never links there.
    # English protects the same pair with "homologous chromosomes/pairs".
    r"chromosomes?\s+homologues?",
    r"(?:les|des|deux|ses|leurs|aux)\s+homologues?\b",
    r"d'homologues?\b",
    r"ne\s+sont\s+pas\s+homologues?\b",
    r"sont\s+homologues?\s+du\b",
    r"\\emph\{homologues\}",
]

AMBIG_POLICY = "nearest-preceding"   # school book; matches book2_en.py
