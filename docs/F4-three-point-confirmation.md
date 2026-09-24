已查地图：命中（`P1-3-unresolved-finite-problem-pool`／`F2-three-point-confirmation`／`C1-LIN-linear-covering-codes-locked`）⟹ 引用，不开新案
D0: 本档对象 = `F4`（覆盖码 `K_q(n,R)`）**三点确认** ＋ 第二层（资产能否压平 `L<U`）初判
D1: 0 （[REVIEW] 轮次：确认，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`F4` 三点确认**

## §1 ⭐ 一手证据（`arXiv:2608.19872`，2026-09-02 提交，逐字）

```
【规模】"We improve the known bounds on `K_q(n,R)` **in 83 cases (82 distinct cells)**" ✓
【上界侧】"**25 improved bounds for `5\le q\le15`** … **the first improvements to any upper bound on `K_q(n,R)` with `q\ge5` since the 2011 revision of Kéri's tables**"；例子"**`K_6(8,4)\le166` (previously 216)**" ✓✓
【双侧改善一例】"**One cell is improved from both sides: `441\le K_6(10,4)\le2751`, previously 417–2952**" ✓ ✓
【证书】"**All codes and certificates are provided in machine-readable form together with standalone verifiers**" ✓✓ ⟹ **该跑道已自带证书与独立校验器** ✓
【权威表源】`Kéri` 表（`old.sztaki.hu/~keri/codes/index.htm`）为现行 best-known bounds 表 ✓
```

## §2 三点确认判定

```
**(1) 问题存在且开放** ✓ —— 经典结论（`Cohen–Lobstein–Sloane` 型综述逐字）："**Only few values … are exactly determined. Mostly, only lower and upper bounds are known, with large gaps in between**" ✓✓
**(2) 目标参数未知** ✓ **但须逐格核** —— 多个 `(q,n,R)` 仍 `L<U`；**具体哪些在 `2026-08/09` 之后仍开，须对 `Kéri` 表逐格比对** ✓
**(3) 无后续已解决** ⚠️ **部分不成立** —— `2026-09-02` 论文一次性改善了 **`82` 个 distinct cells** ⟹ **前沿刚被移动** ✓
```

## §3 ⚠️ 第二层（资产能否把 `L<U` 压平或推进一侧）—— 初判**弱**

```
**【关键观察】该族 gap 多为\textbf{大口径}，不是"差一"** —— 例：`441\le K_6(10,4)\le2751` ⟹ **`L` 与 `U` 相差 `6` 倍** ✓✓ ⟹ **不存在"只差一边"的近失型目标**（与 `F2` 的"within one edge"形成对比）✓
**【构造侧（抬下界）】** 我方 `D` 可用，但 **`2026-09` 论文的 LM/LNS 搜索＋证书链已占据该侧** ⟹ **竞争激烈** ✓
**【穷尽侧（压上界）】** 覆盖码上界改善的现代路线是 **`LM/LNS` 搜索 + 传播**；**穷尽证明"不存在更小码"在中大口径下不可行** ✓
**【我方差异化之所在（但未建）】** **可机器核验的\textbf{下界}证书**（如 `SDP`/矩方法对偶证书、或 LP 对偶）—— 该技术我方**尚无** ⟹ 若要打，须先"造工具"（`P1-2` 已证该模式风险高）✓
【⟹ 初判】**`F4` 第二层 = 弱**：`L<U` 是**大口径**而非"差一"，**无近失型目标**；且构造侧被 `2026` 证书化流水线占据 ⟹ **大概率只能重跑构造搜索** ✓✓
```

## §4 结论与建议

```
$$\boxed{F4:\ (1)(2)\ \text{过（须逐格核）};\ (3)\ \text{部分不过};\ \text{第二层弱}\ \Longrightarrow\ \textbf{不建议直接投计算}}$$ ✓
【若仍要打，唯一合法形态】 先在 `Kéri` 表上**逐格筛**，找**同时满足**：**(a)** `2026-09` 之后仍开；**(b)** `U-L` 为**小常数**（"差一"型）；**(c)** 参数小到 `D` 可穷尽 ⟹ 三条同时成立者才立项 ✓
【⚠️ 预期】 按 §1 证据（该族 gap 多为大口径），**(b)** 命中概率不高 ✓
【⛔ 纪律】 本轮**未计算**；`n=38`／`TARGET-L9`／RH 未作筛选依据 ✓
【边界】 §1 全为**逐字 snippet**（`arXiv:2608.19872` 摘要、`Cohen–Lobstein–Sloane` 综述句）；**未读全文、未对 `Kéri` 表逐格核**；§3–§4 为**本档初判**；未制造候选／未启动搜索／未碰 RH。
