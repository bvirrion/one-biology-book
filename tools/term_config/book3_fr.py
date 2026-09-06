"""Book 3 -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-09-06 from THIS edition's own harvest, never by translating
book3_en.py: the collisions were re-derived from the French corpus, and they
are not the English ones. What the two censuses (per-target frequency against
the English twin, and per-target chapter set) actually showed:

  * French collisions English does not have. "endoderme" is BOTH the plant
    endodermis (ch. 3) and the animal embryonic endoderm (ch. 4), where
    English has "endodermis" and "endoderm"; the harvest kept the animal
    sense and ch. 23's Casparian-strip prose linked seven times to a germ
    layer. Dropped. "source" is the phloem source AND, through the whole of
    ch. 26, a limestone SPRING (fourteen wrong links). "matrice" is the
    mitochondrial and extracellular matrix, the TEMPLATE strand of ch. 18-19
    ("brin matrice") and ch. 29's character matrix. "genre" as an ordinary
    noun was reworded in the prose instead of dropped.
  * English collisions French does NOT have, kept on purpose: "plasma"
    (French says "membrane plasmique", so the English plasma-membrane
    collision is absent -- all 21 links are blood plasma), "polaire" (French
    says "polarité cellulaire"), "lisse" (no "muscle lisse" occurrence
    outside its own chapter), "caractère" is dropped for link fatigue, not
    for a collision, "résistance", "opérateur" and "empilement" are
    single-sense here.
  * Verified against WORD_TAIL = (?:e?s)? with TAIL_ON_EVERY_WORD: the tail
    manufactures nothing false out of these terms (it yields "basees",
    "cirees" and the like, which occur nowhere), so no EXTRA_PROTECT is
    needed. French irregular plurals the tail cannot reach are declared in
    EXTRA below.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 3 --lang fr --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --lang fr --apply
"""

STOP = {
    # the enzyme substrate of ch. 13, the "phosphorylation au niveau du
    # substrat" of ch. 15, the growth substrate of a succession (ch. 28) and
    # the substrate of a transporter (ch. 22) are four senses of one word --
    # the same call English makes
    "substrat", "substrats",
}

NO_CAPITAL = set()

EXTRA = {
    # The index key is the two-word "appareil de Golgi", so the 18 bare uses
    # ("du RE au Golgi", "la face cis du Golgi", "le dictyosome de Golgi")
    # link nowhere. All 18 were read: every one is the organelle, never
    # Camillo Golgi the person, and the longer "appareil de Golgi" still wins
    # where it occurs. Mirrors the same entry added to book3_en.py.
    "Golgi": "def:b1:eukaryotic-cell:endomembrane",
    # French says "règles de Chargaff", so the two bare uses of the surname
    # -- "Chargaff (1950) hydrolysa..." and "(Chargaff, les dimensions des
    # rayons X...)" -- linked nowhere. English makes the same call.
    "Chargaff": "prop:b1:nucleic-acids:chargaff",
    # French irregular plurals, which WORD_TAIL = (?:e?s)? cannot build
    "niveaux trophiques": "def:b1:ecosystem-organization:trophic",
    "parois cellulaires": "prop:b1:carbohydrates:wall",
    # singulars the harvest folded away (it kept only the plural)
    "hydrophyte": "prop:b1:flowering-plant-organization:plasticity",
    "xérophyte": "prop:b1:flowering-plant-organization:plasticity",
}

DROP = {
    # the four exchanges of the open system, and the functions of a mammal,
    # are ordinary French words on every page
    "énergie", "matière", "information", "environnement",
    "relation", "reproduction", "nutrition",
    # "vitesse" is the reaction rate of ch. 13 and the speed of sap, of a
    # glacier and of an extinction everywhere else (72 links, 37 of them the
    # ordinary sense); "couplage" likewise
    "vitesse", "couplage",
    # "eau" alone carried 365 of the 398 links to the water definition;
    # "acide" and "base" are the pH pair, but "acide" lives inside "acide
    # aminé"/"acide gras" and "base" is the nitrogenous base of the DNA
    # chapters
    "eau", "acide", "acides", "base", "bases",
    # mitochondrial/extracellular matrix vs the template strand vs a
    # character matrix; plant node vs a node of a cladogram; phloem source
    # vs the spring of ch. 26; xylem vessel vs blood vessel; plant epidermis
    # vs animal epidermis; plant endodermis vs embryonic endoderm
    "matrice", "nœud", "source", "vaisseau", "vaisseaux", "épiderme",
    "endoderme",
    # membrane transporter vs electron carrier; membrane channel vs the
    # pancreatic duct and the channels between gill lamellae
    "transporteur", "transporteurs", "canal", "canaux",
    # microscope resolution vs solving an equation; systematic character
    # (57 links, all inside its own chapter -- dropped for link fatigue, as
    # English drops it); endoskeleton vs the carbon and sugar-phosphate
    # backbones of ch. 11-12; hydrostatic skeleton vs hydrostatic pressure;
    # saturated fatty acid vs saturated haemoglobin; carbon vs nitrogen
    # fixation; gut absorption vs root and light absorption; a condensation
    # reaction vs chromosome condensation; modular growth as a bare
    # adjective; the two denaturations, whose index displays never occur in
    # prose
    # "grossit" is harvested from the \\emph'd verb of the microscope
    # definition and matched "le foie grossit" in ch. 16
    "grossit",
    "résolution", "caractère", "caractères", "squelette", "hydrostatique",
    "saturé", "fixation", "absorption", "condensation", "modulaire",
    "dénaturation", "dénaturation (ADN)", "dénaturation (protéine)",
}

EXTRA_PROTECT = []

AMBIG_POLICY = "drop"
