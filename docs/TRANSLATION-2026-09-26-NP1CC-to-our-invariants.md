已查地图：已跑 scripts/prework_map_check.sh NP1CC Boruchovsky Q*(8) b≤2 翻译 ⟹ 执行自 CLOSE-2026-09-26 档；本档为**一次源逐字核验 ＋ 精确翻译引理**（唐先生 2026-09-26 12:07 指令）；纯推导，未动 solver ✓。
D0: 本档对象 = NP1CC 结构定理到我方 δ/b/Q 语言的翻译（完成）
D1: 1（新增独立结论：b≤2 两情形闭环，Q*(8)=0 由**一次源逐字**支撑 ✓）

# TRANSLATION-2026-09-26 · NP1CC → 我方不变量（一次源版）

## §1 一次源核验（**已读到全文** ✓）

```
$$\text{A. Boruchovsky, T. Etzion, R. M. Roth, \textit{On Nearly Perfect Covering Codes}, IEEE Trans.\ IT }\textbf{71(4) 2494--2504 (2025)}\ ✓;\ \text{DOI }10.1109/TIT.2025.3528303\ ✓$$
$$\text{全文版本}: \textbf{arXiv:2405.00258v2}\ (2024\text{-}10\text{-}06,\ 24\ \text{页},\ 55{,}464\ \text{字符})\ ✓\ \text{—— 已逐字抽取 ✓}$$
```

## §2 逐字陈述（五条 ✓）

```
$$\textbf{NP1CC 定义}（\text{摘要逐字}\ ✓）:\ \textit{"A related bound for covering codes is known as the van Wee bound. }\textbf{Codes that meet this bound will be called nearly perfect covering codes.}\textit{"}\ ✓$$
$$\textbf{over-covering 定义}（\text{§II 逐字}\ ✓）:\ \textit{"The over-covering of a subset }Y\subseteq\mathbb F_2^n\textit{ (with respect to a 1-covering code }C\textit{) is defined by }\sum_{y\in Y}(|B_1(y)\cap C|-1)"\ ✓$$
$$\textbf{Lemma 1}（\text{逐字}\ ✓）:\ \textit{"Let }C\textit{ be an }(n,M)\textit{ NP1CC and let }x\in\mathbb F_2^n\setminus C\textit{ be a non-codeword. Then }B_1(x)\textit{ contains }\textbf{exactly one word that is covered by two codewords}\textit{ of }C\textit{ and }\textbf{no word that is covered by more than two codewords}\textit{ of }C\textit{"}\ ✓$$
$$\textbf{Corollary 2}（\text{逐字}\ ✓）:\ \textit{"For every non-codeword }x\in\mathbb F_2^n\setminus C,\ |B_1(x)\cap C|\le2\textit{"}\ ✓\quad(\text{=2 者称 }\textbf{midword}\ ✓)$$
$$\textbf{Theorem 3}（\text{逐字}\ ✓）:\ \textit{"For every non-codeword }x,\ |B_2(x)\cap C|=\tfrac n2+1\textit{"}\ ✓\ \Longrightarrow\ n=8:\ \mathbf{5}\ ✓$$
$$\textbf{Theorem 6}（\text{逐字}\ ✓）:\ \textit{"For every codeword }c\in C,\ |B_2(c)\cap C|=2\textit{"}\ ✓\ \Longrightarrow\ \text{每码字有\textbf{唯一 partner}}\ ✓\ (16\ \text{对}\ ✓,\ \text{Type I/II}\ ✓)$$
```

## §3 **翻译表**（同一坐标系，非相似 ✓）

```
$$\begin{array}{c|c|c}
\text{NP1CC 文献} & \text{我方} & \text{关系}\\
\hline
f(x)=|B_1(x)\cap C| & b(x)=|C\cap B_1(x)| & \textbf{同一个量}\ ✓\\
\text{over-covering }\sum_{y\in Y}(f(y)-1) & \text{excess }\sum_{y\in Y}e(y),\ e=b-1 & \textbf{同一个量}\ ✓\\
\mid\text{midword} & b(x)=2\ \text{的非码字} & \text{同一}\ ✓\\
\partial B_2(x)\ \text{/ partner} & d(c,c')\le2\ \text{的唯一近邻} & \text{同一}\ ✓\\
\text{van Wee 界取等} & E=(n+1)M-2^n\ \text{型等式} & \text{一致}\ ✓\\
\end{array}$$
```

