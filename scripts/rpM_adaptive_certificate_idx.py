#!/usr/bin/env python3
"""
rpM_adaptive_certificate_idx.py
目标 (RP_M): 对所有 phi in [0,pi]^M,  max_{1<=k<=5M} sum_j cos(k phi_j) >= 1/2

表示法: 第 d 层网格每维 n_d = N0 * 2^d 格; 箱 = 整数索引 (i_1..i_M), 纵坐标
        lo_j = i_j*pi/n_d,  hi_j = (i_j+1)*pi/n_d
        => 前沿内存降 ~8x (int32 索引 vs float64 坐标), LIFO 保持前沿小
数学内容与保守化参数与 rpM_adaptive_certificate.py 完全相同。
"""
import numpy as np, sys, time, json
from itertools import product

SLACK = 1e-12; TEST_EPS = 1e-9; CHUNK = 200000

def lb_batch(M, K, lo, hi):
    best = None; two_pi = 2.0*np.pi
    for k in range(1, K+1):
        a = k*lo; b = k*hi
        mn = np.minimum(np.cos(a), np.cos(b))
        hit = np.ceil(a/two_pi - TEST_EPS - 0.5) <= np.floor(b/two_pi + TEST_EPS - 0.5)
        np.copyto(mn, -1.0, where=hit)
        s = mn.sum(axis=1) - M*SLACK
        best = s if best is None else np.maximum(best, s)
    return best

def certify(M, N0, budget, maxdepth, verbose=True):
    K = 5*M
    t0 = time.time()
    idx = np.array(list(product(range(N0), repeat=M)), dtype=np.int32)
    stack = [(0, idx)]
    nel = 0; unresolved = 0; min_margin = np.inf; maxdepth_seen = 0; depth_hist = {}
    while stack:
        if nel >= budget:
            pend = sum(a.shape[0] for _, a in stack)
            return dict(M=M, ok=False, reason="budget exceeded", neval=int(nel),
                        pending=int(pend), min_margin=float(min_margin), seconds=round(time.time()-t0,1))
        d, arr = stack.pop()
        n = N0 * (2**d); h = np.pi/n
        take = min(CHUNK, arr.shape[0])
        cur, rest = arr[:take], arr[take:]
        if rest.shape[0]: stack.append((d, rest))
        nel += take
        lo = cur.astype(np.float64)*h
        hi = lo + h
        lb = lb_batch(M, K, lo, hi)
        ok = lb >= 0.5
        if ok.any(): min_margin = min(min_margin, float((lb[ok]-0.5).min()))
        bad = ~ok
        if not bad.any(): continue
        b_idx = cur[bad]
        if d+1 >= maxdepth:
            unresolved += int(b_idx.shape[0]); depth_hist[d+1] = depth_hist.get(d+1,0)+b_idx.shape[0]
            continue
        maxdepth_seen = max(maxdepth_seen, d+1)
        # 子箱: (2i_j + b_j)
        parts = []
        for bits in product([0,1], repeat=M):
            parts.append(2*b_idx + np.array(bits, dtype=np.int32)[None,:])
        stack.append((d+1, np.concatenate(parts, axis=0)))
        if verbose and nel % 2000000 < CHUNK:
            pend = sum(a.shape[0] for _, a in stack)
            print(f"    ... 已评估 {nel:,}, 栈内 {pend:,}, 未决 {unresolved}, 深度 {d+1}, {time.time()-t0:.0f}s", flush=True)
    return dict(M=M, ok=True, neval=int(nel), unresolved=0, min_margin=float(min_margin),
                max_depth=maxdepth_seen, depth_hist=depth_hist, N0=N0, seconds=round(time.time()-t0,2))

if __name__ == "__main__":
    M = int(sys.argv[1]); N0 = int(sys.argv[2]) if len(sys.argv)>2 else (10 if M<=4 else 8)
    BUD = int(sys.argv[3]) if len(sys.argv)>3 else 50000000
    DEP = int(sys.argv[4]) if len(sys.argv)>4 else 40
    r = certify(M, N0, BUD, DEP)
    print(json.dumps({k:v for k,v in r.items() if k!="depth_hist"}, ensure_ascii=False))
    if r.get("depth_hist"): print("   depth_hist:", r["depth_hist"])
