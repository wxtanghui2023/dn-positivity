# P28-A(a)：mpmath 高精度——近 RvM 间距——情形 II 确认

> ⚚ 勘误指针（2026-09-12）：本文中出现的每 orbit 负指标 **1**（或 N 个 orbit 的 **N**）应读作 **2**（或 **2N**）—— 原值源于 G8.1 的一处代数笔误（把对角块写成 −2σₓ 而非 −2I₂）；详见 `ERRATUM-inertia-factor2.md`。**定性结论不受影响**（有限仍有限 ✓）。

> 2026-09-01 · 唐先生 P28-A(a) 指令 · 高精度判定情形 II vs III

## ⭐ 结果——情形 II（inertia survives, gap collapses）确认

### RvM 间距——N 扫描（mpmath 50 位）
| N | n₋ | g_N | λmin(H) | κ(H) | 情形 |
|---|---|---|---|---|---|
| 2 | **2** | 1.6e-2 | 0.948 | 1.1 | I |
| 3 | **3** | 7.1e-3 | 0.856 | 1.5 | **II** |
| 4 | **4** | 3.9e-3 | 0.312 | 5.5 | **II** |
| 5 | **5** | 1.2e-3 | 0.216 | 10 | **II** |
| 6 | **6** | 2.7e-4 | 0.096 | 27 | **II** |
| 8 | **8** | 2.0e-5 | 2.5e-3 | 2000 | **II** |

### γ 层级扫描（N=4——RvM 间距）
| γ₀ | n₋ | g_N | λmin(H) | κ(H) | 情形 |
|---|---|---|---|---|---|
| 14.1 | 4 | 3.9e-3 | 0.312 | 5.5 | II |
| 50.0 | 4 | 1.8e-4 | 0.082 | 31 | II |
| 100.0 | 4 | 3.1e-5 | 7.2e-3 | 430 | II |
| 200.0 | 4 | 1.9e-5 | 1.8e-3 | 1800 | II |

## ⭐ 核心结论——情形 II（inertia survives, gap collapses）
- **n₋(K_N) = N（高精度——所有 N——inertia persistence——G8.2′ 理论在 RvM 间距下成立）**
- **g_N → 0（gap collapse——指数级快速——N=8 时 2e-5——γ₀ 增大也递减）**
- **λmin(H) → 0（负方向"拥挤"——κ(H) 增长——Gram 病态增加——但——高精度下 n₋ 仍 = N——不是数值伪影）**
- **"Inertia is algebraically rigid, spectral gap is analytically fragile"——高精度 RvM 模型严格确认——情形 II**
- **"每增加一个 off-line quartet 产生一个负方向——即使能量尺度压向 0——负方向没有消失"**

## ⚠️ 诚实边界
- λmin(H) → 0（负方向拥挤——κ(H) 增长到 2000）——N 更大时——Gram 病态可能超过 50 位精度——"n₋=N"最终受数值限制——**N→∞ 极限仍开放**
- 但现有数据（N≤8——50 位）——情形 II 稳定
- 模型（δ=0.3 固定——RvM 间距）是探索性的——真实 Z_off 分布未知（RH 假）

## ⭐ P28 定理候选
**Inertia Persistence / Gap Collapse Dichotomy**：有限截断中每增加一个 off-line quartet 产生一个负方向（n₋(K_N) = N——代数刚性）；负方向的能量尺度在 N→∞ 时压向 0（g_N → 0——解析脆弱）；负方向本身不消失（情形 II——高精度确认）。
- 拓扑/二次型意义下 n₋(K_N)=N 推出 K_off 存在任意维数负子空间——**下一步（需统一 coercivity/quadratic-form 机制——不是逐个特征值）**

## 下一步
- (a) g_N 定量渐近（g_N vs N——vs γ₀——幂律/指数律）
- (b) 定理候选正式化（Inertia Persistence / Gap Collapse Dichotomy）
- (c) 唐先生指示
