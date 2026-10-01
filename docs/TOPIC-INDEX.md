结论: 已查地图：命中 2 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 组织性索引（课题分档）；非数学命题，不主张任何新值
D1: 0
ASSUMES: N/A (组织性索引)

# TOPIC-INDEX — 课题分档索引（每课题单独建档）

> 依 唐先生 2026-10-01 14:07 令：**每个课题单独建档**；**前沿方法论单独成资产**（见 `METHODOLOGY-ASSETS.md`）

## 一、已确认课题

| 课题 | 空间 | 状态 | 主档／索引 | 备注 |
|---|---|---|---|---|
| **RH 线** | A | 已封（多条 NO-GO） | `MASTER-STATUS-AND-CLOSURES.md`｜`INDEX-BY-DIRECTION.md` §A | 早期主战场；E/V/C 系列 |
| **119 线（K(10,1)）** | B | **进行中** | `MASTER-FAILURE-MAP-107-LINE.md`｜`ROUTE-FINGERPRINTS.tsv` | 覆盖码；SDP-3 ⟹ 106；107 = BÖW |
| **A23D4（depth-four 局部最优性）** | — | **已完成** | `A23D4-CLOSURE-2026-09-26-depth-four-local-optimality-theorem.md` ＋ dossier/archive/census｜`scripts/C2a_depth.py` | 完成但**此前未单独建档** ⟹ 本档补 |

## 一之二、**已建之"前沿已有成果"课题**（代号＝小灵按主题自定 ✓ 2026-10-01）

| **`ALIGN-LI`**（Li 系数对齐线） | A | **结果＝前沿已有** ⟹ 归档 | `topics/ALIGN-LI/README.md` | 证据：Λ₂(0)=5/36 与前沿一致 ✓ |
| **`ALIGN-COMPRESS`**（有限压缩–惯性对齐线） | A | **结果＝前沿已有** ⟹ 归档 | `topics/ALIGN-COMPRESS/README.md` | 证据：P27 = Bombieri（自曝重发现）⚠️ |

## 二、**待唐先生确认之二课题**（成果为**前沿已有**，但须单独归档 ⚠️）

| 候选 | 证据（档案原文） |
|---|---|
| ~~（甲）P27 / Bombieri 恒等式线~~ ⟹ **已建为 `ALIGN-COMPRESS`** ✓ | — |
| ~~（乙）Λ 矩线（有限阶矩↔个体 β）~~ ⟹ **已建为 `ALIGN-LI`** ✓ | `"Λ₂(0)=5/36≈0.1389（与前沿一致 ✓）"`；`"我方预言'任何固定有限阶矩都无法强制个体 β' 与前沿结论【一致】✓✓"` |

**请唐先生点名**（或另指名）：这两课题的**正式代号**与**主档**。确认后即建 `topics/<代号>/` 并归一其文档。

## 三、建档规范（每课题必备）

```
topics/<代号>/
  README.md    # 一句话陈述 + 状态 + 空间(A/B/无关) + ASSUMES 行
  MAIN.md      # 主档：目标、现状、封口判词
  ROUTES.md    # 路线与 NO-GO（引 CLOSED-ROUTES-MAP）
  ASSETS.md    # 本课题可复用资产（引 ASSETS-REGISTRY）
  METHOD.md    # 用过的/产出的方法论（引 METHODOLOGY-ASSETS）
  docs.md      # 本课题全部文档清单
```

**每条断言须带** `ASSUMES:`／`DERIVES-FROM:`（见 `CONVENTION-ASSUMES.md`）；机械门 `scripts/assumes_gate.sh` 已挂 pre-commit ✓
