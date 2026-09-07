#!/usr/bin/env python3
"""
R2：A 型 triangle-of-triangles——Rédei 高阶关联检验
X₁ = R(a₁,b,c₁)——X₂ = R(a₂,b,c₁)——X₃ = R(a₁,b,c₂)——X₄ = R(a₂,b,c₂)（矩形——）
1. 收集 8 状态表（X₁,X₂,X₃——）
2. T_real = E[X₁X₂X₃]
3. pairwise max-ent null（保持 marginal + pairwise——）→ T_pair
4. Δ₃ = T_real − T_pair——D_KL
5. 矩形 I□ = E[X₁X₂X₃X₄] − E_pair[...]
"""
import math, sys, random
sys.path.insert(0, 'scripts')
from redei_v4 import redei_v4, legendre
import numpy as np

def R_pm(a, b, c):
    """R = ±1"""
    v = redei_v4(a, b, c)
    return None if v is None else v  # redei_v4 返回 ±1

def collect_A_type(pool, n_target=300):
    """收集 A 型结构——每样本 (X₁,X₂,X₃,X₄)"""
    samples = []
    random.seed(57)
    for _ in range(2000):
        b = random.choice(pool)
        a_pool = [a for a in pool if a != b and legendre(a, b) == 1]
        if len(a_pool) < 30:
            continue
        a1, a2 = random.sample(a_pool, 2)
        c_pool = [c for c in pool if c not in (a1,a2,b)
                  and legendre(b,c)==1 and legendre(a1,c)==1 and legendre(a2,c)==1]
        if len(c_pool) < 20:
            continue
        c1, c2 = random.sample(c_pool, 2)
        X = []
        ok = True
        for (x,y,z) in [(a1,b,c1),(a2,b,c1),(a1,b,c2),(a2,b,c2)]:
            v = R_pm(x,y,z)
            if v is None:
                ok = False
                break
            X.append(v)
        if not ok:
            continue
        samples.append(X)
        if len(samples) >= n_target:
            break
    return samples

def fit_pairwise_maxent(counts8):
    """拟合 pairwise max-ent（Ising——）到 8 状态计数
    参数 h₁,h₂,h₃,J₁₂,J₂₃,J₃₁——用矩匹配（梯度上升——）
    counts8: 8 数组（顺序 +++,++-,+-+,+--,-++,-+-,--+,---）"""
    # 真实矩
    total = sum(counts8)
    p = np.array(counts8, dtype=float) / total
    X = np.array([[1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1],
                  [-1,1,1],[-1,1,-1],[-1,-1,1],[-1,-1,-1]], dtype=float)
    mu = p @ X  # E[X_i]
    C = np.array([p @ (X[:,i]*X[:,j]) for i,j in [(0,1),(0,2),(1,2)]])
    
    # 用 Newton/梯度拟合 Ising 参数
    # 参数 (h1,h2,h3,J12,J13,J23)
    params = np.zeros(6)
    for it in range(2000):
        # 计算模型概率
        H = (params[0]*X[:,0] + params[1]*X[:,1] + params[2]*X[:,2] +
             params[3]*X[:,0]*X[:,1] + params[4]*X[:,0]*X[:,2] + params[5]*X[:,1]*X[:,2])
        logZ = np.log(np.exp(H).sum())
        p_model = np.exp(H - logZ)
        # 模型矩
        mu_m = p_model @ X
        C_m = np.array([p_model @ (X[:,i]*X[:,j]) for i,j in [(0,1),(0,2),(1,2)]])
        # 梯度
        grad = np.zeros(6)
        grad[0:3] = mu - mu_m
        grad[3] = C[0] - C_m[0]
        grad[4] = C[1] - C_m[1]
        grad[5] = C[2] - C_m[2]
        if np.max(np.abs(grad)) < 1e-10:
            break
        params += 0.5 * grad  # 简单梯度（小步——）
    # 模型的三阶矩
    H = (params[0]*X[:,0] + params[1]*X[:,1] + params[2]*X[:,2] +
         params[3]*X[:,0]*X[:,1] + params[4]*X[:,0]*X[:,2] + params[5]*X[:,1]*X[:,2])
    logZ = np.log(np.exp(H).sum())
    p_model = np.exp(H - logZ)
    T_pair = p_model @ (X[:,0]*X[:,1]*X[:,2])
    return p, p_model, T_pair

