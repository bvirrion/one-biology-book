"""Book 5 -- ar. Curation only; the rules live in tools/termlink/.

Curated 2026-09-17 from THIS edition's own harvest (823 linkable terms, 2,290
links before curation), against the two censuses the instruction prescribes:
per-target FREQUENCY against the English twin and per-target CHAPTER SET.
Nothing here is translated from book5_en.py and nothing is seeded from
book4_ar.py.

The homograph families Arabic mints of its own are not English's. Two
properties of the language drive the whole list below:

  * Arabic builds its technical vocabulary out of ordinary verbal nouns
    (masdars). "قراءة" is both a sequencing read and the act of reading;
    "تحول" both bacterial transformation and any change at all; "إعادة"
    both hippocampal replay and the prefix "re-" of "إعادة الإدخال",
    "إعادة التوحش", "إعادة الاستعمار". The English twin has the same
    trouble with "read" and STOPs it; Arabic has it in a dozen more places.
  * lang_ar.py sets HEAD_ON_EVERY_WORD, so the article and the one-letter
    prepositions attach to every word of a phrase. That is what makes the
    edition link at all, and it also means a one-word masdar matches in
    every grammatical dress it wears (قراءة، القراءة، بقراءة، فالقراءة).

STOP is the right lever for all of these and DROP is not: each wrong link
sits in ANOTHER chapter, so folding the term into its own chapter's local
map keeps every correct link and removes every wrong one. That was measured
per term, not assumed -- the census was re-run after this file was written
and each entry below moved exactly the links it was meant to move.

Regenerate with:
  python3 tools/link_defined_terms.py --book 5 --lang ar --unwrap --apply
  python3 tools/link_defined_terms.py --book 5 --lang ar --apply
then a PLAIN dry run over the wrapped tree; "links to insert" must be 0.
"""

# Terms kept for their own chapter only (the harvest folds a STOPped term
# into the per-chapter local map). Each line names the chapter where the
# sense is pinned down, then the sense it was linking to elsewhere.
STOP = {
    # ch04 sequencing read -- against "قراءة" as the plain act of reading:
    # reading a gradient (ch23), reading a code (ch18), an open reading
    # frame (ch05). 86 links, of which only chapter 4's 48 were the read.
    "قراءة",
    # ch04 genome assembly -- against the assembly of a virion (ch13), of a
    # spliceosome (ch10), of a sensory map (ch18).
    "تجميع", "التجميع",
    # ch04 assembly again, by the display the harvest took from the same
    # definition; outside it the word is plain "characterisation".
    "توصيف",
    # ch05 BLAST seed -- against the plant seed (ch22) and, worse, against
    # amyloid seeding (ch07), which is a different technical sense.
    "بذرة",
    # ch07 X-ray/cryo-EM resolution -- against sensory discrimination
    # (ch18, five links), taxonomic resolution (ch14), immune discrimination
    # (ch15). English STOPs "resolution" for the same collision.
    "تمييز",
    # ch07 protein fold and protein domain -- against the neural fold and the
    # expression domain (ch23) and the plain "range" (ch10).
    "طية", "نطاق",
    # ch06 cloning vector -- against "ناقل عصبي" (neurotransmitter, ch17,
    # ch19), the carrier vesicle (ch08), the membrane transporter (ch20,
    # ch21, ch22). The plasmid displays reach the same target and stay.
    "ناقل",
    # ch11 tumour invasion -- against the invasion of a territory (ch26).
    "غزو",
    # ch12 conjugation and transformation -- against "اقتران" as any
    # coupling (ch19, ch22) and "تحول" as any change at all (ch22).
    "اقتران", "تحول", "التحول",
    # ch03 DNA lesion -- against "الآفة" as an affliction or a disorder
    # (ch19, ch21).
    "الآفة",
    # ch09 microtubule catastrophe -- against the environmental catastrophe
    # (ch27) and the catastrophic interference of ch19.
    "كارثة",
    # ch16 anergy -- against "خمود" as damping or exponential decay, which
    # is how ch21's control loops and ch27's heterozygosity use it.
    "خمود",
    # ch17 convergence of a circuit -- against convergent evolution (ch25),
    # convergence of a series (ch20, ch26).
    "تقارب",
    # ch18 basilar membrane -- "الغشاء القاعدي" is also the basement
    # membrane of a kidney corpuscle (ch20) and a plant cell (ch22).
    "الغشاء القاعدي", "غشاء قاعدي",
    # ch19 hippocampal replay -- against "إعادة" as the prefix "re-":
    # إعادة الإدخال, إعادة التوحش, إعادة التركيب, إعادة الاستعمار. 51 links,
    # of which 25 were in seven chapters that never mention a hippocampus.
    "إعادة",
    # ch23 embryonic induction -- against induced pluripotency (ch24).
    "استحثاث",
    # ch13 viral latency -- "الكمون" is also the latency of a reflex and the
    # membrane potential of a neuron (ch17), which is the sense every Arabic
    # physiology text gives it.
    "الكمون",
}

