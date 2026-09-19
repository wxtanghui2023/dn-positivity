#!/usr/bin/env python3
"""damped_rpM_certificate.py — 通用 M 的【阻尼版】鲁棒证书（精确可分离箱下界 + 高维自适应 B&B）

命题: 设 |z_1| = 1, |z_i| = r_i ∈ [0,1] (i=2..M)，则
        max_{1<=k<=5M} [ cos(k phi_1) + sum_{i>=2} r_i^k cos(k phi_i) ]  >=  TARGET
      对一切 (r_2..r_M) ∈ [0,1]^{M-1} 与 (phi_1..phi_M) ∈ [0,pi]^M

箱下界（可分离）: LB(B) = max_k [ sum_i min_{corner} r_i^k cos(k phi_i) ]
  依据 max_k min_B <= min_B max_k; 每 (r_i, phi_i) 对取矩形四角最小（双线性单调）
保守化: SLACK=1e-12/项; pi 命中检测 TEST_EPS=1e-9
用法: python3 damped_rpM_certificate.py M TARGET [N0] [BUDGET] [MAXDEPTH]
"""
import sys, json, time, hashlib
import numpy as np

SLACK = 1e-12; TEST_EPS = 1e-9; PI = np.pi

def cosmin(lo, hi, k):
    a = k*lo; b = k*hi
    m = np.ceil((a/PI - 1.0)/2.0)
    hit = (2.0*m + 1.0)*PI <= b + TEST_EPS
    return np.where(hit, -1.0, np.minimum(np.cos(a), np.cos(b))) - SLACK

def cosmax(lo, hi, k):
    a = k*lo; b = k*hi
    m = np.ceil(a/(2.0*PI))
    hit = 2.0*m*PI <= b + TEST_EPS
    return np.where(hit, 1.0, np.maximum(np.cos(a), np.cos(b))) + SLACK

def box_lb(LO, HI, M, KS):
    n = LO.shape[0]
    lb = np.full(n, -np.inf)
    nphi0 = M - 1                      # r 维数 = M-1；phi 从第 M-1 列开始
    for k in KS:
        tot = np.zeros(n)
        for i in range(M):
            cmin = cosmin(LO[:, nphi0+i], HI[:, nphi0+i], k)
            if i == 0:
                tot += cmin
            else:
                cmax = cosmax(LO[:, nphi0+i], HI[:, nphi0+i], k)
                rl = LO[:, i-1]**k; rh = HI[:, i-1]**k
                corner = np.minimum(np.minimum(rl*cmin, rl*cmax), np.minimum(rh*cmin, rh*cmax))
                tot += corner - SLACK
        np.maximum(lb, tot, out=lb)
    return lb

def run(M, TARGET, N0=6, BUDGET=30_000_000, MAXDEPTH=40):
    D = 2*M - 1                        # 维数：r_2..r_M (M-1) + phi_1..phi_M (M)
    KS = np.arange(1, 5*M + 1)
    dom = [ (0.0, 1.0) ]*(M-1) + [ (0.0, PI) ]*M
    # 初始网格 N0^D
    grids = [np.linspace(a, b, N0+1) for (a,b) in dom]
    mesh = np.meshgrid(*[np.arange(N0)]*D, indexing='ij')
    idx = np.stack([m.ravel() for m in mesh], axis=1)   # (N0^D, D)
    LO = np.stack([grids[d][idx[:, d]] for d in range(D)], axis=1)
    HI = np.stack([grids[d][idx[:, d]+1] for d in range(D)], axis=1)
    DEP = np.zeros(LO.shape[0], dtype=np.int32)
    t0=time.time(); neval=0; maxdep=0; minmarg=float('inf')
    while True:
        n = LO.shape[0]; neval += n
        if neval > BUDGET:
            return dict(ok=False, reason="budget exceeded", M=M, neval=neval, pending=int(n),
                        min_margin=float(minmarg), maxdepth=maxdep, seconds=round(time.time()-t0,1),
                        TARGET=TARGET, N0=N0)
        lb = box_lb(LO, HI, M, KS)
        maxdep = max(maxdep, int(DEP.max()))
        good = lb >= TARGET
        if good.any(): minmarg = min(minmarg, float((lb[good]-TARGET).min()))
        if good.all():
            return dict(ok=True, M=M, neval=neval, unresolved=0, maxdepth=maxdep,
                        min_margin_over_target=float(minmarg), seconds=round(time.time()-t0,1),
                        TARGET=TARGET, N0=N0)
        sel = ~good
        LO = LO[sel]; HI = HI[sel]; DEP = DEP[sel] + 1
        W = (HI - LO) / np.array([b - a for (a, b) in dom])
        d = np.argmax(W, axis=1)
        newLO = []; newHI = []; newDEP = []
        for dim in range(D):
            m = (d == dim)
            if not m.any():
                continue
            mid = (LO[m, dim] + HI[m, dim]) / 2.0
            lo1 = LO[m].copy(); hi1 = HI[m].copy(); hi1[:, dim] = mid
            lo2 = LO[m].copy(); hi2 = HI[m].copy(); lo2[:, dim] = mid
            newLO += [lo1, lo2]; newHI += [hi1, hi2]
            newDEP += [DEP[m], DEP[m]]
        LO = np.concatenate(newLO); HI = np.concatenate(newHI); DEP = np.concatenate(newDEP)

if __name__ == '__main__':
    M = int(sys.argv[1]); T = float(sys.argv[2])
    N0 = int(sys.argv[3]) if len(sys.argv) > 3 else 6
    BU = int(sys.argv[4]) if len(sys.argv) > 4 else 30_000_000
    MD = int(sys.argv[5]) if len(sys.argv) > 5 else 40
    res = run(M, T, N0, BU, MD)
    res['sha16'] = hashlib.sha256(json.dumps(res, sort_keys=True).encode()).hexdigest()[:16]
    print(json.dumps(res, ensure_ascii=False))
