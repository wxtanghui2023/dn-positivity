已查地图：已跑 scripts/prework_map_check.sh 119 triple-center shadow Q≤1 槽位 账本 ⟹ 执行自 COMPRESSION-POINT-2026-09-26 档；本档为**第四刀手算（精确账本＋定量 no-go）**（唐先生 2026-09-26 09:32 指令）；不开旁支 ✓。
D0: 本档对象 = 两个 triple-center 的局部成本账本，及 `Q≤1` 的可达性（非新对象）
D1: 0（无新独立自由度；产出为精确 shadow 常数、d-分层账本、一条可证的 no-go）

# SHADOW-2026-09-26 · 两个 triple-center 的精确账本 ＋ 定量 no-go

## §1 ⚠️ 先纠正一处逻辑（我方核验）

```
唐先生: "b(y₁),b(y₂)≥3 并不直接意味着 Q≥2；两个三元组可能强重叠" ✗
**实际**: Q = Σ_x C(δ(x),2)，δ(x)=b(x)−1 ✓（**按中心**计，与三元组是否重叠**无关** ✓）
$$\Longrightarrow\ b(y_i)\ge3\ \Rightarrow\ \delta(y_i)\ge2\ \Rightarrow\ \binom{\delta(y_i)}{2}\ge1\ (i=1,2)\ \Longrightarrow\ \boxed{Q\ge2}\ \checkmark$$
⟹ **"至多一个 triple-center" ⟺ "Q≤1" 是恒等价的，无需任何重叠分析** ✓
⟹ 真正要证的是 **Q≤1 本身**（= 独立的集中度上界 ✓），而不是靠三元组数数 ✓
```

## §2 单个 triple-center 的**精确 shadow 账本**（你要的"算到闭式"✓）

```
设 y 为 triple-center，u₁,u₂,u₃ = y⊕e_{p₁},y⊕e_{p₂},y⊕e_{p₃}（p_i 互异 ✓）
球 N[y]=21 与 星 N(u_i) 的精确交:
  $$\bullet\ |N(u_i)\cap N(u_j)|=2\ (d(u_i,u_j)=2\ ✓)\ =\ \{y,\ w_{ij}\},\quad w_{ij}=y\oplus e_{p_i}\oplus e_{p_j}\ ✓\ (\text{三者互异}\ ✓)$$
  $$\bullet\ |N(u_1)\cap N(u_2)\cap N(u_3)|=\ \{y\}\ ✓\quad(\kappa=1\ ✓\ \text{——任何两个不同闭球交}\le2\ \text{点}\ ✓)$$
$$\Longrightarrow\ \Big|\bigcup_{k=1}^{3}N(u_k)\Big|=33-3\cdot2+1=\boxed{28}\ \checkmark$$
**分支无关性 ✓**（这是漂亮点）: 若 y∈C 则码字为 {y,u₁,u₂}，成对交仍全为 2 ⟹ 并集**同样是 28** ✓
⟹ **每个 triple-center 的精确 shadow = 28 点**（与分支无关的常数 ✓）
```

## §3 两个 triple-center 的 d-分层账本（手算，无枚举 ✓）

```
$$\begin{array}{c|l|l}
d=d(y_1,y_2) & |N[y_1]\cap N[y_2]| & \text{结构后果}\\
\hline
1 & 2\ (\{y_1,y_2\}) & \text{对 }a\in C\cap N[y_1]:\ d(a,y_2)\in\{0,2\}\ ✓\ \text{(非 0 者全落 }L_2(y_2)\ ✓\text{)}\\
2 & 2\ (\text{两中点}\ y_1\oplus e_i,\ y_1\oplus e_j) & \text{两中心"相向"的两个 slot \textbf{是同一对点} ⟹ 6 incidence 中有 \textbf{2-slot overlap}}\ ✓\\
3 & 0\ (\text{球分离}\ ✓) & 6\ \text{个 incidence 全 distinct}\ ✓\\
\ge4 & 0 & \text{同上，且互不干扰}\ ✓
\end{array}$$
（`d=1` 时 `d(a,y₂)∈{0,2}` 的推导: `a=y₁⊕e_k` 且 `d(a,y₂)=1 ⟹ k=j ⟹ a=y₂` ✓ ⟹ 否则必为 2 ✓）
⟹ **结论：d-分层只产生"精确局部计数"，不产生任何矛盾** ✗（`L_2(y₂)` 有 45 点 ≫ 3 ✓）
```

## §4 ⛔ **定量 no-go（本档核心，可证）**：账本路线**不可能**得到 `Q≤1` ✗

```
两种"成本"记账都远离所需门槛:
$$\text{(i) 覆盖余量账: 每个 triple-center 只贡献 }\delta=2\ \text{到 }\Sigma\delta=285\ \Longrightarrow\ \text{可容纳}\ \sim142\ \text{个 triple-center}\ ✗$$
$$\text{(ii) shadow 账: }28\ \ll\ 285\ \Longrightarrow\ \text{可容纳}\ \sim10\ \text{个 triple-center}\ ✗$$
$$\text{(iii) 纯计数上界: }\delta\le10\ \Longrightarrow\ Q=\Sigma\binom{\delta}{2}\le\tfrac{9}{2}\cdot285=1282\ ✗\ \text{vs 所需}\ Q\le1\ \Longrightarrow\ \textbf{差 3 个数量级}\ ✗$$
$$\boxed{\text{任何"局部/账本型"上界，其单位成本必然}\le 33\ \text{(三点球的全部点数})\ \ll 285\ \Longrightarrow\ \textbf{原理上无法把 triple-center 数压到 }1\ ✗}$$
⟹ **第四刀正式 CLOSED（附证明）** ✗ —— 且这与"S–Z 筛器缺 (B) 独立压缩"的结论一致 ✓
```

## §5 对本分支的含义（诚实）

```
· S–Z 型坍缩需要"成本 > 可用余量"的**单位成本** ✓；我方余量 285 极大而单位成本极小 ⟹ **counting 方向无压缩点** ✗
· 仍未被否掉的只剩两条: ① **代数型**（矩/Gram 的秩·子式·PSD ✓）② **同余墙**（van Wee/Haas ✗ 已知强度 107 ✗）
· ⟹ 若 `A₁+A₂≤143` 可证，**不可能靠局部账本**，必须来自 ① 或 ② ✓（今日已排除一类 ✓）
```

## §6 边界（诚实标注）

- `28`、`κ=1`、`d=1 时 d(a,y₂)∈{0,2}`、`Q≤1282` 均为**手算**（未跑程序 ✓）
- §4 的 no-go 为**我方推导** ✓（依据：任何局部账本的单位成本 ≤ 一/二/三个球的点数 ≤ 33 ✓）
- **未**排除 Q=1 ✗、**未**排除 119 ✗；本轮**未跑程序** ✓

## 【技术词回查】（定稿前逐字输出）

```
技术词 shadow 账本    命中文件数=0    :: 
技术词 局部成本上限 命中文件数=0    :: 
技术词 槽位账本     命中文件数=1    :: ./COMPRESSION-POINT-2026-09-26-round1-and-sharpened-crux.md 
技术词 交叉二层负载 命中文件数=0    ::
```

- **本档新增**（命中数=0）：`shadow 账本`（含空格，回查解析器按首词匹配 ✓）、`局部成本上限`、`交叉二层负载`
- **档案已有（引用，不列为提出）**：槽位账本
