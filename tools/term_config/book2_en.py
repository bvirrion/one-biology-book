"""Book 2 -- en. Curation only; the rules live in tools/termlink/.

High-school register: the defined vocabulary is mostly honest biology
and links nearly everywhere. Curated on 2026-09-02 after the English
edition landed. Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 2 --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --apply
"""

STOP = {
    # honest in the eye chapter; "the naked eye", "under the eye of the
    # pancreas" elsewhere
    "eye",
    # antibiotic sense in its chapter; insulin-resistant tissues,
    # pest-resistant crops elsewhere
    "resistant",
    # allele frequencies in the population chapter; firing frequencies
    # of a spindle elsewhere
    "frequencies",
    # the sense of "resolution" in the microscopy chapter only
    "resolution",
}

NO_CAPITAL = set()

EXTRA = {
    # plurals the harvest folded away, all single-sense in this volume
    "stomata": "def:g12:plant-rooted-life:stomata",
    "antibody": "prop:g12:adaptive-immunity:antibodies",
    "antigens": "def:g12:adaptive-immunity:antigen",
    "hormones": "def:g11:hormones-and-reproduction:hormone",
    "neurons": "def:g12:stretch-reflex:neuron",
    "synapses": "def:g12:stretch-reflex:synapse",
    "genes": "def:g10:universal-dna:gene",
    "mutations": "def:g11:mutations:mutation",
    "vaccines": "def:g12:adaptive-immunity:vaccine",
    "populations": "def:g12:selection-drift-speciation:population",
    "tumours": "def:g11:cancer:cancer",
    "carcinogens": "def:g11:cancer:carcinogen",
    "antibiotics": "def:g11:antibiotic-resistance:antibiotic",
    "reflexes": "def:g12:stretch-reflex:reflex",
    "pedigrees": "def:g11:genes-and-disease:pedigree",
    "phenotypes": "def:g11:enzymes-and-phenotype:phenotype",
    "organelles": "def:g10:cells-common-unit:organelle",
    "joints": "def:g10:muscles-and-joints:joint",
    "tendons": "def:g10:muscles-and-joints:muscle",
    "lipids": "def:g10:chemistry-of-life:families",
    "carbohydrates": "def:g10:chemistry-of-life:families",
    "nucleic acids": "def:g10:chemistry-of-life:families",
}

DROP = {
    # animal culture in one chapter; bacterial cultures and human culture
    # everywhere else
    "culture", "culture (animal)",
    # a carrier of a recessive allele in one chapter; the NAD carriers of
    # respiration and photosynthesis in three others
    "carrier",
    # "acids and bases" as well as the DNA bases; the singular "base (DNA)"
    # never occurs in prose
    "bases", "base (DNA)",
}

# never link "homologous" in "homologous chromosomes / pairs" (the meiosis
# sense), which is not the homology of the common-ancestry chapter
EXTRA_PROTECT = [
    r"homologous (?:chromosomes?|pairs?)",
]

AMBIG_POLICY = "nearest-preceding"   # the volume re-defines chloroplast, chromosome, enzyme, protein
