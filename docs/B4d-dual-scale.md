# B4d：第二对象 = 不动域塔 ⟹ **A′ 型双尺度结构成立，balance 受阻**

**依据**：唐先生选 **(d)**（$\rho\otimes\rho$ / 自对偶伴随方向）｜**约束**：不输入 $1/2$、不输入递推、不人为定义权重、不做 GPS 审计｜**L2 未动**｜`scripts/B4d_dual_scale.py`

---

## §1 第二对象（并**升级**到对偶尺度层面）
$$\boxed{\text{第二对象} = \text{不动域塔 } F_i=L^{G_i}\ \text{（Galois 对应）}}$$
**理由**：$\rho\otimes\rho$ 自身是**阿贝尔侧对象**（$\rho(\sigma^2)=-I_2$ 但 $(\rho\otimes\rho)(\sigma^2)=(-I)\otimes(-I)=+I_4$ ⟹ 它经 $G/\langle\sigma^2\rangle$ 分解 ⟹ 恰为 $\rho$ 的阿贝尔影子）；因此真正的"对偶第二对象"应由 **Galois 对应** 给出 ⟹ 不动域 $F_i$ ✓（**定理级对偶，非人为**）
**对偶塔（与本项目已核验的域完全一致）**：
$$\mathbb Q_2\ (d{=}1)\ \longrightarrow\ \mathbb Q_2(i)\ (d{=}2)\ \longrightarrow\ \mathbb Q_2(\zeta_8)\ (d{=}4)\ \longrightarrow\ L\ (d{=}8)$$
（$L^{\langle\sigma^2\rangle}=\mathbb Q_2(\zeta_8)$：中心含于三个 index-2 子群 ⟹ 其不动域是三个二次域的合成 ⟹ $\mathbb Q_2(\zeta_8)$ ✓，其 $d=8$ 已在 L2 中核验 ✓）

## §2 ⭐ 两个尺度与**守恒积**（逐层核验）
| $i$ | $\lvert G_i\rvert$ | $\ell_i=\lvert G_i\rvert/\lvert G\rvert$ | $F_i$ | $d_i=[F_i:\mathbb Q_2]$ | $\ell_i d_i$ | $\lvert G_i\rvert d_i$ |
|---|---|---|---|---|---|---|
| 0,1 | 8 | 1 | $\mathbb Q_2$ | 1 | 1 | **8** |
| 2,3 | 4 | $1/2$ | $\mathbb Q_2(i)$ | 2 | 1 | **8** |
| 4–7 | 2 | $1/4$ | $\mathbb Q_2(\zeta_8)$ | 4 | 1 | **8** |
| 8 | 1 | $1/8$ | $L$ | 8 | 1 | **8** |
$$\boxed{\lvert G_i\rvert\times[F_i:\mathbb Q_2]=\lvert G\rvert=8\ \text{对【每一层】成立（自检 True）}}$$
$$\Longrightarrow\ \text{这正是 A′ 的守恒形状}:\ (\text{尺度}_1)\times(\text{尺度}_2)=\lvert G\rvert\ \text{（A′: }|\Lambda||\Lambda^\perp|=|G|\text{）}$$

## §3 profile 高度**由对偶尺度决定**
$$c_i=|G|-d_i=|G|-[F_i:\mathbb Q_2]\ \Longrightarrow\ \text{高度} = 7,7,6,6,4,4,4,4,0\ \text{（与 B4 实算完全一致，自检 True）}$$
$$\Longrightarrow\ \text{每层二元组}\ (\ell_i,c_i)=\Bigl(\frac1{d_i},\ |G|-d_i\Bigr)\ \text{——【对偶次数 }d_i\text{ 的一参数族】}$$
$$\boxed{\text{故"长度"与"高度"两侧【可交换】：经 Galois 对应（子群}\leftrightarrow\text{不动域），定理级，非人为}}$$

