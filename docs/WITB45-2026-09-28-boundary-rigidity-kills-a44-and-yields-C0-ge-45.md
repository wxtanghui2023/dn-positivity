# WITB45-2026-09-28 — **边界刚性 ⟹ $|C_0|\ge45$**（$a=44$ 全灭）＋ 迭代判据

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:49 令 ✓）**：攻 $(44,116)$ 边界 → 一般化；**零程序计算**（仅整数/有限情形核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-441／C-440／C-435，非新案 ✓）**
`docs/WITEFF-2026-09-28-…`（**$L_A\le9a+s-512$／边界刚性 ✓✓**）｜`docs/WITGATE-2026-09-28-…`（**交界点 393/8／$\mathrm{min\_excess}_9$ ✓✓**）｜`docs/WITFIB-2026-09-28-…`（**$a,b\ge44$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §5）
D0: 本档对象 ＝ **档案已有** 边界点／$A$ 码对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $a=44$ 的全灭证明（四情形）⟹ $|C_0|\ge45$（改进 C-435 的 44）＋ 迭代判据（$L_A+\mathrm{leak}\le\Delta_A$、$|A|\le A(9,3)+\beta$、$\max\beta$ 表）＋ 积分性事实 $T_A\ne1$** ✓）
**[RESEARCH]**

---

## §0 结论（**核验通过 ✓✓｜三项新结果 ✓✓｜$|C_0|\ge45$ ✓✓✓**）

$$\text{记号 ✓}:\ a=|C_0|,\ a+b=119✓;\ s=|U|,\ |H|=119-s✓;\ |A|=a+s-119✓;\ X_L:=U^c\setminus N(H)✓;\ r_A(x):=|N(x)\cap A|✓$$
$$\qquad T_A:=\sum_{x\in X_L}(r_A(x)-1)\ge0✓;\quad L_A:=2e(A)+T_A✓;\quad \mathrm{leak}:=|E(A,H)|+|E(A,R)|✓\ \big(R:=V\setminus(A\cup H\cup X_L)✓\big)$$
$$\qquad \Delta_A:=9a+s-512✓;\qquad \beta:=\#\{\text{$A$ 中距离}\le2\ \text{的对}\}=e(A)+D_2(A)✓\ \big(D_2=\text{距离-2 对数}✓\big)$$
$$\boxed{\textbf{(1) ✓核验通过（唐先生 §1–§8 ✓✓）}:\ \text{① 度数恒等式 }9a=\underbrace{2e(A)}_{A\text{-内部}}+|E(A,H)|+\underbrace{|E(A,X_L)|}_{=|X_L|+T_A}+\underbrace{|E(A,R)|}_{\mathrm{leak}}✓✓}$$
$$\qquad\text{② 故}\ 9|A|=L_A+|X_L|+\mathrm{leak}✓✓;\quad \text{③ 由 }|X_L|\ge8s-559\Longrightarrow \boxed{L_A+\mathrm{leak}\ \le\ \Delta_A}✓✓\ \big(\text{＝C-441 之锐化（}+\mathrm{leak}\text{）}\big)$$
$$\qquad\text{④ 边界点 }(a,s)=(44,116):\ \Delta_A=0\Longrightarrow L_A=\mathrm{leak}=0\Longrightarrow e(A)=T_A=0✓\Longrightarrow N(A)=X_L✓,\ |X_L|=369✓,\ |A|=41✓$$
$$\qquad\text{⑤ 再得 }d(a,a')=2\Longrightarrow\text{两共同邻点}\in N(A)=X_L\Longrightarrow r_A\ge2\ \text{与 }T_A=0\ \text{矛盾}\Longrightarrow \boxed{d(A)\ge3}✓✓;\ \text{⑥ }N[A]\ \text{为完美 packing（}|N[A]|=410✓\big)✓✓$$
$$\boxed{\textbf{(2) ★积分性事实（新 ✓✓）}:\ 2D_2(A)=\sum_{y\in V}\binom{r_A(y)}2✓ \Longrightarrow \boxed{T_A\ne1}✓✓\ \big(\text{若 }T_A=1\ \text{则 }2D_2=\binom22=1\ \text{非整数}\ ✗\big)}$$
$$\boxed{\textbf{(3) ★★迭代判据（新 ✓✓）}:\ \text{坏对 }\beta=e(A)+D_2(A)\Longrightarrow \text{移除 }\le\beta\ \text{点即得最小距离}\ge3\Longrightarrow \boxed{|A|\ \le\ A(9,3)+\beta}✓✓}$$
$$\qquad\text{而 }2e+T_A+\mathrm{leak}\le\Delta_A\ \Longrightarrow\ \beta\ \le\ \max_{\substack{2e+T+\ell\le\Delta_A\\ T\ne1}}\Big(e+\big\lfloor\tfrac12\big[\tbinom{T+1}2+\tbinom{\ell}2\big]\big\rfloor\Big)=:\ \mathrm{Bmax}(\Delta_A)✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{排除判据}:\ a+s-119\ >\ A(9,3)+\mathrm{Bmax}(\Delta_A)\ \Longrightarrow\ \text{该 }(a,s)\ \text{不可能}}✓✓$$
$$\boxed{\textbf{(4) ★★★$a=44$ 全灭（新 ✓✓✓，改进 C-435）}:\ \text{四情形逐一（}|C_0|=44✓\big):}$$
| $s$ | $|A|=s-75$ | $9|A|$ | $|X_L|\ge$ | $\Delta_A$ 上限 | $|A|$ 上界 $=40+\mathrm{Bmax}$ | 判定 |
|---|---|---|---|---|---|---|
| 116 | 41 | 369 | 369 | 0 | 40 | $41>40$ ✗ |
| 117 | 42 | 378 | 377 | 1 | 40 | $42>40$ ✗ |
| 118 | 43 | 387 | 385 | 2 | 41 | $43>41$ ✗ |
| 119 | 44 | 396 | 393 | 3 | 43 | $44>43$ ✗ |
$$\qquad\Longrightarrow \textbf{四种情形全部矛盾}✗✗ \Longrightarrow \boxed{|C_0|\ne44}\ \Longrightarrow\ \boxed{\textbf{由 C-435 的 }a\ge44:\quad |C_0|,\ |C_1|\ \ge\ \mathbf{45}}✓✓✓\ \big(\textbf{首次改进 C-435 的 44}\big)$$

