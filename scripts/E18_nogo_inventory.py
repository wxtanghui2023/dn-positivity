#!/usr/bin/env python3
"""
E18 (programme item): build the inventory of this project's negative results ("NO-GO map")
so that each one can be aligned against the frontier.

Why: the operator's programme is (1) align every direction's results with the frontier,
(2) align ALL negative results, (3) align model analyses, then extract the frontier's strengths
and look for breakthrough points. This script produces part (2): a machine-readable inventory.

Method
------
Scan docs/*.md for the documents that record negative/closed results, using the naming
conventions this project has used all along (no-go, closed, dead, archive, kill, verdict,
boundary, forbidden, audit, retraction, impossibility, wall, obstruction, nogo, DEAD, STOP).
For each hit, extract the title (first markdown heading) and the first substantive line, and emit
a table with columns:
    direction | document | title | marker (which keyword triggered) | alignment status (blank)
The alignment status column is intentionally left for the analyst to fill from the frontier reading.

Inputs : docs/*.md
Outputs: scripts/E18_nogo_inventory.txt  (and a companion .md table is written by the analyst)
"""
import os, re
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, 'docs')
KEY = ['no-go','nogo','closed','dead','kill','verdict','boundary','forbidden','retraction',
       'impossibility','wall','obstruction','archive','stop','barrier','vacu','失败','封','死']
def first_heading(txt):
    for line in txt.splitlines():
        s = line.strip()
        if s.startswith('#'):
            return re.sub(r'^#+\s*', '', s)[:110]
    return ''
def first_sub(txt):
    for line in txt.splitlines():
        s = line.strip()
        if s and not s.startswith('#') and not s.startswith('```') and len(s) > 25:
            return s[:150]
    return ''
rows=[]
for name in sorted(os.listdir(DOCS)):
    if not name.endswith('.md'): continue
    low=name.lower()
    hits=[k for k in KEY if k in low]
    if not hits: continue
    try: txt=open(os.path.join(DOCS,name),encoding='utf-8',errors='replace').read()
    except Exception: continue
    rows.append((name, first_heading(txt), first_sub(txt), ','.join(hits), len(txt)))
print("="*118)
print("E18 NO-GO inventory: %d documents matched the negative-result naming conventions" % len(rows))
print("="*118)
print("  %-46s %-8s %7s  %s" % ("document","marker","bytes","title"))
for n,h,s,m,sz in rows:
    print("  %-46s %-8s %7d  %s" % (n[:46], m[:8], sz, h[:64]))
print()
print("  columns for the alignment table (to be filled by the analyst):")
print("    status in { known-to-frontier (rediscovery) | ours-possibly-new | superseded | closed-by-frontier }")
print()
print("="*118); print("READ-OFF"); print("="*118)
print("  * %d candidate negative-result documents; the alignment table is docs/E18-NOGO-ALIGNMENT.md" % len(rows))
