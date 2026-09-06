"""Book 3 -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-09-06 from THIS edition's OWN Dutch harvest, read in context.
Nothing here is translated from book3_en.py and nothing is seeded from
book2_nl.py: the English twin was consulted only for the *kind* of sense
collision a university biology volume has, and every entry below was then
re-decided on the Dutch word that actually carries it. Several English DROPs
are deliberately NOT repeated, because Dutch welds the compound that made the
English word ambiguous ("plasmamembraan", "aminozuur", "stamcel",
"spijsverteringskanaal") and the word boundary already protects it.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 3 --lang nl --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --lang nl --apply

Two Dutch-specific defect classes drive most of this file.

  * harvest.py skips any \\index entry WITHOUT A SPACE outside a definition.
    Dutch welds its compounds, so a proposition whose English key is
    "water-use efficiency" has the Dutch key "watergebruiksefficiëntie" and is
    never harvested at all. Thirty-three targets of the English twin were
    missing from the Dutch harvest for exactly this reason; every one of them
    is restored by an EXTRA below, found by a `comm` of the two target sets,
    not by eye.
  * lang_nl.py's WORD_TAIL is (?:e?[ns])?, which MANUFACTURES ordinary Dutch
    words out of single-word terms, and neither STOP nor DROP can reach a
    derived form -- only EXTRA_PROTECT can. It also cannot produce the
    plurals Dutch really uses (cel -> cellen, eiwit -> eiwitten, chromosoom ->
    chromosomen, blad -> bladeren, taxon -> taxa), which is the other half of
    the EXTRA list. Note what is deliberately absent: "genomen" is the plural
    of "genoom" AND the past participle of "nemen", so the genome target is
    left with its singular rather than linked to two hundred ordinary verbs.
"""

STOP = set()

NO_CAPITAL = set()