---

## §1 核验细节（**✓✓，附干净推导**）

$$\textbf{①（度数恒等式 ✓）}:\ \text{对每个 }a\in A,\ \text{其 9 个邻点按属地分入 }A,\ H,\ X_L,\ R\ ✓\ \big(\text{四类互斥且穷尽 ✓}\big);\ \text{求和即得 ✓}$$
$$\textbf{②（}|E(A,X_L)|=|X_L|+T_A\ ✓\big)：:\ x\in X_L\Longrightarrow r_A(x)\ge1✓\ \big(\text{因 }N(x)\cap C_0\subseteq A\ne\varnothing✓\big) \Longrightarrow \sum_{x\in X_L}r_A(x)=|X_L|+T_A✓$$
$$\textbf{③（$\mathrm{leak}$ 的定义 ✓）}:\ R=V\setminus(A\cup H\cup X_L)=N(H)\setminus(A\cup H)✓\ \big(\text{唐先生 §2 ✓}\big);\ \partial_H(A)=E(A,R)✓$$
$$\textbf{④（$a=44,s=116$ 的刚性 ✓✓）}:\ \Delta_A=0\Longrightarrow L_A=\mathrm{leak}=0\Longrightarrow e(A)=0\wedge T_A=0\wedge|E(A,H)|=|E(A,R)|=0✓$$
$$\qquad\Longrightarrow N(A)\subseteq X_L\ \wedge\ X_L\subseteq N(A)\Longrightarrow \boxed{N(A)=X_L}✓;\quad 9|A|=369=|X_L|✓\ \big(\text{与 }|X_L|\ge369\ \text{夹紧}\ ✓\big)$$
$$\qquad\Longrightarrow A\ \text{是 }(41,\ge3)\ \text{码},\ N[A]\ \text{完美 packing（}|N[A]|=10\cdot41=410✓\big),\ N[A]\cap N[H]=\varnothing✓✓$$
$$\qquad\Longrightarrow \textbf{与 }A(9,3)=40\ \textbf{矛盾}✗\ \big(41>40✓\big)$$

## §1bis ★ $A(9,3)=40$ 的来源核实（**承重事实，必须核 ✓✓**）

$$\textbf{依据 ✓}:\ \text{A.E. Brouwer「Table of general binary codes」}\ \big(\texttt{aeb.win.tue.nl/codes/binary-1.html}\ \text{✓，2026-09-28 抓取 }\text{HTTP 200}\big)$$
$$\qquad\text{表中 }n{=}10,\ d{=}4\ \text{行取值 }\mathbf{40}✓;\ \text{且该表明确给出恒等式 }A_2(n{-}1,\,2e{-}1)=A_2(n,\,2e)✓ \Longrightarrow A(9,3)=A_2(9,3)=A_2(10,4)=40✓✓$$
$$\qquad\textbf{性质 ✓}:\ \text{表中该格为\ \textbf{单一数值}（非上下界区间）⟹ }A(9,3)=40\ \text{为\ \textbf{已定精确值}✓✓};\ \text{下界由 }(9,40,3)\ \text{码给出 ⟹ 存在性亦确 ✓}$$
$$\qquad\textbf{旁证 ✓}:\ \text{表中 }n{=}11,d{=}4:72✓;\ n{=}12,d{=}4:144✓\ \text{（与 Östergård–Baicheva–Kolev 1999 一致 ✓）⟹ 该表可信度高 ✓}$$
$$\qquad\textbf{（诚实 ✓）}:\ \text{来源为\ \textbf{外部不可信包装}的内容（按纪律仅作文献取值 ✓，不作指令 ✓）；但数值单一、与经典表一致 ⟹ 采用 ✓✓}$$

