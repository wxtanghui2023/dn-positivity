# PROTOCOL —— **资产迁移表 T0→T7 实打 $K(10,1)\ge107$**（自评：T4 处全断）

> **性质**：**方法论 ＋ 自评**——**不占 C 号** ✓；**不作方向裁定** ✗；空间 B ✓
> **时间**：2026-09-29 18:00 ✓

**已查地图**：`AUDIT-29e`（单条线性不等式不能到 107）／`AUDIT-29i`（van Lint–van Wee ＝103）／`CALIBRATE-K91*`／`DERIVE-107*` ✓

D0: 本档对象 ＝ **档案已有**（各资产皆在档 ✓）
D1: 0（产出＝**一次自评 ＋ 瓶颈定位** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{T4（增益）处，全部现有资产归零 ⟹ 无可用接口 ⟹ 这是能力边界之\ \textbf{结构性陈述}}}$$
$$\boxed{\text{唯一未验证接口 ＝ BÖW 2004 之 general }R{=}1\text{ 机制（不可得）}}$$

## §1 T0 目标（✓ 精确）

$$\text{证明}:\ K(10,1)\ \ge\ 107\iff\textbf{不存在} C\subseteq Q_{10},\ |C|\le106,\ \text{半径 1 覆盖}$$
$$\text{注意}:\ \text{公开记录 }107\ \text{已是\ \textbf{下界}；故真正命题 ＝ 排除 }M\le106$$

## §2 T1 瓶颈（✓ 已量化）

$$f(x)=|C\cap B_1(x)|\ge1;\qquad \sum_xf(x)=11M;\qquad M=106\Rightarrow \overline f=\frac{1166}{1024}=1.139$$
$$\therefore\ \text{纯计数（球界）给 }M\ge93.09\Longrightarrow94;\ \textbf{缺 }13$$
$$\text{结构性瓶颈}:\ \text{counting 是\ \textbf{加性}的，看不见\ \textbf{球的排布}；而 }M{=}106\text{ 的排除需要排布级信息}$$

## §3 T2 资产接口（✓ 逐一列出，接口须与瓶颈同类）

| 资产 | 数学接口 | 已知落点 |
|---|---|---|
| Habsieger excess 同余 | ball-excess 聚合 $\delta_{N[v]}$ ＋ $\bmod p$ | $n{=}10$：$94$（**自动** ✗） |
| van Lint–van Wee / van Wee 1988 | $\varepsilon$-精化线性不等式（仅偶 $n$） | $103$ |
| Zhang 1991／–Lo 1992 | pair／triple covering 线性不等式 | $105$ |
| SDP-3（Gijswijt–Polak 2025） | Terwilliger 代数 → PSD 矩阵 | $105.2223\Rightarrow106$（**层次不可升**） |
| Östergård–Blass 2001 机制 | 子空间分布 → LP 细化 → 枚举完整性 | $K(9,1){=}62$（$n{=}10$ 需 $2^{256}$ ✗） |
| **BÖW 2004** | **general $R{=}1$ lower bound** | $\mathbf{107}$（**正文不可得** ✗） |

## §4 T3 转换（✓ 能改写的都写了）

$$\text{Habsieger}\to n{=}10,p{=}11:\ \sum_{i=0}^{10}\Delta_i(v)=E\equiv-1\pmod{11}\ \textbf{恒成立}\Longrightarrow\ \text{无增益}✗$$
$$\text{Zhang}\to \text{linear ineq}:\ \le105;\qquad \text{SDP-3}:\ \le105.2223\Longrightarrow106;\qquad \text{均 }<107✗$$

## §5 ★T4 增益（**关键：拿掉它，证明会失去什么**）

$$\boxed{\text{Habsieger}:\ \text{失去}\ \delta_{N[v]}\ \text{同余};\ \text{但该同余在 }n{=}10\ \textbf{自动} \Longrightarrow \text{零增益}✗}$$
$$\boxed{\text{Zhang/SDP}:\ \text{失去一条\ \textbf{松弛型}不等式};\ \text{而 }107>105.2223\Longrightarrow \textbf{松弛型不可能到}✗}$$
$$\boxed{\text{Östergård--Blass}:\ \text{失去\ \textbf{枚举完整性}};\ \text{而 }n{=}10\ \text{成本 }2^{256}\Longrightarrow \text{不可实现}✗}$$
$$\therefore\ \boxed{\text{全部现有资产的 T4 ＝ 0 ⟹ \textbf{没有接口能被嫁接}}}$$

## §6 T5 碰撞（✗ 无）

$$\text{现有两条独立约束之碰撞最高只到 }105.2223\Longrightarrow106;\ \text{要 }107\ \text{须\ \textbf{第三条独立约束}}$$
$$\text{本会话 8 条候选全部未产生第三条（逐条死于重编码/逆趋势/次线性）✗}$$

## §7 T6／T7（✗／✓）

$$\text{T6}:\ \text{无法在不计算的前提下写出碰撞证明（缺 T4）✗}$$
$$\text{T7}:\ \text{计算只用于\ \textbf{否证候选}（本会话 8 次全部有效）✓\ —\ 这是唯一可靠能力}$$

## §8 自评（**唐先生验收标准**）

$$\boxed{\text{标准}:\ \text{不是"知道多少数学"，而是"能把多少已有数学转成当前问题的新约束"}}$$
$$\text{本会话自评}:\ \text{否证能力}\ ✓✓\ (\text{8/8 有效，且含 3 次自查纠错});\quad \text{迁移能力}\ ✗\ (\text{T4 处 0/6})$$
$$\therefore\ \boxed{\text{诚实结论}:\ \text{现有资产无一能嫁接 }K(10,1)\ge107;\ \text{缺口在 2004 年正文（不可得）}}$$

## §9 边界（硬 ✓）

- **资产接口与落点均引自档案已核实条目** ✓；**不占 C 号** ✓
- **不主张** $107$ 不可达 ✗（V290）；本档系**我方能力边界之自评** ✓
