# AUDIT-2026-09-28 — **C-448→C-548 证明链审计：四类分档 ＋ accounting invariant 缺口**

> **性质**：**审计**（非研究轮）——遵唐先生 2026-09-28 20:19 令 ✓「**在找到 invariant 之前，不再继续增加 C 编号**」⟹ 本档**不占 C 号** ✓
> **空间隔离**：空间 B（119 线）✓；**不作路线裁定** ✗

**已查地图**：承 C-548（新链 $P_0\to P_5$）／C-544（$H_k$ 判死）／C-539（excess-shell 无闸门）✓

D0: 本档对象 ＝ **审计**（无新数学对象 ✗）
D1: 0（**本档不产生新数学自由度**；产出＝分档 ＋ 缺口定位 ⚠️）

---

## §0 结论（先给）

$$\boxed{\text{(i) 现有内部结构\ \textbf{丰富}，但\ \textbf{尚未形成 lower-bound mechanism}}}\ ✓\text{（如实承认）}$$
$$\boxed{\text{(ii) D 栏（\textbf{无 accounting interface}）在数量上压倒性最大}}$$
$$\boxed{\text{(iii) 唯一缺件 ＝ \textbf{global accounting map}：local facts}\ \to\ \text{global resource deficit}}$$

**统计佐证（本档实测 ✓）**：C-448→C-548 共 **122** 档中——`恒等式` 39 档／`容量` 48 档／`刚性` 24 档／`闸门` 10 档／`CLOSED` 7 档／`STOP` 4 档。
⟹ **结构/容量/恒等式三样都多，"账本"为零** ✓✓（与唐先生诊断完全吻合）

## §1 根因：三类混淆（**本档立此为审计基准 ✓**）

$$\boxed{\text{结构信息}\ \neq\ \text{独立约束}\ \neq\ \text{可用于下界的量}}$$

| 混淆 | 实例 | 后果 |
|---|---|---|
| 新符号 ⇒ 新信息 | **$H_k$**（C-543→**C-544 判其 ≡ covering 重写**） | 假约束 |
| 局部限制 ⇒ 全局损失 | $A_i{\cap}A_j{=}\varnothing$（C-460 系） | 损失可**重叠** |
| 真命题 ⇒ 有 leverage | 大量 rigidity | 与目标无关 |

## §2 四类分档

### A 栏 — **真正独立的结构事实** ✓（约 12 组）

| 项 | 内容 | 出处 |
|---|---|---|
| A1 | 签名定理：$\forall T{=}\{a,b,c\}$，$\lambda$-签名 $\equiv(1,2,2)$ 之排列；$r_{\rm dist}\equiv4$ | C-489 |
| A2 | $K_{40}{=}H_0\sqcup H_1\sqcup H_2$，$H_1,H_2$ 皆 **8-正则／无三角／160 边**；$|E(H_0)|{=}460$ | C-489 |
| A3 | 闭环恒等：$r_w{\equiv}4$，$r_{\bar y}{\equiv}4$，$r_w{+}r_{\bar y}{\equiv}8{=}d_{H_1}{=}d_{H_2}$ | C-490 |
| A4 | $A_1A_2{=}A_2A_1$ 对易；$A_3{=}\frac12A_1A_2$，$d(H_3){=}32$；$\operatorname{Spec}$ 相同 | C-491 |
| A5 | $n_i(T)\equiv(128,29,2)$ 常数 | C-488 |
| A6 | **对角不相交普适** ＋ 对角重叠 ⇒ owner${\ge}4$ | C-513／**C-514** |
| A7 | $d(w^*,\cdot)$ 多重集 $\equiv(2,2,2,4)$；远元 ＝ 共码字之伙伴 | C-519 |
| A8 | **骨架冻结**：$x$ 对 $d{=}4$／$y$ 对 $d{=}2$／$q$ 全刚性 | C-520/521/522 |
| A9 | $K_3(4)$ 支撑型 $(4,4,2)$ | C-523 |
| A10 | **最小障碍阶 ≡ 4**（1路 4/4，2路 6/6，3路 4/4，**4路 0/1**） | **C-529** |
| A11 | 第四槽障碍 ＝ **点态 owner**（候选全 owner${\ge}4$） | **C-530** |
| A12 | $A_r$ 分类（2 个 D ＋ 余 $D^c$）；邻域覆盖签名两类；**无一邻点被 >1 个 Best owner 覆盖** | C-537 |
| A13 | 中点参数化 ＋ 额外 owner $\iff \operatorname{supp}{=}S{\cup}R$，$R{\in}\binom{D^c}2$ | C-532/533 |

### B 栏 — **covering 的重写**（＝bookkeeping，**降级 ✓**）

| 项 | 内容 | 判定 |
|---|---|---|
| B1 | **$H_k(F)\equiv\sum_{x\in F}\delta(x)\ge0$** | **纯 covering 重写** ✗（C-544） |
| B2 | $k$-子空间覆盖不等式（C-543 之"独立性"主张） | **C-544 已更正** ✗ |
| B3 | $\sigma$-和恒等（$\sum|\sigma|{=}\sum\lambda$） | 恒等 ✗（C-526/527） |
| B4 | $P_3$ 之包含排除分解 | 记账 ✗（C-486） |
| B5 | 三球/三阶矩恒等式族 | 恒等 ✗（`EXCESS-2026-09-25`／C-540） |

