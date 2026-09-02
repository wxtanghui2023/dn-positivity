# P40-G1：Prime-Support Inverse Rigidity——第一轮

> 2026-09-02 11:32 · 唐先生 P40 指示 · 可实现性 · 几乎周期 · 唯一性半结果

## 框架（唐先生）
- **砍掉 P36-P39 问题设定**（zero-side constraint engineering）——**改问"哪些 divisor 能作为 admissible completed Euler object 的 divisor"（全局可实现性——反问题）**
- **Arithmetic Curvature**：K_D(s) = −Σ_{ρ∈D}1/(s−ρ)²——**二重表示**：global divisor = local arithmetic（prime-power Dirichlet）+ archimedean
- **目标**：K_D ∈ P∩H∩R ⟹ supp D ⊆ {Re s = ½}——**P40-G1**：有限 quartet——K_D ∈ P ⟹ δ_j = 0?

## ① 核心分析——几乎周期论证（严格）
- **有限 K_D（有理——衰减 ~N/t²）——非几乎周期**（经典：一致几乎周期 + 衰减到 0 ⟹ 恒 0）
- **prime-power Dirichlet（绝对收敛——Bohr 一致几乎周期）**
- **⭐ 定理：有限非空 quartet 的 K_D ∉ P（严格——与 δ 无关——trivial——有限 vs 无限）**

## ② 数值验证
- K_D（3 quartet——含 δ=0.1）：|K_D(x)| = 0.035 → 0.004（x=2→50——衰减）
- prime-power Dirichlet 部分和：|Σ| = 0.06-0.29（t=5-50——振荡不衰减）——**对比确认**

## ③ 有限 vs 无限——本质跳跃
- 有限 K_D 非几乎周期——无限 K_D（ζ 的 curvature）几乎周期——**中间没有"有限但非平凡"版本——有限设置无区分力**

## ④ 非平凡版本——可实现性唯一性（半结果）
- 无限 D——K_D ∈ P（von Mangoldt 系数 a_{p^k}=k(log p)²）——Dirichlet 系数唯一决定函数——K_D 的延拓极点 = ζ 零点——K_D 的极点 = D
- **⭐ 半结果：K_D ∈ P ⟹ D = ζ 的零点集（可实现性唯一性——没有其他 divisor 匹配）——但——ζ 零点集是否在线——未知（RH——循环）**
- **"K_D ∈ P ⟹ δ_j = 0"不成立**（trivial 空真/循环）

## ⑤ T4（Herglotz）初步审计
- K_D(x) Re 可正可负——**不自动 Herglotz**——"适当变换"未找到——未闭环

## ⭐ P40-G1 第一轮判定
- **有限 quartet 设置 trivially 失败**（几乎周期——与 δ 无关）
- **⭐ 有价值半结果：prime-power 支撑（von Mangoldt）+ 几乎周期 ⟹ 唯一地 = ζ 的二阶对数导数——可实现性是唯一的（除 ζ 的 divisor——没有其他匹配）**
- 几何支撑（在线）——循环（ζ 未知）——需 T4（Herglotz）或新 Gate

## ⚠️ 诚实
- 几乎周期论证严格（Bohr——绝对收敛覆盖——prime-power 系数绝对收敛 ✓）
- T4 未闭环（变换未找到）——"可实现性唯一性"是唯一性不是几何支撑（在线需 RH——循环）

## 下一步候选
- (a) T4 深化（Herglotz/Stieltjes——适当变换——未找到）
- (b) 扰动版本（ζ + 移动 quartet——同样 trivial——无区分力）
- (c) 唐先生指示
