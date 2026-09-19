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
