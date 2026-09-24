已查地图：命中（`C3-targeted-evidence-round`／`C3-parameter-table-spec-and-status`／`C3-s_t-status-framework-and-hard-fork`）⟹ 引用，不开新案
D0: 本档对象 = `C3` **参数级问题陈述获得**（`Problem 16`/`Problem 17` 逐字）＋ `D\ne\varnothing` 判定 ＋ 参数空间形式化
D1: 0 （[REVIEW] 轮次：取证，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`C3`：`Problem 16/17` 逐字 ＋ 参数空间**

## §1 来源（已归档）

```
**`arXiv:math/0608397v1`**，`Egon Schulte` ＆ `Asia Ivi\'c Weiss`，**"Problems on Polytopes, Their Groups, and Realizations"**（`2006`，`25` 页）✓
⟹ **`Schulte` 本人的开放问题清单（权威）＋ 免费** ✓；已存 `sources/Schulte-Weiss-2006-open-problems-polytopes.pdf` ✓
```

## §2 ⭐⭐ 逐字证据（本轮核心）

```
**【总况】** "The enumeration is **complete except in the cases `\{4,4,4\}` and `\{3,6,3\}`**." ✓✓
**【rank 4 七型（up to duality）】** "`\{4,4,3\},\{4,4,4\},\{6,3,3\},\{6,3,4\},\{6,3,5\},\{6,3,6\}` or `\{3,6,3\}`" ✓
**【`\{3,6,3\}` 现状逐字】** "For `\{3,6,3\}`，**only partial results are known and involve \textbf{sparse sequences of parameters}**（see `[42, Sections 11E,H]`）." ✓✓✓
**【`Problem 16`（`\{4,4,4\}`，逐字）】** "Classify the universal regular 4-polytopes `\{\{4,4\}_{(s,0)},\{4,4\}_{(u,0)}\}` with `s,u\ge3`，**odd and distinct**. **It is conjectured**（see `[42, p.376]`）**that these polytopes exist for all such `s` and `u`, but are finite only if `(s,u)=(3,5)` or `(5,3)`**." ✓✓✓
**【`Problem 17`（`\{3,6,3\}`，逐字）】** "Classify the universal regular 4-polytopes `\{\{3,6\}_{(s,t)},\{6,3\}_{(u,v)}\}`. Here, **`s\ge2`，`t=0` or `s=t\ge1`，and `u\ge2`，`v=0` or `u=v\ge1`**." ✓✓✓
```

## §3 参数空间形式化

```
$$\text{侧面参数}\ s\in\{(a,0):a\ge2\}\cup\{(a,a):a\ge1\},\qquad \text{另一侧}\ u\in\{(b,0):b\ge2\}\cup\{(b,b):b\ge1\}$$ ✓（与 §1 前档逐字正则性条件 `st(s-t)=0` 完全一致 ⟹ **交叉验证通过**）✓✓
【问题三重性（`Schulte` 明写）】 "which parameters do these polytopes **exist**, what are their **groups**, and when are they **finite**?" ⟹ **存在性 / 群结构 / 有限性 三分，不可混同** ✓✓（正是您要求的四档语义的来源）✓
```

## §4 ✅ `D` 判定

```
$$\boxed{D\ne\varnothing}$$ ✓✓ —— **`Problem 17` 明写 "only partial results … sparse sequences"** ⟹ **未决参数集合非空（陈述级已成立）** ✓✓
【⚠️ 但尚未拿到】**"sparse sequences" 的\textbf{具体清单}**（即哪些 `(s,t,u,v)` 已定）⟹ 仍需 `[42, §11E/§11H]`（或 `1992\ CMH` 论文／`Monson–Schulte 2010`）✓
【⟹ 最小未决 `(s_*,t_*,u_*,v_*)` 仍 `OPEN`】**两硬问**（`\dim H` 是否固定？`H>0\iff` 有限？）**待该清单到手后才能问** ✓
```

## §5 附带发现（`\{4,4,4\}` 分支，可能更干净）

```
**【`Problem 16` 结构】** 参数 `(s,0),(u,0)`、`s,u\ge3` **奇数且相异** ⟹ **两参数族** ✓
**【猜想极锐】** 存在性：所有此类 `s,u`；**有限性：仅 `(s,u)=(3,5)` 或 `(5,3)`** ✓✓ ⟹ **若要"用固定维代数判定把未决参数定下来"，这是一个天然候选（猜想已给出精确答案，缺的是证明）** ✓
【⚠️ 竞争】 该猜想出自 `[42, p.376]`，**须审计 2002 后是否已被证明** ✓
```

## §6 下一步（不计算）

```
**【第一优先】** 取 **`[42] §11E/§11H`** 的 **"sparse sequences" 具体清单** ⟹ 得**已定参数集** ⟹ **取补集** ⟹ **最小未决** ✓
【路径（三条，按可得性）】 **(a)** `1992\ Comment.\ Math.\ Helv.\ 67,\ 77`–`118`「Locally toroidal regular polytopes of rank 4」（**免费，`e-periodica`，需浏览器**）；**(b)** `Monson–Schulte 2010`「Locally toroidal polytopes and modular linear groups」（**`academia.edu` 免费 PDF**）；**(c)** 书 `[42]`（`Cambridge`，站点挡下载）✓
【⛔ 纪律】 **不计算、不实现**；`C2` 暂停；`n=38`／`TARGET-L9`／RH 未作筛选依据 ✓
【边界】 §2 全部为**逐字抽取**（`arXiv:math/0608397v1` pp.10–11，本地 `pymupdf` 提取，**已归档原文**）；§3–§5 为**本档形式化与判定**；`§11E/11H` 正文**仍未读**；未制造候选／未启动搜索／未碰 RH。

## §7 【技术词回查】（补录）
```
技术词 locally toroidal 命中文件数=6    :: ./C3-parameter-table-spec-and-status.md ./C3-concretized-36s-63t-family.md ./C3-targeted-evidence-round.md 
技术词 Hermitian form   命中文件数=12   :: ./V294-A-finite-order-aggregation-gain-classification.md ./ASSETS-REGISTRY.md ./E8-ceiling-0682.md 
```
