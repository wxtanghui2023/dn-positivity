#!/usr/bin/env python3
"""n=8 证伪 v3（结构性）：广义 doubling 族 C(A,B)={(a,0)}∪{(b,1)}, A=Hamming(7), B=任意16子集。
   覆盖 ⟺ N(B)∪A = 全空间。在族内局部搜索，找 Q!=0 的 (8,32)_1 码 ⟹ 推翻 n=8 pinning ✗"""
import random
from itertools import combinations
from collections import Counter
n,N,M=8,256,32; E=M*(n+1)-N
BALL=[]
for v in range(N):
    m=1<<v
    for i in range(n): m|=1<<(v^(1<<i))
    BALL.append(m)
FULL=(1<<N)-1
H=[[1,1,1,0,1,0,0],[1,1,0,1,0,1,0],[1,0,1,1,0,0,1]]
H7=[x for x in range(128) if all(sum(H[r][i]*((x>>i)&1) for i in range(7))%2==0 for r in range(3))]
A=set(H7)
# 用 7 位词表示 (word, bit)：code = {(w,0) for w in A} ∪ {(w,1) for w in B}
def to8(w,b): return (w<<1)|b
def code_of(B): return set([to8(w,0) for w in A]) | set([to8(w,1) for w in B])
def valid(B):
    c=0
    for w in B: c|=BALL[to8(w,1)]
    for w in A: c|=BALL[to8(w,0)]
    return c==FULL
def stats(B):
    C=code_of(B); cnt=[0]*N
    for c in C:
        mm=BALL[c]
        while mm:
            low=mm&-mm; cnt[low.bit_length()-1]+=1; mm^=low
    A1=sum(1 for a,b in combinations(sorted(C),2) if (a^b).bit_count()==1)
    A2=sum(1 for a,b in combinations(sorted(C),2) if (a^b).bit_count()==2)
    return dict(Q=sum((bb-1)*(bb-2)//2 for bb in cnt), A1=A1, A2=A2, b=dict(sorted(Counter(cnt).items())))
print("起点 B=H7 =", stats(set(H7)), flush=True)
random.seed(3)
B=set(H7); found={frozenset(B):stats(B)}; acc=0
for step in range(400000):
    out=[w for w in range(128) if w not in B]
    b_out=random.choice(sorted(B)); b_in=random.choice(out)
    B2=(B-{b_out})|{b_in}
    if not valid(B2): continue
    B=B2; acc+=1
    key=frozenset(B)
    if key not in found:
        found[key]=stats(B)
        s=found[key]
        if len(found)%50==0 or s['Q']!=0:
            print(f"[{acc}] 新码 #{len(found)}: Q={s['Q']} A1={s['A1']} A2={s['A2']} b={s['b']}", flush=True)
    if acc>=4000: break
qd=Counter(v['Q'] for v in found.values())
print(f"\n=== 接受={acc} 不同码={len(found)}  Q 分布 = {dict(sorted(qd.items()))}", flush=True)
print(f"(A1,A2) 分布 = {dict(sorted(Counter((v['A1'],v['A2']) for v in found.values()).items()))}", flush=True)
print(("⛔ 找到 Q!=0 ⟹ **n=8 pinning 被反驳** ✗" if any(v['Q']!=0 for v in found.values()) else "全部 Q=0 ✓（证伪未成功 ⟹ pinning 在 n=8 存活 ✓，仍非穷举 ✗）"), flush=True)
