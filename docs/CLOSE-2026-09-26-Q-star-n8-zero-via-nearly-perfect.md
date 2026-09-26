已查地图：已跑 scripts/prework_map_check.sh nearly-perfect Boruchovsky van Wee (8,32)_1 Q* ⟹ 执行自 CONGRUENCE-2026-09-26 档；本档为**文献结构定理 → 我方语言翻译完成**（唐先生 2026-09-26 12:06 指令）；纯推导，未动 solver ✓。
D0: 本档对象 = (8,32)_1 码的覆盖重数上界（经 nearly-perfect 定理）
D1: 1（新增独立结论：**Q*(8)=0**，并推广为所有 n=2^m ✓）

# CLOSE-2026-09-26 · Q*(8)=0（文献定理链）

## §1 第一步：van Wee 界的**精确形式**（逐字 ✓）

```
$$\text{van Wee (1988)}（\text{经 Struik 1994 简化，逐字引自 arXiv:2608.12595}\ ✓）:$$
$$M\Bigl(\sum_{i=0}^{R}\binom{n}{i}-\frac{\binom{n}{R}}{\lceil\frac{n-R}{R+1}\rceil}\Bigl(\bigl\lceil\tfrac{n+1}{R+1}\bigr\rceil-\tfrac{n+1}{R+1}\Bigr)\Bigr)\ \ge\ 2^{n}\qquad(5)\ ✓$$
$$\textbf{代入 } n=8,\ R=1:\ \sum_{i=0}^{1}\binom{8}{i}=9;\quad \frac{\binom{8}{1}}{\lceil 7/2\rceil}\Bigl(\lceil 9/2\rceil-\tfrac92\Bigr)=\frac{8}{4}\cdot\tfrac12=1$$
$$\Longrightarrow\ M\,(9-1)=8M\ \ge\ 256\ \Longrightarrow\ \boxed{M\ \ge\ 32}\ ✓\ \text{（与 }K(8,1)=32\ \text{精确一致 ✓）}$$
$$\text{更一般（偶数 }n\text{）}:\ \lceil(n-1)/2\rceil=n/2,\ \lceil(n+1)/2\rceil=n/2+1\ \Longrightarrow\ \text{修正项}=1\ \Longrightarrow\ \boxed{nM\ge2^n}\ ✓$$
$$\Longrightarrow\ \text{当 }n=2^m\ \text{且 }K(n,1)=2^n/n\ \text{时},\ (5)\ \textbf{取等}\ ✓$$
```

## §2 第二步：nearly-perfect 的定义（**逐字** ✓）

```
$$\text{arXiv:2608.12595 摘要逐字}:\ \textit{"nearly-perfect covering codes, which are codes that }\textbf{attain the Van Wee bound with equality}\textit{"}\ ✓$$
$$\Longrightarrow\ (8,32)_1\ \text{码满足 }8\cdot32=256\ \text{（取等}\ ✓) \Longrightarrow\ \textbf{是 nearly-perfect}\ ✓$$
$$\text{（并注: 该文 Definition 2.10 另有 refined 版本 } (14);\ \text{但与 (5) 在 }\lceil d/2\rceil=1\ \text{时一致}\ ✓\ —— \text{我方用\textbf{原始定义}，绕开循环性}\ ✓）$$
```

## §3 第三步：结构引理（**逐字** ✓，本轮关键）

```
$$\textbf{Lemma 3.18}（\text{arXiv:2608.12595 §3}\ ✓）:\ \textit{"If }C\text{ is an }(n,M,d)_R\ \text{nearly-perfect covering code, and }z\in\mathbb{F}_2^n\text{ is }\textbf{over-covered}\textit{, then it is covered by }\textbf{exactly two}\textit{ codewords, }c\text{ and }c^{\prime}"\ ✓$$
$$\text{（并逐字注明: \textit{"by instantiating Lemma 3.16 with }R=1\text{ we obtain (Boruchovsky et al., 2025, }\textbf{Theorem 3}\textit{) as a Corollary"}\ ✓）$$
$$\textbf{over-covered 的定义（逐字} ✓）:\ \lvert B_R(x)\cap C\rvert\ \ge\ 2\ ✓\ \Longrightarrow\ R=1\ \text{时即}\ b(x)\ge2\ ✓$$
```

## §4 第四步：翻译到我方语言（**结论** ✓✓）

