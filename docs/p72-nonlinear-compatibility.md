# P7.2：Nonlinear Euler-Product Compatibility Audit——三道门

> 2026-09-01 · 唐先生 P7.2 指令 · 只打一枪 · Dirichlet-convolution 跨尺度一致性

## 核心对象
- L(s) = −ζ'/ζ(s) = ΣΛ(n)n^{−s}
- **multiplicative closure**：exp_*(A_Λ) 的系数（Dirichlet 卷积指数）——对 ζ：ζ = exp(Σ_{p,k} 1/(k p^{ks}))——系数全 1
- **跨尺度一致性**：Λ(p^k) = log p = Λ(p)——素数幂系数 = 底素数系数——D_T = Σ|c_{p^k} − c_p|²

## Gate N1 — Algebraic tautology（完整数据）——杀
完整零点数据 ⟹ A_Λ = A_ζ（唯一性）⟹ exp_*(A_Λ) = ζ 的系数（1）——**非线性 Euler 恒等式自动成立——代数重言式——杀**

## Gate N2 — Finite-data rigidity（有限数据 |γ| ≤ T）——循环
| δ | D_T（跨尺度缺陷） |
|---|---|
| 0.00 | 0.216（基线——截断误差/恢复不精确——不小） |
| 0.05 | 0.232（+7%） |
| 0.10 | 0.283（+31%） |
- 假想离轴（修改 Hadamard）：D_T 增大（离轴破坏 c_{p^k} vs c_p 一致性——数值）
- **但——实际离轴（RH 假——ζ）：D_T ≈ 截断误差（小——ζ 的 Euler 积精确满足跨尺度一致性）——反例——循环**

## Gate N3 — RH independence
- D_T 定义只用显式公式 + 素数幂支撑——RH-independent ✓
- **但——N2 的"离轴 ⟹ D_T 大"被实际离轴（ζ）反例——循环**

## ⭐ 结论（初步——完整审计）
**非线性 Euler 兼容性——自适应**——与线性/变换恒等式一样：
- N1 杀（代数重言式）——N2 循环（实际离轴满足）——N3 定义干净但结论循环
- **"非线性闭包"不提供独立排除**

## ⭐ 更强的结构发现（唐先生框架）
> **linear identity → transform identity → nonlinear Euler identity 全部不能提供 exclusion**

- **代数重写类机制（线性/变换/非线性——全部自适应）——统一排除（初步）**
- **真正机制候选只剩：不变量 / 单调量 / 全局预算 / 动力学（不再属于"代数重写"）**

## 下一步（P7 系列）
1. **Global compensation/budget**（负贡献必须有界正项承担——全局预算障碍）
2. **Dynamical/Lyapunov**（临界线作为吸引子——dE/dτ = −R(τ)——R ≥ 0 ⟺ β = ½）
3. **不变量/单调量**（非代数重写类——最后候选类）

## 诚实状态
- P7 系列（prime-power support + nonlinear compatibility）：**全部被杀/循环（初步）**
- **但——"代数重写类统一自适应"是确认的强负结果**（比 P6.2 更强——linear → transform → nonlinear 完整链条）
- **机制候选收窄到非代数重写类**（预算/动力学/不变量）——这是 P7 的价值
