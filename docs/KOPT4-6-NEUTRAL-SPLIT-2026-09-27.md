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

### 5.4 净结论（严格）

- **三个代数（A：delete-refill／B：1-for-1／C：k=2）在基准码上全部零位移** ⟹ 基准 124 码在这些邻域内是**强局部刚性** ✓
- 要产生位移，须 **k≥3 交换** 或 **多起点**（换基准码）✓ —— 这是**机制面**的结论，**不是**码空间的结论 ✗
- 唐先生原判定事件（$|C|=124,h=0,R\ge1$）**仍未观测**，但其**未观测的原因已被精确定位＝装置无法移动** ✓（不再是"搜索没找到"这种含混说法 ✓）

### 5.4 强度边界（唐先生 18:38 收紧 ✓）

- "kopt4 是强搜索证据"**已作废** ✗（它根本不是搜索证据）
- **能说的**：代数 A／B 均**无位移能力** ⟹ 其 `desc=0／R=0` **无统计意义** ✓
- **不得**说"所有 124 码都不可约" ✗；**不得**说"等基数轨道与可约层分离" ✗（该问题在 A／B 下**不可判** ✓）
- 实验覆盖的永远是**搜索访问到的状态集合**，不是整个 124 覆盖码空间 ✗

## §6 红线（硬 ✓）

- 找不到 ⟹ 只记"该邻域／该预算未找到" ✗，**绝不推出** $K(10,1)\ge120$ 或任何下界 ✗
- 120 是**上界** ⟹ 不可写 $K(10,1)=120$ ✗；119 是真 P2 target ✓
- `/tmp/cov` ＝ covering-**design** 搜索器（Nurmela–Östergård）⟹ 与 code 搜索**严格分账** ✗，不得称"复现" ✓
- 不写"不可能／不存在／方向已死" ✗（除本档 §5.3 **可证**的 1-for-1 刚性——那是**限定邻域内的局部事实** ✓）
- 只有 $|C|=120\wedge h=0$ 才做 **1024 点独立逐点验证** ✓

## §7 术语与分账（引用时必标 ✓）

- **代数 A** ＝ delete-refill repair（kopt2–kopt6）｜**代数 B** ＝ 1-for-1 swap（kopt7）｜**代数 C** ＝ k=2 swap（kopt9）
- 三代数读数**不可直接比较** ✗；"等基数 replacement"一词须注明代数 ✓

## §8 文件

- 档：本档 `docs/KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md`
- 上游：`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`（A-HANDOFF119-1）｜`docs/ASSETS-REGISTRY.md`
- 脚本：`/tmp/kopt4.py`、`/tmp/kopt6.py`（A）｜`/tmp/kopt7.py`（B）｜`/tmp/kopt8_stat.py`（核验）｜`/tmp/kopt9.py`（C）
- 日志：`/tmp/kopt4.log`、`/tmp/kopt6.log`、`/tmp/kopt7.log`、`/tmp/kopt9.log`
