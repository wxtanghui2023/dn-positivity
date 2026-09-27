# R5-2026-09-27 — 三点层**可证伪实验**：$U(a,b,c)$ 精确值 ＋ **精确全局恒等式** ＋ 强制三角形

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:30 令 ✓）**：**切实推进**（不是诊断）：把三点层做成有限可证伪实验，并与全局资源 $1024/1309/285$ 接上 ✓；**零程序计算**（全部由公式解析完成 ✓）。

**已查地图：★ 命中两档直接相关（必须对照 ✓✓）**
所查并**已核**：`docs/FIBER-2026-09-26-boolean-fiber-and-the-third-order-invariant.md`（**三阶不变量 $\sum_xP(x)^2$ 不被二阶数据决定（带证人 ✓）**；$P(x)=\binom{S(x)}2$ 为**定义性** ✓；$\sum_x\binom{b(x)}2=2(N_1+N_2)\Rightarrow N_1+N_2=143$ ✓）｜`docs/TERM-2026-09-27-triple-neighbourhood-terminating-experiment.md`（**（BB-1）$n=4$ 全枚举 480 例 ⟹ 邻域结构（shell1+shell2）零变化 ⟹ 被完全决定 ⟹（BB-2）无独立杠杆 ⟹ 封存三阶耦合 ✗**；$n=5$ 局部搜索命中 0 例 ⟹ **无数据，不得断言不存在** ✓）｜`docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`（**STAR/TRI**）｜`docs/R4-P1b-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §6）
D0: 本档对象 ＝ **档案已有** 三点层对象的**可证伪实验与全局恒等式**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**新：$U$ 的精确值集、精确全局恒等式、三角形计数的 STAR-叉识别**；**并诚实标注与 FIBER／TERM 的重叠** ✓）
**[RESEARCH]**

---

## §0 结论（**三产出 ＋ 一处诚实降级 ✓**）

$$\boxed{\textbf{产出 1（精确值集 ✓）}:\ U(a,b,c):=|B_1(c_1)\cup B_1(c_2)\cup B_1(c_3)|\ \in\ \{\mathbf{28,29,31,33}\}\ ✓\ \Longrightarrow\ \text{浪费}\ 33-U\in\{0,2,4,5\}✓}$$
$$\boxed{\textbf{产出 2（精确全局恒等式 ✓✓）}:\ \mathbf{1024}=\mathbf{1309}-2(N_1+N_2)+T_3-T_4+\cdots\ \Longleftrightarrow\ \boxed{E=285=2(N_1+N_2)-T_3+T_4-\cdots}✓✓}$$
$$\boxed{\textbf{产出 3（强制事实 ✓）}:\ \text{任一 119-cover 有}\ \boxed{T_3(G_2)\ge1}\ ✓\ (\text{由 }Q\ \text{奇}\Longrightarrow\exists x:b(x)\ge3\Longrightarrow\ \text{三点同覆盖}\ \Longrightarrow\ \text{三角形}\ ✓)}$$
$$\boxed{\textbf{⚠️ 诚实降级}:\ \text{T3-b（三点层超二阶自由度）与档案 }FIBER\ \text{的"}\sum_xP(x)^2\ \text{不被二阶决定（带证人）"}\ \textbf{同型} ⟹ \textbf{本档不主张其为新}✗✓}$$

---

## §1 $U(a,b,c)$ 的**精确计算**（**产出 1**；零程序 ✓）

$$U=33-I_{12}-I_{13}-I_{23}+\tau\ ✓\qquad I_{ij}=|B_1(c_i)\cap B_1(c_j)|=2\cdot\mathbf 1[d_{ij}\le2]\ ✓;\qquad \tau=\mathbf 1[\max\le2]\ ✓\ (\text{R4-P1b §2})$$
$$\textbf{四情况（完备 ✓）}:\quad \text{三对皆 }\le2:\ U=33-6+1=\mathbf{28}✓\ \big|\ \text{恰两对}:\ U=33-4+0=\mathbf{29}✓\ \big|\ \text{恰一对}:\ U=33-2=\mathbf{31}✓\ \big|\ \text{零对}:\ U=\mathbf{33}✓$$
$$\Longrightarrow\ \textbf{三球并\textbf{永不小于 28}}✓\ \text{—— 故"并集太小"在单三元组层面\textbf{不产生矛盾}✗（\text{三球最多只"损失" }5\ \text{个入射}✓）}$$
$$\text{（\textbf{与唐先生的告诫一致 ✓}：仅靠三球自身不能制造 uncovered 点 ✓——容量账：余 }116\ \text{球}\ =1276\ \text{入射}\ \ge\ 1024-28=996✓\ \textbf{松}✗）}$$

## §2 **精确全局恒等式**（**产出 2；与三资源接上 ✓✓**）

$$H:=\bigcup_{c\in C}B_1(c)=H(\text{全空间})\ \Longrightarrow\ \text{包含排除（有限集，精确 ✓）}:\ |H|=\sum_{c}|B_1(c)|-\sum_{c<c'}I_{cc'}+\sum_{c<c'<c''}\tau_{cc''}-\cdots$$
$$\sum_c|B_1(c)|=11\cdot119=\mathbf{1309}✓;\qquad \sum_{c<c'}I_{cc'}=2(N_1+N_2)✓\qquad(\text{距离}\le2\ \text{的无序对每对 }2✓)$$
$$\sum_{c<c'<c''}\tau=\#\{\text{无序码字三元组}:\ \max(d)\le2\}=T_3(G_2)✓;\qquad T_4,\ T_5,\dots\ \text{同型（}k\ \text{阶交集和}✓)$$
$$\Longrightarrow\ \boxed{1024=1309-2(N_1+N_2)+T_3-T_4+T_5-\cdots}\ ✓✓\ \text{（\textbf{精确}，非估计 ✓；高阶项因 }\max d\ \text{有限而\textbf{自动截断} ✓）}$$
$$\text{等价形式（把 285 放到左边 ✓）}:\quad \boxed{E=285=2(N_1+N_2)-T_3+T_4-T_5+\cdots}\ ✓✓$$
$$\textbf{读数 ✓}:\ 285\ \text{＝"二阶层贡献}\ 2(N_1+N_2)\ \text{被三阶及以上\textbf{交替修正}"}\ ⟹ \textbf{三层全在同一恒等式上耦合}✓✓\ \text{（这正是唐先生要的"与 1024/1309/285 接上" ✓）}$$
$$\text{（与 R3 恒等式一致 ✓）}:\ 2(N_1+N_2)=285+\big(T_3-T_4+\cdots\big)\ \text{—— 与 R3-A §2 的"}\delta\text{-型恒等式"同源 ✓（本档给出其\textbf{组合意义} ✓✓）}$$

## §3 **强制三角形**（**产出 3 ✓**）＋ 精确三联恒等式

$$Q:=\sum_x\binom{\delta(x)}2\ \textbf{奇}✓\ (\text{档案链：}P=E+Q\ \text{且}\ P=2(A_1+A_2)\ \text{偶}\ ⟹\ Q\equiv E\equiv1\ (\!\!\bmod2))✓\ \Longrightarrow\ Q\ge1⟹\exists x:b(x)\ge3✓$$
$$\Longrightarrow\ \text{该 }x\ \text{的覆盖者中任取三者：两两距离}\le2⟹\text{三角形}✓\ \Longrightarrow\ \boxed{T_3(G_2)\ge1}✓✓\ (\text{\textbf{无条件}}✓,\ \text{对 }K(10,1)=119\ \text{的任何反设码成立}✓)$$
$$\text{精确三联恒等式（档案 ✓ 形式 ＋ 本档\textbf{修正}）}:\ \boxed{\sum_x\binom{b(x)}3=T_3(G_2)=Q+\sum_x\binom{\delta(x)}3}\ ✓✓\ \Longrightarrow\ T_3\ge Q\ \ge1✓✓$$

## §4 与档案的**逐项对照**（**诚实 ✓✓ —— 哪些是新、哪些是重述**）

| 本档项 | 档案状态 | 判定 |
|---|---|---|
| 三点层超二阶计数（$A\not\Rightarrow$ 三阶量） | `FIBER-2026-09-26`：$\sum_xP(x)^2$ **不被二阶决定（带证人 ✓）** | **同型 ⟹ 本档不主张为新** ✗✓ |
| triple 邻域局部结构 | `TERM-2026-09-27`：$n=4$ 全枚举 ⟹ 邻域结构**零变化** ⟹ **封存三阶耦合** ✗ | **已被封（但封的是"邻域结构"对象 ✓）**；$n=5$ 无数据（**不得断言不存在** ✓） |
| STAR/TRI 局部二分 | `KOPT4-6`（$k=4$ 局部证书线） | 已有 ✓ |
| **$U(a,b,c)$ 精确值集 $\{28,29,31,33\}$** | 未见 | **新增 ✓** |
| **精确全局恒等式 $1024=1309-2(N_1+N_2)+T_3-T_4+\cdots$** | 未见（R3 有同源 $\delta$-型恒等式，但**无此组合解释**） | **新增 ✓✓** |
| **强制事实 $T_3(G_2)\ge1$** | 未见（$Q$ 奇已知，但**未转成三角形计数**） | **新增 ✓** |
| 三角形 ＝ **STAR-叉**（两距离-2 邻居共享恰一个坐标 ✓） | `KOPT4-6` 有 STAR 但**未与 $T_3$ 相连** | **新增（桥接）✓** |

$$\textbf{故本档的真实增量 ✓}:\ \textbf{(i)}\ U\ \text{值集};\ \textbf{(ii)}\ \text{全局恒等式};\ \textbf{(iii)}\ T_3\ge1\ \text{与 STAR-叉桥接}\ \text{—— 三点层的"}\textbf{计数表述}"（此前只有"邻域表述" ✓）}$$

## §5 下一步（**本路线的真实缺口，具体 ✓**）

$$\text{恒等式给出：}T_3\ \text{与}\ N_1+N_2\ \text{被同一个 285 绑住 ✓};\ \text{要产生}\ \bot,\ \text{须：}\ \exists\ \text{两侧夹逼}:\ \underbrace{T_3\ge L}_{\text{covering 迫使}}\ \wedge\ \underbrace{T_3\le U}_{\text{其它必要约束}}\ \wedge\ L>U✓$$
$$\text{候选上界 }U\ \text{的来源（本档提出 ✓）}:\ \textbf{(a)}\ \text{R4-P1 的局部占用预算}\ \sum_c|S(c)\cup V(H_c)|\le451✓;\ \textbf{(b)}\ \text{恒等式自身的可行性（}N_1+N_2\in[143,459]✓）;\ \textbf{(c)}\ \text{STAR-叉结构：}T_3\le\#\{\text{共享坐标的对}\}✓$$
$$\text{候选下界 }L\ \text{的来源}:\ \text{目前仅有 }\ \ge1\ (\text{弱 ✗});\ \text{需要更强的"覆盖迫使三角形"论证 ⚠️——\textbf{这是本路线的真缺口}✓}$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "并集恒等式"
技术词 并集恒等式      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "STAR 叉"
技术词 STAR 叉        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "三阶耦合"
技术词 三阶耦合        命中文件数=6    :: ./FIBER-2026-09-26-boolean-fiber-and-the-third-order-invariant.md ./RESEARCH-CONSTITUTION.md ./TERM-2026-09-27-triple-neighbourhood-terminating-experiment.md
$ bash scripts/tech_word_check.sh "浪费分解"
技术词 浪费分解        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "包含排除恒等式"
技术词 包含排除恒等式  命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`并集恒等式`／`STAR 叉`／`浪费分解`／`包含排除恒等式` 命中 0 ⟹ 本档自造标签，作结构命名，**不作新性主张** ✓；`三阶耦合`（6 档）为档案已有 ✓ —— 正因命中，本档做了 §4 逐项对照 ✓✓）
- **注 ✓**：本档实质＝**§1 $U$ 值集 ＋ §2 全局恒等式 ＋ §3 强制三角形 ＋ §4 诚实对照**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓（全部解析 ✓）；**未碰** $\mu$／PSD／SAT／124-deletion ✓；**未上 Terwilliger** ✗；**未开门②** ✓；**未改门** ✓
- **不声称** $K(10,1)\ge120$ ✗（V290）；**不声称** 三点层必然破局 ✗ —— 只给恒等式 ＋ 强制事实 ＋ 缺口定位 ✓
- **§4 的诚实对照必须与该恒等式一同引用** ✓（防把重述当新 ✗）
- §2 的高阶项 $T_4,T_5,\dots$ **确为有限**（$k>11$ 时相交为空 ⟹ 截断 ✓），故恒等式**精确** ✓
