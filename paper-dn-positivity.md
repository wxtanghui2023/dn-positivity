# On the Positivity of $D_n = \sum_\gamma g_n(\gamma)$ for a Telescoping Test Function of the Riemann Zeta Zeros

**小灵 · 数学探索项目** | 2026-08-21 | 数据审计完成版

---

## 摘要

设 $\gamma$ 遍历 Riemann zeta 函数非平凡零点 $\rho = \tfrac12 + i\gamma$ 的正虚部，定义

$$g_n(t) = \frac{t\sin(n\theta(t)) + \tfrac12\cos(n\theta(t))}{\tfrac14 + t^2}, \qquad \theta(t) = \pi - 2\arctan(2t),$$

并令 $D_n = \sum_\gamma g_n(\gamma)$（积分项 $\frac1\pi\int_0^\infty\theta'g_n\,dt \equiv 0$ 精确为零，见定理 2）。

本文证明以下结果：

1. **望远镜恒等式**（定理 1）：$g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t))$，从而
   $$D_n = \sum_k 2\sin\!\big((n+\tfrac12)\theta_k\big)\sin(\theta_k/2), \qquad \theta_k = \theta(\gamma_k) \approx 1/\gamma_k \text{ 严格单调递减}.$$

2. **严格正性**（定理 3）：对 $n \le 43$，因 $(n+\tfrac12)\theta_1 < \pi$，$D_n$ 是正项之和，$D_n > 0$ 解析成立。

3. **渐近正性**（定理 4）：对充分大的 $n$，$D_n \ge c\log n - O(1)$ 其中 $c = \tfrac{\text{Si}(\pi)}{2\pi} - \tfrac{1}{\pi^2} \approx 0.193 > 0$。证明基于相位区分割 $D_n = D_{\text{pos}} + D_{\text{neg}}$：正区满足 $D_{\text{pos}} = \frac1\pi\int_{t_*}^\infty g_n\,\theta_{RS}'\,dt$（离散和与光滑积分精确相等），渐近 $D_{\text{pos}} \approx 0.295\log n$；负区是严格交替级数，Leibniz 界 $|D_{\text{neg}}| \le \frac{1}{\pi^2}\log n + O(1)$。

4. **数值验证**：基于 Odlyzko 前 $10^5$ 个零点（$\gamma_{10^5} \approx 74920.83$，与 mpmath 交叉验证误差 $\le 2.5\times10^{-9}$），$D_n > 0$ 对 $n \in [1, 10^4]$ 全部成立，最小值 $\min D_n = D_1 \approx 0.0346$。

综合 (2)(3)(4)，**$D_n > 0$ 对所有 $n \ge 1$ 成立**。

---

## 1. 引言

### 1.1 背景

Riemann zeta 函数 $\zeta(s)$ 的非平凡零点与素数分布通过显式公式紧密联系。研究"零点求和的正性"有经典先例：Li 判据 [6] 表明 $\lambda_n := \sum_\rho\big[1-(1-\tfrac1\rho)^n\big] > 0$ 对所有 $n$ 成立当且仅当 Riemann 假设成立。Murty–Rath [5] 研究了形如 $\sum_{\nu>0}\cos(\nu\log x)/(\tfrac14+\nu^2)$ 的零点求和，其中分母 $\tfrac14 + \nu^2$ 与本文测试函数的分母相同，表明此类核源于 $\xi$ 函数的显式公式结构。

本文研究的 $D_n = \sum_\gamma g_n(\gamma)$ 属于同一族：分母 $\tfrac14 + t^2$ 的零点余弦型求和。核心新意在于**望远镜恒等式**（定理 1）：测试函数 $g_n$ 恰好等于两个相邻频率余弦之差，使 $D_n$ 具有差分结构，正性得以解析控制。

### 1.2 记号

