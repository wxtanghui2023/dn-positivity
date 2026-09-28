# WITA0-2026-09-28 — **两处假前提（$t{=}12$ 球不交／$d(C_0)\ge3$）＋ $A_0$ 结构（新 ✓✓）＋ wedge 闭包（新 ✓✓）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 11:10 令 ✓）**：$|H|{=}1$ 之 $D_2$ 攻击 ＋ $t{=}12$ 干净命题；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-446／C-445／C-444，非新案 ✓）**
`docs/WITSAT2-2026-09-28-…`（**饱和仅 $t{=}12$／$\#\{d_U{=}0\}\ge33$ ✓✓**）｜`docs/WITSH-2026-09-28-…`（**singleton-$H$ 分离引理 ✓✓**）｜`docs/WITCAR-2026-09-28-…`（**载体 $U\cup N(H)$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（三词**两空间皆 0**，见 §4）
D0: 本档对象 ＝ **档案已有** Case I／$A_0$／wedge 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $d(A_0)\ge3$ 及其三推论（球不交／$|N[A_0]|{=}10|A_0|$／$d(A_0,A_1)\ge3$）＋ wedge 闭包之定量形式（被迫中点 $\le\lfloor t/2\rfloor$）＋ 两处假前提之否证** ✓）
**[RESEARCH]**

---

## §0 结论（**两处假前提 ✗✗｜$A_0$ 结构 ✓✓｜wedge 闭包 ✓✓｜无杀 ✗**）

