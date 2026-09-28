# WITCHOICE-2026-09-28 — **C-490：$\mathcal T\cong E(H_1)$ ✓✓；$|W_e|\equiv2$ 且 $w(e)\in W_e$ ✓✓；$\boxed{r_w\equiv\mathbf4,\ r_{\bar w}\equiv\mathbf4,\ r_w{+}r_{\bar w}\equiv\mathbf8{=}d_{H_1}{=}d_{H_2}}$ ✓✓✓（闭环）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 14:28 令 ✓）**：C-490（$W_e$ ／ 实际选择 $w(e)$ ／ 未选候选 $\bar w$ ／ 边对关系）；**先跑后写 ✓✓**；**不作路线裁定** ✗。

**已查地图：命中（接续 C-489／C-488／C-487，非新案 ✓）**
`docs/WITLAM40-2026-09-28-…`（**signature／$H_1,H_2$／交叉正则 ✓✓✓**）｜`docs/WITEX32-2026-09-28-…`（**$j$-分解／$n_i$ ✓✓✓**）｜`docs/WITMUCONST-2026-09-28-…`（**四层／自然双射 ✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $H_1$／三元组／$\lambda$；**新对象**：选择映射 $w(e)$ 首次入档 ✓
D1: 1（**首次证明 $\mathcal T\cong E(H_1)$（双射）＋ 首次给出 $|W_e|\equiv2$ 与 $w(e)\in W_e$ ＋ 首次给出\ \textbf{闭环恒等式} $r_w{\equiv}4,r_{\bar w}{\equiv}4,r_w{+}r_{\bar w}{\equiv}8$ ＋ 首次给出 $H_1$-边对之 $H_2$-关系表** ✓）
**[RESEARCH]**

---

## §0 结论（**四项全中 ＋ 闭环成立**）

$$\textbf{设定 ✓}:\ 40\ \text{码字};\ K_{40}{=}H_0\sqcup H_1\sqcup H_2\ (460,160,160)✓;\ H_1,H_2\ \text{皆 8-正则、三角形自由、交叉正则}\equiv2✓\ \big(\text{C-489 ✓✓}\big)$$
$$\qquad\text{每个 triple }T\ \text{之 signature }(1,2,2)\ ⟹\ \text{恰一个 }H_1\text{-边 ＋ 两个 }H_2\text{-边}✓✓\ \big(\text{C-489 ✓}\big)$$
$$\boxed{\textbf{(0) ✓✓✓\mathcal T\cong E(H_1)（双射）}:\ }\text{160 个 triple 与 160 条 }H_1\text{-边\ \textbf{一一对应}}\ ✓✓\ \big(\text{实测}: |\mathcal T|{=}|E(H_1)|{=}\mathbf{160}✓;\ \text{且}\ \lambda{\equiv}1\ \text{之边只属一个 triple ⟹ \textbf{单射}}✓✓\big)$$
$$\qquad\Longrightarrow\ \boxed{X\ \longleftrightarrow\ \mathcal T\ \longleftrightarrow\ E(H_1)}\ ✓✓\ \text{——\ 唐先生之"再编码"判断\ \textbf{成立}}✓✓$$
$$\qquad\textbf{（含义 ✓✓）}:\ \text{每特殊点 }x\ \text{可视为 }H_1\ \text{的一条边};\ \text{故 }P_3(x)\ \text{可重读为\ \textbf{128 条 }H_1\text{-边之子集}}\ ✓✓\ \big(\text{唐先生 §最后之展望 ✓}\big)$$
$$\boxed{\textbf{(1) ✓✓✓两候选结构}:\ }\forall e{=}\{u,v\}\in E(H_1):\ W_e:=N_{H_2}(u)\cap N_{H_2}(v)⟹\boxed{|W_e|\equiv\mathbf2}\ ✓✓\ \big(160/160✓\big)$$
$$\qquad\text{实际 triple 给出 }w(e)\in W_e\ ✓✓\ \big(\mathbf{160/160}\ \text{True}✓✓\big)\ \text{——\ 即"两候选 ⟹ 实选一"之结构\ \textbf{完全成立}}✓✓$$
$$\boxed{\textbf{(2) ✓✓✓闭环恒等式（唐先生之预测，本档证实）}:\ }\forall v\in I_{40}:\ \boxed{r_w(v)=\mathbf4,\qquad r_{\bar w}(v)=\mathbf4}\ ✓✓\ \big(40/40\ \text{各 ✓✓}\big);\quad \sum r_w{=}\sum r_{\bar w}{=}160✓✓$$
$$\qquad\Longrightarrow\ \boxed{r_w(v)+r_{\bar w}(v)\equiv\mathbf8\ =\ d_{H_1}(v)\ =\ d_{H_2}(v)}\ ✓✓✓\ \text{——\ 唐先生之"4+4=8 闭环"\ \textbf{精确成立}}✓✓\ \big(\text{极强结构证据 ✓✓}\big)$$
$$\qquad\textbf{（读法 ✓✓）}:\ \text{每码字有 8 个"第三点角色"（4 次被选中 ＋ 4 次未选中），恰等于其 }H_1／H_2\ \text{度 ✓}$$
$$\boxed{\textbf{(3) ⚠️H_1-边对之 }H_2\textbf{-关系表（不完全由 }H_1\textbf{ 关系决定）}:\ }$$
| $e,e'$ 在 $H_1$ 中之关系 | $d_{H_2}(w(e),w(e')){=}0$ | ${=}1$ | ${=}2$ | 合计 |
|---|---|---|---|---|
| 共端点 | $480$ | $640$ | $\mathbf0$ | $1120$ ✓ |
| 距离 2 | $3920$ | $1280$ | $1280$ | $6480$ ✓ |
| 不相交 | $3200$ | $640$ | $1280$ | $5120$ ✓ |
$$\qquad\text{（合计 }12720{=}\binom{160}2✓✓\big)\ \textbf{（观察 ✓）}:\ \text{共端点者\ \textbf{绝不}处 }H_2\text{-距离 2}✓\ \big(\text{0 例 ✓}\big);\ \text{但同关系下计数\ \textbf{不恒定} ✗}$$
$$\qquad\Longrightarrow\ \text{选择映射 }w\ \textbf{不能}仅由 }H_1\ \text{关系重建 ✗\ ——\ 唐先生之"能否由 }H_1\ \text{单独重建三元组系"\ ⟹\ \textbf{否}（需 }H_2\ \text{或更多数据）✗$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生之"每个 triple ＝ 一条 }H_1\text{-边 ＋ 一个共同 }H_2\text{-邻点"\ \textbf{完全正确}}✓✓$$
$$\textbf{✓✓✓}:\ \text{其 }r_w(v){=}4\ \text{与 }r_{\bar w}(v){=}4\ \text{之双预测\ \textbf{双双击中}}✓✓\ \big(\text{含 }4{+}4{=}8{=}d\ \text{之闭环 ✓}\big)$$
$$\textbf{✓✓}:\ \text{其 §①（}\sum r_w{=}160\big)、§③（比较 }w(e),w(e')\big)\ \text{之方向\ \textbf{正确} ✓};\ \text{唯 §③之"少数固定值"\ ⟹\ \textbf{不成立}✗\ \big(\S0(3)\big)$$
$$\textbf{✓✓}:\ \text{其"降维后再编码"之整体规划（}X\leftrightarrow\mathcal T\leftrightarrow E(H_1)\big)\ \textbf{成立}✓✓\ \text{——\ 且 }P_3(x)\ \text{之 128 重读为边子集\ \textbf{已可正确定义}}✓✓$$

