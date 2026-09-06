"""Book 3 -- ar. Curation only; the rules live in tools/termlink/.

Curated from THIS edition's own harvest (734 candidate displays, 727
linkable), never by translating book3_en.py and never by seeding from the
Book 2 Arabic twin. English's cross-sense list is a starting question, not an
answer: some of its collisions are not collisions in Arabic (its "matrix" is
this edition's الحشوة, which has no second sense here), and Arabic has
several that English does not -- فصل is both "separation" and "chapter",
جهاز is both "organ system" and "apparatus" (جهاز غولجي), أعراف is both
"cristae" and "conventions", الفجوة is both "vacuole" and "gap", محيط is both
"environment" and "ocean" (عرض المحيط), عقدة is both a stem "node" and a tree
"node", and ورقة is both "leaf" and "sheet of paper".

DROP, not STOP. STOP removes a word from the global terms table but
harvest.py still feeds it to the per-chapter "local" map, so any chapter with
exactly one candidate definition links it anyway; DROP is applied to terms,
local, nearest and primary alike and is the only switch that actually removes
a term. (Measured by the Indonesian Book 3 agent, confirmed in harvest.py.)

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 3 --lang ar --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --lang ar --apply
"""

STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # Arabic pluralises by internal vowel change, which lang_ar.py's empty
    # WORD_TAIL cannot reach, so every plural the book actually writes has to
    # be declared. Counts are occurrences in this edition's own prose, taken
    # with the existing \omterm wrappers stripped. HEAD still supplies the
    # article and the one-letter proclitics, so "والخلايا" links from "خلايا".
    "خلايا": "def:b1:cell-unit-of-life:cell",                 # 286
    "أنواع": "def:b1:classifying-biodiversity:species",       # 164
    "بروتينات": "def:b1:proteins:peptide",                    # 150
    "أوراق": "def:b1:flowering-plant-organization:organs",    # 107
    "إنزيمات": "def:b1:enzymes:enzyme",                       # 99
    "مورّثات": "def:b1:genomes:gene",                          # 75
    "جذور": "def:b1:flowering-plant-organization:organs",     # 59
    "أنسجة": "def:b1:body-plans-tissues:tissue",              # 58
    "أغشية": "def:b1:membranes-transport:membrane",           # 57
    "متقدرات": "def:b1:eukaryotic-cell:mitochondrion",        # 50
    "ريبوزومات": "def:b1:gene-expression:ribosome",           # 42
    "ثغور": "def:b1:plant-transport:stoma",                   # 39
    "صبغيات": "def:b1:genomes:genome",                        # 38
    "نوكليوتيدات": "def:b1:nucleic-acids:nucleotide",         # 35
    "كائنات": "def:b1:organism-environment:organism",         # 26
    "أعضاء": "def:b1:mammal-organization:organ",              # 24
    "زغابات": "def:b1:digestion-absorption:surface",          # 21
    "إنترونات": "def:b1:genomes:gene",                        # 20
    "إكسونات": "def:b1:genomes:gene",                         # 18
    "جمهرات": "def:b1:populations:population",                # 17
    "سكاكر": "def:b1:carbohydrates:monosaccharide",           # 14
    "غلاصم": "def:b1:gas-exchange:gill",                      # 12
    "فيروسات": "def:b1:genomes:virus",                        # 10
    "أحماض أمينية": "def:b1:proteins:aminoacid",              # 9
    "مورثومات": "def:b1:genomes:genome",                      # 8
    "كودونات": "def:b1:gene-expression:code",                 # 7
    "أحماض دهنية": "def:b1:lipids:fattyacid",                 # 6
    "أسناخ": "def:b1:gas-exchange:lung",                      # 6
    "عقيدات": "def:b1:plant-water-minerals:nodules",          # 6
    "أوبرونات": "def:b1:expression-control:operon",           # 2
    "طفيليات": "def:b1:species-interactions:symbiosis",       # 2
    # Compounds whose HEAD word is a different, much commoner term. Without
    # these the harvest's bare النواة swallowed every "eukaryote" and
    # "prokaryote" in the book -- 92 links to the nucleus definition against
    # English's 14 -- and the bare حمض swallowed "nucleic acid". Declared as
    # terms so that the linker's longest-match rule reaches them first.
    "حقيقيات النواة": "def:b1:cell-unit-of-life:prokeuk",     # 36
    "حقيقية النواة": "def:b1:cell-unit-of-life:prokeuk",      # 31
    "بدائيات النواة": "def:b1:cell-unit-of-life:prokeuk",     # 8
    "بدائية النواة": "def:b1:cell-unit-of-life:prokeuk",      # 4
    "حمض نووي": "def:b1:nucleic-acids:chain",                 # 3, definite only
    # Plurals and variants whose target was starved because the singular the
    # definition displays is never the form the prose writes. Each was found
    # by the per-target census against the English twin: the trophic levels
    # had 7 links against English's 51, the niche 5 against 27, the
    # Lotka--Volterra isoclines 2 against 23.
    "محلِّلات": "def:b1:ecosystem-organization:trophic",        # 26
    "منتِجات": "def:b1:ecosystem-organization:trophic",         # 23
    "مستهلِكات": "def:b1:ecosystem-organization:trophic",       # 12
    "آكلات الفتات": "def:b1:ecosystem-organization:trophic",   # 3
    "مكانة": "def:b1:ecosystem-organization:niche",            # 22
    "مكانات": "def:b1:ecosystem-organization:niche",           # 8
    "نظم بيئية": "def:b1:ecosystem-organization:ecosystem",
    "خطي التساوي": "prop:b1:species-interactions:lotka",       # 6
    "خط التساوي": "prop:b1:species-interactions:lotka",        # 4
    "ثلاثيات غليسريد": "def:b1:lipids:triglyceride",           # 2
    "نويصمات": "def:b1:genomes:nucleosome",                    # 1
    "بيروكسيسومات": "def:b1:eukaryotic-cell:peroxisome",       # 12
}

