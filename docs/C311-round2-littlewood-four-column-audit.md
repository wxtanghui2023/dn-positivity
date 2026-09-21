已查地图（**先查后写**）：`C-310`（Barker：缺失型反例 ✓）、`C-309`／`C-308`（方向① 两族 ✓）、`C-292`（Littlewood 深审回执：K_n vs L_n 分离 ＋ 2020 定理精确出处 ＋ Saffari–Smith 1988 含错 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-311：Round 2 第二项 —— Littlewood 四格审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\text{① failure 类型}\ \textbf{必须先钉死}✓✓：\text{存在}\ \textbf{两种互不相同的 failure 概念}✓（\text{见 §1}✓）}$$
$$\boxed{\textbf{F}\text{（性质型）}✓✓：\text{「该}\ \pm1\ \text{多项式不}\ \varepsilon\text{-flat」}✓\ \text{是}\ \textbf{关于一个实际存在对象的性质}✓ \Longrightarrow \textbf{YES}✓}$$
$$\boxed{\textbf{F}\text{（缺失型）}✗：\text{「}L_n\ \text{中不存在 ultraflat 序列」}✗\ \text{是}\ \textbf{类为空}✗ \Longrightarrow \textbf{缺席型，不适用}✗（\text{同 Barker}✓）}$$
$$\boxed{\textbf{A}_1／A_2／C\ ✗：\textbf{未见真正的传播}✓（\text{只有对合／等距}✗＋\text{构造}✗＋\text{破坏归一化者}✗）}$$
$$\Longrightarrow \textbf{未通过四格}✓ \Longrightarrow \textbf{第六类反例}✓；\textbf{不进入}\ RH\ ✗；\textbf{不补传播}✗$$

## §1 先钉死 failure 类型（✓✓，本刀第一要务 ✓）

$$\textbf{对象}✓：P(z) = \text{sum}_{k=0}^{n} a_k z^k✓，a_k \in \{\pm1\}✓；\text{flatness 量}\ W(P)✓（\text{归一化后}\ \max - \min✓，Odlyzko 记法 ✓）$$
$$\textbf{F}_{\text{prop}}\ （\text{性质型}）✓✓：\text{对固定}\ n，\{\pm1\ \text{多项式}\ P:\ W(P) > \varepsilon\}✓\ —— \ \textbf{每个元素都是实际存在的多项式}✓，\text{性质可逐例核}✓ \Longrightarrow \textbf{可用于四格}✓$$
$$\textbf{F}_{\text{abs}}\ （\text{缺失型}）✗：\text{「}L_n\ \text{中不存在 ultraflat 序列」}✓（\text{Erdős 在}\ L_n\ \text{上的猜想}✓）\ —— \ \textbf{类为空}✗ \Longrightarrow \textbf{FSD 无处落脚}✗（\text{同}\ C\text{-310 Barker}✓）$$
$$\textbf{关键区分}✓✓：\text{两者}\ \textbf{不可混}✗；\text{本刀只审}\ F_{\text{prop}}✓$$
$$\textbf{层级纪律}✓（C\text{-292}✓）：\text{类}\ K_n\ \text{与}\ L_n\ \text{严格分开}✓；\ K_n\ \text{侧}\ \text{Kahane 1980 已否证}✓，\textbf{不}\ \text{下降为}\ L_n\ \text{的结论}✗✓$$

## §2 A₁ 格：**保 failure 的对合 ≠ 传播**（✓✓，本档关键发现 ✓）

