已查地图：命中 406 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 档案约定（机器可读假设登记）；非数学命题，不主张任何新值
D1: 0

# CONVENTION — 断言必须有机器可读的假设登记（`ASSUMES`）

## 为何（本日实测之结论 ✓✓）

$$\text{正则从散文抽假设}:\ 91\ \text{条中}\ \textbf{52 条垃圾},\ \text{余者多为碎片（"与结论"/"对相关猜想"）} \Longrightarrow \textbf{\text{不可行}} ✗✗$$
$$\therefore\ \text{唯一可行解 ＝ \textbf{显式登记}}:\ \text{与其事后猜，不如写入；（覆盖率实测仅 }10.7\%\text{，且其中可用者极少）}\ ✓$$

## 约定（唯一真源：`docs/ASSUMPTIONS.tsv`）

| 列 | 含义 |
|---|---|
| `id` | 断言 id（同 `ID-CLAIMS.tsv`） |
| `assumes` | 分号分隔之**假设标签**（canonical，取自 `ASSUMPTIONS-LEXICON.tsv`） |
| `provenance` | `人工定标`（可信）／`正则(待清洗)`（不可信，待替换） |

**标签前缀（照 CLAIM-GRAPH-SCHEMA §3）**：`★`＝不可得/未证/代理（危险）；`△`＝单点验证；无前缀＝普通假设。

## 纪律（借 OpenMath 信任边界 ✓）

1. **未登记的假设不得使用**：迁移引擎对未登记 assumption **fail-closed** ✓
2. **假设 ≠ 推导**：若 X 是我方**已立**结论，应作为**路线前提＋license**，**不得**降格写进 `assumes`（本日曾犯 ✗）
3. **空间不混**（AMEND-27）：RH 类标签只在空间 A 文档出现；跨空间引用须显式标注
4. **不许批量灌正则结果**：`provenance` 非"人工定标"者，一律视为**待清洗**

## 落地状态

- ✅ `docs/ASSUMPTIONS-LEXICON.tsv`（词表：raw→class→canonical）
- ✅ `docs/ASSUMPTIONS.tsv`（登记册；**27 条最承重断言已人工定标**）
- ⏳ 其余 1263−27 条待补

## 写入即登记（**新断言必走** ✓ 2026-10-01 立）

**根因**：历史账 1263 条中人工定标仅 27 条（2.1%），且正则抽取不可行（91 条中 52 垃圾）⟹ 补历史账永远追不上。**故改为"诞生即登记"**。

每个新断言（新 `.md` 档或 `ID-CLAIMS.tsv` 新行）**必须**在档头给出：

```markdown
### <断言 id> — <一句话陈述>
ASSUMES: <标签1> | <标签2>        # ★=不可得/未证/代理  △=单点验证
DERIVES-FROM: <前提断言 id> ...   # 已立结论走此列，**不得**写进 ASSUMES
```

并**同批**在 `docs/ASSUMPTIONS.tsv` 追加一行（`provenance=人工定标`）。

**审计**：`python3 scripts/assumes_audit.py` ⟹ 输出覆盖率与 `docs/ASSUMES-BACKLOG.md`（按被引用次数排序的待补清单）。
