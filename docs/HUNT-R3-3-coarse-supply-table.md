已查地图：命中（`HUNT-R3-round2-coverage-verdicts-S1-S4` ＋ `RESEARCH-CONSTITUTION` AMEND-23）⟹ `HUNT-R3.3` 三池粗筛，不开新案
D0: 本档对象 = **三池（`OPG`／`erdosproblems`／`Joyner–Kim`）粗筛表** ＋ **8 项候选（`X1`–`X8`）初筛 A/W/D** ＋ **两条整池级校准** ＋ 唯一 A 项的下一步
D1: 0（粗筛型，零计算）
[REVIEW]

# **`HUNT-R3.3`：三池粗筛表**

## §0 本轮口径（照先生）

```
$$\text{优先序}:\ \boxed{\text{明确旧记录}\to\text{可形成严格新记录}\to\text{证书可机器验证}\to\text{规模不过分依赖穷举}}$$
$$\text{要}:\ \text{记录型 }R_0\to R_1\to\text{独立证书验证};\qquad \text{降权}:\ \text{“存在一个尚未证明的下界”}$$
$$\text{排除}:\ \text{纯猜想}\ |\ \text{无有限证书接口}\ |\ \text{仅把 }n\ \text{做大}\ |\ \boxed{\text{已有系统计算项目在跑}}$$
$$\text{本轮只做粗筛};\ \textbf{不跑 \textsc{amend-20}/21};\ \textbf{零计算}$$ ✓
```

## §1 粗筛表

```
$$\begin{array}{c|l|l|l|l|l|c}
\#&\text{来源}&\text{已知记录}&\text{缺口类型}&\text{可证书化}&\text{疑似纯穷举}&\text{初筛}\\\hline
X1&\texttt{OEIS A000983}\ (=\text{超立方体支配数 }\gamma(Q_n)\ =\ \text{二元长 }n\text{、半径 }1\ \text{最小覆盖码})& n\le9\ \text{精确 }(1,2,2,4,7,12,16,32,62);\ \boxed{a(10)\in[107,120]}\ (\text{OEIS 注，2016})&\boxed{\text{记录型（区间未闭合）}}&\boxed{\text{可}}:\ \text{码＝显式集合};\ \text{覆盖性＝枚举邻居可验证};\ \text{下界＝ILP/SAT 证书}&\text{部分}（\text{历史 tabu search／ILP}）&\boxed{\textbf{A}}\\
X2&\texttt{A000983}\ \text{之 }n=11\ \text{格}& \text{已有 best-known 构造 }(n\le11,\ \text{Kamenetsky});\ \text{精确值未定}&\text{记录型}&\text{可}&\text{部分（规模更大）}&\text{W}\\
X3&\text{覆盖码总表 }K(n,R)\ (\text{Cohen–Honkala};\ n\le33,R\le10)&\text{表中大量上下界；}\text{部分格已闭合}&\text{记录型}&\text{可}&\boxed{\text{是}}\ (\text{tabu search 系列在跑})&\text{D/W}\\
X4&\text{超立方体}\ \textbf{全支配数}\ \gamma_t(Q_n)& n\le10\ \text{已知}\ (\gamma_t(Q_{10})=124);\ n\ge11\ \text{开}&\text{记录型}&\text{可}&\text{是（ILP 在跑）}&\text{W}\\
X5&\texttt{OPG}\ \text{图论池（228 条）}&\text{检索所见多为}\boxed{\text{猜想型}}（\text{Cycle Double Cover／3-Decomposition／Fractional Hadwiger／Chromatic Number of Common Graphs…}）&\text{非记录型 ✗}&\text{否}&\text{—}&\boxed{\textbf{D}}\ (\text{除 Extremal G.T. 9 条＋Coloring 66 条待细看})\\
X6&\texttt{erdosproblems.com}\ (\sim1{,}179\ \text{题},\ 483\ \text{已解})&\text{整池被系统攻击（见 §2）}&\text{—}&\text{—}&\text{—}&\boxed{\textbf{D}（整池降权）}\\
X7&\text{Joyner–Kim《Selected Unsolved Problems in Coding Theory》}&\text{方向（covering／domination 表缺口）与 }X1\ \text{重合；}\textbf{条目级抽取本轮未完成}&\text{记录型（待抽取）}&\text{可}&\text{待判}&\text{W（来源补充）}\\
X8&\text{多重／混合覆盖码表（Hämäläinen 等；binary/ternary mixed）}&\text{已有上下界表；例：}K(9,1)\ge57\ (\text{原 }55),\ K(11,1)\ge180\ (\text{原 }178)&\text{记录型}&\text{可}&\text{是}&\text{W}
\end{array}$$ ✓✓
```

