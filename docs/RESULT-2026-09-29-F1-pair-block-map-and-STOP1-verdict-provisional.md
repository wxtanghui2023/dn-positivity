# RESULT-2026-09-29-F1 — F 首个实验（pair-block 映射）＋ STOP#1 判定（**含两处自查缺陷**）

> 空间 B｜非 C 号｜唐先生 23:08 程序「**F-G-H-B**」之第一步｜**不主张任何新值**（V290）
> 时间：2026-09-29 23:5x

**已查地图**：承 `MAP-2026-09-29-M1`（机制空间 A–H）／`AUDIT-zj`（类级标定）／`AUDIT-zl`（开邻域已判非新信息）
D0: 本档对象 = **档案已有**（划分/类型商、覆盖码样本统计）之**组合**（新数学对象：无 ✗）
D1: 0（产出 = **一个映射结构 ＋ 一次 STOP 判定（暂定）** ⚠️✓）

---

## §0 唐先生程序（**逐字固化**）✓

$$\boxed{\textbf{F}\to\textbf{G}\to\textbf{H}\to\textbf{B}}:\quad
\text{F＝换\ \textbf{几何}（非换坐标）}|\ \text{G＝对称性\ \textbf{压缩器}}|\ \text{H＝局部信息\ \textbf{变传播}}|\ \text{B＝最终\ \textbf{反向容量约束}}$$

**四条 STOP 条件（逐字固化，本轮起生效）**：
$$\text{F-STOP}:\ \text{若所有 mixed 关系最终都能写回 }(W,X,H,P_1,P_2)\ \text{的函数} \Longrightarrow \textbf{STOP}$$
$$\text{G-STOP}:\ \text{若 orbit 分类只减少枚举量、未产生新蕴含} \Longrightarrow \textbf{STOP}$$
$$\text{H-STOP}:\ \text{若所有传播链长}\le2\ \text{且无禁形/资源增长} \Longrightarrow \textbf{STOP}$$
$$\text{B-STOP}:\ \text{若只得 }N_T\ge0\ \text{或已有下界、无新容量限制} \Longrightarrow \textbf{STOP}$$
$$\text{（宗旨：}\textbf{任一步不产生真新信息即砍掉，不再"换符号包装"}\text{）}$$

## §1 F 的几何内容（本档实算）

$$\pi:\ Q_2^{10}\to\{0,1,2\}^5,\qquad \text{5 个 block；block 状态 }0{=}00,\ 2{=}11,\ 1{\in}\{01,10\}$$
$$\text{不变量}\ \tau(x){=}(n_0,n_1,n_2)\ (\Sigma n_i{=}5)\ \Longrightarrow\ \binom72{=}\mathbf{21}\ \text{型（G 的压缩器）}$$
$$\text{实算关键结构}:\ \text{单坐标翻转只影响\ \textbf{一个} block，且类型转移恰为}\ 0\!\to\!1,\ 2\!\to\!1,\ 1\!\to\!0,\ 1\!\to\!2$$
$$\Longrightarrow\ \boxed{E_x=\varnothing\ (\textbf{无例外})}:\ \text{邻域像＝"一个 block 类型变化"之集合 ⟹ 结构纯净（便于 H 传播）}\ ✓$$
$$\text{（注意：}\pi\ \text{为有损映射；其 fiber 语言＝档案 }R05\ \text{已判"精确重述"}\ \therefore\ \text{价值不在 fiber，而在\ \textbf{局部类型商}\ ⚠️）}$$

## §2 STOP#1 判定（实跑，**暂定**）

**样本**：45 例覆盖码（120-码 ＋ 24"扰动" ＋ 20 贪心，规模 120–153）
**旧特征**（6）：$M,\ A_1,\ A_2,\ A_3,\ \Sigma\binom\mu3,\ \#\mathrm{priv}$；**新特征**（5）：$T_k{:=}\Sigma_{\pi(x)\text{之不等 block 数}=k}\mu(x)$

| 新特征 | $R^2$ | 最大相对残差 | 判定 |
|---|---|---|---|
| $T_0$ | 0.8634 | 0.158 | 新信息候选 |
| $T_1$ | 0.9180 | 0.119 | 新信息候选 |
| $T_2$ | 0.9809 | 0.042 | 新信息候选 |
| $T_3$ | 0.9687 | 0.069 | 新信息候选 |
| $T_4$ | 0.9470 | 0.121 | 新信息候选 |

$$\Longrightarrow\ \text{形式判定}:\ \textbf{STOP#1 未触发}\ \checkmark\ (\text{存在残差})$$

## §3 ⚠️ 两处**自查缺陷**（不得当作放行证据）

1. **样本多样性不足** ✗：所谓 24 个"扰动"**与基准码特征逐项相同** —— 因 120-码**极小**（单删即失覆盖），"加词后贪心剪冗余"会**回到原码** ⟹ 有效样本实为 **21 个**（1 ＋ 20 贪心），且贪心族挤在 $M{\in}[146,153]$
2. **检验过弱** ✗：本检验只测**线性**可解释性；"能写回旧量之**函数**"（F-STOP 原文）应为**函数依赖**，线性无关≠函数无关 ⟹ 残差存在**不足以**排除"实为旧量的非线性函数"

$$\therefore\ \boxed{\text{结论暂定}:\ F/G\ \textbf{未 STOP，但亦未获放行}};\ \text{须先补（i）真多样样本（ii）函数依赖检验/或直接测 H 之蕴含} \ ⚠️✓$$

## §4 下一步（**具体、可执行**）

- **(i)** 样本：多随机种子贪心 ＋ 定向构造出的 $M{\in}[120,146]$ 码（如上界侧 119-搜索的中间产物）＋ **n=9 控制组**（真值 62，可判定检验灵敏度）
- **(ii)** 把检验从"线性残差"升级为 **H 型蕴含测试**：对 21 个类型对 $(τ,τ')$，在所有样本上统计 $\text{cov}(τ)\Rightarrow\text{cov}(τ')$ 是否为**必然**（零反例），零反例者即为**候选局部规则**（喂给 H 做传播）
- **(iii)** 若 (ii) 得到零反例规则但传播链 $\le2$ 或无资源增长 ⟹ 按 **H-STOP** 砍掉

## §5 边界（硬 ✓）

- **不主张** 107／任何新值 ✗；本档为**程序第一步 ＋ 暂定判定**；两处自查缺陷**公开记录** ✓
- 未取论文原文（R16–17）／未重攻 pair（R02）／fiber（R05）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=FINGERPRINT-CITED R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
