# AUDIT-2026-09-29zh — (α) 与 (β) **双双否定** ⟹ 总量/计数层**已饱和**

> 空间 B｜非 C 号｜唐先生令（22:40「先 a 后 b」）｜**不主张 107／不主张 106 可排除**（V290）
> 承接：`AUDIT-2026-09-29zg`（聚合系统可行）＋ `LEMMA-2026-09-29-L1`（局部刚性）
> 时间：2026-09-29 22:4x

**已查地图**：承 `ERRATUM-n1`／`ROUTE-…-107-ladder`／`AUDIT-zg`／`LEMMA-L1`
D0: 本档对象 = **档案已有**（内部码字计数／$\mu_{\max}$ 迭代）之**上界测试**（新数学对象：无 ✗）
D1: 0（产出 = **两条否定性读数** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\textbf{(α)}\ \text{内部码字计数之自然上界}\approx\mathbf{3492}\ \gg\ \text{所需}\ \mathbf{132}\ \Longrightarrow\ \text{数量级差 }26\times\ \text{，\textbf{无法对撞}}\ ✗✗}$$
$$\boxed{\textbf{(β)}\ \text{聚合系统在}\ \mu_{\max}\ge3\ \text{与}\ \ge4\ \text{处\textbf{仍可行}}\ \Longrightarrow\ \text{迭代}\ \mu_{\max}\ \text{在聚合层\textbf{无矛盾}}\ ✗✗}$$

## §1 (α) 内部码字计数：上界（实跑）

$$\text{目标}:\ \max\ \sum_{c}\binom{10-a_c-t_c}2\quad \text{s.t.}\ \Sigma a_c{=}2A_1{=}98\ (a_c\le1),\ \ \Sigma t_c{=}2\times44{=}88\ (t_c\le10)$$
$$\text{（}t_c:=\#\{\text{距 }c\ \text{为 1 之中点}\};\ \text{每中点恰距其 2 个对端为 1}\ \Longrightarrow\ \Sigma_c t_c{=}88\ ✓\text{）}$$
$$\text{凸性}\Longrightarrow\text{极值在端点（把 }t\ \text{集中到}\ a_c{=}0\ \text{之词）}:\quad \mathbf{3492}\ \text{（实跑）}$$
$$\therefore\ 3492\ \gg\ 132\ \Longrightarrow\ \textbf{该计数路线不能闭合}\ ✗\ ✓\ (\text{诚实记录})$$

## §2 (β) $\mu_{\max}$ 迭代：聚合候选解（实跑，逐条核验）

| 分支 | 候选 | 判定 |
|---|---|---|
| $\mu_{\max}\ge3$ | $n_1{=}884,\ n_2{=}138,\ n_3{=}2$；$A_1{=}49,\ A_2{=}23,\ P{=}0,\ E{=}2$ | **可行 ✓** |
| $\mu_{\max}\ge4$ | $n_1{=}886,\ n_2{=}136,\ n_4{=}2$；$A_1{=}49,\ A_2{=}25,\ P{=}0,\ E{=}8$ | **可行 ✓** |

（核验项：$\Sigma n{=}1024$｜$\Sigma(i{-}1)n{=}142$｜$\Sigma m_a{=}106$｜$\Sigma a m_a{=}2A_1$｜$n_{1+a}\ge m_a$｜$\Sigma\binom i2 n{=}2(A_1{+}A_2)$｜$\Sigma\binom i3 n{=}P{+}E$｜$P{\le}2A_2$｜$A_1{\le}49$）

$$\therefore\ \text{逐级加严}\ \mu_{\max}\ \text{在\ \textbf{聚合层}不复产生矛盾}\ ✗$$

## §3 汇总：**总量/计数层的四条独立否定**

$$\text{（1）}AUDIT\text{-}29e:\ \text{\textbf{单条}线性不等式}\le LP\le SDP\text{-}3{=}105.2223 ✗$$
$$\text{（2）}AUDIT\text{-}zg:\ \text{全部恒等式}+A_1{\le}49\ \text{于}\ M{=}106\ \textbf{可行} ✗$$
$$\text{（3）本档 (α)}:\ \text{内部码字计数差 }26\times\ \text{无法对撞} ✗$$
$$\text{（4）本档 (β)}:\ \mu_{\max}\ \text{迭代无矛盾} ✗$$
$$\boxed{\Longrightarrow\ \text{总量／计数层\ \textbf{彻底饱和}；}106\to107\ \text{必须靠\ \textbf{实现层（几何）} 或\ \textbf{换框架}}}\ ⚠️✓$$

## §4 下一步候选（**待唐先生定**，属方向性决策 ✗ 不自裁）

- **(A) 实现层不等式**：求 $A_2$ 之**几何下界/上界**（形状需 $A_1{=}49,A_2{=}22$；而 120-码实测 $A_1{=}50,A_2{=}\mathbf{149}$ ⟹ 二者相差 $7\times$，可能藏着一条真不等式）
- **(B) 换框架**：BÖW 之**混合码（binary/ternary）**框架 —— 历史路径；但论文不可得 ⟹ 须**自推**其关系式（大工程）
- **(C) 先验性反问**：为何"总量/计数"必然饱和？—— 与 `MASTER-FAILURE-MAP` §2 定理 A/B 是否同一墙的第三表现

## §5 边界（硬 ✓）

- **不主张** 107／105／任何新值 ✗；本档只**否定两条路线** ✓
- 候选解为**聚合层**之解（非码）⟹ 不声称存在 106-覆盖码 ✗✓
- 未重攻 pair 层（R02）／未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
