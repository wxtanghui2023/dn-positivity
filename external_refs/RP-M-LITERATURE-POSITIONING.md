# (RP_M) 的文献定位（外部文献，一手逐字）

> 建立日期 2026-09-19 · 触发：唐先生问「文献有没有其它版本可读」
> 纪律：以下均为**外部一手逐字**（arXiv HTML / 出版商页），来源标 URL ✓

## §1 核心发现：我们的 (RP_M) 属于 **Turán 幂和问题族** ✓✓

**来源**：J. Andersson, *On some power sum problems of Montgomery and Turán*,
arXiv:0706.4131v3（2007；math.NT）— **免费可读** ✓

**族量（逐字）**：
```
(⋆) = inf_{|z_k|=1}  max_{ν=1,...,m} | Σ_{k=1}^{n} z_k^ν |
```
本文目标（逐字）："determine the quantity (⋆) for various choices of integers n,m …
For any fixed B > 1 and m = ⌊n^B⌋ we prove that (⋆) ≍ √n. This solves open problems
of Hugh Montgomery and Paul Turán."

## §2 族内已知结果（逐字转引）

| 结果 | 内容 | 出处（文件内编号） |
|---|---|---|
| 平凡 | z_k = e(k/n) ⟹ (⋆) = 0（1 ≤ m ≤ n−1） | — |
| **Turán** | $(\star) = 1$ 当 $m = n$ | [13] |
| Andersson | $(\star) = \sqrt{n-1}$（$m=n^2-n$，$n-1$ 为素数幂）；$(\star)=\sqrt n$（$m=n^2-j$） | [2] |
| Andersson | $m\in(n^{1+\delta}, n^2]$ ⟹ $(\star)\sim\sqrt n$ | [3] |
| **Montgomery Thm 10** | $\sqrt{nB}\ \ll\ \max_{\nu=1,\ldots,n^B}\big|\sum_{k=1}^n z_k^\nu\big|$，$1+\delta\le B\le n$，$\|z_k\|=1$ | [12] **p.100, Theorem 10** |
| Erdős–Rényi | 存在元组使 $\big|\sum z_k^\nu\big|\le\sqrt{6n\log(m+1)}$ | [9] |
| Leenman–Tijdeman | 显式构造给同阶 | [11] |

## §3 ⭐⭐ Montgomery《Ten Lectures》的两处**逐字引用**（我们拿不到原书）

$$\textbf{Problem 1 (Montgomery, [12] \textbf{page 197, Problem 13})}✓$$
> "Show that for any positive B there exist complex numbers z_1,…,z_n such that |z_k| = 1
>   for all k and  |Σ_{k=1}^n z_k^ν| ≪_B √n.  (ν = 1,…,⌊n^B⌋)"

$$\textbf{Problem 2 (Turán, [14] page 197, Problem 54)}✓$$
> "Does there exist an w(x) ↗ ∞ such that b_j > 0, |z_j| = 1, j=1..n implies for
>   g(ν)=Σ_j b_j z_j^ν the inequality  max_{1≤ν≤n^{100}} |g(ν)| > (w(n)/√n)|g(0)|?"

**⟹ 意义**：
- 我们缺的 CBMS 84 那本，其 **p.100 Thm 10** 与 **p.197 Problem 13** 已由本文逐字带出 ✓✓
- Palojärvi 引的 "Chapter 5, Theorem 11"（= 我方 `(RP_M)` 的来源引理）**同属该章** ⟹ 与 Thm 10 同源 ✓
- **故 `(RP_M)` 应定位为**：Montgomery Thm 11（实部版，常数 1/20，窗口 5M）的**尖锐常数改进** ✓✓

## §4 Andersson 的解法工具（供参考）

