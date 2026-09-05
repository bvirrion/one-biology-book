"""Book 2 -- hi. Curation only; the rules live in tools/termlink/.

Curated on 2026-09-05 from THIS edition's own harvest (never seeded from
book1_hi.py). Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 2 --lang hi --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang hi --apply

What shaped this file, none of which the English config can see:

  * `lang_hi.py` sets WORD_TAIL to '' and DERIVE to False: Hindi does not
    inflect by a Latin-style suffix, so NOTHING is derived automatically and
    every oblique/plural form a body actually writes has to be declared in
    DERIVED. Without them this edition linked 4,898 times where English links
    5,547; the DERIVED block below is where the difference lives. Each entry
    was read off this book's own corpus -- a form is listed only where it
    occurs -- and each was checked for a second sense before being added.
  * The English collisions of book2_en.py mostly do NOT exist here, and the
    words are therefore not suppressed. "eye" is आँख and never the naked eye's
    idiom nor "under the eye of the pancreas" (which this edition writes
    नज़र); "resistant" is प्रतिरोधी, and its only non-antibiotic uses are the
    toxin-resistant borers of grade 12, which the chapter itself calls the
    same selection; "frequencies" splits, because the allele frequency is
    युग्मविकल्पी बारंबारता (a term of its own) while a spindle's firing rate
    is the bare बारंबारता, which is therefore NOT listed as a term; "bases"
    is क्षारक and never an acid-base pair.
  * The one English collision that survives translation is the carrier:
    वाहक is the carrier of a recessive allele in grade 11 and the reduced-NAD
    carrier of photosynthesis and respiration in grade 12, 48 times over. It
    is DROPped, exactly as English drops "carrier".
  * A collision English does not have: संधि is the body's JOINT (grade 10)
    and also the second element of तंत्रिका-संधि (the synapse) and दृक्-संधि
    (the optic chiasm). The synapse keeps its links because the longer term
    wins; the chiasm and the synaptic cleft are protected below.

Terms are spelled as the bodies spell them: raw UTF-8, no TeX escapes.
"""

# NOT_A_TERM is deliberately left at its English default. Its members are
# English result-words ("theorem", "lemma", "law of", ...); no Hindi display
# in this book contains any of them, so translating the list could only
# over-suppress -- the "law of" idiom alone cost another edition 88 links.

STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # displays the definitions wrote in an oblique/plural form only, so the
    # harvest registered the inflection and not the base word
    "मूलरोम": "prop:g12:plant-rooted-life:surfaces",
    "पेशी तंतु": "def:g10:muscles-and-joints:muscle",
    "इंट्रॉन": "prop:g11:gene-expression:splicing",
    "द्वीपिका": "prop:g12:glucose-and-diabetes:hormones",
    "शलाका": "def:g11:the-eye:photoreceptors",
}

DROP = {
    # a carrier of a recessive allele in grade 11; the reduced-NAD carriers of
    # photosynthesis and respiration in grade 12 -- as in book2_en.py
    "वाहक",
}

# multi-word patterns use \s+ between words; never consume a `$`
EXTRA_PROTECT = [
    # NOTE ON DEVANAGARI IN THESE PATTERNS: a matra is its own code point, so
    # "समजातों?" makes only the anusvara optional and never matches the plain
    # "समजात". Every optional Hindi ending below is therefore a GROUP:
    # (?:ों)?, not ों?. Three wrong links survived the first draft of this
    # file for exactly that reason.
    #
    # the optic chiasm and the synaptic cleft are not the skeleton's joint
    r'दृक्-संधि',
    r'संधि-दरार',
    # समजात is the homology of grade 10's common ancestry AND the second word
    # of समजात गुणसूत्र, the homologous chromosomes of meiosis -- book2_en.py
    # protects exactly this pair with r'homologous (?:chromosomes?|pairs?)',
    # and Hindi needs the bare noun's idioms too ("समजातों का हर जोड़ा").
    # 19 wrong links in grade 12 before these lines.
    # The second --apply pass reads the first pass's output, where the
    # neighbouring word may already be wrapped: the patterns tolerate it.
    r'समजात(?:ों)?\s+(?:\\omterm\{[^{}]*\}\{)?गुणसूत्र(?:ों)?',
    r'समजात(?:ों)?\s+(?:का|के|की)\s+(?:हर\s+|कोई\s+|कितने\s+)?जोड़\S*',
    r'समजात(?:ों)?\s+को\s+अलग',
    r'समजात(?:ों)?\s+के\s+अलग\s+होने',
    r'जोड़े\s+बने\s+समजात',
    r'जोड़ी\s+बनाने\s+को\s+कोई\s+समजात',
    r'दोनों\s+समजात',
    r'समजात\s+जोड़े',
    r'दूसरे\s+समजात\s+के',
    r'गुणसूत्र(?:ों)?\}?\s+समजात',
    r'बिना\s+किसी\s+समजात',
    r'सेट\s+के\s+समजात',
    # the toxin-resistant borers of the maize chapter are not the antibiotic
    # resistance mechanisms of grade 11 (book2_en.py STOPs "resistant" for the
    # same reason; here the grade-11 uses are worth 73 links and are kept)
    r'प्रतिरोधी\s+छेदक',
    r'प्रतिरोधी\s+बच(?:ा|े)',
    r'प्रतिरोधी\s+कीटों',
    r'प्रतिरोधी\s+व्यक्तियों',
    r'प्रतिरोधी\s+हो\s+जाते',
    r'प्रतिरोधियों\s+को\s+पतला',
    r'प्रतिरोधियों\s+से\s+हुए',
    r'प्रतिरोधियों\s+से\s+कहीं',
]

