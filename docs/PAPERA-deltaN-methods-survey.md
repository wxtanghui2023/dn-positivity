# PAPERA · Fluc(n) 控制方法综述 —— 六方向文献侦察

**日期**：2026-09-12 ｜ **性质**：侦察报告（只检索 + 只写本文件；不提交、不改动其它文件）
**触发**：唐先生指令「侦察文献与原理上**有哪些技术**可以控制那个涨落项；列出方法、写出前提、逐条对照我们的具体需求」

**对象**
```
Fluc(n) = ∫_0^{T₀} f(nθ(t)) dS(t),   S(T) = N(T) − main(T),
θ(t) = 2·arctan(1/(2t)),   f = 1 − cos
⟺ Fluc(n) = Σ_{γ ≤ T₀} f(nθ_γ)  −  ∫_0^{T₀} f(nθ(t)) d main(t)
需要：|Fluc(n)| < 允许量 = N(T₀) − n·B_{T₀}  （n ≲ T₀²，允许量 ≈ N(T₀)·(1−o(1))）
难点：相位 nθ(t) 的瞬时频率 ≈ n/t²，S 是素数频率 log p^k 的正弦叠加
     ⟹ 共振点 t_res ≈ √(n/log n) 落在 [0,T₀] 内（对 n ≲ T₀²·log T₀）
```

**纪律（本文件自约束）**：不虚构任何引用或 arXiv 编号；每条技术都写明其**前提**才给判定；
凡未亲自核验的条目一律标注「未核验」；结论允许且欢迎是「没有一条直接适用」。

---

## 0. ⭐ 一个结构性发现（它决定了下文至少 3 条判定）

**命题（本文件自证，初等）**：作为复变量 z 的函数，`θ(z) = 2·arctan(1/(2z))` 的支点在
`1/(2z) = ±i`，即 **`z = ±i/2`**。

```
【代数核验】arctan(w) 的支点在 w=±i；此处 w=1/(2z) ⟹ 1/(2z)=±i ⟺ z=∓i/2 ✓
【等价表述】θ(T)=Im logΓ(1/4+iT/2) − (T/2)logπ 的奇点在 Γ 的极点 ⟹ 1/4+iT/2 = −m (m=0,1,2,…)
           ⟹ T = i(2m+½) ⟹ 最近的两个是 T = ±i/2 ✓（与上式一致）
【推论】g(z) := f(nθ(z)) = 1 − cos(nθ(z)) 在 |Im z| < 1/2 内解析，
       其**首奇点恰好落在 Im z = ±1/2 上** —— 这正是临界带边界在 γ 变量下的位置。
【关键】此现象**对每个 n ≥ 1 都成立**（含 n=1）——障碍来自 θ 本身，与 n 无关 ✗✓
【奇点强度】近 z=i/2（记 w=z−i/2）有 θ(z) ≈ π/2 + i·log w ⟹ nθ ≈ nπ/2 + i·n·log w
           ⟹ cos(nθ) 含 w^{±n} ⟹ |g(z)| ≍ |w|^{−n}（**n 阶支点**）
⟹ 傅里叶对偶：ĝ(x) 的衰减由"奇点到实轴距离 = 1/2"决定：|ĝ(x)| ≲ e^{−π|x|}·|x|^{n−1}
            ⟹ 在素数侧取样点 x = (log n)/2π 处：ĝ((log n)/2π) ≈ n^{−1/2}·(log n)^{n−1}
```

**两个直接后果（下文的共同根因）**：
```
(i) 一切"临界带显式公式"的标准前提都要求测试函数在  |Im s| ≤ 1/2 + ε （**ε > 0**）内解析；
    我们的 f 恰好是 ε = 0（奇点就在边界上）⟹ **不满足** ✗
(ii) 若强行代入 Guinand–Weil 式，素数侧和 Σ_{m≥2} Λ(m)/√m·ĝ(log m/2π) ≈ Σ Λ(m)/m
     **对数发散**（ε>0 时正是 e^{−2πε·|x|} 这个因子保证收敛；ε=0 处它消失）✗
```

> 这不是巧合：θ 是 Riemann–Siegel theta，其复奇点在 ±i/2 是**设计使然**（Z(t)=e^{iθ(t)}ζ(½+it) 取实值）。
> 于是 f(nθ(·)) 恰好"卡"在容许类的边界上——本文发现的六条路线里有三条（方向 1、2、6）栽在这里。

