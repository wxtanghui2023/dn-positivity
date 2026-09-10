# R-A8.2 审计记录：Precision-Gap Audit（第一轮，唐先生执行）

**日期**：2026-09-10 13:37+ ｜ 协议：`PROTOCOL-R8.2-precision-gap.md` ｜ 预算：纸面，无代码
**裁决**：$$\boxed{\textbf{R8-B（强化版）｜ R8-C 未证 ｜ R8-A 未证 ｜ R8-D 已排除}}$$
**本轮真正定位**：瓶颈 = **S2**；但**尚不足以升级为 R8-C**

---

## 六槽审计总表

| 槽 | 无条件状态 | 对 λ>1 的作用 | 判定 |
|---|---|---|---|
| **S1 对角** | 可控制（$\sum\Lambda(n)^2$ 型，由 PNT/平均二阶矩控制） | 非核心（不解释 support 为何停在 1） | ✓ |
| **S2 非对角 ★** | **有定义、有上界，但缺所需主项** | **核心瓶颈** | ⚠️ |
| **S3 H-均匀性** | 强结果不足 | 必需（依赖 S2 的 uniform 求值） | ⚠️ |
| **S4 主项精度** | 强渐近未得 | **必需** | ❌ |
| **S5 规范化/涌现** | 可处理（正负对称/三角权/端点/ψ-离散转换/素数幂/H 接近 X 的边界） | **技术层，非新机制** | ✓ |
| **S6 局部性** | 奇异级数 $\mathfrak S(h)=\prod_p(\cdot)$ 可得 | **不能全局锁定** | 🔒 |

**S5 警示**：它决定"你是否正确计算了 S2"，**不得让 S5 偷偷变成新机制**。
**S6 锁死**：$\mathfrak S(h)$ 只记录局部可容许性 ⟹ **R8 的潜在活口不能是"发现一个更漂亮的奇异级数"**（否则重落 local→global 旧 NO-GO）。

---

## ⭐ S2 的三级严格分离（本轮关键）

```
S2-a 可定义：C(h;X)=Σ_{n~X}Λ(n)Λ(n+h) 完全独立可定义 ⟹ **YES**
S2-b 无条件上界：筛法给强上界/平均控制，但**不能给 HL 型主项**
     ⟹ **unconditional upper bound ≠ correct second-order asymptotic**
S2-c 无条件正确主项：需要 C(h;X) ~ 𝔖(h)X 在适当 h-平均/平滑意义下 ⟹ **这才是 R8 的真正要求**
```
**文献状态**：2024 年短区间方差综述明确"prime short-interval variance asymptotics 无条件所知甚少"；
GM 标准方差公式 $V(X,H)\sim H\log X\,(1-\log H/\log X)$ 与 strong pair correlation 的关系**在 RH 框架下**建立。
$$\boxed{S2:\ \text{carrier = 独立}；\ \text{所需无条件精确评价 = 未知}}$$

---

## S4 — 主项精度（最易误判处）

R8 要辨认的主项：
$$V(X,H)\sim HX\log(X/H)=HX(1-\eta)\log X$$
$$\boxed{\text{support 参数正是通过 }1-\eta=1/\lambda\ \text{进入方差}}$$
⟹ 若误差项与主项同阶，**support 信息即丢失**。
⟹ 故 $H\ge X^{1/6+o(1)}$ 的 almost-all **一阶**结果 $\not\Rightarrow\lambda>1$。

---

## 无条件精度表（"有结果" vs "够 R8" 严格分开）

