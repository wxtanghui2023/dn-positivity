# E100 · ⭐⭐⭐ **Frobenius 载体差异 × L2 严格交叉审计** ✓ —— $p=0$ 已证对照 ✓；迁移撞**已判死的 purity 箱** ✗

> 委托 ✓ 唐先生 21:19（更正：函数域 Li 是 $p=0$ ✓；建议做"Frobenius 载体差异 × L2"严格交叉审计 ✓）
> 执行 ✓ 小灵｜脚本 ✓ `scripts/E100_function_field_onset.py` ＋ `.txt` ✓｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 三条结论（✓）

```
✅ **① 接受更正 ✓**：**函数域 Li 判据 ＝ $p=0$ 型** ✗（**不是** $T^2$ ✓）
   $\lambda_K(n)=-\sum_j\alpha_j^n$ ✓、等价性 ✓（我已复核 ✓），起始点 $n_0\approx\frac{\log(2g)}{\varepsilon\log q}$ ✓
   ⟹ **我上一条的框架（"若函数域也 $p=2$ ⟹ 内在"）被否定** ✗ —— **"$T^2$ 是 Li 结构本身的内在尺度"不成立** ✓
⭐⭐ **② $p=0$ 的真正来源不是"有限谱"** ✗ —— 而是 **Frobenius 作用在【有限维极化上同调】上、由 Hodge–Riemann 正定给出 $|\alpha_j|=q^{1/2}$（purity ✓）** ✓✓
   （Weil 曲线 RH 的证明正走此路 ✓）⟹ **purity 才是 $p=0$ 的引擎** ✓✓
⛔ **③ 而 char-0 的对应物【已在总册判死】✗**（本轮最关键的交叉核对 ✓）：
   · `CLOSED-ROUTES-MAP.md` 第 6 箱 ✓："谱／HP 箱（无算术来源）…… **Deninger/Connes（char 0 缺正性）**" ✗
   · `rct-four-layer-final.md` 逐字 ✓："**谱流（终点=HP ＋ 谱线守恒 ＋ 非自适应——）死**" ✗
     ＋ ⭐ "**purity 载体（Frobenius/HP/Weil——全封——）死**" ✗✓✓
   · 第 12 箱「极化⊥元素性箱」✓："正定（Hodge–Riemann；pure 极化 HS 半单）与「非平凡活动」互斥" ✓
     ⟹ "**存在性终审：char 0 无 canonical similitude**" ✗✓
   ⟹ $$\boxed{\text{您问的"char-0 Frobenius 载体"【已在总册判为死】✗ —— 理由 ＝ char 0 缺正性／无 canonical similitude}}$$
```

## 1. 我复核了他的公式（✓ console ✓）

$$\text{必要性 ✓}：|\alpha_j|=q^{1/2}\ \forall j\ \Longrightarrow\ |\lambda_K(n)|\le\sum_j|\alpha_j|^{n}=2g\,q^{n/2}\ \checkmark$$
$$\text{充分性 ✓}：\exists\,|\alpha_*|=q^{1/2+\varepsilon}\ \Longrightarrow\ |\lambda_K(n)|\ge q^{n/2}\bigl(q^{\varepsilon n}-(2g-1)\bigr)\ \text{破坏包络 ✗}\ \Longrightarrow\ \text{全}\le q^{1/2}$$
$$\text{再由}\ \prod_j\alpha_j=q^{g}\ \Longrightarrow\ \Pi|\alpha_j|=q^{g}\ \text{＋全}\le q^{1/2}\ \Longrightarrow\ \textbf{全}=q^{1/2}\ \checkmark$$

## 2. ⭐ $p=0$ 的引擎 ＝ **purity**（✓ 本轮关键澄清 ✓）

| | 函数域 ✓ | 数域 ✗ |
|:--|:--|:--|
| **载体** | **Frobenius 本征值 $\alpha_j$ 本身** ✓ | **阻尼映射 $\rho\mapsto1-\frac1\rho$** ✗ |
| 偏离量的标度 | $|\alpha_*|-q^{1/2}\asymp q^{1/2}\varepsilon\log q$ ⟹ **$\asymp\varepsilon$** ✓ | $|q_\rho|-1\asymp\frac{\varepsilon}{\gamma^{2}}$ ✗ |
| 起始指标 ✓ | $n_0\approx\frac{\log(2g)}{\varepsilon\log q}$ ✓ | $n_0\approx\frac{\gamma^{2}\log M}{\varepsilon}$ ✓ |
| **来源** | **有限维极化上同调 ＋ Hodge–Riemann 正定（purity ✓）** | **无对应结构** ✗ |

$$\text{数值核验 ✓（脚本 ✓）}：\text{测得/预测}\ \to 0.96\sim1.04\ \checkmark\ (\ g=50,q=11\ );\quad g:1\to10^{6}\ \Longrightarrow\ n_0:6.3\to66\ (\textbf{对数 ✓})$$

