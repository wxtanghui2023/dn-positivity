# WITC546-2026-09-28 — **C-546：Haas-2002／Plagne 族对 $n{=}10$ 之天花板 $\ll119$（门检）**

> **范围（照唐先生 2026-09-28 20:14 令 ✓）**：condition (15) 门检；**不作路线裁定** ✗。空间 B ✓

**已查地图**：承 C-545（2013 奇偶门）／C-541（阶梯）／`M2-PREWORK-2026-09-27` ✓

D0: 本档对象 ＝ **档案已有**（Haas 2002／Plagne／$K(n,1)$ 阶梯——**无新数学对象** ✓）
D1: 1（**首次取得 Plagne 2009 主定理逐字 ＋ 首次对 $n{=}10$ 重建其主项（$\max\approx94.4$）⟹ 首次判定 Haas-2002／Plagne 族天花板 $\ll119$ ✓✓**）
[R]

---

## §0 判定

$$\boxed{\text{Haas-2002／Plagne 族对 }n{=}10\ \text{之天花板}\ \ll\ 119}\ \text{（与文献记录 }107\ \text{一致）}$$

## §1 Plagne 2009 主定理（**逐字 ✓**）

$$\textbf{Theorem (Plagne 2009).}\ \text{Let }k,r,s\ \text{be positive integers with }1\le k\le n\ \text{and}$$
$$\boxed{s\le2^{n-k}-(n+1)r}$$
$$\text{If }C\ \text{is a code with covering radius }1\ \text{in }A^n\ \text{then}$$
$$|C|\ \ge\ \Bigl(r+\frac{s}{s+k}\Bigr)2^k\ +\ \frac1{s+k}\sum_{i=1}^{r}\Bigl(\Bigl(\frac{s(n-k+1)}{k}+n+1-s-2k\Bigr)i+\frac{s(s-k)}{k}\Bigr)N_i$$

**结构（Plagne §1 逐字）**：$A^n$ 按前缀 $\sigma\in A^k$ 分成 $2^k$ 个平行 $(n-k)$-维子空间；$n_\sigma{=}$ 该块码字数；$W_i{=}\{\sigma:n_\sigma{=}r-i\}$，$N_i{=}|W_i|$ ✓

**condition (15)（Plagne 逐字）**：Haas Thm 2 中"剩余项须为正"的**数值条件**；Plagne 之目的即"always possible to make an optimal choice of parameters"（把该项显式化并在非正时控制其大小）✓

## §2 $n{=}10$ 门检（**本档重建 ✓**）

**主项** $\bigl(r+\frac{s}{s+k}\bigr)2^k$ 之最大（$N_i{\ge}0$ 且系数 $\ge0$ ⟹ 最弱界即 $N_i{=}0$）：

| $k$ | $r$ | $s$ | $2^k$ | 主项 |
|---|---|---|---|---|
| $2$ | $23$ | $3$ | $4$ | $\mathbf{94.4}$ |
| $1$ | $46$ | $6$ | $2$ | $93.7$ |
| $3$ | $11$ | $7$ | $8$ | $93.6$ |
| $6$ | $1$ | $5$ | $64$ | $93.09$ |
| $4$ | $5$ | $9$ | $16$ | $91.08$ |

$$\boxed{\max_{(k,r,s)}\ \Bigl(r+\frac{s}{s+k}\Bigr)2^k\ \approx\ \mathbf{94.4}\qquad(k{=}2,r{=}23,s{=}3)}$$

（Haas 经验最优 $k{=}\lfloor(n{-}1)/2\rfloor{=}4$ 在此反而不最优；$k{=}2$ 更好）

$$\text{阶梯}:\quad \underbrace{93.09}_{\text{球覆盖}}\ <\ \underbrace{94.4}_{\text{Haas-2002 主项}}\ \ll\ \underbrace{103}_{\text{van Wee}}\ <\ \underbrace{107}_{\text{B\"OW 2004 记录}}\ \ll\ \underbrace{119/120}_{\text{目标}}$$

## §3 结论（**三重交叉一致 ✓**）

$$\textbf{(i)}\ \text{主项天花板}\approx94.4\ \ll119\ ✓$$
$$\textbf{(ii)}\ \text{含 }N_i\ \text{修正之全界需实际分布（循环依赖 }K{=}\sum_\sigma n_\sigma\text{）};\ \text{文献\textbf{已实现}水平仅 }107\ \ll119\ ✓$$
$$\textbf{(iii)}\ \text{condition (15) 只影响"参数选择可否最优"，不改变族之量级}\ ✓$$

$$\therefore\ \boxed{\text{Haas-2002／Plagne 路线对 119 无攻击力}}\ \text{（与 C-545 之 2013 线互补封口）}$$

## §4 ⭐ 机制族穷尽（**本档核心结论 ✓**）

$$\boxed{\text{三大已发表机制族皆够不到 }119:}$$

| 机制族 | 对 $n{=}10$ 之水平 | 状态 |
|---|---|---|
| excess／congruence（van Wee／Habsieger／**Haas 2013**） | 退回 $2^n/n{=}103$ | ✗ C-545 奇偶门 |
| subspace linear-inequality（**Haas 2002**／**Plagne 2009**） | 主项 $\approx94.4$，已实现 $\le107$ | ✗ 本档 |
| SDP（Gijswijt 2005／**Gijswijt–Polak 2025**） | $105.2223$ | ✗ C-474 |

$$\Longrightarrow\ \boxed{119\ \text{处于一切已发表机制的\textbf{可达域之外}}}\ ⟹\ \text{我们之 119-专属结构工作确在\ \textbf{前沿}}}$$

## §5 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "块占据分布" "主项天花板" "机制族穷尽"
技术词 块占据分布   命中文件数=0    ::
技术词 主项天花板   命中文件数=0    ::
技术词 机制族穷尽   命中文件数=0    ::
```

## §6 边界（硬 ✓）

- 文献审计（逐字引文）＋ 有限参数穷举（$k\le10$）✓；未上 SDP/SAT ✗；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §4 为"已发表机制"之枚举，**非**"不存在任何机制"（V290 ✓）
- 本档**不主张** Haas 2002 全文已审毕（仅据 Plagne 之复述 ＋ 主定理）⚠️
