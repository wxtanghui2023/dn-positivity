# P31：Deep-sector Uniform Margin Test——deep 有限（不增长）——倾向情形 I（moving inertia）

> 2026-09-01 · 唐先生 P31 指令 · deep sector transfer test · 情形 I vs II

## ⭐ deep sector 统计（M=1——N=6, 8, 10）
**λ₀=0.05**：deep = 2（N=6,8,10——**不随 N 增长！**）——deep/N：0.40→0.25→0.17（下降——稀释）——min margin：0.084→0.077→0.070
**λ₀=0.1**：deep = 1（N=6,8,10——**恒 1 个！**）——deep/N：0.20→0.12→0.08——min margin：0.141→0.135→0.132（稳定）

## ⭐⭐ 关键发现
- **deep sector 大小不随 N 增长（λ₀=0.1：恒 1 个——λ₀=0.05：恒 2 个）——绝大多数负方向是 edge（λ→0）**
- **deep margin（−λ ≥ λ₀——统一——0.13-0.14——保持）——但——只有 1-2 个方向**
- **deep 方向是"同一个"**（λ~0.13 稳定——mass_M 4.119（N=8）→ 4.514（N=10）——随 N 微调——不独立）
- **rem（deep）**：8.4e-4 → 7.1e-4（小——deep 的 margin 是 λ 本身）

## ⭐ 判定——倾向情形 I（只有 edge 有结构——deep 漂移）
- **deep sector 有限（1-2 个——不增长）——不能提供"无限多个 N-uniform 负方向"**
- **deep 方向是"同一个方向"（随 N 微调——不是渐近独立的新方向）——noncompactness control 未满足**
- **绝大多数负方向是 edge（λ→0——margin→0——无 uniform margin）**
- **"情形 I：extensive inertia + asymptotically critical coherence + no uniform negative form"——倾向（moving inertia 机制支持）**
- **"n₋(K_off)=∞ 的 transfer"——当前无望（deep 不增长——edge 无 margin）**

## ⚠️ 诚实边界
- N≤10（小）——deep 的"有限性"（1-2 个）——可能 N 更大时增长？（但——deep/N 下降——稀释趋势）
- deep 方向的"独立性"（mass_M 4.1→4.5——变化——但——同一个方向）——未严格测（重叠/弱收敛）
- λ₀ 的选择（0.05/0.1——任意）——更小 λ₀（0.01）——deep 更大（但——margin 更小——接近 edge）
- 正则化广义（G+εI）——N=9,10 精度

## 下一步
- (a) deep 方向独立性（重叠矩阵——弱收敛——noncompactness control 严格测）
- (b) 更大 N（deep 绝对数是否增长——决定性）
- (c) 唐先生指示
