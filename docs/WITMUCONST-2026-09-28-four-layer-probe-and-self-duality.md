# WITMUCONST-2026-09-28 — **C-487 四层全通：$c$-incidence $\equiv\mathbf5$；$\mu(y)\equiv\mathbf{384}$（\textbf{自对偶入射结构} $v{=}160$、$k{=}r{=}128$）；码字度数 $\equiv\mathbf{12}$；owner 三元组皆\ \textbf{等边}（$4,4,4$）$128{=}160-32$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 14:21 令 ✓）**：四层（$c$-incidence ／ $\mathcal T_x$ ／ 交分布 ／ $\mu$ 双计数）＋ $(d_p,d_q,d_c)$ 表；**先跑后写 ✓✓**；**不作路线裁定** ✗。
> **符号纪律 ✓**：不用 $A_x$（C-485 ✗）；局部对象＝$O_{I_{40}}(x){=}\{p,q,c\}$ ＋ 三球 $X,P,Q$ ✓。

**已查地图：命中（接续 C-486／C-485／C-482，非新案 ✓）**
`docs/WITP3128-2026-09-28-…`（**包含排除／仿射否证 ✓✓✓**）｜`docs/WITINC38-2026-09-28-…`（**兼容池常数 ✓✓**）｜`docs/WITD0LEMMA-2026-09-28-…`（**160 额外零点 ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $O(x)$／$N_2$ 球／特殊点集对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $c$-incidence $\equiv5$（480/480）＋ 首次给出 $\mu(y)\equiv384$ 与\ \textbf{双计数恒等式} $160\times384{=}480\times128$ ＋ 首次给出\ \textbf{自对偶性} $Y{=}X$（入射结构 $v{=}160,k{=}r{=}128$）＋ 首次给出码字度数 $\equiv12$ 与 owner 三元组\ \textbf{皆等边} $(4,4,4)$** ✓）
**[RESEARCH]**

---

## §0 结论（**四层全通 ＋ 自对偶 ＋ 五个整数常数**）

