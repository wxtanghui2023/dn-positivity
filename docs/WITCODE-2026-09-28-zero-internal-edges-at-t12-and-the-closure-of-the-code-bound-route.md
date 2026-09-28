# WITCODE-2026-09-28 — **$t{=}12$：$e(A)=0$ 成立（新 ✓✓）但码上界路线已封闭（$D_2\ge5$ 被强制）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 11:20 令 ✓）**：$t{=}12$ 极限构型与码上界路线；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-447／C-446／C-445，非新案 ✓）**
`docs/WITA0-2026-09-28-…`（**$d(A_0)\ge3$／wedge 闭包 ✓✓**）｜`docs/WITSAT2-2026-09-28-…`（**饱和仅 $t{=}12$／$\#\{d_U{=}0\}\ge33$ ✓✓**）｜`docs/WITB45-2026-09-28-…`（**$A(9,3)=40$ 取证 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §4）
D0: 本档对象 ＝ **档案已有** $t{=}12$／$A_0,A_1,P,W$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首证 $t{=}12\Rightarrow e(A)=0$（对全部 $q{=}|A_1|$ 成立）＋ $N(P)\cap A_0=\varnothing$ ＋ $U^c$ 精确二分割 ＋ 判死 $A(9,3)$ 路线（$D_2\ge5$ 被强制）＋ $D_2\le18$ 锐化** ✓）
**[RESEARCH]**

---

## §0 结论（**$e(A){=}0$ ✓✓（新）｜码路线 ✗✗判死｜$D_2\in[5,18]$ ✓**）

