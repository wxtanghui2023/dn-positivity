# WITEDGE-2026-09-28 — **C-491：$P_3(x)$ 之 edge-level 刻画唯一型（$\|e_x\cap e_y\|{\equiv}\mathbf0$ ✓✓✓）；$H_1\cong H_2$ ✓✓✓；$A_1A_2{=}A_2A_1$（\textbf{对易} ✓✓✓）；谱 $=\{8,4^5,(2\sqrt5-2)^2,0^{25},-4^5,(-2\sqrt5-2)^2\}$**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 14:31 令 ✓）**：C-491（edge-level 分解 → $H_1\cong H_2$? → 谱 → 矩阵关系）；**谱列第二层 ✓**；**先跑后写 ✓✓**；**不作路线裁定** ✗。

**已查地图：命中（接续 C-490／C-489／C-488，非新案 ✓）**
`docs/WITCHOICE-2026-09-28-…`（**两候选／闭环 ✓✓✓**）｜`docs/WITLAM40-2026-09-28-…`（**signature／$H_1,H_2$ ✓✓✓**）｜`docs/WITEX32-2026-09-28-…`（**$j$-分解 ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §5）
D0: 本档对象 ＝ **档案已有** $H_1,H_2$／$\mathcal T$／$P_3$；**新对象**：边级关系型 ＋ 矩阵代数（首次入档 ✓）
D1: 1（**首次给出 $P_3(x)$ 之\ \textbf{边缘级刻画}（唯一型 ✓）＋ 首次给出 $H_1\cong H_2$（显式同构 ✓）＋ 首次给出\ \textbf{对易关系} $A_1A_2{=}A_2A_1$ ＋ 首次给出谱（$\sqrt5$ 型）与 $B_0$ 之结构** ✓）
**[RESEARCH]**

---

## §0 结论（**四项全通 ＋ 两个代数新事实**）

