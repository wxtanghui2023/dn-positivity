#!/usr/bin/env python3
"""独立核验：[20,9] 二元线性码覆盖半径 4 的构造证书。
方法 A：组合枚举（itertools）——所有 <=4 列子集 XOR。
方法 B：按重量 BFS（多源分层）——独立算法。
另做：GF(2) 秩；<=3 层计数；重量分布对比。
输入：20 列（整数 0..2047，11-bit）。
"""
from itertools import combinations
from collections import defaultdict

COLS = [484,1200,1437,325,491,1137,1,1124,1017,348,
        693,72,1433,1318,1591,1491,1301,44,1981,208]

def rank_gf2(vals, dim=11):
    basis = []
    for v in vals:
        x = v
        for b in basis:
            x = min(x, x ^ b)
        if x:
            basis.append(x); basis.sort(reverse=True)
    return len(basis)

def method_A(cols):
    dist = {}
    for k in range(0,5):
        for I in combinations(range(len(cols)), k):
            s = 0
            for i in I: s ^= cols[i]
            if s not in dist: dist[s] = k
    return dist

def method_B(cols):
    dist = {0:0}
    frontier = {0}
    for k in range(1,5):
        nxt = set()
        for v in frontier:
            for c in cols:
                w = v ^ c
                if w not in dist:
                    dist[w] = k; nxt.add(w)
        frontier = nxt
    return dist

print("=== 0. 输入检查 ===")
print("列数:", len(COLS), "| 全部非零:", all(0 < c < 2048 for c in COLS),
      "| 全在 11-bit 内:", all(c < 2048 for c in COLS))
print("重复列数:", len(COLS) - len(set(COLS)))

print("\n=== 1. GF(2) 秩 ===")
r = rank_gf2(COLS)
print("rank_F2(H) =", r, "=> 码参数 [20,", 20-r, "]", "| PASS" if r == 11 else "| FAIL")

print("\n=== 2. 方法 A（组合枚举）===")
dA = method_A(COLS)
print("可达 syndrome 数:", len(dA), "| 期望 2048 |", "PASS" if len(dA)==2048 else "FAIL")
histA = defaultdict(int)
for v in dA.values(): histA[v]+=1
print("最小重量分布 A:", dict(sorted(histA.items())))

print("\n=== 3. 方法 B（重量 BFS，独立算法）===")
dB = method_B(COLS)
print("可达 syndrome 数:", len(dB), "|", "PASS" if len(dB)==2048 else "FAIL")
histB = defaultdict(int)
for v in dB.values(): histB[v]+=1
print("最小重量分布 B:", dict(sorted(histB.items())))

print("\n=== 4. 双法一致性 ===")
same = (dA == dB)
print("分布完全一致:", same)
if not same:
    diff = {k:(dA.get(k),dB.get(k)) for k in set(dA)|set(dB) if dA.get(k)!=dB.get(k)}
    print("差异条数:", len(diff), "示例:", list(diff.items())[:5])

print("\n=== 5. 球覆盖下界（<=3 不可能）===")
import math
cnt3 = sum(math.comb(20,i) for i in range(0,4))
cnt4 = sum(math.comb(20,i) for i in range(0,5))
print("<=3 子集数:", cnt3, "< 2048 ?", cnt3 < 2048, "| <=4 子集数:", cnt4)
d3 = {s for s,k in dA.items() if k<=3}
print("实际可达的 <=3-sums 数:", len(d3), "(上界", cnt3, ")")

print("\n=== 6. 结论 ===")
ok = (r==11) and (len(dA)==2048) and same and max(dA.values())==4
print("R(C)=4 且 [20,9]:", "PASS" if ok else "FAIL",
      "| 最大最小重量:", max(dA.values()))