# Terms removed from the term set entirely -- the lever for a true homograph,
# where STOP's per-chapter fall-through would still leave wrong links. Arabic
# needed none in this volume: every collision measured here is cross-chapter,
# and STOP removes it without costing the correct links.
DROP = set()

# display -> label, for a target harvest.py cannot reach on its own. Every
# entry was checked against parts/bachelor-3/'s own label set AND against the
# place in the Arabic prose where it occurs (a term is never linked inside its
# own definition, so a phrase that appears nowhere else buys nothing).
EXTRA = {
    # def:b3:rna-regulation:pirna is reachable in English only through the
    # PLURAL key "piRNAs"; the singular harvests to the ncRNA definition
    # instead. Arabic does not mark that plural, so every "piRNA" in this
    # edition landed on ncRNA and the piRNA definition was an unreachable
    # target. English's other key for it is "piRNA clusters" -- here
    # "عناقيد piRNA", in the same sentence of the solutions -- and the
    # exercise on hybrid dysgenesis says "بجزيئات piRNA".
    "عناقيد piRNA": "def:b3:rna-regulation:pirna",
    "جزيئات piRNA": "def:b3:rna-regulation:pirna",
    # English links these four from a phrase whose Arabic equivalent the
    # harvest does not take from the statement (the Arabic display in the
    # environment differs from the one used in the running prose).
    "مقاومة الصادات": "def:b3:bacteriology:resistance",
    "وحدات تصنيفية إجرائية": "met:b3:microbiomes:16s",
    "محرّك السوط البكتيري": "prop:b3:cytoskeleton-motility:flagellar-motor",
    "نقل مورّثي تعايشي": "prop:b3:microbiomes:reduction",
    # lang_ar.py has no WORD_TAIL (Arabic pluralises by internal vowel
    # change), and it has no suffix rule either, so an attached pronoun has
    # to be declared term by term, as that file says. English's single link
    # to the conservation-tools definition is the photograph caption
    # "after their reintroduction"; Arabic writes "بعد إعادة إدخالها".
    "إعادة إدخالها": "def:b3:conservation-biology:tools",
    # English links "polygenic score" from the exercise; the Arabic exercise
    # says "درجة تعدد المورّثات" where the definition says
    # "درجة متعددة المورّثات".
    "درجة تعدد المورّثات": "def:b3:genomics:gwas",
}

# Regexes marking spans that must NOT be linked (a collocation where the term
# carries another sense). Never anchor one on a word that is itself a term --
# once that word is wrapped the lookaround stops matching and the protection
# lapses silently. None was needed here: every collision this edition has is
# a whole-word one that STOP already settles.
EXTRA_PROTECT = []

# Displays that must not be matched in their capitalised form. Arabic has no
# letter case, so this list is empty by construction.
NO_CAPITAL = set()

# University register: an ambiguous term links nowhere rather than to a guess.
AMBIG_POLICY = "drop"
