"""Book 3 -- id. Curation only; the rules live in tools/termlink/.

Curated from THIS edition's own harvest (never seeded from book3_en.py or from
book2_id.py). Two censuses were run against the English twin -- per-target link
frequency and per-target chapter set -- and every entry below answers a
collision that one of them exposed.

University register (Year 1), so AMBIG_POLICY is "drop", matching book3_en.py.

Regenerate with:
  python3 tools/link_defined_terms.py --book 3 --lang id --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --lang id --apply
"""

# Every entry is an Indonesian word that is BOTH a defined term's index key and
# an ordinary word of the language, so the linker mints a well-formed link
# pointing at the wrong definition. English has no term for any of them (each
# target below carried ZERO English links, or the English term was the longer
# phrase that survives here), so dropping them moves the edition TOWARD the
# English profile, not away from it.
STOP = {
    # "air" is simply water; it is also the second half of "ruang udara",
    # "air laut", "air tanah", "air sungai" ... 370 links against 0 in English,
    # which links only "hydrogen bonds" and "polar molecules" to this target.
    "air",
    # "polar" is an adjective before it is a term ("landaian polar", "sisi
    # polar"); the two-word "molekul polar" survives and matches English.
    "polar",
    # "asam" is the head of "asam amino", "asam lemak", "asam nukleat", "asam
    # karbonat", "asam absisat" -- none of them the pH definition. English
    # links "base"/"pH" here and never "acid"; "basa" is kept for that reason.
    "asam",
    # "laju" is *rate* in every chapter: laju alir, laju pertumbuhan, laju
    # serangan, laju kelahiran. 143 links against 0 in English. The two-word
    # "laju reaksi" survives.
    "laju",
    # The three exchanges of an open system. In Indonesian each is an ordinary
    # noun that appears on nearly every page ("energi", "materi", "informasi"):
    # 238 links against 0 in English, which links only the full
    # "exchange of energy/matter/information" phrases.
    "energi", "materi", "informasi",
    # "ciri" is *feature* in ordinary prose ("ciri yang menaikkan fluksnya");
    # English does not link "character" either.
    "ciri",
    # The three transporter words are all common nouns: "pembawa" (bearer,
    # "pembawa pesan"), "pompa" ("sistem dua pompa" of a fish's gills), and
    # "saluran" -- which is also *duct* and *tract*: "saluran pencernaan",
    # "saluran udara", "saluran xilem". English links "channel" cleanly because
    # English has separate words; Indonesian does not, so the 20 legitimate
    # ion-channel links are given up rather than ship ten wrong-sense ones.
    # "pompa natrium--kalium", "difusi terbantu" and "akuaporin" survive.
    "pembawa", "pompa", "saluran",
    # Source and sink of the phloem. "sumber" is *source* in "sumber daya",
    # "sumber energi", "lubuk sumber"; "penampung" is any receptacle. English
    # links "phloem" and "sieve tube" only, and "floem"/"tabung tapis" survive.
    "sumber", "penampung",
    # "rangka" is *frame* as well as *skeleton* ("rangka sel", "dalam rangka");
    # "hidrostatik" is an adjective of pressure ("tekanan hidrostatik").
    # "rangka luar", "rangka dalam" and "rangka hidrostatik" survive.
    "rangka", "hidrostatik",
    # A verb: *to separate*. It reached the microscope's resolving power 22
    # times, every one of them the ordinary verb. "daya pisah" survives.
    "memisahkan",
    # The three great functions of an organism are ordinary nouns in
    # Indonesian; "laju reproduksi" linked *reproduksi* to the definition of
    # the functions. The "fungsi ..." forms survive.
    "nutrisi", "reproduksi", "relasi",
    # "penumpukan" is *accumulation* as often as *stacking* ("riwayat
    # penumpukan dan kehilangan"). "penumpukan basa" survives.
    "penumpukan",
    # "plasma" is a body-fluid compartment, but it is also the second half of
    # "membran plasma": once the membrane target was saturated in a file, the
    # leftover "plasma" was linked to the compartments definition inside the
    # phrase "membran plasma". "plasma darah" survives.
    "plasma",
}

NO_CAPITAL = set()

EXTRA = {}

# The same words again: STOP keeps them out of the global term table, but a
# stop-listed word still reaches the per-chapter "local sense" table, where a
# chapter with only one candidate definition links it anyway (that is how
# "laju" still reached the rate definition 38 times after STOP alone). DROP
# empties every table, which is what a homograph needs.
DROP = {
    "air", "polar", "asam", "laju", "energi", "materi", "informasi", "ciri",
    "pembawa", "pompa", "saluran", "sumber", "penampung", "rangka",
    "hidrostatik", "memisahkan", "nutrisi", "reproduksi", "relasi",
    "penumpukan", "plasma",
    # "bersaing" is the verb *to compete*: it linked the competitive-inhibition
    # definition from "asas penyisihan bersaing", "spesies bersaing" and
    # "rerumputan yang bersaing" all through the ecology chapters.
    "bersaing",
    # Smooth and rough endoplasmic reticulum. Alone, "halus" is *fine* and
    # *small* ("usus halus", "akar halus", "tabung halus", "kasa halus") and
    # "kasar" is *gross* and *coarse* ("produksi kasar", "asupan kasar",
    # "serat kasar"): 62 links, nearly all of them wrong-sense. The full
    # "retikulum endoplasma" survives.
    "halus", "kasar",
}

EXTRA_PROTECT = [
    # "batang otak" is the brainstem; "batang" alone is the stem of a plant and
    # was linked to the plant-organs definition inside it.
    r"batang\s+otak\w*",
    # "akar nyata" is a real root of a quadratic, not a plant root.
    r"akar\s+nyata",
]

AMBIG_POLICY = "drop"