$$\textbf{设定 ✓}:\ t=12\Rightarrow s=119,\ |A|=45,\ |U|=119,\ |U^c|=393✓;\ r_A|_{U^c}\equiv1✓;\ \sum_{y\in U}r_A(y)=12✓;\ H=\varnothing✓$$
$$\qquad A_0:=\{a:d_U(a)=0\}✓,\ A_1:=A\setminus A_0✓,\ q:=|A_1|\le12✓,\ \boxed{\sum_{a\in A_1}d_U(a)=12}✓✓\ \big(\text{C-447 ✓}\big)$$
$$\boxed{\textbf{(1) ✓✓新结果：}t{=}12\Longrightarrow\boxed{e(A)=0}\quad\textbf{（对全部 }q\in[0,12]\ \text{成立 ✓✓）}}$$
$$\qquad\textbf{链条 ✓✓}:\ \text{① }d(A_0)\ge3\Rightarrow e(A_0)=0✓\ \big(\text{C-447 ✓}\big);\ \text{② }d(A_0,A_1)\ge3✓\ \big(\text{见 §1 —— 本档给出更简洁证明 ✓}\big)$$
$$\qquad\text{③ }\boxed{U^c=N(A_0)\ \dot\cup\ \big(N(A_1)\cap U^c\big)}✓✓\ \big(\text{因 }r_A|_{U^c}\equiv1\Rightarrow U^c\subseteq N(A)✓,\ \text{且 }N(A_0)\cap N(A_1)=\varnothing✓\big)$$
$$\qquad\text{④ 集合大小 ✓}:\ \Big|N(A_1)\cap U^c\Big|=|U^c|-9|A_0|=393-9(45-q)=\boxed{9q-12}✓✓$$
$$\qquad\text{⑤ 入射计数 ✓}:\ E(A_1,U^c)=E(A_1,A_1^c)-E(A_1,U)=\big(9q-2e(A_1)\big)-12=9q-12-2e(A_1)✓$$
$$\qquad\text{⑥ 比较 ④⑤ ✓✓}:\ \text{每点 }\ge1\ \text{入射}\Rightarrow E\ge\text{集合大小}\Rightarrow 9q-12-2e(A_1)\ge9q-12\Rightarrow\boxed{e(A_1)=0}✓✓$$
$$\qquad\Longrightarrow\ \text{由 ①②③}: e(A)=e(A_0)+e(A_1)+E(A_0,A_1)=0+0+0=\mathbf 0✓✓;\quad \text{且每点 }x\in N(A_1)\cap U^c\ \text{恰一个 }A_1\text{-邻 ✓}$$
$$\boxed{\textbf{(2) ✓✓配套新结果}:\ \text{①}\ \boxed{N(P)\cap A_0=\varnothing}\ ✓✓\ \big(P:=N(A_1)\cap U✓;\ p\sim a_0\ \text{与}\ p\sim a_1\Rightarrow d(a_0,a_1)\le2\ \text{违 ②}✗\big)}$$
$$\qquad\text{②}\ \boxed{\mathrm{leak}=|E(A,B)|=t=12}✓✓\ \big(2e(A)+\mathrm{leak}=t✓\ \text{而 }e(A)=0✓\big);\quad \text{③}\ A_1\subseteq R:=Q_9\setminus(A_0\cup N(A_0)),\ |R|=512-330=\mathbf{182}✓✓$$
$$\boxed{\textbf{(3) ✗✗但最后一步不成立（本档判死该路线）}:\ \text{"}e(A)=0\Longrightarrow d(A)\ge3\Longrightarrow45\le A(9,3)=40\Longrightarrow\bot\text{"}\ \textbf{无效}\ ✗✗}$$
$$\qquad\textbf{病根 ✓✓}:\ e(A)=0\ \text{只排除\ \textbf{距离-1}}\ 对 ✗；\ A_1\ \text{内部的距离-2 对\ \textbf{未被排除}}✓;\ \text{而}\ \beta=e+D_2=D_2\ \ge\ t-7=5✓✓$$
$$\qquad\Longrightarrow\ \boxed{D_2(A)\ \ge\ 5\ >\ 0\ \text{被强制}}✓✓\ \Longrightarrow\ \boxed{A\ \textbf{可证不是}最小距离\ge3}\ ✗✓\ \big(\text{即 }A(9,3)\ \text{路线\textbf{封闭}}\ ✗✓\big)$$
$$\boxed{\textbf{(4) ✓锐化后的 }D_2\ \textbf{窗口（新）}:\ }\text{所有 }A\ \text{的距离-2 对之两共同邻点皆 }\in P✓\ \big(\notin X_L=U^c✓,\ \notin A\ \text{因 }e(A){=}0✓,\ \notin W\ \text{因 }W\cap N(A){=}\varnothing✓\big)$$
$$\qquad2D_2=\sum_{p\in P}\binom{r_A(p)}2✓;\quad \sum_{p\in P}r_A(p)=12✓;\quad r_A(p)\le9✓;\quad |P|\le12✓ \Longrightarrow \boxed{D_2\le18}✓✓\ \big(\text{锐于 C-446 的 }19✓\big)$$
$$\qquad\Longrightarrow\ \boxed{D_2\in[5,\ 18]}✓\ \big(\text{全部整数值可达 ✓；}\text{杀 }t{=}12\ \text{只需}\ D_2\le4\ ✗\big)$$

---

## §1 $d(A_0,A_1)\ge3$ 的简洁证明（**✓✓**）

$$\textbf{设}\ a\in A_0,\ b\in A_1✓.\ d(a,b)=1\Longrightarrow b\in N(a)\subseteq U^c\ \text{而}\ b\in A\subseteq U\ ✗\ \text{矛盾}✓$$
$$\qquad d(a,b)=2\Longrightarrow\ \text{共同邻点 }y\ \text{满足}\ r_A(y)\ge2\Longrightarrow y\notin X_L=U^c\Longrightarrow y\in U✓;\ \textbf{但}\ y\sim a\ \text{且}\ a\in A_0\Longrightarrow y\in N(a)\subseteq U^c\ ✗\ \text{矛盾}✓✓$$
$$\qquad\Longrightarrow\ \boxed{d(A_0,A_1)\ge3}✓✓\ \big(\text{本证明不需"}|A_1|=12\text{"也不需 }d(A_1)\ge3✓;\ \text{唐先生 §2 之证明依赖 }d_U(b)=1✓\ \text{仅在极端情形成立 ✓}\big)$$

## §2 逐条核验（**✓／✗**）

