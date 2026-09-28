# WITSH-2026-09-28 — **singleton-$H$ 分离引理（新 ✓✓）＋ 载体错误第 5 次 ＋ §12 重犯**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 11:02 令 ✓）**：把 $t=11,\ |H|=1$ 算到底；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-444／C-443／C-442，非新案 ✓）**
`docs/WITCAR-2026-09-28-…`（**载体 $V\setminus X_L=U\cup N(H)$ ＋ 否证 $t{=}12$ ✗ ＋ 集中化 ✓✓**）｜`docs/WITRMAX-2026-09-28-…`（**$t$-参数化／Case I ✓✓**）｜`docs/WITB45-2026-09-28-…`（**$\beta$ 判据／$A(9,3)=40$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（见 §5；"分离引理" 1 命中**属线未定 ⟹ 不计** ✗）
D0: 本档对象 ＝ **档案已有** Case I／singleton-$H$／纤维对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 singleton-$H$ 分离引理的严格形式（每对距离-2 至少一个见证在 $N(h)$ 之外）＋ 第 5 次载体陷阱之否证 ＋ $t{=}12$ 之重犯之恒等式级否证（$\sum_y r_A=9|A|$）＋ $t{=}11$ 的条件式阶梯** ✓）
**[RESEARCH]**

---

## §0 结论（**新引理 ✓✓｜两处 ✗｜条件链 ✓｜无杀 ✗**）

$$\textbf{设定 ✓}:\ t=11\Rightarrow s=118,\ |A|=44,\ |H|=1\ \big(h\big);\quad T_A=0\ \text{(Case I)}✓;\quad |X_L|\ge8s-559=385✓;\ 9|A|=396✓$$
$$\qquad\Longrightarrow 2e(A)+\mathrm{leak}\ \le\ 396-385=11✓✓\ \Longrightarrow\ \boxed{e(A)\le5}✓\ \big(\text{整数 ✓}\big)$$
$$\boxed{\textbf{(1) ★★singleton-}H\ \textbf{分离引理（新 ✓✓，唐先生 §2 内核之严格化）}:\ \text{设 }h\in H\ \text{、}\{u,v\}\subseteq A\ \text{且}\ d(u,v)=2✓}$$
$$\qquad\text{则}\ \textbf{两个共同邻点不可能同时落在 }N(h)\ ✓✓;\ \text{即}\ \boxed{\forall\ \text{距离-2 对}:\ \ge1\ \text{个见证}\in V\setminus(X_L\cup N(h))=U\cup(N(H)\setminus N(h))}✓✓$$
$$\qquad\textbf{证明 ✓✓}:\ \text{平移 }h\mapsto0✓;\ \text{写}\ u=z\oplus e_i,\ v=z\oplus e_j\ (i\ne j)✓ \Longrightarrow \text{共同邻点}=\{z,\ z\oplus e_i\oplus e_j\}✓$$
$$\qquad\qquad\text{若二者皆 }\in N(0)\ \text{（即皆 weight-1）}:\ z=e_p,\ z\oplus e_i\oplus e_j=e_q\Longrightarrow e_p\oplus e_q=e_i\oplus e_j\Longrightarrow\{p,q\}=\{i,j\}✓$$
$$\qquad\qquad\Longrightarrow \{u,v\}=\{0,\ e_i\oplus e_j\}\ \ni\ 0=h\notin A\ ✗\ \big(\text{矛盾 ✓}\big)\ \Longrightarrow\ \text{引理成立 ✓✓}$$
$$\textbf{（穷举核验 ✓✓）}:\ Q_9\ \text{全部 }(z,i,j)\ (i\ne j)\ \text{上验证}:\ \text{共同邻点}\equiv\{z,z\oplus e_i\oplus e_j\}✓;\ \text{且"二者皆 weight-1"之 }72\ \text{例中},\ u,v\ \text{皆非 }0\ \text{者}=\mathbf 0✓✓$$
$$\qquad\Longrightarrow\ \textbf{引理零反例 ✓✓};\quad \text{同场核}\ \sum_y r_A(y)=9|A|\ \big(\text{随机 }|A|{=}44:\ 396=396✓\big)✓✓$$