DERIVED = {
    # Hindi obliques and plurals, read off this book's corpus. A form is
    # listed only where it occurs, and only for a term whose sense it keeps.
    "आँख": ("आँखें", "आँखों"),
    "आबादी": ("आबादियाँ", "आबादियों"),
    "उत्परिवर्तजन": ("उत्परिवर्तजनों",),
    "उत्परिवर्तन": ("उत्परिवर्तनों",),
    "उपास्थि": ("उपास्थियों",),
    "ऑप्सिन": ("ऑप्सिनों",),
    "कंडरा": ("कंडराएँ", "कंडराओं"),
    "कशेरुकी": ("कशेरुकियों",),
    "कूपिका": ("कूपिकाएँ", "कूपिकाओं"),
    "कूपिकाओं": ("कूपिकाएँ",),
    "केंद्रक": ("केंद्रकों",),
    "कैंसर": ("कैंसरों",),
    "कैंसरजन": ("कैंसरजनों",),
    "कोडॉन": ("कोडॉनों",),
    "कोशिका": ("कोशिकाएँ", "कोशिकाओं"),
    "कोशिकांग": ("कोशिकांगों",),
    "क्रियाधार": ("क्रियाधारों",),
    "क्रोमैटिड": ("क्रोमैटिडों",),
    "क्लेड": ("क्लेडों",),
    "क्षारक": ("क्षारकों",),
    "जाति": ("जातियाँ", "जातियों"),
    "जीन": ("जीनों",),
    "जीनप्ररूप": ("जीनप्ररूपों",),
    "टीका": ("टीके", "टीकों"),
    "थाइलेकॉइड": ("थाइलेकॉइडों",),
    "द्वीपिकाएँ": ("द्वीपिकाओं",),
    "न्यूक्लियोटाइड": ("न्यूक्लियोटाइडों",),
    "न्यूरॉन": ("न्यूरॉनों",),
    "परपोषी": ("परपोषियों",),
    "पारितंत्र": ("पारितंत्रों",),
    "प्रकाशग्राही": ("प्रकाशग्राहियों",),
    "प्रतिजन": ("प्रतिजनों",),
    "प्रतिजैविक": ("प्रतिजैविकों",),
    "प्रतिपुष्टि": ("प्रतिपुष्टियाँ", "प्रतिपुष्टियों"),
    "प्रतिरक्षी": ("प्रतिरक्षियों",),
    "प्रतिरोधी": ("प्रतिरोधियों",),
    "प्रतिवर्त": ("प्रतिवर्तों",),
    "बहुगुणित": ("बहुगुणिता",),
    "भक्षककोशिका": ("भक्षककोशिकाएँ", "भक्षककोशिकाओं"),
    "भक्षककोशिकाएँ": ("भक्षककोशिकाओं",),
    "मध्यस्थ": ("मध्यस्थों",),
    "युग्मविकल्पी": ("युग्मविकल्पियों",),
    "रंध्र": ("रंध्रों",),
    "राइबोसोम": ("राइबोसोमों",),
    "लसीकाणु": ("लसीकाणुओं",),
    "शंकु": ("शंकुओं",),
    "शलाका": ("शलाकाएँ", "शलाकाओं"),
    "शलाकाएँ": ("शलाकाओं",),
    "समजात": ("समजातों",),
    "समजातता": ("समजातताएँ",),
    "सहजीविता": ("सहजीविताएँ",),
    "सूत्रकणिका": ("सूत्रकणिकाएँ", "सूत्रकणिकाओं"),
    "सूत्रकणिकाएँ": ("सूत्रकणिकाओं",),
    "सेंट्रोमियर": ("सेंट्रोमियरों",),
    "स्नायु": ("स्नायुओं",),
    "स्मृति कोशिका": ("स्मृति कोशिकाओं",),
    "स्मृति कोशिकाएँ": ("स्मृति कोशिकाओं",),
    "हॉर्मोन": ("हॉर्मोनों",),
    "वृक्षाभ कोशिका": ("वृक्षाभ कोशिकाएँ",),
    "सहायक T कोशिका": ("सहायक T कोशिकाओं",),
    "सहायक T कोशिकाएँ": ("सहायक T कोशिकाओं",),
    "शोथरोधी दवा": ("शोथरोधी दवाओं",),
    "शोथरोधी दवाएँ": ("शोथरोधी दवाओं",),
}

PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"   # school book; matches book2_en.py
