已查地图：命中（`S2-CENSUS-1-and-2-...`）⟹ 本档为 Zone-A/B/C 逐条清单交付 ＋ ⚠️族矩阵计数修正，不开新案
D0: 本档对象 = **Zone-A/B/C 逐条成员清单（含逐字命题、主状态、形态）** ＋ ⚠️**族矩阵 F9/F10 计数修正**
D1: 0（交付/复核档）
[REVIEW]

# **Zone-A／B／C 逐条清单 ＋ 计数修正**

## §0 ⚠️ 族矩阵计数修正（F9／F10）

```
$$\textbf{按锁定记录逐条复原}:\ F9=\{D01..D08\}=\mathbf{8}\ \text{条};\quad F10=\{M01..M08\}=\mathbf{8}\ \text{条}$$ ✓
$$\qquad F9:\ P^*=3\ (D01,D02,D05);\ P_4=4\ (D03,D04,D06,D07);\ U=\mathbf{1}\ (D08)$$ ✓
$$\qquad F10:\ P_2=2\ (M05,M08);\ P_4=1\ (M07);\ U=\mathbf{5}\ (M01,M02,M03,M04,M06)$$ ✓
$$\textbf{先生族表}: F9\ N=9,\ U=2;\quad F10\ N=10,\ U=7\ \Longrightarrow\ \text{族表 }N\ \text{列和}=103,\ U\ \text{列和}=44$$ ⚠️
$$\Longrightarrow\ \boxed{F9\ N=8\ (U=1);\quad F10\ N=8\ (U=5)};\ \text{修正后 }N\ \text{和}=100\ \checkmark,\ U\ \text{和}=41\ \checkmark$$ ✓✓
$$\text{主状态合计 }7+17+14+4+17+41=100\ \text{不受影响}$$ ✓
```

## §1 Zone-A（`P4` 密集，10 条）—— 待做甲（四判据硬筛）

```
$$\begin{array}{c|c|c|c|c}
\text{族}&\text{ID}&\text{逐字命题}&\text{主状态}&\text{形态}\\
\hline
F9&D03&\text{给定参数非同构设计个数}&P_4&\texttt{ED}\\
F9&D04&2\text{-(v,k,}\lambda\text{) packing 数表缺口}&P_4&\texttt{FT}\\
F9&D06&\text{给定参数差集存在性小例分类}&P_4&\texttt{EN}\\
F9&D07&\text{Turán 型小超图极值数未收割格}&P_4&\texttt{EX}\\
F11&Mt06&\text{小阶 STS 相关系统自同构群阶分布}&P_4&\texttt{ED}\\
F11&Mt07&\text{Ramsey 型小参数未收割格}&P_4&\texttt{EV}\\
F11&Mt08&\text{小阶拟阵 Tutte 多项式唯一性/反例}&P_4&\texttt{UQ}\\
F5&C06&\text{固定 }n\ \text{下最优码非同构个数}&P_4&\texttt{EV}\\
F5&C07&q\text{-ary 小参数 covering radius 表缺口}&P_4&\texttt{FT}\\
F5&C09&\text{小 }n\ \text{下最小距离的谱（达到者分类）}&P_4&\texttt{SP}\\
\end{array}$$ ✓（\text{形态分布}: \texttt{ED}2,\texttt{FT}2,\texttt{EN}1,\texttt{EX}1,\texttt{EV}2,\texttt{UQ}1,\texttt{SP}1）$$
```

## §2 Zone-B（`U` 密集，**16 条**）—— 待做乙（`U` 拆因）

```
$$\begin{array}{c|c|c|c|c}
\text{族}&\text{ID}&\text{逐字命题}&\text{主状态}&\text{形态}\\
\hline
F10&M01&\text{特定结构矩阵族 }n\le30\ \text{秩亏精确值}&U\ (\texttt{SPEC})&\texttt{EV}\\
F10&M02&\text{参数化族 PSD 阈值精确刻画}&U\ (\texttt{SPEC})&\texttt{EV}\\
F10&M03&n=5\ \text{SNIEP 整谱可实现性完整表}&U&\texttt{EN}\\
F10&M04&\text{小尺寸 (0,}\pm\text{1)-矩阵 rank 分布}&U&\texttt{ED}\\
F10&M06&\text{给定惯性最小秩矩阵计数}&U\ (\texttt{SPEC})&\texttt{EV}\\
F12&Au03&n=5\ \text{布尔函数吸引子计数分布}&U\ (\texttt{SPEC})&\texttt{ED}\\
F12&Au04&\text{小布尔网络暂态长度极值}&U\ (\texttt{SPEC})&\texttt{EX}\\
F12&Au05&\text{小正则网络极限环极值}&U\ (\texttt{SPEC})&\texttt{EX}\\
F12&Au06&\text{特定类 Collatz 型停时记录（有界域）}&U&\texttt{EX}\\
F12&Au07&\text{小自动机最小 DFA 计数（给定语言类）}&U\ (\texttt{SPEC})&\texttt{ED}\\
F12&Au08&\text{给定规则可逆性阈值精确刻画}&U\ (\texttt{SPEC})&\texttt{EV}\\
F1&G01&\text{阶 }n\le512\ \text{中非超可解精确个数与最小反例序列}&U&\texttt{EV}\\
F1&G02&\text{固定 }n\le2000\ \text{下自同构群阶的精确分布}&U&\texttt{ED}\\
F1&G05&\text{小群中 }|H\cap gKg^{-1}|\ \text{的精确分布}&U&\texttt{ED}\\
F1&G06&n\le256\ \text{阶群的生成元对数最小值与达到者分类}&U&\texttt{EX}\\
F1&G08&\text{小阶群特征标表上独立量的极值}&U&\texttt{EX}\\
\end{array}$$ ✓
$$\text{合计 }16\ \text{条}=\ F10\ 5+F12\ 6+F1\ 5;\quad \texttt{SPEC}\ \text{占 }9/16\ (\text{即 }U\ \text{高密度中过半是"规格未闭合"})$$ ✓✓
```

