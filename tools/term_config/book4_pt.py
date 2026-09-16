"""Book 4 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Curated 2026-09-16 from THIS edition's own harvest
(python3 tools/link_defined_terms.py --book 4 --lang pt --terms), never
seeded from book3_pt.py and never a translation of book4_en.py. Every EXTRA
value below is a label defined in parts/bachelor-2/, and every STOP and
EXTRA_PROTECT entry answers a flag of the two homograph censuses
(frequency and chapter set, against the English twin).

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --lang pt --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --lang pt --apply

Three Portuguese-specific facts shaped this file.

1. WORD_TAIL is "(?:e?s)?", so it builds "flores" and "capilares" but not
   the "-cao" -> "-coes", "-al" -> "-ais", "-m" -> "-ns" plurals, nor
   "celulas-tronco". Those plurals are the EXTRA entries; "mutacoes" alone
   was 52 lost links.

2. "ovulo" is at once the plant OVULE (defined with heterospory in the plant
   life-cycle chapter, and the word of the angiosperm chapter) and the
   ordinary Portuguese word for the animal EGG (mammal reproduction,
   hormones, parthenogenesis, cloning, gamete isolation). English says
   "ovule" and "egg" and cannot collide; here every egg-sense site is masked
   in EXTRA_PROTECT, which keeps the ovule links in chapters 5-6.

3. "potencia" is both the cell's POTENCY (defined in cell differentiation)
   and physical or mathematical POWER (Poiseuille's fourth power, cardiac
   and muscle power, the species--area power law). STOP pins it to its own
   chapter, which is the only one that uses the potency sense after the
   definition.
"""

STOP = {
    # potency (cell differentiation) vs power (heart, muscle, Poiseuille,
    # species--area): the potency sense occurs only in its own chapter
    "potência",
    # the flower's ovary (angiosperm chapter) vs the mammal's ovary: English
    # STOPs "ovary" for the same reason; pinned to the flower chapter
    "ovário",
}

NO_CAPITAL = set()

EXTRA = {
    # --- irregular plurals the "(?:e?s)?" tail cannot build, each of a
    # --- single sense in this volume ---
    "mutações": "def:b2:genome-diversification:mutation",
    "mutações pontuais": "def:b2:genome-diversification:mutation",
    "fermentações": "def:b2:microbial-metabolism:fermentation",
    "induções": "def:b2:vertebrate-development:induction",
    "clivagens": "def:b2:vertebrate-development:egg",
    "coloniais": "def:b2:unicellular-diversity:unicellular",
    "ovulações": "def:b2:mammal-reproduction:ovary",
    "aptidões": "def:b2:population-genetics:fitness",
    "adaptações": "def:b2:plant-plasticity:plasticity",
    "anéis anuais": "def:b2:plant-meristems:wood",
    "potenciais de ação": "prop:b2:neurons-synapses:ap",
    "potenciais de equilíbrio": "thm:b2:neurons-synapses:nernst",
    "potenciais de Nernst": "thm:b2:neurons-synapses:nernst",
    "células-tronco": "def:b2:cell-differentiation:differentiation",
    # --- the trophic definition indexes the bare adjectives; the prose says
    # --- the welded noun (mirrors the three EXTRA entries of book4_en.py) ---
    "quimiolitotrofia": "def:b2:microbial-metabolism:trophic",
    "quimiolitotróficos": "def:b2:microbial-metabolism:trophic",
    # --- the definition indexes "abalo muscular" and the phosphagen is one
    # --- welded word the harvest skips; the prose says the bare forms ---
    "abalo": "def:b2:muscle-movement:motorunit",
    "abalos": "def:b2:muscle-movement:motorunit",
    "fosfocreatina": "prop:b2:muscle-movement:energy",
}

DROP = set()

# Spans where a linkable word carries a sense the definition does not cover.
# Never consume a `$` (see tools/termlink/protect.py).
EXTRA_PROTECT = [
    # "ovulo" as the animal EGG, not the plant ovule (see the docstring)
    r'óvulos?(?=\s+humanos?\b)',
    r'(?<=chegarão\sao\s)óvulo', r'óvulo(?=\s+fecundado\s+se\b)',
    r'(?<=produz\sum\s)óvulo', r'(?<=onde\so\s)óvulo',
    r'(?<=Junto\sao\s)óvulo', r'(?<=com\sa\sdo\s)óvulo',
    r'(?<=O\s)óvulo(?=\s+(?:responde|completa)\b)',
    r'(?<=produz\s)óvulos(?=\s+aos\b)', r'(?<=um\s)óvulo(?=\s+precisa\b)',
    r'(?<=superfície\sdo\s)óvulo', r'óvulo(?=\s+penetrado\b)',
    r'(?<=fecha\so\s)óvulo', r'(?<=cromossômicos\sdo\s)óvulo',
    r'(?<=alcançando\so\s)óvulo', r'(?<=alcançam\so\s)óvulo',
    r'óvulo(?=\s+pode\s+ser\s+fecundado\b)', r'(?<=é\so\s)óvulo(?=,)',
    r'(?<=por\s)óvulos(?=\s+aneuploides\b)', r'(?<=nos\s)óvulos(?=\s+que\b)',
    r'(?<=único\s)óvulo', r'óvulo(?=\s+fica\s+parado\b)',
    r'(?<=400\s)óvulos', r'óvulo(?=\s+leva\s+cem\b)',
    r'(?<=Os\s)óvulos(?=\s+ficam\b)',
    r'óvulo(?=\s+é\s+liberado\b)', r'óvulo(?=\s+pronto\b)',
    r'óvulo(?=\s+um\b)', r'óvulo(?=\s+precisa\s+ser\s+liberado\b)',
    r'óvulo(?=\s+de\s+(?:ovelha|outra\s+espécie)\b)',
    r'óvulos?(?=\s+não\s+fecundado)', r'(?<=produzem\s)óvulos',
    # "dominante" outside genetics
    r'(?<=geração\s)dominante', r'(?<=plantas\s)dominantes',
    r'(?<=folículo\s)dominante', r'(?<=folículo\}\s)dominante',
    r'(?<=exceto\so\s)dominante',
    r'dominante(?=\s+numa\s+de\s+dezenas\b)',
    # "transformacao" outside horizontal gene transfer
    r'(?<=Toda\sessa\s)transformação',
    # "sangue" in "warm-blooded"
    r'sangue(?=\s+quente\b)',
    # organ budding of the gut tube, not the budding of a unicell
    r'brotamento(?=\s+os\s+pulmões\b)',
    # photoperiodic (floral) induction and mathematical induction, not the
    # embryonic induction the defined term names
    r'(?<=cancela\sa\s)indução', r'indução(?=\s+exige\b)',
    r'(?<=após\sa\s)indução', r'indução(?=\s+não\s+é\b)',
    r'indução(?=\s+completada\b)', r'(?<=por\s)indução(?=,)',
    r'indução(?=\s+floral\})',
    # mass flow of water to a root, not a biogeochemical flux
    r'fluxo(?=\s+de\s+massa\b)',
    # "em flor" (in bloom), a state, mirroring English's masks of the verb
    r'(?<=cerejeiras\sem\s)flor\b',
]

AMBIG_POLICY = "drop"
