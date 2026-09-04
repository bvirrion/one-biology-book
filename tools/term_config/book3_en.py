"""Book 3 -- en. Curation only; the rules live in tools/termlink/.

University register (Year 1): the defined vocabulary is precise and links
nearly everywhere; the curation removes the words whose defined sense
collides with an ordinary or a second technical sense elsewhere in the
volume, and adds the plurals the harvest folded away. Curated on
2026-09-04 after the English edition landed. Regenerate after editing
definitions or prose with:
  python3 tools/link_defined_terms.py --book 3 --unwrap --apply
  python3 tools/link_defined_terms.py --book 3 --apply
"""

STOP = {
    # enzyme substrate in its chapter; the rock substrate of a succession
    # and the substrate of a reaction elsewhere
    "substrate", "substrates",
}

NO_CAPITAL = set()

EXTRA = {
    # plurals (and a few lower-case forms) the harvest folded away, all
    # single-sense in this volume
    "Okazaki fragments": "def:b1:replication-mitosis:fork",
    "aldoses": "def:b1:carbohydrates:monosaccharide",
    "allosteric enzymes": "def:b1:enzymes:allosteric",
    "alveoli": "def:b1:gas-exchange:lung",
    "amino acids": "def:b1:proteins:aminoacid",
    "anticodons": "def:b1:gene-expression:trna",
    "antiporters": "prop:b1:membranes-transport:secondary",
    "aquaporins": "def:b1:membranes-transport:transporters",
    "base pairs": "thm:b1:nucleic-acids:helix",
    "biotopes": "def:b1:ecosystem-organization:ecosystem",
    "buffers": "def:b1:water-small-molecules:buffer",
    "capsids": "def:b1:genomes:virus",
    "carbohydrates": "def:b1:carbohydrates:monosaccharide",
    "carotenoids": "def:b1:photosynthesis:pigments",
    "cells": "def:b1:cell-unit-of-life:cell",
    "centromeres": "def:b1:genomes:karyotype",
    "channels": "def:b1:membranes-transport:transporters",
    "chromatids": "def:b1:replication-mitosis:mitosis",
    "chromosomes": "def:b1:genomes:genome",
    "clades": "def:b1:classifying-biodiversity:systematics",
    "codons": "def:b1:gene-expression:code",
    "coenzymes": "def:b1:enzymes:enzyme",
    "cofactors": "def:b1:enzymes:enzyme",
    "communities": "def:b1:ecosystem-organization:ecosystem",
    "consumers": "def:b1:ecosystem-organization:trophic",
    "covalent bonds": "def:b1:water-small-molecules:bonds",
    "cristaes": "def:b1:eukaryotic-cell:mitochondrion",
    "cuticles": "def:b1:flowering-plant-organization:tissues",
    "decomposers": "def:b1:ecosystem-organization:trophic",
    "digestive enzymes": "prop:b1:digestion-absorption:enzymes",
    "disaccharides": "def:b1:carbohydrates:glycosidic",
    "double helixes": "thm:b1:nucleic-acids:helix",
    "ecosystem engineers": "def:b1:ecosystem-dynamics:engineers",
    "ecosystems": "def:b1:ecosystem-organization:ecosystem",
    "enterocytes": "def:b1:digestion-absorption:surface",
    "enzymes": "def:b1:enzymes:enzyme",
    "epitheliums": "def:b1:body-plans-tissues:epithelium",
    "essential elements": "def:b1:plant-water-minerals:elements",
    "exchange surfaces": "prop:b1:organism-environment:surfaces",
    "exons": "def:b1:genomes:gene",
    "fats": "def:b1:lipids:triglyceride",
    "food chains": "def:b1:ecosystem-organization:foodweb",
    "food webs": "def:b1:ecosystem-organization:foodweb",
    "genes": "def:b1:genomes:gene",
    "genomes": "def:b1:genomes:genome",
    "genuses": "def:b1:classifying-biodiversity:nomenclature",
    "gills": "def:b1:gas-exchange:gill",
    "glycerophospholipids": "def:b1:lipids:amphiphilic",
    "glycolipids": "def:b1:carbohydrates:glycoconjugate",
    "glycoproteins": "def:b1:carbohydrates:glycoconjugate",
    "guard cells": "def:b1:plant-transport:stoma",
    "habitats": "def:b1:ecosystem-organization:niche",
    "histones": "def:b1:genomes:nucleosome",
    "homologies": "def:b1:classifying-biodiversity:characters",
    "homoplasies": "def:b1:classifying-biodiversity:characters",
    "hydrophyte": "prop:b1:flowering-plant-organization:plasticity",
    "inhibitors": "def:b1:enzymes:inhibitors",
    "internodes": "def:b1:flowering-plant-organization:organs",
    "introns": "def:b1:genomes:gene",
    "ionic bonds": "def:b1:water-small-molecules:bonds",
    "isoclines": "prop:b1:species-interactions:lotka",
    "isoprenoids": "def:b1:lipids:steroids",
    "ketoses": "def:b1:carbohydrates:monosaccharide",
    "keystone specieses": "def:b1:species-interactions:keystone",
    "leaves": "def:b1:flowering-plant-organization:organs",
    "lichens": "def:b1:species-interactions:symbiosis",
    "life tables": "def:b1:populations:lifetable",
    "lipids": "def:b1:lipids:fattyacid",
    "lungs": "def:b1:gas-exchange:lung",
    "lysosomes": "def:b1:eukaryotic-cell:endomembrane",
    "macronutrients": "def:b1:plant-water-minerals:elements",
    "meristems": "def:b1:flowering-plant-organization:meristem",
    "micronutrients": "def:b1:plant-water-minerals:elements",
    "mitochondria": "def:b1:eukaryotic-cell:mitochondrion",
    "monosaccharides": "def:b1:carbohydrates:monosaccharide",
    "niches": "def:b1:ecosystem-organization:niche",
    "nitrogenous bases": "def:b1:nucleic-acids:nucleotide",
    "nucleosomes": "def:b1:genomes:nucleosome",
    "nucleotides": "def:b1:nucleic-acids:nucleotide",
    "oils": "def:b1:lipids:triglyceride",
    "operons": "def:b1:expression-control:operon",
    "organelle": "def:b1:cell-unit-of-life:prokeuk",
    "organisms": "def:b1:organism-environment:organism",
    "organs": "def:b1:mammal-organization:organ",
    "outgroups": "def:b1:classifying-biodiversity:characters",
    "parasites": "def:b1:species-interactions:symbiosis",
    "peptide bonds": "def:b1:proteins:peptide",
    "peroxisomes": "def:b1:eukaryotic-cell:peroxisome",
    "phospholipids": "def:b1:lipids:amphiphilic",
    "photosystems": "def:b1:photosynthesis:zscheme",
    "plasmodesmas": "def:b1:eukaryotic-cell:plantcell",
    "plasmodesmata": "def:b1:eukaryotic-cell:plantcell",
    "plastids": "def:b1:eukaryotic-cell:plastid",
    "polynucleotides": "def:b1:nucleic-acids:chain",
    "polypeptides": "def:b1:proteins:peptide",
    "polysaccharides": "def:b1:carbohydrates:polysaccharide",
    "populations": "def:b1:populations:population",
    "producers": "def:b1:ecosystem-organization:trophic",
    "proteins": "def:b1:proteins:peptide",
    "proteoglycans": "def:b1:carbohydrates:glycoconjugate",
    "proton pumps": "prop:b1:plant-water-minerals:uptake",
    "purines": "def:b1:nucleic-acids:nucleotide",
    "pyrimidines": "def:b1:nucleic-acids:nucleotide",
    "reading frames": "def:b1:gene-expression:code",
    "replication forks": "def:b1:replication-mitosis:fork",
    "repressors": "def:b1:expression-control:operon",
    "ribosomes": "def:b1:gene-expression:ribosome",
    "root nodules": "def:b1:plant-water-minerals:nodules",
    "roots": "def:b1:flowering-plant-organization:organs",
    "sieve tube": "def:b1:flowering-plant-organization:tissues",
    "sigma factors": "prop:b1:expression-control:trp",
    "signal peptides": "prop:b1:gene-expression:after",
    "specieses": "def:b1:classifying-biodiversity:species",
    "sphingolipids": "def:b1:lipids:amphiphilic",
    "steroids": "def:b1:lipids:steroids",
    "sterols": "def:b1:lipids:amphiphilic",
    "symporters": "prop:b1:membranes-transport:secondary",
    "synapomorphies": "def:b1:classifying-biodiversity:characters",
    "taxons": "def:b1:classifying-biodiversity:nomenclature",
    "telomeres": "def:b1:genomes:karyotype",
    "tissues": "def:b1:body-plans-tissues:tissue",
    "transcription factors": "def:b1:expression-control:enhancer",
    "triglycerides": "def:b1:lipids:triglyceride",
    "type specimens": "def:b1:classifying-biodiversity:nomenclature",
    "vacuoles": "def:b1:eukaryotic-cell:plantcell",
    "villi": "def:b1:digestion-absorption:surface",
    "viruses": "def:b1:genomes:virus",
    "waxes": "def:b1:lipids:wax",
    "xerophyte": "prop:b1:flowering-plant-organization:plasticity",
    "xylem vessels": "def:b1:plant-transport:xylem",
    "zwitterions": "def:b1:proteins:aminoacid",
}

