已查地图：命中（`REVERSE-POSTMORTEM-weapons-correctly-used`／`CORRECTION-cases-show-move-not-compute`／`META-OBSTRUCTION`）⟹ 引用，不开新案
D0: 本档对象 = `Astra-Transfer` 三攻击登记（global→local／fixed→moving `T_\rho`／defect→bounded potential）
D1: 0 （[REVIEW] 轮次：登记与排序，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`Astra-Transfer`：三攻击登记（唐先生 2026-09-23 22:41 裁示）**

【核心判据（照录）】 首次尝试失败 ≠ 武器失败；而是"揭示了缺失的自由度/不变量/位置信息"，然后**换对象**。证据语言：missing invariant／missing degree of freedom／global norm forgets location／decisive change of setting。

【三攻击（含顺序）】
- **A｜global → local / β-sensitive**：不问"如何让统计量对 β 敏感"，而问"**当前量丢掉了 β 的哪一种信息**"（对应 sphere-packing："global norm forgets where the negative mass lies"）。
- **B｜fixed → moving `T_\rho`**：让测试对象**随 `\rho` 移动**，最终仍压回**低维 scalar inequality**（对应 moving stabilizer representation；不是更大矩阵/SDP）。
- **C｜defect → bounded potential**：寻找 `\text{离轴 defect}\Rightarrow\Delta P(\rho)>0` 且 `P\in[0,1]` ⟹ 转为**potential budget** 问题（对应 entropy→potential→bounded potential）。

【纪律】 不重启 RH 总攻；只围绕已冻结的**有限离轴零点**；不追 `668`／`R(5,5)` 型数字缺口；模板来自 Astra 已成功案例。
【下一步】 先做 **A**：逐项审计我们现有量各自丢弃 β 的哪一类信息（位置/符号/多重度/参数依赖），产出"丢弃清单"。
【边界】 全部为登记与排序；未制造候选／未启动搜索／未改状态。

## 【技术词回查】（补录）
```
技术词 translation-before-launch 命中文件数=1    :: ./AUDIT-POST-MORTEM-were-astra-problems-considered.md 
技术词 机制可得性  命中文件数=1    :: ./AUDIT-POST-MORTEM-were-astra-problems-considered.md 
```
