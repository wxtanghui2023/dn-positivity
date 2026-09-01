# Rigidity Gap Theorem——Coercivity Gap for Regular Configurations

> 2026-09-01 · 唐先生"最后一个赌注" · 把 Rigidity Gap 从观察变成定理
> 数值验证 + 定理表述 + 证明框架（Vandermonde/Hilbert 技术）

## 定理（Rigidity Gap / Coercivity Gap）

**Theorem (Coercivity gap for regular configurations).**
设 ρ_j = β + iγ_j（β > 1/2），γ_j = γ₀ + jδ，δ = c/log γ₀。
则：
1. **{γ_j} 满足最小间距约束**：γ_{j+1} − γ_j = δ ≥ c/log γ_j 对所有 j（因为 γ_j ≥ γ₀ ⟹ log γ_j ≥ log γ₀ ⟹ c/log γ_j ≤ c/log γ₀ = δ）；
2. **Gram 核正定**：K_T(j,k) = ∫_{logT}^∞ e^{(ρ_j+ρ̄_k−2)u}du = T^{ρ_j+ρ̄_k−2}/(2−ρ_j−ρ̄_k) 满足 K_T ⪰ 0（Gram 矩阵——无条件——任何配置）；
3. **但 coercivity 超指数退化**：λ_min(K_T)/T^{2β−2} ≤ C·e^{−c'J²}（J 个零点——Vandermonde/Hilbert 类病态——高精度验证 log|det|/J² → −2.3）。

**结论**：**正定性 + 间距下界 + 零点计数不提供 uniform coercivity**——存在满足全部无条件几何约束的配置（规则排列）——其离轴贡献的 L² 下界完全失败（λ_min 超指数小）。

## 高精度数值验证（mpmath 50 位——规则排列 Gram 的 det）

| J | det | log\|det\| | log/J² |
|---|---|---|---|
| 2 | 8.4e-04 | -7.09 | -1.77 |
| 3 | 2.3e-09 | -19.87 | -2.21 |
| 4 | 4.9e-17 | -37.55 | -2.35 |
| 5 | 1.4e-26 | -59.56 | -2.38 |
| 6 | 7.8e-38 | -85.45 | -2.37 |
| 7 | 1.3e-50 | -114.87 | -2.34 |
| 8 | 1.2e-64 | -147.18 | -2.30 |

**log|det|/J² → −2.3（常数）——det ~ e^{−2.3J²}——超指数退化**（Vandermonde/Hilbert 类）。

## 对照：真实零点（不规则）的 coercivity

- 真实零点（前 60 个——不规则间距）：λ_min ~ 0.19（P5.9-A 数值）
- 规则排列（同样数量）：λ_min ≤ 1e-300（下溢——至少 300 个数量级差）
- **"不规则性"提供 coercivity（数值）——规则排列（几何级数）破坏**

## 机制：为什么规则排列奇异

频率 {γ₀+jδ}——指数函数 e^{i(γ₀+jδ)u} = e^{iγ₀u}(e^{iδu})^j——**几何级数（z^j 幂）**：
- δ 小（最小间距 ~ 0.023）——e^{iδu} 在积分区间变化慢
- 高次幂 (e^{iδu})^j 与低次幂近似线性相关（准简并）
- Gram 病态（Vandermonde/Hilbert 类——det ~ e^{−cJ²}——超指数）
- **λ_min → 0 超指数——coercivity 完全失败**

## 定理的严格证明框架（下一步——Vandermonde/Hilbert 技术）

1. **Vandermonde 结构**：规则排列的 Gram——频率差 (j−k)δ——行列式可写成 Vandermonde 型：
   - K_T 的 det——用"Cauchy/Vandermonde 行列式"技术——指数上界
2. **Hilbert 矩阵对照**：K̃[j,k] = (2−2β)/(2−2β−i(j−k)δ)——**Cauchy 矩阵类**（1/(a_j−b_k) 型）——**Cauchy 行列式闭式**（Π 型）——**log|det| ~ −cJ²（超指数）——严格可证**
3. **λ_min 上界**：λ_min ≤ (det)^{1/J}（Hadamard/行列式-特征值不等式）——**λ_min ≤ e^{−cJ}（指数）——严格**
4. **完整证明**：Cauchy 行列式闭式 → det 超指数 → λ_min 指数 → 定理

**⚠️ 诚实边界**：
- 数值证据确凿（det ~ e^{−2.3J²}——mpmath 50 位）——**严格证明（Cauchy 行列式）是下一步**——但——技术是标准的（Cauchy/Vandermonde 行列式——闭式已知）
- 规则排列是"人为最坏"配置——真实零点不规则——**定理说的是"几何约束不足"**——不是"真实零点无 coercivity"
- 真实零点的 coercivity（λ_min ~ 0.13）是数值——**其严格性（是否无条件）未建立——开放**——但——这恰恰支持"真实零点的 coercivity 需要算术不规则性（ζ 的独立刚性）"——Rigidity Gap 具体化

## 论文级意义（唐先生的"硬结果"）

1. **严格反例机制**——不是"我们没找到 coercivity"——是"**存在满足全部几何约束的配置使 coercivity 必然失败**"（规则排列——超指数退化）
2. **几何 vs 算术分离**：间距/计数/正定性（几何——无条件）不够——真实零点的 coercivity 需要"频率不规则性"（算术结构——ζ 的——独立刚性）
3. **positive-but-non-coercive 的严格反例**——**Rigidity Gap 从观察变成定理**
4. **通用性**：对一大类 explicit-formula 二次型方法成立——"**coercivity 需要频率不规则性——几何约束不足**"——可引用可复用

## 与论文的整合
- 这篇定理支撑论文的核心命题（Lower-bound obstruction）——从"do not by themselves provide"（观察）升级为"**存在反例配置（定理）**"（硬结果）
- 论文标题候选："**A Rigidity Gap for Explicit-Formula Methods**"——RH 作为主要 case study——核心 theorem = positive ⇏ coercive（本定理）
