# §7.3 Hochschild——H1-H4 定点审计

> 2026-09-07 22:50 · 唐先生：H1-H4 审计——尤其 H4（去 Weil 化——）——失败则 Connes 2026 降格

## §7.3 对象（精确——）
- Y_S = A_S/Γ_S——semilocal adele class space（A_S = Π_{v∈S}Q_v——Γ_S = {±Πp_j^{n_j}}——）
- 编码：cross products S(A_S)⋊Γ_S——非交换代数——Spec Z 上的 sheaf
- Thm 7.2：O⋊G_m sheaf——generic stalk = S(A_Q)⋊Q^×——global = S(R)⋊{±1}
- §7.4：函数空间（Weil 测试函数——）= semilocal algebras 的 Hochschild homology

## H4：去 Weil 化测试（最重要——）
**问题**：删掉 Weil form——Hochschild 结构能否独立存在？
**分析**：
- Y_S/cross product/HH_* **形式上独立定义**（由 adeles + Γ_S——不需 Weil——）✓
- **但**——该结构的内容（Connes 1998/2014——）：adele class space 的循环同调 = **Weil 显式公式的几何化**（编码素数 + Gamma——不自知零点——）
- §7.4 明说函数空间 = HH_*——即 Hochschild 被用作 **Weil form 的测试函数空间的表示**——非产生新不变量
- 判定：⚠️ 形式上独立——**内容 = 显式公式的几何编码**（Hochschild 提供 Weil 的"几何语言"——非 Weil 外的量——）

## H1：非平凡性
- HH_*/HC_*/cyclic pairing 产生什么不由 Weil form 决定的量？
- 分析：semilocal 代数上同调 = 显式公式的迹公式侧（素数 + Gamma 的几何——）
- pairing 最终 = ΣΛ(n)(...) 经 Mellin/Weil——回到二次型
- 判定：❌ 失败倾向——**Hochschild = Weil 的代数 repackaging**（提供几何语言——非新量——）

## H2：β-blindness
- Y_S/HH_* 由 S（素数集——）与 Γ_S 定义——**不含零点位置参数**
- δ 改变（离轴——）不改变 semilocal 代数结构（S 与 Γ_S 不变——）
- 到 β 需经显式公式（Weil 求和——循环——）
- 判定：❌ β-盲（结构不含 δ——除非循环插入——）

## H3：独立约束
- 无 δ≠0 ⟹ I(ρ) ∉ A（整数/index/谱允许集——）的机制
- semilocal 结构不产生"逐零点"的算术量
- 判定：❌ 无独立约束来源

## 综合判定：❌ H1-H4 审计失败（Connes 2026 家族——）
```
H1：Hochschild = Weil repackaging（几何语言——非新量——）失败
H2：结构 β-盲（S/Γ_S 不含零点——）失败
H3：无独立约束（无逐零点算术量——）失败
H4：形式上独立——但内容 = 显式公式几何化——§7.4 用它表示 Weil 函数空间
⟹ Connes 2026 整条路线 = 已审计的 Weil 重表达（降格——）
```

## 母问题确认（唐先生的先验——）
**arithmetic encoding ≠ individual weight/purity**——semilocal/Hochschild 把 Λ(n)/idele/Weil pairing 组织起来——但不产生逐零点 β-obstruction——同一母问题

## 评级更新
Connes 2026：A− → **B−（审计后——实际 = 已审计的 Weil 重表达——）**
- 6.6② = P49 II-A（死——）
- §7 分析壳 = C1-C3（死——）
- §7.3 代数核 = H1-H4（死——）
