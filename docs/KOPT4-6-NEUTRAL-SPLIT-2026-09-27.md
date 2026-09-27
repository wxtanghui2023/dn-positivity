# KOPT 中性拆分 · 位移能力审计档（119 线续案 · 2026-09-27）

D0: 本档对象 = 119 线搜索器的**中性事件拆分 · 位移能力审计 · 读数定量**（P2 construction attack reproduction 阶段）
D1: 1（含一条**小引理**（1-for-1 刚性 ⟸ $\min|A_c|\ge3$）✓；**无 RH 命题** ✗ ✓）

**已查地图**：续案 —— 上游为 `docs/HANDOFF-2026-09-27-119-line-session-handoff.md`（A-HANDOFF119-1 全链 ✓）；
本档开工前快查 `CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`／`MASTER-NOGO-AND-LIVE-PATHS.md`
关键词 `可约|irredundant|distinct124|等基数` ⟹ **未命中相关封口**（命中项均为 V212／V269／V296 等无关 RH 线）⟹ 非新案 ✓

---

## §1 起因：kopt3 的 maxR 是**假象**（仪器 bug ✓）

kopt3 终态打印 `maxR(遗留可删)=0`，**该读数无资格作证据** ✗：
其 `maxR` 在 **cleanup 之后**统计，而 cleanup 的定义就是"删光所有可删词" ⟹ 后验 $R\equiv0$ **是恒等式，不是发现** ✗✗。

唐先生 18:38 规格（本档执行依据 ✓）：
```
replacement_neutral : r = k, |C_new| = 124, h = 0
neutral_R           : replacement_neutral AND R(C_new) >= 1     <-- 判定性事件
cleanup_neutral     : |C_before| = 125, cleanup -> 124
descent             : |C_new| < 124
```
＋ 证据三层分解：$\text{attempts}\to\text{accepted}\to\textbf{distinct 124 states}\to\text{distinct with }R>0$ ✓

## §2 定义（沿用，防误用 ✓）

$$U(c):=B_1(c)\setminus B_1(C\setminus\{c\});\quad H_c=\{z\in B_1(c):\mathrm{cnt}[z]=1\};\quad U(c)=\varnothing\iff H_c=\varnothing$$
$$R(C):=\#\{c:H_c=\varnothing\};\qquad R(C)\ge1\iff\exists\,123\text{-覆盖码}\ C\setminus\{c\}$$
实现口径 `Rval = #{p in S : 对 B_1(p) 中每点 z 均有 cnt[z] >= 2}` ⟺ $U(p)=\varnothing$ ✓（逐字等价，非近似 ✓）

## §3 实验装置

