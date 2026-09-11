#!/usr/bin/env python3
"""
Provenance: retroactive archive header added 2026-09-11 by scripts/fix_archive_compliance.py
under the code-archive protocol (docs/PROTOCOL-CODE-ARCHIVE.md, R4).
The analysis itself was performed earlier; this header only records the file's existence
in the committed archive so that the computation is reproducible. Original code below.
"""
# P51-T3 representation 层测试 2: 系数层 + 计数检查
# 逃逸配置的系数 a_n (Mellin 反演 - 显式公式差分) vs von Mangoldt Λ(n)
# 计数 N_W(T) vs N_ζ(T)
import numpy as np

data = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
gammas = np.sort(np.asarray(data).flatten())

def delta_psi(x, g, delta_move=None, idx_move=None):
    """ψ 的零点贡献差: 逃逸配置 - 在线 (移动 idx_move 零点到 ½±δ)"""
    # 在线贡献
    s_on = 0.0
    for gg in g:
        rho = 0.5 + 1j*gg
        s_on += 2*(x**rho/rho).real
    if delta_move is None:
        return s_on
    # 逃逸: 替换 idx_move
    gg = g[idx_move]
    rho_orig = 0.5 + 1j*gg
    contrib_orig = 2*(x**rho_orig/rho_orig).real
    rho_p = (0.5+delta_move) + 1j*gg
    rho_m = (0.5-delta_move) + 1j*gg
    contrib_esc = 2*(x**rho_p/rho_p).real + 2*(x**rho_m/rho_m).real
    return s_on - contrib_orig + contrib_esc

if __name__ == "__main__":
    N = 400
    g = gammas[:N].copy()
    delta = 0.2
    
    print("=== 系数层测试: a_n(W) vs Λ(n) ===")
    print("用显式公式差分: a_n ≈ ψ(n) - ψ(n-1) (平滑版)")
    print(f"{'n':>8} {'Λ(n)':>10} {'在线 a_n':>12} {'逃逸 a_n':>12} {'逃逸偏离':>12}")
    
    # 素数幂的 Λ
    def lam(n):
        # 检查 n 是否素幂
        import math
        # 试除
        for p in range(2, int(n**0.5)+1):
            if n % p == 0:
                # n = p^k?
                m = n
                while m % p == 0:
                    m //= p
                if m == 1:
                    # 素幂
                    return math.log(p)
                return 0
        return math.log(n) if n > 1 else 0
    
    # 选一些 n (避开大筛)
    # 注意: 用 ψ(x) 差分需要 x 连续 - 这里用"跳跃"近似 (x=n 处 ψ 跳 Λ(n))
    # 更准确: ψ(n) - ψ(n-1) = Λ(n) 当 n 素幂 (精确 - 显式公式给 ψ 连续版 - 差在跳跃)
    # 直接比较: 逃逸的"跳跃"是否改变
    # 简化: 检查 ψ_esc(n) - ψ_esc(n-1) vs ψ_on(n) - ψ_on(n-1) (跳跃是否保持)
    for n in [2, 4, 8, 16, 3, 9, 27, 5, 25, 7, 49, 11, 13, 100, 500]:
        if n >= 600: break
        # 跳跃 (用显式公式 - 但显式公式是光滑的 - 跳跃来自截断?)
        # 直接用: ψ(x) 的精确跳跃在素幂 = Λ - 显式公式重建应重现
        # 测: Δ_esc(n) = [ψ_esc(n)-ψ_esc(n-1)] - [ψ_on(n)-ψ_on(n-1)] (逃逸引起的跳跃变化)
        # 用 delta_psi (零点贡献差 - 逃逸 vs 在线)
        d_on = delta_psi(n, g) - delta_psi(n-1, g)  # 在线零点贡献的 n 处变化
        d_esc = delta_psi(n, g, delta, N-1) - delta_psi(n-1, g, delta, N-1)
        jump_change = d_esc - d_on  # 逃逸引起的"跳跃"变化 (应 = 0 若逃逸不可见)
        if n in [2,4,8,16,3,9,27,5,25,49,100,500]:
            print(f"{n:>8} {lam(n):>10.4f} {'':>12} {'':>12} {jump_change:>12.2e}")
    
    print("\n=== 计数检查: N_W(T) - N_ζ(T) ===")
    print(f"移动最高零点 γ_N={g[-1]:.1f} 到 FE 四重奏 (上半 2 个):")
    print(f"上半零点数: 在线 {N} → 逃逸 {N+1} (在 γ_N 高度 +1)")
    print(f"RvM 渐近: N(T) ~ (T/2π)log(T/2πe) - 局部 +1 是 O(1/log T) 相对")
    T = g[-1]
    rvm = (T/(2*np.pi))*np.log(T/(2*np.pi*np.e))
    print(f"RvM({T:.0f}) = {rvm:.1f} - 在线 N={N} (差 {N-rvm:+.1f} - 截断) - 逃逸 +1 相对 {1/N*100:.3f}%")
    
    print("\n=== 结论观察 ===")
    print("1. 系数跳跃变化: 看上面 (应 ~1e-6 量级或更小 - γ_N 贡献)")
    print("2. 计数: 逃逸 +1 上半 - 局部 - RvM 渐近容忍")
    print("3. 矩: 偏离 ~ γ_N^{-k} - 高处不可排除")
