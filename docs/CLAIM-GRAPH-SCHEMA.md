结论: 已查地图：命中 406 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 项目内工具/schema（非数学命题；不主张任何新值）
D1: 0

# CLAIM-GRAPH-SCHEMA v0 — 断言图 schema（借 OpenMath 之数据模型／信任边界 ✓）

> 依 2026-10-01 决策：**借 schema 与信任边界设计，不依赖 OpenMath 代码**（其论域＝整数多项式＋MP，我方数学整体在片段之外 ✗）

## 1 节点（断言）

| 字段 | 含义 | 取值 |
|---|---|---|
| `id` | 唯一标识 | `E###`／`V###`／`C-###`／`F#`／`R##` |
| `stream` | 线 | `main`／`spaceA`(RH)／`spaceB`(119/资产) |
| `doc` | 来源文件 | `docs/<slug>.md` |
| `status` | **逻辑状态** | `axiom`｜`proven`｜`conjectured`｜`unknown`｜`DEAD`｜`NO-GO`｜`alias` |
| `assumptions` | **显式假设集（★必填）** | 字符串数组（如 `RH`、`(D)′`、`M=106`、`i=40..44`） |
| `obligations` | 未闭合前提 | 字符串数组 |
| `evidence` | 证据/出处 | `{kind, source, note}` |
| `fingerprint` | 上下文指纹 | 含 `language/domain/axiomSet/statement` 之 hash（借 OpenMath `claimKey`）|

## 2 边（推导）

| 类型 | 含义 |
|---|---|
| `derives` | 由…推出（真依赖） |
| `references` | 仅引用 |
| `refutes` | 反驳/否证（**非依赖** ⟹ 不得计入支撑） |
| `supersedes` | 取代（alias 关系） |
| `uses-assumption` | 断言 → 假设节点 |

## 3 信任边界（照抄 OpenMath 之纪律 ✓✓）

1. **`confidence` 仅在 `proven`（或 `axiom`）时为 1，否则 `null`** ✓
2. **`supportScore` ≠ 真值概率**；"长期没找到反例"只记搜索启发式，**不因次数自动升级** ✓
3. **公理/假设政策在模型控制之外** —— LLM 不得自批新公理（逐字："Automatically allowing an LLM to approve its own new axioms would destroy the intended trust boundary"）✓
4. **反循环**：最小不动点从 `axiom`＋已验证节点播撒；互相引用的未证节点**不得**获得 `proven` ✓
5. **fail-closed**：前提陈述须逐字匹配；缺失/不匹配即报错，不静默通过 ✓

## 4 自动审计（脚本 `scripts/claim_graph.py`）

- **A 循环支撑**：SCC＞1 或自环 ⟹ 候选"循环论证" ✗
- **B 悬空断言**：被引用但自身无 `derives` 出边且非 `proven/axiom` ⟹ 无支撑 ✗
- **C 未声明假设**：文本含"假设/条件下/模 X/若…成立"却未登记 `assumptions` ⟹ 我方最大复发性失效之候选 ✓
- **D 反驳误用**：`refutes` 边被当作支撑计入 ✗
