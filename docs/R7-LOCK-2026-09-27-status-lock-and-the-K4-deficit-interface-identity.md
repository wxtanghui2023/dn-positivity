# R7-LOCK-2026-09-27 — **R7 状态锁**：PROFILE-LEVEL STOP，STRUCTURAL $K_4$-DEFICIT **OPEN**

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:42 令 ✓）**：钉死四族目录；给出**接口恒等式** $\Delta_4(C)=N_{\rm square}+N_{\rm tetra}$；落 **R7 状态**；零程序计算 ✓。

**已查地图：命中（接续 R6／R7，非新案 ✓）**
所查：`docs/R7-2026-09-27-K4-shape-catalog-correction-and-T4-profile-STOP.md`（**形状目录 ＋ STOP** ✓✓）｜`docs/R6-2026-09-27-K4-common-centre-…`（**反例／亏空层级** ✓✓）｜`docs/C3-119-2026-09-27-triple-intersection-has-size-at-most-one.md`（**IA-1 前置，交叉引用，不重复登记** ✓✓）｜`docs/R5-2026-09-27-…`｜`docs/E58`（空间 A 同名，不跨 ✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（四词，见 §7）
D0: 本档对象 ＝ **档案已有** $K_4$ 亏空对象的**状态锁与接口恒等式**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出接口恒等式** $\Delta_4=N_{\rm square}+N_{\rm tetra}$ **＋ 更干净的四族计数推导** ＋ **R7 状态锁** ✓）
**[RESEARCH]**

---

## §0 结论（**状态锁 ＋ 接口恒等式 ＋ 干净计数 ✓✓**）

