已查地图：命中（`S2-30-FINAL-LOCK` ＋ `AMEND-17`）⟹ 本档为 `Batch-1` 记录，不开新案
D0: 本档对象 = **`S2 / Batch-1`（`F1+F2+F3`，19 条）**：逐条七列记录 ＋ 批统计 `(C,P1,P2,P3,P4,U,SPEC)` ＋ 两处新校准点（`G01`、`P02`）
D1: 1（首个 70 条批次完成 S2；产出 `P4` 严格化与多标签归并两条口径）
[RESEARCH]

# **`S2 / Batch-1` 记录（`F1＋F2＋F3`，19 条）**

## §1 逐条（ID｜S2｜P类｜直接文献/数据集｜覆盖对象｜未覆盖部分｜Decision）

```
$$\begin{array}{c|c|c|l|l|l|c}
\text{ID}&\texttt{S2}&P&\text{直接文献／数据集}&\text{覆盖对象}&\textbf{未覆盖部分}&Decision\\
\hline
G01&U&—&\text{SmallGroups Library（阶}\le2000\ \text{除 }1024;\ \approx4.23\times10^8\ \text{对象};\ 2^9\ \text{完整层）}&\text{给定阶完整有限群对象}&\text{"非超可解精确个数＋最小反例序列"未作为 exact 命题给出}&U\\
G02&U&—&\text{SmallGroups 对象全集 ＋ LMFDB 部分结构}&\text{小阶群及部分群数据}&n\le2000\ \text{按 }|\mathrm{Aut}G|\ \text{的完整精确分布}&U\\
G03&P&P3&\text{maximal-subgroup index 理论};\ \text{Costantini–Zacher 子群指数问题};\ \text{Hall 型指数定理}&\text{极大子群指数结构性理论}&n\le1000\ \text{缺失指数完整清单未列出};\ \text{对象族不完全相同}&P3\\
G05&U&—&\text{Berkovich《Groups of Prime Power Order》子群交章节}&\text{某些 }p\text{-群子群交结构}&|H\cap gKg^{-1}|\ \text{的完整精确分布}&U\\
G06&U&—&p\text{-群 generators／Frattini／minimal-generation 理论}&\text{生成理论}&n\le256\ \text{全群最小生成元数＋达到者分类}&U\\
G07&P&P4&\text{SmallGroups 的 }p\text{-群完整枚举（}p^n,n\le6;\ p^7\ \text{若干素数）＋ Frattini/生成数据层}&\text{阶}\le3^7\ \text{的 }p\text{-群对象及 Frattini 结构}&\text{按 Frattini 指数的完整分布表（非现成输出）}&P4\\
G08&U&—&\text{Berkovich：character degrees／minimal classes 章节}&\text{小 }p\text{-群字符理论}&\text{特征标表独立量极值的 exact extremal 命题}&U\\
Gr06&U&—&\text{图惯性一般理论 ＋ unicyclic graphs inertia 完整刻画（LAA）}&\text{特殊图族 inertia}&n=9\ \text{给定 }(p,q,z)\ \text{存在性完整表}&U\\
Gr08&U&—&\text{House of Graphs（明确非给定阶全集）};\ \text{Graph Atlas 仅到 7 顶点}&\text{部分图及不变量}&n\le10\ \text{正则化 Laplacian slope 完整取值集合}&U\\
Gr09&P&P2&\text{图能量一般界＋extremal characterization};\ \text{2021 "few distinct eigenvalues and extremal energy"};&\ \text{2025–26 新 bounds}&\text{图能量极值理论及若干达到者}&\text{小阶 exact 极值＋唯一性（未被通用定理直接蕴含）}&P2\\
Gr10&U&—&\text{inertia／minimum-rank 一般理论 ＋ outerplanar 等族结果（LAA）}&\text{特定图族 rank/inertia}&n\le10\ \text{给定 inertia 且取极小秩的图的计数}&U\\
P01&P&P4&\text{长度 5 的 120 模式} \to 16\ \text{Wilf classes ＋ 系统系数计算（EJC）}&\text{长度 5 模式及 Wilf-class 分类}&n=12\ \text{每类 exact count（非分类定理本身）}&P4\\
P02&P&\boxed{P3}&{\text{长度 4 Wilf-equivalence 基本分类（}S_4:\ 3\ \text{类）};\ \text{4-pattern 集合完整分类};\ \text{完整 Wilf-equivalence 推进到长度 7}}&{\text{Wilf-equivalence／classification}}&{\text{"弱 Wilf 等价类完整分类证书"规格未给出};\ \text{weak/refined}\ne\text{普通 Wilf-equivalence}}&{P3\ +\ \texttt{SPEC}}\\
P03&P&P2&{\text{Chow：involutions 按 descent set 的 Eulerian 枚举（EJC）};\ \text{Brualdi–Ma exact enumeration}}&{\text{involution＋descent-set 精确枚举}}&{\text{"公式之反例搜索"非被公式直接判定的 exact 命题};\ \text{反例目标须先具体化}}&P2\\
P04&U&—&\text{permutation statistics／descent 广泛枚举理论}&\text{邻近排列统计}&\text{循环递降最大值对应排列数的 exact 公式／表}&U\\
P05&P&P4&\text{单／双模式与小模式集合大量完整枚举（含 }3{+}4\ \text{类 exact sequences）}&\text{大量小模式 avoidance classes}&n\le13\ \text{指定两模式且未列入现有表的 exact cells}&P4\\
P06&U&—&\text{riffle／perfect-shuffle 标准结构理论}&\text{shuffle 的排列结构}&\text{最短分解长度极值＋达到者分类}&U\\
P07&P&P3&\text{特定生成集 }S_n\ \text{diameter 已列到 }n=13（\text{OEIS A186783}）＋ 精确 diameter 论文}&\text{若干特定生成集的 Cayley 图 diameter}&\text{候选指定生成集尚未与已知序列／论文逐字对应}&P3\\
P08&U&—&\text{LIS 一般分布／渐近／精确小阶理论}&\text{LIS distribution theory}&n\le11\ \text{exact tail table}&U\\
\end{array}$$ ✓✓
```

