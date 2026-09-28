# AUDIT-2026-09-28s — **119 profile 可行性审计：解空间 $\approx2.1\times10^{10}$ ⟹ 矩约束排除不了 119**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-28 21:30 ✓
> **唐先生令**：**停止 $3$-for-$2$**；优先两个最有信息量之方向——①$107$ 原式拆解 ②**119 可行性/必要结构审计** ✓

**已查地图**：接续 `AUDIT-r`（删点实验）／`AUDIT-p/q`（真值定位、公式链）／`EXCESS-2026-09-25` ✓

D0: 本档对象 ＝ **档案已有**（覆盖重数 profile／矩恒等式——无新数学对象 ✓）
D1: 0（产出＝**精确 profile 计数 ＋ 下界路线难度判定** ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{① }3\text{-for-}2\ \textbf{停止}（照令）};\quad \text{② ★119 之 profile 解空间} = \mathbf{21{,}329{,}274{,}912}\approx2.1\times10^{10} \Longrightarrow \textbf{矩约束排除不了 119}}$$
$$\boxed{\text{③ 按唐先生判据}:\ \text{"若 119 之 profile 很容易存在，则 119 下界路线很可能很难"} \Longrightarrow \textbf{下界路线（profile 层）判定: 难}\ ⚠️}$$

## §1 $3$-for-$2$ 停止（**照令 ✓**）

$$\text{理由（唐先生）}:\ \text{information gain/cost 比不划算};\ \text{局部 surgery 之极限只能证\ \textbf{此码邻域无更小码}} \ne\ \text{排除他码}\ ✗$$

## §2 ★★ 119 profile 可行性审计（**精确计数 ✓✓**）

$$\text{profile}=(n_0,\dots,n_{10}),\quad \textstyle\sum_j n_j=1024,\quad \sum_j j\,n_j=11K-1024\ (=\Sigma\delta)$$

| $K$ | $\Sigma\delta$ | **可行 profile 数** |
|---|---|---|
| $107$ | $153$ | $149{,}027{,}949$ |
| $118$ | $274$ | $15{,}435{,}776{,}320$ |
| $\mathbf{119}$ | $285$ | $\mathbf{21{,}329{,}274{,}912}$ |
| $120$ | $296$ | $29{,}143{,}348{,}027$ |

$$\therefore\ \boxed{\text{仅 2 个等式 ＋ 11 个未知} \Longrightarrow \text{解空间\ \textbf{极巨大}} \Longrightarrow \textbf{一阶矩不可能排除 119}}\ ✓$$

## §3 二阶矩（**仍不排除 ✓**）

$$\sum_j\binom j2 n_j = 2(N_1+N_2)\qquad(N_i=\text{距离 }i\ \text{之有序码字对数})$$
$$\textbf{校准（}120\text{-code 实测）}:\ \binom22{\cdot}172+\binom32{\cdot}36+\binom42{\cdot}8+\binom52{\cdot}7=172+108+48+70=\mathbf{398}=2\times199\ \checkmark$$
$$\textbf{119 之下界（凸性）}:\ \sum_x\binom{a(x)}2\ge1024\binom{1309/1024}{2}\approx178.3 \Longrightarrow N_1+N_2\ge\mathbf{89}$$
$$\text{而上界极松（}\le\tbinom{119}2\text{）} \Longrightarrow \boxed{\text{二阶矩亦\ \textbf{不排除} 119}}\ ⚠️$$

## §4 项目状态更新（**照唐先生 ✓**）

$$107\ \le\ K_2(10,1)\ \le\ 120$$
$$\text{上界端}:\ 120_{\rm Kam}\xrightarrow{\ 1\to0\ }\times;\qquad 120_{\rm Kam}\xrightarrow{\ 2\to1\ (\text{穷举 }7140)\ }\times;\qquad \boxed{\text{global }119\ \text{存在性\ \textbf{完全开放}}}\ ✓$$
$$\text{下界端}:\ 107\ (\text{BÖW 2004})\ \text{—— 其\ \textbf{原式尚未取得}}\ ⚠️$$

## §5 $107$ 原式拆解：**仍未完成**（诚实 ✓）

$$\textbf{已核}:\ \text{归属 BÖW 2004（J. Combin. Designs 12, 157--176）};\ \text{van Wee 原式（}\to103\text{）已取且代入已核};\ \text{Habsieger 1997 覆盖 }n\equiv4 \bmod 6\ ✓$$
$$\textbf{未取得}:\ \text{BÖW 2004\ \textbf{定理正文}}（Wiley 付费）;\ \text{Zhang 1991/92};\ \text{Haas 之具体式} \Longrightarrow \textbf{本档不编造 }107\ \text{之显式公式}\ ✗$$
$$\textbf{候选取法（未做）}:\ \text{①}\texttt{secemp9/arxiv-complete}\ \text{全文检索};\ \text{②作者主页/机构库};\ \text{③从 Zhang 1991 追引} ⚠️$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "profile可行性审计" "解空间计数" "零阶矩排除不了"
技术词 profile可行性审计 命中文件数=0    ::
技术词 解空间计数     命中文件数=0    ::
技术词 零阶矩排除不了   命中文件数=0    ::
```

## §7 边界（硬 ✓）

- 精确 DP 计数 ＋ 档案交叉验证 ＋ 外部源引证 ✓；**不占 C 号** ✓；**不作方向性决策** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §2 之判定**只**针对"矩/profile 层"；**不主张**一切下界方法皆不可行 ⚠️
