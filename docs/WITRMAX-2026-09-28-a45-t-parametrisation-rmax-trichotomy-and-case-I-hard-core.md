# WITRMAX-2026-09-28 — **$a=45$ 的 $t$-参数化 ＋ $r_{\max}$ 三分类**（三处因子 2 修正；Case I 是硬核）

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏** ✓。
> **范围（照唐先生 2026-09-28 10:55 令 ✓）**：火力集中于 $a=45$；**零程序计算**（仅整数核对 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-442／C-441／C-440，非新案 ✓）**
`docs/WITB45-2026-09-28-…`（**$|C_0|\ge45$／迭代判据 $\beta$／$A(9,3)=40$ 取证 ✓✓**）｜`docs/WITEFF-2026-09-28-…`（**$L_A+\mathrm{leak}\le\Delta_A$ ✓✓**）｜`docs/WITGATE-2026-09-28-…`（**$\Delta_A$ 阶梯／$\mathrm{min\_excess}_9$ ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（见 §5）
D0: 本档对象 ＝ **档案已有** $a=45$ 参数化／$r_y$ 多重度对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $a=45$ 的 $t$-参数化核验 ＋ 三处因子 2 修正 ＋ $r_{\max}$ 三分类的精确内容 ＋ Case I 之硬核判定（含预算相容性）＋ 命题式二分** ✓）
**[RESEARCH]**

---

## §0 结论（**参数化 ✓｜三处 ✗因子修正 ✓｜三分类内容 ✓✓｜Case I 硬核 ✓✓**）

