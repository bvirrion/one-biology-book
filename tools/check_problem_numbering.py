#!/usr/bin/env python3
"""The weekend problem's answers must be numbered 1..k, with k questions.

    python3 tools/check_problem_numbering.py parts/bachelor-1          # English
    python3 tools/check_problem_numbering.py parts/bachelor-1/fr       # an edition

WHY THIS EXISTS. A weekend `problem` is a numbered list of \\item questions; its
solution answers them as a run of `\\textbf{N.}` paragraphs. That numbering is
PROSE, and no other check in this repository can see it:

  * check_translation.sh compares \\label sets, environment counts and
    \\begin{solution}{key} sequences -- an answer paragraph has none of those;
  * id_apply's censuses compare a translation against its English twin, so a
    defect present in BOTH is invisible by construction;
  * every prose gate reduces the file to visible text and asks whether words are
    foreign, never whether a sequence of integers is complete.

Biology Book 3's English canon shipped `solutions/16-biosyntheses-integration`
with 25 questions and 24 answers: the answer labelled 13 was question 12's, and
question 13 -- the ATP cost of gluconeogenesis -- had no answer at all. Three
separate translation agents found it by reading, which is not a gate. Found
2026-09-06; the check was proposed by the French Book 3 agent.

WHAT IT CANNOT SEE, deliberately stated so nobody trusts it too far: a
PERMUTATION. The same book's `solutions/25-populations` had answers 16, 17 and
18 present, in order, individually correct, and attached to the wrong questions
(16 asked the maximum sustainable yield and was answered with the doubling
time). The integers are a complete 1..k run, so this check passes it. Reading
the answers against the questions is the only thing that finds that class.
"""
import argparse
import pathlib
import re
import sys

PROBLEM = re.compile(r"\\begin\{problem\}(.*?)\\end\{problem\}", re.S)
ANSWER = re.compile(r"\\textbf\{(\d+)\.\}")


def check_dir(d, findings):
    """Check one CHAPTER directory. A solutions directory is skipped.

    The chapters and their solutions are two halves of one comparison, so this
    takes the chapter half and finds the other itself. Handing it a solutions
    directory as well used to make it walk those files as if they were
    chapters -- comparing each solution against itself, always passing, and
    reporting twice the real chapter count ("OK (58 chapters)" for a
    29-chapter book). Harmless but misleading, and it made the call in
    check_translation.sh read as though solutions were being skipped. Reported
    by the Arabic and French Book 3 agents, 2026-09-06.
    """
    d = pathlib.Path(d)
    if d.name == "solutions" or d.parent.name == "solutions":
        return 0                      # the twin half; check_dir finds it itself
    sol = d / "solutions" if (d.name.startswith(("bachelor-", "grade-"))) \
        else d.parent / "solutions" / d.name
    n = 0
    for ch in sorted(d.glob("[0-9]*.tex")):
        twin = sol / ch.name
        if not twin.is_file():
            continue
        n += 1
        m = PROBLEM.search(ch.read_text(encoding="utf-8"))
        if not m:
            continue                     # a chapter may carry no weekend problem
        items = len(re.findall(r"\\item", m.group(1)))
        nums = [int(x) for x in ANSWER.findall(twin.read_text(encoding="utf-8"))]
        if not nums:
            continue                     # answers not written as \textbf{N.}
        expected = list(range(1, items + 1))
        if nums == expected:
            continue
        missing = [i for i in expected if i not in nums]
        extra = [i for i in nums if i not in expected]
        dupes = sorted({i for i in nums if nums.count(i) > 1})
        why = []
        if missing:
            why.append("missing " + ",".join(map(str, missing)))
        if extra:
            why.append("out of range " + ",".join(map(str, extra)))
        if dupes:
            why.append("repeated " + ",".join(map(str, dupes)))
        if not why:
            why.append("out of order")
        findings.append("%s: %d questions, %d answers (%s)"
                        % (twin, items, len(nums), "; ".join(why)))
    return n


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("dirs", nargs="+")
    ap.add_argument("--quiet", action="store_true")
    args = ap.parse_args()
    findings, files = [], 0
    for d in args.dirs:
        files += check_dir(d, findings)
    if findings:
        print("  problem numbering: %d issue(s)" % len(findings))
        for f in findings:
            print("      " + f)
        return 1
    if not args.quiet:
        print("  problem numbering: OK (%d chapters)" % files)
    return 0


if __name__ == "__main__":
    sys.exit(main())
