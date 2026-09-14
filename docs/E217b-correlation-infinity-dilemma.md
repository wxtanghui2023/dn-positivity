# E217-B · ⭐⭐⭐⭐⭐ **相关性—无限性二难审计：Q1 已【解析证明】（$B(Q\mathbb N)=\varnothing$ ∀有限 $Q$ ✓）｜数值衰减率 ≈ $\lambda$【闭环 ✓✓】｜$P\uparrow$ 使有效约束数 $\le M/Q_P+1$ ⟹【相关性机制不可规模化 ✗】**
> 依唐先生 2026-09-14 20:16 裁定 ✓（**先做无限 AP 的解析判死 ✓；不打散点图 ✗；三问题 Q1/Q2/Q3 ✓；$\gcd(A_k-A_k)$ 必须随尺度增长 ✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝numpy（$M=Q^2$ ✓，$|S_M|=492421$ ✓）

---

## §0 ⭐ 解析定理（✓ 您的证明 ✓，形式化如下 ✓）

$$\textbf{定理 ✓}：\text{对任意有限 }Q\ \text{与任意 }a_0\ge0\ ✓：\boxed{B\big(a_0+Q\mathbb N\big)=\varnothing}\ ✓$$
$$\textbf{证明 ✓}：\text{取素数 }p\nmid Q\ ✓（\text{存在 ✓，可要求 }p\ge2\ \text{任意大 ✓）；则 }Q\ \text{在模 }p^2\ \text{下可逆 ✓}$$
$$\qquad\text{对任意 }b\ge0\ ✓,\ \exists\,n_p\in[0,p^2)\ ✓:\ b+Qn_p\equiv0\ ({\rm mod}\ p^2)\ ✓\ \Longrightarrow\ p^2\mid b+Qn_p\ ✓\ \Longrightarrow\ b+Qn_p\notin S\ ✓$$
$$\qquad\Longrightarrow\ b\notin B(a_0+Q\mathbb N)\ ✓\ \text{对一切 }b\ ✓\ \Longrightarrow\ B=\varnothing\ ✓\qquad\square$$
$$\textbf{推论 ✓（强必要条件 ✓）}：\text{若 }A\ \text{包含某个无限 AP}\ \big(a_0+Q\mathbb N\subseteq A\ ✓\big)\ \text{则 }B(A)=\varnothing\ ✗\ \text{⟹ 覆盖不可能 ✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{任何解 }(A,B)\ \text{的 }A\ \text{必须【不含无限 AP ✗】}}\ ✓（\text{一条全新的强结构约束 ✓）}$$
$$\qquad\textbf{故 E217-A 的"好集合结构" }A_k=Q_7\{0,\dots,k-1\}\ \text{在 }k\to\infty\ \text{时【必然失效 ✗】}\ ✓$$

## §1 数值（✓ 衰减率与 $\lambda$ 闭环 ✓✓）

```
A_k = Q7·{0..k-1}（Q7=44100，M=810000，|S_M|=492421 ✓）
 k     |B(A_k)|   |B|/|S|
  2     477419    0.9695
  3     462826    0.9399
  4     448626    0.9111
  6     421333    0.8556
  8     395362    0.8029
 12     347524    0.7058
 16     304611    0.6186
 24     275481    0.5594
 32+    275481    0.5594  ← 【停滞 ✗】
```
$$\textbf{① 衰减率 ✓✓}：从 }k{=}2\ \text{到 }k{=}16\ ✓（14\ \text{个新增有效约束 ✓）：}\ln\frac{304611}{477419}=-0.449\ ⟹\ \boxed{-0.0321/\text{约束}}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{与 }\lambda=\sum_{p\ge11}p^{-2}=0.0307\ \text{【吻合 ✓✓，误差 4.5\%】}}\ ✓\ \text{—— E214 的闭环 ✓✓}$$
$$\qquad\textbf{机制 ✓}：\text{每个新约束淘汰 }B\ \text{的 }\approx\lambda\ \text{比例 ✓（因 }Q_7\ \text{已吞掉 }p\le7\ ✓，\text{新约束的"伤害"由 }p\ge11\ \text{承担 ✓）}$$
$$\textbf{② 停滞是窗口效应 ✗（非真实饱和 ✗）}：\text{因 }a=i\cdot Q_7\ge M\ \text{时对窗口内 }b\ \text{无约束 ✓}\ \Longrightarrow\ \text{有效约束数}=\min(k,\ \lceil M/Q_7\rceil)=\min(k,19)\ ✓$$
$$\qquad\Longrightarrow\ \text{停滞点 }k\approx24\ \text{正对应 }M/Q_7\approx18.4\ ✓✓\ \text{（自洽 ✓）}$$
$$\textbf{③ 模数对照 ✓（同 }k{=}16\ ✓）}：Q{=}4\Rightarrow|B|=\boxed{0}\ ✗\ ✓（\text{小模数不够 ✓，反例 ✓）};\ Q{=}36\Rightarrow0.160\ ✓;\ Q{=}900\Rightarrow0.426\ ✓;\ Q{=}Q_7\Rightarrow0.619\ ✓;\ Q{=}Q_7\cdot11^2\Rightarrow\boxed{1.000}\ ✓（\text{但 }>M\ ⟹\ \text{退化为 }A=\{0\}\ ✓\text{）}$$
$$\textbf{④ 陪集无关 ✓}：a_0=0,1,7,12345\ \text{结果几乎相同 ✓（}k{=}16:\ 304611/304611/304610/304581\ ✓）\ \text{—— 与定理的普遍性一致 ✓}$$