$$\text{设定 ✓（唐先生 §1 ✓）}:\ a=45\Longrightarrow|A|=a+s-119=s-74✓;\quad t:=s-107=\Delta_A=9a+s-512✓;\quad s\in[107,119]\Longrightarrow\boxed{t\in[0,12]}✓$$
$$\qquad\text{预算 ✓}:\ L_A+\mathrm{leak}\le t✓\ \big(\text{C-442 ✓}\big);\quad \text{判据 ✓}:\ |A|=33+t\le A(9,3)+\beta=40+\beta\Longrightarrow \boxed{\beta\ \ge\ t-7}✓✓$$
$$\qquad\Longrightarrow\ \textbf{战场确为 }t\ge8✓✓\ \big(t\le7:\ |A|\le40\ \text{自动满足 ✓ ⟹ 无需码判据 ✓}\ \text{—— 唐先生表 ✓ 逐位无误 ✓}\big)$$
$$\boxed{\textbf{(1) ✗✗三处因子 2 修正（本档必标 ✓）}:\ \text{核心恒等式为}\ 2D_2(A)=\sum_{y\in V}\binom{r_y}2✓✓\ \big(\text{唐先生 §7 亦写对 ✓}\big)}$$
$$\qquad\textbf{①}\ \text{唐先生 §5 的}\ D_2(A)\ge T_A\ \textbf{不对}\ ✗\ \text{（应为）}\ \boxed{D_2(A)\ \ge\ \tfrac12\,T_A}\ ✓✓\ \big(\text{因对 }y\in X_L:\ \binom{r_y}2\ge r_y-1✓\big)$$
$$\qquad\textbf{②}\ \text{唐先生 §6 的表给的是}\ \sum\binom{r_y}2\ \text{值，不是 }D_2\ ✗\ \text{（须减半）}:\ T_A{=}2,3,4\Longrightarrow\boxed{D_2\le1,3,5}✓✓\ \big(\text{非 }3,6,10✗\big)$$
$$\qquad\textbf{③}\ \text{§9 之"桥"缺 }1/2\ ✗;\ \textbf{正确形式 ✓✓}:\ \boxed{\beta\ =\ \tfrac12L_A\ +\ \tfrac12\sum_{y\in X_L}\tfrac{(r_y-1)(r_y-2)}2\ +\ \tfrac12\sum_{y\notin X_L}\binom{r_y}2}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\beta\ \ge\ \tfrac12 L_A}\ ✓✓\ \big(\text{后两项皆 }\ge0✓\big)\ \text{—— 且 }\textbf{Case I 时取等 ✓✓（见 §2）}$$
$$\boxed{\textbf{(2) ✓✓三分类成立（唐先生 §12 ✓，本档给出精确内容）}:\ r_{\max}:=\max_{x\in X_L}r_A(x)✓}$$
$$\qquad\textbf{Case I }(r_{\max}{=}1):\ T_A=0✓\ \Longrightarrow\ L_A=2e(A)✓;\quad \beta=e(A)+\tfrac12\sum_{y\notin X_L}\binom{r_y}2✓\ \big(\text{见 §2 之锐化}\big)$$
$$\qquad\textbf{Case II }(r_{\max}{=}2):\ T_A=\#\{r_y{=}2\}✓;\quad \sum_{X_L}\binom{r_y}2=T_A✓ \Longrightarrow \beta=e(A)+\tfrac12\big(T_A+\sum_{y\notin X_L}\binom{r_y}2\big)✓$$
$$\qquad\textbf{Case III }(r_{\max}{\ge}3):\ \text{局部三角结构 ✓✓（唐先生 §11 ✓ 已核）}:\ \{e_i,e_j,e_k\}\ \text{两两距离 2 ✓；三对的共同邻点 }(0,e_i{\oplus}e_j),(0,e_i{\oplus}e_k),(0,e_j{\oplus}e_k)✓$$
$$\qquad\qquad\Longrightarrow 2D_2\ \ge\ \binom32+3=\mathbf 6\Longrightarrow \boxed{D_2\ge3}✓✓\ \big(\text{每 }r{=}3\ \text{点至少再带 3 个 }r{\ge}2\ \text{的邻点 ✓}\big)$$
$$\boxed{\textbf{(3) ★★硬核判定（本档 ✓✓）}:\ Case\ I\ \text{的}\ \beta=\tfrac12L_A\ \text{是同一预算下\ \textbf{最小值}}\ ✗✓ \Longrightarrow \textbf{排除 }a{=}45\ \text{必须\textbf{结构性排除 Case I}}✓✓}$$
$$\qquad\textbf{（预算相容性核对 ✓✓）}:\ Case\ I\ \text{需}\ e(A)\ \text{充足};\ \text{而 }2e\le L_A\le t\Longrightarrow e\le t/2⟹\ \text{对 }t{=}8{:}\ \text{需 }e\ge1\le4✓;\ t{=}12{:}\ \text{需 }e\ge5\le6✓ \Longrightarrow \textbf{预算不排除 Case I}✗✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{命题式二分（新 ✓✓）}:\ t\ge8\ \Longrightarrow\ \text{或 }e(A)+\tfrac12\sum_{V\setminus X_L}\binom{r_y}2\ \ge\ t-7\ (\text{Case I}),\ \text{或 }r_{\max}\ge2✓}$$
$$\qquad\textbf{（锐化 ✓）}:\ Case\ I\ \text{中 }T_A=0\Longrightarrow\ \text{每个 }x\in X_L\ \text{恰有一个 }A\text{-邻 ✓} \Longrightarrow X_L\ \text{与 }A\ \text{近似一一对应 ✓}\ \big(\text{＝最容易满足判据的退化结构}\ ✓✓\big)$$

---

## §1 $t$-参数化的核验（**✓✓**）

| $t$ | $s$ | $\|A\|$ | 需 $\beta\ge t-7$ | 状态 |
|---|---|---|---|---|
| 0…7 | 107…114 | 33…40 | $\le0$ | **自动** ✓（$\|A\|\le40$ ✓ 无需码判据 ✓） |
| 8 | 115 | 41 | 1 | 战场 |
| 9 | 116 | 42 | 2 | 战场 |
| 10 | 117 | 43 | 3 | 战场 |
| 11 | 118 | 44 | 4 | 战场 |
| 12 | 119 | 45 | 5 | 战场 |

$$\Longrightarrow\ \Delta_A=t=s-107✓;\quad \text{并验证 }L_A+\mathrm{leak}\le\Delta_A=t✓\ \big(\text{C-442 §0(1) ✓}\big)$$

## §2 三分类的精确内容（**✓✓ 含因子修正**）

