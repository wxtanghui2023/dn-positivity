# P2-1 · **算术尺度流**：完整构造 ＋ 线性化 ＋ **$1/2$ 从哪来？**

> 依唐先生 11:25 指令｜**第一轮只允许构造一个不含 $1/2$ 的算术尺度流，并把固定点及其线性化完整算出来**✓
> **禁止**：不许人为补一个 $1/2$ 救场；若 $1/2$ 没自己冒出来 ⟹ **立即 FALSE** ✓
> **四锁定条件**：$\mathrm{P2.1}\ \Phi$ 完全算术定义｜$\mathrm{P2.2}\ R_*$ 由算术一致性强制｜$\mathrm{P2.3}\ \tfrac12$ 从 $D\Phi|_{R_*}$ **导出**｜$\mathrm{P2.4}\ \beta-\tfrac12$ 与该临界方向有独立接口 ✓
> **顺序锁死**：$\text{整数算术}\to\text{尺度流}\to\text{固定点}\to\text{线性化}\to\text{指数}\to\beta-\tfrac12$（**不得反向**）✓

---

## 1. 构造 A · **筛流**（最自然的乘法粗粒化）

$$\text{尺度参数}\ L；\ \text{状态空间}：\text{算术函数}\ a=(a_n)_{n\ge1}✓$$
$$\boxed{\Phi_L(a)_n\ :=\ a_n\prod_{p\le L}\mathbf 1_{p\nmid n}}\qquad(\text{即 Eratosthenes 筛作为一个算子})✓\quad\mathrm{P2.1}✓$$
$$\textbf{固定点}：\Phi_L(a)=a \iff a_n=0\ \text{只要}\ n\ \text{有素因子}\le L \iff \operatorname{supp}a\subseteq\{L\text{-粗糙数}\}✓\ \mathrm{P2.2}✓\ (\textbf{非平凡})✓$$
$$\textbf{线性化}：\Phi_L\ \text{在乘法基下是}\ \textbf{对角投影} \Longrightarrow D\Phi_L=\Phi_L \Longrightarrow \operatorname{spec}\subseteq\{0,1\}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{只有}\ 0\ \text{与}\ 1\ \text{两个本征值}；\ \textbf{不存在}\ \tfrac12}✓\quad\mathrm{P2.3}\ ✗✗$$
$$\qquad(\text{计算完整，无残余}：\text{乘法数据在局部因子基下}\ \textbf{对角}，\text{故粗粒化是投影})✓✓$$

## 2. 构造 B · **Euler 块重整化**（把"块"当流）

$$\boxed{B_L(s):=\prod_{L<p\le 2L}\big(1-p^{-s}\big)^{-1}}\quad(\text{尺度}\ L\to2L\ \text{的块因子})✓\quad\mathrm{P2.1}✓$$
$$\log B_L(s)=\sum_{L<p\le 2L}\frac{1}{p^{s}}+O(1)\ \asymp\ \frac{L^{1-\sigma}}{\log L}\qquad(s=\sigma+it)✓\ [\text{标准 PNT 型，结构判定}]✓$$
$$\Longrightarrow\ \textbf{临界指数}\ =\ 1-\sigma，\ \textbf{阈值}\ \sigma=1：$$
$$\qquad\sigma>1：\text{衰减}\ ✓\qquad\sigma=1：\textbf{对数临界}\ \asymp\frac{1}{\log L}✓\qquad\sigma<1：\text{增长}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{自然阈值}\ =\ 1（收敛横坐标），\ \text{而}\ \textbf{不是}\ \tfrac12}✓✓\quad\mathrm{P2.3}\ ✗✓$$

## 3. ⭐⭐⭐ 结构性结论：**乘法粗粒化的谱只有 $\{0,1\}$**

