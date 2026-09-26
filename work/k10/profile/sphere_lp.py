#!/usr/bin/env python3
"""A5 最后一刀: sphere-covering 线性不等式族 + 部分状态形式 + 与奇偶引理的接口"""
from collections import Counter, defaultdict
import itertools
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
print("=== ① 球交大小表 |B(u)∩B(v)| (n=9,R=1) ===")
for d in range(0,5):
    u=0; v=(1<<d)-1 if d<=n else 0
    # 取距离恰为 d 的一对
    v=0
    for i in range(d): v|=1<<i
    c=sum(1 for x in range(N) if (BALL[u]>>x)&1 and (BALL[v]>>x)&1)
    print(f"  d={d}: |B(u)∩B(v)| = {c}")
print("""  ⟹ d=0→10, d=1→2, d=2→2, d≥3→0 ✓
  故而 Σ_{y∈B(x)} b(y) = 10·1[x∈C] + 2·(d1(x)+d2(x)) ⟹ **恒为偶数** ✓""")
print()
print("=== ② 验证奇偶引理（本会话早前结果）===")
for idx,C in enumerate(load(),1):
    Cs=set(C)
    bl=[sum(1 for c in C if (BALL[c]>>x)&1) for x in range(N)]
    par=set(); vals=Counter()
    for x in range(N):
        s=[y for y in range(N) if (BALL[x]>>y)&1]
        OC=sum(bl[y]-1 for y in s)
        par.add(OC%2); vals[OC]+=1
    print(f"  码#{idx}: OC(B(x)) 的奇偶 = {par} ⟹ {'全部偶数 ✓（奇偶引理成立）' if par=={0} else '✗'}")
    print(f"          OC 分布 = {dict(sorted(vals.items()))}")
print()
print("=== ③ sphere-covering 不等式族（含部分状态形式）===")
print("""  全局形式: ∀S⊆Q_n:  Σ_c |B(c)∩S| ≥ |S|     （等价于 S 内每点被覆盖）
  部分状态: 设已固定码字集合 F，剩余 k 个待定:
            Σ_{c∈C\\F} |B(c)∩S| ≥ |S| − |{x∈S : x 被 F 覆盖}|
            ⟹ **线性不等式（对剩余码字的选择变量）** ✓ = 剪枝工具
  对偶: 权函数 w(x)≥0 且 Σ_{x∈B(c)}w(x) ≤ 1 ∀c ⟹ M ≥ Σ_x w(x)（= weighted covering ✓）""")