$$\textbf{候选一（系数 reversal}：P(z) \mapsto z^n P(1/z)✓）✗：\text{在}\ |z| = 1\ \text{上}\ \textbf{是等距}✓ \Longrightarrow \textbf{保 flatness}✓，\text{但}\ \textbf{是对合}✗ \Longrightarrow \text{按唐先生预注册：}\textbf{除非真把 failure 传到新结构状态，否则不算}✗✓$$
$$\textbf{候选二（整体 negation}：P \mapsto -P✓）✗：\text{平凡对合}✗$$
$$\textbf{候选三（}z \mapsto z^k\ \text{代换}✓）✗：\text{产生}\ \textbf{稀疏} \text{（零系数）多项式}✗ \Longrightarrow \textbf{离开}\ \pm1\ \text{类}✗✓$$
$$\textbf{候选四（乘积} P \cdot Q✓）✗：\text{尖峰虽保持}✓，\text{但阈值随阶数改变}✓（\sqrt{(n+1)(m+1)}✓）\ \Longrightarrow \textbf{依赖归一化}✗（\text{唐先生排除}✓）$$
$$\textbf{候选五（Rudin–Shapiro 递推}✓／\text{Golay 对}✓／\text{Kahane 构造}✓）✗：\textbf{是构造}✗，\textbf{不是作用}✗✓$$
$$\Longrightarrow \textbf{A}_1 = \textbf{未见真正传播}✗；\textbf{A}_2 = \textbf{未见}✗$$

## §3 ⭐ 必须区分的两类"共同约束"（✓✓）

$$\textbf{类型 A（不算）}✗：\text{两个理论结果}\ \textbf{共同限制同一个量}✓\ —— \text{本侧确实存在}✓：\text{Parseval／}L^2\ \text{恒等式}✗（\text{排除项}✓）＋\ \text{Shapiro／Rudin 上界}✓＋\ \text{discrepancy 下界}✓ \Longrightarrow \text{它们}\ \textbf{共同约束 flatness}✓\ \text{但}\ \textbf{不是两传播兼容}✗✓$$
$$\qquad \text{2020 定理}✓：\text{Balister–Bollobás–Morris–Sahasrabudhe–Tiba, Annals 192(3):977–1004}✓\ \text{只给}\ \textbf{bounded flatness}✓（\delta\sqrt{n} \le |P| \le \Delta\sqrt{n}✓），\textbf{不解决} ultraflat ✗ \Longrightarrow \textbf{存在性定理}✗，\textbf{不是兼容律}✗$$
$$\textbf{类型 B（才算）}✓：\text{两个}\ \textbf{独立传播作用}，\text{其}\ A_1 A_2\ \text{与}\ A_2 A_1\ \text{之间存在非平凡律}✓ \Longrightarrow \textbf{本侧未见}✗$$

## §4 判定（✓✓）

$$\textbf{未通过四格}✗ \Longrightarrow \textbf{第六类反例}✓；\text{六反例并表}✓：\quad \begin{array}{c|c|c|c} & \text{Failure} & \text{类型} & \text{兼容律}\\ \hline \text{Hecke} & ✗ & — & ✗\\ \text{Schur} & ✓ & \text{性质型} & ✗\\ \text{素数间隙} & ✓ & \text{内禀} & ✗\\ \text{零点间距} & 🟡 & \text{模型相对} & ✗\\ \text{Barker} & ✓ & \text{缺失型} & ✗\\ \text{Littlewood} & ✓ & \textbf{性质型＋含对合等距} & ✗ \end{array}$$
$$\Longrightarrow \text{六反例}\ \textbf{一致指向}✓✓：\textbf{稀缺物＝独立存在的非平凡兼容律}✓✓$$
$$\textbf{新增精确区分}✓✓：\ \boxed{\text{「保 failure 的对合」} \ne \text{「把 failure 传到新状态的传播」}}✓$$

## §5 避雷执行确认（✓✓）

$$\textbf{① Parseval／}L^2\ \text{恒等式}\ \textbf{未}计作传播✗✓；\textbf{② 对合（reversal／negation／}z \mapsto z^{-1}\text{）}\ \textbf{未}计作传播✗✓；\textbf{③ 构造（随机构造／Kahane／Rudin–Shapiro／上下界估计）}\ \textbf{未}升级为兼容✗✓$$

## §6 待做（✓）

$$\textbf{Round 2 剩余}✓：\text{Lonely Runner}✓（\text{逐项四格}✓，\text{不并行}✓）\ ;\ \text{其天然兼具「整数速度结构＋torus orbit／covering obstruction」}✓，\textbf{尤须防「看起来有两个作用」}✗✓$$

## §7 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：Littlewood 已排除 ✗（仅"未通过四格"✓）；K_n 结论下降为 L_n ✗；2020 定理＝ultraflat ✗
- **本档新增词**：`保 failure 的对合`／`性质型＋对合等距`（0 命中 ✓）
