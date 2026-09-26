#!/usr/bin/env python3
"""P10<->X4: (d1,p) 联合分布 + 可证跨层不等式 + P10 与 X4 的 incidence"""
import itertools
from collections import Counter, defaultdict
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
    Cs=set(C)
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    d1={c:sum(1 for c2 in C if c2!=c and bin(c^c2).count('1')==1) for c in C}
    p={}
    for c in C:
        nb=[c]+[c^(1<<i) for i in range(n)]
        p[c]=sum(1 for x in nb if bl[x]==1)
    joint=Counter((d1[c],p[c]) for c in C)
    print(f"[码#{idx}] (d1(c), p(c)) 联合分布:")
    for k in sorted(joint): print(f"     d1={k[0]}, p={k[1]}: {joint[k]} 个")
    # 可证不等式: p ≤ 9 - d1 + [d1==0]
    viol=[c for c in C if p[c]>9-d1[c]+(1 if d1[c]==0 else 0)]
    print(f"   **可证不等式 p(c) ≤ 9 − d₁(c) + [d₁=0]** : 违反 {len(viol)} {'✓✓' if not viol else '✗'}")
    print(f"   （证明: d₁ 方向 c+e_i∈C ⟹ b(c+e_i)≥2 ⟹ 非 private ✓; c 自身 private 仅当 d₁=0 ✓）")
    n0=sum(1 for c in C if d1[c]==0)
    A1=sum(d1.values())//2
    Sp=sum(p.values()); rhs=9*62-2*A1+n0
    ok = "OK" if Sp<=rhs else "FAIL"
    print("   A1=%d n0=%d  Sigma_p=%d | 求和式 N1 <= 9M-2A1+n0 = %d  %s" % (A1,n0,Sp,rhs,ok))
    # P10 与 X4
    P10=[c for c in C if p[c]==10]
    X4=[x for x in range(N) if bl[x]==4]
    inc=sum(1 for x in X4 for c in C if (BALL[x]>>c)&1 and p[c]==10)
    print(f"   **P10={len(P10)} 个 (p=10) | Σ_(x∈X4)|S_x∩P10| = {inc}**")
    print(f"   每 X4 点含 P10 码字数分布 = {dict(Counter(sum(1 for c in C if (BALL[x]>>c)&1 and p[c]==10) for x in X4))}")
    print(f"   P10 的码字是否参与 X4? (即是否有 p=10 的码字在某个 X4 球内): {inc>0}")
    # P10 的结构: 它们彼此距离? 它们与 X4 的关系?
    if P10:
        dd=Counter(bin(a^b).count('1') for a,b in itertools.combinations(P10,2))
        print(f"   P10 内部距离分布={dict(sorted(dd.items()))}")
        print(f"   P10 码字的 b 值分布={dict(Counter(bl[c] for c in P10))}")
