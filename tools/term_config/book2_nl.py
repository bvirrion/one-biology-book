"""Book 2 -- nl. Curation only; the rules live in tools/termlink/.

Curated 2026-09-05 from THIS edition's own Dutch harvest, in context.
Nothing here is inherited from book1_nl.py or translated from book2_en.py:
the English twin was read for the SENSE collisions this volume has, and each
of them was then re-decided on the Dutch word that carries it.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 2 --lang nl --terms
  python3 tools/link_defined_terms.py --book 2 --lang nl --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang nl --apply

Dutch adds two defect classes English does not have.

  * lang_nl.py's WORD_TAIL is (?:e?[ns])?, which MANUFACTURES words: it is
    appended to every single-word term, so a term that is also a Dutch stem
    grows into an ordinary word ("drager" -> "dragers", the NAD carriers of
    photosynthesis and respiration as well as the carrier of a recessive
    allele). STOP is checked before derivation and DROP only sees term keys,
    so a manufactured form that is wrong in ONE phrase can only be reached by
    EXTRA_PROTECT.
  * Dutch welds compounds, and harvest.py skips any \\index entry without a
    space outside a definition -- so the plural the prose actually uses is
    often a different string from the \\index key and is never seen. Every
    EXTRA below was found by counting the unlinked surface forms in the
    bodies, not by eye, and each is single-sense in this volume.
"""

STOP = {
    # the eye chapter's own word; but "het blote oog", "onder het oog van de
    # alvleesklier" (g12 glucose) and "oog en nier" (g12 diabetes) are
    # ordinary Dutch. English STOPs "eye" for exactly this.
    "oog",
    # "bestand" is the antibiotic chapter's "resistant", but also the
    # toxin-resistant borers of the maize chapter and, as a noun, an
    # ordinary Dutch word. English STOPs "resistant".
    "bestand",
    # allele frequencies in the population chapter; but "de frequentie van
    # de actiepotentialen" is the coding of the two nerve chapters.
    # English STOPs "frequencies".
    "frequenties",
}

NO_CAPITAL = set()

# Forms the Dutch morphology cannot derive from the harvested key: an -en/-s
# tail cannot produce hormoon->hormonen, antibioticum->antibiotica,
# organel->organellen, pees->pezen, and it never runs backwards, so a term
# harvested in the plural loses its singular. Counted in the bodies.
EXTRA = {
    # The single largest gap this edition had against its English twin.
    # Dutch doubles the l in the plural, which an -en/-s tail cannot
    # produce, so "cellen" -- 411 standalone uses -- was invisible while
    # "cel" linked 285 times. English links its :cell target 908 times.
    "cellen": "def:g10:cells-common-unit:cell",
    # the glycaemia chapter says "bloedglucose" as often as it says the
    # full compound; the word boundary keeps it out of
    # "bloedglucosespiegel", which is the harvested key
    "bloedglucose": "def:g12:glucose-and-diabetes:glycaemia",
    "mutagenen": "def:g11:mutations:mutagen",
    "centromeren": "def:g11:cell-cycle-mitosis:chromosome",
    "neurotransmitters": "def:g12:stretch-reflex:synapse",
    "fylogenetische bomen": "def:g12:phylogenetic-trees:tree",
    # harvested as the plural "genfamilies"; the welded singular is what
    # the prose uses six times, and without it the proposition is
    # unreachable (English reaches it through "gene family")
    "genfamilie": "prop:g12:diversification-of-life:duplication",
    "hormonen": "def:g11:hormones-and-reproduction:hormone",
    "antibiotica": "def:g11:antibiotic-resistance:antibiotic",
    "organellen": "def:g10:cells-common-unit:organelle",
    "carcinogenen": "def:g11:cancer:carcinogen",
    "antigenen": "def:g12:adaptive-immunity:antigen",
    "pezen": "def:g10:muscles-and-joints:muscle",
    # harvested only in the plural; the singular is what the prose uses
    "spiervezel": "def:g10:muscles-and-joints:muscle",
    "actiepotentiaal": "prop:g12:stretch-reflex:actionpotential",
    "antistof": "prop:g12:adaptive-immunity:antibodies",
    "geheugencel": "prop:g12:adaptive-immunity:selection",
    "reflexbogen": "def:g12:stretch-reflex:reflex",
    "wortelhaar": "prop:g12:plant-rooted-life:surfaces",
    "tropisme": "prop:g12:plant-rooted-life:tropisms",
    "eilandje": "prop:g12:glucose-and-diabetes:hormones",
    "mediator": "prop:g12:innate-immunity:inflammation",
    # \emph'd at the head of a sentence, so the harvest keeps only the
    # capitalised string and the lowercase singular of the prose is unseen
    "ontstekingsremmer": "prop:g12:innate-immunity:drugs",
    # the proposition is reached in English through its \index phrase
    # "antibiotic resistance"; the Dutch key welds into one word, which
    # harvest.py never sees outside a definition, and the \emph that
    # carries it ("bestand") is in STOP above.
    "antibioticaresistentie": "prop:g11:antibiotic-resistance:mechanisms",
}

DROP = {
    # "drager" is the carrier of a recessive allele in the disease chapter,
    # but ALSO the NAD/electron carriers of photosynthesis, respiration and
    # the light phase, and the pollen carrier of the flower chapter. Dutch
    # uses one word for all four; English DROPs "carrier" for the same
    # reason. This costs the disease chapter its own links, which is the
    # cheaper of the two errors.
    "drager",
    # NOTE on "soort": it is NOT dropped. It is the one Dutch homograph in
    # this volume that was resolved in the PROSE instead of in this file.
    # Dutch "soort(en)" is both "species" and "kinds/sorts", and 39 sites --
    # "twee soorten fotoreceptoren", "twintig soorten aminozuur", "de drie
    # soorten puntmutatie", "twee soorten bewijs" -- meant *kinds*. They had
    # no stable lexical neighbourhood to key an EXTRA_PROTECT on (most are a
    # bare numeral plus "soorten", which is also how the species chapters
    # count species), so each was rewritten to "type/typen", which is what a
    # Dutch biology text says for a cell or receptor TYPE anyway. "soort"
    # now means species everywhere in the volume and links freely.
    # the DNA bases and the bases of "zuren en basen" are the same Dutch
    # word; the singular key never occurs in prose. English DROPs both.
    "basen", "base (DNA)",
    # animal culture in one chapter; bacterial cultures and human culture
    # everywhere else. English DROPs "culture".
    "cultuur", "cultuur (dier)",
}

# "vergroting" is the microscope's magnification in 13 of its 14 uses; the
# fourteenth is the enlargement of the brain in the human-evolution
# solutions, where the microscopy link would be plainly wrong. STOP would
# cost the other thirteen, so the one phrase is protected instead.
EXTRA_PROTECT = [
    r"vergroting van de hersenen",
]

AMBIG_POLICY = "nearest-preceding"   # school book; matches book2_en.py