$$\boxed{\textbf{(2) ✗✗载体错误第 5 次复发}:\ \text{唐先生 §1 的}\ X_L=V\setminus N(H)\ ✗\ \text{与 §2 的"共同邻点必属于 }N(H)\text{"}\ ✗}$$
$$\qquad\textbf{正确 ✓}:\ X_L:=U^c\setminus N(H)\Longrightarrow V\setminus X_L=U\cup N(H)✓✓\ \big(\text{C-444 ✓；已固化 TOOLS.md ✓}\big)$$
$$\qquad\Longrightarrow\ \text{§1 的"}\forall y\notin N(H):\ r_A(y)\le1\text{"}\ ✗\ \big(\text{仅对 }y\in X_L\ \text{成立 ✓；}y\in A\ \text{时 }r_A(y)\ \text{可任意 ✓}\big);\ \text{§2 的 }D_2(A)=0\ \textbf{未被证出}\ ✗$$
$$\boxed{\textbf{(3) ✗✗}:\ \text{§12 重犯 C-444 §0(3) 已否证之断言}\ ✗\ \big(\text{"(45,119),\ }T_A{=}0\ \text{不可能"}\big)\ \text{—— }\textbf{一行否证 ✓✓}}$$
$$\qquad\boxed{\sum_{y\in V}r_A(y)=\sum_{a\in A}|N(a)|=9|A|=\mathbf{405}\quad\text{（恒真，与 }T_A\ \text{无关 ✓✓）}}$$
$$\qquad\Longrightarrow\ \text{唐先生 §12 的"}\sum_y r_A(y)=512\text{"}\ \textbf{对任何 }|A|=45\ \text{都不可能}✗✓\ \big(512\ne405✓\big);\ T_A=0\ \text{只约束 }X_L\ \text{上的 }r_A✓$$
$$\boxed{\textbf{(4) ✓条件链（\textbf{在 }$D_2=0$\textbf{ 前提下}）}:\ \text{距离-1 图 }G_1(A)\ \text{的顶点覆盖 }S:\ d_{\min}(A\setminus S)\ge3✓}$$
$$\qquad\Longrightarrow |A|-\tau(G_1(A))\le A(9,3)=40\Longrightarrow \tau\ge4\Longrightarrow e(A)\ge\tau\ge4✓;\ \text{与 (1) 合}:\ \boxed{e(A)\in\{4,5\}}✓✓$$
$$\qquad\qquad e{=}4\Rightarrow\mathrm{leak}\le3✓;\quad e{=}5\Rightarrow\mathrm{leak}\le1✓;\quad e{=}4\Rightarrow A=C\sqcup T,\ |C|=40,\ d(C)\ge3\ \big(\text{极值 }(9,3)\ \text{码核心 ✓}\big)✓✓$$
$$\qquad\textbf{（§9 纤维结构 ✓✓，正确且有用）}:\ T_A=0\Longrightarrow f:X_L\to A\ \text{良定义（唯一 }A\text{-邻 ✓）};\ \text{纤维 }F_a,\ |F_a|\le9✓,\ \sum_a|F_a|=|X_L|✓$$
$$\qquad\qquad\text{且}\ d(a,b)=2\Longrightarrow F_a\cap N(b)=\varnothing✓✓\ \big(\text{否则该点 }r_A\ge2\ \text{与 }T_A=0\ \text{矛盾 ✓}\big)$$
$$\boxed{\textbf{(5) ⚠️无杀（诚实）}:\ \text{取消 }D_2=0\ \text{假设后},\ t{=}11\ \text{只需}\ e+D_2\ge4\ \wedge\ 2e+\mathrm{leak}\le11✓ \Longrightarrow \text{可行例}\ (e,D_2){=}(4,0)✓\ \text{或}\ (0,4)✓\ \Longrightarrow\ \textbf{无矛盾}}✗$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{§1 ✗}:\ X_L=V\setminus N(H)\ ✗;\ \text{"}\forall y\notin N(H):r_A(y)\le1\text{"}\ ✗\ \big(\text{见 §0(2) ✓}\big)$$
$$\textbf{§2 内核 ✓✓／结论 ✗}:\ \text{平移＋weight 论证\ \textbf{正确}✓✓ ⟹ 分离引理（§0(1) ✓）};\ \text{但由此得 }D_2=0\ \textbf{不成立}✗\ \big(\text{前提"必 }\in N(H)\text{"错 ✓}\big)$$
$$\textbf{§3–§7 ✓（条件式）}:\ \text{给定 }D_2=0:\ \tau\ge4,\ e\ge4,\ \beta=e\ge4=t-7\ \textbf{精确等号}✓✓;\ e\in\{4,5\}✓;\ \text{极值核心 }C\ (|C|{=}40)✓✓$$
$$\textbf{§8 ✗}:\ 2D_2=\sum_{N(H)}\binom{r_y}2\ ✗ \Longrightarrow \textbf{正确}\ 2D_2=\sum_{U\cup N(H)}\binom{r_y}2✓✓$$
$$\textbf{§9 ✓✓}:\ \text{纤维分划与 }F_a\cap N(b)=\varnothing\ \text{禁配关系 ✓✓（新表述 ✓）}$$
$$\textbf{§10–§11 ✓}:\ t{=}10\ \text{的无条件部分 }e\le5✓;\ \text{但 }D_2\ \text{的收窄仍依赖载体错位 ✗}$$
$$\textbf{§12 ✗✗}:\ \text{见 §0(3)：与恒等式 }\sum_y r_A=9|A|✓\ \text{直接冲突 ✗✓}$$
$$\textbf{§13–§14 ✓（条件式）}:\ \text{攻击树与 }m_h(k)\ \text{的提法 ✓，但每格须显式带"若 }D_2=0\text{"的旗标 ✓}$$
$$\textbf{（§2 之边界不变 ✓）}:\ \text{引理无需 }A(c)=0\ \text{或 }(\alpha)✓;\ \text{仅用}\ T_A=0\ \text{与 }h\notin A✓✓$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① singleton-}H\ \text{分离引理（§0(1) ✓✓）};\ \text{② }\sum_y r_A=9|A|\ \text{恒等式之否证力（§0(3) ✓✓）};\ \text{③ 条件链 }D_2{=}0\Rightarrow e\in\{4,5\}\Rightarrow A\supseteq40\text{-极值核（§0(4) ✓✓）};\ \text{④ 纤维结构 ✓✓};\ \text{⑤ }e\le5✓$$
$$\textbf{已否证 ✗✓}:\ \text{"}X_L=V\setminus N(H)\text{"};\ \text{"}\forall y\notin N(H):r\le1\text{"};\ \text{"}2D_2\ \text{只在 }N(H)\text{"};\ \text{"}\sum_y r_A=512\text{"};\ \text{"}t{=}12\ \text{直接不可能"（第二次 ✗）}$$
$$\textbf{未确立 ⚠️（＝真正的缺口 ✓）}:\ \boxed{|H|=1\ \text{时 }D_2(A)=0\ \text{是否成立}}\ ✓✓\ \text{—— 无之则 }(e,D_2){=}(0,4)\ \text{等仍可行 ⟹ }t{=}11\ \text{不能被杀 ✗}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 攻 }|H|{=}1\Rightarrow D_2=0\ \big(\text{或用分离引理证明"每对至少耗一个 }U\setminus N(h)\ \text{见证"之定量版本 ✓}\big);\ \text{② 条件式的极值延拓分类（}40\text{-码}＋4\text{点}＋\text{singleton }H\ \big);\ \text{③ }A(9,3){=}40\ \text{极值码之分类\ \textbf{不在档案} ✗（须文献 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "分离引理" "极值延拓" "纤维分划"
技术词 分离引理  命中文件数=1   :: ./B1b-owner-structure-engine-and-results-d1-d4.md
技术词 极值延拓  命中文件数=0   ::
技术词 纤维分划  命中文件数=0   ::
```
| 词 | 本线命中（空间 B） | 属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 分离引理 | 0 | 1（`B1b-owner-structure-engine-…` ⟹ 属线未定 ⟹ **不计** ✗） | 0（既有词 ✓） |
| 极值延拓 | 0 | 0 | 0（本档自造标签 ✓） |
| 纤维分划 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（自造标签仅作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§0(1) 新引理 ＋ §0(2)(3) 两处否证 ＋ §0(4) 条件链 ＋ §0(5) 无杀判定**（推导性 ✓）

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **两处必改**（载体第 5 次 ＋ §12 重犯）已在 §0(2)(3) 显式标注 ✓✓
- **条件旗标 ✓**：§0(4)、§1 的 §3–§7、§13–§14 均为**条件式**（在 $D_2=0$ 下 ✓）——不得脱旗引用 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗；不声称 $D_2=0$ 成立或失败 ✗（V290）