# Homographs. Each of these is a real defined term whose Arabic display is
# also an ordinary word of the language, or a second technical term of this
# same book. A homograph collision passes every structural and prose gate --
# the link is well formed, the word is real, the sentence is native -- so the
# only defence is to suppress the term.
DROP = {
    # --- English's own cross-sense list, re-checked in Arabic ---
    "الطاقة",            # energy: ordinary in every paragraph of the book
    "ماء", "مائي",       # water
    "بلازما",            # plasma
    "وعاء", "الأوعية",   # vessel: xylem vessel vs الأوعية الدموية
    "البشرة", "بشرة",    # epidermis: plant and animal, and the skin
    "الساق", "ساق",      # stem
    "مُشغِّل",             # operator: the lac operator vs an employer
    "المشبع",            # saturated
    "الأملس", "الخشن",   # smooth / rough endoplasmic reticulum
    "الصفة",             # character (systematics) vs attribute
    "مقاومة",            # resistance
    "ركيزة", "ركائزه",   # substrate (English STOPs it; only DROP works)
    # --- collisions that exist in Arabic and not in English ---
    "فصل", "يفصل",       # "separate/resolve" vs هذا الفصل, this chapter (33x)
    "معدل",              # enzyme "rate" vs معدل النمو / الخطأ / الهجوم / ...
    "التعرف",            # molecular "recognition" vs ordinary recognising
    "عرف",               # a mitochondrial crista vs the perfect of "to know"
    "تقطع", "متقطعًا",    # "segmentation" vs the verb: فتقطع \qty{5}{cm}, "it covers"
    "هيكل", "الهيكل",    # "skeleton" vs الهيكل السكري الفوسفاتي, a backbone.
                         # The compounds هيكل مائي / الهيكل الخارجي / الداخلي
                         # are terms of their own and keep their links.
    "المادة", "المعلومة",  # matter / information: 60 links to a proposition
                         # the English canon links 0 times
    "التغذية", "التكاثر", "العلاقة",   # the three "functions of relation and
                         # nutrition": 10 links against English's 0, and all
                         # three are ordinary Arabic
}

EXTRA_PROTECT = [
    r"RNA\s+الناقل",        # transfer RNA -- not a membrane "carrier" (24x)
    r"قناة\s+البنكرياس",     # the pancreatic duct -- not an ion "channel"
    r"الخشب\s+الميت",        # dead wood -- not xylem
    r"قصيبات\s+موازية",      # a bird's parabronchi -- not xylem tracheids
    r"ورقة\s+معشبة",         # a herbarium sheet -- not a leaf
    r"كابح\s+تحرره",         # a brake the kidneys release -- not a repressor
    r"المراتب\s+أعراف",      # ranks are conventions -- not mitochondrial cristae
    r"قاعدة\s+العشرة",       # the ten-percent rule -- not a nucleotide base
    r"قاعدة\s+عريضة",        # a broad base (age pyramid) -- not a base
    r"التغذية\s+الراجعة",    # negative feedback -- not nutrition, a life function
    r"المحيط\s+الهادئ",      # the Pacific Ocean -- not the environment
    r"المحيط\s+الحيوي",      # the biosphere -- not the environment
    r"عرض\s+المحيط",         # the open ocean -- not the environment
    r"مجمع\s+مصدر",          # a source pool of species -- not a phloem source
    r"الفجوة\s+بينهما",      # the gap between them -- not a vacuole
    r"كل\s+عقدة",            # every node of a tree -- not a stem node
    r"RNA\s+ناقل",          # "a transfer RNA", indefinite -- not a carrier
    r"(?:ال)?مقطع\s+(?:ال)?ناقل",   # conducting cross-section -- not a carrier
]

AMBIG_POLICY = "drop"