# Two kinds of entry, both counted in the bodies rather than guessed:
#   (a) the welded \index key of a target the harvest skipped entirely
#       (every label here is absent from the Dutch harvest and present in the
#       English one);
#   (b) the plural or singular that lang_nl.py's -e?[ns] tail cannot derive.
EXTRA = {
    # --- (a) targets the welded-key skip lost outright -------------------
    "darmwand": "prop:b1:body-plans-tissues:gutwall",
    "anomeer": "prop:b1:carbohydrates:rings",
    "haworthprojectie": "prop:b1:carbohydrates:rings",
    "pyranosering": "prop:b1:carbohydrates:rings",
    "furanosering": "prop:b1:carbohydrates:rings",
    "celwand": "prop:b1:carbohydrates:wall",
    "celtheorie": "prop:b1:cell-unit-of-life:theory",
    "pens": "prop:b1:digestion-absorption:cellulose",
    "herkauwer": "prop:b1:digestion-absorption:cellulose",
    "herkauwers": "prop:b1:digestion-absorption:cellulose",
    "achterdarmfermentatie": "prop:b1:digestion-absorption:cellulose",
    "verteringsenzym": "prop:b1:digestion-absorption:enzymes",
    "verteringsenzymen": "prop:b1:digestion-absorption:enzymes",
    "spijsverteringskanaal": "prop:b1:digestion-absorption:tract",
    "activeringsenergie": "prop:b1:enzymes:whatitdoes",
    "overgangstoestand": "prop:b1:enzymes:whatitdoes",
    "histonacetylering": "prop:b1:expression-control:chromatin",
    "DNA-methylering": "prop:b1:expression-control:chromatin",
    "mRNA-stabiliteit": "prop:b1:expression-control:posttranscriptional",
    "trp-operon": "prop:b1:expression-control:trp",
    "attenuatie": "prop:b1:expression-control:trp",
    "sigmafactor": "prop:b1:expression-control:trp",
    "koolzuuranhydrase": "prop:b1:gas-exchange:transport",
    "bohreffect": "prop:b1:gas-exchange:transport",
    "haldane-effect": "prop:b1:gas-exchange:transport",
    "genexpressie": "prop:b1:gene-expression:dogma",
    "transcriptie": "prop:b1:gene-expression:dogma",
    "translatie": "prop:b1:gene-expression:dogma",
    "splicing": "prop:b1:gene-expression:processing",
    "boodschapper-RNA": "prop:b1:gene-expression:processing",
    "poly-A-staart": "prop:b1:gene-expression:processing",
    "warmtebalans": "prop:b1:mammal-organization:heatbudget",
    "lichtreacties": "prop:b1:photosynthesis:lightreactions",
    "abscisinezuur": "prop:b1:plant-transport:opening",
    "watergebruiksefficiëntie": "prop:b1:plant-transport:wue",
    "nitraatreductase": "prop:b1:plant-water-minerals:nitrate",
    "nitrietreductase": "prop:b1:plant-water-minerals:nitrate",
    "stikstofassimilatie": "prop:b1:plant-water-minerals:nitrate",
    "worteldruk": "prop:b1:plant-water-minerals:rootpressure",
    "guttatie": "prop:b1:plant-water-minerals:rootpressure",
    "protonpomp": "prop:b1:plant-water-minerals:uptake",
    "protonpompen": "prop:b1:plant-water-minerals:uptake",
    "populatiecyclus": "prop:b1:populations:cycles",
    "dichtheidsafhankelijkheid": "prop:b1:populations:densitydependence",
    "dichtheidsafhankelijke": "prop:b1:populations:densitydependence",
    "celademhaling": "prop:b1:respiration-fermentation:overview",
    "pasteureffect": "prop:b1:respiration-fermentation:pasteur",
    "eilandbiogeografie": "thm:b1:ecosystem-dynamics:island",
    "nernstvergelijking": "thm:b1:membranes-transport:nernst",
    "evenwichtspotentiaal": "thm:b1:membranes-transport:nernst",
    "chemiosmose": "thm:b1:photosynthesis:chemiosmosis",
    "ATP-synthase": "thm:b1:photosynthesis:chemiosmosis",
    "transpiratie": "thm:b1:plant-transport:cohesiontension",
    "drukstroommechanisme": "thm:b1:plant-transport:pressureflow",
    "eiwitvouwing": "thm:b1:proteins:anfinsen",
    "schijfvergelijking": "thm:b1:species-interactions:holling",
    "aanvalstempo": "thm:b1:species-interactions:holling",
    "hanteertijd": "def:b1:species-interactions:functional",
    "henderson-hasselbalchvergelijking": "thm:b1:water-small-molecules:hh",
    # --- (b) forms the -e?[ns] tail cannot produce ------------------------
    # Dutch doubles the consonant, drops a vowel or takes a foreign plural;
    # every one of these was counted as a standalone surface form in the
    # bodies before it was added.
    "cellen": "def:b1:cell-unit-of-life:cell",
    "aminozuren": "def:b1:proteins:aminoacid",
    "organen": "def:b1:mammal-organization:organ",
    "vetten": "def:b1:lipids:triglyceride",
    "lysosomen": "def:b1:eukaryotic-cell:endomembrane",
    "eiwitten": "def:b1:proteins:peptide",
    # English sends "organelles" to the prokaryote/eukaryote definition, not
    # to the organelle definition of chapter 6; matched here.
    "organellen": "def:b1:cell-unit-of-life:prokeuk",
    "chromosomen": "def:b1:genomes:genome",
    "ribosomen": "def:b1:gene-expression:ribosome",
    "mitochondriën": "def:b1:eukaryotic-cell:mitochondrion",
    "bladeren": "def:b1:flowering-plant-organization:organs",
    "kanalen": "def:b1:membranes-transport:transporters",
    "meristemen": "def:b1:flowering-plant-organization:meristem",
    "taxa": "def:b1:classifying-biodiversity:nomenclature",
    "virussen": "def:b1:genomes:virus",
    "biotopen": "def:b1:ecosystem-organization:ecosystem",
    "ecosystemen": "def:b1:ecosystem-organization:ecosystem",
    "levensgemeenschappen": "def:b1:ecosystem-organization:ecosystem",
    "biomen": "prop:b1:ecosystem-organization:biomes",
    "fotosystemen": "def:b1:photosynthesis:zscheme",
    "korstmossen": "def:b1:species-interactions:symbiosis",
    "basenparen": "thm:b1:nucleic-acids:helix",
    "microtubuli": "def:b1:eukaryotic-cell:cytoskeleton",
    "transcriptiefactoren": "def:b1:expression-control:enhancer",
    "cofactoren": "def:b1:enzymes:enzyme",
    "sluitcellen": "def:b1:plant-transport:stoma",
    "wortelharen": "def:b1:flowering-plant-organization:organs",
    "darmvlokken": "def:b1:digestion-absorption:surface",
    "chylomicronen": "prop:b1:digestion-absorption:routes",
    "wortelknolletjes": "def:b1:plant-water-minerals:nodules",
    "zeefvaten": "def:b1:plant-transport:phloem",
    "xyleemvat": "def:b1:plant-transport:xylem",
    "xyleemvaten": "def:b1:plant-transport:xylem",
    "tracheïden": "def:b1:plant-transport:xylem",
    "huidmondjes": "def:b1:plant-transport:stoma",
    "longblaasjes": "def:b1:gas-exchange:lung",
    "vluchtige vetzuren": "prop:b1:digestion-absorption:cellulose",
    "isoclinen": "prop:b1:species-interactions:lotka",
    # welded key again ("controlepunt"); English reaches this target through
    # its own EXTRA "checkpoint(s)", added 2026-09-06.
    "controlepunt": "prop:b1:replication-mitosis:checkpoints",
    "controlepunten": "prop:b1:replication-mitosis:checkpoints",
    # harvested as the bare adjective "Integrale"; the prose always says
    # the full noun phrase, exactly as English does ("integral proteins").
    "integrale eiwitten": "def:b1:membranes-transport:proteins",
    "peroxisoom": "def:b1:eukaryotic-cell:peroxisome",
    "peroxisomen": "def:b1:eukaryotic-cell:peroxisome",
    # the only lowercase "wassen" in the volume is the plural of the wax of
    # chapter 9; the singular "was" is DROPped below because it is the past
    # tense of "zijn", so without this line the wax target is an orphan.
    "wassen": "def:b1:lipids:wax",
    "xerofyt": "prop:b1:flowering-plant-organization:plasticity",
    "xerofyten": "prop:b1:flowering-plant-organization:plasticity",
    "hydrofyt": "prop:b1:flowering-plant-organization:plasticity",
    "hydrofyten": "prop:b1:flowering-plant-organization:plasticity",
    "fenotypische plasticiteit": "prop:b1:flowering-plant-organization:plasticity",
    "signaalpeptide": "prop:b1:gene-expression:after",
    "posttranslationele modificatie": "prop:b1:gene-expression:after",
    "uitwisselingsoppervlak": "prop:b1:organism-environment:surfaces",
    "uitwisselingsoppervlakken": "prop:b1:organism-environment:surfaces",
    "michaelis-mentenvergelijking": "thm:b1:enzymes:mm",
    "michaelisconstante": "thm:b1:enzymes:mm",
    "omzetgetal": "thm:b1:enzymes:mm",
}

