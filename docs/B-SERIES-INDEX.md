# B 系列 + A′ 链：**单页索引**（防止文档重写本）

**建立**：2026-09-10 20:57｜**规则**：每轮只更新对应文件；README 式索引只此一份
**全局约束**（贯穿所有轮次）：**未输入 $1/2$、未输入递推、未人为定义权重、未做 GPS 审计、未声称与 ζ 连接**

---

## 状态总表
| 文件 | 内容 | 状态 |
|---|---|---|
| `L2-RAMIFICATION-STATE.md` | Layer 2 分歧 bookkeeping（index/tower/filtration/conductor 三链闭合） | **VERIFIED（冻结）** |
| `materialA-cross-scale-transport.md` | A′：双坐标 + 守恒总量 + 跨层 transport | 构造成功（transport 层） |
| `number-field-Aprime.md` | 数域版：$\sqrt{\lvert D_K\rvert}$ 由自对偶强制；算术选择律 | 构造 |
| `two-cover-explicit-construction.md` | 2-cover $K\to K'=K(\sqrt{\sqrt2})$：$\mathfrak a'=(δ^{-3})$，$\mathfrak a'^2=\mathfrak D^{-1}\mathcal O_{K'}$ | 构造成功 ⟹ **下一轮候选 (c)** |
| `B1B2-layer-pairing.md` | B1 层商/断层（$i=1,3,7$；upper breaks 1,2,3）；B2 自然配对 | **退化（rank 1）** ⟹ 排除 |
| `B3-central-layer.md` | 中心层 $\sigma^2$-特征；Schur 强制 $\rho(\sigma^2)=-I_2$；conductor 精确对应 | **positive structure** |
| `B4-profile.md` | profile $C(u)$、$C_{\rm tot}(H)=\lvert G\rvert-\lvert G\rvert/\lvert H\rvert$；24 恒等式被【推导】 | **positive structure** |
| `B4b-second-object.md` | 第二对象筛选 + $\rho\otimes\rho$ 核验（同 conductor 8、不同 profile） | positive（(a)(b) 排除；(c)(d) 活跃） |
| `C1-cover-balance-verification.md` | (c) 部分验证：平衡障碍 = |G| 的 2-adic 指数为奇；一次二次 lift 解除（3→4）；含 **B4d 勘误** | **positive（机制层面）** |
| `B4d-dual-scale.md` | 第二对象 = **不动域塔**；$\lvert G_i\rvert[F_i:\mathbb Q_2]=\lvert G\rvert$；balance 受阻（判别式 60 非平方） | **positive structure** |

## 已被排除 / 已撤回（不要再引用）
```
· B2：(a) 局部互反/单位 filtration 与 (b) Hilbert 配对 —— 在本例【退化】（rank 1，radical = span{[2]}）
· L2 §2：10 条撤回项（d=50/22/30、index=1、1/8、|disc Q(ζ₈)|=2¹⁰、非极大基结果等），逐条附原因
· Layer 3（双尺度守恒 + 递推 r↦(r−1)/2 ⟹ 1/2 不动点）= **结构猜想，未建立，继续冻结**
· B4d §4 的 "ℓ = c 平衡障碍" 表述 = **已勘误**（正确判据见 C1 §1/§5）
```

## 未验证的活跃候选（下一轮）
$$\boxed{\text{(c) Kummer 2-cover } K\to K'=K(\sqrt{\sqrt2})}$$
理由：B4d 的 balance 障碍 = $\lvert G\rvert=8$ 非平方（与 $\sqrt{\lvert D\rvert}$ 情形同一类平方根障碍），
而此前解该类障碍的手段正是 2-cover ⟹ **是否可由 2-cover 解除本例 balance 障碍，尚未验证**

## 一句话现状
$$\text{L2 = VERIFIED（冻结）};\quad \text{B3/B4/B4b/B4d = positive structure};\quad \text{Layer 3 = 冻结的结构猜想};\quad \text{下一轮 = (c)}$$