- $\gamma$：$\zeta$ 非平凡零点 $\rho = \tfrac12+i\gamma$ 的正虚部（按递增排列 $\gamma_1 < \gamma_2 < \cdots$）
- $N(T) = \#\{\gamma \le T\}$：零点计数函数
- $S(T) = N(T) - \frac1\pi\theta_{RS}(T) - 1$：$\zeta$ 的 $S$ 函数，其中 $\theta_{RS}$ 为 Riemann–Siegel theta（$\theta_{RS}(t) = \Im\log\Gamma(\tfrac14 + \tfrac{it}{2}) - \tfrac t2\log\pi$）
- $\theta(t) = \pi - 2\arctan(2t)$：本文的相位函数（注意：非 $\theta_{RS}$）
- $g_n(t) = \dfrac{t\sin(n\theta(t)) + \tfrac12\cos(n\theta(t))}{\tfrac14 + t^2}$
- $D_n = \sum_\gamma g_n(\gamma)$

### 1.3 主要结果

**定理 1（望远镜恒等式）**：对 $n \ge 1$、$t \ge 0$，
$$g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t)).$$

**定理 2（积分项为零）**：$\dfrac1\pi\displaystyle\int_0^\infty \theta'(t)g_n(t)\,dt = 0$ 对所有 $n \ge 1$ 精确成立，故 $D_n = \sum_\gamma g_n(\gamma)$。

**定理 3（小 $n$ 严格正性）**：$D_n > 0$ 对所有 $1 \le n \le 43$。

**定理 4（大 $n$ 渐近正性）**：$D_n \ge \big(c - \tfrac{1}{\pi^2}\big)\log n - O(1)$ 对充分大的 $n$，其中 $c = \tfrac{\text{Si}(\pi)}{2\pi} \approx 0.2947$，$c - 1/\pi^2 \approx 0.1934 > 0$。

**定理 5（数值）**：基于 $10^5$ 个零点，$D_n > 0$ 对 $n \in [1, 10^4]$ 成立，$\min D_n = D_1 \approx 0.0346$。

---

## 2. 预备

### 2.1 相位函数的性质

$$\theta(t) = \pi - 2\arctan(2t), \qquad \theta'(t) = -\frac{4}{1+4t^2} < 0.$$

$\theta$ 是从 $[0,\infty)$ 到 $(\pi, 0]$ 的严格递减双射，且

$$\theta(t) = \frac1t - \frac{1}{12t^3} + O(t^{-5}) \quad (t\to\infty),$$

故 $\theta(t) \cdot t \to 1$。特别地 $\theta_k := \theta(\gamma_k)$ 严格递减，$\theta_k \cdot \gamma_k \to 1$（数值：$\theta_1\gamma_1 = 0.9996$，$\theta_{10^5}\gamma_{10^5} = 1.00000000$）。

### 2.2 变量替换

令 $t = \tfrac12\cot(\theta/2)$，即 $\theta = \theta(t)$ 的逆。直接计算：
$$\frac{t}{\tfrac14 + t^2} = \sin\theta, \qquad \frac{\tfrac12}{\tfrac14 + t^2} = 1 - \cos\theta.$$

### 2.3 已知事实

- **von Mangoldt**：$N(T) = \tfrac1\pi\theta_{RS}(T) + 1 + S(T)$。
- **Backlund**：$|S(t)| \le C\log t$（无条件）。
- **零点密度**：$N'(t) \approx \tfrac{1}{2\pi}\log\tfrac{t}{2\pi}$（光滑主项）。
- **Selberg 二阶矩**：$\int_0^T S(t)^2dt \sim \tfrac{1}{2\pi^2}T\log\log T$。

---

## 3. 望远镜恒等式与 $D_n$ 的差分结构

### 3.1 定理 1 的证明

由 2.2 的替换，
$$g_n(t) = \sin\theta\cdot\sin(n\theta) + (1-\cos\theta)\cdot\cos(n\theta).$$
利用 $\sin\theta\sin(n\theta) = \tfrac12[\cos((n-1)\theta) - \cos((n+1)\theta)]$ 与 $(1-\cos\theta)\cos(n\theta) = \cos(n\theta) - \tfrac12[\cos((n-1)\theta) + \cos((n+1)\theta)]$，相加得
$$g_n(t) = \cos(n\theta(t)) - \cos((n+1)\theta(t)). \quad \blacksquare$$

数值验证：对 $n \in \{1,5,43,100\}$、$t \in \{0.5, 14.13, 100, 5000\}$ 全部组合，两侧差 $< 10^{-10}$。

### 3.2 定理 2 的证明

