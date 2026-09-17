"""Book 5 -- fr. Curation only; the rules live in tools/termlink/.

Curated 2026-09-17 from THIS edition's own harvest (775 linkable terms, 3.1k
candidate links before curation), never by translating book5_en.py and never
by seeding from book4_fr.py. BOTH censuses were run against the English twin
-- per-target frequency and per-target chapter set -- and every flag was read
in a link dump with its sentence. What they showed:

  * French collisions English does not have, each found by the chapter-set
    census and each a plain noun outside its chapter:
      - "lecture" is the sequencing read of ch. 4 AND the ordinary act of
        reading, which this volume performs on gradients, codes, clocks and
        instruments (132 links in nine chapters against English's 98 in one).
      - "motif" is the sequence motif of ch. 5 AND the French word for any
        pattern: the PAMPs and DAMPs of ch. 15, the pattern receptors of
        ch. 22, the combinatorial code of ch. 18, Turing's patterns and the
        Hox domains of ch. 23, the activity patterns of ch. 19 (93 links in
        nine chapters against English's 19 in three).
      - "lésion" is the DNA lesion of ch. 3 AND a tissue lesion (ch. 10, 15,
        17, 19, 21, 24) -- the same call English makes with STOP, re-derived.
      - "domaine" is the protein domain of ch. 7 AND the Hox expression
        domain, the antibody's variable domain, the domains of life and, in
        two photograph credits, "domaine public".
      - "vecteur" is the cloning vector of ch. 6 AND the weight VECTOR of
        Hebb's rule in ch. 19 (twelve links there, none of them a plasmid).
      - "conjugaison" is bacterial conjugation (ch. 12) AND the conjugation
        of a plant hormone (ch. 22); "transformation" is the bacterial one
        (ch. 12) AND the homeotic transformation of ch. 23.
      - "manteau" is the vesicle coat of ch. 8 AND the C3b coat that titles
        Part II of the innate-immunity problem.
      - "retour en arrière" is the alignment traceback of ch. 5 AND the dark
        reversion of phytochrome in ch. 22.
      - "taux de mortalité" is Gompertz's hazard (ch. 24) AND the ordinary
        demographic rate of ch. 27.
  * English collisions that survive translation and are STOPped here for the
    same reason: assemblage/profil/résolution/enveloppe/tolérance/
    transduction/barrière/catastrophe/divergence/convergence/latence/
    lecteur/écrivain/cil. Each was verified in a dump first: "résolution"
    linked the resolution of inflammation (ch. 15) and an angular resolution
    (ch. 18) to a crystallographic method; "latence" linked six neural
    latencies of ch. 17 to viral latency; "tolérance" linked the glucose
    tolerance test of ch. 21 to immunological tolerance.
  * English collisions French does NOT have, checked link by link and
    deliberately left linked: "virus", "chromatine", "tumeur", "apoptose",
    "inflammation", "anticorps", "antibiotique", "plasmide", "insuline",
    "cycline", "hormone", "niche" (the ecological sense is never linked),
    "empreinte" (only the compound "région de contrôle de l'empreinte" is a
    term, so the gosling's imprinting in ch. 26 cannot collide), "bâtonnet"
    (the ch. 21 use is the retinal rod), "amorce" (the ch. 18 use is a PCR
    primer), "sénescence", "microtubules", "endosome".
  * The volume's heaviest target, "lymphocyte(s)" (72 links in ch. 16 against
    English's 5), is NOT a homograph: French writes "lymphocyte~B" and
    "lymphocytes~T" where English writes "B cell" and "T cell", so the head
    noun carries the link that English spreads over two compounds it then
    fails to match through its own non-breaking spaces. Every link is the
    defined sense and none was removed.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 5 --lang fr --unwrap --apply
  python3 tools/link_defined_terms.py --book 5 --lang fr --apply
and then a PLAIN dry run, which must report 0 links to insert.
"""

# Terms kept for their own chapter only (the harvest folds a STOPped term
# into the per-chapter local map). Singular keys: the linker derives the
# plural through WORD_TAIL.
STOP = {
    # ---- French homographs English does not have ------------------------
    "lecture",          # sequencing read vs reading anything
    "motif",            # sequence motif vs any pattern
    "lésion",           # DNA lesion vs tissue lesion
    "domaine",          # protein domain vs domain of life / "domaine public"
    "vecteur",          # cloning vector vs the vector of Hebb's rule
    "conjugaison",      # bacterial conjugation vs hormone conjugation
    "transformation",   # bacterial transformation vs homeotic transformation
    "manteau",          # vesicle coat vs the complement coat
    "retour en arrière",  # alignment traceback vs phytochrome dark reversion
    "taux de mortalité",  # Gompertz hazard vs the demographic rate
    # ---- collisions shared with English, re-derived in French ------------
    "assemblage",       # genome assembly vs protein/virus assembly
    "profil",           # HMM profile vs an expression or daily profile
    "résolution",       # crystallographic resolution vs resolution of inflammation
    "enveloppe",        # virus envelope vs bacterial envelope
    "tolérance",        # immunological tolerance vs glucose tolerance
    "transduction",     # phage transduction vs sensory transduction
    "barrière",         # innate barrier vs blood--brain barrier
    "catastrophe",      # microtubule catastrophe vs an environmental one
    "divergence",       # neural divergence vs sequence divergence
    "convergence",      # neural convergence vs evolutionary convergence
    "latence",          # viral latency vs neural latency
    "lecteur",          # chromatin reader vs a reader
    "écrivain",         # chromatin writer vs a writer
    "cil",              # the axonemal cilium vs airway and hair-cell cilia
}

NO_CAPITAL = set()

# display -> label, for a target harvest.py cannot reach on its own.
# AUDIT every entry against parts/bachelor-3/'s OWN label set before use.
EXTRA = {}

# The lever for a true homograph, where STOP's per-chapter fall-through would
# still leave wrong links. None was needed: every collision above is between
# chapters, so STOP is sufficient and keeps the defining chapter's own links.
DROP = set()

# Regexes marking spans that must NOT be linked. Never anchor one on a word
# that is itself a term.
EXTRA_PROTECT = []

# University register: an ambiguous term links nowhere rather than to a guess.
AMBIG_POLICY = "drop"

# def:b3:rna-regulation:pirna is reachable in ENGLISH only through the PLURAL
# key "piRNAs" -- the singular harvests to the ncRNA definition instead -- so
# the target's reachability is an accident of English morphology and this
# language loses it silently. Recovered here on the CLUSTER phrase, which is
# English's other key for the same target ("piRNA clusters"), exactly as the
# id, ar and hi editions of this book did. Found by the Indonesian Book 5
# agent and confirmed by the Arabic and Hindi ones; added for this edition by
# the coordinator, 2026-09-17.
EXTRA = dict(EXTRA or {})
EXTRA["amas de piARN"] = "def:b3:rna-regulation:pirna"
