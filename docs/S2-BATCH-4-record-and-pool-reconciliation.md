已查地图：命中（`S2-BATCH-3-record` ＋ `AMEND-17`）⟹ 本档为 `Batch-4` 记录 ＋ 全池口径复核，不开新案
D0: 本档对象 = **`S2 / Batch-4`（`F10+F11+F12`，18 条）**＋ **100 条全池口径复核**（两处计数修正：`SPEC` 与合计式）
D1: 1（末批完成 S2；100 条全过 S2；产出全池口径锁定与两处修正）
[RESEARCH]

# **`S2 / Batch-4` 记录 ＋ 全池复核**

## §0 ⚠️ 独立复核（两处计数修正）

```
$$\textbf{修正①}\ \texttt{SPEC}\ \text{数}:\ \text{先生摘要记 }\texttt{SPEC}=8;\ \text{但}\ \textbf{逐行表与所列集合均为 }10\ \text{项}$$
$$\qquad \{M01,M02,M06,Mt04,Mt05,Au03,Au04,Au05,Au07,Au08\}=\mathbf{10};\ \text{且 }U\ \text{的 10 行}\ \textbf{全部}挂 \texttt{SPEC}$$ ✓✓
$$\qquad \Longrightarrow\ \boxed{\texttt{SPEC}=10}\ (\text{与 }U\ \text{逐行一致};\ \text{摘要的 }8\ \text{应为笔误})$$ ⚠️
$$\textbf{修正②}\ \text{全池合计式}:\ \text{先生写 }7+0+14+4+17+41=83\ \text{并称"83 条有明确主状态"}$$
$$\qquad \text{但 }S2\text{-}30\ \text{的 }\mathbf{17\ P}\ \text{在其汇总行记"—"（}\textbf{未按 }P_1\text{–}P_4\ \text{细分}）;\ \text{故 }83\ \text{是}\textbf{漏了这 }17\ \text{条}$$ ⚠️
$$\qquad \text{正确恒等式}:\ \boxed{7\ (C)+17\ (S2\text{-}30\ \text{的 }P)+14\ (P_2)+4\ (P_3)+17\ (P_4)+41\ (U)=100}\ \checkmark$$ ✓✓✓
$$\qquad \Longrightarrow\ \text{100 条}\ \textbf{全部已有主状态};\ \text{其中 }P\ \text{总量}=17+35=\mathbf{52};\ \text{批 1–4 的 }35\ \text{条已细分为 }P_2/P_3/P_4$$ ✓✓
```

## §1 逐条判定（18 条）

