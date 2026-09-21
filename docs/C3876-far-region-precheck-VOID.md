已查地图（**先查后写**）：`C3875prime`（**LOCAL-SHARP-CLOSED；`\rho_{\mathrm{cert}} = 1.18278\times10^{-4}`；`\underline\eta = 0.0766443`；`K = 648`** ✓✓）、`C3874B`（**even-blind 反例；存在性 YES** ✓✓）、`C3874A`（**纯区间 LOCAL-ONLY** ✓✓）、`C-3849`（**零原子层已排除** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-78：C-3876 —— 远区可行性预检（A→B→C）**（唐先生 2026-09-21 23:09 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 目标（唐先生定性）}✓✓：\text{找}\ \textbf{反例的几何刚性}✓✓,\ \textbf{不是} \text{远区数值最小值}✗✓$$
$$\qquad R := E_{\mathrm{even}}\setminus B_{\rho_{\mathrm{cert}}}(x^*)✓✓;\ \text{理想出口}✓：\boxed{M(x) < c_0 \Longrightarrow x \in B_{\rho_{\mathrm{cert}}}(x^*)}✓✓$$

$$\textbf{② A（几何）}⚠️✓：\text{随机拒绝采样}\ \textbf{效率极低}✗（4000 次仅 1 个真可行点✓,\ 全 12 条偶频约束极难命中✓） \Longrightarrow \text{本档 A 地图}\ \textbf{不具结论性}✗✓$$

$$\qquad \text{较可靠地图}✓：C\text{-}3874B\ \text{的修正探针（全 12 约束＋下降}✓）：\text{最优可行}\ M = 2.1704✓,\ \textbf{无}\ M < c_0\ \text{点}✓✓$$

$$\qquad \textbf{A2（}\text{配对轨，决定性}✓✓）}：\text{在}\ c_1 = c_3✓,\ c_2 = c_4\ \text{上}：F_k = \sigma_5T_k(c_5)✓ \Longrightarrow M = \max_{k\ \mathrm{odd}}|T_k(c_5)|✓✓$$

$$\qquad \qquad \text{其最小值}\ \mathbf{0}\ \text{恰在}\ \boxed{c_5 = 0}✓✓ —— \text{即}\ C\text{-}3849\ \text{已排除的}\ \textbf{零原子点}✓✓ \Longrightarrow \text{该轨上唯一的}\ < c_0\ \text{点已被排除}✓✓$$

$$\qquad \Longrightarrow \text{（}\text{即 even-blind 的}\ M=0\ \text{反例有}\ \textbf{唯一} \text{位置}✓,\ \text{且落在已排除层}✓✓）$$

$$\textbf{③ B（一阶结构）}\textbf{否}✗✓：\text{一阶尖锐性}\ \textbf{不能} \text{外推到任意}\ h✗✓$$

$$\qquad \text{外推式}✓：\max_ig_i(x^*+h) \ge c_0 + \max_i[(Gh)_i + \delta_i] - K\|h\|^2✓,\ \delta = (0,0,-c_0,-c_0,-c_0,-c_0)✓✓$$

$$\qquad \qquad \text{（对每个}\ i\ \text{取界后}\ \max\ \text{保序}✓✓：a_i \ge b_i \Rightarrow \max a_i \ge \max b_i✓）$$

$$\qquad \text{但}\ \|h\| \gtrsim \eta/K\ \text{时}\ -K\|h\|^2\ \textbf{压倒} \text{一阶项}✗ \Longrightarrow \textbf{"回流"结论不可由局部一阶数据得到}✗✓$$

$$\qquad \Longrightarrow \text{与}\ C\text{-}3874A\ \text{的发现一致}✓：\text{区间／一阶手段}\ \textbf{都不覆盖远区}✗✓$$

$$\textbf{④ C（Gordan 全局化）}\textbf{不可能}✗✓（\text{本档决定性结论}✓✓）$$

$$\qquad \text{even-blind 见证点（}M = 0✓,\ \text{零原子层}✓）\ \text{处锥}\ \{Gh \le 0\}\ \textbf{非平凡}✓⟹ \text{该点}\ \textbf{不存在}\ y > 0\ \text{使}\ G^{\top}y = 0✗✓$$

