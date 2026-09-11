# ⭐⭐⭐⭐ **两件都做**：① TP/PF 秩亏版重开（成功）② Farmer 复核（判决成立）

**依据**：唐先生 2026-09-11 20:55（"两件都需要做"）｜**脚本**：`scripts/PF1_rank_deficient_prime_toeplitz.py` ✓
**标注**：【★★★新发现】｜【ERR】｜【判决】

---

## §1 ⭐⭐⭐⭐ **① 素数侧秩亏 Toeplitz：机制【无损地】复现素数频率**
```
构造：**c_k = Σ_{j: p_j ≤ P} w_j·cos(k·log p_j)**（w_j = log p_j / √p_j ✓，原子取在 **θ_j = log p_j** ✓）
   T_{kl} = c_{|k−l|}，**size = 2r+1**（r = 素数个数 ✓；**size > 2r ⟹ 强制秩亏** ✓）

   P   r   size  rank  2r   min eig     回文      max||root|−1|   根角 vs {±log p}
   7   4     9     8    8  4.86e-17  8.06e-15   6.22e-15        **4.44e-15  MATCH**
  11   5    11    10   10 -3.07e-16  8.30e-16   1.67e-15        **2.00e-15  MATCH**
  13   6    13    12   12 -8.86e-17  2.55e-15   4.66e-15        **4.44e-15  MATCH**
  17   7    15    14   14 -8.98e-16  6.59e-14   1.54e-13        **5.51e-14  MATCH**
  19   8    17    16   16  1.43e-15  5.35e-11   1.25e-10        **3.38e-12  MATCH**
  23   9   (16 roots vs 18 freqs——**频率 mod 2π 碰撞**，仍有 6.03e-09 MATCH ✓)
```
$$\boxed{\text{素数原子 Toeplitz（size }2r+1\text{、rank }2r\text{）}\ \Longrightarrow\ \text{核多项式根【恰在】}e^{\pm i\log p_j}\text{ 处}}$$
```
⟹ ⭐⭐⭐ **发现**：**该机制不只是"产生实零点"，而是【无损地】把输入频率（素数频率 log p_j）复现为零点** ✓✓✓
   —— 即：**核多项式 = ∏(z − e^{±i log p_j})** 型 ✓（8/10/12/14/16 个根 ⟺ 2r 个频率 ✓✓）
   —— 对照：**控制组（非素数频率）同样精确复现** ✓（mismatch ~1e-13 ✓）⟹ **机制对输入测度【无损】** ✓✓
【⚠️ 诚实边界】**我们的测试是【输入】素数频率再【取回】** ⟹ **不是"从素数【导出】零点"** ✗✓
   但**结构事实成立且实质**：**该机制在输入频率上【无损】（injective）** ✓✓
```

## §2 ⭐⭐⭐ **关键对照（本轮新获的结构二分）**
```
【① 正性 + 秩亏】：**信息【保持】**（零点 = 输入频率 ✓✓，机器精度 ✓）
【② 微分（Farmer）】：**信息【丢失】**（通用余弦吸引子 ✗ —— 见 §3 ✓）
⟹ ⭐⭐ **两者形成清晰对偶**：**"正性+秩亏"保信息，"微分"毁信息** ✓✓
   —— 而**我们全程的核心主题正是【信息】**（β 墙 = 信息丢失；检测≠排除 = 信息不足 ✓✓）
   ⟹ **本轮把该主题落到了两个【具体机制】的定量对比上** ✓✓✓
```

## §3 ⭐⭐⭐ **② Farmer 复核：其论证成立（判决：Jensen 路线仍关闭）**
```
【原文关键段（arXiv:2008.07206v2 ✓）】
"…**Kim** 定理：f 阶 < 2、在实轴上实、零点在条带 |ℑz| < A 内 ⟹ 对任意固定 R>0，
   当 n 充分大时 **f^(n) 在 |z|<R 内只有实零点**" ✓
"**The analogous result holds for functions in the extended Selberg class**: 该类有函数方程但
   **不一定有 Euler 乘积**，**故包含大量【不满足 RH 类比】的例子** ✓✓
 **The same result holds for random functions**, which **by construction satisfy the RH analogue
   but have Poisson statistics** for their zeros ✓✓"
"**Berry** 猜想：**cos(ω_n t + δ_n) 是微分映射的【通用吸引子】**" ✓
"⭐ **'differentiation causes a LOSS OF INFORMATION about the zeros of the functions considered
   here, and so in terms of the Riemann Hypothesis there is little revealed by the derivatives.'**" ✓✓✓
【复核判决】✔ **论证成立**：
   (a) 现象（大 n 时 J^{d,n} 双曲 ✓）对**不满足 RH 类比的对象**同样成立 ⟹ **不能蕴含 RH** ✗✓
   (b) 机制 = **微分丢失零点信息** ✓（通用吸引子 ✓）
   (c) **每 d 的"有限多个例外"仍在** ✗（与 T² 形状并不矛盾 ✓）
⟹ **N6 解决**：**Jensen 路线【仍关闭】** ✓✓；**Li 仍为【唯一强型放大器】** ✓✓
⟹ ⭐⭐ **额外收获**：**Farmer 的"微分丢失信息"是【同行评审文献】对我们"β 墙/信息丢失"主题的独立表述** ✓✓✓
```

## §4 ⚠️ **ERR（本轮重复犯的构造错误）**
```
【ERR-重复】**PF1 首版又用 size = r+1 ≤ 2r** ⟹ **满秩** ✗（rank = r+1 ✗，非 2r ✗）
   ⟹ 与 CVS1b 的 E1 **同类错误**（"size 不够大 ⟹ 不强制秩亏" ✓）
【修正】size = 2r+1（n = 2r ✓）⟹ rank = 2r ✓ 亏 1 ✓（修正后全部 MATCH ✓✓）
【教训·已记】**构造秩亏 Toeplitz 的充要条件：size > 2r（原子数 r）** ✓ —— 此前两次失败均因 size ≤ 2r
```

## §5 **本轮净新发现**
```
【P1】**正性+秩亏 ⟹ 信息【保持】**（零点 = 输入素数频率，1e-15~1e-12 ✓✓）—— 新机制属性 ✓
【P2】**与 Farmer 的"微分毁信息"形成对偶** ⟹ 我们的核心主题（信息）有了**两个定量实例** ✓✓
【P3】**Farmer 判决成立**：Jensen 关闭，**Li 为唯一强型放大器** ✓✓（N6 解决 ✓）
【P4】**构造规则固化**：秩亏 Toeplitz 需 **size > 2r** ✓（两次 ERR 的教训 ✓）
```

## §6 边界
```
【核验】§1 的表与 MATCH（脚本可复现 ✓，含控制组 ✓）；§4 的 ERR 与修正 ✓
【外部·原文】§3 的引文（Farmer arXiv:2008.07206v2 ✓，**已读关键段** ✓）
【推导】§2 的信息对偶；§5 的 P1–P4
【⚠️】P1 的"无损"是在**输入频率已知**的测试中成立（**非从素数导出** ✗）；未输入 1/2；未构造模型；未改 L2
【未做】未读 Farmer 全文其余部分 ✗；未跑 Far
mer 的 Section 4 "illustrative example"（信息丢失的算例 ✓）✗
```
## §7 提交链
```
REAUDIT（8e44e23）→ 本篇（PF1 秩亏版成功 + Farmer 复核 + 信息对偶）
```
