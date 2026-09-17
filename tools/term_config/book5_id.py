"""Book 5 -- id. Curation only; the rules live in tools/termlink/.

Curated 2026-09-17 from THIS edition's own harvest (790 linkable terms),
after both homograph censuses against the English twin: per-target FREQUENCY
and per-target CHAPTER SET. Never seeded from book4_id.py and never
translated from book5_en.py -- the collisions Indonesian mints are its own,
and three of the worst ones below have no English counterpart at all
("primer" = both PCR primer AND "primary"; "perancah" = both genome
scaffold AND a wading bird; "laju kematian" = both the Gompertz mortality
rate AND an ordinary population death rate).

Regenerate with:
  python3 tools/link_defined_terms.py --book 5 --lang id --unwrap --apply
  python3 tools/link_defined_terms.py --book 5 --lang id --apply
then a PLAIN dry run, which must print "links to insert: 0".

NOT stopped, deliberately, although the chapter-set census flags them: the
target is right and the extra links are worth having.
  * "bacaan" (a sequencing read) -- English STOPs "read" because the English
    word is also a verb; the Indonesian noun is not, so chapters 5 and 14 keep
    98 correct links English cannot have.
  * "profil" (an HMM profile), "pembaca"/"penulis" (chromatin readers and
    writers), "silium", "antibodi", "antigen", "uji baca", "luar sasaran",
    "kaidah Oja", "pemusatan" -- every occurrence is the defined sense.
"""

# Terms kept for their own chapter only. Each of these is a one- or two-word
# display whose OTHER-chapter occurrences are a different sense entirely.
STOP = {
    # cloning vector (ch. 6) against the eigenvector of chapter 19's Oja rule
    "vektor", "Vektor",
    # genome assembly (ch. 4) against polymer, spindle and capsid assembly
    "perakitan", "Perakitan",
    # genome scaffold (ch. 4) against "burung perancah", the wading bird of
    # chapter 20's countercurrent exchangers
    "perancah", "Perancah",
    # BLAST seed (ch. 5) against plant seeds, seed banks, prion seeds and
    # Paget's "seed and soil"
    "benih", "Benih",
    # phage transduction (ch. 12) against sensory transduction (ch. 17, 18)
    "transduksi", "Transduksi",
    # microtubule catastrophe (ch. 9) against error catastrophe, systemic
    # catastrophe and chapter 19's catastrophic interference
    "bencana", "Bencana",
    # immunological tolerance (ch. 16) against the glucose tolerance test
    "toleransi", "Toleransi",
    # DNA lesion (ch. 3) against tissue, brain and endocrine lesions
    "lesi", "Lesi",
    # PCR primer (ch. 6) against "struktur primer", "silium primer" and
    # "tanggapan primer" -- Indonesian spells primer and primary alike
    "primer", "Primer",
    # innate barrier (ch. 15) against a leaky glomerular barrier (ch. 20)
    "penghadang", "Penghadang",
    # vesicle coat (ch. 8) against the complement coat of chapter 15
    "salut", "Salut",
    # crystallographic resolution (ch. 7) against optical, angular and
    # phylogenetic resolution
    "daya pisah", "Daya pisah",
    # viral reassortment (ch. 13) against antibody class switching (ch. 16)
    "penyusunan ulang", "Penyusunan ulang",
}

# No true homograph needed the heavier lever: every collision above is
# confined correctly by STOP's per-chapter fall-through.
DROP = set()

# display -> label, for a target the harvest cannot reach on its own.
# AUDITED against parts/bachelor-3/'s own label set.
EXTRA = {
    # English splits piRNA between two definitions by NUMBER: the singular
    # "piRNA" is one of the ncRNA classes (ch. 2's first definition), the
    # plural "piRNAs" opens the transposon-silencing definition. Indonesian
    # has no plural -s, so both collapse onto one key and the transposon
    # definition becomes unreachable. "gugus piRNA" (piRNA clusters) is
    # English's other key for that target and restores it.
    "gugus piRNA": "def:b3:rna-regulation:pirna",
}

NO_CAPITAL = set()

# Spans where a linkable word carries a sense the definition does not cover.
# None is anchored on a word that is itself a linked term.
EXTRA_PROTECT = [
    # "domain publik" is the public domain of a photograph credit, not a
    # protein domain -- 8 photo credits across six chapters.
    r'domain publik',
    # the embryo's head fold (ch. 23), not a protein fold
    r'lipatan kepala',
    # hormone conjugation (ch. 22), not bacterial conjugation
    r'sintesis, konjugasi',
    # an ordinary population death rate (ch. 27), not Gompertz's mortality rate
    r'laju kematiannya melampaui',
    # the spread of a titration curve (ch. 20), not neural divergence
    r'pemencaran kurva',
    # the bacterial cell envelope (ch. 14), not the viral envelope
    r'selubung, gerak, pengaturan',
]

# University register: an ambiguous term links nowhere rather than to a guess.
AMBIG_POLICY = "drop"
