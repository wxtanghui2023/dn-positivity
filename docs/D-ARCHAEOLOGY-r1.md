# D-ARCHAEOLOGY r1：跨极限非退化定理考古（D1/D2/D3 + 五问审计）

**日期**：2026-09-10 17:00+ ｜ 依据：唐先生「甲，但不是再找耗散候选」→ D1–D3 ｜ 预算：纸面 + 文献核验（web）

---

# 0. 方向登记与修正（唐先生）

$$\boxed{\text{现在要考古【非有限来源的耗散定理】，而不是构造算术耗散}}$$
**⚠️ 关键修正**：不要把 dissipation 理解成动力系统意义的耗散
$$\boxed{\text{真正需要的是：uniform non-degeneracy across }X}$$
即存在 $D_X$ 阻止 $D_X\to0$ 把有限尺度刚性冲掉（≈ coercivity at infinity / uniform invertibility / critical inequality）
**三站**：D1 uniform coercivity at infinity｜D2 limit-operator uniform invertibility｜D3 **sharp critical inequalities**（唐先生认为最有希望）
**五问（每站必答，Q3 是生死线）**：
```
D-Q1 它到底防止哪一种极限退化？
D-Q2 它需要什么【非有限】假设？
D-Q3 它的【临界量是否由 theorem 自己产生】？（生死线）
D-Q4 该假设能否有 arithmetic primitive analogue？
D-Q5 若把 arithmetic primitive 替进去，是否仍逃出 N1–N7？
```
**三关（不得跳关）**：① 能否产生一个**不是预装进去**的 critical exponent $\alpha_*$？② $\alpha_*=1/2$？③ arithmetic 能否实现？
**裁决**：$\boxed{\textbf{不收线，走甲}}$；若 D1–D3 最终只提供**有限来源**的正性，则收线 = 一个相当强的**成分级 NO-GO**

---

# 站 D1：Uniform coercivity at infinity

## 定义与形态
$$\exists\ \text{紧集 }K,\ c>0:\quad Q_X[f]\ge c\,N_X[f]\quad\text{对所有支集在 }K\text{ 之外的 }f$$
关键：**不是** $Q_X\ge0$，而是 **positive with an X-uniform margin**

## 五问
| 问 | 答 |
|---|---|
| D-Q1 | 防止"去紧集后下界消失"= **moving-edge 的最直接补丁** ✓ |
| D-Q2 | 假设本身是**渐近/在无穷处**的条件（非有限）✓ |
| **D-Q3** | **✗ 不过关**：coercivity 常数 $c$ 是**假设（输入）**，不是定理产出 |
| D-Q4 | 需要算术的"势在无穷处一致有下界"——未识别 |
| D-Q5 | 因 Q3 不过关而**无独立价值** |

$$\boxed{\text{D1 不独立：其"一致性"必须来自 D2 的机制 ⟹ }D1\subseteq D2}$$

---

# 站 D2：Limit-operator uniform invertibility（上轮站 1 的深化）

## 已核实（文献级）
```
经典：band-dominated A Fredholm ⟺ 所有 limit operators 可逆【且逆一致有界】
⭐ 演进：一致有界【自动】——JFA 2014《An affirmative answer to a core issue on limit operators》
        ⟹ 后期表述（arXiv:1801.08442）不再附带一致性条款
```

## 五问
| 问 | 答 |
|---|---|
| D-Q1 | 防止**逆的爆炸**（= 统一下界丢失）✓ 与 D1 同目标，但**推导**而非假设 |
| D-Q2 | **非有限**假设：极限对象族的**紧性** + 参数化**连续性** + **局域性**（band-domination/有限传播，使局部模型穷尽信息）✓✓ |
| **D-Q3** | **✅ 过关（目前最强的一条）**：统一下界（逆的一致有界）**由定理产出**，不是外加 |
| D-Q4 | 需要 ① 一个随尺度走向无穷的"极限对象族" ② 该族**紧** ③ 算术运算的**有限传播/局域性** ④ 范数结构。<br>⚠️ 算术**自然的紧族是 profinite/adelic（0 维）**，与我们的非紧尺度族**结构不同** |
| D-Q5 | 未替换测试（Q4 未解决） |

$$\boxed{\text{D2 是本轮唯一【Q3 过关】且机制明确异的模板}}$$

---

# 站 D3：Sharp critical inequalities（⭐ 唐先生重点）

## 已核实的三个实例