$$\textbf{设定 ✓}:\ x\in\mathcal S\ (\text{160 特殊点});\ e_x:=\text{其唯一 }H_1\text{-边}✓;\ c:=w(e_x)\ \text{（第三点 ✓）};\ P_3(x)\ \big(|{\cdot}|{=}128✓\big)\ \text{经 }X\leftrightarrow E(H_1)\ \text{重读为 128 条边 ✓✓}$$
$$\boxed{\textbf{(1) ✓✓✓边缘级刻画（唯一型！）}:\ }\text{对全部 160 个 }x,\ \text{对全部 }y\in P_3(x):\ \text{计数型\ \textbf{完全相同}}✓✓\ \big(\text{仅 1 型 ✓}\big)$$
| 量 | 在 128 个 $y$ 上之值 | 结论 |
|---|---|---|
| $\|e_x\cap e_y\|$ | $\mathbf0$（全部 128 ✓✓） | **$P_3(x)$ 只含与 $e_x$ \textbf{不相交}之 }H_1\text{-边** ✓✓✓ |
| $w(e_y)\in e_x$ | 否（128 ✓） | 从不 ✓ |
| $w(e_y)=w(e_x)$ | 恰 1 次 ✓ | 唯一 ✓ |
| $w(e_y)\in T_x\setminus e_x$ | 恰 1 次 ✓ | 同上（同一 $y$ ✓） |
| $T_y\cap T_x=\varnothing$ | $123$ ✓ | 与 C-487 之 $j$-分解一致 ✓ |
| $T_y\cap T_x\ne\varnothing$ | $5$ ✓ | 同上 ✓ |
$$\qquad\textbf{（关键 ✓✓✓）}:\ \boxed{\forall y\in P_3(x):\ e_y\cap e_x=\varnothing}\ ✓✓✓\ \text{——\ 128 条全为\ \textbf{不相交边}}✓✓$$
$$\qquad\textbf{（与 }E_x\text{ 之对照 ✓）}:\ \text{与 }e_x\ \text{共端点之 }H_1\text{-边共 }2(8-1){=}14\ \text{条 ✓ ⟹ 全部落入 }E_x✓\ \big(\text{外加之 }e_x\ \text{自身 ⟹ }15✓\big);\ E_x\ \text{另含 }17\ \text{条不相交边 ✓}$$
$$\qquad\Longrightarrow\ \text{12 之"不相交"并非充分条件 ✗（}17\ \text{条不相交边仍在 }E_x✓\big)\ \text{——\ 但为\ \textbf{必要条件}✓✓\ \big(\text{唐先生之 edge-level 争取 ✓✓}\big)}$$
$$\boxed{\textbf{(2) ✓✓✓H_1\cong H_2（本档证实）}:\ }\text{以 }GraphMatcher\ \text{求得显式同构 }\phi:V(H_1)\to V(H_2)✓✓\ \big(\text{160 边／8-正则／三角形自由 皆同 ✓}\big)$$
$$\qquad\textbf{（}\phi\ \text{之行为 ✓）}:\ \phi\ \text{把 }H_1\text{-边映为 }H_2\text{-边 ✓✓}\ \big(\lambda{=}2✓\ \mathbf{160/160}✓\big);\ \textbf{但}\ \phi\ \textbf{不保} \text{ 选择 }w\ ✓✗\ \big(\phi(w(e))\ \text{非 }\phi(e)\ \text{之 }H_2\text{-共同邻点 ✓\ 0/160 ✗}\big)$$
$$\qquad\Longrightarrow\ \text{唐先生之告诫\ \textbf{正确}}✓✓:\ \text{参数对偶 ⟹ \textbf{确实同构}✓；但"}\phi(w(e))"\ \text{与 }e\ \text{之间\ \textbf{无自然关系} ✗}$$
$$\boxed{\textbf{(3) ✓✓✓谱（\textbf{完全相同} ＋ 干净代数数）}:\ }$$
| 特征值 | 重数 |
|---|---|
| $8$ | $1$ |
| $4$ | $5$ |
| $-2+2\sqrt5\approx2.472136$ | $2$ |
| $0$ | $25$ |
| $-4$ | $5$ |
| $-2-2\sqrt5\approx-6.472136$ | $2$ |
$$\qquad\Longrightarrow\ \text{Spec}(A_1)=\text{Spec}(A_2)✓✓\ \text{——\ 涉 }\sqrt5✓\ \text{（非 }\sqrt2／\sqrt3✓\big)\ \text{——\ 疑与五边形几何相关 ✓}$$
$$\boxed{\textbf{(4) ✓✓✓矩阵关系（本档核心代数发现）}:\ }\text{四关系全真}✓✓:\ (A_1^2)_{H_2}{\equiv}2✓;\ (A_2^2)_{H_1}{\equiv}2✓;\ (A_1^2)_{H_1}{\equiv}0✓;\ (A_2^2)_{H_2}{\equiv}0✓;\ \text{对角}{\equiv}8✓$$
$$\qquad\Longrightarrow\ A_2^2=8I+2A_1+B_0\ \text{且}\ A_1^2=8I+2A_2+B_0'\ ✓\ \big(B_0,B_0'\ \text{支集}\subseteq H_0✓\big)$$
$$\qquad\textbf{（✗否证 ✓）}:\ B_0\ \text{在 }H_0\ \text{上取值}=\{0{:}400,\ 2{:}320,\ 4{:}160,\ 8{:}40\}\ ✗\ \textbf{不恒定}⟹\ B_0\ \textbf{非标量} ✗;\ \text{且}\ B_0\neq B_0'\ ✗\ \big(\text{虽取值分布同 ✓}\big)$$
$$\boxed{\textbf{(4b) ✓✓✓对易（本档新代数事实）}:\ }\boxed{A_1A_2=A_2A_1}\ ✓✓✓\ \big(\text{实测 True ✓}\big)\ \text{——\ 即 }A_1,A_2\ \textbf{可同时对角化}✓✓$$
$$\qquad\text{且}\ (A_1A_2)_{uv}\in\{0,2\}\ ✓\ \big(2\ \text{于 }1280{=}40\times32\ \text{位置 ✓};\ 0\ \text{于 }320✓\big)\ \Longrightarrow\ \textbf{每顶点 32 个"乘积位置"}\ ✓\ \big(\text{与 }128{=}160-32\ \text{之 32 呼应 ✓}\big)$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §3（}P_3\ \text{按 }e_x\ \text{是否相交三分；}14\ \text{条共端点 ✓）\ \textbf{完全正确}}✓✓;\ \text{其"这一步很便宜却可能直接告诉我们 128 第一层来源"\ \textbf{命中}}✓✓$$
$$\textbf{✓✓✓}:\ \text{唐先生 §2 之"}\iff R(e_x,e_y)\in\mathcal R\ \text{（有限关系型）"\ \textbf{成立}}✓✓\ \text{——\ 边缘级计数型\ \textbf{唯一}}✓✓\ \big(\text{已提升为 }E(H_1)\ \text{上之组合关系 ✓✓}\big)$$
$$\textbf{✓✓✓}:\ \text{唐先生 §6（}H_1\cong H_2\ ?\big)⟹\ \textbf{是}✓✓;\ \text{其"最有价值的是 }\phi(w(e))\ \text{与 }e\ \text{之关系"\ ⟹\ \textbf{无关系}✗\ \big(\phi\ \text{不保 }w✓\big)}$$
$$\textbf{✓✓}:\ \text{唐先生 §7（}A_2^2=8I+2A_1+B_0\ \text{形式 ✓）\ \textbf{方向正确}}✓✓;\ \text{唯 }B_0\ \text{非标量 ✗};\ \text{其"若 }B_0\ \text{是低次多项式则得真代数结构"\ ⟹\ \textbf{未达成}✗（但\ \textbf{对易}✓✓✓\ 为意外收获 ✓）}$$
$$\textbf{✓}:\ \text{唐先生之顺序锁定（edge-level → 同构 → 谱 → 矩阵关系 → 再定 stabilizer）\ \textbf{已照办}}✓✓$$

