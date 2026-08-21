# ε_m 符号分解：f'(t) = A cosφ + B sinφ（研究笔记 2026-08-21）

## 来源
唐先生最终评审中的技术建议，与我们的数值发现（ε_m 符号与 (-1)^m 局部同步）一致。

## 精确表达式（评审推导，已验证）

从 Stieltjes 积分 + 分部积分（块边界 f(t_m) = f(t_{m+1}) = 0）：

$$\varepsilon_m = -\int_{B_m} f'(t) S(t)\, dt$$

其中 B_m = [t_{m+1}, t_m]，φ(t) = (n+½)θ(t) ∈ (mπ, (m+1)π)。

## 关键分解

$$f'(t) = 2\theta'(t)\Big[(n+\tfrac12)\cos\varphi(t)\sin\tfrac{\theta(t)}{2} + \tfrac12\sin\varphi(t)\cos\tfrac{\theta(t)}{2}\Big]$$

在 B_m 上：
- **A 项**（振荡）：A_m(t)cosφ(t)，A_m = 2θ'(n+½)sin(θ/2) < 0（θ'<0），cosφ 在块内变号一次
- **B 项**（同号）：B_m(t)sinφ(t)，B_m = θ'cos(θ/2) < 0，sinφ 在块内不变号

因此：
$$\varepsilon_m = \underbrace{-\int_{B_m} A_m\cos\varphi\, S\, dt}_{\text{振荡项，van der Corput}} \underbrace{-\int_{B_m} B_m\sin\varphi\, S\, dt}_{\text{同号项，符号确定}}$$

**第二项的符号是确定的**（与 (-1)^{m+1} 同号）——这正是数值观察到的"ε_m 符号与 (-1)^m 同步"的数学来源。

## 意义

1. **同号项**：符号确定 → 可以按交替级数处理（即使幅度不单调，可用部分和/Abel）
2. **振荡项**：cosφ 块内变号 → van der Corput 适用，高频相位显式
3. 这比"逐项控制 |ε_m|"更弱——只需控制**累积和** Σε_m

## 与 V(S) 饱和的联系

- V(S) ≈ 1000 饱和（T ∈ [3×10³, 7.5×10⁴]）→ S 是有界变差型（对数尺度）
- 若 V(S) = O(log T) 无条件成立，则 van der Corput 给 |振荡项| ≤ V(S·A_m)/n ~ O(log T/n)·n... 需要精确化
- 但同号项可以直接用交替求和 + |S| ≤ C log t

## 待做

- [x] 数值验证 ε_m = -∫ f'S 的分解（A/B 项分别计算）：**B 项 ≈ 0，A 项主导且 ΣepsA 有界**（+0.084/+0.115/−0.025 for n=1000/5000/10000；Σ|epsA| ≤ 0.39）
- [ ] 检查 V(S) 的文献（Fujii 是否已证 V(S) 的界）
- [ ] 严格化：A 项 van der Corput（φ=(n+½)θ 显式）+ B 项交替/直接界 → |Σε_m| ≤ c log n

## 2026-08-21 验证结果（dn_Apart.py）

ε_m 分解数值确认：
- **B 项（同号项）≈ 0**：ΣepsB ≈ ±0.001（可忽略）——唐先生的"符号同步"项贡献可忽略
- **A 项（振荡项）主导**：ΣepsA = +0.084/+0.115/−0.025（n=1000/5000/10000），有界
- **Σ|epsA| ≤ 0.39**：即使绝对值也远小于裕量 0.1934·log n（n=10000 时 = 1.78）
- A 项 = -∫ A·cosφ·S dt，A = 2θ'(n+½)sin(θ/2) 为确定函数，cosφ 高频振荡，φ=(n+½)θ 显式 → **van der Corput 直接适用**

**严格化路径（明确）**：A 项用 van der Corput（显式相位，V(S) 饱和），B 项直接界 → |Σε_m| ≤ c·log n，c 可显式计算。若 c < 0.1934，定理 4 无条件化。

## 注意（已修正）

- Littlewood "M(T) = O(log T)" 引用**不成立**（M(T) 实际增长，见 docs/mt-correction.md）
- 不要在任何 ε_m 论证中使用 M(T) 有界性
