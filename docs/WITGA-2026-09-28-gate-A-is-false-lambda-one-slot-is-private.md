# WITGA-2026-09-28 — **C-517：Gate A 答案 ＝ \textbf{否}（$\lambda{=}1$ 槽\ \textbf{从不}属 $E(w^\ast)$，0/640）✓✓；新刚性事实 $\pi(w^\ast)\cap\{\lambda{=}1\ \text{槽}\}=\varnothing$ ✓✓ —— 唐先生 §4 之\ \textbf{第二种情形}为实**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 15:50 §10-Gate A ✓）**：只查"唯一 $\lambda{=}1$ 槽是否必属 $E(w^\ast)$"；**不作路线裁定** ✗。

**已查地图：命中（接续 C-516／C-515／C-512，非新案 ✓）**：`WITGATE-…`／`WITCAPB-…`／`WITTYPE-…`
D0: 本档对象 ＝ **档案已有**（$\lambda$/$\pi$/$E(w)$；无新数学对象 ✓）
D1: 1（**首次判定 Gate A 为\ \textbf{否}（0/640）：唯一 $\lambda{=}1$ 槽从不属 $E(w^\ast)$ ＋ 首次得\ \textbf{刚性事实} $\pi(w^\ast)\cap\{\lambda{=}1\}=\varnothing$ ＋ 首次给出 $(\lambda{=}1\ \text{槽},\pi)$ 之\ \textbf{八格联合分布}** ✓）
**[RESEARCH]**

---

## §0 结论（**★Gate A ＝ 否 ✓✓**）

$$\textbf{设定 ✓}:\ \text{四正实例 }640;\quad \text{唯一 }\lambda{=}1\ \text{槽之序号 }i_{\rm one}\in\{0,1,2,3\};\quad \pi(w^\ast){=}\{ij:w^\ast\in W_{ij}\}\ ✓$$
$$\boxed{\textbf{(1) ✗✓Gate A\ \textbf{为否}}:\ }i_{\rm one}\in\pi(w^\ast)\ \text{之实例}=\mathbf0\ /\ 640\ ✓✓\ \text{——\ }\textbf{从不成立}✗✓$$
$$\qquad\Longrightarrow\ \text{唯一 }\lambda{=}1\ \text{槽\ \textbf{恒为私有槽}}（\text{其 }|W|{=}1\ \text{之点不是 }w^\ast\big)\ ✓✓$$
$$\qquad\Longrightarrow\ \textbf{（故唐先生 §4 之"若成立则 }W_{11}{=}\{w^\ast\}\text{"\ 之规范化\ \textbf{不能用} ✗✓）}$$
$$\boxed{\textbf{(2) ✓✓★新刚性事实}:\ }\boxed{\pi(w^\ast)\cap\{i_{\rm one}\}=\varnothing}\ ✓✓\ \big(640/640✓\big)\ \text{——\ 双支撑对\ \textbf{恒避开}\ }\lambda{=}1\ \text{槽}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{双支撑对之两槽\ \textbf{皆为 }\lambda{=}2\ ✓✓};\quad \lambda{=}1\ \text{槽\ \textbf{完全私有}\ ✓✓}$$
$$\boxed{\text{(3) ✓八格联合分布 }(i_{\rm one},\pi)}:\ \text{每 }i_{\rm one}\ \text{恰配\ \textbf{两}\ 个 }\pi\ \text{——\ 即\ \textbf{避开 }i_{\rm one}\ 之两条共端点对}\ ✓✓$$
| $i_{\rm one}$ | $\pi$ | 计数 |
|---|---|---|
| $0$ | $\{1,3\}$ | $79$ |
| $0$ | $\{2,3\}$ | $79$ |
| $1$ | $\{0,2\}$ | $81$ |
| $1$ | $\{2,3\}$ | $81$ |
| $2$ | $\{0,1\}$ | $81$ |
| $2$ | $\{1,3\}$ | $81$ |
| $3$ | $\{0,1\}$ | $79$ |
| $3$ | $\{0,2\}$ | $79$ |
$$\qquad\textbf{（读法 ✓✓）}:\ i_{\rm one}{=}0\ \text{时 }\pi\in\{\{1,3\},\{2,3\}\}\ ✓\ \text{——\ 恰为\ \textbf{不含 0} 之两条共端点对}✓✓;\ \text{其余三行同理 ✓✓}$$

## §1 ★四正之完整 incidence 结构（**✓✓已定型**）

$$\text{设 }\pi(w^\ast)=\{u_1,u_2\}\ \big(\text{两槽皆 }\lambda{=}2✓\big);\ \text{第四槽 }u_3\ \big(\lambda{=}2\big);\ \lambda{=}1\ \text{槽 }u_0\ ✓$$
$$\qquad W_{u_1}=\{w^\ast,x_1\};\quad W_{u_2}=\{w^\ast,x_2\};\quad W_{u_3}=\{y_1,y_2\};\quad W_{u_0}=\{q\}\ ✓$$
$$\qquad\Longrightarrow\ \text{相异点}=\{w^\ast,x_1,x_2,y_1,y_2,q\}\ \big(\mathbf6✓\big);\ \text{incidence}=2{+}2{+}2{+}1=\mathbf7✓✓;\ \text{支撑多重集}=(2,1,1,1,1,1)✓✓$$
$$\qquad\Longrightarrow\ \textbf{（结论 ✓✓）}:\ \text{四正之全部结构可\ \textbf{完全参数化}为\ }\big(\pi(w^\ast),\ R(w^\ast),\ \text{五点之位置}\big),\ \text{且 }\pi\cap\{u_0\}=\varnothing\ ✓✓$$

