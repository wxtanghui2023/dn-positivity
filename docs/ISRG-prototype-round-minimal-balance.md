# ISRG 造原型轮：最小 arithmetic scale-balance prototype（5 个尝试）

**日期**：2026-09-10 16:52+ ｜ 依据：唐先生 A/B/C/D 模板 + 「先用一个最小原型试活」｜ 预算：纸面
**纪律**：不碰 ζ；不套 RG/谱/范畴/物理等现成名字；只用 +, ×, |, gcd, 素因子分解, v_p, rad, ⌊·⌋

---

## 0. 本轮模板（唐先生）
$$\boxed{\text{不是寻找 }\sqrt X\text{，而是寻找「不预设 }\tfrac12\text{ 的 arithmetic scale law」}}$$
其全尺度 rigidity 自己产生 $\alpha_*$，而 $\alpha_*$ 最后被迫等于 $\tfrac12$

**要求四项**：
```
A  有限尺度观察无法确定临界指数（α_loc 无唯一值）
B  存在真正跨尺度的 primitive law T_{X→Y}（不能拆成各尺度独立约束）
C  存在由该 law 自己产生的守恒/平衡方程 B(α)=0
D  B(α) ≠ B(1−α) 【不作为公理】，但其唯一 admissible 解恰为 α_*=1/2
```
（= 之前 A/B 两轴 + C-rigidity 的动力学化表述）

---

## 1. 尝试 ①：除子配对平衡（$d\leftrightarrow n/d$）
$$\text{状态：}d,\ \tfrac nd\ (d\mid n);\quad\text{平衡点：}d=\tfrac nd\iff d=\sqrt n$$
**A 检验**：每个 $n$ 独立给出平衡点 $\sqrt n$ ⟹ $\alpha$ **局部可读** ⟹ **A-fail**
（且即已注册的 N43 / 双曲线）
$$\boxed{①\ \text{死因}=\textbf{A-fail}（local identity）}$$

## 2. 尝试 ②：乘法求逆流（$n\mapsto 1/n$）+ 不变测度 $dx/x$
**这是【唯一纯粹算术】的自对偶**：$dx/x$ 在 $n\mapsto1/n$ 下不变
设权重 $n^{-s}$，逆变换给 $n^{s}$；自对偶条件
$$-s=s\ \Longrightarrow\ \boxed{s=0}$$
$$\boxed{\textbf{新否定事实 ①}:\ \text{乘法求逆（算术中最纯粹的 self-duality）的自对偶指数}=\alpha=0\ \text{，不是 }\tfrac12}$$
**⟹ 单靠「乘法逆」不可能产生 1/2**；要 1/2 必须用**对象与其对偶之间的 pairing**（$s\leftrightarrow1-s$ 型），
而算术中此类 pairing 只有 FE 型（本轮不碰）/ 有限型（N5）/ 几何型（char 0 无）
$$\boxed{②\ \text{死因}=\textbf{值不对}（\alpha=0\ \text{而非 }\tfrac12）\ +\ \text{无平衡方程}}$$

## 3. 尝试 ③：筛法/Mertens 密度平衡
$$\text{密度}\prod_{p\le z}\Big(1-\frac1p\Big)\sim\frac{e^{-\gamma}}{\log z};\quad\text{「剩一半」给}\ \log z=2e^{-\gamma}$$
* 但「剩一半」是我们**规定**的（人为 1/2）⟹ **D-fail**
* 且真实临界行为住在 $\log$ 变量（$X e^{-c\sqrt{\log X}}$）⟹ **G5-fail**
$$\boxed{③\ \text{死因}=\textbf{D-fail}（人为 1/2）+\textbf{G5-fail}（log 尺度）}$$

## 4. 尝试 ④：平方/位似流（$n\mapsto n^2$，纯算术自映射）
$$\text{log 空间：}u\mapsto 2u\ (\text{位似})\ \Longrightarrow\ \text{无不动指数（只有扩张）}$$
**⟹ 位似流没有自对偶指数**，除非**外接**一个不动点条件（=规定）
$$\boxed{④\ \text{死因}=\text{无内禀不动点}\Longrightarrow \text{任何 }\alpha\ \text{都须外加}}$$

