#!/usr/bin/env python3
"""A23-D4 Step 5: 收集 |S(D)|>=5 的 D（可行族：4-组 / 3-组∪{x} / 两个2-组之并）
   对每个这样的 D 建冲突图并判 alpha >= 5"""
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
    print(f"C0={M} | 小-blocker 候选={len(small)}", flush=True)

    g = Counter(small.values())          # 精确组 -> 计数
    G1 = {k: v for k, v in g.items() if len(k) == 1}
    G2 = {k: v for k, v in g.items() if len(k) == 2}
    G3 = [k for k in g if len(k) == 3]
    G4 = {k: v for k, v in g.items() if len(k) == 4}
    print(f"组: |B|=1:{len(G1)} |B|=2:{len(G2)} |B|=3:{len(G3)} |B|=4:{len(G4)}", flush=True)

    def SD(D):
        """|S(D)| = sum_{nonempty B subseteq D} g(B)"""
        t = 0
        for r in range(1, 5):
            for c in itertools.combinations(D, r):
                t += g.get(c, 0)
        return t

    cand = {}   # D -> |S(D)|
    # 族 A: 精确 4-组
    for B in G4:
        cand[B] = SD(B)
    print(f"族A(4-组) 完成 {len(cand)} 用时 {time.time()-T0:.0f}s", flush=True)
    # 族 B: 3-组 ∪ {x}
    for B in G3:
        Bs = set(B)
        for x in range(M):
            if x in Bs:
                continue
            D = tuple(sorted(B + (x,)))
            if D not in cand:
                cand[D] = SD(D)
    print(f"族B(3-组∪x) 完成 {len(cand)} 用时 {time.time()-T0:.0f}s", flush=True)
    # 族 C: 两个 2-组之并 (|union|=4)
    G2l = list(G2.keys())
    for i in range(len(G2l)):
        A = G2l[i]
        for j in range(i + 1, len(G2l)):
            B = G2l[j]
            if A[0] in B or A[1] in B:
                U = tuple(sorted(set(A) | set(B)))
                if len(U) == 4 and U not in cand:
                    cand[U] = SD(U)
    print(f"族C(2∪2) 完成 {len(cand)} 用时 {time.time()-T0:.0f}s", flush=True)

    dist = Counter(cand.values())
    print(f"\n|S(D)| 分布（可行族）: {dict(sorted(dist.items()))}", flush=True)
    mx = max(cand.values())
    print(f"**max |S(D)| = {mx}**", flush=True)
    big = [(D, v) for D, v in cand.items() if v >= 5]
    print(f"|S(D)| >= 5 的 D 数 = {len(big)}", flush=True)

    def maxIS(nodes, bad):
        """nodes: ids; bad(i,j): conflict. 返回最大兼容族大小"""
        n = len(nodes)
        order = sorted(range(n), key=lambda i: -sum(1 for j in range(n) if j != i and not bad(i, j)))
        best = 0

        def bk(R, P, pos):
            nonlocal best
            if not P:
                best = max(best, len(R))
                return
            if len(R) + len(P) <= best:
                return
            for k in range(len(P)):
                v = P[k]
                if any(bad(v, u) for u in R):
                    continue
                bk(R + [v], [w for w in P[k + 1:] if not bad(v, w)], 0)
        bk([], order, 0)
        return best

    best_a = (0, None)
    for D, v in sorted(big, key=lambda kv: -kv[1]):
        S = [s for s, bl in small.items() if set(bl) <= set(D)]
        assert len(S) == v, (len(S), v)
        bad = lambda i, j: pc(S[i] & S[j]) >= 8
        a = maxIS(list(range(len(S))), bad)
        if a > best_a[0]:
            best_a = (a, D, len(S))
            print(f"   D={D}: |S|={len(S)} alpha={a}", flush=True)
    print(f"\n=== 结论 ===", flush=True)
    print(f"可行族中 max alpha = {best_a[0]}  (在 |S(D)|={best_a[2]} 的 D 上)", flush=True)
    if best_a[0] >= 5:
        print(f"⟹ **depth-4 正交换 EXISTS** (alpha>=5): 2969 -> >=2970 witness ✓", flush=True)
    else:
        print(f"⟹ 可行族中所有 D 的 alpha < 5 ⟹ (需补完全部 D 才能定论)", flush=True)
    print(f"总用时 {time.time()-T0:.0f}s", flush=True)


main()
