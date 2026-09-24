已查地图：命中（`S2-BATCH-4-record-and-pool-reconciliation`）⟹ 本档为 `Census-1`（族×状态）＋ `Census-2`（形态×状态），不开新案
D0: 本档对象 = **`Census-1`**：族×状态矩阵 ＋ `P4`/`U` 密度 ＋ ⚠️**`SPEC` 逐条重核（20 vs 26）**；**`Census-2`**：100 条按「目标数量形态」重标并交叉 `C/P*/P2/P3/P4/U`
D1: 1（首次池结构量化；产出族-状态矩阵、形态-状态矩阵与两处密度分区）
[RESEARCH]

# **`Census-1` ＋ `Census-2`**

## §0 口径（照先生）

```
$$\text{主状态}:\ C\ |\ P^*\ (S2\text{-}30\ \text{的 }17\ \text{条，未细分})\ |\ P_2\ |\ P_3\ |\ P_4\ |\ U;\qquad \texttt{SPEC}\ \textbf{正交}$$ ✓
$$\text{主状态核验}:\ 7+17+14+4+17+41=\boxed{100}\ \checkmark\ (\textbf{完全闭合};\ \text{与先生一致})$$ ✓✓
```

## §1 ⚠️ `SPEC` 逐条重核（**以逐条集合为准 → 20**）

```
$$\textbf{逐批集合（来自各批记录，权威）}:$$
$$\qquad S2\text{-}30:\ \{Po06\}\ (1);\quad B1:\ \{P02\}\ (1);\quad B2:\ \{L02,L06,C04,C05,Po05,Po08\}\ (6);$$
$$\qquad B3:\ \{R06,R08\}\ (2);\quad B4:\ \{M01,M02,M06,Mt04,Mt05,Au03,Au04,Au05,Au07,Au08\}\ (10);$$
$$\qquad \Longrightarrow\ 1+1+6+2+10=\boxed{20}$$ ✓✓✓
$$\textbf{按族展开}: F3\ 1,\ F4\ 2,\ F5\ 2,\ F6\ 3,\ F8\ 2,\ F10\ 3,\ F11\ 2,\ F12\ 5\ \Longrightarrow\ 20$$ ✓
$$\textbf{先生族表 SPEC 列} = 26;\ \text{差异 6 处}:\ F1\ (+1),\ F4\ (+1),\ F5\ (-2),\ F6\ (+1),\ F10\ (+4),\ F12\ (+1)$$ ⚠️
$$\Longrightarrow\ \boxed{\texttt{SPEC}=20\ \text{锁定（逐条为准）}};\ \text{族表 }SPEC\ \text{列须重核（}F5\ \text{应为 }2\ \text{而非 }0;\ F1\ \text{应为 }0,\ \text{表记 }1)$$ ✓✓
$$\textbf{附注}:\ Au06\ \text{曾挂 spec-gap，补齐规格后转"待核"，}\textbf{不}计入 20$$ ✓
```

## §2 `Census-1`：族 × 状态矩阵（主状态；`SPEC` 见 §1）

```
$$\begin{array}{c|c|r|r|r|r|r|r}
\text{族}&\text{对象族}&C&P^*&P_2&P_3&P_4&U&\text{合计}\\
\hline
F1&\text{有限群}&0&1&0&1&1&5&8\\
F2&\text{图}&1&3&1&0&0&5&10\\
F3&\text{排列}&0&0&1&2&2&3&8\\
F4&\text{格／球堆}&1&2&1&1&0&3&8\\
F5&\text{编码}&0&3&1&0&3&2&9\\
F6&\text{多项式／根}&3&0&1&0&0&4&8\\
F7&\text{有限域}&0&3&4&0&0&2&9\\
F8&\text{递推／序列}&1&1&2&0&2&2&8\\
F9&\text{设计／配置}&0&3&0&0&4&2&9\\
F10&\text{矩阵／谱}&0&0&2&0&1&7&10\\
F11&\text{拟阵／偏序}&1&0&1&0&3&3&8\\
F12&\text{自动机／动力}&0&1&0&0&1&6&8\\
\hline
\text{合计}&&7&17&14&4&17&41&100\\
\end{array}$$ ✓✓（\text{与先生表一致}）$$
```

## §3 密度分区（算好待用）

```
$$\textbf{P4 密度}: F9\ 4/9=44.4\%;\ F11\ 3/8=37.5\%;\ F5\ 3/9=33.3\%;\ F3\ 2/8,\ F8\ 2/8=25\%;\ \text{余低}$$ ✓
$$\textbf{U 密度}: F12\ 6/8=75\%;\ F10\ 7/10=70\%;\ F1\ 5/8=62.5\%;\ F2\ 5/10=50\%;\ F6\ 4/8=50\%;\ \text{余低}$$ ✓
$$\textbf{P4+U}: F12\ 7/8=87.5\%;\ F10\ 8/10=80\%;\ F11\ 6/8,\ F1\ 6/8=75\%;\ F9\ 6/9=66.7\%;\ F3\ 5/8=62.5\%$$ ✓
$$\Longrightarrow\ \text{三区}:\ \textbf{Zone-A}\ (P4\ \text{密})\ F9,F11,F5;\quad \textbf{Zone-B}\ (U\ \text{密})\ F10,F12,F1;\quad \textbf{Zone-C}\ (\text{交叉})\ F2,F6,F8$$ ✓✓
```

