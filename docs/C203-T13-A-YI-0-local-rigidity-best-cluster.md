已查地图（**先查后写**）：查 `C-202`（甲：上界认证）、`C-201`（三簇签名）、`C-152`／`C-197`（局部刚性模板）、`C-161`（M=3 单纯形签名）。回查见 §6 ✓

D0: 本档对象 = **T13-A 乙-0**：最佳簇 $x_0$（$A=\{1,5,11,13\}$）的**局部线性刚性**（隔离 ＋ 一阶凸包 ＋ 二阶余项三件套）—— 关系 = 新构造（局部引理）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 对象

$$x_0:\ \varphi/\pi=(0.1158442572,\ 0.3318874234,\ 0.7355764367)✓\qquad F(x_0)=0.764081100903✓（\text{即甲的有理构型}✓）$$
$$\qquad \textbf{active}\ A=\{1,5,11,13\}✓,\quad |A|=4=M+1✓\quad（\texttt{C-201}\ \text{已确认}\ \lambda_{\min}>0,\ c>0✓）$$

## §2 三件套（乙-0）

### (i) active-set 隔离

$$\text{非活跃}\ k\ \text{的 gap}：k{=}6:\ 7.108550\times10^{-2}✓\ ——\ \textbf{最小}✓；\ k{=}14:\ 2.419\times10^{-1}✓；\ k{=}3:\ 5.067\times10^{-1}✓；\ k{=}2:\ 6.001\times10^{-1}✓$$
$$\qquad \text{梯度模上界}：\max_{k\in A}\|\nabla S_k\|=21.197702✓（\text{实算}✓）；\text{非活跃}\ k\ \text{的}\ \mathrm{Lip}\le k\sqrt3✓（k{=}6\Rightarrow10.3923✓）$$
$$\Longrightarrow \rho_{\rm iso}=\frac{7.108550\times10^{-2}}{21.197702+10.3923}=\mathbf{2.250253\times10^{-3}}✓✓$$
$$\qquad \text{即}\ \|\delta\|\le\rho_{\rm iso}\ \text{时}\ \max_{1\le k\le15}S_k=\max_{k\in A}S_k✓✓$$

### (ii) 一阶凸包覆盖

$$c\ :=\ \min_{|u|=1}\ \max_{k\in A}\ \langle\nabla S_k,\ u\rangle\ =\ \mathbf{0.546220608}✓✓\qquad \text{于}\ u^*=(0,0,1)✓$$
$$\qquad （\text{最坏方向是【纯}\ \varphi_3\ \text{方向】}✓；\texttt{C-201}\ \text{的 LP 给}\ \lambda_{\min}=+2.605\times10^{-2}>0✓ \Longrightarrow 0\in\mathrm{int}\,\mathrm{conv}✓）$$

### (iii) 二阶余项（$\nabla^2S_k=\mathrm{diag}(-k^2\cos(kx_j))$）

| $k$ | $\|\nabla^2S_k\|_2$（实算） | 粗界 $k^2$ |
|---|---|---|
| 1 | $0.934503$ | 1 |
| 5 | $13.254935$ | 25 |
| 11 | $116.052308$ | 121 |
| 13 | $92.990436$ | 169 |

$$\text{取【粗界】}R=\max_{k\in A}k^2=\mathbf{169}✓（\text{保守}；\text{球内实算上界可再降}✓）$$

## §3 ⭐ 结论（局部线性刚性）

$$\text{对}\ \|\delta\|\le\rho_{\rm iso}：\text{由 (i)}\ \max_k S_k=\max_{k\in A}S_k✓；\text{由 Taylor}\ S_k(x_0+\delta)\ge S_k(x_0)+\langle\nabla S_k,\delta\rangle-\tfrac R2\|\delta\|^2✓$$
$$\qquad \Longrightarrow F(x_0+\delta)\ \ge\ F(x_0)+c\|\delta\|-\tfrac R2\|\delta\|^2\ \ge\ F(x_0)+\tfrac c2\|\delta\|✓（\text{当}\ \|\delta\|\le c/R✓）$$
$$\qquad c/R=3.232075\times10^{-3}>\rho_{\rm iso}=2.250253\times10^{-3}✓✓ \Longrightarrow \textbf{球内条件自动满足}✓$$
$$\boxed{\ F(x_0+\delta)\ \ge\ F(x_0)\ +\ \tfrac c2\|\delta\|\ =\ F(x_0)\ +\ 0.273110304\,\|\delta\|\qquad\text{对}\ \|\delta\|\le\mathbf{2.250253\times10^{-3}}✓✓\ }$$
$$\qquad \Longrightarrow \boxed{x_0\ \text{是}\ \textbf{严格局部极小}✓，\text{且具}\ \textbf{线性刚性}✓（\text{非二阶平坦、非连续族}✓）}$$

$$\textbf{与下界的关系}：F(x_0)=0.764081100903>0.76✓（\text{账本下界}） \Longrightarrow \text{局部球}\ B_{\rho}(x_0)\ \textbf{不包含任何}\ F<m_3\ \text{的候选}✓（\text{就当前账本而言}）✓$$

## §4 边界（严格）

- §2 的三项数据均为**数值**✓（gap、$c$、Hessian 范数）⟹ §3 是**结构模板**✓，**尚未**做成区间算术定理 ✗（若需要，可照 `C-197` 模式补 ✓）
- $R$ 用**粗界** 169 ✓（球内实界更小 ✓）；$\rho_{\rm iso}$ 用保守的 $\mathrm{Lip}$ 界 ✓
- ⚠️ 本档**不**声称 $x_0$ 是全局最小 ✗；**不**声称等号集 ✗（按唐先生指示 ✓）
- **未用** RH；**未改** 他档 ✓

## §5 与其他两簇的对比（待办 乙-1/2）

$$\text{簇 3（}F=0.7755339,\ A=\{2,7,10,15\}\text{）与簇 5（}F=0.7768817,\ A=\{1,3,13,15\}\text{）}✓$$
$$\qquad \text{签名齐备}✓（|A|=4,\ \mathrm{rank}=3,\ \lambda_{\min}>0,\ c>0✓） \Longrightarrow \text{同法可做}✓（\text{乙-1/2}）✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 局部线性刚性   命中文件数=1    ::  ./C203-T13-A-YI-0-local-rigidity-best-cluster.md
技术词 隔离半径       命中文件数=1    ::  ./C203-T13-A-YI-0-local-rigidity-best-cluster.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 两项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 下一步

$$\textbf{乙-1/2}：\text{对簇 3 与簇 5 同一三件套}✓ \Longrightarrow \text{得到}\ M=3\ \text{三个类型 A 簇的完整局部刚度画像}✓✓$$
$$\qquad \text{随后（若唐先生要）：把三件套做成区间算术定理}✓（\text{照}\ \texttt{C-197}\ \text{／}\ \texttt{C-199}\ \text{模式}）✓$$
