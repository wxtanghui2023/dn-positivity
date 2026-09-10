# R_conv 解出：坐标层闭合（唐先生核实原文）

**日期**：2026-09-10 13:48+ ｜ 状态：**R_conv 已解**；**R8v-iv 撤回（被取代）**；**新状态 = R8v-ii（强） + R8.3-B′**

---

## 1. R_conv 解出：$\alpha=\lambda=\dfrac1{1-\eta}$
标准 Montgomery–Goldston 关系：目标区间 $X=T^\alpha$，短区间 $H=X/T$ ⟹ $H=T^{\alpha-1}$，
代入 $T=X^{1/\alpha}$ 得 $H=X^{1-1/\alpha}$。令 $H=X^\eta$：
$$\boxed{\eta=1-\frac1\alpha\qquad\Longleftrightarrow\qquad \alpha=\frac1{1-\eta}}$$
$$\boxed{\alpha=\lambda\quad\text{（同一 Montgomery }F(X,T)\text{ normalization 下的同一参数）}}$$

| $H=X^\eta$ | $\alpha=\lambda$ |
|---|---|
| $\eta=0$ | 1 |
| $\eta=1/3$ | 3/2 |
| **$\eta=1/2$** | **2** |
| $\eta=2/3$ | 3 |
| $\eta\to1^-$ | $+\infty$ |

$$\boxed{H=\sqrt X\iff\eta=\tfrac12\iff\alpha=\lambda=2}$$
⟹ **R8 的"自对偶尺度"不再悬空，已被精确坐标化** ✓

## 2. ⚠️ 取代登记（勘误）：$\alpha=1+\eta$ 为坐标误用
```
被取代：上一轮登记的 α = 1 + log H/log X = 1+η（并据此生成的"1.5 vs 2 未对齐"）
正确：  α = 1/(1−η)
⟹ 之前的"未对齐"是【坐标误用】所致，非两个真实约定冲突
⟹ 本条以取代形式留档（不静默改写）
```

## 3. ⭐ Montgomery–Soundararajan 主项验证该坐标
$$\frac1X\int_0^X\big(\psi(x+H)-\psi(x)-H\big)^2dx\ \sim\ H\log\frac XH$$
令 $H=X^\eta$：$H\log(X/H)=HX(1-\eta)\log X/X$
$$\boxed{\text{尺度系数 }(1-\eta)=\frac1\alpha=\frac1\lambda}$$
⟹ R8.2 的"support 信息进入二阶主项"判断与 Montgomery 的 $F(\alpha)$ 坐标**精确接上** ✓

## 4. ⭐⭐ 第二个前置项：未平均 $V(X,H)$ 的无条件范围
```
结果：**未找到无条件的目标 S2-c 渐近**——不是"没找到论文"：
 · 2024 综述：primes in short intervals 的 variance 之 asymptotics，
   无条件情况下所知甚少（与 RH / Montgomery PC / Hardy–Littlewood 均相关）
 · 同一综述记录 Goldston–Montgomery：**在 RH 下**
     (1/X)∫_0^X(Σ_{x<n≤x+H}Λ(n)−H)²dx ~ H log X (1 − log H/log X)
     对 1 ≤ H ≤ X^{1−ε} 一致成立，**且与 Strong Pair Correlation Conjecture 等价**
```
$$\boxed{\text{S2-c}\ \Longleftrightarrow_{\rm norm}\ \text{short-interval variance asymptotic}\ \Longleftrightarrow_{\rm RH}\ \text{Strong Pair Correlation}}$$
**⚠️ 关键限定（唐先生）**：该等价**在 RH 框架内**建立；**不得**写成"无条件 RH-free 等价"。
⟹ 这同时意味着：**R8v-i（等价点精确定位）以【条件形式】达成**——等价点已被定位，且它是 RH-条件性的。

## 5. A2：结构性可逆（预判获得明确结构依据）
$$S_H(x)=\sum_{x<n\le x+H}\Lambda(n)\ \Longrightarrow\ V(X,H)\sim\sum_{|h|<H}(H-|h|)\,C_X(h)+\text{diag/principal/boundary}$$
三角核 $(H-|h|)$ 满足 $\Delta_H^2(H-|h|)$ 在 $H=h$ 附近产生离散 delta
$$\boxed{\text{A2：结构性可逆；精确公式尚需完整记账}}$$
**三项必须保留的 bookkeeping**：
```
① Λ(n)² diagonal
② 主项 H 的平方及交叉项
③ x-积分边界造成的 O(H²)/endpoint correction
```
**标签纪律**：写"结构性可逆"，**不得**写"已证 exact inverse"。
$$\boxed{\text{⟹ R8v-iii（缺口在变换本身）【排除】}}$$

## 6. A3/A4：坐标已统一，A4 解除悬置
$$\boxed{C(X,H)\ \longleftrightarrow\ V(X,H)\ \longleftrightarrow\ F(\alpha),\qquad \alpha=\frac1{1-\eta}}$$
特别：$C(X,\sqrt X)\leftrightarrow V(X,\sqrt X)\leftrightarrow F(2)$
⟹ R8 的 $\lambda=2$ 与经典 Montgomery $\alpha=2$ **完全统一**
**⚠️ 不得写** $C(X,H)\leftrightarrow F(1+\eta)$（旧坐标误用）
**A4 判定**：四选项中"exact/asymptotic"由经典 GM/LPZ 框架给出，但**方向与假设须逐条标清**；
**不得**把变换关系写成无条件 RH-free 等价。

## 7. 真正缺口（精确定位）
```
不是 C↔V（基本可逆，A2）
不是 H↔η↔α（已闭合：η=1−1/α，λ=α）
```
$$\boxed{\text{真正缺口 = 【求值】：如何无条件求出 }V(X,H)\ \text{的正确非对角主项？}}$$
```
且一旦在整个 X^ε ≤ H ≤ X^{1−ε} 范围正确得到，即进入 α>1 的 Montgomery F 区域，
而经典理论已把该区域与 Strong Pair Correlation 连接（RH 条件性）
```

## 8. 状态更新 + 下一刀
$$\boxed{\textbf{R8v-ii（强）} \quad+\quad \textbf{R8.3-B′}}$$
```
R8v-iv（坐标层未对齐）—— **撤回**（由本篇取代）
Hooley 仍不能成为 R8-A：对象是 AP 方差；短区间范围 h ≥ x^{7/12+ε}；
  主项虽含短区间 h，但 cancellation 的平均坐标仍是 (q,a)
```
**下一刀（两问）**：
$$\boxed{\text{① 严格化 A2（完整记账）}\ \Longrightarrow\ \text{S2-c}\ \Longrightarrow\ \text{目标 }F(\alpha),\ \alpha>1}$$
$$\boxed{\text{② 是否存在一种【完全不经过 }F(\alpha)\text{】的方法，直接给出 }h\text{-shift 非对角主项？}}$$
> ②若被堵死 ⟹ R8-C 才真正开始具有**结构性**，而不只是"已知文献都没做到"的经验判断。

## 9. 诚实边界
```
· §1 的 α=λ 关系来自标准 Montgomery–Goldston normalization（唐先生核实，文献级）
· §4 的两条（2024 综述 + GM 在 RH 下 1≤H≤X^{1−ε} 且等价于 Strong PC）为【文献级】
· §5 的"结构性可逆"为结构性判断（三角核差分），**非已证 exact inverse**
· §6 的四选项判定未逐条落定（仅指出方向/假设须标清）
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```