---

## 1. 六方向逐条评估

> 每条给出：**名称/来源（含核验状态）** · **前提** · **对我们的 f 是否适用** · **一行判定**。

### 方向 1 —— 把 Guinand–Weil 显式公式**直接**用于 f(nθ(·))

**来源（已核验）**
- Guinand (1947)（转述见 P. Garrett 讲义 *Guinand's explicit formula*，UMN；原刊页码本文件**未独立核验**）；Weil (1952), *Sur les "formules explicites" de la théorie des nombres premiers*, Comm. Lund, 252–265（经 Exeter 页转述）。
- **现代严格版（我逐字读到）**：E. Carneiro, A. Chirre, M. B. Milinovich, *Bandlimited approximations and estimates for the Riemann zeta-function*, **arXiv:1710.10362** = Publ. Mat. **63** (2019), no. 2, 601–661，**Lemma 8**：
  > "Let h(s) be analytic in the strip |Im s| ≤ 1/2 + ε for some ε > 0, and assume that |h(s)| ≪ (1+|s|)^{−(1+δ)} for some δ > 0 when |Re s| → ∞. … Then Σ_ρ h((ρ−½)/i) = h(1/(2i)) + h(−1/(2i)) − (1/2π)ĥ(0)log π + (1/2π)∫ h(u)Re Γ'/Γ(¼+iu/2)du − (1/2π)Σ_{n≥2} Λ(n)/√n (ĥ(log n/2π) + ĥ(−log n/2π))."
- **紧支版本（F ∈ C²_c）**：Weil 显式公式的另一标准形（在 2026 年一份 Claude 撰写的"2/3 单零点"预印本中逐字读到）：对 **F ∈ C²_c(R)** 偶函数，`Σ_ρ m_ρ F̂(γ_ρ) = F̂(i/2)+F̂(−i/2)+∫F̂(τ)μ(τ)dτ − 2Σ_{n≥1} Λ(n)/√n F(log n)`。
- **非紧支/更宽松版本确实存在**：Weil 本人允许含**阶跃函数**的较大类（math/9810169 摘要逐字：*"Weil proved his formula for a large class of g's, including in particular the step-function for which ĝ(s) = (X^s−1)/s"*），但结果是**条件收敛 + 极限**形式。
- **Selberg 迹公式类比（已核验）**：CUNY 博士论文 *Explicit Formulae and Trace Formulae* 中 Theorem 5.2.1（引 Hejhal, p.154）："h(r) analytic in the strip |Im(r)| ≤ 1/2 + δ and |h(r)| ≪ |r|^{−2−δ}" —— **同一个条带前提**。
- **"能否放松"的公开讨论（已读到）**：MathOverflow 163234。Marc Palm 评论："…the test function should be bounded by (1+|Im z|)^{−2−ε} … your argument … would imply an explicit formula with **more relaxed conditions** on the allowed test functions"；paul garrett 回答："the additional details that get used in a proof of an explicit formula are **probably necessary**"。

**前提**：h 在 **闭条带 |Im s| ≤ 1/2 + ε（ε>0）** 内解析 + 多项式衰减 (1+|s|)^{−1−δ}；等价地（Paley–Wiener）要求 ĥ 为紧支/指数型。

**对我们的 f**
```
衰减 ✓：|f(nθ(γ))| ≍ n²/(2γ²) ⟹ 满足 (1+|γ|)^{−1−δ}（δ=1）
条带 ✗：g 在 |Im|<1/2 解析、奇点恰在 |Im|=1/2 ⟹ **不满足 ε>0**
素数侧 ✗：Σ Λ(m)/√m·ĝ(log m/2π) ≈ Σ Λ(m)/m **对数发散**（见 §0(ii)）
```

**判定**：**DOES-NOT-APPLY** —— 前提（条带 ε>0）被恰好违反，且违反处正是素数侧收敛所需的那个因子；"更宽松"版本（Weil 阶跃类）仍要求在临界带内解析，同样失效。

---

### 方向 2 —— 用**容许（带限）测试函数逼近 f**，并控制逼近误差