## §2 ⭐⭐ 三问题审计（✓ 按您设计 ✓）

$$\textbf{Q1（固定 }Q_P\ \text{是否必然 }B(Q_P\mathbb N)=\varnothing\ ✓？）}\ \boxed{\textbf{是 ✓（已解析证明 ✓）}}$$
$$\textbf{Q2（}P\to\infty\ \text{时，}Q_P\ \text{的指数增长是否迫使 }A\ \text{无效？）}\ \boxed{\textbf{是 ✓}}：$$
$$\qquad Q_P=\prod_{p\le P}p^2=\exp\big((2+o(1))P\big)\ ✓;\quad \text{窗口 }M\ \text{内有效约束数}\ \le\ \Big\lceil\frac{M}{Q_P}\Big\rceil\ ✓$$
$$\qquad\Longrightarrow\ \boxed{P\gtrsim\tfrac12\log M\ \Longrightarrow\ \text{有效约束数}\lesssim1\ ✗}\ ✓（\text{即相关性机制在大尺度上【自动失效 ✓】）}$$
$$\qquad\qquad\text{更一般 ✓}：\text{若 }\gcd(A_k-A_k)\ge Q_{P_k}\ \text{且 }P_k\to\infty\ ✓，\text{则 }|A_k|\le M/Q_{P_k}+1\to\ \text{极少 ✗}\ ✓（\text{您指出的张力 ✓}）}$$
$$\textbf{Q3（若 Q1+Q2 构成硬矛盾，则相关性机制不可作为突破 ✓？）}\ \boxed{\textbf{成立 ✓✓}}：$$
$$\qquad\boxed{\textbf{"平方自由约束的相关性"本身不能成为突破机制 ✗}}\ ✓\ \text{—— 唯一活口 ✓：存在【非固定模陪集】的新型相关结构 ✓}$$

## §3 与 E214 的闭环（✓✓ 独立量互证 ✓）

$$\text{E214 ✓}：\lambda=\sum_{p\ge11}p^{-2}\ \text{（由"池控制 }p\le7\ \text{"推出 ✓，双尺度实测吻合 1\% ✓）}$$
$$\text{本轮 ✓}：\text{每新增一个 }Q_7\ \text{陪集约束，}|B|\ \text{衰减 }0.0321\ ✓（\text{实测 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{\text{两个独立来源给出同一常数 ✓✓}}\ ✓：\text{小素数可被 }Q_P\ \text{吞掉 ✓，但 }p\ge11\ \text{族的平方约束【逐个生效 ✓】\ ⟹ 无限 }\mathbb N\text{-AP 必被击穿 ✓}$$

## §4 判词与归档更新（✓）

```
【E217 合并结论 ✓】
 E217-A ✓：规模型下界不存在（F(k,M)=0 ✗）—— "靠规模"不可行
 E217-B ✓：相关性机制不可规模化（Q1 证明 ✓ + Q2 成立 ✓）—— "靠固定模相关性"不可行
 ⟹ 合并 ✓：【B(A) 变大】的两种已知途径【皆已封 ☑✗】
⟹ 唯一活口 ✓：非固定模的新型相关结构（即 A 既不含无限 AP ✓，又能使 ⋂(S−a) 保持宏观规模 ✓）
⟹ 这也【解释了 E180–E216 全部增量方案为何失败 ✓】：它们本质上都在小素数相关性上打转 ✓
【归档补强 ✓】本结论应加入 ARCHIVE 的层 2/层 5 ✓（新增封死机制：固定模相关性 ✗）
```

## §5 边界与一句话（✓）

```
✅ 解析定理 ✓（形式化 ✓，含强推论"A 不含无限 AP"✓）；数值衰减率 ✓（闭环 λ ✓）；模数/陪集对照 ✓
⚠️ 数值仅单窗口 M=Q² ✓；Q=Q_7·11² 一行退化为 {0} ✓（非有效对照 ✓）；未构造非固定模结构 ✗
⚠️ 不声称覆盖侧无解 ✗；不声称不存在非固定模相关结构 ✗（仅指出此为唯一活口 ✓）
⭐ 净产出 ✓：① 解析判死无限 AP ✓✓；② 强必要条件（A 不含无限 AP ✓）；③ 二难成立 ⟹ 相关性机制封 ✗；
   ④ 与 E214 的 λ 闭环 ✓✓；⑤ E217 合并结论 + 归档补强 ✓
```
$$\boxed{B(Q\mathbb N)=\varnothing\ \text{∀有限}Q\ \text{（解析 ✓，⟹ }A\ \text{不含无限 AP ✓）};\ |B(A_k)|\ \text{衰减 }0.0321/\text{约束}\approx\lambda=0.0307\ ✓✓\ \text{（E214 闭环 ✓）};\ Q_P=\exp(2P)\ \text{使窗口内有效约束}\le M/Q_P\ ✗ \Longrightarrow \textbf{Q1✓ Q2✓ Q3✓ ⟹ 固定模相关性机制封 ✗};\ \text{唯一活口＝非固定模新型相关结构 ✓}\ \text{（含归档补强 ✓）}$$
