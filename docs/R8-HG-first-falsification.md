# R8-HG-1：首要否证（inversion 是否强迫 Kloosterman）——第一轮执行

**日期**：2026-09-10 14:20+ ｜ 依据：唐先生 HG-1–HG-7 + 小灵补两个初等引理 ｜ 预算：纸面

---

## 1. ✅ 已严格成立（群型情形）：HG-1 引理

$$G_q=(\mathbb Z/q\mathbb Z)^\times,\quad \mathcal F_+f(a)=\sum_{x\in G_q}f(x)\psi_p(ax),\quad I:x\mapsto x^{-1}$$
**Pontryagin 事实（严格）**：$\overline{\chi(x)}=\chi(x^{-1})$ ⟹ 特征共轭 $J_\times:\chi\mapsto\bar\chi$ 在点空间对应**恰是** inversion
$$\boxed{(\mathcal F_+ I\mathcal F_+^*)(a,b)\ \text{的核}\ =\ \sum_{x\in G_q}\psi_p(ax+bx^{-1})=K_p(a,b)\ \text{（Kloosterman）}}$$
$$\boxed{\text{加法 Fourier}\ +\ \text{乘法对偶共轭}\ +\ \text{点空间 inversion}\ \Longrightarrow\ \text{Kloosterman 核}}$$
**⚠️ 但推导偷用了关键条件**：$J^\vee$ 在点空间**对应** $x\mapsto x^{-1}$——这在**乘法群**成立，
而 R8 要找的正是**改变有限层组合律本身** ⟹ 真问题是：**hypergroup/scheme 中，character-side conjugation 对应何种 point-side involution？**

## 2. 一般交换 hypergroup（唐先生 HG-2）
$$\delta_x*\delta_y=\sum_z p_{xy}^z\delta_z,\quad \overline{\chi(x)}=\chi(\bar x)\quad\text{（与群情形平行）}\quad\text{但}\ \boxed{\bar x\neq x^{-1}\ \text{一般成立}}$$
$$K_H(a,b)=\sum_{x\in X}w(x)e_p\!\big(a\,\iota(x)+b\,\iota(\bar x)\big),\qquad \iota:X\to\mathbb F_p$$
⟹ $\bar x=x^{-1}$ 时 $K_H=$ Kloosterman；$\bar x\neq x^{-1}$ 时得到**不同于标准 Kloosterman 的 reciprocal kernel**
$$\boxed{\text{⟹ (ii)「inversion 强迫 Kloosterman」【不能】作为总 NO-GO}}$$
能严格推出的是更窄的命题：**群型乘法结构 + character conjugation + additive Fourier 耦合 ⟹ Kloosterman**

---

## 3. ⭐⭐ 小灵补两引理（初等可验算）

### 引理 HG-3（环可定义对合清单 —— 含**非 Kloosterman** 实例）
```
环 (ℤ/q,+,×) 可定义的对合除 {x, −x, x⁻¹, −x⁻¹} 外，还有【幂映射族】：
   x ↦ ±x^k，其中 k² ≡ 1 (mod λ(q))（λ = Carmichael 函数）
（验证：(x^k)^k = x^{k²} = x^{1 + t·λ(q)} = x ✓）
```
**核的形态** $K(a,b)=\sum_x w(x)e_q(a\,x+b\,x^k)$：
| $k$ | 核 | 判定 |
|---|---|---|
| $k=1$ | $e_q((a+b)x)$ | **退化**（仅依赖 $a+b$，非 reciprocal） |
| $k=-1$ | $\sum_x w(x)e_q(ax+b x^{-1})$ | **Kloosterman** |
| $k$ 使 $x^k=-x$（如加符号） | $e_q((a-b)x)$ | **退化** |
| **其他** $k^2\equiv1$ | $\sum_x w(x)e_q(a x+b x^k)$ | ⭐ **非退化、非 Kloosterman 的新 reciprocal 核** |

**具体实例（重要）**：$q=17$ 时 $\lambda(16)=16$，$7^2=49\equiv1\ (\mathrm{mod}\ 16)$
⟹ $x\mapsto x^7$ 是 $(\mathbb Z/17)^\times$ 上的**对合**，且 $x^7\neq\pm x^{\pm1}$
$$\boxed{\text{⟹ 存在环可定义、非退化、且【不是 Kloosterman】的 reciprocal 核}\ \sum_x w(x)e_{17}(ax+bx^7)}$$
（例：$q=17$ 的对合还有 $k=9,15$；$k=15\equiv-1$ 即 inversion）

### 引理 HG-4（**CRT 刚性** —— 由此 (i) 严格杀死环可定义类）
```
① 模数【一致】的幂对合：要求 k² ≡ 1 (mod λ(q)) 对【所有】q 成立
   ⟹ k²−1 被所有 λ(q) 整除 ⟹ k²−1 被 lcm_q λ(q) = ∞ 整除 ⟹ **k = ±1**
② 允许【逐素数】选择 k_p（k_p² ≡ 1 mod λ(p^e)）：CRT 张量自动成立，
   但需要一条【固定有限局部规则】选出 k_p
   而 λ(p^e) 的平方根 1 有 2^{ω(λ)} 个（k=±1 之外大量存在，如 p=17 的 7, 9）
   ⟹ 除了 k=±1，**没有 canonical 选择** ⟹ 违反 Z1 的生成性要求
```
$$\boxed{\textbf{(i) CRT（+ Z1 生成性）杀死环可定义类中的一切非 Kloosterman 对合}}$$
**⟹ 在"环可定义对合"这一整类内，结论是**：
$$\boxed{\text{reciprocal 核只能【退化】或【Kloosterman】——没有第三种}}$$

