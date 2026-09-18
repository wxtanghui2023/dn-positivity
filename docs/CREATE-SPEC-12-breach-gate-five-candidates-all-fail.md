已查地图（**先查后写**）：**`C-127`** §3（突破口＝**与 T 无关的一致有限性界**；机制＝计数＋整数性；唯一非付精度尺度的通道）、**`C-128`／`C-129`**（该界的最自然候选"离轴零点有限"＝**路线循环**，已审）、`C-126`（log-free 排除＝渐近零例；尺度墙）、`C-111`／`C-115`（DBN 端点／同墙异述）、`V191`＋GORZ（Jensen 超曲性 ⟺ RH）、`p512-additive-energy.md`／`V2-21-degenerate-set-parametrization-and-dof-count.md`（**四元组计数**已有）、`p26a21-merging-host.md`。关键词回查：`四元组计数`＝**3 档（已有）**；`正项恒等式`／`可数对象门槛`＝**0 档（新增）**。**结论**：⭐ (继续攻) 攻 C-127 的突破口——**给出"突破口对象"的门槛**并**审五个候选，全部失败（各因不同）** ✓✓：**B1** `#\{\text{离轴}\le T\}\le C` ⟹ 循环（`C-129`）；**B2** `#\{\sigma\ge1-\delta\}` ⟹ 目标本身、无独立界 ⟹ 循环；**B3** Jensen 非实根计数 ⟹ 超曲性＝RH ⟹ **强度过强**（不是更弱）；**B4 ⭐ 边界情形 `#\{\sigma\ge1\}=0` 是\ \textbf{定理级}（经典 `\zeta(1+it)\neq0`）**，但**邻域推不动**——已知结果与"零点以 `(\log T)^{-2/3}` 逼近 `\sigma=1`"相容 ⟹ **边界定理不可变形** ✓✓；**B5 ⭐ 正项恒等式路线**（`\sum_\rho1/(\rho(1-\rho))＝1+\gamma/2-\tfrac12\log4\pi`，各项实部**恒正**）⟹ 是"**已知总和的正项级数**"＝真正的 β-约束，**但**计算离轴零点（`\beta=\tfrac12+y`）在高度 `\gamma` 的**赤字** `\approx3y^2/\gamma^4`，而 `y\le\tfrac12` ⟹ 总赤字 `\le\sum3\cdot\tfrac14/\gamma^4<\infty` ⟹ **自动满足、无信息** ✓✓；**新增登记**：**四重对称 ⟹ 离轴计数 ∈ 4ℤ** ⟹ 门槛可由"`<1`"放宽为"**`\le3`**" ✓ ⟹ **突破口仍未被占据** ✓✓

FREEZE-ACK: 本档即冻结期内的方向攻击与候选审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **突破口对象门槛 ＋ 五候选审计（全败）＋ 四重对称放宽** —— 关系 = 候选审计与门槛细化，非新机制
D1: 0

# CREATE-SPEC-12 · **(继续攻) 突破口：门槛 ＋ 五候选全败**

> **时间**：2026-09-18 22:28 唐先生：**「继续攻」** ⟹ 攻 `C-127` §3 的突破口 ✓

---

## §0 结论（先行）

$$\textbf{突破口（}C-127\text{ §3）}＝\text{与}\ T\ \textbf{无关的一致有限性界} \Longrightarrow \text{集内计数}\le C<1✓$$
$$\textbf{门槛（本档）}：\text{对象须}\ \text{(a) 算术可定义};\ \text{(b) 计数为整数};\ \text{(c)}\ T\text{-无关};\ \text{(d)}\ \textbf{非"离轴零点有限"}（\text{已判循环}）✓$$
$$\textbf{五候选}：\text{B1 循环};\ \text{B2 循环};\ \text{B3 过强};\ \text{B4 边界定理不可变形};\ \text{B5 正项恒等式自动满足} \Longrightarrow \textbf{全败}✓✓$$
$$\textbf{新增}：\text{四重对称} \Longrightarrow \text{离轴计数}\in4\mathbb Z \Longrightarrow \text{门槛可放宽为}\ \boxed{\le3}\ ✓✓$$

---

## §1 突破口对象门槛（本档）

$$\text{要}\ \textbf{log-free 排除} \text{（无零点于}\ \sigma>1-\delta）\ \text{，须一个}\ \textbf{计数对象}\ \text{满足}：$$
$$\qquad \text{(a)}\ \textbf{算术可定义}（\text{不预设零点位置}）\quad\text{(b)}\ \textbf{整数计数}（\text{整数性机制的前提}）$$
$$\qquad \text{(c)}\ \textbf{T-无关界}（\forall T:\ \text{计数}\le C）\quad\text{(d)}\ \neq\ "离轴零点有限"\（\text{`C-129` 已判路线循环}）✓✓$$
$$\qquad \Longrightarrow \text{(d) 是本档主要工作}：\text{换对象}✓$$

## §2 五候选审计（全败，各因不同）

| # | 候选对象 | 判定 | 死因 |
|:--|:--|:--|:--|
| **B1** | $\#\{\rho:\ \operatorname{Re}\rho\ne\tfrac12,\ |\gamma|\le T\}\le C$ | ✗ | **路线循环**（`C-129`：等价于"离轴零点有限"，需 ISO，其两输入已判循环） |
| **B2** | $\#\{\rho:\ \sigma\ge1-\delta\}$ | ✗ | **目标本身**：无独立上界 ⟹ 循环 |
| **B3** | Jensen 多项式非实根计数 | ✗ | **强度过强**：超曲性 ⟺ RH（`V191`/GORZ）⟹ 不是更弱目标 |
| **B4** | $\#\{\rho:\ \sigma\ge1\}=0$ | ⚠️ **是定理** | **经典**（$\zeta(1+it)\neq0$）✓ 但**边界不可变形**（见 §3） |
| **B5** | 正项恒等式路线 | ✗ | **自动满足**（见 §4） |

