已查地图：命中（`A5-FORMAL-SPEC-r9-n38`／`TARGET-L9-q11-four-sources-complete`）⟹ 引用，不开新案
D0: 本档对象 = 更正：`17` ＝ **reduced representatives**，**非** `17` 个轨道；并修正 `A5` 的 A-侧口径
D1: 0 （[REVIEW] 轮次：更正与规格修正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **更正：`17` 是"归约代表"，不是"17 个轨道"**

## §0 ⭐ 决定性证据（`gen_asets.c` 头注，逐字）

```
"The family depends on A only through B = V \ (A u {0}), and GL(V) acts on the whole family, so **one A per GL(F,2)-orbit of B suffices**. **Reduction (rigorous; possibly more than one representative per orbit):**
 `rank(B)=F` -> B may be assumed to contain `e_1..e_F`, and to be lexicographically minimal under the coordinate permutations `S_F` (which stabilise `{e_1..e_F}`); `rank(B)=d<F` -> B may be assumed to lie in `<e_1..e_d>`.
**Prints hex A-masks, one per line.**" ✓✓✓
【⟹ 关键一句】**"possibly more than one representative per orbit"** ⟹ **该列表是"覆盖性归约"，不是轨道分解** ⟹ 行数**可以大于**轨道数 ✓✓✓
```

## §1 冲突的解释（本档判定）

```
【您的复核】 `\binom{15}{7}=6435` 全枚举 ⟹ `5040` 个满足 `\{0\}\cup A\cup(A+A)=V` ⟹ `|GL(4,2)|=20160` 作用 ⟹ **`2` 个轨道** ✓
【源文件】 `r9_n38_classes.txt` 有 **`17` 行**（`sa_graph.c -A <mask>` 的 mask）✓
【⟹ 判定】**两者不冲突**：`17` ＝ `gen_asets.c` 的**归约代表数**（`S_4`-lex-最小 ＋ 含 `e_1..e_4` 归一化），**非**轨道数 ✓✓
【`A5` 的数学条件本身正确】 `graph_search.c` 第 10 行逐字："`fiber 0 : {0} u A u (A+A) = V` (A is 1-saturating in V)" ⟹ **`A5` 写的 1-saturating 条件与源一致** ✓✓
【⟹ 需要改的是措辞与口径，不是数学】 $$\boxed{17=\text{reduced reps（覆盖性、可重复）}\ \ne\ \text{orbit count}}$$ ✓
```

## §2 ⭐ `A5` 规格修正（A-侧）

```
**(a)** A-侧的正确对象＝`\mathrm{GL}(4,2)`-**轨道集**（据您的独立穷举＝**`2` 个**；本档按档级接受，待我方独立复核）✓
**(b)** `17` 的作用＝**运行清单**（每个代表跑一次退火），**不是**"17 个本质不同的 A" ⟹ **`17` 行的成本数据在轨道层面只需看 ≤2 组** ✓✓
**(c)** 轨道分解的合法替代：**取每轨道的一个 canonical representative**（可用 `gen_asets.c` 的输出再按轨道合并）✓
**(d)** 其余规格（`248` 条 incidence／shear 规范化的 `104` bit／三层群作用分离）**不变** ✓
```

## §3 战略含义（本档补）

```
【A-侧极小】 若轨道数确为 `2`，则 `(4,5)` 切片的 **A-侧本质上只有 2 种结构** ⟹ **"17 类穷尽"这一表述下隐藏的真实搜索面比看上去小得多** ✓✓
【⟹ 自由度重心移到 g-侧】 未闭合量集中在 `g`（shear 规范化后 `104` bit；再商 `\mathrm{GL}(5,2)` 与 `A` 的稳定子）✓
【⟹ 对穷尽的含义】**逐 A-轨道的 `g`-穷尽**比"17 类"更可执行；且**退火已报 `14`**（在 ≤2 个 A 结构上）⟹ 剩下要么是 `g`-侧未被搜到，要么是 `cost\ge1` 为真 ✓
【⚠️ 独立复核待办】 我方**尚未自跑** 5040 / 2-轨道 的复核 ⟹ 记为**待核**（您已核；我按档级引用）✓
【边界】 §0 为**一手逐字**；§1 判定、§2 修正、§3 战略含义为**本档自行推导**；未制造候选／未启动搜索／未碰 RH／未跑 SAT。