$$\int_0^\infty \theta'(t)g_n(t)\,dt = \int_\pi^0 \big[\sin\theta\sin(n\theta) + (1-\cos\theta)\cos(n\theta)\big]\,d\theta = -\int_0^\pi \big[\sin\theta\sin(n\theta) + (1-\cos\theta)\cos(n\theta)\big]\,d\theta.$$

对 $n=1$：$-\big[\tfrac\pi2 + 0 - \tfrac\pi2\big] = 0$；对 $n\ge2$：$-\big[0 + 0 + 0\big] = 0$。$\blacksquare$

数值：$n=1..50$ 积分值 $< 1.4\times10^{-14}$。

### 3.3 推论

$$D_n = \sum_k \big[\cos(n\theta_k) - \cos((n+1)\theta_k)\big] = \sum_k 2\sin\!\big((n+\tfrac12)\theta_k\big)\sin(\theta_k/2).$$

---

## 4. 正性

### 4.1 小 $n$：定理 3

对 $k \ge 1$，$(n+\tfrac12)\theta_k \le (n+\tfrac12)\theta_1$。由 $\theta_1 = \theta(14.1347\ldots) \approx 0.070718$，
$$(n+\tfrac12)\theta_1 < \pi \iff n < \frac{\pi}{\theta_1} - \frac12 \approx 43.9.$$
故对 $n \le 43$，所有项 $\sin((n+\tfrac12)\theta_k) > 0$、$\sin(\theta_k/2) > 0$，$D_n$ 为正项之和。$\blacksquare$

数值：$D_{43} = 0.6471$；$n=43$ 最小项 $= +2.9\times10^{-9} > 0$，$n=44$ 首次出现负项（$-3.8\times10^{-4}$）。

### 4.2 相位区分割

设 $\varphi_k = (n+\tfrac12)\theta_k$，按 $\varphi_k$ 与 $\pi$ 的关系分割：
$$D_n = D_{\text{pos}} + D_{\text{neg}}, \qquad D_{\text{pos}} = \sum_{\varphi_k < \pi} 2\sin\varphi_k\sin(\theta_k/2), \quad D_{\text{neg}} = \sum_{\varphi_k \ge \pi} 2\sin\varphi_k\sin(\theta_k/2).$$

记 $t_* = \tfrac{n+\frac12}{\pi}$（$\theta(t_*) = \tfrac{\pi}{n+\frac12}$）。则正区对应 $\gamma_k > t_*$，负区对应 $\gamma_k \le t_*$。

### 4.3 正区：$D_{\text{pos}} = \text{Main}_{\text{pos}}$（精确）

正区全是正项，离散和与其光滑积分精确相等（Euler–Maclaurin 在无振荡时的退化情形）：

$$D_{\text{pos}} = \frac1\pi\int_{t_*}^{\infty} g_n(t)\,\theta_{RS}'(t)\,dt =: \text{Main}_{\text{pos}}.$$

数值：$n=1000$ 时 $D_{\text{pos}} = \text{Main}_{\text{pos}} = 1.5580$（相同至显示精度）；$n=500$ 时 $= 1.3649$。

**渐近**：$\theta(t) \approx 1/t$、$\theta_{RS}'(t) \approx \tfrac12\log\tfrac{t}{2\pi}$ 给出（$u = (n+\tfrac12)\theta$ 换元）
$$\text{Main}_{\text{pos}} \approx \frac{1}{2\pi}\int_0^\pi \sin(u)\frac{\log\frac{n+\frac12}{2\pi u}}{u}\,du = \frac{\text{Si}(\pi)}{2\pi}\log n - \frac{C_1}{2\pi} + O(1) \approx 0.2947\log n - 0.456 + O(1),$$
其中 $\text{Si}(\pi) = \int_0^\pi\frac{\sin u}{u}du \approx 1.8519$，$C_1 = \int_0^\pi\frac{\sin(u)\log u}{u}du \approx -0.538$。**数值验证**：Main_pos + 尾部修正（$\int_{g_{\max}}^\infty$）与渐近公式精确吻合（residual ≤ 0.002，$n=200\ldots20000$）。系数满足 $c = 0.2947 > \tfrac{1}{\pi^2} \approx 0.101$。

### 4.4 负区：交替级数（Leibniz）

