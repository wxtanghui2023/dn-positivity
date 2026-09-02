# P45-G1 剥离实验：逐层维数 + Parity Audit——Toy B = Artifact

> 2026-09-02 12:15 · 唐先生解析审计 · 剥离实验 · Toy B 杀掉

## 唐先生的审计（关键）
- **Fix(M_a)∩Fix(M_b) = span{x₀} 可能已完成全部筛选**——generic 4×4——Fix(M_a) 一维（含 x₀）——Fix(M_b) 一维（含 x₀）——交 = span{x₀}——**第三条件（holonomy）无贡献——3000/3000 不是证据**
- **黄金结果**：dim V₁ = 2——dim V₂ = 2——dim V₃ = 1（第三条件真正起作用）——且——dim(V₂∩H⁻) > 0 但 dim(V₃∩H⁻) = 0
- **反偏置**：x₀⁺（Fix(Γ)）/x₀⁻（AntiFix(Γ)）——两类 seed——holonomy distinguishes duality parity？
- **隐藏代数**：第三条件 (CΓ)²x = x（C = M_aM_b——Γ⁻¹ = Γ）——允许二阶周期
- **状态降级**：P45-G1 = 预备性结果——不计入机制证据

## ① 逐层维数（3000 样本——x₀⁺ self-dual seed）
- **dim V1 = 1：3000/3000——dim V2 = 1：3000/3000——dim V3 = 1：3000/3000**
- **dim V2 > 1：0/3000——dim V3 < dim V2：0/3000（第三条件零贡献）**
- V2 含 Γ-odd：0/3000——V3 含 Γ-odd：0/3000

## ② 反偏置测试（anti-self-dual seed x₀⁻ = (v₀,−v₀)）
- **x₀⁻ ∈ V3（残差 1.5e-14——通过！）——解析：(CΓ)²x₀⁻ = x₀⁻（Cx₀⁻ = x₀⁻——Γx₀⁻ = −x₀⁻——CΓx₀⁻ = −x₀⁻——(CΓ)²x₀⁻ = x₀⁻ ✓）**
- **⚠️ Γ-fixedness 反例：anti-fixed x₀⁻ 通过 holonomy（二阶周期）——Γx₀⁻ = −x₀⁻ ≠ x₀⁻**

## ③ 解析确认——(CΓ)² 的二阶周期允许 anti-fixed
- (CΓ)²x = x 允许 (CΓ)x = −x（二阶周期）——**holonomy 条件 (CΓ)² 不区分 duality parity**
- **⟹ "holonomy distinguishes duality parity"——在 Toy B 中失败（解析——非数值）**

## ⭐ 剥离实验判定——Toy B = Artifact（确认）
- **dim V2 = 1 全部（3000/3000）——V3 = V2（第三条件自动——零贡献）——Toy B = local common-fixed-vector artifact（唐先生预判确认）**
- **反偏置：anti-fixed x₀⁻ 也 ∈ V3——holonomy 不区分 parity——Γ-fixedness 反例（人为 seed——artifact）**
- **⟹ Toy B 经不起剥离实验——按唐先生规则——杀掉——"3000/3000"不计入机制证据（P45-G1 = 预备性——降级确认）**

## 下一步候选
- (a) Toy B 正式杀掉（确认）——P45-G1 保持预备性
- (b) 修正第三条件（一阶 CΓx = x？——或——更高阶环——或——三 morphism——使 holonomy 真正排除 anti-fixed）——或——换 toy（V2 需要 > 1 维——需要"非 generic"的 M_a/M_b——共享更大不动子空间）
- (c) 唐先生指示
