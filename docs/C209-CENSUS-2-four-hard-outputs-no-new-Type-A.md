已查地图（**先查后写**）：查 `C-208`（CENSUS-1）、`C-206`（模块）、`C-201`（三簇）。回查见 §6 ✓

D0: 本档对象 = **CENSUS-2 最终四项硬输出** ＋ 唐先生对 basin 数据的解读修正 —— 关系 = 方法学校准 ＋ 发现工具定位
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 唐先生的解读修正（2026-09-20 11:34，全盘采纳）

$$\textbf{① basin 数据只叫}\ \boxed{\texttt{CENSUS-2 basin-capture calibration}}✓✓\ —— \textbf{不叫}"basin radius"／"basin volume estimate"✗$$
$$\qquad \Longrightarrow \text{唯一稳健结论}：\boxed{\text{局部 basin-capture 随距离单调下降，且在}\ 3\times10^{-2}\ \text{内仍有显著捕获率}}✓$$
$$\textbf{② 禁止外推}✗✗：\text{全局 basin 体积}✗；\text{体积分数}\sim10^{-5}✗；\text{"800 次必然漏掉}\ x_0\text{"✗；\text{其他两个 Type-A 的 basin 更大}✗$$
$$\qquad （\text{这三条都需要【另外设计的全域测量】}✓；本档前一条消息中的相关推断}\ \textbf{已撤回}✓✗）$$
$$\textbf{③ census 的定位}：\boxed{\text{发现工具，不是穷尽性证明}}✓✓$$
$$\textbf{④ 分类入口锁死}：\boxed{|A|=4\quad\wedge\quad\mathrm{rank}\,\Delta=3\quad\wedge\quad c>0}✓✓$$
$$\qquad \text{单凭 NM 能下降／"看起来像局部极小"}\ \textbf{不再作为认证依据}✗（\text{只能叫 numerical stagnation}✓）$$

## §1 CENSUS-2 basin-capture calibration

| $r$ | 捕获 $x_0$ 比例 | 起算点数 |
|---|---|---|
| $3\times10^{-3}$ | $62.7\%$ | $251/400$ |
| $10^{-2}$ | $61.5\%$ | $246/400$ |
| $3\times10^{-2}$ | $54.0\%$ | $216/400$ |
| $10^{-1}$ | $23.0\%$ | $92/400$ |
| $3\times10^{-1}$ | $4.0\%$ | $16/400$ |

$$\text{起点}：\text{均匀落在}\ B(x_0,r)\ \text{内}✓；\text{判据}：\text{精修后}\ |F-0.7640811032|<10^{-6}✓$$
$$\qquad \textbf{注意}：\text{这是【条件捕获率】}✓，\text{不是体积占比}✗；\text{球外 basin 形状未知}✓$$

## §2 ⭐ CENSUS-2 最终四项硬输出（唐先生指定）

$$\textbf{①} S_3\ \text{去重后的轨道数}：\text{全部}\ \mathbf{723}\ \text{个}✓\qquad \textbf{②}\ F<0.78\ \text{的轨道数}：\mathbf{60}\ \text{个}✓$$
$$\textbf{③}\ \textbf{真正 Type-A 的数量}：\mathbf{3}\ \text{个}✓✓（\text{入口判据}\ |A|=4\wedge\mathrm{rank}\Delta=3\wedge c>0✓）$$
$$\textbf{④}\ \textbf{是否出现新的 active set／新候选}：\boxed{\textbf{没有}}✗✓✓$$
$$\qquad \text{四个}\ c>0\ \text{条目中，第 4 条经核实为【重复】}✗：$$

| 条目 | $F$ | $A$ | $\mathrm{rank}$ | $c$ | $\varphi/\pi$ | 判定 |
|---|---|---|---|---|---|---|
| 0 | $0.7640811008$ | $\{1,5,11,13\}$ | 3 | $0.540247976$ | $(0.11584426,\ 0.33188742,\ 0.73557644)$ | **Type-A ✓**（= 簇 0） |
| 1 | $0.7755338917$ | $\{2,7,10,15\}$ | 3 | $1.218503803$ | $(0.63276145,\ 0.83500219,\ 0.94378950)$ | **Type-A ✓**（= 簇 3） |
| 2 | $0.7755405405$ | $\{2,7,10,15\}$ | 3 | $1.218509574$ | $(0.63276122,\ 0.83500193,\ 0.94378928)$ | **重复 ✗**（$d=1.284\times10^{-6}$ 同一轨道 ✓） |
| 3 | $0.7768817151$ | $\{1,3,13,15\}$ | 3 | $0.750466653$ | $(0.11240005,\ 0.42461340,\ 0.62961738)$ | **Type-A ✓**（= 簇 5） |

