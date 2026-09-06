#!/usr/bin/env python3
"""One \\omterm target, two different display strings: a terminology drift.

    python3 tools/check_term_display_drift.py parts/bachelor-1/ar
    python3 tools/check_term_display_drift.py parts/bachelor-1/fr --min 3

WHY THIS EXISTS. Nothing else in the toolchain can see this. The prose gates
ask "is this word foreign?"; id_apply's censuses ask "is this structure
identical to English?"; the collision censuses ask "is this target linked where
English does not link it?". A drift passes all three: every link is well
formed, every display is correct target-language prose, and the structure
mirrors English exactly. The book simply calls one concept two things in two
chapters, which splits a reader's mental index and looks like carelessness.

The Arabic Book 3 agent ran this by hand and it found NINE defects in about a
minute -- fatty acid written both الحموض الدسمة and الأحماض الدهنية across 17
sites, plus cytosol, endoplasmic reticulum, peroxisome, chaperone,
plasmodesmata and gluconeogenesis. On Physics Book 4 the same idea found six
more in Arabic (تدرّج/تدرج, مستقرّ/مستقر at 214 sites) and one in Indonesian.
Two spellings of one term also split its links across the count diff, which is
what makes the drift visible at all.

WHAT IT CANNOT DECIDE. Plenty of variation is CORRECT: a language inflects, and
a display is whatever surface form the sentence needed -- singular and plural,
definite and indefinite, a genitive construction. So this reports candidates
and ranks them; a human decides. Use --min to raise the floor, and read the
English twin's own display set beside each one: where English varies too, the
translation almost certainly should.
"""
import argparse
import collections
import pathlib
import re
import sys

OMTERM = re.compile(r"\\omterm\{([^}]*)\}\{((?:[^{}]|\{[^{}]*\})*)\}")


def displays(dirs):
    """{target: Counter(display -> n)} over every chapter and solutions file."""
    out = collections.defaultdict(collections.Counter)
    for d in dirs:
        p = pathlib.Path(d)
        for f in sorted(p.glob("[0-9]*.tex")):
            for m in OMTERM.finditer(f.read_text(encoding="utf-8")):
                # a display wrapped across a line is the same display
                out[m.group(1)][re.sub(r"\s+", " ", m.group(2)).strip()] += 1
    return out


def _twin(d):
    """parts/<year>[/solutions]/<lang> -> the English directory beside it."""
    parts = str(d).replace("\\", "/").rstrip("/").split("/")
    return "/".join(parts[:-1]) if len(parts[-1]) == 2 else None


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--min", type=int, default=2,
                    help="only report a variant seen at least this often (default 2)")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()

    dirs = list(args.dirs)
    # include the solutions twin automatically: half of Book 5's untranslated
    # \text{} fragments were there, and a drift is no different
    for d in list(dirs):
        sol = pathlib.Path(d).parent / "solutions" / pathlib.Path(d).name
        if sol.is_dir() and str(sol) not in dirs:
            dirs.append(str(sol))

    mine = displays(dirs)
    en_dirs = [t for t in (_twin(d) for d in dirs) if t and pathlib.Path(t).is_dir()]
    theirs = displays(en_dirs) if en_dirs else {}

    findings = 0
    for target, forms in sorted(mine.items()):
        strong = {f: n for f, n in forms.items() if n >= args.min}
        if len(strong) < 2:
            continue
        en_forms = theirs.get(target, {})
        en_strong = {f: n for f, n in en_forms.items() if n >= args.min}
        # English varying the same way is licence to vary: report it, rank last
        note = "  (English varies too: %d forms)" % len(en_strong) if len(en_strong) >= 2 else ""
        findings += 1
        print("  %s%s" % (target, note))
        for f, n in sorted(strong.items(), key=lambda kv: -kv[1]):
            print("      %4d  %s" % (n, f))
    if findings:
        print("\n  %d target(s) with two or more displays seen >= %d times."
              % (findings, args.min))
        print("  Not all are defects -- inflection is normal. Read each against"
              " its English twin.")
    elif not args.quiet:
        print("  term display drift: none (%d targets)" % len(mine))
    return 0


if __name__ == "__main__":
    sys.exit(main())
