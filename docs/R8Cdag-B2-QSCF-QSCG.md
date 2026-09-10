# R8-C†-B2：QSC_F / QSC_G 分叉 + Global-QSC Lemma

**日期**：2026-09-10 14:14+ ｜ 依据：唐先生本轮 ｜ 预算：纸面

---

## 1. ⚠️ 撤回 7.1（torus 识别不能给出唯一 Kloosterman）

$$\boxed{R1+R2\ \not\Rightarrow\ \text{标准 Kloosterman}}$$
一般核可写为
$$K_q(a,b)=\sum_{d\in(\mathbb Z/q)^\times}w_q(d)\,e_q(ad+bd^{-1}),\qquad w_{q_1q_2}(d_1,d_2)=w_{q_1}(d_1)w_{q_2}(d_2)$$
仍满足 $K_{q_1q_2}\simeq K_{q_1}\otimes K_{q_2}$，而 $w_q\equiv1$ 只是最特殊情形；
甚至可允许 $d\mapsto\phi(d,d^{-1})$ 的有限局部权重。
$$\boxed{\text{最多压到【torus-twisted exponential kernels】的候选空间，而非唯一核}}$$

## 2. ⚠️ Finite-QSC Lemma 的必要修正：**成立但排除力弱**

```
若 R3/QSC 只要求【有限卷积闭合】，则固定 q 时进入有限群代数
   ℂ[G_q] ≃ ⊕_{π∈Ĝ_q} End(V_π)
⟹ 任何有限核都可分解为有限维不可约表示块
⟹ "finite algebraic closure ⟹ finite representation decomposition" 是【代数事实】，非深层定理
```
$$\boxed{\text{故原 Finite-QSC Lemma 即使成立，也没有真正解决 R8 核心问题}}$$
**改名（唐先生）**：$\boxed{\textbf{Finite-QSC Reduction Lemma}}$——价值是**压缩候选空间**，不是杀死候选。

## 3. ⭐ 真正生死线：Kuznetsov 强在【三层同时闭合】
$$\boxed{\text{finite reciprocity}\ \leftrightarrow\ \text{archimedean harmonic analysis}\ \leftrightarrow\ \text{global spectrum}}$$
具体：$S(m,n;q)$ 必须进入 $\sum_c\frac{S(m,n;c)}{c}J_\nu\!\big(\frac{4\pi\sqrt{mn}}{c}\big)$ 并与**同一谱空间**中的 $\lambda_j(m)\lambda_j(n)$ 匹配。

## 4. ⭐⭐ Z4 少了一层：**QSC_F ≠ QSC_G**
| 级别 | 内容 | 性质 |
|---|---|---|
| **QSC_F** | finite closure: $A_qA_q^*\in\mathcal A_q$，$\dim\mathcal A_q<\infty$ | **近乎代数事实** |
| **QSC_G** | global spectral closure: 存在**统一**谱空间 $\mathscr H$，使 $\{K_q\}_q\to\mathscr H$，且同时含 finite $q$-算术侧 + archimedean transform + global spectral parameter + **同一谱闭合所有 $q$** | **这才是 Kuznetsov/automorphic 有、而普通有限群表示没有的东西** |

**L3 拆两级**：
$$\boxed{\text{L3}_F:\ Z2+Z3+QSC_F\ \Rightarrow\ \text{finite representation envelope}\quad(\text{大概率可证，排除力弱})}$$
$$\boxed{\text{L3}_G:\ Z2+Z3+QSC_G+Z5\ \stackrel{?}{\Longrightarrow}\ \mathcal E_{\rm global}}$$
$$\mathcal E_{\rm global}=\{\text{同一有限算术核族}+\text{同一 archimedean transform}+\text{同一全局谱}\}\ \supset\ \mathcal E_{\rm theta}\cup\mathcal E_{\rm automorphic}\cup\mathcal E_{\rm other\ global\ harmonic}$$
$$\boxed{\mathcal N_G=\text{QSC-G}\setminus\mathcal E_{\rm global}}$$

## 5. ⭐ Epstein/theta 的位置（清楚化）
$$\text{lattice}\to\text{Poisson}\to\Theta\to\text{Weil rep}\to\text{modular/global spectrum}$$
⟹ 它**确实通过 finite/local → global 这一关** ⟹ **Epstein 是 QSC-G 的合法实现**（与 Kuznetsov、GL(n) Voronoi 并列）。

## 6. ⭐ 伪活路命名：**finite-QSC impostor**
```
可精心选 w_q 使 K_q(a,b)=Σ_d w_q(d)e_q(ad+bd^{-1}) 看似五门全过
但若各 q 的谱只是 ℋ_q（各自独立），则未形成 ℋ_global
⟹ 无法把 Λ×Λ 二阶相关推进到统一谱参数
⟹ 标为 **finite-QSC impostor**；由 Z1-IDC 拦截
```
**Z1 再加一层（唐先生）**：
$$\boxed{\text{Global independence}:\ A_q=\mathcal V_q(\Lambda)\ \text{须来自统一构造}\ \mathcal V:\Lambda\mapsto\{A_q\}_{q\ge1}\ \text{与统一谱}\ \mathscr H_{\mathcal V}}$$
（而非逐模数拼装 $\mathscr H_q$）

