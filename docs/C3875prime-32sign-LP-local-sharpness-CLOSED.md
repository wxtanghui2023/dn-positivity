已查地图（**先查后写**）：`C3875`（**结构 YES／定量 VOID；`K = 648`** ✓✓）、`C-3872`（**Gordan** ✓✓）、`C-3873`（**机制命题；LOCAL-ONLY 标签** ✓✓）、`C-3868`（**`\lambda,\omega`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-77：C-3875′ —— 32-sign LP 认证（`\eta_1` 严格下界 ＋ 封口半径）**（唐先生 2026-09-21 23:07 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 问题与符号分解}✓✓：\eta = \min_{\|u\|_2 = 1}\max_{i \le 6}(Gu)_i✓；\ \text{正齐次} \Longrightarrow \text{尺度不变}✓✓$$

$$\qquad \text{令}\ u = s \odot w✓,\ s \in \{\pm1\}^5✓,\ w_j \ge 0✓,\ \sum_jw_j = 1✓✓$$

$$\textbf{② ⭐ }\ell_1\ \textbf{归一化的等价性（唐先生要求显式证明}✓✓**）：\forall u \ne 0✓,\ \text{置}\ w = |u|/\|u\|_1✓ \Longrightarrow u = s \odot w\ \text{唯一落入某 sign-simplex}✓✓；$$

$$\qquad \text{反向}\ \forall w\ \text{给出非零}\ u✓✓ \Longrightarrow \boxed{\eta > 0 \iff \eta_1 > 0}✓✓$$

$$\qquad \text{且}\ \text{比率传递}✓✓：\text{ratio}_2(u) = \text{ratio}_1(u)\cdot\frac{\|u\|_1}{\|u\|_2} \ge \eta_1\cdot1✓（\|u\|_1 \ge \|u\|_2✓） \Longrightarrow \boxed{\eta_2 \ge \eta_1}✓✓$$

$$\textbf{③ 每个 LP 是}\textbf{等价 LP}✓✓（\textbf{不是}先前错误的"共同严格 margin"形式✗✓）:\ \min t\ \text{s.t.}\ G(s \odot w) \le t\mathbf1✓,\ w \ge 0✓,\ \mathbf1^{\top}w = 1✓✓$$

$$\qquad \boxed{\eta_1 = \min_{s}\ t_s^*}✓✓（\text{32 个 LP}✓）$$

$$\textbf{④ 数值结果}✓✓：\text{32 个 LP}\ \textbf{全部 status 0}✓✓；\ \boxed{\min_s t_s^* = 0.076644303068}✓✓,\ \max_s t_s^* = 25.175858796✓$$

$$\qquad \text{argmin}\ s = (-1,-1,-1,-1,-1)✓;\ \text{primal}\ w = (0.3289024,\ 0.16037046,\ 0.19471226,\ 0.15658896,\ 0.15942592)✓,\ \|w\|_1 = 1✓✓$$

$$\qquad \text{对偶（}\textbf{符号约定修正后}✓）:y = (0.338423,\ 0,\ 0.270663,\ 0.315685,\ 0.027259,\ 0.047970)✓,\ \sum y = 1✓,\ y \ge 0✓✓$$

$$\textbf{⑤ Sanity（唐先生的简化}✓✓**）：\text{由}\ G^{\top}y_{\mathrm{KKT}} = 0✓（y_{\mathrm{KKT}} > 0✓）\Longrightarrow \text{六分量不可能全} < 0 \Longrightarrow \boxed{t_s^* \ge 0}✓✓$$

$$\qquad \text{实测}✓✓：\text{全部}\ t_s^* \ge 0✓；\ \boxed{t_s^* < 10^{-9}\ \text{的类数} = 0}✓✓ \Longrightarrow \text{无退化类}✓,\ \text{与 Gordan}\ \textbf{一致}✓✓$$

$$\textbf{⑥ ⭐ 严格有理下界}✓✓：\text{变分弱对偶}✓✓：\text{对任意}\ y \in \text{simplex}✓：\ t_s^* = \min_w\max_i(G_sw)_i \ge \min_w w^{\top}G_s^{\top}y = \boxed{\min_j (G_s^{\top}y)_j}✓✓$$

$$\qquad \text{（}\textbf{只需}\ y \ge 0✓,\ \sum y = 1✓ —— \textbf{不需}站性}✓✓，故证书极简✓）$$

$$\qquad \text{取 LP 对偶}\ y\ \text{化为有理}✓,\ \text{配合}\ G\ \text{的有理包围}（\text{余量}\ 10^{-30}✓,\ 50\ \text{dps}\ \text{截断误差} \sim10^{-45}✓） \Longrightarrow$$

