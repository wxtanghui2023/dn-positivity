# 🗺️ **107 线 · 失败地图 ＋ 资产账 ＋ 反重复清单**（**每轮开工前必读**）

> **性质**：**汇总地图**（不产生新数学）——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **用途**：**今后任何 107/119 轮次，开工第一件事读本档**（唐先生 2026-09-29 令：失败必须学习、总结、积累）✓
> **维护**：每轮结束若新增封闭/新增资产，**必须回写本档** ✓

**已查地图**：本档由 `docs/` 全档汇总（引档名可核）✓

D0: 本档对象 ＝ **档案已有**（全部条目皆有出处 ✓）
D1: 0（产出＝**一份汇总地图 ＋ 反重复清单** ⚠️✓）

---

## §1 阶梯（**数值均已核验** ✓）

$$94\ (\text{球界})\ <\ 103\ (\text{van Wee 1988},\ 2^n/n)\ <\ 105\ (\text{Zhang pair},\ \textbf{未复现})\ <\ 107\ (\text{BÖW 2004},\ \textbf{源不可得})\ \ll\ 120\ (\text{上界},\ \textbf{证书在手})$$
$$\textbf{最强松弛}:\ \text{SDP-3 (Gijswijt--Polak 2025)}\Rightarrow\mathbf{105.2223}\Longrightarrow106\ <\ 107\ (n{=}10)$$
$$\textbf{excess 数值}:\ M{=}106\Rightarrow E{=}142;\quad 107\Rightarrow153;\quad 119\Rightarrow285;\quad 120\Rightarrow296\ \checkmark$$

## §2 ⭐⭐ **两条结构性定理**（**解释"为什么全部失败"** —— 最该记住的）

$$\boxed{\text{【定理 A｜Aut-不变性】}\ \text{松弛族（Delsarte LP／SDP-3/Terwilliger／Habsieger 同余）皆}\ \operatorname{Aut}(Q_{10})\text{-不变}}$$
$$\qquad\Longrightarrow\ \text{其天花板}\ \textbf{结构上}\ =\ 105.2223;\quad \text{而 }107>105.2223\ \Longrightarrow\ \boxed{107\ \textbf{必出自非松弛／整性论证}}✓$$
$$\text{（出处}\ \texttt{AUDIT-29d}\ \text{原作者自述"层次不可升"／}\texttt{DIAGNOSIS-2026-09-29}）$$

$$\boxed{\text{【定理 B｜目标等价】}\ F(A)>9a-406\iff |D_A|>106-a\iff\ \text{覆盖问题本身（fiber＝精确重述）}}$$
$$\qquad\Longrightarrow\ \boxed{\text{任何对 }A\ \text{的\ \textbf{局部/统计分解}（}u,\ f(j),\ \text{profile 矩},\ G_3\ \text{度数},\ \text{逐-}q,\ \text{过剩分解）对目标\ \textbf{信息量为零}}}✓$$
$$\text{（出处}\ \texttt{CONNECTION-AUDIT-2026-09-29}／\texttt{RESULT-l}\ \text{—— 十几轮反复验证）}$$

## §3 🚫 **反重复清单（DO-NOT-RE-DO）** ← **最重要的一节**

| # | 禁止重做的事 | 为何 | 出处 |
|---|---|---|---|
| 1 | 从 Struik 论文重取 van Wee 界 | **同一界，已在档** | `AUDIT-28q`（源 `arXiv:2608.12595` 自注引 Struik 1994） |
| 2 | 重攻 pair 层（任何形式） | **三重独立失败，皆 103** | `ASSETS-REGISTRY` L3392／`AUDIT-28ai` |
| 3 | 点态 parity 主张 | **三次被推翻** | `AUDIT-29z` |
| 4 | 粗 $p{=}11$ 同余 | **恒等式** | `AUDIT-29z` |
| 5 | fiber 分解（任意 $r$） | **精确重述，非归约** | `WITFIB`／`AUDIT-29s` |
| 6 | 任何 $\sum f(\mu(x))$ 型矩不等式 | **∈Delsarte 张成** | `AUDIT-29zc`（face／`AUDIT-29y`） |
| 7 | 任何 Aut-不变线性/谱泛函 | **≤105.2223（定理 A）** | `DIAGNOSIS` |
| 8 | "局部 → 强制 holes" 型论证 | **无机制，已被反例堵死** | `RESULT-h`／`RESULT-l` |
| 9 | 找 BÖW 2004 正文 | **不可得（唐先生多次令）** | — |
| 10 | $\Lambda$ pair 污染量 | **$=3\sum\binom\mu3$ 重编码** | `AUDIT-29za` |
| 11 | $L(p)$ 全局 packing 机制 | **$\equiv0$（packing 零 excess）** | `RESULT-m` |
| 12 | 逐-$q$ 敌意关系 | **违例 300/576** | `RESULT-l` |
| 13 | 度数集中 → 压 $u$ | **被 $\lvert Q\rvert$ 截断** | `RESULT-j` |

