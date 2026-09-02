# P49-G2.7.3-R2c-R2：三分块 Sector Decomposition 实验准备

> 2026-09-02 14:08 · 唐先生指示 · W_{0,2}/W_R/prime-power 三块贡献审计

## R2c 判定（唐先生：PASS — coefficient-structure reduction——非 even-ground explanation）
- 真实 QW 系数公式：✓——b_n 非简单 alternating：✓——单纯 b_n 符号不足以决定 ordering：✓——a_n/b_n 必须联合处理：✓
- **完整 sector decomposition：下一步——μ₊<μ₋ 理论证明：OPEN——simple-even：仍 OPEN**

## 关键纠正
- **QW_λ^N = W_{0,2} − W_R − Σ_p W_p**（**减号——不是加**——W_{0,2} rank-one/point——W_R archimedean——Σ_p W_p 素数项）
- b_n = −(1/π)∫₀^L sin(2πny/L)D(y)dy——a_n = 2∫₀^L(1−y/L)cos(2πny/L)D(y)dy——**a_n/b_n 是同一完整 D 的 Fourier 系数——三部分不能拆开判断 ordering**
- **"非交替 b_n"不构成障碍**——μ± = λmin(QW|E±) 同时依赖 a_n 和全部 off-diagonal (b_i−b_j)/(i−j)
- 符号错误会得到错误的 ground state——不是 CCM 的 QW_λ

## R2c-R2 实验设计（三分块）
- QW^(0) = W_{0,2}——QW^(∞) = −W_R——QW^(p) = −Σ_{k≤λ²}Λ(k)k^{−1/2}q(log k)
- 逐块 Δ^(j) = λmin(QW^(j)|E⁻) − λmin(QW^(j)|E⁺)——最终 Δ = μ₋ − μ₊
- **三种可能**：
  1. 单独 prime sector Δ>0 → 纯算术 variational inequality 希望
  2. prime Δ<0 但 archimedean/rank-one 翻转 → global cancellation/coercivity（更难）
  3. 三块单独无稳定符号但总和稳定 Δ>0 → **最值得注意——Weil-form-specific spectral ordering——不是 Toeplitz positivity/prime Fourier sign pattern——G2.7.3 重新定位为 global Weil-form coercivity problem**

## ⚠️ 实现前需确认（论文约定）
1. **W_{0,2} 的精确定义**（"0,2"下标——疑似 ∫f + ∫f^♯ 项——对应显式公式平凡点留数——需 3 节后半确认）
2. **log 坐标约定**（U_n 在 [0,L]——V_n 在 [λ⁻¹,λ]——D 在 [0,L]——f^♯ 如何折叠进 D）
3. **D_p 的精确形式**（素数 δ 的负号/位置——f^♯ 项）
4. D_R archimedean 核（W_R 公式的 log 坐标形式）

## 状态
- R2c PASS（coefficient-structure reduction）——R2c-R2 实验准备中（需 W_{0,2}/D 约定确认——避免符号/约定错误）