```
$$\begin{array}{c|c|c|l|l|l|c}
\text{ID}&\texttt{S2}&P&\text{直接证据}&\text{已覆盖对象／统计}&\textbf{未覆盖部分}&Decision\\
\hline
M01&U&—&{\text{未找到针对"特定结构矩阵族 }n\le30\text{"并直接给出秩亏 exact 值的现成结果（结构化秩亏问题本身有成熟研究）}}&{\text{structured rank-deficiency 一般问题}}&{\text{"特定结构族"未指定};\ \text{exact rank-defect table 未找到}}&{U+\texttt{SPEC}}\\
M02&U&—&{\text{PSD 参数化判定理论丰富（含有限域 PSD 的枚举/界），但未命中候选所指的具体参数化族}}&{\text{一般 PSD／参数化 positivity 理论}}&{\text{参数化族、阈值变量、exact threshold 均未定义}}&{U+\texttt{SPEC}}\\
M05&P&P2&{\text{sign-rank 与 rank 关系成熟（sign-rank／VC-dimension 系统上下界；sign-rank 极值研究多）}}&{\text{sign-rank、rank 的一般极值/比较理论}}&{\text{小尺寸指定矩阵类的 exact extremal gap 及 achievers}}&P2\\
M06&U&—&{\text{minimum-rank／inverse-inertia 理论丰富（图所描述矩阵类的 minimum rank 与 inertia 已有分类）}}&{\text{特定零模式下 minimum rank／inertia}}&{\text{候选要的是"给定 inertia 后\textbf{矩阵数量}"，非 minimum-rank existence/classification}}&{U+\texttt{SPEC}}\\
M07&P&P4&{\text{小阶 totally-positive matrix 已有直接 enumeration；近期工作给出小阶数量公式/枚举与其余情形的 structural formula/bounds}}&{\text{小尺寸 TP matrices 的现成计数}}&{\text{"count 极值"及完整 achiever classification}}&P4\\
M08&P&P2&{\text{特定矩阵族 eigenvalue multiplicity／spectral structure 一般结果多};\ \text{未见"小尺寸＋极值＋唯一性"完整表}}&{\text{特定族特征值重数理论}}&{\text{候选族未具体指定};\ \text{exact extremum/uniqueness}}&P2\\
Mt03&P&P2&{\text{finite-poset width/max antichain 完整一般理论};\ \text{工具以 width 为基本对象并给算法}}&{\text{width／maximum-antichain 理论}}&{\text{指定有限偏序族的 exact maximum}}&P2\\
Mt04&U&—&{\text{格/poset 表示数有一般表示理论，但未取得"小阶格"现成 exact extremal count}}&{\text{小格表示的一般理论}}&{\text{"表示数"指哪种 representation 未定义，目标族亦未定义}}&{U+\texttt{SPEC}}\\
Mt05&U&—&{\text{hypergraph minimal-obstruction 理论存在，但候选未指定 hypergraph property／obstruction relation}}&{\text{一般 forbidden／minimal-obstruction 理论}}&{\text{minimal obstruction 的尺寸分类对象未闭合}}&{U+\texttt{SPEC}}\\
Mt06&P&P4&{\text{STS(19) 完整分类逐个记录 }|\mathrm{Aut}|\ \text{并已有按 automorphism-group order 的完整统计表};\ STS(15)\ \text{亦有 }\mathrm{Aut}\ \text{数据}}&{\text{STS(19)/STS(15) 各同构类 }|\mathrm{Aut}|\ \text{distribution}}&{\text{更一般小阶 STS 参数范围的完整分布/极值分类}}&P4\\
Mt07&P&P4&{\text{小参数 Ramsey numbers 已有直接表格（exact 值与上下界分格列出）}}&{\text{一批小 Ramsey 参数的 exact/bound 数据}}&{\text{未收割参数格的 exact extremal values}}&P4\\
Mt08&P&P4&{\text{小 matroid 的 Tutte polynomial 已有直接计算实例};\ \text{并有 }T\text{-unique}／T\text{-equivalent 分类与反例结果}}&{\text{小 matroid 的 Tutte polynomial、}T\text{-unique/}T\text{-equivalent 部分分类}}&{\text{完整小阶唯一性/反例谱}}&P4\\
Au02&P&P4&{\text{有限 CA 的 cycle structure／cycle-set 已有直接枚举与最大周期数据（含经典计算给出的 maximal periods）}}&{\text{指定 CA/rule/width 下的 cycle-length 数据与 enumeration}}&{\text{"特定 CA 规则"未固定} \Longrightarrow\ \textbf{不能 C}}&P4\\
Au03&U&—&{\text{小 Boolean network 可穷举 }2^n\ \text{状态空间};\ \text{另有 }n\le5\ \text{特定性质证明}}&{\text{小网络 attractor enumeration 方法、特定结构结果}}&{\text{全部 }n=5\ \text{网络的 exact attractor-count distribution}}&{U+\texttt{SPEC}}\\
Au04&U&—&{\text{transient／limit-cycle 理论成熟，有限状态空间结构明确}}&{\text{transient/limit-cycle 一般动力学理论}}&{\text{网络类未指定};\ \text{exact maximum transient length}}&{U+\texttt{SPEC}}\\
Au05&U&—&{\text{Boolean／Kauffman 网络有大量 limit-cycle 数量/长度研究，但主要是随机网络/特定模型统计}}&{\text{random Boolean networks 的 cycle statistics}}&{\text{小正则网络的 exact extremum ＋ achievers}}&{U+\texttt{SPEC}}\\
Au07&U&—&{\text{minimal DFA exact enumeration 存在：二字母、按等价语言计，OEIS A129622 给出 }n=1..7\ \text{逐值序列（}0,2,24,1028,56014,\dots\text{）}}&{\text{特定语言宇宙（二字母）下 minimal-DFA counts}}&{\text{候选写"给定语言类"但\textbf{语言类未指定};\ \textbf{不能}把特定类冒充目标覆盖}}&{U+\texttt{SPEC}}\\
Au08&U&—&{\text{未见"给定规则"的一般可逆性 threshold exact characterization};\ CA/有限自动机可逆性有特定规则结果但不足以覆盖}}&{\text{特定 CA/离散规则的可逆性结果}}&{\text{rule family、参数、threshold 均未定义}}&{U+\texttt{SPEC}}\\
\end{array}$$ ✓✓
```