## §4 **b ≤ 2 的两情形闭环**（我方语言 ✓，**本档核心**）

```
$$\textbf{情形 I}（x\notin C）:\ \text{Corollary 2}\ ✓\ \Longrightarrow\ b(x)\le2\ ✓$$
$$\textbf{情形 II}（c\in C）:\ \text{Theorem 6}\ \text{给}\ |B_2(c)\cap C|=2;\ \text{而}\ B_1(c)\subseteq B_2(c)\ ✓\ \Longrightarrow\ b(c)=|B_1(c)\cap C|\le2\ ✓$$
$$\Longrightarrow\ \boxed{b(x)\le2\quad\forall x\in\mathbb F_2^8}\ ✓✓\ \Longrightarrow\ Q=\sum_x\binom{b(x)-1}{2}=\boxed{0}\ ✓✓\ \Longrightarrow\ \boxed{\textbf{Q}^*(8)=0}\ ✓✓$$
$$\text{（\textbf{一次源逐字}支撑 ✓；且 }(8,32)\ \text{属 NP1CC 因}\ 32=2^8/8\ \text{取 van Wee 等号}\ ✓)$$
```

## §5 附带结构（比 b≤2 更强 ✓）

```
$$\sum_x(b-1)=E=32\ \text{＋}\ b\in\{1,2\}\ \Longrightarrow\ \textbf{恰 }32\ \text{个 }b=2\ \text{点 ＋ }224\ \text{个 }b=1\ \text{点}\ ✓$$
$$A_1+A_2=\frac{E+Q}{2}=\frac{32}{2}=\mathbf{16}\ ✓\ (\text{与 doubled Hamming 实测一致}\ ✓✓)$$
$$\text{每码字唯一 partner} \Longrightarrow 32/2=\mathbf{16}\ \text{对}\ ✓;\ \ \forall x\notin C:\ |B_2(x)\cap C|=\mathbf{5}\ ✓$$
$$\textbf{对 }\delta=(2,2)\ \text{坏型的影响}: b\le2\ \Longrightarrow\ \text{不存在 }\delta\ge2\ \text{的点}\ \Longrightarrow\ \textbf{该坏型被直接消解}\ ✓✓\ (\text{无需额外几何论证}\ ✓)$$
$$\textbf{推广}: n=2^m\ \text{时}\ nM\ge2^n\ \text{且}\ K=2^n/n\ \Longrightarrow\ \text{NP1CC}\ \Longrightarrow\ \textbf{Q}^*(n)=0\ ✓\ (\text{自检 }n=2,4\ \text{吻合 ✓✓})$$
```

## §6 三张表（更新 ✓）

```
$$\textbf{CLOSED}: \ldots;\ \boxed{b\le2}\ (\text{一次源 Lemma 1/Cor 2 ＋ Thm 6}\ ✓);\ \boxed{Q^*(8)=0}\ ✓;\ n=2^m\Rightarrow Q^*(n)=0\ ✓;\ \text{profile}(224,32)\ ✓;\ A_1+A_2=16\ ✓$$
$$\textbf{EVIDENCE}: \text{solver 结果（已退居后台 ✓）};\ \text{doubled Hamming 单例}\ ✓$$
$$\textbf{RETRACTED}: \text{"n=8 适用三进制同余"}\ ✗$$
$$\textbf{OPEN}: \text{非 }n=2^m\ \text{的 }Q^*(n)\ \text{规律};\ K(2^m,1)\ \text{逐字出处（补引用）};\ \textbf{n=10, M=119: UNKNOWN}\ ✓$$
```

## §7 边界（诚实标注）

- §1–§2 全为**一次源逐字**（arXiv:2405.00258v2 ✓）；**无**转述依赖 ✓
- §4–§5 为**我方翻译与推导** ✓（两情形均给出出处 ✓）
- **本档未使用任何 solver 结果** ✓；**未**对非 2^m 情形外推 ✗；**未**触碰 119 ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 翻译引理     命中文件数=0    :: 
技术词 覆盖数有界  命中文件数=0    :: 
技术词 伙伴对结构  命中文件数=0    :: 
技术词 过量覆盖同坐标 命中文件数=0    ::
```

- **本档新增**（命中数=0）：翻译引理、覆盖数有界、伙伴对结构、过量覆盖同坐标
- **档案已有（引用，不列为提出）**：—