$$\textbf{Lemma 1 (逐字)}：\text{Let}\ h\ge2,\ q\ \text{prime power. Then there exist unimodular}\ z_1,\ldots,z_q\ \text{such that}$$
$$\qquad \max_{\nu=1,\ldots,q^h-2}\Big|\sum_{k=1}^q z_k^\nu\Big|\ \le\ (h-1)\sqrt q✓$$
$$\textbf{Theorem 1 (逐字)}：\sqrt{Bn}\ \ll\ \inf_{|z_k|=1}\max_{\nu=1,\ldots,\lfloor n^B\rfloor}\Big|\sum_{k=1}^n z_k^\nu\Big|\ \ll\ B\sqrt n，\text{一致于}\ 1+\delta\le B\le n✓$$
$$\text{工具（逐字}）：\text{"We use an estimate for character sums over finite fields of Katz"；}$$
$$\qquad \text{构造法}：\text{素数幂}\ 2^m\ \text{上的特殊元组 ＋ 二进制展开拼装（}\text{加法构造}）✓$$

## §5 ⭐ 我们 `(RP_M)` 与文献的**精确差别**（关键，必须写对）

$$\text{文献族}：\textbf{模长版}＋\textbf{多项式窗口}（m=\lfloor n^B\rfloor,\ B>1）⟹\text{已知}\ (\star)\asymp\sqrt n✓$$
$$\text{我方}：\textbf{实部版}＋\textbf{线性窗口}（k\le 5M，即\ m=5n）✓$$
$$\qquad \Longrightarrow \textbf{窗口小得多}（5n\ \text{vs}\ n^{1+\delta}）⟹\ \text{文献结论}\ \textbf{不直接适用}✗✓$$
$$\qquad \Longrightarrow\ \text{但定位清楚}：\text{Turán 的}\ (\star)=1\ (m=n)\ \text{与 Montgomery Thm 10 的}\ \sqrt{nB}\ \text{夹在两端}✓$$
$$\qquad \qquad \text{我方窗口}\ 5n\ \text{正落在"线性窗口"区，恰是文献最薄弱的位置}✓✓$$

## §6 待办（下一步）

1. 取 Andersson 全文（9 页；HTML 可读 ✓）以获取 §3 的 Katz 特征和引理与完整证明 ✓
2. 查 [2]/[3]（Andersson 前作）中 $m=n^2-n$ 的**精确值**结果，确认是否有我们窗口附近的显式值 ✓
3. 论文文献栏按 §3/§5 定位改写（**不再写"与文献无关"**）✓
4. Turán 幂和教科书（Turán 1984）是否可得 —— 幂和法的系统表述 ✓

---

## §7 Andersson 全文（arXiv:0706.4131v3）其余结果（逐字）

$$\textbf{Lemma 1}：h\ge2,\ q\ \text{素数幂} \Longrightarrow \exists\ \text{单位模}\ z_1,\ldots,z_q：\max_{\nu\le q^h-2}\Big|\sum_{k\le q}z_k^\nu\Big|\le(h-1)\sqrt q✓$$
$$\textbf{Theorem 1}（\text{解 Montgomery Problem 13}）：\sqrt{Bn}\ \ll\ \inf_{|z_k|=1}\max_{\nu\le\lfloor n^B\rfloor}\Big|\sum_{k\le n}z_k^\nu\Big|\ \ll\ B\sqrt n\quad(1+\delta\le B\le n)✓$$
$$\textbf{Corollary 1}：\text{Turán Problem 2（}w(x)\ \text{不存在）}✓\qquad\textbf{Theorem 2}：C_h\sqrt n-O(n^{-1/2})\le\inf_{|z_k|\ge1}\max_{\nu\le n^h}\Big|\sum\Big|\le(h-1)\sqrt n+O(n^{0.2625+\epsilon})✓$$
$$\qquad C_{2m}=(m!)^{1/2m},\ C_{2m+1}=C_{2m}；\textbf{Remark 1}：h=3\ \text{时下界可改进为}\ \sqrt{2n}✓$$
$$\textbf{Problem 3（$\text{本文提出，开放}$）}：\text{找递增}\ \Lambda(x)\ \text{使}\ \inf_{|z_k|=1}\max_{\nu\le\lfloor n^B\rfloor}|\sum|\sim\Lambda(B)\sqrt n✓$$

