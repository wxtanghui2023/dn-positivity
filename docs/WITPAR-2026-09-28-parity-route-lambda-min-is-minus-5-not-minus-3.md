# WITPAR-2026-09-28 — **奇偶路线审计：$\mathbf{\lambda_{\min}(\frac12Q_{10})=-5}$ 非 $-3$ ✗✗ ⟹ 谱下界失效（$a{=}44/45$ 未被杀）；上界侧有效；**新资产已登记**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 13:41 令 ✓）**：奇偶分层路线审计（P0 重展开）；**有限穷举／谱计算** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-475／C-472／C-442，非新案 ✓）**
`docs/WITINT-2026-09-28-…`（**② 归约到 C-472 ✓✓✓**）｜`docs/WITPOBJ-2026-09-28-…`（**$P{:=}P_0{\cup}P_1$／单调下界障碍 ✓✓✓**）｜`docs/WITB45-2026-09-28-…`（**$|C_0|\ge45$ ✓✓**）｜`docs/C-427 registry`（**$107\le K(10,1)\le120$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §4）
D0: 本档对象 ＝ **档案已有** 奇偶分层／$L$／$p$ 对象（重命名：否 ✗；新对象：**奇偶分层 $p_E/p_O$ ＋ $L_E/L_O$ 系首次入档** ✓）
D1: 1（**首次计算 $\frac12Q_{10}$ 之完整谱并判定 $\lambda_{\min}{=}-5$（非 $-3$）⟹ 唐先生之谱下界失效 ＋ 首次给出奇偶路线之\ \textbf{有效上界侧}（$44\le a,b\le75$、$L_E\le9a{-}393$、$L_E{+}L_O\le285$、$p_E\le\frac52L_E$）＋ 首次证明该路线与 C-472 之 $q$ 为\ \textbf{不同对象}（但下界工具缺）** ✓）
**[RESEARCH]**

---

## §0 结论（**✗✗$\lambda_{\min}$ 更正 ⟹ 下界失效｜✓上界侧有效｜窗口不存在**）

$$\boxed{\textbf{(1) ✗✗\frac12Q_{10} 之谱（本档完整计算）}:\ }\text{特征值}\ =\ K_2(|S|)\ \big(|S|{=}0..5\ \text{模补 ✓，因偶类上 }\chi_S{=}\chi_{S^{\mathsf c}}✓\big):\ \big\{45,\ 27,\ 13,\ 3,\ -3,\ \mathbf{-5}\big\}\ ✓✓$$
$$\qquad\text{(数值核对 ✓)}:\ \text{512 顶点，度 }45\ \text{（min}{=}\text{max}{=}45✓）；\mathrm{eigvalsh}\ \text{之最小特征值}\ =\ \mathbf{-5.0000}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\lambda_{\min}(\tfrac12Q_{10})\ =\ \mathbf{-5}\ \ \text{而非}\ \ -3}\ ✗✗\ \big(\text{唐先生本轮用 }-3\ ✗\big)$$
$$\boxed{\textbf{(2) ✗✗⟹ 谱下界失效（a{=}44/45 \textbf{未被杀}）}:\ }\text{Hoffman 型界}\ p_E(s)\ge\tfrac12\big(d\tfrac{s^2}{V}+\lambda_{\min}s(1-\tfrac sV)\big)\ \big(d{=}45,V{=}512\big)✓$$
$$\qquad\text{用正确 }\lambda_{\min}{=}-5:$$
| $s$ | 谱下界（$\lambda{=}-5$ ✓） | 唐先生所用（$\lambda{=}-3$ ✗） |
|---|---|---|
| 44 | $\mathbf{-15.47}$ ⟹ **无信息** ✗ | $24.75$ ⟹ ≥25（**无效** ✗✗） |
| 45 | $\mathbf{-13.62}$ ⟹ **无信息** ✗ | $27.42$ ⟹ ≥28（**无效** ✗✗） |
| 50 | $-2.93$ ⟹ 无信息 ✗ | — |
| 60 | $25.78$ ⟹ ≥26 ✓ | — |
| 74 | $82.38$ ⟹ ≥83 ✓ | — |
$$\qquad\Longrightarrow\ \boxed{\text{谱界仅在 }s\gtrsim55\ \text{起才为正 ⟹ 于 }a{=}44,45\ \textbf{给不出任何下界}}\ ✗✗\Longrightarrow\ \text{"}a{=}44\ \text{不可能"与"28}\le p_E\le30\text{"\ \textbf{均不成立}} ✗✗$$
$$\boxed{\textbf{(3) ✓✓上界侧有效（本档确认，逐条 ✓）}:\ }10b\ge512-a\Longrightarrow\boxed{44\le a,b\le75}\ ✓;\quad L_E:=10a-|N(C_E)|\le9a-393✓$$
$$\qquad L_O\le9b-393✓\Longrightarrow\boxed{L_E+L_O\le285}\ ✓\ \big(9\cdot119-786{=}285{=}\text{excess ✓ 数值巧合确为真 ✓}\big)$$
$$\qquad\sum_y\binom{k_y}{2}=2p_E✓\ \big(k_y{=}|N(y)\cap C_E|✓,\ \sum_y k_y{=}10a✓\big);\quad \binom k2\le5(k-1)\ \big(k\le10✓\big)\Longrightarrow\boxed{p_E\le\tfrac52L_E}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{a{=}44:\ L_E\le3\Rightarrow p_E\le7}✓;\quad \boxed{a{=}45:\ L_E\le12\Rightarrow p_E\le30}✓\ \text{（\textbf{仅上界} ✗ 无配对下界 ✗）}$$
$$\qquad\text{另两条（✓）}:\ \sum_x\binom{m_x}2=2(n_1{+}n_2)\ \text{＋凸性}\Longrightarrow\boxed{n_1{+}n_2\ge143}✓;\quad |\pi_i(C)|{=}119-e_i\ge K(9,1){=}62\Longrightarrow\boxed{e_i\le57}\Rightarrow|E(C)|\le570✓$$

