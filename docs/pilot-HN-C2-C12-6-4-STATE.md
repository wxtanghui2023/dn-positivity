已查地图：见 docs/TOPIC-INDEX.md（L1 课题级 · HN-C2 覆盖设计）
D0: 本档对象 = 试点状态（工具产物）；非数学命题，不主张任何新值
D1: 0
ASSUMES: N/A (状态档)

# pilot HN-C2 — $C(12,6,4)$ 试点状态（2026-10-01 15:3x）

## 已得 ✓

$$\text{[① n}\le41\text{]}:\ \textbf{FEASIBLE}\ (\text{CP-SAT}\ 1.7\,\mathrm{s},\ 16646\ \text{冲突},\ 972358\ \text{分支})\ \Longrightarrow\ \textbf{\text{41 块显式构造，覆盖 }495/495\ \text{完备}}\ ✓✓$$
⟹ **独立复现 best-known 上界 41，且带可复核证书**（41 个 6-块，见 `out/ljcr_c12_cpsat.log`）

## 结果（300 s 轮）⏳⟹加长重跑

$$\text{[② n}\le40\text{]}:\ \textbf{UNKNOWN}\ (300\,\mathrm{s}\ \text{用尽}:\ 3{,}456{,}004\ \text{冲突},\ 37{,}921{,}730\ \text{分支})\ \Longrightarrow\ \textbf{\text{未决（不作不存在证据）}};\ \text{已启动 }1800\,\mathrm{s}\ \text{长跑（仅 }n{=}40\text{）} ✓$$

## 待决 ⏳

$$\text{[② n}\le40\text{]}:\ \text{CP-SAT 上限 }300\,\mathrm{s}\ \text{运行中};\ \text{三出口}:\ \textbf{FEASIBLE}\ (\text{上界 }41\to40,\ \text{记录改进})\ \mid\ \textbf{INFEASIBLE}\ (\Longrightarrow C(12,6,4)=41\ \text{精确},\ \text{gap 闭合})\ \mid\ \textbf{UNKNOWN}\ (\text{未决，不作不存在证据})$$

**工具** ✓：`scripts/ljcr_C12_6_4_cpsat.py`（CP-SAT）｜`scripts/ljcr_C12_6_4.py`（HiGHS 版，已因求最优过慢中止）
**数据** ✓：块 $=C(12,6)=924$；4-子集 $=C(12,4)=495$；Schönheim 下界 $=\lceil495/15\rceil=33$（**与库下限 40 相差 7** ⟹ 库下限来自更强方法，待核）

## 纪律

$$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{41 构造可秒级复核} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## 【技术词回查】

```
技术词 试点状态     命中文件数=1    :: ./pilot-HN-C2-C12-6-4-STATE.md
```

ROUTE-CHECK: <全部>=NEW
