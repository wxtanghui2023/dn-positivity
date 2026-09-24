已查地图：命中（`P1-2-stricter-search-no-math-gap-no-go`／`RESEARCH-PIVOT-asset-centered-independent-problem-pool`）⟹ 引用，不开新案
D0: 本档对象 = `C2` 首轮检索结果：**未定位到"仍开放"的计数冲突**（负结果）＋ 下一轮精确检索位置清单
D1: 0 （[REVIEW] 轮次：检索与清单，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`C2` 首轮：未定位到仍开放冲突（负结果）**

## §1 本轮做了什么

```
【检索式】 "two independent enumerations disagree counts unresolved discrepancy …"（advanced）✓
【结果】 返回**均为通用枚举文献**（图枚举综述、匹配枚举、独立集计数等），**无一条给出"两地计数冲突且未被消解"的具体实例** ⟹ **本轮 `0` 靶子** ✓✓
【⟹ 判定】 不硬挑、不把"历史 discrepancy"冒充研究突破 —— **维持"继续搜索"状态** ✓✓
```

## §2 已由您排除的三例（照录，避免重复劳动）

| 靶子 | 曾有冲突 | 后续已消解 | 状态 |
|:--|:--:|:--:|:--|
| Latin squares／isotopy classes（`562\to564`） | ✓ | ✓ | ❌ |
| `18`-run 3-level OA | ✓ | ✓ | ❌ |
| `2609.20492` Leech tree | 不适用 | 已有结果 | ❌ |

```
【方法学正例（保留为"模式有效"的证据，非靶子）】 `McKay–Wanless` 的 Latin-square 枚举**明确纠正了前文献错误** ⟹ "计数冲突 → 重新枚举 → 新结果"是**成熟产出模式**，非我们凭空设计 ✓✓
```

## §3 ⭐ 下一轮精确检索位置（本档提出，附三道门测点）

```
**`L1`｜骑士巡游（knight's tour）计数**：`8\times8` 开/闭巡游的文献值有**历史分歧**（`Loebbing–Wegener` vs 后续）⚠️
　**`C2-2` 必查**：**有向 vs 无向**、含起点／旋转对称折半 —— 这是最可能的"假冲突"来源 ✓
**`L2`｜幻方（magic squares）计数**：`6` 阶数值在文献中有**早期错误与修正**史；`5` 阶亦有多源记载 ⚠️
**`L3`｜Latin squares 高阶计数**（`11`／`12` 阶、reduced LS）多源记载 ⚠️
**`L4`｜组合设计表**（`2`-`(v,k,\lambda)` designs、STS 高阶）—— `Kaski–Östergård` 型枚举表中**是否存在未二次独立验证的条目** ⚠️
**`L5`｜OEIS 型"两值并存"注释**：直接检索 `"two values"`／`"discrepancy"`／`"incorrect"` 类注释条目 ✓✓（**最省力、最易命中**）
**`L6`｜census 计数**（小图/竞赛图/二元结构）—— 找**只有一次枚举、无第二独立枚举**者（此时冲突不存在，但**完整性**可查，属 `C3`／`C4`）✓
【优先】 `L5` ＞ `L1` ＞ `L2` ＞ `L3`／`L4` ＞ `L6` ✓
【三道门（照录）】 `C2-1` 冲突仍开放（无 correction／erratum／later census）｜`C2-2` 两边必须**同一数学对象**（排除 labeled/unlabeled、iso/isotopy、ordered/unordered、rooted/unrooted、geometric/combinatorial、参数定义差异）｜`C2-3` **成功后新命题必须提前写出**：$$\text{"该对象精确计数为 }N\text{"}\quad\text{或}\quad\text{"文献 A 遗漏某类，共漏 }k\text{ 个"}$$ ✓✓
【边界】 §1 为**检索事实**；§2 照录您已排除项；§3 位置清单为**本档提出**（`L1`–`L6` **均未核查**，⚠️ 标注未验证）；未制造候选／未启动搜索／未碰 RH。
