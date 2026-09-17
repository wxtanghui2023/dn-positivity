# （i）-1 · **无条件聚合**：靶子确认 ＋ GM 定理**窗口的独立推导**

> 依唐先生 11:36「继续」｜执行 `V293` 留下的选项 **(i)**（＝无条件化机制 B 的预算输入；＝前沿 §7.2(e) 的 $T^{1/3}$ 缺口）✓
> **纪律**：沿用 `STRATEGY` §5／§6（不做常数优化；不以"又关掉一条路"为战绩）✓

---

## 1. ⭐ 靶子（我方档案逐字，两处独立登记）

$$\text{前沿 §7.2(e) 逐字}（`A3-third-moment-barrier.md`）：\ \text{"The prime-side evaluation of}\ \mathrm{tr}\tilde G^k\ \text{by the diagonal method}（\text{multiplicative relations among}\ k\ \text{prime powers, Montgomery--Vaughan for the rest}）\ \text{is available}\ \textbf{exactly in the Rudnick--Sarnak range}\ X^k\le T^{2-\varepsilon};\ \text{at}\ X\asymp T\ \text{this allows only}\ k=1.\ \text{Thus, unconditionally, higher moments add nothing."}✓✓$$
$$\text{我方登记的目标}（`A3-break-682-attempt.md` L103 逐字）：$$
$$\qquad \boxed{\text{必须无条件地证明三阶矩——即在}\ X\asymp T\ \text{处无条件求值}\ \mathrm{tr}\tilde G^3\ \text{的素数侧对角和}（\text{＝无条件化 Hejhal 1994／RS 1996 的三点相关}，\text{＝把 Montgomery 型 form factor 从 Fourier 支撑}\ 1\ \textbf{推到支撑}>1）}✓✓✓$$
$$\text{缺口的精确量}：X\ \text{范围}\ T^{2/3-\varepsilon}\to T\ \Longrightarrow \textbf{因子}\ T^{1/3}；\ \text{等价地}\ X^3\le T^2\to T^3\ (\textbf{因子}\ T)✓✓$$

## 2. ⭐ GM 主定理（**原文本地，逐字**）`external_refs/guth_maynard_2405.20552.txt`

$$\textbf{Theorem 1.1（Large values estimate）}：|b_n|\le1,\ (t_r)_{r\le R}\ 1\text{-separated in }[0,T],\ \big|\sum_{N}^{2N}b_nn^{it_r}\big|\ge V\ \forall r$$
$$\qquad\Longrightarrow\ \boxed{R\le T^{o(1)}\Big(N^2V^{-2}+N^{18/5}V^{-4}+TN^{12/5}V^{-4}\Big)}✓✓$$
$$\textbf{经典对照（其 (1.1)，MVT＋Montgomery--Halász--Huxley）}：\ R\le T^{o(1)}\Big(N^2V^{-2}+T\min\big(NV^{-2},\ N^4V^{-6}\big)\Big)✓$$
$$\text{GM 自述}：\text{旧结果在}\ V<N^{7/10}\ \text{或}\ V>N^{8/10}\ \text{时至少一样强；}\ \textbf{GM 严格更强} \text{于两者之间}（\text{临界}\ V\sim N^{3/4}）✓$$

## 3. ⭐⭐⭐ **本档新得：窗口＝两条交叉线的交点（独立推导）**

$$\text{GM 的两项新贡献各自只在}\ \textbf{一侧} \text{胜过经典：}$$
$$\text{(a) 无}\ T\ \text{项}：\ N^{18/5}V^{-4}\ \text{vs 经典}\ N^2V^{-2}\ \Longrightarrow\ \text{相等}\iff N^{8/5}=V^2\iff \boxed{V=N^{4/5}=N^{8/10}}✓✓$$
$$\text{(b) 含}\ T\ \text{项}：\ TN^{12/5}V^{-4}\ \text{vs 经典}\ T\cdot NV^{-2}\ \Longrightarrow\ \text{相等}\iff N^{7/5}=V^2\iff \boxed{V=N^{7/10}}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{GM 的改进窗口}\ \textbf{恰为}\ N^{7/10}\lesssim V\lesssim N^{8/10}}✓✓✓$$
$$\qquad(\textbf{独立推出}，\text{与 GM 自己的那句话}\ \textbf{逐字吻合}：N^{7/10}\to N^{8/10}✓✓)$$
$$\text{交点处}\ \textbf{恰好打平}：V=N^{7/10}\ \text{时两端项均为}\ TN^{-2/5}\ (\text{由}\ NV^{-2}=N^{1-7/5}=N^{-2/5}，\ TN^{12/5}V^{-4}=TN^{12/5-14/5}=TN^{-2/5})✓$$
$$\qquad V=N^{8/10}\ \text{时}\ N^{18/5}V^{-4}=N^{18/5-16/5}=N^{2/5}=N^2V^{-2}✓✓$$

