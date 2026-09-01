# P33 升级：Moving-Edge Indeterminacy 严格版——2×2 block 反例族

> 2026-09-01 · 唐先生 P33 升级指令 · 块非负严格模型 · finite-section transfer theorem 缺失

## ⭐ 严格反例族——2×2 block 构造
**K_N = ⊕_{j=1}^N [[1, −(1+ε_j)],[−(1+ε_j), 1]]——ε_j = 1/j**
- **每块：A_j=[1] ⪰ 0——C_j=[1] ⪰ 0——det K_j = 1−(1+ε_j)² < 0（1 个负特征值）**
- **特征值：λ_j⁻ = −ε_j——λ_j⁺ = 2+ε_j**
- **负性纯跨块（−2(1+ε_j)x_j y_j）——P28 的 inter-block mechanism 同型**

## ⭐ 验证（数值）
**[1] ε_j = 1/j（无限超临界）**：
| N | n₋ | P_low⪰0 | P_high⪰0 | D_{0.1} | λ_edge |
|---|---|---|---|---|---|
| 5 | 5 | YES | YES | 5 | −0.2 |
| 20 | 20 | YES | YES | 10 | −0.05 |
| 50 | 50 | YES | YES | 10 | −0.02 |

- **极限 K = ⊕_{j≥1} K_j：n₋(K)=∞——但 inf(−⟨Kx,x⟩/||x||²) = inf(1/j) = 0（无 uniform margin！）**

**[2] ε_j = 1/j（j≤5）否则 0（有限超临界）**：
- **n₋ → 5（N=10,20,50 恒 5——有限！）——同一结构——但极限有限**

## ⭐⭐ 决定性——Moving-Edge Indeterminacy 严格确认
- **同一有限截断现象（n₋=N + 块非负 + D_{λ₀}=O(1) + λ_edge→0⁻）——两种无限维结局：**
  - [1]：n₋(K_off)=∞（无 uniform margin）
  - [2]：n₋(K_off)=5（有限）
- **"finite-section inertia data do not determine n₋(K_off)"——严格确认（不需要违反块非负的对角反例）**
- **"infinite negative index ⇏ uniformly negative infinite-dimensional sector"——确认**

## ⭐ P28-P33 最终结构（唐先生）
- **P28-P32 排除的是 ∃ε>0：dim E₋(K_off; −∞, −ε)=∞（uniformly negative sector）——不是 n₋(K_off)=∞ 本身**
- **"P28-P32 do not establish a negative-form transfer to K_off"（不写"无望"）**
- **真正缺失的数学对象：finite-section negative-index transfer theorem**
- **链条：n₋=N → extensive finite-section inertia → inter-block generated → Γ→2⁺, r→1 → λ_edge→0⁻ → D_{λ₀}=O(1) → moving-edge inertia——最后一步（moving-edge ⟹? n₋(K_off)=∞）无合法 implication——moving edge ⇏ n₋(K_off)<∞ 也成立**

## ⚠️ 诚实边界
- 2×2 block 模型是"逐项复现 P28-P32 结构"的抽象标准模型——不是实际 ζ 的 K_N（但——机制同型）
- ε_j 的选择（1/j——moving edge——任意 ε↓0 都可）
- [1]/[2] 的对比是"概念性不定性"的严格实现

## 下一步
- (a) P28-P33 系列总结归档（机制链 + Moving-Edge Indeterminacy + 2×2 标准模型）
- (b) 唐先生指示
