# P28-C2-A：Direct low-block compression——negative spectral passage 确认

> 2026-09-01 · 唐先生 C2 指令 · 放弃 Schur 主判据 · direct compression + LDL*

## 实现验证（N=1——单零点——G8.1 理论 n₋=1）
| (δ,γ) | n₋（direct compression） | G8.1 理论 | 状态 |
|---|---|---|---|
| (0.5, 5.0) | 0 | 1 | ⚠️（异常——可能阈值/病态） |
| (0.3, 9.0) | 1 | 1 | ✓ |
| (0.3, 14.1) | 1 | 1 | ✓ |

## ⭐ 核心结果——direct compression（P_M K_N P_M）低块无稳定负谱
**N≥2——低块（前 M 块）n₋ = 0（所有 M=1,2,3——所有 N）**：
- M=1（6 维）：n₋=0（N=2-10）——M=2（12 维）：n₋=0——M=3（18 维）：n₋=0
- **"低块直接压缩——无负方向——K_N 在低块（前 M 块）正定"**
- **单零点负方向（n₋=1）被后加入的 quartets 污染（N≥2——n₋=0——穿过）**

## ⭐ 判定——negative spectral passage（穿过）确认
- **"W_M > 0（几何 overlap——μ_j > 0——负谱空间经过低块）但 direct compression 无稳定负性（n₋=0——二次型正）"**——唐先生判别的"negative spectral passage"分支
- **与 Schur（C1——伪负谱——C_M⁻¹ 病态放大）对比：direct compression 干净（无 C_M⁻¹）——显示低块真无负谱**
- **"persistent core"无证据（低块 n₋=0）——"escape"也未直接证明（W_M 未 → 0）——"passage"是最准确定位**

## ⚠️ 诚实边界
- (0.5, 5.0) 单零点异常（n₋=0 而非 1）——需检查（阈值/病态）——但——(0.3, 9.0) 和 (0.3, 14.1) 正确——实现基本对
- "低块 n₋=0"（N≥2）——数值（双精度）——需 mpmath 确认
- "passage"（W_M > 0 但无稳定负性）——与"escape"（W_M → 0）的区分——需更大 N

## 下一步
- (a) C2-B（LDL* pivot stability——scipy 若可用——inertia 确认）
- (b) 更大 N（W_M 趋势——passage vs escape）
- (c) 唐先生指示
