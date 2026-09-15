# V184-0 · ⭐⭐⭐⭐⭐ **Inertia Mechanism Audit（反向拆解 67.2% 证明）—— ⭐ 关键一刀的答案：终点会【退化回 Weil 正性】⟹ 按预定规则**关；但机制与"转移原理"两个收获必须留下

> 委托 ✓ 唐先生 2026-09-15 12:50：**"真正值得我们搬运的不是'AI+Lean'，而是论文里的一个结构变化"**；**V184 改题 ＝ Indefinite-Form / Inertia Bridge**；**开 V184-0：Inertia Mechanism Audit**，第一阶段不碰 RH 证明，只做硬拆解（七问），再做关键一刀 **67.2% ⟹ 100%？**（若 100% ⟺ 已等价于 Weil 正性／RH ⟹ **立刻关**）
> 阅读来源 ✓ 论文 arXiv:2608.13637v2（§1.2 三步 (Z)(P)(L) 与单链；Remark 1.1）＋ 本地形式化 `~/lean-repro/formal-math/zeta23/`（`LinAlg/RankTrace.lean`＝Lemma R **精确形式**；`LinAlg/Inertia.lean`、`PairCeiling/Ceiling.lean`、`ZeroSide/`、`PrimeSideA/B`、`Taper/`、`Poisson.lean`；`README.md`）
> 执行 ✓ 小灵（**§1 七问拆解、§2 交换率、§3 终点退化、§4 转移原理 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓｜编号 ✓ **V184-0**

---

## §0 判定（四条）

**① 机制确实是新的 ✓✓✓**
$$\boxed{\text{indefinite quadratic form}\ \longrightarrow\ \text{inertia}\ \longrightarrow\ \text{rank}\ \longrightarrow\ \text{zero-count constraint}}$$
它**不要求** $Q\succeq0$，因此**绕开** `V182` 的困境（"PSD 正性 ⟹ 无计数界"）。这是 V1–V183 **从未审计过**的机制形状 ✓✓✓

**② 但它的杠杆只有一个：**二阶矩**（＝带宽一的素数侧输入）✓✓**
$$\text{单链的常数就是}\ \boxed{2-R(\psi)},\ \text{其中}\ R(\psi)=\lim\|\widetilde G\|_{\rm HS}^2/N;\quad R(\psi_0)=\tfrac43\Longrightarrow\tfrac23;\quad R(\psi_{\rm MT})=c_{\rm MT}^{-1}\approx1.3275\Longrightarrow0.6725\ \ ✓\（\text{本档已核算}）$$

**③ 关键一刀的答案：100% ⟺ $R(\psi)\le1$ ⟺ 需要 **support $>1$** 的输入，且**终点退化为 $n_-(Q_T)=0$ ＝ 正性** ✓✓✓**
$$\textbf{终点退化定理}：n_-(Q_T)\ \text{恰数}\ \textbf{离轴对}\ \Longrightarrow\ 100\%\ \text{要求}\ n_-=0\ \text{对全族成立}\ \Longrightarrow\ \textbf{正性}\ \Longrightarrow\ \text{Weil 正性}\ \Longrightarrow\ \text{RH}$$
$$\qquad\Longrightarrow\ \boxed{\text{inertia 路线}\ \textbf{不是}\text{Weil 正性的替代；它是}\textbf{部分比例}\text{的替代，而在"消灭离轴零点"这一步}\textbf{退回正性}} ✓✓✓$$

**④ 结论 ＝ 关（按预定规则）＋ 两项收获留下 ✓✓**：机制本身（新）；**转移原理**（二阶矩＋惯性 ⟹ 计数下界）—— 后者是 `V182` 的**对偶面**，应进工具箱。

---

## §1 七问逐条拆解（✓ 按唐先生清单）

### (1) $Q_T$ 是什么？——**Weil 形式的 Gabor 压缩**（且**非对角**）

