"""Book 5 -- nl. Curation only; the rules live in tools/termlink/.

STUB. The edition agent fills this in from THIS edition's OWN harvest --
never by translating book5_en.py, and never by seeding from book4_nl.py.
A seeded EXTRA points at the other book's labels and ships as undefined
references; a seeded EXTRA_PROTECT masks the links you wanted. (You may read
book4_nl.py's PROSE NOTES for the language's homograph families -- that
knowledge does carry over -- but re-derive every key here.)

Procedure (translation_instruction.md section 5):

  1. Translate the bodies, then run the harvest and read the candidate list.
  2. Run BOTH homograph censuses against the English twin -- per-target
     frequency AND per-target chapter set. Neither is sufficient alone.
  3. Decide each flag by reading the link in context, never by the ratio.
  4. Regenerate:
       python3 tools/link_defined_terms.py --book 5 --lang nl --unwrap --apply
       python3 tools/link_defined_terms.py --book 5 --lang nl --apply
  5. Then a PLAIN dry run over the wrapped tree -- "links to insert" must be 0:
       python3 tools/link_defined_terms.py --book 5 --lang nl
     Anything else is a protect pattern that has stopped protecting (do not
     anchor a lookaround on a word that is itself a linked term).

English's own curation for this volume is a 28-word STOP list: Book 5 spans
twenty-seven fields, and one-word terms ("read", "domain", "fold", "seed",
"niche", "tolerance", "vector", "coat", "rod", "imprinting"...) change sense
between chapters, so STOP keeps each in its own chapter. Ask which of those
collisions survive translation and which new ones the target language mints
of its own -- the answer is different for every language.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").
"""

# Terms kept for their own chapter only (the harvest folds a STOPped term
# into the per-chapter local map).
STOP = {
    # Curated 2026-09-17 from the per-target CHAPTER-SET census against the
    # English twin: each of these is a Dutch one-word term that reached
    # chapters its English counterpart does not, in a second sense.  STOP
    # keeps it linked in its own chapter and nowhere else.
    # protein domain (ch 7) against domains of life, expression domains and
    # topologically associating domains -- it reached eight other chapters
    "domein", "domeinen",
    # DNA lesion (ch 3) against the clinical lesion of chs 17, 19 and 21
    "laesie", "laesies",
    # the vesicle coat (ch 8) against the endospore coat (ch 12) and the
    # phage coat (ch 13)
    "mantel", "mantels",
    # genome assembly (ch 4) against virus assembly (chs 13, 15)
    "assemblage", "Assemblage",
    # neural convergence and divergence (ch 17) against sequence divergence
    # (ch 25)
    "divergentie", "convergentie",
    # viral latency (ch 13) against the latency of a reflex (ch 17)
    "latentie", "Latenties",
    # bacterial transformation (ch 12) against the homeotic transformation of
    # a vertebra (ch 23)
    "transformatie", "Transformatie",
    # bacterial conjugation (ch 12) against auxin conjugation (ch 22)
    "conjugatie", "Conjugatie",
    # immunological tolerance (ch 16) against the glucose tolerance test (ch 21)
    "tolerantie",
    # the HMM profile of bioinformatics (ch 5) against a concentration
    # profile (ch 23)
    "profiel",
    # the innate barriers (ch 15) against the glomerular filtration barrier
    # (ch 20)
    "barrière", "barrières",
    # viral reassortment (ch 13) against the rearrangement of the antibody
    # locus (ch 16)
    "herschikking",
}

# Terms removed from the term set entirely -- the lever for a true homograph,
# where STOP's per-chapter fall-through would still leave wrong links.
DROP = set()

