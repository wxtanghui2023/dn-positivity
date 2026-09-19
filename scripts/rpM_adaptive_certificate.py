#!/usr/bin/env python3
"""
rpM_adaptive_certificate.py
===========================
目标 (RP_M):  对所有 phi in [0,pi]^M,  max_{1<=k<=5M} sum_j cos(k phi_j)  >=  1/2

方法: 自适应分支定界 + 每箱【精确】下界
    LB(B) = max_{1<=k<=5M} sum_{j=1..M} min_{phi_j in [a_j,b_j]} cos(k phi_j)

严格性: 对箱内任意 phi 与任意 k,
        sum_j cos(k phi_j) >= sum_j min_{[a_j,b_j]} cos(k phi_j) =: L_k
        => max_k S_k(phi) >= max_k L_k = LB(B)
   (逐坐标取最小 + 弱对偶; 无 Lipschitz 松量)

保守化 (为抵消浮点):
   * 每项减去 SLACK
   * pi-判定按保守方向扩展 (宁可判为"含 pi" => min = -1 => 界更弱 => 安全)

输出: 认证箱数 / 未决箱数 / 已认证箱的最小余量 / 最大深度
"""
import numpy as np, sys, time, hashlib, json, os
from itertools import product

SLACK = 1e-12          # 每项安全余量 (远大于 double 的 cos 误差 ~1e-16)
TEST_EPS = 1e-9        # pi-判定的保守扩展 (弧度尺度)

def lb_box(M, lo, hi, K):
    """保守版每箱下界 (numpy 向量化 over k)"""
    k = np.arange(1, K+1, dtype=float)                     # (K,)
    a = k[:, None] * lo[None, :]                           # (K,M)
    b = k[:, None] * hi[None, :]
    mn = np.minimum(np.cos(a), np.cos(b))
    # 保守 pi-判定: 区间 [a,b] 是否(近似)含有 k*phi ≡ pi mod 2pi
    # 存在整数 m: m + 1/2 in [a/2pi, b/2pi]
    u1 = a/(2*np.pi) - TEST_EPS
    u2 = b/(2*np.pi) + TEST_EPS
    hit = np.ceil(u1 - 0.5) <= np.floor(u2 - 0.5)
    mn = np.where(hit, -1.0, mn)
    per_k = mn.sum(axis=1) - M*SLACK                       # (K,)
    return float(per_k.max())

def certify(M, N0=10, maxdepth=24, budget=400000, verbose=True):
    K = 5*M
    edges = np.linspace(0.0, np.pi, N0+1)
    idx = np.array(list(product(range(N0), repeat=M)))
    stack = list(zip(edges[idx], edges[idx+1]))
    nel = 0; unresolved = 0; depth_hist = {}
    min_margin = np.inf; maxdepth_seen = 0
    while stack:
        lo, hi = stack.pop(); nel += 1
        if nel > budget:
            return dict(M=M, ok=False, reason="budget exceeded", neval=nel,
                        unresolved=len(stack)+unresolved, min_margin=min_margin)
        lb = lb_box(M, lo, hi, K)
        if lb >= 0.5:
            min_margin = min(min_margin, lb-0.5)
            continue
        width = float((hi-lo).max())
        depth = int(np.ceil(np.log2(np.pi/max(width, 1e-300))))
        maxdepth_seen = max(maxdepth_seen, depth)
        if depth >= maxdepth:
            unresolved += 1; depth_hist[depth] = depth_hist.get(depth,0)+1
            continue
        mid = (lo+hi)/2.0
        for bits in product([0,1], repeat=M):
            bits = np.array(bits)
            stack.append((np.where(bits==0, lo, mid), np.where(bits==0, mid, hi)))
    return dict(M=M, ok=(unresolved==0), neval=nel, unresolved=unresolved,
                min_margin=float(min_margin), max_depth=maxdepth_seen,
                depth_hist=depth_hist, N0=N0, slack=SLACK, test_eps=TEST_EPS)

if __name__ == "__main__":
    Ms = [int(x) for x in (sys.argv[1:] or ["3","4"])]
    res_all = []
    for M in Ms:
        t = time.time()
        N0 = int(os.environ.get("N0", 10 if M <= 4 else 8))
        BUD = int(os.environ.get("BUDGET", 400000))
        r = certify(M, N0=N0, maxdepth=24, budget=BUD)
        r["seconds"] = round(time.time()-t, 2)
        print(json.dumps({k:v for k,v in r.items() if k!="depth_hist"}, ensure_ascii=False,
                         default=str), flush=True)
        if r.get("depth_hist"): print("   depth_hist:", r["depth_hist"], flush=True)
        res_all.append(r)
    sig = hashlib.sha256(json.dumps([{k:v for k,v in r.items() if k!='depth_hist'} for r in res_all],
                                     sort_keys=True, default=str).encode()).hexdigest()[:16]
    print("params SLACK=%g TEST_EPS=%g  result_sha256[:16]=%s" % (SLACK, TEST_EPS, sig))
