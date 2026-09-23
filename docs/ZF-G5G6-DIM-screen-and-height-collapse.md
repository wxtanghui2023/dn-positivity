已查地图：命中（`ZF-CONT-1/2/3`／`ZF-LEM`／`E-11`／`E-44`／`T7`／`S6`／第一断裂 本线自档与既有封存）⟹ **引用，不开新案** ✓
D0: 本档对象 = `DIM`/`CAN` 门与最小充分架构的落档（95–118）＋ 本档自行执行的 `§118` 反例筛选（1–3）＋ 新硬门 `HG`（高度塌缩）
D1: 0 （`[REVIEW]` 轮次：框架落档与筛选推导，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **`ZF-G5G6`：`DIM` 维数压测 ＋ `CAN` 门 ＋ 最小架构；及本档自行筛选（含新硬门 `HG`）**

## §1 **唐先生框架（95–118，落档压缩 ✓✓）**

```
【§95–98 `DIM` 维数压测】 母问题参数空间 `\mathcal M`（`\dim=d`），异常由 `r` 个独立方程给 ⟹ 一般位置 `\dim\mathcal D=d-r` ⟹ 要 `\mathcal D` 离散**至少须** `r\ge d`；若 `r<d` ⟹ `\dim\mathcal D>0` ⟹ $$\boxed{\mathcal D\ \text{不可能有限容量}}$$ ✓
　⟹ **普通 Fredholm kernel locus 判死**（单一 `\ker D_x\ne0` 通常 codim 1 ⟹ 只是 hypersurface）；反例 `D_{s,t}=\mathrm{diag}(s,1)`（`\mathcal D=\{s=0\}` 是整条直线）⟹ $$\boxed{\text{kernel finite-dimensional}\not\Rightarrow\text{kernel locus finite}}$$ ✓✓
【§99–102】**普通 moduli boundary 判死**（`\dim\partial\mathcal M=\dim\mathcal M-1` ⟹ 即使 compact 也只是"compact 正维" ⟹ `[0,1]` 之例）⟹ 须 $$\boxed{\text{compact}+\text{discrete}}$$ 或有限 degree/交定理；
　⭐ **有限容量的本质等价物**：$$\boxed{\mathcal D\ \text{有零维紧支撑}}$$（`\dim_{\rm top}\mathcal D=0` ＋ compact；Hausdorff 下 compact+0-dim+discrete ⟹ 有限）✓✓
　⭐ **弱/强接口之分**：弱＝`\Phi(\rho_{\rm off})\in\mathcal D`；**强**＝$$\Phi(Z_{\rm off})\subset\mathcal D^{(0)}\ (\text{零维有限/紧-离散子层})$$ ⟹ 只有**强接口**有用 ✓✓
【§103–106 `CAN` 门】 多条件同时退化可行，但**须 Jacobian 满秩** `\operatorname{rank}DF=r`（＝有限容量的真实来源）；孤立退化证书：`F^{-1}(0)` 中 `\det DF\ne0` ＋ `\mathcal D\Subset\mathcal M` ⟹ `|\mathcal D|<\infty` ✓；
　⛔ **风险**：不可为凑维数**人工拼方程** ⟹ $$\boxed{CAN:\ \text{异常方程须由母理论 canonical 结构产生}}$$ ✓✓
【§107–109】 局部孤立仍可无限（`d_n=1/n`）⟹ 须 `closed+discrete+compact` ⟹ $$\boxed{\text{三件齐⟹有限}}$$；
　**最小充分架构**：母层 `\overline{\mathcal M}` compact ＋ canonical `F` ＋ `\mathcal D=F^{-1}(0)` discrete 且 `\mathcal D\cap\partial_\infty\mathcal M=\varnothing` ⟹ `|\mathcal D|<\infty`；实现层 `\Phi:Z(\zeta)\to\mathcal M`，`\rho\in Z_{\rm off}\Rightarrow\Phi(\rho)\in\mathcal D` 且 $$\sup_{d\in\mathcal D}|\Phi^{-1}(d)|<\infty$$ ⟹ `N_{\rm off}<\infty` ✓✓
【§110 候选判据】 正维 anomaly ⟹ **CLOSED**｜离散但逃到 infinity ⟹ **CLOSED**｜有限但 zero fiber 无限 ⟹ **CLOSED**｜canonical+compact+discrete+boundary-separated ⟹ **真正 OPEN**｜无 zero→anomaly 定理 ⟹ **OPEN/GAP** ✓
【§111–115 四路复查 ＋ Survivor 重命名】 Fredholm kernel locus **CLOSED as-is**｜moduli boundary **CLOSED**｜relative Morse/Floer **OPEN**（缺 canonical finite anomaly theorem）｜**MULTI-COMPATIBILITY/ISOLATED-DEGENERACY OPEN+**；
　⚠️ §112：须解释"**为何离轴恰好意味着所有 `F_i=0`**"，⛔ 若 `F_1=\beta-\tfrac12` 或 `=\zeta` ⟹ **独立性丧失** ✓；
　⭐ §113 **关键分离**：**I** Zero compatibility（`\zeta(\rho)=0\Rightarrow\Phi(\rho)\in\mathcal M_0`，所有非平凡零点皆满足）｜**II Transverse rigidity**（`\mathcal M_0` 中 `\Re\rho=\tfrac12\Rightarrow\Phi\notin\mathcal D`；`\Re\rho\ne\tfrac12\Rightarrow\Phi\in\mathcal D`）—— **真正困难的是 II**，但 II 可由**独立 involution/duality/positivity/orientation**产生 ✓；
　Survivor 重命名：$$\boxed{\textbf{Canonical Isolated Degeneracy}+\textbf{Regular Infinity}}$$（**只要求异常"发生的位置"有限，不要求 `\kappa` 全局有界**）✓✓
【§117 墙表】 连续横向检测／有界标量／普通 spectral flow／普通 Morse index／有号交数 ⟹ CLOSED（或 INSUFFICIENT）；compact 无离散 ⟹ INSUFFICIENT；Fredholm 有限核 ⟹ INSUFFICIENT；普通 Fredholm kernel locus／标准 moduli boundary／人为 compactification ⟹ CLOSED；relative Morse-Floer／multi-Fredholm／canonical isolated degeneracy／regular-infinity separation ⟹ **OPEN(+)；zero→anomaly 与 finite anomaly→finite fiber ⟹ GAP** ✓
```

