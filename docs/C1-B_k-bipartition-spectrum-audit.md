# ⚔️ **C1 执行**：Heath–Brown $k$-阶分裂的**二分谱 $\mathcal B_k$** —— **C1 不构成 NO-GO**，但**重定位了障碍**

> 依唐先生 15:29「开 C」＋四层判死树规格（**参数化结构审计**，非验证预设结论）✓
> **本档结果**：$\mathcal B_k$ 显式求出；$\mathcal B_k\cap\mathcal I\ne\emptyset$ **恒成立** ⟹ **C1 单独不是 NO-GO**；真障碍**重定位到"长侧的多因子性"**✓✓✓

---

## §0 C 档规格（唐先生逐字采纳）
$$\textbf{C1 长度几何}：\forall k,\ \mathcal B_k\cap\mathcal{II}\ne\varnothing\ ?\qquad\textbf{C2 系数结构}：\text{Type II 项能否因}\ \mu/\log\ \text{结构坍缩？}$$
$$\textbf{C3 cancellation 机制}：\text{若不能坍缩，是否}\ \textbf{只能用} \text{双线性估计？}\qquad\textbf{C4 parity 接口}：\text{突破}\iff\text{超越 sieve parity 的 prime-detection？}$$
$$\text{唐先生预判（本档验证成立）}：\text{"}\textbf{仅凭长度计数，不能证明 Type II 必不可少}\text{"}✓✓$$

## §1 Heath–Brown 恒等式的精确形式 ⟹ 因子结构
$$\Lambda(n)=\sum_{j=1}^{k}(-1)^{j-1}\binom{k}{j}\sum_{\substack{n=n_1\cdots n_jm_1\cdots m_j\\ n_1,\dots,n_j\le R}}\mu(n_1)\cdots\mu(n_j)\log m_1\cdots\log m_j✓\qquad(R=X^{1/k})✓$$
$$\Longrightarrow \text{第}\ j\ \text{项因子数}\ \ell=2j\ (\le2k\ ✓)；\ \textbf{结构}：\underbrace{j\ \text{个}\ \mu\text{-因子}}_{N_i\le R=X^{1/k}\ (\textbf{短、固定})}\ +\ \underbrace{j\ \text{个}\ \log\text{-因子}}_{\textbf{长度可调、乘积}\asymp X}✓✓$$

## §2 ⭐ C1 执行：$\mathcal B_k$ 显式
$$\mathcal B_k=\Big\{(\alpha,\beta)=\Big(\log_X\!\!\prod_{i\in I}\!N_i,\ 1-\alpha\Big):\ I\ \text{合法二分}\Big\}✓$$
$$\text{取"}\mu\text{侧}\ |\ \log\text{侧"}\ \text{这一}\ \textbf{特定二分}：\ \alpha=\log_X\!\!\prod_{\mu\text{侧}}\!N_i\ \le\ \log_X R^{\,j}=\boxed{\frac jk}✓✓$$
$$\Longrightarrow \text{取}\ j=1：\alpha\le\frac1k；\ \text{而}\ \theta_I\gtrsim\frac13 \Longrightarrow \boxed{\frac1k\le\theta_I\ (k\ge3)} \Longrightarrow \textbf{μ 侧落在 Type I}✓✓✓$$
$$\Longrightarrow \boxed{\mathcal B_k\cap\mathcal I\ne\varnothing\ \textbf{恒成立}（k\ge3）} \Longrightarrow \boxed{\textbf{C1 单独不构成 NO-GO}}✓✓✓\quad(\text{与唐先生预判一致})✓$$

**小案表**：
| $k$ | $R$ | 第 $j=1$ 项：$\mu$侧长度 $\le$ | $\alpha_{\max}$ | Type I？（$\theta_I\!\approx\!1/3$）|
|:--:|:--|:--|:--|:--:|
| 1（Vaughan 型）| $X$ | $X$ | 1 | ✗（须另法）|
| 2 | $X^{1/2}$ | $X^{1/2}$ | $1/2$ | ✗（$1/2>1/3$）|
| **3** | $X^{1/3}$ | $X^{1/3}$ | $\mathbf{1/3}$ | ✓（临界）|
| 4 | $X^{1/4}$ | $X^{1/4}$ | $1/4$ | ✓✓ |
| $k$ | $X^{1/k}$ | $X^{1/k}$ | $1/k$ | ✓（$k\ge3$）|

