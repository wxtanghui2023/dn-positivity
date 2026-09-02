# P41-G1：Arithmetic Unitary Factorization——第一轮

> 2026-09-02 11:40 · 唐先生 P41 指示 · 消零定理 · unitary 不约束零点 · inner 循环

## 框架（唐先生）
- **P40-G1 封档**："uniqueness achieved, geometric rigidity absent"
- **T4 方向选错**（二阶 Cauchy transform ≠ Herglotz 一阶核）——**integrate K**（一阶对数导数——Poisson kernel）
- **P41：Arithmetic Unitary Factorization**——S_arith(−w) = S_arith(w)^{-1}——Euler locality + reflection + unitarity ⟹ zero/pole support——**Blaschke 型 S(w) = ∏(w−ρ)/(w+ρ)**
- **陷阱**：不能把 Ξ 塞进 Hardy（普通 Hardy 零点可在半平面内部）——需特殊 arithmetic unitary structure

## ① ⭐ 消零定理（新观察——严格）
- **S(w) = ζ(½−w)/ζ(½+w)——FE：ζ(½−w) = χ(½−w)·ζ(½+w)⟹ S(w) = χ(½−w)——ζ 的零点在比值中完全消掉！**
- **"比值型 unitary"不携带零点信息（= archimedean χ——Γ 因子）——极点在实轴负侧（w=−2n−½）——与 RH 无关**
- S(−w) = 1/S(w)（unitary ✓——FE 自动）——但——无零点信息

## ② 数值验证
- S(w) vs χ(½−w)：差 ~1e-22（FE ✓ 消零）——|S(it)| = 1（共轭——unitary——平凡）

## ③ unitary 模条件不约束零点（反例）
- S(w) = (w−a)/(w+a)（a 实）——S(−w) = 1/S(w) ✓——|S(it)| = 1 ✓——**但——极点在实轴（不是虚轴）**
- **"|S(it)| = 1"不⟹ 极点在虚轴**

## ④ inner-outer 分解——循环审计
- ζ(½+w) 的 inner 因子 = Re ρ > ½ 的零点——**RH ⟺ inner 平凡——循环**——Ingham 只给 o(T) 密度——不排除存在——"Euler 结构 ⟹ inner 平凡"需 Euler 延拓——循环

## ⑤ Hardy 类障碍
- Ξ(w) = ξ(½+w)——整函数——但——实轴增长（Γ 因子——(x/2)^{x/2}）——**不 ∈ H²**——规范化需实轴模（|ξ(½+it)|——含零点——循环）

## ⭐ P41-G1 第一轮判定
- **消零定理**：比值型 unitary（ζ(½−w)/ζ(½+w)）——FE ⟹ = χ——**"unitary 比值"不可能携带零点——携带零点的 unitary 需非比值构造**
- **unitary 模条件不约束零点**（反例 Blaschke 实极点）
- **inner-outer 循环**（RH ⟺ inner 平凡——Ingham 不够）
- **Hardy 类障碍**（Ξ 增长——规范化循环）
- **⟹ "unitary factorization"第一轮——与 β-wall 同深度（比值消零/循环）——"global factorization rigidity"未出现**
- **⚠️ 未完全死：非比值 unitary（相位 Ξ/|Ξ|——虚轴）——|Ξ(it)| 含在线零点（离轴不在）——相位结构的零点信息——未探索**

## ⚠️ 诚实
- 消零定理严格（FE——数值验证 ✓）——unitary 不约束零点（反例严格）——inner 循环——Hardy 障碍
- "相位 Ξ/|Ξ|"未探索——但——|Ξ(it)| 含在线零点——离轴不在——"相位"如何约束离轴——未明——可能循环

## 下一步候选
- (a) 非比值 unitary（相位 Ξ/|Ξ|——虚轴）——"相位"的零点结构——（未明——可能循环）
- (b) 接受 P41-G1 部分封口（比值消零——unitary 不约束——inner 循环——与 β-wall 同深度）
- (c) 唐先生指示
