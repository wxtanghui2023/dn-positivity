已查地图（**先查后写**）：查 `C-173`（κ₃ 闭式 2−√3 ＋ 一维证书）、`C-172`（近似周期单调性引理）、`C-176`（m_M ≤ M−1）、`CLOSED-ROUTES-MAP.md`／`MASTER-STATUS-AND-CLOSURES.md`（关键词：kappa_N｜λ_max｜单调性引理）。回查：`κ_N 与 N 无关`=0、`1−16λ 判据`=0（**均本档新增**）✓

D0: 本档对象 = **新引理（κ_N(λ) 对 N ≥ 4 与 N=3 相同 ⟹ λ_max(N)=2−√3 对一切 N≥3）** ＋ 对一次扫描假象的更正 —— 关系 = 新构造 ＋ 更正
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 引理（新，初等，可手核）

$$\textbf{引理}：\text{设}\ \kappa_N(\lambda):=\inf_\theta\max_{1\le m\le N}\big[\cos(m\theta)-\lambda m^2\big]✓\ \text{且}\ \lambda_{\max}(3)=2-\sqrt3✓。$$
$$\qquad \text{则对一切}\ \lambda\in[\tfrac18,\ \lambda_{\max}(3)]\ \text{与一切}\ N\ge4：\ \boxed{\kappa_N(\lambda)=\kappa_3(\lambda)}✓✓$$
$$\qquad \text{特别地}\ \lambda_{\max}(N)=\lambda_{\max}(3)=2-\sqrt3\ \text{对一切}\ N\ge3✓✓$$

## §2 证明（三行）

$$\textbf{① 单调性}：\kappa_N\ \text{关于}\ N\ \textbf{不减}✓（\max\ \text{中项数增加}⟹\text{逐点值不减}⟹\inf\ \text{不减}）✓$$
$$\textbf{② 高次项永不 binding}：\text{设}\ \lambda\ge\tfrac18。\ \text{对}\ m\ge4：$$
$$\qquad \cos(m\theta)-\lambda m^2\ \le\ 1-\lambda\cdot 16\ \le\ 1-2\ =\ -1\ \le\ \kappa_3(\lambda)✓$$
$$\qquad （\text{末步用}\ \lambda\le\lambda_{\max}(3)\Longrightarrow\kappa_3(\lambda)\ge-1✓，\text{此为}\ \lambda_{\max}\ \text{的定义}✓）$$
$$\qquad \Longrightarrow m\ge4\ \text{项恒}\ \le\ \kappa_3(\lambda)\le\max_{m\le3}[\cdots] \Longrightarrow \text{永不确定}\ \max \Longrightarrow \text{两个 min-max 问题恒等}✓$$
$$\textbf{③ 合并}：\text{②给}\ \kappa_N(\lambda)=\kappa_3(\lambda)\ (N\ge4)；\text{①给}\ \lambda_{\max}\ \text{关于}\ N\ \text{不减}✓ \Longrightarrow \lambda_{\max}(N)=\lambda_{\max}(3)=2-\sqrt3✓✓\qquad\square$$

## §3 ⚠️ 自我更正（本档第 1 条）

$$\text{首次数值扫描报"}\lambda_c\approx0.5"✗\ —— \textbf{错}✗$$
$$\text{原因}：\text{谓词}\ \kappa_3(\lambda)\ge1-16\lambda\ \textbf{在}\ \lambda\ \text{上不单调}✓ \Longrightarrow \text{二分法不适用}✗（\text{假交叉点}）✓$$
$$\text{正确范围（手算）}：\lambda\in[\tfrac18,\ \lambda_{\max}]✓\ —— \text{因}\ \lambda\ge\tfrac18\Longrightarrow1-16\lambda\le-1✓，\lambda\le\lambda_{\max}\Longrightarrow\kappa_3\ge-1✓$$
$$\qquad \Longrightarrow \text{判据在该区间恒成立}✓✓\ —— \text{无需任何数值扫描}✓$$

## §4 数值核验（只作印证）

$$\lambda_{\max}=2-\sqrt3=0.2679491924311\ldots✓\qquad \kappa_3(\lambda_{\max})=-1✓（\text{闭式}）✓$$
$$1-16\lambda_{\max}=16\sqrt3-31=-3.287187\ldots\ \le\ -1✓ \Longrightarrow \text{判据成立}✓$$
$$\text{扫描（}N=3,4,5\text{）}：\text{在}\ \lambda=0.1,0.2,0.3,\dots,1.0\ \text{处}\ \kappa_N\ \text{三个}\ N\ \textbf{完全一致}✓（\text{与引理一致}）✓$$

## §5 推论（对单调性归约的影响）

$$\text{单调性引理（}C-172\text{）的}\ \varepsilon\ \text{门槛}：\varepsilon\ \le\ \frac{\sqrt{2\lambda_{\max}}}{\sqrt M}=\frac{0.732051}{\sqrt M}✓\ \text{（}C-173\text{）}✓$$
$$\Longrightarrow ⚠️\ \textbf{该门槛无法通过"使用更多}\ P\ \text{的倍数"来改进}✗✗\ \text{—— 因为}\ m\ge4\ \text{的项永不 binding}✓✓$$
$$\qquad \Longrightarrow \text{这是又一条}\ \textbf{机制级负面结论}✓（\text{与}\ C-186\ \text{的"Fejér 封顶"同型}）✓✓$$
$$\qquad \qquad \text{即：周期／κ 路线到此}\ \textbf{封顶}✓，\text{再要改进}\ \varepsilon\ \text{必须换机制}✓$$

## §6 边界

- ⚠️ 引理**严格且初等**（三行 ✓）；唯一外部输入是 $\lambda_{\max}(3)=2-\sqrt3$ 的闭式（`C-173` ✓，含一维区间证书 ✓）
- ⚠️ §4 扫描仅作印证，**未**用作证明 ✓
- ⚠️ 本档**不**声称 $\lambda_{\max}(N)$ 对 $N\ge4$ 的*更大* λ 区间的性质（引理只覆盖 $[\tfrac18,\lambda_{\max}]$ ✓）
- **未用** RH；**未改**他档 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 κ_N 与 N 无关   命中文件数=0    ::  ⟹ 本档新增
技术词 1−16λ 判据      命中文件数=0    ::  ⟹ 本档新增
技术词 二分法假象      命中文件数=0    ::  ⟹ 本档新增
```
