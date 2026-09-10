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

---

# 续篇：C/D/E 系列（2026-09-10 夜，全部为**推导/核验**，非审计终结）

| 文件 | 内容 | 状态 |
|---|---|---|
| `C1-cover-balance-verification.md` | (c) 2-cover 机制验证：平衡障碍 = $\lvert G\rvert$ 的 2-adic 指数为奇；一次二次 lift 解除（$3\to4$） | **positive（机制层面）**；含 **B4d §4 勘误** |
| `D1-prime-history-audit.md` | prime-history composition：Euler 化 = 唯一分解的推论；非交换算子不够；add×mult defect = 平移 ⟹ Aff(ℤ) **可解** | 路线**拟判死**（已审天然类内） |
| `D2-mutation-canonicality-audit.md` | mutation：canonical 根替换 = Cayley–Hamilton ⟹ 秩-2 ⟹ **算术格** ⟹ 自守影子 ✗；自然临界量是 δ 非 1/2 | **拟判死**（§3 已收紧为"已识别来源的压缩"） |
| `D3-dual-scale-closure-prea_audit.md` | dual-scale closure：$\alpha+\beta=1$ 且 $\alpha=\beta$ ⟹ 两者 $\asymp\sqrt r$；本问题已有 canonical 答案（A′/B4d）但**答案是 generic** | **建议新增第 (5) 过滤器：非 generic** |
| `F-closure-and-H-exact-cancellation-audit.md` | F（无限非消去）= **CLOSED**；H（精确抵消律）canonical 实例 = Möbius/Mertens ⟹ **RH 等价重述**；成功实例 = 函数域 Weil（有限性正性） | F **CLOSED**；H 三分（trivial / RH-等价 / 有限性支撑） |
| `E1-information-loss-route-audit.md` | AFAC-v1 **CLOSED**；信息损失路线三重困境；canonical 极限 = $\widehat{\mathbb Z}\times$ archimedean profile ⟹ **Mellin 变换正是显式公式** | 路线**判死**；但正确解释了 Mellin 的不可避免性 |
| `E2-transport-second-order-dichotomy.md` | 二阶传输 $\Delta_{p,q}L$ 精确核验（1266 组）；**二分**：分解决定 ⟺ 只依赖局部数据；非分解决定 ⟹ 计数/误差函数 ⟹ 显式公式类 | **核验完成**；§14 形状 = 局部-整体 obstruction（Ш/类群/Brauer–Manin，全由 L-值测度） |
| `E3-why-this-is-not-the-old-pit.md` | 为何新方向不在旧坑 + 记录更正（唯一洞 = **OPEN, apparatus pending**）+ 技术修正（anomaly **不可能**是极限值；必须是**非单射局部化的核类**） | 方向 **OPEN**；含"四个缺口是同一个缺口"综合 |
| `E4-apparatus-bounded-and-Pi1-constraint.md` | anomaly 的**三处家**：(a) Galois 上同调（L-值测度 ✗）｜(b) Spec ℤ 新上同调（Deninger/Connes，停点已定位）｜(c) 模型论（新但未连线）；**Robin/Π₁ 必要条件** | (b) 与领域硬核**合流**（char 0 缺正性 = C6-C） |
| `E5-fourth-localisation-spec.md` | **三名字同构**（§15 ≡ 核类 ≡ β-wall 自由层）；精确刻画 **limit-seeing but finite-blind**；**五条设计规格**；四类 canonical 局部化全落已知箱子 ⟹ 需**第五个** | 产出 = **规格**而非对象；无候选 |

## 唯一那个洞的**四个等价表述**
```
① 【D3 §4】(5) 非 generic（依赖算术特异性）
② 【E1 §5】第三种不变量（非 congruence、非 archimedean）
③ 【E2 §3】非分解决定的 L（不是计数/误差函数）
④ 【E5 §6】第五个局部化系统（canonical + limit-seeing/finite-blind + 核非 L-值可测）
⟹ 单一缺口 = 【算术特异 + 非 completion + 非 L-测量 + limit-seeing/finite-blind】的机制
⟹ 该路线的实现可证明地归约到本领域核心难点（char 0 正性）⟹ 不是捷径；方向 OPEN 但 = 核心难点本身
```

## 全局约束（贯穿 B/C/D/E 全部轮次）
```
无 1/2 输入｜无递推输入｜无人为权重｜无人为范数｜无 GPS 审计｜未声称与 ζ 连接｜L2 保持冻结（VERIFIED）
```
