已查地图（**先查后写**）：查 `CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`／`ASSETS-REGISTRY.md`（关键词：总产出盘点｜优先级｜交付｜论文）。命中条目均为**不相关**内容（Weil 正性／V223／V249 等）⟹ 本档为**成果与优先级登记**，不涉已封路线 ⟹ 可开 ✓

D0: 本档对象 = 档案已有各线成果（RP_M/C₃ 线、T-I 三例、矩猜想/Palojärvi 线、论文 A/B、方法学资产）的**汇总与优先级重排** —— 关系 = 汇总／登记（非重命名、非新对象）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产新数学结论）

# 总产出盘点 · 2026-09-20（唐先生指令：C₃ 封版后立即执行）

> **纪律**：每项回答三问 —— ① **已经证明了什么？** ② **真正的新数学在哪里？** ③ **再投 10 小时最可能产出什么级别的信息？**
> **不按"哪个项目刚撞墙"排序**，按"单位投入的信息产出"排序 ✓

---

## A. RP_M / C₃ 线（本线主成果）

### A.1 已证明（按严格等级分层）

$$\textbf{[手工·严格]}\ \text{Lemma C（}M{=}1\text{）：}\max_{k\le5}\Re z^k\ge\tfrac12✓；\text{鸽笼定理：}\max_{m\le N}\cos(m\theta)\ge\cos\tfrac{2\pi}{N+1}\（\textbf{且锐}）✓$$
$$\qquad \text{覆盖引理（}N{=}3\text{）}✓；\text{Case A（任意}M\text{）}✓；\text{近似周期单调性引理 ＋ 其推论（现已无条件）}✓$$
$$\qquad m_M\le\sqrt{2M\ln10M}\（M\ge12\text{，概率法}）✓ \Longrightarrow m_M\le M-1\（\text{一切}M\ge2\text{，}M\le11\ \text{由 C-176 证书承担}）✓$$
$$\qquad \kappa_N\ \text{的}\ \lambda_{\max}=2-\sqrt3\ \text{闭式 ＋ 一维证书}✓$$
$$\textbf{[计算机辅助·区间认证]}\ \text{Theorem 1（}M{=}2\text{，三段拼装}）✓；\text{无阻尼}M{=}3,4,5\ \text{证书（双实现＋误差模型）}✓$$
$$\qquad \textbf{阻尼}M{=}2：\text{全}\ r\in[0,1]\ \text{一致界}\ 0.364984✓（=7.3\times\tfrac1{20}）✓$$
$$\qquad \textbf{阻尼}M{=}3：\text{封版夹逼}\ \boxed{0.3730918\le C_3\le0.373092075762}✓（\text{宽}\ 2.75762\times10^{-7}）✓✓$$
$$\qquad \text{且}\ \textbf{同时证明}\ F\ge0.3730918\ \text{处处成立}\Longrightarrow\text{不存在更深的点}✓（\text{证明，非搜索}）✓$$

### A.2 真正的新数学

$$\text{① 常数改进}：\text{文献}\ \tfrac1{20}=0.05 \longrightarrow\ \text{我方}\ 0.364984（M{=}2）／0.3730918（M{=}3）＝\mathbf{7.3\sim7.5\ \text{倍}}✓$$
$$\qquad \text{无阻尼（}|z_j|{\equiv}1\text{，Montgomery Lemma 2.2 的特例}）：m_3{=}0.764,\ m_4{=}0.842,\ m_5{=}1.027 \Longrightarrow \mathbf{15\sim20\ \text{倍}}✓✓$$
$$\text{② 鸽笼定理（}\kappa_N=\cos\tfrac{2\pi}{N+1}\text{，锐）}：\text{三行初等证明}✓\ —— \text{待核文献先例}（\text{同族：Fejér／Chebyshev 极值}）✓$$
$$\text{③ 机制定位}：\text{文献窗口}\ m\sim n^2／n^{1+\delta}\ \text{与本题窗口}\ m=5n\ \text{之间的}\ \textbf{空隙}✓（\text{literature gap}）✓✓$$
$$\qquad \text{已建窗口-机制映射}：m\le n-1\to0；m=n\to1；\mathbf{m=5n\to\text{未知（本题）}}；m\sim n^2\to\text{Andersson 体系}✓$$
$$\text{④ 方法学资产}：\text{四门协议（精确铺砌／区间正性／双实现／数学域覆盖）＋"域覆盖先于余量"＋"用证明不用搜索"}✓✓$$

### A.3 再投 10 小时

$$\textbf{写论文（最高推荐）}：\text{材料已齐（}M\le5\ \text{无阻尼 ＋ 阻尼夹逼 ＋ 窗口映射 ＋ 方法学}）\Longrightarrow\ \textbf{可提交级草稿}✓✓$$
$$\text{阻尼}\ M{=}4：\text{同流水线，成本升高}✓\ \text{但边界价值低（}M{=}3\ \text{已示范方法}）\Longrightarrow\ \textbf{缓办}✓$$
$$\text{精确值／突破分辨率墙}：\text{需}\ \textbf{新机制}（\text{active-set／窄盆地解析化／更强联合约束}）\Longrightarrow\ \textbf{研究项目，非 10 小时任务}✗$$

---

## B. T-I 短文线（三例并列结构）

### B.1 已证明