## §8 Andersson 系列（同族全部论文）

| 编号 | 文献 | 内容（逐字/摘要） |
|---|---|---|
| [1] | Acta Math. Hungar. **70**(4):305–316 (1996) | On some power sum problems of Turán and Erdős |
| [2] | arXiv:math/0607238（Indag. Math.） | **精确值**：$\sqrt n\le\inf_{|z_k|\ge1}\max_{\nu\le n^2}|s_\nu|\le\sqrt{n+1}$（$n+1$ 素）；$\inf_{|z_k|=1}\max_{\nu\le n^2-n}|s_\nu|=\sqrt{n-1}$（$n-1$ 素数幂）；$\inf_{|z_k|\ge1}\max_{\nu\le n^2-i}|s_\nu|=\sqrt n$（$n$ 素数幂，$2\le i\le n-1$）✓ **给出显式构造并证明为全局极小**✓ |
| [3] | arXiv:math/0609271 | Turán's problem 10 revisited |
| [4] | arXiv:0704.1879 | **下界**（用 **Fejér 核**的特征）：$m\sim cn^2$（$c>1$）、单位模情形 ✓ |
| [12] | **Montgomery, Ten Lectures（CBMS 84）** | p.100 Thm 10（下界）；p.197 Problem 13（= 本文解决）；**Ch.5 Thm 11 = Palojärvi Lemma 2.2** |
| [14] | **Turán 1984, _On a new method of analysis and its applications_（Wiley）** | 幂和法专著（系统工具）✓ |

## §9 ⭐⭐ 窗口 regime 地图（我们的位置）

$$\begin{array}{c|c|l}
\text{窗口}\ m & (\star)\ \text{（模长版）} & \text{出处}\\\hline
m\le n-1 & 0 & \text{平凡}（z_k=e(k/n)）\\
m=n & \mathbf{1} & \text{Turán [13]}\\
\mathbf{m=5n\ （\text{我方}）} & \textbf{未知}✗ & \text{—— 文献空白区}\\
m=n^{1+\delta}\sim n^2 & \asymp\sqrt n & \text{Andersson [3]}\\
m=n^2\ (\text{特殊}) & \text{精确值}\ \sqrt{n-1},\ \sqrt n\ \ldots & \text{Andersson [2]}\\
m=n^B,\ B>1 & \asymp\sqrt n & \text{本文（0706.4131）}\\
\end{array}✓$$

$$\Longrightarrow ⭐\ \textbf{我方}\ (RP_M)\ \text{正落在"线性窗口"区}\ （m=5n）⟹\ \textbf{文献空白}✗✓$$
$$\qquad \textbf{且}\ 实部版 \ne\ 模长版：\max_\nu|\Sigma|\ge c\ \Longrightarrow\ \text{不能推出}\ \max_\nu\Re\Sigma\ge c\ ✗$$
$$\qquad （\text{因}\ |\Re|\le|\cdot|\ \text{只给上界}；\text{且窗口取正指标 ⟹ 共轭对称帮不上忙}）✓$$

## §10 对论文的直接用途

1. **文献栏必须写**（原稿"与文献无关"是错的 ✗）：Turán 幂和法 → Montgomery Thm 10/Thm 11 → Andersson 0706.4131（Problem 13）✓
2. **定位句**：本工作研究 **Montgomery Thm 11（实部版、线性窗口 5M）的常数尖锐化**；该窗口在文献中**尚无结果** ✓
3. **工具对接**：Andersson [4] 用 **Fejér 核** —— 与我方 `C-181` §3(a) 的 Fejér 权路线**同族** ✓（可对照）
4. **Turán 1984 专著**是幂和法的系统来源（若能取得，可补工具）✓
