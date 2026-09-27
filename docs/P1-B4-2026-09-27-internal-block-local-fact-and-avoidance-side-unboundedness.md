# P1-B4-2026-09-27 — **$b_4$ 的独立控制** micro-check：新局部事实 ＋ avoidance 侧无界 ＋ 三来源汇总

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 23:21 令 ✓）**：做 $b_4$ 的 P1 micro-check（能否被非 profile 机制压低）；零程序计算 ✓；**不升级任何项** ✓。

**已查地图：命中（接续 C-419／C-418／P1-D4b，非新案 ✓）**
`docs/P1-NINT-2026-09-27-…`（**折衷关系／独立性闸** ✓✓）｜`docs/P1-SCREEN-2026-09-27-…`（**C-418 门** ✓✓）｜`docs/P1-D4b-2026-09-27-…`（**$C_0$ 逃逸反例** ✓✓）｜`docs/P1-G2-2026-09-27-…`｜`docs/P1-MICRO-…`（**$(\alpha)(\alpha')$** ✓✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词，**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** $b_4$／见证对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出内部块的局部事实 $S(y)\cap u=\varnothing$（$d_1(y)\le6$）＋ avoidance 侧 $b_4$ 无界族 ＋ 三来源汇总** ✓）
**[RESEARCH]**

---

## §0 结论（**新局部事实 ✓✓｜avoidance 侧无界 ✓✓｜三来源皆不给控制 ⚠️**）

$$\boxed{\textbf{(1) ★新局部事实（本档 ✓✓）}:\ \text{内部块 }y=c\oplus u\ \big(u\subseteq S(c),|u|=4✓\big)\ \Longrightarrow\ \boxed{S(y)\cap u=\varnothing}\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{d_1(y)\ \le\ 10-4=6}\ ✓\ \big(\textbf{排列级、非 profile 型 ✓}\big)$$
$$\qquad\textbf{（证明 3 行 ✓）}:\ i\in u\Longrightarrow y\oplus e_i=c\oplus e_{(u\setminus i)}\ \big(\text{重量 3、支撑}\subseteq S(c)✓\big)\ \overset{(\alpha)}{=}\ \notin C\ \Longrightarrow\ i\notin S(y)✓$$
$$\boxed{\textbf{(2) ★avoidance 侧：}b_4\ \textbf{无界（}\le\binom{10}4=210✓\big)✓✓}:\ \text{显式族 }C_1:=\{0\}\cup\{e_i\}\cup\{e_u:u\in\mathfrak U\}\ \text{满足\textbf{全 avoidance}}\ ✓;\ \text{且 }b_4=\#\mathfrak U✓$$
$$\qquad\textbf{（但 ✓）}:\ C_1\ \textbf{非覆盖码}✗ \Longrightarrow\ \text{只证明"\textbf{avoidance 层面}"}b_4\ \text{无界 ✓（＝唐先生所预测的 natural limit 支 ✓），\textbf{不}证明 119-cover 中 }b_4\ \text{可大}✗✓$$
$$\boxed{\textbf{(3) 三来源汇总 ⚠️}:\ \text{avoidance}✗（C_1 ✓）;\ \text{degree/profile}✗（只见 }d_4\ \text{总数 ✓）;\ \text{covering}✗（只给需求关系、单侧 ✓） \Longrightarrow \textbf{三条皆不给 }b_4\ \textbf{的独立控制}⚠️}$$
$$\boxed{\textbf{(4) 状态（照唐先生 23:21 ✓）}:\ \textbf{C-419 PASS ＋ 新排列级关系，未闭合}✓;\ \textbf{下一攻击点 ＝ 独立控制 }b_4✓;\ \textbf{不 CLOSED}✗、\textbf{不 NO-GO}✗;\ \textbf{HOLD}✓}$$

---

## §1 **新局部事实的证明**（**3 行 ✓✓**）

$$\text{设 }A(c)=0\ ✓,\ u\subseteq S(c)\ (|u|=4✓),\ y=c\oplus u\in C\ ✓（\text{内部块 ✓}\big)$$
$$\text{取 }i\in u:\quad y\oplus e_i=c\oplus e_{(u\setminus i)}✓;\ |u\setminus i|=3✓\ \text{且其支撑}\ u\setminus i\subseteq S(c)✓$$
$$\qquad\overset{(\alpha)}{\Longrightarrow}\ \text{（P1-MICRO 内部子立方体排斥：相异 }i,j,x\in S(c)\Rightarrow c\oplus e_i\oplus e_j\oplus e_x\notin C✓\big)}\ \Longrightarrow\ y\oplus e_i\notin C\ \Longrightarrow\ i\notin S(y)✓$$
$$\Longrightarrow\ S(y)\cap u=\varnothing\ \Longrightarrow\ |S(y)|\le|[10]\setminus u|=6\ \Longrightarrow\ \boxed{d_1(y)\le6}✓✓$$
$$\textbf{性质 ✓}:\ \text{这是\textbf{纯排列级}事实（依赖"哪 4 个坐标构成 }u"\ ✓）};\ \text{且它\textbf{不}由 }\{d_j\}\ \text{或 }\{N_j\}\ \text{决定 ✓} \Longrightarrow\ \text{过 C-418 门 ＋ 独立性闸 ✓}$$
$$\textbf{注 ✓}:\ \text{此前所有局部事实（}A(c)=0\Rightarrow(\alpha)(\alpha')\ ✓\big)\ \text{都是"以 }c\ \text{为中心"的};\ \text{本事实是\textbf{以内部块为中心}的\textbf{第二条}（第一条为 P1-D4b 的 }C_0\ ✓\big)✓}$$

## §2 **avoidance 侧 $b_4$ 无界**（**显式族 ＋ 逐类核验 ✓✓**）

$$C_1:=\{0\}\ \cup\ \{e_i:1\le i\le10\}\ \cup\ \{e_u:u\in\mathfrak U\},\qquad \mathfrak U\subseteq\binom{[10]}4\ \text{任意子族 ✓}\ \big(b_4(0)=\#\mathfrak U✓\big)$$
$$\textbf{核验 ✓（点数类型 0／1／4 ✓）}:\quad\textbf{① 无重量 2、3、5、6 点} \Longrightarrow A(0)=0✓,\ (\alpha)\ \text{在 0 成立}✓$$
$$\textbf{② 无 square ✓}:\ \text{2-coset}=\{v,v{+}e_a,v{+}e_b,v{+}e_a{+}e_b\}\ \text{需重量 2 点（}v=0✓\big)\ \text{或重量 3／5 点（}v=e_i/e_u✓\big) \Longrightarrow \text{全部 }\notin C_1✗✓$$
$$\textbf{③ 无 tetra ✓}:\ \text{3-coset 偶部}=\{v,v{+}e_a{+}e_b,v{+}e_a{+}e_c,v{+}e_b{+}e_c\}\ \text{需重量 2（}v=0✓\big)\ \text{、1／3（}v=e_i✓\big)\ \text{、或 2／6（}v=e_u✓\big)\ \text{点} \Longrightarrow \text{总有一顶点 }\notin C_1✗✓$$
$$\qquad\textbf{（}v=e_u\ \text{情形的细查 ✓）}:\ a,b,c\ \text{中 }|u|\ \text{的落入数决定偏移重量：全在 }u\Rightarrow\text{重量 2}✗;\ \text{1 在外}\Rightarrow\text{一对重量 2}✗;\ \text{2 在外}\Rightarrow\text{重量 6}✗;\ \text{3 在外}\Rightarrow\text{全重量 6}✗✓\ \Longrightarrow\ \text{恒不可行 ✓}$$
$$\textbf{④ }A(y)=0\ \text{对 }y=e_u✓:\ \text{含 }y\ \text{的 square 需 }y\oplus e_a\ \text{（重量 3 或 5）}\notin C_1✗ \Longrightarrow \text{空真 ✓}$$
$$\Longrightarrow\ C_1\ \textbf{满足全 avoidance}✓✓;\ \text{取 }\mathfrak U=\binom{[10]}4\ \text{得 }b_4(0)=\mathbf{210}=\binom{10}4\ \big(\textbf{上界可达 ✓}\big)✓✓$$
$$\Longrightarrow\ \boxed{\text{在 avoidance 层面，}b_4\ \text{可任意大（到 210 ✓）}} \Longrightarrow\ \textbf{"N}_{\rm int}\ \textbf{路线的自然极限"支获得明确支持}✓✓\ \big(\text{但 }C_1\ \text{非覆盖码}✗\big)$$