### (a) Hardy 不确定性原理（Escauriaza–Kenig–Ponce–Vega；Ponce 讲义；Tao 博文）
$$\text{若 }f(x)=O(e^{-x^2/\beta^2}),\ \hat f(\xi)=O(e^{-4\xi^2/\alpha^2}):\quad \frac1{\alpha\beta}>\frac14\Rightarrow f\equiv0;\quad \frac1{\alpha\beta}=\frac14\Rightarrow f=c\,e^{-x^2/\beta^2}$$
**⚡ 结构**：**两个对偶衰减参数之积**有**精确阈值 $1/4$**；达到阈值时**解被强制成 Gaussian**（唯一极值 ⟹ rigidity）
**动力学版**（同一文献）：$T/(\alpha\beta)=\frac14$ 临界 ⟹ **时间也被卷入平衡**（空间衰减 × 频率衰减 × 时间）
**证明结构**：用 Appell（共形）变换**归约到 $\alpha=\beta$** ⟹ 内部含**尺度不变性**

### (b) Hardy 不等式（Hoffmann-Ostenhof–Laptev；Cazacu；Tao 评论）
$$\int|\nabla u|^2\ge \frac{(N-2)^2}{4}\int\frac{|u|^2}{|x|^2}\quad(\text{sharp};\ N=1\ \text{时}=\frac14)$$
**⚡ 关键**（Tao 评论核实）：**该不等式永不取等**——存在近极值序列逼近而**不收敛到取等对象**（形式极值 $x^{-1/p}$ 两端对数发散）
**⟹ 第二种 rigidity 模式：sharp constant + critical + 近极值存在但【不达到】**

### (c) Selberg 1/4 猜想（Wikipedia；MathOverflow；Kim–Sarnak JAMS 16 (2003)）
$$\lambda_1\ge\frac14=0.25;\quad \text{Selberg 证 }\ge\frac3{16};\quad \text{现最佳 }\frac{975}{4096}\approx0.2380=\frac14-\Big(\frac7{64}\Big)^2$$
**⚡ 等价**：Selberg 猜想 ⟺ **GL₂/Q 在无穷处的 Ramanujan 猜想**（表示在 ∞ 处为主序列而非补序列）⟸ Langlands 函子性

## ⚡ 这三个实例共同的常数结构
$$\frac{(N-2)^2}{4}=\Big(\frac{N-2}{2}\Big)^2;\qquad \frac14=\Big(\frac12\Big)^2;\qquad \frac1{\alpha\beta}=\frac14$$
$$\boxed{\text{临界常数一律是【半个整数间隔】的平方}:\ (N-2)/2,\ \tfrac12\cdot(\text{weight}),\ \ldots}$$
**⟹ 与函数域 $|\alpha|=q^{1/2}$（半个 weight）同一结构来源** ✓

## 五问
| 问 | 答 |
|---|---|
| D-Q1 | 防止"两个对偶约束可同时接近饱和"的**松弛**（slackness）；把竞争转成**阈值+等号刚性** |
| D-Q2 | **非有限**：无穷处的衰减/增长条件 + 变换或竞争本身的结构 |
| **D-Q3** | **✅ 过关**：sharp constant / 阈值**由定理自身产出**（(N−2)²/4 来自尺度不变的竞争；1/4 来自对偶参数耦合；Selberg 的 1/4 来自谱参数化 λ=s(1−s) 的 s=1/2） |
| D-Q4 | **✅ 有真实算术实例**：Selberg 1/4 ⟺ Ramanujan@∞ ⟺ Langlands 函子性 |
| **D-Q5** | **✗ 不逃出**——两条独立理由（见下） |

### D-Q5 的两条理由（诚实）
```
① 这些阈值以 **1/4 = (1/2)²** 的形式到达，1/4 与 1/2 之间的字典恰好是
   **二次自对偶参数化 λ = s(1−s)**（s=1/2 ⟺ λ=1/4）
   ⟹ 即我们已经识别的"自对偶配对"结构（门⑮ 中间 weight / 门⑰ 1/4=(1/2)²）
   ⟹ **D3 的 1/2 来源与 FE 中心同型**，不是新入口
② 其算术实现（Selberg/Ramanujan）属**自伴离散谱**；而 ζ 零点在**散射/共振侧**（门⑲/⑳）；
   且通往 ζ 的引擎（Kuznetsov + Sym²）在 GL(1) 上**平凡化**（门⑰）
   ⟹ **门⑯–⑳ 已审计封闭**
```
$$\boxed{\text{D3 过关 Q3，但其算术实现 = 已封闭路线的【更高分辨率重推】，非新入口}}$$

---

# 4. ⭐⭐ 本轮的结构性合成（最有价值的产出）