$$\textbf{Case I ✓}:\ r_{\max}=1\Longrightarrow T_A=0\Longrightarrow L_A=2e(A)✓;\quad D_2=\tfrac12\Big(0+\sum_{y\notin X_L}\binom{r_y}2\Big)✓$$
$$\qquad\textbf{（关键锐化 ✓✓）}:\ \sum_{y\notin X_L}r_y=2e(A)+\mathrm{leak}✓ \Longrightarrow \sum_{y\notin X_L}\binom{r_y}2\le\binom{2e+\mathrm{leak}}2✓ \Longrightarrow \boxed{\beta\ \le\ e(A)+\tfrac12\binom{2e+\mathrm{leak}}2}✓$$
$$\qquad\Longrightarrow\ \text{与 }\beta\ge t-7\ \text{合}:\ t-7\le e+\tfrac12\binom{2e+\mathrm{leak}}2\ \wedge\ 2e+\mathrm{leak}\le t✓\ \text{—— }\textbf{相容（无矛盾 ✗）}$$
$$\textbf{Case II ✓}:\ \sum_{X_L}\binom{r_y}2=T_A✓ \Longrightarrow \beta=e+\tfrac12\big(T_A+\sum_{y\notin X_L}\binom{r_y}2\big)✓;\quad \text{（唐先生 §12 之 }\beta=L_A-e\text{ 需 }D_2=T_A\ ✗\text{，仅当无外部贡献时成立 ✓\big)}$$
$$\textbf{Case III ✓}:\ r\ge3\ \text{之处必生三角；}D_2\ge3✓✓;\ \text{且三对之第二共同邻点两两不同 ✓ ⟹ 额外 }r\ge2\ \text{点}\ge3✓$$

## §3 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }t\text{-参数化与预算（§1）};\ \text{② 三处因子修正（§0(1)）};\ \text{③ 三分类精确内容（§2）};\ \text{④ }D_2\ge\tfrac12T_A\ \text{与 }\beta\ge\tfrac12L_A✓;\ \text{⑤ Case III 之 }D_2\ge3✓;\ \text{⑥ 命题式二分（§0(3)）}✓$$
$$\textbf{已否证 ✗}:\ \text{"Case I 由预算排除"（可相容 ✓）};\ \text{"}D_2\ge T_A\text{" ✗};\ \text{"}D_2\le3,6,10\text{" ✗}$$
$$\textbf{未确立 ⚠️}:\ a=45\ \text{的排除};\ \text{Case I 的结构性排除（须证 }T_A=0\Rightarrow|A|\le40\ \text{或等价）};\ r\ge3\ \text{的局部相容性分类}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① 证 }T_A=0\ (\text{Case I})\Longrightarrow|A|\le40\ \big(\text{即可杀 }t\ge8\ \text{之 Case I ✓}\big);\ \text{② 或分类 }r{=}3,4,\dots\ \text{之局部构型与互斥 ✓（唐先生 §11-§12 ✓）}$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "因子二修正" "三分类" "多重度分层"
技术词 因子二修正  命中文件数=0    ::
技术词 三分类      命中文件数=59   :: ./WHY-CANNOT-CREATE-TOOLS-bohr-and-tao.md ./C141-today-net-output-card-2026-09-19.md …
技术词 多重度分层  命中文件数=0    ::
```
| 词 | 本线命中（空间 B） | 跨空间／属线未定（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 因子二修正 | 0 | 0 | 0（本档自造标签 ✓） |
| 三分类 | 0（59 命中多属空间 A／未定 ⟹ **不计** ✗） | 59 | 0（既有词 ✓） |
| 多重度分层 | 0 | 0 | 0（本档自造标签 ✓） |

- **本档新增**：**0** 个术语 ✓（三词本线皆 0 ⟹ 自造标签，作结构命名，不作新性主张 ✓）
- **注 ✓**：本档实质＝**§1 核验 ＋ §0(1) 三处修正 ＋ §2 三分类内容 ＋ §0(3) 硬核判定**（推导性 ✓）

## §5 边界（硬 ✓）

- **零程序计算** ✓（仅整数核对 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **三处因子修正**已在 §0(1) 显式标注 ✓✓（防误用 ✓）；$A(9,3)=40$ 承重事实已在 C-442 取证 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）
- **不声称** $a=45$ 已排除 ✗；**不声称** Case I 不可行 ✗；不声称 P1 成立 ✗（V290）
