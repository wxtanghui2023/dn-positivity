# ABD-0：Arithmetic Balance Defect —— 构造与实算

**日期**：2026-09-10 17:25+ ｜ 依据：唐先生「造机器，不审计」｜ 代码：`scripts/abd0.py` ｜ 输出：`/tmp/abd0_out.txt`

---

## 0. 规格登记（唐先生）
$$\boxed{\text{不是生成 }\sqrt X,\ \text{而是生成一个跨尺度稳定性方程，其唯一中性点恰好是 }\alpha=\tfrac12}$$
**ABD 定义**：对整数三元组 $a+b=c$（同时记录乘积 $ab$），混合尺度矩
$$\mathcal B_X(\alpha)=\sum_{\substack{a+b=c\\ c\le X}}W_X(a,b,c)\Big[\Big(\frac{ab}{c^2}\Big)^{\alpha}-\Big(\frac{ab}{c^2}\Big)^{1-\alpha}\Big]$$
**禁令**：不得人为规定 $X_{k+1}=2X_k$；不得把 $1/2$ 写入权重；不得用 ζ 零点 / 显式公式 / 统计拟合
**目标**：标量闭合量 $E_X(\alpha)$ 满足精确尺度演化 $E_{X'}(\alpha)=\Phi_{X,X'}(\alpha,E_X)$，
且 $\limsup_X|E_X(\alpha)|<\infty$ **只在 $\alpha=\tfrac12$ 成立** ⟹ 指数是**稳定流形的参数**，不是 observable

## 1. 机器（本轮实际构造）
$$r=\frac ac,\quad 1-r=\frac bc,\qquad m=\frac{ab}{c^2}=r(1-r)\quad(\text{乘积两个因子}\Rightarrow\textbf{arity}=2)$$
* 单态转移：$\rho_{\rm state}(\alpha)=\sum_{i}m_i^{\alpha}$（对 children 求和）
* **临界根**：$\rho_{\rm state}(\alpha)=1$ ⟹ 这是 **Moran 型方程**（自相似维数方程）

---

## 2. PART 1：算术上界钉死 $m\le 1/4$【精确】
```
c<=1500 全部三元组穷举：m_max = 0.25（在 a=b 处）
m = 1/4 精确成立的三元组数 = 750（全部满足 a=b，即精确加法平衡）
```
$$\boxed{m=\frac{ab}{c^2}\le\frac14\quad(\text{AM-GM，纯算术}),\qquad\text{等号}\iff a=b}$$
**⟹ 指数被纯算术【从上方】钉住，不是被插入的。**

## 3. PART 2/3：唯一"无选择"的 refinement ⟹ 中性点**发散**【精确数值】
**R_full**（唯一强制、无参数）：$\{(\ x,\ c-x,\ c\ ):\ x=1,\dots,c-1\}$
| c | $\alpha_*(c)$ | $\rho(1/2)$ |
|---|---|---|
| 10 | 1.307891555 | 3.80e+00 |
| 50 | 2.328119912 | 1.96e+01 |
| 100 | 2.779084602 | 3.92e+01 |
| 800 | 4.160379047 | 3.14e+02 |

闭式校验 $c\cdot C(\alpha)=1$，$C(\alpha)=B(1+\alpha,1+\alpha)$：$c=10^6\Rightarrow\alpha_*=9.055$
$$\boxed{\alpha_*(c)\sim\tfrac12\log_2 c\ \text{（发散）};\quad \alpha_*/\log_2 c\to 0.5\ \text{（缓慢，}c=10^6\ \text{时 }0.454\text{）}}$$
**⟹ 无尺度稳定的中性常数；强度：分支数 $\sim c$ 线性增长而每个 child 尺度 $<1$，
必须把 $\alpha$ 上推才能把和压到 1（系数 $1/2$ 又是 $1/\text{arity}$，因最大尺度 $=1/4=2^{-2}$）**
**⟹ 无选择 refinement 在此处一关即死（不是死在别处）**

### ⚠️ 勘误（记录，不静默重写）
首轮跑出的结论文字误写为"$\alpha_*\to0$"（单调方向写反）；实为**发散**。已修正代码并重跑，
输出文件旧声明计数 = 0。**结论方向（"无稳定中性点"）不变，但机制表述必须按发散写法。**

## 4. PART 4：根何时恰为 $1/2$？【精确】
均匀 $k$-child（每个 child 同尺度 $m$）：$k\,m^{\alpha}=1\iff\alpha_*=\dfrac{\log k}{\log(1/m)}$
| k | m | $\alpha_*$ |
|---|---|---|
| 2 | 0.25 | **0.500000000000** |
| 2 | 0.125 | 0.333333333333 |
| 3 | 1/9 | **0.500000000000** |
| 4 | 1/16 | **0.500000000000** |
$$\boxed{\alpha_*=\tfrac12\iff m=\frac{1}{k^2}\iff\text{两个因子各为 }\frac1k\iff\alpha_*=\frac{1}{\text{arity}},\ \text{arity}=2}$$
**⟹ "2" 来自乘积 $ab$ 的因子数（算术），不是插入**

