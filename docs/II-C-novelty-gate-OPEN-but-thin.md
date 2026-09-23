已查地图：命中（`II-GABOR-BLIND-MEASURE-round1`／`I-DH-PARITY-GATE-CLOSED-prior-art`／`ASSET-NATIVE-INDEPENDENT-PROBLEMS`／`META-OBSTRUCTION`）⟹ **引用，不开新案** ✓
D0: 本档对象 = 课题 II-C 的 novelty gate（仅 C：`\sigma`-对称离线扰动落在有限 Gabor 测量的**近似核**内）＋ 内容厚度判定
D1: 0 （`[REVIEW]` 轮次：核查与厚度判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **II-C novelty gate：未撞车（OPEN），但**薄**——建议不升级为研究线**

## §1 **本档任务（照录您的裁示）**

```
只核查 II-C：$$\boxed{\ \frac{\mathcal M_\psi(\nu_\delta)}{\delta^2}\to\bigl(\widehat\psi''(\gamma-\alpha_k)\bigr)_k\ },\qquad \nu_\delta=\delta_{\gamma-i\delta}+\delta_{\gamma+i\delta}-2\delta_\gamma$$ 及其"σ-对称离线扰动 ∈ 有限 Gabor 测量的**近似核**"的完整定理化表述，是否已有同型先例 ✓（**不做乙**，不碰稳定性）✓
```

## §2 **检索结果（两轮定向，逐字）**

```
【命中 1（邻近，非本命题）】 **FRI（finite rate of innovation）**：Vetterli–Marziliano–Blu 系 —— "sampling theorems for classes of signals and kernels"，采样点**在实轴**、目标是**重构** ⟹ 与"复偏移评估 + 近似核"**不同层** ✓
【命中 2（邻近，非本命题）】 **Kloos–Stöckler**：Gabor 框架与**全正性（STP）**的联系 ⟹ 覆盖 II-**A**（原子唯一性），**不覆盖** II-C ✓
【命中 3（邻近，非本命题）】 **复点评估/解析延拓**：标准数学常识（唯一延拓），**未**用于"离线扰动 vs 实高度扰动的可分辨性" ✓
【命中 4（"approximate kernel / null space" 检索）】 返回均为**机器学习核近似**（Nyström/低秩）⟹ **与本命题无关** ✗✓
【⟹ 检索结论】 $$\boxed{\text{未发现 II-C 的同型先例（在本次两轮定向检索范围内）}}$$ ✓ —— 记为 **II-C = OPEN**（⚠️ 证据强度：snippet 级、两轮、单一来源族 ⟹ 档级 ✓）
```

## §3 ⚠️ **但内容厚度判定（本档核心，比 novelty 更重要）**

```
【成分拆解】 II-C 的陈述含三部分：
**(i)** 恒等式 `\mathcal M_\psi(\nu_\delta)=\delta^2\widehat\psi''+O(\delta^4)` ⟹ **初等 Taylor 展开** ⟹ 技术无新 ✗
**(ii)** 其解释"∈ 近似核" ⟹ **＝本线 `T1` 的换语言重述**（`T1`：σ-配对一阶响应 `=0`，二阶 `\delta^2\hat h''`）⟹ $$\boxed{\text{(ii) 是对我们\textbf{自己}结果的再包装}}$$ ✗ —— 按 `SURVIVOR-5` 第 ④ 条（**核心量必须真正改变**）与 `E-41`（再包装不得升级）⟹ **不构成新对象** ✓✓
**(iii)** 唯一可能有料者：**"精确核"（`d+1` 原子）与"近似核"（`\delta\to0` 方向）之间的差别** ⟹ 即**可分辨性的阶**：要用 `d` 个实高度点把 `(\widehat\psi'')` 表达出来只能到精度 `O(h^2)`（`h` 为可达间距）⟹ 判据变为 $$\text{可分辨} \iff \delta^2\ \gtrsim\ h^2\quad\text{即}\quad \delta\gtrsim h$$ ✓✓ —— **这是一个真正的量化权衡，且不是初等恒等式** ✓
```

## §4 **判定（本档）**

```
【novelty】 II-C = **OPEN**（未发现先例）✓
【厚度】 ⛔ **(i)(ii) 无新**；✅ **(iii) 有实质**（`\delta` vs 可达间距 `h` 的**权衡关系**）✓✓
【⟹ 建议】 $$\boxed{\text{不把 II-C 本身升级为研究线}}$$（其主体是自家 `T1` 的换语言版 ✗）；若继续，**只做 (iii)**：
　$$\boxed{\text{【可提问题】`d` 个 Gabor 测量下，σ-对称离线对可被辨识的\textbf{最小 }\delta\ \text{下界}}{\sim d^{-?}}\ \text{是什么？}}$$ ✓✓
【⚠️ 但 (iii) 须先再过一次 gate】 它与 **sampling/uncertainty/超分辨（super-resolution）** 文献**邻近**（尤其"两近点分辨极限"型结果）⟹ ⛔ 不得直接启动；须先核"**复偏移对 vs 实点扰动**的最小 `\delta` 下界"是否已有 ⟹ **记为 II-D，待裁** ✓✓
```

## §5 **结论与边界**

```
【结论】 $$II\text{-C}=\text{OPEN（未撞车）但薄（主体＝自家 }T1\text{ 换语言）}\ \Longrightarrow\ \text{不建议升级；只保留问题 II-D}$$ ✓✓
【`SURVIVOR-5` 复检（对 II-D）】 ①需 gate｜②非重包 ✓（与 `T1` 不同的量化对象）｜③不要求 `N_{\rm off}=O(1)` ✓｜④核心量真变（从"是否可检测"变为"**最小可检测 `\delta`**"）✓｜⑤第一轮可计算（有限维 SVD/最小奇异值）✓ ⟹ **II-D 是本轮唯一值得保留的产物** ✓✓
【边界】 ⚠️ §2 检索为**两轮定向 + snippet 级** ⟹ 档级；§3 (iii) 的权衡推导为**本档自行推导** ✓；⛔ 未碰 `DH`／RH／零点分布；未制造候选／未启动搜索／未改状态 ✓
```

## §6 【技术词回查】（逐字粘贴 ✓）

```
技术词 approximate kernel 命中文件数=0    :: 
技术词 distinguishability 命中文件数=9    :: ./RESEARCH-CONSTITUTION.md ./p46-g3-canonical-representative.md ./WEAK-RH-LOCALIZATION-LINE-STATE-SUMMARY.md 
```
【三分类】 **本档新增**：`II-D` 问题表述（最小可检测 `\delta` 下界）与 `\delta\gtrsim h` 权衡 ✓；**档案已有（引用）**：无同型；**通用词（不计）**：`approximate kernel`／`distinguishability`（标准英文词）✓
