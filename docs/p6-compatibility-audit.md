# P6-Compatibility Audit——第二件事（B_T 构造 + transversality）

> 2026-09-01 · 唐先生 P6-Compatibility Audit 指令 · 三件事

## ① Test-function family（RH-independent）
**f_a(t) = 1/(a²+t²)——Weil admissible——RH-independent**
- ⚠️ **admissibility 条件：素数侧 ΣΛ(n)f̂(log n) ~ Σ log p·p^{−a}——收敛需要 a > 1**（a=1 边界——log log 发散——a<1 快发散）
- **合法 family：a = 2, 3, 4, ...（跨尺度）**

## ② Compatibility operator B_T——transversality
**定义**：
- B_T(Λ) = (Z_Λ(f₁),...,Z_Λ(f_M))——零点侧
- b_T = (P(f₁),...,P(f_M))——素数侧（固定——素数数据）
- **目标**：inf_{a ∈ N_ε(K)} ||B_T a − b_T|| ≥ κ（坏方向违反兼容性）

**数值问题（需修复）**：
- 零点侧截断（500）与素数侧截断（30 万）不匹配
- archimedean 项（Γ）未实现（返回 0）
- a ≤ 1 的 f 不合法（素数侧发散）
- **需要：a > 1 的 f + 匹配截断 + archimedean（Γ 项）——精确 Weil 数值**

## ③ Anti-circularity 检查
- ✅ B_T 构造只用素数数据（P_f）和零点虚部（Z_f）——未用 β≤1/2、pair correlation、RH 等价
- ⚠️ 但——"坏方向违反兼容性"需要非平凡结构联系：
  - **坏方向（系数 v_min）vs 兼容性（配置的性质）**——连接 a(Λ) = 1/ρ(Λ) 不覆盖坏方向
  - **"兼容配置的系数集合"（A_arithmetic）难刻画**——v_min 与"整个集合"的距离——需刻画集合
  - **transversality（任何 Rayleigh 商 < ε 的配置 ⟹ 兼容性偏差 > κ）——非平凡——未建立**

## P6 的诚实状态
**方向正确**（spectral degeneracy + arithmetic constraint ⟹ restricted coercivity——transversality inequality a*Ka + λ||Ba−b||² ≥ c||a||²——即使 K 无谱隙）——**但两个障碍**：
1. **技术障碍（可解决）**：精确 Weil 数值（a > 1 的 f + 匹配截断 + archimedean）
2. **结构障碍（根本）**：A_arithmetic（兼容配置的系数集合）刻画——**与 P5 的"F_U 完备性"类似——可能撞同样的墙**

## 关键区别（P6 vs P5）
- P5：K 有没有谱隙？（spectral rigidity——已撞墙）
- P6：显式公式允许的方向能否进入 K 的近零空间？（compatibility rigidity——新问题）
- **P6 的 transversality inequality 即使 K 无谱隙也可能成立**（兼容性项补足）——**这是"创造机制"的正确方向**

## 下一步
- (a) 修复 Weil 数值（a > 1 的 f + 匹配截断 + archimedean）——让 B_T 计算可靠
- (b) 检查 transversality（Rayleigh 商 vs 兼容性偏差的负相关——对合法配置族）
- (c) 刻画 A_arithmetic（结构问题——核心挑战）
