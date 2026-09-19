已查地图（**先查后写**）：`C-156`（单调性归约；本档**撤回其 §3 的"10 倍改进"动机表述**）、`C-155`／`C-154`／`C-153`（`M\le3`）、`C-152`／`C-151`、`E4-ENGINE-1/4`（引理 C；Montgomery 1/20）、`papers/palojarvi-constant/note.md` §3（`m\ge2` 自足缺口）、本地 `docs/Palojarvi-2019-tau-Li-explicit-zero-free.pdf` p.6。关键词回查：`阻尼情形`=0、`新增窗口段`=0、`小周期引理`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:26 三条）**：**① 归约基点澄清 ② 逐字核对 "10 倍改进" ③ 试"新增窗口段"切入点。**
**结论（先行）**：$$\textbf{(一)}\ ⚠️\ \textbf{逐字核对发现}\ \textbf{不匹配}：\text{Lemma 2.2}\ \text{的模长条件是}\ \max_j|z_j|=1（\textbf{含阻尼}），$$
$$\qquad (\text{RP}_M)\ \text{要求}\ \textbf{所有}\ |z_j|=1 \Longrightarrow (\text{RP}_M)\ \textbf{只锐化无阻尼子情形}，\ \text{不是整条引理的}\ 10\ \text{倍改进}✓✓$$
$$\qquad \Longrightarrow \textbf{撤回}\ \text{`C-156` §3 的动机表述（"(\text{RP}_M) 对所有}\ M\ \text{即可补上}\ m\ge2\ \text{缺口"}\ \textbf{不成立}）✓✓$$
$$\textbf{(二)}\ \text{归约基点澄清（唐先生指出）：}\text{若单调性只对}\ M\ge2\ \text{可证} \Longrightarrow \text{归纳从}\ M=2\ \text{起}，\ M=1\to2\ \textbf{单独验证}✓✓$$
$$\qquad (\text{因}\ M=1\ \text{退化}：\text{窗口}\ [1,5]\ \text{与}\ [1,10]\ \text{结构不同}；\ \text{且}\ m_1=m_2\ \text{持平而非严格增})✓$$
$$\textbf{(三)}\ ⭐\ \textbf{唐先生建议的"新增窗口段"}\ \textbf{5/5 应验}：\text{`M=3..7` 的最大值}\ \textbf{全部落在} [5(M-1)+1,\ 5M]✓✓$$
$$\qquad (\text{如}\ M=3:0.7816@k=13；\ M=4:0.8424@k=17；\ M=5:1.0304@k=23；\ M=6:1.1888@k=27；\ M=7:1.3665@k=31)✓✓$$
$$\textbf{(四)}\ ⭐\ \textbf{新增可证引理（小周期情形）}：\text{若旧}\ M\ \text{点的共同周期}\ P\le5(M+1)，\ \text{则新配置在}\ k=P\ \text{的和}=M+\cos(P\varphi_{M+1})\ge M-1✓✓$$
$$\qquad \Longrightarrow M\ge2\ \text{时}\ \ge1\ \ge\tfrac12 \Longrightarrow \text{单调性在该情形}\ \textbf{成立}✓✓$$
$$\textbf{(五)}\ ⭐\ \textbf{阻尼情形实算（本档新增）}：d_M=0.395/0.373/0.363\ (M=2,3,4)\ \gg\tfrac1{20}✓✓$$
$$\qquad \Longrightarrow \textbf{正确的靶子}\ \text{是}\ \textbf{阻尼版}\ (\text{RP}_M)，\ \text{而它仍有}\ \approx7\text{–}8\times\ \text{改进空间}✓✓$$

FREEZE-ACK: 本档即冻结期内的逐字核对、撤回与实算（依 `§8.1`；不产候选结论）

D0: 本档对象 = **Lemma 2.2 逐字核对（模长不匹配）＋ 对该动机表述的撤回 ＋ 新增窗口段实算 ＋ 小周期引理 ＋ 阻尼情形实算** —— 关系 = 核对与撤回，非新机制
D1: 0

# C-157 · ⚠️ **逐字核对发现不匹配；撤回"10 倍改进"；新增窗口段建议 5/5 应验**

> **唐先生 2026-09-19 13:26**：① 归约基点 ② 逐字核对"10 倍" ③ "新增窗口段"切入点 ✓

---

## §1 ⭐ 逐字核对（本地 PDF `docs/Palojarvi-2019-*.pdf` p.6）

