# P49-G2.7.4：Limit Identification Wall——L0-LF 定理级审计（第一轮）

> 2026-09-02 15:35 · 唐先生接口设计 · CCM determinant 路线逐项审计

## G2.7.4 框架（唐先生定义）
- **目标**：F_{λ,N}(z) = C_{λ,N}(z)·det_reg(D_{λ,N}−z) → locally uniformly Ξ(z)——非"特征值收敛"
- **Limit-Rigidity Transfer Theorem**（目标形式）：F_j ∈ O(ℂ)——Z(F_j) ⊂ ℝ ∀j——F_j → Ξ locally uniform ⟹ Z(Ξ) ⊂ ℝ ⟹ RH（+ Ξ(s) = ξ(½+is) 对称性）
- **六层**：L-A 对象（F entire）——L-B 归一化（C 消除 ambiguity）——L-C 函数（F → Ξ compact-open——最重要）——L-D 谱（Z(F) = σ(D)）——L-E 有限刚性（σ ⊂ ℝ）——L-F 联合极限（合法路径）
- **L0 zero-blind normalization**（C 不偷用 Ξ 零点——防 P42/P48 encoding trap）
- **最低门槛降维**：∃(λ_j,N_j) → (∞,∞)：F_j → Ξ locally uniformly（非 uniform double-limit——每 F_j 已有实零点——存在单路径可能足够）

## CCM 论文已确认内容（审计基础）
- **Theorem 5.10(ii)**：det_reg(D_log^(λ,N) − z) = **−iλ^{−iz}ξ̂(z)**（simple-even 下——定理）
- **Theorem 5.10(iii)**：ξ̂ entire——**Z(ξ̂) = Spec(D_log^(λ,N)) ⊂ ℝ**（simple-even 下——定理）
- Theorem 1.1(i)：D self-adjoint（simple-even 下——定理）
- 第 7 节 Lemma 7.3：k_λ（prolate 逼近）的 Fourier λ→∞ 一致收敛到 Ξ（**k_λ 路线——非 det_reg 路线**）
- 第 7 节开头：det_reg 归一化 → Ξ 作为"strategy"
- 第 8 节：missing steps（simple-even + k_λ 逼近 ξ_λ——零点收敛）

## L0-LF 逐项审计
| 层 | 状态 | 依据 |
|---|---|---|
| L0 zero-blind | ⚠️ 部分 | λ^{−iz} 因子 zero-blind（scaling）✓——完整归一化 C（e^{a+ibs} 类）需核验 |
| L-A F entire | ✓ conditional | ξ̂ entire（Thm 5.10iii——simple-even 下）——C 选择需保 entire |
| L-B 归一化 | ⚠️ OPEN | det_reg = −iλ^{−iz}ξ̂ 明确——但 →Ξ 的归一化 C 是 strategy 非定理 |
| **L-C 函数收敛** | **✗ OPEN（核心缺口）** | **det_reg 路线的 F → Ξ compact-open 未建立——Lemma 7.3 是 k_λ 路线（不同对象）——论文只有 numerical + strategy** |
| L-D 谱层 | ✓ conditional | Z(ξ̂) = Spec（Thm 5.10iii——simple-even 下） |
| L-E 有限刚性 | ✓ conditional | Spec ⊂ ℝ（self-adjoint——Thm 1.1——simple-even 下） |
| L-F 联合极限 | ✗ OPEN | Lemma 7.3 是 λ→∞（k_λ 单参数）——det_reg 的 (λ,N) 联合路径未建立 |

## ⭐ 审计发现
1. **CCM 的 det_reg ↔ ξ̂ 关系是定理**（Thm 5.10——strong——但 conditional on simple-even）
2. **ξ̂ entire + Z(ξ̂) = Spec ⊂ ℝ 是定理**（同）
3. **L-C 是核心缺口**：F_{λ,N} → Ξ 的严格收敛——论文第 7 节 det_reg 路线 = strategy + numerical——**Lemma 7.3 是 k_λ（prolate）路线——不是 det_reg 路线的收敛定理**
4. **L0 需核验**：完整归一化 C 的 zero-blind 性（λ^{−iz} 部分 ✓——其余待查）
5. **L-F 需设计**：联合路径 (λ_j,N_j)——Lemma 7.3 的单参数 λ→∞ 不够
6. **第一次出现真正不可替代新困难的位置 = L-C**（entire-function convergence——det_reg 归一化后到 Ξ）——L-A/L-D/L-E 有定理基础（conditional）——Hurwitz 传递标准——**L-C 的严格证明是 G2.7.4 的真正硬核**

## 判定
- G2.7.4 第一轮审计完成：**CCM determinant 路线的缺口精确定位在 L-C（F → Ξ compact-open）+ L-B（归一化核验）+ L-F（联合路径）——L-A/L-D/L-E conditional PASS——L0 部分 PASS**
- **核心新困难 = L-C**（非 simple-even——非 tail 数值）
- ⚠️ 注意：det_reg 路线与 k_λ 路线是两个不同对象（论文都讨论——但收敛定理只在 k_λ 侧有 Lemma 7.3——det_reg 侧 open）

## 下一步候选
- (a) L-C 深审（det_reg 路线 vs k_λ 路线的关系——论文第 7 节的 det_reg 策略细节——C_{λ,N} 的候选形式——评估 F → Ξ 的可证性——需要论文第 7 节全文精读）
- (b) L0 核验（完整归一化的 zero-blind——从论文公式推导 C 的显式——检查是否含零点信息）
- (c) 唐先生指示