**来源（已核验）**
- **Beurling–Selberg 极值函数 / 指数型 majorant–minorant** 的系统化现代用法：Carneiro–Chirre–Milinovich，**arXiv:1710.10362**（同上），其中 §3 "Extremal bandlimited approximations"。该文**逐字**说明其动机：
  > "the functions f_{n,α} … **do not possess the required smoothness properties to allow the application of the Guinand-Weil formula**. The key idea … is to replace the functions f_{n,α} by appropriate **extremal majorants and minorants of exponential type (thus with a compactly supported Fourier transform by the Paley–Wiener theorem)**."
- 相关：Carneiro–Chandee–Milinovich 2013（Math. Ann. 356）"Bounding S(t) and S₁(t) on RH"——同门技术（书目经 arXiv:2412.15470 参考表核对）。

**前提（逼近法的一般要求）**：(i) 目标函数在**比所用带宽更宽一档**的条带内**有界**（以保证指数型逼近的误差 ~ e^{−2πaτ}）；(ii) 能给出 majorant/minorant 对及其显式 L¹/sup 误差；(iii) 逼近后素数侧 Σ_{log m ≤ 带} Λ(m)/√m·ĝ_Δ(log m/2π) 可评估/可控。

**对我们的 f**
```
目标 g(z)=f(nθ(z)) 在 |Im z|<1/2 解析，但
  · 奇点在 |Im|=1/2 **边界上**（不在内部）⟹"严格更宽条带内有界"这一前提**不成立**；
  · 且该奇点是 **n 阶支点**（|g|≍|w|^{−n}）⟹ 逼近误差随 n 急剧恶化，**不一致**。
误差预算（本文件算）：‖g−ĝ_Δ‖_∞ ≤ ε 时误差贡献 ≤ N(T₀)·ε；
  需 < 允许量 ⟹ **ε < 1 − nB_{T₀}/N(T₀)**（在 n=T₀² 处 ≈ 0.41）——**预算极宽松** ✓
⤷ 但标准极值函数理论无法把上述 ε 做到"对所有 n ≤ T₀² 一致" ✗
```
**判定**：**NEEDS-ADAPTATION**（在所需**一致性**下很可能 **DOES-NOT-APPLY**）—— 误差预算虽宽松（≈0.4），但奇点在**边界**且**高阶**，经典 bandlimited-approximation 误差估计的"条带严格更宽 + 条带内有界"前提恰恰缺失。

---

### 方向 3 —— 对 S(t)/零点测度的**非线性相位振荡积分**（van der Corput / 平稳相位）

**来源（教科书级，已核验其标准形式）**：van der Corput 一阶/二阶导检验、"平稳相位法"（Titchmarsh, *The Theory of the Riemann Zeta-Function*，Chs. 3–5；Stein, *Harmonic Analysis*；MSE 5055953 逐字给出**二阶导检验**：`|Σ_{N<n≤N₁} e(±f(n))| ≤ 4/√(πλ₂)`，要求 f'' ≥ λ₂ ∈(0,π⁻¹)）。

**前提**：在积分区间上 `|φ'| ≥ λ`（一阶导检验）或 `|φ''| ≥ λ₂`（二阶导检验），**或**存在非退化驻点（平稳相位）。

**对我们的 f**
```
φ(t)=nθ(t)；φ'(t) = −4n/(4t²+1)；φ''(t) = 32nt/(4t²+1)²
· 一阶导检验：min|φ'| = |φ'(T₀)| ≈ n/T₀² ≤ 1（n ≤ T₀²）⟹ 界 ≳ T₀²/n ✗
· 二阶导检验：λ₂ ≈ 2n/T₀³ ⟹ 界 ≳ T₀^{3/2}/√n ✗
⟹ n ≲ T₀² 时两者都 **≥ 信号量级**，定量失败 ✗
· φ'(t) 在 (0,T₀] 上**无零点** ⟹ **不存在驻点** ⟹ 平稳相位法"无对象" ✗
```
（以上与项目内独立计算 `PAPERA-two-regime-attempt.md` 一致：三个常规估计都定量失败，根因是 φ'(T₀)≈2 "相位不够快"。）
**且真正的机制不是平稳相位**：是**啁啾频率 n/t² 与离散素数频率 log p^k 的匹配**（t_res≈√(n/log p)），属"两个不同振荡源相互作用"，van der Corput / 平稳相位不捕捉此类现象。

**判定**：**DOES-NOT-APPLY（定量）** —— 前提（|φ'|或|φ''|下界、或驻点）在本问题的最要紧区间 [T₀^{2/3}, T₀] 上不成立；且机制类型不匹配。

