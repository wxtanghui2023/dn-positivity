已查地图：命中（`EDS-REBUILD-blocked-no-nontorsion-in-box`／`EDR-CAP-1-counterexample-and-corrected-form`）⟹ 引用，不开新案
D0: 本档对象 = **`CAP-1` 反例（`37a1`）**：合法数据层四审计通过 ⟹ `|Z_S\setminus I|>|S|` 出现
D1: 0 （[REVIEW] 轮次：数据层与反例，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`CAP-1` 反例：`E=37a1,\ P=(0,0),\ S=\{2\}`**

## §1 数据层（合法，四审计）

```
`E:y^2+y=x^3-x`（**37a1**；**秩 1**、挠群平凡、`(0,0)` 无限阶）✓
**(1)** `B_n`：`B_2=B_3=B_4=B_6=1`；`B_5=2,\ B_7=3,\ B_8=5,\ B_9=7,\ B_{10}=2,\ B_{11}=23,\ B_{12}=29` ⟹ `I=\{1,2,3,4,6\}` ✓
**(2)** `m\mid n\Rightarrow B_m\mid B_n`：**OK** ✓
**(3)** `\gcd(B_m,B_n)=B_{\gcd(m,n)}`：**OK** ✓
**(4)** `\operatorname{Prim}(n)=P_n\setminus\bigcup_{m<n}P_m` ✓；**例外池 `X=\{10\}`**（`B_{10}=2`，但 `2` 已由 `n=5` 占先 ⟹ `\operatorname{Prim}(10)=\varnothing`）✓
```

## §2 ⭐ 反例（本档核心）

```
【判据】 `T(S)=\{n>1:B_n>1,\ P_n\subseteq S\}` ⟹ 检查 `|T(S)|>|S|` ✓
【反例】 取 `S=\{2\}`：`P_5=\{2\}`、`P_{10}=\{2\}` ⟹ $$T(\{2\})=\{5,10\}\ \Longrightarrow\ |T(\{2\})|=2>1=|S|$$ ✓✓✓
【⟹ 判词】 $$\boxed{\text{修正版容量猜想（}|Z_S\setminus I|\le|S|\text{）为\textbf{假}}}$$ —— 反例极小、可手核 ✓✓
【⟹ 机制（本档给出）】 因 `5\mid10` 且 `B_5\mid B_{10}`（审计 (2) 已证）⟹ **同一素因子在多个指标上重复出现** ⟹ **非本原指标与先驱指标共享同一 `q`** ⟹ 容量 `|S|` 被突破 ✓✓
【⟹ 结论（对 `CAP` 命题）】 `CAP-1` **出口 A 命中**：容量上界**不成立**；因此 `|Z_S|\le|I(E,P)|+\omega(D)` **应废弃** ✓
【⟹ 新的精确命题（后续可攻）】 需计入"重复占位"：$$\boxed{|Z_S\setminus I|\ \le\ \#\{q\in S:\ \exists\, n,\ r_q=n\}\ +\ \#\{n:\ B_n>1,\ \operatorname{Prim}(n)=\varnothing\}}$$ 即**本原容量 ＋ 例外池**两层 ✓✓
【边界】 全部为本机实算（`out/eds_layer_37a1.txt`，可复跑）；§2 机制与精确命题为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
