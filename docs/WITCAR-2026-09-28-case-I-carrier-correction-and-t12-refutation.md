# WITCAR-2026-09-28 — **Case I 的载体修正**：见证区 ＝ $U\cup N(H)$（非 $N(H)$）＋ $t{=}12$ 之杀不成立 ＋ 集中化可修好

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 11:00 令 ✓）**：把 $T_A=0$（Case I）推到底；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-443／C-442／C-438，非新案 ✓）**
`docs/WITRMAX-2026-09-28-…`（**$t$-参数化／三分类／Case I 硬核 ✓✓**）｜`docs/WITB45-2026-09-28-…`（**$\beta$ 判据／$A(9,3)=40$ ✓✓**）｜`docs/ERRATUM-2026-09-28-WITSAT-…`（**$X_L$ 约定（第 3 次同型陷阱 ✓✓）**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** Case I／$X_L$ 载体对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 Case I 的载体恒等式修正（$V\setminus X_L=U\cup N(H)$）＋ 否证"$t{=}12$ 直接不可能"＋ 集中化之正确形式（$2e+\mathrm{leak}\le t\Rightarrow D_2\le\binom t2/2$）＋ Case I 计数层全存活之判定** ✓）
**[RESEARCH]**

---

## §0 结论（**§1–§2 ✓｜两处 ✗｜集中化可修好 ✓✓｜Case I 计数层全存活 ✗✓**）

