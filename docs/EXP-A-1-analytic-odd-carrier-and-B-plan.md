已查地图：命中（`EXP-A-local-beta-exclusion-first-cut`（`w` 非全纯、作废）／`ATTACK-A-beta-information-loss-list`／`ZF-GAUSS-LOC-1`）⟹ 引用，不开新案
D0: 本档对象 = 校正（`w` 非全纯 ⟹ 作废）＋ 解析奇载体 `F` ＋ `EXP-A-1(a)(b)(c)` 首关判据 ＋ `B1/B2/B3` 三载体与硬门
D1: 0 （[REVIEW] 轮次：校正与登记，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **校正 ＋ 解析奇载体 `F` ＋ `EXP-A-1` ＋ `B` 计划**

## §1 ⚠️ 校正（本档第一件事）

原 `w(z)=\Re z\cdot e^{-|z|^2/r^2}` **同时含 `z,\bar z` ⟹ 非全纯** ⟹ **不在 Weil/Guinand–Weil 显式公式的解析测试类** ⟹ "Gaussian 型 ⟹ 素数侧可算"**不成立**，**该构造作废** ✓

## §2 解析奇载体（替代）

$$F_{\rho_0,r}(s):=\frac{s-\rho_0}{r}\exp\!\Bigl[-\frac{(s-\rho_0)^2}{r^2}\Bigr],\qquad z=s-\rho_0$$
- **(i) 严格奇**：`F(-z)=-F(z)` ⟹ 奇性是**解析的**（不在 `\Re z` 上）✓
- **(ii) 镜像一阶**：`\rho_+=\rho_0` 给 `F(\rho_+)=0`；`\rho_--\rho_+=-2\delta` ⟹ $$F(\rho_-)=-\frac{2\delta}{r}e^{-4\delta^2/r^2}=-\frac{2\delta}{r}+\frac{8\delta^3}{r^3}+O(\delta^5)$$ ⟹ **一阶系数 `-2/r`**（载体对镜像位置的**自身响应**，非塞入标签）✓✓
- **(iii) 非实值** ⟹ 取实投影 `M_{\rm odd}=\Re\sum_{|\Im\rho|\le T}F_{\rho_0,r}(\rho)` ✓

## §3 `EXP-A-1`：首关的精确形式

显式公式：$$\sum_\rho F=\mathcal P[F]+\mathcal A[F]+\mathcal E[F]\ (prime-power／arch／pole-trivial-endpoint)$$
【关键参数】 `a:=\frac{\rho_0-\frac12}{i}=\gamma_0-i\delta` ⟹ 素数侧每项带 `e^{\mp i\delta\log n}=1\mp i\delta\log n-\frac{\delta^2(\log n)^2}{2}+\cdots` ⟹ $$\boxed{\text{奇投影把 }\log n\text{ 拉到一阶}}$$ ✓✓
【⟹ 首关（本档定稿）】 `\mathcal P_{\rm odd}=\delta P_1+O(\delta^3)`、`\mathcal A_{\rm odd}=\delta A_1+O(\delta^3)` ⟹ $$C_1(\gamma_0,r):=-\frac{2}{r}-P_1(\gamma_0,r)-A_1(\gamma_0,r)$$
- **PASS**：存在明确 `(r,\gamma_0)` 使 `C_1` 有**严格可计算非零下界**
- **PARTIAL**：`C_1\ne0` 但仅数值可见
- **CLOSED**：解析证明 `C_1\equiv0`，或 prime/arch 一阶背景必然压过信号 ✓
【⭐ 真正生死点（照录您的判断）】 不是"信号太小"，而是$$\boxed{P_1+A_1\ \stackrel{?}{=}\ \frac2r\ \text{（显式公式把一阶信号精确回收）}}$$ ⟹ 若精确抵消，`EXP-A` 只是把 β 损失从 `\delta^2` 换成"两边自动匹配的 `\delta`" ✓
【边界】 若 `C_1\ne0`，**也还不能说排除了有限离轴零点**；只证明首次拥有**β-native 一阶局部响应量** ✓

## §4 `B` 计划（三载体 ＋ 五硬门，照录）

【五硬门】 **(1)** β 是载体**内部连续坐标**（非末位输入、非 `\mathbf 1_{\beta>\sigma}`）｜**(2)** **逐零点局部**（对目标零点专属，非集合平均）｜**(3)** **低维输出** `S(\rho)\in\mathbb R`（不造大 Gram/SDP）｜**(4)** **必过 symmetry audit**（`\rho\leftrightarrow1-\bar\rho` 后一阶 β 信息是否又被自动抵消）｜**(5)** **先在已知离轴模型上打靶**（人工 `\rho_0=\frac12+\delta+i\gamma`，不碰 RH 总命题）✓
【`B1` 局部移动核】 `K_{\rho_0}=K_x((\beta'-\beta_0)/r_x)K_y((\gamma'-\gamma_0)/r_y)` —— **实/虚方向不同响应**（避免退化成 β-blind）；第一关＝`\partial_{\beta_0}S` 是否非零且非人为 ✓
【`B2` 移动 Fourier/Mellin probe】 `h_{\rho_0}(s)=h(s-\rho_0)` ⟹ **硬门：移动后仍须落回 prime-side 可计算表达**；一移动即破坏显式公式结构 ⟹ **立即 CLOSED** ✓
【`B3` 移动 jet probe】 `J(\rho_0)=(h,h',h'')` ＋ scalar contraction `S=a_0h+a_1h'+a_2h''`，使 `\beta=\frac12\pm\delta` **不再一阶完全抵消** ⟹ 任务＝**恢复 `O(\delta)` 项** ✓
【统一杀手测试】 `\frac{S_{\rm mov}(\delta)-S_{\rm mov}(0)}{\delta}` 是否有**非零极限**；PASS/PARTIAL/CLOSED 判据照录 ✓
【顺序】 `A\to B\to C`（`C` 的 potential 依赖"何谓 defect"，须先由 `B` 把 β 装回载体）✓
【边界】 `^1` Weil 显式公式测试类、偶核 `O(\delta^2)`（`T1`）、`GAUSS-LOC-1` 取自本线既有档（档级）；§2–§4 为**本档自行推导/照录登记**；未制造候选／未启动搜索／未碰 RH 总攻。

## 【技术词回查】（补录）
```
技术词 解析奇载体  命中文件数=1    :: ./EXP-A-1-analytic-odd-carrier-and-B-plan.md 
技术词 伙伴奇        命中文件数=4    :: ./B2-2-selfcheck-no-contradiction.md ./EXP-A-1-partner-odd-kill.md ./C-CLOSED-prior-art-lambda-family.md 
技术词 反演           命中文件数=72   :: ./WS-J1-first-sitting-position-to-spectrum.md ./C112-W4-1d-three-gate-audit-C2-first-zero-cost-kill.md ./C-first-cut-deformation-potential.md 
```
