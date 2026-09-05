"""Book 1 -- ar. Curation only; the rules live in tools/termlink/.

Curated by the ar agent from this book's OWN harvest (2026-09-04); nothing
here is inherited from a sibling config. Every entry below was decided by
reading the display in its chapter and then diffing the target's link count
against the English twin.

Young-book register, as in book1_en.py: most defined vocabulary is also
ordinary language, so a word earns a link only where it means the defined
thing in nearly all of its uses. Honest-in-its-own-chapter words go in STOP;
everyday furniture words go in DROP (their compound phrases survive as terms
of their own).

Arabic specifics, none of which the other configs need:

* lang_ar.py sets DERIVE off, because Arabic pluralises by internal vowel
  change. Every plural a term actually reaches must therefore be DECLARED in
  DERIVED below -- that list is where most of this edition's link density
  lives, and it was built by grepping the bodies for each base, not guessed.
* the definite article and the one-letter proclitics are handled by HEAD, so
  a term listed bare ("خلية") already matches "الخلية"، "والخلية"، "بالخلية".
  Listing both forms is redundant, not wrong -- the harvest produces both
  when the bodies write both.
* HEAD also makes ب+term match, which is why a term whose bare form is a
  common preposition-phrase head is dangerous. Those are DROPped by hand.

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
NOT_A_TERM = ("مبرهنة", "صيغة", "معيار", "مفارقة")

# honest term in its own chapter, ordinary word elsewhere -- the exact
# counterparts of book1_en.py's STOP, term by term.
STOP = {
    # "adult" -- the life-cycle stage in grades 2-3, an ordinary adjective
    # ("بالغ واحد موثوق" = one trusted adult) everywhere after
    "بالغ", "بالغًا",
    # "stage/stages" -- honest in the life-cycle chapters, "مرحلة" is the
    # ordinary register word for any step of anything
    "مرحلة", "المراحل",
    # "balance" -- the food web's equilibrium in its chapter; "التوازن"
    # is also the body's sense of balance (grade 8's alcohol paragraph)
    "توازن", "توازن (الشبكة الغذائية)",
    # "control" -- the fair test's control in grade 4; but "شاهد" is also
    # "witness", and chapter g9-05 argues from four independent WITNESSES.
    # The disambiguated display "شاهد (تجربة)" is kept and never fires,
    # exactly as English's "control (experiment)" does not.
    "الشاهد",
    # "fields" -- managed land in its chapter, ordinary "الحقول" elsewhere
    "الحقول",
    # "movement" -- the exercise need of grade 1; "الحركة" is the ordinary
    # word for any motion, including the breathing movements of grade 7
    "حركة",
    # "sorting"/"classify" -- honest in the classification chapters,
    # imperative elsewhere ("افرز الصفات الخمس"). The compound
    # "فرز النفايات" survives as a term of its own.
    "فرز", "تفرز", "تصنّف",
    # "tree" -- the plant in grade 1, the kinship tree in grade 6.
    # "شجرة القرابة" survives as a term of its own.
    "شجرة", "الشجرة", "شجرةً",
    # "nature" -- the grade-2 chapter's subject; "طبيعة" is also the
    # ordinary "nature of a thing" (and "علماء الطبيعة" = naturalists)
    "طبيعة", "الطبيعة",
}

NO_CAPITAL = set()

# Manual entries, for targets harvest.py cannot see.
EXTRA = {
    # The kinship proposition writes \emph{قرابتهما} (a possessive form,
    # useless as a term) and \index{قرابة}; harvest.py skips a ONE-WORD
    # index display, so the target harvested nothing and shipped zero links
    # against English's 22. The bare noun is what the bodies actually use.
    "قرابة": "prop:g6:classification-kinship:kinship",
    # Same shape: the address proposition's display is \emph{أعضائه الهدف},
    # inflected with a pronoun. The bare compound carries the sense.
    "عضو هدف": "prop:g8:hormonal-communication:address",
    "أعضاء هدف": "prop:g8:hormonal-communication:address",
    "الأعضاء الهدف": "prop:g8:hormonal-communication:address",
    # And again: \emph{مستضداته}. Arabic derives no plural by suffix, so
    # both numbers are declared.
    "مستضد": "prop:g9:immune-defenses:specific",
    "مستضدات": "prop:g9:immune-defenses:specific",
    # Arabic writes an individual plant "نبتة", a word no definition
    # display contains (the grade-1 definition emphasises "نبات"), so 86
    # correct mentions were going unlinked.
    "نبتة": "def:g1:plants-around-us:plant",
    "نبتات": "def:g1:plants-around-us:plant",
    # The dual "رئتين" is how the body chapters actually write "lungs";
    # the harvested display is the nominative dual "الرئتان". wrap_file
    # links a term only from its own chapter on, so this entry cannot
    # reach the grade-4 breathing chapter -- see the score file's note on
    # def:g4:breathing:organs, the one target this edition leaves thin.
    "رئتين": "def:g7:how-animals-breathe:four",
    # "صفة" is genuinely ambiguous (attribute / trait) and resolves by
    # nearest-preceding; its broken plural "صفات" cannot inherit that,
    # because DERIVED only extends UNambiguous bases. Pointed at the LATER
    # of the two definitions on purpose: wrap_file then leaves the grade-6
    # attribute mentions unlinked rather than mis-targeting them.
    "صفات": "def:g9:heredity-and-traits:traits",
    # indefinite "أوعية" (blood vessels); the harvest saw only "الأوعية"
    "أوعية": "def:g4:heart-and-blood:vessels",
    # restored after DROPping the bare "حمل" above
    "الحمل": "def:g5:human-reproduction:pregnancy",
}

DROP = {
    # --- signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # words of the register everywhere after (English drops the same set)
    "حي",              # "alive" -- also the ordinary adjective and "quarter"
    "يولد", "يموت", "موت", "يشيخ",
    "يتغذى", "ينمو",
    "صغير", "صغيرًا",
    "رضيع", "طفل",
    # --- body furniture: the sense is right everywhere, but linking every
    # mention is noise. English drops head/neck/mouth/tail and the plurals.
    "الرأس", "رأس", "العنق", "عنق", "الفم", "فم", "ذنب",
    # "طرف" is "limb" in grade 1 and "party/end" later ("أحد طرفي الزوجين",
    # "من طرفها إلى طرفها"): the plural "أطراف" is unambiguous and stays
    "طرف",
    # --- the five senses, exactly as English drops them: only "sense organ"
    # and the ambiguous "skin" earn links
    "حاسة", "الحاسة", "بصر", "البصر", "سمع", "السمع", "شم", "الشم",
    "ذوق", "الذوق", "لمس", "اللمس",
    "أنف", "الأنف", "لسان", "اللسان",
    # --- fish covering: "حرشفة/الحراشف" is the scale of grade 1, but
    # "مقياس"-free Arabic still writes "الحراشف" only here; dropped for
    # symmetry with English's "scale"/"scales"
    "حرشفة", "الحراشف",
    # --- ordinary everywhere ("الماء والهواء"); "ماء (شراب)" survives
    "الماء",
    # --- movement verbs defined for grade 1's animals
    "تسبح", "تطير",
    # --- "link": "حلقة" is the food chain's link in grade 3 AND the
    # report-decide-order LOOP of grades 5-8 AND a seminar ("حلقة دراسية").
    # Three senses, one spelling: never auto-linked.
    "حلقة",
    # --- "الفطور" is both the plural of "فطر" (fungi) and "breakfast",
    # and grades 8-9 eat breakfast repeatedly. "فطر" and the declared
    # plural "فطريات" carry the target.
    "الفطور",
    # --- the trunk of a tree (English drops "trunk"); "البدن" (the body's
    # trunk) is a different word and stays
    "جذع", "الجذع",
    # --- harvest artifacts: a display captured mid-phrase
    "بالدقّة",         # from "بالدقّة" in the heart chapter; "دقة القلب" stays
    "قرابتهما",
    "نمطها الصبغي",
    "مستضداته",
    "نبيتك المقيم",
    "أعضائه الهدف",
    "بيئته",
    "حليبها",
    "بولًا", "بيوضًا", "ولودًا", "جنينًا", "نطفًا", "بذورًا", "مذابًا",
    "تطورًا",
    # --- homograph collisions, each found by reading the display/target
    # pairs the linker actually produced (the census the brief asks for) ---
    # "حمل" is BOTH "pregnancy" and the perfect verb "carried". In the
    # heredity chapters "حمل كل والد محددًا مستترًا" = each parent CARRIED
    # a hidden determinant, and "الانتثار هو حمل بذور" = dispersal is the
    # CARRYING of seeds. Twelve wrong-sense links. The definite "الحمل" is
    # the pregnancy in every one of its uses and is restored in EXTRA.
    "حمل",
    # "تحول" is BOTH the noun "metamorphosis" and the verb "turns X into
    # Y": grade 8's sheep TURN day-length into hormones, and the ear's
    # cells TURN sound into nerve messages. The definite "التحول" is the
    # grade-2 noun in every one of its uses and stays.
    "تحول",
}

# Broken plurals and duals. Arabic derives none of these by suffix, so the
# forms below were found by grepping the ar bodies for each base term and
# keeping the ones that actually occur. This is where roughly a fifth of
# the edition's links come from.
DERIVED = {
    "خلية": ["خلايا"],
    "عضلة": ["عضلات"],
    "عظم": ["عظام"],
    "عظمة": ["عظام"],
    "نبات": ["نباتات"],
    "حيوان": ["حيوانات"],
    "نوع": ["أنواع"],
    "جذر": ["جذور"],
    "بذرة": ["بذور"],
    "زهرة": ["أزهار"],
    "ورقة": ["أوراق"],
    "غصن": ["أغصان", "غصون"],
    "صبغي": ["صبغيات"],
    "مورّثة": ["مورّثات"],
    "أليل": ["أليلات"],
    "طفرة": ["طفرات"],
    "أحفورة": ["أحافير"],
    "فيروس": ["فيروسات"],
    "بكتيريا": [],
    "عصبون": ["عصبونات"],
    "مشبك": ["مشابك"],
    "غدة": ["غدد"],
    "هرمون": ["هرمونات"],
    "كلية": ["كليتان", "كليتين"],
    "وريد": ["أوردة"],
    "شريان": ["شرايين"],
    "جمهرة": ["جمهرات"],
    "مشيج": ["أمشاج"],
    "مستضد": ["مستضدات"],
    "كرية بيضاء": ["كريات بيضاء", "الكريات البيضاء"],
    "موئل": ["موائل"],
    "بوغ": ["أبواغ"],
    "يرقة": ["يرقات"],
    "محك": ["محكات"],
    "درنة": ["درنات"],
    "بصلة": ["بصلات"],
    "فطر": ["فطريات"],
    "ميكروب غذائي": [],
    "مضغة": ["مضغ"],
    "جنين": ["أجنة"],
    "خصية": ["خصيتان", "خصيتين"],
    "مبيض": ["مبيضان", "مبيضين"],
    "رئة": ["رئتان", "رئتين"],
    "أذين": ["أذينان"],
    "بطين": ["بطينان"],
    "سلسلة غذائية": ["سلاسل غذائية"],
    "شبكة غذائية": ["شبكات غذائية"],
    "وعاء دموي": ["أوعية دموية"],
    "شعيرة دموية": ["شعيرات دموية"],
    "سنخ رئوي": ["أسناخ رئوية"],
    "قصيبة هوائية": ["قصيبات هوائية"],
    "غلصمة": ["غلاصم"],
    "عصارة هاضمة": ["عصارات هاضمة"],
    "خلية ذاكرة": ["خلايا ذاكرة"],
    "جسم مضاد": ["أجسام مضادة"],
    "عضو حس": ["أعضاء الحس", "أعضاء حس"],
    "مفصل": ["مفاصل"],
    "ضرس": ["أضراس"],
    "ناب": ["أنياب"],
    "قاطعة": ["قواطع"],
    "ضلع": ["أضلاع"],
    "نطفة": ["نطف"],
    "بويضة": ["بويضات"],
    "قناة البيض": ["قناتا البيض", "قناتي البيض"],
    "برعم": ["براعم"],
    "جرثوم": ["جراثيم"],
    "كائن مجهري": ["كائنات مجهرية"],
    "ممرض": ["ممرضات"],
    # --- restored density, found by diffing each target against English ---
    "الثمرة": ["ثمرة", "ثمار", "الثمار"],
    "بيضة": ["بيض"],
    "ساق": ["سيقان"],
    "بتلة": ["بتلات"],
    "سداة": ["أسدية"],
    "منتج": ["منتِجون", "منتِجين", "منتِجة"],
    "مستهلك": ["مستهلِكون", "مستهلِكين"],
    "الطاقة": ["طاقة"],
    "النبض": ["نبض"],
    "فقاري": ["فقاريات"],
    "لافقاري": ["لافقاريات"],
    "شجرة القرابة": ["شجرة العائلة", "شجرة قرابة"],
    "واقي ذكري": ["الواقي"],
    "رجل": ["رجلان", "رجلين", "أرجل", "أرجلها"],
    "ذراع": ["ذراعان", "ذراعين", "أذرع"],
    "عين": ["عينان", "عينين", "أعين"],
    "أذن": ["أذنان", "أذنين", "آذان"],
}

PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = [
    # "نوع من ..." = "a kind of ...", not the biological species
    r'نوع\s+من\b',
    r'أنواع\s+من\b',
    # "حمل" is pregnancy AND "load/carrying": the circulation of grade 8
    # carries a doubled LOAD, the marsh holds flood water
    r'حملًا\s+مضاعفًا',
    r'الحمل\s+المضاعف',
    # "صدفة" is the shell of grade 1 and "coincidence" elsewhere
    r'بالصدفة',
    r'صدفة\s+محضة',
    # "الدورة" is the menstrual cycle AND the circulation AND a lap:
    # the compound terms carry the senses, the bare phrase below does not
    r'دورة\s+واحدة\s+في\s+المجرى',
    # "الجهاز" alone is any system; only the named systems are terms
    r'الجهاز\s+كله',
    # "رجل" is grade 1's leg; grade 9 writes "a boy or a MAN" twice
    r'أو\s+رجل\b',
    # "واقي" is the condom of grade 8; grade 9's pigment is the body's
    # SUNSCREEN ("كان واقي الجسم من الشمس")
    r'واقي\s+الجسم',
    # "بول" is grade 7's urine and the photographer Paul Nadar's forename
    r'بول\s+نادار',
    # "مضغ" is the plural of grade 5's embryo and the verbal noun for
    # CHEWING ("حلاوة المضغ الطويل", grade 7)
    r'المضغ\s+الطويل',
    # the valve arrangement of grade 8's male tract is not a heart valve
    r'ترتيب\s+من\s+الصمامات',
    r'الصمامات\s+بين\s+المهمتين',
    # the DNA extraction mashes an onion; it is not grade 4's bulb-and-tuber
    r'موزة\s+أو\s+بصلة',
    # the hair's root and shaft are not a plant's
    r'خلايا\s+الجذر',
    r'ساق\s+الشعرة',
]
