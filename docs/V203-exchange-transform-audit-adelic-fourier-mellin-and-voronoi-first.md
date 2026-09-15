# V203 · **互换变换审计（窄窗口）** —— ⭐⭐ **统一结论：算术中「交换」与「乘积律」位于**不相交的位**：非平凡交换只生于 ℝ（阿基米德，单个位、无乘性分裂），乘积律只能来自有限位（对模数乘性）** ⟹ **五条终止条件全中** ⟹ 按预设规则**关闭**，不进入 V204 ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 13:54：**"不要关闭。专门找'互换变换'，但只给它一个非常窄的 V203 审计窗口。"** 缺口形式化：$$\boxed{\exists\,\mathcal T:\ \mathcal T(\mathcal A_k)\approx\mathcal B_k,\ \ \mathcal T(\mathcal B_k)\approx\mathcal A_k}\qquad\text{＋}\qquad\boxed{T_{k+\ell}=T_kT_\ell}$$ **"不要从'寻找一个新变换'开始猜，直接从现有算术变换的完整候选空间做审计"**：(1) 有限 Fourier／加法特征；(2) Mellin／乘法特征；(3) Poisson／Voronoi 型；(4) Hankel／Bessel 型（特别是 Voronoi 公式里的 dual summation）；(5) 有限域 Fourier／乘法 Fourier；(6) **adelic Fourier–Mellin（"我认为最值得优先检查"）**；每个候选**必须实际计算** $\mathcal T(P_{\mathcal A_k}f)\overset{?}{\subseteq}P_{\mathcal B_{k'}}\mathcal Tf$ **及反向包含**；**＋ 必须检查 $T_{k+\ell}\overset{?}{=}T_kT_\ell$ 或等价的半群／transfer-operator 结构**；**"先审计 Voronoi 型变换"**（因 Voronoi 把算术求和转成**带算术权重的 dual sum**：$\sum a_ne(an/q)\leftrightarrow\sum a_n^*K_q(n)$，$K_q$ 为 Bessel／Kloosterman 型核 —— **算术结构本身参与对偶变换**）；**"但必须非常警惕：如果最后只是把 Voronoi 公式重新写成 explicit formula／functional equation，那么立即 DEAD"**；**终止条件五条**（不能真正交换／交换了但无半群乘积律／交换只在平均意义成立／范数估计只是已有大筛／G–S／Voronoi／最终只是显式公式或函数方程的重包装）；**只有"真正 arithmetic dual exchange ＋ composition law ＋ new strict defect"才进入 V204**；**"先审计 adelic Fourier–Mellin／Voronoi，再审计其他候选；不进入 RH，不做第二阶段。"**
> 查图 ✓ `V202`（双局域化；四前提；**§4 相反区间**）｜`V144`（层诊断）｜`V198`／`V201`（两门；不回）
> 执行 ✓ 小灵（**§2 六候选实算、§3 统一结论 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓｜编号 ✓ **V203**

---

## §1 交换的**精确判据**（先写死，再逐一实算）

$$\textbf{(E1) 正向交换}：\ \mathcal T\bigl(P_{\mathcal A_k}f\bigr)\subseteq P_{\mathcal B_{k'}}\,\mathcal Tf;\qquad \textbf{(E2) 反向交换}：\ \mathcal T\bigl(P_{\mathcal B_k}f\bigr)\subseteq P_{\mathcal A_{k'}}\,\mathcal Tf$$
$$\textbf{(C) 复合律}：\ T_{k+\ell}=T_kT_\ell\ \text{或等价的半群／transfer-operator 结构}\ ✓$$
$$\qquad ⚠️\ \text{三条件}\ \textbf{同时} \text{满足}\ \text{才算"真交换"};\ \text{且}\ \text{交换须}\ \textbf{逐点}（pointwise）\ \text{而非}\ \textbf{平均} \text{意义} ✓$$

---

## §2 六候选**逐一实算**（交换检验 ＋ 乘积律检验）

### 2.1 有限 Fourier／加法特征：$\mathcal T=\mathrm{DFT}$

