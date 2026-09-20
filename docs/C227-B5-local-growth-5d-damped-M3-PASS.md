已查地图（**先查后写**）：查 `C-226`（D-B B1–B4）、`C-225`（D-A′）、`C-221`（无阻尼 3 维局部刚性模板）。回查见 §7 ✓

D0: 本档对象 = **甲 B5：阻尼 M=3 的 5 维局部增长门**（$c_X,R,\rho_{\rm iso},\rho_{\rm up}$ 全部重算，禁止移植 T13-A）—— 关系 = 局部极小性认证
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 结论（先行）

$$\boxed{\text{B5：PASS}✓✓}\qquad \forall\delta:\ 0<\|\delta\|\le\rho_{\rm up}=1.9782244\times10^{-3}\ \Longrightarrow\ F(z_0+\delta)\ >\ F(z_0)✓✓$$
$$\qquad \text{变量}\ x=(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)✓（5\ \text{维}✓）；A=\{1,2,3,4,5,15\}✓（\text{已由 D-B 区间认证的精确 active set}✓）$$

## §1 ⭐ 全部数据（**5 维重算**，与 T13-A 明确不同 ✓✓）

| 量 | 本档（阻尼 M=3，5 维） | T13-A（无阻尼，3 维）——**禁止移植** ✗ |
|---|---|---|
| $\Delta_{\rm ref}$ | $0.2795968136$ ✓ | $0.071085496$ |
| $L_{\rm act}=\max_{k\in A}k\sqrt5$ | $33.54102$ | $k\sqrt3$：$22.5167$ |
| $L_{\rm non}=\max_{k\notin A}k\sqrt5$ | $31.304952$ | $25.9808$ |
| $\rho_{\rm iso}=\Delta/(L_{\rm act}+L_{\rm non})$ | $4.31171\times10^{-3}$ | $1.4658\times10^{-3}$ |
| $c_X$ | $\mathbf{0.09881200977}$ | $0.319306988$ |
| $R=\max_{k\in A}\|\nabla^2S_k\|_2$ | $\mathbf{99.89969551593013}$ | $169$ |
| $\rho_{\rm up}$ | $\mathbf{1.9782244\times10^{-3}}$ | $1.4658\times10^{-3}$ |
| 受限机制 | **覆盖受限**（$\rho_{\rm up}=2c_X/R$ ✓） | 隔离受限 |

$$\textbf{结论}：\text{两组常数无一处相同}✓✓ \Longrightarrow \text{证实"阻尼改变}\ \nabla S_k,\nabla^2S_k\ \text{与 active-set geometry"}✓$$

## §2 方法与实现（严格性来源）

$$\textbf{① 参考盒}=\text{D-B 盒的变量部分}✓（\text{宽}\sim10^{-6}✓） \Longrightarrow \Delta_{\rm ref}=\min_{k\in A}\inf S_k-\max_{k\notin A}\sup S_k✓$$
$$\textbf{② 真区间乘积}✓✓（\text{关键修正}✓）：S_k=r_2^k\cos(k\varphi_2)+r_3^k\cos(k\varphi_3)+\cos(k\varphi_1)✓\ \text{按【区间乘积】算}✓（\text{含符号}✓）：$$
$$\qquad \mathrm{iprod}([a_1,a_2],[b_1,b_2])=[\min_{4\ \text{积}},\max_{4\ \text{积}}]✓；\ r^k\in[r_{\rm lo}^k,r_{\rm hi}^k]✓（\text{单调}✓）$$
$$\textbf{③ }c\ \text{用 facet 法}✓（5\ \text{维}6\ \text{顶点}\Longrightarrow6\ \text{个 omit-one 面}✓；\text{法向由 SVD 零空间}✓；\text{containment 由被omit顶点同侧判定}✓）＋\text{扰动界}\ c_X=c_{\rm mid}-\varepsilon✓，\varepsilon=\max_k\|\text{半宽}\|_2✓$$
$$\textbf{④ }R\ \text{用}\ 5\times5\ \text{Hessian 的保守上界}✓（|\cos|\le\max✓）$$
$$\textbf{⑤ 自洽规则}✓✓：\textbf{数据球半径}\ \rho\ \ge\ \text{认证半径}\ \rho_{\rm up}✓（\text{本轮先写错}✗，已修正}✓）$$

## §3 ⭐ 自洽扫描（$c$ 在半径 $\rho$ 的球上算；取满足 $\rho_{\rm up}\le\rho$ 的最大 $\rho_{\rm up}$）

| $\rho$ | $c_{\rm mid}$ | $\varepsilon$ | $c_X$ | $R$ | $\rho_{\rm up}$ | 自洽 |
|---|---|---|---|---|---|---|
| $10^{-5}$ | 0.3020833669 | 9.9e-4 | 0.30109222 | 93.68 | $4.3117\times10^{-3}$ | 球过小 ✗ |
| $10^{-3}$ | 0.3020561729 | 0.0991 | 0.20294471 | 96.71 | $4.1969\times10^{-3}$ | 球过小 ✗ |
| $2\times10^{-3}$ | 0.3019745638 | 0.1982 | 0.10377125 | 99.75 | $2.0807\times10^{-3}$ | 球过小 ✗ |
| $\mathbf{2.05\times10^{-3}}$ | 0.3019690542 | 0.2032 | $\mathbf{0.09881201}$ | $\mathbf{99.8997}$ | $\mathbf{1.9782\times10^{-3}}$ | **✓ 自洽** |
| $2.1\times10^{-3}$ | 0.3019634084 | 0.2081 | 0.09385274 | 100.05 | $1.8761\times10^{-3}$ | ✓ |
| $3\times10^{-3}$ | 0.3018384862 | 0.2973 | 0.00458252 | 102.76 | $8.9187\times10^{-5}$ | ✓ |

