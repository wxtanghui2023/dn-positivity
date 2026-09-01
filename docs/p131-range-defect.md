# P13.1：Arithmetic Range / Adjoint-Kernel Test——第一枪

> 2026-09-01 · 唐先生 P13 指令 · 第一枪（三个问题）

## P13 框架（唐先生——P12 纠偏）
**P12 的 index 失败不是"没找到不定算子"——而是把 index 放在错误对象 K（正定 Gram——n_-(PKP) = 0 结构性事实）**——**应该改变"对象"**：
- K ⟶ A ⟶ Ran A, ker A*, defect
- **"离轴是否产生一个 arithmetic range 无法填补的缺口？"**（不是"离轴产生负能量吗？"）
- **Nyman-Beurling 型 range defect**：dist(f, A_arithmetic)——正定算子 + range defect（不需要不定）
- **β ≠ 0 ⟹ Defect(A) > 0 + arithmetic side 独立给出 Defect(A) = 0**——冲突 ⟹ RH

## P13.1 结果
### ① 非 Weil 的 arithmetic operator A（Nyman-Beurling）
- A = span{ρ_n(x) = {n/x}}（分数部分——整数 dilation）——**RH ⟺ 1 ∈ span closure（已知等价——反循环闸门）**
- **⚠️ 决定性：ρ_n 固定（不含配置参数——不随 ζ 的零点变）——Nyman-Beurling 的 range 是"固定的"——不感知离轴——"β 进入"困难**

### ② d_N² = dist²(1, span{ρ_n: n≤N})——数值（基线）
| N | d_N² |
|---|---|
| 2 | 0.242 |
| 5 | 0.122 |
| 8 | 0.086 |
| 10 | 0.074 |
- **递减——逼近 0 的迹象（与 RH 的 d_N → 0 一致——数值支持——但——是已知等价）**

### ③ 模型离轴轨道的 defect——Defect(ρ) ~ C(γ)β²？
- **路径 1（A(β) 含配置）**——修改 Hadamard ≠ 实际离轴（唯一性——循环）
- **路径 2（g_ρ ∈ ker A*）**——需要"A 的算术结构与零点几何的耦合"——耦合 = 显式公式（自适应——P6）——或——"非自适应桥"（未构造——P12 核心）

## ⭐ P13.1 判定（初步）
1. **Nyman-Beurling 的 A——已知等价（不是新机制）——且——ρ_n 固定——range 不感知离轴**
2. **ker A* 描述——与 RH 等价（循环风险）**
3. **"Defect(ρ) ~ C(γ)β²"——需要"非自适应桥"（未构造——P12 核心——未解决）**
- **P13 撞同样的核心墙（需要"非自适应桥"）——初步**
- **但——"range defect"（而非负谱）是正确的新视角**——"正定 + range defect"（不是不定）——**P12 困境的答案方向确认**
- **候选出路（de Branges 的 H(E)/H_arith quotient）——撞 K1 循环（E 需要零点——HB 条件）**

## 核心未解决（P12 → P13 的统一）
**"非自适应桥"（A 的算术结构 ⟷ 零点几何的独立耦合——非显式公式）**：
- 显式公式是"自适应桥"（两种表示相等——无排除力）
- 需要"非自适应桥"（T_arithmetic ≠ T_zero——较弱投影相等）——**未构造——可能不存在**
- **所有 P5-P13 路线（coercivity/compatibility/positivity/variational/collision/range-defect）都撞这个核心**

## 下一步
- (a) 构造"非自适应桥"A（de Branges defect——但——E 含零点——循环风险）——或——其他候选
- (b) 接受 P13.1 初步收口（核心：非自适应桥——未解决——P5-P13 统一图景）
- (c) 唐先生指示
