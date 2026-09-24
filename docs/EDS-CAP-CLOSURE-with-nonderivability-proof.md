已查地图：命中（`EDS-DC-injection-reduced-to-one-lemma`／`EDS-Q1Q2Q3-structural-verdict`／`EDS-CAP-1-COUNTEREXAMPLE-37a1`／`DC_counterexample_targeted`）⟹ 引用，不开新案
D0: 本档对象 = `甲` 纸面推导审计（**成链引理不可由现有公理推出**，给抽象模型）＋ `乙` 正式收口（资产清单）
D1: 0 （[REVIEW] 轮次：审计与收口，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`EDS/CAP` 收口 ＋ 成链引理不可推导性证明**

## §1 ⭐ `甲`：成链引理**不可由现有 EDS 公理推出**（本档核心）

```
【现有公理】 **(A1)** `m\mid n\Rightarrow B_m\mid B_n` ✓；**(A2)** `q\mid B_n\iff r_q\mid n`（由 A1 ＋ gcd 恒等式）✓
【待判命题】**`E_q(N)` 在整除偏序下成链**
【反模型（本档构造）】 取 `r_2=5`、另设 `q'` 满足 `r_{q'}=3`；指定
　`B_1=B_2=B_4=1`，`B_3=q'`，`B_5=2`，`B_6=q'`，`B_{10}=2`，`B_{15}=2q'`（其余取 1 或相容值）
【校验 `A1`】 `3\mid15`：`q'\mid2q'` ✓；`5\mid10`：`2\mid2` ✓；`5\mid15`：`2\mid2q'` ✓；`3\mid6`：`q'\mid q'` ✓；`1\mid\cdot` ✓ ⟹ **A1 相容** ✓
【校验 `A2`】 `2\mid B_n\iff5\mid n`（`B_5,B_10,B_15` 含 2）✓；`q'\mid B_n\iff3\mid n` ✓ ⟹ **A2 相容** ✓
【例外性】 `\operatorname{Prim}(10)=\{2\}\setminus\{2\}=\varnothing` ✓；`\operatorname{Prim}(15)=\{2,q'\}\setminus\{2,q'\}=\varnothing` ✓ ⟹ **`10,15\in X`** ✓
【⟹ 结论】 `E_2\supseteq\{10,15\}`，而 $$10\nmid15,\quad15\nmid10$$ ⟹ **`E_2` 不是整除链** ✓✓✓ $$\boxed{\text{成链引理不可由 (A1)+(A2) 推出}}$$ ✓✓
【意义】 这解释了定向搜索为何在 `37a1` 上找不到反例 —— **不是引理为真，而是真实 EDS 的额外约束（primitive-divisor 机制）太强**，使反例在真实序列上极稀 ⟹ **"找不到反例"不等于"引理成立"** ✓✓
```

## §2 `乙`：正式收口 ＋ 资产清单

```
**【成功资产（击破）】** $$\boxed{|T(S)|\le|S|\ \text{被最小反例击破：}\ E=37a1,\ P=(0,0),\ S=\{2\},\ B_5=2,\ B_{10}=4,\ T(\{2\})=\{5,10\}}$$ ⟹ `|T|=2>1=|S|` ✓✓
**【结构资产（严格）】** **(1)** `q\mid B_n\iff r_q\mid n`｜**(2)** `r_q=n\iff q` 在 `n` 处 primitive｜**(3)** `|P_N(S)|\le|S|` ✓
**【未决资产（已降级）】** `\operatorname{Prim}(n)=\varnothing\Rightarrow` 单一整除链继承 —— **§1 已证其不可由 (A1)+(A2) 推出** ⟹ 从"未证"降为"**需新输入**" ✓✓
**【机制判定】** $$\boxed{\text{CAP surplus}\ =\ \text{primitive-divisor 继承现象的定量影子}}$$ ⟹ **无证据表明它已脱离经典 EDS primitive-divisor 理论形成独立容量机制** ✓
**【弱化版 `DC'` 的定性】** `X_N\subseteq[2,N_0]`（`N_0` 来自 primitive-divisor 定理）⟹ `|T_N(S)|\le|S|+|X_{N_0}|` —— **正确但不是新定理**，而是 primitive-divisor 定理的**重新计数形式** ✓
【收口理由（照录您的判词）】 $$\boxed{\text{错误猜想}\to\text{真实最小反例}\to\text{机制定位}\to\text{精确识别剩余引理}\to\text{确认其缺乏独立支撑}}$$ ✓✓
【保留用途】 `B_5=2,\ B_{10}=4` 这一最小反例可作为**独立问题筛选的比较基准**：以后任何序列/递推系统若出现"primitive capacity 被旧因子继承打破"，直接拿此结构对照 ✓
【边界】 §1 反模型为**本档构造**（初等，可手核）；§2 资产取自本线各档（可核）；未制造候选／未启动搜索／未碰 RH。
