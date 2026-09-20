已查地图（**先查后写**）：查 `C-206`（局部刚性模块）、`C-207`（乙-4）、`C-201`（三簇分类）、`C-199`／`C-200`（T13-B2）。回查见 §7 ✓

D0: 本档对象 = **乙-4 判 PASS** ＋ **两处措辞修正**（唐先生 11:23）＋ **GLOBAL-CENSUS-1**（候选穷尽性搜索第一刀，含两个关键发现）—— 关系 = 结构定位 ＋ 方法学更正
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 乙-4 正式判 PASS ＋ 措辞修正（唐先生 2026-09-20 11:23）

$$\boxed{\ \textbf{三个 Type-A 候选轨道均为孤立的严格局部极小构型，且不存在穿过它们的局部连续极小族}\ }✓✓$$

$$\textbf{措辞修正 ①}：\text{"一阶可行集为单点"}✓ \Longrightarrow \text{须限定为}\ \boxed{\text{一阶零方向／KKT 可行结构为单点}}✓✓\ —— \textbf{不得} \text{误解为整个非线性优化问题的可行集只有一个点}✗$$
$$\textbf{措辞修正 ②}：\text{"有限个 Type-A 轨道"}✗ \Longrightarrow \boxed{\text{"当前数值搜索发现有限个 Type-A 轨道，其中三个已完成严格局部孤立性认证"}}✓✓$$
$$\textbf{禁止扩大}：\textbf{不得} \text{写作"全部极小构型只有这三个"}✗✗（\text{无此结论}✓）$$

## §1 GLOBAL-CENSUS-1（第一刀，探索性）

$$\text{设计}：60^3\ \text{网格布种} ＋ 800\ \text{随机起点} \to \text{Nelder-Mead 精修} \to \text{合并}\ S_3\ \text{轨道} \to \text{active-set 分类}✓$$

$$\textbf{⚠️ 网格布种【完全失效】}✗：60^3=216{,}000\ \text{格点中}\ F<0.78\ \text{者}=\mathbf{0}✓（\text{网格最小值}\ 0.831735✓）$$
$$\qquad \Longrightarrow \text{极小点盆地在参数空间【极窄】}✓✓ \Longrightarrow \text{本刀退化为 800 随机起点}✗$$

$$\text{结果}：F<0.78\ \text{的轨道}\ 26\ \text{个}✓（\text{清单}\ \texttt{/tmp/census1.json}✓）$$

## §2 ⭐ 关键发现 ①：搜索【不可靠】

