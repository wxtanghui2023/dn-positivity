已查地图：命中（`ZF-EDR-1/2/3`／`ZF-G5G6-VI-...`／`ZF-CONT-1/2/3`／`E-11`／`S6` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = `RPC-1` 自然实例枚举与检验（三类），及该类路线的 CLOSED 判定
D1: 0 （`[REVIEW]` 轮次：枚举检验与判死，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-RPC-1`：自然实例枚举与检验 ⟹「以 resultant/ramification 供 `S_{\rm exc}`」路线 CLOSED**（本档全为自行检验 ✓✓）

**【本档任务（照录您的指令 ✓）】** 枚举并**实际检验**一批已有的"固定 discriminant/resultant 异常"（ramification／resultant collision／bad-reduction collision），看能否找到一种事件使 EDS primitive 新素数**同时**被独立的固定 discriminant/resultant 强迫；**若第一批全部只是"人为并置"，立即把该类路线 CLOSED，不再包装** ✓✓

---

## §1 **机制复核（`RPC-1` 引擎本身：PASS ✓）**

```
【Bézout 机制】 `R=A F+B G` ⟹ 模 `q`：`F(u)\equiv G(u)\equiv0\Rightarrow R\equiv0\pmod q` ⟹ $$\boxed{q\mid R\Rightarrow q\in\operatorname{Supp}(R)}$$ ✓（有限素数靶 ✓）
【压力测试（照录 ✓）】 固定 `q\mid R` 后可有**无穷多** `u`（`u=u_0+kq`）⟹ $$\boxed{\text{resultant collision 只有 finite prime target，没有 finite event target}}$$ ⟹ **必须**再接 EDS primitive 条件 ✓
【接 EDS 后（照录 ✓）】 三条件 `q\mid F(u_n)`、`q\mid G(u_n)`、`q` primitive in `B_n` ⟹ `q\mid R` 且 `n=r_q` ⟹ $$\boxed{\#\{n\}\le\omega(R)}$$ ✓（严格 ✓）；更强版 `N_{\rm RPC}\le|\mathcal R_R|`，`\mathcal R_R=\{r_q:q\mid R,\ q\nmid\Delta_E\}` ✓
【⟹ 机制状态】**`RPC-1` 引擎 ＝ CLOSED/PASS** ✓（无争议）
```

## §2 ⭐ **Class B（resultant collision）自然族检验 ⟹ 死**

```
【自然候选族】 除子/分圆型：`F=\psi_m`、`G=\psi_n`（`\psi` 为除子多项式；取**另一条固定曲线** `E'` 以满足 Rule-R2 ✓）
【检验 1】 若 `\gcd(m,n)=d>1`：`\psi_m,\psi_n` 在 `\overline{\mathbb Q}` 上**有公共根**（有 `d`-扭点）⟹ $$R=\operatorname{Res}(\psi_m,\psi_n)=0$$ ⟹ **不合前提（须 `R\ne0`）** ✗
【检验 2】 若 `\gcd(m,n)=1`：**无公共复根** ⟹ 但模 `q` 公共根 ⟺ `E'` 上存在同时被 `m,n` 整除阶的点 ⟹ 阶整除 `\gcd(m,n)=1` ⟹ **不存在** ⟹ $$\operatorname{Supp}(R)=\varnothing$$ ⟹ **无碰撞素数** ✗
【⟹ 判死】 该自然族**二分皆死**（`R=0` 或 `\operatorname{Supp}=\varnothing`）✓✓
【唯一"活"的实例】 形如 `F=X^2-1,G=X^2+1`（`R=4`，`\operatorname{Supp}=\{2\}`）—— 但这是**手工构造**，其"碰撞素数"来源不具独立性 ⟹ **人为** ✗
【⟹ Class B 结论】 机制透明，但**自然实例未找到**；存活实例均属手工 ⟹ **人为并置** ✗
```

## §3 ⭐ **Class A（ramification）检验 ⟹ 等价重述，无独立增益**

```
【机制】 `q\mid\operatorname{Disc}(F)` ⟹ `S_{\rm ram}` 天然有限 ✓
【⛔ 检验结论】 要求"离轴零点 ⟹ 固定对象发生**退化/坏约化**" ⟹ 这正是本线一直在找的 **zero-to-obstruction 定理**（您早前 §97 的最终缺口）⟹ **Class A 并未提供新来源，只是把同一 GAP 换个名字** ✗
【⛔ 进一步】 退化为"坏约化"是**固定有限**事件；若无独立刚化定理强迫之，则事件侧无从产生 ⟹ **无独立增益** ✓
```

## §4 ⭐⭐ **Class C（bad reduction）检验 ⟹ 定义级死 ＋ 相撞要求**

```
【检验 1（定义级死）】 若 `X=E`（即 EDS 自身曲线）：primitive divisor 的**前提就是好约化**（`r_q` 需 `q\nmid\Delta_E`）⟹
　$$\boxed{S_{\rm bad}(E)\cap\{\text{primitive divisors}\}=\varnothing\ \text{（按定义）}}$$ ⟹ **该类实例整体死** ✗✓✓
【检验 2（`X\ne E`）】 须两个**独立定义的稀有集**相撞：`\operatorname{Supp}(\Delta_X)` 与 `\{r_q:q\mid\cdots\}` ⟹ 这要求
　$$\text{两个独立稀有算术集存在自然强制相交定理}$$ ⟹ 此类定理**不存在**（要么是定义推论，要么是深开问题）⟹ **人为并置** ✗
```

## §5 ⭐⭐⭐ **统一判死理由（本档核心）**

```
【三类共同结构】 它们都要求：$$\text{两个\textbf{独立定义}的稀有算术集相撞}\qquad\text{且事件侧\textbf{强迫}相撞}$$ ✓
【而"强迫相撞"这一半】 恰恰就是本线唯一的 residual GAP（**zero-to-obstruction**：离轴 ⟹ 固定对象退化/碰撞）✓✓
【⟹ 统一结论】 $$\boxed{\text{三类均无独立新来源；全部归约到同一个 residual GAP}}$$ ✓✓✓
【⟹ 按您的指令判定】 $$\boxed{\textbf{RPC-1 的自然实例路线 CLOSED（人为并置）}}$$ —— ⛔ 不再继续枚举/包装 ✓✓
【保留项】 `EDR` finite-capacity engine（PASS）｜`RPC-1` 机制本身（PASS，作为"若有事件则预算成立"的条件引擎）｜二者作为**条件工具**保留 ✓
```

## §6 **账本更新**

| 部件 | 状态 |
|:--|:--|
| `EDR` finite-capacity engine | **CLOSED / PASS** |
| `RPC-1` 机制（resultant 压缩素数靶） | **CLOSED / PASS** |
| `RPC-1` + `EDR` 组合（条件形式） | **PASS**（`e\Rightarrow q_e\mid R\Rightarrow N_e\le\omega(R)`）|
| Class A（ramification 供 `S_{\rm exc}`） | **CLOSED**（等价重述，无独立增益）|
| Class B（resultant collision 自然实例） | **CLOSED**（自然族二分皆死；存活者手工）|
| Class C（bad reduction 供 `S_{\rm exc}`） | **CLOSED**（`X=E` 定义级死；`X\ne E` 须相撞定理）|
| **residual GAP** | **单一**：zero-to-obstruction（离轴 ⟹ 固定对象退化/碰撞）|
| 与零点的自然对应 | 尚未建立（FROZEN）|

```
【边界】 ⛔ 未制造候选／未启动搜索／未改状态；⚠️ §1 机制为经典（档级）；⭐ §2–§5 的检验与统一判死为**本档自行推导** ✓
```
