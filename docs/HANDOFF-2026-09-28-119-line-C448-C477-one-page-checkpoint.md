# HANDOFF-2026-09-28 — **119-cover 线｜C-448 → C-477 单页交接（checkpoint）＋ 两处新推导**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:50 令 ✓）**：本轮**只收尾、不盲攻** ✓ —— 出单页交接 ＋ 钉死下一轮唯一主攻量；**零新增搜索** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-477／C-476／C-472，非新案 ✓）**
`docs/WITM44-2026-09-28-…`（**$m(44)$ 审计／外部度均值 3.814 ✓✓✓**）｜`docs/WITPAR-2026-09-28-…`（**$\lambda_{\min}{=}-5$／上界侧 ✓✓✓**）｜`docs/WITINT-2026-09-28-…`（**② 归约 ✓✓**）｜`docs/WITPOBJ-2026-09-28-…`（**单调下界障碍 ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §6）
D0: 本档对象 ＝ **档案已有** $m(44)$／$\frac12Q_{10}$／$A(9,3)$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次完成 C-448→C-477 之单页交接 ＋ 首次指出唐先生 P1 链之\ \textbf{顶点覆盖缺口}（$e(S)\le7\Rightarrow\alpha(S)\ge\mathbf{37}$ 非 41）＋ 首次证明 $\boxed{A_{\rm even}(10,4)=A(9,3)=40}$（穿刺/延拓论证）** ✓）
**[RESEARCH]**

---

## §0 当前问题接口（**✓✓ 钉死**）

$$\boxed{m(44):=\min_{|S|=44}e_2(S)}\quad\big(S\subseteq E(Q_{10})\ \text{＝偶重量层},\ e_2{=}\text{层内距离-2 边数 ✓}\big)$$
$$\qquad\textbf{（与 119 之接口 ✓）}:\ \text{奇偶分裂 }C_E,C_O\ \text{于 }Q_{10}\ \text{二分层 }E\sqcup O\ \big(|E|{=}|O|{=}512✓\big),\ a{=}|C_E|,\ b{=}|C_O|,\ a{+}b{=}119✓$$
$$\qquad L_E:=10a-|N(C_E)|\le9a-393✓\Longrightarrow\boxed{p_E\le\tfrac52L_E}\ ✓\Longrightarrow\ a{=}44:\ L_E\le3\Rightarrow p_E\le7✓$$
$$\qquad\Longrightarrow\ \text{若 }\boxed{m(44)\ge8}\Longrightarrow a{=}44\ \text{无 119-cover ✓✓}$$

## §1 已闭／已废（**不再重开 ✓**）

| 模块 | 结论 | 状态 |
|---|---|---|
| C-472 covering bridge（$q$ 上界） | 覆盖条件皆**单调下型** ⟹ 只给 $q$ 下界 | **CLOSED** ✗ |
| C-475 共同邻域容量 | $N(C_0){\cap}N(C_1)\subseteq N(H)\cup\{$距离-2 对之共同邻$\}$ ⟹ $\le9h{+}2q$ ⟹ **归约到 C-472 同一不等式** | **CLOSED** ✗ |
| Thm 2.5／4.9 SDP | 抽取完成 ✓；$n{=}10$ 之值 $105.2223<107\le K(10,1)$ ⟹ 跨不到 120 | **不够** ✗ |
| 谱下界（$\frac12Q_{10}$） | $\lambda_{\min}{=}\mathbf{-5}$ 非 $-3$ ⟹ $s{=}44,45$ 无正下界 | **废弃** ✗✗ |
| Type I $(0,4,4,4)$ | 状态图无三角形 | **KILLED** ✓✓✓ |
| Type III $(2,2,3,3)$ | $|F_p|{=}3\Rightarrow J(6,3)$-三角形（刚性 ✓）但**惰性**（16/16 组合可共存） | **INERT** ✗ |
| Type II $(2,2,2,4)$ 局部 | 状态空间 15/30 ✓；$|D|\le14{\sim}16$ ✓；但只触及 41/119 点 | **无 P1** ⚠️ |

## §2 奇偶路线之有效部分（**✓✓ 保留**）