DROP = {
    # The four exchanges of the open system and the five functions of the
    # organism are, in Dutch as in English, ordinary words on every page:
    # "de energie van een binding", "de omgeving van de wortel", "de relatie
    # tussen twee grootheden". 180 uses of "energie" and 497 of "water"
    # would each carry a link to chapter 1 or chapter 8.
    "energie", "materie", "informatie", "omgeving", "relatie",
    "voortplanting", "voeding", "herkenning", "water",
    # DUTCH-ONLY, and the single most damaging entry in this file: "was" is
    # the wax of the lipid chapter AND the past tense of "zijn". 48 of its 49
    # occurrences in this volume are the verb. The capitalised "Wassen" of
    # the definition's own display is left, so the target is not orphaned.
    "was",
    # "vat" is a xylem vessel, a blood vessel, Pasteur's flask and the
    # hundred-litre vat of a cow's rumen -- 54 uses, four senses, one word.
    # English DROPs "vessel(s)" for two of these. The xylem sense is
    # recovered by the welded "xyleemvat(en)" in EXTRA above.
    "vat",
    # the phloem's source and sink. "bron" is also the limestone SPRING that
    # the whole of chapter 26 is built on (32 uses) and the "bronvoorraad" of
    # the island model; "put" is a well. English DROPs "source" and "sink"
    # and loses the phloem target with them; so does Dutch.
    "bron", "put",
    # plant node, but also the knot of a rope and -- in chapter 29 -- every
    # node of a cladogram. English DROPs "node".
    "knoop",
    # "kenmerk" is the systematist's character, but in Dutch it is also the
    # ordinary word for a feature or property, used 63 times across the
    # volume ("de vier kenmerken die de flux verhogen"). English DROPs
    # "character" for the same reason.
    "kenmerk",
    # ecological resistance versus the resistance of a prey to a toxin and
    # the resistance of water to flow.
    "weerstand",
    # the mitochondrial matrix versus the extracellular matrix of chapter 4
    # and the cellulose matrix of the cell wall.
    "matrix",
    # the membrane pump versus the verb: "water over haar kieuwen pompen",
    # "protonen uit te pompen". 50 uses, most of them the verb.
    "pomp", "Pompen",
    # a condensation reaction versus the condensation of a chromosome;
    # "denaturatie" is disambiguated by the two parenthesised keys, which
    # are kept, so only the bare word goes.
    "condensatie", "denaturatie",
    # a saturated fatty acid versus a saturated enzyme, saturated air and
    # the percentage saturation of haemoglobin in chapters 12 and 21. The
    # two-word keys "verzadigd vetzuur" / "onverzadigd vetzuur" are kept.
    "verzadigd", "onverzadigd",
    # competitive inhibition versus competitive exclusion: two different
    # targets share the bare adjective, so it can only be wrong.
    "competitief",
    # the plant epidermis of chapters 3 and 24 versus the epidermis of skin.
    "epidermis",
    # UV absorbance at 260 nm and the absorption of light by a pigment
    # versus absorption in the gut, which is what the term is defined as.
    "absorptie",
    # a bare adjective; the two-word "hydrostatisch skelet" is kept.
    "hydrostatisch", "onbepaald",
    # DUTCH-ONLY. "snelheid" is the reaction rate of chapter 13, but it is
    # also the plain Dutch word for speed, and it carried 57 links --
    # the speed of sap in a sequoia, of a sprinting horse, of succession.
    # English DROPs "rate" for exactly this.
    "snelheid",
    # DUTCH-ONLY. The microscope "resolves" two points; the Dutch verb
    # "scheidt" also means separates and secretes, and all twelve of its
    # links were the other two senses (a gland that "scheidt 10 g per dag
    # af", a centrifuge that "scheidt op grootte"). English DROPs "resolves".
    "scheidt",
}

