# WITSAT2-2026-09-28 — **饱和只在 $t{=}12$**（$9a$／$9|A|$ 第 2 次滑落）＋ $\#\{d_U{=}0\}\ge33$（全 $t$ 成立 ✓✓）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 11:04 令 ✓）**：Case I 由 C-444 正确约定重推到底；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-445／C-444／C-443，非新案 ✓）**
`docs/WITSH-2026-09-28-…`（**singleton-$H$ 分离引理 ✓✓**）｜`docs/WITCAR-2026-09-28-…`（**载体 $V\setminus X_L=U\cup N(H)$ ✓✓**）｜`docs/WITRMAX-2026-09-28-…`（**$t$-参数化 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §4）
D0: 本档对象 ＝ **档案已有** Case I／$X_L$／$U^c$ 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次判定"饱和 $X_L=U^c$"恰在 $t{=}12$ 成立（附等号条件 $9t{=}108$）＋ 首证 $\#\{a:d_U(a){=}0\}\ge|A|-t=33$ 对全部 $t$ 成立 ＋ $t{=}12$ 容量封顶 $D_2\le19$** ✓）
**[RESEARCH]**

---

## §0 结论（**$\#\{d_U{=}0\}\ge33$ ✓✓ 全 $t$｜饱和仅 $t{=}12$ ✓✗｜无杀 ✗**）

$$\textbf{设定 ✓}:\ a=45,\ s=107+t,\ 8\le t\le12,\ |A|=33+t,\ |H|=12-t,\ |U^c|=512-s=405-t,\ |X_L|\ge8s-559=297+8t✓$$
$$\qquad\text{正确约定 ✓}:\ X_L=U^c\setminus N(H)\Longrightarrow V\setminus X_L=U\cup N(H)✓✓;\quad T_A=0\Longrightarrow r_A(x)=1\ \forall x\in X_L✓$$
$$\qquad S_A:=\sum_{y\in V\setminus X_L}r_A(y)=|E(A,V\setminus X_L)|=2e(A)+\mathrm{leak}✓;\quad \boxed{9|A|=|X_L|+S_A}✓✓$$
$$\boxed{\textbf{(1) ✗✗}:\ \text{唐先生 §1 的}\ \mathbf{405=|X_L|+S_A}\ \textbf{不对}\ ✗\ \big(\text{＝}9a\ \text{与}\ 9|A|\ \text{之滑落，}\textbf{第 2 次}✗\big)}$$
$$\qquad\textbf{正确 ✓✓}:\ 9|A|=9(33+t)=297+9t✓ \Longrightarrow \boxed{S_A=297+9t-|X_L|\ \le\ (297+9t)-(297+8t)=t}✓✓$$
$$\qquad\Longrightarrow\ \text{§1–§2 在 }t\le11\ \text{时\ \textbf{未给出任何新信息}}\ ✗\ \big(\text{即 C-444 的 }S_A\le t✓\ \text{之重述}\big);\ \text{且 }405=9a\ \text{仅 }t{=}12\ \text{时成立 ✓}$$
$$\boxed{\textbf{(2) ✓✓但饱和结论\ \textbf{恰在 }$t{=}12$\ \textbf{成立}}（本档判定 ✓✓）:\ |X_L|\le|U^c|=405-t✓\ \text{与 }|X_L|\ge297+8t✓\ \text{同取等}}$$
$$\qquad\iff 297+8t=405-t\iff 9t=108\iff \boxed{t=12}✓✓\ \big(t\le11:\ \text{区间非退化（如 }t{=}11{:}\ [385,394]✓\big)\ ✗\big)$$
$$\qquad\Longrightarrow\ \textbf{仅 }t{=}12:\ \boxed{|X_L|=|U^c|=393}\ \big(\text{故 }X_L=U^c✓\big),\quad \boxed{S_A=t=12}\ \big(\text{预算饱和 ✓✓}\big),\quad N(H)=\varnothing\subseteq U✓\ \big(\text{空真 ✓}\big)$$
$$\boxed{\textbf{(3) ★★新结果：}\#\{a\in A:d_U(a)=0\}\ \ge\ |A|-t\ =\ \mathbf{33}\quad\text{（对全部 }t\in[8,12]\ \text{成立 ✓✓）}}$$
$$\qquad\textbf{证明 ✓✓}:\ \sum_{a\in A}d_U(a)=\sum_{y\in U}r_A(y)\le S_A\le t✓ \Longrightarrow \#\{a:d_U(a)\ge1\}\le t✓ \Longrightarrow \#\{a:d_U(a)=0\}\ge|A|-t=33✓✓$$
$$\boxed{\textbf{(4) ✓}$t{=}12$\ \textbf{格：唐先生 §6–§9、§12 全部成立}（本档逐条核 ✓✓）}$$
$$\qquad\text{① }r_A\equiv1\ \text{on }U^c\ \Longrightarrow\ N(a)\cap N(a')=\varnothing\ \big(a\ne a'\in A✓\big)✓;\quad \text{② }2D_2=\sum_{y\in U}\binom{r_A(y)}2✓,\ \sum_{y\in U}r_A(y)=12✓✓$$
$$\qquad\text{③ 容量封顶极大 ✓}:\ t=9q+r\Rightarrow2D_2\le36q+\binom r2✓;\ t{=}12\Rightarrow q{=}1,r{=}3\Rightarrow2D_2\le39\Rightarrow\boxed{D_2\le19}✓$$
$$\qquad\text{④ }\boxed{2e(A)+e(A,B)=12}✓✓\ \big(U=A\sqcup B✓\big);\quad \text{⑤ }\ge33\ \text{个 }A\text{-点之\ \textbf{完整球}\ }B_1(a)\subseteq U^c\ \text{且两两不交 ✓}✓$$
$$\qquad\qquad\Longrightarrow\ \Big|\bigcup_{a\in A_0}B_1(a)\Big|=10\cdot33=330\ \le\ |U^c|=393✓\ \big(\text{slack }63✓\big)\ \Longrightarrow\ \textbf{无矛盾}✗$$
$$\boxed{\beta\ \le\ \lfloor t/2\rfloor+\tfrac12\binom t2}✓\quad\big(\text{而 }\beta\ge t-7✓,\ 2e+\mathrm{leak}=t\Rightarrow e\le\lfloor t/2\rfloor✓\big)$$
$$\qquad t{=}12:\ \beta\le6+19=25\gg5✓;\quad t{=}8{:}\ \beta\le4+14=18\gg1✓ \Longrightarrow\ \textbf{全部 }t\ \text{仍可行}✗✓\ \big(\text{与 C-444 ✓ 一致}\big)$$

---

## §1 记号对照（**防第 3 次滑落 ✓✓**）

| 量 | $t=8$ | 9 | 10 | 11 | 12 |
|---|---|---|---|---|---|
| $9|A|$ | 369 | 378 | 387 | 396 | **405** |
| $9a$（$a{=}45$） | 405 | 405 | 405 | 405 | 405 |
| $\|U^c\|=405-t$ | 397 | 396 | 395 | 394 | 393 |
| $\|X_L\|\ge297+8t$ | 361 | 369 | 377 | 385 | **393** |
| $S_A$ 上界 $=t$ | 8 | 9 | 10 | 11 | 12 |
| $\|X_L\|=\|U^c\|$？ | ✗ | ✗ | ✗ | ✗ | **✓** |

$$\Longrightarrow\ \textbf{规则（登记 ✓✓）}:\ a=45\ \text{时一律写作}\ 9|A|=297+9t✓;\ \boxed{405=9a\ \text{仅 }t{=}12\ \text{时与 }9|A|\ \text{重合}}✓$$

## §2 逐条核验（**✓／✗**）

$$\textbf{§1 ✗（405）};\ \textbf{§2 ✗（饱和仅 }t{=}12\text{）};\ \textbf{§3 ✓（重述）};\ \textbf{§4–§5 ✓✓（在 }t{=}12\text{）};\ \textbf{§6 ✓（且 }(11)\ \text{对全 }t✓\big)$$
$$\textbf{§7 ✓（}t{=}12\text{）}:\ 2D_2=\sum_{y\in U}\binom{r_y}2✓;\ \text{一般 }t\ \text{时载体仍为 }U\cup N(H)✗\ \big(\text{C-444 ✓、C-445 ✗}\big)$$
$$\textbf{§8–§9 ✓}:\ \text{等号条件（集中于一点）与容量封顶 }36q+\binom r2✓✓\ \text{（本档复核正确 ✓）};\ \text{§9 末"耦合优化"之提法 ✓（正解 ✓）}$$
$$\textbf{§10–§11 ✓}:\ \beta\ge t-7✓;\ \text{但 §11 之表须带"}\le\lfloor t/2\rfloor+\tfrac12\binom t2\text{"上界旗标 ✓}$$
$$\textbf{§12 ✓✓}:\ t{=}12\ \text{之 }2e+e(A,B)=12✓\ \text{与 }D_2\le19✓\ \text{均正确 ✓}$$
$$\textbf{§13 ✓（形式 ✓）}:\ \text{"去 }H\ \text{噪声"之干净命题在 }t{=}12\ \text{成立 ✓✓（因 }H{=}\varnothing✓\big);\ \text{一般 }t\ \text{仍含 }N(H)\ \text{噪声 ✗}$$

