# P39-G1：Finite Euler-Orbit Moduli——第一轮

> 2026-09-02 11:20 · 唐先生 P39 指示 · 轨道闭包 · 超平面因子 · no-go 候选

## 框架（唐先生）
- **Euler orbit 三层**：基本 orbit（z_q(s_k)）→ 配置空间 E_σ = ∏S¹_q(σ) → 有限维投影 O_{p,S}‾ = {p^{−s₀}}×∏S¹_q(σ)（Kronecker——唯一分解——P38-G1.7 几何核心）
- **Global compatibility**：C(z) = 0——z ∈ M_arith ⟺ C(z) = 0——C 不能用零点——O_p‾ ⊂ M_arith ⟹ C 在 torus 恒零——**identity theorem 在 Euler 配置空间（不是单变量 s 平面）**
- **P39-G1**：T_S(σ)——O_{p,S}(s₀)——**C1（只用 Euler data）C2（compatibility ≠ ζ=0）C3（轨道 ⟹ torus）C4（torus + normalization 矛盾）**
- **具体实验**：S={2,3,5}——σ=½——p=2 冻结——找 zero-free 非平凡 C(z₂,z₃,z₅)=0——找到 = P39 开始——找不到 = **no-go：Euler finite-orbit geometry has no independent global rigidity**

## ① 轨道闭包（Kronecker——严格）
- z₂ 冻结（|z₂| = 2^{−1/2} ✓）——z₃, z₅ 旋转（α 无理——唯一分解 ⟹ 1,α₃,α₅ ℚ-线性无关）——**O_{p,S}‾ = {z₂⁰}×S¹₃×S¹₅ ✓**

## ② 核心分析——C 轨道恒零 ⟹ 超平面因子
- C(z₂⁰,·,·) 在稠密轨道恒零 ⟹ ≡ 0（T²）⟹ **C = (z₂−z₂⁰)·H（超平面因子——必须）**
- **⭐ 超平面因子吸收全部轨道约束——H 完全自由（不受轨道约束）**——**"稠密 orbit ⟹ 全局刚性"——✗**

## ③ 数值构造验证
- C = (z₂−z₂⁰)·∏(1−α_q z_q)——**轨道上恒零 ✓（max|C| = 0——超平面因子）**——**H 在 torus 上非恒零（样本 0.55-0.58——自由）**

## ④ C1-C4 审计
- C1 ✓（Euler 坐标 + 冻结值）——C2 ✓（不含 ζ——防陷阱通过——z₂=z₂⁰ 冻结兼容/H=0 局部因子零点——非 ζ(s)=0）——C3 ✓（但——torus 恒零只约束 z₂——H 自由）——**C4 ✗（超平面零点与 normalization 不矛盾——矛盾不自然产生）**

## ⭐ P39-G1 第一轮判定——no-go 候选确认（唐先生预设）
- **"C 轨道恒零"⟹ 超平面因子（z₂−z₂⁰）——H 自由——稠密坐标无约束力**
- **"zero-free 非平凡 C"存在（超平面+自由 H）——但——平凡（轨道约束全在超平面——H 不产生刚性）**
- **⟹ "Euler finite-orbit geometry has no independent global rigidity"——"dense orbit ⟹ global rigidity"不成立**
- **机制：p 冻结坐标吸收全部轨道约束——q 稠密坐标"无约束力"（恒零被迫恒等（平凡）——或——被超平面吸收——H 自由）**

## ⚠️ 诚实
- no-go 覆盖"自然候选"（C 实解析/全纯——超平面结构）——非解析 C（指示函数/范数）未覆盖——但——算术 compatibility 通常要求解析结构
- "H 的算术来源"限制 H 的类——H 在 torus 恒零（如果也要求）——又回到平凡（恒等/系数全零）
- 下一步：(a) H 的算术类穷举（∏/对数/多项式——轨道恒零 ⟹ 平凡——确认）(b) 接受 no-go（P39 封档候选）(c) 唐先生指示
