"""Book 1 -- pt. Curation only; the rules live in tools/termlink/.

Curated from THIS edition's own harvest (`--terms`), then diffed
target-by-target against the English twin: for every definition label, the
Portuguese surface forms that link to it were compared with the English ones,
and a Portuguese form was suppressed exactly where its English counterpart is
suppressed in book1_en.py. Nothing is inherited from another book: an `EXTRA`
seeded from a sibling config points at labels of THAT book and ships as
undefined references, and a seeded `EXTRA_PROTECT` masks the links you wanted.

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
NOT_A_TERM = ("teorema", "lema", "desigualdade", "fórmula", "critério", "paradoxo")

STOP = {
    # honest stage-words in their chapters; ordinary everywhere else
    # ("a dentição de adulto", "as etapas da infecção")
    "adulto", "Adulto", "etapa", "etapas",
    # food-web equilibrium in its chapter; "o equilíbrio do corpo" elsewhere
    "equilíbrio",
    # the heart's beat in its chapter; "a batida" of anything elsewhere
    "batida",
    # the muscle sense in its chapter; "contrair uma doença", "contrair-se"
    # in ordinary prose elsewhere
    "contrair", "se contrair",
    # experiment control in its chapter; "centro de controle", "controle de
    # natalidade" elsewhere
    "controle",
    # managed-land sense in its chapter; "lavouras" as ordinary fields
    "lavouras",
    # the exercise need in its chapter; "os movimentos respiratórios",
    # "o movimento das folhas" everywhere else
    "movimento",
    # honest in the classification chapters, ordinary imperative elsewhere
    # ("classifique", "classificar por tamanho")
    "classificar", "Classificar",
    # the plant in its chapter; family/kinship trees elsewhere
    "árvore",
    # the g2 chapter's subject; "a natureza de" turns elsewhere
    "natureza",
}

NO_CAPITAL = set()

EXTRA = {
    # English links bare "vessels" to the grade-4 definition everywhere (the
    # grade-7 label owns artery/vein/capillary instead). Portuguese harvests
    # only the two-word "vaso sanguíneo", so the bare plural went unlinked:
    # 31 English links against 7.
    "vasos": "def:g4:heart-and-blood:vessels",
}

DROP = {
    # signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # words of the register everywhere after
    "vivo", "nasce", "morre", "cresce", "se alimenta", "jovem", "velho",
    "bebê", "criança",
    # body furniture: correct sense everywhere, but linking every
    # mention is noise
    "cabeça", "pescoço", "braços", "pernas", "boca", "cauda",
    # sense words, as in the physics book1 config
    "sentido", "visão", "audição", "tato", "olfato", "paladar",
    "olhos", "ouvidos", "nariz", "língua",
    # ordinary everywhere ("comida e água", "o oxigênio da água")
    "água",
    # the soil/earth a plant needs: ordinary noun in every later chapter
    "terra",
    # movement verbs defined for grade 1's animals
    "nadam", "voam",
    # ordinary verbs/nouns colliding with their defined senses
    "elo", "reservas", "produtoras",
    # "galhos" of trees AND of the kinship tree; "tronco" of trees AND of
    # the body -- twice-used words are not auto-linked
    "galhos", "tronco",
    # vertebrate classes in one chapter, school classes in the problems
    "classes",
    # fish covering in its chapter; "a escama" reading elsewhere is rare but
    # "escala" collisions and the plural fold make the link noise
    "escama", "escamas",
    # the seed's germ (grade 2): collides with grade 1's germs, and
    # nearest-preceding sends late mentions to the seed
    "germe",
    # \index{morte} harvested from the life-cycle definition; "a morte" in
    # prose is ordinary
    "morte",
    # THE homograph of this language. "pelo"/"pelos" is fur AND the
    # contraction of "por" + "o"/"os" ("carregado pelos insetos"). Measured on
    # a full pass: 298 of the label's 388 links were the preposition, in every
    # grade -- the single largest wrong-sense class in this edition. English
    # can keep "fur"; Portuguese cannot link it at all, so the covering
    # definition ships with "concha", "pena/penas" and the "pelo de inverno"
    # compound only.
    "pelo", "pelos",
    # a grade-7 display that has no English twin term: it would point every
    # ordinary "movimentos respiratórios" of grades 4-8 at the grade-7
    # definition of respiration, across the grade-4 breathing definition
    "movimentos respiratórios",
}

# Irregular plurals that lang_pt.py's "(?:e?s)?" tail cannot produce
# (-ao -> -oes, -al -> -ais, -il -> -eis, -iz -> -izes). Each was measured
# against its English twin's link count before being added; "pulmoes" is
# deliberately ABSENT, because it is already the grade-7 four-ways-of-
# breathing term and DERIVED only fills gaps (setdefault), never overrides.
DERIVED = {
    "animal": ["animais"],          # EN "animals": 119 links, all of them lost
    "raiz": ["raízes"],
    "coração": ["corações"],
    "fóssil": ["fósseis"],
    "embrião": ["embriões"],
    "adaptação": ["adaptações"],
    "mutação": ["mutações"],
    "infecção": ["infecções"],
    "população": ["populações"],
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = []
