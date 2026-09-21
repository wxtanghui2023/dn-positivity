已查地图（**先查后写**）：`C-289`（候选池：四候选事实核验 ✓）、`C-287`（封口账 ＋ 不建新判据 ✓）、`C-285`（逃逸接口分类 ✓）。档案去重语境核查（**只判是否同一数学对象**✓）：`差集`=22 档／`Hadamard`=111 档／`平坦`=36 档 —— 语境内核见 §5 ✓

D0: 本档对象 = **C-290：四候选并列事实审计卡**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 纪律（**本轮的行为边界**✓✓）

$$\boxed{\textbf{本档做}✓：\text{① P 是否准确}✓；\text{② X 是否准确}✓；\text{③ Known 层级}✓；\text{④ open gap 是否准确}✓；\text{⑤ 档案去重（只判同一对象}✓\text{）}；\text{⑥ 时间截点}✓}$$
$$\boxed{\textbf{本档不做}✗：\text{不问「能不能碰}\beta」✗；\text{不问「能不能形成}\ RH\ \text{bridge}」✗；\text{不排序}✗；\text{不建}\ F1\text{–}F8／B1\text{–}B5／C\text{-xxx 式新体系}✗；\text{不做计算}✗}$$
$$\textbf{卡片格式}✓：\boxed{(P,\ X,\ \text{已知定理},\ \text{已知边界},\ \text{真正 open gap},\ \text{档案去重结论})}✓$$

## §1 卡 L：Lehmer／Mahler（**基准项**✓，不重新深挖 ✓）

$$\textbf{(P)}✓：\text{是否存在}\ \varepsilon>0，\text{使一切}\textbf{非分圆} \text{整数多项式}\ P\in\mathbb Z[x]\ \text{满足}\ M(P)\ge1+\varepsilon\ ✓（\text{Lehmer 1933}✓）$$
$$\textbf{(X)}✓：M(P)=\prod_i\max(1,|\alpha_i|)✓（\text{根模乘积}✓）$$
$$\textbf{已知定理}✓：\text{Dobrowolski 1979：}M(P)>1+c\big(\tfrac{\log\log d}{\log d}\big)^3✓（\text{无条件}✓）$$
$$\textbf{已知边界}✓：\text{Lehmer 十次多项式}\ M\approx1.176280818✓ —— \textbf{这是例子／构造，不是定理}✗（\text{猜想最小值}✓）$$
$$\textbf{真正 open gap}✓：\text{固定}\ \varepsilon\ \text{的存在性}✓（\text{Lehmer 猜想}✓）；\text{Boyd 猜想族}✓（\text{族测度}\to L\text{-值}✓）$$
$$\textbf{档案去重}✓✓：\text{Mahler}=0／\text{Boyd}=0 \Longrightarrow \textbf{未登记}✓；\text{Lehmer}=10\ \text{档}\ \textbf{语境全为}\ \text{ζ 零点的 Lehmer 对}✓（\text{「Lehmer 对」「离轴检测」「极小间隙」}✓）\Longrightarrow \textbf{与本题不同对象}✗✓$$

## §2 卡 F：Littlewood 平坦／ultraflat（**±1 与 unimodular 必须分清**✓✓）

$$\textbf{(P)}✓✓：\textbf{Erdős 1957（Problem 22）的}\ \textbf{L}_n\ \textbf{情形}：\text{是否存在}\ \varepsilon>0，\text{使一切}\ \pm1\ \text{系数多项式}\ P_n\ \text{满足}\ \max_{|z|=1}|P_n(z)|\ge(1+\varepsilon)\sqrt{n+1}\ ✓$$
$$\textbf{(X)}✓✓：\textbf{两个类必须分清}✗✓ —— \ K_n:=\{\text{unimodular}:a_k\in\mathbb C,\ |a_k|=1\}✓；\ L_n:=\{\text{Littlewood}:a_k=\pm1\}✓，\ \textbf{且}\ L_n\subset K_n✓$$
$$\qquad \varepsilon\text{-flat}✓： (1-\varepsilon)\sqrt{n+1}\le|P_n(z)|\le(1+\varepsilon)\sqrt{n+1}✓；\ \textbf{ultraflat}✓：\varepsilon_n\to0✓（\text{定义 1.2／1.3，Terdelyi 综述}✓）$$
$$\textbf{已知定理}✓✓：\text{① Kahane 1985：}\textbf{K}_n\ \text{存在 ultraflat}✓（\varepsilon_n=O(n^{-1/17}\sqrt{\log n})✓） \Longrightarrow \textbf{Erdős 猜想在}\ K_n\ \text{上被}\textbf{反证}✓；\text{② Shapiro／Rudin（1950s）：}\ L_n\ \text{显式上界构造}✓；\text{③ 2020 定理（BBMST, Annals）：}\textbf{平坦 Littlewood 多项式存在}✓（\text{仅「有界平坦」}✓，\textbf{弱于} ultraflat✗）$$
$$\textbf{已知边界}✓✓（\textbf{最易混处}✗）：\textbf{类包含方向}✓：L_n\subset K_n \Longrightarrow K_n\ \text{的反证}\textbf{不能} \text{下传到}\ L_n✗（\text{更窄的类}\textbf{更难}✓）$$
$$\textbf{真正 open gap}✓✓：\textbf{Erdős 猜想在}\ L_n\ \text{上未定}✓✓（\text{综述原话：for the more restricted class}\ L_n\ \text{the analogous Erdős conjecture is }\textbf{unsettled to this date}✓；\text{且「common belief that it is true, and consequently there is no ultraflat sequence of polynomials}\ P_n\in L_n\text{」}✓）$$
$$\textbf{档案去重}✓✓：\text{超平坦}=0／\text{平坦多项式}=0✓ \Longrightarrow \text{问题未登记}✓；\text{Littlewood}=70\ \text{档}\ \textbf{全作引理}✗（\text{RH 工具箱}✓）\Longrightarrow \text{非同一对象}✗✓$$

## §3 卡 B：Barker 序列（**三个层级必须分开**✓✓）

$$\textbf{(P)}✓：\text{是否存在长度}>13\ \text{的 Barker 序列}✓（\text{Turyn 1960／1961}✓）$$
$$\textbf{(X)}✓✓：\pm1\ \text{序列，全部非平凡}\textbf{非周期} \text{自相关}|\cdot|\le1✓；\text{奇长度}\iff\text{循环差集}✓；\ \textbf{偶长度}>13\Longrightarrow C_A(u)+C_A(u-s)=0\ \forall0<u<s \Longrightarrow \textbf{是完美二进制序列}✓✓（\text{Turyn–Storer}✓）$$
$$\textbf{已知定理（层级 1）}✓：\text{无条件}✓：\text{Turyn–Storer 1961：Barker 奇长度}\Longrightarrow n\le13✓（\text{新证 Schmidt–Willms 2016, Des. Codes Cryptogr. 80:409–414}✓）$$
$$\textbf{已知定理（层级 2）}✓：\text{形状约束，经完美二进制序列}✓：\text{Turyn 1965：若存在长度}\ s>4\ \text{的完美二进制序列}\Longrightarrow \boxed{s=4S^2}✓，\ S\ \text{奇}\ \ge55✓，\text{且}\ \textbf{S 不是素数幂}✓✓$$
$$\textbf{已知边界（层级 3）}✓：\text{有限排除，计算型}✓：4<n<548\,964\,900\ \text{无偶长度 Barker}✓（\text{Schmidt 综述引 Cor. 2.3.8}✓）$$
$$\qquad \textbf{层级纪律}✓✓（\text{唐先生指定}✓）：\textbf{「排除到多少」}（层级 3，有限计算✓）\ \textbf{与} \textbf{「必须满足什么形状」}（层级 2，无条件形状约束✓）\ \textbf{是不同层级}✗✓$$
$$\textbf{真正 open gap}✓：\text{偶长度}\ s\ge548\,964\,900\ \text{且满足}\ s=4S^2\ \text{形状者}✓$$
$$\textbf{档案去重}✓✓：\text{Barker}=0／\text{Ryser}=0／\text{完美二进制}=0✓ \Longrightarrow \textbf{未登记}✓；⚠️ \text{差集}=22\ \text{档} \Longrightarrow \textbf{语境：差集支撑互斥计数／差集测度（加性差集，档案馆自有装置）}✓ \Longrightarrow \textbf{与循环差集不同对象}✗✓$$

