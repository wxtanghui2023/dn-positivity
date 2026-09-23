已查地图：命中（`ASSET-NATIVE-INDEPENDENT-PROBLEMS`（课题 II 提名）／`I-DH-PARITY-GATE-CLOSED-prior-art`／`META-OBSTRUCTION T1/T2`／`V186 §1(1)`（`v_\rho`）／`V188`（空关系））⟹ **引用，不开新案** ✓
D0: 本档对象 = 课题 II 第一轮：Gabor 测量映射的有限维核计算（盲类普遍性、STP 注入性、T1 的测度论形式）
D1: 0 （`[REVIEW]` 轮次：有限维计算与判定，不主张新自由度）
FREEZE-ACK: D1=0
[REVIEW]

# **课题 II 第一轮：Gabor 测量映射的核与盲类**

## §1 **测量映射（照您的压法 ＋ 一处对偶化简）**

```
$$\mathcal M_\psi(\mu)=\Bigl(\int\widehat\psi(\gamma-\alpha_k)\,d\mu(\gamma)\Bigr)_{0\le k<d}\in\mathbb C^d,\qquad \alpha_k=T+\frac{2\pi k}{L}$$ ✓
【对偶化简（本档）】 取 `\widehat\psi(y)=\int\psi(x)e^{-2\pi ixy}dx` ⟹
　$$\boxed{\ \mathcal M_\psi(\mu)_k=\bigl(\psi\cdot\widehat\mu\bigr)^{\vee}(\alpha_k)\ }$$ —— 即**「乘积 `\psi\cdot\widehat\mu` 的 Fourier 变换在 `\{\alpha_k\}` 的采样」** ✓✓
　⟹ 问题等价于：**采样映射 `F\mapsto(F^{\vee}(\alpha_k))_k` 在函数族 `\{\psi\widehat\mu\}` 上的核** ✓
```

## §2 ⭐ **结论 1：盲类**普遍存在**（不是特殊现象）**

```
【维数计数】 `\mathcal M_\psi` 只有 `d` 个约束；而函数/测度空间**无限维** ⟹
　$$\boxed{\ker\mathcal M_\psi\neq\{0\}\quad(\forall d<\infty)\ \text{—— 只要 } \{\widehat\psi(\cdot-\alpha_k)\}\ \text{有限维张成}}$$ ✓✓
【⟹ 分支判定（本档）】 您提的二分中，$$\boxed{\ \ker=\{0\}\ \text{分支在有限 }d\text{ 下为\textbf{假}}\ }$$ ⟹ **II 不可能给出"无盲性定理"**；II 的真内容只能是**受限类上的可辨识性** ✓✓
```

## §3 ⭐⭐ **结论 2：高斯（更一般：STP）窗 ⟹ `\le d` 原子构型**严格可辨识**（本档核心）**

```
【矩阵】 取 `n` 个高度 `\gamma_1<\dots<\gamma_n` 与 `d` 个采样点 `\alpha_k`：$$A_{jk}=\widehat\psi(\gamma_j-\alpha_k)$$ ✓
【⚠️ 经典事实（档级，Karlin 全正性理论）】 高斯核 `e^{-(x-y)^2}` 是**严格全正（STP）**核 ⟹ 对任意互异 `\{\gamma_j\}`、`\{\alpha_k\}`，**一切子式 `>0`** ✓✓
【⟹ 结论】 `n\le d` 时 `A` 的 `n\times n` 子式**全非零** ⟹ $$A\ \text{列满秩}\ \Longrightarrow\ \boxed{\text{任何 }n\le d\ \text{个不同实高度的构型都被唯一辨识（无盲类）}}$$ ✓✓✓
【⟹ 反面】 盲类**恰从 `n=d+1` 开始**（超定 ⟹ 核 `\ge1` 维）✓✓
```

## §4 **结论 3：核在 `d+1` 处出现且最小情形 1 维**

```
【最小盲构型】 `n=d+1` 点、`d` 个测量 ⟹ 矩阵 `d\times(d+1)` ⟹ $$\dim\ker=d+1-d=1$$（一般位置）✓✓
【读法】 **盲类 = 「比测量数多一个点」的构型族** ⟹ 盲性是**分辨率-计数现象**，非零点几何现象 ✓✓
```

## §5 ⭐⭐⭐ **结论 4：`T1` 的**测度论形式**（本档最有价值的一条）**

