已查地图（**先查后写**）：`C-321`（本体审计第一阶段 ＋ 四层范围 ＋ 两条硬纪律 ✓）、`C-292`（Lehmer 深审回执 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-322：Mahler／Lehmer 现有机制兼容性审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条）

$$\textbf{① 出口}✓✓：\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓$$
$$\textbf{② 原因}✓✓：\text{已确认的现有操作}\ \textbf{两两交换}✓，\text{或以}\ \textbf{因子分解恒等式} \text{相连}✓ —— \text{按你的 C 条，}\textbf{两者均不计}✗✓$$
$$\textbf{③ 无异常由兼容律产生}✓（\text{D 条：}\textbf{无}\ \text{可回答的}\ \text{「哪一异常} \leftarrow \text{哪两操作} \leftarrow \text{哪一兼容律」}✗✓）$$
$$\textbf{④ 纪律}✓✓：\text{本档只作}\ \textbf{Mahler／Lehmer 内部审计}✓；\textbf{不}\ \text{谈}\ RH\ \text{关系}✗（\text{除非后续另有独立证据}✓）$$

## §1 协议（唐先生口径 ✓）

**A. 操作是否 genuinely different** ✓（同一结构的不同表达 ✗——如相乘性 vs 积分形 vs 对数高度 ✗✓）
**B. 是否传播同一对象上的性质／异常** ✓（须明确 `T_1: X -> X`、`T_2: X -> X` ✓；不同层面的定理 ✗）
**C. 是否存在非平凡兼容** ✓（`T_1 T_2 != T_2 T_1` 且有**数学内容的补偿／交换／约束律** ✓；**单纯交换律／因子分解恒等式／换语言全部不计** ✗✓）
**D. 异常是否由该兼容律产生** ✓（须明确指出"哪一异常 ⟵ 哪两操作 ⟵ 哪一兼容律" ✓；**不得事后串故事** ✗✓）
**三出口** ✓：`FOUND` ／ `NO SUCH COMPATIBILITY FOUND` ／ `GAP`（**不用 FSD 等标签作判据** ✗✓）

## §2 操作清单（✓，仅取 C-321 已确认者）

| 操作 | 定义 | 保 `M`？ | genuinely different？ |
|---|---|---|---|
| **互反变换** `R` | `P(x) -> x^n P(1/x) = P*(x)` | **保** ✓ | **是** ✓（在多项式类上是真对合 ✓，且**其不动点恰是互反多项式**＝Smyth 二分留下的未决类 ✓✓） |
| **代换** `S_k` | `P(x) -> P(x^k)` | **保** ✓（根 `alpha -> alpha^{1/k}` ⟹ 模不变 ✓） | **是** ✓（**升次** ✓） |
| **乘分圆因子** `C_m` | `P -> P · Phi_m` | **保** ✓（`M(Phi_m) = 1` ✓） | **是** ✓（升次 ✓） |
| **乘一般因子** `Q` | `P -> P Q` | **不保** ✗（`M(PQ) = M(P)M(Q)` ✓） | 属**相乘性泛函** ✗，非保性质操作 ✗✓ |
| **Galois 作用** | 共轭置换 | **保** ✓ | 是**不变性** ✓，非多项式类上的映射 ✗✓ |

## §3 A 条判定（✓）

**排除** ✗✓：`M(PQ) = M(P)M(Q)`（相乘性 ✓）、积分形（Jensen ✓）、`h = (1/deg) log M`（换语言 ✓）—— \textbf{三者是同一结构的不同表达} ✗，**不计为两个操作** ✓（唐先生 A 条 ✓）
**保留** ✓：`R` ✓、`S_k` ✓、`C_m` ✓ —— 三者均为**多项式类上的真映射** ✓

## §4 B／C 条判定（✓✓，本档关键）

$$\textbf{B 条}✓：R／S_k／C_m\ \text{均作用在同一对象类上}✓（\text{非互反}\ P \in \mathbb{Z}[x]✓）\ \Longrightarrow \text{合格}✓$$
$$\textbf{C 条}✓✓：\text{逐对检验}✓ —— \ \boxed{S_k(P^*) = S_k(P)^*}✓（\text{直接计算：}S_k(P^*)(x) = P^*(x^k) = x^{kn}P(x^{-k})✓；S_k(P)^*(x) = x^{kn}P(x^{-k})✓）\ \Longrightarrow \ \textbf{交换}✗✓$$
$$\textbf{另一对}✓✗：\ \textbf{分圆代换恒等式}✓：\Phi_m(x^k) = \prod_{d | mk,\ d \nmid m} \Phi_d(x)✓ \Longrightarrow C_m\ \text{与}\ S_k\ \text{以}\ \textbf{因子分解恒等式} \text{相连}✗✓$$
$$\textbf{结论}✓✓：\text{合格操作对}\ \textbf{要么交换}✗，\textbf{要么以因子分解恒等式相连}✗ —— \text{按 C 条，}\textbf{二者均不计}✗✓ \Longrightarrow \textbf{无非平凡兼容}✗$$

## §5 D 条判定（✓）

$$\text{不存在可回答的三元组}\ \ \text{「异常} \leftarrow \text{两操作} \leftarrow \text{兼容律」}✗✓$$
$$\textbf{附带说明}✓：\text{`R` 的不动点}\ \textbf{恰是互反多项式}✓（\text{Smyth 已解决非互反}✓）\ —— \text{这是}\ \textbf{结构事实}✓，\textbf{不是} \text{兼容律}✗✓$$

## §6 出口与纪律（✓✓）

$$\boxed{\textbf{NO SUCH COMPATIBILITY FOUND}}✓（\text{预注册出口二}✓）$$
$$\textbf{① 不升级}✓✓：\text{即使找到漂亮的内部兼容律，也只记作}\ \textbf{Mahler／Lehmer 内部数学机制}✓；\textbf{只在后续另有独立证据时才讨论} RH\ \text{关系}✗✓$$
$$\textbf{② 不建新框架}✗✓：\text{本档}\ \textbf{不}\ \text{设}\ F9／F10✗，\textbf{不}\ \text{以 FSD 标签作判据}✗✓$$
$$\textbf{③ 两线分离}✓✓：\ `M=5 certificate -> \textbf{OPEN/AUDIT}`\ \textbf{继续冻结}✓，\textbf{不与}\ C\text{-322 混线}✗✓$$

## §7 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 双操作审计  命中文件数=0    :: 
技术词 补偿律        命中文件数=1    :: ./p30d-joint-scaling.md 
技术词 互反变换     命中文件数=0    :: 
```
- 本档新增 ✓：`双操作审计`／`补偿律`（依上表判 ✓）；`互反变换` 视命中判 ✓
- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：Mahler／Lehmer 已有 RH bridge ✗；互反对合＝兼容律 ✗；因子分解恒等式＝兼容律 ✗