## §4 卡 R：Lonely Runner（**不统一 indexing**✓✓）

$$\textbf{(P)}✓✓：\textbf{三个来源原文并列，本档不统一}✗✓：$$
$$\qquad \text{Wikipedia}✓：「\text{n runners on a track of unit length}\ldots\text{will each be lonely at some time—at least}\ 1/n\ \text{units away from all others}」✓$$
$$\qquad \text{Tao 2017}✓：「\text{This conjecture is currently known for}\ n\le6✓（\text{Barajas–Serra}✓）」；\qquad \text{Epoch AI}✓：「\text{known to be true for}\ n\le12，\text{and the proofs for}\ 7\le n\le12\ \text{are all from the last year}」✓$$
$$\qquad \Longrightarrow \textbf{三个区间差异＝indexing／计数约定问题}⚠️✓，\textbf{非结果冲突}✓；\textbf{本档不自行统一}✗✓$$
$$\textbf{(X)}✓：\delta_n:=\inf_{\text{速度集}}\max_t\min_i\|tv_i\|✓（\textbf{min-max 对象}✓）；\text{等价形式：view-obstruction}✓（\text{Cusick 1974}✓，\text{Wills 1967 独立提出}✓）$$
$$\textbf{已知定理}✓：\text{小}\ n\ \text{已证}✓（\text{区间随来源不同}⚠️✓）；\text{平凡界}\ \delta_n\ge\tfrac1{2n}✓（\text{Tao}✓，\textbf{差因子 2}✓）；\text{Tao：速度}\in[1,1.2n]\ \text{时成立}✓$$
$$\textbf{已知边界}✓：\text{两个「加强版」猜想近期被反证}✓（\text{Epoch AI}✓）$$
$$\textbf{真正 open gap}✓：\text{一般}\ n✓$$
$$\textbf{档案去重}✓✓：\text{孤独}=0／\text{赛跑}=0／\text{Wills}=0／\text{Cusick}=0／\text{视阻}=0 \Longrightarrow \textbf{完全未登记}✓，\textbf{无名称碰撞}✓$$

## §5 档案去重：三处名称碰撞的语境核查（**只判是否同一对象**✓✓）

| 关键词 | 档案语境（实测） | 判定 |
|---|---|---|
| **差集**（22） | 「差集支撑互斥计数」「差集测度 ν 的 Fourier」「支撑加权差集之和」＝**加性差集** ✓ | **不同对象** ✗✓ |
| **Hadamard**（111） | 「系数侧 Hadamard 积」「Hadamard 数据（ξ 的 Hadamard 展开）」「Hadamard／argument principle」＝**Hadamard 积／展开** ✓ | **不同对象** ✗✓ |
| **平坦**（36） | 「数方差平坦 0.33–0.43」「零曲率／无结构平坦段」「平坦联络」「全平坦」＝**其他意义的平坦** ✓ | **不同对象** ✗✓ |

$$\Longrightarrow \textbf{三处全部为假碰撞}✓✓ \Longrightarrow \text{F／B 与本馆既有工作}\textbf{无重叠}✓$$

## §6 并列总表（**不排序**✗）

