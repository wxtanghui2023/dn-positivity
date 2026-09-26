#!/usr/bin/env python3
"""对角构造: C = C0×{0} ∪ C1×{1} ⊆ F_2^9，|C0|=32,|C1|=30 ⟹ 62
 覆盖条件 ⟺ N[C0]=F_2^8 (自动) 且 U1 := F_2^8 \ N[C1] ⊆ C0
 目标: 找 C1 (30 词) 使 U1 ⊆ C0 ⟹ 显式 (9,62) 覆盖码"""
import random
from collections import Counter
n=8; N=256
def hamming7():
    syn=lambda x: sum((i+1) for i in range(7) if (x>>i)&1)^0
    s=[]
    for x in range(128):
        v=0; t=x
        for i in range(7):
            if (t>>i)&1: v^=(i+1)
        if v==0: s.append(x)
    return s
H7=hamming7()
C0=[(h<<1)|b for h in H7 for b in (0,1)]        # 32 词，doubled Hamming
assert len(set(C0))==32
NB=[[x^(1<<i) for i in range(8)] for x in range(N)]
def covered(S):
    c=0
    for w in S: c|=1<<w
    for w in S:
        for y in NB[w]: c|=1<<y
    return c
cov0=covered(C0); FULL=(1<<N)-1
assert cov0==FULL, "C0 必须覆盖 F_2^8"
C0s=set(C0)
def bad(S):
    cov=covered(S); miss=[x for x in range(N) if not (cov>>x)&1]
    return sum(1 for x in miss if x not in C0s), miss
best=None
random.seed(11)
for trial in range(40):
    S=set(random.sample(range(N),30))
    b,_=bad(S); T=2.0
    for it in range(20000):
        T=max(0.02,T*0.9997)
        out=random.choice(list(S)); inn=random.randrange(N)
        if inn in S: continue
        S2=(S-{out})|{inn}
        b2,_=bad(S2)
        if b2<=b or random.random()<pow(2.718281828,-(b2-b)/max(T,1e-9)):
            S,b=S2,b2
        if b==0: break
    if b==0:
        best=sorted(S); break
    if best is None: pass
print("=== 对角构造搜索结果 ===")
if best:
    print(f"✅ 找到 C1 (30 词) 使 U1 ⊆ C0 ⟹ |C| = 32+30 = 62 ✓✓")
    C1=best
    C=sorted([((w<<1)|0) for w in C0]+[((w<<1)|1) for w in C1])
    print(f"  |C| = {len(C)} (去重后)")
    # 验证覆盖
    NB9=[[x^(1<<i) for i in range(9)] for x in range(512)]
    cov=0
    for w in C:
        cov|=1<<w
        for y in NB9[w]: cov|=1<<y
    full=(1<<512)-1
    print(f"  覆盖 F_2^9: {cov==full} ✓  (未覆盖数 = {512-bin(cov).count('1')})")
    open('wille62_candidate.txt','w').write("\n".join(f"{w:09b}" for w in C))
    print(f"  已写 wille62_candidate.txt ({len(C)} 词)")
else:
    print("✗ 未找到（需要更强搜索/不同 C0）")
print()
print("=== 构造原理 ===")
print(" (x,0) 被覆盖 ⟺ x ∈ N[C0] ∪ C1 = F_2^8 ✓（自动）")
print(" (x,1) 被覆盖 ⟺ x ∈ N[C1] ∪ C0 ⟹ 条件 = U1 := F_2^8 \\ N[C1] ⊆ C0 ✓")
print(" |C| = |C0| + |C1| = 32 + 30 = 62 ✓（比盲搜 62 出 512 少了一个数量级 ✓）")
