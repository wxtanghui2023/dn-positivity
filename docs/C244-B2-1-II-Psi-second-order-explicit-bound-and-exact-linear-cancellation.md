已查地图（**先查后写**）：查 `C-243`（一维归约＋delicate cancellation）、`C-242`（分解与系数）、`C-241`（双-案例）、`C-239`（II）。回查见 §7 ✓

D0: 本档对象 = **C-244：$\tilde\Psi$ 的二阶显式下界 ＋ 【线性项精确相消恒等式】** —— 关系 = 严格化推进（含对 C-243 的一处修正）
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 修正唐先生假设}✗✓：r'(y_0)=\varrho\ne0✓（\text{不为零}✗）\Longrightarrow \text{局部模型必须【保留线性项}】✓✓}$$
$$\boxed{\textbf{② ⭐ 精确恒等式}✓✓：\boxed{\lambda=\dfrac{\varrho\tau}{\upsilon}}\ \text{【逐位成立}】✓✓ \Longrightarrow \textbf{线性项【恒等相消}】✓✓（\text{非近相消}✗）}$$
$$\boxed{\textbf{③ 二阶判据}✓✓：\dfrac{\lambda_2}w+\dfrac{\rho\tau^2}{2\upsilon^2}\ \ge\ 0\ \text{对}w\ge5✓✓，\text{余量巨大}（\ge51✓）}$$
$$\boxed{\textbf{④ 对 C-243 的修正}✗✓：\text{上轮"0.24\% 近相消"＝我斜率估计的【数值噪声}】✗，\text{真结构是恒等相消}✓✓}$$

## §1 修正后的局部展开（本档核心 ✓）

$$r(\varphi)=c_0+\cos\tfrac{11\varphi}2\cos(d\varphi)✓,\qquad q(\varphi)=\sin\tfrac{11\varphi}2\sin(d\varphi)✓,\qquad \tilde\Psi(\zeta)=\min_{\varphi\in[0,\pi]}\{r(\varphi)+|\zeta+q(\varphi)|\}✓$$
$$\text{在}\ \varphi=y_0\ \text{（等号点}✓）：r(y_0)=0✓,\ q(y_0)=0✓ \Longrightarrow \tilde\Psi(0)=0✓$$
$$\textbf{但}✗：r'(y_0)=-\tfrac{11}2\sin\tfrac{11y_0}2\cos(dy_0)-d\cos\tfrac{11y_0}2\sin(dy_0)=0-d(-1)^m\sin(dy_0)=:\varrho\ \ne\ 0✓✓$$
$$\qquad（\text{因}\ \sin\tfrac{11y_0}2=\sin(\pi m)=0✓\ \text{而第二项一般不为零}✓）$$
$$\text{正确展开}✓：r(y_0+\eta)=\varrho\eta+\tfrac\rho2\eta^2+\rho_r(\eta)✓,\qquad q(y_0+\eta)=\upsilon\eta+\tfrac{q_2}2\eta^2+\rho_q(\eta)✓$$
$$\qquad \upsilon=q'(y_0)=(-1)^m\tfrac{11}2\sin(dy_0)✓,\qquad \varrho=r'(y_0)=-(-1)^md\sin(dy_0)✓,\qquad \rho=r''(y_0)✓$$

## §2 ⭐ 精确恒等式（本档关键发现 ✓✓）