# WORD_TAIL manufactures forms that STOP and DROP cannot see, and a few
# legitimate terms carry a second, ordinary sense in one or two phrases only
# -- too few to justify losing the term, so the phrase is masked instead.
EXTRA_PROTECT = [
    # "kanaal/kanalen" is the membrane channel in 20 of its 23 uses; these
    # two are the physical routes of exchange in chapter 1 and the water
    # passages between a fish's gill lamellae in chapter 21.
    r"vier fysische kanalen",
    r"kanalen van een fractie",
    # "skelet" is the body skeleton of chapter 4 in nine of its twelve uses,
    # but chapters 5 and 6 call the CYTOskeleton "het skelet van de cel".
    # DROPping the word would cost the nine; these two phrases are masked.
    r"skelet dat de vorm",
    r"inwendig skelet van",
    # DUTCH-ONLY, and invisible to STOP and DROP because WORD_TAIL DERIVES
    # it: "blad" + -en = "bladen", which in this volume is never a plant
    # leaf (that plural is "bladeren", linked 63 times) but always the two
    # LEAFLETS of a lipid bilayer and the leaves of a cow's omasum. All
    # nine of its links pointed at the leaf definition of chapter 3.
    r"bladen",
]

AMBIG_POLICY = "drop"   # university register; matches book3_en.py
