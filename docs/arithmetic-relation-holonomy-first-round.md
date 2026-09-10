# Arithmetic Relation Holonomy：最小分配律面的首轮判决

**日期**：2026-09-10 ｜ 前置：T4 判 K₂ 关闭 ｜ 新增门槛：Arithmetic Null Separation

---

## 0. 新门槛（唐先生定，写死）

$$\boxed{\textbf{Arithmetic Null Separation}}\qquad
I(\text{真实算术})\;\not\sim\;I(\text{随机权})$$

且差异必须来自**整数的公理性关系**，而非"真实数据更复杂"。
T4 已判：$K_2/\Delta_3$ **未通过**此门槛（random 权 100% 通过 T1、10/10 通过 T3）。
⟹ 以后**"出现三体项"不得作为突破信号**。

---

## 1. 最小分配律面（显式）

重写边：$\;x(y+z)\longrightarrow xy+xz$。

设把每个表达式赋以某个代数 $\mathcal A$ 中的元素（transition），记 $\varphi$。
两种可能：

**(A) 函子性（R2 成立）**：$\varphi$ 是半环同态
$$\varphi:\mathbb N[x,y,z]\longrightarrow\mathcal A .
$$
则 $\varphi(x),\varphi(y),\varphi(z)$ **交换**（同态的像是交换的），于是
$$\varphi\big(x(y+z)\big)=\varphi(x)\varphi(y)+\varphi(x)\varphi(z)=\varphi(xy+xz)$$
$$\boxed{\;H_{\rm dist}:=\varphi(\text{LHS})-\varphi(\text{RHS})\equiv 0\;}$$
即分配律面的 holonomy **恒为恒等**。同理结合律、交换律面全为恒等。

**(B) 非函子性（R2 不成立）**：transition 依赖**语法路径**。
则 $H_{\rm dist}\neq0$ 只反映**路径/字**的差异；把同样的语法结构换上**随机标签**，
照样得到 $H\neq0$（T4 已实测：random 100%）。
$$\boxed{\;\text{不满足 R1（Arithmetic Null Separation）}\;}$$

## 2. 钳形定理（首轮判决）

$$\boxed{\;R2\;\Longrightarrow\;H_{\rm dist}\equiv0\;;\qquad \neg R2\;\Longrightarrow\;R1\text{ 失败}\;}$$

**两条腿都被夹住 ⟹ 以形式半环恒等式（结合/交换/分配）为基础的关系 holonomy 不可能成为桥。
按唐先生"第一轮该杀就杀"的标准：分配律面 [关闭]。**

---

## 3. 唯一的活口：把"形式恒等式"换成"算术恒等式"

钳形的死因是：形式半环恒等式**在任何交换半环**里都成立 ⟹ 函子性强制交换性。
活口必须使用**不是形式推论**的关系，即只在 $\mathbb Z$（特征 0、有具体进位）里成立的：

$$\boxed{\;v_p(a+b)=\min(v_p a,v_p b)\ \text{除非}\ v_p a=v_p b\ \text{（进位）}\;}$$

$$\boxed{\;\text{Kummer}:\ v_p\binom{n}{k}=\#\{\text{在 }k+(n-k)=n\ \text{中的进位}\}\;}$$

理由：
1. 这些**不是**任何交换半环的公理推论 ⟹ 函子性**不**强制交换性 ⟹ 非平凡 holonomy 可能；
2. 随机标签**不能**满足进位律 ⟹ 有希望通过 R1。

## 4. 与全部历史结论的一致性（说明这不是又一次换名字）

```
· 早期结论：加法是唯一打破 Sym(ℙ) 的要素
· v2 结论：进位是跨素数耦合的唯一来源（2¹⁰+1=5²·41）
· C2-a 结论：rad/整除类权在四状态差分中深度被消掉（K_p=1）
⟹ 三者共同指向同一处：进位/赋值层的加法×乘法交互
   这正是"算术关系 holonomy"唯一未被排除的落点
```

## 5. 首轮可测判据（不做事前扫描）

```
RH1：进位关系面上的 holonomy 是否 ≡0？
     若 ≡0 且对随机标签也 ≡0 ⟹ 关闭
RH2：Arithmetic Null Separation：H_arith ≁ H_random（必须系统性地分不开）
RH3：关系同伦：H(γ₁∘γ₂) = H(γ₁)H(γ₂) 是否成立
     （注意：若 RH3 成立且关系是形式的，则由 §2 必死 ⟹ RH3 只应在进位关系上检验）
```

## 6. 状态

```
rad/product curvature   : 关闭（C2-a 证书）
K₂ 非交换矩阵曲率        : 关闭（T4）
分配律/结合律 holonomy   : 关闭（§2 钳形定理）
Arithmetic relation holonomy（进位层）: 待审，唯一活口
```

---

# 进位层（最后活口）关闭（2026-09-10）

## RH1（计数版）：由定理自动失败
```
p=2,3 验证：经典恒等式 K = [S(a)+S(b)−S(a+b)]/(p−1) 成立 ✓
             分组无关 K_L = K_R 成立 ✓
K_L = K_R = [S(a)+S(b)+S(c) − S(a+b+c)]/(p−1)   （S(a+b) 精确抵消）
⟹ 总进位数 = 势函数差（coboundary）⟹ 结合律面上 holonomy 恒为 0（定理，非数值）
```

## RH1（模式版）：通过但无判别力
```
进位位向量差 ≠ 0：p=2 81.3% | p=3 67.9%
但由路径中间值唯一确定（确定性函数）⟹ 历史硬编码 ⟹ 保留中间值的零模型照样复现
```

## RH2：失败（死因 = CRT 的统计表现）
```
corr(v2(a+b), v3(a+b)) = −0.0092
corr(v2(a+b), v5(a+b)) = −0.0084
corr(v3(a+b), v5(a+b)) = +0.0028
⟹ 不同素数赋值在随机输入下统计独立 ⟹ 逐素数打乱的零模型统计不可分 ⟹ 无 Null Separation
```

## 死因三条（逐条给）
```
① 不变部分（总进位）：coboundary ⟹ 可积 ⟹ holonomy ≡ 0（定理）
② 路径部分（进位模式）：中间值的确定性函数 ⟹ 历史硬编码 ⟹ 零模型可复现
③ 跨素数部分：CRT ⟹ 统计独立 ⟹ 零模型统计不可分
```

---

# 通用筛（本段研究的最重要产物）

## Integrability–Null Pincer
$$\boxed{\text{任一候选结构的不变量必落入二者之一，且二者皆死}}$$
```
(i)  coboundary / 势函数差 ⟹ 可积 ⟹ holonomy 恒为 0
(ii) 依赖路径 ⟹ 轨迹的确定性函数 ⟹ 保留轨迹统计的零模型可复现
```
**推论（元结论）**：ℤ 中"自由"的算术——形式的（半环公理）、组合的（数字恒等式）、
CRT 的——恰好就是零模型能复现的那一部分。剩下的正是**素数分布本身**，即 RH 所在之处。
本段三条支线（rad/product curvature、K₂ 非交换矩阵、进位层）各自独立地落进此筛。

## 登记册最终状态
```
rad/product curvature      : 关闭（C2-a 证书）
K₂ 非交换矩阵曲率           : 关闭（T4：random 权照样通过）
分配律/结合律 holonomy      : 关闭（钳形定理：函子性 ⇒ 交换 ⇒ H≡0）
进位层 holonomy             : 关闭（本轮：①coboundary ②历史硬编码 ③CRT 独立）
新增固资产                  : Arithmetic Null Separation 门槛 + Integrability–Null Pincer
```
