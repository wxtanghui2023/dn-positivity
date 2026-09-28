# WITMIX-2026-09-28 — **C-501：旧 fallback 关闭 ✓（5 个 mixed OrbType）＋ ★★机制找到：\textbf{轨道型骨架 ＋ 容量余量} $\delta{=}C(O){-}(k_1{+}k_2)$，且 $E\Rightarrow\delta\le1$ ✓✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 15:07 令 ✓）**：(A) 关旧 fallback；(B) 列 mixed OrbType；(C) 其内 $(k_1,k_2)$ 分叉；(D) 容量余量；**不作路线裁定** ✗。

**已查地图：命中（接续 C-500／C-499／C-498，非新案 ✓）**
`docs/WITSTAB-2026-09-28-…`（**(A)(B)(C) 全否 ✗✗✗**）｜`docs/WITORB-2026-09-28-…`（**三关全过 ✓✓✓**）｜`docs/WITENV-2026-09-28-…`（**细环境量砍 ✗**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §4）
D0: 本档对象 ＝ **档案已有** $\Pi$/OrbType/容量（无新数学对象 ✓）
D1: 1（**首次关旧 fallback（5 mixed OrbType 具体列出）＋ 首次得\ \textbf{每个 mixed 内 }$(k_1,k_2)$\textbf{ 完全分隔} ✓✓＋ 首次得\ \textbf{容量余量} $\delta$ 与 $E\Rightarrow\delta\le1$ ✓✓＋ 首次给出\ \textbf{轨道骨架＋容量余量}之确切机制形式** ✓）
**[RESEARCH]**

---

## §0 结论（**机制的形式已定 ✓✓**）

$$\textbf{记号 ✓}:\ O(y):=\text{OrbType（本档用\ \textbf{全 16 位平面等式型}之 }G\text{-轨道，较 C-499 之逐 entry 规范\ \textbf{更细}：}\mathbf{78}\ \text{类 vs }46✓\big);\ C(O):=\max_{y\in O}(k_1{+}k_2)✓;\ \delta(y):=C(O)-(k_1{+}k_2)✓$$
$$\boxed{\textbf{(A) ✓✓旧 fallback 正式关闭}:\ }\text{OrbType 总数}=\mathbf{78};\ \textbf{mixed OrbType}=\mathbf5\ ✓✓\ \big(\text{同型内 }E\ \text{与 }P_3\ \text{并存}\big)$$
$$\qquad\Longrightarrow\ \boxed{\text{OrbType-only 精确刻画 }E\ \textbf{不可能}}\ ✓✓\ \text{——\ 无论取单 }O\text{、}O_1\lor O_2\ \text{或任意子集 }\mathcal S ✗\ \big(\text{照唐先生 §9-A ✓}\big)$$
$$\boxed{\textbf{(B) ✓✓5 个 mixed OrbType 及其内部分叉（本档核心）}:\ }$$
| mixed $O$ | 内容 |
|---|---|
| $O_1$ | $(0,1){:}E\,320$ ／ $(0,2){:}P_3\,320$ |
| $O_2$ | $(0,0){:}P_3\,320$ ／ $(1,3){:}E\,320$ |
| $O_3$ | $(0,3){:}E\,160$ ／ $(1,0){:}P_3\,160$ |
| $O_4$ | $(0,3){:}E\,160$ ／ $(1,0){:}P_3\,160$ |
| $O_5$ | $(1,2){:}P_3\,320$ ／ $(1,3){:}E\,320$ |
$$\qquad\Longrightarrow\ \boxed{\text{每个 mixed }O\ \text{内，}(k_1,k_2)\ \textbf{完全分隔} }E/P_3\ ✓✓✓\ \text{——\ 无例外 ✓}$$
$$\qquad\textbf{（mixed 之量 ✓）}:\ E{=}1280,\ P_3{=}1280\ \text{在 mixed 内}\ ✓;\ \text{余 }E{=}1440\ \text{已在\ \textbf{pure} }O\ \text{内被单 }O\ \text{判定 ✓}$$
$$\boxed{\textbf{(C) ✓✓分叉关系（照唐先生 §9-C）}:\ }\text{在 mixed 内，}k_1{+}k_2\ \text{／}\ k_2{-}k_1\ \text{／}\ 3{-}k_2\ \text{皆可分隔 ✓✓（因两侧 }(k_1,k_2)\ \textbf{不相交} ✓）；\ 而\ \mathbf{k_2{=}3\ 单独\ \textbf{不}分隔} ✗✓$$
$$\qquad\Longrightarrow\ \boxed{k_2{=}3\ \text{只解释 }8/17\ ✓✓\ \text{——\ 余 }9/17\ \text{须由\ \textbf{容量余量}解释 ✓✓}}\ \big(\text{照唐先生 §2 ✓✓}\big)$$
$$\boxed{\textbf{(D) ✓✓✓容量余量（照唐先生 §7 之猜想，\ \textbf{成立}}）:\ }\delta(y)=C(O)-(k_1{+}k_2)\ \text{之分布}:$$
| 标签 | $\delta{=}0$ | $\delta{=}1$ | $\delta{=}2$ | $\delta{=}4$ |
|---|---|---|---|---|
| $E$ | $2400$ | $320$ | $\mathbf0$ | $\mathbf0$ |
| $P_3$ | $16640$ | $2880$ | $640$ | $320$ |
$$\qquad\Longrightarrow\ \boxed{E\ \Longrightarrow\ \delta\le1}\ ✓✓\ \big(\text{全部 }2720\ \text{之 }E\ \text{皆}\ \delta\in\{0,1\}✓✓\ \text{——\ \textbf{无例外}}\big)$$
$$\qquad\textbf{（但非充分 ✗）}:\ P_3\ \text{亦大量取 }\delta{=}0\ (16640)\ ✓ \Longrightarrow\ \delta\ \text{单独\ \textbf{不}判 }E ✗$$
$$\qquad\Longrightarrow\ \boxed{\text{确切机制形式}:\ \big(O(y),\ \delta(y)\big)\ \text{——\ \textbf{轨道型骨架＋容量余量}}}\ ✓✓\ \big(\text{因同 }O\ \text{内 }\delta\ \text{与 }(k_1,k_2)\ \text{一一对应 ✓✓}\big)$$
$$\qquad\textbf{（读法 ✓✓）}:\ E\ \text{＝\ \textbf{近饱和（}\delta\le1\text{）之配置}\ ✓✓\ \text{——\ 即 }E\ \text{几乎吃满其轨道型之容量 ✓✓\ \big(照唐先生 §7 之"容量碰撞" ✓✓}\big)}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §1（"}\operatorname{OrbType}\ \text{单独 78.62\% ⟹ 存在 mixed ⟹ OrbType-only 精确刻画不可能"\ ）\ \textbf{完全正确}}✓✓✓\ \text{——\ 本档证实（5 mixed ✓）}$$
$$\textbf{✓✓✓}:\ \text{唐先生 §2（}17{=}8{+}9\text{，}k_2{=}3\ \text{只解释 }8/17\text{）\ \textbf{完全正确}\ ✓✓✓\ （余 9 须由容量解释 ✓✓）}$$
$$\textbf{✓✓✓}:\ \text{其 §7 之猜想（"}\delta=C(O)-k_1-k_2\ \text{；若 }E\ \text{对应固定小值则即所求机制"\ ）\ \textbf{成立}}✓✓✓\ \text{——\ }E\Rightarrow\delta\le1✓✓$$
$$\textbf{✓✓}:\ \text{其 §3–§4 之"非对齐/相对排列"直觉\ \textbf{部分正确}}✓✓\ \text{——\ 但机制经实测为\ \textbf{容量余量}（较之更简 ✓✓）}$$
$$\textbf{✗（须记）}:\ \text{其 §5 之"轨道间等式图 }H_\Pi\text{"\ \textbf{未采纳}}✗\ \text{——\ 因 (D) 已给出更简之机制 ✓（避免换表示 ✗✓）}$$
$$\textbf{✓（更正）}:\ \text{C-499 之 OrbType 计数 }\mathbf{46}\ \text{系\ \textbf{逐 entry} 规范 ⟹ 本档改用\ \textbf{全 16 位}规范得 }\mathbf{78}\ \text{类 ✓（更细 ✓）——\ C-499 之三关结论\ \textbf{不受影响} ✓（其留出门已过 ✓）}$$

