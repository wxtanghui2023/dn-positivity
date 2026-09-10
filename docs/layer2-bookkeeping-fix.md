> ⚠️ **SUPERSEDED**：本文件的权威版本为 `L2-RAMIFICATION-STATE.md`。
> 本文件保留作历史记录；其中的若干数值**已撤回**（见权威文件 §2），请勿引用本文件的数值结论。

# ① 修正局部 ramification bookkeeping（**不碰 Layer 3/4**）

**日期**：2026-09-10 21:00+ ｜ 依据：唐先生收窄指示（只修 bookkeeping）｜ 代码 `scripts/ramification_bookkeeping_fix.py` ｜ 输出 `/tmp/bookkeeping_fix_out.txt`

---

## §1 标定对象 $F=\mathbb Q_2(\zeta_8)$：真值 $d=8$
（因 $|\mathrm{disc}\,\mathbb Q(\zeta_8)| = |\mathrm{disc}(x^4+1)| = 4^4\cdot N(\zeta)^3 = 256 = 2^8$ ✓；$\mathbb Z[\zeta_8]$ 极大 ✓）

**环模型**：$\mathbb Z[x]/(x^4+1)$，$v(x)=v_2|N_{F/\mathbb Q}(x)|$（$e=4=[F:\mathbb Q]$, $f=1$ ⟹ $v=v_2(N)$ 正确 ✓）
**sanity**：$v(2)=4$ ✓（$=e$）；$v(x-1)=1$ ✓（$\zeta_8-1$ 是 uniformizer ✓）
**判据**：$G_i=\{\sigma:\min_{e\in\mathfrak B}v(\sigma(e)-e)\ge i+1\}$，$\mathfrak B$ 为 $O_F$ 的 $\mathbb Z$-基

### ⭐⭐ 同一判据、两个基 ⟹ 结果不同：**bug 机制就是这个**
| 基 | $i_G(\sigma_3)$ | $i_G(\sigma_7)$ | $i_G(\sigma_5)$ | $\lvert G_i\rvert$ | $d$ |
|---|---|---|---|---|---|
| **极大基** $\{1,x,x^2,x^3\}=O_F$ | 2 | 2 | 4 | **4,4,2,2,1** | **8 ✓ 与真值一致** |
| 非极大基 $\{1,i,\sqrt2,i\sqrt2\}$ | 4 | 4 | 6 | 4,4,4,4,2,2,1,1 | **14 ✗ 膨胀** |

$$\boxed{\text{bug 机制} = \text{用【非极大阶】的 }\mathbb Z\text{-基} \Longrightarrow i_G\text{ 偏大} \Longrightarrow \text{群偏大} \Longrightarrow d\text{ 膨胀（index trap）}}$$
**⟹ 这解释了 $L$ 上我得到的 $d=50$：它用的是 $\mathbb Z[\delta,i]$，若 $O_L\supsetneq\mathbb Z[\delta,i]$ 则该值被膨胀。**

## §2 三栏对照（$F$，lower $G_i$ ↔ Herbrand $\varphi$ ↔ upper $G^u$）
| $i$ | $\lvert G_i\rvert$（lower） | $\varphi(i)=\frac1{\lvert G_0\rvert}\sum_{j\le i}\lvert G_j\rvert$ | $G^i$（upper） |
|---|---|---|---|
| 0 | 4 | 0 | 4 |
| 1 | 4 | **1** | 4 |
| 2 | 2 | 1.5 | 2 |
| 3 | 2 | **2** | 2 |
| 4 | 1 | 2.25 | 1 |

**lower breaks**：$\gamma_1=1$（$|G_1|=4\to|G_2|=2$），$\gamma_2=3$（$|G_3|=2\to|G_4|=1$）
**upper breaks**：$\varphi(\gamma_1)=1$，$\varphi(\gamma_2)=2$ ⟹ **皆整数 ⟹ Hasse–Arf ✓**
（⚠️ 更正：$\varphi(2)=1.5$ **不是**问题——$i=2$ 不是 break；Hasse–Arf 只对 break 处要求整数 ✓）

## §3 Tower 记录（唐先生要求的逐层 $e,f,d,G_i,G^u$）
| 层 | $e$ | $f$ | $d$ | Galois? | filtration / 备注 |
|---|---|---|---|---|---|
| $\mathbb Q_2(\sqrt2)/\mathbb Q_2$ | 2 | 1 | 3 | 是 | $\lvert G_i\rvert=2,2,2,1$（$i_G(\sigma)=3$）✓ |
| $\mathbb Q_2(2^{1/4})/\mathbb Q_2$ | 4 | 1 | **11** | 否 | 闭包为 $L$（Layer 1 精确 ✓） |
| $L/\mathbb Q_2$ | 8 | 1 | $\le 30$ | 是 | **真值未定 —— 需 $O_L$** |

## §4 本轮结论（严格按唐先生的收窄目标）
```
① 的【方法学部分已完成】：判据与 valuation 约定校准通过（F 上 d = 8 ✓），
   且我上一轮的失败机制被【复现证明】为 index trap（非极大基 ⟹ 膨胀：8 → 14）
⟹ 路线 C 的数值（L 上 50）确认为【artifact】，作废 ✓（与唐先生判断一致）
⚠️ 但①的【完成】需要一个我此前没有的东西：O_L（极大阶）。
   即：要把 L 的 filtration 算对，必须先知道 O_L ⟹ 唐先生列为第③步的 index 检验
   在此【被证明为①的必要前提】，不是可选的独立验证。
⟹ 我【没有】为了匹配 30 去调 filtration（遵嘱）；也没有开始②；Layer 3/4 保持"结构猜想"，未污染本轮。
```

## §5 诚实边界
```
· §1 的标定（F：极大基 8 ✓ / 非极大基 14 ✗）为精确可复现计算 ✓
· §2 的 Herbrand 表按 φ(i)=(1/|G_0|)Σ_{j≤i}|G_j| 计算 ✓；Hasse–Arf 检查通过 ✓
· §3 中 L 的真值【未定】；d ≤ 30 来自路线 A（阶判别式 = index²·D_L 的上界性质）
· 经典引用（非我证明）：disc(x⁴+1)=256；ℤ[ζ₈] 极大；d=Σ(|G_i|−1)（Galois lower 编号）
· 本轮未做任何审计；未声称临界指数；未声称与 ζ 连接；Layer 3/4 未触碰
```

## §6 下一步（需唐先生批准，因涉及③）
```
要完成①：必须先定 O_L（或找一组极大基）。两条候选：
  (a) 在 Z[δ,i] 上做 round-2 式搜索，判定 index（[O_L:Z[δ,i]]）
  (b) 用 D₄ 的五个特征做 conductor-discriminant 定 |D_L|，再反推 index（= 唐先生第②步）
⟹ 建议：先做 (a)（直接、局部、不需解析输入），再做 (b) 作独立验证
```
