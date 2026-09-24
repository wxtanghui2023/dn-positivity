已查地图：命中（`S2-BATCH-1-record` ＋ `AMEND-17`）⟹ 本档为 `Batch-2` 记录（判定已回填），不开新案
D0: 本档对象 = **`S2 / Batch-2`（`F4+F5+F6`，18 条）**：逐条七列判定 ＋ 批统计 `(C,P1,P2,P3,P4,U,SPEC)` ＋ 四种边界样本登记
D1: 1（第二批完成 S2；产出四种 S2 边界样本）
[RESEARCH]

# **`S2 / Batch-2` 记录（`F4＋F5＋F6`，18 条）**

## §0 执行口径（沿用 `AMEND-16`／`AMEND-17`）

```
(1) 七列: ID | S2 | P类 | 直接证据 | 已覆盖对象/统计 | 未覆盖部分 | 决策
(2) P4 只认「现成输出已覆盖目标统计量的一部分」; 仅有底层全集数据库 或「我们自己计算」⟹ 不算 P4
(3) 多标签最终唯一归类（证据最直接者）; 无法判断 ⟹ PENDING
(4) SPEC-REQUIRED 正交，不进入 C/P/U
(5) COVERED 须有直接定理/现成结果实质覆盖目标命题
(6) U 仅表示「本轮检索未取得直接覆盖证据」
(7) S3 冻结
```

## §1 逐条判定（18 条）

```
$$\begin{array}{c|c|c|l|l|l|c}
\text{ID}&\texttt{S2}&P&\text{直接证据}&\text{已覆盖对象／统计}&\textbf{未覆盖部分}&Decision\\
\hline
L02&U&—&{\text{未找到"给定指数的极小行列式子格"分类/计数的直接表或定理}}&{\text{一般子格/行列式与指数理论}}&{\text{"给定指数""极小行列式""分类与计数"的参数族及完整输出}}&{U+\texttt{SPEC}}\\
L04&\boxed{C}&—&{BW_{16}\ \text{Voronoi 区域研究给出覆盖半径}\sqrt{3/2};\ \text{Leech 已有直接定理}\sqrt2}&{\text{两个指定经典格的覆盖半径精确值}}&{\text{无}}&\boxed{COVERED}\\
L05&U&—&{\text{子格/短向量一般理论；无"按小指数分类并输出最短向量数"的直接表}}&{\text{一般短向量与格分类资料}}&{\text{指定指数层面的 exact count ＋ achievers}}&U\\
L06&U&—&{\text{小维 unimodular lattice 已有分类/目录（维 12 对象数、最小范数）}}&{\le12\ \text{维对象/部分最小范数与分类数据}}&{\text{"不变量极值"未指定是哪一个 invariant，亦无该统计的现成输出}}&{U+\texttt{SPEC}}\\
L07&P&P2&{\text{theta series 的 modular-form 结构与 extremal-theta-series 理论；极小范数约束决定部分低阶系数}}&{\text{给定维数/极小范数时 theta series 的结构约束与 extremal series}}&{\text{任意"给定 minimum"下所要求的系数极值}}&P2\\
L08&P&P3&{8、10\ \text{维欧氏格不可约有限自同构群完整分类（}52、47\ \text{类）}}&{\text{特定维数、特定自同构群结构的分类}}&{\le10\ \text{全部 unimodular lattice 的 }\mathrm{Aut}\ \text{阶极值及达到者}}&P3\\
C04&U&—&{\text{BCH 覆盖半径大量一般/参数族结果（primitive BCH 精确 covering-radius 定理）}}&{\text{若干 BCH 参数族的 exact covering radius}}&{\text{"特定 BCH 码"未给 }n,k,d,q\ \text{或具体族}}&{U+\texttt{SPEC}}\\
C05&U&—&{\text{list-decoding radius 已有 Reed–Muller／Reed–Solomon 等族精确/近精确理论}}&{\text{特定 code families 的 list-decoding radius}}&{\text{"小码"未指定 family／field／参数／list size}}&{U+\texttt{SPEC}}\\
C06&P&P4&{\text{小参数 optimal-code 实际分类输出（}\mathbb F_5,\mathbb F_7\ \text{部分分类}）＋ inequivalent-code 计数/唯一性结果}&{\text{部分 }(q,n,k,d)\ \text{的 optimal code 非等价分类}}&{\text{全部"固定 }n"\ \text{最优码非同构数}}&P4\\
C07&P&P4&{q\text{-ary covering-code 表直接列出大量 }K_q(n,R)\ \text{参数 lower/upper bounds，且有明确表格缺口}}&{\text{部分 }q\text{-ary 小参数 covering-radius／covering-code 数据}}&{\text{未收割格中的 exact cells}}&P4\\
C08&P&P2&{\text{MacWilliams identities／Pless moments 提供直接线性约束，未知项足够少时可唯一确定 weight distribution}}&{\text{一类参数条件下的 uniqueness mechanism}}&{\text{并非任意给定 parameters 都已有唯一性结论}}&P2\\
C09&P&P4&{\text{Grassl／Brouwer code tables 对大量 }[n,k,d]_q\ \text{给出 bounds/constructions ＋ 小参数分类}}&{\text{大量小 }n\ \text{的 minimum-distance 数据及部分达到者分类}}&{\text{完整"谱＋所有达到者分类"}}&P4\\
Po01&U&—&{\text{未找到直接覆盖 }x^n\pm x^m\pm1,\ n\le40\ \text{的"整数根型完整分类"}}&{\text{一般整数根判别、低次数 trinomial 结果}}&{\text{指定高次数三项式族的完整分类表}}&U\\
Po03&\boxed{C}&—&{\text{给定 trace（甚至同时给定 constant term）的不可约多项式数量有明确公式}}&{\text{小 }q,n\ \text{的 prescribed-trace irreducible polynomial count}}&{\text{无（候选为该一般命题的有限参数截取）}}&\boxed{COVERED}\\
Po04&P&P2&{\text{Cohen–Movahhedi–Salinier 对 }x^n+ax^s+b\ \text{的 Galois groups 一般定理（互素条件直得 }A_n/S_n）}&{\text{三项式 Galois group 一般结构与大量参数条件}}&{\text{"次数}\le30\ \text{完整分布"未被直接列出}}&P2\\
Po05&U&—&{\text{polynomial ideal／cyclic-code 文献把理想与 Hamming weight 联系，但 ideal 所属环、系数域、weight 定义未固定}}&{\text{cyclic/ideal code 中 minimum weight 的一般理论}}&{\text{指定 ideal family ＋ coefficient domain ＋ exact minimum-weight statistic}}&{U+\texttt{SPEC}}\\
Po07&\boxed{C}&—&{\text{不可约二项式成熟充要判据（}x^n-g\ \text{在}\ \mathbb F_q\ \text{上不可约条件已明确）}}&{\text{给定 }q,n\ \text{的 existence 判定}}&{\text{无（"小 }n\ \text{完整表"为该判据的有限截取）}}&\boxed{COVERED}\\
Po08&U&—&{\text{未找到"给定判别式的整系数多项式计数（小范围）"直接现成表/定理}}&{\text{有关判别式的多项式/Galois 理论}}&{\text{degree／height／系数范围／判别式范围均未指定；计数目标不闭合}}&{U+\texttt{SPEC}}\\
\end{array}$$ ✓✓
```