## §3 **三来源汇总**（**⚠️ 皆不给独立控制 ✓**）

| 来源 | 能否独立控制 $b_4$ | 依据 |
|---|---|---|
| avoidance | **不能** ✗ | $C_1$ 全 avoidance 且 $b_4$ 可达 210 ✓ |
| degree／profile | **不能** ✗ | 只见 $d_4=\sum_jb_j$ 总数、不见分裂（C-419 ✓） |
| covering 本身 | **不能（仅单侧）** ✗ | 只给 $b_3+4b_4\ge\binom s3$（需求型 ✓，不能上界 $b_4$ ✓） |
| **新事实 §1** | **部分**⚠️ | $S(y)\cap u=\varnothing\Rightarrow d_1(y)\le6$ ✓ —— 对 $y$ 的**度数**有约束，**不**直接界 $b_4$ ✗ |

$$\Longrightarrow\ \textbf{现状 ⚠️}:\ \text{尚无任何已证机制能独立压低 }b_4 \Longrightarrow\ \text{C-419 的折衷式\textbf{暂不能}产生实质 squeeze}✗$$
$$\textbf{（下一步的两个出口 ✓）}:\ \text{① 找新机制界 }b_4\ \text{（如用 §1 的 }d_1(y)\le6\ \text{做全局计数 ⚠️）};\ \text{② 若在 119-cover 中 }b_4\ \text{可大 ⟹ 明确记为 natural limit ✓}$$

## §4 状态锁（**照唐先生 23:21 ✓**）

$$\boxed{\text{C-419}:\ \textbf{PASS ＋ 新排列级关系，未闭合}✓;\ \textbf{下一攻击点 ＝ 独立控制 }b_4✓;\ \text{无理由 CLOSED}✗、\text{无理由 NO-GO}✗;\ \textbf{HOLD}✓}$$
$$\textbf{未升级 ✓}:\ \text{短名单项皆未升级 ✗};\ \textbf{未改} closure gate／nogo gate ✗;\ 119\ \text{主问题仍完全 LIVE}✓$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "内部块群" "级联下降" "块容量上限"
技术词 内部块群      命中文件数=0    ::
技术词 级联下降      命中文件数=0    ::
技术词 块容量上限    命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 内部块群 | 0 | 0 | 0（本档自造标签 ✓） |
| 级联下降 | 0 | 0 | 0（本档自造标签 ✓） |
| 块容量上限 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 本档自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 局部事实 ＋ §2 avoidance 侧无界 ＋ §3 三来源汇总**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **不声称** 119-cover 中 $b_4$ 可大 ✗（$C_1$ 非覆盖码 ✓）；**不声称** 折衷式无用 ✗（只写"**暂不能产生实质 squeeze**" ✓）
- §2 的核验③（tetra 情形细查）**必须保留** ✓（该族正确性的直接证据 ✓）
