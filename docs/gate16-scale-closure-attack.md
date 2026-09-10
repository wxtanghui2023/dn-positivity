# 第⑯关：Scale-Closure Attack（P-Lock* 存在性审计）

**日期**：2026-09-10 ｜ 承接 `41711d0` ｜ 结果：**char 0 【存在】尺度闭包——在自守/谱世界；断裂点是"空间+流"而非"闭包本身"**

---

## 0. P-Lock* 的正式形式（唐先生升级）
允许一般尺度闭包：存在三个自然量
$$C(X)=\text{计数尺度},\quad M(X)=\text{内禀动力学尺度},\quad W(X)=\text{权重单位}$$
以及**内禀、非人为**的代数关系 $\Phi(C,M,W)=0$，使自对偶权重自然给出 $W(X)\asymp X^{1/2}$。
（最理想仍 $C=M=W^2$，但允许更一般锁定。）**禁止参数作弊**：不能人为规定 $M=X,\ W=\sqrt X$。

九项要求：C 计数 / M 内禀动力学 / W 权重 / L 锁定关系 / D 自对偶 / P 独立正性 / I 整性 / G 共轭同步 / N 不读零点。

---

## 1. ⭐ 审计发现：char 0 的自守/谱世界**有**尺度闭包

### (i) Patterson–Sullivan 临界指数闭包
```
C : 闭测地线计数 ~ e^{δL}/L            （δ = 临界指数 = 计数增长率）
M : 测地流 / 群作用                     （内禀动力学）
W : 谱底 √λ ↔ δ                         （权重）
L : δ 与谱底由【同一对象】锁定 ⟹ 自对偶点
```
对共紧曲面：$\delta=1$、谱底 $=0$；对夹在镜面间的曲面：$\delta\in(1/2,1)$，谱底 $<1/4$ ⟹
$$\boxed{\delta\ \text{与谱底由同一临界结构锁定}}$$

### (ii) **Selberg 1/4 猜想 = 该闭包在算术情形的尖锐形态**
$$\lambda_1\ \ge\ \frac14\ \Big(=(1/2)^2\Big)\quad\text{对同余子群 $$\Gamma_0(N)$$}$$
- 这是 **char 0 的"谱底必落在自对偶点 1/2"** 命题 ✓
- **无条件**（非 RH 依赖）✓、**非 Fourier** ✓、**非 Weil** ✓
- 最佳部分结果：$975/4096\approx0.238<0.25$（Kim–Sarnak 2003）——**本身仍是开问题**

### (iii) Ramanujan / temperedness
$$\text{局部谱参数 }|\alpha_p|=\sqrt{\text{scale}}\quad(\text{如权 12 形式 }|\alpha_p|\le 2\sqrt p)$$
——**这是 char 0 的"$|\alpha|=\sqrt{\text{scale}}$"结构的真实存在** ✓
（但最难的实例 Deligne 是用 **char p 几何**证的 ⟹ 见 §3）

## 2. 因此第⑯关的第一层裁决：P-Lock* **不是空条件**

$$\boxed{\text{char 0 【有】尺度闭包（自守/谱世界），且它们不是 Fourier/Weil/RH-循环}}$$
⟹ 第⑮关那句"char 0 缺锁定"需要**收窄**为：
$$\boxed{\text{char 0 缺的不是"闭包"，而是承载闭包的【空间 + 流】}}$$

## 3. 断裂点的精确位置

| 闭包 | 承载物 | Spec ℤ 是否有 |
|---|---|---|
| Patterson–Sullivan / Selberg 1/4 | 对称空间 + 测地流 | ✗（ℚ 无此空间） |
| Ramanujan / temperedness | 自守表示 + Hecke | ✓（有 Hecke，但**证明走 char p 几何**） |
| Frobenius 锁定（⑮关） | 有限域几何 | ✗（char p 特有） |

$$\boxed{\text{⟹ 三处闭包的共同承载物是"具有内禀流的几何/群对象"；}}\\
\text{Spec ℤ 恰恰缺这个（= Arakelov/Connes 纲领的全部动机）}}$$

## 4. 与第⑮关的合并结论（本轮真正产出）

$$\boxed{\text{十五关的"三重锁定}" \to \text{本关的"闭包需空间+流"} \to
\text{Spec ℤ 无非平凡内禀流}}$$
$$\boxed{\text{⟹ 残余问题被精确化为：}\textbf{Spec ℤ 是否可能携带（哪怕是奇异的）空间+流？}}$$
——**这正是 Connes "scaling site" 纲领**；而该项目中具体的一步（prolate 桥）已被本项目数值判崩（P49-G2.7.4）；
但**"闭包机制"本身**（Patterson–Sullivan / Selberg 1/4 型）**未被本项目审计过** ✓

## 5. 止损条件的检查（唐先生设）

P-Lock* 的闭包在 char 0 的实现**不来自**清单七项：
```
✗ Fourier/Pontryagin（PS/Selberg 是谱几何，不是特征理论）
✗ Frobenius
✗ height/discriminant
✗ Arakelov
✗ explicit formula
✗ Weil quadratic form
✗ 已知 RH criterion
```
$$\boxed{\text{⟹ 按你的止损条件，本关【不触发关闭】；P-Lock* 应升格为"真缺口"但内容改写为"缺空间+流"}}$$

## 6. 第⑯关裁决

```
P-Lock（⑮，"必须同一参数"）      : 过强，修正（可能误杀）——已按你的意见弃用
P-Lock*（本关，"闭包需空间+流"）  : char 0 有实现（自守/谱），故非空条件
新残余                            : Spec ℤ 的内禀空间+流（奇异的或在算术 site 上）
未被本项目审计的机制              : Patterson–Sullivan / Selberg 1/4 型闭包
```

## 7. 诚实边界
```
· "闭包需空间+流"是对 PS/Selberg 情形的结构性解读，不是定理
· Selberg 1/4 本身仍是开问题（975/4096）⟹ 不可用作已证基石
· "Spec ℤ 无内禀流"是【未找到】（且是 Connes 纲领的公开困难）
· 未写程序；RH 本身未动
```

## 8. 提交链
```
41711d0 ⑮ → 本篇 ⑯
```