$$\Longrightarrow ⭐\ \text{即：}\textbf{提高} \ k\ \text{确实能把}\ \mu\text{侧压进 Type I}\ ——\ \text{但见 §3：障碍不在}\ \mu\ \text{侧}✓✓$$

## §3 ⭐⭐⭐ 真正的障碍：**长侧是"多因子（multilinear）"，不是 Type I**
$$\text{把}\ \mu\ \text{归一侧后，}\textbf{另一侧＝若干}\ \log\text{-因子的乘积} \Longrightarrow \text{待估的对象是}$$
$$\sum_{m_1\cdots m_r\asymp X}\Big(\prod_{i=1}^r\log m_i\Big)F(m_1\cdots m_r)\qquad(r\ \text{个因子},\ r\ge2)✓✓$$
$$\Longrightarrow ⚠️\ \text{这}\ \textbf{不是} \text{经典 Type I（单一长变量）}，而是\ \textbf{多线性型}✓$$
$$\qquad \text{估计多线性型}：\text{按}\ \text{Cauchy--Schwarz／对偶} \Longrightarrow \text{化回}\ \textbf{双线性型}\ \text{（经典唯一可行路径）}✓$$
$$\Longrightarrow \boxed{\text{Type II 以"}\textbf{必备工具}\text{"而非"坏二分"的形式重现}}✓✓✓$$
$$\qquad 📌\ \text{这正是唐先生"第二刀"的可证化}：}\textbf{增加因子数不消灭二分，只增加可选二分} —— \text{而}\ \textbf{可选二分里没有一个是"真 Type I"}✓✓$$

## §4 ⭐⭐ 文献数据点（支持本档判定）
$$\text{越过}\ 1/2\ \text{的实际进展}：\ \theta<\tfrac{16}{49}\ (\text{Heath-Brown--Jia}) \longrightarrow \theta<\tfrac13\ (\text{Matomäki})✓$$
$$\qquad 📌\ \text{文献逐字（引文）：}\text{"Matomäki was able to extend this to handle any}\ \theta<\tfrac13\text{"}\ ——\ \text{机制＝}\boxed{\text{平均值上的}\ \textbf{Kloosterman 和}\ \text{结果}}✓✓✓$$
$$\Longrightarrow ⭐\ \text{关键：}\text{越过}\ 1/2\ \text{靠的}\ \textbf{不是} \text{提高分裂阶数，而是}\ \textbf{换输入}（\text{Kloosterman／谱}）✓✓✓$$
$$\qquad \Longrightarrow \text{与我们}\ \texttt{V254}\ \text{T6 的判词}\ \textbf{一致}：\text{"新对象}\ \textbf{不应属筛法权重类}"✓✓$$

## §5 C1 判词 ＋ 转入 C2
$$\boxed{\text{C1 判词}：\text{长度几何}\ \textbf{不产生 NO-GO}（μ 侧总能进 Type I）；\ \text{但}\ \textbf{障碍被重定位}}✓✓✓$$
$$\qquad \Longrightarrow \text{障碍}＝\textbf{"长侧多因子性"}\ \text{（C2/C3 的对象）}，\ \text{而非"坏二分"}✓✓$$
$$\text{转入}\ \textbf{C2}\ \text{的精确问题}：\text{长侧的多线性型}\ \sum_{m_1\cdots m_r}\prod\log m_i\,F(\prod m_i)\ \text{的}\ \textbf{系数能否坍缩}？$$
$$\qquad(\log\ \text{是}\ \textbf{光滑、无符号} \text{的——}\text{与}\ \mu\ \text{的符号结构不同；须查是否可用}\ \textbf{光滑性＋vdC／Poisson} \text{绕过双线性})✓✓$$

## §6 边界
$$\text{(i)}\ §1\ \text{的 Heath--Brown 形式为}\ \textbf{标准形式}（\text{本档未逐字核原论文}）✓\quad\text{(ii)}\ §2\ \text{为初等长度计数}✓\quad\text{(iii)}\ §3\ \text{为}\ [\textbf{结构}] \text{级判断}✓$$
$$\text{(iv)}\ §4\ \text{引文为唐先生所引文献}\ \textbf{逐字片段}（\text{未取原文}）✓✓\quad\text{(v)}\ \textbf{未用 RH}；\ \textbf{零数值}✓$$
