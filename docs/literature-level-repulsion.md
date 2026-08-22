# 文献综述：能级排斥与无条件对关联结果

> 日期: 2026-08-22 11:30
> 目的: 评估"弱能级排斥的无条件结果"能否支撑 r(n) = O(1) 证明
> 结论: ✅ 找到无条件 Montgomery 定理 + Gallagher-Mueller 零排斥；❌ 但不足以直接控制一阶量 ∫f dS

---

## 1. 关键文献

### 1.1 BGSTB24 — 无条件 Montgomery 定理（最重要）

**引用**: S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya, C. L. Turnage-Butterbaugh, "An unconditional Montgomery theorem for pair correlation of zeros of the Riemann zeta-function", Acta Arith. 214 (2024), 357–376. DOI: 10.4064/aa230612-20-3

**定理（无条件）**：对 r ∈ L¹(R) 实偶函数，支撑在 [−1,1]，在 α=0 Lipschitz：
$$\sum_{\rho,\rho'} \hat{r}\left(\frac{i(\rho-\rho')\log T}{2\pi}\right)W(\rho-\rho') = \frac{T}{2\pi}\log T\left(r(0) + 2\int_0^1 \alpha r(\alpha)d\alpha + O\left(\frac{1}{\sqrt{\log T}}\right)\right)$$

**应用**：若 γ ∈ (T^{3/8}, T] 的零点满足 |β−½| < 1/(2logT)，则 ≥61.7% 零点简单（无条件，无需 RH！）
- 原 Montgomery 定理需 RH；BGSTB24 用 Selberg/Fujii 方法去掉了 RH
- 关键：素数侧评估无条件（Dirichlet 多项式均值），零点侧读法用线性代数（Sylvester 惯性定律）替代 RH

### 1.2 Gallagher-Mueller 零排斥（无条件）

**引用**: P. X. Gallagher, J. H. Mueller, "Primes and zeros in short intervals", J. reine angew. Math. 303/304 (1978), 205–220

**结果（无条件）**：对 0<λ≤√L（L = (1/2π)logT）：
$$\mathcal{N}^\circledast(T) + \frac{2}{\lambda}\int_0^\lambda \mathcal{N}(\alpha)d\alpha = \frac{TL}{\lambda} + \frac{\log(2+\lambda)}{\pi^2\lambda} + O\left(\frac{\sqrt{\log(2+\lambda)}}{\lambda}\right)$$

用平凡下界 N⊛(T) ≥ N(T) = TL + O(T) → **近距离零点排斥**（无条件）。

### 1.3 Goldston-Lee-Schettler-Suriajaya 2026 — PCC ⟹ 100% 简单+临界线

**引用**: arXiv:2503.15449（2026-08-11 版）

**定理 1**: 假设 PCC（对关联猜想），则渐近 100% 零点简单且在临界线上。
- Gallagher-Mueller 方法不依赖 RH
- PCC 对垂直分布 → 水平分布信息（新）
- 相关: arXiv:2501.14545（BGSTB 对关联 I）、arXiv:2508.10857（Alternative Hypothesis）

### 1.4 其他相关

- Aryan (2022): Landau-Gonek 公式扩展（J. Number Theory 233, 389–404）
- Inoue (2024): Selberg r-间距结果证明（Bull. LMS）
- Simonič-Trudgian: 无条件大间距 > 3.18（无穷多）

---

## 2. 对 r(n) = O(1) 的可应用性评估

### 2.1 需要控制的量（一阶）

$$r(n) = \int_0^\infty f_n(t)\,dS(t), \quad f_n(t) = 4\sin^2(n\theta(t))$$

这是 **S(t) 的线性泛函**（一阶量）。

### 2.2 无条件结果给什么（二阶/近距离）

| 结果 | 类型 | 能否控制 ∫f dS？ |
|:---|:---|:---|
| BGSTB24 无条件 Montgomery | 对关联（二阶）| ❌ 不是一阶量 |
| Gallagher-Mueller 零排斥 | 近距离零点数上界 | ⚠️ 间接（抑制小间距）|
| Selberg ∫S²dt ~ TloglogT | 二阶矩 | ❌ Cauchy-Schwarz 太粗 |
| S(T) = O(logT) | 逐点界 | ❌ 积分后 O(log n) |

### 2.3 关键结论

**无条件对关联定理不能直接证明 ∫f dS = O(1)**：
- 对关联是二阶统计（pairs），∫f dS 是一阶量（单零点加权和）
- 需要的是 **S 的振荡抵消**（黎曼-勒贝格型或 van der Corput 型）
- Gallagher-Mueller 的**方法**（Selberg/Fujii 去 RH 技巧）可能是正确工具，但需要新的推导

---

## 3. 可能的方向（评估）

### 方向 1：Selberg/Fujii 方法直接应用于 ∫f dS
- BGSTB24 展示了如何用 Selberg 方法去 RH
- 若能对 ∫f_n dS 应用类似方法 → 可能无条件
- 难点：f_n 依赖于 n（非固定测试函数），需要一致估计

### 方向 2：黎曼-勒贝格型振荡抵消
- f_n' 是啁啾（频率从 −n 扫到 0）
- S(t) 逐点 O(log t) + 振荡
- 需要：∫f_n'(t)S(t)dt = o(1) 或 O(1) 的振荡抵消证明

### 方向 3：d_k 负相关的直接证明
- d_k ≈ f·N'·δ_k（间距偏差加权）
- 零排斥（无条件）抑制小间距 → δ_k 下界
- 但负相关（大后必小）需要更多结构

### 方向 4：数值验证振荡抵消（当前最可行）
- 分解 ∫f_n' S dt 的频率贡献
- 检验高频部分（黎曼-勒贝格型）是否主导且抵消
- 若成立 → 支持方向 2 的证明路径

---

## 4. 引用格式（备查）

```bibtex
@article{BGSTB24,
  author = {Baluyot, Siegfred Alan C. and Goldston, Daniel Alan and Suriajaya, Ade Irma and Turnage-Butterbaugh, Caroline L.},
  title = {An unconditional {M}ontgomery theorem for pair correlation of zeros of the {R}iemann zeta-function},
  journal = {Acta Arithmetica},
  volume = {214},
  year = {2024},
  pages = {357--376},
  doi = {10.4064/aa230612-20-3}
}

@article{GM78,
  author = {Gallagher, P. X. and Mueller, J. H.},
  title = {Primes and zeros in short intervals},
  journal = {J. reine angew. Math.},
  volume = {303/304},
  year = {1978},
  pages = {205--220}
}

@article{GLSS26,
  author = {Goldston, Daniel A. and Lee, Junghun and Schettler, Jordan and Suriajaya, Ade Irma},
  title = {Pair {C}orrelation {C}onjecture for the zeros of the {R}iemann zeta-function {I}: simple and critical zeros},
  journal = {arXiv:2503.15449},
  year = {2026}
}
```

---

## 5. 结论

1. **无条件 Montgomery 定理存在**（BGSTB24 2024）——对支撑 [−1,1] 测试函数
2. **Gallagher-Mueller 零排斥无条件**（0<λ≤√L）
3. **但都是二阶/近距离信息，不能直接控制一阶量 ∫f dS = O(1)**
4. **最可行路径**：Selberg/Fujii 方法（去 RH 技巧）应用于 ∫f_n dS + 数值验证振荡抵消结构
5. **PCC ⟹ 100% 简单 + 临界线**（GLSS26）——若 PCC 成立则 RH 渐近成立（新的等价形式）
