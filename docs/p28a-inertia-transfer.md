# P28-A：Finite-to-Infinite Inertia Transfer——初步（inertia persistence 迹象）

> 2026-09-01 · 唐先生 P28-A 指令 · N→∞ 极限 · inertia persistence vs escape

## ① 理论——K_off 良定义 + inertia 极限
- K_off = Σ_{ρ∈Z_off} K_ρ——K_ρ 秩 ≤ 6——良定义（算子范数）需要 Σ||K_ρ|| < ∞——||K_ρ|| ~ C(δ_ρ)（依赖 δ——不依赖 γ——相位在加权内积中消失）
- **K_off 良定义 ⟺ ΣC(δ_ρ) < ∞（δ_ρ 的加权和）**
- n₋(K_N) = N（有限——G8.2′ 严格）——N→∞：inertia persistence（n₋=∞）vs escape（n₋<∞ 或 0）——决定因素：负方向分离（λ_min(H_N)）

## ② 模型 A/B（RvM 间距——近 γ）——数值受限
- RvM 间距（Δγ ~ 2π/log γ——小）——Gram 病态——n₋ > N（N=5：7——N=8：10）——**伪特征值（阈值 1e-7——Gram 病态）**——数值不可靠

## ③ 模型 C/D（分离 γ——Δγ=5——避免病态）⭐⭐
| N | n₋ | λ₋(K_N) | λmin(H 归一化) | cond(G) |
|---|---|---|---|---|
| 2 | **2** | −0.031 | 0.760 | 6e3 |
| 3 | **3** | −0.035 | 0.793 | 1e4 |
| 4 | **4** | −0.041 | 0.755 | 1.6e4 |
| 5 | **5** | −0.042 | 0.709 | 1.8e4 |
| 6 | **6** | −0.047 | 0.735 | 1.9e4 |
| 8 | **8** | −0.051 | 0.704 | 2.1e4 |
| 10 | **10** | −0.053 | 0.675 | 2.1e4 |

**⭐⭐ 分离 γ——n₋ = N 精确（G8.2′ 确认）——λ_min(H) ≈ 0.67-0.79（稳定——负方向分离——不拥挤）——λ₋ 稳定（不 collapse）——inertia persistence 迹象**

## ⭐ P28-A 初步判定
- **"分离 γ"（大间距）——inertia persistence（n₋=N——λmin(H) ≥ c > 0——负方向分离）——数值确认**
- **"近 γ"（RvM——真实零点）——λ₋ → 0（gap collapse——G7.2）——但——n₋ 是否保持（inertia persistence）需高精度（mpmath）确认**
- **"inertia rigid（n₋=N——代数）but gap fragile（λ₋→0——近 γ——解析）"——dichotomy 在 N→∞ 的形态：分离 γ——两者都保持——近 γ——gap collapse 但 inertia 可能保持（待确认）**

## ⚠️ 诚实边界
- 模型（δ=0.3 固定——γ 等距大间距）是探索性的——真实 Z_off 分布未知（RH 假）
- 近 γ（RvM）——Gram 病态——数值不可靠——需 mpmath 高精度
- "n₋=N"（分离 γ——数值——G8.2′ 理论支持）——"近 γ 的 inertia 保持"未确认

## 下一步
- (a) mpmath 高精度（近 γ——n₋ 是否保持——gap collapse 但 inertia rigid？）
- (b) 模型扩展（δ 随机——γ 密集——真实 RvM 型）
- (c) 报告 P28-A（inertia persistence 迹象——分离 γ 确认——近 γ 待高精度）
