#!/usr/bin/env python3
# n=30 的 refinement 系统: 找最小非平凡环, 测可填平性
# 节点 = 30 的部分分解 (multiset, 无序); 边 = 一步拆分(合数->两因子) 或 合并(两因子->积)
from collections import defaultdict
from itertools import combinations

N = 30

def prime_factors(n):
    fs = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d)
            n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs

def is_prime(n):
    return len(prime_factors(n)) == 1

# 生成所有部分分解 (multiset) 的节点
def all_partial_factors(n):
    """返回 n 的所有因子分解 (multiset, 递归拆分到因子>=2)"""
    results = set()
    def rec(parts):
        results.add(tuple(sorted(parts)))
        for i, x in enumerate(parts):
            if not is_prime(x):
                # 拆分 x = a*b (a<=b, a>=2)
                for a in range(2, int(x**0.5) + 1):
                    if x % a == 0:
                        b = x // a
                        new = list(parts)
                        new[i] = a
                        new.append(b)
                        rec(new)
    rec([n])
    return results

nodes = all_partial_factors(30)
print(f"节点数 (部分分解 multiset): {len(nodes)}")
for nd in sorted(nodes, key=lambda x: (len(x), x)):
    print("  ", nd)

# 边: 一步拆分或合并
def neighbors(nd):
    res = set()
    parts = list(nd)
    # 拆分一个合数
    for i, x in enumerate(parts):
        if not is_prime(x):
            for a in range(2, int(x**0.5) + 1):
                if x % a == 0:
                    b = x // a
                    new = parts[:i] + parts[i+1:] + [a, b]
                    res.add(tuple(sorted(new)))
    # 合并两个因子
    for i, j in combinations(range(len(parts)), 2):
        prod = parts[i] * parts[j]
        if prod <= 30:
            new = [parts[k] for k in range(len(parts)) if k != i and k != j] + [prod]
            res.add(tuple(sorted(new)))
    return res

# 图
from collections import deque
def bfs_shortest_cycle(node_set, start, maxlen=10):
    """BFS 找经过 start 的最短环"""
    # 找两个邻居间的最短路径 (不含 start)
    nbrs = {nd: neighbors(nd) for nd in node_set}
    best = None
    for n1 in nbrs[start]:
        # BFS from n1 to n2 (avoid start), 对所有 n2 in nbrs[start], n2 != n1
        dist = {n1: (0, [n1])}
        q = deque([n1])
        while q:
            u = q.popleft()
            d, path = dist[u]
            if d >= maxlen:
                continue
            for v in nbrs[u]:
                if v == start or v == n1:
                    continue
                if v not in dist:
                    dist[v] = (d + 1, path + [v])
                    q.append(v)
        # 检查所有其他邻居 n2
        for n2 in nbrs[start]:
            if n2 == n1 or n2 not in dist:
                continue
            d2, path2 = dist[n2]
            cycle = [start] + path2 + [start]
            if best is None or len(cycle) < len(best):
                best = cycle
    return best

# 找最小环
nbrs = {nd: neighbors(nd) for nd in nodes}
print(f"\n每个节点的邻居数: {[(nd, len(nbrs[nd])) for nd in sorted(nodes, key=lambda x:(len(x),x))]}")
print(f"\n总边数: {sum(len(nbrs[nd]) for nd in nodes)//2}")

# 最小环 (全局)
all_cycles = []
for nd in nodes:
    c = bfs_shortest_cycle(nodes, nd, maxlen=8)
    if c:
        all_cycles.append(c)
minlen = min(len(c) for c in all_cycles)
print(f"\n最短环长度: {minlen}")
for c in all_cycles:
    if len(c) == minlen:
        print("  环:", " -> ".join(str(x) for x in c))
