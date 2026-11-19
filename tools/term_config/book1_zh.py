"""Book 1 -- Simplified Chinese. Curation only; the rules live in tools/termlink/.

Written 2026-11-18 for the pilot run (sources/TRANSLATION_BOOKS_1-5_ZH.md); refined at the book's close against the
link census (pilot_translation/census.py). Chinese is matched in CJK mode (lang_zh.py): no word boundary inside Han
text, so a word that is also part of a common compound must be stopped or dropped here. One-character terms never link.
"""

# result names are never terms
NOT_A_TERM = ("定理", "引理", "公式", "判据", "准则", "原理", "法则", "定律", "问题")

# Mirrors book1_en.py at the book's close (census, 2026-11-19): honest in their own chapter, ordinary everywhere else.
STOP = {
    "成体", "成年", "阶段", "平衡", "搏动", "心跳", "收缩", "对照", "田地", "运动", "分类", "树", "自然",
    # no English link at all, or everyday words in Chinese: 特征 (feature), 分解 (break down), 森林 (31 links against 2)
    "特征", "分解", "森林",
}
# English DROPs: signs-of-life vocabulary, body furniture, the senses, movement verbs, twice-used words
DROP = {
    "活的", "出生", "死亡", "取食", "生长", "幼体", "老年", "婴儿", "儿童", "青少年",
    "头", "颈", "手臂", "腿", "口腔", "尾巴",
    "感觉", "感官", "视觉", "听觉", "触觉", "嗅觉", "味觉", "眼睛", "耳朵", "鼻子", "舌头",
    "水", "飞行", "游动", "环节", "储备", "食物储备", "树枝", "树干", "纲", "鳞片", "胚",
    # 落叶 is also the fallen leaves on the ground
    "落叶",
}
# One-character terms never link in Chinese (根, 茎, 叶, 花, 芽): their two-character forms carry the target
EXTRA = {
    "叶子": "def:g1:plants-around-us:parts", "花朵": "def:g1:plants-around-us:parts",
    "根系": "def:g1:plants-around-us:parts", "茎干": "def:g1:plants-around-us:parts",
    "冬芽": "def:g6:life-through-seasons:buds", "芽苞": "def:g6:life-through-seasons:buds",
}
NO_CAPITAL = set()
DERIVED = {}
PRIMARY_OK = set()
AMBIG_POLICY = "nearest-preceding"
MAX_TERM_WORDS = 5
MAX_TERM_CHARS = 20
EXTRA_PROTECT = [
    r'生物学',      # biology, the subject, is not "living thing"
    r'人造|自然界',
]
