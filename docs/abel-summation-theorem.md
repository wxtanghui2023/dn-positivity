# Abel 求和定理：临界线投影 O(1)（无条件新定理）

> 2026-08-23 17:30 定稿
> 状态：✅ 无条件严格证明 + 数值验证
> 定位：独立无条件定理——但注意（核不匹配发现）它是"临界线投影"控制——不是 r(n) 的完整振荡

## 1. 定理陈述

**定理**：设 {γ_k} 为非平凡零点虚部（递增），S(t) = N(t) − N₀(t) 为 Riemann-Siegel 函数，
δ_k = γ_{k+1} − γ_k − 1/N₀'(γ_k) 为间距偏差。定义权重

$$w_k = \tilde f(\gamma_k)\cdot N_0'(\gamma_k), \qquad \tilde f(t) = 2\sin(c\theta(t))\sin(\theta(t)/2), \quad \theta(t) = \pi - 2\arctan(2t)$$

则（无条件——不假设 RH）：

$$\sum_{k=1}^{N} w_k \delta_k = O(1)$$

## 2. 证明

### 步骤 1：Abel 求和

$$\sum_{k=1}^{N} w_k \delta_k = w_N\left(\sum_{k=1}^{N}\delta_k\right) - \sum_{k=1}^{N-1} \Delta w_k \left(\sum_{j=1}^{k}\delta_j\right), \qquad \Delta w_k = w_{k+1} - w_k$$

### 步骤 2：部分和界（Backlund——无条件）

$$\left|\sum_{k=1}^{N}\delta_k\right| = O(\log\log\gamma_N)$$

（8/22 已严格证明：Σδ_k = O(loglog T)——Backlund |S| ≤ C·log t + 第二中值 + Littlewood）

### 步骤 3：权重差分界

$w_k = \tilde f(\gamma_k)N_0'(\gamma_k)$——$\tilde f(t) \sim c/t^2$（t 大——θ ≈ 1/t），$N_0'(t) = \log(t/2\pi)/(2\pi)$：
$$w_k \sim \frac{c\log\gamma_k}{2\pi\gamma_k^2}, \qquad |\Delta w_k| \le \frac{C}{\gamma_k^2}\log\log\gamma_k$$

（数值：max|Δw| ≈ 0.016，Σ|Δw| ≈ 0.17——n=3000——缓变衰减）

### 步骤 4：余项和收敛

$$\sum_{k=1}^{N-1}|\Delta w_k|\cdot\left|\sum_{j=1}^{k}\delta_j\right| \le C\sum_{k=1}^{N-1}\frac{(\log\log\gamma_k)^2}{\gamma_k^2} < \infty$$

（γ_k ~ 2πk/log k——Σ 1/k² 收敛）

### 步骤 5：边界项

$$|w_N|\cdot\left|\sum_{k=1}^{N}\delta_k\right| \le \frac{c\log\gamma_N}{2\pi\gamma_N^2}\cdot\log\log\gamma_N \to 0$$

### 结论

$$\sum_{k=1}^{N} w_k \delta_k = O(1) \qquad\blacksquare$$

## 3. 数值验证

| N | Σ_{k≤N} w_k δ_k | max|部分和| | Σ\|Δw\|·loglog γ |
|---|---|---|---|
| 500k (n=100) | −0.0026 | — | 0.0433 |
| 500k (n=1000) | −0.0274 | — | 0.1767 |
| 500k (n=3000) | +0.0231 | — | 0.2433 |

- Abel 重建 = 直接计算（差 < 1e-10——恒等式精确）
- 尾部 Σ|Δw|·loglog → 0（后 1/3 = 0.0000——收敛）

## 4. ⚠️ 诚实定位（核不匹配发现——2026-08-23）

**定理 1 证明的是 f̃ 核（8/23 ε_m 核）——不是 r(n) 的完整振荡！**

- r(n) 真实核：f_n(t) = 4sin²(nθ₁(t))，θ₁ = arctan(1/2t)（8/22 权威）
- f̃(t) = cos(2nθ₁) − cos((2n+2)θ₁)（望远镜——ε_m 核）
- **数值**：f̃ 核黎曼和差 ±0.1 vs r(n) ±2.5——差一个数量级

**定理 1 的正确表述**：Σ f̃(γ_k)N₀'δ_k = O(1)——"f̃ 加权的 δ 和"（临界线投影的一环）——无条件真定理——但**不直接证明 r(n) = O(1)**。

**r(n) = O(1) 的真正 Abel 项**：Σ f_n(γ_k)N₀'(γ_k)δ_k——数值 O(1)（−2.76@3000）——但 Σ|wδ| 发散（2683@3000）——**需要 δ 的强抵消 = 相位均匀性 = RH 深度**——未证。

## 5. 意义

1. **独立无条件定理**——"f̃ 加权间距偏差和有界"——可发表为小引理
2. **δ 的 Abel 可和性**——展示 δ_k 的振荡结构（带符号收敛、绝对值发散）
3. **不是 r(n) = O(1) 的证明**——核不匹配——但展示了 Abel 技术的力量
4. **与等价链一致**：r(n) = O(1) ⟺ RH——缺口 = δ 强抵消 = 相位均匀性

## 6. 文件

- scripts/abel_riemann_sum.py（验证——Abel 重建精确）
- scripts/fn_abel_term.py（f_n 核 Abel 项——数值 O(1)——Σ|wδ| 发散）
- docs/kernel-mismatch-finding.md（核不匹配——重要）