## §2 ⭐⭐ **本档自行执行 `§118` 筛选（1–3；纯独立数学）**

```
【筛选 1：成熟理论中是否存在"自然出现的零维 canonical anomaly"？】 ✅ **存在，至少两族**：
　**(a) 孤立完全交／Milnor 数型**：canonical 方程组 `F:\mathcal M^d\to\mathbb R^d`，`F^{-1}(0)` 孤立 ⟹ 有限（`\det DF\ne0`）；典型成熟场景＝**Schubert 演算/相交理论**（"有限多个解"是定理，且解集 canonical）✓✓
　**(b) 特殊点与非常规交（Zilber–Pink / André–Oort；Pila–Wilkie o-minimality；Habegger–Pila、Gao 等）**：Shimura 簇中**特殊点（CM 点）**canonical、离散；**非常规交理论**给出"某类特殊点构成的集合有限"的定理（活跃且成熟）✓✓✓
　⟹ **筛选 1 = PASS（有成熟机器）** ✓
【筛选 2：能否同时拥有 compactification？】 ✅ 可：算术侧对应物＝**Northcott 定理**（有界高度且有限度 ⟹ 有限）⟹ 这就是"compact+discrete⟹有限"的算术实现 ✓✓
　⟹ **筛选 2 = PASS** ✓
【筛选 3：infinity boundary 是否天然与 anomaly 分离？】 ⚠️ **须精确化 —— 本档新增关键推论**：
　Northcott 只给"**有界高度/有界度**内的有限性"，而**特殊点集合在高度上是无界的** ⟹ 故"boundary separation"在算术侧**不等于**"整体分离"，而必须加强为
　$$\boxed{h\big|_{\mathcal D}\le C\qquad(\text{anomaly 集合在高度上\textbf{有界}})}}$$ ✓✓✓
　⟹ 即：**不是"异常层紧化后不与无穷相交"，而是"异常条件本身强制高度有界"** ✓
　⟹ **筛选 3 = PASS（但须加强为"高度有界"而非仅"边界分离"）** ✓
```

