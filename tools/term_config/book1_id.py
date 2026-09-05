"""Book 1 -- id. Curation only; the rules live in tools/termlink/.

Curated by the id agent from this book's own harvest, target by target,
against the English twin's display census (\\omterm displays per label,
not just link totals). Nothing here is inherited from a sibling config.

Young-book register, as in book1_en.py: most defined vocabulary is also
ordinary language, so a word earns a link only where it means the defined
thing in nearly all of its uses. Honest-in-its-own-chapter words go in STOP;
everyday furniture words go in DROP (their compound phrases survive as terms
of their own).

Indonesian-specific note, and the reason this file is NOT a translation of
book1_en.py: Indonesian marks no number. Every English DROP/STOP decision
that turns on a singular/plural split has to be re-taken here, in both
directions:

  * English DROPs "eyes"/"ears" but keeps the singulars "eye"/"ear" (215
    links).  Indonesian has one form each, so "mata" and "telinga" are KEPT
    -- dropping them would cost ~180 links that English has.
  * English DROPs "scale"/"scales" because "at cell scale" collides.
    Indonesian says "sisik" for the fish covering and "skala" for the
    measure: no collision, so "sisik" is KEPT.
  * English DROPs "germ" because its plural collides with grade 1's "germs".
    Indonesian says "lembaga" (seed) and "kuman" (microbe): no collision,
    so both are KEPT.
  * Conversely, "biji" covers English's seed/seeds, which English splits
    across def:g2:...:seed and prop:g3:...:transform. The two id targets are
    +131/-48 against their twins and the pair nets out; nothing to curate.

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
NOT_A_TERM = ("teorema", "lema", "rumus", "kriteria", "paradoks")

STOP = {
    # honest stage-words in their chapters; ordinary everywhere else
    # ("bentuk dewasanya" vs "orang dewasa", "tahap perkembangannya" vs
    # "tahap berikutnya"). English STOPs adult/stage/stages.
    "dewasa", "tahap",
    # food-web equilibrium in its chapter; "keseimbangan tubuh" elsewhere
    "keseimbangan",
    # experiment control in its chapter; "kelenjar kendali" is a different
    # word, but "kontrol" is ordinary prose everywhere else
    "kontrol",
    # managed land in its chapter; "hutan hujan", "ladang" as scenery
    # elsewhere (English STOPs "fields")
    "hutan", "ladang",
    # the exercise need in its chapter; "gerak refleks", "gerakan bernapas"
    # and plain motion everywhere else (English STOPs "movement")
    "gerak",
    # honest in the classification chapters, imperative elsewhere
    "mengelompokkan", "mengklasifikasikan", "pemilahan",
    # the plant in its chapter; the kinship tree in ITS chapter; ordinary
    # scenery in between. English STOPs "tree" for the same double duty.
    "pohon",
    # the g2 chapter's subject; "alam liar", "gejala alam" elsewhere
    "alam",
}

NO_CAPITAL = set()

EXTRA = {}

DROP = {
    # signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # words of the register everywhere after. "makan"/"tumbuh" are the
    # book's two commonest verbs; English links neither (its own
    # prop:g1:living-or-not:signs carries 0 links).
    "makan", "tumbuh", "hidup", "lahir", "mati", "muda", "tua",
    "bayi", "anak",
    # body furniture: correct sense everywhere, but linking every
    # mention is noise. NOT "lengan"/"tungkai": English DROPs the plurals
    # arms/legs yet keeps arm/leg/limb/limbs, which carry 148 of that
    # target's 158 links -- the id singulars have to carry them alone.
    "kepala", "leher", "mulut", "ekor",
    # sense words, as in book1_en.py -- but NOT "mata"/"telinga", which
    # carry English's singular "eye"/"ear" links (see the module docstring)
    "indra", "penglihatan", "pendengaran", "penciuman", "pengecapan",
    "perabaan", "hidung", "lidah",
    # ordinary everywhere ("air dan makanan", "oksigen di dalam airnya");
    # "air minum" and "air liur" survive as terms of their own
    "air",
    # movement verbs defined for grade 1's animals
    "terbang", "berenang",
    # a chain's link AND the linker's own noise word; "rantai makanan"
    # survives (English DROPs "link" for exactly this reason)
    "mata rantai",
    # ("ranting" and "batang pokok" are NOT dropped: English's DROP of
    # branches/trunk still leaves branch:23 + branches:29 linked, and with
    # "pohon" STOPped they are all this target has.)
    # vertebrate classes in one chapter, school classes in the problems
    "kelas",
    # the winter food store in its chapter; "cadangan oksigen", "cadangan
    # spesiesnya" elsewhere. "cadangan makanan" survives.
    "cadangan",
    # \index{kematian} harvested from the life-cycle definition; "kematian"
    # in prose is ordinary (English DROPs death/deaths)
    "kematian",
    # the heart's beat in its chapter; "denyut nadi"/"denyut jantung"
    # survive as terms (English STOPs "beat")
    "denyut",
}

DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
#
# Indonesian compounds are written open, so a two-word compound whose HEAD is
# a term is the dominant false-positive shape here (English's closed compounds
# -- "milkmaid", "eyebrow" -- are protected by word boundaries for free).
EXTRA_PROTECT = [
    # mood, not the liver
    r'[Ss]uasana\s+hati',
    r'\b[Hh]ati-hati\b',
    # a chain's LINK is "mata rantai" -- literally "eye of chain". Without
    # this the bare "mata" fires inside it and points 59 food-chain
    # mentions at the grade-1 sense organ. The single largest wrong-sense
    # class this edition had; the enclitic makes \b useless, hence \w*.
    r'\b[Mm]ata\s+rantai\w*',
    # the other "eye of" idioms, same shape
    r'\b[Mm]ata\s+(?:uang|pencaharian|acara|angin|air|buku)\w*',
    # bark and peel and seed coat are not the skin/sense organ. (English
    # links "onion-skin", so "kulit bawang" is deliberately NOT here.)
    r'\b[Kk]ulit\s+kayu\w*',
    r'\b[Kk]ulit\s+(?:sayur|wortel|buah|kentang|pisang|biji|pelindung|mentah)\w*',
    # a rod, a cigarette, a stick of chalk, a hair shaft -- "batang" is
    # also Indonesian's counter word for long thin things, not the stem
    r'\b[Bb]atang\s+(?:kayu|rokok|kapur|rambut|korek)\w*',
    # the testis is its own term; guard "buah" (fruit) from firing in it
    r'\b[Bb]uah\s+zakar\w*',
    # the body's trunk is its own term; guard "batang" (plant stem)
    r'\b[Bb]atang\s+tubuh\w*',
    # the milkmaids of the cowpox story are not the grade-2 milk, and
    # limewater "keruh seperti susu" is a simile, not the drink (English
    # guards the same pair with \bmilk-white\b)
    r'[Pp]emerah\s+susu\w*',
    r'seperti\s+susu\b',
    # the yolk is the g2 provisioning image, not the egg itself
    r'\b[Kk]uning\s+telur\w*',
    # the millipede is not the g1 limb vocabulary
    r'\b[Kk]aki\s+seribu\w*',
]