$$44\le a,b\le75✓;\quad L_E\le9a-393✓,\ L_O\le9b-393✓\Longrightarrow\boxed{L_E+L_O\le285}\ ✓\ \big({=}9\cdot119-786{=}\text{excess}\ ✓\big)$$
$$\sum_y k_y=10a✓\ \big(k_y{=}|N(y)\cap C_E|✓\big);\quad \boxed{2p_E=\sum_y\binom{k_y}2}\ ✓✓;\quad \binom k2\le5(k-1)\ (k\le10)\Longrightarrow p_E\le\tfrac52L_E✓$$
$$\sum_x\binom{m_x}2=2(n_1{+}n_2)\Longrightarrow n_1{+}n_2\ge143✓;\quad |\pi_i(C)|=119-e_i\ge62\Longrightarrow e_i\le57\Rightarrow|E(C)|\le570✓$$
$$\boxed{\text{与 C-472 之 }q\ \text{为\ \textbf{不同对象}}}\ ✓\ \big(q\ \text{＝跨半侧；}p_E\ \text{＝同奇偶层 ✓}\big)\ \text{—— 唐先生判断 ✓✓}$$

## §3 ✗✗ 新推导①：**P1 链有顶点覆盖缺口**（本档）

$$\text{唐先生之链（}13{:}41\big):\ |S|{=}44,\ e(S)\le7\Longrightarrow\alpha(S)\ge\mathbf{41}\ \text{vs}\ \alpha{=}A(10,4){=}40\Longrightarrow\text{矛盾}\ ✗✗$$
$$\textbf{（实测 ✗）}:\ \text{取每条边一端 ⟹ 顶点覆盖 }|T|\le e(S)\le7\Longrightarrow S\setminus T\ \text{独立},\ |S\setminus T|\ge44-7=\mathbf{37}\ ✗\ \text{非 41}$$
$$\qquad\Longrightarrow\ 37\le40\ \textbf{不矛盾}\ ✗✗\Longrightarrow\ \boxed{\alpha\text{-路线\ \textbf{给不出}\ }m(44)\ge8}\ ✗$$
$$\qquad\textbf{（}\alpha\ \text{能给的仅有 ✓）}:\ \tau\ge44-\alpha{=}4\Longrightarrow\boxed{e(S)\ge4}\ \big(\text{弱，距 8 尚远 ✗}\big)$$
$$\qquad\Longrightarrow\ \text{故 }m(44)\ge8\ \text{须由\ \textbf{直接极值论证}（非 }\alpha\ \text{中转）✓；}\ \text{唐先生 §5–§6 之"blocking capacity"方向\ \textbf{仍成立}✓（唯其 }\alpha\ \text{环节须删 ✗）}$$

## §4 ✓✓ 新推导②：**$A_{\rm even}(10,4)=A(9,3)=40$**（本档）

$$\textbf{① 上界 ✓}:\ C\ \text{＝偶重量 }(10,4)\text{-码；删去任一坐标 ⟹ 长度 9；因 }C\ \text{内距离皆\ \textbf{偶}且}\ge4\Longrightarrow\text{删一位后}\ge3\Longrightarrow|C|\le A(9,3)=\mathbf{40}$$
$$\textbf{② 下界 ✓}:\ \text{取 }(9,3)\text{-码 }D\ \big(|D|{=}A(9,3){=}40✓\big),\ C:=\{(d,\ \mathrm{parity}(d)):d\in D\}✓$$
$$\qquad d_D\ \text{奇}\ (\ge3)\Longrightarrow\text{校验位异}\Longrightarrow d_C=d_D+1\ge4✓;\quad d_D\ \text{偶}\ (\ge4)\Longrightarrow\text{校验位同}\Longrightarrow d_C=d_D\ge4✓$$
$$\qquad\Longrightarrow\ C\ \text{为偶重量 }(10,4)\text{-码},\ |C|{=}40✓\Longrightarrow\boxed{A_{\rm even}(10,4)=A(9,3)=\mathbf{40}}\ ✓✓$$
$$\qquad\textbf{（意义 ✓✓）}:\ \text{(i) 确认 }\alpha(\tfrac12Q_{10}){=}40✓\ \text{（唐先生引用 ✓）；(ii) 与 C-442 之 }A(9,3){=}40\ \text{同源 ✓（同一常数）；(iii) 为 }\S0\ \text{之阈值提供确切值 ✓}$$

