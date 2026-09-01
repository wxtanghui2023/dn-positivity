# P5.11-1：Adversarial Theorem 测试——相位工程——构造失败

> 2026-09-01 · 唐先生指令 · 先做 adversarial theorem（不做更多正面数值）

## 任务
构造满足最强 RvM/local regularity 条件（N(T) = N_RvM(T) + o(T log T) + 最小间距 + 渐近局部间距）但 inf_θ F(θ) = 0 的配置——沿稀疏 θ_k 子序列。

## 测试结果
| 构造 | min/bohr | 判定 |
|------|:--:|:--:|
| 基线 RvM | 0.0453 | — |
| 随机扰动（±2%） | 0.0456-0.0458 | ≈ 基线（不降低） |
| block 交替（±5%） | 0.0463 | ≈ 基线 |
| block 交替（±10%） | 0.0493 | 略大 |
| 成对镜像（相位 π） | 0.269 | 增强（破坏 RvM 结构） |
| 大范围 [0,200] | 0.0454 | 无深零（稳定） |
| 3-block 优化（非法） | 1e-30 | **伪影**（shifts=1.6e16——无限平移——排除） |

## ⭐ 结论
**在合法扰动（保持 RvM 密度/间距——o(1)）内——相位工程无法制造深零——min/bohr 稳定 ≥ 0.045（甚至略增强）**：
1. **自然深零**：不存在（[0,200] 大范围——覆盖多周期——min/bohr 稳定 0.045）
2. **合法扰动**：不能降低（±2/5/10%——都 ≥ 基线）
3. **成对镜像**：增强（0.269——镜像破坏 RvM 的"准随机相位"——反而增强 coercivity）
4. **非法优化**：伪影（排除——shifts 天文数字）

**RvM-calibrated 配置的 arithmetic-direction coercivity 数值上稳定——抵抗相位工程**——**adversarial 构造失败**。

## 按唐先生框架——进入 BM/de Branges/sampling 理论
**adversarial 构造失败 ⟹ 才值得认真上 BM——寻找真正的 sufficient condition**：
- 问题：**什么是 arithmetic-direction coercivity 的最小充分条件？**
- 候选（BM/de Branges）：sine-type regularity / de Branges 空间 / sampling theory 的 uniform frame bounds
- "接近临界密度时如何得到 uniform frame bounds"（2025 文献）——正是专门研究的问题

## 候选定理（完全脱离 RH——唐先生的改写）
**inf_{Λ∈R} inf_θ ∫_0^∞ e^{−cv}|S_Λ(v+θ)|²dv > 0?**——S_Λ(v) = Σ e^{iγ_j v}/(c−iγ_j)
- A. False：有价值的负结果（Rigidity Gap 扩大）
- B. True：重大结果（独立 harmonic-analysis coercivity theorem）——然后才问 ζ 零点是否满足 R

## 三层正式数学化（唐先生）
1. **F(θ) ≥ 0**：Gram positivity（无条件——严格）
2. **F(θ) > 0**：pointwise nonvanishing
3. **inf_θ F(θ) > 0**：coercivity（**目标**——"phase rigidity"）

**Fourier 化**：F(θ) = Σ a_j ā_k K_c(γ_j−γ_k)e^{i(γ_j−γ_k)θ}——正定 almost-periodic quadratic functional——**"什么时候正定 almost-periodic function 保证严格正下界？"——phase rigidity 问题**

## 七层状态表（唐先生的降级）
| 层次 | 状态 |
|------|:--:|
| Gram positivity | 严格 |
| spacing | 严格/已知 |
| global RvM | 严格/已知 |
| RvM-calibrated model C_arith | **数值** |
| adversarial local-regularity test | **数值（构造失败——抵抗）** |
| general coercivity theorem | **未知** |
| application to ζ zeros | **未知** |
| RH | **完全未触及** |

## 下一步
- (a) 进入 BM/de Branges/sampling 理论——找"uniform frame bound / Riesz bound"的充分条件（接近临界密度的专门问题）
- (b) 尝试证明候选定理（inf_{Λ∈R} inf_θ F > 0——对某 regularity class R）
- (c) 唐先生指示
