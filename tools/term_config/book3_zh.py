"""Book 3 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

# Calibrated against book3_en.py and the census at the book's close (2026-11-19).
# Everyday words here; English links them little or not at all.
STOP = {"吸收", "消化", "竞争", "固定", "碱基", "基质", "偶联", "水解"}
DROP = {"能量", "物质", "信息", "速率", "反应速率", "营养", "联系", "生殖"}
EXTRA = {
    "碱基对": "thm:b1:nucleic-acids:helix",
    "双螺旋": "thm:b1:nucleic-acids:helix",
    "自由能": "prop:b1:water-small-molecules:gibbs",
    "过渡态": "prop:b1:enzymes:whatitdoes",
    "活化能": "prop:b1:enzymes:whatitdoes",
    "环境容纳量": "thm:b1:populations:logistic",
    "逻辑斯谛增长": "thm:b1:populations:logistic",
    "光反应": "prop:b1:photosynthesis:lightreactions",
    "克莱伯定律": "thm:b1:organism-environment:kleiber",
    "根压": "prop:b1:plant-water-minerals:rootpressure",
    "检查点": "prop:b1:replication-mitosis:checkpoints",
    "营养级效率": "thm:b1:ecosystem-organization:lindeman",
    "碳酸酐酶": "prop:b1:gas-exchange:transport",
    "玻尔效应": "prop:b1:gas-exchange:transport",
    "霍尔丹效应": "prop:b1:gas-exchange:transport",
    "裂解周期": "prop:b1:genomes:lambda",
    "溶源周期": "prop:b1:genomes:lambda",
    "查加夫": "prop:b1:nucleic-acids:chargaff",
    "质子泵": "prop:b1:plant-water-minerals:uptake",
    "指数增长": "thm:b1:populations:exponential",
    "消化道": "prop:b1:digestion-absorption:tract",
    "硝酸还原酶": "prop:b1:plant-water-minerals:nitrate",
    "中度干扰假说": "prop:b1:ecosystem-dynamics:idh",
    "岛屿生物地理学": "thm:b1:ecosystem-dynamics:island",
    "圆盘方程": "thm:b1:species-interactions:holling",
    "能斯特方程": "thm:b1:membranes-transport:nernst",
    "平衡电位": "thm:b1:membranes-transport:nernst",
    "压力流": "thm:b1:plant-transport:pressureflow",
    "脱落酸": "prop:b1:plant-transport:opening",
    "米氏常数": "thm:b1:enzymes:mm",
    "米氏方程": "thm:b1:enzymes:mm",
    "细胞学说": "prop:b1:cell-unit-of-life:theory",
    "巴斯德效应": "prop:b1:respiration-fermentation:pasteur",
    "水分利用效率": "prop:b1:plant-transport:wue",
    "信号肽": "prop:b1:gene-expression:after",
}
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