```
【您的候选扰动】 $$\nu_\delta:=\delta_{\gamma-i\delta}+\delta_{\gamma+i\delta}-2\delta_\gamma$$ ✓
【其测量向量（本档计算）】 $$\mathcal M_\psi(\nu_\delta)_k=\widehat\psi(\gamma-i\delta-\alpha_k)+\widehat\psi(\gamma+i\delta-\alpha_k)-2\widehat\psi(\gamma-\alpha_k)$$ ⟹ 展开：$$=2\widehat\psi(\gamma-\alpha_k)+\delta^2\widehat\psi''(\gamma-\alpha_k)+O(\delta^4)-2\widehat\psi(\gamma-\alpha_k)$$ ⟹
　$$\boxed{\ \mathcal M_\psi(\nu_\delta)=\delta^2\bigl(\widehat\psi''(\gamma-\alpha_k)\bigr)_k+O(\delta^4)\ }$$ ✓✓
【⭐ 关键】 向量 `(\widehat\psi''(\gamma-\alpha_k))_k` 是**对高度的二阶导** ⟹ 可由**实高度的有限差分**逼近：
　$$\widehat\psi''(\gamma-\alpha_k)=\frac{\widehat\psi(\gamma+h-\alpha_k)-2\widehat\psi(\gamma-\alpha_k)+\widehat\psi(\gamma-h-\alpha_k)}{h^2}+O(h^2)$$ ✓✓
　⟹ 即：**`\nu_\delta` 的测量向量落在「由实高度零点构型可达的 `O(\delta^2)` 方向」内** ⟹ $$\boxed{\nu_\delta\ \text{位于 }\mathcal M_\psi\ \text{的 }O(\delta^2)\text{-近似核}}$$ ✓✓✓
【⟹ 定理化 `T1`/`T2`】 离线对在**一阶与常数阶上无可辨识性**（`O(\delta^2)` 内与"实高度扰动"不可分）⟹ 与 `T1`（σ-配对一阶响应 `=0`）**同一结论**，但本档把它写成**测量映射的近似核命题** ✓✓✓
```

## §6 **判定 ＋ 与痕迹 1 的区别 ＋ novelty 状态**

```
【II 第一轮判定】 (a) 有限 `d` 下 **盲类普遍存在**（核 ≠ 0）✓；(b) 高斯/STP 窗下 **`\le d` 原子严格可辨识** ✓；(c) 盲性从 `d+1` 点起，最小 1 维 ✓；(d) `T1` 扰动落在 `O(\delta^2)`-近似核 ⟹ **II 把元障碍提升为可辨识性命题** ✓✓
【⟹ II 不是"无盲性定理"，而是"**分辨率-计数型可辨识性定理**"】 ✓
【与痕迹 1 的区别】 痕迹 1 针对 `\log`-导数系数与 Euler 支撑/符号（**数论判据**）；II 针对**测量映射的核与 STP 结构**（**调和分析/测度论**）⟹ **不同层** ✓（⚠️ 仍须一次文献核查，记为 II 的 gate）
【`SURVIVOR-5`】 ①未知名定理 ⚠️需核查｜②非重包 ✓｜③不要求 `N_{\rm off}=O(1)` ✓｜④核心量真变（零点 → 测量映射核）✓｜⑤第一轮已有**可计算判据与结论** ✓ ⟹ **II 第一轮 PASS；须补 novelty gate** ✓
```

## §7 **边界**

```
⚠️ §3 的 STP 事实按**档级**（Karlin 全正性理论，未逐字核）；§2/§4 为**初等维数计数**（无外部输入）✓；§5 展开为**本档自行计算** ✓
⛔ 本档**未碰** `DH`／RH／零点分布（按您的裁示 ✓）；未制造候选／未启动搜索／未改状态 ✓
```

## §8 【技术词回查】（逐字粘贴 ✓）

```
技术词 可辨识性     命中文件数=6    :: ./E211-minimal-sufficient-state-audit-no-go.md ./RESEARCH-CONSTITUTION.md ./ASSET-NATIVE-INDEPENDENT-PROBLEMS.md 
技术词 盲测度        命中文件数=2    :: ./ASSET-NATIVE-INDEPENDENT-PROBLEMS.md ./I-DH-PARITY-GATE-CLOSED-prior-art.md 
技术词 total positivity 命中文件数=11   :: ./V124-P-scalarization-threshold-finite-order-barrier.md ./V173-euler-local-flexibility-and-global-coupling-audit.md ./p49-g273r2-even-simple-structural.md 
技术词 Gabor            命中文件数=20   :: ./V186-inertia-mechanism-audit-endpoint-degenerates-to-positivity.md ./ANALYTIC-6-E46-SUMMARY.md ./V185-paper-reading-notes-arXiv-2608-13637.md 
```
【三分类】 **本档新增（命题级）**：`\mathcal M_\psi` 核的有限维计数结论、STP 注入性应用、`T1` 的近似核形式 ⟹ 均为**本档推导** ✓；**档案已有（引用）**：`Gabor`（若命中，见上逐字）；**通用词（不计）**：`可辨识性`／`total positivity`（标准数学词）✓
