# ERR-R8-ARCH-1 撤回 + 算术 hypergroup 框架（R8-C†-B3）

**日期**：2026-09-10 14:17+ ｜ 依据：唐先生核实（Hankel/Poisson、Bessel–Kingman hypergroup、BK–Ngo 框架）｜ 预算：纸面

---

## 0. ⚠️ ERR-R8-ARCH-1（撤回 10.2）

**被撤回**：
> "−ζ'/ζ 的 archimedean functional-equation 项为 Γ'/Γ 型，因此**不能产生** Bessel/Hankel kernel"

**撤回理由**：
```
Bessel/Hankel transform 可有非常一般的参数依赖，其 Mellin 表达式含 Γ 因子；
对参数/谱变量求导后自然产生 ψ(s)=Γ'/Γ（digamma）项
⟹ 出现 Γ'/Γ ⇏ 不能存在 Bessel/Hankel transform
文献：广义 Hankel transform 本身即谱变换；且已存在 **Hankel transform 的 Poisson summation 理论**；
      BK–Ngo 型框架把此类变换推广到一般表示 ρ
```
**保留（L1″ 仍正确）**：
$$\boxed{-\zeta'/\zeta\ \text{的 Mellin FE dual 仍是 logarithmic-derivative/residue 结构}}$$
$$\boxed{\text{但【不得】再推出：logarithmic derivative}\Rightarrow\text{no Bessel transform}}$$
**⟹ archimedean 层**不能作为 Λ 的 NO-GO**。

## 1. 关键事实：global spectral closure **不**蕴含显式群作用
```
Bessel–Kingman hypergroup：卷积在正半轴由 Bessel product formula 产生
   φ_s(r)φ_s(t) = ∫φ_s(u) d(δ_r*δ_t)(u)
   其 Fourier transform = Hankel/Bessel transform
⟹ 标准【非群型】harmonic analysis 实例（文献明确）
矩阵锥上的 Bessel convolution / hypergroup 亦有 Fourier–Plancherel 结构
```
$$\boxed{\text{global spectral closure}\ \not\Rightarrow\ \text{显式 group action}}$$
**但**：Bessel–Kingman 的核心变量是**连续径向变量** $r\in\mathbb R_{\ge0}$；
它**不**自动提供 $(\mathbb Z/q,+)$ 与 $(\mathbb Z/q)^\times$ 的耦合，更无 $d\mapsto d^{-1}$
⟹ 它是"第三类的**原型**"，**尚未进入 R8 的算术入口**。

## 2. 第三类的具体化：**Arithmetic hypergroup**
$$\boxed{H_q:\ \text{finite arithmetic hypergroup};\ R_{q_1q_2}\simeq R_{q_1}\otimes R_{q_2};\ \text{characters contain }d\mapsto d^{-1};\ \text{globalization gives Hankel/Bessel transform};\ \text{one common }\mathscr H;\ \text{zero-blind}}$$
**H1–H5（唐先生）**：H1 inversion symmetry $P_q(a,b;c)=P_q(a^{-1},b^{-1};c^{-1})$｜H2 CRT tensor $P_{q_1q_2}=P_{q_1}\otimes P_{q_2}$｜
H3 reciprocal character $\chi_{q,m}(a)\sim e_q(am+a^{-1}m')$｜H4 global Hankelization $\mathcal H_\nu[A_q](t)$｜H5 zero-blind。

**⚠️ H3 暴露的巨大障碍**：若直接把 $e_q(am+a^{-1}m')$ 塞入 ⟹ 得到**已是 Kloosterman 型对象** $S(m,m';q)$
⟹ 该 hypergroup 很可能立即退化为 **Kloosterman/automorphic envelope**
⟹ **真正的第三类不能"把 Kloosterman 改成 hypergroup"，必须改变【有限层的组合律本身】同时保留 inversion 耦合**

## 3. ⭐ 唐先生的新尝试：**inversion 不作用在点上**
```
传统 Kloosterman：d ↦ d^{-1}（点级 inversion）
Z2 实际只要求：e(an/q) → e(±ā m/q′)，**未规定** ā 须由点变换实现
⟹ 可定义【有限谱 involution】J_q: X̂_q → X̂_q，J_q²=1，使 F_q(e_a)=e_{J_q(a)} 在适当坐标下表现为 a↦a^{-1}
⟹ **reciprocity 来自【谱侧 involution】**，而非 Kloosterman 的点级 torus inversion
```
**优点**：CRT 自然（$J_{q_1q_2}=J_{q_1}\otimes J_{q_2}$）；QSC 天然（$J_q^2=1$ ⟹ 二次闭合）；
**不必**有 $S(m,n;q)=\sum_d e_q(md+nd^{-1})$ ⟹ $\boxed{Z2\not\Rightarrow\text{Kloosterman}}$（承接既有结果）

**Z1 硬门槛**：$J_q$ 不可任意定义（否则 = **finite-QSC impostor**）
$$\boxed{J_q=\mathcal J_q(\Lambda)\quad\text{须局部定义、与 }X,H\text{ 无关、与 }C(X,H)\text{ 无关、CRT 自然、不用零点、不预设谱}}$$

## 4. ⭐⭐ 小灵补：**canonical 谱侧 involution = 复共轭**，而它可能把路线推回 Kloosterman
```
在 (ℤ/q)^× 上，dual = Dirichlet 特征群；其**canonical** 对合 = 复共轭 χ ↦ χ̄
而 χ̄(a)=χ(a^{-1}) ⟹ **共轭恰实现 inversion**（群侧）✓
⟹ J_q = 特征共轭是 canonical（非 impostor）、CRT 自然
```
**但**：一旦同时拥有 (i) 加法特征 $e_q(an)$ 与 (ii) 作用在乘法变量上的 inversion，
**把两者 canonical 耦合的方式恰恰就是 Kloosterman 和**。
更进一步（**待核实**）：有限域上与该对合相容的 harmonic/hypergroup 结构
（GL₂(F_q)/B 的 Hecke 代数、有限域 Bessel 函数）其结构常数即是 Kloosterman 型 ⟹
$$\boxed{\text{最可能的失败模式 = 唐先生三选一中的【inversion 强迫 Kloosterman】}}$$
**⟹ 因此下一轮应把"是否会退回 Kloosterman"作为首要否证目标，而非先找正例。**

## 5. ⭐⭐ 框架升级建议：把"有限算术卷积"放到 **association scheme / Bose–Mesner 代数**语言
```
Delsarte/Bose–Mesner 理论 = 有限 hypergroup 型结构的正规归属（association schemes）
· CRT 张量条件在 scheme 语言中有自然表述
· inversion/共轭对合 = scheme 的（反）自同构/对偶性
· "Kloosterman scheme" 一类 scheme 在代数组合学中已被研究（术语与分类状态【待核实】）
⟹ 下一轮可判定的问题变为：
$$\boxed{\text{在 }\mathbb Z/q\text{ 上的 CRT 张量 scheme 类中，与共轭-compatible inversion 相容者，}\\
\text{是否【只有】Kloosterman 型？（即第三类是否为空）}}$$
```
**这比"再找一个函数"可判定得多**，且失败原因会自动落入你的三选一。

## 6. 反例搜索树与状态表（唐先生）
$$\text{Non-group global closure}\to\text{hypergroup/generalized convolution}\to\text{finite arithmetic structure}\to\text{CRT tensor}\to\text{character-side inversion}\to\text{Bessel/Hankel globalization}\to\text{Z1+Z5 audit}$$
| 环节 | 状态 |
|---|---|
| hypergroup / global harmonic | **存在** |
| Bessel/Hankel global transform | **存在** |
| 非群卷积 | **存在** |
| **finite arithmetic reciprocal hypergroup** | **尚未发现** |
| **CRT-compatible reciprocal hypergroup** | **尚未发现** |
| 能同时进入 Λ 二阶相关 | **完全未知** |
⟹ **第三类目前没有被杀。**

## 7. R8 更新状态表
| 层 | 状态 |
|---|---|
| finite algebra | 太容易 |
| finite representation | 排除力弱 |
| global harmonic | 非群型也存在 |
| **archimedean Bessel** | **不能作为 Λ 的 NO-GO（ERR-R8-ARCH-1）** |
| **finite arithmetic + reciprocal** | **真正未知** |
| **CRT + reciprocal + global Bessel** | **真正未知** |
| **Λ×Λ second-order closure** | **最终门槛** |
$$\boxed{\textbf{R8 的真正活口现在不是"新谱"，而是【新算术卷积】}}$$
（更准确：**new arithmetic hypergroup / character-side reciprocity**）

## 8. 下一轮唯一硬问题（唐先生指定）
$$\boxed{\text{是否存在一个有限算术卷积 }*_q\ \text{满足 CRT tensor + character-side inversion + quadratic closure，}\\
\text{但不是 Kloosterman/Hecke/Weil/automorphic 的重命名？}}$$
**失败原因会非常具体**：究竟 (i) **CRT 杀死 hypergroup**｜(ii) **inversion 强迫 Kloosterman**｜(iii) **global Besselization 强迫已有表示论**。
**小灵建议**：以 (ii) 为**首要否证目标**（§4 的共轭分析指向它），并用 §5 的 scheme 语言做判定。

## 9. 诚实边界
```
· §0 的撤回依据为唐先生核实（Hankel/Poisson summation 文献；Bessel–Kingman hypergroup；BK–Ngo）——文献级
· §1 的"非群型 global harmonic 存在"为文献级；"不自动提供算术耦合"为结构性观察
· §4 的"canonical 谱侧对合 = 共轭"为严格事实（χ̄(a)=χ(a^{-1})）；但"共轭与加法特征的 canonical 耦合即 Kloosterman"
  以及"有限域 Bessel/Hecke 结构常数即 Kloosterman 型"标【待核实】
· §5 的 association scheme 框架为方法论建议；"Kloosterman scheme"术语与分类状态【待核实】
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 10. 提交链
```
fa49a7f B2 → 本篇（ERR-R8-ARCH-1 + 算术 hypergroup 框架）
```
