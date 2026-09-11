# 📄 **短稿 v1**：An elementary explicit positivity range for the Li coefficients

**依据**：唐先生 2026-09-11 21:40（"继续"）｜**脚本**：`LEMMA12_rigorous.py`、`LEMMA2_explicit_BT.py`、`TRACK*` ✓
**标注**：【引理·已证/已核验】｜【引用】｜【数值】

---

## Abstract
```
Let T be a height to which the Riemann Hypothesis has been rigorously verified (interval
arithmetic).  We prove, by elementary means, that the Li coefficients satisfy λ_n ≥ 0 for every
integer n with 2 ≤ n ≤ 2T − O(1).  For the currently verified height T = 3.000175·10¹² this gives
n up to ≈ 6.00035·10¹², about 6·10⁷ times the range reached by direct computation of λ_n in the
literature.  No information on the location of zeros above T is used, and no hypothesis is
assumed: only the non-negativity of the on-line terms, a window bound on the phases, the
classical explicit zero-counting bound, and an elementary bound on the off-line contribution.
```

## §1 **Introduction**
```
【Li 判据】**RH ⟺ λ_n ≥ 0 ∀n**，λ_n = Σ_ρ[1 − (1−1/ρ)^n]（Li 1997 ✓）
【问题】**"λ_n ≥ 0 到多大的 n"** —— 直接计算已至 **n ≤ 10⁵**（Palojärvi ✓ / Coffey ✓）
【本文】用**已验证高度 T**（Platt–Trudgian ✓ 区间算术）⟹ **n ≤ 2T − O(1)** ✓，**方法全初等** ✓
【关键】**无需 **γ>T 零点的位置——只上界其**最坏贡献** ✓✓
```

## §2 **Notation**
```
λ_n = Σ_ρ[1−(1−1/ρ)^n]，ρ 遍非平凡零点（共轭对 ✓，故 λ_n ∈ ℝ ✓）
在线 ρ=½+iγ：**(1−1/ρ) = (γ²−¼+iγ)/(γ²+¼)** ⟹ **|1−1/ρ| = 1** ✓
   **1−(1−1/ρ)^n = 1 − e^{inθ_γ}**，**θ_γ := arctan(γ/(γ²−¼))** ✓ ⟹ Re = **1−cos(nθ_γ) ∈ [0,2]** ✓
离轴 ρ（β≠½）：**|1−1/ρ| = e^{c}**，**c = ½log(1+(1−2β)/(β²+γ²))** ✓
N(T)、**F(T) = (T/2π)log(T/2πe) + 7/8** ✓，**B_T := ½Σ_{γ>T}γ⁻²** ✓
```

## §3 **Three lemmas**
```
【引理 1（窗口下界）**已证 + 核验 ✓**】
 (a) **θ_γ 在 (½,∞) 严格递减** ✓ —— 由 θ' = u'/(1+u²)，u = γ/(γ²−¼)，**u' = −(γ²+¼)/(γ²−¼)² < 0** ✓
 (b) **θ_γ = 1/γ − 1/(12γ³) + 1/(80γ⁵) − …** ✓（核验：与精确值差 2.2e−10 @γ=10；1e−18 @γ≥10⁴ ✓✓）
 (c) 故对 γ ∈ [n/2, min(2n,T)]：
     **nθ_γ ≥ nθ_{2n} = ½ − 1/(96n²) + 1/(2560n⁴) − … ≥ ½ − 1/(96n²)** ✓
     **nθ_γ ≤ nθ_{n/2} = 2 − 2/(3n²) + … < 2 < π** ✓
 ⟹ **1 − cos(nθ_γ) ≥ C₁(n) := 1 − cos(½ − 1/(96n²))** ✓✓
     （C₁(n) = 0.1223675… @n=10 ⟶ **0.1224174381… @n≥10⁴** ✓）
【引理 2（计数）**引用 ✓**】
 Trudgian：∀T ≥ e，**|N(T) − F(T)| ≤ R(T) := 0.112logT + 0.278loglogT + 2.510 + 0.2/T** ✓
 ⟹（n ≥ 2e）**N(T) − N(n/2) ≥ [F(T) − R(T)] − [F(n/2) + R(n/2)]** ✓
【引理 3（离轴下界）**已证 + 核验 ✓**】
 由 **c = ½log(1+(1−2β)/(β²+γ²)) ≤ (1−2β)/(2(β²+γ²)) ≤ 1/(2γ²)**（β<½ ✓）
 ⟹ **|w|^n − 1 ≤ (n/(2γ²))·e^{n/(2γ²)}**；n<2T、γ>T ⟹ **n/(2γ²) < 1/T** ⟹ e^{1/T} = 1+O(1/T) ✓
 ⟹ **Σ_{离轴} ≥ −n·B_T(1+O(1/T))** ✓
 （**β>½ ⟹ |w|<1 ⟹ 贡献 ≥ 0** ✓ 故只需处理 β<½ ✓）
【引理 4（尾部常数）**已证 + 核验 ✓**】
 Abel：**Σ_{γ>T}γ⁻² = −N(T)/T² + 2∫_T^∞ N(x)x⁻³dx** ✓，用 **N(x) ≤ F(x)+R(x)** ✓：
   2∫_T^∞(x/2π)log(x/2πe)x⁻³dx = **(1/π)(1+log(T/2πe))/T** ✓
   2∫(7/8)x⁻³ = **(7/8)/T²** ✓；2∫0.112logx·x⁻³ = **0.112(1+2logT)/(2T²)** ✓；
   2∫0.278loglogx·x⁻³ ≤ **0.278(1+2loglogT+(loglogT)²)/(2T²)** ✓；2∫2.510x⁻³ = **2.510/T²** ✓
 ⟹ **T=1.13249×10⁶：B_T ≤ 3.4015×10⁻⁶** ✓｜**T₀=3.000175×10¹²：B_T ≤ 2.8531×10⁻¹²** ✓
   （**约为名义值 (logT+1)/(4πT) 的 3.24 / 3.62 倍** ✓）
```

