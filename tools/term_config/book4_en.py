"""Book 4 -- en. Curation only; the rules live in tools/termlink/.

University register (Year 2): the defined vocabulary is precise and links
nearly everywhere. Curated on 2026-09-10 after the English edition landed,
from a context dump of every link whose display word carries a second sense
somewhere in the volume. Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --apply

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").
"""

STOP = {
    # The flower's ovary (angiosperm-reproduction) and the mammal's
    # (mammal-reproduction) are both defined; STOP keeps each chapter's own
    # sense (the harvest folds the term into the per-chapter local map) and
    # links nothing in the hormone chapter, where the word is the organ and
    # the definition lives elsewhere.
    "ovary",
}

NO_CAPITAL = set()

EXTRA = {
    # a target that carried zero links while its phrases occur in the prose
    # (the definition indexes the bare trophic adjectives, which the prose
    # never uses on their own)
    "chemolithotrophs": "def:b2:microbial-metabolism:trophic",
    "chemolithotrophy": "def:b2:microbial-metabolism:trophic",
    "lithotrophy": "def:b2:microbial-metabolism:trophic",
}

DROP = set()

# Spans where a linkable word carries a sense the definition does not cover.
# Never consume a `$` (see tools/termlink/protect.py).
EXTRA_PROTECT = [
    # "flower" as a verb (the noun is the defined term)
    r'\b(?:Annuals|perennials|plants|cocklebur\)|maize\)) flower\b',
    r'\bwhole plant flower\b', r'\bnot flower until\b', r'\bwould flower\b',
    r'\bto flower\b', r'\bcrop\s+flower\b', r'\bit flower that\b',
    r'\bnever flowers\b', r'\bIt flowers\b', r'\bit flowers\b',
    r'\bbolts and flowers\b', r'\bplant flowers\b',
    r'\band flowers (?:open|when)\b', r'\bthat flowers for\b',
    r'\bflora flowers\b',
    # "dominant" outside genetics
    r'\bdominant (?:generation|plants|follicle)\b',
    r'\bdominant in one of dozens\b',
    # "transformation" outside horizontal gene transfer
    r'\bthat transformation\b', r'\bsame transformations\b',
    # "wood" as woodland, not the tissue
    r'\bin a wood\b', r'\bin the wood\b', r'\bthen a wood\b',
    r'\bsooty wood\b', r'\bbeech wood\b',
    # "seed" as a verb
    r'\bseed the clouds\b',
]

AMBIG_POLICY = "drop"
