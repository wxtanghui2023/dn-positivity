# V260 · **极坐标／应力张量路线：直接计算 —— 两个正面事实 ＋ 一条结构性毙掉理由** —— ⭐⭐ **直接计算一（本档）**：对称离轴对 $\rho_\pm=\tfrac12\pm\delta+i\gamma$ 的**中点** $m=\tfrac12+i\gamma$ **恰在临界线上**，且是 $u=\log|\zeta|$ 的**临界点**（$\nabla u(m)=0$），且为 **saddle**：沿 $\sigma$ 方向是**局部极大**、沿 $t$ 方向**局部极小**（$u\approx\text{const}-\frac{x^2-y^2}{\delta^2}$）✓✓✓；⭐⭐ **直接计算二（本档，新恒等式）**：$$u_\sigma(\sigma,t)+u_\sigma(1-\sigma,t)=\partial_\sigma\log|\chi(\sigma+it)|$$ 且**临界线上** $$\boxed{u_\sigma(\tfrac12,t)=-\theta'(t)}$$（$\theta$ ＝ Riemann–Siegel theta）—— **完全显式、零零点信息** ✓✓✓；⭐⭐⭐⭐ **结构性毙掉（本档核心）**：$\log|\zeta|$ 的**无迹无散应力张量**等价于**单个解析函数** $(\zeta'/\zeta)^2$ ⟹ 其通量／守恒量的计算就是**留数＝辐角原理** ⟹ **落入 (A) 家族（`V188`）** ✓✓✓✓；⭐⭐⭐ **死亡测试答案**：对称对的横向通量**并不相消**，但**不相消的那部分完全显式**（唯一 $\sigma$-不对称因子 $|\chi|$）⟹ **archimedean／$\chi$ 通道（`V215`(c)）** ⟹ **DEAD** ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 22:55：**极坐标路线**（$u=\log|\zeta|$、$\varphi=\arg\zeta$ 为共轭调和场；零点＝$u$ 的对数奇点＋$\varphi$ 的绕转奇点；FE 反射下的局部应力／守恒律）；**§10 明令：直接计算一般对称对 $\rho=\tfrac12+\delta+i\gamma$、$1-\rho=\tfrac12-\delta+i\gamma$ 产生的 stress tensor／flux，若通量完全相消则立即 DEAD；若存在严格非零 $\delta$-依赖守恒量，再过四关** ✓✓
> 纪律 ✓ **直接算，不造抽象模型**（唐先生明令）✓；未用 RH 作推导 ✓；未跑 Lean ✓；**零数值（全部符号／初等）** ✓｜编号 ✓ **V260**

---

## §1 采纳的极坐标设置

$$\zeta(s)=R(s)e^{i\varphi(s)},\quad s=\sigma+it;\qquad u=\log R=\log|\zeta|,\ \varphi=\arg\zeta ✓$$
$$\qquad \log\zeta=u+i\varphi\ \textbf{局部解析} \Longrightarrow \textbf{Cauchy–Riemann}：\boxed{u_\sigma=\varphi_t,\quad u_t=-\varphi_\sigma} ✓✓$$
$$\qquad \text{即：}\textbf{模与相位不是两个独立变量，而是一对共轭调和场} ✓✓$$
$$\text{零点}\ \rho\ \text{（阶}\ m\text{）附近}：\zeta=(s-\rho)^m g \Longrightarrow u=m\log|s-\rho|+O(1),\ \varphi=m\arg(s-\rho)+\arg g ✓$$
$$\qquad \Longrightarrow \oint_{C_\rho}d\varphi=2\pi m \qquad（\textbf{拓扑缺陷／vortex}，\text{不需要知道}\ \beta）✓$$

## §2 ⭐⭐⭐ **直接计算一：对称离轴对的中点是一个 saddle**

