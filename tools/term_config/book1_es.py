"""Book 1 -- es. Curation only; the rules live in tools/termlink/.

Young-book register, as in book1_en.py: most defined vocabulary is also
ordinary Spanish, so a word earns a link only where it means the defined
thing in nearly all of its uses. Honest-in-its-own-chapter words go in STOP;
everyday furniture words go in DROP (their compound phrases survive as terms
of their own).

Curated against the English twin, term by term, from this book's own harvest.
The English canon is the reference for link PLACEMENT: every entry below was
chosen so that the Spanish edition links the same senses, in the same
chapters, as `--lang en` does -- measured with a per-target frequency diff and
a per-target chapter-set diff, not assumed.

Two facts about the engine drove several choices and are easy to forget:

  * `morphology.pattern` appends WORD_TAIL `(?:e?s)?`, so DROPping a plural
    while keeping its singular changes nothing -- "ojo" already matches
    "ojos". A sense is suppressed only when every harvested spelling of it is
    listed (or the singular is).
  * a display carrying a parenthesis ("agua (bebida)", "testigo (experimento)")
    can never match running prose. English uses that shape deliberately: it
    keeps the printed index entry while suppressing the link. Those displays
    are therefore left alone -- listing them would be a no-op.

Terms are spelled as the bodies spell them: raw UTF-8, no TeX escapes.
"""

# The English default list ({"theorem", "lemma", ..., "law of", "problem"})
# suppresses exactly ONE definition display in this book -- "criterion" --
# measured over parts/grade-1..9 before this file was written. So the only
# load-bearing member of the list below is "criterio", and the technical
# result-names are kept only for symmetry.
#
# Deliberately ABSENT, and do not "restore" them:
#   * the multi-word "law of" idiom. It never fires on English (Ohm's law,
#     Gauss's law) but its literal translation swallows every named law in a
#     book. It cost one edition 88 links and 5 target labels.
#   * "principle", "rule", "identity", "problem". Their translations are
#     ordinary words of this language, and NO English display in this book
#     contains any of them -- so listing them can only over-suppress.
NOT_A_TERM = ("teorema", "lema", "desigualdad", "fórmula", "criterio", "paradoja")

STOP = {
    # --- the English STOP list, transposed sense by sense ---
    # honest stage-words in their chapters; ordinary everywhere else
    # ("la etapa siguiente del razonamiento", "ya es un adulto")
    "adulto", "etapa", "etapas",
    # food-web equilibrium in its chapter; "el equilibrio del cuerpo",
    # "en equilibrio" elsewhere. The phrase term survives on its own.
    "equilibrio",
    # the experiment's control in its chapter -- and, unlike English
    # "control", the Spanish word is ALSO the ordinary word for a witness,
    # which grade 9 uses on almost every page ("testigos independientes",
    # "unos testigos que no han podido confabularse"). English keeps only
    # the parenthesised display; so does this edition.
    "testigo",
    # the exercise need in its chapter; "movimientos respiratorios", "el
    # movimiento de las placas" elsewhere
    "movimiento",
    # honest in the classification chapters, imperative in every exercise
    # stem after them ("Clasifica: ...")
    "clasificar", "Clasificar",
    # the plant in its chapter; family/kinship trees from grade 6 on.
    # "árbol del parentesco" survives as its own term.
    "árbol",
    # the g2 chapter's subject; "de naturaleza distinta" and similar turns
    # elsewhere. English STOPs "nature" for the same reason.
    "naturaleza",
    # English STOPs "fields" (the "field scientist" collision) and keeps no
    # field term at all; managed land is carried by "bosques" /
    # "bosque (gestionado)". Linking the Spanish phrase would add links the
    # English canon does not have.
    "campo de cultivo", "campos de cultivo",
}

NO_CAPITAL = set()