---

### 方向 4 —— Landau–Gonek 及其亲属

**来源（已核验）**
- **Landau (1911)**：对固定 x>1，`Σ_{0<γ≤T} x^ρ = −Λ(x)·T/(2π) + O(log T)`（Baluyot–Gonek, *Explicit formulae and discrepancy estimates*（ECU 预印本）逐字）。
- **Gonek (1993) 一致细化**（同上逐字）：`Σ_{0<γ≤T} x^ρ = −(T/2π)Λ(x) + O(x log(2xT)loglog(3x)) + O(log x·min(T, x/⟨x⟩)) + O(log(2T)·min(T, 1/log x))`，其中 ⟨x⟩=x 到最近**其它**素数幂的距离；推论 `Σ_{0<γ≤T} x^{−ρ} = −(T/(2πx))Λ(x) + …`。RH 下常见形（MathOverflow 484526 逐字）：`Σ_{0<γ≤T} 1/n^ρ = −TΛ(n)/(2nπ) + O(log(2nT)loglog(3n))`。
- **近期推广（2026，已读到摘要）**：**arXiv:2601.18025**，*Generalisations of the Landau–Gonek Theorem and Applications to Mean Values of Zeta* —— 处理 `Σ_ρ χ(ρ)x^ρ`（χ 为函数方程因子），结果按 x 与 T 的大小分**三情形**。（作者名单本次**未核验**；同期学位论文 B. Durkan, *Two theorems on sums over zeros of the Riemann zeta function*（Manchester, 2026）同主题。）
- 相关：MathOverflow 484526 *A smooth Landau–Gonek type formula*（光滑化以压误差）——**尚未见答案**（该问无回答）。

**前提**：相位对 γ 是**线性**的（权 x^ρ = x^{1/2}e^{iγlog x}）；x 的**算术性**（是否为素数幂）决定主项；误差 O(log T) 且需对称极限。

**对我们的 f**
```
相位是 nθ(γ)（非线性、≈n/γ），**非**线性相位 ⟹ Landau–Gonek 不直接给 Σ_γ f(nθ_γ)。
若要用：把 f(nθ(·)) 分解为线性相位叠加 f(nθ(γ))=∫ ĉ(λ)e^{iγλ}dλ，
        再逐 λ 用 Landau–Gonek ⟹ Σ_γ f = ∫ ĉ(λ)[−Λ(e^λ)T/(2π)]dλ + O(log T·∫|ĉ|dλ)。
⟹ 合法性要求 ĉ∈L¹（即 f 的傅里叶变换绝对可积）并要求误差对 λ 一致
⟹ **回到方向 1 的可积性/解析性前提**（而我们始终"卡在边界"）✗
且 2601.18025 的非线性相位是 **log 型**（arg χ(ρ) ~ γ log γ），与我们的 **n/γ 型**形状不同，
   其方法（绑在函数方程因子上）不可直接搬 ✗
```
**判定**：**NEEDS-ADAPTATION**（它本质是显式公式的**素数侧信息**，需再分解+再积分）；对"**直接**给出 |Fluc| 界"而言 = **DOES-NOT-APPLY**。

---

### 方向 5 —— S(t) 的**局部（短区间）二阶矩**（Selberg 积分 / 数方差）

**来源（已核验）**
- **Selberg 矩/CLT**：`∫_0^T S(t)^{2k}dt ~ ((2k)!/(k!2^k))·T·(loglog T)^k`；S(t) 的分布近似 Gauss，方差 ½loglog T（Ann. Math. 170 (2009) 981–993 的引言逐字）。
- **Goldston 细化**（arXiv:2211.14918 逐字）：RH 下 `∫_0^T |S(t)|²dt = T/(2π²)·loglog T + …`，用零点**配对关联**的下阶项。
- **Fujii**（同上转述）：无条件 `∫_0^T [S(t+Δ)−S(t)]^{2k}dt = …`（短区间差分矩）。
- **短区间数方差 / Berry 猜想**：**arXiv:2211.14918** *On the number variance of zeta zeros and a conjecture of Berry* (2022)；**arXiv:1302.1452** *Statistical properties of zeta functions' zeros* 逐字给出"长度 ~(log t)^{−δ} 的区间内零点超出数为 Gauss 变量、方差 ∝ (1−δ)loglog t"。