def main():
    primes = np.load('/home/node/.openclaw/workspace/prime_data/primes_1e8.npy')
    pool = [int(p) for p in primes if p % 4 == 1 and p > 5 and p < 6000][:300]
    print(f"素数池: {len(pool)}")
    
    samples = collect_A_type(pool, 400)
    print(f"A 型样本: {len(samples)}")
    if len(samples) < 100:
        print("样本不足——扩大池——")
        return
    
    # 8 状态表（X₁,X₂,X₃——）
    # 顺序: +++,++-,+-+,+--,-++,-+-,--+,---
    state_idx = {(1,1,1):0,(1,1,-1):1,(1,-1,1):2,(1,-1,-1):3,
                 (-1,1,1):4,(-1,1,-1):5,(-1,-1,1):6,(-1,-1,-1):7}
    counts8 = np.zeros(8)
    X123 = []
    for s in samples:
        key = (s[0], s[1], s[2])
        counts8[state_idx[key]] += 1
        X123.append(s[0]*s[1]*s[2])
    
    T_real = np.mean(X123)
    print(f"\nT_real = E[X₁X₂X₃] = {T_real:.4f}")
    
    p_real, p_pair, T_pair = fit_pairwise_maxent(counts8)
    print(f"T_pair（max-ent pairwise——）= {T_pair:.4f}")
    print(f"Δ₃ = T_real − T_pair = {T_real - T_pair:.4f}")
    
    # KL 散度
    eps = 1e-12
    KL = np.sum(p_real * np.log((p_real+eps)/(p_pair+eps)))
    print(f"D_KL(P_real ∥ P_pair) = {KL:.6f}")
    
    # 矩形 I□（X₁X₂X₃X₄——）
    X4 = [s[0]*s[1]*s[2]*s[3] for s in samples]
    I4_real = np.mean(X4)
    # pair null 下的 X₁X₂X₃X₄ 期望——需要 X₄ 的模型——近似：用真实 marginal 的独立乘积？
    # 简化：null 下若 X 独立（去相关——）E[X₁X₂X₃X₄] = ΠE[X_i]——但 X 相关——
    # 用"洗牌配对"null——比较真实矩形矩 vs 随机洗牌的
    # 简化报告真实矩形矩 + F₂ 版本
    R_F2 = [(1 if s[0]>0 else 0) + (1 if s[1]>0 else 0) + (1 if s[2]>0 else 0) + (1 if s[3]>0 else 0) for s in samples]
    parity_nonzero = sum(1 for r in R_F2 if r % 2 == 1) / len(R_F2)
    print(f"\n矩形: I□（乘积矩——）= {I4_real:.4f}——parity 非零率 = {parity_nonzero:.3f}")
    
    # 显著性（bootstrap——）
    rng = np.random.default_rng(59)
    n_boot = 200
    boot_T = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(samples), len(samples))
        boot_T.append(np.mean([X123[i] for i in idx]))
    boot_std = np.std(boot_T)
    z = (T_real - T_pair) / (boot_std + 1e-9)
    print(f"\nbootstrap std(T_real): {boot_std:.4f}——z-score（vs pair null——）= {z:.2f}")
    
    print("\n" + "="*60)
    if abs(T_real - T_pair) > 3*boot_std:
        print("✅ R2 通过：三阶残差显著（超出 pairwise max-ent null——）")
    elif abs(T_real - T_pair) > boot_std:
        print(f"⚠️ 弱信号（{abs(T_real-T_pair):.4f} vs {boot_std:.4f}——1-3σ——）需更多样本")
    else:
        print("❌ R2 判死：三阶残差 ≈ 0——无跨三角形高阶关联")

if __name__ == "__main__":
    main()
