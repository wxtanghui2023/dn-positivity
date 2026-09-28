# WITCASC-2026-09-28 — **级联引理（无条件）＋ 终止二择 ＋ 为何仍不产生矛盾**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:14 令 ✓）**：攻击级联的真正问题 —— 强制出的高层码字之间能否产生**排斥／容量不足**；**零程序计算** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-433／C-432／C-410，非新案 ✓）**
`docs/WITCOV-2026-09-28-…`（**强制高层覆盖定理 ＋ 级联登记** ✓✓）｜`docs/P1-MICRO-2026-09-27-…`（**$(\alpha)$ 原文与证明** ✓✓）｜`docs/P1-AVOID-…`（**avoidance 接口** ✓✓）｜`docs/R7-LOCK-…`（**四族分解／realized K₄** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（见 §5）
D0: 本档对象 ＝ **档案已有** 级联／forced-tower 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出无条件级联引理（$4\le k\le9$）＋ $k{=}10$ 终止二择 ＋ 与 witness 定理的统一 ＋ 无矛盾的精确原因** ✓）
**[RESEARCH]**

---

## §0 结论（**级联引理 ✓✓｜终止二择 ✓✓｜统一 ✓✓｜无矛盾 ⚠️**）

$$\boxed{\textbf{(1) ★★一般级联引理（新 ✓✓，\textbf{无条件}、不需 }(\alpha)\text{、不需 }R{=}0\text{）}:\ \text{设 }W\subseteq[10],\ 4\le|W|=k\le9✓}$$
$$\qquad c\oplus e_W\notin C\quad\wedge\quad \forall i\in W:\ c\oplus e_{W\setminus i}\notin C\quad\Longrightarrow\quad \exists\,j\notin W:\ \boxed{c\oplus e_{W\cup j}\in C}\ \ ✓✓$$
$$\qquad\textbf{证明（4 行 ✓）}:\ \text{点 }p:=c\oplus e_W\ \text{须被覆盖 ✓；其 1-邻点恰两类：}\ p\oplus e_j=\begin{cases}c\oplus e_{W\setminus j}\ (j\in W✓\ \text{—— 假设排除 ✗})\\ c\oplus e_{W\cup j}\ (j\notin W✓)\end{cases}$$
$$\qquad\text{（外加 }p\ \text{自身 —— 亦被假设排除 ✗）} \Longrightarrow \textbf{唯一出路 ＝ }j\notin W\ \text{的一类}✓✓\ \big(\text{权 }\le10\ \text{故 }k\le9\ \text{必需 ✓}\big)$$
$$\boxed{\textbf{(2) ★★终止二择（新 ✓✓，对\ \textbf{每个} }c\in C\text{）}:\ k=10\ \text{时无 }j\notin W \Longrightarrow \text{若 }c\oplus e_{[10]}\notin C\ \wedge\ \forall i:\ c\oplus e_{[10]\setminus\{i\}}\notin C\ \text{则该点\textbf{未被覆盖}}✗ \Longrightarrow}$$
$$\qquad\boxed{\text{或 }c\oplus e_{[10]}=c\oplus e_{S_{\rm all}}\in C\ \text{（weight-10）};\quad\text{或}\ \exists i:\ c\oplus e_{[10]\setminus\{i\}}\in C\ \text{（weight-9）}}\ ✓✓\ \big(\text{对任一 }119\text{-cover 的任一码字成立 ✓}\big)$$
$$\boxed{\textbf{(3) ★与 witness 系统的统一（新 ✓✓）}:\ k=3\ \text{的同类式（"下邻"} =\text{weight-2 点）由 }A(c)=0\ \text{自动排除} \Longrightarrow \textbf{强制 weight-4 witness}\ ✓✓\ \big(=\text{见证系统 C-419／C-430／C-433}\ ✓\big)}$$
$$\qquad\Longrightarrow\ \textbf{见证系统 ＝ 级联的 }k{=}3\ \textbf{层}✓✓;\quad \text{级联 ＝ 其 }k\ge4\ \text{的自然延拓 ✓（此前的"迫使高层"是同一机制的连续谱 ✓）}$$
$$\boxed{\textbf{(4) ⚠️ 诚实：级联\textbf{不产生矛盾} ✗ —— 三条精确原因（见 §3）}:\ \text{① 禁层只有 weight 2／3 ✓；② 各层容量充裕 ✓；③ 顶端仅给二择、不给否证 ✓}}$$