## §2 逐条核验（**✓／✗**）

$$\textbf{✗✓}:\ \text{唐先生 §4 之规范化（唯一 }\lambda{=}1\ \text{槽属 }E(w^\ast)\Rightarrow W_{11}{=}\{w^\ast\}\big)\ ⟹ \textbf{不成立} ✗✓\ \big(0/640\big)$$
$$\textbf{✓✓✓}:\ \text{唐先生 §4 之\ \textbf{预判（"若不成立，则存在另一种几何情形：}w^\ast\subseteq\text{两个 }\lambda{=}2\ \text{槽，而唯一 }\lambda{=}1\ \text{槽完全私有"\ ）\ \textbf{完全命中}}✓✓✓\ \text{——\ 即实测之情形 ✓✓}}$$
$$\textbf{✓✓}:\ \text{唐先生 §1（四正}\Rightarrow\text{incidence 多重集}(2,1,1,1,1,1)\big)\ \textbf{成立}}✓✓\ \big(\text{C-515 ✓\big)$$
$$\textbf{✓✓}:\ \text{唐先生 §7（"private witness propagation"\ 为下一步）\ \textbf{方向正确}}✓✓\ \text{——\ 本档已给出其\ \textbf{精确参数化}✓✓}$$
$$\textbf{✓✓}:\ \text{唐先生 §8（勿再追求"四正}\Rightarrow\exists\,\text{owner}\ge4\text{"）\ \textbf{同意}}✓✓\ \big(\text{C-516 更正一 ✓}\big)$$

## §3 汇总裁（**✗✓／✓✓**）

| 项 | 值 |
|---|---|
| Gate A | **否**（$0/640$）✗✓ |
| $\pi(w^\ast)\cap\{i_{\rm one}\}$ | $\varnothing$ ✓✓ |
| 双支撑对之槽 | 皆 $\lambda{=}2$ ✓✓ |
| $\lambda{=}1$ 槽 | 完全私有 ✓✓ |
| 相异 witness 点 | $6$ ✓ |
| incidence 总数 | $7$ ✓ |
| 支撑多重集 | $(2,1,1,1,1,1)$ ✓ |

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "邻接引理" "私有槽" "八格分布"
技术词 邻接引理     命中文件数=1    :: ./WITGA-2026-09-28-gate-A-is-false-lambda-one-slot-is-private.md
技术词 私有槽        命中文件数=1    :: ./WITGA-2026-09-28-gate-A-is-false-lambda-one-slot-is-private.md
技术词 八格分布     命中文件数=1    :: ./WITGA-2026-09-28-gate-A-is-false-lambda-one-slot-is-private.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 邻接引理 | 0 | 0 | ✓（照唐先生 §5 ✓） |
| 私有槽 | 0 | 0 | ✓（本档新命名 ✓） |
| 八格分布 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 下一靶（**照唐先生 §10 之序 ✓；Gate A 已答 ✓**）

$$\textbf{（Gate B ✓✓✓下一刀）}:\ w^\ast\ \text{之 owner-3 profile 三型完备性}:\ \text{由四点 radius-2 约束 ＋ }|\mathrm{own}(w^\ast)|{=}3\ \text{＋ }d(ab){=}d(uv){=}4\ ⟹\ R(w^\ast)\in\{R_1,R_2,R_3\}\ ✓\ \big(\text{局部有限距离引理 ✓✓}\big)$$
$$\textbf{（Gate C ✓）}:\ \text{固定 }w^\ast\ \text{＋}\ \pi\cap\{u_0\}{=}\varnothing\ ⟹\ \text{五个 private witness 之延拓恰为 }T_1,T_2\ \text{两型}✓$$
$$\textbf{（本档新增之接口 ✓✓）}:\ \text{四正结构 ＝ }\big(\pi,\ R(w^\ast),\ u_0,\ \text{五点位置}\big)\ \text{——\ 参数化已备，可直接用于 Gate C ✓✓}$$
$$\textbf{（禁止 ✗）}:\ \text{再走 owner-计数容量矛盾 ✗✓；再用 }\lambda{=}1\ \text{槽属 }E(w^\ast)\ \text{之规范化 ✗✓}$$

## §6 边界（硬 ✓）

- **有限穷举** ✓（640 四正实例之 $i_{\rm one}$／$\pi$ ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★否证（Gate A ✗✓）** ＋ **一项★刚性事实（$\pi\cap\{i_{\rm one}\}{=}\varnothing$ ✓✓）** ＋ **一项参数化（四正结构 ✓✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** Gate B／C 已证 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
