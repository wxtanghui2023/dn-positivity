# WITSAT-2026-09-28 — **精确条件锐化（$U^c\subseteq N(C_0)\cap N(C_1)$）＋ $q_{ab}$ 恒等式 ＋ 饱和事件无局部上界（诚实）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:32 令 ✓）**：① **不攻 62-码完整分类**（照唐先生源核查 ✓：公开资料只确认"两个已知构造同属一个 switching class" ✓，未给全分类 ✗；且 2001 证明本身是计算辅助子空间分解＋LP ✓）；② 攻 $(\alpha)/(\beta)$ 的 $q_{ab}$ 与 $n_2$ 上界问题；**零程序计算**（仅整数/逻辑核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-436／C-435／C-431，非新案 ✓）**
`docs/WITW2C-2026-09-28-…`（**双色精确条件／跨色收紧／$K(9,1)$ 咬点 ✓✓**）｜`docs/WITFIB-2026-09-28-…`（**精确等价／$U_b\subseteq P_{1-b}$ ✓✓**）｜`docs/P1-AVOID-…`（**avoidance／square 机制先例 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §6）
D0: 本档对象 ＝ **档案已有** 双色加权／$q_{ab}$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出精确条件的最锐形式（$U^c\subseteq N(C_0)\cap N(C_1)$，并与 C-435 形式等价）＋ "纤维自覆盖 ⟹ 要求只落 $U^c$"的修正 ＋ $q_{ab}$ 精确恒等式 ＋ 饱和事件无局部上界（附局部模型）** ✓）
**[RESEARCH]**

---

## §0 结论（**锐化 ✓✓｜一处修正 ✗✓｜恒等式 ✓✓｜饱和无局部界 ✗ + 构造 ✓**）

$$\text{记号 ✓}:\ C_0,C_1\subseteq Q_9;\ H=C_0\cap C_1,\ A=C_0\setminus C_1,\ B=C_1\setminus C_0,\ U=H\sqcup A\sqcup B;\ s=|U|;\ |H|=119-s;\ |A|+|B|=2s-119✓$$
$$\boxed{\textbf{(1) ★★精确条件的最锐形式（新 ✓✓）}:\ \textbf{119-cover of }Q_{10}\iff \boxed{U^c\ \subseteq\ N(C_0)\cap N(C_1)}\ ✓✓}$$
$$\qquad\text{读法 ✓}:\ \textbf{每个外部点同时被两色邻接}（\text{一 }C_0\text{-邻点}\ \wedge\ \text{一 }C_1\text{-邻点}✓\big);\ \text{与 C-435 形式 }U_b\subseteq P_{1-b}\ \textbf{严格等价}✓✓\ \big(\text{证明见 §1 ✓}\big)$$
$$\boxed{\textbf{(2) ✗修正（本档 ✓）}:\ \text{两色要求只落在 }U^c\text{，而不落在 }D\ ✗\ \big(\text{唐先生 §1 所写"对任意 }x\in D"\text{ 过强}\ ✗\big)}$$
$$\qquad\textbf{理由（3 行 ✓✓）}:\ g(x)\ge1 \Longrightarrow \text{整条 fibre}\ \{(x,0),(x,1)\}\ \textbf{自覆盖}\ ✓✓\ \big(\text{若 }x\in C_0:\ (x,0)\in C\ \text{覆盖自身与 }(x,1)✓\ \text{（距离 1）}✓\big)$$
$$\qquad\Longrightarrow\ \text{约束只对 }g(x)=0\ \text{（即 }x\in U^c\text{）出现 ✓；故 }D\cap A,\ D\cap B\ \text{的点}\ \textbf{无任何覆盖要求}✓✓\ \big(D:=V\setminus N[H]✓\big)$$
$$\boxed{\textbf{(3) ★★$q_{ab}$ 精确恒等式（新 ✓✓）}:\ q_{ab}:=|U^c\cap N(a)\cap N(b)|\in\{0,1,2\}✓ \Longrightarrow}$$
$$\qquad\boxed{\sum_{a\in A,\,b\in B}q_{ab}\ =\ \sum_{x\in U^c}\big|N(x)\cap A\big|\cdot\big|N(x)\cap B\big|\ \ge\ |U^c|\ \ge\ 8s-559✓}\ ✓✓$$
$$\qquad\text{（左＝pair 侧计数；右＝点侧乘积 ✓；}\ge|U^c|\ \text{因每个 }x\in U^c\ \text{恰贡献 }|N_A|\cdot|N_B|\ge1✓✓\ \text{—— 反过来说明 }q_{ab}\ \textbf{不是} $e_2^{AB}$ 的重复计数 ✗）$$
$$\boxed{\textbf{(4) ✓饱和 ＝ square（唐先生 §6 ✓）}:\ q_{ab}=2\iff \text{两中点}\ (a\oplus e_i,\ a\oplus e_j)\ \text{皆}\in U^c✓\ \big(\text{＝该 pair 承担一个完整 4-cycle ✓}\big)}$$
$$\boxed{\textbf{(5) ⚠️诚实判定：}\ n_2\ \textbf{无局部上界}✗✓\ \big(\text{附局部模型 ✓，见 §5}\big)}$$
$$\qquad\textbf{原因 ✓✓}:\ \text{若 }q_{ab}=2,\ \text{则两中点的\ \textbf{两色要求\ 已被 }\{a,b\}\ \textbf{自动满足}}✓✓\ \big(\text{中点 }\in A:\ \text{有 }B\text{-邻 }b✓;\ \in B:\ \text{有 }A\text{-邻 }a✓;\ \notin U:\ \text{两者兼有}✓\big)$$
$$\qquad\Longrightarrow\ \text{饱和情形\ \textbf{不产生任何新的禁配}}✗ \Longrightarrow \textbf{局部禁配路线无法给出 }n_2\le F\ ✗✓$$

---

## §1 精确条件两形式等价（**✓✓**）

$$\textbf{(a)（C-435 ✓）}:\ \mathbb F_2^9=N_9[C_0]\cup C_1\ \wedge\ \mathbb F_2^9=N_9[C_1]\cup C_0✓;\qquad \textbf{(b)（本档 ✓）}:\ U^c\subseteq N(C_0)\cap N(C_1)✓$$
$$\textbf{(b)}\Longrightarrow\textbf{(a)}:\ x\notin N_9[C_0]\Longrightarrow x\notin C_0\ \wedge\ (Ac_0)(x)=0 \overset{(b)}{\Longrightarrow}x\in U \Longrightarrow x\in U\setminus C_0=C_1✓\ \text{（即 }U_0\subseteq C_1✓\big)$$
$$\textbf{(a)}\Longrightarrow\textbf{(b)}:\ x\notin U \Longrightarrow x\notin C_1 \overset{(a)}{\Longrightarrow} x\in N_9[C_0]\ \text{且}\ x\notin C_0 \Longrightarrow (Ac_0)(x)\ge1✓;\ \text{对称得 }(Ac_1)(x)\ge1✓ \Longrightarrow \text{(b)}✓✓$$
$$\textbf{（故 }U_b\subseteq P_{1-b}\iff U^c\subseteq N(C_0)\cap N(C_1)✓✓\big)\ \text{—— 后者更直白：}\textbf{外部点必须"双色邻接"}✓$$