## 4. ⭐⭐ 由此得到的**精确缺口规格**（本档产出）

$$\text{GM 的机器是一台}\ \textbf{窗口机器}：\text{只在}\ V/N^{3/4}\in[N^{-1/20},N^{1/20}]\ \text{内改进}✓$$
$$\text{而三阶矩在}\ X\asymp T\ \text{处所需的（}N,V\text{）落在何处}——\textbf{尚无我方推导}✓$$
$$\Longrightarrow\ \boxed{\textbf{决定性待查}：\text{在}\ \mathrm{tr}\tilde G^3\ @\ X\asymp T\ \text{的归约中，（}N,V\text{）落在哪个区间？是否落在}\ N^{7/10}\lesssim V\lesssim N^{8/10}\ \text{内？}}✓✓✓$$
$$\qquad\text{若}\ \textbf{落在窗口内} \Longrightarrow \text{GM 型输入}\ \textbf{可能} \text{直接补上}\ T^{1/3} \Longrightarrow (\text{i})\ \text{有戏}✓✓$$
$$\qquad\text{若}\ \textbf{落在窗口外} \Longrightarrow \text{GM}\ \textbf{给不出} \text{缺口}；\ \text{须}\ \textbf{新的} \text{大值定理}（\text{瞄准矩问题、非密度问题}）✓$$

## 5. ⚠️ 已登记的反向证据（**不得忽略**）

$$\text{我方既有判断}（`CLOSED-ROUTES-MAP.md` L727 逐字）：\text{"GM 2024}\ \textbf{方向是"密度／排斥"}，\ \textbf{非涨落相消"}✓✓$$
$$\qquad\Longrightarrow\ \text{而三阶矩}\ \mathrm{tr}\tilde G^3\ \textbf{要的是相消}（\text{三点相关的振荡结构}），\ \text{不是密度排除}✓$$
$$\qquad\Longrightarrow\ \text{故}\ (\text{i})\ \text{的}\ \textbf{先验} \text{是：}\text{方向可能不匹配}——\text{但}\ \text{§4 的}\ (N,V)\ \text{位置检查}\ \textbf{可判定}，\ \text{不必停在判断层}✓✓$$
$$\qquad ⚠️\ \text{另有：}\text{GM 的}\ V\ \text{是单个多项式的大值频率}，\ \text{而}\ \mathrm{tr}\tilde G^3\ \text{涉及}\ \textbf{多个多项式的乘积} ⟹ \text{对象型可能不同}（\text{须核}）✓$$

## 6. 判定与下一步
$$\text{本刀}\ \textbf{未} \text{闭合}\ T^{1/3}；\ \text{产出}\ = \text{① GM 定理数字化入仓（含窗口的独立推导）② 缺口规格精确化（§4 一行判定）③ 方向匹配的先验警示}✓$$
$$\Longrightarrow\ \textbf{下一步（(i)-2）}：\text{取前沿 §5（对角法）原文} \to \text{定位其}\ (N,V)\ \text{坐标} \to \text{对照}\ \text{§3 窗口} \to \text{判定}✓✓$$
$$\qquad ⚠️\ \text{若前沿原文（arXiv:2608.13637）不可得} \Longrightarrow \text{按我方可及材料重建归约，或转 (ii)}✓$$

## 7. 边界
$$\text{(i)}\ §2\ \text{为}\ \textbf{原文逐字}（本地 PDF，已抽取 91{,}905 字符）✓\quad\text{(ii)}\ §3\ \text{为}\ \textbf{本档推导}（初等指数比较，可逐行核）✓$$
$$\text{(iii)}\ §5\ \text{的 L727 为既有}\ [\textbf{判断}] \text{（未重核原文）}✓\quad\text{(iv)}\ \textbf{未用 RH；零数值}✓$$
