"""Book 1 -- hi. Curation only; the rules live in tools/termlink/.

Young-book register, as in book1_en.py: most defined vocabulary is also
ordinary language, so a word earns a link only where it means the defined
thing in nearly all of its uses. Honest-in-its-own-chapter words go in STOP
(they stay linked inside the chapter that defines them); everyday furniture
words go in DROP (their compound phrases survive as terms of their own).

Hindi specifics that shaped this file, none of which the English config can
see:

  * Hindi inflects by oblique/plural endings, and `lang_hi.py` disables
    DERIVE. So a definition whose \\emph display is an oblique form registers
    only THAT form ("जोड़ों", "सूक्ष्मजीवों", "रसांकुरों"), and the base form
    goes unlinked unless EXTRA restores it. Worse, an oblique form harvested
    from one chapter is a perfectly ordinary word in another: "जोड़ों" is the
    body's joints in grade 3 and the synapses' junctions in grade 8, and the
    grade-8 uses would all have pointed at the skeleton. Those are STOPped,
    not DROPped: inside their own chapter they are the honest term.
  * Several English collisions simply do not exist here, and the words are
    therefore NOT stopped: "control" splits into नियंत्रण (the fair test's
    control) and क़ाबू (self-control); "contract" into संकुचन (a muscle) and
    इक़रारनामा (the daily contract); "scale" into शल्क (a fish's) only;
    "tree" into पेड़ (the plant) and वृक्ष (the kinship tree), each with its own definition. Suppressing them
    would have cost links English keeps for good reasons. (खेत IS stopped,
    but for noise, not for a collision: it means farmland and nothing else,
    and 28 links to "managed land" on every mention of a farm is exactly the
    reading English refuses for "fields".)

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
NOT_A_TERM = ("प्रमेय", "उपप्रमेय", "असमिका", "सूत्र", "मानदंड", "विरोधाभास")

STOP = {
    # honest stage-words in their chapters; ordinary everywhere else
    # ("वयस्क मेंढक" is the life-cycle stage; "वयस्क शरीर" is any grown-up)
    "वयस्क", "अवस्था", "अवस्थाओं",
    # food-web equilibrium in its chapter; "संतुलित खाना" and any balance
    # elsewhere
    "संतुलन", "संतुलन (आहार-जाल का)",
    # the heart's beat in its chapter
    "धड़कन",
    # the exercise need in grade 1; ordinary "activity" elsewhere
    "हलचल",
    # the grade-2 chapter's subject; "प्रकृति" as character/kind elsewhere
    "प्रकृति",
    # the body's joints in grades 1 and 3; in grades 8-9 "जोड़" and "जोड़ों"
    # are the SYNAPSES' junctions, dozens of times over -- the single worst
    # over-linking trap this edition had.
    "जोड़", "जोड़ों",
    # the food workforce of grade 6; grade 9 re-defines the word for its own
    # chapter and the oblique plural must not point back at the bakery
    "सूक्ष्मजीवों",
    # managed farmland in grade 5; every mention of a farm or a field
    # thereafter ("खेतों में बिखेरे प्रतिजैविक") is ordinary language
    "खेत",
}

NO_CAPITAL = set()

EXTRA = {
    # bases whose definition wrote an oblique/plural \emph display, so the
    # harvester registered only the inflected form (lang_hi disables DERIVE)
    "रसांकुर": "prop:g7:digestion-and-nutrients:absorption",
    "कलम": "met:g4:plants-without-seeds:cutting",
    "स्मृति-कोशिका": "def:g9:immune-defenses:memory",
    "स्मृति-कोशिकाएँ": "def:g9:immune-defenses:memory",
    # two-character displays: harvest.py requires len(term) >= 3, so the
    # book's own \emph{लत}\index{लत} and \emph{फल}\index{फल} never
    # registered. English links "addiction" 12 times and "fruit" 66.
    "लत": "prop:g5:healthy-choices:substances",
    "फल": "prop:g3:flowers-fruits-seeds:transform",
    # the chapters say दिल throughout; only the grade-4 definition writes
    # the Sanskritic हृदय, so the harvested term missed every later use
    "दिल": "def:g4:heart-and-blood:heart",
}

DROP = {
    # signs-of-life vocabulary: defined gently in grades 1-2, ordinary
    # words of the register everywhere after
    "जीवित", "पोषण", "जन्म", "जन्म लेता है", "जन्म लेना",
    "मरता है", "मर जाता है", "मृत्यु", "बढ़ता है", "वृद्धि",
    "शावक", "बूढ़ा", "शिशु", "बालक",
    # body furniture: correct sense everywhere, but linking every mention
    # is noise
    "गरदन", "मुँह", "पूँछ",
    # sense words, as in the physics book1 config
    "इंद्रिय", "दृष्टि", "श्रवण", "स्पर्श", "घ्राण", "स्वाद",
    "नाक", "जीभ",
    # ordinary everywhere ("पानी और भोजन", "पानी की ऑक्सीजन")
    "पानी", "पानी (पेय)",
    # movement verbs defined for grade 1's animals
    "उड़ते", "तैरते",
    # ordinary verbs/nouns colliding with their defined senses: छाँटना is
    # the imperative of half the exercises in the book, and कड़ी is any
    # link of any chain, argument or hormone cascade
    "छाँटना", "छँटाई", "कड़ी",
    # "शाखा" of a tree AND of the kinship tree AND of an airway; "तना" of a
    # tree AND the trunk of a body -- twice-used words are not auto-linked
    "शाखा", "शाखाओं", "तना",
    # vertebrate classes in one chapter, school classes and food families
    # ("आहार-वर्ग") in the problems
    "वर्ग", "वर्ग (कशेरुकियों का)",
}

DERIVED = {
    # Hindi inflects; lang_hi.py disables DERIVE, so every oblique and
    # plural form has to be declared. Generated from this book's own
    # corpus -- a variant is listed only where it actually occurs -- and
    # then read one by one. Two notes:
    #   * "घुटने" is deliberately absent: it is the knee's oblique AND the
    #     verb of "दम घुटने" (to suffocate), which grade 7 uses repeatedly.
    #   * ambiguous terms (त्वचा, फेफड़ा, पोषक तत्व, हॉर्मोन, सजीव, ...)
    #     cannot take DERIVED entries at all -- harvest.py applies them only
    #     to unambiguous terms -- so their oblique forms stay unlinked.
    "अंकुर": ("अंकुरों",),
    "अंकुरित होना": ("अंकुरित होने",),
    "अंडवाहिनियाँ": ("अंडवाहिनियों",),
    "अंडवाहिनी": ("अंडवाहिनियों",),
    "अंडा": ("अंडों",),
    "अंडाणु": ("अंडाणुओं",),
    "अंडाशय": ("अंडाशयों",),
    "अकशेरुकी": ("अकशेरुकियों",),
    "अनुकूलन": ("अनुकूलनों",),
    "अभिलक्षण": ("अभिलक्षणों",),
    "आँख": ("आँखों",),
    "आँखें": ("आँखों",),
    "आबादी": ("आबादियाँ", "आबादियों"),
    "आवास": ("आवासों",),
    "आहार शृंखला": ("आहार शृंखलाएँ", "आहार शृंखलाओं"),
    "इल्ली": ("इल्लियाँ", "इल्लियों"),
    "उत्पादक": ("उत्पादकों",),
    "उपभोक्ता": ("उपभोक्ताओं",),
    "उभयचर": ("उभयचरों",),
    "कंकाल": ("कंकालों",),
    "कंद": ("कंदों",),
    "कंधा": ("कंधे", "कंधों"),
    "कपाट": ("कपाटों",),
    "कली": ("कलियाँ",),
    "कवक": ("कवकों",),
    "कशेरुकी": ("कशेरुकियों",),
    "कान": ("कानों",),
    "कीट": ("कीटों",),
    "कूपिका": ("कूपिकाओं",),
    "कूपिकाएँ": ("कूपिकाओं",),
    "कृंतक": ("कृंतकों",),
    "केंद्रक": ("केंद्रकों",),
    "केशिका": ("केशिकाओं",),
    "केशिकाएँ": ("केशिकाओं",),
    "कोशिका": ("कोशिकाएँ", "कोशिकाओं"),
    "कोशिका भित्ति": ("कोशिका भित्तियाँ",),
    "कोहनी": ("कोहनियाँ",),
    "क्लोम": ("क्लोमों",),
    "खनिज लवण": ("खनिज लवणों",),
    "खोल": ("खोलों",),
    "गुणसूत्र": ("गुणसूत्रों",),
    "गुर्दा": ("गुर्दों",),
    "ग्रंथि": ("ग्रंथियाँ", "ग्रंथियों"),
    "चर्वणक": ("चर्वणकों",),
    "जंतु": ("जंतुओं",),
    "जड़": ("जड़ों",),
    "जड़ें": ("जड़ों",),
    "जीन": ("जीनों",),
    "जीवन चक्र": ("जीवन चक्रों",),
    "जीवाणु": ("जीवाणुओं",),
    "जीवाश्म": ("जीवाश्मों",),
    "ज्ञानेंद्रिय": ("ज्ञानेंद्रियों",),
    "झिल्ली": ("झिल्लियाँ",),
    "टाँग": ("टाँगों",),
    "टाँगें": ("टाँगों",),
    "टैडपोल": ("टैडपोलों",),
    "डंठल": ("डंठलों",),
    "तंत्रिका-संदेश": ("तंत्रिका-संदेशों",),
    "तंत्रिका-संधि": ("तंत्रिका-संधियाँ", "तंत्रिका-संधियों"),
    "तंत्रिकाएँ": ("तंत्रिकाओं",),
    "दूध के दाँत": ("दूध के दाँतों",),
    "धमनियाँ": ("धमनियों",),
    "धमनी": ("धमनियों",),
    "नाड़ी": ("नाड़ियाँ",),
    "निलय": ("निलयों",),
    "न्यूरॉन": ("न्यूरॉनों",),
    "पंख": ("पंखों",),
    "पंखुड़ियाँ": ("पंखुड़ियों",),
    "पंखुड़ी": ("पंखुड़ियों",),
    "पक्षी": ("पक्षियों",),
    "पत्तियाँ": ("पत्तियों",),
    "पत्ती": ("पत्तियों",),
    "परिस्थितियाँ": ("परिस्थितियों",),
    "पसलियाँ": ("पसलियों",),
    "पसली": ("पसलियों",),
    "पसीना": ("पसीने",),
    "पुंकेसर": ("पुंकेसरों",),
    "पेड़": ("पेड़ों",),
    "पेशी": ("पेशियाँ", "पेशियों"),
    "पौधा": ("पौधे", "पौधों"),
    "प्यूपा": ("प्यूपाओं",),
    "प्रजाति": ("प्रजातियाँ", "प्रजातियों"),
    "प्रतिजन": ("प्रतिजनों",),
    "प्रतिरक्षी": ("प्रतिरक्षियों",),
    "फल": ("फलों",),
    "फ़र्न": ("फ़र्नों",),
    "फ़सल": ("फ़सलें", "फ़सलों"),
    "फ़सल उगाना": ("फ़सल उगाने",),
    "बहाली": ("बहालियाँ",),
    "बहुवर्षी पौधा": ("बहुवर्षी पौधे",),
    "बाँह": ("बाँहों",),
    "बाँहें": ("बाँहों",),
    "बीज": ("बीजों",),
    "बीजांड": ("बीजांडों",),
    "बीजाणु": ("बीजाणुओं",),
    "भूस्तारी": ("भूस्तारियों",),
    "मछलियाँ": ("मछलियों",),
    "मस्तिष्क": ("मस्तिष्कों",),
    "मांसाहारी": ("मांसाहारियों",),
    "मादा": ("मादाओं",),
    "मानदंड": ("मानदंडों",),
    "मिट्टी": ("मिट्टियों",),
    "युग्मक": ("युग्मकों",),
    "रक्त वाहिका": ("रक्त वाहिकाएँ", "रक्त वाहिकाओं"),
    "रोगजनक": ("रोगजनकों",),
    "रोगाणु": ("रोगाणुओं",),
    "रोम": ("रोमों",),
    "लक्षण": ("लक्षणों",),
    "लत": ("लतें",),
    "वाहिकाएँ": ("वाहिकाओं",),
    "विकल्पी": ("विकल्पियाँ", "विकल्पियों"),
    "विषाणु": ("विषाणुओं",),
    "वृक्ष": ("वृक्षों",),
    "वृषण": ("वृषणों",),
    "शल्क": ("शल्कों",),
    "शल्ककंद": ("शल्ककंदों",),
    "शाकाहारी": ("शाकाहारियों",),
    "शिरा": ("शिराओं",),
    "शिराएँ": ("शिराओं",),
    "शीतनिद्रा लेना": ("शीतनिद्रा लेने",),
    "श्वासनलिकाएँ": ("श्वासनलिकाओं",),
    "श्वेत रक्त कोशिका": ("श्वेत रक्त कोशिकाएँ",),
    "संक्रमण": ("संक्रमणों",),
    "सरीसृप": ("सरीसृपों",),
    "सूक्ष्म आवास": ("सूक्ष्म आवासों",),
    "स्तनधारी": ("स्तनधारियों",),
    "स्त्रीकेसर": ("स्त्रीकेसरों",),
    "स्थायी दाँत": ("स्थायी दाँतों",),
    "हड्डी": ("हड्डियाँ",),
}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # a spiral curriculum re-defines its terms
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 40

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected.
EXTRA_PROTECT = [
    # "खोल" is a shell (grade 1's coverings) AND the stem of खोलना, "to
    # open/undo": "पत्ते खोल देता है", "झिल्लियाँ खोल दी गईं". The noun is
    # worth 36 links, so protect the verb's auxiliaries instead of dropping
    # the word.
    r'खोल\s+(?:सकते|सकती|सकता|देते|देता|देती|दिया|दी|दें|दो|रही|रहा|रहे)',
]
