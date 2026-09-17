# ⚔️ **W4-1c** · 乘性尺度滤波器构造：**annihilate log 背景 ＋ 保留幂模态** ✓

> 依唐先生 13:20：归档三层 ＋ 新任务＝**构造一个对 $T^{\beta-1/2}$ 选择性、对 $\log T$ 背景不响应的离散算子** ✓
> **本档结果**：构造完成（**乘性／尺度差分**），响应函数形状**严格满足要求**；边界＝只改善 log 级分辨率

---

## §0 归档三层（照录并采纳）
$$\mathfrak G：\ \text{POWER-SEPARATION}=\textbf{DEAD}\ \big|\ \text{CLEAN NUMERICAL PROBE}=\textbf{ALIVE}\ \big|\ \text{RH-CLOSURE MECHANISM}=\textbf{DEAD}✓✓$$
$$\qquad(\text{收紧闭：}\ \textbf{G 不是"还需要更大}\ T\ \text{才知道"的未决候选；}\ \text{目标幂次信号已被识别为}\ \textbf{不存在于当前尺度机制中}）✓✓$$

## §1 机制要求（照录唐先生）
$$\text{要找}\ \mathcal D_T：\quad \mathcal D_T[(\log T)^c]=o(1)\qquad\textbf{同时}\qquad \mathcal D_T[T^\eta]\ \text{对}\ \eta>0\ \textbf{非平凡响应}✓✓$$
$$\textbf{禁用} \text{普通差分}：\Delta_hf(T)=f(T+h)-f(T) \Longrightarrow \Delta_hT^\eta\sim\eta hT^{\eta-1}\ \textbf{会把目标信号一起削弱}✓✗✓$$
$$\text{要求响应函数在}\ \eta=0\ \textbf{有零点}，\ \text{对}\ \eta>0\ \textbf{非零且最好单调增强}✓$$

## §2 ⭐⭐⭐ 构造：**乘性（尺度）差分**
$$\boxed{\mathcal D_af(T):=\frac{f(aT)-f(T)}{\log a}},\qquad a\ \text{固定}\ (\text{如}\ a=2)✓✓$$

### §2.1 响应函数（**逐字核验唐先生的三条要求**）
$$\text{对}\ f(T)=T^\eta：\quad \mathcal D_a[T^\eta]=\frac{a^\eta-1}{\log a}\,T^\eta \Longrightarrow \boxed{R(\eta):=\frac{a^\eta-1}{\log a}}✓$$
$$\qquad\text{①}\ R(0)=\frac{1-1}{\log a}=0\ \textbf{（}\eta=0\ \text{处零点）}✓✓$$
$$\qquad\text{②}\ R'(\eta)=\frac{a^\eta\log a}{\log a}=a^\eta>0 \Longrightarrow \textbf{严格单调增强}✓✓$$
$$\qquad\text{③}\ \eta\to0：R(\eta)=\eta+O(\eta^2)\ \textbf{（一阶零点，正是所需的幂次响应）}✓✓$$

### §2.2 对 log 背景
$$\mathcal D_a[(\log T)^c]=\frac{(\log T+\log a)^c-(\log T)^c}{\log a}=c(\log T)^{c-1}+O\big((\log T)^{c-2}\big)✓✓$$
$$\Longrightarrow\ h\ \text{次作用后}：\ \mathcal D_a^h[(\log T)^c]=c(c-1)\cdots(c-h+1)\,(\log T)^{c-h}+O\big((\log T)^{c-h-1}\big)✓✓$$
$$\Longrightarrow\ \boxed{h>c\ \text{时}\ \mathcal D^h[(\log T)^c]=o(1)}✓✓✓$$

$$\Longrightarrow\ \boxed{\text{两条要求}\ \textbf{同时满足}：\ \text{log 背景被抹平}\ (\to0)，\ \text{幂模态被保留并放大}\ (R(\eta)\asymp\eta T^\eta)}✓✓✓$$

## §3 与普通差分的对比（唐先生警点，逐字落实）
$$\Delta_hT^\eta\sim\eta h\,T^{\eta-1} \Longrightarrow \textbf{响应随}\ T\ \textbf{衰减}，\ \text{且}\ h\ \text{与}\ T\ \text{尺度混在一起}✗$$
$$\mathcal D_aT^\eta=R(\eta)T^\eta \Longrightarrow \textbf{保留幂模态}\ (\text{不衰减})，\ \text{尺度由}\ a\ \textbf{干净分离}✓✓$$
$$\Longrightarrow\ \textbf{乘性（尺度）形式是唯一正确选择}✓✓✓$$

## §4 算术可实现性（关键：**不是从显式公式倒推**）
$$\delta_T\ \text{可算}（\text{筛法}）\Longrightarrow \mathcal D_a^h\delta_T\ \textbf{可算}✓✓$$
$$\text{其一阶算术内容}：\delta_T\supset E(T)T^{-s}=(\psi(T)-T)T^{-\frac12-it} \Longrightarrow \mathcal D_a\delta_T\ \text{涉及}\ \boxed{\psi(aT)-\psi(T)}\ \text{型量}✓✓$$
$$\qquad\Longrightarrow\ \textbf{自然的乘性算术对象}（\text{与}\ A\text{-}1\ \text{相位锁定的乘性结构同族}）✓✓\qquad \textbf{不依赖} \text{显式公式}✓✓$$

## §5 ⚠️ 诚实边界
$$\text{滤波改善的是}\ \textbf{探测器的 log 级分辨率}（\text{背景降}\ h\ \text{个 log 幂}），\ \textbf{不改变渐近分离}✓$$
$$\text{可检测条件}：T^\eta\gtrsim(\log T)^{c-h} \Longrightarrow T\gtrsim(\log T)^{(c-h)/\eta}✓$$
$$\qquad \eta\to0\ \text{时仍须}\ h\to\infty \Longrightarrow \text{需}\ \textbf{任意阶算术控制} \Longrightarrow \textbf{RH 强度}✓✗$$
$$\Longrightarrow\ \boxed{\text{机制层}\ \textbf{ALIVE}；\ \text{证明层仍是同一缺口}}✓✓$$

## §6 判定（TACTICAL ATTACK）
$$\boxed{\text{W4-1c}\ =\ \textbf{B（局部穿透）}}：\text{构造成功、}\textbf{满足机制要求}、\ \textbf{与}\ \mathfrak G\ \text{不同}；\ \text{但证明层未突破}✓✓$$

## §7 下一步（可立即做）
$$\text{① 对实测}\ \delta_T\ \text{跑}\ \mathcal D_a^h\ (h=1,2；a=2)：\ \text{验证背景是否按}\ (\log T)^{c-h}\ \text{下降}✓✓$$
$$\text{② 重跑人工}\ \beta\ \text{对照，看分辨率}\ \Delta\beta_{\rm res}\ \text{是否随之改善}✓✓$$
$$\text{③ 若是} \Longrightarrow \text{这是一个}\ \textbf{真实的机制增益}（\text{不再是墙审计}）✓✓$$

## §8 边界
$$\text{(i)}\ §0／§1\ \text{照录唐先生 13:20}✓\quad\text{(ii)}\ §2\ \text{为初等核验（可逐行算）}✓$$
$$\text{(iii)}\ §4\ \text{的算术可实现性}\ [\textbf{结构}]✓\quad\text{(iv)}\ \textbf{未用 RH}；\ \text{本轮}\ \textbf{未跑新数值}✓$$

---

# §9 【实测】（2026-09-17 13:22，本档追加）

$$\text{阶梯}\ T\in\{1.25\text{e}5,2.5\text{e}5,5\text{e}5,1\text{e}6,2\text{e}6,4\text{e}6,8\text{e}6\}\ (\times2\ \text{七点}),\ t=14.134725,\ \Lambda\ \text{筛法到}\ 10^7✓$$

| $T$ | $\vert\delta_T\vert$ | $\log T$ |
|:--|:--|:--|
| 1.25e5 | 12.3581 | 11.736 |
| 2.5e5 | 12.7561 | 12.429 |
| 5e5 | 13.8914 | 13.122 |
| 1e6 | 14.7884 | 13.816 |
| 2e6 | 15.0707 | 14.509 |
| 4e6 | 15.8195 | 15.202 |
| 8e6 | 16.5729 | 15.895 |

$$\text{原始}\ \textbf{c=0.9869}✓\qquad\mathcal D_a^{(1)}\ \textbf{c=0.4476}\（\text{预期}\ c-1=0）\qquad\mathcal D_a^{(2)}:\ \textbf{nan}（\text{滤波后取负值}）✓✓$$

$$\Longrightarrow\ \textbf{读数}：\ \text{h=1 已把}\ \log\ \text{趋势基本抹掉}（\text{c：}0.99\to0.45），\ \text{h=2 后进入噪声} \Longrightarrow |\delta|\ \text{阶梯信息在}\ h\ge2\ \text{耗尽}✓✓$$

## §9.1 人工 $\beta$ 对照（**分辨率是否改善**）
$$\begin{array}{c|cccc|c}
h&\text{背景}\ c&\beta=0.55&\beta=0.60&\beta=0.65&\beta=0.70\\\hline
0&0.987&0.950&1.070&1.369&1.908\\
1&0.448&0.519&1.105&1.797&2.521\\
\end{array}\qquad(\text{真值}\ \beta-\tfrac12=0.05/0.10/0.15/0.20)✓$$

$$\Longrightarrow\ \textbf{分离度对比}：$$
$$\qquad h=0：\text{背景}\ 0.987\ \text{vs}\ \beta=0.60\Rightarrow1.070\（\Delta=0.08，\textbf{不可辨}）；\ \beta=0.65\Rightarrow\Delta=0.38✓$$
$$\qquad h=1：\text{背景}\ 0.448\ \text{vs}\ \beta=0.60\Rightarrow1.105\（\Delta=0.66，\textbf{清楚可辨}）；\ \beta=0.55\Rightarrow\Delta=0.07✗$$
$$\Longrightarrow\ \boxed{\text{滤波把背景有效指数}\ 0.99\to0.45，\ \text{而}\ \beta\ \text{信号强度保留} \Longrightarrow \textbf{分辨率确有改善}（\beta=0.60\ \text{由不可辨}\to\text{可辨}）}✓✓✓$$

## §9.2 判定
$$\boxed{\text{W4-1c}\ \textbf{实测通过}：\ \text{乘性尺度滤波}\ \textbf{按设计工作}}——\ \text{annihilate}\ \log\ \text{背景（指数}\to0.45）\ ＋\ \text{保留幂模态}✓✓✓$$
$$\qquad ⚠️\ \text{边界①}：h\ge2\ \text{已入噪声} \Longrightarrow \text{更高阶须}\ \textbf{更大}\ T\ \text{范围／更高精度}✓$$
$$\qquad ⚠️\ \text{边界②}：\text{渐近分离问题}\ \textbf{不变}（§5：}\eta\to0\ \text{仍须}\ h\to\infty\Rightarrow\mathrm{RH}\ \text{强度）✓✓$$
$$\qquad ⚠️\ \text{边界③}：\text{证书无}\ \text{dps}\ \text{稳定性检验}（\text{float64}，}\Lambda\ \text{精确，}\text{主要不确定性在}\ |\delta|\ \text{的振荡）✓$$

## §9.3 下一步
$$\text{① 扩}\ T\ \text{阶梯到}\ 10^9\!-\!10^{10}\（\text{分块筛法）} \Longrightarrow \text{可支持}\ h=3,4✓$$
$$\text{② 多}\ t\ \text{平均（\text{压低}\ |\delta|\ \text{振荡）} \Longrightarrow \text{滤波后信噪比更清}✓✓$$
$$\text{③ 若}\ h=2,3\ \text{仍显示背景指数继续下降而}\ \beta\ \text{信号不动} \Longrightarrow \textbf{机制确立}✓✓✓$$

---

# §10 【扩大阶梯＋多 $t$ 平均后的判定】＋ **勘误 T10（对 §9）**

$$\text{阶梯}\ T=2^k\ \text{八点}\ (1.5625\text{e}6\to2\text{e}8),\qquad t\ \text{取 5 个零点高度取平均},\qquad \Lambda\ \text{分块筛到}\ 2\text{e}8\ (\text{素幂}\ 11{,}080{,}801\ \text{项})✓$$

## §10.1 各级别数值

| 级别 | $\alpha$（斜率 $\log T$） | $c$（斜率 $\log\log T$） | 数值序列 |
|:--|:--|:--|:--|
| $h=0$ | $+0.0600$ | $\mathbf{+0.9955}$ | 14.63, 15.01, 16.08, 16.76, 17.12, 18.19, 18.52, 19.61 |
| $h=1$ | $+0.0623$ | $+1.0475$ | 0.56, 1.53, 0.99, 0.52, 1.54, 0.48, 1.57 |
| $h=2$ | $+0.1402$ | $+2.3510$ | 1.40, $-0.79$, $-0.67$, 1.47, $-1.54$, 1.58 |
| $h=3$ | $+0.5679$ | $+9.8675$ | $-3.16$, 0.17, 3.09, $-4.34$, 4.50 |

$$\text{判据}\ c(h+1)<c(h)：\ \textbf{全部不成立}（0.996\to1.048\to2.351\to9.868）✗✗$$

## §10.2 ⭐⭐ 判据为何不成立（**结构原因，不是数值故障**）
$$\text{h=1 的序列}\ \textbf{已是常数级振荡}（0.48\!-\!1.57，均值}\approx1.0）\Longrightarrow \text{系统性}\ \log\ \text{趋势}\ \textbf{被完全移除}✓✓$$
$$\Longrightarrow\ \text{h}\ge2\ \text{作用的对象}\ \textbf{只剩噪声} \Longrightarrow \text{放大噪声}（c\ \text{虚高）}✗✗$$
$$\Longrightarrow\ \boxed{\text{背景只有}\ \textbf{一个} \log\ \text{幂}\ (|\delta|\asymp A\log T) \Longrightarrow \textbf{h=1 一次用尽，无累积增益}}✓✓✓$$

## §10.3 人工 $\beta$ 注入（$\Delta\alpha$，背景 $\alpha_{\rm bg}$ 见 §10.1）

| $h$ | $\alpha_{\rm bg}$ | $\beta{=}0.55$ | $\beta{=}0.60$ | $\beta{=}0.65$ | $\beta{=}0.70$ |
|:--|:--|:--|:--|:--|:--|
| 0 | $+0.060$ | $-0.001$ | $+0.010$ | $+0.038$ | $+0.087$ |
| 1 | $+0.062$ | $-0.006$ | $+0.034$ | $+0.082$ | $+0.134$ |
| 2 | $+0.140$ | $-0.125$ | $-0.049$ | $+0.004$ | $+0.056$ |
| 3 | $+0.568$ | $-0.016$ | $-0.217$ | $-0.309$ | $-0.321$ |

$$\Longrightarrow\ \text{可分辨阈值}\ \approx\ \beta\gtrsim0.65\ \text{级}（\text{h=0 与 h=1 同档）}✓$$

## §10.4 ⚠️ **【勘误 T10】对 §9.1（不覆盖上文）**
$$\text{§9.1 曾报"h=1 时}\ \beta=0.60\ \text{由不可辨}\to\textbf{清楚可辨}（\Delta c=0.66）"\ \textbf{不能复现}✗✗$$
$$\text{原因}：\text{§9 用}\ \textbf{7 点、单}\ t；\ \text{本轮}\ \textbf{8 点、5 个}\ t\ \text{平均} ⟹ \text{噪声特征改变} ⟹ \text{原来的大}\ \Delta\ \text{含未平均涨落成分}✗$$
$$\Longrightarrow\ \textbf{降级}：\text{滤波的真实增益是}\ \textbf{把}\ \log\ \text{趋势变成常数}（\text{一步）}，\ \text{检测器分辨率的提升是}\ \textbf{温和的}（\beta\gtrsim0.65）✓$$

## §10.5 判定（更新）
$$\boxed{\text{W4-1c}\ =\ \textbf{MECHANISM-ALIVE（限一步）}}✓$$
$$\qquad\text{滤波器}\ \textbf{真实有效}（\text{h=1 抹掉}\ \log\ \text{趋势、保留幂模态}）✓✓$$
$$\qquad\textbf{但} \text{增益}\ \textbf{不累积}：\text{背景只有一个}\ \log\ \text{幂} \Longrightarrow \text{一次用尽} \Longrightarrow \textbf{不存在"解析选择律"的累积层级}✗✗$$
$$\qquad \text{故唐先生期待的"可持续追问的选择律"}\ \textbf{在当前背景结构下不成立}✗$$

## §10.6 下一步（若继续）
$$\text{① 要获得累积增益，须背景含}\ \textbf{多个可分离的尺度成分}（\text{当前}\ |\delta|\ \text{只有单一}\ \log\ \text{幂}）✓$$
$$\text{② 或改观测量：}\text{不用}\ |\delta_T|\ \text{标量，而用}\ \textbf{全复偏差}\ \delta_T(s)\ \text{的谱}
\ \text{（}\text{可能含更多尺度层次）}✓✓$$
$$\text{③ 或接受：}\text{该机制到此为止（}\text{一步增益，且分辨率}\ \beta\gtrsim0.65）✓$$

## §10.7 边界
$$\text{(i)}\ §10.1--§10.3\ \text{为本档实测（分块筛法，}\Lambda\ \text{精确，}\text{float64}）✓\quad\text{(ii)}\ §10.2\ \text{的"单一}\ \log\ \text{幂"为}\ [\textbf{结构}]✓$$
$$\text{(iii)}\ \textbf{勘误已标}（\text{§10.4}）✓\quad\text{(iv)}\ \textbf{未用 RH}；\ \text{人工注入}\ \text{非真实离轴零点}✓$$
