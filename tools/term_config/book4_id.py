"""Book 4 -- id. Curation only; the rules live in tools/termlink/.

Curated on 2026-09-16 from THIS edition's own harvest (234 terms, 1 dropped
as defined twice -- the same one English drops), never seeded from another
book or translated from book4_en.py: the collisions of an Indonesian surface
are not the English ones.

Three observations from the audit of this volume:

  * Indonesian compounds the trophic adjectives (`kemolitotrof`,
    `kemolitotrofik`, `kemolitoautotrof`, `kemoorganoheterotrof`) exactly as
    English does, and the definition indexes only the four bare roots
    (`fototrof`, `kemotrof`, `litotrof`, `organotrof`), which the prose after
    the definition never uses on their own. Without the EXTRA below the
    target carries ZERO links, as it did in English before book4_en.py
    added the same three entries.
  * `lang_id.py`'s TAIL_AFTER_S earns its keep here: the enclitic `-nya`
    tail is what links `meristemnya`, `stomanya`, `auksinnya`,
    `sarkomernya` ... Nothing had to be added for it.
  * No DROP was needed. The homograph censuses (per-target frequency, and
    the per-target chapter set against the English twin) found no
    translated surface that is also an ordinary Indonesian word in a second
    sense: the register keeps the loanwords (meiosis, sarkomer, fitokrom,
    klad, isoterm) distinct from everyday vocabulary, which is the opposite
    of the `laju`/`air` problem that cost Book 3 its DROP list.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 4 --lang id --unwrap --apply
  python3 tools/link_defined_terms.py --book 4 --lang id --apply
"""

STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # def:b2:microbial-metabolism:trophic indexes the four bare roots only;
    # every later use in the prose is a compound. Same defect, same cure as
    # book4_en.py's chemolithotrophs/chemolithotrophy/lithotrophy.
    "kemolitotrof": "def:b2:microbial-metabolism:trophic",
    "kemolitotrofi": "def:b2:microbial-metabolism:trophic",
    "kemolitotrofik": "def:b2:microbial-metabolism:trophic",
    "kemolitoautotrof": "def:b2:microbial-metabolism:trophic",
    "kemoorganoheterotrof": "def:b2:microbial-metabolism:trophic",
}

DROP = {
    # HOMOGRAPH, and the one the census found. English's "cleavage" is a
    # word of embryology only; Indonesian "pembelahan" is the ordinary noun
    # for any division -- of a cell, of a lineage, of a data set. Harvested
    # from def:b2:vertebrate-development:egg it linked 67 times: 34 of them
    # inside chapter 10 (where the definition stands three lines away and
    # the link is worth least) and 33 of them WRONG -- "pembelahan sel" in
    # the muscle, limb, signalling and meristem chapters, and the
    # lineage "pembelahan" of every date in the phylogeny chapter, all
    # pointing at the cleavage of a zygote. STOP would not help (the term
    # would fall through to the per-chapter map and keep every one of those
    # chapters that pins a sense); only DROP removes it. The target is still
    # reached, by its other term "kuning telur" (yolk).
    "pembelahan",
}

# Never consume a `$` (see tools/termlink/protect.py).
EXTRA_PROTECT = [
    # "lumut kerak" is a lichen, not a moss: the collocation must not link
    # its first word to def:b2:plant-life-cycles:moss.
    r'\blumut kerak\b',
    # "bunga matahari" is a sunflower; the plant, not the flower organ.
    r'\bbunga matahari\b',
    # "pengatur" is the embryologist's organiser in chapter 10 and the
    # ordinary adjective "regulatory/regulating" everywhere else.
    r'\bdaerah pengatur\b', r'\bpusat pengatur\b',
    # the dominant FOLLICLE of the ovarian cycle is not a dominant allele
    # (book4_en.py protects "dominant follicle" for the same reason).
    r'\bfolikel\s+dominan(?:nya)?\b',
]

AMBIG_POLICY = "drop"