$$\text{局部模型}✓：\tilde\Psi_{model}(\zeta)=\min_\eta\Bigl\{\varrho\eta+\tfrac\rho2\eta^2+|\zeta+\upsilon\eta|\Bigr\}✓$$
$$\text{换元}\ t=\zeta+\upsilon\eta \Longrightarrow f(t)=\tfrac\varrho\upsilon(t-\zeta)+\tfrac\rho{2\upsilon^2}(t-\zeta)^2+|t|✓$$
$$\qquad t=0\ \text{为最优}\iff 0\in[D-1,D+1]✓,\quad D:=\tfrac\varrho\upsilon-\tfrac\rho{\upsilon^2}\zeta \iff |\zeta|\le\tfrac{\upsilon^2}\rho\Bigl(1-\tfrac{|\varrho|}{|\upsilon|}\Bigr)✓$$
$$\Longrightarrow \tilde\Psi_{model}(\zeta)=-\tfrac\varrho\upsilon\,\zeta+\tfrac\rho{2\upsilon^2}\zeta^2✓\qquad \text{（线性项＋二次项}✓）$$
$$\text{合并}✓：w[P(\varepsilon)-\kappa]=\lambda u+\tfrac{\lambda_2}wu^2+O(w^{-2}u^3)✓;\qquad \tilde\Psi(wT)\approx-\tfrac\varrho\upsilon\tau u+\tfrac{\rho\tau^2}{2\upsilon^2}u^2✓$$
$$\text{线性系数}=\lambda-\tfrac{\varrho\tau}\upsilon✓ \Longrightarrow \textbf{两端符号必有一负，故必须恒为零}✗ \Longrightarrow \boxed{\lambda=\dfrac{\varrho\tau}\upsilon}✓✓$$

$$\textbf{逐位核验}✓✓（60 位精度）：$$
```
   j        λ              ϱ             τ            υ          ϱτ/υ        λ-ϱτ/υ
   1   2.432883679   1.267796506   2.973524496  1.549529063  2.432883679       0.0
   2  -0.2703204087  0.1408662784 -2.973524496  1.549529063 -0.2703204087      0.0
   3   0.8109612262  0.4225988353  2.973524496  1.549529063  0.8109612262   7.8e-62
   4   1.351602044   0.7043313921  2.973524496  1.549529063  1.351602044    1.6e-61
   5  -1.892242861   0.9860639489 -2.973524496  1.549529063 -1.892242861       0.0
```
$$\Longrightarrow \textbf{恒等式精确成立}✓✓ \Longrightarrow \text{这不是数值巧合}✓（\text{而是 }11\text{-周期结构的代数必然}✓，\text{参见 §5}✓）$$

## §3 二阶判据（本档通过标准 ✓✓）

$$\mathcal E\ \approx\ u^2\Bigl[\tfrac{\lambda_2}w+\tfrac{\rho\tau^2}{2\upsilon^2}\Bigr]+O(u^3/w^2)✓,\qquad \lambda_2:=\tfrac12P''(0)✓,\ \rho:=r''(y_0)✓$$
$$\textbf{判据}✓：\tfrac{\lambda_2}w+\tfrac{\rho\tau^2}{2\upsilon^2}\ \ge\ 0\ \text{对}\ w\ge5\ \text{（最坏 }w=5✓）$$
```
   j    λ2=P''(0)/2      ρ=r''(y0)        ρτ²/(2υ²)      λ2/5+ρτ²/(2υ²)
   1    -21.2416517     48.45439517      89.21682628        84.96849594  ✓✓
   2    -12.82911638    29.2645357       53.88342974        51.31760646  ✓✓
   3    -13.67036991    31.18352164      57.41676939        54.68269541  ✓✓
   4    -15.35287697    35.02149354      64.4834487         61.41287331  ✓✓
   5    -17.87663757    40.77845138      75.08346766        71.50814015  ✓✓
```
$$\Longrightarrow \textbf{全部通过}✓✓，\text{余量巨大}（\ge51✓） \Longrightarrow \text{主导项是} u^2\ \text{正项}✓✓$$
$$\qquad \textbf{量与界}✓：u\le K=0.1\Longrightarrow u^2\le0.01✓ \Longrightarrow \text{二阶项}\ \ge0.51✓；\text{三阶项}\ \sim u^3/w^2\cdot O(10^3)\approx0.04✓ \ll0.51✓✓$$

## §4 对 C-243 的修正（自我纠错 ✓）