---

## §1 $(\alpha)$ 的假设已核（**引用纪律 ✓**）

$$\textbf{（原文逐字 ✓ P1-MICRO 行 17-18）}:\ (\alpha):\ A(c)=0\ \wedge\ \text{相异 }i,j,x\in S(c)\Longrightarrow c\oplus e_i\oplus e_j\oplus e_x\notin C✓;\ \text{证明：否则四点构成 }\textbf{tetra}\ ✗\ \text{与 avoidance 矛盾 ✓}$$
$$\Longrightarrow\ \textbf{故 }(\alpha)\ \text{实际依赖}\ \textbf{全局 tetra-avoidance}\ \big(N_{\rm tetra}=0✓\ \text{即 P1-AVOID 案前提 ✓}\big)\ \textbf{而非仅 }A(c)=0\ ✗✓$$
$$\qquad\textbf{（本档的级联引理\textbf{不需} }(\alpha)✓\big) \Longrightarrow \text{级联在\textbf{不假设 avoidance} 时亦成立 ✓✓\ \big(\text{与 WITCOV §0(3) 相反：那条\textbf{需要} }(\alpha)✓\big)}$$
$$\qquad\textbf{（}k=3\ \text{层需要 }A(c)=0\ ✓:\ \text{下邻 }c\oplus e_{T\setminus i}\ (|T\setminus i|=2)\ \text{由 }A(c)=0\ \text{排除 ✓} \Longrightarrow \text{强制 witness ✓（此为唯一需 avoidance 的层 ✓）}$$

## §2 $s=10$ 的强制塔定量（**✓ 新，登记**）