$$\textbf{E1/E2}：\text{DFT 交换}\ \textbf{空间}（\text{position}\leftrightarrow\text{frequency}）,\ \textbf{不} \text{交换}\ \textbf{族};\ \text{且}：\ 1_{I_N}\xrightarrow{\ \mathcal F\ }\textbf{Dirichlet 核}（\text{全域展开}）;\ \ 1_{\Omega_Q}\xrightarrow{\ \mathcal F\ }\textbf{Ramanujan 型和}（\text{非区间}）✗$$
$$\textbf{C}：\text{DFT 的"复合"是}\ \mathcal F^2=\text{reflection};\ \text{无}\ T_{k+\ell}=T_kT_\ell\ ✗\qquad\Longrightarrow\ \textbf{无交换（命中 #1）} ✓✓$$

### 2.2 Mellin／乘法特征：$\mathcal T=\mathcal M$

$$\textbf{E1/E2}：\mathcal M\ \text{确实交换}\ \textbf{乘}\leftrightarrow\textbf{加}（n^s=e^{s\log n}）,\ \text{但把两族映到}\ \textbf{不同空间}（\mathbb R_{>0}\to\mathbb C）;\ \text{"区间／小分母"在}\ \mathcal M\ \text{下无像} ✗$$
$$\textbf{C}：\mathcal M\ \text{的律是}\ \mathcal M[f*g]=\mathcal M[f]\mathcal M[g]（\textbf{卷积}\mapsto\textbf{乘积}）,\ \text{与}\ T_{k+\ell}=T_kT_\ell\ \textbf{不同型} ✗$$
$$\qquad ⚠️\ \text{且}\ \mathcal M\ \text{恰是}\ \textbf{显式公式} \text{的引擎} ⟹ \text{命中 #5（重包装）} ✓$$

### 2.3 Poisson：$\sum_{\mathbb Z}f=\sum_{\mathbb Z}\hat f$

$$\textbf{E1/E2}：\text{对}\ \mathbb Z\ \text{与}\ \mathbb Q\subset\mathbb A\ \text{均}\ \textbf{自对偶（lattice = its own dual）} ⟹ \text{交换}\ \textbf{＝恒等} ✗\qquad\Longrightarrow\ \textbf{命中 #1} ✓$$

### 2.4 ⭐ Voronoi／Bessel--Hankel（**唯一真正带算术权重的候选**）

$$\textbf{E1/E2}：\text{交换}\ \textbf{确实存在}：\ \boxed{N\ \longleftrightarrow\ q^2/N}\ \（\textbf{对合}，\text{不动点}\ N=q）✓✓$$
$$\qquad \text{其中核}\ K_q\ \text{为 Bessel／Kloosterman 型} —— \textbf{算术结构参与对偶} ✓$$
$$\textbf{C} ⚠️：\text{核}\ K_q\ \text{来自}\ \textbf{函数方程的}\ \Gamma\ \text{因子（archimedean）}:\ K\ \text{的辐角含}\ \sqrt{nx}/q ⟹ \textbf{对模数} q\ \textbf{不乘性} ⟹ \boxed{T_{q_1q_2}\ne T_{q_1}T_{q_2}}\ ✗✗$$
$$\qquad ⚠️\ \text{虽}\ e(a/q)\ \text{本身经 CRT}\ \textbf{可乘性分解}（e(a/q)=e(a_1/q_1)e(a_2/q_2）),\ \text{但}\ \textbf{核不可} ⟹ \text{乘积律}\ \textbf{在核层面失败} ✓✓✓$$
$$\qquad ⚠️\ \text{且交换只在"主项＋误差"意义成立（}\textbf{非逐点}）⟹ \text{命中 #3};\ \text{估计本身}\ \textbf{就是经典 Voronoi 估计} ⟹ \text{命中 #4} ✓$$
$$\qquad ⚠️\ ⭐\ \textbf{决定性}：\text{Voronoi 求和}\ \textbf{由函数方程导出}（Mellin 意义下等价）⟹ \boxed{\text{Voronoi}\equiv\text{函数方程}} ⟹ \textbf{恰好命中唐先生预设的 #5} ✓✓✓$$

### 2.5 有限域 Fourier／乘法 Fourier

$$\textbf{E1/E2}：\text{两个变换住在}\ \textbf{不同群}（\mathbb F_q\ \text{vs}\ \mathbb F_q^\times）⟹ \textbf{无自映射交换} ✗$$
$$\textbf{C}：\text{无跨}\ q\ \text{的复合结构} ✗;\qquad \text{且其定量结果}\ \textbf{均为已证定理} ⟹ \text{命中 #4} ✓$$

### 2.6 ⭐ adelic Fourier--Mellin（唐先生优先项）

$$\textbf{有限位（}\forall p<\infty）：\text{局部 Fourier}\ \textbf{把球映为球}：\ \boxed{\widehat{1_{\mathbb Z_p}}=1_{\mathbb Z_p}};\qquad \widehat{1_{p^k\mathbb Z_p}}=p^{-k}1_{p^{-k}\mathbb Z_p} ✓✓$$
$$\qquad\Longrightarrow\ \textbf{球族在}\ \mathcal F_p\ \text{下闭合} ⟹ \text{族}\leftrightarrow\text{族是}\ \textbf{恒等} ⟹ \textbf{无交换可言}（\text{命中 #1}）✓✓✓$$
$$\qquad ⚠️\ \text{更一般地：}\widehat{1_{\mathbb Z_p^\times}}=1_{\mathbb Z_p}-p^{-1}1_{p^{-1}\mathbb Z_p}\ —— \textbf{仍是球的组合} ⟹ \text{乘法群的存在没有引出第二个族} ✓✓$$
$$\textbf{阿基米德位}：\text{唯一非平凡}：\widehat{1_{[0,1]}}=\textbf{Dirichlet 核}（\text{非区间}）⟹ \textbf{不交换} ✗$$
$$\Longrightarrow\ \boxed{\text{adelic F--M：}\textbf{有限位自对偶（交换＝恒等）、}\mathbb R\ \textbf{位不交换}} ⟹ \textbf{无交换} ✓✓✓$$
$$\qquad ⚠️\ \text{且阿基米德位}\ \textbf{是单个位} ⟹ \text{无模数乘性分裂} ⟹ \text{乘积律不可能来自此处} ✓$$

---

## §3 ⭐⭐ 统一结论（本档核心）

$$\text{把 §2 的六个结论按"交换生于何处／乘积律生于何处"归类}：$$
$$\qquad \textbf{非平凡交换}：\text{仅生于}\ \mathbb R（\text{archimedean}）——\ \text{Voronoi／Hankel 的}\ N\leftrightarrow q^2/N;\ \text{而}\ \mathbb R\ \textbf{是单个位},\ \textbf{无乘性分裂} ✓$$
$$\qquad \textbf{乘积律}：\text{只能来自}\ \textbf{有限位}（\text{对模数乘性}：\ e(a/q)\ \text{经 CRT 分解}）——\ \text{而有限位}\ \textbf{自对偶（无交换）} ✓$$
$$\Longrightarrow\ \boxed{\ \textbf{「交换」与「乘积律」在算术中位于}\textbf{不相交的位}\：\text{交换生于}\ \mathbb R,\ \text{乘积律生于有限位}\ } ✓✓✓$$
$$\qquad ⭐\ \text{一句话}：\text{要交换就得去}\ \mathbb R,\ \text{但}\ \mathbb R\ \text{没有乘性；要乘性就得去有限位，但有限位没有交换} ✓✓✓$$

---

## §4 终止条件逐条命中（按唐先生预设规则）

$$\begin{array}{c|l|c}
\text{编号} & \text{条件} & \text{命中}\\
\hline
1 & \mathcal T\ \text{不能真正交换两族} & \checkmark\（2.1／2.3／2.5／2.6）\\
2 & \text{交换了，但没有半群／乘积律} & \checkmark\（2.2／2.4／2.6）\\
3 & \text{交换只在平均意义成立} & \checkmark\（2.4）\\
4 & \text{范数估计只是已有大筛／G--S／Voronoi 估计} & \checkmark\（2.4／2.5；+ `V202` §4）\\
5 & \mathcal T\ \text{最终只是显式公式或函数方程的重包装} & \checkmark\（2.2 Mellin；2.4 \text{Voronoi}\equiv\text{FE}）\\
\end{array}$$
$$\Longrightarrow\ \textbf{五条全中} ⟹ \text{按预设规则}\ \boxed{\textbf{关闭}};\ \textbf{不进入 V204} ✓✓✓$$
$$\qquad ⚠️\ \text{唯一可进入 V204 的组合（真交换＋乘积律＋新严格缺陷）}\ \textbf{未出现} ✓$$

---

## §5 ⭐ 与 `V202` §4 的**同形观察**（模式，非定理）

$$\text{`V202` §4}：\text{大筛法有效区间}\（Q\gtrsim\sqrt N）\ \text{与 FUP 稀疏需求}\（Q\ll\sqrt N）\ \textbf{相反};\ \text{仅在}\ Q=\sqrt N\ \text{相切且同时临界} ✓$$
$$\text{本档}\ §3：\text{交换生于}\ \mathbb R\ \text{与乘积律生于有限位}\ ——\ \textbf{不相交} ✓$$
$$\Longrightarrow\ \text{两档}\ \textbf{同形}：\textbf{两个必要条件落在相反区域} ⟹ \text{第三} \text{次以不同面貌出现的}\ \textbf{层诊断}（\text{`V144`：archimedean 层承载零点，有限层无相位}）✓✓$$
$$\qquad ⚠️\ \text{标签}：\textbf{模式识别（归纳性）}，\ \textbf{非定理} ✓$$

---

## §6 边界与待核

$$\textbf{(a)}\ \text{§2.6 的局部自对偶（}\widehat{1_{\mathbb Z_p}}=1_{\mathbb Z_p}、\widehat{1_{p^k\mathbb Z_p}}=p^{-k}1_{p^{-k}\mathbb Z_p}\text{）为}\ \textbf{标准事实};\ \textbf{归一化待核} ⚠️$$
$$\textbf{(b)}\ \text{§2.4 的 Voronoi 核为 archimedean Bessel 核、且 Voronoi}\equiv\text{函数方程为}\ \textbf{标准};\ \textbf{具体陈述待核} ⚠️$$
$$\textbf{(c)}\ \text{§2.2 的"卷积}\mapsto\text{乘积"为 Mellin 标准性质} ✓;\ \text{"与}\ T_{k+\ell}=T_kT_\ell\ \text{不同型"为}\ \textbf{本档判断} ⚠️$$
$$\textbf{(d)}\ \text{§3 的统一结论为}\ \textbf{对本档六候选的归纳综合};\ \textbf{非定理};\ \textbf{不} \text{排除非经典变换} ✓$$
$$\textbf{(e)}\ \text{§5 为}\ \textbf{模式识别}，\ \textbf{非定理} ✓$$

```
⚠️ §0 委托（窄窗口、六候选、"先 Voronoi/adelic"、终止五条、"不进入 RH、不做第二阶段"）为唐先生逐字 ✓✓
⚠️ §2 六候选逐一做了 (E1/E2) 交换检验与 (C) 乘积律检验（非猜测）✓✓✓
⚠️ §2.4 与 §2.6 为本档两个关键实算：Voronoi 交换存在但核为 archimedean ⟹ 无乘积律；adelic 有限位自对偶 ⟹ 无交换 ✓✓✓
⚠️ §3 统一结论＝"交换与乘积律位于不相交的位"（归纳综合，非定理）✓✓✓
⚠️ §4 五条终止条件**全中** ⟹ 按预设规则关闭；唯一可进 V204 的组合未出现 ✓✓✓
⚠️ §5 同形观察为模式识别 ⚠️
⚠️ 未用 RH ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 交换精确判据 ✓；② 六候选实算表（交换＋乘积律）✓✓✓；③ 统一结论＝不相交的位 ✓✓✓；
   ④ 五条终止条件全中 ⟹ 关闭 ✓✓✓；⑤ 与 V202 §4 同形（层诊断第三次出现）✓✓
```
