#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""机制 C-1：3-for-2 穷举（120-码 → ≤119）

找 T ⊆ C (|T|=3) 与 W ⊆ Q_10 (|W|=2)，使 (C\\T) ∪ W 覆盖 ⟺ U(T) ⊆ ∪_{w∈W} N[w]
高效：对每个 pair W 算 M，取 Good={c: priv(c)⊆M}（T⊆Good 为必要条件），仅 |Good|≥3 时枚举 T。
附验证：2-for-1（档案已记 0/7140）。
"""
import itertools, time, os

N = 10
Q = 1 << N
MASK = [1 << i for i in range(N)]
NB = [[v] + [v ^ m for m in MASK] for v in range(Q)]
FULL = (1 << Q) - 1
NM = [0] * Q
for v in range(Q):
    m = 0
    for x in NB[v]:
        m |= 1 << x
    NM[v] = m
HERE = os.path.dirname(os.path.abspath(__file__))
CERT = os.path.join(HERE, "..", "sources", "K10-1-120-cover-CERTIFICATE.txt")


def load():
    return [int(l.strip(), 2) for l in open(CERT) if l.strip() and not l.startswith("#")]


def main():
    C = load()
    M = len(C)
    idx = {c: i for i, c in enumerate(C)}
    own = [[] for _ in range(Q)]
    for x in range(Q):
        for c in C:
            if bin(c ^ x).count("1") <= 1:
                own[x].append(idx[c])
    priv = [0] * M
    pairmask, triplemask = {}, {}
    for x in range(Q):
        o = own[x]
        if len(o) == 1:
            priv[o[0]] |= 1 << x
        elif len(o) == 2:
            k = (min(o), max(o))
            pairmask[k] = pairmask.get(k, 0) | (1 << x)
        elif len(o) == 3:
            k = tuple(sorted(o))
            triplemask[k] = triplemask.get(k, 0) | (1 << x)
    mu = [len(o) for o in own]
    print(f"[seed] |C|={M}  μ分布={ {k: mu.count(k) for k in sorted(set(mu))} }")
    print(f"      Σpriv={sum(bin(p).count('1') for p in priv)}  #μ=2点={len(pairmask)}  #μ=3点={len(triplemask)}")

    def Umask(T):
        u = 0
        for c in T:
            u |= priv[c]
        for a, b in itertools.combinations(T, 2):
            u |= pairmask.get((min(a, b), max(a, b)), 0)
        u |= triplemask.get(tuple(sorted(T)), 0)
        return u

    # ── 验证 2-for-1 ──
    t0 = time.time(); hit21 = 0; best21 = None
    for a, b in itertools.combinations(range(M), 2):
        U = Umask((a, b))
        if U == 0:
            hit21 += 1; continue
        for v in range(Q):
            if U & ~NM[v] == 0:
                hit21 += 1; best21 = (a, b, v); break
    print(f"[验证] 2-for-1 命中={hit21}（档案 0/7140）  {time.time()-t0:.1f}s")
    if best21:
        print("       示例:", best21)

    # ── 主搜索 3-for-2 ──
    t0 = time.time(); budget = 900.0
    scanned = 0; found = None; good_hits = 0
    for v in range(Q):
        for w in range(v + 1, Q):
            scanned += 1
            if scanned % 50000 == 0:
                print(f"       ... 已扫 {scanned} 对，Good≥3 者 {good_hits}，"
                      f"{time.time()-t0:.0f}s", flush=True)
                if time.time() - t0 > budget:
                    print("       [预算用尽，部分扫描]")
                    break
            M_ = NM[v] | NM[w]
            notM = FULL & ~M_
            Good = [c for c in range(M) if priv[c] & notM == 0]
            if len(Good) < 3:
                continue
            good_hits += 1
            for T in itertools.combinations(Good, 3):
                U = Umask(T)
                if U & notM == 0:
                    found = (T, (v, w), U); break
            if found:
                break
        if found or time.time() - t0 > budget:
            break
    print(f"[主搜索] 3-for-2：扫描 {scanned} 对（Good≥3: {good_hits}）  用时 {time.time()-t0:.1f}s")
    if found:
        T, (v, w), U = found
        newC = sorted(set([C[i] for i in range(M) if i not in T] + [v, w]))
        cnt = [0] * Q
        for c in newC:
            for x in NB[c]:
                cnt[x] += 1
        unc = sum(1 for k in cnt if k == 0)
        print(f"★★★ 命中！T={[C[i] for i in T]}  W=({v},{w})  |U|={bin(U).count('1')}")
        print(f"    新码 |C'|={len(newC)}  覆盖={Q-unc}/1024  未覆盖={unc}")
        p = os.path.join(HERE, "..", "out", "n10_leq119_certificate.txt")
        with open(p, "w") as f:
            f.write(f"# 3-for-2 命中 |C'|={len(newC)} coverage={Q-unc}/1024\n")
            for c in newC:
                f.write(format(c, "010b") + "\n")
        print(f"    证书：{os.path.relpath(p)}")
    else:
        print("    未命中 ⟹ **3-for-2 于该 120-码上闭合**（负结果，升级档案 '未做候选 ①'）")


if __name__ == "__main__":
    main()
