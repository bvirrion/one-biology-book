"""Book 1 -- fr. Curation only; the rules live in tools/termlink/.

**This is a STUB, seeded by the coordinator. The fr agent owns it.**
Nothing here is inherited from another book: an `EXTRA` seeded from a
sibling config points at labels of THAT book and ships as undefined
references, and a seeded `EXTRA_PROTECT` masks the links you wanted. Build
each entry from this book's own harvest, in context, and diff every target's
link count against the English twin before believing a low density is "just
the language".

Young-book register, as in book1_en.py: most defined vocabulary is also
ordinary language, so a word earns a link only where it means the defined
thing in nearly all of its uses. Honest-in-its-own-chapter words go in STOP;
everyday furniture words go in DROP (their compound phrases survive as terms
of their own).

Terms are spelled as the bodies spell them: raw UTF-8, no TeX escapes.
"""

# The English default list ({"theorem", "lemma", ..., "law of", "problem"})
# suppresses exactly ONE definition display in this book -- "criterion" --
# measured over parts/grade-1..9 before this file was written. So the only
# load-bearing member of the list below is that one word, and the technical
# result-names are kept only for symmetry.
#
# Deliberately ABSENT, and do not "restore" them:
#   * the multi-word "law of" idiom. It never fires on English (Ohm's law,
#     Gauss's law) but its literal translation swallows every named law in a
#     book. It cost one edition 88 links and 5 target labels.
#   * "principle", "rule", "identity", "problem". Their translations are
#     ordinary words of this language, and NO English display in this book
#     contains any of them -- so listing them can only over-suppress.
NOT_A_TERM = ("théorème", "lemme", "inégalité", "formule", "critère", "paradoxe")

# ---------------------------------------------------------------------------
# Curated from THIS book's own French harvest (299 terms), chapter by chapter,
# against the English twin's 7,609 links. The uncurated run inserted 9,128.
#
# STOP = honest term inside its own chapter, ordinary French elsewhere (the
# harvester keeps it chapter-local). DROP = never a link anywhere; the
# compound phrases built on the word survive as terms of their own.
# ---------------------------------------------------------------------------

STOP = {
    # life-stage words: honest in the life-cycle chapters, ordinary after
    # ("l'étape suivante", "à l'âge adulte")
    "adulte", "étape", "étapes",
    # food-web equilibrium in its chapter; "en équilibre", "l'équilibre du
    # corps" everywhere else
    "équilibre",
    # the heart's beat in grade 4; "les battements du moteur" of the
    # selection chapter, "battre en retraite" elsewhere
    "battement",
    # muscle contraction in grade 3; "contracter une maladie" elsewhere
    "contracter",
    # the fair test's control in grade 4; "les témoins indépendants" of the
    # evidence chapter would otherwise all point at a plant experiment
    "témoin",
    # managed land in grade 5; "le champ de bataille", "sur le terrain"
    "champs",
    # the exercise need in grade 1; "les mouvements de la cage thoracique"
    "mouvement",
    # honest in the classification chapters, plain imperatives elsewhere
    "trier", "Trier", "classer", "Classer",
    # the plant in grade 1 AND the kinship tree in grade 6: a twice-used
    # word is never auto-linked outside its own chapter
    "arbre",
    # grade 2's subject; "de nature à", "la nature du sol" turns elsewhere
    "nature",
    # menstrual periods in grade 8; "les règles de l'usage durable" and
    # "la règle du codage" would otherwise land on the ovarian cycle
    "règles",
}

NO_CAPITAL = set()

EXTRA = {
    # French irregular plural: WORD_TAIL is (?:e?s)?, so "animaux" is
    # invisible to the deriver and 120 links of the book's commonest term
    # vanish with it.
    "animaux": "def:g1:animals-around-us:animal",
    # the grade-2 definition names the notion "milieu de vie", but French
    # school prose says "habitat" as readily as English does -- without
    # this the target keeps 10 links against the English twin's 79.
    "habitat": "def:g2:where-animals-live:habitat",
    "habitats": "def:g2:where-animals-live:habitat",
}

DROP = {
    # signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # French of the register everywhere after
    "vivant", "naît", "meurt", "mort", "morts", "nourrit", "grandit",
    "jeune", "vieux", "bébé", "enfant",
    # body furniture, exactly the four the English twin really suppresses.
    # "bras", "jambe(s)" and "membre(s)" are NOT here: measured against the
    # twin, they carry 158 of its links -- the English DROP of "arms"/"legs"
    # is a no-op, because the harvested key is the singular and the tail
    # regex matches the plural at link time.
    "tête", "cou", "bouche", "queue",
    # sense words, as in book1_en.py -- "langue" is also the language of the
    # shared genetic code, "goût" is "à son goût", "sens" is "au sens de",
    # "toucher" and "vue" are ordinary verbs. "œil"/"yeux"/"oreille" stay
    # linkable: the twin links eye/eyes/ear/ears 93 times.
    "sens", "vue", "ouïe", "toucher", "odorat", "goût",
    "nez", "langue",
    # ordinary everywhere ("de l'eau et des sels", "l'eau de la mare")
    "eau",
    # movement verbs defined for grade 1's animals
    "volent", "nagent",
    # the food chain's link AND "nomme le maillon" of the audit methods;
    # "réserves" is both the winter store and every metaphorical reserve
    "maillon", "réserves",
    # the trunk of a tree AND of the body. "branche(s)" is NOT dropped:
    # it carries 52 of the twin's 60 links on the grade-1 tree definition.
    "tronc",
    # French "paroi" is any wall -- of a vessel, of the gut, of a capillary.
    # Uncurated it took 72 links to the plant cell wall against the twin's
    # 4; the compound "paroi cellulaire" survives as a term of its own.
    "paroi",
    # vertebrate classes in grade 4, school classes in the problems
    "classes",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = [
    # "une espèce de" = "a sort of", not the biological species
    r'\bespèce\s+de\b',
    # "le milieu de la décennie/du chapitre" is not the habitat
    r'\bmilieu\s+de\s+(?:la\s+décennie|l[ae]\s+)',
    # WORD_TAIL is (?:e?s)?, so "rein" + "es" matches "reines": the queens
    # blamed for their kingdoms' daughters were being linked to the kidneys.
    r'\breines\b',
    # "se brancher sur" (the embryo plugging into the supply) is the verb,
    # not a bough of the grade-1 tree.
    r'\bbranche\s+sur\b',
]
