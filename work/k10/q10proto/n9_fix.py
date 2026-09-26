#!/usr/bin/env python3
"""修正版：CW=码字指示掩码 ✓；COV=覆盖掩码 ✓（严格分名 ✓）"""
import random
from collections import Counter
n=9; N=1<<n
NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
BM=[1<<x for x in range(N)]
for x in range(N):
    for y in NB[x]: BM[x]|=1<<y
FULL=(1<<N)-1
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C8=[(h<<1)|b for h in H7 for b in (0,1)]
C9=[(c<<1)|b for c in C8 for b in (0,1)]
def COV(C):
    c=0
    for w in C: c|=BM[w]
    return c
def CW_of(C):
    m=0
    for w in C: m|=1<<w
    return m
def stats(C):
    CW=CW_of(C); COV_=COV(C)
    b=[bin(BM[x]&CW).count('1') for x in range(N)]      # 距 x ≤1 的码字数 ✓
    Q=sum((v-1)*(v-2)//2 for v in b)
    return dict(M=len(C),cover=(COV_==FULL),Q=Q,minb=min(b),maxb=max(b),
                dist=dict(sorted(Counter(b).items())),sum_b=sum(b),E=len(C)*(n+1)-N,
                Qmod2=Q%2)
r=stats(C9)
print("=== (9,64) 覆盖码（doubled(8,32)×2）===")
print(f"  M={r['M']} 覆盖={r['cover']}  Q={r['Q']}  minb={r['minb']} maxb={r['maxb']}")
print(f"  Σb={r['sum_b']} (=M(n+1)={r['M']*10} ✓)  E={r['E']}  Q≡{r['Qmod2']} (应 ≡E={r['E']} mod2 ✓)")
print(f"  b 分布={r['dist']}")
# 快速删词搜索（限时）
def cnt_build(C):
    cnt=[0]*N
    for w in C:
        cnt[w]+=1
        for y in NB[w]: cnt[y]+=1
    return cnt
import time
t0=time.time(); best=None; random.seed(11)
while time.time()-t0<150:
    C=set(C9)
    for _ in range(2): C.discard(random.choice(sorted(C)))
    cnt=cnt_build(C)
    for st in range(800):
        zeros=[z for z in range(N) if cnt[z]==0]
        if not zeros: break
        x=random.choice(zeros); w=random.choice([x]+NB[x])
        if w in C: continue
        cnt[w]+=1
        for y in NB[w]: cnt[y]+=1
        C.add(w)
        rem=[c for c in C if c!=w and cnt[c]>=2 and all(cnt[y]>=2 for y in NB[c])]
        c=random.choice(rem) if rem else random.choice([q for q in C if q!=w])
        cnt[c]-=1
        for y in NB[c]: cnt[y]-=1
        C.discard(c)
    if all(cnt[z]>0 for z in range(N)) and len(C)<=63:
        if best is None or len(C)<len(best): best=set(C)
print(f"\n删词搜索 150s: {'得 M='+str(len(best)) if best else '未达 ≤63 ✗'}")
if best:
    r2=stats(best); print(f"   M={r2['M']} 覆盖={r2['cover']} Q={r2['Q']} minb={r2['minb']} maxb={r2['maxb']}")
    print(f"   b 分布={r2['dist']}  E={r2['E']}  Q≡{r2['Qmod2']}")
