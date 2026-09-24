已查地图：命中（`S2-C07-STAGE-REPORT-CLOSED` ＋ `AMEND-18/19`）⟹ `Zone-B` 八条 `U_research` 五元组补齐，不开新案
D0: 本档对象 = **`Zone-B` 口径锁定（`N=16/SPEC=8/U_research=8`）** ＋ **八条 `(X,G,A,P,E)` 五元组补齐** ＋ **文献／参数级排除结果（`DROP/KEEP/WATCH`）** ＋ **一条口径不一致标注**
D1: 1（首次对 `Zone-B` 非 `SPEC` 类做五元组化与攻击入口判定）
[RESEARCH]

# **`Zone-B` 八条 `U_research` 五元组（第一轮）**

## §0 口径锁定（不重新统计）

```
$$\boxed{N=16}\ (\text{Zone-B});\quad \boxed{SPEC=8}=\{M01,M02,M06,Au03,Au04,Au05,Au07,Au08\};\quad \boxed{U\_{research}=8}=\{M03,M04,Au06,G01,G02,G05,G06,G08\}$$ ✓✓
$$\textbf{五元组记号}:\ X=(\mathcal O,\mathcal P)\ \text{精确对象＋参数窗口};\ G=\text{已知结果／覆盖程度};\ A=\text{可动用资产};\ P=\text{攻击入口（}AMEND\text{-}19\ \text{的 }P1/P2\text{）};\ E=\text{可执行检验／证据等级}$$ ✓
$$\text{（与 }AMEND\text{-}18\ \text{对应}:\ X\supseteq(\mathcal O,\mathcal P);\ G=\mathcal G;\ E=\mathcal T;\ \mathcal I\ \text{并入 }X/P\text{）}$$ ✓
$$\textbf{⚠️ 口径标注}:\ \text{census L154 将 }Au06\ \text{记为 }P\ \text{（非 }U\text{）};\ \text{Zone-B 名单将其列为 }U\_{research} \Longrightarrow \textbf{该条标签需回填校正};\ \text{本轮按其实质补齐}$$ ⚠️
```

## §1 八条五元组（逐条）