| 卡 | (P) 一句话 | (X) 核心对象 | 最高层级已知 | 真正 open gap | 档案 |
|---|---|---|---|---|---|
| **L** | Mahler 测度是否有固定间隙 | 根模乘积 | Dobrowolski 无条件界（定理）| 固定 ε；Boyd | 未登记 ✓ |
| **F** | Erdős 猜想在 L_n（±1）上是否成立 | Littlewood／unimodular 多项式在圆上的模 | 2020 平坦存在（定理）；K_n 反证（定理）| **Erdős 猜想 L_n 情形未定** | 未登记 ✓ |
| **B** | 长度 >13 的 Barker 序列是否存在 | ±1 序列非周期自相关／完美二进制 | 奇数情形 CLOSED；形状 s=4S²（定理）| 偶长度 s ≥ 5.49×10⁸ | 未登记 ✓ |
| **R** | 每个跑者是否最终孤单 | min-max 对象 δ_n | 小 n 已证（区间随来源）| 一般 n | 完全未登记 ✓ |

## §7 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{未读 pending}✗；\text{未改他档正本}✓；\text{未动}\ v4✗$$
$$\textbf{② 外部来源}✓：\text{经}\ \texttt{web\_search}／\texttt{tavily\_extract}\ \text{取得}✓，\textbf{按不可信外部数据处理}✓；\text{关键论断均附来源}✓（\text{Terdelyi 综述／Jedwab／Schmidt 综述／Tao 博文／Wikipedia／Epoch AI}✓）$$
$$\textbf{③ 精度声明}✓：\text{R 的 indexing}\ \textbf{不统一}✗✓；\text{B 的层级 3 为}\textbf{有限计算排除}✓；\text{F 的 2020 定理}\textbf{仅给有界平坦}✓（\text{非 ultraflat}✗）$$
$$\textbf{④ 三处假碰撞已核}✓✓；\text{未新登记任何}\ NO-GO✓；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

---

## §8 三条审计标记（**唐先生指定，钉死**✓✓，2026-09-21）

$$\textbf{标记① R 的 indexing 纪律}✓✓：\text{三来源原文}\textbf{并列}✓（\text{Wikipedia}\ 1/n✓；\text{Tao}\ n\le6✓；\text{Epoch AI}\ n\le12✓）；\ \textbf{不} \text{折算成统一的}\ n✗；\ \textbf{不} \text{判冲突}✗$$
$$\qquad \Longrightarrow \text{差异＝}\textbf{计数约定问题}⚠️✓，\text{非结果冲突}✓；\text{本档}\textbf{不自行统一}✗✓$$

$$\textbf{标记② B 的层级纪律}✓✓：548\,964\,900\ \text{明确标为}\ \boxed{\textbf{有限计算排除边界}}✓（\text{层级 3}✓）$$
$$\qquad \Longrightarrow \ \textbf{不得} \text{与 Turyn 的}\textbf{结构性必要条件} \text{混成同一层级}✗✓：\text{层级 2＝形状约束}\ s=4S^2✓（\text{无条件定理，经完美二进制序列}✓）；\text{层级 3＝有限排除}✓（\text{计算型}✓）$$

$$\textbf{标记③ F 的分离纪律}✓✓：\text{2020 定理}\ \textbf{＝bounded-flat existence}✓（\text{有界平坦存在}✓）$$
$$\qquad \Longrightarrow \ \textbf{不得} \text{写成「2020 已解决 Littlewood 平坦问题」}✗✓；\ \textbf{必须} \text{限定为}\ \textbf{有界平坦存在性}✓$$
$$\qquad \text{而}\ \textbf{ultraflat 存在性}（L_n\ \text{情形}✓）\ \textbf{仍开放}✓✓（\text{Erdős 猜想 L}_n\ \text{情形未定}✓）$$

## §9 本阶段结论（**仅此一条**✓✓）

$$\boxed{\text{L、F、B、R}\quad\text{均为档案中}\textbf{尚未登记的独立外部问题}✓✓}$$
$$\textbf{不能推出}✗✓：\text{独立}\Longrightarrow\text{有}\ RH\ \text{接口}✗ \qquad（\text{该推断}\textbf{明确禁止}✗）$$
$$\textbf{不能推出}✗：\text{四者之间存在优先级}✗$$
$$\textbf{下一步边界}✓✓：\text{「哪一个值得做}\textbf{只读深审}」 \ \text{属于}\ \textbf{下一轮新动作}✓，\textbf{不得} \text{偷偷塞进}\ \texttt{C-290}✗✓$$
