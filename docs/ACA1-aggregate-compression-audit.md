# ACA-1：Aggregate Compression Audit（纯纸面，无程序）

**日期**：2026-09-10 ｜ 唐先生指定四步 ｜ 结果：强支持"结构性 NO-GO"分支，但唯一性定理未建立

---

## 0. 设定与要求

$D(x)=\psi(x)-x$，RH 强度等价形式 $|D(X)|\le C_\varepsilon X^{1/2+\varepsilon}$。
候选聚合态 $C$ 必须同时满足（唐先生）：
```
(A) 组合律  C(I∪J)=𝒞(C(I),C(J),X,H)，且不重读 J 中素数
(B) 压缩    L(C_N)=o(N)（最好 polylog）
(C) 聚合    能推出整体命题（非单点判定）
(D) 非等价  不存在已知显式映射 C_N ↔ {ρ: |Im ρ|≤T}
```

## 1. 步一：信息下界

**充分侧（严格，来自显式公式）**：
$$D(x)=-\sum_{|\gamma|\le T}\frac{x^\rho}{\rho}+O\!\Big(\frac{x\log^2 x}{T}\Big)$$
要 pointwise 达到 $O(\sqrt x)$，需 $T\asymp\sqrt x\log^2 x$。零点计数 $N(T)\sim\frac{T}{2\pi}\log T$：
$$\boxed{N\asymp\frac{\sqrt x\,\log^3 x}{4\pi}\ \text{个零点参数 / 精度}\sqrt x}$$
对比素数表 $\pi(x)\sim x/\log x$：
$$\boxed{\text{压缩因子}\sim\sqrt x/\log^4 x}$$
（这就是"解析通道"实际达到的压缩比——零点集确实比素数表紧凑得多。）

**必要侧（启发式，相位计数）**：
$D(x)/\sqrt x=\sum_\gamma c_\gamma x^{i\gamma}$ 是几乎周期和；在尺度 $x$ 处主导项为 $|\gamma|\lesssim\sqrt x\log x$。
pointwise 控制需要**频率的相位**，每个频率需 $\Theta(\log x)$ 比特精度：
$$\boxed{L(C)\gtrsim\Omega(\sqrt x)\ \text{参数（up to logs）}}$$
⟹ **polylog 级状态不可能达成 $\sqrt x$ 精度**（这是 LL 级结论；严格形式需把相位计数固定化）。

## 2. 步二：单尺度统计量是"相位盲"的（严格）

设 $F(x)=D(x)/\sqrt x=\sum_\gamma c_\gamma x^{i\gamma}$。由正交性：
$$\frac1X\int_1^X|F|^2\,dx=\sum_\gamma|c_\gamma|^2\,(1+o(1))\qquad\text{（与相位无关）}$$
$$\boxed{\text{单尺度平均统计量对相位不敏感 ⟹ 不足以做 pointwise 控制}}$$
且注意：$\sum|c_\gamma|^2\sim1$ 给出 $D$ 的 **L² 规模恰为 $\sqrt x$（无条件可得）**。
$$\boxed{\Longrightarrow\ \sqrt x\ \text{是 L² 尺度；RH = L²→L∞ 的零损失}}$$

## 3. 步三：跨尺度不可分解性

pointwise 控制要求频率**在所有尺度上不聚簇**（聚簇会使和冲高过 $\sqrt x$）：
$$\boxed{\text{所需结构 = 全局刚性振荡系统（非独立尺度块之并）}}$$
$$C_{2N}\not\equiv F(C_N,C'_N)\quad\text{（独立尺度摘要）}$$
与既有结论一致：本项目早先测到长程刚性 $\approx0.25\times$GUE——素数/零点的刚性是真实的、跨尺度的。

## 4. 步四：RH 强度门槛

```
PNT 级      : x\,e^{-c\sqrt{\log x}}   ← "无抵消"尺度（坏项密度）
RH  级      : x^{1/2+ε}                ← L² 尺度
⟹ RH = sup 尺度 命中 L² 尺度 = 零 L²→L∞ 损失
⟹ 所需机制是【转移/刚性定理】，不是估计式
⟹ 一切"平均型/筛法/泛型"机制本质上只能停在平均尺度 ⟹ 结构性不足
```

## 5. ACA-1 结论

**必要结构**：一个压缩的、全局刚性的振荡/频率系统，其参数能把 $D$ 控制到 $\sqrt x$ 精度。

**非等价性**：由显式公式，$D$ 的频率**就是**零点。故任何达成 $\sqrt x$ 抵消的候选，
其内部频率系统必须重现零点相位。

**诚实标注（三步的证据等级）**：
```
① 单尺度相位盲      : 严格（正交性）
② 参数计数 √x 级    : 充分侧严格（显式公式）；必要侧为启发式（相位计数需固定化）
③ 刚性要求          : 结构性论证（非定理）
⟹ "不存在非零点等价的压缩聚合态"这一 NO-GO【强支持但未证明】；
   其严格形式本身就是一个新定理。
```

## 6. 因此 ACA-1 的真正产物

$$\boxed{\text{机制层搜索空间已穷尽（FPCA/FPCA-2）＋ 聚合层所需结构已被刻画到"刚性频率系统"}}$$
$$\boxed{\text{唯一剩余问题是【唯一性】：能否存在一个不与零点集等价的刚性频率系统，}\\
\text{对 }D\text{ 产生 }\sqrt x\text{ 抵消？}}$$
而按显式公式，$D$ 的频率被唯一确定——所以这个问题的答案很可能是否定的，
但其证明**正是 RH 级别的定理**。

## 7. 门槛登记（最终）
```
P1″    具体位置约束
P0′    不读取未来 prime label
P-Info 三量分离 I_state/I_rule/I_out（修正版）
P-Type 点式正确性 ⇒/⇒ 聚合刚性（缺蕴含，非独立性定理）——按唐先生修正
P-Phase 新增：候选必须携带【相位信息】；单尺度平均数据相位盲 ⟹ 不足以判别
P-Comp 不采纳（素性 ∈ P，无法判别）
```

**未写程序。** 下一轮若继续，只剩唯一性问题本身（定理级）。
