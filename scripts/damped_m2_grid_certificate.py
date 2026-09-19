#!/usr/bin/env python3
"""damped_m2_grid_certificate.py — 甲：全 r 区间证书（网格 + 10-Lipschitz 桥接）

逻辑:
  ① 对 r 网格 r_i = i/(N-1), i=0..N-1，逐点用【精确可分离箱下界 + 自适应 B&B】证明
        max_{k<=10}[cos(k phi1) + r_i^k cos(k phi2)] >= TARGET   (∀ phi ∈ [0,pi]^2)
  ② d_2(r) = min_phi max_k S_k(r,phi) 关于 r 是 10-Lipschitz
     （max 的 Lipschitz 常数 = 各 S_k 的常数；|∂S_k/∂r| = |k r^{k-1} cos(k phi2)| <= k <= 10）
  ③ 故 r ∈ [r_i, r_{i+1}] 时  d_2(r) >= TARGET - 10*step/2
用法: python3 damped_m2_grid_certificate.py N TARGET [BUDGET]
"""
import sys, json, time, hashlib
import numpy as np
sys.path.insert(0, 'scripts')
from damped_m2_certificate import run as cert_run

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 334
    TARGET = float(sys.argv[2]) if len(sys.argv) > 2 else 0.38
    BUD = int(sys.argv[3]) if len(sys.argv) > 3 else 6_000_000
    step = 1.0 / (N - 1)
    print(f"网格 N={N} (step={step:.6f})  TARGET={TARGET}  ==> 桥接后保证 >= {TARGET - 10*step/2:.4f}")
    t0 = time.time(); fails = []; tot = 0; worst_margin = 1e9
    for i in range(N):
        r = i * step
        res = cert_run(r, r, TARGET, 8, BUD, 80, quiet=True)
        tot += res.get('neval', 0)
        if res.get('ok'):
            worst_margin = min(worst_margin, res.get('min_margin_over_target', 1e9))
            if i % 40 == 0:
                print(f"  r={r:.4f} ok  neval={res['neval']:>6}  margin={res.get('min_margin_over_target'):.3e}  ({time.time()-t0:.1f}s)")
        else:
            fails.append((round(r, 5), res.get('reason'), res.get('neval')))
            print(f"  r={r:.4f} FAIL {res.get('reason')} neval={res.get('neval')}")
    all_ok = (len(fails) == 0)
    out = dict(N=N, step=step, TARGET=TARGET, certified=all_ok,
               n_fail=len(fails), fails=fails[:20], total_neval=tot,
               bridged_bound=TARGET - 10*step/2, worst_margin=float(worst_margin),
               seconds=round(time.time()-t0, 1))
    out['sha16'] = hashlib.sha256(json.dumps(out, sort_keys=True).encode()).hexdigest()[:16]
    print(json.dumps(out, ensure_ascii=False))
    return 0 if all_ok else 1

if __name__ == '__main__':
    raise SystemExit(main())
