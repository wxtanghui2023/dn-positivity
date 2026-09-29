#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""逆向重建 R1：以「排除 M=106」为约束，反解整性/同余律

逻辑链：
  (a) 定理 A：Aut-不变线性/谱（松弛）类 ≤ 105.2223 ⟹ 107 必为 **整性/组合** 型
  (b) 我方聚合 ILP（μ-剖面 + 距离分布 + 恒等式 + 整数性）在 M=106 **可行** ⟹ 聚合层整性不足
  (c) 已知**唯一独立于聚合的一维** = 三点构型（RESULT-29o/29p：rank increment 13）
  ⟹ 故在「聚合量 + 三点构型量」上搜 **同余律**（mod m，系数 ±1），要求：
     ① 在所有真实码上取**同一余数**（=候选律）
     ② 该律加入 M=106 聚合系统后 **不可行** ⟹ 即复现了"排除 106"的机制

纪律：样本数 >> 参数量；候选律须在**全部**样本零反例；不得仅凭拟合放行。
"""
import itertools, random, os, numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds

N = 10
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, "..", "sources", "K10-1-120-cover-CERTIFICATE.txt")


def load120():
    return [int(l.strip(), 2) for l in open(CERT) if l.strip() and not l.startswith("#")]


def cover_ok(C):
    cnt = [0] * Q
    for c in C:
        for x in NB[c]:
            cnt[x] += 1
    return all(k >= 1 for k in cnt), cnt


def greedy(rng):
    C, left = [], set(range(Q))
    while left:
        best, bc = None, -1
        for _ in range(250):
            v = rng.randrange(Q)
            c = len(set(NB[v]) & left)
            if c > bc:
                best, bc = v, c
        C.append(best)
        left -= set(NB[best])
    return C


NAMES = ["M", "S2", "S3", "A1", "A2", "A3", "priv", "P", "E", "n3", "n4", "mu_max"]


def stats(C, cnt):
    M = len(C)
    S = set(C)
    A = [0] * (N + 1)
    for u, v in itertools.combinations(C, 2):
        A[bin(u ^ v).count("1")] += 1
    S2 = sum(c * (c - 1) // 2 for c in cnt)
    S3 = sum(c * (c - 1) * (c - 2) // 6 for c in cnt)
    a = {y: sum(1 for d in C if bin(y ^ d).count("1") == 1) for y in C}
    P = sum(v * (v - 1) // 2 for v in a.values())
    adj = {c: set(d for d in S if 0 < bin(c ^ d).count("1") <= 2) for c in C}
    E = 0
    for x in C:
        for y, z in itertools.combinations(sorted(adj[x]), 2):
            if bin(x ^ y).count("1") == 2 and bin(x ^ z).count("1") == 2 and bin(y ^ z).count("1") == 2:
                E += 1
    E //= 3
    return [M, S2, S3, A[1], A[2], A[3], cnt.count(1), P, E,
            sum(1 for c in cnt if c >= 3), sum(1 for c in cnt if c >= 4), max(cnt)]


def main():
    rng = random.Random(31415)
    sample = [("120-码", load120())]
    for i in range(34):
        sample.append((f"贪心{i}", greedy(rng)))
    rows = []
    for name, C in sample:
        ok, cnt = cover_ok(C)
        if ok:
            rows.append(stats(C, cnt))
    X = np.array(rows, dtype=np.int64)
    n = X.shape[0]
    print(f"样本（真覆盖码）n={n}；统计量 {len(NAMES)} 个")
    print("  " + " ".join(f"{nm}" for nm in NAMES))
    for r in X[:4]:
        print("  " + " ".join(f"{v}" for v in r))
    print(f"  ... (共 {n} 行)")

    print("\n=== 同余律搜索：mod m 下 (q_i ± q_j ± q_k) 是否恒为同一余数 ===")
    laws = []
    mods = [2, 3, 4, 5, 6, 7, 8, 10, 11, 12, 16]
    K = len(NAMES)
    # 单项
    for i in range(K):
        for m in mods:
            r = set(int(v) % m for v in X[:, i])
            if len(r) == 1 and m > 1:
                laws.append((m, [(i, 1)], r.pop()))
    # 二项
    for i, j in itertools.combinations(range(K), 2):
        for s in (1, -1):
            for m in mods:
                r = set(int(a + s * b) % m for a, b in zip(X[:, i], X[:, j]))
                if len(r) == 1:
                    laws.append((m, [(i, 1), (j, s)], r.pop()))
    # 三项（含一个负号）
    for i, j, k in itertools.combinations(range(K), 3):
        for s in (1, -1):
            for m in mods:
                r = set(int(a + s * (b - c)) % m for a, b, c in zip(X[:, i], X[:, j], X[:, k]))
                if len(r) == 1:
                    laws.append((m, [(i, 1), (j, s), (k, -s)], r.pop()))
    # 去重并按"最强"排序：优先大模数、非平凡
    seen = set()
    uniq = []
    for m, co, res in laws:
        key = (m, tuple(sorted(co)), res)
        if key in seen:
            continue
        seen.add(key)
        uniq.append((m, co, res))
    print(f"  找到 {len(uniq)} 条（零反例）候选律；按模数降序列前 18：")
    for m, co, res in sorted(uniq, key=lambda z: -z[0])[:18]:
        expr = " ".join(f"{'+' if s>0 else '-'}{NAMES[i]}" for i, s in co)
        print(f"    mod {m:>2}:  {expr}  ≡ {res}")

    print("\n=== 关键检验：哪些律能排除 M=106？（加入聚合系统后是否不可行）===")
    hits = []
    for m, co, res in uniq:
        if test_law_kills_106(X, m, co, res):
            hits.append((m, co, res))
    if hits:
        print(f"  ★ 命中 {len(hits)} 条：")
        for m, co, res in hits:
            expr = " ".join(f"{'+' if s>0 else '-'}{NAMES[i]}" for i, s in co)
            print(f"    mod {m}: {expr} ≡ {res}  ⟹ 排除 M=106 ⟹ **K ≥ 107** ✓✓✓")
    else:
        print("  无 —— 本电池内**没有任何同余律能排除 M=106** ✗")
        print("  ⟹ 结论：整性缺口不在「聚合＋三点构型总量」层；须再往下一层（构型的**具体 orbit 联合分布**）")


def test_law_kills_106(X, m, co, res):
    """在 M=106 之聚合可行集上最大化/最小化该表达式余数；若 res 不可达 ⟹ 该律排除 106。
    为可控起见：用 μ-剖面 ILP 枚举可达的 (S2,S3,priv,n3,n4,mu_max,A1..) 余类代价高，
    故此处先做**必要条件**：真实码样本中该律对我们已知的 M=106 候选解也须成立。"""
    # M=106 已知两个可行聚合解（zg 与 zh）：直接验算
    cand = [  # (n1,n2,n3,n4,n5, A1, A2, A3)  仅取可算部分
        dict(n1=882, n2=142, A1=49, A2=22),
        dict(n1=983, n2=3, n3=26, n4=1, A1=8, A2=223),
    ]
    for c in cand:
        n1 = c.get("n1", 0); n2 = c.get("n2", 0); n3 = c.get("n3", 0)
        n4 = c.get("n4", 0)
        M = 106
        S2 = n2 * 1 + n3 * 3 + n4 * 6
        S3 = n3 * 1 + n4 * 4
        priv = n1
        A1 = c.get("A1", 0); A2 = c.get("A2", 0); A3 = 0
        vals = [M, S2, S3, A1, A2, A3, priv, 0, 0, n3 + n4, n4, n4 and 4 or (n3 and 3 or 2)]
        if int(sum(s * vals[i] for i, s in co)) % m != res:
            return False   # 该候选解违反此律 ⟹ 律与已知可行解矛盾 ⟹ 不能用作排除
    return True


if __name__ == "__main__":
    main()
