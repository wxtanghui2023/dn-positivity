# **门⑤收口**：Burnol 原文解开常数之谜 + 机制 = **零点索引的障碍向量** + 缺口 = **均匀性**（第四次印证）

**依据**：唐先生 2026-09-11 20:18（"先读全文，继续"）
**原文**：**Burnol, arXiv:math/0103058v2**（Adv. Math. 170(1) 56–70 ✓）全文 ✓
**标注**：【外部·全文】｜【推导】

---

## §1 ⭐⭐⭐ **精确下界（原文 Theorem 1.2 = BDBLS 的结果）**
```
记 B_λ 为膨胀界 λ 的逼近空间，**D(λ) := inf_{f∈B_λ}‖χ − f‖**（Hilbert 距离 ✓）
【定理】**lim inf_{λ→0} D(λ)·√( log(1/λ) ) ≥ √( Σ_ρ 1/|ρ|² )** ✓✓✓
```
$$\boxed{D(\lambda)^2\ \gtrsim\ \frac{\sum_\rho 1/|\rho|^2}{\log(1/\lambda)}\qquad(\lambda = 1/N\ \Rightarrow\ D^2\gtrsim \frac{C}{\log N})}$$
```
⭐⭐⭐ **常数之谜解开**：**C = Σ_ρ 1/|ρ|²**，而（在线时）**Σ_ρ 1/|ρ|² = 2 + γ_E − log(4π) ≈ 0.04619** ✓✓✓
   ⟹ 我前两轮看到的两处"不同常数"**是同一个数** ✓✓（= 零点上的谱和 ✓ = Burnol 的下界常数 ✓）
   ⟹ **我上轮的更正被原文证实**：正确形式是 **D² ≍ C/log N**（递减 ✓），不是 C log N ✓✓
【附注】Burnol 说自己是"**slightly improve** BDBLS 的下界" ✓（并指出改进在大 |ℑλ| ✓）
```

## §2 ⭐⭐⭐ **机制（原文自述）= 零点索引的【障碍向量】+ 投影**
```
原文："**To bound it from below we will exhibit remarkable Hilbert space vectors X_{λρ,k}
   indexed by the zeros of the Riemann zeta function and perpendicular to C_λ. We then compute the
   exact asymptotics of the orthogonal projection of χ₁ to the vector spaces spanned by the X_{λρ,k},
   for a finite set of roots, exactly as in the Grenander–Rosenblatt method**" ✓✓✓
【向量形式】**ψ_{w,k}(t) = (log(1/t))^k · (…) ** ✓ —— **第 k 个向量探到零点的第 k 阶行为** ✓
⟹ **与 Li 系数同构**：λ_n 含 (1−1/ρ)^n = Σ_k C(n,k)(−1)^k ρ^{−k} ✓（**对每个零点的【阶 k 敏感度】** ✓）
⟹ ⭐ **√(log) 的来源**：有效阶 k 的数目 ~ log(1/λ) ✓（即"**阶数预算**"✓）
⟹ ⭐⭐ **这就是"有限压缩 + 投影/惯性"范式**（与 2/3 论文、我们的 P36 Gram 刚性同族 ✓✓）
```

## §3 ⭐⭐ **判据本身的"无信息"声明**（原文自述，很重要）
```
"**It is a disappointing fact that this theorem can be proven without leading to any new
  information whatsoever on the zeros lying on the critical line**（基本只是 Hardy 空间分解）" ✓✓
   ⟹ **NB 判据【定性】地不含零点信息** ✗；**只有【定量】版本（Thm 1.2）才带信息** ✓✓
   —— 这正是本项目"**转换才是全部内容**"的又一独立印证 ✓✓
【另注】Burnol 提到这些向量"**could prove useful in the context of the so-called Hilbert–Pólya idea**" ✓
```

## §4 ⭐⭐⭐ **缺口 = 均匀性**（第四次独立出现）
```
Burnol 的关键步（math/0202166 Thm 3.1）：**|ζ(s)/ζ(s+A)| = O(|s|^{inf(ε,A/2)})，对 A 【一致】** ✓
   原文自述："**what is essential is the uniformity as A → 0**" ✓✓
⟹ 本项目"均匀性缺口"的**第四次独立出现**：
   ① 经典无零点区域：margin 非均匀 ✓｜② YM：格点→连续缺一致界 ✓
   ③ Burnol：A → 0 的一致 ✓｜④ 我们的 Li 转换：缺"在线零点相位分散界"（同为一致性问题 ✓）
⟹ 与登记的"缺口第七条"完全吻合 ✓✓
```

## §5 **门清单终态**（读毕后的结论）
| 门 | 转换类型 | 状态 |
|---|---|---|
| ① Li/模长 | **数值输入 ⟹ 符号范围（T²，放大器）** | **唯一"放大器"** ✓；缺在线相位分散界 ✗ |
| ② 显式公式 | 衰减型局部化 ⟹ 经典截断 | 无新意 ✗ |
| ③ 稳定性机器 | 符号即对象本身 ⟹ 自我指涉 | 无增益 ✗ |
| ④ GUE → 双曲性 | 转换存在（文献） | **未细读** ⚠️ |
| ⑤ NB | **零点 ⟹ 距离下界（方向相反）** | **已彻底读通** ✓（本系列） |
| ⑥⑦ 墙类 | 无 | ✗ |

## §6 **我们能从门⑤学到什么（可复用）**
```
① **把零点当【障碍向量】**（X_{λρ,k} ⊥ 逼近空间）—— 这是一条**可移植的技术** ✓✓
② **"阶数预算"产生 log 因子**（k ≤ log(1/λ) ⟹ √log ✓）—— 解释了 log 型形状的来源 ✓
③ **定性判据无信息、定量版本才有**（原文自述 ✓）—— 支持我们的"转换即内容"论 ✓
④ **均匀性是所有路线的共同缺口** ✓✓
```

## §7 边界
```
【外部·全文】§1 Thm 1.2 与常数、§2 机制原文引用与 ψ_{w,k}、§3 原文自述、§4 的一致性 ✓
   （Burnol 论文的中间章节未逐页读 ⚠️；DFMR I 的 §3–§6 亦未逐页读 ⚠️）
【推导】§1 的 C 与谱和的等同（依据在线关系 Σ1/|ρ|² = 2+γ_E−log4π ✓）；§5/§6 的归纳
【未核】Σ1/|ρ|² = 2+γ_E−log4π 的**无条件**成立范围 ⚠️（离线时 ρ(1−ρ) ≠ |ρ|² ✓）
【未做】未输入 1/2；未构造模型；未改 L2；未声称任何证明
```
## §8 提交链
```
DOOR5e（bdc83cd 均匀性 + 精确圆盘）→ 本篇（Burnol 原文：常数谜解 + 机制 + 门清单终态）
```
