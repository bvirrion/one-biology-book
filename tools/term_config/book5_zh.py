"""Book 5 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

INDEX_CJK = True      # most propositions index their terms at the head of the statement (as Book 4)
# English STOPs read, domain, fold, seed, niche, tolerance, vector, coat, rod, imprinting, positive selection (book5_en.py): the same
# words here keep their links inside their own chapter.
STOP = {"读段", "结构域", "折叠", "种子", "生态位", "耐受", "载体", "衣壳", "视杆", "印记", "正选择"}
# Calibrated at the book's close (2026-11-19): index-only keys English links twice or less against 10 or more here, and 转化.
DROP = {"TSH", "克隆", "清除率", "潜伏", "筛选", "缺氧", "耐药性", "肌酐", "覆盖度", "重叠群", "阈值", "高尔基体", "转化"}
EXTRA = {t: "def:b3:rna-regulation:ncrna" for t in ("ncRNA", "miRNA", "siRNA", "piRNA", "lncRNA")}   # the Chinese keys of this definition hold a space and cannot link (Book 2 finding)          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
