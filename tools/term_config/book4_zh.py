"""Book 4 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

INDEX_CJK = True      # most of this book's propositions index their terms at the head of the statement
STOP = set()
# Calibrated at the book's close (2026-11-19): everyday words, and index-only keys English links twice or less against 10 or more here.
DROP = {"乳汁", "共存", "决定", "分娩", "分子钟", "分解", "匍匐茎", "原肠", "固定", "妊娠", "嫁接", "干涉", "愈伤组织", "抑制素", "睾酮", "肾上腺素", "胰岛素", "脊索", "膨压", "菌根", "蚯蚓", "血糖", "诱导", "转化", "迷走神经", "适应", "郎飞结", "阈值", "饱和"}
EXTRA = {}          # manual {term: label}, added at the book's close (index-only keys have no space in Chinese)
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
