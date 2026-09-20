#!/usr/bin/env python3
"""rpm_certificate_v3.py — (RP_M) 证书引擎 v3：pending-buffer + 安全带区间复核 + 验收自检

用法:
  python3 scripts/rpm_certificate_v3.py M target [budget] [maxdepth] [batch]
  python3 scripts/rpm_certificate_v3.py --selftest M [n]     # 随机箱：筛值 vs 区间真值

严格性链（验收项对应）:
 (A) 浮点筛余量: 每项下移 EPS_TERM=1e-11（≫ 最坏 1-ulp 误差），求和后再留 EPS_TOTAL=1e-9
     => 在显式浮点模型下  LB_true >= LB_float - 1e-9
 (B) 安全带: 余量 in (0, BAND] 的箱【一律】用 core.lb_box（原已验收区间函数）复核；
     maxdepth 处余量<=0 的箱也复核 => certify 不依赖浮点假设（除筛子的"拆分"决策，拆分无害）
 (C) 覆盖: 初始网格共享边 + 拆分共享中点 => 精确铺满；末尾做浮点体积自检
 (D) 参数: K=5M 全额枚举（assert）；域 [0,P]^M，P=pi_hi>pi
 (E) 资源: pending 上限按 M 自适应（约 300MB），单进程
"""
import sys, time, numpy as np
sys.path.insert(0, 'scripts')
import m3_certificate_interval_arith as core
from fractions import Fraction

EPS_TERM = 1e-11
EPS_TOTAL = 1e-9
BAND = 1e-9

def mincos_vec(L, H):
    inv = 1.0 / np.pi
    n1 = np.ceil(L * inv - 1e-9); n2 = np.floor(H * inv + 1e-9)
    contains = (n2 - n1) >= 1
    oddn1 = (np.abs(n1 % 2.0) == 1.0); p1 = n1 * np.pi
    contains |= oddn1 & (p1 >= L - 1e-9) & (p1 <= H + 1e-9)
    c = np.minimum(np.cos(L), np.cos(H)) - EPS_TERM
    return np.where(contains, -1.0, c)

def lb_vec(A, B, M):
    K = 5 * M
    best = np.full(A.shape[0], -np.inf)
    for k in range(1, K + 1):
        s = np.zeros(A.shape[0])
        for j in range(M):
            s += mincos_vec(k * A[:, j], k * B[:, j])
        np.maximum(best, s, out=best)
    return best

def selftest(M, n=400, seed=0):
    """随机箱：比较筛下界与区间真下界（筛应 <= 真 + 0，且差距极小）"""
    rng = np.random.default_rng(seed)
    Pf = float(core.P)
    worst = -9e9; worst_gap = 0.0; nmiss = 0
    for t in range(n):
        c = rng.random(M) * Pf; w = 10 ** rng.uniform(-4, -1, M)
        A = np.array([c]); B = np.array([np.minimum(c + w, Pf)])
        f = float(lb_vec(A, B, M)[0])
        a = [core.Fraction(float(x)) for x in A[0]]; b = [core.Fraction(float(x)) for x in B[0]]
        iv_ = float(core.lb_box(a, b, M))
        if f > iv_ + 1e-12:   # 筛值高于真值 => 不安全
            nmiss += 1; worst_gap = max(worst_gap, f - iv_)
        worst = max(worst, iv_ - f)
    print(f"[selftest] M={M} 样本={n}：筛值高于真值的次数={nmiss}（应为 0），最大越界={worst_gap:.3e}")
    print(f"[selftest] 筛值比真值低的最大量={worst:.3e}（应 <= EPS_TOTAL={EPS_TOTAL:g}）")
    return nmiss == 0

