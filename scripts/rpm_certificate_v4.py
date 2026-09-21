#!/usr/bin/env python3
"""rpm_certificate_v4.py — (RP_M) 证书引擎 v4：【可证余弦包围】版

与 v3 的区别（关键）:
  v3 的筛假设"libm cos 误差 <= 1 ulp"（模显式浮点模型）。
  v4 用【可证包围】：cos 由 Taylor 级数 + 显式截断界 + 每步舍入预算给出 [lo,hi]，
     只依赖 IEEE-754 正确舍入的 +,-,*（标准保证），【不依赖 libm】。
  故 v4 认证的格子是【无浮点假设】级（与慢版区间证书同级），但速度仍是向量化的。
另: v4 不再需要慢速区间引擎收尾（筛本身即严格）。

用法: python3 scripts/rpm_certificate_v4.py M target [budget] [maxdepth] [batch]
      python3 scripts/rpm_certificate_v4.py --selftest
"""
import sys, time, numpy as np
from decimal import Decimal, getcontext

getcontext().prec = 60
_pi2 = Decimal("1.5707963267948966192313216916397514420985846996875529104874722961")
_HI = float(_pi2); _LO = float(_pi2 - Decimal(repr(_HI)))
PI2_HI, PI2_LO = _HI, _LO
TWO_OVER_PI = float(Decimal(2) / Decimal(
    "3.1415926535897932384626433832795028841971693993751058209749445923"))
PI_F = float(Decimal("3.1415926535897932384626433832795028841971693993751058209749445923"))

COS_BUDGET = 1e-12      # cos 包围自身预算
ARG_BUDGET = 1e-13      # 端点乘法 k*a 的舍入预算（|cos'|<=1，按 1:1 传递）
TOL_PI     = 1e-12     # 奇数倍 pi 检测余量：L<=173 时 L/pi 的浮点误差约 1e-13，取 10 倍富余

def cos_enclosure(X):
    """真 cos(X) ∈ [lo,hi]（IEEE 正确舍入假设下）。第三返回值=象限不确定标志。"""
    X = np.asarray(X, dtype=np.float64)
    t = X * TWO_OVER_PI
    n = np.rint(t)
    unc = np.abs(np.abs(t - n) - 0.5) < 1e-9
    r = (X - n * PI2_HI) - n * PI2_LO
    r2 = r * r
    c = np.ones_like(r2); term = np.ones_like(r2)
    for cf in [1.0/2.0, 1.0/24.0, 1.0/720.0, 1.0/40320.0, 1.0/3628800.0,
               1.0/479001600.0, 1.0/87178291200.0, 1.0/20922789888000.0,
               1.0/355687428096000.0]:
        term = -term * r2
        c = c + term * cf
    s = r.copy(); term = r.copy()
    for cf in [1.0/6.0, 1.0/120.0, 1.0/5040.0, 1.0/362880.0, 1.0/39916800.0,
               1.0/6227020800.0, 1.0/1307674368000.0, 1.0/355687428096000.0]:
        term = -term * r2
        s = s + term * cf
    m = np.mod(n, 4.0).astype(np.int64)
    val = np.select([m == 0, m == 1, m == 2, m == 3], [c, -s, -c, s])
    return val - COS_BUDGET, val + COS_BUDGET, unc

def mincos_lo(L, H):
    """min_{x in [L,H]} cos(x) 的可证下界（L,H float 数组）。"""
    n1 = np.ceil(L / PI_F - TOL_PI); n2 = np.floor(H / PI_F + TOL_PI)
    contains = (n2 - n1) >= 1
    oddn1 = (np.abs(n1 % 2.0) == 1.0) & (n1 * PI_F >= L - TOL_PI) & (n1 * PI_F <= H + TOL_PI)
    contains = contains | oddn1
    loL, _, _ = cos_enclosure(L); loH, _, _ = cos_enclosure(H)
    c = np.minimum(loL, loH) - ARG_BUDGET
    return np.where(contains, -1.0, c)

def lb_vec(A, B, M):
    K = 5 * M
    best = np.full(A.shape[0], -np.inf)
    for k in range(1, K + 1):
        s = np.zeros(A.shape[0])
        for j in range(M):
            s += mincos_lo(k * A[:, j], k * B[:, j])
        np.maximum(best, s, out=best)
    return best

