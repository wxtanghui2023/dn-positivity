# WITAUDIT-2026-09-28 — **对象审计：$N$ ＝ $Q_9$ 普通 Hamming 邻域（✓）；$d(A_0)\ge3$ 只属 $A_0\subseteq C_0$，**不是** $C_0\cup C_1$（✗✗消解 §9 之"冲突"）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:44 令 ✓）**：$N$／$C_0$／$C_1$／$A_0$ 之**对象审计**（引档案原文 ✓）；**零程序计算** ✓；**不作路线裁定** ✗。

**已查地图：命中（引 C-435／C-436／C-437／C-438／WITA0／C-442，非新案 ✓）**
`docs/WITFIB-2026-09-28-…`（**$N_9[\cdot]$＝闭邻域／$P_b$ 定义 ✓✓✓**）｜`docs/WITW2C-2026-09-28-…`（**$C_0,C_1\subseteq Q_9$／点式条件 ✓✓✓**）｜`docs/WITSAT-2026-09-28-…`（**$U^c\subseteq N(C_0)\cap N(C_1)$／$q_{ab}$ ✓✓**）｜`docs/ERRATUM-2026-09-28-…`（**$X_L$ ✓✓**）｜`docs/WITA0-2026-09-28-…`（**$A=C_0\setminus\{h\}$ ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** $N$／$C_0,C_1$／$A_0$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次逐条引档完成 $N$／$C_0,C_1$／$A_0$ 之口径审计，并消解"$d(A_0)\ge3\Rightarrow N(C_0)\cap N(C_1)=\varnothing$"之伪冲突（实为 $A_0$ 与 $C_0\cup C_1$ 之混淆 ✗）** ✓）
**[RESEARCH]**

---

## §0 结论（**$N$＝普通 Hamming ✓✓｜$A_0\subseteq C_0$ ✓✓｜§9 之冲突＝混淆 ✗✗**）

