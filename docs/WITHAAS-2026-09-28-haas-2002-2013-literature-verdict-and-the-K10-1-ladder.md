# WITHAAS-2026-09-28 — **C-541：Haas 2002／2013 文献判定与 $K(10,1)$ 阶梯状态（119 仍开放）**

> **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。词回查见 §8。
> **范围（照唐先生 2026-09-28 19:59 令 ✓）**：文献判定 ＋ 阶梯状态；**不作路线裁定** ✗；**不继续攻击 Haas 2002** ✓。
> **措辞纪律 ✓**：本档一切"未达 120"之陈述为**文献状态交叉验证后的事实判定**，**非**论文内部结论 ✗。

**已查地图：命中（接续 C-540／`EXCESS-2026-09-25`／`FACE-2026-09-26`／`M2-PREWORK-2026-09-27`，非新案 ✓）**

D0: 本档对象 ＝ **档案已有**（$K(10,1)$／阶梯／文献下界——**无新数学对象** ✓）
D1: 1（**首次登记 Haas 2002／2013 之文献判定 ＋ $K(10,1)$ 阶梯状态 ＋ "119 仍开放"之交叉验证结论 ✓✓**）
[R]

---

## §1 当前任务

核查 Haas 2002 之 fixed-$k$-dimensional-subspace 线性不等式方法，判断其是否已闭合

$$K(10,1)\ge120\qquad(\text{即排除 }119\text{-word covering code}).$$

## §2 Haas 2002 fingerprint

**摘要（逐字 ✓，2026-09-28 由 ScienceDirect 抓取）**：

> "Let $k_q(n)$ denote the minimal cardinality of a $q$-ary code $C$ of length $n$ and covering radius one. **The numbers of elements of $C$ that lie in a fixed $k$-dimensional subspace of $\{0,\dots,q-1\}^n$ satisfy a certain system of linear inequalities.** In a recent paper, the author developed a method to deal with this system for values of $k$, which are unbounded with increasing $n$. The aim of the present paper is to generalize the method in the cases $q=2$ and $3$, which provides new lower bounds for $k_2(n)$ and $k_3(n)$."

$$\boxed{\text{固定 }k\text{-维子空间}\ \longrightarrow\ \text{其中码字数满足一组线性不等式}}$$

**摘要本身不含**：$n{=}10$ ✗；$119$ ✗；$120$ ✗；$K(10,1)$ 专项结论 ✗

$$\therefore\ \boxed{\text{Haas 2002}＝\textbf{general lower-bound method}\ \text{（非 }K(10,1)\text{ 专项闭合论文）}}$$

## §3 与 FACE 之结构关系

`FACE-2026-09-26` 处理二维 face occupancy $q_F$，得

$$\sum_F\binom{q_F}{2}=9A_1+A_2$$

⟹ 二维 face incidence **退化为已有 distance-distribution 数据** ⟹ 不提供独立约束 ✓

Haas 2002 之 fingerprint：

$$\boxed{k\text{-维子空间}\ \to\ \textbf{cross-subspace linear coupling}}$$

$$\therefore\ \boxed{\text{Haas-type subspace coupling}\ \not\equiv\ \text{FACE incidence}}$$

**⚠️ 但这只说明机制不同，不等于该机制对 $n{=}10$ 尚未被档案覆盖** ✗；具体应用边界仍需以档案审计为准 ✓。

## §4 文献阶梯（校准后）

| 层次 | 下界 | 来源 |
|---|---|---|
| sphere covering | $94$ | 基本球覆盖界 |
| LP／layered | $93.09$ | Haas 2013 路线（档案校准 ✓） |
| 3-point／SDP | $105.2223$ | Gijswijt–Polak 2025, Table 5（C-474 ✓） |
| **published record** | $\mathbf{107}$ | BÖW 2004 |
| known upper bound | $120$ | 已知构造 |

$$\boxed{107\le K(10,1)\le120}\qquad\boxed{K(10,1){=}120\ \text{尚未由已发表方法证明}}$$

## §5 Haas 2002 之状态判定

$$\boxed{\text{Haas 2002：NOT CLOSED}}$$

**交叉验证后的表述 ✓**（措辞收紧 ✓）：

$$\boxed{\text{Haas 2002 provides a genuine method family, but does not close the }119\text{-word case.}}$$

**🔒 两条必须分开记 ✓**：

$$\textbf{(甲)}\ \boxed{\text{Haas 2002 fingerprint}\ \neq\ \textbf{已证明新下界}}\ \ \text{（方法存在 ⟹ 目标未解）}$$
$$\textbf{(乙)}\ \boxed{119\text{-word case：OPEN}}$$

⟹ **后做 novelty audit 时，不得把"方法存在"误记成"目标已解决"** ✓✓（本档立法目的）

**本轮不从摘要外推 $n{=}10$ 具体数值** ✗。

## §6 Haas 2013：单独登记之潜在线索

$$\delta_{p-1}\ge(p-2)^{p-1}\qquad\big(n\equiv-1\ (\mathrm{mod}\ p),\ p\ \text{奇素数},\ \delta_0{=}\cdots{=}\delta_{p-2}{=}0\big)$$

对本问题：$n{=}10$、$p{=}11$ **确实** $10\equiv-1\pmod{11}$ ✓。但前提 $\delta_0{=}\cdots{=}\delta_9{=}0$ **极强** ✓。

$$\boxed{\text{Haas 2013／}p{=}11\text{：POTENTIAL GAP}}$$

**而**非当前攻击路线 ✗，理由：

1. 未证该条件能由 119-word covering code **强制产生** ✗；
2. 未证其能与当前 excess／profile 数据**耦合** ✗；
3. 当前任务非重启已关闭之 Layer 2+ 线 ✗；
4. 该方向应待**后续专门审计** ✓。

## §7 本轮最终状态

$$\boxed{\begin{array}{l}
\text{Haas 2002：一般性 subspace-linear-inequality method}\\
\text{Haas 2002：未闭合 }K(10,1)\\
\text{Haas 2013：存在 }n{=}10,p{=}11\text{ 之形式匹配，但前提过强}\\
\text{Gijswijt–Polak 2025：}105.2223\text{，仍未到 }120\\
\text{当前 published record：}107\le K(10,1)\le120\\
\text{119-word case：OPEN}
\end{array}}$$

### 🛑 STOP

本轮**不再**计算 Haas 2002 具体不等式，**亦不重跑**：2-face occupancy ✗；excess moments ✗；三球／三阶矩 ✗；已关闭之 Layer-2 incidence ILP ✗；已验证无效之固定 Best-code 局部容量路线 ✗。

（皆属既有边界或已触发 stop-loss 之机制 ✓）

**下一轮若重启，应从真正未覆盖之 cross-subspace coupling 或已登记之 Haas-2013 $p{=}11$ 条件链开始，而非重复上述路线** ✓。

## §8 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "文献状态交叉验证" "subspace coupling" "潜在线索"
技术词 文献状态交叉验证 命中文件数=0    ::
技术词 subspace coupling 命中文件数=0    ::
技术词 潜在线索     命中文件数=0    ::
```

| 词 | 本线他档命中 | 跨空间同名（不计 ✗） | 本档新增 |
|---|---|---|---|
| 文献状态交叉验证 | 0 | 0 | ✓ |
| subspace coupling | 0 | 0 | ✓ |
| 潜在线索 | 0 | 0 | ✓ |

## §9 边界（硬 ✓）

- **不作路线裁定** ✗；不开门② ✓；不改门 ✓；**不跨空间** ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- **本档不产生新数学** ✓（D1 为文献状态登记）
