# P49-G2.7.3-R2c：Real Weil Coefficients (a_n, b_n) Audit——第一轮

> 2026-09-02 14:04 · 唐先生指示 (a) · Section 3 → Ψ/D → a_n/b_n

## R2b 封口（唐先生判定：PASS — abstract-structure insufficiency established）
- **结构性 No-Go（局部）**：对 a_{−n}=a_n, b_{−n}=−b_n 的一般 divided-difference parity 矩阵——Z₂ 只保证 even/odd 块分解——不保证 μ₊<μ₋——**CCM 的 even-ground 不能从抽象矩阵结构推出**
- a_n=1, b_n>0 单调衰减族系统出现 μ₋<μ₊——**否定"单调衰减 divided-difference 自动产生 even ground"**
- b_n~(−1)^n/n 族全 N even ground——**ground-sector ordering depends on actual coefficient geometry**
- **重要限定：不能推出 CCM 真实 b_n 必须交替**——真实 a_n≠1——a_n/b_n 是同一 Weil 分布 D 的 Fourier 型泛函——强耦合——实验只证明抽象结构不够——不能识别真实机制

## R2c 目标（唐先生——决定性实验/理论分叉）
- 从 QW_λ(f,g) = Ψ(f**g) 展开到 Fourier/parity 基底——得 a_n = a_n(D), b_n = b_n(D)
- 计算 Δ_N := μ₋(N) − μ₊(N)——观察：
  1. Δ_N > 0 是否对所有测试 N 保持
  2. Δ_N 的渐近量级
  3. b_n 是否交替/准交替
  4. **a_n 是否提供主要 sector ordering（第 4 点重要——不能锁死"交替 b_n"）**
  5. Rayleigh quotient 不等式：QW(g_even, g_even) < QW(g_odd, g_odd) 对所有非零候选向量
- **R2c 分叉三情况**：
  | 真实系数表现 | 对 G2.7.3 意义 |
  |---|---|
  | b_n 明显交替 + 可证符号/完全单调结构 | 具体 variational theorem 入口 |
  | b_n 不交替但 a_n/b_n 联合产生 μ₊<μ₋ | 需 a,b 耦合型不等式 |
  | a,b 都无可利用符号/单调结构 | variational 路线恶化——考虑换机制（第三种也有价值——simple-even 缺失定位成 Weil 分布谱性质问题） |

## 状态
- **R2b PASS（abstract-structure insufficiency established）**
- **R2c OPEN（real Weil coefficients audit）——本轮执行**
- 论文已知：QW_λ(f,g) = Ψ(f**g)——D = log*(Ψ^♯) 在 [0,L]——b_n = −(1/π)∫₀^L sin(2πny/L)D(y)dy——a_n = 2∫₀^L (1−y/L)cos(2πny/L)D(y)dy——γ(V_j) = V_{−j}——L = 2 log λ
- **需 Ψ/D 的显式**（论文 Section 3——Weil 形式定义——显式公式的分布形式）
