"""Book 4 -- es. Curation only; the rules live in tools/termlink/.

University register (Year 2), so AMBIG_POLICY is "drop", as in book4_en.py.

CURATED 2026-09-16 FROM THIS EDITION'S OWN HARVEST. Nothing here was seeded
from book3_es.py or translated from book4_en.py: every entry below was found
by censusing the Spanish links themselves (per-target frequency against the
English twin, per-target chapter set) and each flagged link was read in
context before it was written down.

The levers, as used here:
  * STOP keeps a term only in the chapter that defines it (the per-chapter
    map): right for a word whose defined sense lives in one chapter and whose
    other senses turn up later in the book.
  * EXTRA_PROTECT masks a collocation where the ordinary sense is certain,
    so the term keeps its links in the chapters that do use the defined sense.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --lang es --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --lang es --apply
"""

STOP = {
    # --- "óvulo" is the plant OVULE of ch. 5 (heterospory) and, in Spanish,
    # also the animal EGG: 33 links in ch. 8, 9, 12 and 23 ("un óvulo humano",
    # "el óvulo fecundado", "un óvulo de oveja") pointed at the heterospory
    # definition. The two senses cannot be told apart by collocation ("el
    # óvulo", "del óvulo" occur in both), so the term keeps only its defining
    # chapter. English links "ovule" in ch. 5 and 6 only.
    "óvulo", "óvulos",
    # --- "ovario" is the flower's ovary (ch. 6); in ch. 8 and 9 it is the
    # mammalian ovary (7 links). English links "ovary" in ch. 6 only.
    "ovario", "ovarios",
    # --- "potencia" is cell POTENCY in ch. 12 and physical POWER (the heart's
    # work rate, muscle power, "la cuarta potencia del radio", "una potencia
    # del área") in ch. 16, 17, 18, 21 and 27: 20 wrong links. English links
    # "potency" in ch. 12 only.
    "potencia", "Potencia",
    # --- "competencia" is embryonic COMPETENCE in ch. 10 and ecological
    # COMPETITION in ch. 23 and 27 (10 wrong links). English links
    # "competence" in ch. 10 and 12.
    "competencia",
    # --- "inducción" is embryonic induction in ch. 10; in ch. 14 it is
    # FLORAL induction (7 links) and in ch. 19 mathematical induction ("por
    # inducción, $a^{n}$"). English links "induction" in ch. 10 only.
    "inducción", "Inducción",
    # --- "transformación" is bacterial transformation (horizontal gene
    # transfer, ch. 3); in ch. 6 it is the ordinary "toda esa transformación"
    # of an ovule into a seed. English links "transformation" in ch. 3 only.
    "transformación", "Transformación",
}

NO_CAPITAL = set()

EXTRA = {
    # Spanish drops the accent in the plural of a term ending in "-ón"
    # ("mutación" -> "mutaciones"), so WORD_TAIL, which can only add an s or
    # an es, never reaches these forms. Every one was checked to occur in the
    # book and to carry the defined sense; "mutaciones" alone is 53 uses.
    "mutaciones": "def:b2:genome-diversification:mutation",
    "transposones": "def:b2:genome-diversification:transposon",
    "retrotransposones": "def:b2:genome-diversification:transposon",
    "fermentaciones": "def:b2:microbial-metabolism:fermentation",
    "segmentaciones": "def:b2:vertebrate-development:egg",
    "cotiledones": "def:b2:angiosperm-reproduction:seed",
    "axones": "def:b2:neurons-synapses:neuron",
    "adaptaciones": "def:b2:plant-plasticity:plasticity",
    "ovulaciones": "def:b2:mammal-reproduction:ovary",
    # the trophic-type definition is displayed in Spanish by the welded
    # compounds the harvest cannot key ("quimiolitotrofia", the noun of the
    # Winogradsky caption, and its adjective), where English links
    # "chemolithotrophy"/"chemolithotrophs" 4 times.
    "quimiolitotrofia": "def:b2:microbial-metabolism:trophic",
    "quimiolitótrofos": "def:b2:microbial-metabolism:trophic",
    "quimiolitótrofas": "def:b2:microbial-metabolism:trophic",
}

DROP = set()

# Never consume a `$` (see tools/termlink/protect.py).
EXTRA_PROTECT = [
    # "corteza" is BARK (ch. 13, and the sooty bark of the moths in ch. 22),
    # but the adrenal and motor CORTEX in ch. 18 and 21 (6 wrong links).
    r'corteza(?=\s+(?:suprarrenal|motora|envía|o\s+de\s+un\s+reflejo))',
    # "latencia" is seed DORMANCY (ch. 6, 7, 14), but the LATENCY of a reflex
    # in ch. 20 and a dormant microbial biomass in the soil problem (ch. 26).
    r'latencia(?=\s+(?:medida|calculada|mecánica))',
    r'(?<=en )latencia(?=\))',
    # "sangre" in "animales de sangre caliente" (ch. 24) is not the blood
    # definition.
    r'sangre(?=\s+caliente)',
    # "dominante" is the dominant ALLELE; in ch. 9 it is the dominant
    # FOLLICLE, and in the ch. 18 solutions "la presión dominante".
    # (a lookbehind on "folículo" would not survive re-linking, because
    # "folículo" is itself a linked term: key on what follows instead)
    r'dominante(?=\.\s+En\s+el\s+útero|\s+y\s+hace\s+madurar)',
    r'(?<=salvo al )dominante',
    r'(?<=presión )dominante',
    # "gemación" is the budding of unicellular organisms (ch. 1, 7); in ch. 10
    # the gut tube buds off the lungs and liver.
    r'gemación(?=\s+los\s+pulmones)',
]

AMBIG_POLICY = "drop"