## §2 修正：约束只落在 $U^c$（**✓✓**）

$$\text{对 }x\ \text{的 fibre}\ \{(x,0),(x,1)\}:\ \text{被覆盖的条件} = \begin{cases}g(x)\ge1:&\textbf{自动}✓\ \big((x,0)\in C\ \text{或}\ (x,1)\in C\ \text{覆盖整条 fibre}✓\big)\\ g(x)=0:&\text{须 }(Ac_0)(x)\ge1\ \wedge\ (Ac_1)(x)\ge1✓\end{cases}$$
$$\Longrightarrow\ \text{故 (b) 中 }U^c=\operatorname{supp}(g)^c\ \text{恰是全部约束集}✓✓\ \big(\text{唐先生 §1 的 }D=V\setminus N[H]\ \text{是更小的集合，其中 }D\cap A,D\cap B\ \textbf{无要求}✗\big)$$
$$\textbf{（副产品 ✓）}:\ \text{唐先生 §3–§4 的"A–H–B 桥"结构：若 }x\in D\cap U^c\ \text{（即 }\beta\text{ 点）则有 }A\text{-邻与 }B\text{-邻}✓\ \text{（＝(b) ✓）；若无 }H\text{-邻则两者皆在 }A,B✓\ \text{—— 该读法本身没错，只是适用范围是 }D\cap U^c\ ✗\ \text{而非全 }D✓$$

## §3 $q_{ab}$ 与精确恒等式（**✓✓**）

$$q_{ab}:=\big|U^c\cap N(a)\cap N(b)\big|✓;\quad d(a,b)=2\Longrightarrow|N(a)\cap N(b)|=2 \Longrightarrow \boxed{q_{ab}\in\{0,1,2\}}✓✓\ \big(\text{$Q_9$ 中距离-2 对恰两共同邻点 ✓}\big)$$
$$\textbf{恒等式 ✓✓}:\ \sum_{a\in A,b\in B}q_{ab}=\sum_{a\in A,b\in B}\sum_{x\in U^c}\mathbf 1[x\sim a]\mathbf 1[x\sim b]=\sum_{x\in U^c}\big|N(x)\cap A\big|\cdot\big|N(x)\cap B\big|✓✓$$
$$\qquad\ge\sum_{x\in U^c}1=|U^c|✓\ \big(\text{每 }x\in U^c\ \text{有 }\ge1\ \text{个 }A\text{-邻与}\ge1\ \text{个 }B\text{-邻 ✓}\big);\qquad |U^c|=512-s\ \overset{s\ge62}{=}\ \ge\ 450✓$$
$$\textbf{（与 }8s-559\ \text{的关系 ✓）}:\ |U^c|=512-s\ \ge\ 8s-559\iff s\le119✓\ \text{（总成立 ⟹ }8s-559\ \text{是\textbf{更弱}的旧下界 ✓）}$$

