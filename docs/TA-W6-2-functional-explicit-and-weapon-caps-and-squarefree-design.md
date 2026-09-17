# ⚔️ W6-2 · **泛函显式化 ＋ 武器上限（②）＋ 平方自由实验设计（③）**

> 承接 `TA-W6-1`（sieve 武器＝C，卡 parity）✓｜**已查地图** ✓（`E119`／`HE-JIA1b`／`V254`／`V255`／`CLOSED-ROUTES-MAP` L725）✓

---

## ① 泛函显式化（把待攻对象写死）

$$\text{载体}：\ \text{集合}\ \mathcal A\subseteq[1,X]\（\text{先}\ \mathcal A=\mathbb P\ \text{素数，后}\ \mathcal A=\square\text{平方自由}）✓$$
$$\text{位移计数}：\ C_{\mathcal A}(h;X):=\#\{a\le X:\ a\in\mathcal A,\ a+h\in\mathcal A\}✓$$
$$\text{随机模型（须同密度／同分布，Arithmetic Null Separation）}：\ \mathbb E_{\rm rand}C_{\mathcal A}(h;X)=\frac{|\mathcal A\cap[1,X]|^2}{X}✓$$
$$\text{期望主项（素数）}：\ \mathfrak S(h)\frac{X}{\log^2X}\quad(\mathfrak S=\text{奇异级数})✓$$
$$\boxed{\textbf{待攻泛函}：\ \mathcal F_{\mathcal A}(w;H,X):=\sum_{|h|\le H}w(h)\Big(C_{\mathcal A}(h;X)-\text{主项}_{\mathcal A}(h,X)\Big)}✓✓$$
$$\text{所需}：\ |\mathcal F_{\mathbb P}(w;H,X)|\le\text{允许误差}\quad(\textbf{特定}\ w，\textbf{非全体}\ h)✓✓$$

## ② 武器上限（地图查证结果）

| 武器 | 地图位置 | 上限／卡点 | 判定 |
|:--|:--|:--|:--|
| **(i) Selberg／Rosser–Iwaniec 筛权重** | `V254`／`V255` | **可证 parity barrier**（看不见素数，只能到 almost-primes）；`V255 §5(b)` 唯一接链（重述为 Dirichlet 级数横坐标上界）**不存在** | **C** ✓ |
| **(ii) dispersion（色散）** | `CLOSED-ROUTES-MAP` L725（ICTS 2025 讲义 arXiv:2603.28454） | 登记为**正性来源**（酉性＋解析性 ⟹ 色散关系＋**正谱密度** ⟹ Stieltjes）；⚠️ 风险已注明："等价于已有正性 ＝ 换语言" | **C（方向错）**：色散给的是**正性（下界）**，而 W6 要**上界** ✓ |
| **(iii) divisor-switching** | `V2-8b`（BC §4.1.1 互补除数切换） | 我方仅在 BC 语境出现，**无独立上限登记** | **未定**（需单独审） |
| **(iv) 大筛／large-sieve** | `HE-JIA1b`（离对角三分） | 大筛用于 **(G) 一般／minor arc** 项；`E119` 显示大筛只把 $\theta$ 推到手头这一步 | **C（已用尽于该层）** ✓ |
| **(v) 对偶正性／正定 majorant** | `E119 §④` 逐字 | ⭐ 关键：$K_Y$ 是 Gram ⟹ **半正定** ⟹ positivity 给**下界**；**上界须用"对偶正性"＝窗口指示函数的正定 majorant（Beurling–Selberg／Selberg 型）** | ⭐ **唯一方向正确者** ✓✓ |

$$\Longrightarrow\ \boxed{\text{五项武器：}\ \textbf{三项 C}\（\text{sieve：parity}；\text{dispersion：方向错}；\text{大筛：已用尽}）\ + \text{一项未定（divisor-switching）}\ + \text{一项方向正确（对偶正性／majorant）}}✓✓$$

### ⭐⭐ 附带：我方已有的**离对角三分**（`HE-JIA1b` 逐字）
$$\text{(N) 近对角}（m-n\ \text{小}）\to\text{divisor／}\sum_d\ \text{型和}\quad\big|\quad\text{(K) Farey／小分母}\to\textbf{Kloosterman}\to\text{Deshouillers--Iwaniec}\quad\big|\quad\text{(G) 一般（minor arc）}\to\textbf{大筛／Bombieri--Vinogradov}✓$$
$$\qquad\Longrightarrow\ \text{W6 的短差泛函}\ \mathcal F\ \text{应}\ \textbf{按此三分} \text{逐类攻}，\ \text{而非整体估计}✓✓$$

## ③ 平方自由实验——**可执行设计**

$$\text{对象替换}：\ \mathcal A=\mathbb P\ \to\ \mathcal A=\square\（\text{平方自由}）✓$$
$$\mu^2(n)=\sum_{d^2\mid n}\mu(d)\ \Longrightarrow\ \text{一切二体量化为}\ \textbf{精确有限算术和}✓$$
$$\textbf{二分判据}：$$
$$\qquad\text{(I) squarefree 能突破而 primes 坍塌} \Longrightarrow \text{墙}＝\boxed{\textbf{prime extraction}＝\text{parity 位置}}✓✓$$
$$\qquad\text{(II) squarefree 也突破不了} \Longrightarrow \text{障碍}\ \textbf{比素数稀疏性更深} \Longrightarrow \text{墙在}\ \textbf{二体结构本身}✓✓$$
$$\textbf{可判定性}：\text{该二分}\ \textbf{不依赖任何猜想}（\text{两边都可直接算}）✓✓$$

### 执行规格（含数值卫生，按 `§3.3` 协议）
```
① 规模：X = 10^7（素数 664,579 个；squarefree ≈ 6.08×10^6 个）
② 窗口 w：先取 w ≡ 1（平坦）与 w(h) = (1 − |h|/H)_+（三角）两种，H ≪ X
③ 归一同密度：把 squarefree 结果按 |A|²/X 归一，与 primes 同尺度比较
④ 报出量：F_A(H,X)/|A|² 随 H 的变化（两族对照），并给 dps 稳定性证书
⑤ 判定：(I)/(II) 由"归一封顶值"是否随 X（10^6 → 10^7）稳定判定
⑥ ⚠️ 不用任何 ζ／零点输入；不用 RH；纯整数运算
```

## ④ 本轮判定与下一步
$$\text{② 的收获}：\textbf{五项武器中三项确定为 C}，\ \text{且}\ \textbf{唯一方向正确的工具＝对偶正性／正定 majorant}（`E119 §④`）✓✓$$
$$\text{③ 的收获}：\text{二分实验}\ \textbf{设计完成且可判定}，\ \text{下一步＝跑（含数值卫生）}✓$$
$$\textbf{下一步}：\text{① 跑平方自由实验} \to \text{② 按三分逐类攻}\ \mathcal F \to \text{③ 单独审 divisor-switching}✓$$
$$\qquad ⚠️\ \textbf{若}\ (I)\ \text{成立} \Longrightarrow \text{墙被定位到 prime extraction，}\ \text{则}\ \textbf{对偶正性 majorant} \text{成为唯一活口}✓✓$$

## ⑤ 边界
$$\text{(i)}\ §①\ \text{的}\ w(h)\ \text{与误差预算}\ \textbf{尚未与前沿 Prop 5.4 逐字对齐}（\text{待核}）✓$$
$$\text{(ii)}\ §②\ \text{各项为}\ [\textbf{结构}]\ \text{级判定}；\ \text{(iii) 本轮}\ \textbf{未跑计算}，\ \text{未用 RH}✓$$
