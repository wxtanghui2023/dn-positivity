已查地图（**先查后写**）：`ls docs | grep -E "^C1[0-9][0-9]"` 全量号表 ＋ 重号扫描（`uniq -c`）。

# 勘误 · **C-121 至 C-128 重号**（两条线并行编号）＋ 处置规则

> **发现时间**：2026-09-19 11:1x（我自己在给新档编号时撞号，随即全量扫描）
> **性质**：**档案完整性**问题（编号唯一性），不涉及数学内容

## §1 事实（实测）

```
扫描: ls | grep -oE "^C1[0-9][0-9]" | sort | uniq -c | awk '$1>1'
结果: C121 2档 | C122 2档 | C123 2档 | C124 2档
      C125 2档 | C126 2档 | C127 2档 | C128 2档
```

**原因**：两条线（① B2-1／LP-前沿线；② 尺度-墙／log-free 线）在 2026-09-18 同一时段**各自独立编号**，都从 C-121 起，造成 8 个号各 2 档。

## §2 具体重号清单

| 号 | 线① | 线② |
|:--|:--|:--|
| C-121 | `C121-directional-correction-and-three-layer-design-A-measured.md` | `C121-conceptual-correction-scale-law-asset-beta-channel-priority.md` |
| C-122 | `C122-C121-B-first-cut-Toeplitz-PSD-K2-audit-...md` | `C122-beta-channel-noncanonicalization-audit-three-requirements.md` |
| C-123 | `C123-C121-B2-1-mixture-essentiality-first-cut-...md` | `C123-scan-...-erratum-to-C122-and-failure-point-is-iii.md` |
| C-124 | `C124-B2-1-ii-three-cuts-...md` | `C124-family-shape-bypasses-POS1-first-rung-...md` |
| C-125 | `C125-R-audit-R1-R2-...md` | `C125-density-chain-cannot-give-fixed-delta-...md` |
| C-126 | `C126-B2-1-formal-suspension-...md` | `C126-log-free-exclusions-zero-examples-...md` |
| C-127 | `C127-EXT-SCAN-4-persistent-homology-...md` | `C127-merge-aggregate-pointwise-wall-...md` |
| C-128 | `C128-shape-test-...md` → **已改号 C-130** | `C128-uniform-counting-bound-candidate-...md` |

## §3 处置（三项，即刻生效）

1. **不回溯改历史档**（避免破坏既有点名引用）；**引用时必须带文件名**，不得只写"C-12x"。
2. **本档之后的编号规则（硬）**：编号前必须先跑
   `ls docs | grep -oE "^C[0-9]+" | sort -V | tail -3`
   取**严格大于现有最大值**的号；且**一次只由一条线分配号**。
3. **本档之后新档凡自称"C-1xx"必须写全文件名**，否则视为无编号（可信度按"无编号档"处理）。

## §4 边界

- ⚠️ 本档**只**处理编号唯一性；**不改**任何数学内容、**不改**任何既有判词 ✓
- ⚠️ §1／§2 为**实测**（`ls` ＋ `uniq -c`）✓
- **未用** RH；**未改**原档（仅改我自己新档的号）✓

FREEZE-ACK: 本档即冻结期内的档案完整性勘误（依 `§8.1`）
D0: 本档对象 = C121–C128 重号的登记与处置规则（关系 = 档案完整性勘误，非新机制）
D1: 0
