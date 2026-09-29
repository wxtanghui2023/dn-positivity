# AUDIT-2026-09-29za —— $\Lambda$（pair 污染量）**符号审计：$=$ 三重重叠矩之重编码 ⟹ 立即关闭** ✗

> **性质**：**符号审计**（非研究轮）——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 15:52 ✓

**已查地图**：`WITFIB-2026-09-28`（fiber 封）／`AUDIT-2026-09-29s`（fiber＝精确重述）／三预检 ✓

D0: 本档对象 ＝ **档案已有**（重叠矩／距离分布—皆经典 ✓）
D1: 0（产出＝**一次符号审计 ＋ 一候选关闭** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 符号展开}:\ \Lambda=\sum_x(\mu(x)-2)\cdot N_2(x)\quad(N_2(x)=\#\{\text{owner 距离-2 对}\})}$$
$$\boxed{\text{② 恒等式}:\ \Lambda=3\sum_x\tbinom{\mu(x)}3-\sum_{x\in C}(\mu(x)-2)s(x)\ \Longrightarrow\ P_1{=}0\ \text{时}\ \Lambda\equiv3\sum_x\tbinom{\mu}3}$$
$$\boxed{\text{③ 实测（8 码最小二乘）}:\ \Lambda=3\sum\tbinom{\mu}3\ \text{，残差}\ 0.00}$$
$$\boxed{\text{④ 判定}:\ \Lambda\in\operatorname{span}\{\sum\tbinom{\mu}{j}\}\ \textbf{（重编码）}\Longrightarrow\ \textbf{CLOSE}\ ✗}$$
$$\boxed{\text{⑤ P-c 亦否}:\ \Lambda\ge L\ \text{须"强制 }\mu\ge3"\ \Longrightarrow\ \textbf{逆趋势}\ ✗}$$

## §1 符号展开（✓）

$$\Lambda=\sum_{\{c,d\}:d(c,d)=2}\ \sum_{x\in N[c]\cap N[d]}(\mu(x)-2)=\sum_x(\mu(x)-2)N_2(x)$$
$$\text{（换序；无权重版}\ \sum_xN_2(x)=2P_2\ ✓\ \text{——即无权重版只需 }P_2\ \text{）}$$

## §2 恒等式（✓ 核心）

$$\text{对 }x:\ N_2(x)=\tbinom{k}2-\#\{O(x)\ \text{内距离-1 对}\};\quad k=\mu(x)$$
$$\#\{O(x)\ \text{内距离-1 对}\}=s(x)\ \text{当 }x\in C,\ =0\ \text{当 }x\notin C\ (\text{否则三球成三角形}\ ✗)$$
$$(k-2)\tbinom k2=3\tbinom k3\ \Longrightarrow\ \boxed{\Lambda=3\sum_x\tbinom{\mu(x)}3-\sum_{x\in C}(\mu(x)-2)s(x)}$$

## §3 实测（✓ 8 码）

$$8\ \text{个 }Q_9\ \text{覆盖码（}M{=}86..104\text{）}: \text{最小二乘拟合系数}\ =[P_1{:}0,\ P_2{:}0,\ P_3{:}0,\ \Sigma\tbinom{\mu}2{:}0,\ \Sigma\tbinom{\mu}3{:}\mathbf{3},\ \text{常数}{:}0]$$
$$\text{残差}\ \max|\Lambda-\text{fit}|=\mathbf{0.00}\ ✓\qquad(\text{全部码 }P_1{=}0\ \text{——贪心码必 }d_{\min}\ge2\ ✓)$$

## §4 判定（✓ 按唐先生预设规则）

$$\boxed{\Lambda\ \text{落于}\ \{\sum\tbinom{\mu}{j}\}\ \text{之 span}\ (\text{三重重叠矩之重编码})\Longrightarrow \textbf{立即关闭，不实验}\ ✓}$$
$$\text{二次否决（P-c 燃料预检）}:\ \text{所需方向}\ \Lambda\ge L\ \iff\ \text{"强制 }\exists x:\mu(x)\ge3"\ \Longrightarrow\ \textbf{excess 逆趋势}\ (M\downarrow\Rightarrow\text{excess}\downarrow)\ ✗$$
$$\therefore\ \boxed{\Lambda\ \text{路线双重否决}:\ \text{重编码}\ ✗\ +\ \text{逆趋势}\ ✗}$$

## §5 边界（硬 ✓）

- **实测（8 码最小二乘、恒等式核验）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本档仅**关闭一候选** ✓
