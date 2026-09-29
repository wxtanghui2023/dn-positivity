# AUDIT-2026-09-29zi — (A) 层覆盖不等式族：**新工具成立但不足**；(B) 混合框架评估

> 空间 B｜非 C 号｜唐先生令（22:47「A, B」）｜**不主张 107／不主张 106 可排除**（V290）
> 时间：2026-09-29 22:5x

**已查地图**：承 `AUDIT-zh`（α/β 否定）／`AUDIT-zg`／`LEMMA-L1`／`ROUTE-…-107-ladder`（F1–F9）
D0: 本档对象 = **档案已有**（距离分布 $A_k$／层覆盖／Krawtchouk）之**新组合**（新数学对象：**族**为新工具 ⚠️）
D1: 0（产出 = 一个**已验证不等式族** ＋ 一条**否定判定** ＋ 一份 **B 线评估** ⚠️✓）

---

## §1 (A) 层覆盖不等式族 —— **推导 ＋ 双码验证** ✓✓

$$\text{码字 }c\ \text{与层 }k\ge2:\ Y_k(c):=\{y: d(y,c)=k\},\ |Y_k|=\binom nk;\ \text{每点须被覆盖}$$
$$\text{若 } d(c,c')=j,\ \text{则 }c'\ \text{覆盖之}\ Y_k\ \text{点数}\ \psi(k,j)=\begin{cases} n{+}1{-}k & j=k-1\\ 1 & j=k\\ k{+}1 & j=k+1\\ 0 & \text{else}\end{cases}$$
$$\Longrightarrow\ \binom nk\ \le\ (n{+}1{-}k)\,d_{k-1}(c)+d_k(c)+(k{+}1)\,d_{k+1}(c)\qquad(k=2..n)$$
$$\text{对 }c\text{ 求和（}\Sigma_c d_j(c)=2A_j\text{）}:\quad \boxed{\ M\binom nk\ \le\ 2(n{+}1{-}k)A_{k-1}+2A_k+2(k{+}1)A_{k+1}\ }$$

**验证（实跑）** ✓✓：62-码（$n{=}9$）8 条**全部成立**；120-码（$n{=}10$）9 条**全部成立**（逐条数字见脚本 `scripts/layer_cover_A.py`）

## §2 (A) 判定：对 $M{=}106$ **不足** ✗

$$\min\ \Sigma_k A_k\ \text{s.t. 层覆盖族}\ +\ A_1{+}A_2\ge\tfrac12\Sigma\delta\ +\ \text{Krawtchouk 正性}\ +\ A_1\le49\ =\ \mathbf{4930}$$
$$\text{而}\ \Sigma_kA_k\ \textbf{必须}=\binom{106}2=\mathbf{5565}\ \Longrightarrow\ \text{松弛}\ 635\ \Longrightarrow\ \textbf{无矛盾}\ ✗$$
（对比：只加层覆盖族 $=4906$；加 k=10 层后 $4930$）

## §3 聚合层**总判定**：彻底饱和 ✗（本档核心）

$$\text{把**全部**可用聚合约束合起来（}\mu\text{-剖面 2 条恒等式 ＋ }\Sigma\binom\mu2{=}2(A_1{+}A_2)\text{ ＋ }\Sigma\binom\mu3{=}P{+}E\text{ ＋ }P\le2A_2$$
$$\qquad\text{＋ 层覆盖族 }k{=}2..10\text{ ＋ Krawtchouk 正性 ＋ }\Sigma A_k{=}\binom M2\text{ ＋ }A_1\le49\text{），对 }M{=}106\ \text{求可行性}:$$
$$\boxed{\textbf{系统可行} \Longrightarrow\ \text{聚合（总量 ＋ 距离分布 ＋ 谱）层\ \textbf{彻底饱和}}\ ✗✗}$$
**实跑之一解**：$n_{1..11}={983,3,26,1,1,0,1,1,6,1,1}$；$A_{1..10}={8,223,1204,1114,467,1127,1133,186,22,81}$；$P{=}0,\ E{=}920$

## §4 (B) 混合框架评估

| 路径 | 状态 |
|---|---|
| 取 BÖW 原文 | **禁区** ✗（R09／R16／R17，唐先生明令"论文不可得"） |
| fiber／混合**重编码** | **已封** ✗（R05 `EXACT-RESTATEMENT`；`WITFIB`／`AUDIT-29s`：任意 $r$ 之 fiber 分解＝精确重述，非归约） |
| 混合码**球界** | 与二元球界同形（$\Pi q_i/(1{+}\Sigma(q_i{-}1))$）⟹ 于 $n{=}10$ 仍 $93.09$ ✗ |

$$\Longrightarrow\ \text{B 之\ \textbf{经典形式不可复用}（原文不可得 ＋ 重编码已封）};\ \text{只能是\ \textbf{新机制}}$$
$$\Longrightarrow\ \text{而 §3 已证\ \textbf{聚合层饱和} ⟹ 新机制必须位于\ \textbf{实现层（几何可实现性）} 或 \textbf{非线性/整性}}$$

## §5 结论与建议

- **(A) 净收获**：一个**已验证的新不等式族**（层覆盖族，双码核验 ✓✓）—— 可复用工具，但对 106 不足
- **本轮累计否定**（自 `AUDIT-zh` 起）：(α) 计数差 26×｜(β) $\mu_{\max}$ 迭代无矛盾｜(A) 层覆盖不足｜**聚合层总判定可行**
- **建议**：把火力集中到**实现层** —— 即"哪些 $(A_k,\mu\text{-剖面})$ 组合能由 $Q_{10}$ 上的真实点集实现"；这需要**构造性/几何**引理，而非再堆线性约束 ⚠️
- **待唐先生定**：是否转入实现层（属方向性决策 ✗ 不自裁）

## §6 边界（硬 ✓）

- **不主张** 107／106 可排除／任何新值 ✗；层覆盖族为**新工具**，其**不足**亦如实记录 ✓
- 未取论文原文（R16–17）／未重攻 pair 层（R02）或 fiber（R05）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
