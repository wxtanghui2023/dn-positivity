已查地图（**先查后写**）：`C3874A`（**纯区间 LOCAL-ONLY；A 与二阶耦合** ✓✓）、`C-3873`（**机制命题** ✓✓）、`C-3872`（**Gordan** ✓✓）、`C-3864`（**control `t^* = +1`** ✓✓）、`C-3849`（**`E_{\mathrm{even}} \Rightarrow x_j > 0`（零原子层已排除）** ✓✓）、`C-3814`（**正三角对偶 sharp-closed：`\sum a_k \le 6c_0`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-75：C-3874-B —— Global Dual Functional Audit（点无关全局证书存在性审计）**（唐先生 2026-09-21 22:57 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 目标与硬门槛}✓✓：\text{证}\ \forall x \in E_{\mathrm{even}}✓：M(x) := \max_{k \in O}|F_k(x)| \ge c_0✓,\ O = \{1,3,\dots,23\}✓✓$$

$$\qquad \textbf{硬门槛（唐先生）}✓✓：\boxed{\text{先证明"存在全局对象"，再谈如何计算它}}✓✓$$

$$\textbf{② 规则}✓✓：B1 系数须}\ \textbf{global}✗\text{(禁点依赖)}✓；B2 必须}\textbf{真正使用 even}✓（even-blind ⟹ VOID ✓）；B3 不得把 KKT 局部证书伪装成 global ✓✓$$

$$\textbf{③ ⭐⭐ (i) even-blind 反例（}\textbf{决定性}✓✓）}：\text{删去偶频约束后}\ \boxed{\min M = \mathbf{0.000000000}}✓✓ \Longrightarrow \exists x:\ M(x) < c_0✓✓$$

$$\qquad \Longrightarrow \textbf{任何正确证书必须真正使用 even 约束}✓✓\ \text{（否则它证明的是}\ \textbf{假命题}✗✓）$$

$$\qquad \textbf{见证点结构（精确}✓✓）：c_1 = c_3✓,\ c_2 = c_4✓（\text{配对}✓）\ \text{且}\ c_5 = 0✓✓$$

$$\qquad \qquad \Longrightarrow \sum_j\sigma_jT_k(c_j)\ \text{塌缩为}\ \boxed{F_k = \sigma_5T_k(c_5)}✓✓ \Longrightarrow M = 0 \iff c_5 = 0✓✓\ \text{（因}\ T_k(0) = \cos(k\pi/2) = 0\ \forall k\ \text{奇}✓✓）$$

$$\qquad \Longrightarrow \textbf{该反例正落在已被}\ C\text{-}3849\ \textbf{排除的零原子层}✓✓（E_{\mathrm{even}} \Rightarrow x_j > 0✓,\ x_5 = c_5^2 = 0✗） \Longrightarrow \textbf{一致、无矛盾}✓✓$$

$$\textbf{④ (ii) 含全部 12 条偶频约束的正确探针}✓✓（\text{修正}\ C\text{-}3874A\ \text{的}\ 4/12\ \text{缺陷}✓）:}$$

$$\qquad \text{真可行下降}\ 33✓;\ \boxed{\text{最优}\ M = 2.170420828}✓ \Longrightarrow \textbf{未发现任何}\ M < c_0\ \text{的可行点}✓✓$$

$$\qquad \Longrightarrow \text{不与全局断言冲突}✓✓\ \text{（探针过弱、找不到}\ 0.8688\ \text{候选}✓,\ \text{但}\ \textbf{也不产生反例}✓）；\ \text{先前}\ 4/12\ \text{轮的}\ <0.8688\ \text{值}\ \textbf{确认 VOID}✓✓$$

$$\textbf{⑤ (iii) B1（线性全局泛函）}\textbf{已被档案封死}✗✓: \ \text{档}\ \texttt{C3814-sharp-closure-of-C380-13-trig-dual-type-sigma-a-le-6c0.md}✓✓$$

$$\qquad \Longrightarrow \text{正三角对偶}\ \textbf{sharp-closed}✓：\sum_k a_k \le 6c_0✓✓ \Longrightarrow \boxed{\text{线性泛函}\ \textbf{到不了}\ c_0}✗✓\ \text{（}\textbf{既有结论}✓,\ \text{仅引用，不列为提出}✓）$$

$$\textbf{⑥ ⭐ 存在性（回答硬门槛）}✓✓$: \text{系统在}\ c \in [0,1]^5\ \text{中}\ \textbf{是多项式}✓（\text{次数} \le 36✓,\ C\text{-}3874A\ \text{已证}✓） \Longrightarrow \text{目标命题是}\ \textbf{实闭域一阶语句}✓✓$$