$$\textbf{设定 ✓}:\ a=45,\ t=s-107\in[8,12],\ |A|=33+t,\ |H|=119-s=12-t\le4✓;\ T_A=0\ \ (\text{Case I}✓)\Longrightarrow r_A(x)=1\ \forall x\in X_L✓$$
$$\boxed{\textbf{(1) ✓§1–§2 成立（附一处记号 ✓）}:\ |E(A,X_L)|=|X_L|✓;\quad 9|A|=2e(A)+|E(A,H)|+|X_L|+|E(A,R)|✓}$$
$$\qquad\textbf{（记号 ✓）}:\ \text{唐先生 §1 写 }9a\ \text{应为}\ \boxed{9|A|}\ ✓\ \big(\text{仅 }t{=}12\ \text{时 }a=|A|=45\ \text{重合 ✓；一般 }|A|=33+t<45✗\big)\ \text{—— 但结论不变 ✓✓}$$
$$\qquad\Longrightarrow 2e(A)+\mathrm{leak}=9|A|-|X_L|\le9(33+t)-(297+8t)=t\Longrightarrow \boxed{e(A)\le t/2}✓✓\ \big(\mathrm{leak}:=|E(A,H)|+|E(A,R)|✓\big)$$
$$\qquad\text{且}\ \beta=e(A)+\tfrac12\sum_{y\in V\setminus X_L}\binom{r_A(y)}2✓✓\ \big(\text{§2 ✓ 写法与 C-443 §0(1)③ 一致 ✓}\big)$$
$$\boxed{\textbf{(2) ✗必改一（载体错位）}:\ \text{唐先生 §3 的}\ V\setminus X_L=N(H)\ \textbf{不对}\ ✗\ \big(\text{系把 }X_L\ \text{误作 }V\setminus N(H)✓\big)}$$
$$\qquad\textbf{正确 ✓✓}:\ X_L:=U^c\setminus N(H)\Longrightarrow \boxed{V\setminus X_L\ =\ U\ \cup\ N(H)}\ ✓✓\ \big(\text{因 }X_L\subseteq U^c✓\big)$$
$$\qquad\Longrightarrow\ \text{坏对见证可落在\ \textbf{整个 }U\ (\text{含 }A,H,\text{以及 }B\ \text{——至多 }75\ \text{点})}✗;\ \text{故 §4 的 }2D_2=\sum_{N(H)}\binom{r_y}2\ ✗、\text{§5 的"由至多 4 个 }H\text{-球承载"}\ ✗$$
$$\qquad\Longrightarrow\ \text{正确形式 ✓}:\ 2D_2(A)=\sum_{y\in U\cup N(H)}\binom{r_A(y)}2✓✓\ \big(\text{＝C-443 的 }\sum_{V\setminus X_L}✓\big)$$
$$\boxed{\textbf{(3) ✗✗必改二（结论级）}:\ "\,(a,s)=(45,119),\ t{=}12:\ \text{直接不可能}\,"\ \textbf{不成立}\ ✗✗}$$
$$\qquad\textbf{病根 ✓}:\ H=\varnothing\ \text{时}\ X_L=U^c\ \textbf{而非}\ V\ ✗\ \big(\text{唐先生 §10 写"此时 }X_L=V"\ ✗\big);\ \text{故 }T_A=0\ \text{只要求\ \textbf{每个 }x\in U^c\ \text{恰一个 }A\text{-邻}}✗$$
$$\qquad\textbf{实际核对 ✓✓}:\ t{=}12:\ |A|{=}45,\ |U|{=}119,\ |X_L|{=}512-119=\mathbf{393}\le9|A|=\mathbf{405}✓ \Longrightarrow \textbf{可满足（无矛盾）}✗✓$$
$$\qquad\text{且恒等式给}\ 2e(A)+|E(A,R)|=405-393=12=t✓ \Longrightarrow \textbf{与预算 }2e+\mathrm{leak}\le t\ \text{完全相容}✓✓\ \big(\text{即 }t{=}12\ \text{的 Case I \textbf{未被关闭}}✗\big)$$
$$\boxed{\textbf{(4) ★★集中化直觉\ \textbf{可修好}（新 ✓✓）}:\ \text{载体虽\ \textbf{大}（}U\cup N(H)\ \text{可至 119 点 ✓），但其\ \textbf{A-入射预算极小}✓✓:}}$$
$$\qquad\boxed{\sum_{y\in V\setminus X_L}r_A(y)\ =\ 2e(A)+\mathrm{leak}\ \le\ t\ \le\ 12}\ ✓✓\ \big(\text{Case I；由 (1) ✓}\big)\ \Longrightarrow\ \boxed{D_2(A)\ \le\ \tfrac12\binom t2}✓✓$$
$$\qquad\Longrightarrow\ \beta=e(A)+D_2\le\tfrac t2+\tfrac12\binom t2✓;\quad \text{逐位}:\ t{=}8\Rightarrow\beta\le18;\ t{=}10\Rightarrow27;\ t{=}12\Rightarrow39\ \text{—— 而需要仅}\ \beta\ge t-7\le5✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{Case I 的计数层对全部 }t\in[8,12]\ \textbf{存活}}\ ✗✓\ \big(\beta\ \text{上界远大于所需下界 ✓}\big)$$

---

## §1 核验与修正逐条（**✓／✗**）

$$\textbf{§1 度预算 ✓（记号已改）}:\ 9|A|=2e+\underbrace{|E(A,X_L)|}_{=|X_L|✓}+\mathrm{leak}\Longrightarrow e\le\frac{9|A|-|X_L|}2\le\frac t2✓✓$$
$$\textbf{§2 }\beta\ \text{式 ✓}:\ \beta=e(A)+\tfrac12\sum_{V\setminus X_L}\binom{r_A}2✓✓\ \big(\text{此处唐先生写对了 ✓}\big)$$
$$\textbf{§3 ✗}:\ V\setminus X_L=N(H)\ ✗ \Longrightarrow \textbf{正确}\ V\setminus X_L=U\cup N(H)✓✓$$
$$\textbf{§4 ✗}:\ 2D_2=\sum_{N(H)}\binom{r_y}2\ ✗ \Longrightarrow \textbf{正确}\ 2D_2=\sum_{U\cup N(H)}\binom{r_y}2✓✓$$
$$\textbf{§5 ✗}:\ "41\text{--}45\ \text{个 }A\text{-点的坏对全部由至多 4 个 }H\text{-球承载}"\ ✗ \Longrightarrow \textbf{正确}\ \text{: 由 }U\cup N(H)\ \text{承载，且其大而不重（入射}\le t✓✓\big)$$
$$\textbf{§8 ✗}:\ D_2\le\tfrac12\sum_{y\in M}\binom{r_y}2\ \big(M=N(H)\big)\ ✗ \Longrightarrow \textbf{正确}\ M:=U\cup N(H)✓✓\ \big(\text{此时为等号 ✓}\big)$$
$$\textbf{§10 ✗✗}:\ t{=}12\ \text{直接不可能}\ ✗✓\ \big(\text{见 §0(3)：}393\le405✓\ \text{可满足}\big)$$
$$\textbf{§11 ✓（方向）}:\ \text{"}H\ \text{小 ⟹ 结构受限"}\ \text{方向对 ✓，但受限的\ \textbf{不是载体大小}、而是\ \textbf{入射预算}\ }2e+\mathrm{leak}\le t✓✓$$