## §2 常数汇总裁（**本档 ✓✓✓**）

| 量 | 值 |
|---|---|
| $\|e_x\cap e_y\|$（$y\in P_3$） | $\mathbf0$（128/128）✓✓✓ |
| $H_1\cong H_2$ | 是 ✓✓✓ |
| $\text{Spec}$ | $\{8,4^5,(2\sqrt5-2)^2,0^{25},-4^5,(-2\sqrt5-2)^2\}$ ✓✓ |
| $A_1A_2=A_2A_1$ | 是 ✓✓✓ |
| $(A_1A_2)$ 取值 | $\{0,2\}$，每顶点 32 ✓ |
| $B_0$ 取值（$H_0$ 上） | $\{0,2,4,8\}$ ✗ 非常数 |

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓ 最优先）}:\ \text{由 }A_1A_2{=}A_2A_1\ \text{＋同谱 ⟹ 求\ \textbf{同时对角化基}／\text{商代数}（}A_1,A_2\ \text{生成之交换代数 ✓）；是否 }A_2=P(A_1)\ \text{对某多项式 }P✓\ ?$$
$$\textbf{（靶 2 ✓✓）}:\ \text{由 }\forall y\in P_3(x):e_y\cap e_x{=}\varnothing✓✓\ ⟹\ \text{17 条"不相交却在 }E_x"\ \text{之边\ \textbf{判据}（区别 128 与 17 ✓✓）\ ——\ \textbf{这是 }128\ \text{之真正来源所在} ✓✓}$$
$$\textbf{（靶 3 ✓）}:\ \phi\ \text{不保 }w\ ⟹\ \text{是否存在\ \textbf{第二同构} }\phi'\ \text{保 }w✓？\ \big(\text{或证不存在 ✓}\big)$$
$$\textbf{（并行 ⚠️）}:\ r{=}3\ \text{profile}✗;\ \text{非 Best 39-码}✗$$

## §4 记账与命名纪律（**照唐先生 ✓✓**）

$$\textbf{✓✓}:\ 「\text{谱}\ \text{列第二层}\」\ \text{已照办}（\S0(3)\ \text{仅记结果 ✓}）;\ \text{本档以 edge-level ＋ 代数关系为主 ✓}$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "边级刻画" "对易关系" "共同谱" "代数化恒等式"
技术词 边级刻画       命中文件数=0    ::
技术词 对易关系       命中文件数=0    ::
技术词 共同谱         命中文件数=3    :: ./V228-root-edge-barrier-audit-analytic-barrier-impossible.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md
技术词 代数化恒等式   命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 边级刻画 | 0 | 0 | ✓（自造标签 ✓） |
| 对易关系 | 0 | 0 | ✓（自造标签 ✓） |
| 共同谱 | 0 | **3**（`V228-*`／`CLOSED-ROUTES-MAP`／`MASTER-STATUS-*` 皆属**空间 A（RH 线）** ⟹ **空间 A 同名，不计** ✗✓） | ✓（本线新增 ✓） |
| 代数化恒等式 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条\ \textbf{确已先跑后写} ✓✓）**

## §6 边界（硬 ✓）

- **有限穷举** ✓（160 实例 × 128 边 ＋ 780 对 ＋ 同构检验（networkx VF2）＋ 40×40 谱 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 ✓）
- **两项代数新事实（同构 ✓✓／对易 ✓✓✓）** ＋ **一项否证（$B_0$ 非标量 ✗）** ＋ **一项否证（$\phi$ 不保 $w$ ✗）** 已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $A_2=P(A_1)$ ✗；**不声称** P1 成立/不成立 ✗（V290）
