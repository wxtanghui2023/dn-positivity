# C-3898 — T2-b: common-root elimination audit and the three questions (verdict M1-GAP)

已查地图（**先查后写**）：`C3897`（**奇偶分解 `P = uR_1(u^2)+R_2(u^2)`** ✓✓）、`C3896`（**精确 T3 证书** ✓✓）、`C3895`（**ROOT-PAIRING 登记** ✓✓）、`C-3861`／`C-3862`（**五节点极值点 ＋ 活跃集** ✓✓）、`C-3849`（**`E_0 \cap E_{\mathrm{even}} = \varnothing`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-106：C-3898 —— T2-b（共同根消去 ＋ 三问）；判定 `M1-GAP`**（唐先生 2026-09-22 10:11 令）
D1: 0
FREEZE-ACK: 本档即冻结审计（禁 resultant 包装、禁 degree-36 冒充支持界 ✓）

---

## §0 结论（七条 ✓✓）

$$\textbf{① 表 1｜共同根差商}✓：\text{两支撑点}\ u, v✓：P(u) - P(v) = uR_1(u^2) - vR_1(v^2) + R_2(u^2) - R_2(v^2)✓✓$$

$$\qquad \text{置}\ z = u^2✓,\ w = v^2✓ \Longrightarrow \text{差商}\ \frac{P(u)-P(v)}{u-v}\ \text{为}\ (u,v)\ \text{的多项式}✓（\text{次数} \le 35✓）✓$$

$$\qquad ⚠️ \textbf{审计结论}✗：\text{由奇偶分解}\ \textbf{未能} \text{得到}\ (u-v)(u+v)R(u,v)\ \text{型低复杂度因子}✗✓；\ \text{故}\ \textbf{T2-b-1 不成功}✗✓$$

$$\qquad \text{（}\textbf{不}把"消元完成"包装成结构突破}✗✓）$$

$$\textbf{② 表 2｜}R_1／R_2\ \textbf{次数与因子}✓✓**：$$

$$\qquad \text{结构性事实}✓：T_{2q}(u)\ \text{在}\ u\ \text{的首项系数为}\ 2^{2q-1}✓ \Longrightarrow \text{活跃等式}\ \sum_jT_{2q}(u_j) = -\tfrac12\ \text{即}\ z_j := u_j^2\ \text{上的}\ \textbf{4 个方程}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{4 未知}\ z_j\ \text{、4 方程} \Longrightarrow \text{解集一般}\ \textbf{有限}}✓✓\ \text{（但}\ \textbf{不} \text{给出}\ z_j\ \text{全等}✗）$$

$$\qquad \text{而}\ \boxed{M1\text{-PASS} \iff \mathrm{Var}(z) = 0 \iff p_2 = 4a^4}✓✓\ \text{—— 而}\ p_2\ \textbf{不在} \text{被固定的量中}✗✓$$

$$\qquad \text{（已固定}✓：p_0 = 4✓,\ p_1 = \sum z_j = \sum u_j^2 = 4a^2✓,\ \text{及活跃等式所约束的高次组合}✓）$$

$$\textbf{③ ⚠️ 表 3｜范围问题（本档真正发现，须唐先生裁定}✓✓**）：$$

$$\qquad \text{本刀与}\ C\text{-}3894／C\text{-}3897\ \text{用的是}\ \textbf{四节点} \text{模型}✓（Y_j = u_j - m✓,\ j = 1..4✓），\text{来自}\ x_5 = 0\ \text{的}\ \textbf{边界归约}✓$$

$$\qquad \text{但档案已证}\ \boxed{E_0 \cap E_{\mathrm{even}} = \varnothing}✓✓ \Longrightarrow x_5 = 0\ \textbf{不可行}✗✓ \Longrightarrow \textbf{真实可行集是五节点问题}✓（全部}\ x_j > 0✓）$$

$$\qquad \text{且}\ C\text{-}3861／C\text{-}3862\ \text{的极值点是}\ \textbf{五节点} \text{构型}✗✓ \Longrightarrow \textbf{ROOT-PAIRING 目标活在哪个问题里？}✓✓$$

$$\qquad \qquad \text{（}\textbf{须先定}✓：\text{四节点（不可行}✗）\ \text{or 五节点（真实}✓）——\text{否则 M1 陈述失真}✗✓）$$

$$\textbf{④ 表 4｜M1 判定}✓：\ \boxed{M1\text{-GAP}}✗✓$$

| 结果 ✓ | 状态 ✓ |
|---|---|
| `\#\{|u_j|\} = 1` ✓ | **未得** ✗ |
| `\#\{|u_j|\} \le 2` 或 `\le 3` ✓ | **未得** ✗ |
| 仅有限解包络 ✓ | **（4 方程 4 未知 ⟹ 有限）** ⚠️ |
| **判定** ✓ | **`M1-GAP`** ✗✓ |

$$\textbf{⑤ 三问现状（诚实}✓✓**）：\text{(i) }R_1\ \text{未见真正降次／分解}✗；\ \text{(ii) 未得唯一}\ z_\star✗；\ \text{(iii) 未能排除双绝对值}✗✓$$

$$\qquad \Longrightarrow \text{只有"有限解"这一层}✓,\ \textbf{不足} \text{以给}\ \#\{|u_j|\} \le 2／3✗✓$$

$$\textbf{⑥ 明确不做的冒充}✓✓：\textbf{不}用 degree-36 根包络冒充支持界}✗✓；\ \textbf{不}宣称 two-level✗；\ \textbf{不}宣称 M1✗✓$$

$$\textbf{⑦ 下一步（精确形式}✓✓**）：\text{(a) 解 4×4 系统求}\ k = \#\{\text{distinct } z_j\}✓（\text{有界计算}✓,\ \text{非"大 resultant"}✓）；\ \text{(b) 按③裁定后重述目标}✓✓$$

## §1 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| T2-b-1 共同根因子 ✓ | **不成功（未得低复杂度因子）** ✗✓ |
| T2-b-2 (i)(ii)(iii) ✓ | **均未达** ✗ |
| 结构性事实（首项系数 ⟹ 4 方程） ✓ | **已立** ✓✓ |
| 范围问题 ✓ | **已发现，待裁定** ✓✓ |
| **M1** ✓ | **`GAP`** ✗✓ |

## §2 边界（不得声称 ✗✓）

- **不**声称根集成对／支持压缩 ✓✓
- **不**声称 M1（含弱形式） ✓
- **不**把有限解集说成 `\le 3` 支持界 ✓✓
- **不**在四节点（不可行）问题上继续堆结论而不先裁定范围 ✓

## §3 本档**不**做的事 ✓✓

$$\textbf{不}做 T3（含 T3-REGION）✗;\ \textbf{不}做 T4✗;\ \textbf{不}重开 T1✗✓$$

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 幂和固定     命中文件数=0    :: 
技术词 四节点对五节点 命中文件数=0    :: 
技术词 支持压缩判定 命中文件数=0    ::
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{① 范围裁定}✓✓：\text{ROOT-PAIRING 目标改挂}\ \textbf{五节点} \text{问题}✓（\text{建议}✓,\ \text{因四节点不可行}✓✓）$$
$$\textbf{② 有界计算}✓：\text{解 4（或 5）×4 系统求}\ k = \#\{\text{distinct }u_j^2\}✓✓ \Longrightarrow \text{得}\ M1\text{-PASS／WEAK／GAP}✓$$
$$\textbf{③ 若 ② 仍为 GAP}✓：\text{转"支撑压缩的替代机制"}✓（\text{而非继续在同型消元上投入}✓✓）$$
