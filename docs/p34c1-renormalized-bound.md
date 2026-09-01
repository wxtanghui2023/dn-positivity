# P34-C' C2.1 升级：renormalized coefficient bound——R1/R2/R3 分叉

> 2026-09-01 · 唐先生 renormalization 三分支树 · uniform-in-k control

## ① a_k^ren(X)（固定 k——X→∞）
- k=1：max|·|=0.062——k=5：0.021——k=10：0.011
- **剩余振荡（不干净趋零——但——幅度小 ~0.01-0.06）——"a_k^ren(X)→0（固定 k）"——方向正确——但——有限 X 剩余非零**

## ② B_k = sup_X|a_k^ren(X)|——不单调衰减！
- B_k：0.062 → 0.045 → 0.043 → 0.021 → 0.011 → **0.026（k=20 回升）** → 0.023 → 0.017
- **log-log 斜率 +0.06（不衰减！）——"uniform-in-k control"的 k→∞ 未确认**

## ③ ΣB_k r^k（r<1）
- r=0.5：0.050——r=0.8：0.138——r=0.95：0.460（**有限——r^k 指数压住——但——B_k 不衰减——k→∞ 收敛依赖 r^k（只要 B_k 不超指数增长）——需 B_k 的 k→∞ 上界**）

## ④ K^ren 有限 X——n₋=60（意外——中间状态）
- X=20000：n₋(K^ren)=60——λ_min=−35.3（**a_k^ren 小（~0.01-0.06）但 K^ren 有 60 个负特征值——有限 X 的中间状态（a_k^ren 剩余非零）——非极限**）
- ⚠️ 理论：a_k^ren(X)→0（固定 k——X→∞）——若求和可交换——K^ren→0（R1）——有限 X 的 n₋=60 是"过渡"——不是极限

## ⭐ R1/R2/R3 分叉
- **R1（平凡化）倾向**：a_k^ren → 0（固定 k ✓）+ 求和可交换（ΣB_k r^k < ∞——r<1 ✓ 初步）⟹ **K^ren=0——"Renormalization removes the entire endpoint-generated sign-indefinite component"——有价值的负结果（trivialization obstruction）**
- **R2（非零无限秩）**：需 a_k^ren 极限非零无限支撑——当前数据不支持（a_k^ren → 0）
- **R3（uniform-in-k 失败）**：B_k 不衰减（斜率 +0.06）——k→∞ 若 B_k 超指数增长——Σ 不可交换——第二层 obstruction——**风险未排除**

## ⭐ 新筛选原则（唐先生）
**A legitimate renormalization must remove the noncanonical endpoint oscillation without simultaneously annihilating the entire arithmetic sign-indefinite content.**
- 当前：renormalization 消掉 endpoint 振荡——但——**可能同时消掉全部符号内容（R1——K^ren=0）**——这是负结果（非突破）
- 只有 R2（扣除后留下非零无限秩算术特异极限）才值得 spectral-gap test

## ⚠️ 诚实边界
- Kmax=60——X≤10⁶——B_k 的 sup 是数值（有限 X 集）——k→∞ 渐近需分析（a_k^ren 的衰减率——PNT 误差项）
- K^ren 的 n₋=60（有限 X）——需确认是"过渡"还是"极限"（X→∞——a_k^ren→0——K^ren→0？）
- "uniform-in-k"（R1 vs R3）——B_k 的 k→∞ 上界是关键

## 下一步
- (a) B_k 的 k→∞ 渐近（a_k^ren 衰减率——PNT 误差——决定 R1 vs R3）
- (b) K^ren 的 X→∞ 极限确认（→0（R1）？——或——非零（R2）？）
- (c) 唐先生指示
