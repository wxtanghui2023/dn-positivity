# P47-G2.5.2：R2 决定性审计——q^{-1}(1) = Fix(∨)?

> 2026-09-02 12:53 · 唐先生 P47-G2.5.2 指示 · FRS · R2 决定性 Gate

## 框架（唐先生）
- **Legendre 修正**：T(a,b) = −1 ⟺ a ≡ b ≡ 3 (mod 4)——T = 1 ⟺ 至少一个 ≡ 1 (mod 4)——**低分辨率 reciprocity wall——不是同类关系**
- **结构性测试**：q(A) = T(A,JA)——**需要 q(A) = 1 ⟺ A ∈ Fix(J)——orthogonality ≠ equality（q(A) = 1 通常只是"正交"——不是"同一对象"——离散版 β-wall）**
- **FRS Gate**：ker[A ↦ T(A,A∨)] = Fix(∨)——第 5 条决定性（kernel 恰好是 fixed locus——不是 arithmetic congruence class）
- **Legendre 立即 FAIL FRS**（信息量不足以分离 ∨-orbits）
- **ℚ(i) 值得继续**：Gal(ℚ(i)/ℚ) = {1, ∨}——A∨ = Ā 是真实算术 involution
- **R1/R2/R3 三 Gate——R2（q^{-1}(1) = Fix(∨)）是决定性 Gate**

## ① F₂² 系统搜索（标准交替 pairing——线性 involution）
- 4 个线性 involution——**R2 全部通过（4/4）**——（F₂² 太小——标准辛 pairing 的对称性使 R2 通过）

## ② 唐先生的 J'（(x₁,x₂)↦(x₁,x₁+x₂)）详细检查
- Fix(J') = {(0,0),(0,1)}——**q^{-1}(1) = {(0,0),(0,1)} = Fix(J')——R2 通过 ✓**（我算的——这个 J' 实际通过——唐先生可能指别的组合/更高维）

## ③ F₂³ 采样（300 线性 involution——标准辛 pairing）
- **R2 通过：102——R2 失败：198（66%）**
- **⭐ "一般（随机）involution + 标准 pairing"——R2 大量失败——orthogonality ≠ equality 确认（离散 β-wall 的实证）**

## ④ ℚ(i) 最小尝试（∨ = 复共轭——Galois）
- Fix(∨) = 实高斯整数——**范数 Legendre 配对：N(Ā) = N(A)——T(A,Ā) = 1 恒等——杀（R2 平凡——无信息）**
- **"范数"配对对共轭不变——需"非范数"配对（真实 ℚ(i) Hilbert/四次互反符号 (A/B)₄——Gaussian primes——四次互反律有非平凡 transgression——实现复杂——下一步）**

## ⭐ P47-G2.5.2 第一轮判定
- **F₂³ 采样确认"一般 pairing + 一般 involution 的 R2 结构性失败"（66%——orthogonality ≠ equality）**
- **但——"Galois ∨（共轭）"是"特殊 ∨"（算术的——非随机）——"真实 ℚ(i) pairing（四次互反——非范数）"是决定性测试——未完成**
- **ℚ(i) 范数配对对共轭不变（T 恒等——杀）**

## 下一步候选
- (a) **ℚ(i) 四次互反 transgression**（(A/B)₄——Gaussian primes——T(A,Ā)——q^{-1}(1) vs Fix(∨)——R2 决定性测试——实现较复杂）
- (b) 接受第一轮（一般 pairing R2 失败——orthogonality ≠ equality——Galois 特殊情形未测——P47-G2.5.2 待定）
- (c) 唐先生指示