$$\qquad \boxed{\underline{\eta} = 0.076644303067798235521\ldots > 0}✓✓\ \text{（}\textbf{严格有理}✓✓）$$

$$\textbf{⑦ 封口半径与判词}✓✓：\boxed{\rho_{\mathrm{cert}} = \frac{\underline{\eta}}{648} = 1.18278\times10^{-4}}✓✓\ \text{（}\phi\ \text{坐标，}\ell_2✓）$$

$$\qquad \text{最紧坐标的}\ x\ \text{半宽} = 7.99\times10^{-5}✓✓ \Longrightarrow \boxed{\textbf{LOCAL-SHARP-CLOSED}}✓✓$$

$$\qquad \Longrightarrow \textbf{不再做二阶}✓✓（\text{按唐先生令}✓）$$

## §1 记录（数字驱动 ✓✓）

```
32 sign LP: statuses all 0 ; min_s t_s* = 0.076644303068 ; max_s t_s* = 25.175858796
sanity: all t_s* >= 0 ; count(t_s* < 1e-9) = 0
argmin s = (-1,-1,-1,-1,-1) ; w = (0.3289024, 0.16037046, 0.19471226, 0.15658896, 0.15942592)
dual y (sign fixed) = (0.338423, 0, 0.270663, 0.315685, 0.027259, 0.047970) ; sum y = 1 ; y >= 0
eta_lb (rational) = 0.076644303067798235521... ; strictly positive True
K = 648 ; rho_cert = eta_lb/648 = 1.18278e-4 (phi, L2) ; tightest x-halfwidth = 7.985461e-05
VERDICT LOCAL-SHARP-CLOSED : True
```
- 脚本 ✓：`scripts/c380_77_C3875p_32sign.py`、`c380_77b_lowerbound.py`✓；输出 ✓：`out_c380_77.txt`、`out_c380_77b.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 32-sign 分解等价性 ✓ | **CLOSED（显式证明）** ✓✓ |
| 32 个 LP（等价形式） ✓ | **CLOSED（全部 status 0）** ✓✓ |
| Sanity `t_s^* \ge 0` ＋ 无退化类 ✓ | **CLOSED** ✓✓ |
| primal／dual 证书 ✓ | **CLOSED** ✓✓ |
| **严格有理下界 `\underline\eta`** ✓ | **`0.0766443030678... > 0`** ✓✓ |
| 封口半径 `\rho_{\mathrm{cert}}` ✓ | **`1.18278\times10^{-4}`（φ, ℓ₂）** ✓✓ |
| **判词** ✓ | **LOCAL-SHARP-CLOSED** ✓✓ |
| 二阶 ✓ | **不需要** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **只**对 `\sigma = (-1,1,1,-1,1)` 与 `x^*` 成立（**LOCAL-ONLY**）✓✓
- **不**声称其他 `\sigma` 类／全部 `E_{\mathrm{even}}`／全局 `V_\sigma` ✓
- **不**把随机方向的 `0.448803`（上界）当认证值 ✓
- **不**声称远端区域已封（**远区**仍需全局排斥 ✓）
- 认证约定显式声明 ✓：系数取自 50 dps `mpf`＋余量 `10^{-30}`；弱对偶证书**只需** `y \ge 0,\ \sum y = 1` ✓✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}做二阶✗；\ \textbf{不}用}\ c_* = 1/L\ \text{（本档不需要}✓）；\ \textbf{不}碰远区全局排斥✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 32符号型认证 命中文件数=0    :: 
技术词 严格有理下界 命中文件数=0    :: 
技术词 封口半径     命中文件数=1    :: ./C3875-local-sharpness-first-cut-structural-yes-quantitative-void.md
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{拼装（唐先生⑤）}✓✓：E_{\mathrm{even}} = \underbrace{(E_{\mathrm{even}} \setminus B_\rho)}_{\text{远区：全局排斥（未来）}} \cup \underbrace{(E_{\mathrm{even}} \cap B_\rho)}_{\text{近区：}\textbf{本档 CLOSED}}✓✓$$
$$\qquad \Longrightarrow \text{下一步回到}\ \textbf{C-3874-A 的远区}✓：\text{寻求}\ B_\rho(x^*)^{\mathrm c}\ \text{上的严格下界}✓✓$$
$$\qquad \Longrightarrow \text{全部完成后}\ \boxed{V_\sigma = c_0}✓✓\ \text{—— 比"二阶局部封口"干净得多}✓✓$$
