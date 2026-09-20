已查地图（**先查后写**）：查 `C-203`（乙-0 任意簇三件套）、`C-204`（乙-1 隔离）、`C-201`（三簇分类）。回查见 §5 ✓

D0: 本档对象 = **T13-A 乙-2**：Cluster 3、5 的完整 $(\Delta_{\rm gap},c,R,\rho_{\rm iso})$ 三件套 ＋ 与 Cluster 0 的并列对照（机制是否共享、常数是否统一）—— 关系 = 结构定位 ＋ 乙-3 定理化的实例基座
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 措辞锁定（唐先生 2026-09-20 11:14，采纳）

$$\texttt{C-203}\ \text{的刚性球排除的是}\ \boxed{\text{"比}\ x_0\ \text{更低的点"}}✓，\ \textbf{不是}\ \text{排除所有数值停点}✗（\texttt{C-204}\ \text{的簇 1 即球内非极小点}✓）$$
$$\qquad \Longrightarrow \text{正确对象}：\boxed{\ 0<\|x-x_0\|\le\rho\ \Longrightarrow\ F(x)>F(x_0)\ }✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{把"球内只有}\ x_0\text{"写进定理}✗✓$$

## §1 ⭐ 三簇并列（完整三件套）

| 簇 | $F$ | $\vert A\vert$ | $A$ | $\Delta_{\rm gap}$ | 对应 $k$ | $c$ | $u^*$ | 实算 $R$ | 粗界 $R$ | $\rho_{\rm iso}$ | $c/2$ | 拼接 | 局部极小 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **0** | $0.7640811032$ | 4 | $\{1,5,11,13\}$ | $7.1085\times10^{-2}$ | 6 | $0.5462206$ | $(0,0,1)$ | $116.052$ | 169 | $2.2503\times10^{-3}$ | $0.2731103$ | ✓ | 是 ✓ |
| **3** | $0.7755338917$ | 4 | $\{2,7,10,15\}$ | $1.0298\times10^{-2}$ | 12 | $1.2238793$ | $(0,0,1)$ | $198.234$ | 225 | $2.3884\times10^{-4}$ | $0.6119396$ | ✓ | 是 ✓ |
| **5** | $0.7768817151$ | 4 | $\{1,3,13,15\}$ | $9.3350\times10^{-2}$ | 4 | $0.7550665$ | $(0,0,1)$ | $141.244$ | 225 | $3.0434\times10^{-3}$ | $0.3775332$ | ✓ | 是 ✓ |

$$\text{每簇的局部刚性结论}：F(x_j+\delta)\ \ge\ F(x_j)+\tfrac{c_j}2\|\delta\|✓\qquad \|\delta\|\le\rho_{{\rm iso},j}✓$$
$$\qquad \text{簇 0}：\ge F(x_0)+0.273110304\|\delta\|✓,\ \|\delta\|\le2.250252\times10^{-3}✓$$
$$\qquad \text{簇 3}：\ge F(x_3)+0.611939639\|\delta\|✓,\ \|\delta\|\le2.388354\times10^{-4}✓$$
$$\qquad \text{簇 5}：\ge F(x_5)+0.377533239\|\delta\|✓,\ \|\delta\|\le3.043428\times10^{-3}✓$$
$$\qquad （\text{拼接条件}\ \rho_{\rm iso}<c/R\ \text{在【实算 R】与【粗界 R】下均成立}✓✓）$$

## §2 ⭐ 核心判读：机制共享，常数不统一

