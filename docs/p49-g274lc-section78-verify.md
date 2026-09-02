# P49-G2.7.4-LC：第 7-8 节核验（六项实质完成）

> 2026-09-02 15:38 · /tmp/ccm.pdf 可检索（文件系统）· Lemma 7.3 定理确认 · 桥缺失定位

## 六项核验结果（第 7-8 节原文）
1. **Lemma 7.3 精确结论**：**"The Fourier transform of k_λ converges, when λ→∞, towards the Ξ-function of Riemann uniformly on closed substrips of the open strip |ℑ(z)| < ½"**——**定理（有证明——Mellin 估计——O(λ^{−½−α}) 收敛率）——限定闭子带 |ℑ(z)| < ½**
2. **k_λ 定义**：与 h_λ 相关（prolate——h₀,λ/h₄,λ 线性组合——vanishing integral）——经 E map 构造——Mellin 在临界带
3. **ξ_λ 定义**：QW_λ 最小特征值 eigenvector（simple-even 假设）
4. **ξ̂_{λ,N} ↔ k_λ estimate**：**只有数值证据**（第 8 节 indication (3)——"numerical evidence for proximity extends to higher eigenfunctions"）——**无 operator/kernel estimate——missing step 2 正是此桥**
5. **determinant normalization**：det_reg = −iλ^{−iz}ξ̂(z)（Thm 5.10）——λ^{−iz} 显式 zero-blind——→Ξ 完整归一化 C 在第 7 节开头（"suitably normalized"——strategy 措辞——待精读）
6. **"converges toward Ξ" 性质**：Lemma 7.3 = **定理**（k_λ 侧——带内）——det_reg 路线 = strategy（第 7 节开头）

## ⭐ 关键审计发现
1. **Lemma 7.3 是定理**（非 numerical——有证明——带内一致收敛——O(λ^{−½−α})）
2. **带内限定 |ℑ(z)| < ½ 覆盖 ξ 零点区域**（ξ(s) 零点 ℜ ∈ (0,1) ⟹ Ξ(z) = ξ(½+iz) 的 ℑ(z) = ℜ(s)−½ ∈ (−½,½)）——**对 RH 够**（若 F_j 带内一致收敛 + Z(F_j) ⊂ ℝ——Hurwitz 带内传——排除 ξ 全部非平凡零点位置的非实零点）
3. **三角桥判据的关键 = (II)**：ξ̂_{λ,N} ↔ k_λ 的桥（missing step 2——**目前只有数值证据——indication (3)——无定理**）——(I) k_λ → Ξ 是定理（Lemma 7.3）——(III) Z(F) ⊂ ℝ conditional（Thm 5.10）
4. **det_reg 路线的"converges toward Ξ"是 strategy**（非定理——需第 7 节开头精读确认措辞）

## 三角桥评估（更新）
- (I) k_λ → Ξ（带内——Lemma 7.3 定理）✓
- (II) F_{λ,N} − k_λ → 0（桥——missing step 2——**OPEN——数值证据**）
- (III) Z(F) ⊂ ℝ（Thm 5.10 conditional）✓
- **⟹ L-C 的核心缺口 = (II)（桥接定理）——不是 Lemma 7.3 本身（已有）——不是 det_reg 直接收敛（可绕）**
- **判定：L-C = "缺桥接定理"（ξ̂ ↔ k_λ 的严格 estimate）——非"缺本质新定理"？——需看 (II) 的难度——k_λ 与 ξ_λ 的逼近（第 8 节 missing step 2——论文自列为 essential）——可能本质困难（prolate 逼近 Weil eigenvector 的定量估计）**

## 状态
- G2.7.4-LC：OPEN——核心待证压缩为 **(II) ξ̂_{λ,N} ↔ k_λ 的局部一致桥**（或直接 C·det_reg → Ξ）
- 六项核验完成——L-C 判定 = "缺桥接 estimate"（vs "缺本质定理"——待 (II) 难度评估）

## 下一步候选
- (a) 第 7 节开头精读（det_reg "suitably normalized" 的精确措辞——strategy vs 部分定理——L-B 核验）
- (b) (II) 桥的可行性评估（k_λ 与 ξ_λ 的逼近——第 8 节 missing step 2 的数学结构——prolate 逼近 Weil eigenvector 的困难定位）
- (c) 唐先生指示
