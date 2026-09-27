已查地图：已跑 scripts/prework_map_check.sh refined weight 线性不等式 LP Haas van Wee supercode ⟹ **命中既有三档**（故 M-2A 平形式**非新** ✗）；本档为 **M-2 的 PRE-WORK 判定**（唐先生 2026-09-27 09:38 ✓）。
D0: 本档对象 = M-2A／M-2B 的档案先例
D1: 0（产出为已关档判定 ＋ 活口重定向）

# M2-PREWORK-2026-09-27 · M-2A 已在档案中关档

## §0 结论（先给）

```
$$\boxed{\textbf{(DD-1)}\ \text{M-2A（单点 refined-weight 线性不等式 LP）\textbf{档案已做并关档}}\ ✗\ \text{——LP 恰 = }1024/11=93.09\ \le119\ ✓}$$
$$\boxed{\textbf{(DD-2)}\ \text{按唐先生自设判据（"若 }\le119\ \text{则整个 refined-weight 单点坐标族判死"）⟹ \textbf{该族已死}}\ ✗}$$
$$\boxed{\textbf{(DD-3)}\ \text{档案已指明\textbf{升级活口}}：\text{① LP ＋ \textbf{surfeit 受限泛函}}；\text{② \textbf{跨中心／跨子空间耦合变量}（Haas 2002 \text{型}）}$$
$$
$$
```

## §1 档案原文（逐条引用 ✓）

```
$$\texttt{EXCESS-2026-09-25}\ \S7:\ \text{"Haas 2013 层式恒等式：校准通过 ＋ LP 结果（Layer 2 首测）"}\ ✓;\ \text{表: Layer 2 层式不等式族（Haas 2013 局部形式）} \Longrightarrow \textbf{LP}=93.09\ \textbf{不足}\ ✗$$
$$\texttt{PLAN-2026-09-25}\ \text{第 36 行}:\ \text{"Layer 2: 层式不等式族（Haas 2013 局部形式）} \Longrightarrow \textbf{LP 恰}=1024/11\ ✓\ \textbf{CLOSED}\ ✗\text{"}$$
$$\texttt{ALIGN-2026-09-25}\ \text{第 73 行}:\ \text{"LP 求 }\mathrm{OPT}(L_{\rm Haas})\ \text{——已知 }1024/11\text{（解析）}；\text{改为求 }\textbf{LP＋surfeit 受限泛函}\ \text{的新 OPT}\ ✓\text{"}$$
$$\text{下界阶梯（}\texttt{PLAN}\ \text{实测 ✓）}:\ \lceil1024/11\rceil=94 < 103\ (\text{van Wee 1988}) < 107\ (\text{Bertolo--Östergård--Weakley 2004}) \ll 120\ (\text{上界})$$
$$\text{缺失成分（}\texttt{PLAN}\ \text{第 41 行}）:\ \textbf{跨中心／跨子空间耦合变量}（Haas 2002: \text{固定 }k\text{-维子空间后码字数的多变量线性耦合}）✓$$
$$
$$
```

## §2 活口重定向（本档建议 ✓）

```
$$\textbf{M-2A（平形式）}:\ \text{跳过}\ ✗\ \text{（已死 ✓）};\ \textbf{M-2A′}（\text{LP＋surfeit 受限泛函}）:\ \text{与 }\texttt{ALIGN}\ \text{方向相同} ⟹ \text{需先查其后续状态} ⚠️$$
$$\textbf{M-2B（supercode）}:\ \text{本档检索未见档案先例} ⟹ \textbf{可能为真新口} ✓；\ \text{但唐先生自设门槛成立}:"\text{若 }C\ \text{无理由嵌入合适 linear }C_0\ \text{则无入口}"\ ⟹ \text{须先证嵌入性} ⚠️$$
$$\textbf{119 问题形态（已锁定 ✓）}:\ K(10,1)\ge120?\ \text{——不再允许引入 Booleanity 作为独立问题} ✓$$
$$
$$
```

## §3 边界（诚实标注）

- §1 为**档案原文引用** ✓（不列为新提出 ✓）；§0 判定依唐先生自设判据 ✓
- **未**排除 119 ✗；**未**主张 M-2A′／M-2B 必负 ✗（待各自 PRE-WORK ✓）
- 后台：更尖锐测试（`p2b.py`：(supp,δ|supp) 是否决定 Booleanity ✓）在跑 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：M-2A 已关档判定、活口重定向
- **档案已有（引用，不列为提出）**：Layer 2 LP = 1024/11、Haas 2013 层式族、van Wee、跨子空间耦合