---

## §1 与 C-472 之比较（**✓ 确为不同对象；但下界工具缺 ✗**）

| | C-472／C-475 | 本档（奇偶路线） |
|---|---|---|
| 核心量 | $q=\#$**跨半侧**距离-2 对（$C_0\times C_1$，按末坐标分半 ✓） | $p_E=\#$**同奇偶侧**距离-2 对 ✓ |
| 下界来源 | $\|X_L\|\le2q$（覆盖 ⟹ 下界 ✓） | 谱界（**失效** ✗）／$\alpha(\frac12Q_{10}){=}A(10,4){=}40$（仅给 $p_E\ge1$ ✗） |
| 上界来源 | **无** ✗（单调下界障碍 ✓） | $\boxed{p_E\le\frac52L_E}$ ✓✓（**有** ✓） |
$$\Longrightarrow\ \boxed{\text{确为\ \textbf{不同对象}（唐先生之判断 ✓✓）；且本路线\ \textbf{上界侧健全}}\ ✓\ \text{—— 唯\ \textbf{下界侧}之工具（谱）用错了参数 ✗}}$$
$$\qquad\textbf{（正确下界之可及工具 ✓ 登记）}:\ \text{① }\alpha{=}A(10,4){=}40\ \text{仅给 }p_E\ge1\ ✗\ \text{（}|S|{-}40{=}4\ \text{之平凡推论 ✓）};\ \text{② 组合下界（极大独立集 ⊕ 4 点之加边数 ✓）\ —— 未建立 ✗}$$
$$\qquad\textbf{（粗略估计 ✓ 非定理 ✗）}:\ \text{取 40 点 (10,4)-码 }I\ \text{＋ 4 点：}\sum_{x\notin I}|N(x)\cap I|=40\cdot45=1800\ \text{摊于 472 点}\Longrightarrow\text{均}\approx3.8\Longrightarrow\text{4 点约添 }12{\sim}16\ \text{边}$$
$$\qquad\Longrightarrow\ \text{若真值}\ \ge8\ \text{则 }a{=}44\ \text{确实死 ✓✓\ —— 但这\ \textbf{需要严格下界} ✗（本档未得 ✗）}$$