### ⭐⭐ 推论：第三类必须在【环可定义对合类之外】
$$\boxed{\text{逃逸须来自【非环语法】的对合}}$$
**具体候选（我建议的下一入口）**：把对合从**剩余类层**换到**因子分解层**——
即作用在**素数指数向量 / 除数结构**上的对合（非 $\mathbb Z/q$ 上的多项式映射）
```
⟹ 这直接连回本项目早前审计过的 **divisor-complement（d ↦ n/d）** 结构：
   当时的结论是"它给出 δ↔−δ 反射，但缺 γ（振荡）通道"
   —— 但那是【在缺少加法特征的语境下】得出的
   ⟹ 本语境中【加法特征提供振荡】，故 divisor-complement 必须【重新审计】
```
**⚠️ 这一条是本轮真正的收获**：环层已被 CRT 锁死，逃逸被迫移到因子分解层，
而该层恰有一个已审计过但要在此语境重审的候选。

---

## 4. HG-3/HG-4 与既有框架的接口
- **HG-3 的 Euclidean scheme 正向警告样本**（唐先生）：有限域 Euclidean association scheme 的谱矩阵确实出现 Kloosterman sums；二维情形甚至有 $P=Q=\begin{pmatrix}1&(q+1)\mathbf1^T\\\mathbf1&1-K\end{pmatrix}$，$K_{ij}=K(1,ij/4)$ ⟹ **association scheme 本身没有逃离 Kloosterman**（但也不是分类定理）
- **HG-6 三步杀伤链（唐先生）**：$\text{CRT}\to\text{local involution classification}\to\text{reciprocal kernel classification}$
  ⟹ **本轮把中间一步在"环可定义类"内做完了**（HG-3+HG-4）
- **HG-5 两条禁止的假杀法**：① 不得把 "hypergroup 的对合最后总是 group inverse" 当定理（Bessel–Kingman 就是非群卷积）② 不得用"谱表出现 Kloosterman ⟹ 本质是 Kloosterman"（循环论证）

## 5. 下一步框架（唐先生 H1–H7 + A/B/C）
$$\mathfrak H_q=(X_q,*_q,\bar{\phantom{x}},\iota_q),\quad
\begin{cases}
H1\ \text{finite commutative hypergroup}\\
H2\ \overline{\chi(x)}=\chi(\bar x)\\
H3\ \iota_q:X_q\to\mathbb Z/q\mathbb Z\\
H4\ H_{mn}\simeq H_m\otimes H_n\\
H5\ \bar{\phantom{x}}\ \text{CRT-compatible}\\
H6\ \text{quadratic spectral closure}\\
H7\ \text{zero-blind}
\end{cases}$$
研究对象：$K_{\mathfrak H}(a,b)=\sum_{x\in X_q}w(x)e_q(a\iota_q(x)+b\iota_q(\bar x))$
**三种结果**：
```
A  ι(x̄)=c/ι(x) ⟹ K_𝔥 = Kloosterman ⟹ **(ii) 杀死**
B  存在非 Kloosterman 的 x̄ 但 CRT 失败 ⟹ **(i) CRT 杀死**
C  存在真正非 Kloosterman、CRT-compatible 的 𝔥_q ⟹ **第三类首个严格正例**
```
**本轮定位**：在**环可定义类**内已落在 **B（(i) CRT 杀死）**——且是**证明**而非猜测；
**但 H1–H7 允许 $X_q$ 不是 $(\mathbb Z/q)^\times$ 本身**（真正的 hypergroup 状态空间）
⟹ **A/B/C 判定仍未完成**，逃逸口 = §3 的推论（非环语法对合 / 因子分解层）

## 6. 诚实边界
```
· §1 的 Pontryagin 事实与 (F_+ I F_+*) 的核计算为【严格初等事实】（群型情形）
· §3 引理 HG-3 的"幂对合族"为严格验算（k²≡1 mod λ(q)，q=17 的 k=7 实例已验）
  但其【清单完整性】（"环可定义对合恰为此族及 ± 符号"）为【结构性声称】，须形式化"环可定义"概念
· §3 引理 HG-4 的①（一致 k ⟹ k=±1）为【严格初等】；②（逐素数选择非 canonical）依赖
  "canonical/固定有限局部规则"的形式化 ⟹ 属【结构性论证】
· §4 的 Euclidean scheme 谱矩阵与 P=Q 形态为唐先生提供（文献级）
· §5 的 A/B/C 与 H1–H7 为唐先生框架；本轮未完成其判定
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 7. 提交链
```
8caa8be ERR-R8-ARCH-1 → 本篇（R8-HG-1 首要否证第一轮）
```