$$\boxed{\textbf{(1) ✓✓✓对象口径（逐字引档 ✓）}}$$
| 对象 | 精确定义 | 出处 |
|---|---|---|
| $C\subseteq F_2^{10}$ | 半径-1 覆盖码，$\|C\|=119$ ✓ | C-436 §记号 ✓ |
| $C_0,C_1\subseteq Q_9{=}F_2^9$ | $P_b:=\{x\in F_2^9:(x,b)\in C\}$ ✓; $a{=}\|P_0\|,\ b{=}\|P_1\|,\ a+b{=}119$ ✓ | **WITFIB 第 18 行 ✓✓** |
| $N_9[S]$ | **闭半径-1 邻域** ✓ | **WITFIB 第 18 行 ✓✓** |
| $N(C_0)\cap N(C_1)$ | **开**半径-1 邻域之交集 ✓（$U^c$ 须"双色邻接" ✓） | **WITSAT §0(1) ✓✓** |
| 两式等价 ✓ | $F_2^9=N_9[C_0]\cup C_1\wedge F_2^9=N_9[C_1]\cup C_0\iff U^c\subseteq N(C_0)\cap N(C_1)$ ✓ | WITSAT §1 ✓✓ |
| $A$ | $\boxed{A=C_0\setminus\{h\}}$ ✓（$\|A\|=44$ ✓） | **WITA0 第 22 行 ✓✓✓** |
| $A_0$ | $A_0:=\{a\in A:\ d_U(a)=0\}$ ✓（"="干净中心" ✓） | **WITA0 第 24 行 ✓✓** |
$$\qquad\Longrightarrow\ \boxed{N\ \text{＝}Q_9\ \text{中之\ \textbf{普通 Hamming-1 邻域}}}\ ✓✓\ \big(\text{非 quotient／非投影／非 owner-set ✗}\big)$$
$$\boxed{\textbf{(2) ✗✗唐先生 §9 之"立即冲突"为\ \textbf{混淆}（本档消解 ✓✓）}:\ \text{其设 }C_0,C_1\subseteq A_0\ \text{故 }d(u,v)\ge3\Longrightarrow N(u)\cap N(v)=\varnothing\ \forall(u,v)\in C_0\times C_1\ ✗✗}$$
$$\qquad\textbf{真相 ✓✓}:\ \text{① }d(A_0)\ge3\ \text{只属 }A_0\subseteq A=C_0\setminus\{h\}\subseteq C_0\ \big(\text{WITA0 ✓}\big),\ \textbf{不属}\ C_0\ \text{本身、亦不属 }C_0\times C_1\ ✗✓$$
$$\qquad\qquad\quad\ \text{② }\|C_0\|\ge45>A(9,3)=40\ \big(\text{C-442 ✓✓}\big)\Longrightarrow \boxed{C_0\ \text{必含距离}\le2\ \text{之对}}\ ✓✓\ \big(\text{WITA0 已作\textbf{假前提}否证 ✓✓}\big)$$
$$\qquad\qquad\quad\ \text{③ 覆盖条件\ \textbf{需要}距离-2 对：}u\in C_0,v\in C_1\ \text{有共同邻}\iff d(u,v)=2✓✓\Longrightarrow\ \text{正是 }U^c\ \text{双覆盖之源 ✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{无冲突}}\ ✓✓;\quad \text{唐先生第 10 点之"若为普通邻域则冲突"不成立}\ ✗\ \big(\text{前提①错}\Longrightarrow\text{结论不成 ✓}\big)$$
$$\boxed{\textbf{(3) ✓✓唐先生 §8 之 owner-pair 双计数\ \textbf{即档案已有之 }$q_{ab}$ 恒等式}}:\ q_{ab}:=\big|U^c\cap N(a)\cap N(b)\big|✓\ \big(\text{C-437 ✓✓}\big)$$
$$\qquad\sum_{a\in A,b\in B}q_{ab}=\sum_{x\in U^c}\big|N(x)\cap A\big|\cdot\big|N(x)\cap B\big|✓✓;\qquad \textbf{但注意 C-438 之勘误 ✗}:\ \ge\ \big|X_L\big|\ \text{而\ \textbf{非} }\ge|U^c|\ ✗\ \big(X_L:=U^c\setminus N(H)✓\big)$$
$$\qquad\Longrightarrow\ \text{唐先生 §8 之 }\mu(x)\ge1\ \text{对\ \textbf{全 }}$C_0\times C_1$\ \text{积\ \textbf{才}成立 ✓}\ \big(\text{若把 }H\ \text{单列则须改用 }X_L✓✓\big)$$
$$\textbf{(4) ✓唐先生 §2–§3 之 deficit 重参数化正确}:\ \alpha:=20-(c+d),\ \beta:=22-(f+g)\Longrightarrow |A_0|=42-(\alpha+\beta)✓$$
$$\qquad|A_0|\le40\Rightarrow\boxed{\alpha+\beta\ge2}✓;\quad |A_0|\ge33\iff\boxed{\alpha+\beta\le9}✓;\quad |A_0|=40\Rightarrow(c+d,f+g)\in\{(20,20),(19,21),(18,22)\}✓✓$$
$$\qquad\textbf{⚠️（一处须改 ✗）}:\ \text{唐先生 §1 之 }\ M=\max\{|A_0|:\ A_0\ \text{满足 119 覆盖条件}\}\ ✗\ \text{—— }A_0\ \textbf{单独}不载覆盖条件 ✗$$
$$\qquad\qquad\text{覆盖是\ \textbf{联合}条件（作用于 }(C_0,C_1)\ \text{对 ✓）；正确写法：}A_0\subseteq C_0\ \wedge\ (C_0,C_1)\ \text{满足 }U^c\subseteq N(C_0)\cap N(C_1)✓✓$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✗（形式须改）}:\ M\ \text{之定义混淆了单侧码与联合覆盖 ✓（见 §0(4) ✓）；下界 25／上界 40 ✓（C-457 ✓）}$$
$$\textbf{§2 ✓✓}:\ \alpha+\beta\in[2,9]✓✓\ \text{（因 }33\le|A_0|\le40✓\big)\ \text{—— 干净且正确 ✓✓}$$
$$\textbf{§3 ✓✓}:\ \text{角点表}\ (20,20),(19,21),(18,22)✓✓;\ \text{"}c+d\le17\Rightarrow\text{总量}\le39\text{"}✓✓$$
$$\textbf{§4 ✓}:\ f+g=22\Rightarrow f\ \text{在三 extremal 族（C-458 ✓✓ 已证恰 3 类 ✓）✓✓}$$
$$\textbf{§5 ✓（方向 ✓）}:\ 40\ \text{之等号结构 }\big(\text{球覆盖 }40\times10=400\le512✓\big)\ \text{值得用 ✓；唯"完美"之措辞宜慎 ⚠️（}400<512\ ✓\ \text{非完美码 ✓）}$$
$$\textbf{§6 ✓✓}:\ U^c\subseteq N(C_0)\cap N(C_1)\Longrightarrow\big|N(C_0)\cap N(C_1)\big|\ge|U^c|✓✓\ \text{（=C-437 ✓）}$$
$$\textbf{§7 ✓✓}:\ \text{"从点数升级到 owner-pair 数"\ \textbf{方向正确} ✓✓\ \big(\text{即 }q_{ab}\ \text{路线 ✓}\big)}$$
$$\textbf{§8 ✓✓}:\ \text{双计数恒等式正确 ✓✓（=C-437 ✓）；唯 }\ge|U^c|\ \text{须按 C-438 改为 }\ge|X_L|✓\ \big(\text{若 }H\neq\varnothing\ ✓\big)$$
$$\textbf{§9 ✗✗}:\ \text{见 §0(2)：}d(A_0)\ \text{误加于 }C_0\times C_1\ ✗\ \big(\text{前提错}\ \big)$$
$$\textbf{§10 ✓✓✓}:\ \textbf{其审计要求完全正确} ✓✓✓\ \text{—— 本档即完成：}N\ \text{＝普通 Hamming（选项 1 ✓）⟹\ \textbf{无冲突} ✓（因前提错 ✗）}$$
$$\textbf{§11–§13 ✓（方向 ✓）}:\ \text{先攻 }|A_0|=40\ \text{之三分配}\ \big((20,20),(19,21),(18,22)\big)✓✓\ \text{——\ \textbf{可执行} ✓，唯须以 §0(4) 之联合形式书写 ✓}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }N\ \text{＝}Q_9\ \text{普通 Hamming 邻域 ✓✓✓\ \big(\text{引档第 18／§0(1) 行 ✓}\big)};\ \text{② }A=C_0\setminus\{h\}✓,\ A_0=\{d_U=0\}\subseteq A\subseteq C_0✓✓;\ \text{③ }|C_0|\ge45\Rightarrow C_0\ \text{含 }d\le2\ \text{对 ✓✓};\ \text{④ owner-pair ＝}q_{ab}✓✓;\ \text{⑤ }\alpha+\beta\in[2,9]✓✓;\ \text{⑥ }|A_0|=40\ \text{仅三分配}✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}d(A_0)\ge3\Rightarrow N(C_0)\cap N(C_1)=\varnothing\text{"}\ ✗✗;\quad \text{"}M\ \text{可按 }A_0\ \text{单侧定义"}\ ✗;\quad \sum q_{ab}\ge|U^c|\ ✗\ \big(\text{C-438 ✓}\big)$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ M\ \text{之真值};\ \text{（覆盖侧联合容量仍未成式 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 以\ \textbf{联合形式}\ 重写 P1：}\big(A_0\subseteq C_0,\ (C_0,C_1)\ \text{满足 }U^c\subseteq N(C_0)\cap N(C_1)\big)✓;\ \text{② }|A_0|=40\ \text{三分配分支之 }C_0\ \text{结构分类 ✓};\ \text{③ }q_{ab}\ \text{恒等式之上界（}q_{ab}\le2✓\ \text{与 }\sum\le72\min(|A|,|B|)✓\ \text{C-438 ✓）与下界 }\ge|X_L|✓\ \text{之夹逼 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "对象审计" "邻域口径" "owner对"
技术词 对象审计  命中文件数=6    :: ./C3882-noncanonical-escape-hatch-specification-and-closure.md ./C326-Littlewood-cross-object-mechanism-ontology-audit.md ./k1-k2-positivedefinite-kernel.md …
技术词 邻域口径  命中文件数=0    ::
技术词 owner对   命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 对象审计 | **1**（`C3882-…` ⟹ 既有 ⟹ **不计** ✗） | **5**（`C326-Littlewood-…` 等 ⟹ 空间 A 同名 ⟹ **不计** ✗） | ✗（**非新增** ✓） |
| 邻域口径 | 0 | 0 | ✓（自造标签 ✓） |
| owner对 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（本档为**引档审计**，无新计算 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处必改**（§9 之混淆）已在 §0(2) 显式消解并给出**正确前提**（$A_0\subseteq C_0$ ✓、$|C_0|\ge45$ ✓）✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