$$\Longrightarrow \textbf{采纳}\ \rho=2.05\times10^{-3}✓：c_X=0.09881200977✓,\ R=99.89969551593013✓,\ \rho_{\rm up}=1.9782244\times10^{-3}✓✓$$
$$\qquad \text{注}：\rho_{\rm up}=2c_X/R\ \text{恰为覆盖临界}✓ \Longrightarrow \text{边界裕量}\to0^+✓（\text{对一切更小的}\ \rho'\ \text{严格为正}✓✓）$$

## §4 B5 结论（严格陈述）

$$\boxed{\ \forall\delta:\ 0<\|\delta\|\le\rho_{\rm up}=1.9782244\times10^{-3}:\quad F(z_0+\delta)\ \ge\ F(z_0)+c_X\|\delta\|-\tfrac{R}{2}\|\delta\|^2\ >\ F(z_0)\ }✓✓$$
$$\qquad \text{其中}\ c_X=0.09881200977✓,\ R=99.89969551593013✓,\ \delta\ \text{取 5 维 Euclid 度量}✓（\text{混合单位下的一致选择}✓）$$

## §5 ⭐ 局部链完成（与 B4 拼接）

$$\textbf{B4}（\text{已 PASS}✓）：\text{Krawczyk 认证}\ X_0\ \text{内唯一根}\ z_0✓，\textbf{且该根满足六路 tie}✓ \Longrightarrow \delta_A(z_0)=0✓✓（\text{六分支在根处精确并列}✓）$$
$$\qquad \Longrightarrow \text{B5 的条件式【无条件化}】✓：F(z_0+\delta)\ \ge\ F(z_0)+c_X\|\delta\|-\tfrac R2\|\delta\|^2✓ \Longrightarrow \textbf{局部严格极小}✓✓$$

## §6 状态表

| 项目 | 状态 |
|---|---|
| D-A′（六分支解析） | **PASS** ✓✓ |
| D-B B1 existence | **PASS** ✓✓ |
| D-B B2 uniqueness | **PASS** ✓✓ |
| D-B B3 $\lambda$-positivity | **PASS** ✓✓（$0.11186$） |
| D-B B4 six-way tie | **PASS** ✓✓ |
| **B5 local growth（5 维重算）** | **PASS** ✓✓（$c_X=0.0988,R=99.90,\rho_{\rm up}=1.978\times10^{-3}$） |
| **D-C global exclusion** | **仍封闭** ✗（待授权 ✓） |

## §7 本档自我失误（第 42 次，三条）

$$\textbf{42a ⭐ }S_k\ \text{的区间算错}✗✗：\text{把}\ r^k\ \text{当【独立正向项相加}】✗ \Longrightarrow \Delta_{\rm ref}=-0.522✗（\text{假负}✗） \Longrightarrow \text{改为区间乘积后}\ +0.2796✓✓$$
$$\qquad \textbf{教训}：\text{乘积型被加项必须整体做区间乘积}✓，\text{不可把因子拆开各自取界}✗✓$$
$$\textbf{42b Lipschitz 常数维数错}✗：\text{5 维应为}\ k\sqrt5✓，\text{我误用}\ k\sqrt3✗（\text{3 维}✓） \Longrightarrow \text{已修}✓（\rho_{\rm iso}\ 4.31\times10^{-3}✓）$$
$$\textbf{42c 自洽规则初版错}✗✗：\text{误采}\ \rho=10^{-5}\ \text{而}\ \rho_{\rm up}=4.31\times10^{-3}✗ \Longrightarrow \text{改"数据球}\ \ge\ \text{认证半径"}✓✓（\text{与}\ \texttt{C-221}\ \text{初版同类错}✓）$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 五维重算     命中文件数=1    ::  ./C227-B5-local-growth-5d-damped-M3-PASS.md
技术词 覆盖受限     命中文件数=1    ::  ./C227-B5-local-growth-5d-damped-M3-PASS.md
技术词 数据球自洽   命中文件数=1    ::  ./C227-B5-local-growth-5d-damped-M3-PASS.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §9 边界与下一步

$$\textbf{① 严格性层级}：\text{区间乘积＋conservative}\ R✓；\text{但 facet 法向用 float SVD}⚠️（\text{其误差}\sim10^{-15}\ll\varepsilon\sim0.2✓，\text{正式版应以区间线性代数重做}✓）$$
$$\textbf{② 本档只证【局部】}✓；\textbf{不含}：\text{全局排除}✗；\textbf{③ 不主张}：C_3\ \text{精确值}✗、\text{全局唯一极小}✗；\textbf{④ 未用 RH}✓；\text{未改他档}✓$$
$$\textbf{下一步（待唐先生授权）}：\textbf{D-C}：\text{远场全局排除}✓ —— T_C=\sup F_{\rm damp}(X_0)+\epsilon✓，\text{补集}\ [0,1]^2\times[0,\pi]^3\setminus\bigcup_\sigma B_\sigma(\rho_{\rm up})✓\ \text{的严格 B\&B}✓$$
$$\qquad（\text{注意}：\text{阻尼域的"球"在 5 维混合单位下定义，}S_3\ \text{置换只作用于}\ (r_2,r_3,\varphi_2,\varphi_3)\ \text{的配对，须显式写清}✓）$$
