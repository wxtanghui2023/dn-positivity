# CALIBRATE-n5（2026-09-29）—— **defect 递归\ \textbf{精确复现} $K(5,1){=}7$；且\ \textbf{首个非线性出现在 }|A|{=}3$**

> **性质**：**能力校准链（n=5 一级）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 15:3x ✓
> **唐先生令**：开 defect-set recursion；先 $n=5\to8$ 校准，攻 $M{=}K(n,1){-}1$ ✓

**已查地图**：`CALIBRATE-K9*`（纤维层封顶 52）✓

D0: 本档对象 ＝ **档案已有**（defect set／纤维对——皆经典 ✓）
D1: 0（产出＝**一次精确复现 ＋ 首个非线性之定位 ＋ 容量单独不足之证明** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ defect 递归\ \textbf{精确复现} }K(5,1)=\mathbf{7}:\ \min_{A}\bigl(|A|+\mathrm{minB}(A)\bigr)=7\ (\text{取到者 }|A|{=}3,\ |D_A|{=}3,\ |B|{=}4)}$$
$$\boxed{\text{② ★★ 首个\ \textbf{非线性}出现在 }|A|{=}3:\ \min|D_A|=\mathbf{3}\ \text{vs 容量界 }1\ (\textbf{+2})}$$
$$\boxed{\text{③ ✓ 该非线性\ \textbf{承重}}:\ \text{仅用容量界会给 }\mathbf{4}\ (<7)\Longrightarrow \text{非线性不可省}}$$
$$\boxed{\text{④ ✗ 但代价}:\ 2^{\,2^{\,n-1}}\ \text{级枚举}\Longrightarrow n{\ge}6\ \text{不可行}\Longrightarrow \textbf{无压缩}}$$

## §1 ① 精确复现（**✓✓**）

$$\text{设定}:\ n{=}5,\ \mathbb F_2^5=\mathbb F_2^4\times\mathbb F_2,\ V{=}4\text{-cube}\ (16\ \text{点}),\ \text{每字覆盖 }1{+}4{=}5\ \text{点}$$
$$\text{覆盖}\iff N_1(A)\cup B=V\ \wedge\ N_1(B)\cup A=V\iff D_A\subseteq B,\ D_B\subseteq A\ (D_A{=}V\setminus N_1(A))✓$$
$$\text{精确枚举全部 }2^{16}=65536\ \text{个 }A:\quad \min_A\bigl[|A|+\mathrm{minB}(A)\bigr]=\mathbf{7}✓✓$$
$$\textbf{自检（两道，皆过）}:\ \text{①}|A|{=}1\Rightarrow|D_A|{=}11\ (\text{应 }16{-}5)✓;\quad \text{②}\ \mathrm{min\_cover}(4\text{-cube}){=}4\ ({=}K(4,1))✓$$
$$\therefore\ \boxed{\text{defect 递归在 }n{=}5\ \text{处\ \textbf{复现已知值}}\Longrightarrow\ \text{机制\ \textbf{不是}空转}}✓✓$$

## §2 ② ★ 首个非线性（**✓✓ 本档最重要**）

| $\lvert A\rvert$ | $\min\lvert D_A\rvert$ | $\max\lvert D_A\rvert$ | 容量界 $16{-}5\lvert A\rvert$ | 判定 |
|---|---|---|---|---|
| $0$ | $16$ | $16$ | $16$ | 紧 |
| $1$ | $11$ | $11$ | $11$ | 紧 |
| $2$ | $6$ | $8$ | $6$ | 紧 |
| $\mathbf{3}$ | $\mathbf{3}$ | $6$ | $\mathbf{1}$ | **松（非线性 +2）** |
| $4$ | $0$ | $5$ | $0$ | 紧 |
| $5$ | $0$ | $5$ | $0$ | 紧 |

$$\therefore\ \boxed{\text{首个非线性在 }|A|{=}3:\ \min|D_A|=\mathbf{3}>\text{容量界 }1}\ ——\ \text{即 3 个字\ \textbf{至多覆盖 }13\ \text{点}}✓✓$$
$$\text{根因}:\ \text{4-cube 中任两字的球必重叠}\ \Longrightarrow\ 3\ \text{字的覆盖}\le15-2=13✓$$

## §3 ③ 非线性承重（**✓**）

$$\text{仅用容量}:\ |D_A|\ge16-5a\ \text{与}\ |B|\ge|D_A|:\quad \min_a\bigl[a+\max(1,16-5a)\bigr]=\mathbf{4}\ ✗$$
$$\therefore\ \boxed{\text{容量单独只给 }4;\ \text{真值 }7\ \Longrightarrow\ \text{非线性（缺陷内部结构）\ \textbf{不可省}}}✓✓$$
$$\text{本档之 }\min_A[|A|+\mathrm{minB}(A)]\ \text{已含}\ \text{“}B\ \text{须覆盖 }V\setminus A\text{”之完整信息}\ (=\text{纤维对的\ \textbf{精确}}条件)✓$$

## §4 ④ 代价（**✗ 无压缩**）

$$\text{本档之可行性}:\ 2^{16}=\text{65536}\ \text{个子集（可枚举）}✓$$
$$\text{下一级 }n{=}6:\ 2^{32}\approx4.3\times10^9\ ✗;\quad n{=}7{:}2^{64}\ ✗;\quad n{=}8{:}2^{128}\ ✗;\quad n{=}9{:}2^{256}\ ✗$$
$$\therefore\ \boxed{\text{直接枚举\ \textbf{止步于 }n{=}5};\ \text{要带到 }n{\ge}6,\ \text{必须把"非线性"提炼成\ \textbf{定理/可传递的局部律}}}✓\ (\text{＝唐先生所谓"P1 真机制"})$$

## §5 下一步（**供唐先生定**）

$$\textbf{候选 A}:\ \text{提炼 }|A|{=}3\ \text{之非线性为一般律}（\text{两球必重叠}\to\text{覆盖上界}）;\ \text{试推广到 }n{=}6\ \text{之 5-cube}✓$$
$$\textbf{候选 B}:\ n{=}6\ \text{用\ \textbf{对称性约化}}（\text{4-cube 之等距群阶 }2^5\cdot5!=3840;\ \text{5-cube}\ 2^6\cdot6!=46080）\text{把 }2^{32}\ \text{压到可控}✓$$
$$\textbf{候选 C}:\ \text{改攻 }M{=}K(n,1){-}1\ \text{之\ 直接矛盾（按你原定：}n{=}5\Rightarrow M{=}6\ \text{已排除}\ ✓）✓$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "defect递归复现K51" "首个非线性在|A|=3" "容量单独只给4"
技术词 defect递归复现K51  命中文件数=0    ::
技术词 首个非线性在|A|=3   命中文件数=0    ::
技术词 容量单独只给4     命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **$n{=}5$ 全量精确枚举（$2^{16}$）＋ 两道自检 ＋ 容量对照** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓
- **含我自身 bug 之更正**（全宇宙掩码误写为 $V{-}1$，已修为 $(1{\ll}V){-}1$）✓；**不主张** $K(5,1)$ 之值有疑 ✗
