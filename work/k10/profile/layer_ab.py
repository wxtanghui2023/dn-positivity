#!/usr/bin/env python3
"""Layer A (M-covering) vs Layer B (y-SIP): 二元 n=9,R=1
量化 Layer A 的粗度 = log2(给定 y 的 x 数)"""
import math
from collections import Counter
n=9; N=512
def load():
    codes=[];cur=[]
    for line in open('../c62/K_9_1_classif.txt'):
        a=line.split()
        if len(a)==9 and all(c in '01' for c in a): cur.append(int("".join(a),2))
        else:
            if len(cur)>=10: codes.append(cur)
            cur=[]
    if len(cur)>=10: codes.append(cur)
    return codes
print("=== Layer A 粗度: 固定 y 时 x 的自由度 ===")
for m in range(1,10):
    t=1<<m; s=1<<(n-m)
    # 以 M=62 均匀分配为例: y_j ≈ 62/t
    y0=62//t; rem=62-y0*t
    log2=0.0
    for j in range(t):
        yj=y0+(1 if j<rem else 0)
        if yj<=s: log2+=math.lgamma(s+1)-math.lgamma(yj+1)-math.lgamma(s-yj+1)
    print(f"  m={m}: cells={t:3d} 每cell={s:3d} | 给定均匀 y 的 log2(#x) ≈ {log2/math.log(2):.1f} 位 | m=9 时 = 0 位(唯一) ✓")
print()
print("=== Layer A 是否能看到 b-profile? (数值证据) ===")
for idx,C in enumerate(load(),1):
    Cs=set(C)
    BALL=[0]*N
    for x in range(N):
        mm=1<<x
        for i in range(n): mm|=1<<(x^(1<<i))
        BALL[x]=mm
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    prof=Counter(bl)
    print(f"  码#{idx}: b-profile N_j = {dict(sorted(prof.items()))} | N4={prof.get(4,0)}")
    for m in (1,2,3,4):
        t=1<<m; y=Counter(c>>(n-m) for c in C)
        print(f"     m={m}: y={tuple(y.get(j,0) for j in range(t))}")
print()
print("=== M=61 时各层 M-covering system 的可行性（解析）===")
for m in (1,2,3,4):
    t=1<<m; s=1<<(n-m); M=61
    y0=M//t; rem=M-y0*t
    ok=True; worst=9e9
    for i in range(t):
        tot=0
        for j in range(t):
            yj=y0+(1 if j<rem else 0)
            if yj==0: continue
            d=bin(i^j).count('1')
            A=(10-m) if d==0 else (1 if d==1 else 0)
            tot+=yj*A
        worst=min(worst,tot)
        if tot<s: ok=False
    print(f"  m={m}: 均匀 y 下最紧 cell = {worst} 需 ≥ {s} ⟹ {'系统仍可行 ✗ (不能排除 M=61)' if ok else '✗ 排除'}")
