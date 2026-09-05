#!/usr/bin/env python3
# P51-T3 representation 层测试: FE 自洽逃逸配置是否违反算术 relations
# 问题: 移动高零点离轴 δ (完整 FE 四重奏) - 是否被 relations 排除?
# relations 检查: (1) ψ 匹配 (2) 零点计数 N(T) (3) 截断矩 Σρ^{-k} (4) 显式公式系数
import numpy as np

# 载入零点 (虚部)
data = np.load('/home/node/.openclaw/workspace/dn-project/data/zeros_odlyzko_100k.npy')
gammas = np.sort(np.asarray(data).flatten())
print(f"载入 {len(gammas)} 个零点, γ₁={gammas[0]:.6f}, γ_max={gammas[-1]:.1f}")

def psi_W(x, gammas, betas=None):
    """显式公式: ψ(x) = x - Σ_ρ x^ρ/ρ - log(2π) - (1/2)log(1-x^{-2})
    用上半零点 (FE 自动含共轭): ψ(x) = x - 2Re Σ_{γ>0} x^{β+iγ}/(β+iγ) - log 2π - ...
    简化: 只取零点项 (主项 x 和常数单独处理)"""
    if betas is None:
        betas = np.ones_like(gammas) * 0.5
    s = 0.0
    for g, b in zip(gammas, betas):
        rho = b + 1j*g
        # 2Re[x^ρ/ρ] (共轭对)
        val = x**rho / rho
        s += 2*val.real
    return s  # 零点贡献 (负号在外面处理)

def psi_full(x, gammas, betas=None, nmax=100000):
    """完整 ψ: x - Σ x^ρ/ρ - log 2π - ½log(1-x^{-2})"""
    zc = psi_W(x, gammas, betas)
    return x - zc - np.log(2*np.pi) - 0.5*np.log(1 - x**(-2))

if __name__ == "__main__":
    N = 400  # 用前 400 个零点
    g = gammas[:N].copy()
    print(f"\n用前 {N} 个零点 (γ 到 {g[-1]:.1f})")
    
    # 参考 ψ_prime (von Mangoldt 直接求和 - 真值)
    # ψ_prime(x) = Σ_{p^k ≤ x} log p
    def psi_prime(x):
        # 简单筛: 素数和素幂
        import math
        # 用预计算素数 (简单)
        limit = int(x)
        sieve = np.ones(limit+1, dtype=bool)
        sieve[:2] = False
        for i in range(2, int(limit**0.5)+1):
            if sieve[i]:
                sieve[i*i::i] = False
        primes = np.nonzero(sieve)[0]
        s = 0.0
        for p in primes:
            pk = p
            while pk <= x:
                s += math.log(p)
                pk *= p
        return s
    
    # 逃逸配置: 移动最高零点离轴 δ (FE 四重奏: 上半 ½±δ+iγ_N)
    delta = 0.2
    g_esc = g.copy()
    beta_esc = np.ones(N) * 0.5
    # 移动最高零点: 在线 {½+iγ_N} → 离轴四重奏 {½±δ+iγ_N, ½±δ-iγ_N}
    # 上半: 两个零点 ½+δ+iγ_N 和 ½-δ+iγ_N (虚部同 γ_N)
    # 但 ψ 用"上半所有零点": 原 γ_N 贡献 2Re[x^{½+iγ_N}/(½+iγ_N)]
    # 新: 2Re[x^{½+δ+iγ_N}/(½+δ+iγ_N)] + 2Re[x^{½-δ+iγ_N}/(½-δ+iγ_N)]
    # 为保持 N(T) 计数: 若只移动一个零点成两个 - 计数 +1 (RvM 渐近容忍)
    # 测试 A: 简单逃逸 (一个零点 β=½+δ - 不 FE 自洽 - 参考)
    # 测试 B: FE 自洽 (两个上半零点 ½±δ)
    
    print(f"\n=== 测试: 移动最高零点 γ_N={g[-1]:.1f} 离轴 δ={delta} ===")
    print(f"ψ 匹配 (x 扫描 - 相对误差 %):")
    print(f"{'x':>10} {'在线':>12} {'逃逸A(单)':>12} {'逃逸B(FE双)':>12}")
    
    for x in [100, 500, 1000, 5000]:
        psip = psi_prime(x)
        # 在线 (前 N 零点)
        psi_on = psi_full(x, g)
        # 逃逸 A: 移动最高零点到 ½+δ (单 - 不计共轭变化 - 直接改 β)
        ga = g.copy(); ba = np.ones(N)*0.5
        ba[-1] = 0.5 + delta
        psi_a = psi_full(x, ga, ba)
        # 逃逸 B: FE 自洽 - 上半两个 (½±δ+iγ_N) - 替代原一个
        # 实现: 把 γ_N 的贡献替换: 原 2Re[x^{½+iγ_N}/ρ] → 2Re[x^{½+δ+iγ_N}/ρ+]+2Re[x^{½-δ+iγ_N}/ρ-]
        zc_on = psi_W(x, g)
        rho_orig = 0.5 + 1j*g[-1]
        contrib_orig = 2*(x**rho_orig/rho_orig).real
        rho_p = (0.5+delta) + 1j*g[-1]
        rho_m = (0.5-delta) + 1j*g[-1]
        contrib_esc = 2*(x**rho_p/rho_p).real + 2*(x**rho_m/rho_m).real
        zc_escB = zc_on - contrib_orig + contrib_esc
        psi_b = x - zc_escB - np.log(2*np.pi) - 0.5*np.log(1-x**(-2))
        
        err_on = abs(psi_on - psip)/psip*100
        err_a = abs(psi_a - psip)/psip*100
        err_b = abs(psi_b - psip)/psip*100
        print(f"{x:>10} {err_on:>10.4f}% {err_a:>10.4f}% {err_b:>10.4f}%")
    
    # 矩检查: Σ_{γ≤Γ} ρ^{-k} (截断) - 移动零点的贡献
    print(f"\n=== 截断矩 Σ ρ^(-k) (γ ≤ Γ={g[-1]:.1f}) ===")
    for k in [1, 2, 3]:
        mom_on = sum(2*((0.5+1j*gg)**(-k)).real for gg in g)
        # 逃逸 B (FE 双): 替换 γ_N
        mom_esc = mom_on - 2*((0.5+1j*g[-1])**(-k)).real \
                  + 2*(((0.5+delta)+1j*g[-1])**(-k)).real \
                  + 2*(((0.5-delta)+1j*g[-1])**(-k)).real
        print(f"k={k}: 在线={mom_on:+.6e} 逃逸B={mom_esc:+.6e} 差={mom_esc-mom_on:+.6e}")
