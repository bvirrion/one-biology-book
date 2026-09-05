"""Book 1 -- nl. Curation only; the rules live in tools/termlink/.

Curated from this book's own Dutch harvest, in context; nothing here is
inherited from a sibling config (a seeded EXTRA points at another book's
labels and ships as undefined references, a seeded EXTRA_PROTECT masks the
links you wanted).

Young-book register, as in book1_en.py: most defined vocabulary is also
ordinary Dutch, so a word earns a link only where it means the defined
thing in nearly all of its uses. Honest-in-its-own-chapter words go in
STOP; everyday furniture words go in DROP (their compound phrases survive
as terms of their own).

Dutch adds a defect class English does not have: the language welds
compounds, so the ordinary word and the technical word are often the SAME
string ("kiezen" = molars and "to choose"; "opgelost" = dissolved and
solved; "stam" = trunk and virus strain; "trekken" = migrating and
pulling; "proeven" = tasting and experiments). Those are homograph
collisions, not translation errors, and only DROP/STOP can see them.

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
NOT_A_TERM = ("stelling", "lemma", "ongelijkheid", "formule", "criterium",
              "paradox")

STOP = {
    # honest stage-words in their own chapters, ordinary Dutch elsewhere
    "volwassen", "volwassene", "stadium", "stadia",
    # food-web balance in its chapter; body balance and "in evenwicht"
    # everywhere else
    "evenwicht",
    # the experiment's control in its chapters; "controle" is also the
    # check-up of the health chapters and the "controlecentrum" of the brain
    "controle",
    # the plant in its chapter; but "de boom" is also the kinship tree, and
    # "de takken van de boom" runs through grades 6 and 9
    "boom",
    # the g2 chapter's subject; "de natuur" is ordinary everywhere after
    "natuur",
    # soil in the plant chapters; "de aarde" is the planet in grade 9 and
    # "op aarde" is ordinary
    "aarde",
    # soil in its chapter; "de bodem raken" (hit bottom) elsewhere
    "bodem",
    # the healing/recovery sense in its chapter; "herstel" is ordinary prose
    "herstel",
    # the plant's light need in its chapter; "licht" is also the adjective
    # (the moths' "lichte vorm", "licht haar")
    "licht",
}

NO_CAPITAL = set()

# Manual entries for targets harvest.py cannot see. Dutch welds compounds,
# and the index-only harvest path skips any \index entry without a space --
# so a welded Dutch key ("voedselketen") reaches the harvester only through
# its \emph{...}\index{...} pair. Everything below was found by a comm of
# the nl target set against the English one, never by eye.
EXTRA = {
    # Dutch welds compounds, so the plural the prose actually uses is a
    # different string from the \index key, and harvest.py never sees it.
    # Found by a comm of the nl target set against English's, not by eye.
    "witte bloedcellen": "def:g9:immune-defenses:standing",
    # "geslachtscel(len)" is the ordinary Dutch name of a gamete; the book
    # uses it alongside "gameet". English links both through one word.
    "geslachtscellen": "def:g8:sexual-reproduction:gametes",
    "geslachtscel": "def:g8:sexual-reproduction:gametes",
}

DROP = {
    # --- signs-of-life vocabulary: gentle definitions in grades 1-2, and
    #     ordinary words of the register in every grade after
    "leven", "leeft", "eet", "groeit", "jong", "oud", "kind", "dood",
    # ... and the two Dutch multi-word forms of the same idea, which have
    # no English counterpart because English DROPs "born" and "dies"
    "gaat dood", "geboren worden",
    # --- body furniture whose Dutch string is genuinely ambiguous
    "kop",      # animal's head / newspaper headline, "de kop van een lijst"
    "enkel",    # ankle / "enkel" as the adverb "only"
    # --- sense VERBS: the nouns stay linked, the verbs are ordinary Dutch
    "zien", "horen", "voelen", "ruiken", "proeven",
    # --- ordinary everywhere ("voedsel en water", "de zuurstof van het
    #     water")
    "water",
    # --- the grade-1 movement verbs; both are ordinary verbs after
    "vliegen", "zwemmen",
    # --- homograph collisions: the technical word and an ordinary Dutch
    #     word are the SAME string, so the link lands on the wrong sense.
    #     Each of these was caught by the per-target frequency census
    #     against the English twin, never by reading.
    "kies", "kiezen",        # molars / "to choose" (imperative in every stem)
    "opgelost",              # dissolved / solved ("het raadsel opgelost")
    "stam",                  # tree trunk / virus strain (grade 9 uses both)
    "trekken",               # migrating / pulling ("uit elkaar getrokken")
    "sporen",                # fern spores / tracks, traces, "op te sporen"
    "leveren",               # a bad plural of "lever" (liver): it is the
                             # verb "to supply", and it linked 15 times
    "sorteren", "indelen",   # the classification verbs / plain imperatives
    "schakel",               # food-chain link / any "schakel" in an argument
    "voorraden",             # the stores of a plant / any stock
    "beweging",              # the exercise need / "de beweging van de borst"
    "klassen",               # vertebrate classes / school classes
    "takken", "tak",         # of a tree AND of the kinship tree
    # --- \index{sterfte} is ordinary prose everywhere it appears
    "sterfte",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = [
    # "de aard van ..." is character, never the g2 environment sense
    r'\bde\s+aard\s+van\b',
    # the potato's / needle's eye, not the sense organ
    r'\bo(?:og|gen)\s+van\s+(?:een|de)\b',
    # "melkwit" limewater is not milk; boundaries handle it, this guards
    # against rewrites
    r'\bmelkwit\b',
    # --- the two homographs the Dutch plural rule manufactures. lang_nl's
    # WORD_TAIL is (?:e?[ns])?, so the TERM "lever" also matches "leveren"
    # and the TERM "spore" also matches "sporen". DROPping the plural does
    # nothing (it is not a term key) and DROPping the base would throw away
    # the 21 correct "lever" and 24 correct "spore(n)" links -- so the wrong
    # SENSES are masked here instead, phrase by phrase. Found by the
    # per-target frequency census against the English twin.
    #
    # "leveren" is the verb "to supply", never the liver: all 15 uses.
    r'\bleveren\b',
    # "eis" is a demand, never an egg: the Dutch plural of "ei" is
    # "eieren", but the WORD_TAIL rule manufactures "eis" all the same.
    r'\beis\b',
    # "sporen" in the trace/track sense (grade 6's environment components,
    # grade 9's fossil trackways, "op te sporen", traces of a salt)
    r'sporen\s+en\s+resten',
    r'plas;\s+sporen',
    r'sporen\}?\s+in\s+plaats\s+van',
    r'sporen\s+in\s+de\s+modder',
    r'[Dd]rie\s+sporen',
    r'[Ss]poren:',
    r'de\s+sporen\s+---',
    r'materie,\s+sporen',
    r'mineraal,\s+sporen',
    r'met\s+sporen',
    r'op\s+te\s+sporen',
    r'sporen\s+van\s+amfibie',
    r'sporen\s+van\s+de\s+verandering',
]