# display -> label, for a target harvest.py cannot reach on its own (a welded
# or hyphenated compound, or a term whose head word is in NOT_A_TERM).
# AUDIT every entry against parts/bachelor-3/'s OWN label set before use.
EXTRA = {
    # Derived 2026-09-17 from THIS edition's own harvest: the 39 English
    # targets that the Dutch tree could not reach.  Dutch welds its compounds
    # ("genoomgrootte", "mismatchherstel", "kabelvergelijking"), so the
    # \index{} key of a theorem/proposition/method carries no space and
    # harvest.py's outside-a-definition rule skips it.  A handful more are
    # phrases whose Dutch inflection (adjectival -e, plural -en) the linker's
    # WORD_TAIL does not cover.  Every label below was checked against
    # parts/bachelor-3/'s own \label{} set.
    # ch 1 chromatin
    "pakkingsgraad": "prop:b3:chromatin-epigenetics:compaction",
    "positie-effectvariegatie": "prop:b3:chromatin-epigenetics:examples",
    "bisulfietsequencing": "met:b3:chromatin-epigenetics:bisulfite",
    # ch 2 RNA regulation
    "piRNA": "def:b3:rna-regulation:pirna",
    # ch 3 DNA repair
    "mismatchherstel": "prop:b3:dna-repair:fidelity",
    "SOS-respons": "prop:b3:dna-repair:sos",
    # ch 4 genomics
    "genoomgrootte": "prop:b3:genomics:sizes",
    # ch 5 bioinformatics
    "homologiemodellering": "prop:b3:bioinformatics:structure",
    "structuurvoorspelling": "prop:b3:bioinformatics:structure",
    "bitscore": "thm:b3:bioinformatics:evalue",
    # ch 6 genetic engineering
    "basebewerker": "prop:b3:genetic-engineering:editors",
    "prime-bewerker": "prop:b3:genetic-engineering:editors",
    "gendrive": "thm:b3:genetic-engineering:drive",
    "drempelcyclus": "thm:b3:genetic-engineering:pcr",
    # ch 7 structural biology
    "vouwtrechter": "thm:b3:structural-biology:levinthal",
    "hydrofobe effect": "prop:b3:structural-biology:forces",
    "Bohr-effect": "prop:b3:structural-biology:mechanism",
    # ch 8 membrane traffic
    "cisternerijping": "prop:b3:membrane-traffic:golgi",
    # NOT "golgiapparaat": the bare Dutch compound occurs 29 times in its own
    # chapter, where English links "Golgi apparatus" once; "cisternerijping"
    # alone reaches the target.
    # ch 10 cell cycle
    "retinoblastoma-eiwit": "prop:b3:cell-cycle-apoptosis:rb",
    # ch 11 cancer
    "amestest": "met:b3:cancer-biology:ames",
    "immuunontwijking": "prop:b3:cancer-biology:immune",
    "controlepuntremmer": "prop:b3:cancer-biology:immune",
    "Wnt-route": "prop:b3:cancer-biology:pathways",
    "PI3K-route": "prop:b3:cancer-biology:pathways",
    "combinatietherapie": "thm:b3:cancer-biology:goldie-coldman",
    # ch 12 bacteriology
    "antibioticaresistentie": "def:b3:bacteriology:resistance",
    "resistentie tegen antibiotica": "def:b3:bacteriology:resistance",
    "gramkleuring": "met:b3:bacteriology:gram",
    "bouillonverdunning": "met:b3:bacteriology:mic",
    "verdunningssnelheid": "thm:b3:bacteriology:monod",
    # ch 14 microbiomes
    "operationele taxonomische eenheden": "met:b3:microbiomes:16s",
    # ch 16 adaptive immunity
    "SIR-model": "thm:b3:adaptive-immunity:herd",
    # ch 17 nervous systems
    "kabelvergelijking": "thm:b3:nervous-systems:cable",
    "lengteconstante": "thm:b3:nervous-systems:cable",
    "hersenvocht": "prop:b3:nervous-systems:barrier-budget",
    # ch 18 sensory systems
    "frequentie-van-zien-kromme": "thm:b3:sensory-systems:hecht",
    # ch 20 renal
    "tegenstroomvermenigvuldiging": "prop:b3:renal-osmoregulation:countercurrent",
    "enkelvoudige effect": "prop:b3:renal-osmoregulation:countercurrent",
    "vrijwaterklaring": "prop:b3:renal-osmoregulation:water",
    # ch 21 endocrinology
    "glucosetolerantietest": "met:b3:endocrinology:ogtt",
    "reservereceptoren": "prop:b3:endocrinology:dose",
    "schildklierhormoon": "prop:b3:endocrinology:thyroid",
    # ch 22 plant physiology
    "foto-evenwicht": "prop:b3:plant-molecular-physiology:photoequilibrium",
    "schaduwontwijking": "prop:b3:plant-molecular-physiology:photoequilibrium",
    "polaire auxinetransport": "thm:b3:plant-molecular-physiology:auxin",
    "polair auxinetransport": "thm:b3:plant-molecular-physiology:auxin",
    # ch 23 developmental genetics
    "vervallengte": "thm:b3:developmental-genetics:gradient",
    # ch 27 conservation
    "soort--oppervlakteverband": "prop:b3:conservation-biology:area",
    "eilandbiogeografie": "prop:b3:conservation-biology:area",
    "randeffect": "prop:b3:conservation-biology:area",
    # --- Dutch inflection the linker's WORD_TAIL "(?:e?[ns])?" cannot make:
    # a doubled consonant (stamcel -> stamcellen), a shortened vowel
    # (hormoon -> hormonen, macrofaag -> macrofagen), a Latin plural
    # (microtubulus -> microtubuli) or the apostrophe plural of an
    # abbreviation (siRNA -> siRNA's).  Each display below was read in
    # context; they are the same sense as the singular already linked.
    "stamcellen": "def:b3:stem-cells:stem",
    "voorlopercel": "def:b3:stem-cells:stem",
    "voorlopercellen": "def:b3:stem-cells:stem",
    "nucleosomen": "def:b3:chromatin-epigenetics:nucleosome",
    "hormonen": "def:b3:endocrinology:hormone",
    "macrofagen": "def:b3:innate-immunity:innate",
    "dendritische cellen": "def:b3:innate-immunity:innate",
    "natuurlijke doodcellen": "def:b3:innate-immunity:innate",
    "microtubulus": "def:b3:cytoskeleton-motility:filaments",
    "microtubuli": "def:b3:cytoskeleton-motility:filaments",
    "centrosomen": "def:b3:cytoskeleton-motility:filaments",
    "intermediaire filamenten": "def:b3:cytoskeleton-motility:filaments",
    "antibiotica": "def:b3:bacteriology:antibiotics",
    "gramnegatieve": "def:b3:bacteriology:envelope",
    "grampositieve": "def:b3:bacteriology:envelope",
    "microRNA's": "def:b3:rna-regulation:ncrna",
    "siRNA's": "def:b3:rna-regulation:ncrna",
    "piRNA's": "def:b3:rna-regulation:pirna",
    "haarcellen": "def:b3:sensory-systems:cochlea",
    "basilaire membraan": "def:b3:sensory-systems:cochlea",
    "NMDA-receptor": "prop:b3:learning-memory:nmda",
    "AMPA-receptoren": "prop:b3:learning-memory:nmda",
    "plasmacellen": "def:b3:adaptive-immunity:response",
    "geheugencel": "def:b3:adaptive-immunity:response",
    "geheugencellen": "def:b3:adaptive-immunity:response",
    "lusversterking": "thm:b3:endocrinology:loop",
    "instelpunt": "thm:b3:endocrinology:loop",
    "soortboom": "prop:b3:molecular-evolution:ils",
    "genboom": "prop:b3:molecular-evolution:ils",
    "genbomen": "prop:b3:molecular-evolution:ils",
    "ortholoog": "def:b3:genomics:comparative",
    "orthologen": "def:b3:genomics:comparative",
    "geslachtsverhouding": "thm:b3:conservation-biology:ne",
    "inteeltcoëfficiënt": "thm:b3:conservation-biology:ne",
    "substitutietempo": "thm:b3:molecular-evolution:neutral",
    "fixatiekans": "thm:b3:molecular-evolution:neutral",
    "sluitcel": "prop:b3:plant-molecular-physiology:stomata",
    "sluitcellen": "prop:b3:plant-molecular-physiology:stomata",
    "Panethcel": "prop:b3:stem-cells:crypt",
    "Panethcellen": "prop:b3:stem-cells:crypt",
    "blokkeerkracht": "prop:b3:cytoskeleton-motility:physics",
}

# Regexes marking spans that must NOT be linked (a collocation where the term
# carries another sense). Never anchor one on a word that is itself a term.
EXTRA_PROTECT = []

# Displays that must not be matched in their capitalised form.
NO_CAPITAL = set()

# University register: an ambiguous term links nowhere rather than to a guess.
AMBIG_POLICY = "drop"
