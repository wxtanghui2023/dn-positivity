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
