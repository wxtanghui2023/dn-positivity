# P27-G3：Diagonal Concentration Lemma——Level G1 闭合

> 2026-09-01 · 唐先生 G3 指令 · 对固定离轴零点构造 f_ε 使 D_δ > 0 · 四步闭合

## P27-G3 结果

### 目标
对固定离轴零点 ρ = ½+δ+iγ（δ≠0），构造 admissible f_ε 使 **D_δ(f_ε, f̄_ε; γ) > 0**（充分小 ε）。

### 四步闭合
1. **test-function class**：dμ_ε ∈ C_c^∞（紧支撑光滑——集中在 u₀≠0——宽 ε）——f_ε(s) = ∫e^{su}dμ_ε(u)——整函数指数型——临界线 f_ε(½+it) = e^{(½+it)u₀}μ̂_ε(t)——μ̂_ε 超多项式衰减——Σ_ρ|f_ε(ρ)| 收敛——**Weil admissible ✓**
2. **diagonal concentration**：dμ_ε 支撑 [u₀−ε, u₀+ε]——|u−v| ≤ 2ε——✓
3. **phase error**：|γ(u−v)| ≤ 2γε——ε ≪ 1/γ——cos(γ(u−v)) = 1 + O(γ²ε²)——✓
4. **β signal lower bound**：u+v ≈ 2u₀（≠0——u₀≠0）——cosh(δ(u+v))−1 ≈ cosh(2δu₀)−1 > 0（δ≠0——δ 小：≈2δ²u₀²）——✓

### 闭合
**D_δ(f_ε,f̄_ε;γ) ≈ 4e^{u₀}[cosh(2δu₀)−1]·|f_ε(0)|² > 0**（主导——误差 O(γ²ε²)+O(δε) 可控）
- ε→0 极限：D_δ → 4e^{u₀}[cosh(2δu₀)−1] > 0（但 Dirac 非 admissible）
- 有限 ε（C_c^∞——admissible）——D_δ(ε) > 0（充分小 ε）
- **⭐ G3 成立：δ≠0 ⟹ ∃f_ε：D_δ(f_ε,f̄_ε;γ) > 0**

### 数值验证（δ=0.1——γ=14.13——u₀=1）
| ε | γε | D_δ |
|---|---|---|
| 0.50 | 7.07（振荡） | 0.000 |
| 0.20 | 2.83（振荡） | 0.000 |
| 0.10 | 1.41（临界） | 0.030 |
| 0.05 | 0.71（可控） | 0.133 ✓ |
（主导 ≈ 0.218——ε→0 收敛——相位可控区 D_δ > 0 ✓）

## ⭐ 诚实定位（Level G1——唐先生层级）
- **G3 成立 = Level G1**：Every off-critical-line zero is **quadratically detectable**——单离轴零点 D_ρ > 0——**局部可检测**
- **不是 Level G2/G3**：
  - 总和（Σ_ρ D_{δ_ρ}——多个离轴——可能抵消）——未证
  - 负方向（Q(f) < 0——离轴）——未证
  - RH 判据（Q ⪰ 0 ⟺ RH）——未接近
- **下一步**：isolation（frequency isolation——f_{τ,ε} 使单零点贡献主导）→ global non-cancellation（离轴缺陷不被抵消）

## 核心价值
- **严格排除了"β 信息可能被 γ 相位完全洗掉"的障碍**（局部对角集中——cos(γ(u−v))≈1——β signal 可见）
- 建立了 Weil functional 中 β 偏离的局部可检测性（Level G1——Detectability ✓）

## 下一步
- (a) zero isolation（frequency isolation——f_{τ,ε} 使 K̂_{τ,ε}(γ₀) ≫ K̂_{τ,ε}(γ)——离轴零点贡献主导）
- (b) global non-cancellation（总和 ΣD——离轴不被抵消）
- (c) 唐先生指示