$$\textbf{共享（结构）}：\text{三簇均有}\ |A|=M+1=4✓,\ c>0✓,\ \rho_{\rm iso}<c/R✓,\ \text{均为真局部极小}✓（\text{精修变化}\le3.9\times10^{-12}）✓$$
$$\qquad ⭐\ \text{且}\ u^*=(0,0,1)\ \textbf{三者完全相同}✓✓\ —— \text{最坏一阶方向都是【纯}\ \varphi_3\ \text{方向】}✓（\text{待乙-3 核是结构还是采样假象}⚠️）$$
$$\textbf{不统一（常数）}：c\in[0.546,\ 1.224]✓,\ \rho_{\rm iso}\in[2.39\times10^{-4},\ 3.04\times10^{-3}]✓,\ c/2\in[0.273,\ 0.612]✓\ —— \textbf{跨}\ 2.2\times\ \text{与}\ 12.7\times✓$$
$$\qquad \Longrightarrow ⚠️\ \textbf{不能} \text{声称"统一常数可复用"}✗✗\ —— \text{唐先生的顺序修正（乙-2 先行）在此得到验证}✓✓$$
$$\qquad \text{若要有统一陈述，只能取交集}：\min_j c_j=0.5462206✓,\ \min_j\rho_j=2.388354\times10^{-4}✓ \Longrightarrow \text{统一式成立但代价是}\ 12.7\times\ \text{的半径损失}✓$$

## §3 乙-3 的抽象命题形式（由三实例支撑）

$$\boxed{\ \text{Type-A 签名}\Big(|A|=M+1,\ \lambda_{\min}>0\Big)\ +\ \text{active 隔离}\ +\ \text{一阶凸包余量}\ c\ +\ \text{Hessian 界}\ R\ \Longrightarrow\ \text{局部线性刚性}\ ✓\ }$$
$$\qquad \text{其中"局部线性刚性"}=0<\|x-x_j\|\le\rho_j\Rightarrow F(x)>F(x_j)✓（\text{见 §0 措辞}）✓$$
$$\qquad ⚠️\ \textbf{常数按实例给定}✗（\rho_j,c_j\ \text{逐簇）}✓；\text{定理只保证【结构】可复用}✓✓$$
$$\qquad \Longrightarrow \text{三组数据即该命题的三个实例}✓（\text{乙-3 的主要内容}）✓$$

## §4 边界

- 全部数据为**数值**✓（gap ／ $c$ ／ Hessian 范数 ／ 精修验证 ✓）⟹ §3 是**结构模板**✓，尚未区间定理化 ✗（乙-3）
- $R$ 给出**实算**与**粗界**两套 ✓；两者均满足拼接 ✓ ⟹ 乙-3 可自选（粗界更易形式化 ✓）
- $u^*=(0,0,1)$ 三者相同：**可能是采样假象** ✗（方向网格含坐标轴 ✓）⟹ 标为待核 ⚠️
- 本档**不**声称任何一簇是全局极小 ✗；**不**动账本 ✓（仍 $0.76\le m_3\le0.764081100903$ ✓）
- **未用** RH；**未改** 他档 ✓

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 机制共享     命中文件数=1    ::  ./C205-T13-A-YI-2-three-cluster-suite-mechanism-shared-constants-not-uniform.md
技术词 常数不统一   命中文件数=1    ::  ./C205-T13-A-YI-2-three-cluster-suite-mechanism-shared-constants-not-uniform.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 两项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §6 下一步（乙-3）

$$\text{把 §1 的三组实例做成}\ \textbf{统一区间算术定理}✓：$$
$$\qquad \text{① active 隔离}\Longrightarrow \text{gap 与 Lip 的区间版}✓；\text{② 一阶凸包}\ c\ \text{的严格下界}✓（\text{LP 对偶或方向覆盖的区间版}）✓；$$
$$\qquad \text{③ Hessian 界}\ R\ \text{的区间版}✓（\text{用粗界}\ k^2\ \text{最省事}✓）✓；\text{④ 拼接}\ \rho_{\rm iso}<c/R✓$$
$$\qquad \Longrightarrow \text{结论}：F\ge F(x_j)+\frac{c_j}2\|\delta\|\ \text{对}\ \|\delta\|\le\rho_j\ ✓（\text{逐簇常数}）✓$$
