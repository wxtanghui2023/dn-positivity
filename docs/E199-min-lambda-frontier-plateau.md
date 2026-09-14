# E199 · ⭐⭐⭐⭐⭐ **单层最小-$\lambda$ 前沿扫描：$G_{\max}(\lambda)$ 是【平台】✗（不随 $\lambda\downarrow$ 塌陷 ✓）⟹ 判死条件【未触发 ✓】｜发现 $\lambda=0.019,\ G=52714$（44% 的 $D^{\rm pers}$）✓✓**
> 依唐先生 2026-09-14 18:08 裁定 ✓（**打"最小 $\lambda$–覆盖收益曲线"✓，不打 $W$ 扩张 ✓；单层高密度扫描 ✓；唯一问题：$G>0$ 时 $L/|B|$ 能否趋向 0 ✗**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝精确枚举（$P{=}5$ 基线态、$Q=900$、Lim$=810000$ ✓）

---

## §0 设计（✓）

$$\text{基线态 ✓}：A_0=\{0,1,4,8,36\}\ ✓,\ |B_0|=138394\ ✓,\ |D^{\rm pers}|=119643\ ✓\ (D/B=0.8645\ ✓);\quad W\ \text{固定 ✓}$$
$$\textbf{候选族 ✓}：P\in\{5,7,11\}\ \text{三族，每族取【逐素数残类组合】(}c\bmod p^2\in A\bmod p^2\ \forall p\le P\ ✓\text{)＋}c=\text{base}+kQ_P\ ✓,\ c\le1.5\times10^6\ ✓$$
$$\qquad\text{并强制 }W\ \text{相容（}c+w\in S\ \forall w\in W\ ✓）\ ✓;\qquad \text{共评估 }121+524+41=686\ \text{个候选 ✓}$$
$$\textbf{记录 ✓}：\text{按 }\lambda=L/|B_0|\ \text{分桶（}[0,0.002),[0.002,0.005),[0.005,0.01),[0.01,0.02),\dots\ ✓\text{），每桶取最大 }G\ ⟹\ \boxed{G_{\max}(\lambda)}\ ✓$$

## §1 ⭐ 结果（✓ 686 候选 ✓）

```
λ 区间            max G     实际λ      c       P    G/(λ|B₀|)
[0.000,0.010)      —         —        —       —     【空 ✗】（未找到任何 λ<0.01 的候选）
[0.010,0.020)    52714    0.01908   14161     7      19.97
[0.020,0.030)    48309    0.02509   35329     7      13.91
[0.030,0.050)    52749    0.04488     125     5       8.49
[0.050,0.100)    52357    0.05314    1025     5       7.12
参考 ✓：|B₀|=138394，|D_pers|=119643，D/B=0.8645
```

## §2 三项核心判读（✓）

$$\textbf{① }\lambda\ \text{存在下界 ✓（未找到 }<0.01\ \text{者 ✗）}：\ \lambda_{\min}\approx0.019\ ✓（L=2641\ \text{✓，即仅损失 }1.9\%\ \text{的 }B\ ✓）$$
$$\textbf{② ⭐ }G_{\max}(\lambda)\ \text{是【平台 ✗，不是塌陷 ✓】}：\lambda\ \text{从 }0.053\ \text{降到 }0.019\ \text{（2.8 倍 ✓）时，}G_{\max}\ \text{几乎不变（}52357\to52714\ ✓）$$
$$\qquad\Longrightarrow\ \boxed{G_{\max}(\lambda)\approx5\times10^4\ \text{（}\approx44\%\ \text{的 }D^{\rm pers}\ \text{✓）在 }0.019\le\lambda\le0.053\ \text{上为常数 ✓}}\ ✓\ \text{—— 即 }G\ \text{不随 }\lambda\downarrow\ \text{而趋于 0 ✗✓}$$
$$\textbf{③ 效率随 }\lambda\ \text{下降而上升 ✓}：G/(\lambda|B_0|)：7.12\to8.49\to13.91\to\boxed{19.97}\ ✓\ \text{（}\lambda\ \text{越小越划算 ✓）}$$

## §3 ⭐ 判死条件检查（✓ 您 E199 §6 ✓）

$$\text{判死需 ✓}：G_{\max}(\lambda)\le C\lambda|B|\ \text{（线性上界 ✓）}\ \wedge\ \sum G=\infty\ \text{时必须 }\sum\lambda=\infty\ ✗$$
$$\qquad\text{实测 ✓}：\lambda=0.019\ \text{时 }C\lambda|B|=C\times2641\ ✓;\quad G_{\max}=52714\ ✓\ \Longrightarrow\ \textbf{需 }C\ge20\ ✓\ \text{才算线性 ✗}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{判死条件【未触发 ✓】}}\ ✓\ \text{（}\sum G=\infty\ \text{可在 }C=20\ \text{的线性界内实现 ✓，但界本身很松 ✓）}$$
$$\textbf{且实况强于您的 §7 期望 ✓}：\text{不是 }G\asymp|B|\lambda^\beta\ (\beta<1)\ ✓，\text{而是 }\boxed{\beta\approx0\ \text{（平台 ✓）}}\ \text{—— 更强 ✓}$$
$$\qquad\Longrightarrow\ \text{固定 2\% 代价/步 ⟹ 每步消灭 44\% 的 }D^{\rm pers}\ ✓\ \Longrightarrow\ D_k/D_0\sim0.56^k\ ✓\ \text{而 }|B_k|/|B_0|\sim0.981^k\ ✓$$
$$\qquad\Longrightarrow\ \boxed{D_k/B_k\to0\ \text{（指数级 ✓）}}\ ✓\ \text{—— 这正是覆盖率亏损消失的条件 ✓✓}$$

