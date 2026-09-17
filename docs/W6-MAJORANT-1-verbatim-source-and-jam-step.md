# ⚔️ **W6-MAJORANT-1**：Prop 5.4 原式逐字 ＋ **卡点精确定位**（＝Montgomery–Vaughan 步）

> 依唐先生 12:24 指令：**先打 W6**；D3／D5 暂不启动 ✓｜**已查地图** ✓
> 目标问题（唐先生形式）：$$\boxed{\text{对偶正性 majorant 能否在不引入 RH／HL／pair correlation 的情况下，吃掉 Prop 5.4 的 off-diagonal 缺口？}}✓$$

---

## §1 窗口定义（§5.1 逐字，L562–L580）

$$b:=\frac{1}{L}\int\phi^4\quad(0<b\le a\le1),\qquad w:=1✓$$
$$\textbf{(5.1)}\quad \Phi:=c\phi^2,\qquad g:=\phi^2\star\phi^2,\qquad A_\phi:=\phi\star\phi,\qquad (v\star v)(y):=\int v(u)v(u+y)\,du✓$$
$$\text{于是}\ \hat\phi\ \text{与}\ \Phi\ \text{为实、偶、整；}\ \hat\phi(0)\le L,\ \Phi(0)=aL；\ \textbf{配对相关核}\ R:=|\hat\phi|^2\ \textbf{非负}（\text{构造性}）✓$$
$$\hat\phi^2=cA_\phi,\quad \Phi^2=\hat g\ \text{on}\ \mathbb R;\qquad \int_{\mathbb R}\Phi^2=2\pi g(0)=2\pi bL✓$$
$$\text{且}\ \mathbf 1_{[-L/2+w,\,L/2-w]}\le\phi^2\le\phi\le\mathbf 1_{[-L/2,\,L/2]} \Longrightarrow \textbf{(5.2)}\quad \boxed{(L-2w-|y|)_+\le g(y)\le A_\phi(y)\le(L-|y|)_+}✓✓$$
$$\textbf{(5.3)}\quad \max\big(|\hat\phi(r)|,|\Phi(r)|\big)\le\vartheta(r):=\min\Big(L,\ \tfrac{2}{|r|},\ \tfrac{C_\chi w}{r^2}\Big)\qquad(r\in\mathbb R)✓$$
$$\textbf{(5.4)}\quad \Theta_0:=\int_0^\infty\vartheta(r)dr=\frac{4+2\log(C_\chi L)}{4w}\ll\log L,\qquad \int_{\mathbb R}\vartheta(r)^2|r|dr\ll\log L,\qquad \int_{\mathbb R}\vartheta^2\le8L✓$$
$$\textbf{Lemma 5.1}\ \text{(MV07 §2.2)}：\sum_{n\le x}\Lambda(n)\ll x;\quad \sum_{n\le x}\frac{\Lambda(n)}{\sqrt n}\le3\sqrt x;\quad \sum_{n\le x}\frac{\Lambda(n)^2}{\sqrt n\log n}\ \text{-型};\quad \sum_{n\le x}\Lambda(n)^2\ll x\log x✓$$

---

## §2 **Proposition 5.4** 逐字（L839）＋ 分解