## §2 第 4 次同型陷阱（**制度 ✓✓**）

$$\textbf{（第 4 次 ✓）}:\ X_L\ \text{的约定再次被误用}✗:\ \text{本线 }X_L:=U^c\cap\{x:N(x)\cap H=\varnothing\}\ ✓\ \big(\text{闭邻域／}N[H]\ ✓\big)$$
$$\qquad\ne\ V\setminus N(H)\ \big(\text{开邻域版，会把 }H\ \text{与 }N(H)\ \text{混入}\big)✗\ \text{—— 首次 }C\text{-}437\ \text{§0(3)}✓\ \text{、二次 }C\text{-}438\ \text{§1}✓\ \text{、三次 }C\text{-}441\ \text{§0(1)}✓\ \text{、本档第四次}✗$$
$$\qquad\Longrightarrow\ \textbf{（规则强化 ✓✓）}:\ \text{凡涉及 }X_L/V\setminus X_L\ \text{的等式，}\textbf{一律先写出 }V\setminus X_L=U\cup N(H)\ \text{再继续}\ ✓✓$$

## §3 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① §1 度预算 }e\le t/2✓;\ \text{② §2 }\beta\ \text{式}✓;\ \text{③ 载体恒等式 }V\setminus X_L=U\cup N(H)✓✓;\ \text{④ 载体入射预算 }2e+\mathrm{leak}\le t✓✓;\ \text{⑤ }D_2\le\tfrac12\binom t2✓✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}V\setminus X_L=N(H)\text{"};\ \text{"}2D_2\ \text{只在 }N(H)\text{"};\ \text{"由 }\le4\ \text{个 }H\text{-球承载"};\ \boxed{\text{"}t{=}12\ \text{直接不可能}\text{"}}\ ✗✓$$
$$\textbf{未确立 ⚠️}:\ a=45\ \text{的排除};\ \text{Case I 的结构性排除};\ \text{（计数层已证明对全部 }t\ \text{存活 ✗ ⟹ 必须结构论证 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 在\ \textbf{载体入射预算 }\le t\ \text{约束下}，求 }A\ \text{（}|A|=33+t,\ \text{含 }\beta\ \text{个坏对）的可行性（＝带预算的码问题 ✓）；\ \text{② 或直接攻 }A(9,3)=40\ \text{的\ \textbf{带缺陷版}：}|A|=41+t'\ \text{且允许 }\beta\ \text{个坏对时是否可行（＝正则化 }\beta\ \text{的延拓 ✓）}}$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "承载区" "载体预算" "见证区"
技术词 承载区    命中文件数=0    ::
技术词 载体预算  命中文件数=0    ::
技术词 见证区    命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 承载区 | 0 | 0 | 0（本档自造标签 ✓） |
| 载体预算 | 0 | 0 | 0（本档自造标签 ✓） |
| 见证区 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 逐条核验 ＋ §0(2)(3)(4) 三结论 ＋ §2 制度**（推导性 ✓）

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **两处必改**（载体错位 ＋ $t{=}12$ 之杀无效）已在 §0(2)(3) 显式标注 ✓✓（防误用 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）
- **不声称** $a=45$ 已排除 ✗；**不声称** Case I 不可行 ✗；不声称 P1 成立 ✗（V290）
