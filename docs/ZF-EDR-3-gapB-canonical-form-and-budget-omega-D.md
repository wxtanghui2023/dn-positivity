已查地图：命中（`ZF-EDR-1`／`ZF-EDR-2`／`ZF-G5G6-VI-...`／`ZF-LEM`／`E-11` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = `r_q` 表述下的 GAP-B 规范形式（`S_{\rm exc}` 无损等价于固定整数 `D` 的素因子集）＋ 显式预算 `\omega(D)` ＋ A2 自动性
D1: 0 （`[REVIEW]` 轮次：结构推导，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-EDR-3`：GAP-B 的规范形式 `S_{\rm exc}=\{q:q\mid D\}` 与预算 `\omega(D)`**（本档全为自行推导 ✓✓）

## §1 **采用 `r_q` 表述（落档您 §1–§10 的强化 ✓）**

```
【定义】 $$r_q:=\min\{n\ge1:\ q\mid B_n\}=\operatorname{ord}_{E(\mathbb F_q)}(\widetilde P)$$ ✓
【基本关系（⚠️ 档级）】 $$q\mid B_n\iff r_q\mid n$$ ⟹ $$\boxed{q\ \text{在}\ B_n\ \text{中 primitive}\iff r_q=n}$$ ✓✓
【⭐ 局部有限纤维（**无需 `N_0`**）】 固定 `q` 至多对应**一个** primitive 指标 ⟹ 对事先固定有限 `S`：$$\boxed{|\mathcal P_S|\le|S|}$$（**无前缀项**）✓✓
【⭐ 更精确（您的 §10）】 同阶素数只支持同一指标 ⟹ 若事件要求"不同指标"，槽位＝$$|\mathcal R_S|=\bigl|\{\operatorname{ord}_{E(\mathbb F_q)}(\widetilde P):q\in S\}\bigr|\le|S|$$ ✓
【Hasse 上界（您的 §9）】 $$r_q\mid\#E(\mathbb F_q)=q+1-a_q,\ |a_q|\le2\sqrt q\ \Longrightarrow\ r_q\le q+1+2\sqrt q$$ ⟹ `\mathcal R_S` **完全可预先计算** ✓
```

## §2 ⭐ **匹配型精化（本档；处理"多素数同阶"）**

```
【观察】 若 `r_{q_1}=r_{q_2}=m`，则两个**同指标**事件可分别消耗 `q_1,q_2` ⟹ **不需要**指标单射（上一档的"指标单射"要求**过强，可撤**）✓✓
【正确条件】 只需存在**单射** `e\mapsto q_e\in S`，使 `r_{q_e}=n(e)` ⟹ 即 $$\boxed{\text{指标多重集 }\{n(e)\}\ \text{被}\ \{r_q\}_{q\in S}\ \text{支配（Hall 条件）}}$$ ✓
【充分情形】 指标 `n(e)` 两两不同且 `n(e)\in\mathcal R_S` ⟹ 自动可匹配 ✓
```

## §3 ⭐⭐⭐ **GAP-B 的规范形式（本档核心）**

```
【无损等价】 任何**事先固定**的有限素数集 `S` 都等于某个固定整数的素因子集（取 `D=\prod_{q\in S}q`）⟹
　$$\boxed{S_{\rm exc}=\{q:\ q\mid D\}\qquad(D\ \text{固定、canonical})}$$ —— **无损一般性** ✓✓
【⟹ GAP-B 的规范形式】 $$\boxed{\text{事件}\Longrightarrow\text{其 primitive 素数整除一个\textbf{固定 canonical 整数 }D}}$$ ✓✓✓
【⭐ 为何这是对的形态】 算术中产生**事先固定有限素数集**的标准机制**只有**"整除某个固定对象"（判别式/导子/层次/模）⟹ 故这就是 GAP-B 可期望的唯一规范形态 ✓
【⛔ 反循环（承接您 §13）】 `D` **必须独立于事件定义**（不得取 `D=\prod q_e`）⟹ 这是硬要求 ✓✓
```

## §4 ⭐⭐ **推论：显式预算 `\omega(D)` 与指标集 `\mathcal R_D`**

```
【预算】 单射 `e\mapsto q_e` 入 `\{q:q\mid D\}` ⟹ $$\boxed{N_{\rm event}\le\omega(D)\quad(\omega=\text{不同素因子个数})}$$ ✓✓✓ —— **显式、与高度无关**（故**不需要** `HG` ✓，与前述更正一致 ✓）
【指标集有限且可预计算】 $$\boxed{n(e)\in\mathcal R_D:=\{r_q:\ q\mid D\}\qquad(\text{由 Hasse 上界可算})}$$ ✓✓
```

## §5 ⭐⭐ **A2（primitivity）自动满足（本档）**

```
【您的 §7】 `q\mid B_n` 单独＝**可复用**（`q\mid B_{kn}`）⟹ CLOSED ✗；`q` primitive ⟹ 不可复用 ✓
【本档观察】 在 `r_q` 表述下：若事件给出的指标 `n` 满足 `n=r_q`，则 **primitivity 自动成立**（定义即得）⟹
　$$\boxed{A1\ \text{与}\ A2\ \text{合并为一条"指标—秩巧合"条件：}\ n(e)=r_{q_e}}$$ ✓✓✓ —— 故 A2 不再是独立难点 ✓
```

## §6 ⭐ **最终接口定理（条件形式；本档）**

```
【定理（条件形式）】 若存在 **(i)** canonical、逐零点可求值的 `\rho\mapsto n(\rho)`；**(ii)** 固定 canonical 整数 `D`；使
　**(a)** `\rho` 离轴 ⟹ `n(\rho)\in\mathcal R_D=\{r_q:q\mid D\}`；**(b)** 指标多重集被 `\{r_q\}_{q\mid D}` 支配（Hall）
　⟹ 则 $$\boxed{N_{\rm off}\le\omega(D)<\infty}$$ ✓✓✓
【⟹ GAP 的最终精简形态】 $$\boxed{\text{须找到一个独立结构，使离轴零点产生的指标}\ n(\rho)\ \text{恰好与某个固定 }D\ \text{的素因子的秩吻合}}$$ ✓✓
【`PL`/`CAN`/`DIM`/`VI` 一致性】 `PL` ✓（逐零点）；`CAN` ✓（`D` 须 canonical）；`DIM` ✓（`\mathcal R_D` 有限＝零维）；`VI` ✓（单射入有限集）✓✓
```

## §7 **剩余难点与边界**

```
【剩余难点（单一）】 **(α)** 构造 canonical `\rho\mapsto n(\rho)`（`PL` 合规）；**(β)** 找到一个 canonical `D` 且使"指标—秩吻合"独立成立 ⟹ 两者都**必须来自独立结构**，⛔ 不得由事件反推 ✓
【`GAP-T'` 仍待解】 由 `R1`，σ-对须给不同指标（或不同素数）；在 `r_q` 表述下即：σ-对的指标须为**不同秩**，或由**不同素数**承担 ⟹ 需要 `\{q:q\mid D\}` 内存在足够的秩分布 ⟹ **可检验约束** ✓
【边界】 ⚠️ §1 基本关系与 Hasse 型上界为**经典**（档级引用）；⛔ 未构造 `\rho\mapsto n(\rho)`／未构造 `D`／未碰 `\zeta`／未制造候选／未启动搜索／未改状态；⭐ §2–§6 均为**本档自行推导** ✓
```
