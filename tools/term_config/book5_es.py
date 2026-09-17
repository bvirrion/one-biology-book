"""Book 5 -- es. Curation only; the rules live in tools/termlink/.

Curated 2026-09-17 from THIS edition's own harvest, after the twenty-seven
chapters and their solutions were translated, and after BOTH homograph
censuses against the English twin (per-target frequency AND per-target
chapter set). Nothing here was translated from book5_en.py or seeded from
book4_es.py.

Regenerate with:
  python3 tools/link_defined_terms.py --book 5 --lang es --unwrap --apply
  python3 tools/link_defined_terms.py --book 5 --lang es --apply
then a PLAIN dry run, which must report "links to insert: 0".

PROSE NOTES (Spanish homograph families in this volume)

  * Spanish collapses several English pairs that the English edition could
    keep apart by spelling or by compounding, so a few STOP entries here
    have NO counterpart in English:
      - "progenitor/progenitores" is BOTH the haematopoietic/intestinal
        progenitor cell (stem cells) AND the ordinary word for "parent",
        which the developmental-genetics, behavioural-ecology and
        conservation chapters use constantly.
      - "impronta" is both genomic imprinting (chromatin) and the
        gosling's imprinting (behaviour); English has one word too, and
        STOPs it, but in Spanish both senses are high-frequency.
      - "cubierta" is the vesicle coat AND the leaf canopy of the plant
        chapter AND the capsid/spore coat.
  * The rest of the list is the Spanish form of a collision the English
    edition had already found: lectura (read), dominio (domain),
    plegamiento (fold), semilla (seed), ensamblaje (assembly), perfil
    (profile), resolucion (resolution), nicho (niche), tolerancia
    (tolerance), transduccion (transduction), vector, induccion
    (induction), invasion (invasion), catastrofe (catastrophe), lesion
    (lesion), latencia (latency), envoltura (envelope), baston (rod),
    barrera (barrier), convergencia/divergencia.
  * "conjugacion" and "transformacion" are STOPped rather than protected
    by a collocation regex as in English: both are ordinary Spanish nouns
    (hormone conjugation, homeotic transformation, a mathematical
    transformation) and a regex would have to enumerate every context.

Entries are literal display strings, so each inflected and capitalised
form that occurs in the prose is listed.
"""

# Terms kept for their own chapter only (the harvest folds a STOPped term
# into the per-chapter local map).
STOP = {
    # sequencing read (genomics) against "lectura" = reading, read-out,
    # marco de lectura, la lectura de un gradiente
    "lectura", "lecturas", "Lectura", "Lecturas",
    # chromatin readers and writers against the ordinary reader/writer
    "lector", "lectores", "escritor", "escritores",
    # protein domain (structural biology) against domains of life and Hox
    # expression domains
    "dominio", "dominios", "Dominio", "Dominios",
    # protein folding against membrane folding and "un pliegue"
    "plegamiento", "plegamientos", "Plegamiento",
    # vesicle coat against the leaf canopy of the plant chapter, the
    # capsid/spore coat and the bacterial cell coat
    "cubierta", "cubiertas", "Cubierta", "Cubiertas",
    # BLAST seed against a plant's seeds (renal, plant, conservation)
    "semilla", "semillas", "Semilla", "Semillas",
    # genome assembly against protein, virus and spindle assembly
    "ensamblaje", "ensamblajes", "Ensamblaje", "Ensamblajes",
    # HMM profile (bioinformatics) against a hormone profile and the
    # profiles of tubules in a section
    "perfil", "perfiles", "Perfil", "Perfiles",
    # X-ray resolution against angular and phylogenetic resolution
    "resolución", "resoluciones", "Resolución",
    # stem-cell niche against the ecological niche
    "nicho", "nichos", "Nicho", "Nichos",
    # progenitor cell against "progenitor" = parent
    "progenitor", "progenitores", "Progenitor", "Progenitores",
    # immunological tolerance against drought, salt and drug tolerance
    "tolerancia", "tolerancias", "Tolerancia",
    # phage transduction against sensory transduction
    "transducción", "transducciones", "Transducción",
    # bacterial conjugation against hormone conjugation
    "conjugación", "conjugaciones", "Conjugación",
    # bacterial transformation against homeotic and other transformations
    "transformación", "transformaciones", "Transformación",
    # cloning vector against disease vectors
    "vector", "vectores", "Vector", "Vectores",
    # embryonic induction against enzyme induction and induced pluripotency
    "inducción", "inducciones", "Inducción",
    # tumour invasion against invasive species
    "invasión", "invasiones", "Invasión",
    # microtubule catastrophe against environmental catastrophes
    "catástrofe", "catástrofes", "Catástrofe", "Catástrofes",
    # DNA lesion against brain, spinal and hippocampal lesions
    "lesión", "lesiones", "Lesión", "Lesiones",
    # viral latency against reflex and response latency
    "latencia", "latencias", "Latencia",
    # viral envelope against the bacterial cell envelope
    "envoltura", "envolturas", "Envoltura",
    # retinal rod against rod-shaped bacteria
    "bastón", "bastones", "Bastón",
    # innate barriers against the blood--brain barrier and the boundary layer
    "barrera", "barreras", "Barrera", "Barreras",
    # neural convergence and divergence against sequence divergence
    "convergencia", "convergencias", "Convergencia",
    "divergencia", "divergencias", "Divergencia",
    # genomic imprinting (chromatin) is not the gosling's (behaviour)
    "impronta", "improntas", "Impronta",
    # thymic selection (adaptive immunity) against dN/dS selection
    "selección positiva", "selección negativa",
}

# Terms removed from the term set entirely.
DROP = set()

# display -> label, for a target harvest.py cannot reach on its own.
EXTRA = {}

# Regexes marking spans that must NOT be linked.
EXTRA_PROTECT = [
    # Spanish names the cell after the lineage ("linfocito~T", "linfocito~B")
    # where English names it after the letter ("T~cell"), so the HEAD word of
    # the compound is itself a linkable term and the generic
    # "linfocito" link fired on all seventy-four mentions of a T or B cell
    # against English's four. English's own "T cell" term never matches
    # "T~cell" either, so protecting the compound restores parity.
    r'linfocitos?~[TB]\b',
]

# Displays that must not be matched in their capitalised form.
NO_CAPITAL = set()

# University register: an ambiguous term links nowhere rather than to a guess.
AMBIG_POLICY = "drop"

# def:b3:rna-regulation:pirna is reachable in ENGLISH only through the PLURAL
# key "piRNAs" -- the singular harvests to the ncRNA definition instead -- so
# the target's reachability is an accident of English morphology and this
# language loses it silently. Recovered here on the CLUSTER phrase, which is
# English's other key for the same target ("piRNA clusters"), exactly as the
# id, ar and hi editions of this book did. Found by the Indonesian Book 5
# agent and confirmed by the Arabic and Hindi ones; added for this edition by
# the coordinator, 2026-09-17.
EXTRA = dict(EXTRA or {})
EXTRA["agrupamientos de ARNpi"] = "def:b3:rna-regulation:pirna"