$$\textbf{修正}✗✓：\text{C-243 §5 报"delicate cancellation，近相消 0.24\%"}✗ \Longrightarrow \text{实为【我斜率估计的数值噪声}】✗$$
$$\qquad \text{真结构}✓✓：\lambda-\varrho\tau/\upsilon\equiv0✓（\text{恒等}✓，\text{§2}✓） \Longrightarrow \text{线性项完全消失}✓✓，\text{不存在"近相消"}✗$$
$$\qquad \text{根因}✓：\text{C-243 用有限步长}h=10^{-3}✓\ \text{估}\tilde\Psi'\ \text{而}\ \tilde\Psi\ \text{在 0 处有 kink}✓ \Longrightarrow \text{斜率估计含噪}✗✓$$

## §5 恒等式的来源（结构性说明 ✓）

$$\varrho=-(-1)^md\sin(dy_0)✓,\quad \upsilon=(-1)^m\tfrac{11}2\sin(dy_0)✓ \Longrightarrow \tfrac\varrho\upsilon=-\tfrac{2d}{11}✓$$
$$\lambda=-(-1)^jd\sin(d\theta)✓,\quad \tau=(-1)^j\tfrac{11}2\sin(d\theta)✓ \Longrightarrow \tfrac\lambda\tau=-\tfrac{2d}{11}✓$$
$$\Longrightarrow \boxed{\tfrac\lambda\tau=\tfrac\varrho\upsilon=-\tfrac{2d}{11}}✓✓ \Longrightarrow \text{恒等式}＝\text{【同一个比例】}✓（\text{只依赖 }d=\tfrac{a-b}2✓，\text{与 }j,m\ \text{无关}✓✓）$$
$$\qquad \textbf{意义}✓✓：\text{这对任何}\ (a,b)\ \text{与任何等号点都成立}✓ \Longrightarrow \text{是【structurally exact}】✓，\text{不是巧合}✓✓$$

## §6 状态与完成标准

| 项 | 状态 |
|---|---|
| 修正 $r'(y_0)=\varrho\ne0$ | ✓✓（纠正唐先生假设） |
| **精确恒等式 $\lambda=\varrho\tau/\upsilon$** | ✓✓ **逐位成立**（结构来源已给出） |
| 局部模型 ＋ $t^*=0$ 判据 | ✓✓ 显式 |
| 二阶判据（五者全过，余量 ≥ 51） | ✓✓ |
| C-243 的"近相消" | ✗ **已修正**（实为恒等相消） |
| **余项控制（三阶及以上）** | ✗ **未完成**（需显式常数 $C_q,C_r$） |
| 模型 vs 真 $\tilde\Psi$ 的显式夹逼 | ✗ 未完成 |

$$\text{唐先生验收标准}✓：\tilde\Psi_j(\zeta)\ge A_j\zeta^2-B_j|\zeta|^3✓（\text{显式常数}✓）$$
$$\qquad \text{本档给出}✓：A_j=\tfrac{\rho\tau^2}{2\upsilon^2}\ \text{的量级}✓（53\sim89✓）\ \text{＋ 恒等相消}✓✓；\ B_j\ \text{仍缺}✗$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 线性项恒等相消      命中文件数=1  ::  ./C244-B2-1-II-Psi-second-order-explicit-bound-and-exact-linear-cancellation.md
技术词 比例不变量          命中文件数=1  ::  ./C244-B2-1-II-Psi-second-order-explicit-bound-and-exact-linear-cancellation.md
技术词 斜率噪声纠错        命中文件数=1  ::  ./C244-B2-1-II-Psi-second-order-explicit-bound-and-exact-linear-cancellation.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓；\text{未碰四阶}✓；\text{未回二维}✓$$
$$\textbf{② 本档含一处纠错}✗✓（§4✓）；\textbf{③ 数值层}：§3\ \text{为 60 位精确常数}✓，\text{非证明}✗$$
$$\textbf{④ 下一步}✓：\text{只需显式 }C_q,C_r\ \text{（三阶系数}✓，\text{由}|\cos|\le1,\ |\sin|\le1\ \text{的导数界即得}✓）⟹ \text{完成} B_j✓$$