## §2 常数汇总裁（**本档 ✓✓✓**）

| 量 | 值 | 恒定？ |
|---|---|---|
| $\|\mathcal T\|$ / $\|E(H_1)\|$ | $160$ / $160$ | 双射 ✓✓ |
| $\|W_e\|$ | $2$ | ✓✓ |
| $w(e)\in W_e$ | 是 | ✓✓ |
| $r_w(v)$ | $\mathbf4$ | ✓✓ |
| $r_{\bar w}(v)$ | $\mathbf4$ | ✓✓ |
| $r_w{+}r_{\bar w}$ | $\mathbf8{=}d$ | ✓✓✓ |
| 共端点 ⟹ $d_{H_2}(w,w'){\ne}2$ | 0 例 | ✓ |
| 同关系下 $d_{H_2}$ 计数 | 不恒定 | ✗ |

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓ 最优先）}:\ \text{将 }P_3(x)\subset X\ \text{经 }X\leftrightarrow E(H_1)\ \text{重读为\ \textbf{128 条边之子集}}\ ✓✓\ \text{并求其\ \textbf{边关系刻画}（是否 }d_{H_1}\ \text{／}H_2\text{-共同邻点条件 ✓？）}$$
$$\textbf{（靶 2 ✓✓）}:\ \text{由 }r_w{\equiv}4,r_{\bar w}{\equiv}4\ ⟹\ \text{是否 }w\ \text{映射本身诱导一个\ \textbf{8-正则结构}（与 }H_1,H_2\ \text{之关系 ✓）};\ H_1\cong H_2\ ?✓$$
$$\textbf{（靶 3 ✓）}:\ H_1,H_2\ \text{之\ \textbf{谱}（少数整数 ✓？）；三角形自由 ⟹ 谱之界 ✓}$$
$$\textbf{（并行 ⚠️）}:\ r{=}3\ \text{profile}✗;\ \text{非 Best 39-码}✗$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "候选对选择" "第三点角色" "闭环恒等式" "边-三元组双射"
技术词 候选对选择   命中文件数=0    ::
技术词 第三点角色   命中文件数=0    ::
技术词 闭环恒等式   命中文件数=0    ::
技术词 边-三元组双射 命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 候选对选择 | 0 | 0 | ✓（照唐先生 §命名 ✓） |
| 第三点角色 | 0 | 0 | ✓（照唐先生 §② ✓） |
| 闭环恒等式 | 0 | 0 | ✓（自造标签 ✓） |
| 边-三元组双射 | 0 | 0 | ✓（照唐先生 §0 ✓） |

- **（本条\ \textbf{确已先跑后写} ✓✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（160 三元组 ＋ 160 边 ＋ $\binom{160}2$ 边对全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 ✓）
- **四项全中 ✓✓✓**＋ **一项否证（不能仅由 $H_1$ 重建 ✗）** 已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $H_1\cong H_2$ ✗；**不声称** P1 成立/不成立 ✗（V290）