## §3 B4：边界定理级，但邻域推不动（关键诚实点）

$$\textbf{定理（经典）}：\zeta(1+it)\neq0\ \forall t \Longrightarrow \#\{\rho:\operatorname{Re}\rho\ge1\}=0 \Longrightarrow \textbf{log-free}✓✓$$
$$\qquad ⚠️\ \text{但这是}\ \textbf{边界}（\delta=0）;\ \text{要推到}\ \sigma>1-\delta\ \text{需跨越}\ \textbf{一整条带}✓$$
$$\qquad \text{已知定量结果}（\text{Korobov–Vinogradov}）：1-\operatorname{Re}\rho\ \gtrsim\ (\log\gamma)^{-2/3}(\log\log\gamma)^{-1/3}✓$$
$$\qquad \Longrightarrow \text{"零点以}\ (\log T)^{-2/3}\ \text{速度逼近}\ \sigma=1"\ \textbf{与一切已知结果相容}✓✓$$
$$\Longrightarrow ⭐\ \textbf{边界结论无法"变形"到邻域}：\text{不存在已知矛盾可供利用} \Longrightarrow \text{B4 不可用}✓✓$$

## §4 B5：正项恒等式——最像样的一条，仍自动满足

$$\textbf{经典恒等式}（\text{对称配对}）：\sum_\rho\frac{1}{\rho(1-\rho)}=1+\frac{\gamma}{2}-\frac12\log4\pi✓$$
$$\qquad \text{各项实部}：\operatorname{Re}\frac{1}{\rho(1-\rho)}=\frac{\beta(1-\beta)+\gamma^2}{|\rho(1-\rho)|^2}>0\（\text{恒正}）✓✓$$
$$\Longrightarrow \text{这是}\ \textbf{"已知总和的正项级数"} \Longrightarrow \text{形式上}\ \textbf{真正的}\ \beta\text{-约束}✓✓$$
$$\qquad ⚠️\ \text{但计算}\ \textbf{赤字}：\text{离轴}\ \beta=\tfrac12+y,\ \text{高度}\ \gamma：\operatorname{Re}\frac{1}{\rho(1-\rho)}\approx\frac{1}{\gamma^2+\tfrac14+3y^2}<\frac{1}{\gamma^2+\tfrac14}✓$$
$$\qquad \Longrightarrow \text{赤字}\ \approx\frac{3y^2}{\gamma^4};\quad \text{而}\ y\le\tfrac12 \Longrightarrow \text{总赤字}\ \le\sum_\gamma\frac{3\cdot\frac14}{\gamma^4}<\infty✓✓$$
$$\Longrightarrow \textbf{约束自动满足} \Longrightarrow \text{无信息} \Longrightarrow \text{B5 不可用}✓✓$$
$$\qquad （\text{即：平凡界}\ \operatorname{Re}\rho\le1\ \text{已使该恒等式饱和}——\text{与}\ \text{`CREATE-SPEC-11`}\ \text{的"饱和"同型}✓）$$

## §5 新增：四重对称放宽门槛

$$\text{离轴零点} \Longrightarrow \{\rho,\ 1-\rho,\ \bar\rho,\ 1-\bar\rho\}\ \text{四元组（}\text{彼此相异，若}\ \operatorname{Re}\rho\ne\tfrac12）✓✓$$
$$\qquad \Longrightarrow \textbf{离轴计数}\in4\mathbb Z \Longrightarrow \text{门槛由}\ "<1"\ \textbf{放宽为}\ \boxed{\le3}✓✓$$
$$\qquad ⚠️\ \text{但渐近仍}\ \to\infty \Longrightarrow \text{此放宽}\ \textbf{单独不足以} \text{闭合；价值在于}\ \textbf{门槛更精确}✓$$

## §6 净结果（诚实）

$$\textbf{得到}：\text{门槛 (a)--(d) ＋ 五候选全败 ＋ 四重对称放宽 ＋ "边界定理不可变形"与"正项恒等式自动满足"两条}\ \textbf{结构性死因}✓✓$$
$$\textbf{未得到}：\text{突破口对象}\ \textbf{仍未被占据} \Longrightarrow \text{log-free 排除路线}\ \textbf{对已知机制仍封闭}✓✓$$
$$\qquad ⚠️\ \text{这与}\ \text{`C-126`}\ \text{的"渐近零例"}\ \textbf{一致}，且本档把"为什么零例"}\ \textbf{细化到对象级}✓✓$$

## §7 边界与回查

- ⚠️ §4 的恒等式标 **`[经典·待核原文献]`**（本档未逐字核）；但"各项实部恒正"为**本档初等验证** ✓✓
- ⚠️ §3 的 Korobov–Vinogradov 形为**档案已有**（`C-126`）✓
- ⚠️ 本档**不声称**突破口不存在；仅**审计五个自然候选并全败** ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 22:2x）`[纪律]`（先跑后写）

```
技术词 四元组计数        命中文件数=3  :: ./p512-additive-energy.md ./V2-21-degenerate-set-parametrization-and-dof-count.md ./guth-maynard-deepdive.md（**已有**）
技术词 正项恒等式        命中文件数=0  ⟹ 本档新增
技术词 可数对象门槛       命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：`四元组计数`＝**3 档 ⟹ 沿用（引用）**；`正项恒等式`／`可数对象门槛`＝**0 档 ⟹ 本档新增** ✓