$$\text{取对称对}\ \rho_+=\tfrac12+\delta+i\gamma,\qquad \rho_-=\tfrac12-\delta+i\gamma\quad(\delta>0,\ \gamma\in\mathbb R) ✓$$
$$\qquad \text{（这正是 FE 对：}\rho_-=1-\overline{\rho_+};\ \textbf{同一虚部}，\text{跨临界线对称}）✓$$
$$\text{中点}\ m:=\tfrac12+i\gamma \Longrightarrow \textbf{恰在临界线上} ✓;\ \text{令}\ w=s-m \Longrightarrow s-\rho_\pm=w\mp\delta ✓$$
$$\qquad u_{\text{pair}}=\log|w-\delta|+\log|w+\delta|=\log|w^2-\delta^2|=\operatorname{Re}\log(w^2-\delta^2) ✓$$
$$\qquad \frac{\partial}{\partial w}\log|w^2-\delta^2|\ \text{的解析表示}\ h'(w)=\frac{2w}{w^2-\delta^2} \Longrightarrow \boxed{h'(0)=0} \Longrightarrow \boxed{\nabla u(m)=0} ✓✓✓$$
$$\qquad \text{二阶}：u\approx\log|\delta^2|+\log\Big|1-\frac{w^2}{\delta^2}\Big|\approx \text{const}-\frac{x^2-y^2}{\delta^2}\quad(w=x+iy) ✓✓$$
$$\Longrightarrow \boxed{\text{中点是对称对产生的}\ \textbf{临界点}，\ \text{且为 saddle}：\text{沿}\ \sigma\ \text{方向}\ \textbf{局部极大}，\ \text{沿}\ t\ \text{方向}\ \textbf{局部极小}} ✓✓✓$$
$$\qquad \text{（Hessian}\ =\frac{2}{\delta^2}\mathrm{diag}(-1,+1)\text{：一负一正}）✓✓$$
$$\qquad ⭐\ \text{这正是唐先生 §7 想要的"}\textbf{力平衡位置} \text{"——}\textbf{由对称对自身的对称性直接给出，与 FE 无关} ✓✓$$

## §3 ⭐⭐⭐ **直接计算二：FE 导出的恒等式 ＋ 临界线上的显式值**

$$\zeta(s)=\chi(s)\zeta(1-s)\Longrightarrow u(s)=\log|\chi(s)|+u(1-s) ✓$$
$$\qquad \text{对}\ \sigma\ \text{求导（注意}\ \frac{d}{d\sigma}u(1-\sigma,t)=-u_\sigma(1-\sigma,t)\text{）} \Longrightarrow \boxed{u_\sigma(\sigma,t)+u_\sigma(1-\sigma,t)=\partial_\sigma\log|\chi(\sigma+it)|} ✓✓✓$$
$$\qquad （\textbf{这正是唐先生 §7 写下的方程；本档确认其为精确恒等式}）✓✓$$