| $H=X^\eta$ | 无条件一阶 | 无条件二阶控制 | 无条件正确二阶渐近 | 猜想/条件 | R8 所需 |
|---|---|---|---|---|---|
| η→0 | 有，但接近长区间 | 粗控制 | **不足** | HL / PC 型 | 不足 |
| 0<η<1/2 | almost-all 覆盖部分 | 筛法/平均估计 | **无一般强渐近** | GM/HL/PC | 不足 |
| **η=1/2** | 一阶非核心困难 | 若干上界 | **正确二阶主项未知** | RH+PC 给相应理论 | **关键缺口** |
| 1/2<η<1 | 较长区间，一阶更易 | 较强 | 仍非 uniform 二阶理论 | RH/PC/HL | 不足 |
| H 接近 X | PNT/短区间理论较强 | 较易 | 对 λ>1 无关键突破 | 长区间理论 | 非决定性 |

**反直觉但重要**：$\eta$ 越大（H 越长）**一阶** prime counting 越容易，
$$\boxed{\text{但这不等于 }\eta\text{ 越大}\Rightarrow\lambda\text{ 越容易获得}}$$
因为 λ 信息来自**二阶方差主项结构**，不是"一阶有没有足够多素数"。

---

## S2 核心判据裁决：**R8-C 未触发**

```
已证：strong prime variance ⟺ strong pair correlation（在相应 RH 框架下）
⟹ 这只证明"现有强理论落入 zero-statistics 等价类"
⟹ **不能证明"任何未来的 canonical prime-side evaluation 都必然落入该等价类"**
   后者才是 Gate-4 结构性命题，需要一个真正的"必然等价/不可能性"定理 ⟹ 目前没有
⟹ **R8-C：未证**
```
**R8-A 亦未证**：未找到"不用 RH + 不用 zero statistics + 不用 HL + 给出所需二阶主项"的 prime-pair 机制；
BKS（Selberg class）明确采用 zero-statistics 路线，正因为一般不存在相应 HL 型 arithmetic autocorrelation 输入。

---

## ⭐ 新登记 R
$$\boxed{R_{8.2}:\ \text{R8 的困难不是获得 prime-pair 定义或粗上界，而是获得正确的 }HX\log(X/H)\text{ 级二阶主项}}$$
$$\boxed{\text{而该主项恰携带 }1-\eta=\frac1\lambda\ \Longrightarrow\ \textbf{support 信息}\ \longleftrightarrow\ \textbf{二阶方差主项的 }\eta\text{-依赖}}$$
比"素数对很难"精确得多。

## ⚠️ 唐先生的阻断（已入档）
```
λ=2 ⟺ η=1/2 ⟺ H≥√X：H=√X 确是真正的自对偶尺度
但**不能因为 √X 漂亮就把"H=√X"本身解释成 RH 机制**——
目前它只是 GM support 字典的尺度对应
要变成 RH engine 还需：独立 prime variance ⟹ zero-position constraint（**Gate 6 仍有效**）
```

## 本轮正式裁决
$$\boxed{S_1\checkmark\ |\ S_2\ \text{核心缺口}\ |\ S_3\ \text{依赖 S2 的 uniformity 缺口}\ |\ S_4\ \text{正确二阶主项缺口}\ |\ S_5\checkmark\text{技术性}\ |\ S_6\ \text{局部性排除}}$$
$$\boxed{\textbf{R8-B（强化版）}:\ \text{prime-pair carrier 真实、非编码、canonical；}\\
\text{但目前没有独立无条件的二阶精度可推进到 }\lambda_\zeta>1\text{，更不用说 }\lambda_\zeta\ge2}$$
**R8.2 的真正产出**：把"support>1"压缩成一个**明确的二阶非对角求值问题**，而非继续在抽象的 λ 坐标上打转。

## 诚实边界
```
· 第一轮结论为唐先生执行并签署；文献：Math. Z. 2024 综述、IMRN 2023 综述、PMC（pair correlation
  and twin primes revisited）、ORA（BKS）——均标【文献级】
· "R8-C 未触发"的依据是"缺必然性定理"，而非"已证不成立"
· 精度表中的分级为结构性整理，具体格位须以原文核实
· 未写代码、未做数值
```

## 提交链
```
4536671 R8 r1 → 本篇（R8.2 r1）→ PROTOCOL-R8.3
```