## §5 P1 状态与下一轮主攻（**✓✓ 照唐先生，已删缺口环节**）

$$\boxed{\text{119-cover / C-477：LIVE}}\ ✓;\quad \boxed{\text{P1：real structural attack point}}\ ✓;\quad \boxed{m(44)\ge8:\ \textbf{OPEN}}\ ⚠️$$
$$\qquad\Longrightarrow\ \boxed{\text{P1 已形成，但 quantitative lower bound 未证}}\ ✓\ \big(\text{唐先生之措辞 ✓✓}\big);\ \text{且}\ \boxed{\text{缺口很干净}\ne\text{缺口很容易}}\ ✓$$
$$\textbf{（下一轮唯一主攻量 ✓✓）}:\ \boxed{\text{极大 }(10,4)\text{-码的外部点 blocking／degree-1 结构}}\ ✓$$
$$\qquad\textbf{已定之事实 ✓}:\ I\ \text{极大}\ \big(|I|{=}40✓\big)\Longrightarrow\forall x\notin I:\ d_I(x)\ge1✓\ \big(\text{否则 }I\cup\{x\}\ \text{为 41-码 ✗}\big);\quad \sum_{x\notin I}d_I(x){=}1800,\ \text{均值 }3.814✓$$
$$\qquad\textbf{切点 ✓✓}:\ \text{若\ \textbf{存在} 4 个 pairwise }d\ge4\ \text{且 }d_I{=}1\ \text{之外部点}\Longrightarrow e_2(I\cup X){=}4\Longrightarrow m(44)\le4\ \textbf{P1 死}\ ✗;\ \text{若一切极大码 }\min d_I\ge2\Longrightarrow\text{"40＋4"族}\ge8\ \text{边}\ ⟹\ \text{支持 P1} ✓$$
$$\qquad\textbf{（三支 ✓）}:\ \text{P1-A 极大码结构／外部度分布／轨道（文献优先 ✓）};\ \text{P1-B Delsarte-LP 直排 }e_2\le7✓;\ \text{P1-C 具体码之 }D_1(I){=}\{x:d_I(x){=}1\}\ \text{之 }\alpha_{\ge4}\ ✓$$

## §6 下一轮禁止事项（**✓✓ 照唐先生**）

$$\textbf{禁 ✓}:\ \text{① 继续随机/退火搜 }m(44)\ \big(\text{本档实测：独立集仅 29 vs 真值 40；44 点最少边仅 18–21 ✗}\big);\ \text{② 直接上大型 SAT};\ \text{③ 把"未找到 }e\le7\text{"当下界};\ \text{④ 由\ \textbf{非极大} 29-码之外部度分布（}\{1{:}32,2{:}151,3{:}231,4{:}67,5{:}2\}\big)\ \text{推断 40-码}✓$$
$$\qquad\Longrightarrow\ \boxed{\text{下一次启动条件：先做极大 }(10,4)\text{-码结构／外部 blocking，再决定是否入 LP 或精确搜索}}\ ✓✓$$

## §7 技术词回查 ＋ 边界（**✓✓**）

```
$ bash scripts/tech_word_check.sh "顶点覆盖缺口" "偶重量码恒等式" "交接单页"
技术词 顶点覆盖缺口   命中文件数=0    ::
技术词 偶重量码恒等式 命中文件数=0    ::
技术词 交接单页       命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 顶点覆盖缺口 | 0 | 0 | ✓（自造标签 ✓） |
| 偶重量码恒等式 | 0 | 0 | ✓（自造标签 ✓） |
| 交接单页 | 0 | 0 | ✓（自造标签 ✓） |

- **零新增搜索** ✓（本档仅符号推导 ✓；C-477 之搜索数据为引用 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（已分栏 ✓）
- **一处必删**（§3 之 $\alpha$ 环节 ✗✓）＋ **一处新证**（§4 之恒等式 ✓✓）已显式标注 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $m(44)\ge8$ ✓✗（OPEN ⚠️）；**不声称** P1 死 ✗（V290）
