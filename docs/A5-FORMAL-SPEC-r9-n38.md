已查地图：命中（`TARGET-L9-q11-four-sources-complete`／`TARGET-L9-q11-source-closure`）⟹ 引用，不开新案
D0: 本档对象 = `A5` 正式规格：`\mathcal F^{(9,38)}=\bigcup_{i=1}^{17}\mathcal F_i` 的变量/约束/群作用（纸面，不求解）
D1: 0 （[REVIEW] 轮次：规格化，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`A5` 正式规格：`\mathcal F^{(9,38)}`**

## §0 规格前提（已闭合的数学对象）

```
$$\text{切片}\ (F,M)=(4,5),\quad r=9,\quad n=38$$ ✓
$$\tau_g(\{a,b,a+b\})=g(a)+g(b)+g(a+b)$$ ✓
$$C_u(g)=\{\tau_g(\ell):u\in\ell\}$$（`\ell` 遍历 `\mathrm{PG}(4,2)` 的线，`2^5-1=31` 个点、`155` 条线）✓
【状态（照录决定性事实）】 `r=9,n=38` 是 **annealing residue**，**不是非存在性证明** ⟹ 本规格要定义的是"**要搜索/要证明什么**"，**不得**把现有 `bestcost=14` 当作排除结论 ✓✓
```

## §1 逐类集合

```
$$\mathcal F^{(9,38)}=\bigcup_{i=1}^{17}\mathcal F_i,\qquad i=1,\dots,17$$ ✓
$$A_i\subset\mathbb F_2^4\setminus\{0\},\quad |A_i|=7,\quad A_i\ \text{1-saturating}$$ ✓
$$B_i=\mathbb F_2^4\setminus(A_i\cup\{0\}),\quad |B_i|=16-7-1=8$$ ✓
$$g:\mathbb F_2^5\setminus\{0\}\to\mathbb F_2^4$$ ✓
【`A_i` 的来源】 17 个 `\mathrm{GL}(4,2)`-canonical representatives（`r9_n38_classes.txt` 的 17 个十六进制 mask；**展开属 `乙`，本档不做**）✓
```

## §2 约束（逐类）

```
**约束 I（fibre 0）**：$$\{0\}\cup A_i\cup(A_i+A_i)=\mathbb F_2^4$$ —— 对 `|A_i|=7` 且 1-saturating 者**已由 `A_i` 的选择自动满足** ✓
**约束 II（fibre `u\ne0`，主约束）**：$$\forall u\in\mathrm{PG}(4,2):\quad B_i\subseteq C_u(g)$$ 等价地 $$\forall(b,u)\in B_i\times\mathrm{PG}(4,2):\ \exists\ell\ni u\ \text{使}\ \tau_g(\ell)=b$$ ✓
【计数】 $$|B_i|\times|\mathrm{PG}(4,2)|=8\times31=248\ \text{条 incidence 约束}$$ ✓✓（与源文件头注逐字一致）✓
【等价形式（源 §2 逐字）】 每个色类 `L_b=\tau_g^{-1}(b)\ (b\in B_i)` 是**覆盖每个点**的线集，且各类**互不相交** ✓
```

## §3 shear 规范化（写进规格）

```
【shear 作用（源 §2 逐字）】 `g\sim g+K`，`K:W\to V` **线性**；`(v,u)\mapsto(v+K(u),u)` **保 `A`**（故保 `B`）✓
【不变量】**`\tau` 是 shear-不变量**：在线 `\{a,b,a+b\}` 上 `K(a)+K(b)+K(a+b)=0` ⟹ $$\tau_{g+K}(\ell)=\tau_g(\ell)$$ ✓✓ ⟹ **真正变量是 `\tau`，不是 `g`** ✓
【规范化】 取 `W` 的基 `e_1,\dots,e_5`，令 $$g(e_j)=0,\quad j=1,\dots,5$$ ⟹ `g` 的独立自由度 $$(31-5)\times4=\boxed{104\ \text{bit}}$$ ✓✓（**规格须显式写出此 104，而非 31 个 4-bit 变量**）✓
```

## §4 群作用：分三层写清（**不假定半直积**）

```
**(a) `\mathrm{GL}(4,2)`**：作用在 `V`（含 `A_i`、`B_i`）—— **已用于固定 17 个 canonical rep** ⟹ 在 `\mathcal F_i` 内部**不再商** ✓
**(b) `\mathrm{GL}(5,2)`**：作用在 `W`（含 `\mathrm{PG}(4,2)` 的点与线、`e_j` 的选择）—— 与 `(a)` 独立 ✓
**(c) shear**：`g\mapsto g+K`，**保 `A_i`/`B_i`**，**保 `\tau`** ⟹ 仅用于**规范化 `g`**（§3）✓
**【⛔ 纪律（照录）】** **不得**未经验证写成任何半直积商；以下**待定项须显式标为 OPEN**：**(i)** 三层作用之间是否存在非平凡交互；**(ii)** 规范化后是否产生**残余稳定子**（residual stabilizer）；**(iii)** `\mathcal F_i` 的正确商对象究竟是 `g` 还是 `\tau` ✓✓
```

## §5 规格的目标（三种可能结果，先写清）

```
**(1)** 存在 `i` 与 `g` 使 **248 条 incidence 全中**（`cost=0`）⟹ 得 `H`（`9\times38`）⟹ $$\ell_2(9,2)\le38$$（**实质改进，`39\to38`**）✓✓
**(2)** 对全部 `i` 证明 `cost\ge1`（需**穷尽**而非退火）⟹ `n=38` 在**本 `(4,5)` 切片**不可行 ⟹ **切片级结论**（**不得**升级为"全部 `9\times38` 码不可行"）✓
**(3)** 穷尽不成立（搜索空间未闭）⟹ 保持 `residue` ✓
【其它切片（本档补注）】 `F+M=9` 还有 `(3,6),(5,4),(6,3),(7,2),(8,1)` 等切片；`n=38` 在各切片对应不同 `|A|` ⟹ **本规格只覆盖 `(4,5)`**，其余**待列**（不与 17 类混谈）✓
【⛔ 红线（本轮未碰）】 `r=10,n=49`｜`r=11` order `11/17/23`｜`q10` order-7｜族外搜索｜SAT/exact 求解 ✓
【边界】 §0–§3 全部取自**一手逐字**（`README §2`、`r9_n38_classes.txt`、`run_q11_checks.sh`）；§4 的"三层分离＋三项 OPEN"、§5 的切片补注与三种结果为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