## §4 `Census-2`：目标数量形态 × 状态

```
$$\textbf{形态码}:\ \texttt{EV}\ \text{精确值};\ \texttt{ED}\ \text{精确分布};\ \texttt{EX}\ \text{极值};\ \texttt{AC}\ \text{达到者/分类};\ \texttt{EN}\ \text{存在性};\ \texttt{SP}\ \text{谱};\ \texttt{CE}\ \text{反例};\ \texttt{FT}\ \text{有限表补格};\ \texttt{UQ}\ \text{唯一性};\ \texttt{AS}\ \text{渐近/常数}$$ ✓
$$\begin{array}{c|rrrrrr|r}
\text{形态}&C&P^*&P_2&P_3&P_4&U&\text{合计}\\
\hline
\texttt{EV}&1&7&1&1&4&13&\mathbf{27}\\
\texttt{ED}&3&2&1&0&6&8&\mathbf{20}\\
\texttt{EX}&0&2&7&1&2&8&\mathbf{20}\\
\texttt{AC}&0&2&1&1&0&5&9\\
\texttt{EN}&1&2&0&0&1&2&6\\
\texttt{FT}&2&0&0&1&2&2&7\\
\texttt{SP}&0&0&2&0&1&1&4\\
\texttt{CE}&0&0&1&0&0&2&3\\
\texttt{AS}&0&2&0&0&0&0&2\\
\texttt{UQ}&0&0&1&0&1&0&2\\
\hline
\text{合计}&7&17&14&4&17&41&100\\
\end{array}$$ ✓✓（\text{交叉核验 }=100\ \checkmark）$$
```

## §5 池结构读法（**不提名 ACTIVE**）

```
$$\textbf{① 形态高度集中}:\ \texttt{EV}+\texttt{ED}+\texttt{EX}=27+20+20=\mathbf{67/100}\ (67\%)\ \Longrightarrow\ \text{池子 }2/3\ \text{是"格点补格型"问题}$$ ✓✓
$$\textbf{② }\texttt{EV}\times U=13\ \text{为最大单元格};\ \texttt{EX}\times U=8,\ \texttt{ED}\times U=8;\ \text{三者合计 }29/41\ \Longrightarrow\ U\ \text{几乎全是"格点/极值"型}$$ ✓✓
$$\textbf{③ }C\ \text{的形态画像}:\ \texttt{ED}\ 3,\ \texttt{FT}\ 2,\ \texttt{EV}\ 1,\ \texttt{EN}\ 1\ \Longrightarrow\ \textbf{与"一般公式的有限截取"完全吻合}（Po02/Po07/R03/Mt01）$$ ✓✓✓
$$\textbf{④ }P_4\ \text{形态画像}:\ \texttt{ED}\ 6+\texttt{EV}\ 4=10/17\ \Longrightarrow\ P4\ \text{集中于"精确分布/精确值"的表格补格};\ \text{与 }AMEND\text{-}17\ \text{的 }P4\ \text{定义自洽}$$ ✓✓
$$\textbf{⑤ }P_2\ \text{形态画像}:\ \texttt{EX}\ 7/14=50\%\ \Longrightarrow\ \textbf{"极值}＋\text{一般理论"}＝P_2\ \text{的签名}$$ ✓✓
$$\textbf{⑥ }\texttt{AC}\ \text{型风险}:\ 9\ \text{条中 }5\ \text{为 }U,\ \text{且其中 }4\ \text{条带 }\texttt{SPEC}\ (Po06,L02,R08,Mt05)\ \Longrightarrow\ \textbf{分类型目标最易规格不闭合}$$ ✓✓✓
$$\textbf{⑦ }\texttt{FT}\ \text{仅 }7\ \text{条且多落 }C/P_4\ \Longrightarrow\ \text{有限表补格型已被收割较重（与 }Po02\ \text{样本一致）}$$ ✓
$$\Longrightarrow\ \text{池子结构结论}:\ \text{密度分区不能直接用于选题};\ \textbf{必须先在 }Zone\text{-}A\ \text{问"缺口是否独立精确"},\ \text{在 }Zone\text{-}B\ \text{问"U 是缺覆盖还是命题未闭合"}$$ ✓✓
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；**不提名 ACTIVE** ✓
【边界】 §2 主状态与先生表一致；§1 `SPEC=20` 为**逐条为准**的锁定值；§4 形态标注为本档判定 ✓

## §附 【技术词回查】（补录）
```
技术词 form             命中文件数=576  :: ./LIE2D-R1R2R3-is-trilinear-exit-necessary-or-chosen.md ./B-SERIES-INDEX.md ./p3-uniform-decay-results.md 
技术词 census           命中文件数=18   :: ./C264-beta-sensitive-channel-census-three-gates-zero-candidates-and-the-location-vs-counting-criterion.md ./C3844-level3-entrance-audit.md ./C225-DAp-convergence-audit-six-branch-structure-resolved.md 
```