$$\textbf{重复判定的依据}：\text{条目 2 与条目 1 的}\ A\ \textbf{完全相同}✓；\text{模}\ S_3\ \text{距离}\ d=1.284\times10^{-6}✓；$$
$$\qquad \text{二者}\ k\ \text{的共同激活 gap 差异极大}（\text{条目 1 的}\ k{=}2\ \text{gap}=2.55\times10^{-15}✓\ \text{vs 条目 2 的}\ 9.59\times10^{-6}✓） \Longrightarrow \text{条目 2 只是收敛未到位}✓$$
$$\qquad \textbf{其余 57 个轨道}：|A|\in\{2,3\}✓,\ c=\text{None}✓ \Longrightarrow \text{非 KKT} \Longrightarrow \textbf{非局部极小}✓（\text{numerical stagnation}✓）$$
$$\qquad \qquad \text{active set 只出现}\ \{1,5\}\{1,5,11\}\{1,11,13\}\{1,13,15\}\{3,13,15\}\{1,3,13\}\ \text{等【子集型】}✓ \Longrightarrow \text{无新结构}✗✓$$

## §3 ⭐ 结论（唐先生指定的措辞）

$$\boxed{\ \text{在本次}\ 3000\text{-start、均匀随机初始化、Nelder-Mead 精修、}\ c\text{-分类协议下，}\textbf{未发现新的 Type-A 轨道}✓✓\ }$$
$$\qquad \textbf{而【不是】}"已经穷尽全部极小构型"✗✗$$
$$\qquad \Longrightarrow \text{当前}\ \mathcal M_{\rm cand}\ \text{中已认证的 Type-A 轨道仍为【3 个】}✓（A_0,\ A_3,\ A_5✓），\text{三者的严格局部孤立性见}\ \texttt{C-206}／\texttt{C-207}✓✓$$

## §4 顺带发现（廉价改进机会）

$$\text{CENSUS-2 给出的簇 0 数值点}\ F_{\rm float}=0.7640811008✓\ \textbf{略低于} \text{我们已认证的上界}\ 0.76408110090337578✓（\text{差}\approx1.03\times10^{-10}✓）$$
$$\qquad \text{原因}：\mathrm{DEN}=10^{10}\ \text{的有理化把每坐标扰动}\sim10^{-10}✓ \Longrightarrow \text{更细分母可再降上界}✓（\text{廉价}✓）$$
$$\qquad ⚠️\ \text{但这是【浮点】，不是证书}✗；\text{若要收紧账本须重做区间认证}✓$$

## §5 边界

- 四项硬输出为**协议内**结论 ✓；**不构成穷尽性** ✗✗（唐先生明确要求不得如此写 ✓）
- $c$ 用 facet 法（数值版 ✓）；判据入口 $|A|=4$ 的容差取 $10^{-5}$ ✓
- §1 的捕获率为**条件比率** ✓；**不解释为** basin 体积／体积分数／必然性 ✗
- 本次**未**发现新 active set ✓；但**不**排除在其它初始化分布／其它优化器下会出现的可能 ✗
- **未用** RH；**未改** 他档（`C-208` 的 basin 表述以本档 §0 为准 ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 basin捕获校准 命中文件数=1    ::  ./C209-CENSUS-2-four-hard-outputs-no-new-Type-A.md
技术词 条件捕获率    命中文件数=1    ::  ./C209-CENSUS-2-four-hard-outputs-no-new-Type-A.md
技术词 协议内结论    命中文件数=1    ::  ./C209-CENSUS-2-four-hard-outputs-no-new-Type-A.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 下一步（待唐先生定；**不**提前开全域 B&B ✓）

$$\textbf{(甲)}\ \text{收紧上界（廉价）}：\text{用更细分母重新有理化 CENSUS-2 的簇 0 点}✓ \Longrightarrow \text{账本上界可再降}\sim10^{-10}✓$$
$$\textbf{(乙)}\ \text{换初始化分布再跑 census}✓（\text{检验"新 active set"结论对协议是否稳健}✓）$$
$$\textbf{(丙)}\ \text{转 certified global cover} ✗（\text{须唐先生明确批准后才开}✓）$$