## §3 ⭐⭐⭐ **本档新硬门 `HG`（高度塌缩门）：由 §2 筛选 3 推出的结构必然要求**

```
【推导】 由架构：无穷多个零点 `\rho_j`（`|\gamma_j|\to\infty`）须映到**有限的**异常集 `\mathcal D`，且 fiber 有限 ⟹ 若 `\mathcal D` 在高度上**有界**，则
　$$\boxed{\Phi\ \text{必须\textbf{压掉高度方向}：}|\gamma_j|\to\infty\ \text{而}\ h(\Phi(\rho_j))\ \text{有界}}$$ ✓✓✓
【⟹ 新硬门】 $$\boxed{HG:\ \Phi\ \text{不得是高度兼容/高度单调的；须是"高度摧毁型"}}$$ ✓✓
【⭐⭐ 统一解释既有失败模式（本档重要推论）】 本仓一切实现都是**高度指标化**的：Hankel 矩（`\gamma`-侧）、谱实现族、`A_t` 族、`\log`-导数、`\xi'/\xi`、显式公式、`S(T)` 端点 —— **全部保留高度** ⟹ **结构上不可能给出有限性** ✓✓✓
　⟹ 这**独立于** `D3`（extensive）与 `D8`（偶/二阶盲），构成**第三条**排除理由，且是**最根本**的一条 ✓✓
【⟹ 对 §112/§113-II 的加强】 若 `F_i` 或 `\Phi` 含 `\gamma`/"高度相容"信息 ⟹ 立即 `HG` FAIL ⟹ 这正是 `F_1=\beta-\tfrac12`、`F_1=\zeta` 之外**第二类**独立性丧失方式 ✓✓
```

## §4 **本档对 `§118` 第 4–5 问的诚实判定**

```
【第 4 问（非线性、非有限维重编码的 compatibility 机制？）】 ✅ 存在先例：**Zilber–Pink / o-minimality 型**机制本质上是**非线性 + 计数型**（非有限维重编码）✓；且 `\tau` 在 Shimura 侧的自然对合（复共轭/对偶 datum）**不等同**于功能方程反射 `\sigma` ⟹ 与 `L3`（`\tau` 须与 `\sigma` 横截）**不冲突** ✓
【第 5 问（真正的 bridge：zeta 零点可否实现为特殊/非常规点？）】 ⚠️ **GAP（未封，但无已知通路）**：
　本仓已知墙：算术侧 `\alpha_p\equiv1`（第一断裂）、无内生动力学（`D1=0`）⟹ **不存在已知的"zeta 零点 ↔ 特殊点"规范对应** ✓；
　⭐ 且由 `HG` 可给出**可判据的否定倾向**：任何**看似合理的算术字典**（把 `\rho` 送到 Galois 表示 / Frobenius / CM 点等）都**保留或反映高度** ⟹ 极可能 **`HG` FAIL** ⟹ 故 `HG` 是一条**能一次性筛掉大量候选字典**的硬门 ✓✓
　⟹ 第 5 问维持 **GAP**（⛔ 不制造、不臆断"不存在"）✓
```

## §5 **筛选结论（本档）**

```
【筛选 1–3】 PASS ×3（机器存在：孤立完全交/Schubert；特殊点+非常规交；Northcott），但**第 3 项须加强为"高度有界"** ✓
【新增硬门】 $$\boxed{HG:\ \Phi\ \text{须高度摧毁型；anomaly 须高度有界}}$$ ⟹ 与 `DIM`、`CAN`、`VI`（强接口）并列 ✓✓
【最重要净收获】 `HG` **一次性解释了本仓全部既有实现为何不可能成功**（它们全是高度指标化的）✓✓✓
【边界】 ⛔ 未制造候选／未启动搜索／未改状态；⭐ §2–§4（含 `HG`）为**本档自行推导** ✓
```
