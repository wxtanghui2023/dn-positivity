#!/usr/bin/env python3
"""
LIT_1: extract from the archived Droll thesis the exact statements that stand in for Brown (2005),
whose original is paywalled with no open copy: Conjecture 1.7.10 (Brown's Theorem 2 as restated),
the discussion of the two errors in Brown's Lemma 5, and Brown's Theorem 3.

Why: the coefficient direction rests on Brown's Theorem 2 ("zero-free region implies non-negativity of
finitely many Li coefficients"), whose proof is defective. Droll restates it as a conjecture and quotes
the key inequality, so the thesis is the authoritative accessible source for that statement.

Inputs : docs/Droll2012-thesis-Li-criterion-Selberg.pdf
Outputs: scripts/LIT_extract_Droll_conjecture.txt
"""
import os, re
try:
    from PyPDF2 import PdfReader
except Exception:
    from pypdf import PdfReader
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF = os.path.join(ROOT, 'docs', 'Droll2012-thesis-Li-criterion-Selberg.pdf')
rd = PdfReader(PDF)
n = len(rd.pages)
print("="*100); print("Droll (2012) thesis: %d pages -- extracting the Brown-related statements" % n); print("="*100)
texts = []
for i in range(n):
    try: texts.append(rd.pages[i].extract_text() or '')
    except Exception: texts.append('')
full = "\n".join(texts)
pats = [
    ('Conjecture 1.7.10 (= Brown Thm 2 restated)', r'Conjecture\s+1\.7\.10'),
    ('Brown Theorem 2 (as cited)',                 r'Theorem\s+2'),
    ('Brown Theorem 3 (as cited)',                 r'Theorem\s+3'),
    ('Lemma 5 errors',                             r'Lemma\s+5'),
    ('Conjecture 3.2.7',                           r'Conjecture\s+3\.2\.7'),
]
for label, pat in pats:
    hits = [m.start() for m in re.finditer(pat, full)]
    print()
    print("### %s : %d occurrence(s)" % (label, len(hits)))
    for h in hits[:3]:
        seg = re.sub(r'\s+', ' ', full[max(0,h-260):h+900])
        print("   ...", seg[:1150], "...")
        print()
print("="*100); print("READ-OFF"); print("="*100)
print("  * the extracted passages above are the accessible statements of Brown's results;")
print("  * they are quoted from the thesis, so any citation in our work must say so (thesis, not the")
print("    original journal article), unless the original is obtained.")
