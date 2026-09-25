#!/usr/bin/env python3
"""计数路线探路：⌈|U_D| / M(D)⌉ 是否恒 > d−1（M(D)=新字对 U_D 的最大重叠）"""
import itertools, random, sys
from collections import Counter
sys.argv=['x','5','none']
exec(open('/home/node/.openclaw/workspace/dn-project/work/k10/exact_pack.py').read().split('def main()')[0])
CODE=set(WORDS)
BALL=[0]*1024
for w in range(1024):
    m=1<<w
    for b in range(10): m|=1<<(w^(1<<b))
    BALL[w]=m
def stats(d, n):
    random.seed(31)
    # 不物化全池（d=5 时 C(120,5)=1.9e8 ⟹ 会 OOM）
    S=[tuple(sorted(random.sample(range(120), d))) for _ in range(n)]
    usz=[]; mx=[]
    for D in S:
        U=U_of(D); usz.append(U.bit_count())
        m=0
        for w in range(1024):
            if w in CODE: continue
            ov=(BALL[w]&U).bit_count()
            if ov>m: m=ov
        mx.append(m)
    lo=min(-(-u//m) for u,m in zip(usz,mx)); hi=max(-(-u//m) for u,m in zip(usz,mx))
    print(f"d={d} (n={len(S)}): |U_D|∈[{min(usz)},{max(usz)}] 均{sum(usz)/len(usz):.1f} | "
          f"M(D)∈[{min(mx)},{max(mx)}] {dict(sorted(Counter(mx).items()))}")
    print(f"        ceil(|U|/M)∈[{lo},{hi}] 需>{d-1} → {'OK' if lo>d-1 else 'NO'}", flush=True)
for d in (3,4,5):
    stats(d, 300 if d<5 else 60)
