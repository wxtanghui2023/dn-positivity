#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""「甲」第一步：三重覆盖构型账（n=10）

内容：
  ① 120-码核验（覆盖 1024/1024）
  ② 恒等式校验 Σ_x C(μ(x),3) = Σ_{三点组(两两距≤2)} |N[c1]∩N[c2]∩N[c3]|
  ③ 构型分类（平移 × 坐标置换 = Aut(Q_10) 之轨道）→ 每型之 s 与计数
纪律：纯 Python、bitmask；pyguard 受控
"""
import itertools, os, collections

N = 10
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
NM = [0] * Q
for v in range(Q):
    m = 0
    for x in NB[v]:
        m |= 1 << x
    NM[v] = m
HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "sources", "K10-1-120-cover-CERTIFICATE.txt")


def load(path):
    C = []
    for line in open(path):
        line = line.strip()
        if line.startswith("#") or not line:
            continue
        C.append(int(line, 2))
    return C


def main():
    C = load(SRC)
    cnt = [0] * Q
    for v in C:
        for x in NB[v]:
            cnt[x] += 1
    unc = sum(1 for c in cnt if c == 0)
    mu = collections.Counter(cnt)
    print(f"[①] |C|={len(C)} unique={len(set(C))} 覆盖={Q-unc}/1024 未覆盖={unc}")
    print(f"    μ 分布 = {dict(sorted(mu.items()))}")
    lhs = sum(c * (c - 1) * (c - 2) // 6 for c in cnt)
    print(f"    Σ_x C(μ,3) = {lhs}")

    # ② 三点组枚举（两两距 ≤2）
    Cset = set(C)
    adj = {c: [d for d in Cset if 0 < bin(c ^ d).count('1') <= 2] for c in C}
    adjS = {c: set(v) for c, v in adj.items()}
    def s_of(a, b, c):
        return bin(NM[a] & NM[b] & NM[c]).count("1")
    rhs = 0
    ntri = 0
    groups = collections.defaultdict(lambda: [0, set(), 0])   # key -> [count, s值集, s之和]
    for a in C:
        A1 = adj[a]
        for b in A1:
            if b <= a:
                continue
            for c in adj[a]:
                if c <= b:
                    continue
                if c not in adjS[b]:
                    continue
                ntri += 1
                s = s_of(a, b, c)
                rhs += s
                key = canon(a, b, c)
                g = groups[key]
                g[0] += 1
                g[1].add(s)
                g[2] += s
    print(f"[②] 三点组（两两距≤2）数 = {ntri}")
    print(f"    Σ_{'{'}三点组{'}'} |三球交| = {rhs}    （应与 Σ_x C(μ,3) = {lhs} 相等）")
    print(f"    恒等式{'成立 ✓✓' if rhs == lhs else '不成立 ✗✗'}")

    # ③ 构型分类
    print(f"[③] 构型轨道 = {len(groups)} 型")
    print("    type(a_b, a-b, b-a) canon          例数      s集      s和")
    for k, (num, ss, tot) in sorted(groups.items(), key=lambda kv: -kv[1][0]):
        print(f"    {str(k):<34} {num:>6} {str(sorted(ss)):>10} {tot:>7}")


def canon(a, b, c):
    """无序三点组的轨道不变量：对三个基点取最小 (|A∩B|,|A\\B|,|B\\A|)"""
    best = None
    for x, y, z in ((a, b, c), (b, a, c), (c, a, b)):
        A = x ^ y
        B = x ^ z
        t = (bin(A & B).count("1"), bin(A & ~B).count("1"), bin(B & ~A).count("1"))
        if best is None or t < best:
            best = t
    return best


if __name__ == "__main__":
    main()
