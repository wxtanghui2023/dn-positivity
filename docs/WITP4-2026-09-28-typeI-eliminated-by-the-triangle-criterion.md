# WITP4-2026-09-28 — **P3 成立：Type I $(0,4,4,4)$ 被排除（✓✓✓，不依赖 $D$）；Type II 有显式可行构型（✓✓）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓）**。
> **范围（照唐先生 2026-09-28 12:53 令 ✓）**：Type-I 排除（30 状态图）＋ Type-II 可行性；**零程序计算**（仅有限穷举 ✓）；**不作路线裁定** ✗。

**已查地图：命中（接续 C-462／C-461／C-460，非新案 ✓）**
`docs/WITP3-2026-09-28-…`（**$Q_3$ 结构／390／对面桶 ✓✓✓**）｜`docs/WITP2-2026-09-28-…`（**完美匹配定理 ✓✓✓**）｜`docs/WITD1-2026-09-28-…`（**$M_C$ 表 ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓**，见 §3）
D0: 本档对象 ＝ **档案已有** 30 状态图／完美匹配／packing 对象（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次穷举确认 30 状态兼容图无三角形 ⟹ Type I $(0,4,4,4)$ 排除（不依赖 $D$）＋ 首次给出 Type II 之显式局部可行构型（$\|F\|{=}10$、$\|C\|{\ge}6$）＋ 更正 C-462 之 390 为"仅 $F$ 不相交"** ✓）
**[RESEARCH]**

---

## §0 结论（**Type I 排除 ✓✓✓｜Type II 可行 ✓✓｜390 须加条件 ✗✓**）