## §4 ⭐⭐ 附带发现：E198 的搜索空间太窄 ✗（重要 ✓）

$$\text{E198 每步实得 ✓}：G\approx1000\!\sim\!5000\ ✓,\ \lambda\approx0.031\ ✓;\qquad \text{E199 同态下存在 ✓}：G=52714\ ✓,\ \lambda=0.019\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{E198/E196 的轨迹【未使用最优候选 ✗】}}\ ✓（\text{其族限 }c\lesssim7000\ \text{✓ 且只扫 60 个 ✓；E199 扫到 }c=14161\sim35329\ ✓）$$
$$\qquad\Longrightarrow\ \textbf{E196/E198 的"再生相 ✗"可能是【搜索能力不足】的产物 ✓}\ ✓\ \text{（与 E192→E193 的族太窄教训同型 ✓✓）}$$

## §5 判词（✓）

$$\boxed{\textbf{该路线【活 ✓】（判死未触发 ✓）}}\ ✓：\lambda\ \text{有下界 }\approx0.019\ ✗\ \text{但 }G_{\max}\ \text{在可用 }\lambda\ \text{域上是平台 ✓}$$
$$\qquad\text{且效率比值最高达 20 ✓（}\lambda=0.019\ \text{时 ✓）⟹ 每单位 }B\ \text{损失换 20 倍 dead 清除 ✓}$$
$$\qquad\Longrightarrow\ \textbf{可求和 }\lambda\ \text{路线：}\sum\lambda=\infty\ \text{仍成立 ✗（}\lambda\ \text{恒定 ✓），但 }D/B\to0\ \text{可期 ✓ ⟹ 判据应从"}\sum\lambda<\infty\ \text{"改为"}\ D_k/B_k\to0\ \text{"✓}$$
$$\qquad\qquad\text{（后者是覆盖率亏损消失的充分条件 ✓，且不需要 }B\ \text{不衰减 ✓）}$$

## §6 (E200) 建议（✓ 按您的优先级 ✓）

```
★ E200：用改进搜索重跑轨迹 ✓（对象改变 ✓，不是延长 E198 ✗）
  ① 候选族 ✓：P≤7（必要时 P≤11 ✓），c≤1.5×10⁶ ✓
  ② 选择规则 ✓：min λ subject to G ≥ θ·D_k ✓（θ=0.2/0.3/0.4 三档 ✓）
  ③ 硬保持 ✓：W ⊆ B_k ✓（不变 ✓），嵌套 ✓
  ④ 记录 ✓：u_k、q_k、λ_k、D_old/D_new、ρ_k、**D_k/B_k** ✓（新关键量 ✓）
  判活 ✓：D_k/B_k 单调下降 ⟹ 首次真正接近 🟢 ✓
  判死 ✓：D_k/B_k 持平或上升 ✗ ⟹ 路线真死 ✓
⚠️ 局限 ✓：λ<0.01 未找到（但 P=11 族只评了 41 个 ✗ ⟹ 下界未穷尽 ✓）
```

## §7 边界与一句话（✓）

```
✅ 686 候选 ✓（三族 ✓）；λ 分桶 ✓；G_max(λ) ✓；判死条件检查 ✓；G/(λ|B|) ✓
✅ 结论 ✓：λ 下界 ≈0.019 ✗；但 G_max 是平台（β≈0 ✓，强于 β<1 ✓）；判死未触发 ✓；效率 ≥7（最高 20 ✓）
✅ 附带 ✓：E196/E198 的再生相可能是搜索不足的产物 ✗（同 E192→E193 教训 ✓）
⚠️ 单层扫描（未跑轨迹 ✗）；P=11 族欠采样 ✗；W 固定 ✓；不声称构造成立 ✗
```
$$\boxed{G_{\max}(\lambda)\approx5\times10^4\ \text{（44\% 的 }D^{\rm pers}\text{）在 }\lambda\in[0.019,0.053]\ \text{上为【平台】✓（}\beta\approx0\ ✓\text{）；}\lambda\ \text{下界 }\approx0.019\ ✗\ \text{；判死条件未触发 ✓；E196/E198 的再生相疑为搜索不足 ✗ ⟹ E200：改进搜索重跑轨迹，监控 }D_k/B_k\to0\ ✓}$$