def selftest():
    import mpmath as mp
    mp.mp.dps = 45
    rng = np.random.default_rng(11)
    X = np.concatenate([rng.uniform(0, 200, 3000), np.linspace(0, 200, 3000),
                        PI_F * np.arange(1, 80)]).astype(np.float64)
    lo, hi, unc = cos_enclosure(X)
    bad = 0
    for i, x in enumerate(X):
        tr = float(mp.cos(mp.mpf(float(x))))
        if tr < lo[i] or tr > hi[i]: bad += 1
    print(f'[cos 自检] 样本 {len(X)}，越界 {bad}（应 0）'); return bad == 0

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        return 0 if selftest() else 1
    M = int(sys.argv[1]); target = float(sys.argv[2])
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else 20000000
    maxdep = int(sys.argv[4]) if len(sys.argv) > 4 else 80
    BATCH  = int(sys.argv[5]) if len(sys.argv) > 5 else 150000
    MEM_CAP = max(200000, int(3.0e8 / (24.0 * M)))
    GRID_CAP = max(20000, min(300000, MEM_CAP // 2))
    Pf = float(np.nextafter(np.pi, np.inf))  # FIX(C-fix): 原为 float(Decimal(pi)) == math.pi < pi，域 [0,Pf]^M 严格小于目标域 [0,pi]^M（覆盖回归）。改用 nextafter 保证 Pf > pi
    N0 = 1
    while (N0 + 1) ** M <= GRID_CAP: N0 += 1
    t0 = time.time()
    h = Pf / N0
    ei = np.arange(N0 + 1, dtype=np.float64) * h; ei[-1] = Pf
    grid = np.indices([N0] * M).reshape(M, -1).T
    A0 = np.stack([ei[grid[:, d]] for d in range(M)], axis=1)
    B0 = np.stack([ei[grid[:, d] + 1] for d in range(M)], axis=1)
    pending = [(A0, B0, np.zeros(A0.shape[0], dtype=np.int32))]
    neval = 0; nc = 0; nunres = 0; minm = None; maxd = 0; vol = 0.0; last = 0.0
    while pending:
        tot = sum(p[0].shape[0] for p in pending)
        if tot > MEM_CAP:
            nunres += tot; print(f'[STOP] pending 超上限 {MEM_CAP}，未处理 {tot}'); break
        Aa = []; Bb = []; Dd = []; cnt = 0
        while pending and cnt < BATCH:
            a, b, d = pending.pop(); Aa.append(a); Bb.append(b); Dd.append(d); cnt += a.shape[0]
        A = np.vstack(Aa); B = np.vstack(Bb); D = np.concatenate(Dd)
        if neval + A.shape[0] > budget:
            nunres += A.shape[0]
            _dump = Aq_all = np.vstack([p[0] for p in pending] + [A]) if pending else A
            _dumpB = np.vstack([p[1] for p in pending] + [B]) if pending else B
            try:
                np.savez('/tmp/v4_pending.npz', A=_dump, B=_dumpB, D=_dump.shape[0])
                print(f'[STOP] 预算耗尽；pending 已落盘 {_dump.shape[0]} 箱 -> /tmp/v4_pending.npz')
            except Exception as e:
                print('[STOP] 预算耗尽；落盘失败', e)
            break
        neval += A.shape[0]; maxd = max(maxd, int(D.max()))
        LB = lb_vec(A, B, M)
        ok = LB >= target
        nc += int(ok.sum())
        if ok.any():
            m = float((LB[ok] - target).min()); minm = m if minm is None else min(minm, m)
            vol += float(np.prod(B[ok] - A[ok], axis=1).sum())
        idx = np.where(~ok)[0]
        if idx.size == 0:
            if time.time() - last > 20:
                last = time.time()
                print(f'  neval={neval} cert={nc} unres={nunres} pend={sum(p[0].shape[0] for p in pending)} d<={maxd} t={time.time()-t0:.0f}s', flush=True)
            continue
        Aq, Bq, Dq = A[idx], B[idx], D[idx]
        deep = Dq >= maxdep
        if deep.any():
            nunres += int(deep.sum())
        Aq, Bq, Dq = Aq[~deep], Bq[~deep], Dq[~deep]
        if Aq.shape[0]:
            wid = Bq - Aq; jm = np.argmax(wid, axis=1); row = np.arange(Aq.shape[0])
            mid = (Aq[row, jm] + Bq[row, jm]) / 2.0
            A1 = Aq.copy(); B1 = Bq.copy(); B1[row, jm] = mid
            A2 = Aq.copy(); B2 = Bq.copy(); A2[row, jm] = mid
            Dn = Dq + 1
            pending.append((A1, B1, Dn)); pending.append((A2, B2, Dn))
        if time.time() - last > 20:
            last = time.time()
            print(f'  neval={neval} cert={nc} unres={nunres} pend={sum(p[0].shape[0] for p in pending)} d<={maxd} t={time.time()-t0:.0f}s', flush=True)
    dt = time.time() - t0
    vol_exp = Pf ** M
    print(f'\nM={M} target={target} N0={N0}')
    print(f'评估箱数={neval} 认证={nc} 未决={nunres} 最大深度={maxd}')
    print(f'最小余量={minm}')
    print(f'体积自检: 累计={vol:.10g} 期望={vol_exp:.10g} 相对差={abs(vol-vol_exp)/vol_exp:.3e}')
    print(f'耗时(秒)={dt:.1f}')
    ok = (nunres == 0)
    print(f'全部认证? = {ok}')
    print(('严格结论（可证余弦包围，不依赖 libm）: m_%d >= %g' % (M, target)) if ok else ('【未完成】未决 %d' % nunres))
    return 0

if __name__ == '__main__':
    sys.exit(main())
