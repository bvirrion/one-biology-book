"""Book 1 -- en. Curation only; the rules live in tools/termlink/.

Young-book register (cf. the physics/math book1 configs): most defined
vocabulary is also ordinary English, so a word earns a link only if it
means the defined thing in nearly all of its uses. Everyday furniture
words are DROPped (their compound phrases survive as terms of their
own); words that are honest terms inside their own chapter but ordinary
language elsewhere are STOPped.
"""

STOP = {
    # honest stage-words in their chapters; ordinary everywhere else
    # ("the adult set", "the stages of the tract")
    "adult", "stage", "stages",
    # food-web equilibrium in its chapter; "the books balance" elsewhere
    "balance",
    # the heart's beat in its chapter; "beat the record" elsewhere
    "beat",
    # muscle sense in its chapter; the "daily contract" metaphor of the
    # health chapters elsewhere
    "contract",
    # experiment control in its chapters; "control gland/center" and
    # "birth control" elsewhere
    "control",
    # managed-land sense in its chapter; "field scientist" elsewhere
    "fields",
    # the exercise need in its chapter; "breathing movements" etc.
    "movement",
    # honest in the classification chapters, imperative elsewhere.
    # "Sorting" is listed SEPARATELY and on purpose: the grade-2 definition
    # writes \emph{Sorting} at the head of its sentence, so the harvested key
    # is the CAPITALISED form and the lowercase entry never reached it. The
    # target then collected its only two links from the wrong sense entirely --
    # "Sorting by body features" (taxonomy, grade 3) and "Part I --- Sorting
    # the ledger" (grade 9) -- neither of which is waste recycling. Found by
    # the Dutch Book 1 agent, 2026-09-04, whose DROP of "sorteren" correctly
    # refused to reproduce it and left that edition one target short of
    # English. Same trap as the Indonesian \emph{Lensa} case in
    # ../translation_instruction.md: a definition opening with its term
    # capitalised registers only the capitalised display.
    "sorting", "Sorting", "classify",
    # the plant in its chapter; family/kinship trees elsewhere
    "tree",
    # the g2 chapter's subject; "the nature of" turns elsewhere
    "nature",
}

NO_CAPITAL = set()

EXTRA = {
    # restore grade 1's germs (DROPping the seed's "germ" folded the
    # plural away with it); the singular stays unlinked
    "germs": "def:g1:healthy-habits:germs",
}

DROP = {
    # signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # words of the register everywhere after
    "alive", "born", "dies", "feeds", "grows", "young", "old",
    "baby", "child",
    # body furniture: correct sense everywhere, but linking every
    # mention is noise
    "head", "neck", "arms", "legs", "mouth", "tail",
    # sense words, as in the physics book1 config
    "sense", "senses", "sight", "hearing", "touch", "smell", "taste",
    "eyes", "ears", "nose", "tongue",
    # ordinary everywhere ("food and water", "the water's oxygen")
    "water",
    # movement verbs defined for grade 1's animals
    "fly", "swim",
    # ordinary verbs/nouns colliding with their defined senses
    "sort", "link", "stores",
    # "branches" of trees AND of the kinship tree; "trunk" of trees AND
    # of the body -- twice-used words are not auto-linked
    "branches", "trunk",
    # vertebrate classes in one chapter, school classes in the problems
    "classes",
    # fish covering in its chapter; "at cell scale", "the scale of
    # worry" everywhere else (the plural "scales" would fold with it)
    "scale", "scales",
    # the seed's germ (grade 2): its plural collides with grade 1's
    # "germs", and nearest-preceding sends late mentions to the seed
    "germ",
    # \index{death} harvested from the life-cycle definition; "deaths"
    # in prose is ordinary
    "death", "deaths",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped
# across a source line break must still be protected.
EXTRA_PROTECT = [
    # "the nature of ..." -- not the g2 environment sense
    r'\bnature\s+of\b',
    # "the microbe's nature" (character), not the environment
    r"microbe's\s+nature",
    # eye of a potato / needle, not the sense organ (organ is DROPped,
    # but keep the phrase safe for any future un-drop)
    r'\beyes?\s+of\s+a\b',
    # "milky" limewater is not milk; boundaries handle it, this guards
    # rewrites ("milk-white")
    r'\bmilk-white\b',
]
