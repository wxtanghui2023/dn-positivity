# P49-G2.7.3：QW_λ simple-even 严格谱理论审计——第一轮

> 2026-09-02 13:58 · 唐先生 G2.7.3 指示 · 正性/PF/Krein-Rutman/Z₂-grading 审计

## 对象确认（arXiv 2511.22755 正文）
- **QW_λ^N = Weil quadratic form 在 E_N 上的限制**——E_N = E_N(λ) = D_log^(λ)（区间 [λ⁻¹, λ] 上 scaling operator——periodic 边界）的 2N+1 个最小绝对值特征值（≤ Nπ/log λ）特征函数张成的空间——区间外延 0
- **需验证：ε_N = min Spec(QW_λ^N) simple + 特征函数 "even"（u ↦ u⁻¹ 对称下不变）**
- **δ_N ∈ E_N = Dirichlet kernel 的表示向量**（逼近区间边界求值）
- **Theorem 1.1（= Theorem 5.10）**：simple-even 假设下——D_log^(λ,N) = D_log^(λ) − |D_log^(λ)ξ⟩⟨δ_N| self-adjoint（E'_N ⊕ E_N^⊥——E'_N = E_N/ℂξ——内积 = QW_λ^N − ε_N⟨|⟩ 限制）——det_reg(D_log − z) = −iλ^{−iz}ξ̂(z)——**ξ̂ entire——所有零点在实轴且 = 谱**
- 数值：p ≤ 13 得前 50 零点——误差 2.5×10⁻⁵⁵（第一）到 ~10⁻³（第五十）——偶然概率 ~10⁻¹²³⁵
- **结构观察**：E_N 基 = D_log^(λ) 低特征函数（log 坐标下指数模式）——even（u ↦ u⁻¹——log 坐标反射 x ↦ −x）= 偶 Fourier 模式（cos）——odd = sin 模式

## ① 可用机制初步审计
**Z₂-grading（u ↦ u⁻¹——log 反射）**：
- 若 QW_λ^N 与 Z₂ 交换——E_N 分解 even/odd——谱分块
- **⚠️ 但——Z₂ 交换只保证"谱分解为 even/odd"——不保证"最小特征值在 even 子空间"**（最小可能落 odd）——需额外论证

**正性/Perron-Frobenius/Krein-Rutman**：
- 若 QW_λ^N 限制在 even 子空间是"不可约正算子"（保持锥）——Krein-Rutman 给 simple 主特征值 + 正特征向量
- 论文引用的 Carathéodory-Fejér/Toeplitz 结构（bib [7]——"large class of functions whose zeros are on critical line due to selfadjointness of relevant matrices"）——暗示 Toeplitz 正定结构——**正性路径可能可用——但——需 QW_λ^N 的矩阵显式 + 锥结构验证**

**PW_λ（prolate-wave——Slepian）类比**：
- PW_λ 的 simple-even 已知（prolate spheroidal wave functions——Slepian 理论——positive control）
- **⚠️ QW ≠ PW——论文第 8 节说二者通过 information theory 连接（bib [3]）——但——QW 的 simple-even 不是 PW 的推论**

## ② 结构观察（E_N 的 even/odd 分解）
- E_N = D_log^(λ) 低特征空间——log 坐标指数模式 e^{2πik u/log λ} 类——even = cos 模式（k 与 −k 对称组合）——odd = sin
- QW_λ^N 的矩阵——由 Weil 形式给出（论文 2.2 节——q(U_m, U_n)(y) = [sin(2πm|y|/L) − sin(2πn|y|/L)]/[π(n−m)]——奇偶结构可见）
- **⚠️ 需论文 Section 5/6 的 QW_λ^N 矩阵显式 + Section 8 的 missing steps 精确定义**（HTML 获取被截断——750KB 限制——未获 Section 5/8）

## ⭐ G2.7.3 第一轮判定
- **对象定义确认**（QW_λ^N = Weil 形式在 E_N 限制——simple-even 是 Theorem 1.1 假设——论文自列为未证）
- **可用机制初步**：Z₂ 交换（可能——需验证——但不自动给"最小在 even"）——Krein-Rutman（正性路径——Toeplitz 结构暗示——需矩阵显式）——PW 类比（positive control——非 QW 推论）
- **⚠️ 诚实**：第一轮 = 对象确认 + 机制地图——**无法闭合**——需：①论文 Section 5（QW_λ^N 矩阵显式——Z₂ 交换性——正性）②Section 8（missing steps 精确定义——为什么 simple-even 难）——**建议定向获取论文 Section 5/8（或 PDF 全文搜索 QW/simple/even/missing）**
- **初步判断**：simple-even 的"最小特征值在 even 子空间"是核心难点——Z₂ 交换 + 正性（若 QW 在 even 子空间正定且 odd 子空间"更大"的特征值——需特征值比较）——**可能需"even 子空间的主特征值 < odd 子空间的主特征值"的严格比较——这是变分问题（论文的 variational 层——G2.7.3 属 (I) variational/eigenvector identification）**

## 下一步候选
- (a) 定向获取论文 Section 5/8（QW 矩阵/Z₂/正性/missing steps——完成 G2.7.3 审计）
- (b) 接受 G2.7.3 第一轮（对象确认 + 机制地图——需论文细节闭合——"simple-even 的 even 侧最小性"是核心变分难点）
- (c) 唐先生指示
