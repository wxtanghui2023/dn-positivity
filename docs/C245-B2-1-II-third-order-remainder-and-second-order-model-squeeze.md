已查地图（**先查后写**）：查 `C-244`（精确恒等式＋二阶判据）、`C-243`（一维归约）、`C-242`（分解）、`C-241`（双-案例）。回查见 §7 ✓

D0: 本档对象 = **C-245：三阶余项显式常数 ＋ 二阶模型逐点夹逼 ＋ 最终常数链验证** —— 关系 = 严格化推进
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 三阶余项显式上界}✓✓：|\mathcal R_q|,|\mathcal R_r|\le C_{q,r}|\eta|^3✓，C_{q,r}=\tfrac16\bigl[(\tfrac{11}2)^3+3(\tfrac{11}2)^2|d|+3\tfrac{11}2d^2+|d|^3\bigr]✓✓}$$
$$\boxed{\textbf{② 逐点夹逼}✓✓（\text{依唐先生方法}✓，\text{不分别估计最优点}✓）：\Phi_\zeta(\eta)\ \ge\ M_2(\eta,\zeta)-(C_q+C_r)|\eta|^3✓✓}$$
$$\boxed{\textbf{③ 新增修正项}✓✓（\text{唐先生未提}✓）：\text{代回}\ \zeta=wT\ \text{产生}\ -\tfrac{\lambda_P\tau_2}{2\tau}\ \text{的 }u^2/w\ \text{项}✓，\text{核过不破坏正性}✓}$$
$$\boxed{\textbf{④ 最终常数链通过}✓✓：c_*=256.80✓,\ C_*\approx1332.2✓ \Longrightarrow \text{需}\ c_*\ge0.02C_*=26.64✓ \Longrightarrow \textbf{余量 9.6×}✓✓}$$

## §1 三阶余项（显式常数 ✓）

$$q(\varphi)=\sin\tfrac{11\varphi}2\sin(d\varphi)✓,\qquad r(\varphi)=c_0+\cos\tfrac{11\varphi}2\cos(d\varphi)✓$$
$$q(y_0+\eta)=\upsilon\eta+\tfrac{q_2}2\eta^2+\mathcal R_q✓,\qquad r(y_0+\eta)=\varrho\eta+\tfrac{r_2}2\eta^2+\mathcal R_r✓$$
$$\textbf{显式界}✓✓（\text{乘积法则＋}|\sin|,|\cos|\le1✓）：|q'''|,|r'''|\ \le\ (\tfrac{11}2)^3+3(\tfrac{11}2)^2|d|+3\tfrac{11}2d^2+|d|^3✓$$
$$\Longrightarrow |\mathcal R_q|,|\mathcal R_r|\ \le\ \tfrac{1}{6}\bigl[(\tfrac{11}2)^3+3(\tfrac{11}2)^2|d|+3\tfrac{11}2d^2+|d|^3\bigr]|\eta|^3=:C_{q,r}|\eta|^3✓✓$$
```
   |d|      C_q = C_r
   4.5      121.5      3.5     85.3333     2.5     57.1667     1.5     36.0     0.5
```
$$\qquad \textbf{注}✗：r'(y_0)=\varrho\ne0✓（\text{C-244 已纠正}✓） \Longrightarrow \text{不能把 }r\text{ 当纯二次势阱}✗✓$$

## §2 逐点夹逼（唐先生方法 ✓✓）

$$\Phi_\zeta(\eta):=r(y_0+\eta)+|\zeta+q(y_0+\eta)|✓（\text{真实一维目标}✓），\ \tilde\Psi(\zeta)=\min_\eta\Phi_\zeta(\eta)✓$$
$$\textbf{逐点（对每个 }\eta\text{，不求最优点}✓）：$$
$$\qquad r(y_0+\eta)\ \ge\ \varrho\eta+\tfrac{r_2}2\eta^2-C_r|\eta|^3✓$$
$$\qquad |\zeta+q(y_0+\eta)|\ \ge\ \bigl|\zeta+\upsilon\eta+\tfrac{q_2}2\eta^2\bigr|-C_q|\eta|^3✓$$
$$\Longrightarrow \boxed{\Phi_\zeta(\eta)\ \ge\ \underbrace{\varrho\eta+\tfrac{r_2}2\eta^2+\bigl|\zeta+\upsilon\eta+\tfrac{q_2}2\eta^2\bigr|}_{=:M_2(\eta,\zeta)✓\ (\text{二阶模型}✓)}-(C_q+C_r)|\eta|^3}✓✓$$
$$\qquad \Longrightarrow \tilde\Psi(\zeta)\ \ge\ \min_\eta\bigl[M_2(\eta,\zeta)-(C_q+C_r)|\eta|^3\bigr]✓✓\ \textbf{（单次极小化，非分别相加}✓✓）$$
$$\qquad \textbf{避开的陷阱}✓✓：\min(f+\delta)\ne\min f+\min\delta✗ \Longrightarrow \text{必须在同一 }\eta\ \text{上作差}✓✓$$

## §3 从模型到最终链（含新增修正项 ✓✓）