```
$$\textbf{G01}\ \text{阶 }n\le512\ \text{非超可解精确个数 ＋ 最小反例序列}$$
$$\ X:\ \mathcal O=\{\text{群 }|G|\le512\},\ \mathcal P=n\le512;\quad \mathcal I=(\text{每个 }n\ \text{的非超可解个数},\ \text{最小反例阶})$$
$$\ G:\ \textbf{最小反例部分已闭合}:\ \text{最小非超可解群}=\boxed{A_4}\ (\text{阶 }12)\ \text{（标准事实，档级）}\ \Longrightarrow\ \textbf{该半支无缺口}$$
$$\qquad \text{计数部分}:\ \text{SmallGroups 库枚举（除 }1024\text{）＋超可解判定算法}\ \Longrightarrow\ \textbf{纯库内计算}$$
$$\ A:\ D\ (\text{精确计数＋复核})\ \text{为主};\ E\ \text{备用};\quad P:\ \boxed{\text{无}};\quad E:\ \text{无须检验}$$
$$\ \Longrightarrow\ \boxed{\textbf{DROP}}\ ——\ \text{一支平凡（}A_4\text{）};\ \text{另一支为库内计算，不形成数学命题（同 }G01\ \text{既有边界："全库 }\ne\text{ 目标统计量"}$$ ✓✓
$$\textbf{G02}\ \text{固定 }n\le2000\ \text{自同构群阶的精确分布}$$
$$\ X:\ \mathcal O=\{\text{群 }|G|=n\},\ \mathcal P=n\le2000;\ \mathcal I=|{\rm Aut}(G)|\ \text{分布}$$
$$\ G:\ \text{对象由 SmallGroups 库给出（}1024\ \text{除外};\ \text{该阶有 }4.9\times10^{10}\ \text{个群，库不覆盖）};\ |{\rm Aut}|\ \text{可算}$$
$$\ A:\ D;\quad P:\ \boxed{\text{无}};\quad E:\ \text{无须}$$
$$\ \Longrightarrow\ \boxed{\textbf{DROP}}\ ——\ \textbf{纯库内统计};\ \text{且 }n=1024\ \text{的数据空洞} \Longrightarrow \text{窗口天然残缺},\ \text{不构成可证命题}$$ ✓✓
$$\textbf{G05}\ \text{小群中 }|H\cap gKg^{-1}|\ \text{的精确分布}$$
$$\ X:\ \mathcal O=\{(G,H,K,g)\}\ ——\ \textbf{群族未定、}n\ \text{未定};\ \mathcal I=\text{交大小的分布}$$
$$\ G:\ \text{交大小有一般性结论（同阶子群的交、}Isaacs\ \text{型结果});\ \text{但"分布"无既定目标量};\ \textbf{无窗口}$$
$$\ A:\ D/E;\quad P:\ \boxed{\text{不可判（窗口缺失）}};\quad E:\ \textbf{缺}\ \mathcal P\ \text{与目标统计量}$$
$$\ \Longrightarrow\ \boxed{\textbf{WATCH}}\ —— \text{对象成立但\textbf{规格未闭合}；须先钉死（群族＋}n\text{＋目标量），方可判 }P1/P2$$ ✓✓
$$\textbf{G06}\ n\le256\ \text{生成元对数最小值与达到者分类}$$
$$\ X:\ \mathcal O=\{\text{群 }|G|\le256\};\ \mathcal I=\text{"生成元对数最小值"}\ ——\ \textbf{歧义}:\ (\text{i})\ \text{最小生成集大小的配对化};\ (\text{ii})\ \text{生成对的\textbf{覆盖数}（用最少生成对覆盖 }G）$$
$$\ G:\ \text{生成对计数 }|G|^2 P(G)\ \text{与 }2\text{-生成性（单群）有成熟结论};\ \text{但"覆盖数"目标量未见标准结果}$$
$$\ A:\ D\ (\text{精确枚举＋复核});\quad P:\ \text{若取 (ii)} \Rightarrow P2\ \text{可构造／}P1\ \text{待定};\quad E:\ \textbf{须先消除歧义}$$
$$\ \Longrightarrow\ \boxed{\textbf{WATCH}}\ ——\ \text{规格歧义未消；若钉死为 (ii) 且覆盖数无文献结果} \Longrightarrow \text{可升 }KEEP$$ ✓✓
$$\textbf{G08}\ \text{小阶群特征标表上独立量的极值}$$
$$\ X:\ \mathcal O=\{\text{小阶群的特征标表}\};\ \mathcal I=\text{"独立量"}\ ——\ \textbf{未指明是哪一个不变量}$$
$$\ G:\ \text{特征标表标准不变量族（次数、域、}Schur\ \text{指标、}Frobenius\text{-}Schur\ \text{指标等）均有既定理论}$$
$$\ A:\ D/E;\quad P:\ \boxed{\text{不可判}};\quad E:\ \textbf{缺目标量}$$
$$\ \Longrightarrow\ \boxed{\textbf{WATCH}}\ ——\ \text{规格未闭合（同 }G05\ \text{型）}$$ ✓✓
$$\textbf{M03}\ n=5\ \textbf{SNIEP 整谱可实现性完整表}$$
$$\ X:\ \mathcal O=\{\text{整数 }5\text{-谱}\},\ \mathcal P=\text{归一化后（如固定 }+\text{最大元或固定 }trace）;\ \mathcal I=\text{可实现性}\ (\exists\ \text{对称非负 }5\times5\ \text{矩阵})$$
$$\ G:\ \textbf{SNIEP }n\le4\ \text{已解（且与 }NIEP\ \text{一致）};\ n\ge5\ \textbf{开放}\ (\text{且 }n\ge5\ \text{时 }SNIEP\ne NIEP\ \text{已知})$$ ✓✓
$$\ A:\ E\ (\text{矩阵／惯性})\ +\ D\ (\textbf{构造性证书可精确复核}:\ \text{有理／整数矩阵})\ +\ G\ (\text{最小反例})\ \text{高度匹配}$$ ✓✓
$$\ P:\ \boxed{P2\ \text{强}} —— \text{对给定整数谱构造对称非负矩阵，}\textbf{可机器精确验证};\ \boxed{P1\ \text{弱}} —— \text{不可行性};\ \text{已知必要条件是现成工具}$$
$$\ E:\ \text{取"最小开放"}n=5\ \text{具体谱族（如 }trace=0\ \text{或最大元固定）} \Longrightarrow \text{有限子问题，可证书化}$$
$$\ \Longrightarrow\ \boxed{\textbf{KEEP}}\ (\textbf{Zone-B 首选}) —— \text{真开放 ＋ 双侧入口不对称但 }P2\ \text{可产证书}$$ ✓✓✓
$$\textbf{M04}\ \text{小尺寸 }(0,\pm1)\text{-矩阵 rank 分布}$$
$$\ X:\ \mathcal O=\{(0,\pm1)\ n\times n\ \text{矩阵}\},\ \mathcal P=n\le?\ ——\ \textbf{未定};\ \mathcal I={\rm rank}\ \text{的分布（域未定}:\ \mathbb R\ \text{或 }\mathbb F_2\text{）}$$
$$\ G:\ (0,1)\ \text{矩阵秩计数有文献};\ (0,\pm1)\ \text{的 }n\le6\text{ 亦可能已列表};\ \text{规模}:\ 3^{n^2}\ (\text{对称性约化后仍大})$$
$$\ A:\ D/E;\quad P:\ \text{若 }n\ \text{小且域取 }\mathbb F_2 \Rightarrow P2\ \text{枚举};\ \text{但"分布"无定理目标};\quad E:\ \textbf{须先定 }n\ \text{与域＋做收割点检}$$
$$\ \Longrightarrow\ \boxed{\textbf{WATCH}}\ —— \text{规格未闭合 ＋ 收割风险高（枚举型）}$$ ✓✓
$$\textbf{Au06}\ \text{特定类 Collatz 型停时记录（有界域）}$$
$$\ X:\ \mathcal O=\{qx+1\ \text{型},q\in\{5,7,9\}\},\ \mathcal P=x\le10^8;\ \mathcal I=\max T_q(x)\ \text{与达到者集合}$$
$$\ G:\ 3x{+}1\ \text{的延时记录已算到 }10^{20}\ \text{级};\ q=5,7,9\ \text{变体研究较薄},\ \textbf{但同类记录型工作被算力队密集收割}$$
$$\ A:\ D\ (10^8\times3\ \text{可算});\quad P:\ P2\ \text{（构造记录）},\ P1\ \text{无};\quad E:\ \textbf{须先做"是否已收割"点检}$$
$$\ \Longrightarrow\ \boxed{\textbf{WATCH}}\ (\text{记录型}/\text{LANE-A},\ \text{非机制型}) —— \text{可作标定，不作 }Zone\text{-B 主攻}$$ ✓✓
```