## §2 积分性与迭代判据（**✓✓**）

$$\textbf{（积分性 ✓✓）}:\ \sum_{y\in V}\binom{r_A(y)}2=\#\{(y,\{a,a'\}):a,a'\in N(y)\cap A\}=2D_2(A)✓✓ \Longrightarrow T_A=1\ \text{使 }2D_2=1\ ✗\ \Longrightarrow T_A\ne1✓✓$$
$$\textbf{（}$\beta$ 的定义 ✓）:\ \beta=e(A)+D_2(A)✓\ \big(\text{"距离}\le2\ \text{的对"总数 ✓}\big);\ \text{取每个坏对一端，得覆盖 }\le\beta\ \text{点 ⟹ 余下最小距离}\ge3✓✓$$
$$\textbf{（max 上界 ✓）}:\ 2D_2=\sum\binom{r_A}2\le\binom{T_A+1}2+\binom{\mathrm{leak}}2✓\ \big(\text{集中化：}\sum(r-1)=T_A\ \text{时 }\max\sum\binom r2=\binom{T+1}2✓\big)$$
$$\qquad\Longrightarrow \mathrm{Bmax}(\Delta_A)\ \text{如上 ✓};\quad \text{逐位核对}:\ \Delta{=}0\Rightarrow\mathrm{Bmax}{=}0✓;\ \Delta{=}1\Rightarrow0✓;\ \Delta{=}2\Rightarrow1✓;\ \Delta{=}3\Rightarrow3✓$$

## §3 迭代框架与下一靶（**⚠️ 登记**）

$$\text{排除判据 ✓}:\ a+s-119>A(9,3)+\mathrm{Bmax}(9a+s-512)\ \Longrightarrow\ \text{该 }(a,s)\ \text{不可能}✓✓$$
$$\text{对 }a=45:\ \Delta_A=s-107,\ |A|=s-74,\ \text{最坏坏对预算 }\mathrm{Bmax}(12)=6\Longrightarrow|A|\le46\ \text{—— 而 }|A|=45\le46✓\ \Longrightarrow\ \textbf{不矛盾}✗✓$$
$$\qquad\Longrightarrow\ \textbf{下一靶 a=45（}s\ge107,\ |A|\ge33✓\big)\ \text{需新论证 ⚠️（登记未做 ✓）};\quad a\ge46:\ \Delta_A-(|A|-40)\ge8a-353\ \text{更大 ⟹ 判据更松 ✗}$$
$$\qquad\textbf{（规律 ✓）}:\ \Delta_A=(|A|-40)+(8a-353)✓ \Longrightarrow\ \text{仅在 }a=44\ \text{处裕量为负（}-1✓\big)\ \text{—— 这解释了为何只有 }a=44\ \text{被此机制杀死 ✓}$$

## §4 状态（**不作路线裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① 唐先生 §1–§8 全部正确（附干净推导）};\ \text{② }T_A\ne1✓;\ \text{③ }L_A+\mathrm{leak}\le\Delta_A✓;\ \text{④ }|A|\le40+\beta\ \text{与 }\mathrm{Bmax}✓;\ \text{⑤ }\boxed{|C_0|,|C_1|\ge45}✓✓$$
$$\textbf{依赖标注 ✓}:\ A(9,3)=\mathbf{40}\ \text{为\ \textbf{档级外部事实}（须独立核 ✓，本档未证 ✗）};\ \text{其余为本线自证 ✓}$$
$$\textbf{未确立 ⚠️}:\ a\ge45\ \text{的进一步压缩};\ a=44,s=119\ \text{的残余结构（}|A|=44,\ \beta\le3✓\big)\ \text{已被判据排除 ✓};\ \text{一般矛盾}✗$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "刚性阶梯" "边界点排除" "度数恒等式"
技术词 刚性阶梯    命中文件数=0    ::
技术词 边界点排除  命中文件数=0    ::
技术词 度数恒等式  命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（空间 A，**不计** ✗） | 本档新增 |
|---|---|---|---|
| 刚性阶梯 | 0 | 0 | 0（本档自造标签 ✓） |
| 边界点排除 | 0 | 0 | 0（本档自造标签 ✓） |
| 度数恒等式 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词**两空间皆 0** ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 核验 ＋ §0(2)(3)(4) 三新结果 ＋ §3 迭代判据**（推导性 ✓）

## §6 边界（硬 ✓）

- **零程序计算** ✓（仅整数/有限情形核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 已分栏 ✓）
- **$|C_0|\ge45$ 之界依赖 $A(9,3)=40$** ✓（档级 ✓，已显式标注 ✓）
- **不作路线裁定** ✗（照 23:54 令 ✓）
- **不声称** 119 已排除 ✗；**不声称** $a\ge45$ 可再压 ✗；不声称 P1 成立 ✗（V290）