$$\textbf{§1（球计数入口）✗✗}:\ \text{"}A\ \text{最小距离}\ge3\text{／球不交／}450\text{"}\ ✗\ \big(\text{C-447 §0(1) 已否证 ✓}\big)$$
$$\textbf{§2 ✓✓}:\ \#\{d_U>0\}\le12\ \text{与}\ |A_0|\ge33\ ✓✓;\quad \textbf{§3 ✗}:\ \text{"}|P|=12\text{"}\ ✗\ \big(\text{仅}\le12✓;\ \text{"全部 }A_1\text{-邻点落 }P\text{"需 }d_U\equiv1✓\ \text{仅极端情形 ✓}\big)$$
$$\textbf{§4–§5 ✓（形式 ✓）}:\ A_0,A_1,P,W\ \text{四块结构与 }W\cap N(A)=\varnothing✓✓;\ \text{"}|W|=62\text{"}\ \text{须改}\ \ge62✓\ \big(\text{C-447 ✓}\big)$$
$$\textbf{§6–§7 ✓✓}:\ U^c=N(A_0)\dot\cup(N(A_1)\cap U^c)✓✓\ \text{与 }E(P,A_0)=0✓✓\ \text{均正确 ✓};\ \text{"}9|P|=108\text{ 条边分解"}\ ✓$$
$$\textbf{§8–§9 ✓✓（关键 ✓）}:\ E(A_1,U^c)=9q-12-2e(A_1)\ \text{与集合大小 }9q-12③\ \text{比较}\Rightarrow e(A_1)=0✓✓\ \text{—— 且**对全部 }q\ \text{成立}✓✓$$
$$\textbf{§10–§11 ✗✗}:\ \text{"}e(A)=0\Rightarrow d(A)\ge3\Rightarrow\bot\text{"}\ ✗\ \big(\text{见 §0(3) ✓}\big)$$
$$\textbf{§12 ✓（结构 ✓）}:\ A_1\ \text{内距离-2 对之两共同邻点皆 }\in P✓\ \big(\text{唐先生写"另一个必在 }U^c\text{"}\ ✗\ \text{—— 在 }t{=}12\ \text{时 }X_L{=}U^c\ \text{已饱和 ✓}\big)$$

## §3 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{e(A)=0}\ \big(t{=}12✓✓\big);\ \text{② }N(P)\cap A_0=\varnothing✓✓;\ \text{③ }U^c\ \text{精确二分割（}297+96✓\big)✓✓;\ \text{④ }\mathrm{leak}=|E(A,B)|=12✓✓;\ \text{⑤ }A_1\subseteq R\ (|R|=182✓)✓;\ \text{⑥ }D_2\in[5,18]✓;\ \text{⑦ }D_2\ \text{见证全在 }P✓✓$$
$$\textbf{已判死 ✗✓}:\ \boxed{\text{"}e(A)=0\Rightarrow A(9,3)\ \text{矛盾}\text{"}\ \text{路线封闭}\ ✗✓}\ \big(D_2\ge5\ \text{被强制 ✓}\big);\ \text{"球不交／}450\text{"（第二次 ✗）};\ \text{"}|P|=12\text{"}✗$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ t{=}12\ \text{的关闭};\ D_2\le4\ \text{（杀 }t{=}12\ \text{所需 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 证 }D_2\le4\ \big(\text{即 }2D_2=\sum_P\binom{r_p}2\le8\ \text{不可能在 }r\le9,\ \sum r=12,\ |P|\le12\ \text{下发生 ✓}\big)\ \text{—— 等价于排除"六个 }r{=}2\ \text{的 }P\text{-点"最小缺陷构型 ✓};\ \text{② }A_1\ (q\le12)\subseteq R\ (182)\ \text{的局部分类 ✓};\ \text{③ 用 }N(P)\cap A_0=\varnothing\ \text{做二部禁邻计数 ✓}$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "码上界路线" "内部边零" "分区切割"
技术词 码上界路线 命中文件数=0    ::
技术词 内部边零   命中文件数=0    ::
技术词 分区切割   命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 码上界路线 | 0 | 0 | 0（本档自造标签 ✓） |
| 内部边零 | 0 | 0 | 0（本档自造标签 ✓） |
| 分区切割 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（自造标签仅作结构命名，不作新性主张 ✓）

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处判死**（$A(9,3)$ 路线封闭）已在 §0(3) 显式标注 ✓✓；$e(A)=0$ 与 $D_2\ge5$ **必须同时引用** ✓✓（否则误得矛盾 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** $t{=}12$ 已关闭 ✗（V290）
