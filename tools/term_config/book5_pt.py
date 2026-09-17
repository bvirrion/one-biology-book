"""Book 5 -- pt (Brazilian Portuguese). Curation only; the rules live in
tools/termlink/.

Curated 2026-09-17 from THIS edition's own harvest
(python3 tools/link_defined_terms.py --book 5 --lang pt --terms), never
seeded from book4_pt.py and never a translation of book5_en.py. Every STOP
and EXTRA_PROTECT entry below answers a flag of the two homograph censuses
(per-target frequency AND per-target chapter set, against the English twin),
read in context before it was written.

Regenerate after editing definitions or prose with:
  python3 tools/link_defined_terms.py --book 5 --lang pt --unwrap --apply
  python3 tools/link_defined_terms.py --book 5 --lang pt --apply
then a PLAIN dry run, which must report 0 links to insert.

Four Portuguese facts shaped this file.

1. Most of English's 28-word STOP list survives translation, because the
   collision is in the concept and not the word: "leitura" (sequencing read)
   is also "reading" and "fase de leitura"; "lesão" is the DNA lesion and any
   injury; "domínio" is the protein domain, the domain of life and a Hox
   expression domain; "resolução" is the crystallographer's and the
   resolution of inflammation; "barreira", "montagem", "revestimento",
   "semente", "catástrofe", "transdução", "tolerância", "latência" the same.

2. Portuguese mints collisions English cannot have. "progenitor" is the
   stem-cell progenitor AND the ordinary word for a PARENT, which is what
   Hamilton's relatedness proof and the conservation chapter's pedigrees
   need; STOP pins it to the stem-cell chapter. "tumor" is the cancer AND
   the third of Celsus's four signs of inflammation (rubor, calor, tumor,
   dor), the standard Portuguese rendering -- masked in EXTRA_PROTECT, since
   every other "tumor" in the book is the neoplasm. "motivo" is the sequence
   motif AND "reason"; "vetor" the cloning vector AND the weight vector of
   the Hebb/Oja rules; "conjugação" bacterial conjugation AND the hepatic
   conjugation of a hormone; "transformação" bacterial transformation AND
   the homeotic transformation of a vertebra; "perfil" the HMM profile AND
   a concentration profile.

3. NOT_A_TERM must be translated. The default list is English words, and
   the only one that bites a Portuguese index key is "problem" inside
   "problema"; without the translated list Portuguese harvests four terms
   English deliberately drops ("regra de Hamilton", "regra de Oja",
   "regra de Rescorla--Wagner", "teorema do valor marginal"). The list is
   the SINGLE words only: "lei de" is NOT in it, deliberately. English's
   phrase "law of" excludes "law of X" and keeps "Bragg's law", "Weber's
   law", "Fechner's law", "Gompertz law", "Stevens' power law"; Portuguese
   writes every one of those as "lei de X", so a "lei de" entry would
   delete five targets' worth of links that English ships.

4. WORD_TAIL is "(?:e?s)?", which cannot build "-ao" -> "-oes" or
   "-l" -> "-is". The EXTRA entries below are the plurals that actually
   occur in this volume and that the tail cannot reach; each was counted in
   the wrapped tree before it was added, and each is of a single sense here.
"""

# Terms kept for their own chapter only (the harvest folds a STOPped term
# into the per-chapter local map).
STOP = {
    # sequencing read (genomics) vs "reading", "fase de leitura", the
    # reading of a gradient or a signal in nine other chapters
    "leitura", "leituras",
    # DNA lesion (repair) vs any tissue or brain injury, nine chapters
    "lesão",
    # protein domain (structural biology) vs domains of life, Hox expression
    # domains, the domain of a function -- ten chapters
    "domínio", "domínios",
    # genome assembly vs the assembly of a virus, a ribosome, a spindle
    "montagem",
    # vesicle coat vs "o revestimento do intestino", the lining of anything
    "revestimento", "revestimentos",
    # the BLAST seed vs the seeds a kangaroo rat eats and a seedling grows
    "semente", "sementes",
    # crystallographic resolution vs the resolution of inflammation (ch. 15),
    # of a sound (ch. 18) and of a phylogeny (ch. 25)
    "resolução",
    # the innate barrier vs the blood--brain barrier, the nodule's oxygen
    # diffusion barrier, the barrier a scar makes
    "barreira",
    # microtubule catastrophe vs environmental catastrophes (ch. 27)
    "catástrofe", "catástrofes",
    # phage transduction vs sensory and photo-transduction (ch. 17, 18)
    "transdução",
    # immunological tolerance vs the oral glucose tolerance test (ch. 21)
    "tolerância",
    # viral latency vs the latency of a reflex and of pain (ch. 17)
    "latência",
    # neural divergence vs sequence divergence (ch. 25, seven links)
    "divergência",
    # the stem-cell progenitor vs "progenitor" = PARENT, which Hamilton's
    # proof (ch. 26) and the parrot pedigree (ch. 27) need
    "progenitor", "progenitores",
}

# Index keys built on these words are scaffolding, not defined vocabulary.
# Single words only -- see note 3 of the docstring on why "lei de" is absent.
NOT_A_TERM = ("teorema", "lema", "desigualdade", "fórmula", "critério",
              "princípio", "identidade", "regra", "paradoxo", "problema")

NO_CAPITAL = set()

# Plurals the "(?:e?s)?" tail cannot build. Every label is defined in
# parts/bachelor-3/ (checked against its own label set).
EXTRA = {
    "ligações de ponta": "def:b3:sensory-systems:cochlea",
    "nociceptores": "def:b3:sensory-systems:somato",
    "antivirais": "def:b3:virology:drugs",
    "junções de Holliday": "def:b3:dna-repair:dsb",
    "duplicações do genoma inteiro": "def:b3:genomics:comparative",
    "unidades taxonômicas operacionais": "met:b3:microbiomes:16s",
}

DROP = set()

# Spans where a linkable word carries a sense the definition does not cover.
# Never consume a `$` (see tools/termlink/protect.py), and never anchor a
# lookaround on a word that is itself a linked term.
EXTRA_PROTECT = [
    # "tumor" as Celsus's third sign of inflammation, not the neoplasm
    r'(?<=tecido:\s\\emph\{)tumor',
    r'Tumor(?=:\s+vazamento)',
    # "motivo" as reason, and the circuit motifs of ch. 17, not the
    # sequence motif of ch. 5
    r'motivo(?=\s+de\s+preocupação)',
    r'(?<=alguns\s)motivos',
    # a concentration profile, not the profile HMM
    r'perfil(?=\s+é\s+um\s+platô)',
    # the weight vector of the Hebb and Oja rules, not the cloning vector
    r'vetor(?=\s+de\s+pesos)',
    r'vetor(?=\s+unitário)',
    # hepatic conjugation of a hormone, not bacterial conjugation
    r'(?<=síntese,\s)conjugação',
    # the homeotic transformation of a vertebra, not bacterial transformation
    r'transformação(?=\s+anterior)',
]

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
EXTRA["agrupamentos de piRNA"] = "def:b3:rna-regulation:pirna"