**前提**：这些是**对 t 的平均/依分布**陈述（可无条件或需 RH / Montgomery 型输入）。

**对我们的 f**
```
我们需要：**固定 n、具体权 f(nθ(·))** 的确定型界，且对**所有** n ≤ T₀² 一致。
方向 5 给的是：大多数 t 的均方/分布信息 ⟹ 对象不同（"平均" vs "逐 n 一致"）✗
最多能给"对多数 n/平均意义"的版本，不足以保证 worst-case 允许量 ✗
```
**判定**：**DOES-NOT-APPLY（直接）** —— 均方/依分布信息无法转成"对所有 n ≤ T₀² 一致"的确定型界；至多给平均信息（那属 NEEDS-ADAPTATION）。

---

### 方向 6 —— 2020–2026 的**非算术权重零点和**技术

**来源**
- ⭐ **Bondarenko–Radchenko–Seip**, *Fourier interpolation with zeros of zeta and L-functions*, **arXiv:2005.02996**, Constr. Approx. **57**:2 (2023) 405–461（书目经 arXiv:2608.10121 与 MSP *Anal. PDE* 参考表核对；正文从 d-nb.info 复本**逐字读到**）：
  > "We let **H₁** denote the space of functions f(z) that are **analytic in the strip |Im z| < 1/2 + ε** and satisfy sup_{|y|<1/2+ε} ∫_{−∞}^∞ |f(x+iy)|(1+|x|)dx < ∞ for some ε>0."
  该文把 Riemann–Weil 公式改造为**插值恒等式**（值在零点 + 傅里叶变换值在 log n 处）。L-函数推广需**更宽**条带（如奇特征处"need to require that functions be analytic in a strip of width **3 + ε**"）。
- **近期**：Berghaus–Bondarenko–Radchenko–Seip–Sun, *The basis functions of Fourier interpolation*, **arXiv:2512.18677** (2025)。
- **统计/刚性类**：配对关联 SDP 界 **arXiv:1810.08843** (*Pair Correlation Estimates … via Semidefinite Programming*)；"2/3 单零点/线上"新证 **arXiv:2609.02882** (2026)；精确零点和恒等式 **arXiv:1307.5723** (*Some sums over the non-trivial zeros*)。

**前提**：BRS 的 H₁ 类要求条带**严格宽于 1/2**（ε>0）；统计类结果给的是**平均/刚性**信息。

**对我们的 f**
```
g(z)=f(nθ(z)) 只在 **|Im z| < 1/2** 解析 ⟹ 对 H₁ 差一个 ε ⟹ **不满足** ✗
（与方向 1 是**同一个**障碍，出现在**独立**的现代框架里 ⟹ 该障碍是稳健的、非技术性的）
统计/刚性类（配对关联、数方差、SDP、2/3 定理）给的是系综/平均信息，
   不是"具体非算术权重 Σ_γ f(nθ_γ) 的确定型界" ✗
```
**判定**：**NEEDS-ADAPTATION**（BRS 是**最接近**的现代框架，但"ε=0 的边界条带"正是全部难点）；统计类 **DOES-NOT-APPLY**。

---

## 2. 汇总表