$$\text{Weil 显式公式给 Hermitian 形式}\ W(f,g)=\sum_\rho m_\rho\widehat f(\gamma_\rho)\overline{\widehat g(\overline{\gamma_\rho})},\quad \gamma_\rho=\frac{\rho-\frac12}{i}$$
$$\text{取窗 }\psi\ \text{与}\ \phi(u):=\chi(\tfrac L2+u)\chi(\tfrac L2-u)\psi(u/L)^{1/2};\quad \text{等间距调制}\ \alpha_k:=T+\frac{2\pi k}{L},\ 0\le k<d=\lfloor LT/2\pi\rfloor\（d=N(T,2T)+O(L)）$$
$$v_\rho:=\bigl(\widehat\phi(\gamma_\rho-\alpha_k)\bigr)_{0\le k<d}\in\mathbb C^d;\qquad \widetilde G:=\frac1{aL^2}\sum_{\Re\gamma_\rho\in I'}m_\rho v_\rho v_\rho^{\mathsf T},\quad P:=\text{在线部分},\quad Q:=\widetilde G-P$$
$$\qquad\Longrightarrow\ Q_T\ \textbf{就是}\ d\times d\ \text{的实对称矩阵};\ \textbf{非对角性来自相邻窗的重叠}（\text{Gabor 框架}）：$$
$$\qquad(\widetilde G+\widetilde E)_{kk'}=\frac1{aL^2}\int_{\mathbb R}\widehat\phi(\tau-\alpha_k)\widehat\phi(\tau-\alpha_{k'})\nu_X(\tau)\,d\tau\ ✓\（\text{论文 (2.11)}）$$

### (2) $\operatorname{rank}Q_T$／秩从哪里来？——**秩-迹不等式（Lemma R）**

$$\textbf{Lemma R（论文 §3，形式化精确形式）}：P\succeq0,\ \operatorname{rank}P\le r,\ n_+(Q)\le b\ \Longrightarrow\ \forall c>0：$$
$$\qquad\boxed{\|P+Q\|_F^2\ \ge\ c\operatorname{tr}P-\frac{c^2}{4}r+2c\operatorname{tr}Q-c^2b}$$
$$\qquad\text{证明}：Q=Q_+-Q_-\ \text{谱分解};\ \text{展开}\ \|\cdot\|_F^2;\ \text{弃}\ \operatorname{tr}(PQ_+)\ge0;\ \textbf{von Neumann 迹不等式};\ \text{两个初等序列估计} ✓$$
$$\qquad\text{取}\ c=2\ \text{并解出}\ r：\ \operatorname{rank}P\ \ge\ 2\operatorname{tr}P+4\operatorname{tr}Q-4b-\|P+Q\|_F^2\ \（\text{论文 (1.1)}）✓\ \text{（本档核算一致）}$$
$$\qquad ⚠️\ \textbf{纠正一处}：这不是平凡 Cauchy–Schwarz 界 $\operatorname{rank}\ge(\operatorname{tr})^2/\operatorname{tr}(Q^2)$；Lemma R 是\textbf{两矩阵}不等式，且被证明是}\textbf{紧的}（`ZeroSide/TightMult.lean`：`lemmaR_tight`）✓$$

### (3) $\operatorname{tr}Q_T$ 从哪里来？——**零点平均密度（RvM）**

$$\operatorname{tr}\widetilde G=(1+o(1))N\ \Longleftarrow\ \text{Riemann–von Mangoldt ＋ 归一化（孤立简单在线零点贡献 }1）\ \Longrightarrow\ \boxed{\operatorname{tr}\ \text{是"预算总量"}}$$

### (4) $\operatorname{tr}(Q_T^2)=\|\widetilde G\|_{\rm HS}^2$ 从哪里来？——**素数侧二阶矩（带宽一，无条件）** ⭐

$$\|\widetilde G\|_{\rm HS}^2=\bigl(R(\psi)+o(1)\bigr)N;\quad R(\psi_0)=\tfrac43,\ R(\psi_{\rm MT})=c_{\rm MT}^{-1}$$
$$\qquad\Longleftarrow\ \textbf{Montgomery 的无条件素数侧二阶矩}（[Mon73];\ [Ary22];\ [BGSTB24]）——\ \textbf{带宽}\le1\ ✓✓$$

### (5) $n_-(Q_T)$ 如何编码离轴零点？——**功能方程给 $(1,1)$ block** ⭐⭐

