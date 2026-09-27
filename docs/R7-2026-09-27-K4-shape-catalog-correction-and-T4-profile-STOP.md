# R7-2026-09-27 — **$K_4$ 结构定理确认** ＋ **形状目录修正** ＋ **R7 STOP 判定**

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:39 令 ✓）**：确认结构定理；**修正 §2 计数**；给出 $T_4$ 的界与 **STOP 判定**；零程序计算 ✓。

**已查地图：命中（接续 R6 ＋ 档案 `C3-119`，非新案 ✓）**
所查：`docs/R6-2026-09-27-K4-common-centre-…`（**$K_4$ 反例／亏空层级** ✓✓）｜`docs/C3-119-2026-09-27-triple-intersection-has-size-at-most-one.md`（**IA-1：$|\cap_3|\in\{0,1\}$ ✓✓ —— \textbf{唯一性已在该档}，本档不重复主张** ✓）｜`docs/R5-2026-09-27-…`｜`docs/R4-T-2026-09-27-…`｜`docs/FIBER-2026-09-26-…`｜`docs/TERM-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §6）
D0: 本档对象 ＝ **档案已有** $K_4$／亏空对象的**结构定理确认与目录修正**（重命名：否 ✗；新对象：**形状目录**为新增枚举层 ✓）
D1: 1（**首次给出 $K_4$ 形状目录（4 型）＋ 未实现恰两类＋ $\Delta_k=0\ (k\ge5)$ 的完整情形证明 ＋ $T_4$ 的 STOP 判定** ✓）
**[RESEARCH]**

---

## §0 结论（**结构定理确认 ✓｜计数修正 ✗｜STOP 判定 ✓**）

$$\boxed{\textbf{(1) 结构定理确认 ✓✓}:\ \Delta_3=0;\ \ \Delta_4\ge0\ \text{可正};\ \ \Delta_k=0\ (k\ge5)\ \text{—— \textbf{Helly 型阈值恰在 4}✓✓}}$$
$$\boxed{\textbf{(2) 强化 ✓}:\ \text{未实现的 }K_4\ \textbf{恰两型}，且两者皆\textbf{极大团}（不可延拓 ⟹ 自动给 }k\ge5\ \text{的 }\Delta_k=0✓✓）}$$
$$\boxed{\textbf{(3) 修正 ✗}:\ \text{唐先生 §2 的 }245760\ \text{与恒等式 }\Delta_4=245760-\sum_x\binom{b}4\ \textbf{均不成立}✗\ \text{（三处原因，见 §3）}}$$
$$\boxed{\textbf{(4) 形状目录（正确 ✓✓）}:\ 4\ \text{型}:\ \textbf{star}(215040)\ \big|\ \textbf{claw}(122880)\ \big|\ \textbf{square}(11520)\ \big|\ \textbf{tetrahedron}(30720);\ \text{总 }\mathbf{380160}✓}$$
$$\boxed{\textbf{(5) R7 STOP 判定 ✓✓}:\ \text{profile 级只给 }T_4\in[0,\ \mathbf{9255}]\ \text{且\textbf{两端皆相容}} ⟹ \textbf{R6 机制在 profile 级不足}✗✓\ \text{（触发唐先生的 STOP 规则 ✓）}}$$

---

## §1 结构定理的**完整情形分析**（**含权混合，用户证明的补全 ✓✓**）

$$\text{设 }K\subseteq G_2\ \text{为团}，|K|=k;\ \text{平移使 }v_0=0\in K✓\ (\text{平移保距离与共同球心存在性 ✓})$$
$$\text{其余顶点 }w:\ d(0,w)\le2\Longrightarrow \mathrm{wt}(w)\in\{1,2\}✓;\quad W_1:=\{i:\ e_i\in K\},\quad W_2:=\{u:\ \mathrm{wt}(u)=2,\ u\in K\}✓$$
$$\text{约束 ✓}:\ \textbf{(i)}\ u\in W_2,\ i\in W_1\Longrightarrow i\in u\ (\text{否则 }d(e_i,u)=3>2\ ✗)✓;\ \textbf{(ii)}\ u,v\in W_2\Longrightarrow u\cap v\ne\varnothing\ (\text{即 }d\le2\ ✓)✓$$
$$\textbf{情形 A（}|W_1|=0):\ |W_2|=k-1;\ \text{两两相交 2-子集族}\ \Longrightarrow\ \text{star（共点）或 triangle（}\{12,13,23\}✓,\ \text{仅 3 边 ✓）}$$
$$\qquad k\ge5\Longrightarrow|W_2|\ge4\Longrightarrow\ \text{非 triangle}\Longrightarrow\ \text{star}\Longrightarrow\ \text{共坐标 }i\Longrightarrow x=e_i\ \text{实现整个团 ✓（}d(e_i,0)=1,\ d(e_i,u)=1✓)✓$$
$$\qquad k=4\ \text{且 triangle}\Longrightarrow\ \text{四面体}\ \{0,e_1{+}e_2,e_1{+}e_3,e_2{+}e_3\}\Longrightarrow\ \textbf{无共同球心}✗✓\ (\text{R6 §1}✓)$$
$$\textbf{情形 B（}|W_1|=1,\ W_1=\{i\}):\ \text{所有 }u\in W_2\ni i\Longrightarrow x=e_i\ \text{实现 ✓（}d(e_i,e_i)=0✓,\ d(e_i,0)=1✓,\ d(e_i,u)=1✓)✓$$
$$\textbf{情形 C（}|W_1|=2):\ W_1=\{i,j\}\Longrightarrow \text{所有 }u\in W_2\supseteq\{i,j\}\ \text{而 }\mathrm{wt}(u)=2\Longrightarrow u=e_i{+}e_j,\ \textbf{至多一个} \Longrightarrow|W_2|\le1\Longrightarrow k\le4✓$$
$$\qquad k=4\ (\text{即 }|W_2|=1)\Longrightarrow\ \{0,e_i,e_j,e_i{+}e_j\}\Longrightarrow\ \textbf{无共同球心}✗✓\ (\text{"square"，本档补出 ✓})$$
$$\textbf{情形 D（}|W_1|\ge3):\ \text{所有 }u\in W_2\ \text{须含 }|W_1|\ge3\ \text{个坐标}\ ✗\ (\mathrm{wt}=2) \Longrightarrow W_2=\varnothing\Longrightarrow K\subseteq B_1(0)\Longrightarrow x=0\ \text{实现}✓$$
$$\Longrightarrow\ \boxed{\textbf{故}\ k\ge5\ \text{的团皆可实现（}\Delta_k=0✓）；未实现者仅情形 A-triangle 与情形 C \textbf{两型}，且皆 }\textbf{极大}✓✓$$
$$\text{（附赠 ✓）}:\ \text{star 与 tetrahedron 的\textbf{距离型完全相同}（六距全 2 ✓）而可实现性不同 ⟹ 与 P12-PASS 的"同 }A\ \text{异支撑"同型 ✓✓}$$

## §2 **形状目录**（**修正后的正确计数 ✓✓**）

$$\text{按距离型 + 几何形状分 }4\ \text{类（完备 ✓，含平移商 ✓）}:\quad \text{star}:\ \text{四顶点两两距离 2、四者\textbf{对称}}✓;\quad \text{claw}:\ \text{一中心 + 三叶，距离型 }\{1,1,1,2,2,2\}✓$$
$$\qquad \text{square}:\ \{v,v{+}e_i,v{+}e_j,v{+}e_i{+}e_j\},\ \text{型 }\{1,1,1,1,2,2\}✓;\quad \text{tetrahedron}:\ \{0,e_1{+}e_2,e_1{+}e_3,e_2{+}e_3\},\ \text{型全 }2✓$$
$$\text{可实现性 ✓}:\ \textbf{star}\ \text{（球心 }x\notin K✓）\ \big|\ \textbf{claw}\ \text{（中心即球心 ✓）};\qquad \textbf{square}\ ✗\ \big|\ \textbf{tetrahedron}\ ✗$$
$$\text{计数（全空间 }Q_{10}✓，平移商已计入 ✓）:\quad \text{star}=\frac{2^{10}\cdot10\binom93}4=1024\cdot210=\mathbf{215040}✓$$
$$\qquad \text{claw}=2^{10}\binom{10}3=1024\cdot120=\mathbf{122880}✓;\quad \text{square}=\frac{2^{10}\binom{10}2}4=\frac{1024\cdot45}4=\mathbf{11520}✓;\quad \text{tetrahedron}=\frac{2^{10}\binom{10}3}4=\mathbf{30720}✓$$
$$\Longrightarrow\ \#K_4\big(G_2(Q_{10})\big)=\mathbf{380160}✓✓$$

## §3 **唐先生 §2 计数修正**（**三处 ✗，逐条 ✓**）

$$\textbf{(3-a) 缺两个族 ✗}:\ 245760=215040(\text{star})+30720(\text{tetrahedron})\ \textbf{漏}\ \text{claw}(122880)\ \text{与}\ \text{square}(11520)✓⟹\ \text{正确总数为 }380160✓$$
$$\qquad\text{（claw 的存在性 ✓：}\{v,v{+}e_i,v{+}e_j,v{+}e_k\}\ \text{两两}\le2✓\ \text{且被 }x=v\ \text{实现 ✓ —— 唐先生的"从 }x\ \text{的 10 邻点取 4"只数了 }x\notin K\ \text{的 star 型 ✓，未数中心属于团者 ✗）}$$
$$\textbf{(3-b) "可实现总数＝245760"无效 ✗}:\ \sum_x\binom{b(x)}4\ \text{是 }C\ \text{的函数且只数\textbf{落在 }C\ \text{内}的四元组 ✓；而 }245760\ \text{是全空间常数 ✓ ⟹ 二者无可比性 ✗}$$
$$\textbf{(3-c) 恒等式 }\Delta_4=245760-\sum_x\binom{b}4\ \textbf{不成立}✗✓:\ \text{正确关系为}\ \boxed{\Delta_4=\#K_4\big(G_2(C)\big)-\sum_x\binom{b(x)}4}\ ✓\ \text{其中\#}K_4(G_2(C))\ \text{是\textbf{码相关}}量 ✗（全空间 380160 只是上界 ✓）}$$
$$\qquad\text{（常数形式不可得 ✓：}\Delta_4\ \text{必须按 }C\ \text{内四元组计数书写；全空间 380160 仅当 }C=Q_{10}\ \text{时才等于前者 ✓）}$$

## §4 $T_4$ 的界与 **R7 STOP 判定**（**关键 ✓✓**）

$$T_4:=\sum_x\binom{b(x)}4=\sum_j\binom j4n_j\ ✓;\quad \text{Pascal}:\ \binom{b}4=\binom{\delta+1}4=\binom\delta4+\binom\delta3✓\ \text{（唐先生 §3 ✓ 正确）}$$
$$\textbf{profile 级上界 ✓}:\ \text{在 }\sum_j(j-1)n_j=285,\ j\le11\ \text{下极大化 }T_4\ \text{（集中 ✓）}:\ 285=28\cdot10+5\Longrightarrow T_4\le28\binom{11}4+\binom64=28\cdot330+15=\mathbf{9255}✓$$
$$\qquad\text{（该极值 profile 对应 }Q=28\binom{11}2+\binom62=1555-285=\mathbf{1270}✓\ \text{＝ }Q\ \text{的上界 ✓，自洽 ✓）}$$
$$\textbf{profile 级下界 ✓}:\ T_4=0\iff\ \text{所有 }b\le3\iff n_2+2n_3=285\ \wedge\ n_2+3n_3=285+Q\Longrightarrow n_3=Q,\ n_2=285-2Q\ge0\iff Q\le142✓$$
$$\qquad\Longrightarrow\ \text{取 }Q\le142\ \text{即可自洽 ✓ ⟹ }T_4=0\ \textbf{与 profile 约束相容}✗✓$$
$$\Longrightarrow\ \boxed{\text{profile ＋ }A\ \text{只给 }T_4\in[0,\ 9255]\ \text{且\textbf{两端皆相容}} \Longrightarrow \textbf{该层级无法给 }T_4\ \text{非平凡界}✗✓}$$
$$\boxed{\textbf{故按唐先生 §5 的 STOP 规则}:\ \textbf{R6\/R7 机制本身不足（profile 级）}✗✓\ \text{—— 唯一出路须是\textbf{真正的几何约束}（非 profile 型 ✓）}}$$
$$\text{（几何候选 ✓，本档登记未做）}:\ \text{① 团级 cap（Kleitman ✓）与实现型计数的\textbf{耦合}};\ \text{② §1 的极大三角/方形是否\textbf{被迫出现}？};\ \text{③ }\sum_c|S(c)\cup V(H_c)|\le451✓$$

## §5 与档案关系（**防重复 ✓**）

| 项 | 档案 | 本档 |
|---|---|---|
| $|\cap_3|\in\{0,1\}$（唯一性） | **`C3-119-2026-09-27` IA-1 已有** ✓ | **不重复主张** ✗（引用 ✓） |
| $K_4$ 无共同球心反例 | `R6`（本线 ✓） | 沿用 ✓ |
| **形状目录 4 型 ＋ 未实现恰两型极大 ＋ $\Delta_k=0\,(k\ge5)$ 完整证明** | 未见 | **新增 ✓✓** |
| **§2 计数修正（380160 vs 245760）** | —— | **新增 ✓✓** |
| **$T_4$ 的 profile 级区间 $[0,9255]$ ＋ STOP 判定** | 未见 | **新增 ✓✓** |

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "形状目录"
技术词 形状目录        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "爪形"
技术词 爪形            命中文件数=0    ::
$ bash scripts/tech_word_check.sh "方形"
技术词 方形            命中文件数=9    :: ./A1-PROOF-SKELETON-and-constants.md ./C3-119-2026-09-27-triple-intersection-has-size-at-most-one.md ./FACE-2026-09-26-two-face-occupancy-audit.md
$ bash scripts/tech_word_check.sh "四面体"
技术词 四面体          命中文件数=2    :: ./ASSETS-REGISTRY.md ./R6-2026-09-27-K4-common-centre-compatibility-and-realizability-deficit-hierarchy.md
$ bash scripts/tech_word_check.sh "Helly"
技术词 Helly           命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`形状目录`／`爪形`／`Helly` 命中 0 ⟹ 本档自造标签，作结构命名，不作新性主张 ✓；`方形`／`四面体` 档案已有 ✓）
- **注 ✓**：本档实质＝**§1 完整情形证明 ＋ §2 形状目录 ＋ §3 计数修正 ＋ §4 STOP 判定**（推导性 ✓）

## §7 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT/Terwilliger** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **不声称** $K(10,1)\ge120$ ✗（V290）；**不声称** $T_4$ 无从约束（只说"**profile 级**无从约束" ✓，几何级可能仍有机会 ✓）
- §1 的"未实现恰两型且极大"为**本档结论** ✓（唐先生的结构定理经**补全**后成立 ✓：原证明仅覆盖 $|W_1|=0$ 情形 ✓）
- §3 的三处修正**必须**与 §2 目录一同引用 ✓（防复用错误常数 245760 ✗）