EXTRA = {
    # Spanish inflects for gender where English does not, and the harvest
    # only ever sees the form the definition happened to use. Without these,
    # "las plantas productoras" and "las células femeninas" -- which English
    # links as "producers" and "female" -- go unlinked, and def:g5:food-webs:
    # roles alone lost 55 links against the English twin.
    "productora": "def:g5:food-webs:roles",
    "productoras": "def:g5:food-webs:roles",
    "consumidora": "def:g5:food-webs:roles",
    "consumidoras": "def:g5:food-webs:roles",
    "masculino": "def:g4:animal-reproduction:sexual",
    "masculina": "def:g4:animal-reproduction:sexual",
    "femenino": "def:g4:animal-reproduction:sexual",
    "femenina": "def:g4:animal-reproduction:sexual",
    # WORD_TAIL is "(?:e?s)?", which builds plurals but never strips them.
    # The vertebrate-group terms were all harvested in the plural, so their
    # singulars matched nothing -- English's "fish" happens to be invariant
    # and linked both numbers.
    # Only "pez": English's group names are plural-only terms too, so
    # "bird", "mammal", "insect", "amphibian" and "reptile" go unlinked in
    # the canon as well -- adding their Spanish singulars measured +92 links
    # the English twin does not have. "fish" is the one English singular
    # that IS linked, because the word is number-invariant.
    "pez": "prop:g3:sorting-living-things:groups",
    # English links the bare "vessels"; Spanish harvested only the two-word
    # "vaso sanguíneo". Only the PLURAL is safe: the singular "vaso" is the
    # drinking glass that carries the whole grade-7 waste problem
    # ("un vaso de agua bebido en el desayuno"), and EXTRA_PROTECT below
    # guards the two plural uses of it as well.
    "vasos": "def:g4:heart-and-blood:vessels",
}

DROP = {
    # --- signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # words of the register everywhere after (English: alive, born, dies,
    # feeds, grows, young, old, baby, child, death) ---
    "vivo", "nace", "muere", "muerte", "crece", "se alimenta",
    "joven", "viejo", "bebé", "niño",
    # the movement verbs of grade 1's animals (English: fly, swim)
    "vuelan", "nadan",
    # --- body furniture: correct sense everywhere, but linking every
    # mention is noise (English: head, neck, mouth, tail) ---
    "cabeza", "cuello", "boca", "cola",
    # "tronco" is the tree's AND the body's; English DROPs "trunk" and keeps
    # only the disambiguated "trunk (body)" display.
    "tronco",
    # --- sense words, exactly as in book1_en.py: the five sense NAMES are
    # ordinary Spanish ("a la vista", "he oído", "a gusto", "con tacto"),
    # while the organs "ojo" and "oreja" stay linked, as "eye" and "ear" do.
    # "órgano de los sentidos" survives as its own term.
    "sentido", "vista", "oído", "tacto", "olfato", "gusto",
    "nariz", "lengua",
    # ordinary everywhere ("agua y sales", "el oxígeno del agua"); the
    # food-family display "agua (bebida)" is unaffected
    "agua",
    # the grade-6 herb term, but "anual" is first of all the ordinary
    # adjective: "las vacunas anuales", "las renovaciones anuales".
    # "planta anual" / "planta vivaz" survive as terms of their own.
    "anuales",
    # --- ordinary verbs/nouns colliding with their defined senses ---
    # English DROPs "link": "eslabón" is the food chain's link AND the
    # metaphor the method chapters run on ("nombrar su eslabón")
    "eslabón",
    # vertebrate classes in one chapter, school classes in the problems
    # (English: classes); "clase (de vertebrados)" is unaffected
    "clases",
    # fish covering in its chapter, but English DROPs "scale"/"scales" for
    # its metaphorical uses and keeps no scale term at all. Linking the
    # unambiguous Spanish word would add links English does not have.
    "escama", "escamas",
    # the seed's germ: English DROPs "germ" (its plural collides with the
    # grade-1 germs). Spanish carries the germs sense on "microbio", so the
    # seed term is dropped for the same density.
    "germen",
    # grade 1 says "tierra" for soil and grade 6 says "suelo"; English has
    # one word and links it only from the grade-6 definition on. Keeping
    # "tierra" would link nine years of soil AND "la Tierra".
    "tierra",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = [
    # "de naturaleza ..." -- not the g2 environment sense (STOP already
    # covers the bare word; this guards any future un-STOP)
    r'\bde\s+naturaleza\b',
    # "el ojo de la aguja / de la cerradura": not the sense organ
    r'\bojo\s+de\s+(?:la|una)\b',
    # "hoja de papel", "hoja de cálculo": not the plant's leaf
    r'\bhojas?\s+de\s+(?:papel|c[áa]lculo)\b',
    # the drinking glass of the grade-7 waste problem, not a blood vessel
    r'\bvasos?\s+de\s+agua\b',
    # "la hoja de puntuación" of the newborn check: a sheet, not a leaf
    r'\bhojas?\s+de\s+puntuaci[óo]n\b',
    # "la yema de la ..." is the egg yolk of grade 8, not a tree's bud
    r'\bla\s+yema\s+de\s+la\b',
]