$$\textbf{判据}:\ \text{凡新候选先比对本表};\ \textbf{命中即停}\ ✗;\ \text{且失败分类须为类 7（真断点）才可继续};\ \text{类 1–6 一律停}\ ✓$$

## §4 已封闭层（**累计层级账**）

$$\text{sphere}=94\ \|\ \text{excess(van Wee/Habsieger/Honkala/Haas)}=103\ (\text{饱和})\ \|\ \text{Zhang pair 单条}=103\ \|\ \text{induced }Z^{(i)}+非负=103\ \|\ \text{induced}+FM=103\ (\text{无闭合})$$
$$\text{Struik/van Wee\ \textbf{一阶局部不等式}}:\ \text{偶 }n\to1,\ \textbf{奇 }n\to0\ (\text{空})\ \|\ \text{SDP-3}=105.2223\Rightarrow106\ \|\ \text{4F-cell/face/private/fiber}= 平凡或球界$$
$$\Longrightarrow\ \boxed{\textbf{自助路线在全部分解层皆止于 }103\text{–}106;\ \text{无一越过 }107}$$

## §5 ✅ 已验证资产（**可复用，含复用规则**）

| 资产 | 内容 | 出处 |
|---|---|---|
| **120-cover 证书** | 120 词，覆盖 1024/1024 可复跑 | `sources/K10-1-120-cover-CERTIFICATE.txt` |
| **$K(9,1){=}62$ 最优码** | 两份，可复跑 | `sources/KERI-CD-K_9_1-*` |
| **van Wee 原式 ＋ $n{=}10$ 代入** | $\to103$ | `AUDIT-28q` |
| **$r_q=2t_q$（开邻域）** | 精确恒等式 | `RESULT-f` |
| **$f(j)$ 精确表** | $(6,4,3,3,2,2,2,1,0,\dots)$；$D(v,3,2)=(1,1,2,4,7,8,12)$ | `RESULT-i` |
| **$\sum_p m_p=2E_3(P)$；$m_p=\deg_{G_3(P)}$** | 恒等式 | `RESULT-j` |
| **过剩精确分解** | $\mathrm{Def}(A)=\sum_{N_1(P)}q_x+\sum_{\notin N_1(P)}(q_x-1)_+$ | `RESULT-m` |
| **两来源恒等式** | $\mathrm{Def}=2(A_1+A_2)-T$ | `RESULT-c` |
| **度数集中（经验强规律）** | $n_0{+}n_1{+}n_2{+}n_3\le5$ | `RESULT-j` |
| **P12-PASS** | 距离分布**不能**区分码（支撑层可以） | `P12-PASS-2026-09-27` |
| **$2^m$ 杠杆限制** | 支撑杠杆仅在 $n{=}2^m$（perfect code）成立；$n{=}10$ 不迁移 | `119-ATTACK-R1` |

## §6 唯一剩下的方向（**仅此三条**）

$$\textbf{（甲）}\ \text{Zhang--Lo 1992 \textbf{三重覆盖}不等式之 }r{=}1\ \text{类比}（\text{档案自定下一步}\ \texttt{AUDIT-29d}）\ ——\ \text{原式未取}⚠️$$
$$\textbf{（乙）}\ \text{整性／枚举（Østergård--Blass 型）}\ ——\ \text{已实测}:\ \text{fiber LP/ILP 不足};\ \text{SDP 在 }M{=}106\ \text{剪不动};\ n{=}10\ \text{状态空间爆炸}✗$$
$$\textbf{（丙）}\ \text{一个\ \textbf{新表示层}}（\text{非 }A\ \text{的分解}）\ ——\ \text{经 }15{+}\ \text{次尝试\ \textbf{未找到}}✗$$

## §7 边界（硬 ✓）

- **全部条目皆引档名，可核** ✓；**本档不产生新数学，不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）

## §8 【技术词回查】（**提交前实跑，逐字粘贴**）

```
107线失败地图 : 技术词 107线失败地图 命中文件数=0    ::
反重复清单 : 技术词 反重复清单   命中文件数=0    ::
Aut不变性定理 : 技术词 Aut不变性定理 命中文件数=0    ::
```