$$\qquad \Longrightarrow \boxed{\text{"}\exists\ \text{点无关}\ y > 0,\ G(x)^{\top}y = 0\ \forall x\text{"}\ \textbf{为假}}✓✓ \Longrightarrow \text{Gordan 路线}\ \textbf{不可全局化}✗✓$$

$$\qquad \text{（与唐先生警告一致}✓✓：C\text{-}3874B\ \text{的 Tarski–Seidenberg}\ \textbf{只给存在性}✓,\ \textbf{不是} \text{构造}✗✓）$$

$$\textbf{⑤ 判词}✓✓：\ \boxed{\textbf{VOID}}✗✓（\text{本档三条路线均未给出可用的远区机制}✓；\text{剩}\ \text{polynomial／SOS／量词消去}✓\ \text{的}\ \textbf{一般机器}✗）$$

$$\textbf{⑥ 已确立的部分}✓✓：\ \text{近区}\ \textbf{CLOSED}（C\text{-}3875′✓✓）；\ \text{远区}\ \textbf{OPEN}✗；\ V_\sigma = c_0\ \textbf{尚未} \text{获得}✗✓$$

$$\textbf{⑦ 纪律}✓✓：\textbf{不}追远区数值最小值✗（\text{按唐先生令}✓）；\ \textbf{不}做大规模优化✗；\ \textbf{不}做 SOS✗✓$$

## §1 记录（数字驱动 ✓✓）

```
A 地图：4000 次随机抽样仅 1 个真可行点（低效）-> 不具结论性；M = 3.063318（n=1）
A2 配对轨：min_{c5} max_odd|T_k(c5)| = 0.000000 at c5 = 0.0000（= C-3849 已排除的零原子点）
B 外推：max_i[(Gh)_i + delta_i] - K|h|^2 < 0 once |h| >~ eta/K -> 无回流结论
C：even-blind 见证点处不存在 y>0 with G^T y = 0 -> 点无关 Gordan 证书为假
（可靠地图参见 C-3874B：全 12 约束探针最优可行 M = 2.170420828，无 M < c0）
```
- 脚本 ✓：`scripts/c380_78_C3876_precheck.py`✓；输出 ✓：`scripts/out_c380_78.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| A 几何地图 ✓ | **不具结论性（采样低效）** ⚠️✓ |
| A2 配对轨 ✓ | **`M = 0` 仅在已排除的零原子点** ✓✓ |
| B 回流（一阶） ✓ | **不可得（二次余项压倒）** ✗✓ |
| C Gordan 全局化 ✓ | **不可能（点无关 `y` 为假）** ✗✓ |
| 近区 ✓ | **CLOSED（C-3875′）** ✓✓ |
| 远区 ✓ | **OPEN** ✗✓ |
| **判词** ✓ | **VOID** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称远区已封或全局已证 ✓
- **不**把低效采样地图当结论 ✓
- **不**把 C-3874B 的存在性结果当构造 ✓
- **不**追远区数值最小值（按令）✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}大规模优化✗；\ \textbf{不}SOS／量词消去✗；\ \textbf{不}重做近区✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 回流刚性     命中文件数=0    :: 
技术词 一阶外推失效 命中文件数=0    :: 
技术词 点无关Gordan  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 更有效的远区地图}✓：\text{自}\ \textbf{已知可行点} \text{出发的多起点扫描（非拒绝采样}✓） \Longrightarrow \text{刻画}\ \{M < c_0\}\ \text{的形态}✓✓$$
$$\textbf{② 结构性替代}✓：\text{寻找}\ \textbf{非线性} \text{全局不等式（如二阶矩型}✓,\ \text{但}\ B1\ \text{线性路线已 sharp-closed}✗）×$$
$$\textbf{③ 接受现状}✓：\text{将}\ V_\sigma \le c_0\ \text{记为}\ \textbf{上界 ＋ 局部最优证书}✓,\ \text{全局最优记为}\ \textbf{待证}✓✓$$
