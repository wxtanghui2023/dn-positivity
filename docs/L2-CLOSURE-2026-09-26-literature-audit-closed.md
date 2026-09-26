已查地图：已跑 scripts/prework_map_check.sh K(10,1) 文献 SDP 2026 ⟹ 执行自 `docs/L2AUDIT-2026-09-26-gijswijt-polak-sdp-cell-audit.md`（格值钉死 ✓）；本档为 **L-2 关档**（唐先生 2026-09-26 21:18 令 ✓）。
D0: 本档对象 = 2024–2026 covering-code 文献对 $K_2(10,1)$ 的影响（检索对象）
D1: 0（产出为关档结论与证据链冻结）

# L2-CLOSURE-2026-09-26 · 文献审计关档

## §0 关档结论（先给）

```
$$\boxed{\textbf{L-2 状态}:\ \textbf{CLOSED}（审计完成，无新界）\ ✓✓}$$
$$\boxed{\text{2025–2026 新 SDP 文献：\textbf{方法升级 ✓}；}K_2(10,1)\ \textbf{cell 新界} = 106\ ✓;\ \textbf{不足以改变 119 目标状态}\ ✗}$$
$$
$$
```

## §1 证据链（冻结 ✓）

```
$$\text{① 对象一致}:\ 2504.01932v2\ \text{处理一般（非线性）}q\text{ 元覆盖码 }K_q(n,r)\ ✓\ \text{（与 119 线同对象 ✓）}$$
$$\text{② 格值逐字}:\ \text{Table 5（}q=2,R\le6\text{）},\ n=10,\ R=1\ \Longrightarrow\ \mathbf{105.2223}\ ✓\ \text{（\textbf{无星号} ⟹ 论文自认未改进该格 ✓）}$$
$$\text{③ 整数化}:\ \lceil105.2223\rceil=106\ \Longrightarrow\ K_2(10,1)\ge106\ ✓;\quad \text{距 119}:\ 119-106=\mathbf{13}\ ✓$$
$$\text{④ 未越过旧下界}:\ 106<107\ (\text{已知最好下界，BÖW 2004})\ \Longrightarrow\ \text{该 SDP 在}\ (2,10,1)\ \text{格\textbf{不是 improvement}}\ ✗\ ✓$$
$$\text{⑤ 方法确有效（旁证）}:\ n=8,R=1\ \text{格}=31.9999\Rightarrow K_2(8,1)\ge32=\text{已知值}\ ⟹\ \text{界紧}\ ✓\ \text{（非空转 ✓）}$$
$$\text{⑥ 基线阶梯（不可混用 ✓）}:\ 93.09\ (\text{球覆盖})<103\ (\text{van Wee 1988/1991})<\mathbf{107}\ (\text{BÖW 2004})\le120\ (\text{上界，Östergård 构造})\ ✓$$
$$\text{⑦ 旁证一致}:\ \text{论文脚注}\ K_2(18,1)/K_2(30,1)\ \text{改进已被 Wu–Chen 2024 超过}\ ✓\ \text{（与档案一致 ✓）}$$
$$
$$
```

## §2 关档判定

```
$$\textbf{否证对象}:\ \text{“2024–2026 文献已把 }K_2(10,1)\ \text{下界推到 119 附近（或形成新界）”}\ \Longrightarrow\ \textbf{否}\ ✗\ \text{（格值 105.2223／整数 106 ✓）}$$
$$\textbf{未否证}:\ \text{“未来新方法可做到”}\ ✓;\ \text{“119 不可能”}\ ✗\ \text{（本档不作此主张 ✓）}$$
$$\textbf{剩余待钉（不影响关档 ✓）}:\ \text{上界 120 的文献归属（Östergård 构造 vs Wille）}\ ⚠️\ \text{—— 已在本线标为待核，不阻断结论 ✓}$$
$$
$$
```

## §3 边界（诚实标注）

- §1 ②为 **arXiv v2 HTML 逐字直读** ✓；③为整数取顶 ✓；④为与已知下界比较 ✓
- **未**主张该 SDP 方法无价值 ✗；只主张"在 $(2,10,1)$ 格未形成新界" ✓（范围严格）
- **未**跑求解器 ✓（纯文献直读 ✓）
- L-2 **关档 ≠ 该方向死亡** ✓：若 2026 后出现新文献，可**重开**（重开条件：新文献对 $(2,10,1)$ 给出 $\ge107$ 的界 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 独立输入缺口陈述 命中文件数=1    :: ./GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md 
技术词 十族汇总     命中文件数=1    :: ./GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md 
技术词 支撑型约束判定 命中文件数=1    :: ./GAPTHEOREM-2026-09-26-K101-119-independent-input-gap.md
```
- **本档新增**：L-2 关档结论（见上方命中数）
- **档案已有（引用，不列为提出）**：105.2223 格值、球覆盖/Van Wee/BÖW 阶梯、Wu–Chen 2024