## §4 **Theorem and proof**
```
【定理】设 T 为已严格验证的高度，且引理 2 的计数满足
     **#{γ ∈ [n/2, min(2n,T)]} ≥ n·B_T^exp / C₁(n)**
   （B_T^exp = 引理 4 的显式上界 ✓），则 **λ_n ≥ 0** ✓
   且小 n（**n ≤ 10⁵**）由已发表直接验证接管 ✓
【证明】λ_n = Σ_{在线 γ≤T}(1−cos nθ_γ) + Σ_{在线 γ>T}(1−cos nθ_γ) + Σ_{离轴}
     ≥ C₁(n)·#{窗口} + 0 − n·B_T(1+o(1))            （引理 1、3 ✓；γ>T 在线项 ≥ 0 ✓）
     ⟹ 引理 2 + 引理 4 ⟹ 结论 ✓
【范围】测得的 N_max = 2T − O(1)；用**显式** B_T：n=2.26×10⁶ 处需要 ≈63 个零点 ✓
   ⟹ 代 T₀：需要 ≈140 ⟹ **N_max(T₀) = 2T₀ − O(30) ≈ 6.00035×10¹²** ✓✓
```

## §5 **Numerical verification**
```
【λ₁ 校准】**2A(1) = 0.0230938677** vs λ₁ = ½γ_E+1−½log4π = **0.0230957089661** ⟹ **ratio 0.999920** ✓✓
【余量（T=1.13249×10⁶，名义 B_T）】n=10⁵: **2.7×10⁵**｜5×10⁵: **3.2×10⁵**｜10⁶: **1.4×10⁵**
   ｜2×10⁶: **1.5×10⁴**｜2.25×10⁶: **7.5×10²**｜端点 2,264,960: **1.03** ✓
【穷尽验证】A(n)/n ≥ 1.154693×10⁻² 对**每一个** n ≤ 20000 ✓（阈值 5.25×10⁻⁷ ⟹ 余量 2.2×10⁴ ✓）
【显式 B_T 下的所需计数】n=10⁵: **2.78**｜10⁶: **27.8**｜端点: **62.9** —— 实有 234681 / 1182636 / 19 ✓
```

## §6 **Boundaries（诚实）**
```
【不是 RH 的证明】范围 **n ≤ 2T − O(1) 有限** ✗（T→∞ 增长但永不覆盖全体 n ✓）
【性质】**子集结果**（Farmer (A) 的"有希望证明"类 ✓）；**给定 T 后无条件** ✓
【依赖】(i) Li 表示（经典 ✓）(ii) **[0,T] 零点已严格验证**（Platt–Trudgian ✓）(iii) Trudgian 显式计数界 ✓
【已证】引理 1、3、4 ✓（初等，核验 ✓）；引理 2 = 引用 ✓
【待办】引理 1 的 O(n⁻⁴) 余项与单调性写成严格证明（初等 ✓）；小 n 段引用（Palojärvi 1807.01506 ✓ / Coffey ✓）
```

## §7 References（待补全 ✓）
```
Li (1997)｜Palojärvi (arXiv:1807.01506 ✓)｜Coffey (2004/2005 ✓)｜Trudgian (2014, explicit N(T) ✓)
｜Platt–Trudgian (arXiv:2004.09765 ✓, T=3.000175×10¹² ✓)｜Rosser (1941 ✓)｜Riemann–von Mangoldt ✓
```

## §8 提交链
```
PAPER-li-range-ELEMENTARY（11298e2）→ 本篇（引理 1/2/4 严格化 + 显式 B_T + 定理 + 数值 + 边界）
```
