"""Book 3 -- es. Curation only; the rules live in tools/termlink/.

University register (Year 1), so AMBIG_POLICY is "drop", matching book3_en.py
-- not Book 2's school "nearest-preceding".

CURATED 2026-09-06 FROM THIS EDITION'S OWN HARVEST. Nothing here was
translated from book3_en.py or seeded from book2_es.py: every entry below was
found by censusing the Spanish links themselves (per-target frequency against
the English twin, per-target chapter set, and the full display census), and
each one was read in context before it was written down. The English DROP list
was consulted only afterwards, as a checklist of senses to go and look at --
and half of its entries turned out NOT to collide in Spanish (see the note at
the end of DROP).

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 3 --lang es --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --lang es --apply
"""

STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # The harvest keys the singular of a term the prose only ever emphasises
    # in the plural, or fails on a hyphen:
    #  * "xerófitos" is the harvested display; the singular "un xerófito" of
    #    the grade's own exercise is unreachable through WORD_TAIL, which can
    #    add an s but never remove one. English links its one "xerophyte".
    "xerófito": "prop:b1:flowering-plant-organization:plasticity",
    #  * "nitrato-reductasa" is emphasised with a hyphen, and the harvest
    #    keeps only the multi-word index phrase; English links its two
    #    "nitrate reductase".
    "nitrato-reductasa": "prop:b1:plant-water-minerals:nitrate",
    # Re-synced 2026-09-06 with the two entries the wave-1 Dutch and
    # Portuguese agents put into book3_en.py, both of which apply here for the
    # same reason:
    #  * the index key is the two-word "aparato de Golgi"; the bare organelle
    #    name occurs 40 times and linked nothing. All 40 were read: every one
    #    is the organelle (la pila del Golgi, la cara cis del Golgi, del RE al
    #    Golgi), never Camillo Golgi the person.
    "Golgi": "def:b1:eukaryotic-cell:endomembrane",
    #  * the harvested term is the multi-word "reglas de Chargaff", which is
    #    DROPped below to match English's NOT_A_TERM exclusion of "rule"; the
    #    bare surname carries the link instead, exactly as in book3_en.py.
    "Chargaff": "prop:b1:nucleic-acids:chargaff",
}

