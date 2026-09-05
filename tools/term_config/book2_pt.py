"""Book 2 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Curated 2026-09-05 from THIS edition's own harvest
(python3 tools/link_defined_terms.py --book 2 --lang pt --terms), never
seeded from book1_pt.py: every EXTRA value below was checked against the
labels actually defined in parts/grade-1{0,1,2}/.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 2 --lang pt --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang pt --apply

The collisions are not the English ones. "carrier" collides in English
because the NAD/NADP carriers share the word; in pt those are
"transportadores" and "portador" is unambiguous, so it stays linked.
Conversely "aumento" (magnification) is also the ordinary word for "an
increase", and "cultura" is at once the animal culture, a bacterial
culture and a crop -- neither collides in English.
"""

# STOP is checked before derivation; nothing here needs it: every risky
# word below is better handled by DROP (a whole harvested key) or by
# EXTRA_PROTECT (the few phrases where the sense is wrong).
STOP = set()

NO_CAPITAL = set()

EXTRA = {
    # the organ sense of homology survives in the feminine forms only
    # ("estruturas homologas", "asas homologas ou analogas"); the
    # masculine plural is the meiosis sense and is dropped below
    "homólogas": "def:g10:common-ancestry:homology",
    # the prose says "um anti-inflamatorio" where English says "an
    # anti-inflammatory drug", so the harvested phrase never fires and
    # the target shipped with no links at all
    "anti-inflamatório": "prop:g12:innate-immunity:drugs",
}

DROP = {
    # --- the five below restore parity with book2_en.py, whose STOP/DROP
    # --- put these same senses out of reach; the per-target census
    # --- against the English twin is what exposed each one.
    #
    # "especie(s)" was DROPped here on 2026-09-05 and RESTORED the same
    # day: the 206-vs-37 excess was a canon defect, not a Portuguese
    # collision. English had \emph{species}\index{species} in the
    # Biodiversity bullet list AND a bare \emph{species} on the Species
    # definition two paragraphs later, so the harvest lost the key to the
    # defined-twice rule and the target was an orphan. The marker has
    # been moved onto the definition; English now links it 272 times and
    # so does this edition, through the singular key plus the
    # "(?:e?s)?" tail. Portuguese has no independent homograph here:
    # every "especie de" in the volume is "species of", and the two
    # sites that read "kind of" (a section title, and the meiosis
    # definition's "toda especie de reproducao sexuada") were
    # mistranslations, now reworded -- so no EXTRA_PROTECT is needed.
    #
    # "eye": STOPped in English. 99 links against English's 12, 50 of
    # them in the vision chapter alone, plus "a olho nu" and "com um
    # olho humano no lugar do ambiente"
    "olho",
    # "resistant": STOPped in English. 85 links against 2, including
    # the eleven "eixo resistente" (a tough wheat stalk) of the
    # domestication chapter
    "resistente",
    # "bases"/"base (DNA)": DROPped in English. 120 links against 54,
    # among them "Bases de cranio" -- the base of a fossil skull
    "bases", "base (DNA)",
    # English harvests the capitalised "Proteins" and so links the
    # lowercase plural through the AMBIGUOUS "protein" key; the pt
    # harvest yields lowercase "proteinas" and would bypass the
    # nearest-preceding policy in eight chapters
    "proteínas",
    # animal culture in one chapter; a bacterial culture in three, the
    # crops of the domestication chapter, and human culture in two more
    "cultura", "cultura (animal)",
    # allele frequencies where it is defined; recombination frequencies,
    # firing frequencies of a spindle and heart rate elsewhere.
    # "frequencia alelica" keeps the honest links.
    "frequências",
    # "homologos" is the meiosis sense (cromossomos homologos, pares de
    # homologos) in some twenty-five places against six organ ones
    "homólogos",
}

EXTRA_PROTECT = [
    # "aumento" is magnification in the microscopy chapter and the
    # ordinary word for an increase everywhere else
    r"aumento do cérebro",
    r"fator médio de aumento",
    r"aumento de 225",
    # people carrying resistant strains, not carriers of a recessive
    # allele (the other twenty-odd "portador" sites are the honest one)
    r"portadores de linhagens",
    r"a partir dos portadores",
    # the dominant ovarian follicle, and a dominant process -- not the
    # dominant allele of the genetic-disease chapter
    r"dominante reduzem",
    r"o torna dominante",
]

AMBIG_POLICY = "nearest-preceding"   # matches book2_en.py; the volume
                                     # re-defines cloroplasto, cromossomo,
                                     # enzima, proteína
