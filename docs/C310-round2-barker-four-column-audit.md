已查地图（**先查后写**）：`C-309`（零点间距 ✓）、`C-308`（素数间隙 ✓）、`C-305`（Round 2 锁定 ✓）、`C-292`（Barker 深审回执：页码勘误 ＋ 548,964,900 层级 ＋ Turyn 1965 精确陈述 ＋ 方向纪律 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-310：Round 2 第一项 —— Barker 四格审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{F}✓\ ⚠️：\text{Barker 的 failure}\ \textbf{是「缺失型」}\（\text{不存在某长度的 Barker 序列}✓）\ \text{—— 属}\ \textbf{absence-type}✗✓（\text{见 §2}✓）}$$
$$\boxed{\textbf{A}_1\ ✗：\text{只有}\ \textbf{平凡对合}✓（\text{reversal}✓／\text{negation}✓）\ \text{—— 且它们只作用于}\ \textbf{已存在的序列}✗}$$
$$\boxed{\textbf{A}_2\ ✗：\textbf{未见独立第二传播}✓}$$
$$\boxed{\textbf{C}\ ✗：\textbf{未见非平凡兼容律}✓ \Longrightarrow \textbf{未通过四格}✓ \Longrightarrow \textbf{第五类反例}✓}$$
$$\Longrightarrow \textbf{不进入}\ RH\ ✗；\textbf{不给排序}✗；\textbf{不加新过滤条件}✗$$

## §1 F 格（✓）

$$\textbf{定义}✓：\text{Barker 序列}\ \pm1\ \text{序列，全部非平凡}\ \textbf{非周期}\ \text{自相关旁瓣}\ |C_k| \le 1✓$$
$$\textbf{failure 的两种写法}✓：\text{①}\ \textbf{存在性失败}✓（\text{给定长度}\ n\ \text{不存在这样的序列}✓）；\text{②}\ \textbf{猜想形式}✓（\text{不存在长度} > 13\ \text{的 Barker 序列}✓）$$
$$\textbf{文献地位}✓✓：\text{标准问题}✓（\text{已知长度}\ 2,3,4,5,7,11,13✓；\text{奇长度已由 Turyn–Storer 1961 排除} > 13✓\（\text{该文证明有缺陷，Willms 2014；Schmidt–Willms 2016 给可用新证明}✓））$$
$$\Longrightarrow \textbf{F} = YES✓\ \text{但形态特殊}⚠️$$

## §2 ⭐ 结构诊断：**absence-type failure**（✓✓，本档关键）

$$\textbf{对照}✓✓：\ \text{Schur 侧 failure}＝\text{「该集合是 sum-free」}✓\ —— \ \textbf{是关于一个已存在对象的性质}✓ \Longrightarrow \text{有对象可供作用}✓$$
$$\qquad \text{Barker 侧 failure}＝\text{「不存在该长度的序列」}✓\ —— \ \textbf{是关于一个类为空的陈述}✗ \Longrightarrow \textbf{没有对象可供作用}✗✓$$
$$\Longrightarrow \textbf{后果}✓✓：\text{FSD 模板要求}\ \mathcal F = \{\text{失败的对象}\}✓；\text{当 failure 是}\ \textbf{缺失型}✗\ \text{时，}\ A_1／A_2／C\ \textbf{在定义上即无处落脚}✗✓$$
$$\textbf{纪律}✓：\text{不得}把「缺失型 failure」硬重写成「某对象集为空」再人为造作用 ✗✓（\text{唐先生预注册}✓）$$

## §3 A₁／A₂ 格（✗）

$$\textbf{仅有的自然变换}✓：\textbf{reversal}✓（\text{反转序列仍是 Barker}✓）；\textbf{negation}✓（\text{整体取负仍是 Barker}✓）\ —— \textbf{均为对合}✗，\textbf{且只作用于已存在者}✗$$
$$\textbf{排除项}✗✓（\text{按唐先生指定}✓）：\text{非周期／周期自相关之}\ \textbf{关系式}✗（\ C_{per}(u) = C_{aper}(u) + C_{aper}(u-n)\ ✓\ \text{是}\ \textbf{关系}✗，\text{不是作用}✗）$$
$$\qquad \text{差集／Hadamard／circulant-Hadamard 的}\ \textbf{等价链}✗；\text{Turyn–Storer 型}\ \textbf{结构限制}✗ \Longrightarrow \textbf{不得}因「它们最终互相约束」而称作两传播兼容✗✓$$
$$\textbf{shift}✗：\text{非周期自相关}\ \textbf{不}具有平移不变性✗✓ \Longrightarrow \text{平移不是保 failure 的作用}✗$$
$$\Longrightarrow \textbf{A}_1 = \textbf{未见}✗；\textbf{A}_2 = \textbf{未见}✗$$

## §4 C 格（✗）

$$\text{无两传播} \Longrightarrow \text{无从谈兼容}✗$$

## §5 判定（✓✓）

$$\textbf{未通过四格}✗ \Longrightarrow \textbf{第五类反例}✓；\text{五反例并表}✓：\quad \begin{array}{c|c|c|c} & \text{Failure} & \text{类型} & \text{兼容律}\\ \hline \text{Hecke} & ✗ & — & ✗\\ \text{Schur} & ✓ & \text{性质型} & ✗\\ \text{素数间隙} & ✓ & \text{内禀} & ✗\\ \text{零点间距} & 🟡 & \text{模型相对} & ✗\\ \text{Barker} & ✓ & \textbf{缺失型} & ✗ \end{array}$$
$$\Longrightarrow \text{五反例}\ \textbf{一致指向}✓✓：\textbf{稀缺物＝独立存在的非平凡兼容律}✓✓$$

## §6 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：Barker 已排除 ✗（仅"未通过四格"✓）；结构推论链＝兼容律 ✗；Barker 与 RH 无关 ✗
- **Round 2 剩余** ✓：Littlewood ✓ → Lonely Runner ✓（逐项做四格 ✓，不并行 ✓）
- **本档新增词**：`absence-type failure`／`缺失型失败`（0 命中 ✓）