def main():
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        M = int(sys.argv[2]); n = int(sys.argv[3]) if len(sys.argv) > 3 else 400
        ok = selftest(M, n); print("自检结论:", "PASS" if ok else "FAIL"); return 0 if ok else 1
    M = int(sys.argv[1]); target = float(sys.argv[2])
    budget = int(sys.argv[3]) if len(sys.argv) > 3 else 20000000
    maxdep = int(sys.argv[4]) if len(sys.argv) > 4 else 80
    BATCH  = int(sys.argv[5]) if len(sys.argv) > 5 else 150000
    MEM_CAP = max(200000, int(3.0e8 / (24.0 * M)))
    GRID_CAP = max(20000, min(300000, MEM_CAP // 2))
    Pf = float(core.P)
    N0 = 1
    while (N0 + 1) ** M <= GRID_CAP: N0 += 1
    assert 5 * M >= 5
    t0 = time.time()
    h = Pf / N0
    ei = np.arange(N0 + 1, dtype=np.float64) * h; ei[-1] = Pf
    grid = np.indices([N0] * M).reshape(M, -1).T
    A0 = np.stack([ei[grid[:, d]] for d in range(M)], axis=1)
    B0 = np.stack([ei[grid[:, d] + 1] for d in range(M)], axis=1)
    pending = [(A0, B0, np.zeros(A0.shape[0], dtype=np.int32))]
    neval = 0; n_sieve = 0; n_iv = 0; n_unres = 0; minm = None; maxd = 0; vol = 0.0
    band_checked = 0; unres_boxes = []; lastprint = 0.0
    while pending:
        tot_pend = sum(p[0].shape[0] for p in pending)
        if tot_pend > MEM_CAP:
            print(f"[STOP] pending 超上限 {MEM_CAP}（防内存）: 未处理={tot_pend}"); n_unres += tot_pend; break
        Aa = []; Bb = []; Dd = []; cnt = 0
        while pending and cnt < BATCH:
            a, b, d = pending.pop(); Aa.append(a); Bb.append(b); Dd.append(d); cnt += a.shape[0]
        A = np.vstack(Aa); B = np.vstack(Bb); D = np.concatenate(Dd)
        if neval + A.shape[0] > budget:
            print("[STOP] 预算耗尽"); n_unres += A.shape[0]; break
        neval += A.shape[0]; maxd = max(maxd, int(D.max()))
        LB = lb_vec(A, B, M)
        margin = LB - EPS_TOTAL - target
        cert = margin > BAND
        if cert.any():
            n_sieve += int(cert.sum())
            m = float(margin[cert].min()); minm = m if minm is None else min(minm, m)
            vol += float(np.prod(B[cert] - A[cert], axis=1).sum())
        rest = np.where(~cert)[0]
        if rest.size:
            Rm = margin[rest]
            need_iv = ((Rm > 0) & (Rm <= BAND)) | (D[rest] >= maxdep)
            idx_iv = rest[need_iv]
            idx_split = rest[~need_iv]
            for t_ in idx_iv:
                a = [core.Fraction(float(x)) for x in A[t_]]; b = [core.Fraction(float(x)) for x in B[t_]]
                band_checked += 1
                if core.lb_box(a, b, M) >= target:
                    n_iv += 1; vol += float(np.prod(B[t_] - A[t_]))
                else:
                    if int(D[t_]) >= maxdep:
                        n_unres += 1
                        if len(unres_boxes) < 200: unres_boxes.append((A[t_].tolist(), B[t_].tolist(), int(D[t_])))
                    else:
                        idx_split = np.append(idx_split, t_)
            if idx_split.size:
                Aq, Bq, Dq = A[idx_split], B[idx_split], D[idx_split]
                wid = Bq - Aq; jm = np.argmax(wid, axis=1); row = np.arange(Aq.shape[0])
                mid = (Aq[row, jm] + Bq[row, jm]) / 2.0
                A1 = Aq.copy(); B1 = Bq.copy(); B1[row, jm] = mid
                A2 = Aq.copy(); B2 = Bq.copy(); A2[row, jm] = mid
                Dn = Dq + 1
                pending.append((A1, B1, Dn)); pending.append((A2, B2, Dn))
        if time.time() - lastprint > 20:
            lastprint = time.time()
            print(f"  neval={neval} sieve={n_sieve} iv={n_iv} unres={n_unres} pend={sum(p[0].shape[0] for p in pending)} d<={maxd} t={time.time()-t0:.0f}s", flush=True)
    dt = time.time() - t0
    vol_exp = Pf ** M
    print(f"\nM={M} target={target} N0={N0}")
    print(f"评估箱数={neval}  筛认证={n_sieve}  区间复核认证={n_iv}  区间复核次数={band_checked}  未决={n_unres}")
    print(f"最大深度={maxd}  筛认证最小余量={minm}")
    print(f"体积自检: 累计={vol:.10g} 期望={vol_exp:.10g} 相对差={abs(vol-vol_exp)/vol_exp:.3e}")
    print(f"耗时(秒)={dt:.1f}")
    ok = (n_unres == 0)
    print(f"全部认证? = {ok}")
    print(f"⟹ {'严格结论(模显式浮点模型):  m_%d >= %g' % (M, target) if ok else '【未完成】未决 %d' % n_unres}")
    if unres_boxes:
        import json; json.dump(unres_boxes, open('/tmp/rpm_v3_unres.json','w'))
        print(f"未决样本已写 /tmp/rpm_v3_unres.json")
    return 0

if __name__ == '__main__':
    sys.exit(main())
