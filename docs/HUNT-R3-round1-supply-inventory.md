已查地图：命中（`C07-FOUR-GATE-BACKTEST-verified-lane-drift` ＋ `RESEARCH-CONSTITUTION` AMEND-23）⟹ `HUNT-R3` 第一轮，不开新案
D0: 本档对象 = **供给端清单（限具名独立来源）** ＋ **来源四层分级（L1–L4）** ＋ **抽取的具体问题（10 项）** ＋ **双轨分派** ＋ **入场闸序** ＋ 重复投资风险旗标
D1: 0（清单型，零计算）
[REVIEW]

# **`HUNT-R3` 第一轮：供给端清单**

## §0 入口规则（照 `AMEND-23`）

```
$$\textbf{入口}:\ \boxed{\text{具名独立来源}\to\text{具体问题}\to\text{分轨}\ (\text{LANE-A}/\text{LANE-B})}\to\text{闸序}\to\text{入场}$$
$$\textbf{闸序（入场前，缺一不可）}:\ \boxed{\text{\textsc{amend-20}（族字面检索＋等价参数化）}\to\text{\textsc{amend-21}（三合一未覆盖）}\to\text{\textsc{amend-22}（身份锁定：入场后不得偷换对象）}\to\text{赛道闸门}}$$
$$\qquad \text{LANE-A 四闸}:\ \text{① 明确记录缺口（含权威记录源可得并已读）}\wedge\text{② 可机器验证}\wedge\text{③ 独立复核}\wedge\text{④ 非纯算力堆砌}$$
$$\qquad \text{LANE-B 四闸}:\ G1\to G2\to G3\to G4$$
$$\boxed{\textbf{本轮只做“来源→问题→分轨”};\ \textbf{不做覆盖判定}（\text{属第二轮 \textsc{amend-20}/21}）;\ \textbf{零计算}}$$ ✓✓
```

## §1 具名来源四层分级

```
$$\textbf{L1 开放问题库（在线、可检索）}:\ \texttt{erdosproblems.com};\ \boxed{\text{Open Problem Garden}}\ (\text{Algebra 298／Graph Theory 227／Number Theory 49／Topology 40／Combinatorics 35／Geometry 29／Logic 10／Group Theory 5});$$
$$\qquad \textbf{问题清单总目录}:\ \texttt{amathr.org/problems}\ (\text{Hilbert／Scottish Book／Smale／Clay／Arnold／Tabachnikov }\textit{Baker's Dozen}\text{／Nash–Rassias／AIM 工作坊问题表／ICM 2026 猜想／\textbf{Ben Green 的 100 个开放问题}／Joyner–Kim《Selected Unsolved Problems in Coding Theory 2011》／Bandeira 42 个数据科学开放问题})$$
$$\textbf{L2 权威表／动态综述的未收割格（LANE-A 主供给）}:\ \text{Radziszowski }\texttt{DS1.18};\ \text{Brouwer 表（}A(n,d)\text{上下界）};\ \text{Grassl 码表};\ \texttt{codetables.de};\ \text{La Jolla 差集库};$$
$$\qquad \boxed{\text{OEIS}}\ (\text{关键词 }\texttt{more}\text{／含缺口 }\texttt{a-file}\text{／“下一项未知”})——\ \text{共 }\sim39.85\ \text{万序列}$$
$$\textbf{L3 近期研讨会/综述“问题栏”}:\ \boxed{\text{2026 Barbados 图论研讨会开放问题表}}\ (\text{Julien Codsi 收集，2026});\ \text{组合 Gray 码更新综述 }\texttt{EJC DS26}\ (\text{含新提问题});\ \text{Cooper }\textit{Combinatorial Problems I Like};\ \text{设计理论开放问题（MathOverflow 汇总）}$$
$$\textbf{L4 专项开放问题综述}:\ \boxed{\text{《Open Problems in Coding Theory》}}\ (\text{含：}24\ \text{倍数长度的极值 doubly-even 自双工码（Fermat 型）；自双工码与格；}d\le23\ \text{幺模格；}d\le72\ \text{偶幺模格；Construction A 由 }\le40\ \text{长 Type II 码所得格})$$
```

## §2 抽取的具体问题与分派（10 项，**抽取级**）

