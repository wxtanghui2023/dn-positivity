# P27-G6：Quartet-Reduced Collective Signature

> 2026-09-01 · 唐先生 G6 指令 · 修正逻辑边界（¬RH ⟹ Z_off≠∅ 非"有限"）· 集合级 signature

## 逻辑修正（采纳）
- **¬RH ⟹ Z_off ≠ ∅**（∃ρ₀：Re ρ₀ ≠ ½）——**不是**"离轴零点有限"
- 在线零点精确零模：D_ρ(f,f̄) = 0（Re ρ = ½）——D(f) = Σ_{ρ∈Z_off} D_ρ——**global obstruction 完全来自 off-line zeros 之间的相互抵消**

## 第一计算：quartet 求和——核的对称性
- quartet {ρ, ρ̄, 1−ρ, 1−ρ̄}——δ 和 γ 的符号组合（±δ, ±γ）
- **cosh(δ(u+v))−1 是 δ 偶函数——cos(γ(u−v)) 是 γ 偶函数**
- **⭐ K_{δ,γ} = K_{δ,−γ} = K_{−δ,γ} = K_{−δ,−γ}——四成员核完全相同——Q_{δ,γ}(f) = 4·D_ρ——核不变！**
- **⭐⭐ functional-equation quartet symmetry does NOT cure phase cancellation**（确认唐先生预判——γ 振荡完全保留——乘 4）
- 数值确认：D(ρ) = D(ρ̄) = D(1−ρ̄) = D(1−ρ) = −0.000173——Q = 4×——✓

## 第二计算：Q_{δ,γ}(f_{τ,ε}) = 4·R(γ)——R(γ) = α²A + 2αβB·cos(γε) + β²C

## 第三计算：S(f) = 4·Σ_{ρ∈Z_off} R(γ_ρ)

## ⭐ 核心发现——collective signature 的正性（准均匀假设）
- **准均匀分布**（mod 2π/ε——零点无相位相干——GUE 类）：⟨cos(γε)⟩ ≈ 0——**⟨R⟩ = α²A + β²C = 0.00697 > 0**
- **数值模拟**（100 离轴零点——γ 准均匀）：S/N > 0（三 trial 全正——0.0075-0.0080）
- **⭐ "Z_off ≠ ∅ ⟹ ∃f: S(f) < 0"——大概率不成立（准均匀假设）**
- **"可以存在离轴零点——但集合级 quadratic signature 保持正"——比"单零点 isolation 失败"更深的 obstruction——"collective phase cancellation"是真正的墙（唐先生判断）**

## ⚠️ 诚实边界
- "准均匀"是假设（零点统计——GUE 类——无相位相干——合理但未证）
- "选择 f 匹配离轴聚类"（如果离轴零点有聚类——未知）——可能
- "S(f) > 0"（对固定 f）≠ "S(f) ≥ 0 对所有 f"——sup 分析未做

## 下一步
- (a) "⟨R⟩ > 0 的严格化"（准均匀假设——零点相位无相干（GUE/间距统计）——collective signature 正定——集合级 obstruction——"真正的墙：collective phase cancellation"）
- (b) "离轴聚类假设"（如果离轴零点聚类——负区间匹配）
- (c) 唐先生指示