## §3 Zone-C（`F2/F6/F8` 全量，26 条）—— 待做丙（精确参数窗口）

```
$$\begin{array}{c|c|c|c|c}
\text{族}&\text{ID}&\text{逐字命题}&\text{主状态}&\text{形态}\\
\hline
F2&Gr01&n=8\ \text{图的 inertia 集完备表}&U&\texttt{FT}\\
F2&Gr02&n=9\ \text{图的最小秩精确分布}&U&\texttt{ED}\\
F2&Gr03&n=11\ \text{下最大特征值重数极值图分类}&P^*&\texttt{AC}\\
F2&Gr04&\text{三次图 }n\le12\ \text{的 zero forcing number 精确极值}&P^*&\texttt{EX}\\
F2&Gr05&n=9\ \text{下同谱类大小精确分布}&\boxed{C}&\texttt{ED}\\
F2&Gr06&n=9\ \text{下给定 inertia 三元组 (p,q,z) 的存在性完整表}&U&\texttt{EN}\\
F2&Gr07&\text{小阶 rank defect 极值与达到者}&P^*&\texttt{EX}\\
F2&Gr08&n\le10\ \text{下 slope（正则化 Laplacian）取值集合}&U&\texttt{SP}\\
F2&Gr09&\text{小阶图能量极值与唯一性}&P_2&\texttt{EX}\\
F2&Gr10&n\le10\ \text{下给定惯性且极小秩的图的计数}&U&\texttt{EV}\\
F6&Po01&\text{三项式 }x^n\pm x^m\pm1\ \text{的整数根型完整分类（}n\le40\text{）}&U&\texttt{AC}\\
F6&Po02&x^n-1\ \text{在}\ \mathbb F_2\ \text{上按次数分解的精确计数}&\boxed{C}&\texttt{ED}\\
F6&Po03&\text{给定 trace 的不可约多项式计数}&\boxed{C}&\texttt{ED}\\
F6&Po04&\text{次数}\le30\ \text{三项式的 Galois 群分布}&P_2&\texttt{ED}\\
F6&Po05&\text{多项式理想中最小 Hamming 重量}&U\ (\texttt{SPEC})&\texttt{EV}\\
F6&Po06&\text{有限重单位根消去和极小重量分类}&U\ (\texttt{SPEC})&\texttt{AC}\\
F6&Po07&\text{小 }n\ \text{下不可约二项式存在性完整表}&\boxed{C}&\texttt{EN}\\
F6&Po08&\text{给定判别式的整系数多项式计数}&U\ (\texttt{SPEC})&\texttt{EV}\\
F8&R01&\text{EDS 指数集 }|T(S)|>|S|\ \text{的小范围完整分类}&P_2&\texttt{AC}\\
F8&R02&\text{线性递推 mod }m\ \text{周期精确分布}&P^*&\texttt{ED}\\
F8&R03&\text{Fibonacci mod }m\ \text{Pisano 周期计数表缺口}&\boxed{C}&\texttt{FT}\\
F8&R04&\text{给定周期的 }m\ \text{的精确计数}&P_4&\texttt{ED}\\
F8&R05&\text{递推中零和模式极值}&P_2&\texttt{EX}\\
F8&R06&\text{小范围下整除猜想的极小反例}&U\ (\texttt{SPEC})&\texttt{CE}\\
F8&R07&\text{rank of apparition 分布精确统计}&P_4&\texttt{ED}\\
F8&R08&\text{给定参数 }k\text{-正则序列分类小例}&U\ (\texttt{SPEC})&\texttt{AC}\\
\end{array}$$ ✓
```

## §4 待办（照先生的三步）

```
$$\text{甲}\ Zone\text{-}A\ (10\ \text{条}):\ \text{四判据（现成输出／独立缺口／精确性／非纯补格）} \to \{A+,A0,A?,AX\}$$ ✓
$$\text{乙}\ Zone\text{-}B\ (16\ \text{条}):\ U=U_{\rm coverage}\sqcup U_{\rm prop}\sqcup U_{\rm mixed}\sqcup (U\to P?)\sqcup (U\to DROP)$$ ✓
$$\text{丙}\ Zone\text{-}C\ (26\ \text{条}):\ \text{查 }X(n),X(q),X(k),X(r),X(m)\ \text{的\textbf{未覆盖参数窗口}}$$ ✓
$$\textbf{最终}:\ \text{KEEP／WATCH／DROP（\textbf{不选 ACTIVE}）}$$ ✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结 ✓
【边界】 §0 为计数修正（待先生确认）；§1–§3 逐字命题取自 `CANDIDATE-CENSUS-v1.md` ✓