## §3 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }297+9t\ \text{恒等式与 }S_A\le t✓;\ \text{② 饱和恰在 }t{=}12✓✓;\ \text{③ }\#\{d_U{=}0\}\ge33\ \text{对全 }t✓✓;\ \text{④ }t{=}12\ \text{之 }D_2\le19\ \text{与 }2e+e(A,B)=12✓✓;\ \text{⑤ }\ge33\ \text{完整球 packing（}330\le393✓\big)✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}405=|X_L|+S_A\text{"（全 }t\text{）};\ \text{"饱和对全 }t\text{"};\ \text{"}t{=}12\ \text{直接不可能"（第三次 ✗）}$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ |H|{=}1\ \text{时 }D_2{=}0\ \text{（C-445 缺口 ✓）};\ \text{一般 }t\ \text{的饱和替代（}t\le11\ \text{时 }|X_L|\ \text{区间非退化 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① }\mathbf{33\ \text{完整球 packing}}＋\le t\ \text{污染点共存（唐先生 §13–§14 ✓）};\ \text{② }t{=}12\ \text{之干净命题（去 }H\text{）：}|A|=45,\ \text{外部每点恰一 }A\text{邻},\ A\text{-外部入射}=12\Rightarrow|A|\le40\ ?✓$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "饱和恒等式" "缺陷码问题" "完整球packing"
技术词 饱和恒等式    命中文件数=0    ::
技术词 缺陷码问题    命中文件数=0    ::
技术词 完整球packing 命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 饱和恒等式 | 0 | 0 | 0（本档自造标签 ✓） |
| 缺陷码问题 | 0 | 0 | 0（本档自造标签 ✓） |
| 完整球packing | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（自造标签仅作结构命名，不作新性主张 ✓）

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处必改**（§1 之 405 ⟹ 饱和仅 $t{=}12$）已在 §0(1)(2) 显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** $t{=}12$ 已被关闭 ✗（V290）