$$\textbf{Lemma 2.2（逐字）}：\text{"Let}\ M\ge1\ \text{be an integer and let}\ z_1,\dots,z_M\ \text{be complex numbers which satisfy the condition}$$
$$\qquad \max_j|z_j|=1.\ \text{Then}\quad \max_{1\le n\le5M}\ \Re\Big(\sum_{j=1}^{M}z_j^n\Big)\ \ge\ \frac1{20}.\text{"}✓✓$$
$$\textbf{应用处（逐字）}：\tfrac{\rho_j}{\rho_j-\tau}=R'r_j\exp(\varphi_j i)，0\le r_j\le1 \Longrightarrow z_j=r_j^N e^{N\varphi_j i}✓$$
$$\begin{array}{c|c|c}
\text{项目} & \text{Lemma 2.2} & (\text{RP}_M)\\\hline
\text{窗口} & 1\le n\le5M & 1\le k\le5M\quad ✓\text{一致}\\
\text{求和下标} & j=1..M & j=1..M\quad ✓\text{一致}\\
\text{模长条件} & \max_j|z_j|=1\ (\textbf{允许}\ |z_j|<1) & \textbf{所有}\ |z_j|=1\\
\text{结论} & \Re\sum z_j^n\ge\tfrac1{20} & \Re\sum z_j^k\ge\tfrac12\\
\end{array}✓✓$$
$$\Longrightarrow \text{两者}\ \textbf{作用域不同}：(\text{RP}_M)\ \text{只是}\ \text{Lemma 2.2}\ \text{在}\ \textbf{"全部模长}=1"\ \text{子情形上的锐化}✓✓$$

## §2 ⚠️ 撤回（对 `C-156` §3）

$$\text{`C-156` §3 写："}(\text{RP}_M)\ \text{即把常数}\ \tfrac1{20}\ \text{提到}\ \ge\tfrac12（10\ \text{倍以上锐化）"}\ \Longrightarrow \textbf{表述过强，撤回}✓$$
$$\qquad \text{理由：应用处}\ z_j=r_j^N e^{N\varphi_j i}\ \text{含}\ r_j<1 \text{（阻尼）} \Longrightarrow \text{需要}\ \textbf{阻尼版}；\ (\text{RP}_M)\ \textbf{不蕴含}\ \text{Lemma 2.2}✓✓$$
$$\text{故}\ \text{`C-156` §3 的动机句"}(\text{RP}_M)\ \text{对所有}\ M\ \text{即可补上}\ m\ge2\ \text{自足缺口"}\ \textbf{不成立}✓$$
$$\textbf{正确表述}：(\text{RP}_M)\ \text{锐化}\ \text{Lemma 2.2}\ \text{的}\ \textbf{无阻尼子情形}；\ \text{要补缺口需}\ \textbf{阻尼版}✓✓$$
$$\qquad (\text{与本项目}\ \texttt{papers/palojarvi-constant/note.md}\ §3\ \text{已标"modulus comparability"缺口}\ \textbf{自洽}✓)$$

## §3 归约基点澄清（唐先生第一问）

$$\text{唐先生：}m_1=\tfrac12\ \text{单独即可归纳出全}\ M \Longrightarrow \text{为何还列}\ m_2=\tfrac12？✓$$
$$\textbf{答}：\text{因}\ M=1\ \text{是}\ \textbf{退化情形} \Longrightarrow \text{单调性}\ m_{M+1}\ge m_M\ \text{很可能只能在}\ M\ge2\ \text{建立}✓$$
$$\qquad \text{证据：}m_1=m_2\ \textbf{持平}（\text{非严格增}）\Longrightarrow M=1\to2\ \text{这一步}\ \textbf{不属一般单调性}✓$$
$$\qquad \text{且窗口结构不同}：M=1\ \text{时}\ k\le5；\ M=2\ \text{时}\ k\le10，\ \text{两点在}\ k\ \text{上的干涉结构是新的}✓$$
$$\Longrightarrow \textbf{正式版写法}：\text{"归纳从}\ M=2\ \text{开始}，M=1\to2\ \text{单独验证（即定理 1）"}✓✓$$

## §4 ⭐ "新增窗口段"建议（唐先生第三问）

$$\text{建议（唐先生）：}\text{把归纳局部化到}\ \textbf{新增段}\ [5M+1,\ 5M+5]，\ \text{而非让新点竞争整个旧窗口}✓$$
$$\textbf{实算（本档）}：\text{对}\ M=3..7\ \text{的极小点配置，总最大值的}\ \textbf{位置}：$$
$$\begin{array}{c|r|c|l}
M & \max_k h(k) & \arg\max\ k & \text{是否落在新增段}\ [5(M-1)+1,5M]\\\hline
3 & 0.7816 & 13 & ✓\\
4 & 0.8424 & 17 & ✓\\
5 & 1.0304 & 23 & ✓\\
6 & 1.1888 & 27 & ✓\\
7 & 1.3665 & 31 & ✓\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{5/5 应验} \Longrightarrow \text{"新窗口段是新点争取的空间"这一直觉}\ \textbf{实测成立}✓✓$$

$$\text{但精确化后，}M=1\ \text{的充分条件太强：}\text{需}\ \max_{[5M+1,5M+5]}\sum_{j\le M}\cos(k\varphi_j)\ \ge\ m_M+1✓$$
$$\qquad \text{（因新点贡献}\ \ge-1）。\ \text{实测：新增段上的 max}\ \approx m_M\ \textbf{而非}\ m_M+1 \Longrightarrow \textbf{该充分条件不成立}✓✓$$
$$\qquad \Longrightarrow \text{单调性仍需}\ \textbf{联合控制} \text{（不能把"旧点表现"与"新点贡献"完全分开）}✓✓$$

$$\textbf{但本档得到一条}\ \textbf{可证引理}（\text{小周期情形}）：$$
$$\qquad \text{若旧}\ M\ \text{点有共同周期}\ P（\text{即}\ P\varphi_j\in2\pi\mathbb Z\ \forall j）\ \text{且}\ P\le5(M+1)，\ \text{则在}\ k=P：$$
$$\qquad \sum_{j\le M}\cos(P\varphi_j)+\cos(P\varphi_{M+1})=M+\cos(P\varphi_{M+1})\ \ge\ M-1✓✓$$
$$\qquad \Longrightarrow M\ge2\ \text{时}\ \ge1>\tfrac12 \Longrightarrow \textbf{该情形单调性成立}✓✓$$
$$\qquad \text{（余下情形：}\textbf{无小周期} \text{（无理／大分母）} \Longrightarrow \text{需 Turán 型定量输入}✓)$$

## §5 ⭐ 阻尼情形实算（本档新增；决定"正确的靶子"）

$$d_M:=\min\Big\{\max_{k\le5M}\Re\sum_j r_j^k e^{ik\varphi_j}\ :\ 0\le r_j\le1,\ \max_j r_j=1\Big\}✓$$
$$\begin{array}{c|r|r|l}
M & d_M\ (\text{实算}) & m_M\ (\text{无阻尼}) & \text{极小点}\ r\\\hline
2 & +0.395472 & 0.500 & (1.000,\ 0.751)\ \varphi=(29.6^\circ,\ 129.1^\circ)\\
3 & +0.373092 & 0.764 & (0.830,\ 0.791,\ 1.000)\\
4 & +0.363430 & 0.842 & (1.000,\ 0.835,\ 0.820,\ 0.873)\\
\end{array}✓✓$$
$$\Longrightarrow \text{① 阻尼确实}\ \textbf{显著压低} \text{（}0.36\text{–}0.40\ \text{vs}\ 0.50\text{–}0.84）⟹ (\text{RP}_M)\ \textbf{不能} \text{推阻尼版}✓✓$$
$$\Longrightarrow \text{② 但}\ d_M\ \textbf{仍}\ \gg\tfrac1{20} \text{（约}\ 7\text{–}8\times\text{）} \Longrightarrow \textbf{阻尼版本身仍是可观的改进}✓✓$$
$$\qquad \text{③ 阻尼极小点}\ r_j\ \textbf{都较大}（0.75\text{–}1.0）⟹ \text{不是"单点主导"，而是}\ \textbf{多项近单位} \text{配置}✓$$
$$\qquad \text{④ 趋势}：d_2=0.395>d_3=0.373>d_4=0.363 \Longrightarrow \text{推测}\ \lim_M d_M\ \text{为某绝对常数}\ \approx0.35✓$$

## §6 下一步

$$\text{①}\ \textbf{正确靶子改写}：\text{从}(\text{RP}_M)\ \text{改为}\ \textbf{阻尼版}(\text{RP}^{\text{damp}}_M)（\text{才与}\ \text{Palojärvi}\ \text{应用对得上}）✓✓$$
$$\text{②}\ \text{单调性：}\text{用"新增窗口段"作为}\ \textbf{组织框架}，\ \text{在"小周期"情形已可证}✓；\ \text{余下情形需 Turán 型定量输入}✓$$
$$\text{③}\ \text{把}\ (\text{RP}^{\text{damp}}_M)\ \text{的常数做实}（\text{目标}\ \ge\tfrac13\ \text{即已是}\ 6.7\times\ \text{改进}）✓$$

## §7 边界与回查

- ⚠️ §1 为**本地 PDF 逐字抽取**（p.6）；应用处 `z_j` 形式亦逐字 ✓
- ⚠️ §4／§5 的数值为**实算**（`differential\_evolution`＋`Nelder–Mead`）；`d_M` 为**上界**（可能是局部最优）✓
- ⚠️ §4 的"5/5 应验"基于 `C-156` 的极小点（数值上界，非全局最优）⟹ **现象级证据**，非定理 ✓
- ⚠️ **撤回** `C-156` §3 的动机表述（已在原档追加撤回指针）✓
- ⚠️ **不声称** 阻尼版成立；**不声称** 一般 `M`；**不声称** 与 RH 有关 ✓
- **未用** RH；**未改**任何原档（仅追加撤回指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:4x）`[纪律]`（先跑后写）

```
技术词 阻尼情形    命中文件数=0 ::  ⟹ 本档新增
技术词 新增窗口段  命中文件数=0 ::  ⟹ 本档新增
技术词 小周期引理  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
