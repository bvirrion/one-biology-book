"""Book 3 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Curated 2026-09-06 from THIS edition's own harvest
(python3 tools/link_defined_terms.py --book 3 --lang pt --terms), never
seeded from book3_en.py and never from book2_pt.py: every EXTRA value below
was checked against the labels actually defined in parts/bachelor-1/, and
every DROP was chosen after counting, target by target, what the key links
in this volume against what the English twin links.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 3 --lang pt --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --lang pt --apply

Two Portuguese-specific facts shaped this file.

1. WORD_TAIL is "(?:e?s)?" on every word, so it makes regular plurals
   (celula -> celulas, decompositor -> decompositores) but cannot make the
   "-ao" -> "-oes" or "-al" -> "-ais" ones, nor agree an adjective after a
   pluralised head. Every such plural is therefore invisible to the linker
   and has to be added by hand: "pulmoes" alone was 54 lost links, "orgaos"
   38, "populacoes" 19, "ligacoes covalentes" 5. They are the bulk of EXTRA.

2. The collisions are not the English ones. English STOPs "substrate"
   because its rock sense is everywhere; in Portuguese "substrato" is the
   enzyme sense in eleven places and the succession sense in exactly two,
   so it stays linked and the two sites are masked instead. Conversely
   "aumento" is at once magnification and the ordinary word for an
   increase, and "relacao"/"reproducao"/"nutricao" are the three functions
   of the mammal chapter and ordinary nouns everywhere else -- neither
   collides in English.
"""

# Nothing needs STOP: every risky word is either a whole harvested key
# (DROP) or a handful of sites (EXTRA_PROTECT).
STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # --- irregular plurals the "(?:e?s)?" tail cannot build ("-ao" ---
    # --- "-oes", "-al" -> "-ais"), all single-sense in this volume ---
    "pulmões": "def:b1:gas-exchange:lung",
    "órgãos": "def:b1:mammal-organization:organ",
    "populações": "def:b1:populations:population",
    "tampões": "def:b1:water-small-molecules:buffer",
    "perturbações": "def:b1:ecosystem-dynamics:disturbance",
    "sucessões": "def:b1:ecosystem-dynamics:succession",
    "fermentações": "def:b1:respiration-fermentation:fermentation",
    "predações": "def:b1:species-interactions:types",
    "razões P/O": "thm:b1:respiration-fermentation:chemiosmosis",
    "fosforilações em nível de substrato": "def:b1:respiration-fermentation:glycolysis",
    "níveis tróficos": "def:b1:ecosystem-organization:trophic",
    "potenciais hídricos": "def:b1:membranes-transport:osmosis",
    # --- a pluralised head plus an agreed adjective: the tail pluralises
    # --- each word but cannot turn "ligacao" into "ligacoes" ---
    "ligações covalentes": "def:b1:water-small-molecules:bonds",
    "ligações não covalentes": "def:b1:water-small-molecules:bonds",
    "ligações peptídicas": "def:b1:proteins:peptide",
    "ligações glicosídicas": "def:b1:carbohydrates:glycosidic",
    "junções celulares": "def:b1:body-plans-tissues:epithelium",
    # --- singulars of keys the harvest folded to the plural, and terms
    # --- the harvest missed; each target shipped with zero links ---
    "xerófita": "prop:b1:flowering-plant-organization:plasticity",
    "hidrófita": "prop:b1:flowering-plant-organization:plasticity",
    "peptídeo-sinal": "prop:b1:gene-expression:after",
    "nitrato-redutase": "prop:b1:plant-water-minerals:nitrate",
    "ATP-sintase": "thm:b1:photosynthesis:chemiosmosis",
    # The harvested key is the three-word "complexo de Golgi"; the prose
    # says the bare "Golgi" (the stack, its cis face, the ER-to-Golgi step)
    # 25 further times and never means Camillo Golgi the person, so this
    # cannot mint a wrong link. Mirrors the same entry in book3_en.py.
    "Golgi": "def:b1:eukaryotic-cell:endomembrane",
}

DROP = {
    # the four exchanges of the open system are the ordinary words for
    # energy, matter and information: 255 links against English's 0
    "energia", "matéria", "informação",
    # the three "functions" of the mammal chapter are ordinary nouns
    # (a relation between two variables, sexual reproduction, plant
    # nutrition): 24 links against English's 0
    "relação", "reprodução", "nutrição",
    # water the molecule versus water everywhere: 349 links
    "água",
    # "acido" as the pH partner of a base versus every fatty, nucleic,
    # carbonic and amino acid in the volume: 113 links against 89 total
    "ácido",
    # reaction rate versus the speed of sap, of a nerve, of a flow:
    # 90 links against English's 0 ("rate" is DROPped there too)
    "velocidade",
    # xylem vessel versus blood vessel; plant epidermis versus skin
    "vaso", "vasos", "epiderme",
    # membrane pump and carrier versus the electron carriers, the proton
    # pump and a bee "carrying" pollen
    "bomba", "bombas", "carreador", "carreadores",
    # endo/exoskeleton versus the carbon skeleton of six chapters and the
    # bony skeleton of the cladogram; the hydrostatic skeleton keeps its
    # own key
    "esqueleto", "hidrostático",
    # blood plasma versus the plasma membrane of twenty chapters
    "plasma",
    # systematic character versus the character of a curve or a soil
    "caráter",
    # the organism's environment versus every ordinary environment
    "ambiente",
    # phloem source and sink versus a source of energy and a heat sink
    "fonte", "dreno",
    # saturated fatty acid versus a saturated enzyme, saturated air and
    # the half-saturation of a functional response
    "saturado", "insaturado",
    # competitive inhibition versus competitive exclusion (a whole chapter)
    "competitivo",
    # mitochondrial matrix versus the extracellular matrix and a character
    # matrix
    "matriz",
    # the lac operator versus a mathematical operator
    "operador",
    # condensation reaction versus chromosome condensation; light
    # absorption versus absorption in the gut; energetic coupling versus
    # coupled equations; base stacking versus anything piled up
    "condensação", "absorção", "acoplamento", "empilhamento",
    # modular and indeterminate growth as bare adjectives
    "modular", "indeterminado",
    # "resolve" is never the microscope: its one occurrence is a body plan
    # that "resolves the same problem"
    "resolve",
}

EXTRA_PROTECT = [
    # magnification everywhere else; these five are the ordinary "increase"
    r"aumento(?= de turgor)",
    r"aumento(?= de onze)",
    r"aumento(?=\s+das\s+presas)",
    r"aumento(?= de lebres)",
    r"(?<=metade do )aumento",
    # the resolution of a yearly budget, not of a microscope
    r"(?<=na )resolução(?= de um balanço)",
    # the bare rock a primary succession starts on, not an enzyme's
    r"substrato(?= novo)",
]

AMBIG_POLICY = "drop"