$$\text{在线零点}\ \rho（\beta=\tfrac12）\ \Longrightarrow\ P\ \text{的 rank-one 非负项};\qquad \text{离轴}\ \textbf{成对}\ \{\rho,1-\bar\rho\}\ \Longrightarrow\ Q\ \text{一个签名}\ (1,1)\ \text{的 block}$$
$$\qquad\Longrightarrow\ \boxed{n_-(Q)=\#\{\text{离轴对}\}=p}\（\text{至多差小迹范数尾部}）;\quad N\ge s_1+2s_2+2p;\quad n_+(Q)\le p$$
$$\qquad ⭐\ \textbf{用法与我们旧结论相反}：\text{我们 }V147／V148／V174\ \text{把功能方程当"对合 ⟹ 无单边律／选择难题"};\ \text{本文把它当}\ \textbf{计数装置}（\text{用负惯性数离轴对}）✓✓$$

### (6)(7) 哪些输入是**真正算术的**？哪些只是**已有分析数论**？

| 输入 | 性质 |
|:--|:--|
| **素数侧二阶矩（带宽 ≤1）** | ⭐ **真正算术且无条件**（Aryan；BGSTB）——**唯一的算术杠杆** |
| RvM（零点计数） | 经典分析数论（无条件） |
| $N(t,t+1)\ll\log t$ | 经典（无条件） |
| $\Gamma'/\Gamma$ 的 Stirling 估计 | 经典分析 |
| Chebyshev–Mertens（$\sum\Lambda^2$、$\sum\Lambda^2/n$） | 经典 |
| Montgomery–Vaughan 不等式（频率 $\{\log n\}$） | 经典（Hilbert 型不等式） |
| 功能方程配对结构 | **结构性**（经典） |

$$\boxed{\textbf{不用}\ \text{mollifier};\ \textbf{不用}\ \text{零点密度估计};\ \textbf{不用}\ \text{零自由区}} ✓✓\ \text{—— 这与我们此前的假设不同（我们以为要靠这三样）}$$

---

## §2 ⭐ 关键一刀：67.2% ⟹ 100%？（交换率已显式）

$$\text{由 §1 组装（论文 (1.2)）}：N_0^s+o(N)\ \ge\ \operatorname{rank}P_1\ \ge\ 4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^2\ =\ \bigl(2-R(\psi)-o(1)\bigr)N$$
$$\qquad\Longrightarrow\ \boxed{\frac{N_0^s}{N}\ \ge\ 2-R(\psi)}\quad（\text{本档核算：}R(\psi_0)=\tfrac43\to\tfrac23;\quad R(\psi_{\rm MT})\approx1.3275\to0.6725\ ✓）$$
$$\Longrightarrow\ \textbf{要到}\ 100\%\ \text{必须}\ \boxed{R(\psi)\le1}\ ✓✓$$
$$\qquad ⚠️\ R(\psi)\ \text{由}\ \textbf{带宽一}\ \text{的 form factor 数据确定；且论文已证该类}\textbf{天花板}\ 0.68185\ \text{（形式化 }0.6818287）$$
$$\qquad ⭐\ \text{论文自陈阶梯}：\text{用同一路线达}\ 0.70／0.80／0.90\ \text{需 Fourier 支撑约到}\ \boxed{1.04／1.26／1.70}\ \textbf{（超出已知）}$$
$$\Longrightarrow\ \text{即：}\textbf{67.2% 的 inertia 预算}\ \text{与}\ \textbf{100% 的 inertia 预算}\ \text{之间的桥}\ =\ \textbf{我们 }V162／A3\ \text{的 support}>1\ \text{墙} ✓✓✓$$

---

## §3 ⭐⭐ 终点退化定理（本档决定性结论）

$$\text{由 §1(5)}：n_-(Q_T)\ \textbf{恰数}\ \textbf{离轴对};\qquad \text{因此}\ \boxed{100\%\iff n_-(Q_T)=0\ \text{对全族}\（\text{且尾部可忽略}）}$$
$$\qquad\Longrightarrow\ \text{在固定有限压缩上，}Q_T\ \text{变成}\ \textbf{半正定} \Longrightarrow \text{取极限得 Weil 形式非负} \Longrightarrow \text{[Wei52, Bom00]}\ \textbf{Weil 正性}\iff\text{RH}$$
$$\qquad\Longrightarrow\ \boxed{\text{inertia 路线}\ \textbf{不}\text{是 Weil 正性的替代};\ \text{它只在}\textbf{部分比例}\text{处有效，而在"消灭离轴零点"处}\textbf{退回正性}} ✓✓✓$$
$$\qquad ⭐\ \text{这解释了为什么天花板是}\textbf{结构性的}：\text{rank-迹不等式}\textbf{紧}（\text{形式化已证}）＋\text{天花板是}\textbf{定理} ⟹ \text{方法内部再无空间} ✓$$
$$\qquad\Longrightarrow\ \textbf{按唐先生预定规则}：100\%\ \text{等价于"已等价于 Weil 正性／RH 的条件"} ⟹ \boxed{\textbf{关}} ✓✓✓$$

---

## §4 ⭐ 应当留下的收获（两项）

$$\textbf{(收1) 机制本身（新）} ✓✓✓：\boxed{\text{indefinite form}\to\text{inertia}\to\text{rank}\to\text{counting}}——\ \text{不要求 PSD，故 V182 的"正性 ⟹ 无计数界"}\textbf{不适用};\ \text{它是"在}\textbf{不证正性}\text{的前提下压榨二阶矩"的标准范式}$$
$$\qquad ⚠️\ \text{但注意其}\textbf{限度}：\text{该范式把}\ \textbf{二阶矩}\ \text{转成}\ \textbf{计数下界}，\text{而二阶矩的算术可得性}\textbf{受带宽限制} ⟹ \text{上限}\ 0.68185 ✓$$

$$\textbf{(收2) 转移原理（工具，进我们的筛子表）} ✓✓：$$
$$\qquad\boxed{\ \text{若可算}\ \operatorname{tr}G\ \text{与}\ \|G\|_{\rm HS}^2\（\text{或}\ \operatorname{tr}G^2），\text{并可上界}\ n_+(G-P)\ ⟹ \operatorname{rank}P\ \text{有下界}\ \Longrightarrow\ \text{零点计数下界}\ }$$
$$\qquad ⭐\ \text{这是 }V182\ \text{结论的}\textbf{对偶面}：V182\ \text{说"}\textbf{正性}\ \not\Rightarrow\ \text{计数界"}\（\text{一阶/PSD 信息不足）};\ \text{转移原理说"}\textbf{一阶}\ +\ \textbf{二阶}\ +\ \textbf{正惯性上界}\ \Rightarrow\ \text{计数下界}" ✓✓$$
$$\qquad ⭐\ \text{形式化侧可直接引用}：\text{von Neumann 迹不等式 ＋ Sylvester 惯性定律（双向）}\ \text{此前不在 Mathlib，现已由该形式化}\textbf{贡献} ⟹ \text{可复用} ✓$$

---

## §5 判词与下一步

**V184-0 判词**：① 机制**确实是新的**（indefinite ⟹ inertia ⟹ rank ⟹ counting，绕开 V182）✓✓✓；② 七问全部拆解完成 ✓✓；③ 交换率显式：**$N_0^s/N\ge2-R(\psi)$，100% ⟺ $R\le1$ ⟺ support $>1$** ✓✓✓；④ ⭐ **终点退化定理**：$n_-(Q_T)=0$ ⟺ 正性 ⟹ Weil ⟹ RH ⟹ **按规则关** ✓✓✓；⑤ 两项收获留下（机制／转移原理）✓✓；⑥ 纠正一处（Lemma R ≠ 平凡 C-S 界；且它被证明是紧的）✓。

**净收获**：
- 把你提出的直觉**验证成定理级判断**：inertia **能**绕开正性（局部），但**不能**绕开"n₋=0"（终点）；
- 给出一张**交换率表**（$2-R(\psi)$；阶梯 1.04/1.26/1.70 → 0.70/0.80/0.90），与我们 `V162` 的墙**精确对齐**；
- 新增一条**可复用工具**（转移原理），补上 `V182` 的对偶面。

**下一步（V186 预登记，三选）**：
① **把"转移原理"形式化进我们的筛子表**（与 `V179` 有限支撑筛、`V182` 一阶可和门槛、`V183` 源-基数障碍并列）—— 成本低、可复用；
② 攻 **support $>1$** 的**已知进展**：查 BGSTB／Goldston–Lee–Schettler–Suriajaya（"Alternative Hypothesis" 2025）等**无条件**对相关的**可扩带宽**现状，看 1.04 那一档是否已有人在做；
③ 接受"部分比例路线到 0.682 封顶"，**转回**涨落相消（但按 §3 的逻辑，那仍回到 Weil 正性）。

```
⚠️ §1 公式取自论文 §1.2／§2 与本地形式化 docstring（Lemma R 精确形式；c=2 的解出方式由本档核算）
⚠️ §2 交换率 2−R(ψ) 及数值（4/3→2/3；c_MT^{-1}→0.6725）为【本档核算 ✓】；阶梯 1.04/1.26/1.70 取自论文 Remark 1.1
⚠️ §3 终点退化定理为【本档核心新增 ✓✓✓】—— 依据 §1(5) 的 (1,1)-block 结构与 [Wei52,Bom00] 的 Weil 正性 ⟺ RH
⚠️ §4 转移原理为【本档新增 ✓✓】；Lemma R 紧性引自 `ZeroSide/TightMult.lean`（形式化已证）
⚠️ 本档未独立复核论文证明，亦未复现 Lean 构建
⚠️ 未用 RH ✓（仅作等价性引用）；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 七问拆解 ✓✓；② 交换率 ＋ 天花板对齐 ✓✓✓；③ **终点退化定理（关）** ✓✓✓；④ 两项收获（机制／转移原理）✓✓
```
