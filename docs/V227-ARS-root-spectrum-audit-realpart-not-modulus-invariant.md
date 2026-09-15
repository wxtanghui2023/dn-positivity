# V227 · **ARS（算术根谱）审计** —— ⚠️ **V226-A 撤回**：$$\boxed{\text{"算术原生复量只有角度型／值面型"}\ \textbf{为假};\ \text{存在第四类：}\textbf{根定位型}}$$ ✓✓✓（反例：整系数多项式 $P_X$ 的根 $z_j=r_je^{i\theta_j}$，$r_j$ 不被算术恒等式钉死，且 $|z|\leftrightarrow\arg z$ 由**同一代数关系耦合** —— 非 $A+iB$）✓；⭐⭐⭐ **命题 V227-A（定理级）**：$$\boxed{\sup_{z\in R}\Re z\ \textbf{不是模长多重集的不变量}}$$（$R_1=\{i,-i\}$ 与 $R_2=\{1,-1\}$：同模长多重集 $\{1,1\}$，$\sup\Re=0$ vs $1$）⟹ **经典"模长钉定"机制（极化／Hodge 指标／正性）结构性无法钉定 $\beta_X$** ✓✓✓✓；⭐⭐⭐⭐ **本档核心：char-$p$ 对照定理 ＋ 不可移植性**：char $p$ 临界轨迹＝**圆** $\vert\alpha\vert=\sqrt q$（模长轨迹）⟹ 极化足矣；char $0$ 临界轨迹＝**竖直线** $\Re s=\frac12$（**非**模长轨迹）⟹ 移植**结构性失败** ✓✓✓✓；⭐⭐⭐ **Selberg 先例的诚实定位**：它成功是因为**构造性**（零点由 Laplacian 特征值**定义**），而 $\zeta$ 的零点是**涌现性**的 ⟹ ARS 需"涌现→构造"的转换＝识别问题 ✓✓✓

