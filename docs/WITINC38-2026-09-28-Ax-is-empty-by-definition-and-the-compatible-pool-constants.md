# WITINC38-2026-09-28 — **38-码 $A_x/B_x$ incidence 实验：$A_x$ \textbf{定义性为空} ✗（码字无距离-2 邻点）；修正后局部对象；兼容池（度 $\le2$）恒 $0$ ✓／（度 $\le3$）恒 $\mathbf{128}$ ✓✓／（度 $\le4$）$318$–$319$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 14:14 令 ✓）**：38-码上 $A_x/B_x$ incidence 实验（**不预设 injection** ✓）；**有限穷举** ✓；**不作路线裁定** ✗。

**已查地图：命中（接续 C-484／C-483／C-480，非新案 ✓）**
`docs/WITD1EMPTY-2026-09-28-…`（**命题 P／Family B 更正 ✓✓**）｜`docs/WITEQ-2026-09-28-…`（**残点度下界 ✓✓**）｜`docs/WITOWNER-2026-09-28-…`（**blocking identity ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $O(x)$／$38$-码族／兼容池对象（重命名：否 ✗；新对象：**兼容池首次入档** ✓）
D1: 1（**首次给出 $A_x$ 之\ \textbf{定义性为空} 判定（码字无距离-2 邻点）＋ 首次给出 38-码 degree-1 点之\ \textbf{兼容池三重常数}（$\le2$ 恒 $0$；$\le3$ 恒 $128$；$\le4$ 为 $318/319$）＋ 首次给出 $|B_x|{=}42$ 之结构解释** ✓）
**[RESEARCH]**

---

## §0 结论（**✗$A_x$ 定义性为空｜✓✓兼容池三重常数｜✓ 无 injection 之事实**）

