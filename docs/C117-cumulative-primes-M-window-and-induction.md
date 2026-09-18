已查地图（所查：`C-97`（素数间隙记忆：硬记忆＝可容许性；残类反重复（LS 2016）；自相关 `−0.036@40σ`；奇异级数偏差）、`C-98`（零点关联 ＋ **归纳审计三条理由**；`V259` 判死）、`V254`／`V255`（**parity barrier**：非横坐标陈述而是**类型失配**；系数侧→零侧转换唯一已知＝密度链）、`V252`（`1/(a\log a)=∫a^{-s}ds` ⟹ Erdős 型和住 `σ=1` 层 ⟹ **零 `β` 分辨力**）、`CLOSED-ROUTES-MAP:16`（计数／熵箱含 **Euclid–Mullin**／Lyapunov／转移算子）、`W6`／`SUPPORT-1`（原子墙：`support>1 ⟺` prime-pair）、`Maynard–Tao`（admissible tuple 框架；分布水平 `θ`）、`V191`（GORZ Jensen 梯剩余 ≡ RH）、`C-116`（**门／警示清单**：归纳模式不得获得否决权））。**结论**：唐先生 17:05 两提案**均有规范形式**——**提案 1**（每个素数↔此前**全部**素数）＝**Legendre／Meissel 累积筛递推**（精确恒等式）＋其成功版本＝**Selberg 双线性恒等式**（只达 `σ=1` 层 ⟹ PNT 级）；**提案 2**（`M` 个素数之间的关联）＝**admissible `M`-tuple ＝ Maynard–Tao 框架**，无条件可达性由**分布水平 `θ`** 控制 ⟹ 阻塞＝**`SUPPORT-1`**（本会话的原子墙）✓✓；**且本档实测给出新事实**：`M` 窗口记忆的**主结构＝纯跨度律** `log(O/P)≈\text{const}-span/\log x`（**本档给出初等推导**），**`M`-无关**（`M=3`／`M=4` 同斜率）✓✓，并**双数据点验证**（`N=2×10^7`：实测 `0.061`／`0.062` vs 预测 `0.0595`；`N=10^8`：实测 `0.0531` vs 预测 `0.0543`，吻合 `2\text{–}4\%`）✓✓；**残留**＝同跨度内的**形状效应 `~4\text{–}6\%`**（高于 Poisson 噪声，且奇异级数截断误差可忽略 ⟹ **非截断伪影**）⟹ **这是唯一可能藏"新关联"的地方** ✓

# C-117 · **累积联系 ＋ `M` 重窗口 ＋ 归纳：规范形式、阻塞位置与本档实测**

> **时间**：2026-09-18 17:05 唐先生：**① 每个素数和它之前所有素数的关联（不是单点，而是之前的所有）；② 或者看 `M` 个素数之间的数字是否构成记忆和关联；目前机制下看不到突破点，只有通过联系性看看能不能用归纳法** ✓
> ⚠️ **本档遵守 `C-116` 纪律**：阻塞**登记为已注册事实**，**不作自动否决**（`F1`–`F8` ＋ 检验床仍是唯一前置门）✓

---

## §0 结论（先行）

$$\textbf{提案 1（每个素数}\leftrightarrow\textbf{此前全部素数）的规范形式}＝\textbf{Legendre／Meissel 累积筛递推}：✓$$
$$\qquad \pi(x)=x-\sum_{p\le x}\Bigl\lfloor\frac xp\Bigr\rfloor+\sum_{p<q\le x}\Bigl\lfloor\frac x{pq}\Bigr\rfloor-\cdots \Longrightarrow \textbf{精确}，\ \text{且}\ \textbf{确用全部素数}✓$$
$$\qquad \text{其}\ \textbf{截断障碍}＝\text{parity barrier}（\text{`V254`／`V255`}）;\ \text{其}\ \textbf{成功版本}＝\text{Selberg 双线性恒等式} \Longrightarrow \text{PNT}，\ \text{但只到}\ \sigma=1\ \text{层（`V252`）}✓$$
$$\qquad ⚠️\ \text{而"乘积记忆"递归（}\prod_{q<p}q\text{）的最近实例＝}\textbf{Euclid--Mullin}：\text{它}\ \textbf{不生成素数序列}（\text{倍指数增长}） \Longrightarrow \textbf{累积乘积记忆不足以复现素数}✓✓$$
$$\textbf{提案 2（}M\ \text{个素数之间的关联）的规范形式}＝\textbf{admissible }M\text{-tuple}＝\text{Maynard--Tao}✓$$
$$\qquad \text{无条件可达性由}\ \textbf{分布水平}\ \theta\ \text{控制} \Longrightarrow \text{阻塞}＝\text{`SUPPORT-1`}（\text{`W6`，本会话原子墙}）✓✓$$
$$\textbf{本档实测（新）}：M\ \text{窗口记忆的}\ \textbf{主结构}＝\textbf{纯跨度律}：\log(O/P)\approx\text{const}-\dfrac{span}{\log x}✓✓$$
$$\qquad \textbf{初等推导（本档）}：\text{跨度} s\ \text{含}\ s/2\ \text{个偶中间数}，\ \text{每个素数密度}\ \approx 2/\log x \Longrightarrow (1-2/\log x)^{s/2}\approx e^{-s/\log x}✓✓$$
$$\qquad ⭐\ \textbf{`M`-无关性}：M=3\ \text{与}\ M=4\ \text{同}\ x\ \text{下}\ \textbf{斜率相同}（0.061\ \text{vs}\ 0.062） \Longrightarrow \text{效应}\ \textbf{只依赖跨度}✓✓$$
$$\textbf{残留}：\text{同跨度内}\ \textbf{形状效应}\ \sim4\text{–}6\%（\text{高于 Poisson 噪声};\ \text{截断误差可忽略}） \Longrightarrow \boxed{\text{唯一可能藏"新关联"处}}✓$$