$$\boxed{\textbf{P2}\ \text{的规格}\ =\ \underbrace{\text{D2 的 uniformity（推导而非假设）}}_{c\ \text{来自紧性}}\ +\ \underbrace{\text{D3 的对偶耦合阈值（指数由竞争产出）}}_{\beta\ \text{来自 sharp threshold}}}$$
**唐先生 P2 的"守恒平衡" $\beta+\gamma=1$ 因此有了【已证实的类比】**：
$$\text{Hardy 型阈值}\ \frac1{\alpha\beta}=\frac14\ \Longleftrightarrow\ \text{两个指数被【对偶】耦合，阈值由竞争结构固定}$$
**⟹ P2 不再是"提议"，而是"两个已被证明的部件的组合规格"** ✓
**且注意**：D3 家族给出 $1/2$ 的方式是 **$\frac12=\sqrt{\frac14}$**（经 $\lambda=s(1-s)$ 字典），
这正是**"自对偶减半"**结构 —— 与函数域 proof 中"weight 的 /2"完全同型（门⑮三锁的前两锁）

---

# 5. 裁决与下一目标

## 是否"成分级 NO-GO"？
$$\boxed{\textbf{不是}}$$ D1–D3 **并未**都只提供有限来源的正性——**至少两种非有限非退化机制确实存在**：
```
① 极限族紧性 ⟹ 一致性（D2，Q3 ✅，机制明确）
② 对偶竞争 + sharp threshold ⟹ 指数（D3，Q3 ✅，但算术实现已封闭）
```
⟹ **这是正面的考古收获**（我此前的"缺 dissipation"判断过窄，已修正）

## 新目标（取代"找无条件 X-尺度耗散"）
$$\boxed{\text{找一个【紧的算术极限对象族】+ 连续参数化 + 有限传播/局域性}}$$
（D2 的算术实现；D3 的算术实现已知但已封闭 ⟹ 唯一未走的路是 D2 的算术化）

## 三关现状
```
① 非预装 critical exponent：D2 ✓（一致性由定理产出）｜D3 ✓（sharp constant 由竞争产出）
② 是否 1/2：D3 给出 1/4=(1/2)²，须经 λ=s(1−s) 字典 ⟹ 即"自对偶减半"（已知结构）
③ arithmetic 实现：D3 已知但封闭（门⑯–⑳）｜D2 【未识别】← 唯一活口
```

# 6. 诚实边界
```
· §0 的 D-ARCHAEOLOGY 定义、五问、三关、"dissipation→uniform non-degeneracy" 修正、优先序 D1–D3、裁决 —— 唐先生本轮
· D1/D2/D3 的五问审计、D1⊆D2 结论、D3 三实例的常数结构提炼、§4 合成、§5 新目标与三关现状 —— 小灵本轮
· 文献核验（本轮实际检索）：
  D3(a) Hardy 不确定性：Escauriaza–Kenig–Ponce–Vega（Benasque 讲义 PDF）原文含
         "1/(αβ)>1/4 ⟹ f≡0；=1/4 ⟹ f=c e^{−x²/β²}"；Ponce 讲义（UCSB）同；Tao 博文（Gaussian 表述）
  D3(b) Hardy 不等式 sharp 常数 (N−2)²/4：Hoffmann-Ostenhof–Laptev（IC）(3.6)；Cazacu（BCAM）λ*= (N−2)²/4 为临界；
         Tao 在 MathOverflow 明确"永不取等、近极值存在但不收敛"
  D3(c) Selberg：Wikipedia（≥1/4；Selberg ≥3/16；最佳 975/4096 Kim–Sarnak 2003）+ MathOverflow 给出
         975/4096 = 1/4 − (7/64)² + GL₂/Q@∞ 的 Ramanujan 等价
· ⚠️ "常数一律是半个整数间隔的平方"为【结构性归纳】，非定理；对 D3(b) 的 (N−2)/2 与 D3(a) 的 1/4 适用，
  但对 D3(a) 的"4"部分依赖 Fourier 约定（数值 1/4 有约定成分，结构（乘积阈值）才是本质）
· §4 的"P2 = D2 uniformity + D3 threshold"为【结构性合成】，非定理；Hardy 阈值与 β+γ=1 的类比为结构性
· §5 的"D3 算术实现已封闭"引门⑯–⑳ 的既有登记（本轮未重新审计）
· 未写代码、未做数值；本轮仅做文献检索；未使用 Λ；未引入 ζ 零点或谱算子
```

## 提交链
```
241f3f7 LRA r1（三站） → 本篇（D-ARCHAEOLOGY r1：D1/D2/D3 + 五问）
```
