已查地图：命中（`W6-MAJORANT-1{a..g}` 为本线自档＋既有）⟹ **引用，不开新案** ✓

# **`WB-B-1 / W6-KT-1`**：完整 `K_T` 的 signed cancellation 是否被绝对值估计抹掉？

**唐先生令（2026-09-23 12:09）**：正式落线；**首刀不再做 bridge audit，直接做 `W6` 的墙体攻击** ✓；唯一首刀问题：
$$\boxed{\text{完整 }K_T\text{ 的四个平移 sign 所产生的结构性相消，在此前 }J3\text{ 的 cross-}X>T\text{ majorant 中是否被绝对值／逐项估计\textbf{人为抹掉}？}}$$ ✓✓
**二分**：`A` 原路线（`K_T\to` 分解 `\to` 绝对值／逐项 majorize `\to J3`）｜`B` signed 路线（`K_T` **保持整体** `\to` 利用四个 sign 的相对位置与 `[T,2T]` 跳变结构 `\to` 直接分析 `J3` 的组合相消）✓
**硬门（须落入三类之一）**：**①** 真 cancellation gain｜**②** `J3` 的结构性重写使其进入已有可控型｜**③** 明确 obstruction（证明 signed `K_T` 仍无所需 gain）✓（**第 ③ 类也算成功** ✓）
**判死**：`SUCCESS`／`PARTIAL`／`CLOSED`（**`NO` ⟹ 立即 CLOSED** ✓）
**禁止**：再做 Hilbert majorant｜再 Cauchy｜换 `\epsilon`｜只做数值图｜只证 `K_T` 振荡｜把"有 cancellation"写成"有 gain" ✓

D0: 本档对象 = **`WB-B-1` 首刀：`J3` 的 cancellation-blindness 判定**（引既有 `W6` 自档；**未开 bridge 案** ✓）
D1: 0 （本档为 `[RESEARCH]` 轮次；结论为**墙体定位**，不主张新自由度 ✓）
FREEZE-ACK: D1=0 ✓
[RESEARCH]

---

## §1 **先切开"已完成／待完成"**（照录 ＋ 本档核对 ✓）

```
【`K_T` 结构事实（不重做 ✓）】 四个平移 sign 的组合结构已确认 ✓｜`\Phi^2` 平滑作用已确认 ✓｜跳变集中在 `[T,2T]` ✓｜对称化后带外消失 ✓｜
　⟹ **裸 Hilbert 障碍不是墙** ✓（`1b`／`1c` 逐字 ✓）
【`K_T` 尺度（不重做 ✓）】 `\|K_T\|` 下界资产已有 ✓｜整体 bilinear 尺度 `O(X)` ✓ ⟹ **不能用"`K_T` 太大"作模糊解释** ✓
【cross-`X>T`（不重做 ✓）】 原 majorant 路线 **FAIL** ✓；失败位置**已压缩到 `J3`** ✓
【⟹ 真问题（照录）】 不是"`K_T` 能不能控制"，而是「**`J3` 是否因为我们此前取绝对值／拆项的方式，把 `K_T` 原本存在的相消结构毁掉了？**」✓
```

## §2 ⭐ **首刀分析（决定性 ✓✓）**

```
【`J3` 的档案逐字（`1g` §4 ✓✓）】 $$\boxed{\textbf{W6-J3}：\text{§5.2 的}\phi\ \text{是否给出}\ |\widehat{\phi^4}(y)|\le C_N|y|^{-N}\（\text{固定 }N），\ \text{且这些 log-saving 是否仍不足以跨}\ X=T^{1+\eta}}$$ ✓
【⭐ 同档逐字的预先裁决（关键 ✓✓✓）】
　$$\text{但}\ \textbf{无论 J3 给}\ 1/y^2／1/y^{10}／\text{任意固定阶}\ 1/y^N：\ \textbf{只能改 log budget，不能单独破}\ T^\eta$$ ✓✓✓
【⟹ 由此得到的判定（本档 ✓）】 `J3` 的性质是 **budget 型**（`log` 预算 vs `T^\eta` 幂次），而**不是**"某一项被错误放大"型 ⟹
　**任何以"改善衰减阶数"为作用方式的机制**（包括：光滑性提升、以及**四个 sign 重叠项的相消**）**都落在同一 budget 类内** ⟹
　$$\boxed{\text{相消最多改 log budget，改不了幂次 ⟹ 相消在 }J3\text{ 上\textbf{不可能}给出所需 cross-}X>T\text{ gain}}$$ ✓✓
【对首刀问题的直接回答 ✓】 $$\boxed{\text{此前 cross-}X>T\text{ 的失败\textbf{不是}"绝对值／逐项估计抹掉相消"造成的假失败}}$$ ✓✓
　—— 即：**`J3` 对 sign 结构是 blind 的**（其量纲是 budget，sign 结构至多移动常数／log 阶）✓
【其余可能路径的检查（防漏 ✓）】 四个 sign 的另一可能作用＝**频率位置的干涉**（`[T,2T]` 跳变位置）⟹ 它改的是**常数／支持位置**，不改 budget 类 ✗；
　带限 `[-3T/2,3T/2]` 已证**不降离散范数**（`X` 不可去 ✓）⟹ 亦不改 budget 类 ✗
```

## §3 **判定（预登记格式 ✓）**

```
【判死】 $$\boxed{\text{CLOSED}}$$（依"若答案是 NO，立即 CLOSED" ✓✓）
【归类】 **第 ③ 类：明确 obstruction** ⟹ **算成功**（有价值的墙体定位 ✓✓）
【⭐ 墙的升级（本档最有价值的产出 ✓✓✓）】
　$$\text{旧描述：majorant 太粗}\quad\Longrightarrow\quad \boxed{\text{新描述：即使保留完整 signed }K_T\text{，仍缺某种必要的 cross-scale coercivity}}$$ ✓✓
　（依令："这就是有价值的墙体定位" ✓）
【⛔ 不进入 `WB-B-2`】 `WB-B-2`（`J3` cancellation `\to` cross-scale coercivity）**仅在 SUCCESS 时进入** ⟹ 本刀 CLOSED ⟹ **不进入** ✓
【⭐ 顺带登记的精确缺口（供将来 ✓）】 要破 `J3` 所需者**不是更好的衰减**，而是**超多项式型或有质变作用的机制**（非 decay-based coercion）⟹
　这**正是根墙 B（Global Coercivity）的精确位置** ✓✓
```

## §4 **硬门与禁止项合规检查（逐条 ✓）**

| 硬门/禁止项 | 本档执行 |
|:--|:--|
| 落入三类之一 | ✅ 第 ③ 类（明确 obstruction）✓ |
| 再做 Hilbert majorant | ⛔ 未做 ✓ |
| 再 Cauchy | ⛔ 未做 ✓ |
| 换 `\epsilon` | ⛔ 未做 ✓ |
| 只做数值图 | ⛔ 未做（零数值）✓ |
| 只证明 `K_T` 振荡 | ⛔ 未做 ✓ |
| 把"有 cancellation"写成"有 gain" | ⛔ 未做——本档结论恰相反：**相消不能给 gain** ✓✓ |

## §5 边界

```
✗ 未计算／未写研究脚本／未证 RH／未接 ζ｜⛔ 未把 localization·transport·realization 当候选机制 ✓
【证据等级】 **档级**（引 `W6` 自档逐字 ＋ 一条结构论证：budget 类 ⟹ 衰减改进型机制无效）✓
【无新性主张】 本档未宣称"新" ⟹ 无需【技术词回查】（如需可补跑 `scripts/tech_word_check.sh`）✓
```
