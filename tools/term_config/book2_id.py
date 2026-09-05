"""Book 2 -- id. Curation only; the rules live in tools/termlink/.

Curated on 2026-09-05 from THIS edition's own harvest (147 terms, 211 linkable
forms), never seeded from book1_id.py or translated from book2_en.py: a word
that collides in English need not collide in Indonesian, and Indonesian has
collisions English does not. Regenerate after editing definitions or prose:

  python3 tools/link_defined_terms.py --book 2 --lang id --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --lang id --apply

Two divergences from book2_en.py are deliberate and were measured:

  * English DROPs "bases"/"base (DNA)" because "acids and bases" also occurs.
    Indonesian never writes "asam dan basa" in this volume (checked: zero
    hits), so "basa" is single-sense here and stays linked -- 83 honest links
    English cannot have.
  * English STOPs "resistant" because of insulin-resistant tissues and
    pest-resistant crops. Indonesian says "resistansi insulin" for the first
    (a different word) and "penggerek yang tahan" for the second, which IS the
    selection of ch:g11:antibiotic-resistance and is named as such in the
    text, so "tahan" stays linked. All 123 occurrences were read.
"""

STOP = {
    # A sentence-initial \emph{Fermentasi} in prop:g12:...:fermentation is
    # harvested as a term of its OWN, distinct from the lowercase "fermentasi"
    # defined two years earlier in grade-10. The lowercase term wins every
    # occurrence, so the proposition ends up an ORPHAN TARGET either way, and
    # which of the two wins depends on capitalisation, i.e. the link graph is
    # not reproducible. Exactly the collision book2_en.py records for
    # "Fermentation"; suppressed here for the same reason and for parity.
    "Fermentasi",
    # Same shape: \emph{Kloroplas} opens def:g12:photosynthesis:chloroplast, so
    # the capitalised form is harvested separately and points ONLY at the
    # grade-12 definition -- which would forward-link the sentence-initial
    # "Kloroplas" of grade-12 ch.2 (endosymbiosis) past the grade-10 organelle
    # definition it actually means. The lowercase "kloroplas" is ambiguous and
    # resolves nearest-preceding, which is right in both places. English has no
    # capitalised twin here because its definition reads "The \emph{chloroplast}".
    "Kloroplas",
}

NO_CAPITAL = set()

EXTRA = {
    # prop:g11:vision-and-brain:plasticity is displayed as "keplastisan otak";
    # grade-12 ch.14 uses the ordinary scientific noun "plastisitas" for the
    # same property, and WORD_TAIL only manufactures "-nya", not this
    # derivation. Same label, same sense, 7 sites.
    "plastisitas": "prop:g11:vision-and-brain:plasticity",

    # prop:g12:plant-rooted-life:saps is displayed as "\emph{Xilem}" and
    # "\emph{Floem}" -- both open their bullet, so BOTH were harvested
    # capitalised only and the fifteen lowercase uses in the surrounding prose
    # went unlinked (en links this target 15 times, id linked it once).
    "xilem": "prop:g12:plant-rooted-life:saps",
    "floem": "prop:g12:plant-rooted-life:saps",
}

DROP = {
    # animal culture in grade-12 ch.2; human culture in grade-12 ch.5 (the
    # second mode of inheritance) -- the same two senses book2_en.py drops for
    # "culture"/"culture (animal)".
    "budaya", "budaya (hewan)",
    # allele frequency in the population chapter; the frequency of action
    # potentials, of the heart beat, of breathing and of recombination in four
    # others. The compound "frekuensi alel" carries the sense and is kept;
    # book2_en.py STOPs "frequencies" for the same reason.
    "frekuensi",
}

EXTRA_PROTECT = [
    # The homology of grade-10 ch.6 is the homology of a COMMON ANCESTOR
    # (organ homolog, tulang homolog). "kromosom homolog" and every "-nya"
    # form of it are the MEIOSIS sense of grade-11 ch.2 and grade-12 ch.1 --
    # the same distinction book2_en.py protects with
    # "homologous (?:chromosomes?|pairs?)". Indonesian inflects it far more, so
    # the pattern has to cover the enclitic and the four verbs that follow it.
    r"kromosom homolog(?:nya)?",
    r"homolognya",
    r"homolog (?:yang|pada|gagal|tiap)",
    # "mata" is the eye everywhere in this volume except in two frozen idioms:
    # "mata rantai" (a link of a chain, grade-12 ch.5) and "mata tombak" (a
    # spear point, grade-12 ch.5). Protecting the two phrases keeps the ~85
    # honest eye links that a STOP would have thrown away.
    r"mata rantai",
    r"mata tombak",
    # "pembawa" is the carrier of a recessive allele everywhere except
    # "pembawa pesan kimia", the chemical messenger of grade-11 ch.12.
    r"pembawa pesan",
    # "mata" again, in three fixed expressions that are not the eye: "mata
    # uang" (currency -- ATP is the cell's currency, grade-12 ch.8 and ch.9),
    # "air mata" (tears, grade-12 ch.11) and "semata-mata" (solely, grade-12
    # ch.3). The last one is reached through HEAD, which lets a hyphenated
    # element in front of a single-word term.
    r"mata uang",
    r"air mata",
    r"semata-mata",
    # and the figurative eye of grade-12 ch.7, "seleksi alam dengan mata
    # manusia menggantikan lingkungan" -- the judgement, not the organ. The
    # only other "mata manusia" in the volume is grade-10 ch.6, which precedes
    # the definition and is therefore never linked anyway.
    r"mata manusia",
]

AMBIG_POLICY = "nearest-preceding"   # the volume re-defines kloroplas, kromosom, enzim, protein
