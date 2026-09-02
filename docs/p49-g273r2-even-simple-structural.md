# P49-G2.7.3-R2：QW even-simple 结构性审计（唐先生定稿——μ₊<μ₋ 目标）

> 2026-09-02 14:00 · 唐先生 R2 推进 · QW-specific variational theorem

## 关键纠正
- **even-simple = sector ordering（μ₊ < μ₋）+ even-sector simplicity（μ₊ simple）**——非单纯"最小在 even"
- Section 5 矩阵：T_ij = {a_i (i=j), (b_i−b_j)/(i−j) (i≠j)}——divided-difference 型——a_{−j}=a_j, b_{−j}=−b_j——Z₂ 对称——**非经典 Perron matrix——"Toeplitz/CF 直接给最小向量 even"降级为"尚未成立的候选机制"**

## ① Z₂-grading 能证明什么
- [T,γ]=0 ⟹ T = T₊ ⊕ T₋——特征向量可选 parity——**PASS**
- **只能给 Spec = Spec(T₊) ∪ Spec(T₋)——不能给 λmin(T₊) < λmin(T₋)——Z₂-symmetry ⟹̸ even ground state——结构性 No-Go**（反例：T=diag(2,1), γ=diag(1,−1)——commutation only gives parity decomposition, not parity ordering）

## ② QW 的真正优势
- divided-difference operator with parity constraints——**问题 = QW-specific variational inequality（非泛泛 Z₂-symmetric matrix）**

## ③ 精确 theorem target
- μ₊(λ,N) = inf_{f∈E_N⁺,‖f‖=1} QW(f,f)——μ₋ 同理——λmin(QW) = min(μ₊, μ₋)
- **G2.7.3-E：μ₊ < μ₋——G2.7.3-S：dim ker(QW − μ₊I) = 1——μ₊<μ₋ ∧ μ₊ simple ⟹ QW even-simple**

## ④ simple 的路径（未必 Perron-Frobenius）
- 若 T₊ 属 strictly totally-positive/oscillatory/irreducible——给简单谱——**但 divided-difference (b_i−b_j)/(i−j) 不足推 total positivity——需验证 b_i 是否 strict convex/concave/Chebyshev/Pick/moment structure——真正可攻击入口**

## ⑤ PW_λ 不可转移
- PW_λ: simple-even proven——**非 PW ⟹ QW**——PW = positive control / model analogue（保持）

## ⑥ Section 8 原文确认
- missing step 第一项 = QW_λ^N 最小特征值 simple + 特征函数 even——三个 feasibility indications（PW simple-even/QW 极小特征值 PW 相关/higher eigenfunctions 接近）
- **CCM 自己没把 simple-even 归约成已知 Toeplitz theorem——不能说"CF 很可能已解决 simple-even"——正确：CF/self-adjoint machinery 解释"一旦获得 even-simple eigenvector 就能构造自伴谱"——未给 QW even-ground-state theorem**

## ⑦ Krein-Rutman route = LIVE but unproved
- 需构造 K = cI − QW——证 K ≥ 0 强正（cone）——非自动——方向问题（论文用最小特征值——PF 方便控制最大/谱半径）

## ⑧ 搜索目标升级（候选按优先级）
- **A. Reflection-improving variation**：对 odd f 构造 even g——‖g‖=‖f‖——QW(g,g) < QW(f,f) ⟹ μ₊<μ₋（最直接变分证明）
- **B. Rearrangement/symmetrization**：f ↦ f^♯ even——QW(f^♯,f^♯) ≤ QW(f,f)——严格不等号对 odd 成立 ⟹ 同时解决 ordering
- **C. Cone/Perron**：K = cI − QW 强正（even cone）——同时给 μ₊ simple + μ₊<μ₋
- **D. Total positivity/oscillatory**：T₊ STP/oscillatory——给 simple——需另证 μ₊<μ₋——主要解决 S 不自动解决 E

## ⭐ P49-G2.7.3-R2 判定（OPEN — QW-specific variational theorem not yet found）
| 子项 | 状态 |
|---|---|
| QW_λ^N 对象确认 | ✓ |
| Real symmetric | ✓ |
| Z₂-grading | ✓ |
| even/odd block decomposition | ✓ |
| Z₂ ⟹ even ground state | ✗ No-Go |
| ordinary Toeplitz/PF shortcut | ✗ 未成立 |
| PW_λ positive control | ✓ 不可转移 |
| QW-specific divided-difference structure | ✓ |
| even-sector simplicity | OPEN |
| even-vs-odd ordering | OPEN |
| simple-even | OPEN |
| 论文自身是否已证明 | 明确没有 |

## 最重要推进
- G2.7.3 从模糊问题"为什么最小 eigenvector 是 even？"压缩成具体二择：**μ₊ < μ₋** 和 **μ₊ simple**
- 已知道：Z₂ 只解决 sector decomposition 不解决 ordering——PW 只 positive control——普通 Toeplitz/CF 不能替代 QW variational comparison
- **下一步：从 Section 5 的 a_n/b_n 显式公式出发——尝试证明 μ₊(QW) < μ₋(QW) 或构造反例/障碍——若 inequality 严格推出——G2.7.3 从 missing step 进 theorem territory——若不能——证明为什么 Z₂ + divided-difference 不足**