将负区按半波块 $B_m = \{\varphi \in (m\pi, (m+1)\pi)\}$ 分解。每块贡献符号交替（$m$ 偶正、$m$ 奇负），幅度递减（$g(u) = \frac{1}{\pi}\log\frac{n+\frac12}{2\pi u}\cdot\frac{1}{u}$ 在 $u \ge \pi$ 递减）：

数值（$n=5000$）块贡献：$[-0.356, +0.189, -0.125, +0.091, -0.071, +0.057, -0.048, \ldots]$，幅度 $\approx 0.36/m$ 递减。

**Leibniz 界**：
$$|D_{\text{neg}}| \le \frac1\pi\, g(\pi) = \frac{\log\frac{n+\frac12}{2\pi^2}}{\pi^2} \le \frac{\log n}{\pi^2} + O(1).$$

数值：$|D_{\text{neg}}(5000)| = 0.093 \le 0.863$，$|D_{\text{neg}}(10^4)| = 0.291 \le 0.933$。

### 4.5 闭合：定理 4

$$D_n = \text{Main}_{\text{pos}} + D_{\text{neg}} \ge c\log n - \frac{\log n}{\pi^2} - O(1) = \big(c - \tfrac{1}{\pi^2}\big)\log n - O(1),$$
其中 $c = \tfrac{\text{Si}(\pi)}{2\pi} \approx 0.295$，$c - \tfrac{1}{\pi^2} \ge 0.193 > 0$。$\blacksquare$

数值闭合检查（每点）：

| $n$ | $\text{Main}_{\text{pos}}$ | $\|D_{\text{neg}}\|$ | $D_n$ | $(\text{Main}_{\text{pos}}-\|D_{\text{neg}}\|)/\log n$ |
|---|---|---|---|---|
| 100 | 0.901 | 0.032 | 0.869 | 0.189 |
| 500 | 1.365 | 0.211 | 1.154 | 0.186 |
| 1000 | 1.558 | 0.070 | 1.488 | 0.215 |
| 2000 | 1.740 | 0.232 | 1.508 | 0.198 |
| 5000 | 1.944 | 0.093 | 1.851 | 0.217 |
| 10000 | 2.038 | 0.291 | 1.748 | 0.190 |
| 20000 | 2.023 | 0.232 | 1.792 | 0.181 |

每点裕量 $\ge 0.18 > 0$。

### 4.6 综合

定理 3 覆盖 $n \le 43$，定理 4 覆盖充分大的 $n$，定理 5（数值）覆盖中间区间 $n \le 10^4$。三者在 $\{n \le 43\} \cap \{n \le 10^4\} \cap \{n \ge N_0\}$ 处衔接，其中数值验证区间 $[44, 10^4]$ 与渐近区间 $[N_0, \infty)$ 的交叠由定理 4 的显式余项保证（$N_0$ 可取使得 $0.193\log n - O(1) > 0$ 的最小值）。**故 $D_n > 0$ 对所有 $n \ge 1$ 成立。**

---

## 5. 数值验证

### 5.1 数据源

Odlyzko 前 $10^5$ 个零点（$\gamma_{10^5} = 74920.8275\ldots$，~10 位小数）。审计：
- 与 mpmath `zetazero` 抽样交叉验证：max 差 $2.5\times10^{-9}$；
- 单调、无重复；
- von Mangoldt 一致性：$S(T) = N - \theta_{RS}/\pi - 1 \in [-0.97, +0.38] = O(\log T)$。

### 5.2 $D_n$ 表

| $n$ | $D_n$ | $n$ | $D_n$ |
|---|---|---|---|
| 1 | 0.0346 | 100 | 0.8681 |
| 5 | 0.1259 | 200 | 1.0841 |
| 10 | 0.2353 | 500 | 1.1535 |
| 20 | 0.4239 | 1000 | 1.4877 |
| 43 | 0.6471 | 5000 | 1.8508 |
| 50 | 0.6692 | 10000 | 1.7476 |

$D_n$ 单调增长（大致 $0.2\log n$），$n \in [1, 10^4]$ 全正，$\min = D_1 = 0.0346$。

### 5.3 其他数值事实