$$\text{V227-A：}\sup\Re z\ \text{不是模长多重集的函数（}\{i,-i\}\ \text{vs}\ \{1,-1\}）✓$$
$$\text{V253：}\ \sigma{=}1\ \text{的尾和有限性强制型结果}✓\qquad \text{F3：窗口隐形测度反例（秩}\ 47\to256\ \text{而窗口幅频精确不变）}✓✓$$
$$\text{四要素框架}：\text{输入（模长型）／目标（位置型）／隐形方向／缺失的非模长输入}✓$$
$$\text{"局部隐形无意义"原理}：\text{目标约束集全局时，缩窗口技术一律无效}✓$$

### B.2 真正的新数学

$$\text{机制本身}\ \textbf{不是} \text{新的}✗：\text{F3}\equiv\text{FRI／湮灭滤波器零空间（Vetterli--Marziliano--Blu 2002，经典）}✓\ —— \text{已诚实降级}✓$$
$$\qquad \text{新颖性只在}：\text{(a) 四要素框架 (b) 三例并列结构 (c) 与整数质量约束的对接方式}✓$$
$$\Longrightarrow \text{定位：}\textbf{解释性／方法学短注}（\text{不是突破级}）✓$$

### B.3 再投 10 小时

$$\text{先补三项待核}：\text{V227-A／V253 原文逐字 ＋ 主题文献先例}✓（\text{约 2 小时}）$$
$$\text{然后起草}：\text{10 小时}\Longrightarrow\ \textbf{可提交短注草稿}✓（\text{预期等级：方法学短文}）$$

---

## C. 矩猜想／Palojärvi 线

### C.1 已证明

$$\text{Palojärvi}\ m{=}1\ \text{改进（}\tau\text{-一致，}\tau>1/e\text{）}✓；\text{Lemma 2.2 单位模情形的}\ \textbf{自足重证}（\text{对称化 ＋ Andersson Fejér 机制}）✓✓$$
$$\text{机制级审计}：\text{Fejér 机制}\ \textbf{可达}\ 5M\ \text{但}\ \textbf{结构上不尖锐}（\text{封顶}\approx\tfrac1{20}）✓✓\qquad \text{阻尼情形}\ \textbf{Fejér 失效}（\text{对角项衰减}）✓$$
$$\text{文献定位表}：\text{Andersson 系列（}h{-}1\text{）}\sqrt n\ \text{型结果 ＋ 精确值论文 ＋ Fejér 下界}✓✓$$

### C.2 真正的新数学

$$\text{"Fejér 封顶}\ \tfrac1{20}\text{"的机制级解释}✓；\text{阻尼情形}\ \textbf{主动利用半径自由度} \text{（}\inf_{\mathbb D^3}=0.3731<\inf_{\mathbb T^3}=0.8090\text{）}✓✓$$
$$\text{窗口-机制映射作为可引用的定位句}✓$$

### C.3 再投 10 小时

$$\text{把这些并入 A 线论文的一节（"为何}\ \tfrac1{20}\ \text{是 Fejér 的天花板"）}\Longrightarrow\ \textbf{统一的论文更完整}✓✓（\text{比单独另写更值}）$$

---

## D. 交付物线（论文 A／B）

$$A：\lambda_n\ge0\ \text{对}\ 2\le n\le2T-O(1)\（\text{已编译}）✓\qquad B：\text{Droll 3.2.7}\ \tau{=}1\ \textbf{两条不等式均已成定理}（\text{C-179}）✓✓$$
$$\text{待办}：\text{Palojärvi 注记补}\ m{\ge}2\ \text{自足性（可引我方阻尼界）}✓\ \text{约 2--3 小时}✓$$

---

## E. 方法学资产线（跨项目可复用）

$$\text{① 四门证书协议}✓\qquad \text{② 证书附录（可独立复核清单）}✓\qquad \text{③ "数字}\to\text{证书"元目标（T16）}✓$$
$$\text{④ "域覆盖先于余量"（}\pi\ \text{端点薄片事件}）＋"用证明不用搜索"（粗网格失效事件）✓✓$$
$$\text{⑤ 负结果资产}：\text{NO-GO 地图 ＋ NEG-REGISTER（含类型标注）}✓$$

---

## 优先级建议（按"单位投入的信息产出"）

$$\textbf{①}\ \text{写 A 线论文}（\text{含 C 线一节}）\Longrightarrow\ \text{10 小时}\to\textbf{可提交草稿}✓✓\ \text{最高}✓$$
$$\textbf{②}\ \text{B 线短注}（\text{先补三项待核}）\Longrightarrow\ \text{10 小时}\to\textbf{可提交短注}✓$$
$$\textbf{③}\ \text{D 线收尾}（\text{Palojärvi 注记}\ m{\ge}2\text{）}\Longrightarrow\ 2\!-\!3\ \text{小时}✓\ \text{低成本高确定性}✓$$
$$\textbf{④}\ \text{阻尼}\ M{=}4\ \text{扩展} \Longrightarrow\ \text{计算型，边界价值低} \Longrightarrow\ \textbf{缓办}✓$$
$$\textbf{⑤}\ \text{突破分辨率墙／精确}\ C_3 \Longrightarrow\ \textbf{需新机制}，\text{列为独立研究项目}✗\（\text{除非有外部需求}）$$

---

**边界**：本盘点为**成果与优先级登记**，不产新数学 ✓；A 线常数改进的**文献新颖性**仍需逐字核（Turán／Montgomery 原文无法获取，已用 Andersson 转引）✓；B 线新颖性已主动降级 ✓。
