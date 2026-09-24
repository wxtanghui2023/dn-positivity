已查地图：命中（`C3-d1992-table-and-s4-audit-point`／`C3-RGPF-II-free-source-extracted`）⟹ 引用，不开新案
D0: 本档对象 = **新证据链**：`CiteSeerX` 免费源逐字（`11E` 派生事实＋self-dual）＋ `RGPF-II` 的 **`11G/11H` 显式关系** ＋ `tavily_extract` 可穿透性（渠道）
D1: 0 （[REVIEW] 轮次：取证，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **新证据：`11E` 派生事实 ＋ `11G/11H` 关系**

## §1 ⭐ `CiteSeerX` 免费源逐字（`Monson` ＆ `Ivi\'c Weiss`，`Cayley Graphs and Symmetric 4-Polytopes`）

```
**"This locally toroidal 4-polytope is known to be finite only when `s=(1,1),(2,0)` or `(3,0)` `[17, 11E]`. \textbf{In each of these cases, the polytope is self-dual}."** ✓✓✓
**"Example 21. The universal locally toroidal polytopes `\{\{3,6\}_s,\{6,3\}_s\}` `(10)` for `s=(1,1),(2,0),(3,0)`."** ✓✓
**【旁证：另一族的"universal 条件"措辞】** 对 `\langle\{4,4\}_{(p,0)},\{4,4\}_{(p,0)}\rangle`："This locally toroidal polytope **is universal for its class when `p=3`，but almost surely is not for larger primes** `[17, 10C]`." ✓✓ ← **与 `1992` 的 "likely infinite" 同一措辞层级** ⟹ **`s=4` 的"likely infinite"确属"未证明"** ✓✓
```

## §2 ⭐ `RGPF-II` 的 `11G/11H` **显式关系**（逐字）

```
**"[13, Sect. 11G,11H], which also describes the relationship between the polytopes. In particular, if `[6,3,3]=\langle r_0,\ldots,r_3\rangle`（say），then `[3,6,3]` can be identified with the subgroup `\langle r_0,\ r_1r_0r_1,\ r_2,\ r_3\rangle`"** ✓✓✓
⟹ **这是第一条落到我手里的 `\{6,3,3\}\leftrightarrow\{3,6,3\}` 显式子群关系**（`11G/11H` 机制的具体形态）✓✓
**同型旁证**："In `[4,4,3]` … under the modular reduction this index collapses to 1; see `[13, §10E]` … we can identify `[4,4,4]` with the subgroup `\langle r_1,\ r_0,\ r_2r_1r_2,\ r_3\rangle`" ✓（**同一套"子群识别"技术**）✓
```

## §3 ⚠️ 渠道情报（渠道级，重要）

```
**【`tavily_extract` 可穿透 `CiteSeerX`】** 直接返回**正文文本** ⟹ **免费学术 PDF 的一条可用抓取路线** ✓✓
**【`e-periodica`】** 您给的 `digbib` 链接经 `tavily_extract` 得到的是**该卷目录（含页码与 `PDF` 链接）** ⟹ **那 URL 是卷目录，不是论文本体** ✓；**但说明 `e-periodica` 对 `tavily_extract` 不完全封** ⟹ **或可据目录定位论文页并再抓** ✓
【⟹ 下一步可试】**用 `tavily_extract` 抓 `Cambridge` 第 `11` 章 PDF**（`§11E` 本体，`pp.387`–`444`）—— 若成，**`Table 11E1` 当场到手** ✓✓
```

## §4 状态更新

```
$$\begin{array}{c|c}
\text{项目}&\text{状态}\\
\hline
\{3,6\}\ \text{侧 self-dual 有限集}\ (1,1),(2,0),(3,0)\ \text{且自对偶}&\checkmark\ (\text{新增逐字})\\
1992\ \text{三族状态表}&\checkmark\\
11G/11H\ \text{首条显式关系（子群识别）}&\checkmark\\
\text{"likely infinite"}\equiv\text{未证明（措辞旁证）}&\checkmark\\
\text{Table 11E1 全表}&\textbf{OPEN}\\
D_{2026}\ \text{（含关系闭包）}&\textbf{OPEN}\\
\text{两硬问（}\dim H,\ H>0\iff\text{finite）}&\textbf{OPEN}\\
\end{array}$$ ✓
【⛔ 纪律】**不计算、不实现**；`C2` 暂停 ✓
【边界】 §1–§2 为 `tavily_extract` **逐字**（`CiteSeerX` 与 `arXiv` 原文）；§3 为**渠道实测**；未制造候选／未启动搜索／未碰 RH。

## §5 【技术词回查】（补录）
```
技术词 self-dual        命中文件数=19   :: ./S9-strict-and-D2-prescreen.md ./gate17-arithmetic-geodesic-flow-transfer.md ./RIGOR-AUDIT-1-three-candidates-rigor-audit-and-V248-selected.md 
```