## 7. R8 的"真正桥"定义（唐先生）
$$\boxed{\Lambda\ \overset{\mathcal V}{\to}\ \{A_q\}\ \overset{\text{finite reciprocity}}{\to}\ \{K_q\}\ \overset{\text{global closure}}{\to}\ \mathscr H}$$
$\mathscr H$ 须同时承载：所有 $q$｜所有尺度｜additive twist｜archimedean transform｜二阶 $A\times A$ closure｜且 Z5 保证未偷偷放入 $\rho$。

## 8. ⚠️ 不能用"有限表示"杀 R8
$$\boxed{(R1+R2+R3)\Rightarrow\text{finite rep}\Rightarrow\text{R8 closed}\ \ \textbf{不成立}}$$
即使第一步成立，也只是**有限代数化**；距 **global spectral realization** 还差最关键一层。

## 9. ⭐ Global-QSC Lemma（新生死线）
假设 $A_q$ 同时满足 Z1（独立生成）、Z2、Z3、QSC_F、QSC_G、Z5，问：
$$\boxed{\text{是否必然存在一个 global harmonic/representation-theoretic object？}}$$
**且即使答案为"是"，也不能直接杀 Λ**——Λ 可能对应一个**尚未发现的 global object**。
$$\boxed{\text{终点必须是}:\ \text{Global-QSC}+\text{Λ 的特定结构约束}\Rightarrow\text{矛盾}}$$
（例如：证明 Λ 的局部 Euler-factor/log-derivative 结构**不能产生所需的 archimedean/global compatibility**）

---

## 10. ⭐⭐ 小灵补两点

### 10.1 QSC-G ≈「系统满足一个 trace formula / Poisson 型全球恒等式」
```
Kuznetsov = GL₂ 的迹公式（几何侧 = Kloosterman，谱侧 = 自守谱，archimedean 核 = Bessel）
Epstein/theta 的 global closure = adelic Poisson + Weil 表示的谱分解（同属"全球恒等式"型）
⟹ **QSC-G 的实质 = 该机制能写成一个 trace formula / Poisson 型全球恒等式**
⟹ 而已知这一切都【从群作用导出】（Kuznetsov ← SL₂(ℤ) 作用；Poisson ← 加法群作用）
⟹ **反例构造目标因此可以精确化**：
$$\boxed{\text{一个【不借助群作用】却仍具 global closure 的有限 reciprocity 系统}}$$
（这与本项目早前"char 0 缺 Frobenius/群作用"（门⑨⑲）形成呼应）
```
### 10.2 ⭐⭐⭐ 最终 NO-GO 的位置已被提前定位：**archimedean 层**
```
QSC-G 要求 archimedean transform 存在（如 Bessel 核）
而 Bessel 核的代数来源 = 函数方程中【Γ 因子的乘性】
L1″ 已确立：Λ 的 archimedean 对偶项 = −χ'/χ = **Γ'/Γ 型 + cot(πs/2) 型**（非乘性）
⟹ **Λ 在 archimedean 层无法提供 Bessel 型核** ⟹ QSC-G 在 archimedean 层失败
⟹ 且此障碍【独立于】有限 reciprocity 层
```
$$\boxed{\text{R8 的最终 NO-GO 是【两层】的：}\text{① 有限 reciprocity 层（QSC\_F，近乎平凡，无排除力）}\\
\text{② archimedean 层（Λ 的 Γ'/Γ + cot ⟹ 无 Bessel 型核）——【排除力在此层】}}$$
**⟹ 因此 Global-QSC Lemma 应【重新加权】**：排除力不在有限 reciprocity，而在 **archimedean compatibility**。
**这与唐先生 §2 的观察（有限层太容易）完全一致**，并给出了排除力的确切所在。

## 11. 当前最窄活口（唐先生）
$$\boxed{\textbf{有限算术 reciprocity 能否在【不预先指定谱】的情况下，自动产生一个跨所有 }q\textbf{、跨尺度、含 archimedean 对偶的统一全球谱？}}$$
**这解释了为何以往路线会死**：它们最多提供其中一层（有限局部／加法 Fourier／静态相关／既定谱），
**从未把 finite arithmetic → global spectrum 这一跃迁作为独立机制解决**。

## 12. 下一步（唐先生指定）
$$\boxed{\text{对 Global-QSC Lemma 做【反例构造】：先尝试构造满足 Z1–Z5、具真正跨 }q\text{ 全球谱、但不属于 }\mathcal E_{\rm global}\text{ 的 }A_q}$$
若能构造 ⟹ 活路；若连构造都不能 ⟹ 才有资格开始证明 Global-QSC 的刚性。
**小灵建议的构造起点（据 §10.1）**：从"不借助群作用"的全球恒等式候选入手（这是 𝒩_G 的最小可能入口）。

## 13. 诚实边界
```
· §1/§3/§4/§5/§6/§7/§9 的结构判定为唐先生本轮给出（结构性整理）
· §10.1 的"QSC-G ≈ trace formula"为小灵的【结构性论证/猜测】，未形式化；"已知一切从群作用导出"为经验陈述
· §10.2 的 archimedean 层排除为【结构性论证】：依赖 L1″（$\Gamma'/\Gamma + \cot$，显式验算）+"Bessel 核源自 Γ 因子乘性"（标准认识）
  —— 但"非乘性 ⟹ 无 Bessel 型核"这一步未形式化；须补证明
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 14. 提交链
```
d3c11e2 L3‴ → 本篇（B2：QSC_F/QSC_G + Global-QSC Lemma）
```