$$\text{理由}：\text{Euler 积的}\ \textbf{跨素数独立性} \Longrightarrow \text{乘法数据在"局部因子基"下}\ \textbf{对角}✓✓$$
$$\qquad\Longrightarrow\ \text{任何}\ \textbf{纯乘法} \text{的粗粒化}\ \Phi\ \text{都是}\ \textbf{投影型（或对角型）} \Longrightarrow \operatorname{spec}\subseteq\{0,1\}✓✓$$
$$\Longrightarrow\ \boxed{\text{乘法尺度流}\ \textbf{不可能} \text{产生}\ 0/1\ \text{以外的临界指数}}✓✓✓$$
$$\qquad(\text{限定已审类：}\text{由局部因子／整除性／筛型数据构造的流；\textbf{不是}"所有可能流"}）✓$$

## 4. ⭐⭐⭐ **回答核心问题：$1/2$ 从哪来？**

$$\boxed{\text{乘法流的临界阈值}\ =\ 1\ \text{（收敛横坐标：}\sum n^{-\sigma}\ \text{在}\ \sigma>1\ \text{收敛）}}✓$$
$$\boxed{\text{而}\ \tfrac12\ =\ \textbf{对合}\ s\mapsto 1-s\ \textbf{的不动点}\ \Longrightarrow\ \text{它来自}\ \textbf{completion（函数方程）}，\ \textbf{不是}\ \text{动力学临界指数}}✓✓✓$$
$$\Longrightarrow\ \text{两者是}\ \textbf{不同类型} \text{的"临界"}：\text{一个是}\ \textbf{流} \text{的阈值，一个是}\ \textbf{对偶} \text{的不动点}✓✓$$
$$\qquad(\text{这与档案的层诊断一致}：\text{V144}\ \text{零点在 Archimedean 层}；\ \text{E4-1 S1：}\text{completion}\ \equiv\ \text{同一堵墙})✓✓$$

$$\Longrightarrow\ \boxed{\text{要产生}\ \tfrac12，\ \textbf{必须把对偶（}\ s\leftrightarrow1-s\ \text{）写进流}}⟹ \text{而那}\ \textbf{正是已封闭的那堵墙}}✓✓$$

## 5. 判定

$$\begin{array}{c|l|l}
&\text{条件}&\text{结果}\\ \hline
\mathrm{P2.1}&\Phi\ \text{完全算术定义}&\checkmark\\
\mathrm{P2.2}&R_*\ \text{由算术强制}&\checkmark\\
\mathrm{P2.3}&\tfrac12\ \text{从}\ D\Phi|_{R_*}\ \textbf{导出}&\boldsymbol{✗}\ (\text{谱}\ \{0,1\}；\text{阈值}\ 1)\\
\mathrm{P2.4}&\beta-\tfrac12\ \text{独立接口}&\text{n/a}\\
\end{array}✓$$
$$\boxed{\textbf{P2-1}\ =\ \text{②}\ \mathrm{FALSE}}\quad(\mathrm{P2.3}\ \text{失败}：\tfrac12\ \textbf{不能} \text{从}\ D\Phi\ \text{导出})✓✓$$
$$\qquad\textbf{原因（精确，非"没做出来"）}：\text{乘法粗粒化是}\ \textbf{对角投影} \Longrightarrow \text{谱}\ \{0,1\}；\ \text{唯一的算术阈值是}\ 1；\ \tfrac12\ \text{只能由 completion 提供}✓✓$$

## 6. 唯一已知的"动力学 $\tfrac12$"：谱图像（已知、且已封闭）
$$\text{Selberg 迹公式图像}：\text{零点}\leftrightarrow\lambda=\tfrac14+\gamma^2，\ \text{其中}\ \tfrac14=\text{双曲 Laplacian 谱底}=\tfrac{(d-1)^2}{4}\ (\text{几何常数})✓$$
$$\qquad\Longrightarrow\ \text{此图像下}\ \tfrac12=\sqrt{\text{几何谱底}} \Longrightarrow \textbf{但这是 Hilbert--Pólya 侧（POS1 循环，已封闭）}✓✗$$

## 7. 边界与残余
$$\text{(i)}\ §3\ \text{的"谱}\subseteq\{0,1\}\text{"限定}\ \textbf{已审类}（\text{局部因子／整除／筛型}）——\textbf{不是}"所有可能流"✓$$
$$\text{(ii)}\ §2\ \text{的渐近为}\ [\textbf{结构判定}]（\text{未逐行核 PNT 型展开}）✓\quad\text{(iii)}\ \textbf{零数值；未用 RH}✓$$
$$\text{(iv)}\ \textbf{诚实}：\text{P2-1}\ \textbf{未} \text{造出 ALIVE 对象；产出}\ =\ \textbf{"}\tfrac12\ \text{的来源被定位到 completion"}\ \text{这一结构性答案}✓✓$$