### C 栏 — **局部容量界**（保留，但**暂不宣称** global lower bound ✓）

$c{\le}12$、$c{+}d{\le}20$（C-453）；$\max(|F|{+}|G|){\le}22$（C-456）；$c{+}d{+}f{+}g{\le}40$（C-457）；$r{=}0/1/2$ 阶梯 ${\ge}12/{\ge}8/{\ge}8$（C-479/480/481）；$2{\le}\deg(S){\le}3$（C-537）；$|\cap|{\le}9h{+}2q$（C-475）。

### D 栏 — **尚无 accounting interface**（⚠️ **最大栏**）

$$\text{上述 A 栏\ \textbf{除 A10/A11 外全部}、C 栏全部、以及 C-494→C-536 之 profile/orbit/mask/容量余量族}$$
$$\text{——皆回答"若极小码存在，它\ \textbf{长什么样}"，\textbf{不回答}"118 为什么装不下"}}\ ✗✅$$

## §3 leverage test（**制度 ✓**）

$$\boxed{\text{每个 lemma 必须申报}:\ \text{它最多贡献多少\ \textbf{码字损失}？}}$$
$$\text{答不出}\ \Longrightarrow\ \textbf{不许继续堆}\ ✗\quad(\text{即 $P_{2\text{-R}}$ 门之具体化})$$

**本档抽查（$\text{leverage}$ 之粗估）**：

| lemma | 形式 | 粗估 leverage |
|---|---|---|
| C-456 $\max(|F|{+}|G|){\le}22$ | 单胞容量 | ${\sim}1$ 码字/点，且**可重叠** |
| C-537 $\deg(S){\le}3$ | 局部量界 | 未知（无 global 接口） |
| **C-529 障碍阶${\equiv}4$** | 排除型 | **${\sim}4$ 槽**（最接近"损失"语言） |
| **C-530 点态 owner** | 排除型 | **每候选点 1 个**（最可累加） |

$$\Longrightarrow\ \boxed{\text{A10/A11\ \textbf{是唯一两组用"排除/损失"语言说过话的}}}\ ✓\text{——与唐先生"ownership/private coverage"方向一致}$$

## §4 accounting invariant 规格（**缺件之精确定义 ✓**）

$$\mathcal I:=\{(c,x): c\ \text{负责覆盖}\ x\}\ \text{（二部关系）}$$
$$\text{每码字之\ \textbf{不可替代责任}\ } \rho(c):=|\{x:\ x\ \text{仅被}\ c\ \text{覆盖}\}|\ \text{（私有覆盖）}$$
$$\text{总责任}\ R:=\sum_c\rho(c);\quad \text{每字上限}\ r:=\max_c\rho(c)$$
$$\boxed{\text{目标}:\ |C|\le118\ \Longrightarrow\ R>118\,r\ \Longrightarrow\ \Bigl\lceil\frac Rr\Bigr\rceil=119}\ ✓$$

$$\textbf{等价叙述（唐先生原话 ✓）}:\ \text{证明}\ |C|\le118\Rightarrow\boxed{\text{账本亏损}\ge1};\ \text{亏损}\ge1\Rightarrow119$$

**⚠️ 关键**：$\rho$ 必须**不可重复计数**（no double-count）——即不同 $c$ 的私有集**必须互斥**（by definition ✓），这正是它可能通过 $P_{1\text{-I}}$ 门的原因：**私有性不是 covering 的线性重写** ✓

## §5 为何"局部损失$\Rightarrow$全局损失"会失败（**重叠机制 ✓**）

$$\text{设}\ n\ \text{个局部位置各排除 1 个 configuration};\ \text{若其排除集\ \textbf{高度重叠}} \Longrightarrow \text{总损失仍为 }1\ ✗$$
$$\text{本线具体实例}:\ \text{C-515 已证}\ \sum|W|{\le}6\ \textbf{假}（\sum|W|{=}7\ \text{因\ 1 处 overlap 而非 owner}{\ge}4）\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{重叠是常态；accounting 必须显式处理 overlap}}\ ✓$$

## §6 结论：唯一攻击点

$$\boxed{\text{不再找第 4 个 global inequality}}\ ✗\quad(\text{C-546 机制族穷尽 ✓})$$
$$\boxed{\text{唯一攻击点}:\ \text{为 A 栏（尤其 A10/A11）建立\ \textbf{global accounting map}}}\ ✓$$
$$\text{顺序（唐先生 20:19 ✓）}:\ \text{先找 accounting invariant}\to\text{证其独立}\to\text{证其产生\ \textbf{不可累加损失}}\to\text{118 collision}\to119$$

## §7 边界（硬 ✓）

- 审计 ＋ 关键词统计 ＋ 既有档引证 ✓；**无新数学** ✗；**不加 C 号** ✓（遵令）；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §0(ii) 为"**本线档案**"之统计，非全局判断 ✓
