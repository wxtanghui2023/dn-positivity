#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
E169：有限群 Z_{p^2}-SF 阶段一
(A) X+Y = G\{0};  (B) |X|+|Y| <= p^2-1;  (C) |X||Y| >= p^2-1
不碰 RH；纯有限组合。
"""
from itertools import combinations
import collections

def odds(p2):
    return [r for r in range(p2) if r % 2 == 1]

def sumset(X, Y, G):
    return {(x + y) % G for x in X for y in Y}

print("=== 显式构造：X={0,1}, Y=奇剩余 ===")
for p in (3, 5, 7, 11, 13):
    G = p * p
    X = [0, 1]
    Y = odds(G)
    S = sumset(X, Y, G)
    print("  p=%2d G=%3d |X|=%d |Y|=%3d |X|+|Y|=%3d<=%4d? %-5s |X||Y|=%4d>=%4d? %-5s  A? %s"
          % (p, G, len(X), len(Y), len(X)+len(Y), G-1, len(X)+len(Y) <= G-1,
             len(X)*len(Y), G-1, len(X)*len(Y) >= G-1, S == set(range(1, G))))

print()
print("=== p=3 (G=9) 穷举 (A)(B)(C) ===")
G = 9
allsets = [frozenset(s) for r in range(1, G+1) for s in combinations(range(G), r)]
print("  非空子集数 =", len(allsets))
found = []
for X in allsets:
    lx = len(X)
    for Y in allsets:
        ly = len(Y)
        if lx + ly > G - 1:
            continue
        if lx * ly < G - 1:
            continue
        if sumset(X, Y, G) != set(range(1, G)):
            continue
        found.append((lx, ly, sorted(X), sorted(Y)))
print("  解数 =", len(found))
c = collections.Counter((a, b) for a, b, _, _ in found)
print("  (|X|,|Y|) 分布 =", dict(sorted(c.items())))
for a, b, X, Y in found[:5]:
    print("    |X|=%d |Y|=%d X=%s Y=%s" % (a, b, X, Y))
print("  min(|X|,|Y|) 最小值 =", min(min(a, b) for a, b, _, _ in found) if found else None)
print("  是否存在 |X|,|Y| >= 3 且 |X|+|Y| <= 8 的 '均衡' 解 =",
      sum(1 for a,b,_,_ in found if a>=3 and b>=3))
