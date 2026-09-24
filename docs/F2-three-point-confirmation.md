已查地图：命中（`P1-3-unresolved-finite-problem-pool`／`P1-2-stricter-search-no-math-gap-no-go`）⟹ 引用，不开新案
D0: 本档对象 = `F2`（`z(m,n;2,2)`）**三点确认**：含 `2026` 竞争情报与第二层（资产能否压平 `L<U`）初判；`F4` 留至下轮
D1: 0 （[REVIEW] 轮次：确认，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`F2` 三点确认**

## §1 ⭐ 确认结果

```
**(1) 问题存在且开放** ✓ —— `z(m,n;s,t)` ＝`m\times n` 二部图中不含 `K_{s,t}` 的最大边数；**`2026` 年文献逐字**："**Exact values are known only for small parameters or special families**"（MDPI 2026）✓✓
**(2) 目标参数未知** ✓ —— `RIT` 学位论文附录表（`z(m,n;2)`，`m,n=13..22`）**逐字**："**Exact values are shown in bold, all other values are upper bounds**" ⟹ `13..22` 区间**多数条目只有上界**（exact 靠 `nauty` 逐项核）；对角线 exact 值来自 `Dybizbański–Dzido–Radziszowski [DybET13]` ⟹ **前沿附近存在成片"只有上界"的 `(m,n)`** ✓✓
**(3) 无后续已解决** ⛔ **不成立（部分）** —— **`2026` 年 `arXiv:2605.01120`（Bhan 等，"New Bounds for Zarankiewicz Numbers via Reinforced LLM Evolutionary Search"）**：**首次定出** `Z(11,21,3,3)=116`、`Z(11,22,3,3)=121`、`Z(12,22,3,3)=132`，并对 **`41` 个进一步参数建立下界**，"**several that are within one edge of the best known upper bound**" ✓✓ ⟹ **"差一边"的盒子正被 LLM 演化搜索团队系统性收割** ✓
```

## §2 第二层：我方资产能否把 `L<U` 压成等号？

```
**【能一侧】** **构造侧（抬下界）**：我方 `D` 的构造搜索可用 ⟹ 但 ⚠️ **正是 `arXiv:2605.01120` 的强项**（LLM 演化搜索专攻构造）⟹ **竞争激烈** ✓
**【相反一侧】** **穷尽侧（压上界）**：需证明"不存在 `U` 边的 `K_{s,t}`-自由图" ⟹ **`SAT+DRAT` 或对称压缩＋穷尽** ⟹ **这才是 `D` 的差异化优势**（"certificates of completeness"，源仓 `IJCAI 2025` 型）✓✓
【⟹ 初判】**`F2` CONDITIONAL PASS**：三点确认 `(1)(2)` 过、`(3)` 部分不过（须逐项查 `2026` 最新）⟹ **可用性取决于能否找到一个 `2026` 之后仍未被动过、且规模在 `D` 可处理范围内的具体 `(m,n)`** ✓
```

## §3 ⚠️ 关键战场选择（本档建议）

```
$$\boxed{\text{若选 }F2\text{，应打\textbf{穷尽侧}（上界），而非构造侧（下界）}}$$ ✓✓
【理由】 构造侧已被 LLM 演化搜索占据（`2026` 实测）；**穷尽侧的"完备性证书"是我方差异化** ✓
【⚠️ 已知难点】 穷尽侧规模：`K_{2,2}`-自由于 `n=22` 为 `484` 格 ⟹ **远超暴力**；须先做**对称压缩与可满足性编码**的可行性估计（**本轮未做**）✓
【⟹ 建议】**`F2` 先做"穷尽侧可行性估计"**（不计算，只估规模/对称群/编码），不成的概率不低 ✓
```

## §4 状态与下一步

```
【`F9`】**淘汰**（照录您的核查：`16`-clue 不存在性已是完成结果，算法＋完整性逻辑＋checker 均已写明 ⟹ 属"已解决问题的证明审计"，正是要避免的类型）✓
【`F2`】**CONDITIONAL PASS**（见 §1–§3）✓
【`F4`】 待做三点确认（`2026-08` 新工作已改善 `9` 个 `K_q(n,R)` 上界 ⟹ **不能信旧表的 gap**，须逐项查 `2026` 更新）⟹ **下一轮做** ✓
【⛔ 纪律】 本轮**未计算**；`n=38`／`TARGET-L9`／RH 未作筛选依据 ✓
【边界】 §1 三句为**逐字 snippet**（`arXiv:2605.01120` 摘要、`RIT` 论文附录表注、MDPI 2026 摘句）—— **未读全文、未逐项核前沿**；§2–§3 初判为**本档自行给出**；未制造候选／未启动搜索／未碰 RH。

## §5 【技术词回查】（补录）
```
技术词 穷尽侧        命中文件数=1    :: ./F2-three-point-confirmation.md 
技术词 完备性证书  命中文件数=1    :: ./F2-three-point-confirmation.md 
技术词 Zarankiewicz     命中文件数=3    :: ./F2-three-point-confirmation.md ./ASTRA-TYPE-OPEN-PROBLEM-TABLE.md ./AUDIT-POST-MORTEM-were-astra-problems-considered.md 
```
