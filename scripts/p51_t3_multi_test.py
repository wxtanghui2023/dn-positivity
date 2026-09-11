#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# P51-T3 representation 层测试 3 (修正): 逃逸的 ψ 偏差尺度 + 多逃逸累积
# 问题: (1) 单高零点逃逸的 ψ 偏差尺度 (2) 多个逃逸是否累积 (3) 中间尺度是否有 relation 排除
import numpy as np

data = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
gammas = np.sort(np.asarray(data).flatten())

def psi_zc(x, g, beta_shift=None, shift_idx=None):
    """零点贡献 Σ 2Re[x^ρ/ρ] (上半)"""
    s = 0.0
    for i, gg in enumerate(g):
        b = 0.5
        if shift_idx is not None and i == shift_idx:
            b = 0.5 + beta_shift
        rho = b + 1j*gg
        s += 2*(x**rho/rho).real
    return s

def psi_zc_fe(x, g, delta, idx):
    """FE 自洽逃逸: 替换 idx 零点为 ½±δ+iγ (两个上半)"""
    s = 0.0
    for i, gg in enumerate(g):
        if i == idx:
            rp = (0.5+delta) + 1j*gg
            rm = (0.5-delta) + 1j*gg
            s += 2*(x**rp/rp).real + 2*(x**rm/rm).real
        else:
            rho = 0.5 + 1j*gg
            s += 2*(x**rho/rho).real
    return s

if __name__ == "__main__":
    N = 400
    g = gammas[:N].copy()
    delta = 0.2
    
    print("=== 逃逸 ψ 偏差尺度 (x 固定 - 移动不同高度的零点) ===")
    print(f"{'移动零点 γ':>12} {'偏差@x=100':>14} {'偏差@x=1000':>14} {'偏差@x=5000':>14}")
    for idx in [0, 50, 100, 200, 399]:
        gg = g[idx]
        base100 = psi_zc(100, g)
        base1000 = psi_zc(1000, g)
        base5000 = psi_zc(5000, g)
        esc100 = psi_zc_fe(100, g, delta, idx)
        esc1000 = psi_zc_fe(1000, g, delta, idx)
        esc5000 = psi_zc_fe(5000, g, delta, idx)
        print(f"{gg:>12.1f} {abs(esc100-base100):>14.3e} {abs(esc1000-base1000):>14.3e} {abs(esc5000-base5000):>14.3e}")
    
    print("\n=== 多个高零点逃逸的累积 (全部高半移动 - 密度测试) ===")
    # 移动最后 M 个零点 (γ 最高处)
    for M in [1, 5, 20, 50]:
        # FE 逃逸最后 M 个
        def psi_multi(x, g, delta, M):
            s = 0.0
            start = len(g) - M
            for i, gg in enumerate(g):
                if i >= start:
                    rp = (0.5+delta) + 1j*gg
                    rm = (0.5-delta) + 1j*gg
                    s += 2*(x**rp/rp).real + 2*(x**rm/rm).real
                else:
                    rho = 0.5 + 1j*gg
                    s += 2*(x**rho/rho).real
            return s
        base100 = psi_zc(100, g)
        base1000 = psi_zc(1000, g)
        esc100 = psi_multi(100, g, delta, M)
        esc1000 = psi_multi(1000, g, delta, M)
        # 密度: M/N
        dens = M/N*100
        print(f"M={M:>3} (密度 {dens:.1f}%): 偏差@x=100: {abs(esc100-base100):.3e}  偏差@x=1000: {abs(esc1000-base1000):.3e}")
    
    print("\n=== 解释 ===")
    print("若偏差 ~ M·x^{½+δ}/γ_avg - 稀疏逃逸(固定 M)不可见; 正密度(M~N)累积可见")