$$\boxed{\textbf{状态}:\ \textbf{R7 = PROFILE-LEVEL STOP},\quad \textbf{STRUCTURAL }K_4\textbf{-DEFICIT REMAINS OPEN}\ ✓✓\ (\text{不判 CLOSED}✗)}$$
$$\boxed{\textbf{★接口恒等式 ✓✓}:\ \boxed{\Delta_4(C)=\#K_4\big(G_2(C)\big)-T_4=N_{\rm square}+N_{\rm tetra}}\ ✓\ \text{—— 首项码相关，\textbf{不可}用满图常数替代 ✗}}$$
$$\boxed{\textbf{★补恒等式 ✓✓}:\ T_4=\sum_x\binom{b(x)}4=N_{\rm claw}+N_{\rm star}\ \Longrightarrow\ \textbf{接口直接化}:\ \Delta_4=N_{\rm square}+N_{\rm tetra}✓✓}$$
$$\boxed{\textbf{满图层亏空 ✓}:\ 380160-337920=\mathbf{42240}=11520+30720\ \text{（恰为 square＋tetra ✓）}}$$

---

## §1 四族目录（**钉死 ✓；并给更干净的计数推导 ✓**）

$$\text{对 }K_4\subseteq G_2(Q_{10})\ \text{平移一顶点至 }0，其余三点的}(\mathrm{wt}\,1\ \text{个数}, \mathrm{wt}\,2\ \text{个数})=(|W_1|,|W_2|)✓,\ |W_1|+|W_2|=3✓$$
| 形状 | 代表 | 共同球心 | 满图计数 |
|---|---|:--:|---|
| **claw** | $\{x,\ x{+}e_i,\ x{+}e_j,\ x{+}e_k\}$ | ✓ | $2^{10}\binom{10}3=1024\cdot120=\mathbf{122880}$ |
| **star** | $\{x{+}e_i,\ x{+}e_j,\ x{+}e_k,\ x{+}e_\ell\}$ | ✓ | $2^{10}\binom{10}4=1024\cdot210=\mathbf{215040}$ |
| **square** | $\{x,\ x{+}e_i,\ x{+}e_j,\ x{+}e_i{+}e_j\}$ | ✗ | $\dfrac{2^{10}\binom{10}2}4=\mathbf{11520}$ |
| **tetrahedron** | $\{0,\ e_i{+}e_j,\ e_i{+}e_k,\ e_j{+}e_k\}$ | ✗ | $\dfrac{2^{10}\binom{10}3}4=\mathbf{30720}$ |
$$\Longrightarrow\ \#K_4\big(G_2(Q_{10})\big)=122880+215040+11520+30720=\mathbf{380160}✓✓$$
$$\textbf{★更干净的推导 ✓✓（本档）}:\ \text{固定球心 }x:\ B_1(x)\ \text{有 }11\ \text{点};\ \text{其 4-子集分两类}:$$
$$\qquad\textbf{(a) 含 }x:\ \{x\}\cup(3\text{ 个邻点})=\textbf{claw}✓\ \text{—— 每 }x\ \text{有 }\binom{10}3=120\ \text{个 ⟹ 总数 }1024\cdot120=122880✓$$
$$\qquad\textbf{(b) 不含 }x:\ 4\text{ 个邻点}=\textbf{star}✓\ \text{—— 每 }x\ \text{有 }\binom{10}4=210\ \text{个 ⟹ 总数 }1024\cdot210=215040✓$$
$$\qquad\Longrightarrow\ \textbf{claw＋star 计数无需对称商}✓✓\ (\text{且}\ 120+210=330=\binom{11}4✓\ \text{恒等校验通过 ✓})$$
$$\textbf{★须留下的事实 ✓✓}:\ \text{star 与 tetrahedron 的\textbf{六条距离全为 2}}（\text{距离型完全相同}）\ \text{而一个可实现、一个不可实现} \Longrightarrow \boxed{\text{距离谱不足以决定共同球心可实现性}}✓✓$$

## §2 **接口恒等式**（**本档核心 ✓✓**）

$$\textbf{引理（}\textbf{唯一性}✓，档案 \texttt{C3-119} IA-1 ✓）:\ \text{对}\ \ge3\ \text{个中心},\ \big|\bigcap_iB_1(c_i)\big|\le1 \Longrightarrow\ \text{每个\textbf{已实现}的四元组有唯一球心}✓$$
$$\Longrightarrow\ T_4:=\sum_x\binom{b(x)}4\ \text{＝数 (球心 }x,\ 4\text{-子集}\subseteq S(x))\ \text{对};\ \text{由唯一性 ⟹ 与"已实现 }K_4"\ \textbf{一一对应}✓✓$$
$$\qquad\text{而已实现 }K_4\ \text{按球心是否属于该团分两类}:\ x\in K\Rightarrow\textbf{claw};\ x\notin K\Rightarrow\textbf{star}\ ✓ \Longrightarrow\ \boxed{T_4=N_{\rm claw}+N_{\rm star}}\ ✓✓$$
$$\text{四族构成 }G_2(C)\ \text{内全部 }K_4\ \text{的\textbf{划分}}✓\ (\text{R7 §1 情形分析 ✓}) \Longrightarrow\ \#K_4(G_2(C))=N_{\rm claw}+N_{\rm star}+N_{\rm square}+N_{\rm tetra}✓$$
$$\Longrightarrow\ \boxed{\Delta_4(C)=\#K_4(G_2(C))-T_4=N_{\rm square}+N_{\rm tetra}}\ ✓✓\ \text{—— \textbf{轮廓量被完全消去}✓✓}$$
$$\textbf{（\textbf{不可}写成常数的原因 ✓）}:\ \#K_4(G_2(C))\ \text{依赖 }C;\ \text{满图的 }380160\ \text{只在 }C=Q_{10}\ \text{时成立}\ ✗$$

## §3 满图层亏空（**42240 ✓**）

$$C=Q_{10}:\ b(x)\equiv11\Longrightarrow T_4=1024\cdot\binom{11}4=1024\cdot330=\mathbf{337920}=N_{\rm claw}+N_{\rm star}✓✓\ \text{（与 §1 独立算得者一致 ✓）}$$
$$\Longrightarrow\ \text{满图亏空}=380160-337920=\mathbf{42240}=\mathbf{11520}+\mathbf{30720}=N_{\rm square}+N_{\rm tetra}✓✓$$
$$\textbf{恒等校验 ✓✓}:\ \text{每球心 }x\ \text{的 4-子集总数}\ \binom{10}3+\binom{10}4=120+210=330=\binom{11}4✓\ \Longrightarrow\ T_4=1024\cdot330\ \text{与 }N_{\rm claw}+N_{\rm star}\ \text{两算一致 ✓✓}$$

## §4 R7 STOP 的**精确含义**（**逐项 ✓**）

$$\text{STOP 的对象 ✓}:\ \text{仅凭 }(n,|C|,\sum b,\ b\le11,\ Q,\ \text{既有 profile moment})\ \not\Rightarrow\ \text{非平凡 }T_4\ \text{界}✓$$
$$\text{上端显式 ✓}:\ 285=\sum_x(b(x)-1)\ \text{在 }b\le11\ \text{下\textbf{集中}}:285=28\cdot10+5\Longrightarrow T_4^{\max}=28\binom{11}4+\binom64=28\cdot330+15=\mathbf{9255}✓$$
$$\text{下端显式 ✓}:\ \text{把 excess 全分散为 }\delta{=}1:\ T_4=0✓\ (\text{对应 }b\le3,\ Q\le142✓\ \text{相容 ✓})$$
$$\Longrightarrow\ \boxed{T_4\in[0,9255]\ \text{两端皆相容} \Longrightarrow \textbf{profile 层无 leverage}}✓✓$$
$$\textbf{故 STOP 仅限 profile 层 ✓✓};\ \textbf{结构亏空 }N_{\rm square}+N_{\rm tetra}\ \textbf{不被此 STOP 触及}✓\ (\text{它\textbf{不是} profile 量 ✓})$$

## §5 下一次回来的**精确攻击点**（**P1 candidate ✓**）

$$\boxed{\text{119-cover}\ \Longrightarrow\ N_{\rm tetra}>0\ ?\qquad\text{或弱化版}\qquad N_{\rm square}+N_{\rm tetra}\ \ge\ L>0\ ?}✓$$
$$\text{（唐先生原提"四面体构型是否被迫出现"的精确化 ✓）};\ \text{本线\textbf{第一个非 profile 型（真几何）}对象 ✓✓}$$
$$\textbf{诚实边界 ⚠️}:\ \text{本档\textbf{没有} any handle on }N_{\rm square}+N_{\rm tetra}\ \text{的下界};\ \text{已知仅}:\ \text{① 二者皆\textbf{极大团}（不可延拓 ✓）；\ ② 与 }b\text{-profile \textbf{无关}}✓$$
$$\text{（可攻接口登记 ✓）}:\ \text{① }\sum_c|S(c)\cup V(H_c)|\le451;\ \text{② 团级 cap（Kleitman）与实现的耦合};\ \text{③ }N_1+N_2\ \text{下界 143 能否逼出 square\/tetra}$$

## §6 与档案关系（**防重复 ✓**）

| 项 | 档案 | 本档 |
|---|---|---|
| $|\cap_3|\in\{0,1\}$（唯一性） | `C3-119` IA-1 ✓ | **仅交叉引用，不重复登记** ✗✓ |
| $K_4$ 反例／亏空层级 | `R6` ✓ | 沿用 ✓ |
| 四族目录（含计数） | `R7` ✓ | **本档给更干净推导（含 $x$／不含 $x$ ✓）** |
| **接口恒等式 $\Delta_4=N_{\rm square}+N_{\rm tetra}$** | 未见 | **新增 ✓✓** |
| **R7 状态锁（PROFILE-LEVEL STOP／结构层 OPEN）** | 未见 | **新增 ✓✓** |

## §7 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "四族分解"
技术词 四族分解        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "实现型计数"
技术词 实现型计数      命中文件数=2    :: ./ASSETS-REGISTRY.md ./R7-2026-09-27-K4-shape-catalog-correction-and-T4-profile-STOP.md
$ bash scripts/tech_word_check.sh "结构亏空"
技术词 结构亏空        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "接口恒等式"
技术词 接口恒等式      命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`四族分解`／`结构亏空`／`接口恒等式` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`实现型计数` 仅命中本线自身 ✓）
- **注 ✓**：本档实质＝**§1 干净计数 ＋ §2 接口恒等式 ＋ §4 STOP 精确化 ＋ §5 攻击点精确化**（推导性 ✓）

## §8 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT/Terwilliger** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** $K(10,1)\ge120$ ✗（V290）；**不声称** $N_{\rm square}+N_{\rm tetra}$ 必然 $>0$ ✗ —— 只写"**这是下一个 P1 攻击点**"＋"**目前无 handle**" ⚠️
- **R7 只判 profile 层 STOP** ✓，**不判整个 R6 机制 CLOSED** ✗（照唐先生 ✓）