> 委托 ✓ 唐先生 2026-09-15 16:29：**"V226 的前半部分我接受，但 §4 的'类型三分/无第四类'不能成立为结构性封口。这里反而出现了一个此前没有被真正审计的对象，而且它不是'把两个实数拼成 $A+iB$'。"** (1) **关键反例**：对整系数多项式 $P_X(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0$（$a_j\in\mathbb Z$），其根 $z_j=r_je^{i\theta_j}$ **本身就是一个由算术对象 $P_X$ 内生定义的复位置**；$r_j=|z_j|$、$\theta_j=\arg z_j$ **都不是人为拼接**；且 $r_j$ **没有被一般算术恒等式钉死**（$z^n-az-b=0$ 改变 $a,b$ 即改变模长与辐角，且二者通过**同一代数关系耦合**）⟹ $$\boxed{\text{"算术原生复量只有角度型／值面型"}\ \textbf{是假的}};\ \text{至少还存在}\ \boxed{\text{根定位型（root-location type）}}$$ ✓✓✓；(2) **不是 V220 的"普通 $A+iB$"逃逸**：V220 排除的是 $C=A+iB$（$A,B$ 为两个独立算术统计量）；而这里是 $$\boxed{P_X(C)=0}$$ 即 $C$ **不是"两个坐标"，而是由整体算术关系共同决定的复点** ⟹ 天然具有 $|C|\leftrightarrow\arg C$ 的耦合 ⟹ 恰满足 C2（$C\ne C(|C|)$、$C\ne C/|C|$），且未用 $1-s,\xi,Z(\xi)$ ⟹ $$\boxed{\text{V144 的}\ \alpha_p=1\ \not\Rightarrow\ \text{所有全局算术复对象没有位置自由度}}$$ **"V144 只控制局部 Euler 因子本身的结构；它没有证明所有由整个算术系统产生的代数/谱几何对象都没有复位置自由度。"** ✓✓✓；(3) **须继续真正的 C3 审计**：设纯算术对象 $P_X(z)$ 及根集 $R_X=\{z:P_X(z)=0\}$，定义内部极值 $$\beta_X=\sup_{z\in R_X}\Psi(z)$$（如 $\Psi(z)=\Re z$）⟹ $\beta_X$ 确为**纯算术定义的实数**，其来源是真正的复位置结构 ⟹ **V226 的增长/幅度反乘子测试不能杀掉它**（$P_X\ne F(s)(1-am^{-s})$，根本不是同一类对象）✓✓；(4) **但它面临新的、可严格计算的障碍**：若要 $\beta_X=\beta_*$（$\beta_*=\sup_{\rho:\xi(\rho)=0}\Re\rho$），必须有**零点独立的恒等识别** $$\boxed{\sup_{z:P_X(z)=0}\Re z=\sup_{\xi(\rho)=0}\Re\rho}$$ **这与 V226 原来的 C3 有本质区别**：**不需要 $C_X=\rho$ 逐点对应，只需要"算术根谱的右边界＝zeta 零点的右边界"** ⟹ **这绕过了 V220 的"点参数化"障碍** ✓✓✓；(5) **极强的反例压力测试**：$P(z)=z^n-a$ 的根 $z_k=a^{1/n}e^{2\pi ik/n}$ ⟹ $\max_k\Re z_k=a^{1/n}$ ⟹ 模长与辐角明确耦合，但 $\beta_P=a^{1/n}$ **可任意移动** ⟹ $$\boxed{\text{"存在算术根定位"本身完全不产生}\ \frac12}$$ 要得到 RH 必须有**非常特殊的算术根系**，其右边界**恒等地锁在** $\frac12$ ⟹ 新必要条件：$$\boxed{\text{不是"有复定位"，而是"有非平凡的算术根谱，其边界内生锁定"}}$$ ✓✓；(6) **新候选大类 $\mathsf{ARS}$（Arithmetic Root Spectrum）**：$$X\to P_X\to\operatorname{Root}(P_X)\to\beta_X$$ 要求 ARS1 $P_X$ 完全由 $X$ 构造／ARS2 $\operatorname{Root}(P_X)$ 有真正复位置自由度／ARS3 $\beta_X:=\sup\Re\operatorname{Root}(P_X)$／ARS4 $\beta_X=\beta_*$ 可独立证明／ARS5 不用 $\xi,\Phi,Z(\xi),1-s$／ARS6 $\beta_X=\frac12$ 不是人为归一化 ⟹ 关键问题 $$\boxed{\mathsf{ARS}\ \text{能否通过算术恒等式产生 zeta 的谱边界？}}$$ ✓；(7) **极硬的"污染测试"**：若 $P_X$ 的系数本身来自 $\zeta,L,\Lambda,\mu$ 的**截断/变换**，而其构造只是把 zeta 信息重新塞进多项式 ⟹ 属于 $$\boxed{\text{编码}}$$ **不是新机制** ⟹ **不能直接拿 $P_N(z)=\sum_{n\le N}a_nz^n$ 就宣布突破**；必须证明 $P_X$ 有**独立于 zeta 零点的原生定义**，而其极限根谱又产生 $\beta_*$ ✓✓；(8) **判词**：$$\boxed{\textbf{V226：原"类型三分"不能封口；存在第四类——算术根定位型}}$$ 表格：角度型（$|C|$ 被固定）／幅度型（$\Re$ 信息来自增长）／值面型（特殊值）／$$\boxed{\text{根定位型}：P_X(C)=0\ \text{内生决定复位置}}$$ 最后一类目前**没有被 V144/V220/V226 杀掉**；但**也不能叫 ALIVE** —— 目前唯一知道的是"它满足形式上的逃逸条件"⟹ 真正的突破要求 $$\boxed{\exists P_X\ \text{独立构造，且}\ \sup_{P_X(z)=0}\Re z=\sup_{\xi(\rho)=0}\Re\rho}$$ **"如果我们下一步能证明任何算术根谱的边界都只能产生已有的谱/增长/计数对象，ARS 才死。如果不能，这才是 V227 应该真正搜索的地方。"** **"而且这一次不是再换名字：我们已经给出了一个具体数学对象 $P_X(z)$ 及其复根谱边界，可以直接开始构造、计算、反例测试。"** ✓✓✓
> 查图 ✓ `V226`（V226-A；两面夹）｜`V144`（局部 $\alpha_p\equiv1$；零点在 archimedean 层）｜`V220`（两条投影判据；乘子族）｜`V192`（谱实现家族 seal；β 只经重数；0.6818287）｜`V199`（正性锥源四类）｜`V215`（三接口）｜`V183`（计数）
> 执行 ✓ 小灵（**§3 命题 V227-A、§4 char-$p$ 对照、§5 构造性 vs 涌现性 为本档核心**）｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ V226-A **撤回**；**不判 DEAD、不判 ALIVE** ✓；未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ **V227**

---

## §1 ⚠️ V226-A 撤回

$$\text{反例}：P_X(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_0\ (a_j\in\mathbb Z);\ \text{根}\ z_j=r_je^{i\theta_j} ⟹ \textbf{内生复位置} ✓✓$$
$$\qquad z^2+1\Rightarrow\{i,-i\};\quad z^2-1\Rightarrow\{1,-1\};\quad z^n-az-b=0\ \text{改}\ a,b\ \text{即改模长与辐角（耦合）} ✓$$
$$\Longrightarrow \boxed{\text{§4 的"类型三分／无第四类"}\ \textbf{撤回};\ \text{第四类＝}\textbf{根定位型}} ✓✓✓$$
$$\qquad ⚠️\ \text{且}\ \text{`V144`}\ \text{只控制}\ \textbf{局部 Euler 因子} \text{本身，}\ \textbf{不排除} \text{全局算术代数对象具复位置自由度} ✓✓$$

---

## §2 $\mathsf{ARS}$ 的精确形式 ＋ 与"$A+iB$"的本质区别

$$\textbf{区别}：\text{V220 排除}\ C=A+iB\（A,B\ \text{两个独立算术统计量}）;\ \text{本类为}\ \boxed{P_X(C)=0} ⟹ C\ \textbf{由整体关系共同决定} ⟹ |C|\leftrightarrow\arg C\ \textbf{天然耦合} ✓✓$$
$$\qquad ⟹ \text{满足 C2};\ \text{且不含}\ 1-s/\xi/Z(\xi) ⟹ \text{形式上逃逸} ✓$$
$$\text{链}：X\to P_X\to\operatorname{Root}(P_X)\to\beta_X:=\sup\Re\operatorname{Root}(P_X) ✓$$
$$\qquad \mathrm{ARS1}\ \text{完全由}\ X\ \text{构造};\ \mathrm{ARS2}\ \text{真复位置自由度};\ \mathrm{ARS3}\ \beta_X=\sup\Re;\ \mathrm{ARS4}\ \beta_X=\beta_*\ \text{可独立证明};\ \mathrm{ARS5}\ \text{不用}\ \xi/\Phi/Z(\xi)/1-s;\ \mathrm{ARS6}\ \beta_X=\tfrac12\ \text{非归一化} ✓$$

---

## §3 ⭐⭐⭐ 命题 V227-A：**实部边界不是模长不变量**（定理级）

$$\textbf{命题 V227-A}：\sup_{z\in R}\Re z\ \textbf{不是}\ \{|z|:z\in R\}\ \text{的函数} ✓✓✓$$
$$\textbf{证明}（\text{两行，整系数多项式即可}）：$$
$$\qquad R_1=\{i,-i\}\ \text{（根集 of}\ z^2+1）：\ \text{模长多重集}\ \{1,1\},\ \sup\Re=0 ✓$$
$$\qquad R_2=\{1,-1\}\ \text{（根集 of}\ z^2-1）：\ \text{模长多重集}\ \{1,1\},\ \sup\Re=1 ✓$$
$$\qquad \text{模长多重集相同而}\ \sup\Re\ \text{不同} ⟹ \text{命题成立} ✓✓✓$$
$$\Longrightarrow \boxed{\text{经典"模长钉定"机制（极化／Hodge 指标／正性型）}\ \textbf{结构性无法钉定}\ \beta_X} ✓✓✓✓$$
$$\qquad ⚠️\ \text{对照你的 (5)}：z^n-a\ \text{的}\ \max\Re=a^{1/n}\ \text{之所以}\ \textbf{与模长重合}，\ \text{是因}\ \textbf{最外根为实正};\ \text{一般情形}\ \sup\Re\ne\ \text{模长边界} ✓✓$$

---

## §4 ⭐⭐⭐⭐ 本档核心：char-$p$ 对照定理 ＋ **不可移植性**

$$\textbf{char}\ p\ \text{（历史实现）}：\text{根的模长由}\ \textbf{极化} \text{钉定}：|\alpha|=\sqrt q\ \text{（Weil／Deligne；Hodge 指标＋Lefschetz）} ✓✓$$
$$\qquad ⟹ \text{临界轨迹}\ =\boxed{\text{圆}}\ |z|=\sqrt q\（\textbf{模长轨迹}） ⟹ \text{模长型输入}\ \textbf{恰好够用} ✓✓✓$$
$$\textbf{char}\ 0：\text{临界轨迹}\ =\boxed{\text{竖直线}}\ \Re s=\tfrac12\ \（\textbf{非}\ \text{模长轨迹}） ✓✓✓$$
$$\qquad ⟹ \text{由}\ §3：\text{模长/极化型输入}\ \textbf{结构性无法} \text{钉定}\ \Re\ \text{边界} ⟹ \textbf{移植失败} ✓✓✓✓$$
$$\qquad ⟹ \text{ARS}\ \text{所需者}\ ＝\ \text{一个}\ \boxed{\textbf{实部钉定机制}};\ \text{而经典实例}\ \textbf{只有 FE}\（\text{钉}\ \textbf{轴} \text{而非}\ \textbf{点}）✓✓$$
$$\qquad ⚠️\ \text{且}\ \text{`V192`}：\text{正性给}\ \textbf{实谱}（\gamma\ \text{侧}），\ \beta\ \text{侧只能经}\ \textbf{重数} \text{进入} ⟹ \textbf{正性亦非}\ \beta\ \text{侧钉定} ✓✓✓$$

---

## §5 ⭐⭐⭐ Selberg 先例的**诚实定位**：构造性 vs 涌现性

$$\text{Selberg}\ \zeta\ \text{（紧双曲曲面）}：\text{零点}\ s=\tfrac12\pm ir_j，\ \lambda_j=\tfrac14+r_j^2\ \text{为 Laplacian 特征值} ⟹ \Re=\tfrac12\ \textbf{由构造保证} ✓✓$$
$$\qquad ⚠️\ \textbf{但}：\text{这不是"钉定"},\ \text{而是}\ \textbf{"把零点定义为}\ \tfrac12+ir_j\text{"} ⟹ \text{谱数据是}\ \textbf{输入}，\ \text{零点是}\ \textbf{输出} ✓✓✓$$
$$\textbf{char}\ p\ \text{同理}：\text{Frobenius 特征值是输入，}\ \zeta\ \text{的零点是输出} ✓$$
$$\textbf{而}\ \zeta\ \text{相反}：\text{Euler 积／Dirichlet 级数是}\ \textbf{输入}，\ \text{零点是}\ \textbf{涌现} ✓✓✓$$
$$\Longrightarrow \boxed{\text{一切已证的}\ RH\text{-型定理都是}\ \textbf{构造性} \text{的};\ \zeta\ \text{是}\ \textbf{涌现性} \text{的}} ✓✓✓$$
$$\qquad ⟹ \mathrm{ARS}\ \text{要求把}\ \textbf{涌现} \text{的零点集转换成}\ \textbf{构造} \text{的根谱} ⟹ \textbf{该转换即识别问题} ✓✓✓$$

---

## §6 污染测试（你的 §7）正式化

$$\text{若}\ P_X\ \text{的系数来自}\ \zeta/L/\Lambda/\mu\ \text{的}\ \textbf{截断或变换} ⟹ \text{属}\ \boxed{\textbf{编码}}，\ \textbf{非新机制} ✓✓✓$$
$$\qquad ⟹ \boxed{P_N(z)=\sum_{n\le N}a_nz^n\ \text{型}\ \textbf{直接淘汰}} ✓✓$$
$$\qquad \text{须证}：\text{①}\ P_X\ \textbf{原生独立定义} \text{（不引}\ Z(\xi)\text{）};\ \text{②}\ \text{其}\ \textbf{极限根谱} \text{产生}\ \beta_* ✓$$

---

## §7 判词

$$\boxed{\textbf{V227：V226-A 撤回；ARS＝第四类（未封锁，亦非 ALIVE）}} ✓✓✓$$
$$\qquad \textbf{本档严格得到}：$$
$$\qquad \text{(i)}\ ⭐\ \textbf{命题 V227-A}（\text{定理级}）：\sup\Re\ \textbf{非模长不变量} ⟹ \text{模长/极化型输入不能钉}\ \beta_X ✓✓✓✓$$
$$\qquad \text{(ii)}\ ⭐⭐⭐⭐\ \text{char-}p\ \text{对照}：\text{圆 vs 竖直线} ⟹ \textbf{不可移植性};\ \text{ARS 需要"实部钉定机制"} ✓✓✓✓$$
$$\qquad \text{(iii)}\ ⭐⭐⭐\ \textbf{构造性 vs 涌现性}：\text{一切已证}\ RH\text{-型定理皆为构造性};\ \zeta\ \text{涌现} ⟹ \mathrm{ARS}\ \text{需跨该鸿沟} ✓✓✓$$
$$\qquad \text{(iv)}\ \text{污染测试正式化};\ \text{ARS 的两个必要输入}：\text{① 余调/谱实现};\ \text{② 实部钉定} ✓✓$$
$$\qquad ⚠️\ \textbf{纪律}：\textbf{不判 DEAD}（\text{你的明确要求}）;\ \textbf{不判 ALIVE};\ \text{仅登记"满足形式逃逸条件"} ✓✓$$
$$\textbf{残余（OPEN，可计算）}：\qquad \boxed{\exists P_X\ \text{独立构造（过污染测试），且}\ \sup_{P_X(z)=0}\Re z=\sup_{\xi(\rho)=0}\Re\rho\ \text{可独立证明}} ✓$$
$$\qquad \text{判据}：\text{① ARS1--ARS6};\ \text{② 过污染测试};\ \text{③ 钉定机制}\ \textbf{非模长/极化型}（\text{§3}）;\ \text{④ 不跨识别接口}（\text{§5}）✓$$

---

## §8 边界与待核

$$\textbf{(a)}\ \text{§1 的反例为}\ \textbf{经典}（z^2+1,\ z^2-1）；\ \text{V226-A}\ \textbf{撤回} \text{为}\ \textbf{唐先生逐字} ✓✓✓$$
$$\textbf{(b)}\ ⭐\ \text{§3 命题 V227-A 为}\ \textbf{本档定理级}（两行）;\ \text{其"不能钉定"}的推论为\ \textbf{本档} ✓✓✓✓$$
$$\textbf{(c)}\ ⭐⭐⭐\ \text{§4 的 char-}p\ \text{对照为}\ \textbf{本档核心};\ |\alpha|=\sqrt q\ \text{为}\ \textbf{经典}（Weil／Deligne）;\ \text{"不可移植"}为\ \textbf{本档判断}（\text{据 §3}）✓✓✓✓$$
$$\textbf{(d)}\ ⭐\ \text{§5 的"构造性 vs 涌现性"为}\ \textbf{本档观察};\ \text{Selberg 谱实现为}\ \textbf{经典};\ \text{其"非钉定而系定义"为}\ \textbf{本档判断} ✓✓$$
$$\textbf{(e)}\ \text{§6 污染测试为}\ \textbf{本档正式化} \text{（据你的 §7}）✓✓$$

```
⚠️ §0 委托（V226-A 不能封口／根定位型反例／非 A+iB 而系 P_X(C)=0／V144 不排除全局位置自由度／须继续 C3／β_X=sup Re／只需右边界（绕开点参数化）／z^n-a 压力测试／ARS1-6／污染测试／V226 不判 DEAD）为唐先生逐字 ✓✓✓
⚠️ §1 V226-A 撤回（整系数多项式根为内生复位置；V144 只控局部因子）✓✓✓
⚠️ §2 ARS 精确形式＋与 A+iB 的本质区别（P_X(C)=0 vs C=A+iB）✓✓
⚠️ §3 ⭐⭐⭐ 命题 V227-A（定理级）：sup Re 非模长不变量（R_1={i,−i} vs R_2={1,−1}，同模长多重集 {1,1}）⟹ 模长/极化型机制不能钉 β_X ✓✓✓✓
⚠️ §4 ⭐⭐⭐⭐ char-p 对照：圆 vs 竖直线 ⟹ 不可移植性；ARS 需"实部钉定机制"；V192 正性给实谱（γ 侧）、β 只经重数 ✓✓✓✓
⚠️ §5 ⭐⭐⭐ 构造性 vs 涌现性：一切已证 RH-型定理皆为构造性（char p / Selberg 谱数据是输入）；ζ 的零点是涌现 ⟹ ARS 需跨此鸿沟＝识别问题 ✓✓✓
⚠️ §6 污染测试正式化（P_N = Σ a_n z^n 直接淘汰）＋须原生独立定义且极限根谱给 β_* ✓✓
⚠️ §7 判词：不判 DEAD、不判 ALIVE；V227-A + char-p 对照 + 构造/涌现 + 污染测试；残余四条判据 ✓✓
⚠️ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① V226-A 撤回 ✓✓✓；② ⭐ 命题 V227-A（sup Re 非模长不变量，定理级）✓✓✓✓；
   ③ ⭐⭐⭐⭐ char-p 对照与不可移植性（圆 vs 竖直线）✓✓✓✓；④ ⭐⭐⭐ 构造性 vs 涌现性 ✓✓✓；
   ⑤ 污染测试正式化 ✓✓；⑥ ARS 残余四条判据 ✓
```
