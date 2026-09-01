# P5.12-C1：Difference-Spectrum Counterexample——C_Λ 是正确方向——三角不等式不紧

> 2026-09-01 · 唐先生 P5.12-C1 指令 · hostile theorem test

## 唐先生的分解（验证——正确）
**F(θ) = Σ_r b_r e^{irθ}——inf_θ F(θ) ≥ b₀ − Σ_{r≠0}|b_r|**：
- b₀：平均/对角
- Σ|b_r|：phase concentration
- **C_Λ = Σ|b_r|/b₀ < 1 ⟹ coercivity（严格充分——非循环）**

## 数值结果
| 配置 | 差集唯一数 | C_Λ | inf F/bohr |
|------|:--:|:--:|:--:|
| RvM（J=100） | — | **6.85** | **0.067（正）** |
| linear（间距 5） | 119/3600 | 1.17 | 0.779 |
| quadratic（j²） | 2269/3600 | **0.55** | **1.12（强）** |
| log（RvM 局部） | 3541/3600 | 6.16 | 0.073 |

## ⭐ 关键发现
1. **C_Λ 与 F 负相关（趋势）**：C_Λ 大（RvM 6.85 / log 6.16）⟹ F 小（0.067/0.073）——C_Λ 小（quadratic 0.55）⟹ F 大（1.12）——**difference-spectrum concentration 是正确方向**
2. **⚠️ 三角不等式下界太粗**：RvM 的 C_Λ = 6.85 > 1——但 F = 0.067 > 0——**实际相位部分抵消（超出三角不等式）**——**C_Λ < 1 是充分非必要**
3. **additive energy 不是决定性**：quadratic（差频分散——E 低）——C_Λ 也低（0.55）——coercivity 强——**"E 低 ⟹ C_Λ 大"只在系数和发散时成立**（Σ|b_r| ~ (Σ1/γ_j)²——RvM 的 Σ1/γ_j 对数发散——quadratic 收敛）
4. **真正的 rigidity variable：C_Λ（difference-spectrum concentration）——但需要超越三角不等式的精细估计（相位部分抵消）**——**这是"phase rigidity"的精确形态**

## 结论
- **"E 低 ⟹ coercivity"方向不成立**（additive energy 只是 proxy——不是 rigidity variable）
- **"C_Λ < 1 ⟹ coercivity"严格成立**（充分——但三角不等式不紧——RvM 的 C_Λ>1 仍 coercive）
- **"coercivity ⟹ C_Λ < 1"不成立**（RvM 反例——C_Λ=6.85 但 F>0）
- **Rigidity Gap 精确定位**：coercivity 需要"相位部分抵消"（实际 Σb_r e^{irθ} 的相干性 < 三角上界）——**C_Λ 的精细版本（考虑相位）才是核心**

## 下一步（唐先生框架）
- P5.12-C2：有限维版本——inf_θ F_N(θ) ≥ c（与 N 无关）——何时成立
- **"相位部分抵消"的精细估计**：Σ_{r≠0} b_r e^{irθ} 的实际最大模（非三角上界）——需要差频相位的相干性分析
- P5.12-C3：RvM + separation + energy bound ⟹? coercivity
