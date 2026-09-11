#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# T1 测试：二维 (σ,γ) 网格扫描 —— 找谷线
import numpy as np
from addmul_defect_spectrum import build_K, lmin

def scan(N, sigmas, gammas):
    K = build_K(N)
    M = np.zeros((len(sigmas), len(gammas)))
    for i, sg in enumerate(sigmas):
        for j, gm in enumerate(gammas):
            lm, _ = lmin(K, sg + 1j * gm)
            M[i, j] = lm
    return M

if __name__ == "__main__":
    import sys
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 50
    sigmas = np.round(np.arange(0.05, 1.0, 0.05), 2)
    gammas = np.arange(0, 41, 4)
    M = scan(N, sigmas, gammas)
    # 打印: 行=σ, 列=γ, 值=λ_min (科学计数简写)
    print(f"N={N}  λ_min(σ,γ) 矩阵 (行σ 0.05→0.95, 列γ 0→40)")
    hdr = "σ\\γ  " + " ".join(f"{g:>9d}" for g in gammas)
    print(hdr)
    for i, sg in enumerate(sigmas):
        row = " ".join(f"{M[i,j]:9.3e}" for j in range(len(gammas)))
        print(f"{sg:4.2f}  {row}")
    # 每 γ 的谷 σ (λ_min 最负或最小?)
    print("\n每 γ 的 λ_min 最小位置 (谷):")
    for j, gm in enumerate(gammas):
        i = np.argmin(M[:, j])   # 最负
        i2 = np.argmin(np.abs(M[:, j]))  # 最接近 0
        print(f"  γ={gm:3d}: 最负 σ={sigmas[i]:.2f} (λ={M[i,j]:.3e}) | 最接近0 σ={sigmas[i2]:.2f} (λ={M[i2,j]:.3e})")