---

## §1 提案 1 的规范形式与阻塞

$$\textbf{(a) 递推形式}：\text{Legendre／Meissel：}\pi(x)=x-\sum_p\lfloor x/p\rfloor+\sum_{p<q}\lfloor x/pq\rfloor-\cdots✓$$
$$\qquad \text{这是}\ \textbf{精确恒等式}，\ \text{且}\ \textbf{恰是"每个素数关联此前全部素数"的规范化}✓$$
$$\qquad \Longrightarrow\ \text{其}\ \textbf{截断（任何固定层数）的误差与主项同阶} \Longrightarrow \text{parity barrier}（\text{`V254`／`V255` 已注册}）✓$$
$$\textbf{(b) 成功形式}：\text{Selberg：}\sum_{p\le x}\log^2p+\sum_{pq\le x}\log p\log q=2x\log x+O(x)✓$$
$$\qquad \Longrightarrow \text{PNT（初等）}，\ \text{但}\ \text{`V252`}：\text{Erdős 型和住}\ \sigma=1\ \text{层} \Longrightarrow \textbf{零}\ \beta\ \text{分辨力}✓$$
$$\qquad \text{即：}\ \textbf{累积双线性}\ \text{版本}\ \textbf{确实有效}，\ \text{但只到}\ \textbf{PNT 强度}✓$$
$$\textbf{(c) "乘积记忆"的反证}：\text{若递归用}\ \prod_{q<p}q \Longrightarrow \text{Euclid--Mullin：}\ \text{倍指数增长}，\ \text{且}\ \textbf{未知是否含全部素数}✓$$
$$\qquad \Longrightarrow \text{累积乘积的}\ \textbf{信息分辨力}\ \text{远粗于素数本身（}\log\prod\approx p \gg \log p\text{）} \Longrightarrow \textbf{不足以复现素数}✓✓$$
$$\qquad ⚠️\ \text{（`CLOSED-ROUTES-MAP:16` 中 Euclid--Mullin 仅登记于计数／熵箱，}\textbf{未作此判定}）\Longrightarrow \text{本档补充登记}✓$$

## §2 提案 2 的规范形式与阻塞

$$\textbf{admissible }M\text{-tuple}：\mathcal D=\{0,h_1,\dots,h_M\}，\ \text{避开零 residue（所有素数）}✓$$
$$\qquad \Longrightarrow \text{GPY／Maynard--Tao：}\ \text{无条件结果由}\ \textbf{分布水平}\ \theta\ \text{（}\sum_{n\le x}\Lambda(n)\Lambda(n+h)\ \text{类）控制}✓$$
$$\qquad \Longrightarrow \boxed{\text{其墙}＝\text{`SUPPORT-1`}（\theta>1/2;\ \text{`W6` 原子墙：support>1}\iff\text{prime-pair}\iff\text{无条件三阶矩）}}✓✓$$
$$\qquad \text{即：}\ \textbf{"}M\ \text{个素数之间的关联"在}\ \textbf{最锐的已知形式} \text{下}\ \textbf{就是} \text{这张墙的主题}✓✓$$

## §3 本档实测：`M` 窗口记忆的主结构与 `M`-无关性

$$\text{数据}：N=2\times10^7（1{,}270{,}607\ \text{素数}）;\ N=10^8（5{,}761{,}455\ \text{素数}）✓$$
$$\text{方法}：\text{枚举连续间隙型}\ (g_1,\dots,g_M)，\ \text{算 HL 奇异级数}\ S(\mathcal D)\ \text{（截断}\ p\le10^5）;\ \text{单参数全局归一化}✓$$
$$\text{统计量}：\log(O/P)，\ O＝\text{实测计数}，\ P＝C\cdot S(\mathcal D)✓$$

| `x` | `M` | 型数 | `corr(log(O/P), span)` | 实测斜率 | `−1/log x` | 差 |
|:--|:--|--:|--:|--:|--:|--:|
| `2×10⁷` | `3` | 420 | **−0.9800** | −0.061 | −0.0595 | 2.5% |
| `2×10⁷` | `4` | 496 | **−0.9214** | −0.062 | −0.0595 | 4.2% |
| `10⁸` | `3` | 552 | **−0.9862** | −0.0531 | −0.0543 | 2.2% |

