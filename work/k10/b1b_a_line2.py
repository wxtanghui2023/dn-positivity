#!/usr/bin/env python3
"""
A 线第二刀（照唐先生 15:09）：
  ① M(D) = max_{w ∉ C120} |B_1(w) ∩ U_D|，并把达到最大值的 (D,w) 按 owner-pattern 分类
  ② α₂(U_D) = U_D 中两两 Hamming 距离 ≥ 3 的最大子集（精确）
  ③ 分层 q_r(w,D) = |B(w) ∩ U_D^{(r)}|，r = |S(v)|，检查 M=5 时是否只能 q1=5 或少数固定模式
  ④ 确认 M_3 = max_{w,D} |N_D(w)| 的数值并列出全部达到者
输出 b1b_a_line2.json
"""
import itertools, json
from collections import Counter, defaultdict

WORDS = sorted(set(int(t, 2) for t in open('kamenetsky120.txt').read().split()
                   if len(t) == 10 and set(t) <= {'0', '1'}))
CODE = set(WORDS)
N = 1024
BALL = []
for w in range(N):
    m = 1 << w
    for b in range(10):
        m |= 1 << (w ^ (1 << b))
    BALL.append(m)

owners = [[] for _ in range(N)]
for i, w in enumerate(WORDS):
    owners[w].append(i)
    for b in range(10):
        owners[w ^ (1 << b)].append(i)
L1 = defaultdict(int)
for v in range(N):
    if len(owners[v]) == 1:
        L1[owners[v][0]] |= 1 << v


def pack_ge3(pts, cap):
    cnt, rem = 0, pts
    while rem and cnt <= cap:
        v = (rem & -rem).bit_length() - 1
        nxt = 0
        t = rem
        while t:
            u = (t & -t).bit_length() - 1
            t &= t - 1
            if (u ^ v).bit_count() > 2:
                nxt |= 1 << u
        rem &= nxt
        cnt += 1
    return cnt


def U_of(D):
    Ds = set(D)
    u = 0
    for v in range(N):
        S = owners[v]
        if S and set(S) <= Ds:
            u |= 1 << v
    return u


def alpha2_exact(points):
    """精确最大 packing（两两距离 >= 3）：对小规模用 B&B"""
    pts = list(points)
    n = len(pts)
    dist = [[(pts[i] ^ pts[j]).bit_count() for j in range(n)] for i in range(n)]
    best = 0

    def rec(idx, chosen):
        nonlocal best
        if len(chosen) + (n - idx) <= best:
            return
        if idx == n:
            best = max(best, len(chosen))
            return
        # include
        ok = all(dist[idx][c] >= 3 for c in chosen)
        if ok:
            rec(idx + 1, chosen + [idx])
        rec(idx + 1, chosen)
    rec(0, [])
    return best


def main():
    surv = []
    for D in itertools.combinations(range(120), 3):
        u1 = L1[D[0]] | L1[D[1]] | L1[D[2]]
        if u1.bit_count() > 22 or pack_ge3(u1, 2) > 2:
            continue
        U = U_of(D)
        if U:
            surv.append((D, U))
    print(f"幸存 D = {len(surv)}", flush=True)

    M_hist = Counter()
    alpha_hist = Counter()
    max_hits = []            # 达到全局最大值的 (D,w)
    M3 = 0
    perD = []
    for D, U in surv:
        ptsU = [v for v in range(N) if (U >> v) & 1]
        a2 = alpha2_exact(ptsU)
        alpha_hist[a2] += 1
        best, argw = 0, []
        for w in range(N):
            if w in CODE:
                continue
            ov = (BALL[w] & U).bit_count()
            if ov > best:
                best, argw = ov, [w]
            elif ov == best:
                argw.append(w)
        M_hist[best] += 1
        if best > M3:
            M3 = best
            max_hits = []
        if best == M3:
            for w in argw:
                nb = [v for v in ptsU if (BALL[w] >> v) & 1]
                layered = Counter(len(owners[v]) for v in nb)
                max_hits.append({
                    "D": list(D), "w": w, "overlap": best, "U_size": len(ptsU),
                    "layered": dict(layered),
                    "owner_sets": sorted(tuple(sorted(owners[v])) for v in nb),
                })
        perD.append({"D": list(D), "U_size": len(ptsU), "alpha2": a2, "M": best,
                     "rho_ge_alpha2": a2})
    print("M(D) 分布:", dict(sorted(M_hist.items())))
    print("α₂(U_D) 分布:", dict(sorted(alpha_hist.items())))
    print(f"\n⭐ 全局最大 M_3 = {M3}；达到的 (D,w) 对数 = {len(max_hits)}")
    pat = Counter()
    for h in max_hits:
        pat[tuple(sorted(h["layered"].items()))] += 1
    print("分层模式分布（q_r, r=1..3）:")
    for k, v in sorted(pat.items()):
        print(f"   {k}  次数={v}")
    print("\n前 5 个达到 M_3 的例子（含 owner-set 明细）:")
    for h in max_hits[:5]:
        print("   D=", h["D"], "w=", h["w"], "overlap=", h["overlap"], "layered=", h["layered"])
        print("      owner_sets=", h["owner_sets"])
    json.dump({"M_hist": {str(k): v for k, v in M_hist.items()},
               "alpha_hist": {str(k): v for k, v in alpha_hist.items()},
               "M3": M3, "max_hits": max_hits[:200], "perD": perD},
              open('b1b_a_line2.json', 'w'), indent=1)
    print("已写 b1b_a_line2.json")


if __name__ == "__main__":
    main()
