#!/usr/bin/env python3
# ip5_dminus3_search.py —— RUN（预注册）：D(-3)-quadruple 有界精确搜索，域 d <= 200
# 预注册语义：命中 ⟹ EXIT-POSITIVE（证书）；域内穷尽无 ⟹ EXIT-NEGATIVE-FINITE（NOT FOUND for d<=200；不升级、不扩域）
from math import isqrt
N = 200
def sq(x):
    if x < 0: return False
    r = isqrt(x); return r*r == x
print("=== RUN: D(-3)-quadruple 有界精确搜索 (1 <= a < b < c < d <= %d) ===" % N)
edges = []
adj = {a: set() for a in range(1, N+1)}
for a in range(1, N+1):
    for b in range(a+1, N+1):
        if sq(a*b - 3):
            adj[a].add(b); adj[b].add(a); edges.append((a,b))
print("[1] D(-3)-pairs (edges) within domain:", len(edges))
triples = []
for a in range(1, N+1):
    for b in sorted(x for x in adj[a] if x > a):
        for c in sorted(x for x in (adj[a] & adj[b]) if x > b):
            triples.append((a,b,c))
print("[2] D(-3)-triples within domain:", len(triples))
if triples:
    print("    first triples:", triples[:12])
quads = []
for (a,b,c) in triples:
    for d in sorted(x for x in (adj[a] & adj[b] & adj[c]) if x > c):
        quads.append((a,b,c,d))
print("[3] D(-3)-quadruples within domain:", len(quads))
ok = 0
for (a,b,c,d) in quads:
    xs = []
    for (i,j) in ((0,1),(0,2),(0,3),(1,2),(1,3),(2,3)):
        v = (a,b,c,d)[i]*(a,b,c,d)[j] - 3
        r = isqrt(v); xs.append((v, r, r*r == v))
    allsq = all(t[2] for t in xs)
    ok += allsq
    print("QUAD", (a,b,c,d), "six squares:", [(t[0], t[1]) for t in xs], "ALL-INTEGER-SQUARE:", allsq)
print("[4] verified quadruples (all six squares exact):", ok)
print("RESULT:", "EXIT-POSITIVE" if quads else "EXIT-NEGATIVE-FINITE")
