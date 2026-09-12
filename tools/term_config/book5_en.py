"""Book 5 -- en. Curation only; the rules live in tools/termlink/.

University register (Year 3): the defined vocabulary is precise and links
nearly everywhere, but the volume spans twenty-seven fields and a fair
number of one-word terms carry a second sense in another chapter
(``read'' in genomics against the verb, ``niche'' in stem cells against
ecology, ``domain'' in structural biology against the tree of life and Hox
expression domains). Curated on 2026-09-11 after the English edition
landed, from a per-chapter census of every one-word linkable term.
Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 5 --unwrap --apply
  python3 tools/link_defined_terms.py --book 5 --apply

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").
"""

# STOP keeps each term for its own chapter (the harvest folds it into the
# per-chapter local map) and links nothing elsewhere: used for one-word
# terms whose other-chapter occurrences are a different sense.
STOP = {
    # sequencing "read" (genomics) against the verb everywhere
    "read", "Read",
    # chromatin readers and writers against "the reader"
    "reader", "writer",
    # protein domain (structural biology) against domains of life,
    # expression domains, mathematical domains
    "domain",
    # protein fold against "40-fold", "a fold of the membrane"
    "fold",
    # BLAST seed against plant seeds
    "seed",
    # genome assembly against protein and virus assembly
    "assembly", "Assembly",
    # HMM profile (bioinformatics) against a hormone or expression profile
    "profile",
    # X-ray resolution against the resolution of a conflict or an image
    "resolution",
    # stem-cell niche against the ecological niche
    "niche",
    # immunological tolerance against drought, salt and drug tolerance
    "tolerance",
    # phage transduction against sensory transduction
    "transduction",
    # cloning vector against disease vectors and the vectors of algebra
    "vector",
    # embryonic induction against enzyme induction and induced pluripotency
    "induction",
    # tumour invasion against invasive species
    "invasion",
    # microtubule catastrophe against environmental catastrophes
    "catastrophe",
    # vesicle coat against coat colour, spore coat, virus coat
    "coat",
    # innate barriers against the blood--brain barrier and others
    "barrier",
    # neural convergence and divergence against sequence divergence
    "convergence", "divergence",
    # DNA lesion against brain and tissue lesions
    "lesion",
    # viral latency against response latency
    "latency",
    # viral envelope against the bacterial cell envelope
    "envelope",
    # retinal rod against rod-shaped bacteria and viruses
    "rod",
    # genomic imprinting (chromatin) is not the gosling's (behaviour)
    "imprinting",
    # thymic selection (adaptive immunity) against dN/dS selection
    "positive selection", "negative selection",
}

NO_CAPITAL = set()

EXTRA = {}

DROP = set()

# Spans where a linkable word carries a sense the definition does not cover.
# Never consume a `$` (see tools/termlink/protect.py).
EXTRA_PROTECT = [
    # "complement" as the DNA strand or genetic complementation
    r'\bits own complement\b', r'\bthey \\emph\{complement\}',
    # hormone "conjugation" (plant physiology), not bacterial conjugation
    r'\bsynthesis, conjugation\b',
    # homeotic "transformation", not bacterial transformation
    r'\banterior transformation\b', r'\bhomeotic transformation\b',
    r'\bposterior transformation\b',
    # "alignment of interests" (microbiomes), not sequence alignment
    r'\balignment of interests\b',
]

AMBIG_POLICY = "drop"