$$\textbf{Prop 5.4（Prime term）}：\ M[P_X,P_X]=\frac{T}{\pi}\sum_{n\le X}\frac{\Lambda(n)^2}{n}\,g(\log n)+O\big(\chi(L^2X)\big),\qquad g:=\phi^2\star\phi^2✓$$
$$\text{证明起点}：P_X(\tau)=-\frac{1}{2\pi}\sum_na_n\big(n^{i\tau}+n^{-i\tau}\big),\qquad \boxed{a_n=\frac{\Lambda(n)}{\sqrt n}}✓$$
$$\text{代}\ \tau=\tau'+x；\ \text{"for fixed}\ x\ \text{the variable}\ \tau'\ \text{ranges over}\ I\cap(I-x),\ \textbf{which is empty for}\ |x|\ge T\ \text{and equals}\ [T+x_-,2T-x_+]\ \text{for}\ |x|<T"✓$$
$$M[P_X,P_X]=\frac{1}{2\pi^2}\mathrm{Re}\sum_{n,m}a_na_m\int_{-T}^{T}\Phi(x)^2n^{ix}\Big[\underbrace{\int_{T+x_-}^{2T-x_+}(n/m)^{i\tau'}d\tau'}_{\textbf{第一内积分}}+\underbrace{\int(nm)^{i\tau'}d\tau'}_{\textbf{第二}}\Big]dx=:D+O_1+O_2✓$$

### §2.1 **$D$（对角，$n=m$）** 逐字
$$D=\frac{1}{2\pi^2}\sum_na_n^2\Big[T\cdot2\pi g(y_n)+O\Big(\int\Phi(x)^2\big(|x|+T\mathbf 1_{|x|>T}\big)dx\Big)\Big]=\frac{T}{\pi}\sum_na_n^2g(y_n)+O(L^2\log L)✓$$
$$\qquad(\text{用}\ \int_{|x|>T}\Phi^2\le\int\Phi^2|x|/T)✓$$

### §2.2 **$O_2$** 逐字
$$\Big|\int_{T+x_-}^{2T-x_+}(nm)^{i\tau'}d\tau'\Big|\le\frac{2}{\log(nm)}\le\frac{2}{\log4}\ \forall n,m \Longrightarrow |O_2|\le\frac{1}{2\pi^2}\Big(\sum_na_n\Big)^2\cdot2\pi bL\cdot\frac{2}{\log4}\ll XL✓$$

### §2.3 ⭐⭐⭐ **$O_1$（真正的离对角）** 逐字
$$\text{对}\ n\ne m\ \text{记}\ \vartheta:=y_n-y_m\ne0；\ \text{第一内积分}\ =\frac{(n/m)^{i(2T-x_+)}-(n/m)^{i(T+x_-)}}{i\vartheta}；$$
$$\qquad n^{ix}(n/m)^{-ix}=m^{ix}\ (x>0)\ /\ n^{ix}\ (x<0)；\qquad n^{ix}(n/m)^{ix}=n^{ix}\ (x>0)\ /\ m^{ix}\ (x<0)✓$$
$$\boxed{\alpha_n^+:=\int_0^{T}\Phi(x)^2n^{ix}dx,\qquad \alpha_n^-:=\int_{-T}^{0}\Phi(x)^2n^{ix}dx,\qquad |\alpha_n^\pm|\le\pi bL\le\pi L}✓$$
$$O_1=\frac{1}{2\pi^2}\mathrm{Re}\sum_{n\ne m}\frac{a_na_m}{i(y_n-y_m)}\Big[\Big(\frac nm\Big)^{2iT}\big(\alpha_m^++\alpha_n^-\big)-\Big(\frac nm\Big)^{iT}\big(\alpha_n^++\alpha_m^-\big)\Big]✓$$
$$\Longrightarrow\ \boxed{\text{这是四个}\ \sum_{n\ne m}\frac{x_nz_m}{y_n-y_m}\ \text{型双线性形式的组合}，\ \{|x_n|,|z_n|\}=\{a_n,\ a_n|\alpha_n^\pm|\}}✓✓$$

---

## §3 ⭐⭐⭐ **卡点精确定位：就是 Montgomery–Vaughan 那一步**

$$\text{逐字（L960--L965）}：\text{"for instance the first is}\ \sum_{n\ne m}(a_nn^{2iT})(a_mm^{2iT}\alpha_m^+)/(y_n-y_m).\ \textbf{By Lemma 2.2 and (2.12) each of the four is at most}$$
$$\qquad \frac{3\pi}{2}\cdot\pi L\cdot\sum_n a_n^2/\delta_n\ll L^2X.\ \text{Hence}\ |O_1|\ll L^2X.\text{"}✓✓✓$$
$$\text{其中}\ \textbf{Lemma 2.2 ＝ Montgomery--Vaughan 双线性型（Hilbert 型）}，\ \textbf{(2.12)}：\{\lambda_r\}=\{\log n\}，\ \delta_n^{-1}\le2n✓$$

### §3.1 **由此得到天花板的确切数学来源**
$$D\ \asymp\ \frac{T}{\pi}\sum_na_n^2g(y_n)\ \asymp\ \frac{T}{\pi}\cdot\frac{L^3}{6},\qquad |O_1|\ll L^2X✓$$
$$\Longrightarrow\ \text{对角支配}\iff \frac{TL^3}{6}\gg L^2X\iff \boxed{X\ll TL}；\ \text{与}\ L\asymp\log T\ \text{合并} \Longrightarrow \boxed{X\lesssim T\log T}（\text{前沿取}\ X\le T）✓✓$$

### §3.2 **所需改进的精确量**
$$\text{要把范围推到}\ X\gg T：\ \text{须}\ |O_1|\ll TL^3，\ \text{而现为}\ L^2X \Longrightarrow \textbf{须改进因子}\ \asymp\frac{X}{TL^3}✓✓$$
$$\qquad(\text{即：把 MV 给出的}\ L^2X\ \text{压到}\ \lesssim TL^2\cdot L\ \text{级})✓$$

### §3.3 ⭐ **回答唐先生的判断题**
$$\text{唐先生问：能否用}\ \textbf{"一侧不等式"} \text{而不是平均值估计，绕掉导致 bandwidth-one 的那一步？}✓$$
$$\Longrightarrow\ \boxed{\textbf{是}：那个"一步"被精确定位＝}\textbf{Montgomery--Vaughan（Lemma 2.2）}，\ \text{而 MV}\ \textbf{恰是均值型（}\ell^2\text{、双边、绝对值）} \text{的 Hilbert 型不等式}✓✓✓$$
$$\qquad(\text{与}\ V300\ \text{既有判定逐字一致}：\text{MV}\ \textbf{只用}\ \ell^2\ \text{范数} \Longrightarrow \textbf{不含配对相关内容}）✓✓$$

---

## §4 **W6-MAJORANT-1** 实验规格（唐先生形式，登记）

$$\text{记离对角核}\ K(h)\（h=y_n-y_m=\log(n/m)）\ \text{使}\ O=\sum_{m,n}a_na_mK(m-n)✓$$
$$\text{造 majorant／minorant 对}\ K_-(h)\le K(h)\le K_+(h)\ \text{满足}\ \boxed{\widehat{K_\pm}\ \text{有严格有限支撑}}，\ \text{误差}\ E(h):=K_+(h)-K_-(h)\ge0\ \textbf{完全显式}✓$$
$$\text{代入 Prop 5.4 后}\ \boxed{O\le O_{\rm diagonal}+O_{\rm extremal}+O_{\rm error}}✓$$
$$\textbf{只问一个数}：\boxed{\text{extremal gain}-\text{majorant leakage}\ \stackrel{?}{>}\ \text{Prop 5.4 缺口}}✓✓$$
$$\qquad\text{不成立} \Longrightarrow \textbf{精确算出差多少} \Longrightarrow \textbf{W6-majorant 立即 FALSE}✓\quad\text{成立} \Longrightarrow \text{继续第二刀}✓$$

### §4.1 **四条禁止偷渡（硬）**
$$\text{① 不使用 RH}\quad\text{② 不使用 Hardy--Littlewood}\quad\text{③ 不使用 Montgomery pair correlation}\quad\text{④ 不把 support}>1\ \text{写进 majorant 的假设}✓✓$$

---

## §5 边界
$$\text{(i)}\ §1--§3\ \textbf{逐字}（本地 PDF 抽取，行号基于}\ \texttt{zeta23\_2608.13637.clean.txt}\text{）✓$$
$$\text{(ii)}\ §3.1--§3.2\ \text{为本档推导（初等指数比较）}✓\quad\text{(iii)}\ \text{本轮}\ \textbf{未跑计算}，\ \textbf{未用 RH}✓$$