$$\textbf{临界线上的显式值（本档新恒等式）}：\text{因}\ |\chi(\tfrac12+it)|=1\ \text{（}|\Gamma(\tfrac14-\tfrac{it}{2})/\Gamma(\tfrac14+\tfrac{it}{2})|=1\text{）} ✓$$
$$\qquad \text{而}\ (\log|\chi|)_\sigma=\operatorname{Re}\big[(\log\chi)'\big],\ \ (\log\chi)'(s)=\log\pi-\tfrac12\psi\big(\tfrac{1-s}{2}\big)-\tfrac12\psi\big(\tfrac{s}{2}\big) ✓$$
$$\qquad \text{取}\ s=\tfrac12+it：\ \tfrac12\big[\psi(\tfrac14-\tfrac{it}{2})+\psi(\tfrac14+\tfrac{it}{2})\big]=\operatorname{Re}\psi\big(\tfrac14+\tfrac{it}{2}\big) ✓$$
$$\Longrightarrow 2u_\sigma(\tfrac12,t)=\log\pi-\operatorname{Re}\psi\big(\tfrac14+\tfrac{it}{2}\big) \qquad\Longrightarrow\qquad \boxed{u_\sigma(\tfrac12,t)=-\theta'(t)} ✓✓✓$$
$$\qquad \text{（}\theta\ \text{＝Riemann–Siegel theta}：\theta'(t)=\tfrac12\operatorname{Re}\psi(\tfrac14+\tfrac{it}{2})-\tfrac12\log\pi\text{）} ✓✓$$
$$\qquad \Longrightarrow ⚠️\ \textbf{"临界线上力平衡"是}\textbf{显式} \text{的：}u_\sigma(\tfrac12,t)\ \text{由}\ \theta'\ \text{完全决定，}\textbf{不含任何零点信息} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{任何"临界线上的平衡律"都只能是显式的} \Longrightarrow \textbf{不携带 off-line 信息} ✓✓✓$$

## §4 ⭐⭐⭐⭐ **结构性毙掉：应力张量 ≡ $(\zeta'/\zeta)^2$**

$$\text{调和场}\ u\ \text{的无迹应力张量}：T_{ij}=\partial_iu\,\partial_ju-\tfrac12|\nabla u|^2\delta_{ij} ✓$$
$$\qquad \text{无源区}：\partial_iT_{ij}=(\Delta u)\partial_ju+\partial_iu\,\partial_iu_j-\partial_ku\,\partial_ju_k=0 \quad（\Delta u=0\text{）} ✓✓\ \textbf{无散} ✓$$
$$\qquad \text{无迹}：\textstyle\sum_iT_{ii}=|\nabla u|^2-\tfrac12|\nabla u|^2\cdot2=0 ✓✓$$
$$\textbf{复组合（关键）}：T_{xx}-T_{yy}+2iT_{xy}=(u_x+iu_y)^2=\overline{f^{\,2}},\qquad f:=u_x-iu_y ✓$$
$$\qquad \text{而 CR ⟹}\ f=L'\ \text{（}L=\log\zeta\text{）} \Longrightarrow \boxed{f=\frac{\zeta'}{\zeta}}\qquad\Longrightarrow\qquad \boxed{T_{xx}-T_{yy}+2iT_{xy}=\overline{(\zeta'/\zeta)^2}} ✓✓✓✓$$
$$\Longrightarrow \boxed{\text{整个无迹无散应力张量}\ \textbf{等价于单个解析函数}\ (\zeta'/\zeta)^2} ✓✓✓✓$$
$$\qquad \Longrightarrow \text{其}\ \textbf{通量／守恒量} \text{的计算＝围道积分＝}\textbf{留数}（\text{极点恰在}\ \zeta\ \text{的零点与}\ s=1\text{，阶数由重数决定}）＝\textbf{辐角原理} ⟹ \textbf{(A) 家族（`V188`）} ✓✓✓$$
$$\qquad ⭐⭐\ \textbf{更根本的理由}：\text{holomorphy（CR）意味着}\ (u,\varphi)\ \textbf{不是两个场，而是一个解析函数};\ \text{故任何"对一个解析函数取模部再作解析型局部泛函"的构造，}\ \textbf{都只是}\ \zeta'/\zeta\ \text{的重新书写} ✓✓✓✓$$
$$\qquad \Longrightarrow \textbf{极坐标化不是新编码，而是}\ \textbf{逐字等于}\ \zeta'/\zeta ✓✓$$

## §5 ⭐⭐⭐ **死亡测试的答案（唐先生 §10）**

$$\textbf{问}：\text{对称对的横向通量是否完全相消？}$$
$$\qquad \text{答}：\textbf{不相消}。\text{因为}\ u(s)=\log|\chi(s)|+u(1-s)，\ \text{即}\ u\ \textbf{不是}\ \sigma\text{-对称的};\ \text{唯一}\ \sigma\text{-不对称因子就是}\ |\chi| ✓$$
$$\qquad \Longrightarrow \text{横向通量的}\ \textbf{非零部分}\ \text{可}\ \textbf{由}\ \chi\ \textbf{显式算出}（\text{§3 的恒等式就是其精确形式}）⟹ \textbf{archimedean／}\chi\ \textbf{通道}（`V215`(c)）⟹ \textbf{DEAD} ✓✓✓$$
$$\qquad ⚠️\ \text{故本档的毙掉理由}\ \textbf{不是"通量相消"}，\ \text{而是}\ \textbf{"不相消的那部分恰好是显式的"} ✓✓✓$$

## §6 三分表（唐先生 §8）—— C 亦 DEAD，并给出理由

| 分支 | 内容 | 判定 |
|:--|:--|:--|
| **A. Phase winding** | 零点 → 相位绕数 $\oint d\varphi=2\pi m$ | **DEAD**（辐角原理／`V188`）✓（本档 §1 确认） |
| **B. Modulus positivity** | $\vert\zeta\vert$、$\log\vert\zeta\vert$、Dirichlet 能量 | **DEAD**（`V185`／`V199`）✓（本档未新查，沿用既有） |
| **C. Modulus–phase coupling** | CR 方程 ＋ FE ＋ 求独立算术局部约束 | ⚠️ **DEAD（本档）**：CR 只是"$\log\zeta$ 全纯"的重述；应力不变量 $=(\zeta'/\zeta)^2$；其守恒量计算＝留数＝(A)；(§3) 表明 FE 给出的平衡量是**显式**的 ⟹ 归 (A) 或 (c) ✓✓✓ |

## §7 若要救活：需要什么样的泛函（本档给出边界）

$$\text{必须}\ \textbf{不是}\ (\zeta'/\zeta)\ \text{的泛函}，\ \text{即}\ \textbf{不解析} \text{于}\ L=\log\zeta\ \text{的构造};\ \text{自然候选只有两类}：$$
$$\qquad \text{(i)}\ \textbf{Dirichlet 能量型}\ \int|\nabla u|^2：\text{注意}\ \int|\nabla u|^2=\int|L'|^2=\int|\zeta'/\zeta|^2 \Longrightarrow \textbf{二次／正性型} ⟹ \textbf{(B)}（`V185`／`V199`）✓$$
$$\qquad \text{(ii)}\ \textbf{非线性非解析组合}：\text{如}\ (u_\sigma)^2\varphi_t\ \text{型混合项};\ \text{但这类构造}\ \textbf{已在}\ \text{`V236`／`V238`}\ \text{(defect／关联退化)}\ \text{被压回} ✓$$
$$\qquad \Longrightarrow \textbf{残余}：\text{一个}\ \textbf{非}\ (\zeta'/\zeta)\ \textbf{泛函} \text{的、}\ \text{非二次型的、}\ \text{非聚合的模—相耦合量}（\text{并入 `V259` 的"非聚合组合律"残余}）✓✓$$

## §8 判词 ＋ 状态表 ＋ 边界

$$\boxed{\textbf{V260}：\text{极坐标／应力路线}\ \textbf{DEAD};\ \text{理由}\ \textbf{不是"通量相消"}，\ \text{而是}\ \textbf{"应力张量≡}(\zeta'/\zeta)^2\text{"＋"不相消部分是显式的"}} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| 对称对中点 | **在临界线上**，且是 $u$ 的 **saddle**（$\sigma$-向极大、$t$-向极小） | §2（本档计算） |
| FE 恒等式 | $u_\sigma(\sigma,t)+u_\sigma(1-\sigma,t)=\partial_\sigma\log|\chi|$ | §3（确认唐先生 §7） |
| 临界线上 | ⭐ **$u_\sigma(\tfrac12,t)=-\theta'(t)$**（显式） | §3（本档新） |
| 应力张量 | **≡ 单个解析函数 $(\zeta'/\zeta)^2$** | §4（本档，关键） |
| 通量／守恒量 | **＝留数＝辐角原理 ⟹ (A)** | §4 |
| 横向通量是否相消 | ✗ **不相消，但非零部分显式** ⟹ **archimedean/`V215`(c)** | §5 |
| 分支 C（模—相耦合） | **DEAD** | §6 |
| 残余 | 非 $(\zeta'/\zeta)$ 泛函、非二次、非聚合的模—相量 | §7（并入 `V259` 残余） |

$$\textbf{边界（诚实）}：\text{§2–§4 的全部计算}\ \textbf{为本档符号推导（初等）}，\ \text{可直接复核}：$$
$$\qquad h'(0)=0（h=\log(w^2-\delta^2)\text{）};\ |\chi(\tfrac12+it)|=1;\ (\log\chi)'=\log\pi-\tfrac12\psi(\tfrac{1-s}{2})-\tfrac12\psi(\tfrac{s}{2});\ f=u_x-iu_y=L'=\zeta'/\zeta ✓$$
$$\qquad \text{§2 的 saddle 结论为}\ \textbf{对"仅取该对两个因子"的局部结论};\ \text{远处零点／光滑部分会移动临界点，}\ \textbf{本档未处理}（\text{但"中点恰在线上"不依赖任何假设}）⚠️;$$
$$\qquad \text{§6 的 (B) 沿用既有结论，未在本档重算};\ \text{§7 的"自然候选只有两类"是}\ \textbf{[结构性] 判断} ⚠️;\ \textbf{未用 RH 作推导};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 22:55）：极坐标路线 —— u=log|ζ|、φ=arg ζ 为共轭调和场（CR: u_σ=φ_t, u_t=−φ_σ）；
   零点＝u 的对数奇点＋φ 的 m 次绕转奇点；FE 反射下寻求局部应力/守恒律
   §8 三分：A Phase winding → 辐角原理 DEAD；B Modulus positivity → V185/V199；C Modulus–phase coupling → 应打的点
   §10 明令：直接计算对称对 ρ=1/2+δ+iγ、1−ρ=1/2−δ+iγ 的 stress tensor/flux；
    若通量完全相消 ⟹ 立即 DEAD；若存在严格非零 δ-依赖守恒量 F(δ,γ)≠0 ⟹ 再过四关：
    (1) 不依赖显式公式 (2) 不等价于零点计数 (3) 不来自正定二次型 (4) 能由 Euler 算术独立计算
   "这次可以直接算，不需要再造一个抽象模型"
⚠️ §2 直接计算一（本档）：对称对 ρ±=1/2±δ+iγ 的中点 m=1/2+iγ 恰在临界线上；
   令 w=s−m，则 u_pair=log|w²−δ²|=Re log(w²−δ²)，其解析表示 h'(w)=2w/(w²−δ²) ⟹ h'(0)=0 ⟹ ∇u(m)=0；
   二阶 u≈const−(x²−y²)/δ² ⟹ saddle（σ-向局部极大、t-向局部极小），Hessian=(2/δ²)diag(−1,+1)
   ⭐ 这正是唐先生 §7 要的"力平衡位置"，由对称对自身对称性给出，与 FE 无关
⚠️ §3 直接计算二（本档新恒等式）：FE 给出 u_σ(σ,t)+u_σ(1−σ,t)=∂_σ log|χ(σ+it)|（确认唐先生 §7 方程）
   临界线上 |χ(1/2+it)|=1；且 (log χ)'(s)=log π−(1/2)ψ((1−s)/2)−(1/2)ψ(s/2)
   ⟹ 2u_σ(1/2,t)=log π−Re ψ(1/4+it/2) ⟹ 【u_σ(1/2,t)=−θ'(t)】（θ=Riemann–Siegel theta）
   ⟹ "临界线上力平衡"是显式的、不含任何零点信息 ⟹ 任何"临界线上的平衡律"只能是显式的
⚠️ §4 结构性毙掉（本档核心）：调和场 u 的无迹应力张量 T_ij=∂_i u ∂_j u−(1/2)|∇u|²δ_ij；
   无源区无散（Δu=0）、无迹；复组合 T_xx−T_yy+2iT_xy=(u_x+iu_y)²=conj(f²)，
   而 CR ⟹ f=u_x−iu_y=L'=ζ'/ζ
   ⟹ 整个无迹无散应力张量等价于单个解析函数 (ζ'/ζ)²
   ⟹ 其通量/守恒量计算＝围道积分＝留数（极点恰在 ζ 的零点与 s=1，阶由重数定）＝辐角原理 ⟹ (A) 家族（V188）
   ⭐⭐ 更根本：holomorphy（CR）意味着 (u,φ) 不是两个场而是一个解析函数；故"取模部再作解析型局部泛函"
   只是 ζ'/ζ 的重新书写 ⟹ 极坐标化不是新编码，而是逐字等于 ζ'/ζ
⚠️ §5 死亡测试答案：横向通量【不相消】—— 因为 u(s)=log|χ(s)|+u(1−s)，u 不是 σ-对称的，
   唯一 σ-不对称因子就是 |χ|；其非零部分可由 χ 显式算出（§3 的恒等式即精确形式）
   ⟹ archimedean/χ 通道（V215(c)）⟹ DEAD
   ⚠️ 故毙掉理由不是"通量相消"，而是"不相消的那部分恰好是显式的"
⚠️ §6 三分表：A DEAD（辐角原理/V188）；B DEAD（V185/V199）；C DEAD（本档：CR 只是"log ζ 全纯"的重述；
   应力不变量=(ζ'/ζ)²；守恒量计算＝留数＝(A)；§3 表明 FE 的平衡量是显式的）
⚠️ §7 若要救活：必须不是 (ζ'/ζ) 的泛函；自然候选两类 —— (i) Dirichlet 能量 ∫|∇u|²=∫|ζ'/ζ|² ⟹ 二次/正性型 ⟹ (B)；
   (ii) 非线性非解析组合 ⟹ V236/V238 已压回 ⟹ 残余＝非 (ζ'/ζ) 泛函、非二次、非聚合的模—相量（并入 V259 残余）
⚠️ §8 边界：§2–§4 全部计算为本档符号推导（初等，已在卡面列出可复核式）；§2 的 saddle 是"仅取该对两因子"的局部结论，
   远处零点/光滑部分会移动临界点，本档未处理（但"中点恰在线上"不依赖任何假设）；§6 的 (B) 沿用既有结论未重算；
   §7 的"自然候选只有两类"是 [结构性] 判断；未用 RH；未跑 Lean；零数值
✅ 净产出：① 直接计算一：对称对中点是临界线上的 saddle（∇u=0，σ-向极大、t-向极小）
   ② 直接计算二（新恒等式）：u_σ(1/2,t)=−θ'(t) ⟹ 临界线上的平衡律是显式的
   ③ 结构性毙掉：无迹无散应力张量 ≡ (ζ'/ζ)² ⟹ 通量＝留数＝辐角原理 ⟹ (A) 家族
   ④ 死亡测试答案：横向通量不相消，但非零部分显式 ⟹ archimedean/V215(c)
   ⑤ 分支 C DEAD（CR 只是 holomorphy 的重述）
   ⑥ 残余并入 V259：非 (ζ'/ζ) 泛函、非二次、非聚合的模—相耦合量
```