$$\boxed{\textbf{(1) ✗✗假前提一（$t{=}12$）}:\ \text{"}A\ \text{是最小距离}\ge3\ \text{的码}\Longrightarrow\text{球两两不交}\Longrightarrow|\bigcup_aB_1(a)|=45\cdot10=450\text{"}\ \textbf{不成立}\ ✗✗}$$
$$\qquad\textbf{病根 ✓}:\ |A|=45>A(9,3)=40\Longrightarrow A\ \textbf{必有距离}\le2\ \text{的对}✗\ \big(\text{正是 }\beta=e(A)+D_2>0\ \text{之本意 ✓}\big)$$
$$\qquad\textbf{正确 ✓✓}:\ d(a,a')\in\{1,2\}\Longrightarrow|B_1(a)\cap B_1(a')|=\mathbf 2✓ \Longrightarrow \boxed{\Big|\bigcup_aB_1(a)\Big|=450-2(A_1(A)+A_2(A))+\text{三重修正}}✓$$
$$\qquad\Longrightarrow\ \text{§1 之"所有不等式取等"}\ ✗\ \text{与"精确分割 }393+45+12+62\text{"}\ ✗\ \text{均不成立};\ \text{正确：}\ \boxed{|N(A)\cap U|\le12}✓,\ \boxed{|U\setminus(A\cup P)|\ \ge\ 62}✓$$
$$\boxed{\textbf{(2) ✗✗假前提二（$|H|{=}1$）}:\ \text{"}h,u,v\in C_0\ \text{且}\ C_0\ \text{最小距离为 3}\text{"}\ \textbf{不成立}\ ✗✗}$$
$$\qquad\textbf{病根 ✓}:\ A=C_0\setminus\{h\}\ \text{且}\ |A|=44>A(9,3)=40\Longrightarrow C_0\ \text{含距离}\le2\ \text{的对}\ ✗\ \big(\text{即 }e,D_2\ ✗\big)$$
$$\qquad\Longrightarrow\ \text{定位到}\ S_2(h)\cong J(9,2)\ \textbf{不成立}✗\ \big(d(h,u)\in\{1,2\}\ \text{皆可能 ✓}\big);\ \textbf{但}\ \text{"}z\in N(h)\ \text{为中点}\Longrightarrow d(h,u),d(h,v)\le2\text{"}\ ✓✓\ \text{正确 ✓}$$
$$\boxed{\textbf{(3) ✓✓修正后的锋利版（新）}:\ \text{记}\ A_0:=\{a\in A:d_U(a)=0\}\ \big(\text{＝C-446 之"干净中心" ✓}\big)}$$
$$\qquad\boxed{d(A_0)\ \ge\ 3}\ ✓✓\ \big(\text{对全部 }t\ \text{成立 ✓✓}\big)\ \Longrightarrow\ \textbf{三推论 ✓✓}:\ \text{① }A_0\ \text{之球两两不交}✓;\ \text{② }|N[A_0]|=10|A_0|✓;\ \text{③ }\boxed{d(A_0,A_1)\ge3}✓$$
$$\qquad\textbf{证明 ✓✓（两行）}:\ a,a'\in A_0,\ d(a,a')\le1\Longrightarrow a'\in N(a)\subseteq U^c\ \text{而}\ a'\in A\subseteq U\ \text{矛盾}✗;$$
$$\qquad\qquad d(a,a')=2\Longrightarrow\ \text{共同邻点}\in N(a)\subseteq U^c\ \text{且}\ r_A\ge2\Longrightarrow\notin X_L=U^c\ \text{矛盾}✗$$
$$\qquad\Longrightarrow\ \boxed{|A_0|\in[33,\ 40]}\ ✓✓\ \big(33=\text{C-446 ✓};\ 40:\ 9|A_0|\le|U^c|=393\Rightarrow\le43\ ✓,\ \text{再与 }A(9,3)=40\ \text{取小 ✓}\big)$$
$$\qquad\Longrightarrow\ |A_1|\in[5,12]✓;\quad \boxed{\sum_{a\in A_1}d_U(a)=12}✓✓\ \big(\text{全部 }U\text{-入射由 }A_1\ \text{承担 ✓}\big)$$
$$\boxed{\textbf{(4) ✓✓wedge 闭包（新，$|H|{=}1$）}:\ \text{对}\ \{i,j\},\{i,k\}\in E_h\ \big(\text{即 }e_i{\oplus}e_j,\ e_i{\oplus}e_k\in A\cap S_2(h)✓\big):}$$
$$\qquad\text{中点}=\{e_i,\ e_j{\oplus}e_k\}✓;\ e_i\ \text{weight-1}\in N(h)✓,\ e_j{\oplus}e_k\ \text{距离 }h\ \text{为 2}\Longrightarrow\notin N(h)✓;\ r_A(e_j{\oplus}e_k)\ge2\Longrightarrow\notin X_L✓$$
$$\qquad\Longrightarrow\ \boxed{e_j{\oplus}e_k\in U\setminus N(h)✓\ \text{且}\ r_A\ge2}✓✓\ \Longrightarrow\ \text{每个楔消耗}\ge2\ \text{预算} \Longrightarrow\ \boxed{\#\{\text{被迫中点}\}\le\lfloor t/2\rfloor}✓✓$$
$$\qquad\Longrightarrow\ t{=}11:\ \#\{\text{被迫中点}\}\le5✓✓\ \big(\text{唯一"楔"在 }J(9,2)\ \text{上 ✓}\big)$$
$$\textbf{(5) ⚠️推测（非结果）}:\ \text{唐先生提议之}\ D_2>0\Longrightarrow2e(A)+\mathrm{leak}\ge12\ \textbf{未被推出}\ ✗;\ \text{wedge 仅给}\ \ge2✓\ \big(\text{登记为猜想 ✓}\big)$$
$$\textbf{(6) ⚠️无杀（诚实）}:\ \text{全部 }t\ \text{仍可行};\ \text{两处假前提之否证}\ \textbf{不带来新界}✗\ \big(\text{但 (3)(4) 为新的结构资产 ✓✓}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{$|H|{=}1$ 段 §1–§3 ✓}:\ \text{载体 }D_2=\tfrac12\sum_{U\cup N(H)}\binom{r_A}2✓;\ \text{中点类型排除}\ (N(h),N(h))\ \text{与含 }X_L\ \text{者 ✓✓（引理 C-445 ＋ }T_A{=}0✓\big)$$
$$\textbf{$|H|{=}1$ 段 §4–§6 ✓（给定 }d(h,u){=}d(h,v){=}2\text{）}:\ \text{局部二重重量结构}\ B=A\cap S_2(h)\subseteq\binom{[9]}2✓;\ \text{两点距离 2}\iff\text{两边相邻}✓✓$$
$$\qquad\text{"中点}=\{e_i,e_j{\oplus}e_k\}\text{"}\ ✓✓;\ \text{"另一个中点自动}\notin N(h)\text{"}\ ✓✓\ \big(\text{＝wedge 闭包之关键 ✓}\big)$$
$$\textbf{$|H|{=}1$ 段 §7–§9 ✗（条件式）}:\ \text{"每个 wedge 强迫 }jk\in U\text{"}\ ✓;\ \text{但"}\Rightarrow2e+\mathrm{leak}\ge12\text{"}\ ✗\ \text{为跳跃（见 §0(5) ✓）}$$
$$\textbf{$t{=}12$ 段 §1 ✗✗}:\ \text{"球不交／450／精确分割"}\ ✗\ \big(\text{见 §0(1) ✓}\big)$$
$$\textbf{$t{=}12$ 段 §2 ✓（在 }|A_0|\text{ 上）}:\ \#\{d_U>0\}\le12✓ \Longrightarrow |A_0|\ge33✓;\ |N[A_0]|=10|A_0|✓✓\ \big(\text{新据 §0(3) ✓}\big)$$
$$\textbf{$t{=}12$ 段 §3–§4 ✓（形式 ✓）}:\ |P|\le12✓,\ \sum_{p\in P}r_A(p)=12✓,\ r_A(p)\le9✓;\ \text{"无几何时集中给 66"}\ ✓\ \text{但须带容量封顶 }36q+\binom r2✓\ \big(\text{C-446 ✓}\big)$$
$$\textbf{$t{=}12$ 段 §5 ✓／✗}:\ \text{三集合结构 }A\leftrightarrow P\leftrightarrow W\ \text{与 }N(A)\cap W=\varnothing✓✓\ \big(|W|\ge62✓\big);\ \textbf{但"干净命题"含}\ d(A)\ge3\ \textbf{不成立}\ ✗✗$$
$$\qquad\Longrightarrow\ \text{正确版本须写成}\ \boxed{A=A_0\sqcup A_1,\ d(A_0)\ge3,\ d(A_0,A_1)\ge3,\ \sum_{A_1}d_U=12}✓✓\ \big(\text{而非 }d(A)\ge3\ ✗\big)$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }d(A_0)\ge3\ \text{及三推论（§0(3) ✓✓）};\ \text{② wedge 闭包与}\ \#\le\lfloor t/2\rfloor✓✓;\ \text{③ }\sum_{A_1}d_U=12✓✓;\ \text{④ }|A_0|\in[33,40]✓;\ \text{⑤ 球交 2 点之修正恒等式 ✓};\ \text{⑥ 两点距离 2}\iff\text{边相邻 ✓}✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}t{=}12\ \text{球不交／450／精确分割"}\ ✗✗;\ \text{"}C_0\ \text{最小距离 3"}\ ✗✗;\ \text{"干净命题含 }d(A)\ge3\text{"}\ ✗;\ \text{"}N(A)\cap U\ \text{恰 12 点"}\ ✗\ \big(\le12✓\big)$$
$$\textbf{未确立 ⚠️}:\ a{=}45\ \text{的排除};\ D_2{=}0\ \text{对 }|H|{=}1;\ \text{"}D_2>0\Rightarrow2e+\mathrm{leak}\ge12\text{"（猜想 ✓）}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① }t{=}12:\ A_0\ (33\text{--}40\ \text{点、球不交、}d(A_0,A_1)\ge3)＋A_1\ (\le12)＋P\ (\le12)\ \text{之共存问题 ✓✓};\ \text{② }|H|{=}1:\ \text{用 wedge 闭包把}\ \#\text{被迫中点}\le5\ \text{与 }D_2\ \text{下界 }\ge t-7-e\ \text{对撞 ✓};\ \text{③ 猜想之证否／证成 ✓}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "假前提" "干净中心" "wedge闭包"
技术词 假前提   命中文件数=0    ::
技术词 干净中心 命中文件数=0    ::
技术词 wedge闭包 命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 假前提 | 0 | 0 | 0（本档自造标签 ✓） |
| 干净中心 | 0 | 0 | 0（本档自造标签 ✓） |
| wedge闭包 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（自造标签仅作结构命名，不作新性主张 ✓）

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **两处假前提**已在 §0(1)(2) 显式标注 ✓✓；§1 之 $t{=}12$ §5 与 $|H|{=}1$ §7–§9 须带旗标 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；**不声称** 猜想成立 ✗（V290）
