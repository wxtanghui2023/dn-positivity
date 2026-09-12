# P32：Deep-sector Persistence / Independence Test——finite persistent core 确认

> ⚚ 勘误指针（2026-09-12）：本文中出现的每 orbit 负指标 **1**（或 N 个 orbit 的 **N**）应读作 **2**（或 **2N**）—— 原值源于 G8.1 的一处代数笔误（把对角块写成 −2σₓ 而非 −2I₂）；详见 `ERRATUM-inertia-factor2.md`。**定性结论不受影响**（有限仍有限 ✓）。

> 2026-09-01 · 唐先生 P32 指令 · D_{λ₀} + principal angles + block-overlap

## ① D_{λ₀}(N)——deep 完全不增长（O(1) 确认）
| N | D_{0.1} | D_{0.05} | D_{0.02} |
|---|---|---|---|
| 5-10 | **1（恒定）** | **2（恒定）** | **2（恒定）** |

## ② principal angles——σ_max(P_DN P_DN')（deep 低块 overlap——λ₀=0.1）
| (N,N') | σ_max | 判定 |
|---|---|---|
| (6,8) | 0.9986 | **same core** |
| (6,10) | 0.9961 | same core |
| (8,10) | 0.9994 | same core |
| (5,10) | 0.9910 | same core |
| (7,10) | 0.9968 | same core |

**⭐⭐ 全部 σ_max ≈ 0.99+（→1）——deep 方向在不同 N 之间是"同一个"——finite persistent core 确认**

## ③ block-overlap profile（deep mass_M）
N=6：3.543——N=8：4.119——N=10：4.514（**缓慢漂移——但——方向同一（σ_max≈1）——core 在低块内微调**）

## ⭐⭐ 决定性结论——"finite persistent core"确认
- **deep sector = 有限个（D_{0.1}=1——O(1)）——且——在不同 N 之间是"同一个方向"（σ_max ≈ 0.99+）**
- **"extensive negative inertia = finite persistent core + extensive near-zero moving edge"（唐先生公式——数值确认！）**
- **P31 的"情形 I"从数值倾向升级为强结构证据**：
  - n₋(K_N)=N（extensive——edge 增长）
  - deep sector = 1 个固定方向（persistent core——σ_max→1）
  - 其余 N−1 个负方向是 edge（λ→0——moving——margin→0）
- **"n₋(K_off)=∞"无望（deep 不增长——edge 无 margin——moving edge 不能传递）**

## ⚠️ 诚实边界
- N≤10（小）——但——D 恒定 + σ_max≈1 的模式清晰
- deep mass_M 漂移（3.54→4.51——但——方向同一——"core 在低块内微调"）
- "persistent core"是 1 个方向（dim=1——不是"core 增长"）
- principal angles 用"低块分量"（固定 6M 维）——全空间嵌入未做（但——低块已足够）

## ⭐ P27 缺口定位（唐先生）
- **P27 缺口 = 缺少把 extensive edge inertia 转化为固定、非退化负子空间的 compactness/transfer principle**
- **extensive count ⇏ extensive uniform margin（确认）——inertia grows without growing deep sector（确认）**

## 下一步
- (a) 更大 N（D 恒定性 + σ_max 趋势——但——mpmath 慢）
- (b) P28-P32 系列总结归档（机制链完整）
- (c) 唐先生指示