$$\textbf{状态定义 ✓}:\ (M,\epsilon)\ \text{共 }15\times2=30\ \text{个}✓;\ F^{(\epsilon)}(M):=\text{自 }M\ \text{所得 }Q_3\ \text{之 }\epsilon\text{-奇偶类}\ ✓;\quad \text{兼容}\iff M\cap M'{=}\varnothing\ \wedge\ F\cap F'{=}\varnothing✓$$
$$\boxed{\textbf{(1) ✓✓✓唐先生 P3\ \textbf{成立}（本档穷举确认 ✓✓✓）}:\ }\text{穷举 }30\ \text{状态之兼容图}:\ \textbf{每个状态恰 8 个兼容}\ ✓✓,\ \text{边数}=\mathbf{120}✓✓,\quad \boxed{\text{三角形数}=\mathbf0}✓✓✓$$
$$\qquad\Longrightarrow\ \boxed{\text{不存在三个两两兼容之 }(M_i,\epsilon_i)\Longrightarrow\textbf{Type I }(0,4,4,4)\ \textbf{不可行}}✓✓✓\ \big(\textbf{完全不依赖 }D\ ✓✓\big)$$
$$\qquad\textbf{（两条件之必要性 ✓✓）}:\ C_{p_i}\cap C_{p_j}{=}\varnothing\iff M_i\cap M_j{=}\varnothing\ ✓\ \big(\text{同 pair ⟹ }d{=}2\ ✗\big);\ F_{p_i}\cap F_{p_j}{=}\varnothing\ ✓\ \big(\text{同 triple ⟹ }d{=}2\ ✗\big)$$
$$\boxed{\textbf{(2) ✗✓C-462 之 390 须加条件（本档更正）}:\ }390\ \text{系"仅 }F\ \text{两两不相交"之计数 ✓\ \big(\text{当时未加 }M\cap M'{=}\varnothing\ ✗\big)};\ \text{二条件叠加后}＝\mathbf0✓✓$$
$$\qquad\Longrightarrow\ \text{（两个数都对 ✓）}:\ \text{C-462 之 }\sum_q|D_q|\le14\ \text{等结论\ \textbf{仅对 }F\text{-不相交情形成立} ✓\ \text{—— 该情形现已\ \textbf{不可达} ✗✓}}$$
$$\boxed{\textbf{(3) ✓✓Type-II 有显式可行构型（本档构造 ✓）}:\ }\text{满桶 }M_0{=}\{(0,1),(2,3),(4,5)\},\ F_0{=}\{(0,2,4),(0,3,5),(1,2,5),(1,3,4)\}✓\ \big(\epsilon{=}0✓\big)$$
$$\qquad\text{三 }|F|{=}2\ \text{桶（两两不相交且避开 }F_0\text{ ✓）}:\ F_{p_2}{=}\{(0,1,2),(0,3,4)\},\ F_{p_3}{=}\{(0,1,3),(0,2,5)\},\ F_{p_4}{=}\{(0,1,4),(0,2,3)\}✓$$
$$\qquad\text{对应 }C\ \text{可取 }\{0,5\},\ \{0,4\},\ \{1,2\}\ \big(\text{两两相异、避 }M_0\text{、且不 $\subset$ 本桶 }F✓\big)\Longrightarrow |C|\ge3{+}1{+}1{+}1{=}6\le12✓✓,\ |F|{=}10✓$$
$$\qquad\Longrightarrow\ \boxed{\text{Type II }(2,2,2,4)\ \textbf{局部未被排除}}\ ✗\ \big(\text{唯 }\textbf{全局}\ \text{与 }D\text{-侧耦合尚未查 ✓}\big)$$
$$\textbf{(4) 现状 ✓}:\ \text{三 extremal}\ (0,4,4,4),(2,2,2,4),(2,2,3,3)\ \Longrightarrow\ \boxed{(0,4,4,4)\ \textbf{KILLED}}\ ✓✓✓;\ (2,2,2,4)\ \text{局部可行}✓;\ (2,2,3,3)\ \text{未查 ⚠️}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{①✓✓✓}:\ C_{p_i}\cap C_{p_j}{=}\varnothing\iff M_i\cap M_j{=}\varnothing✓✓\ \big(\text{同 pair 于距离-2 prefix ⟹ }d{=}2✗\big);\ \text{三匹配边集两两不交 ⟹ 至少 9 条不同的 }K_6\ \text{边 ✓✓}$$
$$\textbf{②✓✓}:\ F_{p_i}\cap F_{p_j}{=}\varnothing✓✓\ \big(\text{同 }\text{triple}\Longrightarrow d{=}2✗\big);\ \text{30 状态、兼容关系之定义 ✓✓}$$
$$\textbf{③✓✓✓}:\ \text{每态 8 兼容／120 边／}\boxed{\text{无三角形}}✓✓✓\ \big(\text{本档独立穷举 ✓}\big);\ \text{故 Type I 排除 ✓✓✓\ \big(\textbf{不依赖 }D✓✓\big)}$$
$$\textbf{④✓}:\ \text{三 extremal 之重排 ✓✓;\ "(0,4,4,4) KILLED"\ ✓✓;\ \text{余下两型之优先级 ✓✓}}$$
$$\textbf{⑤✓（方向 ✓）}:\ \text{Type II 之 }\mathcal T=\binom{[6]}3\setminus F_1\ \big(16\ \text{个}\ ✓\big);\ \text{"三个两元 packing"\ 之提法 ✓✓;\ \text{本档已给出一个显式见证 ✓✓}}$$
$$\qquad\textbf{⚠️（一处须补 ✗）}:\ \text{Type-II 之三个 }|F|{=}2\ \text{桶}\ \textbf{同时}\ \text{需 }C\ \text{两两相异（}|C|\le12✓\big)\ \text{与 }F\subset\mathcal T✓;\ \text{本档见证满足 ✓，但全局完备性未证 ⚠️}$$

## §2 状态与下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{已确立 ✓}:\ \text{① }\boxed{\text{Type I 排除}}✓✓✓\ \big(\text{纯结构，不依赖 }D✓\big);\ \text{② 30 状态图：8/8 兼容、120 边、0 三角 ✓✓✓;\ \text{③ Type II 局部可行（显式见证 ✓）✓✓;\ \text{④ }M\cap M'{=}\varnothing\ \text{为 }C\text{-侧刚性 ✓✓};\ \text{⑤ }|F|{=}4\Rightarrow C_p\ \text{完美匹配（C-461 ✓✓）}}}$$
$$\textbf{已否证 ✗✓}:\ \text{"Type I 可行"\ ✗✓✓};\ \text{"C-462 之 390 即三满桶可行"\ ✗\ \big(\text{须加 }M\text{-不交 ✓}\big)}$$
$$\textbf{未确立 ⚠️}:\ \text{Type II 之全局可行性};\ \text{Type III}\ (2,2,3,3);\ a{=}45\ \text{的排除};\ M\ \text{之真值}$$
$$\textbf{（下一靶 ✓ 登记）}:\ \text{① Type II：把 }D\text{-侧（对面桶压力之类比 ✓）与 }|C|\le12\ \text{一并纳入，判定其全局可行性 ✓;\ \text{② Type III：无 }F{=}4\Longrightarrow\ \text{须另找结构性 P2（}|F|{=}3\ \text{类之结构定理 ✓ —— C-461 已登记 ✓）};\ \text{③ 若 II 亦排除 ⟹ }F{+}G\le21✓\ \big(\text{直接改进 C-456 ✓}\big)}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "三角形判据" "状态图" "局部见证"
技术词 三角形判据 命中文件数=0    ::
技术词 状态图     命中文件数=5    :: ./EXPLORATION-POINTS-REGISTER.md ./E191-bootstrap-failure-is-small-scale-artifact.md ./V112-input-substitution.md …
技术词 局部见证   命中文件数=3    :: ./E148-P-by-logical-form-dichotomy.md ./V125-S1-completeness-audit-upgrade-fails-equals-E148.md ./E149-L1-equivalence-reaudit.md
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 三角形判据 | 0 | 0 | ✓（自造标签 ✓） |
| 状态图 | 0 | **5**（`E191-…`／`V112-…` 等 ⟹ 空间 A 同名 ⟹ **不计** ✗） | ✗（**非新增** ✓） |
| 局部见证 | 0 | **3**（`E148-…`／`V125-…`／`E149-…` ⟹ 空间 A 同名 ⟹ **不计** ✗） | ✗（**非新增** ✓） |

- **（本条已先跑后写 ✓✓）**：三词均在**写入前**测得 ✓

## §4 边界（硬 ✓）

- **零程序计算** ✓（仅有限穷举：$\binom{30}2$ 状态对 ＋ 三角形检测 ＋ 局部构造搜索 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 已分栏 ✓）
- **一处更正**（C-462 之 390 须加 $M$-不交 ✓）已在 §0(2) 显式标注 ✓✓；**Type II 之全局完备性未证 ⚠️** 已标 ✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $a=45$ 已排除 ✗（V290）
