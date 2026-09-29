# CALIBRATE-n6（2026-09-29）—— **A-3：双侧 defect 闭环\ \textbf{排除 }$M{=}11$，给出 $K(6,1)\ge12$（\textbf{非}阈值律之功）**

> **性质**：**能力校准链（A-3，$n{=}6$）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 16:0x ✓
> **唐先生令**：开 A-3，附硬门槛（**不得把阈值律当证明**）✓

**已查地图**：`CALIBRATE-n5`／`CALIBRATE-n5-b`（packing 阈值律）✓

D0: 本档对象 ＝ **档案已有**（纤维对／defect——皆经典 ✓）
D1: 0（产出＝**一次成功的双侧排除 ＋ 一门槛之正面满足 ＋ 一代价之量化** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ }M{=}11\ \textbf{全部排除}\Longrightarrow \boxed{K(6,1)\ge12}\ (\text{已知值复现})}$$
$$\boxed{\text{② ✓ 且\ \textbf{非}阈值律之功}:\ \text{排除 }a\in\{5,6\}\ \text{用的是\ \textbf{双侧闭环}（}|D_A|\le b\ \text{＋ }B\ \text{覆盖 }V\setminus A\text{）}}$$
$$\boxed{\text{③ ✓ }a\le4\ \text{与}\ a\ge7\ \text{之排除\ \textbf{确是}容量级}（|D_A|\ge32-6a\Rightarrow a\ge5;\ \text{对称地 }b\ge5）}$$
$$\boxed{\text{④ ✗ 代价}:\ n{=}6\ \text{可行}（1.1{\times}10^6）；n{=}7\ \text{需 }C(64,{\sim}7)\approx6{\times}10^8\ ✗\Longrightarrow \text{不能直推 }n{=}9}$$

## §1 ① 分层（**✓ 先省一半枚举**）

$$\text{纤维}:\ \mathbb F_2^6=\mathbb F_2^5\times\mathbb F_2,\ V=Q_5\ (32\ \text{点}),\ \text{球 }6\ \text{点},\ M=a+b$$
$$|D_A|=32-|N_1(A)|\ \ge\ 32-6a;\quad \text{需 }|D_A|\le b=11-a\ \Longrightarrow\ 21\le5a\ \Longrightarrow\ \boxed{a\ge5}$$
$$|D_B|=32-|N_1(B)|\ \ge\ 32-6b;\quad \text{需}\le a\ \Longrightarrow\ \boxed{b\ge5}$$
$$\therefore\ M{=}11\ \Longrightarrow\ a,b\in\{5,6\}\ \text{仅两情形}✓\ (\text{此步确为容量级，如你所述})$$

## §2 ② 双侧闭环（**✓ 真正的承重者**）

$$\text{条件}:\ N_1(A)\cup B=V\ \wedge\ N_1(B)\cup A=V\iff D_A\subseteq B,\ D_B\subseteq A$$
$$\text{对给定 }A:\ \text{需 }B\supseteq D_A,\ |B|=11-a,\ \text{且}\ V\setminus A\subseteq N_1(B)$$
$$\therefore\ \text{令 }R:=(V\setminus A)\setminus N_1(D_A);\quad \text{需}\ \underbrace{\mathrm{min\_cover}(R)}_{\text{精确}}\ \le\ (11-a)-|D_A|✓$$

## §3 ③ 全枚举结果（**✓✓ 零候选**）

| $a$ | $b$ | $\binom{32}{a}$ | 过 $\lvert D_A\rvert\le b$ | 过计数筛 $\lvert R\rvert\le6(b{-}\lvert D_A\rvert)$ | **候选** |
|---|---|---|---|---|---|
| $5$ | $6$ | $201{,}376$ | $5{,}760$ | $0$ | $\mathbf{0}$ |
| $6$ | $5$ | $906{,}192$ | $73{,}680$ | $2{,}640$ | $\mathbf{0}$ |

$$\textbf{自检}:\ |A|{=}1\Rightarrow|D_A|{=}26\ (=32{-}6)✓$$
$$\therefore\ \boxed{\text{全部 }(a,b)\ \text{情形皆无可行对}\Longrightarrow M{=}11\ \text{不可行}\Longrightarrow K(6,1)\ge\mathbf{12}}✓✓$$

## §4 ④ 门槛之正面满足（**✓ 按你要求**）

$$\text{阈值律＋容量（仅此二者）对 }n{=}5\ \text{只给 }6\ (<7)✓\Longrightarrow \text{它本身\ \textbf{不足}}$$
$$\text{本档之排除\ \textbf{不是}阈值律所得}:\ \text{用的是 }|D_A|\le b\ \text{＋「}B\ \text{覆盖 }V\setminus A\text{」之\ \textbf{完整纤维对条件}}$$
$$\qquad\text{尤其 }a{=}6\ \text{时 }2{,}640\ \text{例需\ \textbf{精确覆盖检查}方被拒}\ \Longrightarrow \text{承重者为闭环，非局部律}✓$$

## §5 ⑤ 代价（**✗ 无法直推 $n{=}9$**）

$$n{=}6:\ 1{,}107{,}568\ \text{子集},\ 3\ \text{s}✓;\qquad n{=}7:\ C(64,7)\approx6.2\times10^8\ ✗;\qquad n{=}8,9:\ \text{不可行}✗$$
$$\therefore\ \boxed{\text{机制\ \textbf{可传递}（}n{=}5\to n{=}6\text{ 成功），但\ \textbf{代价爆炸}};\ \text{欲至 }n{=}9\ \text{须\ \textbf{压缩}（对称性约化／defect 结构律）}}$$

## §6 下一步（**供唐先生定**）

$$\textbf{A-1}:\ \text{求 }\mathrm{Def}(m,k)\ \text{之精确结构律}（Q_5:\ k{=}5\to4,\ k{=}6\to6;\ \text{试 }\mathrm{Def}=f(k-A(m,3))）\ \text{以\ \textbf{替代}枚举✓$$
$$\textbf{B}:\ \text{对称性约化}\ \text{把 }C(64,7)\ \text{压到可控}（6\text{-cube 等距群阶 }2^7\cdot8!=5{,}160{,}960）✓$$
$$\textbf{C}:\ \text{接受：机制可传递但不可放大};\ \text{归档本链}✓$$

## §7 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "双侧闭环排除M11" "K61下界复现" "代价增长"
技术词 双侧闭环排除M11  命中文件数=0    ::
技术词 K61下界复现     命中文件数=0    ::
技术词 代价增长       命中文件数=0    ::
```

## §8 边界（硬 ✓）

- **全枚举（$\binom{32}{5}$ ＋ $\binom{32}{6}$）＋ 自检 ＋ 精确覆盖检查** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓
- **含我自身 bug 之更正**（全掩码误写 $V{-}1$，已修 $(1{\ll}V){-}1$；今日第三次同类错）✓；**不主张** $K(6,1)$ 之值有疑 ✗
