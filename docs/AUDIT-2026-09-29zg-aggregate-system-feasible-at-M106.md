# AUDIT-2026-09-29zg — 聚合系统在 $M{=}106$ 处**可行**：恒等式层无法排除 106

> 空间 B｜非 C 号｜唐先生令（22:21「先复现 107」）后 S1 之第一个决定性读数｜**不主张 107**（V290）
> 时间：2026-09-29 22:3x

**已查地图**：承 `ERRATUM-2026-09-29-n1`（×2 勘误）／`ROUTE-2026-09-29-107-ladder-reassessment`（F1–F8）／`AUDIT-29e`（单条线性 ≤105.2223）
D0: 本档对象 = **档案已有**（归约／恒等式／A_1 界）之**可行性测试**（新数学对象：无 ✗）
D1: 0（产出 = 一个**显式候选解** ⟹ 一条**否定性判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{把全部已用恒等式 ＋ }A_1\le49\ \text{ 放在一起，在 }M{=}106\ \text{处\ \textbf{可行}} \Longrightarrow \text{恒等式/总量层\ \textbf{不能}排除 }106 ✗}$$

## §1 系统与**显式候选解**（可复跑）

变量：$\mu$-剖面 $n_i$（$i{=}1..11$）、码字层 $m_a$（$a_y{=}a$ 之码字数）、$A_1,A_2,P,E$。
约束（全部为档案合法式）：$\Sigma n_i{=}1024$；$\Sigma(i{-}1)n_i{=}\Sigma\delta{=}142$；$\Sigma m_a{=}106$；
$\Sigma a\,m_a{=}2A_1$；$n_{1+a}\ge m_a$；$\Sigma\binom i2 n_i{=}2(A_1{+}A_2)$；$\Sigma\binom i3 n_i{=}P{+}E$；
$P{=}\Sigma_a\binom a2 m_a$；**F5** $P\le2A_2$；档案界 $A_1\le49$。

$$\textbf{候选解}:\quad n_1{=}882,\ n_2{=}142\ (\text{其余 }0);\quad m_0{=}8,\ m_1{=}98;\quad A_1{=}49,\ A_2{=}22,\ P{=}E{=}0$$

**逐条核验（实跑，全部 ✓）**：$\Sigma n_i{=}1024$ ✓｜$\Sigma(i{-}1)n_i{=}142$ ✓｜$\Sigma m_a{=}106$ ✓｜$\Sigma a m_a{=}98{=}2A_1$ ✓｜
$n_2{=}142\ge m_1{=}98$ ✓｜$\Sigma\binom i2 n_i{=}142{=}2(49{+}22)$ ✓｜$\Sigma\binom i3 n_i{=}0{=}P{+}E$ ✓｜
$P{=}0\le44$ ✓｜$A_1{=}49\le49$ ✓｜**F7 取等**：$N_{\le2}{=}71{=}\Sigma\delta/2$ ✓

## §2 该候选解的**结构形状**（⟹ 真正的靶子）

$$\text{（i）}\ \textbf{无任何点被覆盖}\ge3\ \text{次}\ (n_i{=}0,\ i\ge3)\ \Longrightarrow\ \text{距离}\le2\ \text{图}\ G\ \text{无三角形},\ E{=}P{=}0$$
$$\text{（ii）}\ 142\ \text{个共享点全为}\ \mu{=}2\ \Longleftrightarrow\ \text{每条近对之 2 个共点各只属一条边}$$
$$\text{（iii）}\ 71\ \text{条近对} = \underbrace{49}_{\text{距 }1,\ \textbf{完美匹配}}\ +\ \underbrace{22}_{\text{距 }2};\quad \text{98 个码字各恰 1 个距-1 邻；8 个码字孤立}$$
$$\text{（iv）}\ \text{重叠账\ 自洽}:\ 49\times2\ (\text{相邻对之重叠}) + 22\times2 = 142 = \Sigma\delta\ ✓✓$$

## §3 含义

$$\boxed{\text{排除 }M{=}106\ \text{必须用到\ \textbf{几何可实现性}（点-团安排的实现），而非再堆总量恒等式}}$$
$$\text{这与 }AUDIT\text{-}29e\ (\text{单条线性}\le105.2223)\ \text{同族}:\ \textbf{总量/松弛层已饱和}\ ⚠️$$
$$\therefore\ \text{S1 原样（聚合夹逼）}\ \textbf{失败};\ \text{须升级为 S1}^{\prime}:\ \text{在聚合系统上再加\ \textbf{可实现层}}$$

## §4 下一步（S1′）

- **(a)** 求 $A_2$ 之**几何上界**（距离-2 对之 packing 结构），代入 §2 之形状看是否冲突
- **(b)** 给"近对安排"（49 匹配 ＋ 22 距-2 对）以**实现性必要条件**（每点 $x$ 之 $\mu$ 由邻域码字数决定）
- **(c)** 检查 §2 形状是否与 **Q_10 的坐标几何**冲突（如孤立码字/匹配对之覆盖余量）

## §5 边界（硬 ✓）

- **不主张 107／不主张 106 不可排除** ✗；本档只证"**该**聚合系统可行"（＝该路线不足）✓
- 候选解为**聚合层**之解，**不是**码 —— 不声称存在 106-覆盖码 ✗✓
- 未重攻 pair 层（R02）／未取论文原文（R16–17）✓；未碰 RH ✓

ROUTE-CHECK: R01=NA R02=FINGERPRINT-CITED R03=NA R04=NA R05=NA R06=NA R07=NA R08=NA R09=NA R10=NA R11=NA R12=NA R13=NA R14=NA R15=FINGERPRINT-CITED R16=NA R17=NA R18=NA R19=NA R20=NA
