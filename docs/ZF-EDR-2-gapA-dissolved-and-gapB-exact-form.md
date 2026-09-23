已查地图：命中（`ZF-EDR-1-primitive-divisor-budget-theorem`／`ZF-G5G6-VI-...`／`ZF-G5G6-finite-point-machines-...`／`ZF-LEM` 本线自档）⟹ **引用，不开新案** ✓
D0: 本档对象 = GAP-A 的自动消解 ＋ GAP-B 的精确形式（`q_n\in S\iff n\in M`，`M` 有限可预计算）＋ 界面要求合一 ＋ `\tau` 的新约束
D1: 0 （`[REVIEW]` 轮次：结构推导，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-EDR-2`：GAP-A 消解 ＋ GAP-B 精确化**（本档全为自行推导 ✓✓）

## §1 ⭐ **GAP-A 其实自动消解（本档核心之一）**

```
【经典刻画（⚠️ 档级）】 对好约化素数 `q`：$$\boxed{q\mid B_n\iff \operatorname{ord}(P\bmod q)\mid n}$$ ⟹ 故
　$$\boxed{q\ \text{是 }B_n\ \text{的 primitive divisor}\iff \operatorname{ord}(P\bmod q)=n\ \text{恰等}}$$ ✓✓
【⟹ GAP-A（"什么自然事件强迫 primitive divisor 出现"）的答案】 primitive divisor 的存在**对一切 `n>N_0` 自动成立**（`EDR` 版 Zsigmondy）⟹
　$$\boxed{\text{任何携带指标 }n>N_0\text{ 的事件}\ \Longrightarrow\ \text{自动获得 primitive divisor}}$$ ✓✓✓
　即：**GAP-A 不是真 GAP** —— 事件只需提供"一个大于 `N_0` 的指标"即可，无需额外界定"哪类事件" ✓
```

## §2 ⭐⭐ **GAP-B 的精确形式（本档核心之二）**

```
【推导】 `q_n\in S` 意味"存在 `q\in S` 使 `\operatorname{ord}(P\bmod q)=n`" ⟹
　$$\boxed{q_n\in S\iff n\in M:=\bigl\{\operatorname{ord}(P\bmod q):\ q\in S\bigr\}}$$ ✓✓✓
【⭐ 关键性质】 `M` 是**有限、可预先计算**的整数集（`|M|\le|S|`）✓✓ —— 即 **GAP-B 被化归为一个具体的有限整数集 `M`**，而**不是**模糊的"限制到 `S`" ✓
【⭐ 预算的精确化】 真正的预算＝$$\boxed{|M|=\#\{\text{不同阶}\}\le|S|}$$（若两个素数给出同阶，只算一次）✓✓
【⟹ 由您 §11 的弱化得到真形】 无需 `\operatorname{Supp}(B_{n(\rho)})\subseteq S`；只需 $$n(\rho)\in M$$ ✓✓
```

## §3 ⭐⭐⭐ **界面要求合一为一条（本档）**

```
$$\boxed{\text{存在 canonical、逐零点可求值的 }\rho\mapsto n(\rho)\text{，使}\quad (a)\ \rho\ \text{离轴}\Rightarrow n(\rho)\in M;\qquad (b)\ n(\rho)\ \text{在离轴零点上\textbf{单射}}}$$ ✓✓
【⟹ 定理（推理闭合）】 由 `(a)` 各离轴零点给出指标 `\in M`；由 `(b)` 不同零点给不同指标 ⟹ $$\#\{\text{离轴零点}\}\le|M|\le|S|<\infty$$ ✓✓✓
【与您 §9 `EDR-FC` 的关系】 本档把 `EDR-FC` 的两个假设 `(3)(4)` **合并并具体化**为"`n(\rho)\in M` ＋ 单射"；同时**消去了对 `\operatorname{Supp}(B_n)\subseteq S` 的整体要求** ✓
```

## §4 ⭐ **为何 `VI` 的"纤维"担忧**消失**（本档）**

```
【旧担忧】 若无穷多个零点映到有限指标集，则某纤维无穷 ⟹ `VI` FAIL ✗
【本档解除】 要求的是**单射**（不是多对一）⟹ 与 `VI`（`\sup_d|\Phi^{-1}(d)|<\infty`）**相容**；更强：若离轴无穷而单射入有限集 `M` ⟹ **矛盾** ⟹ 故**单射性本身即证明有限性** ✓✓
【⟹ 净效果】 界面要求**不再需要**"纤维有限"这一额外条款 ✓（`VI` 由 `(b)` 直接满足 ✓）
```

## §5 ⭐⭐ **由 `R1`（`\sigma`-等变）推出的新约束（本档新增）**

```
【结合 `R1`】 离轴零点成 `\sigma`-对：`\rho` 与 `\sigma\rho=1-\bar\rho` 都离轴 ⟹ 由 `(b)` 单射须
　$$\boxed{n(\sigma\rho)\ne n(\rho)}$$；而由 `\sigma`-等变 `n(\sigma\rho)=\tau\bigl(n(\rho)\bigr)` ⟹ $$\boxed{\tau\ \text{在 }M\ \text{上须无不动点（且非平凡）}}$$ ✓✓✓
【⟹ 可检验约束（本档）】 `M` 须带一个**无不动点对合**（尤其 `|M|` 须为**偶数**；且 `\tau` 须与阶结构相容）✓
【⟹ 与 `GAP-T` 会合】 这正是 `GAP-T`（`\tau` 缺口）的**具体化形式**：`\tau` 不必是抽象的，它须表现为 `M` 上的无不动点置换 ✓✓
【⛔ 注意】 `P\mapsto-P` 保持各阶不变 ⟹ **不能**充当这个 `\tau` ⟹ 须另找（如 `S` 上的自然配对/共轭素数）⟹ 记为 **`GAP-T'`** ✓
```

## §6 **最终 GAP（单一、精确）**

```
$$\boxed{\text{须存在 canonical、逐零点可求值的 }\rho\mapsto n(\rho)\ \text{与事先固定的有限 }S\text{，使}\ \rho\ \text{离轴}\Rightarrow n(\rho)\in M=\{\operatorname{ord}(P\bmod q)\}_{q\in S},\ \text{且在离轴零点上单射}}$$ ✓✓
【等价读法】 ＝「离轴零点**单射地**落入一个**有限、可预先计算的整数集 `M`**」 ✓
【边界】 ⚠️ §1 的 `q\mid B_n\iff\operatorname{ord}\mid n` 为**经典结果**（档级）；⛔ 本档未构造 `\rho\mapsto n(\rho)`、未碰 `\zeta`、未制造候选、未启动搜索、未改状态 ✓；⭐ §1–§5 全为**本档自行推导** ✓
```