## 5. 尝试 ⑤：「计数 vs 重数」累积平衡
$$\text{加法累积 }A(X)=X;\quad\text{乘法累积 }M(X)=\sum_{n\le X}\Omega(n)=X\log\log X+O(X)$$
* 平衡 $A=M$ ⟹ $X=X\log\log X$：**无解**
* 比例结构 $\log X$ vs $\log\log X$：**无指数平衡方程**
$$\boxed{⑤\ \text{死因}=\text{不存在平衡方程}\ B(\alpha)=0}$$

---

## 6. 结果：算术平衡律的**三难**

所有可用的算术平衡律都落入三者之一：
```
(L)  逐尺度恒等式      ⟹ A-fail（局部可读）—— 双曲线 / 除子配对 / FE 中心化
(G5) log 变量平衡      ⟹ 变量错（√log X 而非 √X）—— 筛法/Mertens
(G6) 统计平衡          ⟹ 非 exact —— 各类平均/拟合
```
**没有一条是「真正跨尺度 + X 尺度 + exact」的平衡律。**

## 7. ⭐⭐ 成分级诊断（本轮真正的产出）

一条平衡律需要**两个成分**：
$$\boxed{\text{balance}=\underbrace{\text{invariance}}_{\text{自对偶/不变测度}}+\underbrace{\text{dissipation}}_{\text{单调耗散/正性}}}$$
| 成分 | 算术现状 |
|---|---|
| **invariance** | **可得**：乘法求逆 + $dx/x$ ✓（但中心在 $\alpha=0$，见 §2）<br>或 FE 型 pairing（本轮不碰；且属 N3） |
| **dissipation** | **缺失**：char 0 中一切无条件 √-尺度正性都来自**有限性**（门⑬）；把有限正性推到极限即失去驱动（moving-edge, P28–P33） |

$$\boxed{\text{算术有【不变性】，但没有【无条件 X-尺度耗散】}}$$
**⟹ 这才是"为什么收得越窄越没方向"的真正答案**：缺的不是候选，而是**成分**——**不平衡律里的耗散项**。
**而且它与既有残差同构**：无条件 X-尺度耗散 ⟺ 独立的 √-尺度正性（门⑬/⑭、LIVE-3）

## 8. 裁决（诚实）
$$\boxed{\text{5 个最小原型无一通过 A+C；但本轮把缺口从【对象级】压到【成分级】}}$$
* 新否定事实 ①：乘法求逆的自对偶指数 = $0$（**1/2 必须来自 pair 型对偶，而非逆**）
* 新否定事实 ②：唯一的精确跨尺度算术恒等式（双曲线）**规定**了它的平衡点 ⟹ A-fail
* 成分级缺口：**无条件 X-尺度耗散**（= 独立 √-尺度正性）
**下一轮构造的唯一合法目标因此是**：
$$\boxed{\text{造一个【不预装 1/2、且自带无条件 X-尺度耗散】的算术跨尺度律}}$$
（若造不出 ⟹ 说明 ISRG 入口本身可能不存在，而非"未找到"）

## 9. 提交链与诚实边界
```
87f8ea8 冻结总表并入 → 本篇（ISRG 原型轮）
```
**诚实边界**：
```
· §0 的 A/B/C/D 模板与「先造一个最小原型」的决定 —— 唐先生本轮
· 五个尝试的构造与检验、三难（L/G5/G6）、成分级诊断（invariance+dissipation）、
  两个新否定事实 —— 小灵本轮
· §2 的 s=0 计算为【初等严格】；§1/§3/§4/§5 的各项死因为【逐步核验】，与既有登记一致
· §7 的"balance = invariance + dissipation" 为【结构性论证】（借自平衡律的一般形态），非定理；
  其与门⑬/⑭ 的同构为结构性识别
· 本轮**未**使用 Λ、未使用 ζ 零点、未引入谱算子；未写代码、未做数值
```
