已查地图：命中（`TARGET-L9-source-fetch-report`／`C1-LIN-TOP1-3-scan`）⟹ 引用，不开新案
D0: 本档对象 = `TARGET-L9` 五项判定（据 README 全文）＋ 真实入口识别 ＋ 首攻规格
D1: 0 （[REVIEW] 轮次：判定与规格化，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`TARGET-L9`：五项判定（README 全文为依据）**

## §1 五项（逐条，含逐字）

```
**(1) 39 列记录的确切 `H`？** README 未载（在 `compute/` 内）；但**族内已定位**：`q11` 的"**fibered graph plus kernel**"族 "**contains the documented lengths at `r=4,7,8,9`**" ⟹ `r=9` 记录 `39` 属该族 ✓
**(2) 38 列搜索的 17 个 kernel-block classes？** ✓ 逐字："**The nearest miss is at `r=9`: `n=38` would beat `\ell_2(9,2)\le39` and reduces inside the family to exactly 17 kernel-block classes**" ✓✓
**(3) "14 missing incidences"？** ✓ 逐字："**all 17 of which anneal to the same floor of 14 missing incidences**" ✓
**(4) 17 类是否穷尽**目标结构族**？** ⚠️ **精确回答**：17 类穷尽的是"**该 fibered 族在 `r=9` 的全部情形**"（"reduces inside the family to exactly 17…"），**不是**全部 `r=9` 覆盖码 ✓✓ —— 关键区分：**族内穷尽 ≠ 全局穷尽** ✓
**(5) 是否另有结构入口？** ✓ **是** —— 见 §2 ✓✓
```

## §2 ⭐⭐ 真实入口（本档核心）

```
【入口 A｜族内待判】 逐字："**none of which the exact solver decides**" ⟹ **17 类的精确判定是明确的有限任务**（`9\times38` 二元矩阵 ＋ 512 综合征覆盖条件），**现有 exact solver 未决** ✓✓
【入口 B｜族外空间】 该族仅为**子族**（README 明示它 `r\le8` 恰好复现记录 `\ell_2(8,2)\le26` 且"cannot beat it"）⟹ **`r=9` 的 38 也可来自族外结构** ✓✓
【入口 C｜把 `q10` 的方法搬到 `r=9`】 `q10` 在 `r=10` 用**指定自同构**推进（"order 7 is settled at `r=10` for every fixed-space dimension"）⟹ **`r=9` 未见对应记录** ⟹ **可套用** ✓
【⚠️ 已被封的路（勿重走）】 `r=10`：`n=49` 仍有 **7 holes**；`r=11`：orders `11,17,23` 均无低于 `79` 的不变集 ⟹ 这两个点**不要碰** ✓
```

## §3 首攻规格 ＋ 措辞纪律

```
**【`TARGET-L9`】** $$\boxed{\text{目标：}\ell_2(9,2)\le38\quad\text{或}\quad\text{精确判定 17 类（`residue` 结清）}}$$ ✓
**【第一步（两选一，皆有限）】** **(i)** 取 `compute/q11` 的**族定义与 17 类构造**，复现"14 missing incidences"地板，写出**该有限对象的显式规格**；**(ii)** 直接对某一类写 **SAT/exact 判定**（变量＝38 列的 kernel 部分；约束＝512 综合征至多两列覆盖）✓
**【量变（`SURVIVOR-5`）】** $$39\to38$$（`r=9` 长度减一，即**公开上界实质改进**）✓✓
**【`G2` 结构入口】** projective／quotient-fiber／kernel-block／automorphism-prescribed（⛔ 禁无结构枚举）✓
**【措辞纪律（照录）】 现状只可写** $$\boxed{\text{record: }\ell_2(9,2)\le39,\quad n=38\ \text{尚未找到}}$$ **不得**写成 `\ell_2(9,2)=39` ✓✓
【边界】 §1 各条为**逐字**（README 全文，2026-09-24）；§2/§3 识别与规格为**本档自行推导**；未制造候选／未启动搜索／未碰 RH。