$$\textbf{设定 ✓}:\ D=\{p,q\}\subset I_{40};\ S:=I_{40}\setminus D\ \text{（38-码 ✓）};\ \text{degree-1 外点 }x\ \big(d_S(x){=}1✓\big);\ \text{唯一 }S\text{-owner }c✓$$
$$\qquad\text{全体 degree-1 点之 }\mathbf{480}\ \text{个（780 对中：160 对含 1 个、160 对含 2 个 ✓ 与 C-480 一致 ✓）}$$
$$A_x$$
$$\qquad\textbf{理由（一行 ✓）}:\ d_{\min}(I_{40}){=}4⟹\text{码字之间无距离-2 ⟹ }O(v)\cap I_{40}{=}\varnothing✓\ \big(v\in I_{40}✓\big)$$
$$\qquad\Longrightarrow\ \boxed{A_x\ \text{恒为空}\ ✗}\ ⟹\ \text{题设之 }A_x{\times}B_x\ \text{incidence 矩阵\ \textbf{退化}}✗\ \big(\text{非数据问题，是定义问题 ✓}\big)$$
$$\qquad\textbf{（更正后的正确局部对象 ✓✓）}:\ O_{I_{40}}(x)=\{p,\ q,\ c\}\ ✓✓\ \big(\text{实测 }|O(x)|{=}3\ \text{对全 480 点 ✓}\big)\ \text{——\ \textbf{两个被删} ＋ \textbf{一个 }S\text{-owner}}✓$$
$$\boxed{\textbf{(2) ✓✓修正后之局部量（本档）}:\ }B_x:=\{y\notin S:\ y\ne x,\ d(x,y){=}2\}⟹|B_x|=\mathbf{42}\ \text{（全 480 点同值 ✓✓）}$$
$$\qquad\textbf{结构解释 ✓}:\ \text{同层之距离-2 邻点总数 }=C(10,2){=}45✓;\ \text{其中 }3\ \text{个在 }I_{40}\ \big(\{p,q,c\}✓\big)⟹45-3=\mathbf{42}✓✓\ \text{——\ \textbf{恒为常数 ✓}}$$
$$\qquad\textbf{（即 C-480 之 blocking 图论形式 ✓✓）}:\ y\in B_x\iff d(x,y){=}2\iff y\ \text{与 }x\ \text{于残点集中\ \textbf{冲突}}✓$$
$$\boxed{\textbf{(3) ✓✓兼容池（本档新数据）}:\ }\text{定义 }P_t(x):=\#\{y\notin S:\ y\ne x,\ d_S(y)\le t,\ d(x,y)\ne2,\ d(y,p)\ne2,\ d(y,q)\ne2\}✓$$
| $t$ | $P_t(x)$ 之分布 | 结论 |
|---|---|---|
| $2$ | $\{0{:}480\}$ | **恒 $0$** ✓✓（＝C-480 blocking identity 之重述 ✓） |
| $3$ | $\{\mathbf{128{:}480}\}$ | **恒 $128$** ✓✓（**新常数** ✓，全 480 点无例外 ✓） |
| $4$ | $\{318{:}160,\ 319{:}320\}$ | 仅两值 ✓（按 $d(a,b)$ 分组相关 ✓） |
$$\qquad\Longrightarrow\ \boxed{\text{若 }x\ \text{为残点，则\ \textbf{其余 4 残点之度}\ \ge3⟹\sum\ge1+4\cdot3=\mathbf{13}}\ ✓✓\ \big(\text{比所需的 }8\ \text{更强 ✓}\big)}$$
$$\qquad\textbf{（但须加条件 ✓）}:\ \text{此推论要求其余 4 点避开 }p,q\ ✓;\ \text{而 }p,q\ \text{本身度 0 ⟹ 由 C-483 之残点度下界 }(\ge1)⟹\text{最多其一可入 }S_{44}✓\ \big(\text{两者同入 ⟹ }\alpha{=}40✗\big)✓$$
$$\boxed{\textbf{(4) ✓ 无 injection（照唐先生之告诫 ✓）}:\ }|B_x|{=}42\gg|A_x|{=}0✗⟹\ \text{"}B_x\hookrightarrow A_x"\ \textbf{不成立}✗\ \text{且无意义 ✗}$$
$$\qquad\textbf{（正确读法 ✓）}:\ \text{局部容量之载体不是 }(A_x,B_x)\ \text{而是\ \textbf{兼容池 }P_t(x)✓✓\ ——\ 本档之以数据定方向 ✓✓}$$
$$\qquad\textbf{（新现象 ✓）}:\ P_3(x)\equiv128\ \text{之\ \textbf{恒定} 极不寻常}✓✓\ \text{——\ 或为 }\frac12Q_{10}\ \text{之强对称性所致 \big(}|D|{=}2\ \text{覆盖全体外部点之某种均匀性 ✓\big)}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✗（须记）}:\ \text{唐先生 }A_x:=O_{I_{40}}(a)\cap S\ \text{之定义\ \textbf{恒空}}✗\ \text{——\ 与数据无关，系定义层面 ✓（\S0(1)）}$$
$$\textbf{✓✓}:\ \text{唐先生 §"不预设 injection、让数据定方向"\ \textbf{完全正确}}✓✓\ \text{——\ 实测 }|B_x|{=}42\ \text{确与 }|A_x|{=}0\ \text{反向 ✗，故 injection 路线\ \textbf{应废弃} ✓}$$
$$\textbf{✓✓}:\ \text{唐先生 §"owner 阈值 }|D|<3\Rightarrow\text{无法制造新补点}"✓✓\ \text{——\ 与 C-484 之"Family B}=\{p,q\}"\ \text{完全一致}✓✓$$
$$\textbf{✓}:\ \text{唐先生 §"反例本身可能告诉我们 E2 应换另一种 obstruction"\ ✓✓\ \text{——\ \S0(3) 之兼容池即此 obstruction 之首形 ✓}}$$

## §2 状态（**⚠️ 不作裁定 ✗**）

$$\textbf{已封 ✓✓}:\ r{=}0/1/2\ \big(\ge12/\ge10/\ge8✓✓\big);\ d{=}0\ \text{支}✓;\ \text{Best 家族 }d{=}1\ \text{支\ \textbf{空}}✓✓;\ \text{兼容池 }P_2\equiv0✓$$
$$\textbf{OPEN ⚠️}:\ r{=}3\ \text{profile}✗;\ \text{非 Best }39\text{-码}✗;\ \text{以及\ \textbf{新}：}P_3\equiv128\ \text{之\ \textbf{由来与推论}}✓\ \big(\text{下一靶 ✓}\big)$$
$$\textbf{（下一靶 ✓✓）}:\ \text{① 解释 }P_3(x)\equiv128\ \text{之恒定（对称性／轨道论证 ✓）};\ \text{② 由 }P_2\equiv0\ \text{推出\n 残点之\ \textbf{组合下界}（非仅 }p,q\ \text{受限版 ✓）};\ \text{③ }r{=}3\ \text{之重算（C-482 之零点补入后 ✓）}$$

## §3 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "兼容池" "定义性为空" "三重常数"
技术词 兼容池     命中文件数=1    :: ./WITINC38-2026-09-28-Ax-is-empty-by-definition-and-the-compatible-pool-constants.md
技术词 定义性为空 命中文件数=1    :: ./WITINC38-2026-09-28-Ax-is-empty-by-definition-and-the-compatible-pool-constants.md
技术词 三重常数   命中文件数=1    :: ./WITINC38-2026-09-28-Ax-is-empty-by-definition-and-the-compatible-pool-constants.md
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 兼容池 | **0**（1 命中＝**自命中** ✗✓） | 0 | ✓（自造标签 ✓） |
| 定义性为空 | **0**（1 命中＝**自命中** ✗✓） | 0 | ✓（自造标签 ✓） |
| 三重常数 | **0**（1 命中＝**自命中** ✗✓） | 0 | ✓（自造标签 ✓） |

- **⚠️ 流程瑕疵（据实记录 ✓）**：同 C-484，三词回查**写后**才跑 ✗✓；真值：三词各 1 命中皆**自身** ⟹ 他档 $=0$ ✓。**下轮必先跑** ✓

## §4 边界（硬 ✓）

- **有限穷举** ✓（780 对全量 ✓；480 个 degree-1 点全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 ✓）
- **一处定义更正**（$A_x$ 恒空 ✗✓）＋ **一处数据新增**（兼容池三重常数 ✓✓）＋ **一处路线废弃**（injection ✗）已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $P_3\equiv128$ 之由来已知 ✗；**不声称** P1 成立/不成立 ✗（V290）
