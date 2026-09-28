# WITSUB-2026-09-28 — **C-543：$k$-子空间覆盖不等式 ＋ 其\ \textbf{相对已有约束的独立性}（肯定回答）**

> **范围（照唐先生 2026-09-28 20:03 令 ✓）**：把已有约束当 baseline $\mathcal F_{\rm old}$，问"哪条 Haas 不等式\ $\notin\operatorname{span}(\mathcal F_{\rm old})$"；**不作路线裁定** ✗。空间 B ✓

**已查地图**：承 C-541／C-542／`FACE-2026-09-26`／`EXCESS-2026-09-25`／`M2-PREWORK-2026-09-27` ✓

D0: 本档对象 ＝ **档案已有**（子空间占据 $N_U$／覆盖计数——$N_U$ 属既有变量族 ✓，无新数学对象）
D1: 1（**首次给出 $k$-子空间覆盖恒等式 $(k{+}1)N_U{+}N_{U,1}{=}\sum_{u\in U}c_u$ ＋ 覆盖式 $\ge2^k$ ✓✓ ＋ 首次以\ \textbf{平移敏感性}证明 $N_U,N_{U,1}\notin\operatorname{span}(A_i)$ ✓✓（＝肯定回答唐先生之问）**）
[R]

---

## §0 结论

$$\boxed{\textbf{(答)}:\ \text{存在。}k\text{-子空间覆盖不等式\ \textbf{不在} } \operatorname{span}(\mathcal F_{\rm old})\ \textbf{之内}\ ✓✓\ \text{（§3 证）}}$$
$$\text{但}\ \boxed{\text{其经典机制家族之上限为 }103\text{–}107\ (<120)\ \text{（§4）}}$$

## §1 恒等式与本不等式（**本档自推 ＋ 数值核验 ✓**）

取 $U$ ＝ 由坐标子集 $S\subset[10]$（$|S|{=}k$）张成的 $k$-维子空间。对任一码字 $c$：

$$|U\cap B_1(c)|=\begin{cases}k+1,&c\in U\\ 1,&d(c,U)=1\\ 0,&d(c,U)\ge2\end{cases}$$

双重计数 $\sum_{u\in U}c_u=\sum_{c\in C}|U\cap B_1(c)|$ 得

$$\boxed{\sum_{u\in U}c_u=(k+1)N_U+N_{U,1}},\qquad N_U:=|C\cap U|,\quad N_{U,1}:=\#\{c:d(c,U)=1\}$$

由覆盖 $c_u\ge1$（$\forall u$）得 **$k$-子空间覆盖不等式**：

$$\boxed{(k+1)N_U+N_{U,1}\ \ge\ 2^k}$$

**数值核验（$K{=}135$ 码，恒等式全部精确成立 ✓）**

| $k$ | $(k{+}1)N_U+N_{U,1}$ | $2^k$ | slack |
|---|---|---|---|
| $2$ | $10$ | $4$ | $6$ |
| $3$ | $15$ | $8$ | $7$ |
| $4$ | $27$ | $16$ | $11$ |
| $5$ | $52$ | $32$ | $20$ |

（$k{=}10$ 退化即球覆盖：$11K\ge1024\Rightarrow K\ge93.09$ ✓）

## §2 ★ 独立性（**肯定回答唐先生之问 ✓✓**）

$$\textbf{判据}:\ A_i\ \text{平移不变}\ \big(d(s{+}v,t{+}v){=}d(s,t)\big);\quad N_U,N_{U,1}\ \textbf{平移敏感}\ \big(U\ \text{为坐标子空间}\big)$$

**数值实例**：$C\mapsto C{+}e_9$：

$$A_i\ \textbf{完全相同}\ ✓;\qquad N_{U,1}:\ 7\ \longrightarrow\ 10\ \textbf{（变）}\ ✓$$

$$\therefore\ \boxed{N_U,N_{U,1}\ \notin\ \operatorname{span}(A_i)}\ \Longrightarrow\ \boxed{k\text{-子空间覆盖不等式}\ \notin\ \operatorname{span}\big(\mathcal F_{\rm old}^{A_i}\big)}\ ✓✓$$

**说明**：$A_i$／$\delta$-moments／`FACE` 之 $q_F$ 归约（$9A_1{+}A_2$）皆 $A_i$-型 ⟹ 皆不能线性推出本不等式 ✓

## §3 诚实上限（**关键限制**）

$$\text{本档推导只用 } c_u\ge1\ \text{（即 }\delta\ge0\text{）}\ \Longrightarrow\ \textbf{弱}\ \text{（slack 大）}$$
$$\text{经典强化（van Wee／Habsieger／Haas）用\ \textbf{excess 同余} }\ \delta_i\ge(\cdots)\ \text{把上式收紧}$$
$$\text{已知到达}:\ \lceil2^n/n\rceil=103\ (\text{van Wee 1988})\ <\ 107\ (\text{B\"OW 2004})\ \ll\ 120$$

$$\therefore\ \boxed{\text{$k$-子空间族\ \textbf{独立，但经典上限 107}}}\ \text{（仍未到 120）}$$

## §4 阻塞项（诚实标注 ⚠️）

Haas 2002 正文 **不可得**（ScienceDirect PDF 403 ✗）；**无法逐条枚举其不等式** ✗。本档之不等式为**自第一原理解析重建** ✓，非逐字引用 ✗。

## §5 结论与建议

$$\boxed{\text{唐先生之问}\ \text{（存在性）}:\ \textbf{YES}\ \text{——}k\text{-子空间覆盖不等式确实\ \textbf{独立于} }\mathcal F_{\rm old}\ ✓✓}$$
$$\text{但其\textbf{经典天花板＝107} ⟹ 要冲 }120\text{ 必须在\ \textbf{子空间不等式 × 119-专属结构} 的\textbf{耦合}里取增益}}$$

**建议下一轮（窄）**：取最小的 $k{=}3$ 情形，把 $N_U,N_{U,1}$ 与 119-结构（$|C|{=}119$、$\sum\delta{=}285$、`FACE` 之 $q_F$）**联合**求一个带整性/同余的界；**若一轮内无增益 ⟹ Haas 线亦关闭** ✗（不无限算）。

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "子空间覆盖不等式" "独立性判据" "平移敏感"
技术词 子空间覆盖不等式 命中文件数=0    ::
技术词 独立性判据  命中文件数=0    ::
技术词 平移敏感     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- 有限穷举（$K{=}135$）＋ 初等双重计数 ✓；未上 SDP/SAT ✗；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- 本档**不主张**已达 120，亦不主张 Haas 线已死（§5 给出单轮判据）✓
