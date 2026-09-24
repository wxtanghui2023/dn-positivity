已查地图：命中（`EDS-CAP-1-COUNTEREXAMPLE-37a1`（反例）／`EDS-REBUILD-partial-EZ-equals-torsion-on-11a1`）⟹ 引用，不开新案
D0: 本档对象 = `Q1/Q2/Q3` 结构判定（`37a1`，`n\le28`）＋ 一处数据更正（`B_{10}=4`）
D1: 0 （[REVIEW] 轮次：判定与更正，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`Q1/Q2/Q3`：`n\le28` 判定（`37a1`，`P=(0,0)`）**

## §0 ⚠️ 数据更正（本档）

```
**【更正】** `B_{10}=4`（我前档写 `2`，错）⟹ `\operatorname{Supp}(B_{10})=\{2\}`（不变）⟹ **反例结论不受影响** ✓
【对照】 `B_5=2`、`B_{10}=4=2^2` ⟹ `\operatorname{Supp}(B_5)=\operatorname{Supp}(B_{10})=\{2\}`，`B_5\mid B_{10}` ✓ ✓
```

## §1 判定结果（本机实算）

```
`I=\{1,2,3,4,6\}`；**`X=\{\text{例外指标}\}=\{10\}`**（`n\le28` 全部可分解）✓
**`Q1`**（每个例外 `n` 有 `q\mid B_n` 使 `r_q\mid n`）：**PASS**（`n=10`：`q=2`，`r_2=5`，`5\mid10` ✓）
**`Q2`**（存在 `m\mid n` 且 `\operatorname{Supp}(B_n)\subseteq\operatorname{Supp}(B_m)`）：**PASS**（`m=5`）✓
**`Q3`**（多素覆盖但无单一 parent）：**无反例** ✓
【`r_q` 表（节选）】 `r_2=5,\,r_3=7,\,r_5=8,\,r_7=9,\,r_{23}=11,\,r_{29}=12,\,r_{59}=13,\,r_{43}=14,\,r_{157}=15,\,r_{13}=16,\,r_{11}=17,\,…` ✓
```

## §2 ⟹ 结构性结论（本档核心）

```
【结果】 `n\le28` 上：**`\operatorname{Prim}(n)=\varnothing\Rightarrow\exists m\mid n:\operatorname{Supp}(B_n)\subseteq\operatorname{Supp}(B_m)`** ⟹ **支持继承 ＋ 整除继承同时成立** ✓✓（`Q3` 无反例 ⟹ **单-parent 修正框架可用**）✓
【⟹ 候选命题（`DC`-型，待证）】 令 `\ell_q(N)` 为 `q` 的继承链最大长度、`D_N(S)=\sum_{q\in S}(\ell_q(N)-1)`：$$|T_N(S)|\ \le\ |S|+D_N(S)$$ 当前 `S=\{2\}`：`\ell_2=2`（`5\to10`）、`D=1` ⟹ `2\le1+1` ✓ **sharp** ✓
【范围限定（诚实）】 判定只在 `n\le28` 有效（`n\ge29` 未分解）⟹ **不得写成 `N=50` 全域结论** ✓
【边界】 全部为本机实算（`out/Q1Q2Q3_37a1.txt`，可复跑）；§2 结论与候选命题为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
