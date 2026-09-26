#!/usr/bin/env python3
"""检验 8 位 doubled Hamming 的私有点与删除行为（K(8,1)=32 应阻止任何单点删除）"""
def hamming7():
    return [x for x in range(128) if (lambda v: v==0)(sum((i+1) for i in range(7) if (x>>i)&1)&0x7fffffff if False else 0) or True] if False else [x for x in range(128) if sum((i+1) for i in range(7) if (x>>i)&1)^0 == 0]
def syn(x):
    s=0
    for i in range(7):
        if (x>>i)&1: s^=(i+1)
    return s
H7=[x for x in range(128) if syn(x)==0]
C0=[(h<<1)|b for h in H7 for b in (0,1)]
n=8; N=256
NB=[[x^(1<<i) for i in range(n)] for x in range(N)]
def cov(S):
    c=0
    for w in S: c|=1<<w
    for w in S:
        for y in NB[w]: c|=1<<y
    return c
FULL=(1<<N)-1
print(f"|C0|={len(set(C0))} 覆盖={cov(C0)==FULL} ✓")
b={x:0 for x in range(N)}
for c in C0:
    for y in [c]+NB[c]: b[y]+=1
priv={c:[y for y in [c]+NB[c] if b[y]==1] for c in C0}
print(f"私有点总数 = {sum(len(v) for v in priv.values())}")
print(f"p(c) 分布 = {sorted(set(len(v) for v in priv.values()))}")
print(f"p=0 的码字数 = {sum(1 for v in priv.values() if len(v)==0)}")
# 删除检验
ok=0
for u in C0[:40]:
    C1=[c for c in C0 if c!=u]
    if cov(C1)==FULL: ok+=1
print(f"单点删除后仍覆盖的个数 = {ok} / 40 （K(8,1)=32 ⟹ 应为 0）")
print()
print("=== 结论 ===")
print(" 若 priv 全空 ⟹ 与 K(8,1)=32 矛盾 ⟹ 说明 priv 非空（我方手算错 ✗）")
print(" 对角构造需要 C1 = C0 删两词后 uncovered ⊆ C0；先看 uncovered 到底是什么")
for u in C0[:3]:
    C1=[c for c in C0 if c!=u]
    c=cov(C1); miss=[x for x in range(N) if not (c>>x)&1]
    print(f"  删除 {u:08b}: 未覆盖 {len(miss)} 点 {miss[:6]} 其中在 C0 内 {sum(1 for x in miss if x in set(C0))}")
