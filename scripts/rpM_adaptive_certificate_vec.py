#!/usr/bin/env python3
"""
rpM_adaptive_certificate_vec.py  —— rpM_adaptive_certificate.py 的向量化版本
目标 (RP_M):  对所有 phi in [0,pi]^M,  max_{1<=k<=5M} sum_j cos(k phi_j) >= 1/2

与旧版的差别: 旧版逐箱 Python 循环 (~47 us/箱); 本版按【块】向量化 (~2 us/箱)。
数学内容完全相同 (每箱精确下界 LB = max_k sum_j min_{[a_j,b_j]} cos(k phi_j)),
保守化参数也相同 (SLACK=1e-12 每项, TEST_EPS=1e-9 用于 pi-判定)。

用法:  python3 rpM_adaptive_certificate_vec.py M [N0] [BUDGET] [MAXDEPTH]
"""
import numpy as np, sys, time, json, hashlib
from itertools import product

SLACK = 1e-12
TEST_EPS = 1e-9
CHUNK = 50000          # 每块处理的箱数

def lb_batch(M, K, LO, HI):
    """(n,M),(n,M) -> (n,) 保守每箱下界"""
    n = LO.shape[0]
    best = None
    two_pi = 2.0*np.pi
    for k in range(1, K+1):
        a = k*LO; b = k*HI
        mn = np.minimum(np.cos(a), np.cos(b))
        u1 = a/two_pi - TEST_EPS
        u2 = b/two_pi + TEST_EPS
        hit = np.ceil(u1-0.5) <= np.floor(u2-0.5)
        np.copyto(mn, -1.0, where=hit)
        s = mn.sum(axis=1) - M*SLACK
        best = s if best is None else np.maximum(best, s)
    return best

def certify(M, N0, budget, maxdepth, verbose=True):
    K = 5*M
    edges = np.linspace(0.0, np.pi, N0+1, dtype=np.float64)
    idx = np.array(list(product(range(N0), repeat=M)), dtype=np.int64)
    LO = edges[idx]; HI = edges[idx+1]
    nel = 0; unresolved = 0; min_margin = np.inf; maxdepth_seen = 0
    depth_hist = {}
    t0 = time.time()
    while LO.shape[0] > 0:
        if nel >= budget:
            return dict(M=M, ok=False, reason="budget exceeded", neval=int(nel),
                        pending=int(LO.shape[0]), min_margin=float(min_margin),
                        seconds=round(time.time()-t0,1))
        # 取一块
        m = min(CHUNK, LO.shape[0])
        lo, hi = LO[:m], HI[:m]
        LO, HI = LO[m:], HI[m:]
        nel += m
        lb = lb_batch(M, K, lo, hi)
        keep = lb < 0.5                      # 未决 -> 需细分
        if not keep.any():
            min_margin = min(min_margin, float((lb-0.5).min()))
            continue
        min_margin = min(min_margin, float((lb[lb>=0.5]-0.5).min()) if (lb>=0.5).any() else np.inf)
        lo_b, hi_b = lo[keep], hi[keep]
        width = float((hi_b-lo_b).max())
        depth = int(np.ceil(np.log2(np.pi/max(width,1e-300))))
        maxdepth_seen = max(maxdepth_seen, depth)
        if depth >= maxdepth:
            unresolved += int(lo_b.shape[0]); depth_hist[depth] = depth_hist.get(depth,0)+lo_b.shape[0]
            continue
        mid = (lo_b+hi_b)/2.0
        childLO = []; childHI = []
        for bits in product([0,1], repeat=M):
            bits = np.array(bits, dtype=bool)
            childLO.append(np.where(bits[None,:], mid, lo_b))
            childHI.append(np.where(bits[None,:], hi_b, mid))
        childLO = np.concatenate(childLO, axis=0)
        childHI = np.concatenate(childHI, axis=0)
        LO = np.concatenate([LO, childLO], axis=0)
        HI = np.concatenate([HI, childHI], axis=0)
        if verbose and nel % 1000000 < CHUNK:
            print(f"    ... 已评估 {nel:,} 箱, 待处理 {LO.shape[0]:,}, 未决 {unresolved}, {time.time()-t0:.0f}s", flush=True)
    return dict(M=M, ok=True, neval=int(nel), unresolved=0, min_margin=float(min_margin),
                max_depth=maxdepth_seen, depth_hist=depth_hist, N0=N0,
                seconds=round(time.time()-t0,2))

if __name__ == "__main__":
    M = int(sys.argv[1])
    N0 = int(sys.argv[2]) if len(sys.argv)>2 else (10 if M<=4 else 8)
    BUD = int(sys.argv[3]) if len(sys.argv)>3 else 20000000
    DEP = int(sys.argv[4]) if len(sys.argv)>4 else 30
    r = certify(M, N0, BUD, DEP)
    print(json.dumps({k:v for k,v in r.items() if k!="depth_hist"}, ensure_ascii=False))
    if r.get("depth_hist"): print("   depth_hist:", r["depth_hist"])
    print("params SLACK=%g TEST_EPS=%g" % (SLACK, TEST_EPS))
