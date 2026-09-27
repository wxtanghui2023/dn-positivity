# P1-D4-2026-09-27 — **$d_4$ 独立上界的第一击**：球面覆盖恒等式 ＋ 两类来源排除

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。**范围（照唐先生 23:01 令 ✓）**：攻"119 的全局覆盖能否给出与 $d_4(c)$ 独立、且不依赖已有 profile 计数的上界"；零程序计算 ✓。

**已查地图：命中（接续 P1-D3b／P1-D3／C-409，非新案 ✓）**
`docs/P1-D3b-2026-09-27-…`（**$d_4\ge\lceil\binom s3/4\rceil$／$C(s,4,3)$ 方向纠正** ✓✓）｜`docs/P1-D3-2026-09-27-…`（**被迫高层码字定理** ✓✓）｜`docs/P1-AVOID-2026-09-27-…`（**占用恒等式 ＝ profile 同源** ✓✓）｜`docs/R7-LOCK-2026-09-27-…`｜`docs/P1-TWO-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §6）
D0: 本档对象 ＝ **档案已有** $d_4$ 下界对象的**上界侧第一次尝试**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出球面覆盖恒等式 $8d_2+d_3+4d_4=120+E_3(c)$ ＋ 两类上界来源的显式排除** ✓）
**[RESEARCH]**

---

## §0 结论（**状态锁 ✓｜新恒等式 ✓✓｜方向判定 ✗｜来源排除 ✓✓**）

$$\boxed{\textbf{(0) C-413 状态锁（照唐先生 ✓）}:\ \textbf{LIVE / P1 incomplete}\ ✗;\ \text{链条}:\ \text{D3 forcing}\Rightarrow\text{3-subset coverage demand}\Rightarrow d_4\ge\Big\lceil\tfrac{\binom s3}4\Big\rceil;\ \text{缺 \textbf{independent upper bound on }d_4}✗}$$
$$\boxed{\textbf{(1) ★球面覆盖恒等式（新 ✓✓）}:\ \text{令 }S_3(c):=\{x:d(x,c)=3\}\ (|S_3|=120✓)\ \Longrightarrow\ \boxed{8d_2(c)+d_3(c)+4d_4(c)=120+E_3(c)}✓✓}$$
$$\qquad\big(E_3(c):=\sum_{x\in S_3(c)}\big(b(x)-1\big)\ \ge0\ ✓\big)$$
$$\boxed{\textbf{(2) 方向判定 ✗}:\ \text{covering 为\textbf{单调下型}（}b\ge1\text{）} \Longrightarrow\ \text{本恒等式只给}\ 8d_2+d_3+4d_4\ \ge120\ \textbf{（下界）}✗\ \text{—— 与 forced-}d_4\ \text{下界\textbf{同向}}\ \Longrightarrow\ \textbf{无 squeeze}✗✓}$$
$$\boxed{\textbf{(3) 聚合 ✗}:\ \text{两侧均为 profile 级}:\ 16N_2+2N_3+8N_4=14280+\sum_x(b(x)-1)d_3(x)\ \Longrightarrow\ \textbf{不构成独立 handle}✗✓}$$
$$\boxed{\textbf{(4) ★两类来源排除（本档最重要 ✓✓）}:\ \text{覆盖类}\Rightarrow\text{只给下界}✗;\ \text{容量类恒等式}\Rightarrow\text{profile 决定}（\text{C-409 ✓}）✗ \Longrightarrow\ \textbf{独立 }d_4\ \textbf{上界不能来自这两类} ✓✓}$$

---

## §1 **球面覆盖恒等式**（**逐类阴影计数 ✓✓**）

$$\text{设 }x=c\oplus u\ (|u|=3)\ \text{为球面点 ✓};\ \text{覆盖 }x\ \text{者 }w\in C\ \text{满足 }d(w,x)\le1\ \Longrightarrow\ w=x\ \text{或}\ w=x\oplus e_i✓$$
$$\qquad\Longrightarrow\ w=c\oplus\big(u\oplus e_i\big)✓;\ |u\oplus e_i|\in\{2,4\}✓\ \big(\text{因 }|u|=3✓\big)\ \Longrightarrow\ \textbf{覆盖者只能取重量 2／3／4（相对 }c\text{）}✓✓$$
$$\textbf{（为何 weight-1／5 等不能覆盖 ✓）}:\ |u\oplus v|\ge\big||u|-|v|\big|\ \Longrightarrow\ |v|=1\Rightarrow\ge2✗;\ |v|=5\Rightarrow\ge2✗\ ✓$$
$$\textbf{各类阴影大小 ✓}:\quad\text{weight-2 码字 }c\oplus v\ (|v|=2)\ \text{覆盖 }x=c\oplus u\iff u=v\oplus e_i,\ |u|=3\iff i\notin\mathrm{supp}(v)\ \Longrightarrow\ \mathbf 8\ \text{个球面点}✓$$
$$\qquad\text{weight-3 码字 }c\oplus u_0:\ u=u_0\oplus e_i,\ |u|=3\iff i\in\mathrm{supp}(u_0)\ \text{但}\ |u_0\oplus e_i|=2✗\ \text{或}\ i\notin\Rightarrow4✗\ \Longrightarrow\ \text{仅 }u=u_0\ \text{自身（}\mathbf 1\ \text{个}✓\text{；奇偶性排除 }|u\oplus u_0|=1✓\big)$$
$$\qquad\text{weight-4 码字 }c\oplus v\ (|v|=4):\ |v\oplus e_i|=3\iff i\in\mathrm{supp}(v)\ \Longrightarrow\ \binom43=\mathbf 4\ \text{个球面点}✓$$
$$\textbf{两边同时计数 ✓}:\ \sum_{x\in S_3(c)}b(x)=8d_2(c)+1\cdot d_3(c)+4d_4(c)✓;\qquad \sum_{x\in S_3(c)}b(x)=120+E_3(c)✓\ \Longrightarrow\ \textbf{§0 (1) 得证}✓✓$$

## §2 **方向判定**（**只给下界 ✗**）

$$\text{因 }E_3(c)\ge0✓\ \Longrightarrow\ \boxed{8d_2(c)+d_3(c)+4d_4(c)\ \ge\ 120}\ ✓\ \text{—— 这是\textbf{下界}（加权和的下界 ✓）}$$
$$\textbf{与 forced-}d_4\ \text{的关系 ✓}:\ \text{P1-D3 给 }d_4(c)\ge\lceil\binom{s(c)}3/4\rceil✓;\ \text{本节给 }8d_2+d_3+4d_4\ge120✓\ \text{—— \textbf{两条下界，同向}}✗✓$$
$$\Longrightarrow\ \textbf{J04 型夹逼所需的上界仍缺}✗\ \text{—— 本档\textbf{未}产生 squeeze ✗（诚实 ✓）}$$

## §3 **聚合**（**profile 级 ✗**）

$$\sum_c\big(8d_2(c)+d_3(c)+4d_4(c)\big)=8\cdot2N_2+2N_3+4\cdot2N_4=16N_2+2N_3+8N_4✓;\qquad \sum_c120=14280✓$$
$$\sum_cE_3(c)=\sum_c\sum_{x\in S_3(c)}\big(b(x)-1\big)=\sum_x\big(b(x)-1\big)\cdot\#\{c:x\in S_3(c)\}=\sum_x\big(b(x)-1\big)d_3(x)✓$$
$$\Longrightarrow\ \boxed{16N_2+2N_3+8N_4=14280+\sum_x\big(b(x)-1\big)d_3(x)}\ ✓\ \text{（新恒等式 ✓）}$$
$$\textbf{性质 ✗}:\ \text{左侧＝距离分布量 }(A\text{-data})✓;\ \text{右侧末项 }\sum_x(b(x)-1)d_3(x)\text{) 涉及 }b(x)\ \text{与 }d_3(x)\ \text{的\textbf{联合分布}}✓$$
$$\qquad\Longrightarrow\ \text{仍属\textbf{容量／profile 侧}（与 C-409 占用恒等式同族 ✓）} \Longrightarrow\ \textbf{不构成独立 handle}✗✓$$

## §4 **两类来源排除**（**本档最重要 ✓✓**）

$$\textbf{第一类（覆盖类）✗}:\ \text{covering 条件是 }b\ge1\ \text{型（单调下型 ✓）} \Longrightarrow\ \text{其推论天然为\textbf{下界}}（\S2 ✓）\ \Longrightarrow\ \textbf{结构上不可能给出 }d_4\ \text{上界}✗✓$$
$$\qquad\text{（本档用球面覆盖实测确认：得到恒等式 ＋ 下界，非上界 ✓）}$$
$$\textbf{第二类（容量类）✗}:\ \text{上界只能来自"容量／计数"型恒等式（度数和 ／占用预算 ✓）};\ \text{而 C-409 已证占用类量与 }\{n_j\}\ \textbf{同源}✗✓$$
$$\qquad\text{（R7 STOP 同形态 ✓）} \Longrightarrow\ \textbf{此类上界必为 profile 决定，不能作为独立 handle}✗✓$$
$$\Longrightarrow\ \boxed{\textbf{结论（路线级 ✓✓）}:\ \text{独立 }d_4\ \textbf{上界不能来自"覆盖类"或"容量类"这两大来源}}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{若 }d_4\ \text{夹逼路线要继续，须找到\textbf{第三类}独立全局资源约束（既非 }b\ge1\ \text{型，也非度数／占用型）}⚠️$$

## §5 现状与下一步（**诚实 ✓**）

$$\textbf{已排除 ✗}:\ \text{① 覆盖类（本档球面覆盖 ✓）};\ \text{② 容量／profile 类（C-409／R7 ✓）} \Longrightarrow\ \text{两扇最自然的门已关}✓✓$$
$$\textbf{未判死 ✓}:\ \text{路线\textbf{未}判定为死}✗（\text{照唐先生判据：仅当"独立上界不可能"才判死 ✓；本档只排除了\textbf{两类来源}}✓）$$
$$\textbf{下一步候选（登记未做 ⚠️）}:\ \text{① 第三类全局资源（例：}d_4\ \text{与 }G_2(C)\ \text{的团结构／极大团计数的耦合 ✓）};\ \text{② 用 }B(c)=0\ \text{（tetra-avoidance）给出 }d_4\ \text{侧的约束 ⚠️};\ \text{③ 检验 }16N_2+2N_3+8N_4\ \text{恒等式是否与已知 }A\text{-data 界冲突}✓$$

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "球面覆盖"
技术词 球面覆盖        命中文件数=1    :: ./C207-T13A-YI-4-continuous-family-exclusion-renaming-and-T13B2-seal.md
$ bash scripts/tech_word_check.sh "阴影计数"
技术词 阴影计数        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "独立上界"
技术词 独立上界        命中文件数=16   :: ./p5-6-realisability-space.md ./W5-1-why-Gram-positivity-gives-lower-bounds-only.md ./L2-RAMIFICATION-STATE.md
$ bash scripts/tech_word_check.sh "d_4 上界"
技术词 d_4 上界        命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`阴影计数`／`d_4 上界` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`球面覆盖`／`独立上界` 档案已有（他处语境 ✓））
- **注 ✓**：本档实质＝**§1 恒等式 ＋ §2 方向判定 ＋ §4 两类来源排除**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **C-413 状态 ＝ LIVE / P1 incomplete** ✓（未 CLOSED ✗）
- **不声称** P1 成立 ✗（V290）；**不声称** D3→D4 线已死 ✗ —— 只写"**独立上界的两类来源已排除**" ✓
- §1 的阴影计数（8／1／4）**逐类有证明** ✓（奇偶性与 $|u\oplus v|\ge||u|-|v||$ ✓）
