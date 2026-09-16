"""Book 4 -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-09-16 from THIS edition's own harvest (466 linkable terms, 3.3k
candidate links), never by translating book4_en.py and never by seeding from
book3_fr.py. Both censuses were run -- per-target frequency against the
English twin and per-target chapter set -- and every flag was read in context
with a link dump. What they showed:

  * French collisions English does not have. "paroi" is the prokaryote cell
    wall of ch. 1 AND the wall of an artery, a ventricle, a villus, a
    seminiferous tube, a pollen grain and a growing plant cell (117 links
    against English's 43 for the same target, in eight chapters English never
    links): dropped, with the one phrase that is the defined notion,
    "paroi bactérienne", restored through EXTRA.
  * "ovule" is the plant ovule of ch. 5-6 and, in ordinary French, the
    mammalian egg. The prose of ch. 8, 9 and 12 was written with the precise
    term ("ovocyte"), which is what a Year-2 lecture says anyway, so no lever
    was needed; only the VERB "ovule" ("une femme ovule", "quel jour
    ovule-t-elle") is protected below.
  * "ovaire" is the flower's ovary (ch. 6) and the mammal's (ch. 8-9), each
    with its own definition -- the same call English makes with STOP, which
    folds the term into the per-chapter map.
  * "bois" is the secondary xylem of ch. 13 and a WOODLAND in ch. 15 and 22
    ("dans un bois", "l'escargot des bois"); English protects the same sense
    with "in a wood"/"sooty wood". "transformation" is the bacterial one of
    ch. 3 and the ordinary noun in ch. 6 and 14; English protects it too.
    "dominant" is the genetic allele of ch. 4 and 22 and, outside genetics,
    the dominant follicle (ch. 9) and the dominant land plants (ch. 6) --
    again the English list, re-derived in French.
  * "induction" is the embryonic induction of ch. 10 and 12 and the FLORAL
    induction of ch. 14, which has its own target; the seven ch. 14 uses are
    protected, including the definition's own \\emph{induction florale}.
  * English collisions French does NOT have, checked and deliberately kept:
    "fleur"/"fruit"/"graine" (no verb "to flower" in French: "fleurir" shares
    no form with the noun), "sang" (only "sang chaud" in ch. 24 is figurative
    and is protected), "sol", "flux", "réservoir", "clone", "mutation",
    "segmentation", "capillaire", "dormance", "détermination", "compétence",
    "adaptation" -- every link was read and every one is the defined sense.
  * WORD_TAIL = (?:e?s)? with TAIL_ON_EVERY_WORD manufactures nothing false
    out of the single-word terms of this volume ("clonees", "fleures",
    "récessifes" occur nowhere); the two forms it DOES manufacture and that
    carry a second sense, "dominantes" and "coloniales", are covered by the
    protections above and by context.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --lang fr --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --lang fr --apply
"""

STOP = {
    # The flower's ovary (angiosperm-reproduction) and the mammal's
    # (mammal-reproduction) are both defined here; STOP keeps each chapter's
    # own sense and links nothing in the hormone chapter, where the word is
    # the organ and its definition lives elsewhere. book4_en.py STOPs the
    # English "ovary" for exactly this reason.
    "ovaire", "ovaires",
}

NO_CAPITAL = set()

EXTRA = {
    # The definition indexes the bare trophic adjectives ("chimiotrophe",
    # "lithotrophe"), which the prose never uses alone: it says
    # "chimiolithotrophie" and "chimiolithotrophes" (ch. 2 and 25). Without
    # these the target carried zero links, where English carries four.
    "chimiolithotrophie": "def:b2:microbial-metabolism:trophic",
    "chimiolithotrophe": "def:b2:microbial-metabolism:trophic",
    "chimiolithotrophes": "def:b2:microbial-metabolism:trophic",
    # "paroi" alone is dropped (see DROP); the phrase that names the defined
    # structure is kept, as English keeps "cell wall".
    "paroi bactérienne": "def:b2:unicellular-diversity:prokaryote",
}

DROP = {
    # cell wall vs the wall of an artery, a ventricle, a chorionic villus, a
    # seminiferous tube, a pollen grain, a guard cell and a growing plant
    # cell: 117 links across eight chapters English never links, all but a
    # handful the ordinary anatomical noun
    "paroi", "parois",
}

# Spans where a linkable word carries a sense the definition does not cover.
# Never consume a `$` (see tools/termlink/protect.py).
EXTRA_PROTECT = [
    # "ovule" as the verb of ovulation (the plant ovule is the defined term)
    r"\bfemme\s+ovule\b", r"\bovule-t-elle\b", r"\bovulerait-elle\b",
    # "bois" as woodland, not the secondary xylem
    r"\bdans\s+un\s+bois\b", r"\bdans\s+le\s+bois\b", r"\bun\s+bois\s+à\b",
    r"\bBois~:", r"\bescargot\s+des\s+bois\b", r"\bescargots\s+des\s+bois\b",
    # "transformation" outside horizontal gene transfer
    r"\bcette\s+transformation\b", r"\bmêmes\s+transformations\b",
    # "dominant" outside genetics: the dominant follicle and the land plants
    r"\bfollicules?\s+dominants?\b", r"\bsauf\s+le\s+dominant\b",
    r"\bplantes\s+dominantes\b",
    # floral induction (its own target) vs embryonic induction
    r"\\emph\{induction\s+florale\}", r"\bannule\s+l'induction\b",
    r"\bl'induction\s+exige\b", r"\bsemaines\s+après\s+l'induction\b",
    r"\bune\s+induction\s+achevée\b", r"\bet\s+l'induction\b",
    # "sang chaud" is a figure of speech in the phylogeny chapter
    r"\bsang\s+chaud\b",
]

AMBIG_POLICY = "drop"