| # | 技术（来源，核验） | 前提 | 对 f(nθ(·))（n≤T₀²） | 判定 |
|---|---|---|---|---|
| 1 | Guinand–Weil 显式公式（CCM19 arXiv:1710.10362 Lemma 8；Weil 1952；Selberg 迹公式同构） | h 在 **\|Im s\|≤1/2+ε (ε>0)** 解析 + (1+\|s\|)^{-1-δ}；或 F∈C²_c | 衰减 ✓，**条带 ✗**（奇点恰在 \|Im\|=1/2）；素数侧 ΣΛ(m)/m 发散 | **DOES-NOT-APPLY** |
| 2 | 带限/指数型**逼近**（Beurling–Selberg；CCM19 §3） | 目标在**比带宽更宽**的条带内**有界**；显式 L¹/sup 误差 | 预算 ε<1−nB/N≈0.4 **宽松** ✓，但奇点在**边界且高阶** ⟹ 标准误差估计不适用 | **NEEDS-ADAPTATION**（一致性下很可能 DOES-NOT-APPLY） |
| 3 | van der Corput 一/二阶导检验、平稳相位 | 区间上 \|φ'\|≥λ 或 \|φ''\|≥λ₂，或非退化驻点 | \|φ'(T₀)\|≈n/T₀²≤1、λ₂≈2n/T₀³ ⟹ 两估计均 ≳ 信号；**无驻点** | **DOES-NOT-APPLY（定量）** |
| 4 | **Landau–Gonek**（Landau 1911；Gonek 1993；推广 arXiv:2601.18025, 2026） | 相位对 γ **线性**；x 的算术性；误差 O(log T) | 相位非线性（≈n/γ）；须分解为线性相位 ⟹ 回到方向 1 的可积性前提 | **NEEDS-ADAPTATION**（直接给界：DOES-NOT-APPLY） |
| 5 | S(t) 局部二阶矩（Selberg 矩；Goldston；Fujii；Berry 数方差 arXiv:2211.14918, 1302.1452） | **对 t 的平均/依分布** | 需要"固定 n、逐 n 一致"的确定型界 ⟹ 对象不符 | **DOES-NOT-APPLY（直接）** |
| 6 | **Fourier 插值**（BRS, arXiv:2005.02996, 2023, 类 H₁）；2025–2026 统计/刚性类 | 函数在 **\|Im z\|<1/2+ε (ε>0)** 解析 | g 只在 \|Im\|<1/2 解析 ⟹ 差一个 ε（同方向 1） | **NEEDS-ADAPTATION**（统计类：DOES-NOT-APPLY） |

**跨方向结论**：**没有一条，按其在文献中的现有形式，直接适用于我们的 f。**
三条路线（1、2、6）栽在**同一个、稳健的障碍**上——θ 的奇点恰在临界带边界 \|Im\|=1/2（§0）。

---

## 3. 三个最有希望的候选

> 选取标准：即使文献中无现成定理，**该路线本身可攻击**，且"要证什么"可被精确写出、可被判据检验。

### 候选 A（方向 2）—— **带限逼近 + 宽松误差预算**
**思路**：找指数型（FT 紧支）函数 g_Δ，使 Σ_γ g(γ) 可由显式公式评估，而逼近误差 Σ_γ (g−g_Δ)(γ) ≤ N(T₀)·‖g−g_Δ‖_∞ 落在允许量内。
**必须证明**：存在显式常数的逼近对，满足
```
sup_{γ∈R} |f(nθ(γ)) − g_Δ(γ)| ≤ ε_n，  且  N(T₀)·ε_n < N(T₀) − n·B_{T₀}
即  ε_n < 1 − n·B_{T₀}/N(T₀)（≈0.41 于 n=T₀²），对**所有** n ≤ T₀² 一致，
且带宽小到素数侧 Σ_{log m ≤ 带} Λ(m)/√m·ĝ_Δ(log m/2π) 有限可估。
```
**为何有希望**：预算 **0.4 很宽松**（f∈[0,2]，粗常数逼近已给误差 ~1，故只需**中等**精度）。
**为何可疑**：奇点在**边界**且为 **n 阶**支点，经典极值函数误差估计的"更宽条带内**有界**"前提缺失 ⟹ 需**新**逼近定理（对边界支点型目标函数）。

### 候选 B（方向 1 + 6 的合流）—— **边界条带（ε=0）版显式公式 / 插值恒等式**
**思路**：把 Guinand–Weil 公式（或 BRS 插值恒等式）推广到**只在开条带 |Im s|<1/2 内解析**的测试函数，代价是接受**条件收敛**的素数侧（并给正则化/"对称极限"）。
**必须证明**：
```
① 一个定理：对偶函数 g 在 |Im z|<1/2 解析、|g(γ)|≪|γ|^{−1−δ}，
   显式公式（或插值恒等式）仍成立（或以正则化形式成立）；
② 素数侧 Σ_{m≥2} Λ(m)/√m·ĝ(log m/2π) 的**收敛/可求和**（ε=0 处它本应对数发散），
   或给出其正则化值 + 误差 O(?)；
③ 截断到 γ≤T₀ 的**边界项**可控（= 项目内"受控终止/边界振荡"问题）。
```
**为何有希望**：这是**结构性**的修法，一旦成立，Fluc(n) 立即化为素数侧评估（与项目四步路线吻合）。
**为何可疑**：MathOverflow 163234（garrett）明言放松前提"probably necessary"的细节不可省；
项目自身两独立分析亦指向"必须**评估**而非**界**"。