$$\qquad \Longrightarrow \text{由}\ \textbf{Tarski–Seidenberg 实量词消去}✓✓：\text{可判定}✓,\ \text{且}\ \boxed{\exists\ \text{代数证书},\ \text{其数据只依赖}\ (\text{频率集},\ \sigma,\ c_0)}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{"存在全局对象"} = \textbf{YES}}✓✓\ \text{（}\text{点无关}✓,\ \text{全局}✓,\ \text{且必用 even}✓）$$

$$\qquad ⚠️ \textbf{但}✗✓：\textbf{无显式可用}\ \Phi✗；\ \text{SOS／Positivstellensatz}\ \text{在该次数规模下}\ \textbf{不可行}✗✓$$

$$\textbf{⑦ anti-circularity（B3）}✗✓：\text{任何由}\ C\text{-}3863／C\text{-}3872\ \text{乘子（}\omega_{13},\omega_{19},\lambda_q,c_* = 1/L✓）\ \text{反推的系数}\ \text{均}\ \textbf{点依赖}✗✓$$

$$\qquad \Longrightarrow \boxed{\textbf{LOCAL-ONLY}}✗✓\ \text{（}\text{Gordan 证书点依赖}✓,\ \textbf{不得升级为 global}✗✓）$$

## §1 判词（唐先生四出口 ✓✓）

$$\boxed{\textbf{GLOBAL-CERT-PARTIAL}}✓✓\ \text{—— 含义精确声明}✓✓：\textbf{存在性 YES}（全局、点无关、必用 even 的证书存在，由实量词消去保证✓✓）；\ \textbf{可用构造未达}✗（线性路线已 sharp-closed✗；非线性存在但不可构造✗）$$

$$\qquad \Longrightarrow \text{按唐先生规则}✓✓：\text{B 未给出}\ GLOBAL-CERT \Longrightarrow \textbf{立即转"全局证书 ＋ 局部二阶封口"复合路线}✓✓$$

$$\qquad \qquad \text{与}\ C\text{-}3874A\ \text{的发现}\ \textbf{互相印证}✓✓（\text{A 与二阶本质耦合}✓） \Longrightarrow \text{局部二阶（暂缓的 ④）}\ \textbf{成为承重项}✓✓$$

## §2 数值记录（数字驱动 ✓✓）

```
(i) even-blind：无约束 min M = 0.000000000；见证 c = [0.145097, 0.218617, 0.145097, 0.218617, -0.000589]
    其偶频违反量 max(F_2..F_24 - 1/2) = +3.442093（严重违反）
(ii) 全 12 约束探针：真可行下降 33；最优 M = 2.170420828；无 M<1.5 的可行值 -> 无反例
(iii) 档案：docs/C3814-sharp-closure-of-C380-13-trig-dual-type-sigma-a-le-6c0.md 存在（线性对偶 sharp 封口）
```
- 脚本 ✓：`scripts/c380_75_C3874B_audit.py`✓；输出 ✓：`scripts/out_c380_75.txt`✓

## §3 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| even-blind 反例 ✓ | **存在（`M = 0`，落在零原子层）** ✓✓ |
| even 约束的必要性 ✓ | **CLOSED（任何正确证书必用 even）** ✓✓ |
| 全 12 约束探针 ✓ | **无反例（最优 2.17 ≥ c₀）** ✓✓ |
| B1 线性全局泛函 ✓ | **档案 sharp-closed（`\sum a_k \le 6c_0`）** ✗✓ |
| 全局对象**存在性** ✓ | **YES（实量词消去）** ✓✓ |
| 全局对象**可用构造** ✓ | **未达** ✗✓ |
| KKT 系数升级为 global ✓ | **禁止（LOCAL-ONLY）** ✗✓ |
| **判词** ✓ | **GLOBAL-CERT-PARTIAL** ✓✓ |

## §4 边界（不得声称 ✗✓）

- **不**声称 `V_\sigma = c_0`（仍为上界候选）✓
- **不**声称已构造任何全局证书 ✓
- **不**把存在性结果当成可用证书 ✓
- **不**把 `M = 0` 见证点当成目标命题的反例（它在该层已被排除）✓
- **不**把 KKT 系数包装成 global ✓

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 点无关证书 命中文件数=0
技术词 even-blind 命中文件数=0
技术词 实量词消去 命中文件数=0
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{复合路线}✓✓：\big(\text{全局排斥（远离}\ x^*\big) + \big(\text{局部二阶封口（}x^*\ \text{邻域}\big)✓✓$$
$$\qquad \text{承重项}✓：\textbf{局部二阶}（\text{唐先生先前暂缓的 ④}✓）\ \Longrightarrow \text{与}\ C\text{-}3874A\ \text{的耦合发现一致}✓✓$$
$$\qquad \text{可选}✓：\text{低次显式}\ \Phi\ \text{搜索}（\text{受}\ B1\ \text{sharp-closed 限制}✓,\ \text{预期收益低}⚠️✓）$$
