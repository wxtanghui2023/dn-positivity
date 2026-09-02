# P47-G2.5：Finite Reciprocity Transgression——第一轮（纯离散）

> 2026-09-02 12:50 · 唐先生 P47-G2.5 指示 · 互反 transgression · 判定规则

## 框架（唐先生）
- **不搜任意 H² ≠ 0**——**让离散算术 reciprocity 本身产生 pair-sensitive obstruction**
- **discretization 必须算术**（不能任意 quantization——不能重新引入 Re s——Gate A 升级）
- **从真正 arithmetic symbols**（Hilbert/residue/power-residue——∏_v(a,b)_v = 1）——**T(a,b) = c(a,b)/c(b∨,a∨)——transgression（duality covariance ≠ invariance）**
- **硬 Gate**：T 不能是 s−Γs 的单变量函数（(3/2)^{s−Γs} 假阳性）——不能依赖人为 reduction
- **两阶段定理**：global realizability ⟹ T(A,A∨) = 1——T(A,A∨) = 1 ⟹ A ≃ A∨（structural）——最后 realization map A(s) ≃ A(Γs) ⟹ s = Γs（injectivity 不能人为）
- **判定规则**：H² = 0 → 杀——T ≡ 1 → 杀——T 只是 s−Γs 函数 → 杀——T 依赖人为 reduction → 杀——reciprocity 只产生 symmetry → 杀——genuine pair obstruction → G2.6

## ① Legendre transgression（∨ = 恒等）
- c(a,b) = (a/b)₂——T(a,b) = (a/b)₂/(b/a)₂ = (−1)^{((a−1)/2)((b−1)/2)}（二次互反律）
- **T 非恒等 ✓（6/30——样本）——非距离 ✓（mod 4 类——算术 wall——不是 |a−b|）——算术 ✓（二次互反律）**

## ② T 的算术性 vs 距离编码
- **T = ±1 离散值——依赖 a mod 4, b mod 4——算术 wall（离散变化）——非距离 ✓**
- **⚠️ 但——"T = 1 的集合"（a ≡ b mod 4 类）——不是"固定 locus"（a = b）——T = 1 允许 a ≠ b（同类 mod 4）**

## ③ 与 pair (s,Γs) 的连接——关键缺口
- **∨ = 恒等时——T(A,A∨) = T(A,A) = 1 恒等——trivial pair——无 obstruction！**
- **∨ 必须非平凡（ℚ(i) 复共轭）——且——"T(A,A∨) = 1 ⟹ A ≃ A∨"需验证**

## ④ ℚ(i) 版本（∨ = 复共轭——范数符号）
- T = 范数互反——**非恒等 ✓（数值初步：8/26）**

## ⭐ P47-G2.5 第一轮判定
- **Legendre/范数互反的 T——非恒等 ✓——非距离 ✓——算术 ✓——"genuine transgression"（二次互反律——非对称部分）——结构存在**
- **但——"pair obstruction"（T(A,A∨) = 1 ⟹ A ≃ A∨——structural theorem）——未验证**——且——"T = 1 的集合"（mod 4 同类）不是固定 locus
- **"∨ 非平凡 + family 结构"是下一步**——"s-连接"（A(s) family——不用 p^{−s} 重新包装）未做（最难）

## 下一步候选
- (a) 验证 T(A,A∨) = 1 ⟹ A ≃ A∨（structural——∨ 非平凡 family——ℚ(i) 共轭对/λ ↦ 1−λ 类）
- (b) 接受第一实验（互反 transgression 结构存在——但——pair obstruction 未建立——P47-G2.5 待定）
- (c) 唐先生指示
