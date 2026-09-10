# B4：representation–ramification profile（**构造 + 核验；未输入 $1/2$、未输入递推**）

**依据**：唐先生 B4 指令（把 $C(u)$ 与 A′ 的双尺度放在同一层级参数上找自然交换/守恒；不输入 $1/2$、不输入递推、不人为定义权重）｜**L2 未动（保持冻结）**｜`scripts/B4_profile.py`

---

## §1 对象：上层编号 filtration 与 profile（**已核验**）
$$\varphi(i)=\frac1{|G_0|}\sum_{j\le i}|G_j|:\quad \varphi=(0,1,\tfrac32,2,\tfrac94,\tfrac52,\tfrac{11}4,3,\tfrac{25}8)$$
| 区间（含**边界区间**） | $G^u$ | $\lvert G_i\rvert$ | 长度 |
|---|---|---|---|
| $(-1,0]$ | $G_0$ | 8 | 1 |
| $(0,1]$ | $G_1$ | 8 | 1 |
| $(1,\tfrac32]$, $(\tfrac32,2]$ | $G_2,G_3=\langle\sigma\rangle$ | 4 | $1/2$ each |
| $(2,3]$（四段） | $G_4..G_7=\langle\sigma^2\rangle$ | 2 | $1/4$ each |
| $(3,\tfrac{25}8]$ | $G_8=1$ | 1 | $1/8$ |
$$C_\chi(u)=\operatorname{codim}V_\chi^{G^u},\qquad A_\chi(u)=\int C_\chi$$
**逐角色核验（profile 积分 = Artin conductor）**：
| 角色 | profile 积分 | $a(\chi)$ | 一致 |
|---|---|---|---|
| trivial | 0 | 0 | ✓ |
| linear $(0,1)$ | 2 | 2 | ✓ |
| linear $(1,0)$ | 3 | 3 | ✓ |
| linear $(1,1)$ | 3 | 3 | ✓ |
| **2-dim $\rho$** | **8** | 8 | ✓ |
| **聚合 $C_{\rm tot}=\sum_\chi\chi(1)C_\chi$** | **24** | $d=24$ | ✓ |

## §2 ⚠️ 对你定义的**精确校正**（边界项）
```
按你的写法 A(u) = ∫_0^u C(t)dt  ⟹ A(∞) = 6  ≠  a(ρ) = 8
正确的积分形式（在五个角色上逐一核验通过）：
        a(χ) = C_χ(G_0) + ∫_0^∞ C_χ(t)dt  =  ∫_{-1}^∞ C_χ(t)dt
即：需要【边界区间 (-1,0]】，其上取 G^u = G_0 的值
（原因：Herbrand 差 φ(i)−φ(i−1) = |G_i|/|G_0| 使 Σ_i (|G_i|/|G_0|)c_i = ∫，而对 i=0 要先约定 φ(−1) = −1）
```

## §3 ⭐ **本轮的结构性新结果**（已核验 + 有推导）
$$\boxed{C_{\rm tot}(H)=\sum_\chi\chi(1)\operatorname{codim}V_\chi^{H}=|G|-\frac{|G|}{|H|}=|G|\Bigl(1-\frac1{|H|}\Bigr)}$$
**数值核验**：$H=G$ ⟹ $8-1=7$ ✓；$H=\langle\sigma\rangle$ ⟹ $8-2=6$ ✓；$H=\langle\sigma^2\rangle$ ⟹ $8-4=4$ ✓；$H=1$ ⟹ $8-8=0$ ✓ —— **与实算 profile 高度 7,6,4,0 完全一致**
**推导**（引用正交关系）：$\sum_\chi\chi(1)^2=|G|$；$\dim V_\chi^H=\langle\chi|_H,1_H\rangle$；列正交 $\sum_\chi\chi(1)\chi(h)=|G|\delta_{h,1}$
⟹ $\sum_\chi\chi(1)\dim V_\chi^H=\frac1{|H|}\sum_{h\in H}\sum_\chi\chi(1)\chi(h)=\frac{|G|}{|H|}$ ⟹ 公式成立 ✓
**⟹ 层级守恒是【被推导出来】的，不是被假设的**：
$$\underbrace{\frac{|G_i|}{|G|}}_{\text{区间长度}}\times\underbrace{|G|\Bigl(1-\frac1{|G_i|}\Bigr)}_{\text{profile 高度}}=|G_i|-1\ \Longrightarrow\ \sum_i(\lvert G_i\rvert-1)=d=24\ ✓$$
即：**conductor–discriminant 的局部形式，在此被 profile 结构直接推出** ✓

## §4 $\rho$ 的 profile 是**单个矩形**
```
高度 = dim ρ = 2（因 ρ(σ²) = −I_2 ⟹ 每层 codim 都 = 2，B3 已证）
宽度 = 1 + (upper 断点数 3) = 4
面积 = 2 × 4 = 8 = a(ρ) ✓
【仅此例的观察，不声称一般性】
```

## §5 与 A′ 双尺度的对比：**没有**自然交换/守恒（诚实结论）
```
每层的二元组 (ℓ_k, c_k) = (|G_i|/|G|, |G|(1 − 1/|G_i|))，乘积 = 该层贡献 ✓
但：
 (i) 加法守恒：ℓ + c 不是常数 ✗（A′ 有 S_+ + S_- = log|G|）
 (ii) 乘法守恒：ℓ·c = |G_i| − 1 随层【变化】✗（7, 3, 1）
 (iii) 对数守恒：log ℓ + log c = log(|G_i|−1) 随层变化 ✗
 (iv) 交换对称：A′ 型对偶 x ↦ |G|/x 把 (x/|G|, |G|−|G|/x) 映为 (1/x, |G|−x)，【不是】对称 ✗
⟹ (ℓ, c) 这一对【不满足】A′ 型守恒/交换律 ⟹ 没有非平凡的层间映射 F
⟹ 按唐先生指令：**不重开 Layer 3**；B4 记为 positive structure，继续寻找新的正向桥
```
**如实报告（不作输入）**：profile 高度只依赖 $|G^u|$（§3），故层间"变化"是**群阶的函数**，不是递推律 ✓

## §6 边界
```
· 计算级：§1 全部 profile 与积分（五角色逐一核验）；§3 公式的四个数值 ✓；§4 矩形面积
· 引用（非我证明）：Herbrand 函数与 Σ↔∫ 的换算；列正交关系 Σ_χ χ(1)χ(h) = |G|δ_{h,1}；Σχ(1)² = |G|
· 结构性论证：§2 的边界项必要性；§3 的推导；§5 的四条否定（无守恒/无交换）
· 【未做】：未输入 1/2；未输入任何递推；未人为定义权重；L2 未改；未审计；未声称与 ζ 连接
```

## §7 提交链
```
4ca1240 B3 → 本篇（B4：profile + 结构性公式 + "无 F" 结论）
```