## §2 汇总裁（**✓✓✓**）

| 项 | 值 |
|---|---|
| OrbType 数（全 16 位规范） | $78$（C-499 之 46 为更粗者 ✓） |
| mixed OrbType 数 | $\mathbf5$ ✓✓ |
| mixed 内之分隔 | $(k_1,k_2)$ **完全**分隔 ✓✓✓ |
| $k_2{=}3$ 单独 | ✗ 不分隔（只占 8/17 ✓） |
| $E\Rightarrow\delta\le1$ | ✓✓✓（2720/2720 无例外 ✓） |
| $\delta$ 单独判 $E$ | ✗（$P_3$ 亦取 $\delta{=}0$ ✓） |
| 确切机制 | $\big(O,\delta\big)$ ＝ **轨道骨架＋容量余量** ✓✓ |

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓最优先）}:\ \text{把 }\delta\le1\ \text{之\ \textbf{机制}写成命题}:\ \boxed{\text{为何 }E\ \text{必近饱和？}}\ \text{——\ 疑与 }k_2\ \text{之跨色对之\ \textbf{必消耗性}有关 ✓（照 C-436 之跨色 2-覆盖 ✓）}$$
$$\textbf{（靶 2 ✓✓）}:\ \text{五个 mixed }O\ \text{之几何解释（各对应何局部构型 ✓）——\ 可否总结为\ \textbf{少数几条} ⟹ 接桥④ ✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{若 }\#\{y:\delta\le1\}\ \text{可由结构给出 ⟹ }\boxed{\#\{y\}\stackrel{?}{=}17}\ ✓\ \big(\text{照唐先生 §10 ✓}\big)$$
$$\textbf{（转④条件 ✓，照唐先生）}:\ \text{若 mixed 内之余量亦无统一关系 ⟹ ③ 贡献已尽 ⟹ 转 ④（三重 }N_2\ \text{轨道占据 模式 ✓）}$$

## §4 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "容量余量" "轨道骨架" "混合轨道型"
技术词 容量余量   命中文件数=0  ::
技术词 轨道骨架   命中文件数=0  ::
技术词 混合轨道型 命中文件数=0  ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 容量余量 | 0 | 0 | ✓（照唐先生 §7 ✓） |
| 轨道骨架 | 0 | 0 | ✓（照唐先生 §"骨架＋填充" ✓） |
| 混合轨道型 | 0 | 0 | ✓（照唐先生 §9-B ✓） |

- **（本条\ \textbf{确已先跑后写} ✓✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（23200 对 ＋ 78 类 ＋ mixed 分析 ＋ $\delta$ 分布 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项关闭（旧 fallback ✗）** ＋ **一项机制（轨道骨架＋容量余量 ✓✓✓）** ＋ **一项更正（OrbType 计数 46→78 ✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $\delta\le1$ 之机制已证 ✗（仅实证 ✓）；**不声称** $145{-}17{=}128$ 已证 ✗（V290）
