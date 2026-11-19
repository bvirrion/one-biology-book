"""Book 2 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

# Mirrors book2_en.py at the book's close (census, 2026-11-19).
# 耐药, 训练, 睾酮: everyday or chapter words here (112, 49 and 54 links against 2, 7 and 6 in English)
STOP = {"眼睛", "抗性", "频率", "分辨率", "耐药", "训练", "睾酮"}
DROP = {"文化", "携带者", "碱", "碱基"}
EXTRA = {}
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = []
