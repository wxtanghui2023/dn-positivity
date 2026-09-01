# P28-B2-C：Low-block effective inertia——Schur complement S_M（穿过——非 core）

> 2026-09-01 · 唐先生 B2-C 指令 · S_M = A_M − B_M C_M⁻¹ B_M* · persistent core 判别

## S_M(N)（Schur complement——低块有效二次型）
**M=1**（6 维）：N=2-4 n₋=0——N=5 n₋=1——N=8 n₋=3——N=10 n₋=4——λ_max > 0（混合——非全负）
**M=2**（12 维）：N=3-6 n₋=0——N=8,10 n₋=2——λ_max > 0
**M=3**（18 维）：N=4-6 n₋=0——N=7 n₋=1——N=8 n₋=0——N=10 n₋=3——不稳定

## ⭐ 核心判定——S_M 无稳定全负谱
- **λ_max(S_M) > 0（所有 M——所有 N——正方向存在）**——低块有效二次型**不是全负的**
- **n₋(S_M) 不稳定**（N 增大——0→1→3——波动——不收敛到固定 r）
- **"低块只是被负谱'穿过'——不是 persistent negative core"**（唐先生判别表——"穿过"分支）

## ⭐ 综合判定
- **"persistent negative core"未确认**（S_M 无稳定全负谱——λ_max > 0——n₋ 不稳定）
- **"persistent low-block negative spectral overlap"（μ_j > 0）已确认——但——"穿过"（S_M 无稳定负谱）**
- **"core + edge"：core 部分未确认（S_M 不给出稳定负谱）——edge（临界漂移）已确认**
- **倾向：低块负质量是"穿过"（负谱空间经过低块——但不是低块的负子空间）——core 未形成**
- **"n₋(K_off) ≥ r"（有限 core）——未确认——"quadratic-form transfer"——未建立**

## ⚠️ 诚实边界
- 实现简化（伪逆——正则化——高块病态——C_M⁻¹ 的截断）——Schur 定性——需 mpmath 确认
- "n₋(S_M) 波动"（0→1→3——不单调）——可能数值——或——真实（核心重组）
- "λ_max(S) > 0"（大——正方向强）——低块有效二次型主要正——负方向（如果有）是少数（n₋ 小——不稳定）

## 下一步
- (a) mpmath 高精度（S_M 的谱——确认 n₋ 波动是真实还是数值）
- (b) 更大 N（S_M 的 n₋ 是否稳定/消失——core vs 逃逸）
- (c) 唐先生指示