```
$$\begin{array}{c|l|l|l}
\#&\text{具体问题（来源）}&\text{形态}&\text{分轨}\\\hline
S1&\text{诱导饱和（induced saturation）对偶环 }C_{2t}:\ \text{存在 }C_{2t}\text{-free 的 }G\ \text{使增删任一边都产生诱导 }C_{2t};\ \textbf{现仅 }t\in\{2,3,4,5\}\ \text{有构造}&\text{构造＋有限前沿}\ (t\ge6)&\boxed{\text{LANE-A}}\\
S2&\text{OEIS }\texttt{A110000}:\ \text{正 }n\ \text{边形等面积剖分为等边三角形的最少块数};\ \textbf{仅 }a(3)=1\ \text{确知},\ \text{其余为\textbf{上界}}&\text{记录缺口（缺下界）}&\boxed{\text{LANE-A}}\\
S3&\text{OEIS }\texttt{A046057}（群论序列，带 }\texttt{a-file}\text{，多项未确定）}&\text{记录缺口}&\text{LANE-A（须读条目）}\\
S4&\text{Barbados 2026 问题 }24:\ \text{诱导子式封闭族是否“小”}&\text{结构定理}&\boxed{\text{LANE-B}}\\
S5&\text{Barbados 2026 问题 }1:\ \text{级并联图上的粗粒度 Menger}&\text{结构定理}&\text{LANE-B}\\
S6&\text{长度 }\equiv0\pmod{24}\ \text{的极值 doubly-even 自双工码存在性（Fermat 型）}&\text{存在性（著名）}&\text{WATCH（高重复风险）}\\
S7&\text{设计理论：BIBD 的 }\{1\}\text{-／}\{1,2\}\text{-块相交图 Hamilton 性（}k\ge3,\ v\ge c_k\text{）}&\text{结构定理（渐近）}&\text{LANE-B（渐近，}G3\ \text{偏弱）}\\
S8&\text{组合 Gray 码综述（DS26）所提问题集}&\text{混合（需逐条拆）}&\text{待拆}\\
S9&\text{Open Problem Garden 图论 227 条 ／ 代数 298 条}&\text{池（需条目级抽取）}&\text{待拆}\\
S10&\text{Ben Green 的 100 个开放问题};\ \text{Joyner–Kim 编码论未解问题集}&\text{池}&\text{待拆（Green 集\textbf{高覆盖风险}）}
\end{array}$$ ✓✓
```

## §3 重复投资风险旗标（本轮新增，供第二轮用）

```
$$\boxed{\text{旗标 R1}}:\ \text{OEIS 子集已被“自动形式化＋AI 证明搜索”攻击（2026 年 492 条 OEIS 开放问题被转入 Lean 并跑自动搜索）}\Longrightarrow\ \text{OEIS 供给}\textbf{须逐条查 AI 攻击记录}$$ ⚠️
$$\boxed{\text{旗标 R2}}:\ \text{Ben Green 的 100 个开放问题＝公开清单}\Longrightarrow\ \text{高覆盖风险（此前已判）}$$ ⚠️
$$\boxed{\text{旗标 R3}}:\ \text{著名条目（如 }S6\text{）属“经典主战场”，按 \textsc{amend-22} 指纹预审必降到末位}$$ ⚠️
$$\boxed{\text{旗标 R4}}:\ \text{2026 Barbados 表为}\textbf{当年度新表}\Longrightarrow\ \text{新度高（好），但须核“是否已有 2026 内新解”}$$ ⚠️
```

## §4 第二轮（唯一动作，待先生令）

```
$$\boxed{\text{对 }S1,S2,S3,S4\ \text{四项跑 \textsc{amend-20}/\textsc{amend-21}：族字面检索 → 三列覆盖表 → 三合一未覆盖判定}}$$
$$\qquad \text{优先序（按“一轮内可判定覆盖”的准备度）}:\ \boxed{S1>S2>S3>S4}$$
$$\qquad \text{理由}:\ S1\ \text{对象最具体（}t\ge6\ \text{构造缺口，证书＝显式图＋可验证）；}S2\ \text{记录缺口明确（上界有、下界缺）；}S3\ \text{须先读 OEIS 条目；}S4\ \text{属结构定理（LANE-B 闸门更严）}$$
$$\textbf{硬停止}:\ \text{若四项在第二轮均被判“已覆盖”}\Longrightarrow\ \text{回 L1/L3/L4 换来源，}\textbf{不得}在 }\ S1\text{–}S4\ \text{内改参数硬做（\textsc{amend-22}）}$$
【⛔ 纪律】 本轮**零计算**；`U_{2,3}` 暂停；**不回 RH**；本档**不含任何覆盖判定**（避免预填） ✓
【边界】 §2 全部为**抽取级**（来源摘要）；**未逐条读原文** ⟹ 不得据以宣称任何一项“未被研究” ✓

## §附 【技术词回查】（补录）
```
技术词 supply inventory 命中文件数=0    :: 
技术词 source tier      命中文件数=0    :: 
```