```
$$\text{由 } b(x)\ge1\ (\text{覆盖}\ ✓)\ \text{与}\ b(x)\ge2\Rightarrow b(x)=2\ (\text{Lemma 3.18}\ ✓)$$
$$\Longrightarrow\ \boxed{b(x)\in\{1,2\}\ \forall x\in\mathbb{F}_2^8}\ ✓\ \Longrightarrow\ Q=\sum_x\binom{b(x)-1}{2}=\sum_x\binom{\delta(x)}{2}=\boxed{0}\ ✓✓$$
$$\Longrightarrow\ \boxed{\textbf{Q}^*(8)=0}\ ✓\ \text{（\textbf{文献支撑的定理}，非计算证据}\ ✓)$$
$$\text{附}: A_1+A_2=\frac{E+Q}{2}=\frac{32+0}{2}=\boxed{16}\ ✓\ \text{（与 doubled Hamming 的 }A_1+A_2=16\ \text{一致}\ ✓✓）$$
```

## §5 推广（**同一机制覆盖整族** ✓）

```
$$\text{对 }n=2^m:\ \text{van Wee 化为 }nM\ge2^n;\ \text{又 }K(2^m,1)=2^{2^m-m}=2^n/n\ \Longrightarrow\ \textbf{取等}\ \Longrightarrow\ \text{nearly-perfect}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{对一切 }n=2^m,\ b(x)\in\{1,2\}\ \Longrightarrow\ Q^*(n)=0}\ ✓✓$$
$$\text{（对方: }n=2,4,8,16,32,\dots\ ✓;\ \text{其 }E=(n+1)M-2^n = 2^n/n - 2^n + 2^n\ \text{型 hmm}）$$
$$\text{数值自检}: n=2:\ E=2\cdot3-4=2,\ Q^*=0\ ✓\ (\text{我方早期实算 ✓});\quad n=4:\ E=4,\ Q^*=0\ ✓\ (\text{我方穷举 40 个 ✓✓})$$
$$\Longrightarrow\ \textbf{独立数据与定理一致}\ ✓✓\ (\text{两条独立路径汇聚}\ ✓)$$
```

## §6 诚实缺口（按 AMEND-29/30 ✓）

```
$$\text{⚠️ 二次源}: \text{Boruchovsky et al.\ Theorem 3 的陈述我方经 }\textbf{arXiv:2608.12595 转述}\ \text{得到}\ ✓;\ \textbf{一次源未读}\ ✗$$
$$\qquad \text{一次源 = A. Boruchovsky, T. Etzion, R. M. Roth, \textit{On nearly perfect covering codes}, IEEE Trans.\ IT }\textbf{71(4) 2494--2504 (2025)}\ ⚠️$$
$$\text{⚠️ 待核}: K(2^m,1)=2^{2^m-m}\ \text{为文献已知}\ ✓\ (\text{如 }K(8,1)=32\ ✓,\ K(16,1)=4096\ ✓)\ \text{—— 逐字出处待补}\ ⚠️$$
$$\text{（以上两项属"待补引用"，不影响本次逻辑链的\textbf{结构}成立}\ ✓\ \text{但正式引用前须补齐}\ ✓）$$
```

## §7 三张表更新

```
$$\textbf{CLOSED}: E=32;\ \sum_i\delta_i(x)=32;\ \sum\delta^2\equiv0\ (\mathrm{mod}\ 4);\ \text{单点 }m{=}3/4/7/8\ \text{不可行};\ \text{WLOG 三式};\ d\le2;\ \boxed{b\le2\Rightarrow Q^*(8)=0}\ ✓$$
$$\qquad\qquad \textbf{推广}: n=2^m\Rightarrow Q^*(n)=0\ ✓$$
$$\textbf{EVIDENCE}: \text{CP-SAT 18.5M 冲突无解};\ \text{案 A/B 后台（已无主线地位 ✓）};\ \text{doubled Hamming }Q=0\ ✓$$
$$\textbf{RETRACTED}: \text{"n=8 适用三进制同余"}\ ✗\ (\text{Habsieger 条件 }6\mid n\ ✗)$$
$$\textbf{OPEN}: \text{一次源核验（Boruchovsky）};\ K(2^m,1)\ \text{逐字出处};\ n\ne2^m\ \text{的 }Q^*(n)\ \text{规律};\ \textbf{n=10, M=119: UNKNOWN}\ ✓$$
```

## §8 边界（诚实标注）

- §1 的 (5) 为**逐字**（arXiv:2608.12595 ✓）；n=8 代入为**我方算术** ✓（8M ≥ 256 ✓）
- §3 引理为**二次源逐字** ✓（一次源待补 ⚠️）
- **本档未用任何 solver 结果** ✓；solver 仅列 EVIDENCE ✓
- **未**触碰 119 ✗；**未**对非 2^m 情形外推 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 nearly-perfect 定理链 命中文件数=0    :: 
技术词 覆盖数上界翻译 命中文件数=0    :: 
技术词 幂次长度族  命中文件数=0    :: 
技术词 二次源标注  命中文件数=0    ::
```

- **本档新增**（命中数=0）：覆盖数上界翻译、幂次长度族、二次源标注
- **档案已有（引用，不列为提出）**：—