## §2 现状（**⚠️ 照唐先生 (c)：SUSPENDED ✓**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{\lambda_{\min}(\frac12Q_{10}){=}-5}\ ✓✓;\ \text{② 谱界在 }a{=}44,45\ \text{无信息 ✗};\ \text{③ }44\le a,b\le75✓;\ \text{④ }L_E{+}L_O\le285✓;\ \text{⑤ }p_E\le\frac52L_E✓\ \big(\text{含 }p_E\le7(a{=}44),30(a{=}45)\big);\ \text{⑥ }n_1{+}n_2\ge143✓;\ \text{⑦ }e_i\le57,|E(C)|\le570✓;\ \text{⑧ 与 C-472 为不同对象 ✓}$$
$$\textbf{未确立 ⚠️}:\ p_E\ \text{之\ \textbf{任何非平凡下界}（关键缺口 ✗）};\ a{=}44/45\ \text{之排除};\ q\ \text{之上界};\ M\ \text{之真值};\ \text{Type II 全局可行性};\ \text{Type III 之 P1}$$
$$\textbf{（唐先生之裁定 ✓）}:\ \boxed{\text{119 线 ＝ SUSPENDED（no current P1 source）}}\ ✓;\ \text{复活条件＝新资产须提供此前没有的\ \textbf{P1 上界／排斥机制} ✓✓}$$
$$\qquad\textbf{（本档之补充 ✓）}:\ \text{奇偶路线之\ \textbf{上界侧}（}\S0(3)\ ✓\big)\ \text{即一类\ \textbf{新资产}（L{\to}p 机制 ✓）};\ \text{其\ \textbf{下界侧}仍缺 ✗ ⟹ 复活条件\textbf{尚未满足} ✓（但与"整体无攻击点"不同 ✓）}$$

## §3 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ 119\cdot11=1309,\ E=285✓;\ Q_{10}=E\sqcup O\ (512/512)✓;\ a+b=119✓;\ E\subseteq C_E\cup N(C_O)\ \text{与}\ O\subseteq C_O\cup N(C_E)✓;\ 10b\ge393+b\Rightarrow b\ge44✓$$
$$\textbf{✓✓}:\ L_E{=}10a-|N(C_E)|✓;\ L_E\le9a-393✓;\ (9a{-}393){+}(9b{-}393)=285✓;\ \sum_y k_y=10a✓;\ \sum_y\binom{k_y}2=2p_E✓;\ \binom k2\le5(k-1)✓;\ p_E\le\frac52L_E✓$$
$$\textbf{✓}:\ \sum_x\binom{m_x}2=2(n_1{+}n_2)✓\ \text{（距离-1 与距离-2 对共享闭球 2 点 ✓，其余 0 ✓）};\ \ge285\ \text{（凸性 ✓）}\Rightarrow n_1{+}n_2\ge143✓;\ e_i\le57\Rightarrow|E(C)|\le570✓$$
$$\textbf{✗✗}:\ \text{"}\frac12Q_{10}\ \text{之最小特征值 }=-3\text{"}\ ✗\ \big(\text{实为 }-5✓\big);\ \text{"}p(44)\ge25\text{"}\ ✗;\ \text{"}p(45)\ge28\text{"}\ ✗;\ \text{"}a{=}44\ \text{不可能"}\ ✗;\ \text{"}28\le p_E\le30\text{"}\ ✗$$
$$\textbf{⚠️}:\ \text{"halved }Q_{10}\ \text{是 45-regular"}\ ✓✓;\ \text{谱下界之\ \textbf{形式}\ ✓（Hoffman 型 ✓）唯参数错 ✗}$$
$$\textbf{✓}:\ \text{private-neighbor 与逐坐标投影之\ \textbf{方向}\ ✓✓（皆不经过 }q✓\big);\ \text{唯目前读数松散（}n_1{+}n_2\ge143\ \text{vs}\le570 ✓）$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "谱下界失效" "最小特征值更正" "奇偶路线"
技术词 谱下界失效     命中文件数=0    ::
技术词 最小特征值更正 命中文件数=0    ::
技术词 奇偶路线       命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 谱下界失效 | 0 | 0 | ✓（自造标签 ✓） |
| 最小特征值更正 | 0 | 0 | ✓（自造标签 ✓） |
| 奇偶路线 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §5 边界（硬 ✓）

- **有限穷举＋谱计算** ✓（512×512 之 ½Q_10 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处必改**（$\lambda_{\min}{=}-5$ ✗✓）＋ **一处确认为新对象**（奇偶路线 ✓）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a{=}44/45$ 已排除 ✗（V290）；**不声称** 奇偶路线已死 ✗（仅记其下界工具缺 ✓）