$$\text{已知三轨道在 census 中的命中}：$$
$$\qquad \text{簇 3（}0.7755338917\text{）}✓\ \text{精确命中（\#5}✓）\qquad \text{簇 5（}0.7768817151\text{）}✓\ \text{精确命中（\#12}✓）$$
$$\qquad \text{簇 0（}\mathbf{0.7640811}\text{，全局最佳）}✗\ \textbf{未命中}✓\ —— \text{只到}\ 0.7640885✓（\text{高}\ 7.4\times10^{-6}✓）\text{的伪点}✗✗$$
$$\qquad \Longrightarrow \boxed{\ \text{800 随机起点【不足以】覆盖候选集}✓✓\ } \Longrightarrow \textbf{搜索式 census 不能作为穷尽性依据}✗✗$$
$$\qquad \text{（自我失误：首版判据用}\ |\Delta F|<10^{-4}\ \text{比对⟹报出假的"3/3 命中"✗，容差须}\ \le10^{-6}✓）$$

## §3 ⭐ 关键发现 ②：我的"局部极小验证"方法错了

$$\text{首版用}\ \textbf{Nelder-Mead 下降检验}✗（\text{"再精修后是否下降"}\text{）判定局部极小}✓$$
$$\qquad \text{census \#4}：F=0.770013692✓,\ A=\{1,5,13\}✓,\ |A|=3✓,\ \text{曾判"真极小(非A)"}✗$$

$$\textbf{反例（直接测）}：\text{取}\ w\perp\mathrm{span}\{\nabla S_k-\nabla S_{k_1}\}✓（\text{即三点投影相同方向}✓）：$$
$$\qquad \langle\nabla S_k,w\rangle=(-0.73989165,\ -0.73989165,\ -0.73989165)✓\ \forall k\in A \Longrightarrow \text{一阶导数}<0✓$$
$$\qquad F(x+t w)-F(x)\ \approx\ -0.7399\,t\ <\ 0✓（t=10^{-5}\to-7.40\times10^{-6}✓；t=3\times10^{-3}\to-2.22\times10^{-3}✓）$$
$$\qquad \Longrightarrow \textbf{#4 不是局部极小}✗✗；\text{Nelder-Mead 只是【停滞】}✓（\text{误报下降}=8.3\times10^{-15}✓）$$
$$\qquad \text{结构性原因}：\nabla S_k\ \text{的奇异值}=(21.08,\ 7.35,\ 0.84)✓ \Longrightarrow \text{三点线性无关}✓ \Longrightarrow \mathbf{0\notin\mathrm{conv}}✓$$

$$\Longrightarrow \boxed{\ \textbf{可靠判据} = c:=\min_{\|u\|=1}\max_{k\in A}\langle\nabla S_k,u\rangle\ \textbf{的符号}✓✓\ \text{（即 KKT/covering 条件）}\ }$$
$$\qquad c>0\Rightarrow \text{局部极小（含刚性}✓）；\ c<0\Rightarrow \textbf{存在下降方向，非极小}✓；\ c\approx0\Rightarrow \text{退化，须单独处理}⚠️$$
$$\qquad ⚠️\ \text{本档同时解释}\ \texttt{C-201}\ \text{遗留的"簇 4 存疑（KKT 失败但精修不降）"}✓：\textbf{同一现象}✓ —— \text{它不是极小}✓$$

## §4 T13-A 当前状态块（唐先生指定格式）

$$\boxed{\ 0.76\ \le\ m_3\ \le\ 0.764081100903\ldots\ }✓$$
$$\boxed{\ \begin{array}{c} \text{当前数值搜索发现有限个 Type-A 轨道}✓\\ \downarrow\\ \text{其中 3 个已完成严格局部孤立性认证}✓\\ \downarrow\\ \text{连续极小族在这 3 处已排除}✓\\ \downarrow\\ \textbf{全局穷尽性仍未证明}✗ \end{array}\ }✓$$

## §5 保留的校验样本

$$\text{三个已认证 Type-A 轨道}：A_0=\{1,5,11,13\}✓,\ A_3=\{2,7,10,15\}✓,\ A_5=\{1,3,13,15\}✓\ \text{（值}\ 0.7640811／0.7755339／0.7768817✓）$$
$$\text{伪簇样本（非极小，}c<0\ \text{或}\ |A|<4✓）\text{：}0.7640885✓,\ 0.7641923✓,\ 0.7647698✓,\ 0.7700137✓,\ 0.7769\sim0.7773\ \text{一族}✓$$
$$\qquad \Longrightarrow \text{作 CENSUS-2 与将来全局证书的【校验样本】}✓✓$$

## §6 边界

- CENSUS-1 为**探索性**✓：$\mathrm{NM}$ 起点数有限 ✓、$F<0.78$ 阈值人为 ✓ ⟹ **不构成穷尽性结论** ✗✗
- §3 的反例是**直接数值验算**✓（非证明 ✓）；但它足以证明"NM 下降检验"**不可作为判据** ✓✓
- ⚠️ 本档**不**声称 $m_3$ 精确值 ✗；**不**声称只有 3 个极小 ✗
- **未用** RH；**未改** 他档 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 候选穷尽性搜索 命中文件数=1    ::  ./C208-T13A-YI4-PASS-global-census-1.md
技术词 KKT判据符号    命中文件数=1    ::  ./C208-T13A-YI4-PASS-global-census-1.md
技术词 停滞误报       命中文件数=1    ::  ./C208-T13A-YI4-PASS-global-census-1.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 本档自我失误

$$\textbf{① 容差过宽}：\text{命中判据用}\ 10^{-4}✗ \Longrightarrow \text{假"3/3 命中"}✗ \Longrightarrow \text{改为}\ 10^{-6}✓$$
$$\textbf{② 判据错误}：\text{用 NM 下降检验判局部极小}✗ \Longrightarrow \text{漏掉}\ 0\notin\mathrm{conv}\ \text{的伪点}✗ \Longrightarrow \text{改用}\ c\ \text{符号}✓✓（§3）$$
$$\textbf{③ 网格布种假设错}：\text{以为低网格点可作种子}✗ \Longrightarrow F<0.78\ \text{格点为 0}✗（盆地在网格尺度下不可见}✓）$$
$$\qquad \Longrightarrow \text{①–③ 全为实现/方法错，非数学错}✓（\text{第}\ 25\text{–}27\ \text{次同类应验}）✓$$

## §9 下一步

$$\textbf{CENSUS-2 已启动}✓（3000\ \text{起点}✓；\textbf{用}\ c\ \text{判据分类}✓；\text{并直接估计}\ x_0\ \text{盆地半径}✓）$$
$$\qquad \text{目标}：\text{① 给}\ \mathcal M_{\rm cand}\ \text{一个更可信的清单}✓；\text{② 量化"搜索难度"}✓（\text{盆地半径}✓）$$
$$\qquad \text{随后（待唐先生定）}：\text{是否启动}\ \textbf{真正的全局区间覆盖}✓（\text{局部刚性球内豁免} ＋ \text{补集 B&B}✓）$$
