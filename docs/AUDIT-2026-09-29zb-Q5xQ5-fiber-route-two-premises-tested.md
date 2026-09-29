# AUDIT-2026-09-29zb —— $Q_{10}=Q_5\times Q_5$ fiber 路线：**两前提实测**（① 未证/有压力；② 22% 不成立）✗

> **性质**：**审计＋最小实验**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 16:05 ✓

**已查地图**：`WITFIB-2026-09-28`（单坐标 fiber ＝精确重述）／`AUDIT-29s`／`CALIBRATE-n*`（defect 放大）✓

D0: 本档对象 ＝ **档案已有**（fiber 分解／$Q_5$ defect—皆在档 ✓）
D1: 0（产出＝**两前提实测 ＋ 一合法 120-cover 证书** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 前提甲（某 fiber }\ge5\text{）}:\ \text{cap}{=}4\ \text{贪心\ \textbf{4/4 全败于 128 词}}\ \Longrightarrow\ \textbf{有压力但未证}\ ⚠️}$$
$$\boxed{\text{② 前提乙（5-截面 }\mathrm{Def}{=}4\text{）}:\ \textbf{仅 }12/54\ (\approx22\%)\ \Longrightarrow\ \textbf{不成立（未强迫）}\ ✗}$$
$$\boxed{\text{③ 副产品}:\ \text{合法 }\mathbf{120\text{-cover}}\ \text{已得（自修截断文件）}\ \Longrightarrow\ K(10,1)\le120\ \text{可重跑证书}\ ✓✓}$$
$$\boxed{\text{④ 判定}:\ \text{承重前提乙实测弱}\ \Longrightarrow\ \text{按唐先生顺序，不能继续跨 fiber 补洞}\ ⚠️}$$

## §1 前提甲实验（✓）

$$Q_{10}=Q_5\times Q_5,\ \text{fiber}=u\text{-层};\ \text{硬 cap}{=}4\ (\text{等价 }|C|\le32\cdot4=128)$$
$$\text{贪心}\ \times4\ \text{种子}:\ \text{全部恰好用尽 }128\ \text{词而\ \textbf{仍未覆盖完全}}\ ✗$$
$$\text{对照（无 cap）}:\ 147\text{--}150\ \text{词},\ \text{fiber max }6\text{--}7$$
$$\therefore\ \boxed{\text{"某 fiber }\ge5"\ \text{有支持\ ✓\ 但贪心失败}\neq\text{不可能}\ ⚠️}$$

## §2 前提乙实验（✗ 关键）

$$\text{对 }3\ \text{个覆盖码（}|C|{=}147/150/149\text{）的 }54\ \text{个 }\ge5\text{-fiber，取 5-截面 }A\text{，算 }\mathrm{Def}_{Q_5}(A)=30-|N_1^{Q_5}(A)|$$
$$\text{分布}:\ 4{:}12,\ 5{:}2,\ 6{:}14,\ 7{:}10,\ 8{:}10,\ 9{:}3,\ 10{:}1,\ 11{:}2$$
$$\therefore\ \boxed{\mathrm{Def}{=}4\ \text{占 }22\%;\ \text{中位数 }6\ \Longrightarrow\ \textbf{未被强迫}}\ ✗$$
$$\text{而 }Q_5\ \text{放大定理要求 }\mathrm{Def}{=}4\ \text{恰等}\ \Longrightarrow\ \text{承重前提实测弱}\ ✗$$

## §3 副产品：合法 120-cover（✓✓）

$$\text{起点}=\texttt{kam.txt}\ \text{的 }118\ \text{词（合法但截断，}12\ \text{点未覆盖）};\ \text{补 }2\ \text{词}\Rightarrow\ |C|{=}\mathbf{120},\ \text{全覆盖}\ ✓$$
$$\therefore\ \boxed{K(10,1)\le120\ \text{我方\ \textbf{可重跑证书}}\ ✓✓\ (\text{与公开记录一致})}$$

## §4 边界（硬 ✓）

- **全部实测（cap 贪心、54 截面 Def 分布、120-cover 覆盖检验）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；**不裁定**路线生死（属唐先生）✗
