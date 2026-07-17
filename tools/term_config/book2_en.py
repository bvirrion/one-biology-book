"""Book 2 -- en. Curation only; the rules live in tools/termlink/.

Every key is optional: anything left out falls back to the defaults in
tools/link_defined_terms.py (empty sets, AMBIG_POLICY "drop").

High school volume (Book 2) is written. Curate STOP / EXTRA as needed, then:
  python3 tools/link_defined_terms.py --book 2 --unwrap --apply
  python3 tools/link_defined_terms.py --book 2 --apply
"""

STOP = set()
NO_CAPITAL = set()
EXTRA = {}
DROP = set()
EXTRA_PROTECT = []
AMBIG_POLICY = "nearest-preceding"
