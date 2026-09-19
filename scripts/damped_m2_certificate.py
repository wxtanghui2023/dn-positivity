#!/usr/bin/env python3
"""damped_m2_certificate.py — 甲：阻尼 M=2 鲁棒证书（精确可分离箱下界 + 三维自适应 B&B）

命题: 对 r ∈ [RLO,RHI]，(phi1,phi2) ∈ [0,pi]^2:
      max_{1<=k<=10} [ cos(k phi1) + r^k cos(k phi2) ] >= TARGET

方法: LB(B) = max_{k<=10} [ min_{I1} cos(k phi1) + min_corner_{r∈Ir,phi2∈I2} r^k cos(k phi2) ]
      依据 min_max >= max_min 与可分离性; 阻尼项取矩形四角最小(双线性单调)
      保守化: SLACK=1e-12/项; pi 命中检测 TEST_EPS=1e-9
用法: python3 damped_m2_certificate.py RLO RHI TARGET [N0] [BUDGET] [MAXDEPTH]
"""
import sys, json, time, hashlib
import numpy as np

SLACK = 1e-12; TEST_EPS = 1e-9; PI = np.pi
KS = np.arange(1, 11)

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

def box_lb(Rlo, Rhi, A1, B1, A2, B2):
    lb = np.full(Rlo.shape[0], -np.inf)
    for k in KS:
        c1 = cosmin(A1, B1, k)
        c2lo = cosmin(A2, B2, k); c2hi = cosmax(A2, B2, k)
        rl = Rlo**k; rh = Rhi**k
        damp = np.minimum(np.minimum(rl*c2lo, rl*c2hi), np.minimum(rh*c2lo, rh*c2hi)) - SLACK
        np.maximum(lb, c1 + damp, out=lb)
    return lb

def children(Rlo, Rhi, A1, B1, A2, B2, DEP):
    w = np.stack([Rhi-Rlo, B1-A1, B2-A2], axis=1)
    d = np.argmax(w, axis=1)
    out = []
    for dim in range(3):
        m = d == dim
        if not m.any(): continue
        LO = [Rlo[m], A1[m], A2[m]]; HI = [Rhi[m], B1[m], B2[m]]
        mid = (LO[dim] + HI[dim])/2.0
        for first in (True, False):
            lo = [x.copy() for x in LO]; hi = [x.copy() for x in HI]
            if first: hi[dim] = mid
            else: lo[dim] = mid
            out.append((lo[0], hi[0], lo[1], hi[1], lo[2], hi[2], DEP[m]+1))
    return out

def run(RLO, RHI, TARGET, N0=8, BUDGET=3_000_000, MAXDEPTH=60, quiet=True):
    e = [np.linspace(RLO, RHI, N0+1), np.linspace(0, PI, N0+1), np.linspace(0, PI, N0+1)]
    R=[]; A1=[]; B1=[]; A2=[]; B2=[]; D=[]
    for i in range(N0):
        for j in range(N0):
            for l in range(N0):
                R.append((e[0][i], e[0][i+1], e[1][j], e[1][j+1], e[2][l], e[2][l+1], 0))
    S = [np.array(x) for x in zip(*R)]
    t0=time.time(); neval=0; maxdep=0; minmarg=float('inf')
    while True:
        Rlo,Rhi,A1,B1,A2,B2,DEP = S
        n = Rlo.shape[0]; neval += n
        if neval > BUDGET:
            return dict(ok=False, reason="budget exceeded", neval=neval, pending=int(n),
                        min_margin=float(minmarg), seconds=round(time.time()-t0,1),
                        N0=N0, TARGET=TARGET, R=(RLO,RHI), maxdepth=maxdep)
        lb = box_lb(Rlo,Rhi,A1,B1,A2,B2)
        maxdep = max(maxdep, int(DEP.max()))
        good = lb >= TARGET
        if good.any(): minmarg = min(minmarg, float((lb[good]-TARGET).min()))
        if good.all():
            return dict(ok=True, neval=neval, unresolved=0, maxdepth=maxdep,
                        min_margin_over_target=float(minmarg), seconds=round(time.time()-t0,1),
                        N0=N0, TARGET=TARGET, R=(RLO,RHI))
        sel = ~good
        Ssub = [Rlo[sel],Rhi[sel],A1[sel],B1[sel],A2[sel],B2[sel],DEP[sel]]
        new = children(*Ssub)
        if not new:
            return dict(ok=False, reason="no children", neval=neval, pending=int(sel.sum()))
        S = [np.concatenate([o[i] for o in new]) for i in range(7)]  # 只保留子箱（父箱已被取代）

if __name__ == '__main__':
    RLO=float(sys.argv[1]); RHI=float(sys.argv[2]); T=float(sys.argv[3])
    N0=int(sys.argv[4]) if len(sys.argv)>4 else 8
    BU=int(sys.argv[5]) if len(sys.argv)>5 else 3_000_000
    MD=int(sys.argv[6]) if len(sys.argv)>6 else 60
    # 已在 __main__ 之上 import 完毕，调用
    res = run(RLO, RHI, T, N0, BU, MD)
    blob = json.dumps(res, sort_keys=True).encode()
    res['sha16'] = hashlib.sha256(blob).hexdigest()[:16]
    print(json.dumps(res, ensure_ascii=False))
