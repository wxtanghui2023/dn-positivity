# P34-D1*：uniform tail——B_k* 不衰减（R3 倾向）——符号正交性关键未决

> 2026-09-02 · 唐先生 D1* 指令 · 双参数 UC · B_k* = sup_X(|a_k^ren|·M_k)

## ① B_k* = sup_X(|a_k^ren(X)|·M_k(X))
- k=1: 0.153——k=5: 0.050——k=10: 0.028——**k=20: 0.060（回升）**——k=40: 0.055——k=60: 0.042
- **不单调衰减——k≥20 平台 ~0.04-0.06**

## ② Σ_{k>K}B_k*（粗界——Weierstrass M-test）
- Σ_{k>0}=3.48——Σ_{k>40}=1.17（下降——但——仍大——尾部 k>60 未计）

## ③ B_k* 衰减判定——log-log 斜率正（不衰减！）
- k=5..20: +0.138——k=10..40: +0.486——k=10..60: +0.227
- **⭐⭐ B_k* 不衰减（斜率正——k 增大甚至回升）——"O(k^(−1−δ))（R1）"排除——"O(k⁻¹)（临界）"不成立——"不趋零（R3）"倾向——粗界 Weierstrass M-test 失败——R1（粗界版）排除**

## ④ 符号振荡——a_k^ren 随 X 变号（正交性利用可能）
- k=1: 变号 2 次（9 个 X）——k=5: 6 次——k=10: 4 次
- **变号频繁——"实际 T_K(X)（含符号——正交性抵消）可能远小于粗界 Σ|a^ren|M_k"——唐先生预警"必须利用符号振荡/正交性——不能只用 triangle inequality"——正是这里！**

## ⭐ 判定——R3 倾向（粗界失败）——但——符号正交性是关键未决
- **粗界（Σ|a^ren|M_k）发散/不趋零（B_k* 不衰减）——Weierstrass M-test 失败——"R1（粗界版）"排除**
- **但——B_k* 是"绝对值 sup"——实际 T_K(X)（含符号——a_k^ren(X) 随 X 变号）可能远小于粗界（正交性抵消）**
- **需测"实际 T_K（含符号）vs 粗界"——若实际 T_K 远小（正交性）——R1（正交版）可能——若实际 T_K 停滞——R3 确认**

## ⚠️ 诚实边界
- Kmax=60——X≤10⁶——B_k* 的 sup 数值（有限 X 集）——k→∞ 渐近需分析
- "实际 T_K（含符号）"未测（下一关键——正交性判定）
- R3 ≠ R2（R3 是"fixed-mode renormalization does not control the high-mode tail"——不意味着存在非零 canonical operator）

## ⭐ 封档句（唐先生）
**"The feature-growth obstruction is absent for w=e^-x/2, but canonical trivialization remains a uniform high-mode question. Fixed-mode renormalization together with slow feature growth does not imply operator convergence. The decisive criterion is uniform tail control in the joint (X,k)-limit."**
**顺序：D1*（uniform tail）→ D3（form/operator convergence）→ D4（R1/R2/R3）→ Problem II**

## 下一步
- (a) 实际 T_K(X)（含符号——正交性）vs 粗界——R1（正交版）vs R3 判定
- (b) 唐先生指示