## §2 ⭐ 两条整池级校准（本轮新增，写入来源评估）

```
$$\boxed{\text{校准 E1}:\ \texttt{erdosproblems.com}\ \textbf{整池已是 AI 收割基准}}\ \Longrightarrow\ \text{整池降权（D）}$$
$$\qquad \text{证据}:\ \text{FrontierMath Erdős（Epoch AI，2026-09-01）}:\ \textbf{68 条重大 Erdős 问题（截至 2026-08 仍开）由 Thomas Bloom 精选并 Lean 形式化};\ \text{Bloom 估计 2026-08 前 AI 已解 3–5 条同量级问题};$$
$$\qquad \qquad \text{Quanta（2026-08）}:\ \text{“Erdős problems are falling to AI”};\ \text{Tao 记 }#728\ \text{首例自主解};\ \text{社区用“数千次 GPT-5 查询”解出 10 条列为开放的问题};$$
$$\qquad \qquad \text{案例研究（}\texttt{arXiv:2601.22401}\text{）}:\ \text{“所有下降都来自文献清理而非新数学”}\Longrightarrow\ \textbf{该池“open”标签不可靠}$$
$$\boxed{\text{校准 E2}:\ \texttt{OPG}\ \textbf{以猜想型为主，与“记录型”筛选结构不兼容}}\ \Longrightarrow\ \text{降权（D）}$$
$$\qquad \text{例外}:\ \texttt{Extremal G.T.}（9\ \text{条}）、\texttt{Coloring}（66\ \text{条}）\ \text{两子类可能含记录型条目}\Longrightarrow\ \text{保留待细看（W）}$$
```

## §3 结论与唯一下一步

```
$$\boxed{\text{本轮唯一 A 项}:\ X1\ (\texttt{OEIS A000983}\ /\ K(10,1)\ /\ \gamma(Q_{10})\ \text{记录缺口 }[107,120])}$$ ✓✓
$$\text{为何最像 }C07:\ \text{对象＝有限二元码（非线性）};\ \text{上界＝显式码（可验证覆盖）};\ \text{下界＝证书型（ILP/SAT）};\ \text{记录源＝OEIS 条目（可得）};\ \text{与 }C07\ \text{同族但}\boxed{\text{不同对象}}（\text{半径 }1\ \text{非线性}\ \text{vs 线性协维格}）\ \Longrightarrow\ \text{不违 \textsc{amend-22}}$$ ✓✓
$$\textbf{⚠️ 前置门槛（LANE-A ① 加严条款）}:\ \text{须先读权威记录源、确认 }a(10)\ \text{的}\textbf{现行状态};\ \text{本轮检索}\textbf{未能确认}（\text{仅见 2016 年 OEIS 注）$$
$$\qquad \Longrightarrow\ \textbf{下一步（唯一）}:\ \text{读 }(i)\ \texttt{OEIS A000983}\ \text{条目全文};\ (ii)\ \text{Cohen–Honkala《Covering Codes》表与 1990s–2020s 后续改进};\ (iii)\ \text{Kamenetsky best-known 表};\ \text{确认缺口是否仍开}$$
$$\qquad \text{若 }a(10)\ \text{已定阅}\Longrightarrow\ X1\ \text{降为 }\textbf{W/CLOSED}，\text{并转 }X2\ (n=11)\ \text{或 }X8\ (\text{多重覆盖码})$$
$$【⛔ 纪律】 本轮\textbf{零计算};\ \text{不跑 \textsc{amend-20}/21};\ \text{未制造候选};\ \text{未对任何项作“值得做”排序} ✓
【边界】 全部为\textbf{检索抽取级};\ X1\ 的 }a(10)\ \text{现行状态\textbf{未确认}};\ \text{不得据以宣称该格仍开} ✓

## §附 【技术词回查】（补录）
```
技术词 coarse supply    命中文件数=0    :: 
技术词 record gap       命中文件数=2    :: ./C309-direction1-zero-spacing-anomaly-four-column-audit.md ./C308-direction1-prime-gap-anomaly-four-column-audit.md 
```