## §4 饱和 ＝ square，且**局部自足**（**✓✓／✗**）

$$\text{取 }a\in A,\ b\in B,\ d(a,b)=2✓;\ \text{中点}\ x=a\oplus e_i,\ y=a\oplus e_j✓;\ q_{ab}=2\iff x,y\in U^c✓✓$$
$$\textbf{自足性 ✓✓}:\ \text{若 }q_{ab}=2,\ \text{则 }x\ \text{与}\ y\ \text{的\ \textbf{两色要求}由 }\{a,b\}\ \text{满足}✓✓:\quad x\in A\Rightarrow b\in N(x)\cap B✓;\ x\in B\Rightarrow a\in N(x)\cap A✓;\ x\notin U\Rightarrow \text{两者兼有}✓$$
$$\qquad\text{且 }a\in A\Rightarrow a\ \text{自身 fibre 自覆盖（§2）✓；}b\ \text{同 ✓} \Longrightarrow \textbf{该局部构型不违反任何已知条件}✓$$
$$\Longrightarrow\ \boxed{\text{饱和事件\ \textbf{不产生禁配}、不消耗稀缺资源}✗ \Longrightarrow \textbf{不存在由局部结构推出的 }n_2\le F\ ✗✓}$$

## §5 局部模型（**✓ 说明饱和可规模化 ⚠️**）

$$\textbf{构造（局部 ✓）}:\ \text{取 }A\ni 0\ (=\text{原点}✓);\quad B\supseteq\{e_i\oplus e_j:1\le i<j\le9\}\ (36\ \text{个}✓);\quad U^c\supseteq\{e_1,\dots,e_9\}✓$$
$$\qquad\text{则对每个 }(i,j):\ a=0,\ b=e_i\oplus e_j✓,\ d=2✓,\ \text{中点 }e_i,e_j\in U^c✓ \Longrightarrow q_{ab}=\mathbf 2✓✓ \Longrightarrow \boxed{n_2\ \ge\ 36}✓$$
$$\qquad\textbf{规模核对 ✓}:\ |A|=1,\ |B|=36 \Longrightarrow |A|+|B|=37\overset{!}{=}2s-119\Longrightarrow s=\mathbf{78}✓\ \big(|H|=41,\ |U^c|=434✓\big)\ \text{—— 落在允许区间内 ✓}$$
$$\textbf{⚠️未检项（诚实 ✓）}:\ \text{该构型是否可全局完成（434 个外部点的覆盖、}|C|=119\text{ 与 }H\text{ 的相容性）未验 ✗}$$
$$\qquad\Longrightarrow\ \textbf{本模型只证明"局部禁配不存在"✗，\textbf{不}证明 119-cover 存在 ✗✓（V290 ✓）}$$

## §6 状态（**不作路线裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 精确条件最锐形式（§1）；② 约束只落 }U^c\ \text{（§2）；③ }q_{ab}\ \text{恒等式（§3）；④ 饱和＝square＋自足（§4）}✓$$
$$\textbf{已否证 ✗}:\ \text{局部禁配 }\Longrightarrow n_2\ \text{上界（§4-§5）}✓\ \text{—— 唐先生 §7 所设想的 }n_2\le F(|H|)\ \textbf{不可由局部构型得到}✗✓$$
$$\textbf{仍开 ⚠️}:\ \text{① 全局相容性（§5 未检）；② }n_2\ \text{的\ \textbf{全局}上界（须非局部输入）；③ 一般 }s\ \text{的"存在}\to\text{计数"升级}✗$$
$$\textbf{（与 C-431／C-436 的一致性 ✓）}:\ \text{本路线仍停在"聚合层＝体积界"之外需结构输入；饱和自足再次说明：\textbf{纯局部（二阶以内）结构已被耗尽}✗✓}$$

## §7 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "自覆盖纤维" "饱和事件" "局部自足"
技术词 自覆盖纤维  命中文件数=0    ::
技术词 饱和事件    命中文件数=0    ::
技术词 局部自足    命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 自覆盖纤维 | 0 | 0 | 0（本档自造标签 ✓） |
| 饱和事件 | 0 | 0 | 0（本档自造标签 ✓） |
| 局部自足 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 等价 ＋ §2 修正 ＋ §3 恒等式 ＋ §4-§5 否证与构造**（推导性 ✓）

## §8 边界（硬 ✓）

- **零程序计算** ✓（仅整数/逻辑核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§7 已分栏 ✓）
- **不攻 62-码分类** ✓（照唐先生 10:32 源核查 ✓）；$K(9,1)=62$ 为文献值（档级 ✓，只用下界方向 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）：本档只给锐化、修正、恒等式与"饱和无局部界"的否证；是否转向全局输入由唐先生定 ✓
- **不声称** 119 已排除 ✗；**不声称** §5 构型可全局完成 ✗（已标未检 ✓）；不声称 P1 成立 ✗（V290）