$$\text{设 }s=10\ (S(c)=[10]✓)\ \text{且 }R=0:\ b_3=0,\ b_4=30✓\ \big(\text{C-433 §3}\big) \Longrightarrow \text{缺失 4-子集数 }=210-30=180✓$$
$$\textbf{层-4 强制 ✓}:\ \text{每个缺失 }u\ \text{需 weight-5 覆盖者 ✓；每个覆盖者至多覆盖 }\binom54=5\ \text{个 }u✓ \Longrightarrow \boxed{c_5+c_4\ \ge\ 36}\ ✓$$
$$\qquad\big(c_j:=\#\{w\in C:d(c,w)=5,\ |S_w\cap S(c)|=j\}✓\big)$$
$$\textbf{层-5 强制 ✓}:\ \text{"全 4-子集缺失"的 5-子集 }V:\ \text{总数 }252-\underbrace{30\cdot6}_{B_4\ \text{各含 6 个 5-集},\ \textbf{两两不共 5-集}}✓=72✓ \Longrightarrow \text{每 weight-6 覆盖者至多覆盖 }\binom65=6⟹ \boxed{c_6\ \ge\ 12}\ ✓$$
$$\qquad\big(\text{两 }B_4\ \text{块在 }R=0\ \text{下交 }\le2\ ⟹ \text{不可能共处一个 5-集 ✓}\big) \Longrightarrow\ \textbf{强制塔下界}:\ \ge36\ (\text{层5})+\ge12\ (\text{层6})+\cdots\ \ll118=\sum_jd_j(c)✓$$
$$\textbf{（层-5 覆盖者的共享规则 ✓）}:\ \text{两个缺失 }u,u'\ \text{可共享覆盖者} \iff |u\cap u'|=3\ \wedge\ c\oplus e_{u\cup u'}\in C✓\ \big(=Johnson\ \text{式 ✓}\big)$$

## §3 为何仍无矛盾（**⚠️ 三条精确原因**）

$$\textbf{① 禁层只有 weight }2,3✓:\ (\alpha)\ \text{与 }A(c)=0\ \text{只排 weight}\le3\ \text{的内部码字}✓;\ \text{weight}\ge4\ \text{的内部码字\textbf{完全无约束}✗}\ \big(\text{与 P1-D4b 的 }C_0\ \text{显式反例一致 ✓}\big)$$
$$\textbf{② 容量充裕 ✓}:\ \text{层-5 需 }\ge36\ \text{而可用 }\binom{10}5=252✓;\ \text{层-6 需 }\ge12\ \text{而可用 }\binom{10}6=210✓\ \big(\text{每层都差一个数量级 ✓}\big)$$
$$\textbf{③ 顶端只给二择 ✗}:\ \text{唯一"无出口"处是 }k=10✓\ \text{（无 weight-11）} \Longrightarrow \text{得 §0(2) 的二择 ✓\ 而非矛盾 ✗✓}$$
$$\forall W,\ \text{级联的触发条件是"下层全缺"——}k=4\ \text{时因 }(\alpha)\ \textbf{自动满足}✓,\ k\ge5\ \text{时需逐点假设 ✓（可失败 ✓）} \Longrightarrow \textbf{级联是"条件性强制"，不构成全覆盖强制 ✓}$$
$$\Longrightarrow\ \boxed{\textbf{结论：级联 ＝ forced tower ✓；\textbf{不能}判死 }R=0\ ✗\ \big(\text{照唐先生判据 ✓}\big)}$$
$$\textbf{（要产生矛盾需要什么 ✓ 登记）}:\ \text{① 层}\ge4\ \text{的\textbf{禁配置}（}k\ge4\ \text{的 }(\alpha)\text{-类比 —— 目前不存在 ✗）};\ \text{② 或\textbf{容量冲突}（各层差一个数量级 ⟹ 需全局计数 ✗）}$$

## §4 状态（**不替唐先生裁定 ✓**）

$$\textbf{已确立 ✓}:\ \text{① 级联引理（无条件，}4\le k\le9✓）;\ \text{② 终止二择（每一码字 ✓）};\ \text{③ 与 witness 系统的统一（}k=3\ \text{层 ✓）};\ \text{④ }s=10\ \text{强制塔下界}✓$$
$$\textbf{未确立 ✗}:\ \text{层}\ge4\ \text{禁配置（不存在）；级联矛盾（未得）；}R=0\ \text{的排除（未得）}✓$$
$$\textbf{依赖标注 ✓}:\ k=3\ \text{层需 }A(c)=0✓;\ (\alpha)\ \text{（weight-3 禁）需}\textbf{全局 tetra-avoidance}✓;\ \text{引用须与 C-410／P1-AVOID 同引 ✓};\ k\ge4\ \text{层}\textbf{无依赖}✓✓$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "级联终止" "强制塔" "终止二择"
技术词 级联终止   命中文件数=0    ::
技术词 强制塔     命中文件数=2    :: ./ASSETS-REGISTRY.md ./WITCOV-2026-09-28-r0-two-corrections-and-forced-high-layer-covering-theorem.md
技术词 终止二择   命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 级联终止 | 0 | 0 | 0（本档自造标签 ✓） |
| 强制塔 | 2（`ASSETS-REGISTRY` ＋ `WITCOV` ⟹ **本线已有** ✓） | 0 | 0（沿用 ✓） |
| 终止二择 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（`级联终止`／`终止二择` 两空间皆 0 ⟹ 自造标签，作结构命名，不作新性主张 ✓；`强制塔` 本线已有 ✓）
- **注 ✓**：本档实质＝**§1 假设核对 ＋ §0(1)(2)(3) 三定理 ＋ §2 定量 ＋ §3 无矛盾诊断**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **$(\alpha)$ 依赖已精确标注** ✓（全局 tetra-avoidance ✓）—— 防误引 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）：本档只给级联的三条定理与"无矛盾"诊断；STOP／继续由唐先生定 ✓
- **不声称** $R=0$ 已排除 ✗；**不声称** 级联必终致矛盾 ✗；不声称 P1 成立 ✗（V290）
