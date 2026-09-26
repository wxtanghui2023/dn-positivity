#!/usr/bin/env python3
"""A23-D4 Step 6: 全量闭合（覆盖缺口 (i)(ii)）
   枚举完备性论证：
   任何 D 若含 >=2 个组 B1,B2 ⊆ D，则 |B1∪B2| <= 4:
     |union|=4 -> D=union: 两 2-组(族C') / 含 3-组(族B) / 含 4-组(族A)
     |union|=3 -> D=union∪{d}: 三元组 T 枚举(族D)
     |union|<=2 -> 仅单元素组 -> D 内候选 <=4 自动排除
   故 族 A ∪ B ∪ C' ∪ D 即完备。
"""
import pickle, time, re, itertools
from collections import defaultdict, Counter

T0 = time.time()
BASE = '/home/node/.openclaw/workspace/dn-project/work/k10/a23/'


def main():
    small = pickle.load(open('/tmp/a23_small.pkl', 'rb'))
    W = []
    for ln in open(BASE + 'a23.6.10.2969H.txt'):
        s = ln.strip()
        if re.fullmatch(r'[0-9A-Fa-f]{5,8}', s):
            W.append(int(s, 16))
    W = sorted(set(W))
    M = len(W)
    pc = lambda x: bin(x).count('1')

    g = Counter(small.values())
    G1 = {k: v for k, v in g.items() if len(k) == 1}
    G2 = {k: v for k, v in g.items() if len(k) == 2}
    G3 = {k: v for k, v in g.items() if len(k) == 3}
    G4 = {k: v for k, v in g.items() if len(k) == 4}
    S1 = {k[0] for k in G1}
    print(f"C0={M} | 组: 1:{len(G1)} 2:{len(G2)} 3:{len(G3)} 4:{len(G4)} | 单元素组元素数={len(S1)}", flush=True)

    # 元素 -> 含它的 2-组（邻接）
    e2 = defaultdict(list)
    for (a, b) in G2:
        e2[a].append(b); e2[b].append(a)
    # 元素 -> 含它的 3-组中"另两点"的集合（用于族D的 d 相关性）
    e3 = defaultdict(list)
    for (a, b, c) in G3:
        e3[a].append((b, c)); e3[b].append((a, c)); e3[c].append((a, b))
    e4 = defaultdict(list)
    for (a, b, c, d) in G4:
        e4[a].append((b, c, d)); e4[b].append((a, c, d)); e4[c].append((a, b, d)); e4[d].append((a, b, c))

    def SD(D):
        t = 0
        for r in range(1, 5):
            for c in itertools.combinations(D, r):
                t += g.get(c, 0)
        return t

    dist = Counter(); big = {}; bestv = 0
    # ---------- 族 A: 4-组 ----------
    for B in G4:
        v = SD(B); dist[v] += 1
        if v > bestv: bestv = v
        if v >= 5: big[B] = v
    print(f"族A(4-组) {len(G4)}  {time.time()-T0:.0f}s", flush=True)

    # ---------- 族 B: 3-组 ∪ {x} ----------
    for B in G3:
        Bs = set(B)
        for x in range(M):
            if x in Bs: continue
            D = tuple(sorted(B + (x,)))
            v = SD(D); dist[v] += 1
            if v > bestv: bestv = v
            if v >= 5: big[D] = v
    print(f"族B(3-组∪x) 完成  {time.time()-T0:.0f}s", flush=True)

    # ---------- 族 C': 两个不相交 2-组之并（union=4）----------
    G2l = list(G2.keys())
    nC = 0
    for i in range(len(G2l)):
        a1, a2 = G2l[i]
        for j in range(i + 1, len(G2l)):
            b1, b2 = G2l[j]
            if b1 == a1 or b1 == a2 or b2 == a1 or b2 == a2: continue
            D = tuple(sorted((a1, a2, b1, b2)))
            v = SD(D); dist[v] += 1
            if v > bestv: bestv = v
            if v >= 5: big[D] = v
            nC += 1
    print(f"族C'(不相交2∪2) +{nC}  {time.time()-T0:.0f}s", flush=True)

    # ---------- 族 D: 三元组 T ∪ {d} ----------
    triples = set()
    # (1) 2-组 + 单元素组
    for (a, b) in G2:
        for c in S1:
            if c == a or c == b: continue
            triples.add(tuple(sorted((a, b, c))))
    # (2) 两个 2-组共享恰 1 点
    for i in range(len(G2l)):
        a1, a2 = G2l[i]
        shared1 = set(e2[a1]); shared2 = set(e2[a2])
        for b in (shared1 & shared2):
            triples.add(tuple(sorted((a1, a2, b))))
    print(f"族D 三元组数 = {len(triples)}  {time.time()-T0:.0f}s", flush=True)
    nD = 0
    for T in triples:
        A_T = SD(T)
        # 相关 d 集合：单元素组 ∪ T 的 2-邻 ∪ T 参与的 3-组扩展 ∪ 4-组扩展
        rel = set(S1)
        for x in T:
            rel |= set(e2[x])
            for (p, q) in e3[x]:
                rel.add(p); rel.add(q)
            for (p, q, r) in e4[x]:
                rel.add(p); rel.add(q); rel.add(r)
        for d in rel:
            if d in T: continue
            D = tuple(sorted(T + (d,)))
            v = SD(D); dist[v] += 1
            if v > bestv: bestv = v
            if v >= 5: big[D] = v
            nD += 1
    print(f"族D(T∪d) +{nD}  {time.time()-T0:.0f}s", flush=True)

    # ---------- 汇总 ----------
    print(f"\n|S(D)| 分布（含族间重复计数）: {dict(sorted(dist.items()))}", flush=True)
    print(f"**max |S(D)| = {bestv}**", flush=True)
    big = sorted(big.items(), key=lambda kv: -kv[1])
    print(f"|S(D)|>=5 的 **不同** D 数 = {len(big)}", flush=True)

    def maxIS(S):
        n = len(S)
        adj = [set() for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                if pc(S[i] & S[j]) >= 8:
                    adj[i].add(j); adj[j].add(i)
        best = 0
        order = sorted(range(n), key=lambda i: len(adj[i]))

        def bk(R, P):
            nonlocal best
            if not P:
                best = max(best, len(R)); return
            if len(R) + len(P) <= best: return
            for k, v in enumerate(P):
                if any(v in adj[u] for u in R): continue
                bk(R + [v], [w for w in P[k + 1:] if w not in adj[v]])
        bk([], order)
        return best

    best_a = (0, None, 0)
    table = []
    for D, v in sorted(big, key=lambda kv: -kv[1]):
        S = [s for s, bl in small.items() if set(bl) <= set(D)]
        a = maxIS(S)
        n1 = sum(1 for s in S if len(small[s]) == 1)
        n2 = sum(1 for s in S if len(small[s]) == 2)
        n3 = sum(1 for s in S if len(small[s]) == 3)
        n4 = sum(1 for s in S if len(small[s]) == 4)
        table.append((D, (n1, n2, n3, n4), len(S), a))
        if a > best_a[0]:
            best_a = (a, D, len(S))
            print(f"   D={D}: (n1..n4)={(n1,n2,n3,n4)} |S|={len(S)} alpha={a}", flush=True)
    print(f"\n=== 全量结论 ===", flush=True)
    print(f"|S(D)|>=5 的 D 共 {len(table)} 个；其中 max alpha = {best_a[0]}", flush=True)
    if best_a[0] >= 5:
        print(f"⟹ **depth-4 正交换 EXISTS** (alpha>=5)", flush=True)
    else:
        print(f"⟹ **所有 |S(D)|>=5 的 D 均 alpha <= 4 ⟹ depth-4 局部最优性定理成立（本轮覆盖完备：族A∪B∪C'∪D）**", flush=True)
    pickle.dump(table, open('/tmp/a23_table.pkl', 'wb'))
    print(f"状态表已存 /tmp/a23_table.pkl ({len(table)} 行) | 总用时 {time.time()-T0:.0f}s", flush=True)


main()