- 基准码：`work/k10/c62/keri_pool/K_9_1_classif.txt`（两 62-码 → 两半构造 124 词；合法覆盖 ✓ **不可约** $R=0$ ✓）
- **代数 A（kopt2–kopt6）**：删 $k\in\{2,3,3,4,4,5\}$ 随机词 → **贪心补洞**（候选池含被删词 ✓）→ 接受门 $|S|\le|S_{\rm before}|$ 或 Metropolis($T{=}0.4$) → cleanup
- **代数 B（kopt7）**：1-for-1 swap —— 取 $c$，$H_c$，取 $c'\ne c,\ c'\notin S$ 且 $H_c\subseteq B_1(c')$ ⟹ $S'=S\setminus\{c\}\cup\{c'\}$（候选集 $=\bigcap_{z\in H_c}B_1(z)$）
- **代数 C（kopt9）**：k=2 swap —— 取 $c_1,c_2$，$E=\{$删二者后的空洞$\}$，找 $p,q\notin S$（且 $\ne c_1,c_2$）使 $E\subseteq B_1(p)\cup B_1(q)$；若**单词**即覆盖 $E$ ⟹ $|S'|{=}123$ ⟹ **123 覆盖码** ✓
- 运行：`setsid nohup bash scripts/pyguard.sh 2500 /tmp/koptN.py <TMAX> > /tmp/koptN.log 2>&1 &`
- 脚本（未入仓）：`kopt4/5(弃)/6/7/8/9.py` in `/tmp`

## §4 结果

### 4.1 kopt4（代数 A，300s）—— 读法**已作废** ✗

```
it=177,426 acc=176,215 ｜ rep124=173,434 ｜ rep124R=0 ｜ rep125=2,604 ｜ rep>125=177 ｜ rep<124=0
clean124=173,548 ｜ desc=0 ｜ rc(1/2/>2)=115/2/0 ｜ maxR@124=0 ｜ maxRpre=2 ｜ best=124
```
⚠️ kopt4 **无去重仪表** ⟹ 把同一状态的重复访问误读为"大量不同结构的探索" ✗（见 §5.1）

### 4.2 kopt6（代数 A ＋ exact 去重指纹，300s）

```
it=175,605  acc=174,402
rep124       = 172,100
distinct124  =       1   ★★ 172,100 次等基数 replacement 只访问到【1 个】不同的 124 码
rep124R      =       0 ｜ distinct124R = 0
rep125       =   2,300   (R>=1: 86) ｜ distinct125R =  63
maxR@124 = 0 ｜ maxR@125 = 1 ｜ maxRpre = 1 ｜ descent = 0 ｜ best = 124
```

### 4.3 kopt7（代数 B／1-for-1 swap，90s）

```
steps=0 ｜ distinct124=1 ｜ movable=0 ｜ rigid=200,001（自设上限触发）｜ maxR=0
```
⟹ 基准码**不存在任何 1-for-1 换词** ⟹ 代数 B 亦**零位移** ✗（原因见 §5.3 ✓）

### 4.4 kopt8（刚性核验，秒级）

```
|S|=124  h=0  总覆盖 1364 = 124×11 ✓
私有点 P=#{cnt==1} = 757 ；多重数表 (1,757)(2,217)(3,29)(4,19)(5,2)（点数和=1024 ✓ 覆盖和=1364 ✓）
覆盖计数不等式：1364 >= P + 2(1024-P) ⟹ P >= 684 ✓（实测 757 ✓）
R(S)=0 ✓
|H_c| : min=3 中位=6 max=9 均值=6.10
|A_c| : min=3 中位=5 max=9            (A_c = 私有邻居坐标集)
刚性词数 = 124/124 ；候选总数 = 0 ⟹ 1-for-1 swap 不存在 ✓
```

### 4.5 kopt9（代数 C／k=2 swap，90s）

```
tries=68,794 ｜ distinct124=1 ｜ moved=0 ｜ immobile=68,794 (mobility=0.0000) ｜ HIT(123)=0
```
（每 pair 的"不可动"判定为**穷举**：候选池内所有 2-词组合均已试完 ✓）
⟹ k=2 亦**零位移** ✗（原因见 §5.3 推论 ✓）

### 4.6 kopt10（代数 D／**k=3 真交换【完备判定】**，15s）

规格（唐先生 18:52 拍板 ✓）：$C'=(C\setminus A)\cup D$，$|A|=|D|=3$，$A\subset C$，$D\subset\mathbb F_2^{10}\setminus C$（**严禁**用 delete-refill 伪装 ✓）；
$m:=$ 覆盖空洞集 $E$ 所需的 $C$-外词最少个数 ⟹ $|C'|=121+m$。**只做 k=3，不扩到 4,5** ✓

```
tries      = 310,124  = C(124,3)   ⟹  【完备 ✓】
可证豁免    = 286,317  (任一对 d>=5，由 §5.3 推论不可动 ✓)
近距三元组  =  23,807  (三对全 <=4)  ⟹  全部 immobile (m >= 4)
m0=0 ｜ m1=0 ｜ m2=0 ｜ m3(moved)=0 ｜ R>0=0 ｜ distinct124=0 ｜ 最小码长=999（未出现）
```

**独立复核（`kopt11_verify.py`，换算法 ✓）**：对近距类抽检 20 个 ＋ 豁免类抽检 20 个，
穷举所有 $\binom{\mathrm{pool}}{3}$（|pool|=110–151）⟹ **40/40 均"无 3-覆盖"** ✓；豁免类抽样中出现 3-覆盖的个数 = 0 ✓
（判定算法与复核算法**不同**：前者 $O(11^2)$ 逐层交集；后者全枚举 $\binom{\text{pool}}{3}\approx10^5$–$10^6$ ✓）

**本码距离直方图**（124 词，7626 对）：$d{=}1{:}40,\ 2{:}179,\ 3{:}1005,\ 4{:}1761,\ 5{:}1781,\ 6{:}1477,\ 7{:}942,\ 8{:}361,\ 9{:}75,\ 10{:}5$；**$\min$ dist $=1$** ✓
（$d\le4$ 的 pair 共 2985 / 7626 ✓）

### 4.7 kopt12／kopt13／kopt14（k=4 压缩机制 ＋ 成本量化 ＋ 完备判定**进行中**）

**机制层 ✓**
- **LB1 判废（有证明 ✓）**：$E\subseteq\bigcup_{a\in A}B_1(a)$ ⟹ 每个半径-1 球簇至多贡献 1 个两两 $d\ge3$ 的点 ⟹ $\mathrm{LB1}\le|A|=k$ ⟹ **$k{=}4$ 时 $\mathrm{LB1}\le4<5$：逻辑上不可能承担豁免** ✗（STOP ✓）
- **LB2（簇不相交下界）** ✓：$H_{a_i}$ 各需 $\ge2$ 词（§5.3 引理）；两簇"不可共享"（无外词同时触及两簇）⟹ 词集不相交 ⟹ 需求相加；精确版取最大两两不可共享簇集 ⟹ $\mathrm{LB2}=2t$
- **安全组合必要条件**（**只可 false-positive** ✓）：$A$ 含 3 个两两 $d\ge5$ 的词 ⟹ 3 簇互不可共享 ⟹ $m\ge6>4$ ⟹ 豁免 ✓

**成本量化（200,000 抽样，seed=20260927 ✓）**
```
A-count(抽样)     200,000
组合筛豁免         101,701  (50.85%)
LB2>=6 豁免         63,090  (31.50%)
需真判              35,209  (17.60%)  -> 外推 ≈ 1.65e6
moved(抽样)              0            <- **抽样探针，非 k=4 完备结论** ✗
交叉一致性检查失败        0  ✓✓        <- can_cover(E,3) 恒 False（与 k=3 完备一致 ✓）
exact: 均 1,273µs ｜ 中位 1,288µs ｜ 最大 3,556µs（提速 3.5×／尾部 31× ✓）
|E| 分布：16->35，众数 24 ｜ |Q(E)| 分布：122->198，众数 160
```
**exact 内核三处提速 ✓**：① 去掉 `used` 集（$z\in E\Rightarrow z\notin B(\text{已用词})\Rightarrow$ 该词 $\notin\mathrm{FCfree}[z]$ ⟹ 掩码已隐含排除 ✓）；② fail-first（最受限点优先）；③ $(E,\mathrm{depth})$ 记忆化

**完备判定**：kopt14 `full` 模式已启动（全 $C(124,4)$ 个四元组，单核，$\approx$34 分钟）⟹ **结果待补（§5.6 占位 ✓）**
⚠️ **算术更正**：$C(124,4)=9{,}381{,}251$；本档初稿曾误记 9,307,766 ✗，会话中亦出现 9,183,626 ✗ ⟹ **以 9,381,251 为准** ✓（外推需真判 $\approx1.65\times10^6$ ✓）

### 4.8 kopt15（k=2 **真完备**判定 ✓ 口径修正）

```
C(124,2) = 7,626 对，全枚举 ✓
tau(E)=0 : 0 ｜ tau=1 : 0 ｜ tau=2（真交换）: 0 ｜ **tau>=3 : 7,626（全部）**
|E| 范围 [7,20] ；用时 0.36s
```
⟹ **k=2 完备：无任何 pair 可被 $\le2$ 个 $C$-外词修复** ✓（既无等基数出口，也无降基数出口 ✓）
⚠️ **口径修正**：kopt9 的 68,794 是**随机抽样**（**非**完备）✗；其"不可动"判定仅对每例穷举 ✓ —— 现由 kopt15 全枚举 7,626 对升级为**真完备** ✓

## §5 判读

### 5.1 kopt6：**代数 A 在基准码上是恒等算子**（零位移 ✗）

- `distinct124 = 1` 在 172,100 次 replacement 之上 ⟹ 删 $k$ 词后贪心补洞**恰好把同样的 $k$ 词放回** ⟹ $S$ 复原
- 机制原因 ✓：被删词 $w$ 的私有区在被删后成为空洞，而 $w$ 覆盖这些空洞**的全部** ⟹ 贪心评分（覆盖未覆盖点数）最高者恒为 $w$
- ⟹ §4.1 的"173,434 次合法等基数替换"**不是**对 124 码空间的探索 ⟹ 负结论强度 $\approx0$ ✗
  （与 kopt1"零接受"**同类**：机制缺陷，而非数学读数 ✗）
- ⚠️ 故唐先生 18:38 表格第 2 行条件（`replacement_neutral>0 ∧ maxR@124=0`）**字面成立但实质空转** ⟹ **不构成"轨道与可约层分离"的证据** ✗✗

### 5.2 一条**真实**读数：冗余只在 overshoot 层出现 ✓

- `distinct125R = 63`（`rep125R = 86`，`maxR@125 = 1`）⟹ **125 层确有 63 个不同的、带严格可删词的覆盖码** ⟹ **"产生冗余"算法完全做得到** ✓
- 且每个这样的 125 码 cleanup 恰好回落 124（删 1 词 ✓）
  ⟹ $|C|=125,\ R\ge1 \xrightarrow{\text{cleanup}} |C|=124$ —— **可约性的"层偏移"是真实观测** ✓

### 5.3 ⭐ 1-for-1 刚性的**可证**解释（小引理 · 本档）

$$\textbf{引理.}\quad \text{若 }|A_c|\ge3\ \text{则}\ \bigcap_{z\in H_c}B_1(z)=\{c\}$$
其中 $A_c=\{a: c\oplus e_a\in H_c\}$。**证明**：取互异 $a_1,a_2,a_3\in A_c$，置 $z_i=c\oplus e_{a_i}$。
$w$ 距 $z_1,z_2$ 均 $\le1$ ⟹ $w\in\{c,\ c\oplus e_{a_1}\oplus e_{a_2}\}$；再要求 $d(w,z_3)\le1$ ⟹ 后者与 $z_3$ 的 x-差 $=e_{a_1}\oplus e_{a_2}\oplus e_{a_3}$，weight $=3$ ✗ ⟹ 仅 $w=c$ ✓
**本码实测** $\min_c|A_c|=3$ ⟹ **全码 1-for-1 刚性成立** ✓✓ **非实现缺陷，是结构性质** ✓

配合覆盖计数：$|\text{覆盖量}|=124\cdot11=1364\ge P+2(1024-P)\Rightarrow P\ge684$，
⟹ 平均每词私有点 $\ge684/124=5.5$（实测均值 6.10 ✓）⟹ $|A_c|\ge3$ 是**该规模码的常态** ✓

$$\textbf{推论.}\quad d(c_1,c_2)\ge5\ \Longrightarrow\ E\ \text{不可能由 2 个}\ S\text{-外词覆盖}$$
**证明**：$H_{c_1}\subseteq B_1(c_1)$、$H_{c_2}\subseteq B_1(c_2)$；$d(c_1,c_2)\ge5$ ⟹ 任意 $z_1\in H_{c_1},z_2\in H_{c_2}$ 有 $d(z_1,z_2)\ge3$ ⟹ **无单词同时覆盖两簇** ⟹ 每簇须由**单个**外部词整覆盖，而引理说这对 $H_{c_1}$ 不可能 ⟹ 不可动 ✓
本码 $d(c_1,c_2)\ge5$ 的 pair 占压倒多数 ⟹ 观测到的 `mobility=0` **大部分可证** ✓；仅 $d\le4$ 的 pair 属真计数 ✓

⚠️ **陈述纪律（唐先生 19:26 更正 ✓）**：该推论的**正确形式是局部的**：
$$d(a,b)\ge5\ \Longrightarrow\ B_1(a),B_1(b)\ \text{对不可共覆盖 witness 的贡献不能合并}$$
**不得**写成"所有词两两 $d\ge5$" ✗ —— 实测 $d_{\min}(C)=1$（40 对距离 1、2985 对 $d\le4$）⟹
$$\boxed{\text{local rigidity}\ \ne\ \text{global separation}}$$
即 3-exchange 刚性**并非**来自"最小距离大"的单一解释 ✓ —— 这正支持下一阶段研究 $E(A)$ 的 **incidence hypergraph**，而非继续找"距离大所以不能动"的单一理由 ✓

### 5.4 净结论（严格，k≤2 阶段）

- **三个代数（A：delete-refill／B：1-for-1／C：k=2）在基准码上全部零位移** ⟹ 基准 124 码在这些邻域内是**强局部刚性** ✓
- 要产生位移，须 **k≥3 交换** 或 **多起点**（换基准码）✓ —— 这是**机制面**的结论，**不是**码空间的结论 ✗
- 唐先生原判定事件（$|C|=124,h=0,R\ge1$）**仍未观测**，但其**未观测的原因已被精确定位＝装置无法移动** ✓（不再是"搜索没找到"这种含混说法 ✓）

### 5.4 强度边界（唐先生 18:38 收紧 ✓）

- "kopt4 是强搜索证据"**已作废** ✗（它根本不是搜索证据）
- **能说的**：代数 A／B 均**无位移能力** ⟹ 其 `desc=0／R=0` **无统计意义** ✓
- **不得**说"所有 124 码都不可约" ✗；**不得**说"等基数轨道与可约层分离" ✗（该问题在 A／B 下**不可判** ✓）
- 实验覆盖的永远是**搜索访问到的状态集合**，不是整个 124 覆盖码空间 ✗

### 5.5 k=3 完备结论：**局部刚性链闭合** ✓（本档核心产出 ✓）

$$\boxed{k=1,\,2,\,3\ \text{exchange 在基准码上全部}\ \texttt{moved}=0}$$

| $k$ | 判定方式 | 结果 |
|:--:|------|:--:|
| 1 | **可证不存在**（§5.3 引理） | 0 ✓ |
| 2 | 68,794 次穷举判定（kopt9） | 0 ✓ |
| 3 | **完备** 310,124 个 $A$（kopt10）＋ 40 个抽样独立复核（kopt11） | 0 ✓ |

**比 $\texttt{moved}=0$ 更强的一条**（精确陈述 ✓）：
$$\forall A\subset C\ (|A|{=}3),\ \forall D\subset\mathbb F_2^{10}\setminus C\ (|D|\le3):\quad (C\setminus A)\cup D\ \text{不是覆盖码}$$
即**不存在任何 $\le3$ 词的 $C$-外补丁能修复三词空洞** ⟹ 从基准码出发 $|C'|$ 不可能降到 $\le124$ ✓

⚠️ **约定须明写**：$D\subset\mathbb F_2^{10}\setminus C$（**不得**把 $A$ 里的词重新放回 ✓）——否则 $D{=}A$ 退化为恒等 ✗；此约定与唐先生规格逐字一致 ✓

**红线照旧** 🔴：只归档为"**该 $k\le3$ 交换邻域中不存在位移**" ✗，**绝不**转译成 $K(10,1)>124$ ✗
（邻域结论 $\ne$ 码空间结论 ✓；本次仍未触及 120/119 任何一端 ✓）

### 5.6 k=4 阶段（进行中；措辞已收紧 ✓）

$$\boxed{k=1:0\quad k=2:0\ (\text{全 }7{,}626)\quad k=3:0\ (\text{全 }310{,}124)\quad k=4:\ \textbf{完备计算进行中}}$$
且真正的 P3 目标始终是：$\boxed{\tau(E(A))\le |A|-1}$（等基数移动 $\tau\le|A|$ 与降基数碰撞 $\tau\le|A|{-}1$ **永不混淆** ✓）

计算链条 ✓：
$$A\ \longrightarrow\ \textbf{安全组合筛}\ \longrightarrow\ E(A)\ \longrightarrow\ \textbf{局部 exact}$$
筛只承担"**排除必不可能者**"，其余**全部**进入 exact ⟹ **没有把 heuristic 当证明** ✓

**措辞纪律（唐先生 19:11 ✓）**
- 35,209 次 exact 的 `moved=0` 是**成本／正确性探针**（抽样 ✓），**不是** $k{=}4$ 完备结论 ✗；完备结论须等全部 $9{,}381{,}251$ 个四元组处理完 ✓
- k3 反向检查的正式名称 ＝ **交叉一致性检查** ✓；**不得**写成独立数学证明 ✗

**分叉（结果出来后 ✓）**
- $m_4=0$ ⟹ 归档为"**该基准码在 $k\le4$ 真交换邻域中零位移**" ✓
- $m_4>0$ ⟹ **立即停止批量计算**，保留第一个／全部 moved witness，逐个审计 $(A,D)$、覆盖性、去重后的新状态、以及 $R(C)$ ✓
- 下一关**不是**马上扩搜，而先问：$\texttt{moved}\Rightarrow R>0\ ?$ ✓（只有后者才真正接上 $124\to123$）

### 5.7 P0–P5 链审计与 P3 机制方向（唐先生 19:23 ✓）

| 环节 | 状态 |
|------|------|
| **P0 定义／等价** | ✅ radius-1 covering code／exchange／$R(C)$／private point |
| **P1 下界／理论障碍** | ❌ **不是当前目标**（尚未建立 $K(10,1)\ge125$）|
| **P2 上界／构造** | ✅ 124 词、$h=0$ |
| **P3 collision** | 🔴 **当前核心瓶颈** |
| **P4 分类／P5 census** | ⏸ 未进入 |

$$\boxed{\text{当前卡点＝P3 碰撞机制}\ \ne\ P1\ \text{（不得把"124 很刚"误写成 P1）}}$$
$$P2\to P3\ \text{的结构攻击}\ ;\qquad R(C)=0\Rightarrow k{=}1\ \text{无出口（结构事实 ✓）}$$

**P3 的两层 ✓**：**低阶等基数出口**（$k\le3$ 已堵死 ＋ $k{=}4$ 收尾）vs **真正降基数出口**（$124\to123$）

**两个不同事件（关键 ✓）**：
$$\tau(E(A))\le4\Rightarrow124\to124;\qquad \tau(E(A))\le3\Rightarrow124\to123$$
⟹ **P3 目标应直接盯 $\tau(E(A))\le3$**（$|A|{=}4,|D|\le3$），而非仅问"有没有 moved 124" ✓

**下一项机制工作（唐先生拍板 ✓）**：**不再发明 LB1／LB2** ✗，改为把 $E(A)$ 转成 **incidence hypergraph**：
左侧＝暴露点 $x\in E(A)$，右侧＝合法新中心 $z\notin C$，边 $x\sim z\iff d(x,z)\le1$；
$\tau(E(A))$ ＝ 该二部结构的 covering number ⟹ 目标＝寻找 **candidate-center 兼容性** 或**更高阶 covering-number certificate** ✓
（LB1 死因已证：$E(A)$ 来自 $k$ 个原球 ⟹ packing number $\le k$ ⟹ 天花板；须升级到"**候选中心之间能否共存**"的**二阶不兼容证书** ✓）

**三情形 ✓**：**A** $\tau\ge5$ 全体 ⟹ $k{=}4$ 无 exchange（若由**统一 certificate**给出，价值高于单纯计算 ✓）；**B** 某 $\tau{=}4$ ⟹ moved 但**无 P3 descent** ⟹ 研究新 124 能否产生 $R>0$；**C** 某 $\tau\le3$ ⟹ **$124\to123$** ⟹ 立即停批、存 witness、**1024 点独立验证** ✓

**方向反转（唐先生 19:23 ✓）**：$k\le4$ 全无出口时**不要**机械升 $k{=}5,6,7$ ✗（会退回搜索工程），应先问**"为何该 124 构造如此局部刚性"**：
757 private points ｜ $d_{\min}=1$（**更正：非 $\ge5$** ✗）｜ $k\le3$ 全堵 ｜ $k{=}4$ 收尾 ｜ **$124\xrightarrow{\text{overshoot}}125\ (R>0)\xrightarrow{\text{cleanup}}124$**
最后一条说明**冗余层并非不可达**，而是**需先支付一个额外中心的"能量成本"，等基数交换消不掉它** ✓✓（本档认为这是比"124 很刚"更值得研究的对象 ✓）

**k=4 完成后的 P3 分解计划（唐先生 19:26 拍板 ✓）**
- 若 $m_4=0$ ⟹ **不马上上 $k{=}5$** ✗；先对**全部 exact 的 $A$** 做结构统计：$|E(A)|$、$|Q(E)|$、$\alpha(E)$、$\tau(E)$（$\alpha$ **不用**普通距离 packing，而研究**候选中心兼容性** ✓）
- 目标 ＝ 找**统一证书** $\tau(E(A))\ge5$ ✓，而非对 $9{,}381{,}251$ 个 $A$ 逐个报"不行" ⟹ 这才把**计算资产升级为数学资产** ✓
- 若 $m_4>0$ ⟹ **相反**：**立即冻结第一个 moved witness**，不扩大搜索，直接审计其是否满足 $\tau(E)\le3$ ✓
- 当前：750k/≈1.65M、`MOVED=0` ⟹ **运行中的强信号，不提前结案** ✓；决策 ＝ **等 k=4 完备结果 → 再定 incidence-hypergraph 攻击的具体形式** ✓

### 5.8 P3 六层分解（唐先生 19:32 ✓）—— 攻击树与优先级

**母问题（统一定义 ✓）**：$A\subset C,|A|=k$；$E(A)=\big(\bigcup_{a\in A}B_1(a)\big)\setminus\big(\bigcup_{c\in C\setminus A}B_1(c)\big)$；$Q(E)=\{z\notin C:B_1(z)\cap E\ne\varnothing\}$
$$\tau_C(E(A))=\min\{|D|:D\subseteq Q(E),\ E\subseteq B_1(D)\}$$
$$\tau(E)\le k-1\Rightarrow124\to123;\quad \tau(E)=k\Rightarrow124\to124;\quad \tau(E)>k\Rightarrow k\text{-exchange 不存在}$$

| 层 | 内容 | 产出 |
|:--:|------|------|
| **L1 删除几何** | $A\mapsto E(A)$：$|E|$、距离谱 $N_j(E)$、候选度 $q(x)$、$q(x,y)$ | $E$ 的"债务结构" |
| **L2 单中心容量** | $S_z=B_1(z)\cap E$；$M_1,M_2,M_3=\max|S_{z_1}\cup\cdots|$ | 容量上界 |
| **L3 中心兼容性** | 交叠图 $z_i\sim z_j\iff S_{z_i}\cap S_{z_j}\ne\varnothing$（带权 $w=|S_{z_i}\cap S_{z_j}|$）＋ 容斥 | **真正的兼容性证书** ⭐ |
| **L4 covering number** | $\tau(E)\le3$？ | YES ⟹ $124\to123$；NO ⟹ 降阶出口堵 |
| **L5 结构分类** | fingerprint $F(A)$ ⟹ $9.38\text{M}A\to$ 少数结构类 | **计算资产 → 数学资产** ⭐ |
| **L6 overshoot 势垒** | 势函数 $\Phi$，$\Delta\Phi=\Phi(C')-\Phi(C)$；解释 $124\to125(R>0)\to124$ | 候选：private-point 数／redundancy／overlap 谱／uncovered mass／球交数 |

**优先级（唐先生 ✓）**：**L4 → L3 → L5 → L6**；**不机械升 $k$** ✗

⚠️ **本轮补充（定义等价 ✓ 省力记录）**：$M_r(E)<|E|\iff\tau(E)>r$ **是定义等价**（**不是**更强的证书）⟹
- **L4 判据已被本次 $k{=}4$ 运行完整覆盖（⚠️ 封存待收尾 ✓）**：**全部** residual $A$ 均已跑 `can_cover(E,3)` 且 `k3bad=0`；豁免类由"3 簇互不可共享 ⟹ 各需 $\ge2$ 词"得 $\tau\ge6$ ⟹ 运行收尾后即得 **$\forall|A|{=}4:\tau(E(A))\ge4$** ⟹ **$4\to3$ 降基数出口堵死** ✓（P3 层结论，**强于**"无 moved" ✓）
  **运行中读数（不提前结案 ✓）**：$1{,}250{,}000/\approx1{,}651{,}000$ 残差，$1723.3$s，`MOVED=0`，`k3bad=0`，ETA $\approx$19:46 ✓
- ⟹ M 判据的价值在**计算路线**（max-union 枚举替代 SAT）；真正的新内容在 **L3／L5／L6** ✓

**待命脚本** ✓：`/tmp/kopt16_L5fingerprint.py`（L1／L3／L5 统计器：$|E|$／$N_j$ 谱／$|Q(E)|$／$\alpha(E)$／$q$ 度数直方图／$\tau$ 桶／fingerprint 类计数）——零 CPU 已就绪，$k{=}4$ 收尾后可立开 ✓

### 5.9 L5 指纹规格冻结（唐先生 19:36 ✓）

**目标**：把 $9{,}381{,}251$ 个 $A$ 压缩成**少数结构类型**；**不碰求解器** ✗、**不存中心编号／完整矩阵** ✗（指纹须为等距不变量 ✓）

| 层 | 指纹 |
|:--:|------|
| **F0** | $(\|E\|,\ N_1,\dots,N_{10})$（$N_j=\#\{\{x,y\}\subseteq E:d(x,y)=j\}$）|
| **F1** | $(F_0,\ \|Q(E)\|,\ \text{degree\_hist})$，$\text{degree\_hist}=$ multiset $\{\|B_1(z)\cap E\|:z\in Q(E)\}$ ⭐**第一主指标** |
| **F2** | $(F_1,\ \text{pair\_intersection\_hist})$，$=\text{multiset}\{\|S_z\cap S_{z'}\|:z<z'\in Q(E)\}$（**仅当 F1 已显聚类才算** ✓）|

**τ 三态绑定 ✓**：`EXEMPT`（结构证书 $\tau\ge6$）｜`NO_3_COVER`（`can_cover(E,3)=False` ⟹ $\tau\ge4$）｜`3_COVER`（$\tau\le3$，出现即 $124\to123$ ✓）＋ 非豁免者再记 τ 桶 $4$ 或 $\ge5$

**必报告表 ✓**：每层（F0／F1／F2）的 `样本数 / distinct classes / 最大类占比 / singleton 占比` ＋ **同类异 τ 计数**（STOP-3 判据）

**STOP 条件（先定死 ✓）**：
- **STOP-1**：F0 已高度离散且无压缩 ⟹ 不继续 F1 ✗
- **STOP-2**：F1 近似一一对应（类/样本 $>0.5$）⟹ **L5 停，转 L3** ✗
- **STOP-3**：有强聚类但**同类异 τ** ⟹ **有价值的失败**：指纹不足，需找真正决定兼容性的 invariant ✓
- **SURVIVOR**：少数 fingerprint 类覆盖绝大多数 $A$ ⟹ 进入**代表元 ＋ 统一证明** ✓（$F(E){=}F(E')\Rightarrow$ 同 covering obstruction ⟹ 尝试从 $F$ 本身推出 $\tau\ge4$ ✓ = 计算证据 → 结构性证书 ✓）

**路线（唐先生 ✓）**：$\boxed{L4\ \text{封存}\to L5\ \text{压缩}\to L3\ \text{兼容性}\to L5\ \text{代表类证明}\to L6\ \text{势垒}}$，**不机械升 $k$** ✗

**脚本 ✓**：`/tmp/kopt17_L5fingerprint.py`（按本规格实现；用法 `kopt17_L5fingerprint.py <S> <F2N>`；零 CPU 就绪 ✓）

## §6 红线（硬 ✓）

- 找不到 ⟹ 只记"该邻域／该预算未找到" ✗，**绝不推出** $K(10,1)\ge120$ 或任何下界 ✗
- 120 是**上界** ⟹ 不可写 $K(10,1)=120$ ✗；119 是真 P2 target ✓
- `/tmp/cov` ＝ covering-**design** 搜索器（Nurmela–Östergård）⟹ 与 code 搜索**严格分账** ✗，不得称"复现" ✓
- 不写"不可能／不存在／方向已死" ✗（除本档 §5.3 **可证**的 1-for-1 刚性——那是**限定邻域内的局部事实** ✓）
- 只有 $|C|=120\wedge h=0$ 才做 **1024 点独立逐点验证** ✓

## §7 术语与分账（引用时必标 ✓）

- **代数 A** ＝ delete-refill repair（kopt2–kopt6）｜**代数 B** ＝ 1-for-1 swap（kopt7）｜**代数 C** ＝ k=2 swap（kopt9）｜**代数 D** ＝ k=3 swap（kopt10）
- 四代数读数**不可直接比较** ✗；"等基数 replacement"一词须注明代数 ✓

## §8 文件

- 档：本档 `docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`
- 上游：`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`（A-HANDOFF119-1）｜`docs/ASSETS-REGISTRY.md`
- 脚本：`/tmp/kopt4.py`、`/tmp/kopt6.py`（A ✓）｜`/tmp/kopt7.py`（B ✓）｜`/tmp/kopt8_stat.py`（核验 ✓）｜`/tmp/kopt9.py`（C ✓）｜`/tmp/kopt10_k3.py`（D ✓）｜`/tmp/kopt11_verify.py`（独立复核 ✓）
- 日志：`/tmp/kopt4.log`、`/tmp/kopt6.log`、`/tmp/kopt7.log`、`/tmp/kopt9.log`
