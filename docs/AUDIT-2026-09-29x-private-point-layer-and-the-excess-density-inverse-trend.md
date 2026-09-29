# AUDIT-2026-09-29x — **private 点层：状态已定义正确，但\ \textbf{无强制 excess}；且发现\ \textbf{excess 密度逆趋势}（一切"强制"论证的结构性障碍）**

> **性质**：**纠偏接受 ＋ 实测判定 ＋ 结构性障碍定位**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 12:2x ✓
> **唐先生令**：①纠偏（cell/Walsh ＝ Habsieger，非新机制）；②P1 锁定 private-point／unique-owner 二阶局部状态 ✓

**已查地图**：`AUDIT-29w`（cell/Walsh 天花板）／`29k`（趋势）／`29t`（Zhang 覆盖设计）✓

D0: 本档对象 ＝ **档案已有**（$\delta$／private 点／$\mu$——无新数学对象 ✓）
D1: 0（产出＝**一处纠偏之接受 ＋ 两处计数纠错 ＋ 一处否定性实测 ＋ 一处结构性障碍** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 接受纠偏}:\ \text{cell／Walsh 路线}＝\text{Habsieger 特征函数／子空间路线},\ \textbf{非新机制}}$$
$$\boxed{\text{② ✓ 新硬界（净得）}:\ M{=}106\ \Longrightarrow\ \textbf{private 点}\ \ge\ \mathbf{776}\quad(\text{等价 }P_2\le142)}$$
$$\boxed{\text{③ ✗ 计数纠错}:\ \text{被强制之点}＝\mathbf{36}\ (\text{非 }9)\ ——\ \text{含 }k\ \text{的 }9\ \text{点被 }c\ \text{覆盖}}$$
$$\boxed{\text{④ ✗✗ 实测判定}:\ \textbf{无强制 excess}:\ 740/746\ \text{个 private 点存在 }\delta{=}0\ \text{之 coverer}}$$
$$\boxed{\text{⑤ ★ 结构性障碍}:\ \text{excess 密度}\ \frac{E}{1024-M}\ \text{随 }M\ \textbf{递减}（M{=}120{:}0.327\to M{=}106{:}0.155）\Longrightarrow \text{一切"强制 excess"论证}\ \textbf{逆势}}$$

## §1 ① 接受纠偏（**✓**）

$$\text{cell／Walsh 之 }\ S_T=\widehat{1_C}(T)\ \text{＋ 固定子空间 codeword 数}＝\text{Habsieger 之特征函数线性不等式}✓$$
$$\text{且}\ n\equiv4\bmod6\ \text{时 Habsieger 1995/97 已达 }104;\ \text{Zhang 达 }105;\ \text{BÖW 2004 达 }107\ ✓$$
$$\therefore\ \boxed{\text{该线\ \textbf{不构成新机制}}，不应再计为新 P1}$$

## §2 ② private 点之硬界（**✓ 新、干净**）

$$S(x)=\delta(x)=\mu(x)-1;\qquad x\notin C,\ \delta(x)=0\iff \mu(x)=1\ (\text{唯一 owner})✓$$
$$\Sigma_{x\notin C}(\mu(x)-1)=E_{\rm out}\le E=142\ \Longrightarrow\ P_2:=\#\{x\notin C:\mu\ge2\}\le142$$
$$\#\{x\notin C\}=1024-M=918\ \Longrightarrow\ \boxed{P_1=\#\{\mu=1\}\ \ge\ 918-142=\mathbf{776}}✓$$

## §3 ③ 计数纠错（**✗ 应为 36**）

$$x\notin C,\ \mu(x)=1,\ \text{owner }c=x\oplus e_k;\quad S_2(x)\ (45\ \text{点}):$$
$$\text{含 }k\ \text{者 }9\ \text{点}\ (\text{距 }c{=}1,\ \textbf{被 }c\ \text{覆盖})\ \big|\ \text{不含 }k\ \text{者 }\mathbf{36}\ \text{点}\ (\text{距 }c{=}3,\ \textbf{c 覆盖不到})$$
$$\therefore\ \text{被\ \textbf{强制}接管的}＝\mathbf{36}\ \text{点}✗\ (\text{非你写的 }9)$$

## §4 ④ 实测判定（**✗✗ 无强制 excess**）

$$\text{120-code}:\ \text{private 点 }746\ \text{个};\ \text{每个之 }36\ \text{强制点由 }12{-}19\ \text{个其它码字覆盖（均值 }14.4）$$
| $(\#\text{coverers},\min\delta,\max\delta)$ | 频数 |
|---|---|
| $(15,0,3)$ | $214$ |
| $(15,0,2)$ | $183$ |
| $(13,0,2)$ | $97$ |
| $(14,0,2)$ | $72$ |

$$\therefore\ \min\delta_{\rm coverer}=\mathbf{0}\ \text{者}\ \mathbf{740/746}\colon\ \textbf{零-excess 服务可实现} \Longrightarrow\ \text{该层\ \textbf{不强制}额外 excess}✗✗$$

## §5 ★⑤ 结构性障碍（**本档最重要**）

$$\text{唯一可推之"最锐目标"（由 }P_2\le E_{\rm out}\ \text{与 }P_1\ge776）：\ \text{若可证}\ \frac{P_2}{\#\{x\notin C\}}>\frac{142}{918}=0.1547\ \text{即得 }107$$
| 码 | $M$ | $P_2/\#$非码字 |
|---|---|---|
| 120-code | $120$ | $\mathbf{0.1748}$ |
| greedy2 | $148$ | $0.4235$ |
| greedy0 | $152$ | $0.4484$ |

$$\therefore\ \text{该比值随 }M\ \textbf{递减};\ \text{外推至 }M{=}106\ \text{约 }0.05{-}0.15\ \textbf{低于门槛}\ 0.1547 \Longrightarrow \textbf{目标落空}✗$$
$$\text{（同型：}E/(1024-M):\ M{=}120\Rightarrow0.327,\ M{=}106\Rightarrow0.155\ \textbf{递减}）$$
$$\therefore\ \boxed{\text{一切"强制 excess"论证皆\ \textbf{逆势}:\ 越小的 }M\ \text{越\ \textbf{没有} excess 可用}}✓✓$$
$$\text{（这解释了本会话为何"六族 ＋ fiber ＋ cell ＋ private"全部止步—— 它们的共同燃料\ \textbf{excess}\ 恰在我们需要的方向上最少）}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "private点" "无强制excess" "excess密度逆趋势"
技术词 private点     命中文件数=0    ::
技术词 无强制excess   命中文件数=0    ::
技术词 excess密度逆趋势 命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **120-code 全量 ＋ 三 greedy 码实测** ✓；**不占 C 号** ✓；**不作方向性决策** ✗
- 趋势外推系**启发式**（无 $M<120$ 之码）⚠️；**不主张** $107$ 不可达 ✗（V290）
