"""Book 4 -- ar. Curation only; the rules live in tools/termlink/.

Curated from THIS edition's own harvest (245 definition headwords, 526
linkable surfaces), never by translating book4_en.py and never by seeding
from book3_ar.py: English's collisions are not this edition's, and Arabic
has several that English does not.

The homographs that mattered here, all found by the two censuses
(per-target frequency against English, and per-target chapter set):

  رحم      the moss ARCHEGONIUM (ch. 5) and the mammalian UTERUS
           (ch. 8-9). 36 of its 44 links were the uterus.
  ارتباط   genetic LINKAGE (ch. 4) and chemical BINDING (ch. 19, 21).
  قدرة     cell POTENCY (ch. 12) and mechanical POWER (ch. 21,
           "ضربة القدرة", the power stroke).
  تحول     bacterial TRANSFORMATION (ch. 3) and an ordinary "change"
           (ch. 6, 15).
  مبيض     the flower's OVARY (ch. 6) and the mammalian OVARY
           (ch. 8-9) -- the same collision English STOPs for "ovary".
  استحثاث  embryonic INDUCTION (ch. 10) and FLORAL induction (ch. 14),
           which is ch. 14's own defined term; the linker was wrapping
           a link inside that definition's own \\emph.

DROP, not STOP: STOP only removes a word from the global table and
harvest.py still feeds it to the per-chapter map, so a chapter that has
one candidate definition links it anyway. DROP is the only switch that
actually removes a surface, and it removes only that surface -- every
one of these targets keeps its other displays and stays reachable.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --lang ar --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --lang ar --apply
"""

STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # Arabic pluralises by internal vowel change and derives by pattern, so
    # the forms below are unreachable from the harvested headword with
    # lang_ar.py's empty WORD_TAIL. Each is a surface this edition actually
    # writes; each restores an English target that would otherwise have no
    # Arabic link at all.
    "متغذيات كيميائية معدنية": "def:b2:microbial-metabolism:trophic",
    # ch. 5 and ch. 6 both print the bare "اللقاح", so AMBIG_POLICY dropped
    # it and English's commonest link (81 of them) had no Arabic twin; the
    # two-word "حبة لقاح" above keeps ch. 6's own sense.
    "لقاح": "def:b2:plant-life-cycles:heterospory",
    "حبة لقاح": "prop:b2:angiosperm-reproduction:pollen",
    "مستقبلات نووية": "prop:b2:cell-signalling:nuclear",
    "كيناز التيروزين": "prop:b2:cell-signalling:rtk",
    "إصلاح عدم التوافق": "prop:b2:genome-diversification:repair",
    "رباعيات مرتبة": "prop:b2:meiosis-heredity:tetrads",
    # The plural of "عامل استنساخ"; the singular already links.
    "عوامل استنساخ": "prop:b2:cell-differentiation:transcriptional",
    # The arteriole, this book's most-used vessel word, is written with the
    # diminutive pattern and never appears in the singular headword shape.
    "شرينات": "def:b2:blood-circulation:vessels",
    "شريّن": "def:b2:blood-circulation:vessels",
}

DROP = {
    # Both the bare and the definite form: the harvest records whichever the
    # definition happens to print, and DROP is matched on the surface.
    "رحم", "الرحم",
    "ارتباط", "الارتباط",
    "قدرة", "القدرة",
    "تحول", "التحول",
    "مبيض", "المبيض",
    "استحثاث", "الاستحثاث",
}

# Never consume a `$` (see tools/termlink/protect.py). A LOOKAHEAD, never a
# lookbehind: a lookbehind on a neighbouring word that is itself a linked
# term stops matching once that word is wrapped, and the second --apply then
# inserts new links (wave 1, es and pt).
EXTRA_PROTECT = [
    # "cannot rest" (ch. 17, the heart), not the seed's dormancy.
    r"لا\s+تستطيع\s+السكون",
    # "defines nothing" (ch. 24), not developmental determination.
    r"لا\s+تحدد\s+شيئًا",
    # "the prevailing pressure" (ch. 18), not a dominant allele.
    r"الضغط\s+السائد",
]

AMBIG_POLICY = "drop"
