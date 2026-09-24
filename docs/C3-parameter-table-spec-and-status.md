已查地图：命中（`C3-s_t-status-framework-and-hard-fork`／`C3-premise-confirmed-by-handbook`）⟹ 引用，不开新案
D0: 本档对象 = `C3` **参数表规格**（章分工 ＋ modular 映射 ＋ `H_{s,t}` 判据要求）＋ **诚实标注表未填满**
D1: 0 （[REVIEW] 轮次：规格化，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`C3`：参数表规格 ＋ `H_{s,t}` 判据要求**

## §1 章分工与 modular 覆盖（照录，一手）

```
**【章分工（`Chapter 11` 目录级）】** `11D` ⟹ `\{\{6,3\}_{(s,0)},\{3,6\}_{(t,0)}\}`；**`11E` ⟹ 完整的 `\{3,6,3\}`**；`11F`/`11H` ⟹ **cuts 与参数关系** ✓✓
**【已决基准（不得再作候选）】** 自对偶 `(s,t)=((1,1),(1,1)),((2,0),(2,0)),((3,0),(3,0))` ✓
**【⭐ modular 覆盖（`Monson–Schulte 2010`，`[3,6,3]`）】** 参数映射：$$q=(d,0),\qquad r=\begin{cases}(d,0),&3\nmid d\\(d/3,d/3),&3\mid d\end{cases}$$ ⟹ **大量 `((d,0),(d,0))` 或 `((d,0),(d/3,d/3))` 属"已被构造覆盖"** ⟹ **不得简单当作"未解决"** ✓✓
```

## §2 参数表骨架（四列）

```
$$\bigl((s,t)\ \big|\ \text{已决}\ |\ \text{modular 覆盖}\ |\ \text{`11H` 归约}\ |\ \textbf{真正未决}\bigr),\qquad s=(a,0)\ \text{或}\ (a,a),\ t=(b,0)\ \text{或}\ (b,b)$$ ✓
【已知排除项（本轮累计）】 **(i)** 自对偶三点 `((1,1),(1,1))`／`((2,0),(2,0))`／`((3,0),(3,0))` ⟹ **已决** ✓；**(ii)** `((d,0),(d,0))` 与 `((d,0),(d/3,d/3))` ⟹ **modular 覆盖** ✓
【四类判据（承前档）】 **A** `11E` 已决｜**B** `11D/11E/11H` 关系归约｜**C** modular 覆盖｜**D 真正未决** ⟹ 仅 D 为候选 ✓
```

## §3 `H_{s,t}` 判据要求（本轮最关键，两问必须逐字回答）

```
**【问 1】** $$\boxed{\dim H_{s,t}\ \text{是否固定？}}$$ 若为**固定小维数**（如 `4\times4`）⟹ $$N_{\rm eff}\approx\text{有限个精确代数不等式}$$ ⟹ **满足 `H`-型压缩** ✓✓
**【问 2】** $$\boxed{H_{s,t}>0\iff\text{universal polytope finite}\ \text{是否对该具体未决参数成立？}}$$ —— **不得**再写"由 Hermitian form 控制" ✓✓
【两态出口（照录）】 **(a)** 最小 D 参数 ＋ **固定维 Hermitian 正定性** ⟹ **下一轮进 `G3`（实际计算）** ✓；**(b)** 最小 D 参数存在，但 **Hermitian 判定已被文献完成** ⟹ **`C3` 立即退出**，**不做重复计算** ✓✓
```

## §4 ⚠️ 诚实状态（本轮**未完成**项）

```
【未完成】 **`(s,t)` 完整状态表**与**最小 D 参数** —— 需读 **`§11D`／`§11E`／`§11H` 正文**；本轮**未能取得**（`Chapter 11` 为 `58` 页 PDF，单次抓取远超当前预算）✓
【⟹ 表仍在 `OPEN`】 承前档状态表：`(s,t)` 完整表 / 最小未决 / 显式 `H(s,t)` / `N_{\rm eff}` —— **四项全 `OPEN`** ✓
【本轮实际推进】 **章分工明确化**＋**modular 覆盖参数映射入账**＋**两问规格写死** ⟹ **下一刀可直接"按图索骥"** ✓
```

## §5 竞争审计（照录）

```
【`Monson–Schulte 2010` 状态】 当时 **locally toroidal 整体尚未完全分类**；其 modular 方法对 spherical/Euclidean Coxeter groups 给出完整 modular 描述，并在 `[3,6,3]` 上产生大量具体 locally toroidal polytopes ✓
【⟹ `G4` 的唯一机会形态】 $$\boxed{\text{找一个具体 }(s,t)\text{，其 universal finite/infinite 仍未决，并用一个尚未完成的有限维代数判定把它定下来}}$$ ✓✓ —— **不是**"重新发现一个有限 polytope" ✓
【⛔ 纪律】 本轮**不计算、不实现**；`C2` 暂缓；`n=38`／`TARGET-L9`／RH 未作筛选依据 ✓
【边界】 §1 章分工、已决基准、modular 映射为**您提供的一手/正文级信息**；§2–§3 为**本档规格**；§4 为**诚实状态**；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 Hermitian form   命中文件数=12   :: ./V294-A-finite-order-aggregation-gain-classification.md ./ASSETS-REGISTRY.md ./E8-ceiling-0682.md 
技术词 locally toroidal 命中文件数=5    :: ./C3-parameter-table-spec-and-status.md ./C3-concretized-36s-63t-family.md ./C3-premise-confirmed-by-handbook.md 
技术词 modular construction 命中文件数=1    :: ./C3-s_t-status-framework-and-hard-fork.md 
```
