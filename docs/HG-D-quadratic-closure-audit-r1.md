# HG-D 二阶闭合审计（第一轮）

**日期**：2026-09-10 14:24+ ｜ 对象：$K_n(a,b)=\sum_{d\mid n}W_n(d)\,e_q\!\big(ad+b\,\frac nd\big)$ ｜ 预算：纸面/纯有限代数

---

## 0. 逃逸确认（唐先生）
```
divisor-complement 在指数向量上是 J(j)=(ν₁−j₁,…,ν_r−j_r) ⟹ 来自【因子分解指数格】，
不是 (ℤ/q)^× 上的幂映射 ⟹ **HG-4 的 k²≡1 (mod λ(q)) 完全管不到它**
⟹ R8 已真正逃出"环可定义对合"那一层 ✓
且状态空间层 CRT 严格成立：D(n)≃D(n₁)×D(n₂)，J_n(d₁d₂)=J_{n₁}(d₁)J_{n₂}(d₂)
（但**振荡核不裸张量**——不能因此判死，因 Kloosterman 亦只带 canonical twist 张量）
```

## 1. ⭐ D1（非 Euler 化）：**验算证实为真死亡机制**
取可分权重 $W_n(d)=f(d)g\big(\frac nd\big)$，则
$$K_n(a,b)=\sum_{d\mid n}f(d)g(n/d)\,e_q\!\big(ad+b\,n/d\big)$$
对 $n$ 求和（$n=dm$，$n/d=m$）：
$$\sum_nK_n=\sum_d\sum_m f(d)g(m)\,e_q(ad+bm)=\Big(\sum_d f(d)e_q(ad)\Big)\Big(\sum_m g(m)e_q(bm)\Big)$$
$$\boxed{\text{可分权重 ⟹ 总和 = 两个独立加法 Fourier 变换之积 ⟹ 完全解耦 ⟹ 死亡}}$$
**⟹ D1 门被【计算确认】**（不是猜测）：可分权重使加法特征与因子反射彻底分离。

## 2. ⭐⭐ D2（二阶有限闭合）：**计算失败，且原因特殊**

$$\big|K_n(a,b)\big|^2=\sum_{d,e\mid n}W_n(d)\overline{W_n(e)}\,e_q\!\Big[a(d-e)+b\Big(\frac nd-\frac ne\Big)\Big],\qquad \frac nd-\frac ne=n\frac{e-d}{de}$$
$$\boxed{\text{指数}=(d-e)\Big(a-\frac{bn}{de}\Big)\ \Longrightarrow\ \text{核心变量}=(\Delta,P):=(d-e,\;de)}$$

### 2.1 ⭐ 关键计算：$(\Delta,P)$ **不是压缩，而是双射重参数化**
$$(d+e)^2=\Delta^2+4P\ \Longrightarrow\ d+e\ \text{由}\ (\Delta,P)\ \text{唯一确定}$$
$$\boxed{\text{故 }(\Delta,P)\ \text{与基本对称对 }(d+e,de)\ \text{等价，且唯一确定 }\{d,e\}\ \text{（至交换）}}$$
**⟹ 二阶层【完全不压缩】——配对信息被完整保留** ⟹ 二阶对象本质上是**配对层（pair-level）**的

### 2.2 二阶核的显式形状
$$\boxed{K^{(2)}\ \text{的形态}=\sum_{d,e\mid n}c(d,e)\,e_q\big(a(d-e)+b(n/d-n/e)\big)}$$
即**"差形式"的 Kloosterman 型求和（over the divisor lattice）**
—— 而这类对象正是 **affine-type association scheme** 的范畴；据 HG-7 文献，
有限环 affine-type scheme 的**特征表由 Kloosterman sums 描述** ⟹ **塔 $K_2\to K_3\to\cdots$ 撞回 Kloosterman envelope**
$$\boxed{\text{⟹ 二阶闭合【失败】：闭合必然进入 association-scheme 层级，而该层已被 Kloosterman 描述（失败模式 (ii)/impostor 类）}}$$

### 2.3 素数幂检验（唐先生，独立佐证退化）
$n=p^r$：状态为链 $0..r$，核 $K_{p^r}=\sum_{j=0}^r w_j e_q(ap^j+bp^{r-j})$
$r=2$ 的中间项 $e_q\big(p(a+b)\big)$ **完全不产生 reciprocal 振荡** ⟹ 素数幂因子格不自动产生 Kloosterman 型逆振荡 ✓

## 3. ⭐⭐ 不可分权重的情形：轨道不变量 $d+\frac nd$ 是 **√n-探测器**
取 $W_n(d)=F\big(d+\frac nd\big)$（唐先生建议的不可分候选）：
$$d+\frac nd\ \ge\ 2\sqrt n,\qquad \text{等号}\iff d=\sqrt n$$
$$\boxed{\text{轨道不变量的最小值恰在【自对偶除数】}d=\sqrt n\ \text{处取到}}$$
**⟹ 与项目长期的 √X 主题强共振**（R3 对合不动点 / λ=2 ⟺ H=√X）
**⚠️ 但必须诚实标注**：这**正是经典的因子自对偶（Dirichlet 双曲线）**
$$\boxed{\text{⟹ 不可分逃逸落回【经典双曲线对象】——Round 2 已识别 (= N43)}}$$
即：它**重新导出**了经典自对偶点，而**不是**提供了新的 √X 机制。

## 4. 本轮裁决：HG-D **两条门当前均未通过**，但失败原因被精确分类

| 门 | 结果 | 原因类别 |
|---|---|---|
| **D1 非 Euler 化** | 可分权重 ⟹ **死亡（已验算）** | Euler 化／解耦 |
| **D2 二阶有限闭合** | **不压缩** ⟹ 配对层 ⟹ association-scheme 塔 ⟹ Kloosterman envelope | 失败模式 (ii)/impostor |
| 不可分逃逸（$F(d+n/d)$） | 轨道不变量 = √n-探测器 = **经典双曲线自对偶** | **经典对象（N43）** |

$$\boxed{\text{⟹ HG-D 第一轮：两条硬门都未过；逃逸口落在【经典结构】而非新机制}}$$
**⚠️ 严格限定**：这是"**当前未找到有限闭合**"，**不是**"已证不存在"（§2.1 的双射性排除了自然压缩，
但不排除某种非自然的 canonical 固定维数状态）。

## 5. 保留的结构收获（即便路线未过）
```
① D1 的死亡机制被【计算确证】：可分权重 ⟹ 总和分解为两个独立加法 Fourier 之积（此前只是定性担心）
② 二阶层相位的显式形态：(d−e)(a−bn/(de)) —— 揭示"配对积 P=de 调制有效加法参数"
③ ("Δ,P) 双射"这一条是一个干净的【否证性引理】：任何声称"二阶状态压缩"的方案必须绕过它
④ 不可分不变量的 √n-探测器性质 —— 解释了为何该路线总被经典双曲线吸回
```

## 6. 诚实边界
```
· §1/§2.1/§2.3/§3 均为【有限代数验算】，严格
· §2.2 的"闭合必然进入 association-scheme 层级"依赖两步：
   (a) 二阶对象是配对层（§2.1 已证）；(b) 该层被 Kloosterman 描述（HG-7 文献级，非分类定理）
   ⟹ 整体为【结构性论证 + 文献级输入】，非定理
· §4 的"两条门未过"是【当前状态】，非不可能性结论
· 未写代码、未做数值；未引入 ζ 零点或谱算子
```

## 7. 提交链
```
da1b2b3 R8-HG-1 → 本篇（HG-D r1）
```