$$\textbf{设定 ✓}:\ I_{40}\ \text{＝Best};\ \text{宇宙＝同奇偶层 512};\ \text{特殊点集 }\mathcal S:=\{u\notin I_{40}:\ |O_{I_{40}}(u)|{=}3\},\ |\mathcal S|{=}\mathbf{160}✓✓\ \big(\text{＝C-479 谱 }\{3{:}160\}✓\big)$$
$$\qquad\textbf{（层 0 · 实例归一 ✓✓）}:\ \text{degree-1 实例}\ (x,\{p,q\})\ \text{共 }\mathbf{480}{=}\mathbf{160}\times3✓✓\ \big(\text{每 }x\in\mathcal S\ \text{对应其 owner 三元组内之 3 个对 ✓}\big)$$
$$\boxed{\textbf{(1) ✓✓c-incidence}:\ }\forall x\in\mathcal S,\ \big|\{y\in P_3(x):\ c\in O(y)\}\big|=\mathbf5\ ✓✓\ \big(\text{480/480 同值 ✓✓}\big)$$
$$\qquad\textbf{（与唐先生之预期对照 ⚠️）}:\ \text{其猜"或为 }64"\ ✗\ ——\ \text{实值为\ \textbf{5}（更小、更刚 ✓）};\ \text{故 }128\neq64+64\ ✗$$
$$\boxed{\textbf{(2) ✓✓\mathcal T_x 层}:\ }y\mapsto T_y{=}O_{I_{40}}(y)\ \text{\textbf{单射}}✓✓\ \big(160/160\ \text{True}✓\big);\quad |T_y|{=}3\ \text{恒成立}✓\ \big(|O(y)|{=}3\ \text{对一切 }y\in P_3(x)✓\big)$$
$$\qquad\Longrightarrow\ |\mathcal T_x|{=}\mathbf{128}✓✓;\quad \textbf{码字度数}:\ \forall j\in I_{40}:\ \#\{u\in\mathcal S:\ j\in O(u)\}=\mathbf{12}✓✓\ \big(480/40{=}12✓\big)$$
$$\qquad\Longrightarrow\ \textbf{（新刚性 ✓✓）}:\ \text{每个特殊点之 owner 三元组两两距离型恒为 }\boxed{(4,4,4)}✓✓\ \text{——\ \textbf{等边三元组} ✓✓}$$
$$\boxed{\textbf{(3) ✓✓交分布}:\ }\{|T_y\cap T_z|\}=\{0{:}1028429,\ 1{:}254025,\ 2{:}18026\}\ ✓\ \big(\text{总计 }1300480{=}160\times\binom{128}2✓\big)$$
$$\boxed{\textbf{(4) ✓✓✓\mu 双计数层}:\ }\forall y\ \text{被覆盖}:\ \mu(y){=}\#\{x:\ y\in P_3(x)\}=\mathbf{384}\ ✓✓\ \big(\text{全 160 点同值 ✓✓}\big)$$
$$\qquad\Longrightarrow\ \boxed{160\times384\ =\ 61440\ =\ 480\times128}\ ✓✓✓\ \text{——\ 唐先生所期之\ \textbf{双计数恒等式\ 成立}}✓✓$$
$$\qquad\textbf{（等价形式 ✓✓）}:\ \mu{=}384{=}3\times128⟹\text{每个 }y\ \text{恰含于 }\mathbf{128}\ \text{个 }P_3(x)\ \text{之中 ✓✓}$$
$$\boxed{\textbf{(5) ✓✓✓自对偶性（本档核心发现）}:\ }\text{被覆盖之 }y\ \text{所成集合}\ Y:=\bigcup_{x\in\mathcal S}P_3(x)\ \text{满足}\ \boxed{Y=\mathcal S}\ ✓✓\ \text{——\ 即\ \textbf{同一批 160 点}}✓✓$$
$$\qquad\Longrightarrow\ \text{160 个特殊点上存在\ \textbf{正则自对偶入射结构}}:\ v{=}160,\ \text{块大小 }k{=}128,\ \text{复现数 }r{=}128✓✓\ \big(\text{互补块 }=32✓\big)$$
$$\qquad\textbf{（注意 ✗）}:\ \lambda{=}r(k{-}1)/(v{-}1){=}128\cdot127/159\ \text{非整数}⟹\ \text{\textbf{不是} BIBD ✗（但仍极正则 ✓）}$$
$$\boxed{\textbf{(6) ✓✓128 之新解释}:\ }\boxed{128\ =\ 160-32}\ ✓✓\ \big(\text{而 }\mathcal S\ \text{自对偶 ⟹ 问题化为}\ \textbf{"被排除的 32 个是谁"}\ ✓✓\big)$$
$$\qquad\text{（C-486 之否证仍立 ✓）}:\ 128\ \text{\textbf{不是}仿射子空间大小（40/40 False ✗）};\ \text{今改为"}160-32\ 之\ \textbf{正则互补} ✓"$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生 §1（}P_3\ \text{≅\ 纯 degree-3 层、}d_S(y){=}3\ \text{恒成立、}(x;\{p,q\};c)\ \text{旗标）\ \textbf{完全正确}}✓✓$$
$$\textbf{✓✓}:\ \text{唐先生 §3（}c-incidence\ 之\ 0/1\ 二分 ＋ 期待"漂亮常数"）\ \textbf{方向正确}✓✓;\ \text{唯猜 }64\ ✗\ \text{而实为 }5✓$$
$$\textbf{✓✓}:\ \text{唐先生 §4（}\mathcal T_x\ ／ 单射 ／ 码字度数 ／ 交分布 四问）**全部执行** ✓✓；单射 ✓、度数 \equiv12 ✓、交分布三值 ✓$$
$$\textbf{✓✓}:\ \text{唐先生 §7（}\mu(y)\ 双计数）\ \textbf{命中要害}}✓✓:\ \mu\ \text{恒定 }\mathbf{384}\ ⟹\ \text{恒等式 }160\times384{=}480\times128✓✓\ \text{——\ 其"从以 }x\ \text{为中心之常数转为全局入射参数"\ 之判断\ \textbf{实现}✓✓$$
$$\textbf{✓✓（新）}:\ \text{唐先生未提之\ \textbf{自对偶性 }Y{=}X✓✓\ ——\ 本档\ \textbf{核心新发现}}✓✓$$

## §2 常数汇总裁（**本档 ✓✓**）

| 量 | 值 | 性质 |
|---|---|---|
| $\|\mathcal S\|$ | $160$ | $=4\times40$ ✓ |
| $\|P_3(x)\|$ | $128$ | $=160-32$ ✓ |
| $c$-incidence | $5$ | 恒定 ✓✓ |
| $\mu(y)$ | $384$ | $=3\times128$ 恒定 ✓✓ |
| 双计数 | $160\times384=61440=480\times128$ | 恒等式 ✓✓ |
| 码字度数 | $12$ | $=480/40$ 恒定 ✓✓ |
| owner 三元组型 | $(4,4,4)$ | **等边** ✓✓ |
| 交分布 | $0{:}1028429,\ 1{:}254025,\ 2{:}18026$ | 三值 ✓ |
| 自对偶 | $Y=X$ | $v{=}160,k{=}r{=}128$ ✓✓ |

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓ 最优先）}:\ \boxed{\text{求出每 }x\ \text{之\ \textbf{被排除 32 集}}E_x:=\mathcal S\setminus P_3(x)}\ ✓\ \{|E_x|{=}32✓\};\ \text{其\ \textbf{结构}（是否是 32 个"同类"点 ✓？是否 }E_x\ \text{自身有规律 ✓？）}$$
$$\textbf{（靶 2 ✓）}:\ \text{160 个等边 }(4,4,4)\ \text{三元组之\ \textbf{设计}：（}v{=}40\ \text{码字},\ b{=}160\ \text{三元组},\ \text{每码字 }12\ \text{次）}⟹\ \text{是否为已知设计／可否给出显式参数 ✓}$$
$$\textbf{（靶 3 ✓）}:\ c-incidence {=}5\ \text{之\ \textbf{由来}（每 }P_3(x)\ \text{中恰 5 个 }y\ \text{之 owner 含 }c✓\big)⟹\ \text{是否 }\sum_{x}\cdots\ \text{可给一条\ \textbf{局部恒等式}}✓$$
$$\textbf{（并行 ⚠️）}:\ r{=}3\ \text{profile}✗;\ \text{非 Best 39-码}✗\ \big(\text{无抓手 ✓}\big)$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "自对偶入射" "双层计数恒等式" "等边三元组" "特殊点集"
技术词 自对偶入射       命中文件数=0    ::
技术词 双层计数恒等式   命中文件数=0    ::
技术词 等边三元组       命中文件数=0    ::
技术词 特殊点集         命中文件数=1    :: ./ZF-G5G6-DIM-screen-and-height-collapse.md
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 自对偶入射 | 0 | 0 | ✓（自造标签 ✓） |
| 双层计数恒等式 | 0 | 0 | ✓（自造标签 ✓） |
| 等边三元组 | 0 | 0 | ✓（自造标签 ✓） |
| 特殊点集 | 0 | **1**（`ZF-*` 属**空间 A（RH 线：DIM/CAN 门）** ⟹ **空间 A 同名，不计** ✗✓） | ✓（本线新增 ✓） |

- **（本条\ \textbf{确已先跑后写} ✓✓）**：四词均在**写入前**测得 ✓

## §5 边界（硬 ✓）

- **有限穷举** ✓（480 实例 ＋ 160 特殊点全量 ✓；交分布全量 $\binom{128}2\times160$ ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 已分栏 ✓）
- **一处与预期不符**（$c$-incidence 实为 5 非 64 ✗✓）＋ **一处核心新发现**（自对偶 $Y{=}X$ ✓✓）＋ **一处重释**（$128{=}160-32$ ✓✓）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** 128 之最终来源已定 ✗；**不声称** P1 成立/不成立 ✗（V290）