## §2 批统计（逐批独立；`SPEC` 单列）

```
$$\boxed{C=0,\quad P_1=0,\quad P_2=2,\quad P_3=3,\quad P_4=3,\quad U=11,\quad \texttt{SPEC}=1}$$ ✓✓
$$\text{核对}:\ 0+2+3+3+11=\boxed{19}\ \checkmark;\qquad P_2=\{Gr09,P03\};\ P_3=\{G03,P02,P07\};\ P_4=\{G07,P01,P05\};\ \texttt{SPEC}=\{P02\}$$ ✓
$$\textbf{本批无一条升级 }\texttt{COVERED}$$ ✓✓
```

## §3 本批两处校准点（登记入回归集）

```
$$\textbf{① }\boxed{G01}:\ \text{\textbf{有完整底层数据库}}\ne\text{\textbf{目标统计已被数据库覆盖}}（\text{把 SmallGroups 逐群跑 IsSolvableGroup ＝ \textbf{我们自己的计算}，不是现成 }P4\text{ 证据）}$$ ✓✓✓
$$\textbf{② }\boxed{P02}:\ \text{普通 Wilf classification}\ne\text{weak／refined Wilf target}（\text{refinement 要求保持指定 statistics 的双射}）$$ ✓✓✓
$$\text{连同 }S2\text{-}30\ \text{的 }Po02／Gr03，回归集现为四条}（Po02,\ Gr03,\ G01,\ P02）$$ ✓
```

## §4 状态

```
$$\texttt{S3}\ \textbf{冻结不变};\quad S2\text{-}30\ \text{锁定口径不变}（C=4,P=17,U=9）;\quad \text{下一批}\to \texttt{Batch-2}（18\ \text{条}:\ F4\ \text{余 }6＋F5\ \text{余 }6＋F6\ \text{余 }6）$$ ✓
【⛔ 纪律】 本档零数学计算；`U_{2,3}` 暂停；**不回 RH** ✓
【边界】 §1 文献为**档级**（先生本轮检索）；两条新口径已入 `AMEND-17` ✓

## §附 【技术词回查】（补录）
```
技术词 batch            命中文件数=3    :: ./C380-S1-FREEZE.md ./C380-K4-GATE-FREEZE.md ./C380-221-COMPUTATION-SPEC-FREEZE.md 
技术词 evidence         命中文件数=28   :: ./paper-dimension-reduction.md ./PAPERA-v2-structure.md ./p49-g274lc-section78-verify.md 
```
