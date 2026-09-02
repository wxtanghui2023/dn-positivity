# P38-G1.5：Finite Euler-Rigidity Lemma——单 prime 第一层

> 2026-09-02 11:00 · 唐先生 G1.5 指示 · 有限 Euler 刚性 · 1-prime 层

## 框架（唐先生）
- **修正**：P38-G1 不能判定 H¹=0——"可延拓 v_p"可能偷带零点——**问：Euler-locality + FE 是否本身刚性？**
- **G1.5**：L_v = ζ·∏_{p∈S}D_p——F_v = Λ_v/Λ——FE ⟹ F(s)=F(1−s)（无零点）
- **单 prime 第一道 theorem**：z=p^{−s}——s↦1−s ⟹ z↦1/(pz)——R(z)=R(1/(pz))
- **Lemma 候选**：F(s)=∏R_p(p^{−s})——(1) F→1 (2) 延拓 (3) FE (4) 无额外 archimedean——⟹ F≡1
- **反陷阱**：H¹_finite=0 不能推 H¹_global=0（escape——P28-A）——H¹_finite vs H¹_∞ 两级
- **指示**：先做 1-prime → finite-prime → arbitrary finite-support 三层

## ⭐ 单 prime 解析证明（5 步——严格）
**定理：F(s) = R(p^{−s})——R 非零有理——FE（F(s)=F(1−s)）——F(+∞)=1——Λ_v 整（completed L）——⟹ F ≡ 1**
1. **FE ⟺ R(z) = R(1/(pz))**（z=p^{−s}——s↦1−s ⟹ z↦1/(pz)——T 对合）
2. **T 对合 + z·T(z)=1/p（常数）⟹ R ∈ ℂ(z)^T = ℂ(z+1/(pz))**（Lüroth——基本不变量是"和"）——R(z) = H(z+1/(pz))
3. **Λ_v 整（completed L 标准）⟹ D_p=F 无极点 ⟹ R 无极点 ⟹ R 多项式**
4. **R 多项式 + R(z)=R(1/(pz)) ⟹ R 常数**（z→0：R(1/(pz)) 有极点除非常数——矛盾）
5. **R(0)=1（F(+∞)=1）⟹ R≡1 ⟹ F≡1 ∎**

## 亚纯版本——反例存在（数值确认）
- R(z) = (z+1/(pz)+c)/(z+1/(pz)+d)——非平凡（c≠d）——**FE ✓（数值——差 ~1e-26）——F(+∞)=1 ✓——Euler normalization ✓**
- **但——有极点**（分母 pz²+dpz+1=0——p=2,d=0：z=±i/√2——s_pole=0.5±2.27i）——**Λ_v 不整（不是 completed L——被"整性"排除）**

## ⭐ 判定
- **整版本（Λ_v 整——completed L 标准）：F≡1——Lemma 成立（5 步证明）——P38 的第一个 zero-free rigidity theorem 候选（单 prime）**
- **亚纯版本：反例存在——但——破坏 completed L 整性（不是合法 L 变形）**
- **"整性"是 Lemma 的关键条件（completed L 标准性质——合理要求）**
- **H¹_finite 单 prime = 0（局部版本初步成立）**

## ⚠️ 诚实
- "整性"是更强的解读（唐先生 Lemma 条件 2 只说"适当区域"）
- 亚纯反例说明：不要求整——Lemma 假（但——变形不是合法 completed L）
- 多 prime（有限 S）和 H¹_∞（escape）未做

## 下一步候选
- (a) 多 prime：唯一分解论证（F=∏R_p(p^{−s})——FE+整 ⟹ F≡1?——预判：唯一分解成立则推广）
- (b) H¹_finite 完整判定（单 prime ✓——多 prime ?）
- (c) 唐先生指示