## §2 批统计（逐批独立；`SPEC` 单列）

```
$$\boxed{C=3,\quad P_1=0,\quad P_2=3,\quad P_3=1,\quad P_4=3,\quad U=8,\quad \texttt{SPEC}=6}$$ ✓✓
$$\text{核对}:\ 3+0+3+1+3+8=\boxed{18}\ \checkmark;\quad \texttt{SPEC}\ \text{正交，\textbf{不从 }C/P/U\ \text{中扣除}}$$ ✓✓
$$C=\{L04,Po03,Po07\};\quad P_2=\{L07,C08,Po04\};\quad P_3=\{L08\};\quad P_4=\{C06,C07,C09\};$$
$$U=\{L02,L05,L06,C04,C05,Po01,Po05,Po08\};\quad \texttt{SPEC}=\{L02,L06,C04,C05,Po05,Po08\}$$ ✓
```

## §3 四种 S2 边界样本（登记入回归集）

```
$$\textbf{① }\boxed{L04}:\ \text{两个经典对象已有\textbf{直接 exact theorem}}\ \Longrightarrow\ \mathbf{C}\ (\text{BW}_{16}:\ \sqrt{3/2};\ \text{Leech}:\ \sqrt2)$$ ✓
$$\textbf{② }\boxed{C07}:\ \text{目标统计量已有\textbf{部分表格输出}}\ \Longrightarrow\ \mathbf{P4}\ (\text{与 }G01\ \text{形成对照}:\ \text{有数据库}\ne\text{数据库输出含目标统计})$$ ✓✓
$$\textbf{③ }\boxed{Po03}:\ \text{一般公式\textbf{直接覆盖有限参数命题}}\ \Longrightarrow\ \mathbf{C}$$ ✓✓
$$\textbf{④ }\boxed{Po07}:\ \text{一般\textbf{充要判据}直接覆盖有限表}\ \Longrightarrow\ \mathbf{C}$$ ✓✓
$$\Longrightarrow\ \text{四条共同防止 }S2\ \text{把「理论可算」「对象已有数据库」「部分统计量已有输出」「一般定理直接覆盖」混为一类}$$ ✓✓
$$\text{回归集现为八条}:\ Po02,\ Gr03,\ G01,\ P02,\ L04,\ C07,\ Po03,\ Po07$$ ✓
```

## §4 三批分开锁定

```
$$\begin{array}{c|rrrrrrr|r}
\text{批次}&C&P_1&P_2&P_3&P_4&U&\texttt{SPEC}&\text{总数}\\
\hline
S2\text{-}30&4&—&—&—&—&9&—&30\\
Batch\text{-}1&0&0&2&3&3&11&1&19\\
Batch\text{-}2&3&0&3&1&3&8&6&18\\
\end{array}$$ ✓（\textbf{分开统计，不合并}）$$
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §1 文献为**档级**（先生本轮检索）；`L04/Po03/Po07` 三例已判 `COVERED` ✓

## §附 【技术词回查】（补录）
```
技术词 boundary         命中文件数=168  :: ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md ./grh-goldbach-paper-draft-v2.md ./p47-g2-gluing-defect.md 
技术词 batch            命中文件数=4    :: ./C380-S1-FREEZE.md ./C380-K4-GATE-FREEZE.md ./C380-221-COMPUTATION-SPEC-FREEZE.md 
```