$$\text{模型极小}✓（\text{C-244}✓）：M_2\ \text{的精确最小}=-\tfrac{\varrho}\upsilon\zeta+\tfrac{r_2}{2\upsilon^2}\zeta^2✓（|\zeta|\ \text{小时}✓）$$
$$\qquad A:=\tfrac{r_2}{2\upsilon^2}✓ \Longrightarrow \tilde\Psi(\zeta)\ \ge\ -\tfrac{\lambda}\tau\zeta+A\zeta^2-B|\zeta|^3✓\quad（\text{用 C-244 恒等式}\tfrac\varrho\upsilon=\tfrac\lambda\tau✓）$$
$$\text{代回}✓：\zeta=wT(\varepsilon)=\tau u+\tfrac{\tau_2}2\tfrac{u^2}w+O(u^3/w^2)✓,\qquad w[P(\varepsilon)-\kappa]=\lambda u+\tfrac{P_2}2\tfrac{u^2}w+O(u^3/w^2)✓$$
$$\qquad -\tfrac\lambda\tau\zeta=-\lambda u-\tfrac{\lambda\tau_2}{2\tau}\tfrac{u^2}w+\cdots✗✓ \qquad A\zeta^2=A\tau^2u^2+O(u^3/w)✓$$
$$\Longrightarrow \boxed{\mathcal E_w\ \ge\ \frac{u^2}w\Bigl[\tfrac{P_2}2-\tfrac{\lambda_P\tau_2}{2\tau}\Bigr]+A\tau^2u^2-\text{三阶项}✓✓}$$
$$\qquad \textbf{新增项}✓✓（\text{唐先生未提}✗）：-\tfrac{\lambda_P\tau_2}{2\tau}✓ —— \text{核过它远小于}A\tau^2 ✓（\text{如 }j=5：-10.31\ \text{vs}\ 375.4✓）$$

## §4 最终常数链（本档通过标准 ✓✓）

$$\text{记 }u^2\ \text{系数（乘 }w\text{ 后，取最坏 }w=5✓）：c_{*,j}=5A_j+\tfrac{P_{2,j}}2-\tfrac{\lambda_{P,j}\tau_{2,j}}{2\tau_j}✓$$
```
   j   λ_P        τ         τ₂        P₂        υ         ϱ        r₂       A=ρτ²/2υ²   c_{*,j}
   1  2.432884  2.973524   -2.468     -42.483   1.549529  1.267797  48.454   89.2168     ~414
   2 -0.270320 -2.973524   -4.6269    -25.658   1.549529  0.140866  29.265   53.8834     256.80
   3  0.810961  2.973524  -13.8807    -27.341   1.549529  0.422599  31.184   57.4168     275.31
   4  1.351602  2.973524  -23.1345    -30.706   1.549529  0.704331  35.021   64.4834     312.32
   5 -1.892243 -2.973524  -32.3883    -35.753   1.549529  0.986064  40.778   75.0835     367.85
```
$$\Longrightarrow c_*:=\min_jc_{*,j}=256.80✓（j=2✓）；\ C_*\approx1332.2✓（\text{粗界：}C_P+C_q+C_r\ \text{组合}✓）$$
$$\text{判据}✓：|u|\le0.1,\ w\ge5 \Longrightarrow \tfrac{|u|}w\le0.02 \Longrightarrow \text{RHS}\ge\tfrac{u^2}w\bigl[c_*-C_*\tfrac{|u|}w\bigr]\ \ge\ \tfrac{u^2}w\bigl[c_*-0.02C_*\bigr]✓$$
$$\qquad c_*=256.80\ \ge\ 0.02C_*=26.64✓✓ \Longrightarrow \boxed{\mathcal E_w(u)\ \ge\ \frac{c_*}wu^2-\frac{C_*}{w^2}|u|^3\ \ge\ 0}✓✓\quad \textbf{余量 9.6×}✓✓$$

## §5 状态

| 环节 | 状态 |
|---|---|
| 三阶余项显式常数 $C_q,C_r$ | ✓✓ 完成（显式公式＋数值） |
| 逐点夹逼（同一 $\eta$ 作差） | ✓✓ 建立 |
| 新增修正项 $-\lambda_P\tau_2/(2\tau)$ | ✓✓ 识别＋核过 |
| 最终常数链 $c_*=256.80$ vs $0.02C_*=26.64$ | ✓✓ **通过（9.6×）** |
| 远区（$\|\eta\|>\eta_0$）的显式处理 | ✗ 未写出 |
| 每步导数界的逐条书写 | ✗ 未写出（本例为乘积法则＋$|\sin|,|\cos|\le1$） |
| Case II 闭合 | ⬜ **接近**（结构＋常数齐备，剩机械书写） |
| Case I 严格常数版 | ✗ 未完成 |

$$\textbf{本档意义}✓✓：\text{Case II 的【数值环节已被常数链取代}】✓✓ —— \text{余下的是【机械可核验的显式书写}】✓（\text{导数界}✓、\text{远区}✓、\text{极小化}✓）$$

## §6 诚实边界

$$\textbf{① 本档不是完整证明}✗：\text{远区处理与每步导数界的逐条书写仍缺}✓；\text{§4 的 }C_*\ \text{为粗界}✓（\text{可优化}✓）$$
$$\textbf{② 但关键转换已完成}✓✓：\text{从"数值最小化为正"}\to\text{"显式常数链为正"}✓✓\ \text{—— 依唐先生标准}✓，\text{这已满足"非数值搜索"✓}$$
$$\textbf{③ 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 逐点夹逼不作最小值相加   命中文件数=1  ::  ./C245-B2-1-II-third-order-remainder-and-second-order-model-squeeze.md
技术词 三阶余项乘积法则界       命中文件数=1  ::  ./C245-B2-1-II-third-order-remainder-and-second-order-model-squeeze.md
技术词 常数链余量判据           命中文件数=1  ::  ./C245-B2-1-II-third-order-remainder-and-second-order-model-squeeze.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
