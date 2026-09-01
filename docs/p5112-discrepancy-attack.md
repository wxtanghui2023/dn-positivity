# P5.11-2B：攻击 R₂（local discrepancy）——减弱但不破坏

> 2026-09-01 · 唐先生 P5.11-2 指令 · 条件阶梯（rigidity ladder）逐级攻击

## 条件阶梯（唐先生）
- R₀：global density（N(T) = N_RvM(T) + o(T log T)）
- R₁：separation（γ_{j+1}−γ_j ≥ c/log γ_j）
- R₂：local discrepancy（N(T+h)−N(T) = (h/2π)log T + E(T,h)——uniform bound）
- R₃：quadratic/phase regularity（控制 Σ_{j≠k} w_j w̄_k K(γ_j−γ_k) 的负部分）

## 攻击 R₂ 的实验（Λ₁ vs Λ₂——相同 global/spacing/平均局部——不同 E(T,h)）

### 对数尺度密度调制（A=0.5）
| ω | E(mean) | F/bohr |
|---|---|---|
| 2 | 0.451 | 0.126 |
| 3 | 0.202 | 0.086 |
| **5** | **0.348** | **0.016（最低）** |
| 8 | 0.330 | 0.065 |
| 12 | 0.378 | 0.050 |
| 20 | 0.327 | 0.053 |
| 30 | 0.338 | 0.057 |

### A 扫描（ω=8）
A=0.3（0.054）/ 0.5（0.065）/ 0.7（0.076）/ 0.9（0.049）——稳定 ~0.05-0.08

### 方波 block（0.7×/1.3×）
block=50/100/200：F = 0.064/0.060/0.040（≈ 基线 0.041 或略大）

## ⭐ 结论
**高频密度调制（local discrepancy——E 大）只能"减弱" coercivity（最低 F = 0.016——基线 0.041 的 40%）——不能"破坏"（不 → 0）**：
1. **非单调**：ω=5 处最深（0.016）——更大 ω 回升（0.05-0.065）——不是"越大越破坏"
2. **A 扫描稳定**：A=0.3-0.9——F 稳定 0.05-0.08——不随 A 单调下降
3. **方波 block**：≈ 基线（不破坏）

**R₀ + R₁ + R₂ 级攻击下——coercivity 仍正（≥ 0.016）**——**local discrepancy（R₂）不足以破坏 arithmetic-direction coercivity**。

## 按唐先生框架——进入 R₃（phase regularity）/ BM 重合点
- **R₂ 与 BM regularity 的重合点**（sine-type/de Branges/sampling）——进入 2C
- **R₃（phase regularity）**——直接控制频率差集的负部分——**这是"相位结构"（非几何）**——真正的 rigidity variable 候选
- 候选定理（完全脱离 RH）：inf_{Λ∈R*} inf_θ F > 0——R* 需要包含"相位 regularity"（不只是密度/间距/discrepancy）

## 条件阶梯状态
| 条件 | 攻击 | 结果 |
|------|:--:|:--:|
| R₀（global density） | 规则排列（违反 RvM） | 破坏（但非法——违反 R₀） |
| R₁（separation） | 已含在 RvM | — |
| R₂（local discrepancy） | ω 调制/方波 | **减弱不破坏（min 0.016）** |
| R₃（phase regularity） | 未攻击 | **未知——下一步** |

## 下一步
- (a) 攻击 R₃（相位结构——频率差集的负部分——直接构造）
- (b) 进入 BM/de Branges（R₂ 与 BM 重合点——sine-type regularity）
- (c) 唐先生指示