## §2 分类结果

```
$$\begin{array}{c|c|l}
\text{ID}&\text{判定}&\text{理由（一句话）}\\
\hline
G01&\textbf{DROP}&\text{一支平凡（}A_4\text{）＋一支库内计算}\\
G02&\textbf{DROP}&\text{纯库内统计 ＋ }1024\ \text{空洞}\\
G05&\textbf{WATCH}&\text{规格未闭合（群族/}n/\text{目标量皆缺）}\\
G06&\textbf{WATCH}&\text{"生成元对数"歧义未消}\\
G08&\textbf{WATCH}&\text{"独立量"未指明}\\
\M03&\boxed{\textbf{KEEP}}&\text{真开放 ＋ }P2\ \text{可产机器证书 ＋ 资产 }E/D/G\ \text{匹配}\\
\M04&\textbf{WATCH}&\text{规格未闭合 ＋ 枚举型收割风险}\\
Au06&\textbf{WATCH}&\text{记录型，需收割点检}\\
\end{array}$$ ✓✓
$$\Longrightarrow\ \boxed{8\ \text{条}:\ 2\ \text{DROP}\ +\ 5\ \text{WATCH}\ +\ \boxed{1\ \text{KEEP}\ (M03)}}$$ ✓✓
```

## §3 `C07` 教训的迁移应用（先生提议）

```
$$\textbf{通则}:\ \text{遇"已有 }a\text{-}b\ \text{区间"的表格型问题},\ \textbf{先查是否存在参数变换（对偶／奇偶校验／长度函数）把"补格"变成"造对象"}$$ ✓✓
$$\text{何时可用}:\ \text{问题有线性代数实现（如矩阵／编码）}\ \Longrightarrow\ \text{存在对偶侧目标量};\ \text{此时 }P2\ \text{常转成可机器复核的构造}$$ ✓✓
$$\text{本轮应用}:\ M03\ \text{正是该型} —— \text{可实现性} = \text{构造} = \textbf{可精确复核};\ M04\ \text{若限制在 }\mathbb F_2\ \text{亦近似该型（可枚举＋证书）}$$ ✓
$$\text{不适用}:\ G01/G02\ \text{型（纯库内统计）};\ Au06\ \text{型（记录型）}$$ ✓
```

## §4 指针与下一步

```
$$\boxed{\text{Zone-B 第一轮结论}}:\ \text{唯一 }KEEP=\boxed{M03\ (\text{SNIEP }n=5,\ \text{整数谱})}$$ ✓✓
$$\textbf{下一步（建议）}:\ (i)\ M03\ \text{先做规格闭合（归一化＋最小开放谱族）};\ (ii)\ \text{再套 }AMEND\text{-}19\ \text{写 }P1/P2;\ (iii)\ \text{通过后才谈计算（}P2\ \text{构造＋证书复核）}$$ ✓✓
$$\text{挂起}:\ G05/G06/G08/M04\ \text{四条需先生给规格（群族/}n/\text{目标量}）};\ Au06\ \text{需收割点检};\ G01/G02\ \text{已 }DROP$$ ✓
【⛔ 纪律】 本轮\textbf{零计算}；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；`C07` 已封口不回头 ✓
【边界】 §1 中"内库覆盖／已解 }n\le4$$"等为**档级**；`A_4` 为阶 12 最小非超可解群＝**标准事实（档级）**；`M03` 的开放性与资产匹配为**判断**，非结论 ✓

## §附 【技术词回查】（补录）
```
技术词 SNIEP            命中文件数=5    :: ./S2-HANDOFF-zone-members-and-count-fix.md ./TOPIC-DOSSIER-v1-six-columns-and-relations.md ./S2-ZONEB-eight-U-research-5tuple-round1.md 
技术词 five tuple       命中文件数=0    :: 
```
