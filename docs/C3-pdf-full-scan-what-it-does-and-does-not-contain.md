已查地图：命中（`C3-problem16-17-verbatim-parameter-space`）⟹ 本档为其**通篇扫描补录**，不开新案
D0: 本档对象 = `Schulte–Weiss 2006` PDF **通篇扫描结果**（含什么／不含什么）＋ `Problems 16/17` 为**陈述级**，参数清单在 `[42, §11E,H]` **不在本 PDF 内**
D1: 0 （[REVIEW] 轮次：扫描与定界，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **PDF 通篇扫描：它含什么、不含什么**

## §1 已归档来源

```
`sources/Schulte-Weiss-2006-open-problems-polytopes.pdf`（`arXiv:math/0608397v1`，`25` 页）✓ —— 已用 `pymupdf` 通篇扫 `37` 个关键词 ✓
```

## §2 ⭐ 本 PDF **确实含**（参数级／结论级）

```
**【p9 定义】** "From the plane tessellations `\{3,6\}`、`\{6,3\}` and `\{4,4\}` we obtain the regular polyhedra `\{3,6\}_{(s,t)}`、`\{6,3\}_{(s,t)}` or `\{4,4\}_{(s,t)}`（with `t=0` or `s=t`）on the `2`-torus" ✓（**参数空间来源**）✓
**【p10 总况＋`Problem 16`】** 七型清单；"**complete except `\{4,4,4\}` and `\{3,6,3\}`**"；`Problem 16` 逐字（`s,u\ge3` **odd and distinct**；**finite only if `(3,5)`/`(5,3)`**，猜想）✓
**【p10 `\{3,6,3\}` 现状】** "**For `\{3,6,3\}`，only partial results are known and involve sparse sequences of parameters（see `[42, Sections 11E,H]`）**" ✓✓ ← **明写去查书里的 §11E,H**
**【p11 `Problem 17`】** 逐字（参数范围）✓
**【p12 旁证①】** "the corresponding universal regular polytope `\{\{4,4\}_{(s,t)},\{4,3\}\}`（obtained when `t=0` or `s=t`）**is known to be finite if and only if `(s,t)=(2,0),(2,2)` or `(3,0)`**" ✓✓ ← **与 `\{3,6\}` 侧自对偶有限集 `(1,1),(2,0),(3,0)` 同型（稀疏、三点）** ✓
**【p12 旁证②】** chiral 情形 `\{\{4,4\}_{(s,t)},\{4,3\}\}_{ch}`：**conjectured finite iff `(s,t)=(1,2),(1,3),(1,4),(2,3)`** ✓
```

## §3 ⛔ 本 PDF **不含**（关键缺口）

```
**【不含】** `\{3,6,3\}` 的 **"sparse sequences" 具体参数清单** —— 本 PDF **只给问题陈述＋指向 `[42, §11E,H]`** ✓✓
【⟹ 诚实结论】**您给我的这份 PDF 不足以填 `(s,t,u,v)` 表**；缺的是 **`[42]` §11E/§11H 正文**（或 `1992 CMH` 论文／`Monson–Schulte 2010`）✓
【⟹ 另注】 本 PDF 覆盖的是 `4`–`6` 页的参数定义、`10`–`13` 页的开放问题、`14`–`20` 页实现/`Petrie` 等 —— **无 `Table 11E1` 类清单** ✓
```

## §4 现有拼图（截止本轮）

```
$$\begin{array}{c|c|c}
\text{项目}&\text{状态}&\text{来源}\\
\hline
\text{参数空间}\ s\ge2,\ t=0\ \text{或}\ s=t;\ u\ge2,\ v=0\ \text{或}\ u=v&\checkmark&\text{PDF p11（Problem 17）}\\
\text{存在性}\ne\text{群}\ne\text{有限性}\ \text{三分}&\checkmark&\text{PDF p10}\\
\{3,6,3\}\ \text{仅 partial＋sparse sequences}&\checkmark&\text{PDF p10}\\
\text{sparse sequences 具体清单}&\textbf{OPEN}&[42]\ \S11E,H\\
\text{已知 }\{3,6\}\ \text{侧自对偶有限集}\ (1,1),(2,0),(3,0)&\checkmark\ (\text{档级})&\text{前档（二手转引）}\\
1992\ \text{两族（`(3r,0)`+`(r,r)`；`(s,s)`+`(s,0)`）&\checkmark\ (\text{档级})&\text{您提供}\\
\text{最小未决 }(s_*,t_*,u_*,v_*)&\textbf{OPEN}&—\\
H\ \text{固定维？}\ H>0\iff\text{finite？}&\textbf{OPEN}&—\\
\end{array}$$ ✓
```

## §5 下一步（不计算）

```
**【唯一缺口】** `[42] §11E/§11H` 的 sparse sequences 清单 ⟹ 得**已定参数集** ⟹ **取补集** ⟹ **`D_{2026}`** ⟹ 最小未决 ⟹ 两硬问 ✓
【可得性排序】 **(a)** `1992\ CMH\ 67,\ 77`–`118`（**免费**，`e-periodica` **浏览器可开**，我自动抓取被 `403`）；**(b)** `Monson–Schulte 2010`（`academia.edu` 免费 PDF）；**(c)** 书 `[42]`（`Cambridge` 挡）✓
【⛔ 纪律】 **不计算、不实现**；`C2` 暂停 ✓
【边界】 §2 全部为**本地 `pymupdf` 逐字提取**（原文已归档）；§3–§5 为**本档扫描结论**；`1992` 两族与自对偶有限集为**档级**（二手/您提供）；未制造候选／未启动搜索／未碰 RH。

## §6 【技术词回查】（补录）
```
技术词 sparse sequences 命中文件数=2    :: ./C3-pdf-full-scan-what-it-does-and-does-not-contain.md ./C3-problem16-17-verbatim-parameter-space.md 
```
