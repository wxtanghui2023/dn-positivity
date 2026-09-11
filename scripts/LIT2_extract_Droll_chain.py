#!/usr/bin/env python3
"""
LIT_2 (N2): extract from the archived Droll thesis the logical chain that turns the input inequality
into a theorem about the coefficients, so that we can see exactly which step our proved inequality
supplies and whether the classical case is covered.

Targets: the statements of Lemma 3.2.6, Conjecture 3.2.7, Corollary 3.2.4, and Theorem 3.3.1, plus
the remark that explains how the conjecture repairs Lemma 5 of the source.

Inputs : docs/Droll2012-thesis-Li-criterion-Selberg.pdf
Outputs: scripts/LIT2_extract_Droll_chain.txt
"""
import os, re
from PyPDF2 import PdfReader
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
rd = PdfReader(os.path.join(ROOT, 'docs', 'Droll2012-thesis-Li-criterion-Selberg.pdf'))
full = "\n".join((p.extract_text() or '') for p in rd.pages)
def show(label, pat, before=200, after=1100, maxhits=2):
    hits=[m.start() for m in re.finditer(pat, full)]
    print("\n### %s  (%d hit(s))" % (label, len(hits)))
    for h in hits[:maxhits]:
        seg=re.sub(r'\s+',' ', full[max(0,h-before):h+after])
        print("   ...", seg, "...\n")
show("Lemma 3.2.6 (the bound that Conjecture 3.2.7 replaces)", r'Lemma\s+3\.2\.6')
show("Conjecture 3.2.7", r'Conjecture\s+3\.2\.7')
show("Corollary 3.2.4", r'Corollary\s+3\.2\.4')
show("Theorem 3.3.1", r'Theorem\s+3\.3\.1')
show("how the conjecture repairs Lemma 5", r'repairs?|modified, generalized version|Lemma\s+5', after=700)
print("\n" + "="*100)
print("READ-OFF")
print("="*100)
print("  * if Conjecture 3.2.7 together with the lemma yields the theorem, and our note proves that")
print("    conjecture in the classical case, then that theorem becomes unconditional there.")