```
⭐ **故"损失"可精确定位 ✓**：\(\gamma\to\infty\)（数域真实新谱 ✓）＋ 映射 \(\rho\mapsto1-1/\rho\) ⟹ 信号被 \(\gamma^{-2}\) 阻尼 ✗
   函数域无此映射 ✓（无限零点只是同一 Frobenius 根的**周期复制** ✓ \(s=\frac12-\frac{i\theta}{\log q}+\frac{2\pi ik}{\log q}\) ✓）
```

## 3. ⭐⭐ 他的三条件 ⟺ **总册 L2 的 P-Scale 判据**（✓ 交叉识别 ✓）

$$\text{载体要求 ✓}：(i)\ \text{不预设 RH};\quad (ii)\ |\alpha_\rho|-1\asymp\varepsilon\ \text{而非}\ \varepsilon/\gamma^{2};\quad (iii)\ \text{可由算术数据无条件构造}$$
$$\text{L2 的否决判据 ✓}："\text{若候选载体最终只能给出}\ \textbf{height/log 尺度}\ (\text{P-Scale})\ \text{或}\ \zeta\ \text{只能经显式公式进入}\ \Longrightarrow\ \textbf{关闭}"$$

$$\boxed{\text{条件 (ii)}\ \Longleftrightarrow\ \neg\,\text{P-Scale}\ \checkmark\qquad\text{（}\gamma^{-2}\ \text{阻尼正是 height 尺度 ✗）}}$$

⟹ ⭐ **故他的三条件 ＝ L2 判据的【精确化】，而非另一条路** ✓✓ —— **K1 归结为 L2** ✓

## 4. ⭐⭐ 本轮确实**新增**的东西（✓ 三条 ✓）

```
【新增 1 ✓】**一个【已证】的 $p=0$ 对照实验** ✓ —— 函数域 Li 判据是精确的有限维谱半径判据 ✓
   ⟹ 它**证明**"$T^2$ 不是 Li 结构的内在尺度" ✓✓（此前只是推测 ✓）
【新增 2 ✓】**损失位置的精确坐标** ✓：映射 $\rho\mapsto1-\frac1\rho$（＝ Li 的定义 ✓）✗
   ⟹ 损失的**唯一来源**是它 ✓；换成任何**不经过该映射**的载体即可能修复 ✓
【新增 3 ✓】**把 L2 的 P-Scale 判据写成【可计算的形式】✓**：$\ |\alpha_\rho|-1\asymp\varepsilon$（而非 $\varepsilon/\gamma^{2}$）✓
   ⟹ 从此**任何候选载体都可直接检验**（只需看其偏离量对 $\varepsilon$ 的标度 ✓）✓✓
```

## 5. 边界与纪律（✓）

```
✓ **接受更正 ✓**：我上一条把"函数域对照"预设成 $p=2$ 的可能 ✗ —— 错 ✓；**结论方向相反** ✓
⚠️ **未宣布 K1 死** ✗ —— 只判：**K1 的迁移撞上总册【已判死的 purity 箱】** ✗；
   但**总册同时记有"唯一未关闭缺口"** ✓（1️⃣ 处，四种等价表述 ✓："算术特异 ＋ 非 completion ＋ 非 L-测量 ＋ limit-seeing/finite-blind" ✓）
   ⟹ **K1 与 L2 落在这个同一缺口上** ✓ —— 故 K1 **不是新开口** ✓，但也**未被单独判死** ✓
✓ **未用 RH** ✓；**未跑 Lean** ✓；脚本 R1–R7 ✓
⚠️ **未做** ✗：未检索"是否存在已知 char-0 载体具备线性 $\varepsilon$ 偏离" ✗（**这是下一步的唯一问题** ✓，见 §6）
```

## 6. 下一步（✓ 建议 ✓）

$$\boxed{\text{唯一问题：总册那个【单一未关闭缺口】能否被【实例化】为一个载体，使 } |\alpha_\rho|-1\asymp\varepsilon\ ?}$$

```
【建议（依您指示 ✓）】不穷举 $\tau$-Li／高阶 Li／$\xi^{(k)}$ ✗
【改做 ✓】**"purity 箱为何全封"的逐条复核** ✓ —— 即核对：
   ① 谱流为何"终点=HP ＋ 谱线守恒 ＋ 非自适应 ⟹ 死" ✓（读 `rct-four-layer-final.md` 与 `connes-2026-full-audit.md` ✓）
   ② "char 0 无 canonical similitude" 的论证链 ✓（`AOB4-existence-audit-dichotomy.md` ✓）
   ③ 该论证是否恰好**排除**了"线性 $\varepsilon$ 偏离"的载体 ✓ —— 若其排除理由**不覆盖** (ii) ✗ ⟹ **缺口真实存在** ✓✓
```
