#!/usr/bin/env python3
"""Fail if anything that looks like account data is in the tracked tree.

Patterns: 9-digit runs (Israeli ID numbers), 6+ digit path segments, 32-hex hashes,
identifier query params (relative=, sr_id=, req=<digits>), Israeli phone numbers.
Plus an optional, untracked denylist at local/pii-denylist.txt (one term per line —
put real member/doctor names there; the file itself is gitignored).

Exit 0 and print OK when clean; exit 1 and list hits otherwise.
"""
import pathlib, re, subprocess, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
PATTERNS = {
    "id-like 9 digits": re.compile(r"(?<!\d)\d{9}(?!\d)"),
    "6+ digit path segment": re.compile(r"/\d{6,}"),
    "32-hex hash": re.compile(r"\b[0-9A-Fa-f]{32}\b"),
    "identifier param": re.compile(r"(relative|sr_id)=[0-9A-Za-z]|req=\d"),
    "IL phone": re.compile(r"(?<!\d)0(5\d|[2-489]|7\d)-?\d{7}(?!\d)"),
}
deny = ROOT / "local" / "pii-denylist.txt"
terms = [t.strip() for t in deny.read_text().splitlines() if t.strip()] if deny.exists() else []

files = subprocess.run(["git", "ls-files", "--cached", "--others", "--exclude-standard"],
                       cwd=ROOT, capture_output=True, text=True).stdout.split()
hits = []
for f in files:
    p = ROOT / f
    if p.suffix not in {".md", ".json", ".py", ".txt", ""} or not p.is_file():
        continue
    for n, line in enumerate(p.read_text(errors="ignore").splitlines(), 1):
        for label, rx in PATTERNS.items():
            if rx.search(line) and f != "scripts/pii_check.py":
                hits.append(f"{f}:{n}: {label}")
        for t in terms:
            if t in line:
                hits.append(f"{f}:{n}: denylisted term")
if hits:
    print("\n".join(hits)); sys.exit(1)
print(f"OK — {len(files)} files, {len(terms)} denylist terms")
