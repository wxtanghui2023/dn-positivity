#!/usr/bin/env python3
"""完备性补丁: 对每个三元组 T 检查 SD(T)>=5 的情形（非贡献 d 的 D 与 T 同候选集）"""
import pickle, re, itertools, time
from collections import Counter, defaultdict
T0=time.time()
small=pickle.load(open('/tmp/a23_small.pkl','rb'))
W=[]
for ln in open('a23.6.10.2969H.txt'):
    s=ln.strip()
    if re.fullmatch(r'[0-9A-Fa-f]{5,8}',s): W.append(int(s,16))
W=sorted(set(W)); M=len(W)
pc=lambda x: bin(x).count('1')
g=Counter(small.values())
G1={k:v for k,v in g.items() if len(k)==1}; G2={k:v for k,v in g.items() if len(k)==2}
G3={k:v for k,v in g.items() if len(k)==3}; G4={k:v for k,v in g.items() if len(k)==4}
S1={k[0] for k in G1}
e2=defaultdict(list)
for (a,b) in G2: e2[a].append(b); e2[b].append(a)
G2l=list(G2.keys())
def SD(D):
    t=0
    for r in range(1,5):
        for c in itertools.combinations(D,r): t+=g.get(c,0)
    return t
# 三元组集（与 step6 相同）
triples=set()
for (a,b) in G2:
    for c in S1:
        if c!=a and c!=b: triples.add(tuple(sorted((a,b,c))))
for i in range(len(G2l)):
    a1,a2=G2l[i]
    s1=set(e2[a1]); s2=set(e2[a2])
    for b in (s1 & s2): triples.add(tuple(sorted((a1,a2,b))))
print(f"三元组数={len(triples)}",flush=True)
def maxIS(S):
    n=len(S); adj=[set() for _ in range(n)]
    for i in range(n):
        for j in range(i+1,n):
            if pc(S[i]&S[j])>=8: adj[i].add(j); adj[j].add(i)
    best=0; order=sorted(range(n),key=lambda i:len(adj[i]))
    def bk(R,P):
        nonlocal best
        if not P: best=max(best,len(R)); return
        if len(R)+len(P)<=best: return
        for k,v in enumerate(P):
            if any(v in adj[u] for u in R): continue
            bk(R+[v],[w for w in P[k+1:] if w not in adj[v]])
    bk([],order); return best
bad=[]; n5=0
for T in triples:
    v=SD(T)
    if v>=5:
        n5+=1
        S=[s for s,bl in small.items() if set(bl)<=set(T)]
        a=maxIS(S)
        if a>=5: bad.append((T,len(S),a))
print(f"SD(T)>=5 的三元组数 = {n5}  用时 {time.time()-T0:.0f}s",flush=True)
if bad: print("✗✗ 发现 alpha>=5:",bad[:5],flush=True)
else: print(f"✓✓ 全部 SD(T)>=5 的三元组上 alpha<=4 ⟹ 完备性补丁通过 ✓",flush=True)
# 另外：单组情形（|S(D)|>=5 但 D 只含 1 组）—— 检查是否有 2-组 D 使 |S(D)|>=5
g2big=[]
for P in G2:
    # D ⊇ P，仅 1 个组时 |S(D)|=g(P)+singletons(D) <= 3+4 = 7 —— 需枚举 D=P∪{x,y}
    pass
print(f"总用时 {time.time()-T0:.0f}s",flush=True)