## 5. PART 5：非对称 canonical 2-child（拆较大者）⟹ $1/2$ 是**上确界**【精确数值】
R_split：$a\ge b$ 时 children $=(1,c-1,c)$ 与 $(a-1,b+1,c)$
| c | a | b | $m_1$ | $m_2$ | $\alpha_*$ |
|---|---|---|---|---|---|
| 20 | 10 | 10 | 0.0475 | 0.2475 | 0.3283184 |
| 120 | 60 | 60 | 0.008264 | 0.249931 | 0.2535509 |
| 1000 | 500 | 500 | 0.000999 | 0.249999 | 0.2032548 |
| 1000 | 100 | 900 | 0.000999 | 0.089199 | 0.1626574 |
$$\boxed{\text{非对称实例一律 }\alpha_*<\tfrac12\ \text{（严格）},\ \text{当 }a/b\to1\ \text{时}\to\tfrac12}$$
**⟹ $\tfrac12$ = 可达指数的【上确界】，由 AM-GM 从上方钉住，非插入**

## 6. PART 6：跨尺度稳定性 ❌
聚合压力 $T_X(\alpha)={\rm mean}_{c\le X}\rho_{\rm full}(c,\alpha)$，$T_X(\alpha)=1$ 的根：
$$X=10:\ 0.977;\ X=100:\ 2.341;\ X=400:\ 3.239;\ X=10^6:\ 8.573$$
**⟹ 中性点随尺度上发散：无选择 refinement 不满足 ABD 的稳定性要求**

## 7. PART 7：反对称性 $\mathcal B_X(\alpha)=-\mathcal B_X(1-\alpha)$
数值验证（$c\le300$，和 $=0$ 或 $10^{-12}$）：**精确成立**，故 $\mathcal B_X(1/2)=0$ 平凡。
**⟹ 此反对称性是【搬运进来的】，不是生成的 ⟹ N3 危险（与唐先生预判一致）**

---

## 8. ⭐ 裁决（ABD-0 的回答）
$$\boxed{\text{他问的具体问题是：}\exists\ \text{canonical refinement }R:\ \rho_R(\alpha)=1\ \text{有【内生产生】的非平凡根？}}$$
```
(i)   根【有】，但这是【自动的】：k>=2 时 rho 连续、递减、rho(0+)=k、rho(inf)=0
      => "根的存在"不是判别性检验；内容全在【根在哪里】
(ii)  唯一【无选择】的 refinement（全拆分）=> 无稳定中性常数（发散 ~ (1/2)log2 c）=> 死
(iii) alpha_*=1/2 <=> 均匀 k-child 且 m=1/k^2（两因子各 1/k）<=> alpha_* = 1/arity
(iv)  非对称 canonical refinement：alpha_* < 1/2 严格，a/b->1 时 ->1/2
      => 1/2 是【上确界】，由 AM-GM 钉住
(v)   ⚠️ 但取极值的 locus 恰是 a=b —— 那里【加法不对称信息被销毁】
      => 1/2 是【伴随对称化一起到达】的，不是动力学产出的 => C_NI 风险
(vi)  反对称性为搬运而得，非机制
```
$$\boxed{\text{ABD-0 给出的是 }\tfrac12\tfrac{}{}\text{ 的【变分/极值刻画】，不是【动力学生成】}}$$

## 9. ⭐⭐ ABD-0 打开的新靶点（本轮真正的产出）
AM-GM 给出**上确界**；要把它变成**生成**，机制必须**取到等号**——即
$$\boxed{\text{1/2}\ \text{必须作为【算术 sharp 不等式的等号情形】出现，而不是作为上确界被引述}}$$
**⟹ 问题转化为【等号刚性】（equality rigidity）**：
$$\text{动力学能否【强迫】AM-GM 取等（即强迫 }a=b\text{）？}$$
**⟹ 且这正是 D3 模板的形状**（competition + sharp inequality + critical equality ⟹ rigidity）✓
$$\boxed{\text{新的、精确的靶点：ABD 框架内的【等号刚性】—— 强迫饱和 AM-GM。此前从未以这一形式提出过}}$$

## 10. 诚实边界
```
· §0 规格（不许 X_{k+1}=2X_k / 不许 1/2 入权重 / 禁 ζ / 禁显式公式 / 禁统计 / E_X 稳定流形参数化）—— 唐先生本轮
· §1 机器构造、§2-§8 全部实算与裁决、§9 新靶点 —— 小灵本轮（代码 scripts/abd0.py，输出 /tmp/abd0_out.txt）
· 严格性：[精确] 级 = PART 1（AM-GM 穷举 c<=1500，750 处等号全为 a=b）、PART 4（闭式）、PART 7（反对称恒等式）；
  PART 2/3/5/6 为【精确数值】（bisection tol 1e-14），渐近式 α_*~(1/2)log2c 为【数值观测 + 闭式 C(α) 支撑】，
  其系数 1/2 的"=1/arity"解释为【结构性观察】
· ⚠️ §3 勘误：首轮结论文字误写 α_*->0，实为发散；已修正重跑（记录在案，非静默重写）
· ⚠️ §8(v) 的 C_NI 风险判定为【结构性论证】；§9 的"等号刚性"靶点为【结构性提议】，未构造
· 本轮未使用 ζ / Mellin / 零点 / 函数方程；未使用 Λ；未做统计拟合
```

## 11. 提交链
```
bcb6b52 D2 收口 → 本篇（ABD-0 构造与实算）
```
