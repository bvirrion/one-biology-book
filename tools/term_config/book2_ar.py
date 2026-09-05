"""Book 2 -- ar. Curation only; the rules live in tools/termlink/.

Curated on 2026-09-05 from THIS edition's own harvest (228 terms, 312 keys),
never seeded from book1_ar.py. Regenerate after editing definitions or prose:

  python3 tools/link_defined_terms.py --book 2 --lang ar --terms
  python3 tools/link_defined_terms.py --book 2 --lang ar --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang ar --apply

lang_ar.py has WORD_TAIL = '' and DERIVE = False, so no key can grow a suffix;
every wrong link this book could mint comes from a key that is ALSO an ordinary
Arabic word, or from the definite/indefinite pair of one, and those are the
entries below. The English twin (book2_en.py) has the same five sense
collisions -- eye, resistant, frequencies, culture, carrier, bases -- and its
comments explain each; the Arabic equivalents are named here.
"""

STOP = {
    # عين: honest in the eye chapter, but "تحت عين البنكرياس" and "الموضع
    # عينه" elsewhere. Both the bare and the definite key are stopped, so the
    # eye definition is an orphan target -- exactly what book2_en.py does
    # with "eye".
    "عين", "العين",
    # مقاومة: the antibiotic sense in its own chapter, but also "مقاومة
    # الأنسولين" (glucose chapter), "مقاومة الأعشاب" and "مقاومة المرض"
    # (crops chapter). The three-word key مقاومة المضادات الحيوية survives
    # and carries the chapter's links.
    "مقاومة",
    # تواترات: allele frequencies in the population chapter, but also the
    # firing frequencies of a spindle, the recombination frequencies of the
    # tree chapter and "التواترات التقريبية" of the blood-group figure.
    # تواتر أليلي survives.
    "تواترات",
}

NO_CAPITAL = set()   # Arabic has no case

EXTRA = {
    # Arabic pluralises mostly by internal vowel change, which lang_ar.py's
    # empty WORD_TAIL cannot reach, so every plural a book actually uses has
    # to be declared term by term (lang_ar.py says so). These are the forms
    # this edition writes, counted in its own prose; HEAD still supplies the
    # article and the one-letter proclitics, so "والخلايا" links from "خلايا".
    "خلايا": "def:g10:cells-common-unit:cell",              # 398 occurrences
    "مورّثات": "def:g10:universal-dna:gene",                 # 161
    "أنواع": "def:g10:biodiversity-scales:species",          # 124
    "أليلات": "def:g10:universal-dna:gene",                  # 108
    "أليلين": "def:g10:universal-dna:gene",                  # dual, 19
    "طفرات": "def:g11:mutations:mutation",                   # 83
    "عصبونات": "def:g12:stretch-reflex:neuron",              # 49
    "إنزيمات": "def:g11:enzymes-and-phenotype:enzyme",       # 38
    "جمهرات": "def:g12:selection-drift-speciation:population",# 33
    "تهوية": "def:g10:heart-lungs-effort:ventilation",       # 16; the two-word
                                                             # key التهوية الرئوية
                                                             # is written only at
                                                             # the definition, so
                                                             # the target had 0
                                                             # links against
                                                             # English's 17
    "مضادات حيوية": "def:g11:antibiotic-resistance:antibiotic",  # 30
    "هرمونات": "def:g11:hormones-and-reproduction:hormone",  # 23
    "أجسام مضادة": "prop:g12:adaptive-immunity:antibodies",  # 31
    "صبغيدان": "def:g11:cell-cycle-mitosis:chromosome",      # dual, 15
    "صبغيدين": "def:g11:cell-cycle-mitosis:chromosome",      # dual, 7
    "صبغيدات": "def:g11:cell-cycle-mitosis:chromosome",      # 6
    "ثغور": "def:g12:plant-rooted-life:stomata",             # 11
    "مشابك": "def:g12:stretch-reflex:synapse",               # 7
    "عضيات": "def:g10:cells-common-unit:organelle",          # 5
    "منعكسات": "def:g12:stretch-reflex:reflex",              # 3
}

DROP = {
    # ثقافة: animal culture in the diversification chapter, human culture in
    # the human-evolution chapter and ordinary "ثقافة" elsewhere.
    "ثقافة", "ثقافة حيوانية",
    # حامل: a carrier of a recessive allele in the disease chapter, but the
    # NAD/NADP carriers of respiration and photosynthesis in three others.
    "حامل",
    # قواعد: the DNA bases, but also "قواعد القراءة" (tree chapter),
    # "قواعد المورّثة الواحدة" and "قواعد كل يوم" (a section title).
    # The singular key never occurs in prose. نوكليوتيد carries the target.
    "قواعد", "قاعدة (DNA)",
    # دهن: the lipid family in the chemistry chapter, but the FUEL "fat" in the
    # respiration chapter, where English writes "fat" and links nothing. The
    # plural key الدهون keeps the chemistry chapter's links.
    "دهن",
    # متماثلان: harvested from the common-ancestry definition of homology,
    # but in this volume the word is almost always "الصبغيات المتماثلة" of
    # meiosis, which is a different sense (see EXTRA_PROTECT).
    "متماثلان",
    # Clitic forms the harvest picked up from a sentence-initial \emph{...}
    # inside a definition. They are not spellings a reader meets, and
    # فالنقل المورّثي points at a DIFFERENT label from النقل المورّثي, which
    # would make the same phrase link to two chapters.
    "فالنقل المورّثي", "فالتستوستيرون", "فالعصيات", "فالمناعة الفطرية",
    "بالانتقاء الاصطناعي", "أليلاتها", "ركيزته", "قدرتها الفاصلة",
    "نمطه الظاهري", "سائدًا", "متنحيًا", "ورمًا",
    "خلايا التغصنية",
}

# never link the meiotic "homologous chromosomes", which is not the homology
# of the common-ancestry chapter (book2_en.py protects the same phrase)
EXTRA_PROTECT = [
    r"(?:ال)?صبغيات (?:ال)?متماثلة",
    r"(?:ال)?متماثل(?:ين|ان|ات)",
]

AMBIG_POLICY = "nearest-preceding"   # the volume re-defines بروتين، إنزيم، بلاستيدة خضراء