$$\Longrightarrow\ \text{主结构}＝\textbf{纯跨度律}，\ \text{且}\ \textbf{两数据点吻合}\ 1/\log x\ \text{预测}（2\text{–}4\%）✓✓$$
$$\textbf{初等推导（本档）}：\text{跨度}\ s\ \text{的型，其}\ s/2\ \text{个偶中间数必须}\ \textbf{皆非素数}✓$$
$$\qquad \Longrightarrow\ \text{概率}\approx(1-2/\log x)^{s/2}\approx e^{-s/\log x} \Longrightarrow \textbf{斜率}＝-1/\log x✓✓$$
$$\qquad \Longrightarrow\ \text{故该律}\ \textbf{不是新物理}，\ \text{而是}\ \textbf{归一化效应};\ \text{但它}\ \textbf{关闭了一条想象}：M\ \text{窗口记忆}\ \textbf{主结构无}\ M\ \text{依赖}✓✓$$

## §4 残留（唯一可能藏"新关联"处）

$$\text{同跨度内}\ \log(O/P)\ \text{的}\ \textbf{离散}：\text{std}\approx0.04\text{–}0.06（N=2\times10^7，\text{偏大跨度}）✓$$
$$\qquad \text{排查}：\text{(i) Poisson 噪声}\approx1\text{–}3\% \Longrightarrow \text{实测}\ \textbf{高于} \text{噪声};\ \text{(ii) 奇异级数截断}\ p\le10^5：✓$$
$$\qquad \qquad \text{对}\ p>span\ \text{有}\ \log\text{factor}=-k(k-1)/(2p^2)+O(p^{-3}) \Longrightarrow \sum_{p>10^5}\approx\frac{k(k-1)/2}{10^5\log10^5}\sim5\times10^{-6} \Longrightarrow \textbf{可忽略}✓✓$$
$$\qquad \Longrightarrow \text{故残留}\ \textbf{不是} \text{截断伪影} \Longrightarrow \boxed{\text{存在}\ \textbf{小的、系统性的形状依赖}（\sim4\text{–}6\%）}✓$$
$$\qquad \text{候选解释（均}\ \textbf{未判明}）：\text{二阶奇异级数效应}／\text{归一化残余}／\text{真实高阶关联}✓$$
$$\qquad \Longrightarrow \textbf{下一步（cheap）}：\text{(a) 换归一化（不用单参数全局拟合，改用}\ \text{Gallagher}\ \text{型逐跨度预测）};\ \text{(b) 加}\ N\ \text{到}\ 10^9\ \text{看残留是否}\ \textbf{衰减}✓$$

## §5 归纳法：为什么在此用不上（且本档实测**支持**该判断）

$$\text{`C-98` 三条理由（仍成立）}：\text{(1) 归纳步需把}\ \gamma_n\ \text{与}\ \gamma_{n+1}\ \text{相连的算术内容，而零点}\ \textbf{不是递归定义};\ \text{唯一已知联系＝显式公式（饱和）}✓$$
$$\qquad \text{(2) 唯一"一}\Rightarrow\textbf{多"步（`ISO`）两个输入均已判循环}（\text{`C-62`／`C-63`}）;\ \text{(3) GORZ Jensen 梯虽是归纳型，但其余项}\ \equiv\ \text{RH}（\text{`V191`}）✓$$
$$\textbf{本档实测的补充支持}：\text{若}\ M\ \text{窗口存在}\ \textbf{真递推结构}，\text{应见}\ \textbf{M 依赖}（\text{阶数越高越强}）✓$$
$$\qquad \text{实测：}\textbf{M-无关}（\text{同一}\ x\ \text{下}\ M=3\ \text{与}\ M=4\ \text{斜率相同}） \Longrightarrow \text{与"无新递推"}\ \textbf{一致}✓✓$$
$$\qquad ⚠️\ \text{但这是}\ \textbf{证据}，\ \textbf{非定理};\ \text{按}\ \text{`C-116`}：\textbf{不得} \text{据此自动否决"M 窗口"方向}✓$$

## §6 边界（`C-116` 纪律）

- ⚠️ **阻塞登记而非否决**：§1／§2 的 parity 与 `SUPPORT-1` 是**已注册事实**；本档**不**因其判死提案 1／2 ✓
- ⚠️ §3 的跨度律为**实测＋初等推导**（**本档**）；§4 残留**未判明**（不得写成"无高阶关联"）✓
- ⚠️ §5 的"实测支持无递推"是**证据级**，非定理 ✓
- **不声称**：`M` 窗口方向已死 ✗；不证 RH ✗
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；**未用 RH 作推导** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 17:1x）`[纪律]`（先跑后写）

```
技术词 纯跨度律        命中文件数=1  :: ./C117-cumulative-primes-M-window-and-induction.md
技术词 M-无关性        命中文件数=1  :: ./C117-cumulative-primes-M-window-and-induction.md
技术词 累积乘积记忆      命中文件数=1  :: ./C117-cumulative-primes-M-window-and-induction.md
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增措辞** ✓
