#!/usr/bin/env python3
"""
fix_my_scripts_data_path.py -- make this session's own scripts comply with rule R2.

R2 requires scripts to read their inputs from data/ rather than the volatile directory. The scripts
BL1..BL8 and NB1 were written during the session and read /tmp/zeros_odlyzko_2M.npy directly, which
is exactly the pattern the protocol forbids. This pass rewrites that load line to prefer data/ and
fall back to the volatile path only if data/ is absent.

Run from scripts/:  python3 fix_my_scripts_data_path.py
"""
import os, re, shutil
HERE = os.path.dirname(os.path.abspath(__file__))
TARGETS = ['BL1_decomposition_range.py','BL2_full_budget.py','BL3_conjecture327_route.py',
           'BL4_route_constants.py','BL4b_route_constants_fixed.py','BL5_final_verdict.py',
           'BL6_S4_sharp_with_boundary.py','BL7_S4_bothsigns_check.py','BL8_split_bound.py',
           'NB1_constant_verification.py']
SNIP = ("import os as _os\n"
        "_ZD = _os.path.join(_os.path.dirname(_os.path.dirname(_os.path.abspath(__file__))),'data')\n"
        "_ZP = _os.path.join(_ZD,'zeros_odlyzko_2M.npy')\n"
        "ZEROS_PATH = _ZP if _os.path.exists(_ZP) else '/tmp/zeros_odlyzko_2M.npy'   # R2: prefer data/\n"
        "ZEROS_100K = _os.path.join(_ZD,'zeros_odlyzko_100k.npy') if _os.path.exists(_os.path.join(_ZD,'zeros_odlyzko_100k.npy')) else '/tmp/zeros_odlyzko_100k.npy'\n")
pat = re.compile(r"np\.load\(\s*'/tmp/zeros_odlyzko_2M\.npy'\s*\)")
n=0
for t in TARGETS:
    p=os.path.join(HERE,t)
    if not os.path.exists(p): continue
    s=open(p,encoding='utf-8').read()
    if pat.search(s):
        shutil.copy2(p,p+'.bak')
        s=pat.sub("np.load(ZEROS_PATH)", s)
        # insert the snippet right after the first import block line
        lines=s.split('\n'); ins=0
        for i,l in enumerate(lines):
            if l.startswith('import ') or l.startswith('from '):
                ins=i+1
        lines[ins:ins]=SNIP.split('\n')
        open(p,'w',encoding='utf-8').write('\n'.join(lines)); n+=1
print("rewritten: %d" % n)