## §2 批统计（锁定后）

```
$$\boxed{C=0,\quad P_1=0,\quad P_2=3,\quad P_3=0,\quad P_4=5,\quad U=10,\quad \texttt{SPEC}=10}$$ ✓✓（\texttt{SPEC}\ \text{按逐行}=10）$$
$$\text{核验}:\ 0+3+5+10=\boxed{18}\ \checkmark;\qquad P_2=\{M05,M08,Mt03\};\ P_4=\{M07,Mt06,Mt07,Mt08,Au02\};$$
$$U=\{M01,M02,M06,Mt04,Mt05,Au03,Au04,Au05,Au07,Au08\};\quad \texttt{SPEC}=U\ (\text{10 行全部挂标})$$ ✓
$$\textbf{本批 }C=0;\quad \textbf{无一条升级 }\texttt{COVERED}$$ ✓
```

## §3 本批六处边界（登记）

```
$$\textbf{① }\boxed{M07}:\ \text{目标统计量\textbf{本身已有枚举}}\ \Longrightarrow\ P4\ (\text{但要求"极值"未覆盖} \Rightarrow \text{非 }C)$$ ✓
$$\textbf{② }\boxed{Mt06}:\ \text{目标统计量 }|\mathrm{Aut}|\ \text{distribution \textbf{已作为现成输出存在}}\ \Longrightarrow\ P4\ (\text{与"有 STS 数据库"完全不同})$$ ✓✓
$$\textbf{③ }\boxed{Au07}:\ \text{有 OEIS 逐值序列}\ \textbf{但}\ \text{候选的"给定语言类"未指定}\ \Longrightarrow\ \boxed{U+\texttt{SPEC}}\ (\text{与 }C07\ \text{对照}:\ \text{那里参数格已明确})$$ ✓✓✓
$$\textbf{④ }\boxed{Mt08}:\ \text{有实质部分输出}\ (T\text{-unique/}T\text{-equivalent})\ \text{但完整唯一性/反例谱更强}\ \Longrightarrow\ P4$$ ✓
$$\textbf{⑤ }\boxed{Au03\text{–}Au05}:\ \text{"可穷举"}\ne P4(\text{自己跑 }\ne\ \text{现成输出})\ \Longrightarrow\ U\ (\text{不拔高})$$ ✓✓
$$\textbf{⑥ }\boxed{M06}:\ \text{同域理论（minimum-rank/inertia）}\ne\ \text{候选统计（给定 inertia 的矩阵\textbf{计数}）}\ \Longrightarrow\ U+\texttt{SPEC}$$ ✓✓
```

## §4 四批 ＋ 全池（锁定口径）

```
$$\begin{array}{c|rrrrrrr|r}
\text{批次}&C&P_1&P_2&P_3&P_4&U&\texttt{SPEC}&\text{总数}\\
\hline
S2\text{-}30&4&—&—&—&—&9&1&30\\
Batch\text{-}1&0&0&2&3&3&11&1&19\\
Batch\text{-}2&3&0&3&1&3&8&6&18\\
Batch\text{-}3&0&0&6&0&6&3&2&15\\
Batch\text{-}4&0&0&3&0&5&10&10&18\\
\hline
\text{全池}&7&—&14&4&17&41&20&100\\
\end{array}$$ ✓✓
$$\textbf{全池恒等式}:\ \boxed{7+17\ (\text{其中 }S2\text{-}30\ \text{的 }P\ \text{未细分})+14+4+17+41=100}\ \checkmark$$ ✓✓✓
$$\textbf{结构读法}:\ C=7\ (\text{退出池});\quad P=17+35=52\ (\text{已有资产＋明确缺口});\quad U=41\ (\text{其中 }\texttt{SPEC}=10\ \text{在本批},\ \text{全池 }\texttt{SPEC}\ \text{约 }20\ \text{条})$$ ✓
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §1 文献为**档级**；§0 两处修正须先生确认 ✓

## §附 【技术词回查】（补录）
```
技术词 pool             命中文件数=15   :: ./P1-3-unresolved-finite-problem-pool.md ./TOPIC-SEARCH-R1-candidates-seven-field.md ./F2-three-point-confirmation.md 
技术词 reconciliation   命中文件数=3    :: ./A4-M1-normalization-reconciliation.md ./M0-T-system-verbatim-and-theorem-locations.md ./HOT-STATE.md 
```
