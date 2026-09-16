"""Book 4 -- nl. Curation only; the rules live in tools/termlink/.

Curated from THIS edition's own harvest (never seeded from book3_nl.py,
never translated from book4_en.py).

The one structural difference between Dutch and English here: harvest.py
only accepts an \\index{...} entry that sits OUTSIDE a definition when the
entry contains a space (`" " in d`). English terms such as "stroke volume",
"length constant" or "pollen tube" pass that test; their Dutch equivalents
are welded compounds -- slagvolume, lengteconstante, stuifmeelbuis -- and are
skipped, which silently cost this edition 54 of the English edition's 155
link targets. EXTRA below restores exactly those targets, one entry per
English surface that the English edition actually links, so the Dutch link
map mirrors the English one instead of inventing new senses.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --lang nl --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --lang nl --apply
"""

STOP = set()

NO_CAPITAL = set()

# Welded Dutch compounds that harvest.py's "must contain a space" rule skips
# outside a definition. Every value is a label of THIS book (b2), audited
# against the English edition's own \omterm targets.
EXTRA = {
    # chapter 1
    "oppervlakte-volumeverhouding": "prop:b2:unicellular-diversity:surface",
    # chapter 2
    "chemolithotroof": "def:b2:microbial-metabolism:trophic",
    "chemolithotrofie": "def:b2:microbial-metabolism:trophic",
    "elektronentoren": "thm:b2:microbial-metabolism:redox",
    "verdunningssnelheid": "thm:b2:microbial-metabolism:chemostat",
    # chapter 3
    "mutatiesnelheid": "thm:b2:genome-diversification:rate",
    "fluctuatietest": "thm:b2:genome-diversification:luria",
    "DNA-herstel": "prop:b2:genome-diversification:repair",
    # chapter 4
    "geslachtschromosomen": "prop:b2:meiosis-heredity:sexlinked",
    # chapter 6
    "stuifmeelkorrel": "prop:b2:angiosperm-reproduction:pollen",
    "embryozak": "prop:b2:angiosperm-reproduction:embryosac",
    "poolkernen": "prop:b2:angiosperm-reproduction:embryosac",
    "stuifmeelbuis": "thm:b2:angiosperm-reproduction:tube",
    # chapter 8-9
    "anti-müllerhormoon": "prop:b2:mammal-reproduction:sex",
    "in-vitrofertilisatie": "prop:b2:reproductive-hormones:clinic",
    "desensitisatie van receptoren": "prop:b2:reproductive-hormones:pulses",
    # chapter 11-12
    "progressiezone": "prop:b2:limb-organogenesis:aer",
    "fibroblastgroeifactor": "prop:b2:limb-organogenesis:aer",
    "transcriptiefactor": "prop:b2:cell-differentiation:transcriptional",
    "hoofdregulator": "prop:b2:cell-differentiation:transcriptional",
    # chapter 14-15
    "korte-dagplant": "prop:b2:plant-flowering:photoperiod",
    "lange-dagplant": "prop:b2:plant-flowering:photoperiod",
    "ABC-model": "prop:b2:plant-flowering:abc",
    "risicospreiding": "thm:b2:plant-flowering:bet",
    "zonneblad": "prop:b2:plant-plasticity:sunshade",
    "schaduwblad": "prop:b2:plant-plasticity:sunshade",
    "schaduwvermijding": "thm:b2:plant-plasticity:phytochrome",
    "hypothese van Cholodny--Went": "prop:b2:plant-plasticity:phototropism",
    "CAM-plant": "prop:b2:plant-plasticity:xerophytes",
    "hitteschokeiwit": "prop:b2:plant-plasticity:stress",
    # chapter 16-18
    "continuïteitsvergelijking": "thm:b2:blood-circulation:continuity",
    "polsdruk": "thm:b2:blood-circulation:windkessel",
    "hartcyclus": "prop:b2:heart:cycle",
    "slagvolume": "prop:b2:heart:cycle",
    "ejectiefractie": "prop:b2:heart:cycle",
    "druk-volumelus": "thm:b2:heart:work",
    # chapter 19
    "dissociatieconstante": "thm:b2:cell-signalling:occupancy",
    "receptorbezetting": "thm:b2:cell-signalling:occupancy",
    "receptortyrosinekinase": "prop:b2:cell-signalling:rtk",
    "kernreceptor": "prop:b2:cell-signalling:nuclear",
    # chapter 20-21
    "nernstpotentiaal": "thm:b2:neurons-synapses:nernst",
    "evenwichtspotentiaal": "thm:b2:neurons-synapses:nernst",
    "rustpotentiaal": "thm:b2:neurons-synapses:chord",
    "lengteconstante": "thm:b2:neurons-synapses:cable",
    "geleidingssnelheid": "thm:b2:neurons-synapses:cable",
    "glijdend filament": "prop:b2:muscle-movement:sliding",
    "dwarsbruggencyclus": "prop:b2:muscle-movement:crossbridge",
    "kracht-snelheidscurve": "thm:b2:muscle-movement:hill",
    "creatinefosfaat": "prop:b2:muscle-movement:energy",
    "zuurstofschuld": "prop:b2:muscle-movement:energy",
    # chapter 22-24
    "genenstroom": "prop:b2:population-genetics:migration",
    "inteeltcoëfficiënt": "prop:b2:population-genetics:inbreeding",
    "inteeltdepressie": "prop:b2:population-genetics:inbreeding",
    "erfelijkheidsgraad": "thm:b2:population-genetics:heritability",
    "fokkersvergelijking": "thm:b2:population-genetics:heritability",
    "hybridisatiezone": "prop:b2:speciation:reinforcement",
    "neighbour-joining": "ex:b2:phylogenetic-trees:parsimony",
    # chapter 25-27
    "boxmodel": "thm:b2:biogeochemical-cycles:box",
    "stikstofkringloop": "prop:b2:biogeochemical-cycles:nitrogen",
    "stikstofbinding": "prop:b2:biogeochemical-cycles:nitrogen",
    "dimethylsulfide": "prop:b2:biogeochemical-cycles:ps",
    "kationuitwisselingscapaciteit": "prop:b2:living-soil:cec",
    "veldcapaciteit": "prop:b2:living-soil:cec",
    "bodemvoedselweb": "prop:b2:living-soil:community",
    "bodemademhaling": "prop:b2:living-soil:humus",
    "strooiselafbraak": "thm:b2:living-soil:decay",
    "areaalverschuiving": "prop:b2:global-change:range",
    "verticale temperatuurgradiënt": "prop:b2:global-change:range",
    "verzadigingstoestand": "thm:b2:global-change:acid",
    "koraalverbleking": "thm:b2:global-change:acid",
    "soorten-oppervlakterelatie": "thm:b2:global-change:sar",
    "extinctiesnelheid": "thm:b2:global-change:sar",
    "extinctieschuld": "thm:b2:global-change:sar",
    "habitatverlies": "thm:b2:global-change:sar",
    # surfaces the prose actually carries for six more English targets
    "fermentatietechnologie": "def:b2:microbial-metabolism:fermentation",
    "glijdende filamenten": "prop:b2:muscle-movement:sliding",
    "hypothese van Cholodny en Went": "prop:b2:plant-plasticity:phototropism",
    "hitteschokeiwitten": "prop:b2:plant-plasticity:stress",
    "desensitisatie van de receptoren": "prop:b2:reproductive-hormones:pulses",
    "desensitisatie van de receptor": "prop:b2:reproductive-hormones:pulses",
}

# Homographs. "schors" is cortex, tree bark and the brain's cortex at once
# (the English edition links "cortex" nowhere, so dropping it mirrors it);
# "bloeden" is the verb "to bleed", manufactured by WORD_TAIL out of "bloed".
DROP = {"schors", "Schors"}

# Never consume a `$` (see tools/termlink/protect.py).
# WORD_TAIL turns "bloed" into "bloeden", which in Dutch is the verb "to
# bleed": the heading "Deel III --- Bloeden." was linked to the definition of
# blood. DROP cannot reach a form WORD_TAIL manufactures, so mask it here.
EXTRA_PROTECT = [
    r'(?<![\w])[Bb]loeden(?![\w])',
]

AMBIG_POLICY = "drop"
