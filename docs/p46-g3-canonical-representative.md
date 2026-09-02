# P46-G3：Canonical Representative / CFP——第一轮

> 2026-09-02 12:38 · 唐先生 P46-G3 指示 · G3-A + 三模型 + canonicalization 候选审计

## 框架（唐先生）
- **P46-G2 瓶颈**：d_Γ = ∞ ⟺ orbit indistinguishability——O_cl(x) = O_cl(Γx) ⟹̸ x = Γx——不该继续优化 finite witness
- **P46-G3**：核心不是"能不能区分"——**是"能不能定义完全由约束系统自身产生的 canonical representative，使非固定 Γ-pair 根本不能同时 admissible"**
- **G3-A No-Go**（quotient-level admissibility 不能产生 Γ-fixedness——杀掉 flatness/holonomy/quotient/gauge）
- **G3-B canonical section**（σ([x])——约束内生——Γ-equivariant ⟹ 固定）
- **G3-C 危险**（σ = unique Γ-fixed representative——circular）
- **G3-D CFP**（C1-C5——uniqueness + dual covariance + quotient triviality ⟹ σ(q) ∈ Fix(Γ)）
- **G3-G 核心**（普通 invariant scalar 天然 ⟹ off-line pair 非唯一——需 equivariant canonicalization——非 invariant minimization）
- **Model 1/2/3 测试**

## ① G3-A No-Go（确认——解析）
- [Γx] = [x]（quotient 平凡）——admissibility 依赖 [x]——x 与 Γx 同类——不可区分——**任何纯 quotient-level admissibility 不能产生 Γ-fixedness——确认**

## ② G3-F 三模型
- Model 1（无 canonical ordering——σ 不存在——允许）——Model 2（外部 orientation——不 Γ-covariant——canonical ⟹̸ Γ-fixed——确认）——Model 3（intrinsic N——测试见下）

## ③ G3-G 字符串 toy——canonicalization 候选审计（四类全失败）
- **字典序 NF**：不 Γ-equivariant（C4 失败——反例 ab——NF(ab) = ab——ΓNF(ab) = ba ≠ ab）——且——S2 中 x 与 Γx 不同类（[Γx] ≠ [x]——quotient 平凡性失败）
- **Γ-不变标量（长度）**：off-line pair {ab, ba} 同值——**非唯一（G3-G 确认——invariant scalar 天然 ⟹ x ≠ Γx ⟹ non-uniqueness）**
- **回文规范形**："回文" = "Γ-固定"——**circular（G3-C——把 Γ-fixedness 写进 canonicalization——FAIL）**
- **约束内生 NF（Γ-不变 + 终止合流 + 同类）**：**结构性冲突**——同类需双向规则（不终止）——终止需定向（破坏 Γ-不变）——Γ-不变需双向（不终止）——三者冲突

## ⭐ P46-G3 第一轮判定
- **G3-A No-Go 确认**——**CFP 抽象成立（trivial——唐先生说的）**
- **但——"非 Γ 定义的 canonicalization"（C1-C5）——未找到**——已知候选全失败（字典序不 equivariant/标量非唯一/回文 circular/约束 NF 结构性冲突）
- **"equivariant canonicalization"（非 invariant minimization）——P46-G3 的核心创造点——未构造**
- ⚠️ 若最终只能"回文型"（Γ-fixed 写进 canonicalization）——P46 杀掉

## 下一步候选
- (a) 搜索"equivariant canonicalization"（非 invariant minimization——约束内生的选择规则——使 off-line pair 唯一代表且 Γ-固定——需新结构）
- (b) 接受审计（P46-G3 第一轮——canonicalization 候选全失败——CFP 需新 canonicalization——P46-G3 待定——或——P46 杀掉）
- (c) 唐先生指示
