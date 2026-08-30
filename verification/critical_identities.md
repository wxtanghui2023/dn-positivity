# Critical Identities（v2.14——独立验证用恒等式清单）

## 1. 主恒等式（Main Identity）
$$Q - Q'_{\mathrm{RH}} = \sum_\rho \Delta_H(\gamma_\rho,\delta_\rho)$$
- 逐项恒等（同一零点集——定义直接给出）
- 验证：差 < 1e-21（机器精度——数值）

## 2. 谱偏离量（Discrepancy）
$$\Delta_H(\gamma,\delta) = w_H(\gamma,\delta) - w_H(\gamma,0) = |\delta|\,\widetilde c_H(\gamma,\delta)$$
- **非** δ²c_H（v2.7 修正：δ→0 线性——幂律斜率 1.0）
- c̃_H = N/(|δ|D) > 0（|γ| ≥ γ₁——|δ| ∈ (0,½)——完整闭式）

## 3. 分子恒等式（Numerator）
$$N(x) = \tfrac12(a^2(a+1)+x\gamma^2)(1+\gamma^2)^2 - (a^2+\gamma^2)^2,\quad a = 1+x,\ x=|\delta|$$
- N(0) = 0——∂N/∂x ≥ γ⁶/2+γ⁴+γ²/2−6γ²−13.5 > 0（γ ≥ 2）——N 严格增——N(x) > 0（x > 0）
- D = (a²+γ²)²(1+γ²)² > 0

## 4. 渐近（Asymptotic）
$$\widetilde c_H(\gamma,\delta) \sim \frac{1}{2\gamma^2}\quad (\gamma \to \infty)$$
- 数值确认：γ=100: 5.0015e-5 / 500: 2.0000e-6 / 2000: 1.2500e-7（= 1/(2γ²)）
- ⟹ Σ_ρΔ_H < ∞（Δ_H ~ |δ_ρ|/(2γ_ρ²)——Σγ_ρ^{−2} < ∞）

## 5. 配对定义（Pairing）
$$\langle S,H_0\rangle = \langle \log|\xi(\tfrac12+it)|, H_0''\rangle$$
- H_0''(t) = O(t^{−2}) ∈ L¹——配对有限——避免 H_0 ∈ L¹（H_0 ~ log|t| ∉ L¹）

## 6. 逐项配对（Per-zero pairing）
$$\widehat K_\delta \widehat H_0 = \tfrac{\pi}{2}(1+|u|)e^{-(1+|\delta|)|u|} \in L^1$$
- 零频（u=0）有限（|u| 与 1/|u| 精确抵消——闭式）——非形式操作

## 7. 交换（Interchange）
$$\sum_\rho |\langle K_\rho,H_0\rangle| \ll \sum_\rho |\delta_\rho||H_0''(\gamma_\rho)| < \infty$$
- |δ_ρ| < ½（临界带——无条件）——H_0'' = O(t^{−2})——N(T) = O(T log T)

## 8. 等号（Equality）
$$\sum_\rho \Delta_\rho = 0 \quad (\Delta_\rho \ge 0,\ \text{absolutely convergent}) \Longrightarrow \Delta_\rho = 0\ \forall\rho \Longrightarrow \delta_\rho = 0\ \forall\rho$$
- 正项级数基本性质——不需要 inf Δ_ρ > 0

## 9. 参考投影（Projection）
$$Q'_{\mathrm{RH}} = \sum_\rho w_H(\gamma_\rho,0),\qquad \Pi(\rho) = \tfrac12 + i\gamma_\rho$$
- 参考谱（保持 ordinate/multiplicity）——非断言 Π(ρ) 是零点——无 RH

## 10. 权重复核（Weight check）
- w_target 的 Fourier：ŵ_target(u) = (π/4)(1+|u|)e^{−|u|}（(1+t²)^{−2} 的 F.T.）——Weil 类可算
- ŵ_target(0) = π/2 ≠ 0——Ĥ_0 零频 1/|u| 型——配对仅通过乘积（非单独延拓）
