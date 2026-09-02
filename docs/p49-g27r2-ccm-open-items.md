# P49-G2.7-R2：CCM 四 OPEN 项深审（唐先生定稿——依赖图校正）

> 2026-09-02 13:56 · 唐先生 R2 指示 · 两路线校正 · G2.7.3 下一目标

## 0. 依赖图校正
- **不要把剩余问题压缩成单一 F_λ,N → Ξ 桥**——CCM 论文"essential missing steps"有两个且在不同层级
- 严格链条：QW_λ^N →simple-even? D_log^(λ,N) →D=D* Spec(D_log) ⊂ R
- **Theorem 5.10（simple-even 假设下）**：ξ̂_λ,N entire——Z(ξ̂_λ,N) = Spec(D_log^(λ,N)) ⊂ R——严格条件定理
- **两条需同时闭合的路线**：**A. simple-even/eigenvector approximation——B. determinant/Ξ convergence**——G2.7.3/G2.7.4 不是 G2.7.5 的附属项
- 论文第 8 节两个 essential steps：①Weil quadratic form 最小特征值 simple + eigenvector even ②k_λ 足够准确逼近 ξ_λ——得 ξ̂_λ 零点收敛到 ζ 零点

## ① G2.7.3 — Simple-even unconditionality（OPEN——结构性 OPEN）
- Theorem 5.10 假设：ε_N = min Spec(QW_λ^N) simple + eigenvector even——**simple-even ⟹ D_log = D_log*（非 QW ⟹ D_log 无条件）**
- 支持：PW_λ（prolate-wave）所有 λ simple-even——数值 QW_λ 极小特征值强相应——更高 eigenfunctions 数值支持——**都是 feasibility evidence——非 QW_λ 无条件定理**
- **判定：simple-even for PW_λ = positive control——simple-even for QW_λ = unproved——第一个不能用数值替代严格证明的点**

## ② G2.7.4 — Strict spectral identification（OPEN——与 G2.7.3 实际依赖）
- Spec(D_log^(λ,N)) → {γ_n}——numerical evidence——rigorous 未建立
- "谱收敛"须指定拓扑——8 项控制（eigenvalue convergence/multiplicity/ordering/spectral pollution/escape/accumulation/联合极限/truncation uniform control）
- **修正：不是"8 个已被证明缺失的独立定理"——是"严格 spectral-identification proof 至少需处理的审计接口"**
- 依赖：simple-even → well-defined rigid finite model → spectral identification

## ③ G2.7.5 — Determinant → Ξ + 零点控制（OPEN but well-posed——形态最清楚）
- CCM 提出 e^{a+ibs}det_reg(D_log^(λ,N) − s) ⟶ Ξ(s)——若严格建立可用 Hurwitz
- **好消息**：CCM 已证明有限模型 determinant 结构（Theorem 5.10——ξ̂ entire——零点 = 谱——严格基础）——D_λ,N → det_reg → ξ̂_λ,N 有严格基础
- **真 OPEN：ξ̂_λ,N ⟶ Ξ**（或 normalized determinant convergence）
- 防逻辑跳跃：Fn → Ξ ≠ zero-set convergence——需一致收敛（零点区域紧集）+ 极限非恒零——才可用 Hurwitz/Rouché
- **不能说"Hurwitz 未出现所以失败"——CCM 明确把 Hurwitz 作为后续严格闭合路线**

## ④ G2.7.6 — Global O3（OPEN）
- P49 要求：ρ_off ⟹ L(A_ρ) ≠ 0——CCM finite law（D_log = D_log*）独立/fixed/zero-blind ✓——**O3_finite = ✓**
- **O3_global**：law 严格传递到 ζ 完整零集——缺 Ξ = lim F_λ,N + 零点控制——**O3_global = OPEN**

## 核心结论（结构转换）
- **CCM 的缺口不是"再找 rigidity"——是"如何把 finite rigid object 严格传递到 Ξ"——finite coercivity → ? global coercivity**
- **P49 搜索方向结构转换：mechanism search ⟶ limit-transfer audit**
- **CCM 已完成 finite coercive mechanism——global closure 需至少两个独立层面的严格化：(I) variational/eigenvector identification（G2.7.3）(II) analytic/spectral limit identification（G2.7.4/5）——二者共同给出 independent finite rigidity + strict limit transfer ⟹ O3_global ⟹ RH**
- **不要写成"CCM 只剩一个技术缺口"——是两个独立层面的严格化**

## 依赖 DAG
QW_λ^N →simple-even D_λ,N →self-adjoint Spec ⊂ R——↓F_λ,N / Z(F_λ,N) ⊂ R——↘↙ Ξ——↓ RH
- G2.7.3：simple-even——G2.7.4：F_λ,N/spectrum → Ξ/zeros——G2.7.5：det_reg → Ξ + zero control——G2.7.6：global O3
- **G2.7.4 与 G2.7.5 是两条平行 global-identification 路线——非四级线性链**

## 状态表
| 项目 | 判定 |
|---|---|
| A′ provenance wall | PASS — CCM escaped |
| Independent spectral object | PASS |
| Finite self-adjoint rigidity | PASS conditional |
| G2.7.3 simple-even | OPEN |
| G2.7.4 strict spectral identification | OPEN |
| G2.7.5 determinant → Ξ + zero control | OPEN |
| O3 finite | PASS |
| O3 global | OPEN |
| RH implication | OPEN |

## 下一轮（唐先生指示）
- **G2.7.3：直接审计 QW_λ 的 simple-even 是否存在可利用的严格谱理论**——如果正性/Perron-Frobenius/Krein-Rutman/Z₂-grading 结构性结果能无条件关闭——CCM 第一条缺口从"数值 evidence"升级成 theorem——如果不能——精确证明卡在哪