DROP = {
    # the four exchanges of the open system are ordinary words everywhere
    # else ("energy", "matter", "information", "environment", "relation",
    # "reproduction", "nutrition"); "rate", "coupling", "recognition"
    # likewise
    "energy", "matter", "information", "environment", "relation",
    "reproduction", "nutrition", "rate", "recognition", "coupling",
    # water the molecule versus water everywhere; "acid" inside "amino
    # acid", "nucleic acid"
    "water", "acid",
    # blood plasma versus plasma membrane; extracellular versus mitochondrial
    # matrix; plant node versus lymph node versus tree node; phloem source
    # and sink versus the ordinary words; xylem vessel versus blood vessel;
    # plant stem versus stem cell; plant epidermis versus skin
    "plasma", "matrix", "node", "source", "sink", "vessel", "vessels",
    "stem", "epidermis",
    # membrane carrier versus NAD carrier; pump alone; "Integral" proteins
    # versus the integral of a function
    "carrier", "Carriers", "pump", "Pumps", "Integral",
    # microscope resolution versus the resolution of a conflict; systematic
    # character versus the character of a curve; competitive inhibition
    # versus competition; polar molecule versus cell polarity; smooth and
    # rough ER versus smooth muscle; saturated fatty acid versus a saturated
    # enzyme or saturated air; endoskeleton versus carbon skeleton;
    # ecological resistance versus antibiotic or electrical resistance;
    # condensation reaction versus chromosome condensation; two
    # denaturations; carbon versus nitrogen fixation; light absorption
    # versus absorption in the gut; base stacking versus grana; the lac
    # operator versus a mathematical operator; hydrostatic, indeterminate
    # and modular as bare adjectives
    "resolution", "resolves", "character", "competitive", "polar",
    "polarised", "smooth", "rough", "saturated", "unsaturated", "skeleton",
    "resistance", "condensation", "denaturation", "denaturation (DNA)",
    "denaturation (protein)", "Fixation", "absorption", "stacking",
    "operator", "hydrostatic", "indeterminate", "modular",
}

EXTRA_PROTECT = []

AMBIG_POLICY = "drop"