DROP = {
    # --- the three exchanges of the open system are ordinary words in every
    # chapter after the first ("energía" 189 links, "materia" 46,
    # "información" 16, none of them naming the exchange itself). English
    # drops the same three.
    "energía", "materia", "información",
    # --- "medio" is the worst homograph in Spanish biology: 79 links, of
    # which the CULTURE medium (ch. 5, 18, 20), the arithmetic MEAN ("el
    # número medio de hijas", "el punto medio de la curva"), and plain HALF
    # ("medio millón", "medio micrómetro", "día y medio") outnumber the
    # "medio" that means environment. English drops "environment" for a much
    # milder version of the same collision.
    "medio",
    # --- the three "funciones" of a mammal: "relación" is the ordinary
    # Spanish for a RATIO ("la relación superficie/volumen", "la relación
    # con $K'_{eq}$") in every one of its 12 links, and "nutrición" and
    # "reproducción" are ordinary nouns of the register. The three
    # "función de ..." phrases survive as their own terms.
    "relación", "reproducción", "nutrición",
    # --- "velocidad" is the reaction rate only inside ch. 13: the other 43
    # links are the speed of a replication fork, of sap in the xylem, of
    # elongation, of decomposition, of molecular substitution. "velocidad de
    # reacción" survives.
    "velocidad",
    # --- "agua" the molecule versus water everywhere (355 links); "ácido"
    # inside "ácido láctico / pirúvico / cítrico / nucleico" rather than the
    # acid of the acid-base definition (109). "enlace de hidrógeno",
    # "molécula polar" and "polar" keep the target alive.
    "agua", "ácido",
    # --- "vaso"/"vasos" is the xylem vessel in ch. 3, 7 and 24 and the BLOOD
    # vessel in ch. 4 and 22 (and, once, the drinking glass Beaumont digested
    # meat in). Both numbers go; "vaso del xilema" survives.
    "vaso", "vasos",
    # --- "esqueleto"/"esqueletos" is the animal skeleton in ch. 4 and the
    # CARBON skeleton of a sugar, an amino acid, a nucleic-acid chain or a
    # polypeptide in ch. 8-12 -- 16 of its 39 links are the wrong sense.
    # "exoesqueleto", "endoesqueleto" and "esqueleto hidrostático" survive,
    # which is exactly what English is left with.
    "esqueleto", "esqueletos",
    # --- "matriz" is the mitochondrial matrix (ch. 15-16), the polysaccharide
    # matrix of a cell wall (ch. 6, 10) and the character MATRIX of the
    # cladistics chapter (ch. 29). "matriz mitocondrial" and "matriz
    # extracelular" survive.
    "matriz",
    # --- "aumento" is the microscope's magnification in 3 of its 7 links and
    # the ordinary Spanish for an INCREASE in the other 4 ("el aumento de la
    # actividad específica", "un aumento del once por ciento", "el efecto de
    # aumento de Emerson"); "aumenta" is simply the verb. English keeps
    # "magnification" and "magnifies", which have no such second sense.
    "aumento", "aumenta",
    # --- "resolución" is the microscope's in 4 links and the resolution of a
    # conflict or a question elsewhere; "resuelve" is the verb. "poder de
    # resolución" survives.
    "resolución", "resuelve",
    # --- "lisa" is the smooth OUTER MEMBRANE of a mitochondrion at its only
    # link, not the smooth ER; "saturado" is saturated vapour (ch. 24), a
    # saturated haemoglobin (ch. 21) and a saturated predator (ch. 27) at all
    # four of its links, never a saturated fatty acid, which is reached by
    # "ácido graso saturado".
    "lisa", "saturado",
    # --- "modular" is also the Spanish VERB "to modulate", and its ch. 20
    # link ("un factor de transcripción es modular") is not the plant's
    # modular growth; "reconocimiento" is the recognition PARTICLE of the
    # secretory pathway at one of its two links.
    "modular", "reconocimiento",
    # --- NOT_A_TERM in tools/termlink/ is an ENGLISH word list ("paradox",
    # "rule", "law of", ...), so it silently fails to exclude the Spanish
    # names of the same two results that English excludes. Dropped here so the
    # two editions carry the same targets; "Chargaff" is restored above as a
    # bare surname, which is how English reaches that target too.
    "paradoja del valor C", "reglas de Chargaff",
    # --- CHECKED AND KEPT, against the English DROP list, because the Spanish
    # word has no second sense in this volume (each verified link by link):
    #   "plasma" (21) is blood plasma everywhere -- the membrane is
    #     "membrana plasmática", which WORD_TAIL cannot reach;
    #   "tallo" (17) is the plant stem -- a stem cell is "célula madre" and
    #     the brainstem is "tronco encefálico";
    #   "carácter" (24) is the systematic character -- Spanish says "el
    #     comportamiento de una curva", never "el carácter";
    #   "operador" (14) is the lac operator -- this volume has no
    #     mathematical operator;
    #   "fuente" (8) and "sumidero" (9) are the phloem's source and sink --
    #     the source pool of ch. 28 is "fondo de origen";
    #   "epidermis" (12), "condensación" (6), "sustrato" (56), "hoja" (108),
    #     "transportadores" (18), "bombas" (7), "canal" (3) and
    #     "supervivencia" (5) each have ONE to SIX wrong-sense occurrences
    #     against many right ones, so they are masked one phrase at a time in
    #     EXTRA_PROTECT below rather than thrown away;
    #   "resistencia" (2) and "hidrostático" (2) link only inside the chapter
    #     that defines them, and both links are the defined sense;
    #   "polar" (15) is the polar molecule or polar group at every link --
    #     cell polarity is "polaridad celular", a term of its own;
    #   "apilamiento" (3) is base stacking -- the grana of ch. 14 are
    #     "apilados", a form WORD_TAIL cannot produce;
    #   "absorción" (7) is uptake across an epithelium at every link -- light
    #     absorption is "absorbe" in this edition.
}

# NOTE: multi-word patterns use \s+ between words -- a phrase wrapped across a
# source line break must still be protected. Every pattern below was found by
# reading all of its term's link contexts, not guessed.
EXTRA_PROTECT = [
    # "un sustrato nuevo sin suelo": the ROCK substrate a primary succession
    # starts on (ch. 28, twice), not the enzyme's. English STOPs "substrate"
    # outright for this one collision and loses 54 correct links with it.
    r'\bsustrato\s+nuevo\b',
    # "una hoja de papel": a SHEET (ch. 10), not a leaf.
    r'\bhojas?\s+de\s+papel\b',
    # the ANIMAL epidermis of ch. 4, against the plant epidermis of ch. 3.
    r'\bSu\s+epidermis\b',
    r'\bepidermis\s+de\s+la\s+piel\b',
    # the ELECTRON carriers of the respiratory and photosynthetic chains,
    # against the membrane transporters of ch. 7 (six occurrences).
    r'\bcadenas?\s+de\s+transportadores\b',
    r'\bCu[ée]ntense\s+los\s+transportadores\b',
    r'\blos\s+transportadores\s+y\s+los\s+ciclos\b',
    r'\bdos\s+transportadores\s+m[óo]viles\b',
    r'\btodos\s+los\s+transportadores\b',
    # "un sistema de dos bombas": the buccal and opercular pumps of a fish
    # (ch. 21), not an ion pump.
    r'\bsistema\s+de\s+dos\s+bombas\b',
    # chromosome condensation (ch. 17, 18), not the condensation reaction.
    r'\bcondensaci[óo]n\s+metaf[áa]sica\b',
    r'\bProfase\s+\(condensaci[óo]n\b',
    # the ribosome's exit channel (ch. 19), not a membrane channel.
    r'\bsale\s+por\s+un\s+canal\b',
    # "la supervivencia de los linces": ordinary survival (ch. 25 solutions),
    # not the survivorship of a life table.
    r'\bsupervivencia\s+de\s+los\s+linces\b',
]

AMBIG_POLICY = "drop"