### 候选 C（方向 3 + 4 的合流）—— **素数侧共振的评估（chirp × prime-tone）**
**思路**：不再"界"振荡项，而是**评估**啁啾 n/t² 与素数频率 log p^k 的匹配积分
```
R_p(n) = ∫_0^{T₀} sin(nθ(t))·sin(t·log p)·(4/(4t²+1)) dt,  共振 t_res ≈ √(n/log p)
```
并对全体素数幂求和，给出**一致于 n ≤ T₀²** 的定量主项 + 误差。
**必须证明**：一个**新的、一致于 n ≤ T₀² 的"啁啾 × 素数音"估计**（形式化 §方向 3 的共振图像；
把它从"平稳相位式启发"升级为**定理**），或等价地：显式公式素数侧的非线性相位版本 + 一致误差。
**为何有希望**：与项目自身结论（`PAPERA-two-regime-attempt.md`：区 II "需要**评估**而非界"；
`PAPERA-delta-N-resonance.md`：共振是根因）**完全一致**，是最"对症"的路线。
**为何可疑**：文献里**没有**这种一致估计（Landau–Gonek 只处理**线性**相位；2601.18025 的 log 型相位不可搬）；
且 t_res 落在区间内意味着**无法**用相位相消，必须用素数分布的**离散性/密度**来付账。

---

### 最终一行判断

**六个方向按文献现有形式都**不能**直接达到允许量：候选 A 受"边界 n 阶支点使逼近不一致"所限、候选 B 受"ε=0 时素数侧对数发散"所限、候选 C 受"文献无一致啁啾–素数音估计"所限——
**三者的缺口是同一个**：缺少一个**有限 n、一致于 n ≤ T₀² 的定量 Riemann–Lebesgue（啁啾对素数音）估计**；
因此**没有**一条候选在现有文献下**可信地**达到允许量，它们只是把障碍**精确地**指名并定位到可攻击的位置。

---

## 附：本文件的核验状态一览

| 引用/事实 | 状态 |
|---|---|
| arXiv:1710.10362 = Carneiro–Chirre–Milinovich, Publ. Mat. 63 (2019) 601–661；Lemma 8 全文与 §3 动机 | ✅ **已逐字核验** |
| Guinand–Weil 紧支版（F∈C²_c）与 μ(τ) 标准化 | ✅ 已读到（第三方 2026 预印本引言） |
| Weil 1952, Comm. Lund 252–265 | ⚠️ 经 Exeter 页**转述**，原刊**未核验** |
| Guinand 1947（Proc. LMS 50, 107–119） | ⚠️ **未核验**（仅见 Garrett 讲义转述） |
| math/9810169（Weil 公式含阶跃函数的较大类） | ✅ 摘要逐字读到 |
| MathOverflow 163234（Marc Palm 评论、garrett 回答） | ✅ 已读到 |
| Selberg 迹公式同构（Hejhal, p.154 条带前提） | ✅ 经 CUNY 论文 Theorem 5.2.1 转述 |
| Landau 1911 / Gonek 1993 公式 | ✅ 经 Baluyot–Gonek 预印本逐字核验 |
| arXiv:2601.18025（Landau–Gonek 推广，三情形） | ✅ 摘要读到；**作者名单未核验** |
| MathOverflow 484526（smooth Landau–Gonek） | ✅ 读到（**该问暂无回答**） |
| Selberg 矩 / Goldston 细化 / Fujii（arXiv:2211.14918） | ✅ 逐字读到 |
| Berry 数方差（arXiv:2211.14918）、arXiv:1302.1452 | ✅ 摘要/片段读到 |
| van der Corput 二阶导检验形式（4/√(πλ₂)） | ✅ 经 MSE 5055953 逐字；教科书结论（Titchmarsh） |
| BRS 类 H₁ 定义、arXiv:2005.02996、Constr. Approx. 57 (2023) 405–461 | ✅ 定义逐字读到；书目经两处参考表核对 |
| arXiv:2512.18677、1810.08843、2609.02882、1307.5723、2009.13791、2412.15470 | ⚠️ 仅见检索条目/参考表，**未逐篇核验** |
| §0 的支点位置与 n 阶奇点强度、§方向 2 的 ε_n 预算 | ✅ 本文件**自行推导**（初等） |