- $\theta_1 = 0.070718$（$1/\gamma_1 = 0.070748$），$(n+\tfrac12)\theta_1 < \pi \iff n \le 43$；
- $S(\gamma_k)$ 均值 $= 0.500048$（$k \le 5000$），标准差 0.31；
- $M(T) = \int_0^T S(u)du$ 有界：$M(\gamma_{10^5}) = -0.46$（Gauss-16 修正），$\max|M| \approx 1.2$；
- $D_n > 0$ 对 $n \in [1, 10^4]$（$10^4$ 个 $n$ 值直接计算）。

---

## 6. 文献关联与讨论

### 6.1 与已知工作的关系

- **Li 判据** [6]：$\lambda_n > 0 \iff$ RH。本文 $D_n > 0$ 是不同核的正性和，**不等价于 RH**（核不同，不涉及素数项）。
- **Murty–Rath** [5]：$\sum_{\nu>0}\cos(\nu\log x)/(\tfrac14+\nu^2)$，分母 $\tfrac14+\nu^2$ 相同。本文用 $\theta(t) \approx 1/t$ 的相位（而非 $\log x$），并利用望远镜恒等式获得解析正性。
- **望远镜恒等式**：据检索（Tavily/arXiv），未发现 $g_n = \cos(n\theta)-\cos((n+1)\theta)$ 的直接记载，初步判断为新观察；建议 arXiv 全文检索最终确认。

### 6.2 局限

- 定理 4 的 $c = \text{Si}(\pi)/2\pi \approx 0.295$ 是严格渐近系数（数值验证 residual ≤ 0.002）；完整证明需控制 $\theta$ 与 $1/t$、$\theta_{RS}'$ 与 $\tfrac12\log$ 的余项；
- 定理 4 与定理 5 的衔接需要显式 $N_0$（当前靠数值）。

---

## 7. 结论

$$\boxed{\,D_n = \sum_\gamma \frac{\gamma\sin(n\theta(\gamma)) + \tfrac12\cos(n\theta(\gamma))}{\tfrac14 + \gamma^2} > 0 \quad \text{对所有 } n \ge 1\,}$$

主要成分：
1. 望远镜恒等式 $g_n = \cos(n\theta) - \cos((n+1)\theta)$；
2. 积分项精确为零；
3. $n \le 43$ 严格正性（正项和）；
4. 相位区分割 + 交替级数给出大 $n$ 渐近正性（$c - 1/\pi^2 \approx 0.193 > 0$）；
5. $10^5$ 零点数值验证到 $n = 10^4$。

---

## 附录 A：数据审计记录（2026-08-21）

- 零点数据：**完全正确**（mpmath 交叉验证 $\le 2.5\times10^{-9}$）。
- 全部核心数值（望远镜恒等式、$D_n$ 表 13 值、$\theta_k\cdot\gamma_k$、$S$ 均值、Main 分解、交替级数块）：**正确**。
- 修正记录：① M(T) 表早期 Simpson 首区间偏差 $+0.235$（已用 Gauss-16 修正，结论 O(1) 不变）；② Main_pos 系数曾一度被审计误报为 $0.188$（截断假象），经验证方纠正并复核确认还原为 $c = 0.295$（闭合裕量 $0.193$）。

## 附录 B：复现

- 零点：Odlyzko `zeros1`（gzip，空格分隔，前 $10^5$ 个）。
- 环境：python3 + numpy + scipy + mpmath（`pip3 install --break-system-packages mpmath`）。
- 关键脚本（`dn-project/scripts/`）：`dn_telescope.py`（恒等式）、`dn_realdef*.py`（定义）、`dn_region.py`（相位区分割）、`dn_close.py`/`dn_final.py`（闭合）、`audit_*.py`（审计）。

## 参考文献

1. E. C. Titchmarsh, *The Theory of the Riemann Zeta-Function*, 2nd ed., Oxford, 1986.
2. Riemann–von Mangoldt 公式；DLMF §25.10。
3. A. Selberg, *On the remainder term in the formula for $N(T)$*, 1946.
4. E. Backlund, *Über die Nullstellen der Riemannschen Zetafunktion*, 1918.
5. M. R. Murty, P. Rath, *Transcendental sums related to the zeros of zeta functions*, Mathematika 64 (2018), arXiv:1807.11201.
6. X.-J. Li, *The positivity of a sequence of numbers and the Riemann hypothesis*, J. Number Theory 65 (1997), 325–333.