## §4 balance 障碍（**精确**）
$$\ell=c\iff\frac1d=|G|-d\iff d^2-|G|d+1=0\iff d=\frac{|G|\pm\sqrt{|G|^2-4}}2$$
```
|G| = 8  ⟹  判别式 |G|² − 4 = 60 【不是】完全平方
各层检验：d=1: ℓ=1, c=7 ✗｜d=2: ℓ=1/2, c=6 ✗｜d=4: ℓ=1/4, c=4 ✗｜d=8: ℓ=1/8, c=0 ✗
形式根 = (8 ± √60)/2 是【无理数】 ⟹ 无任何层满足 ℓ = c
```
$$\boxed{\text{balance 障碍} = \lvert G\rvert=8\ \text{不是完全平方}\quad(\text{与此前 }\sqrt{|D|}\text{ 情形同一类平方根障碍})}$$


> ⚠️ **ERRATUM（2026-09-10，见 `C1-cover-balance-verification.md`）**：本文件 §4 把方程 "ℓ = c"（即
> $d^2-|G|d+1=0$，判别式 $|G|^2-4$）称为 "the balance obstruction"，这是**表述错误**。
> 正确的 A′ 型平衡判据是 §5 所用的 $|G_i|=\sqrt{|G|}$；其障碍的精确形态是 **$|G|$ 的 2-adic 指数为奇**，
> 而该障碍**可由一次二次 lift 解除**（$3\to4$，即 $8\to16=4^2$）——见 C1。
> §4 的方程 $\ell=c$ 是一个**无关的、对一切 $|G|>2$ 都不可满足的**方程（C1 §5 有证明）。

## §5 与 A′ 的对比（诚实）
```
A′：两尺度 S_± = log|Λ|, log|Λ^⊥|，守恒 |Λ||Λ^⊥| = |G|；平衡尺度 = √|G|
本处：两尺度 (|G_i|, [F_i:Q_2])，守恒积 = |G| = 8  —— 【形状相同，已核验】✓
      但平衡层需 |G_i| = √|G| = √8 ∉ ℤ ⟹ 【无平衡层】
⟹ A′ 型双尺度结构：**成立** ✓
⟹ balance / 交换不动点：**受阻**（因 |G| 非平方）
⟹ 因此【未】产生任何以 1/2 为不动点的 F ⟹ **Layer 3 不重开**（符合约束）
```

## §6 本轮结论（记为 positive structure）
$$\boxed{\textbf{B4d-positive structure}:\ \text{Galois 侧尺度}\times\text{不动域次数}=\lvert G\rvert\ \text{（守恒）；且}(\ell,c)=(\tfrac1d,\lvert G\rvert-d)\ \text{由对偶次数一参数化}}$$
```
· 第二对象已找到且是定理级的（Galois 对应 / 不动域塔）
· A′ 型守恒积成立（逐层核验）；(length,height) 成为对偶次数的一参数族 ⟹ 两侧可交换
· 未产生 1/2 不动点：balance 被 |G| 的非平方性精确阻断
· 【conjecture-level 观察，不声称】此前解 √ 障碍的手段恰是 (c) 2-cover；本处障碍同类
  —— 是否可由 2-cover 解除，本轮【未做】
```

## §7 边界
```
· 计算级：§2 逐层守恒（两个形式）。§3 高度与 B4 profile 一致。§4 balance 检验与判别式 60
· 引用（非我证明）：Galois 对应 [L^{G_i}:Q_2] = |G|/|G_i|；ρ⊗ρ 的分解与 a 的可加性（B4b 已核验）
· 结构性论证：§1 第二对象的选择理由（ρ⊗ρ 是阿贝尔影子）；§5 的形状对比；§4 的障碍定性
· 【未做】未输入 1/2；未输入递推；未人为定义权重；未做 GPS 审计；L2 未改；未声称与 ζ 连接
```

## §8 提交链
```
3309c64 B4b → 本篇（B4d：不动域塔双尺度 + 守恒 + balance 障碍）
```
