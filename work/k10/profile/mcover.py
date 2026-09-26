#!/usr/bin/env python3
"""验证 binary n=9,R=1 的 level-m M-covering system 与实测码一致"""
from collections import Counter
n=9;N=512
BALL=[0]*N
for x in range(N):
    m=1<<x
    for i in range(n): m|=1<<(x^(1<<i))
    BALL[x]=m
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
for idx,C in enumerate(load(),1):
    Cs=set(C); bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    print(f"=== 码#{idx} ===")
    for m in (1,2,3,4):
        t=1<<m; cell=lambda x: x>>(n-m)   # 前 m 位作前缀
        y=Counter(cell(c) for c in C)
        sz=1<<(n-m)
        ok=True; rows=[]
        for i in range(t):
            # 覆盖 cell i 的总量 = Σ_j y_j * A_ji
            tot=0
            for j in range(t):
                if y[j]==0: continue
                d=bin(i^j).count('1')
                A=(10-m) if d==0 else (1 if d==1 else 0) if m>0 else 0
                tot+=y[j]*A
            rows.append(tot)
            if tot<sz: ok=False
        print(f"  m={m}: t={t} cells, 每 cell {sz} 词 | Σy={sum(y.values())}={len(C)} ✓ | 覆盖量 min={min(rows)} 需≥{sz} ⟹ {'✓ 系统满足' if ok else '✗ 违反'}")
        if m==1: print(f"         m=1 系统: 9y0+y1={9*y[0]+y[1]}, y0+9y1={y[0]+9*y[1]} (需≥256) ⟹ y=({y[0]},{y[1]})")
