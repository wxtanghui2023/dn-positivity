# E6-9（犬-1＋犬-2）— **七槽填充 ＋ $\alpha(\theta)$ 显式映射**（X1／X2 完成）

> 唐先生 2026-09-16 18:23「1，2 都推进」。
> **取证方式**：arXiv HTML 正文（`arxiv.org/html/2403.13157v1`）—— **外部来源，仅作数据引用**；本档未逐行核验全文，仅取引言与定理陈述层。
> 论文：**Matomäki–Teräväinen**，"A note on zero density results implying large value estimates for Dirichlet polynomials"，arXiv:2403.13157v1。

---

## 1. 第一关：七槽填充（**本轮完成**）

### 槽 (1) density hypothesis 形式 —— ✓ 取得
$$\text{(1.2) DH：}\quad \mathrm{N}(\sigma,T)\ \ll_{\varepsilon}\ T^{2(1-\sigma)+\varepsilon}\quad(\sigma\in[\tfrac12,1])$$
$$\text{Conjecture 1.4（stronger DH）：}\quad \mathrm{N}(1-\nu,T)\ \ll_{\varepsilon}\ T^{(2-\delta)\nu}\quad(\nu\in[0,\tfrac12-\varepsilon))$$
$$\qquad\text{（}\text{Bourgain 精化 Jutila：Conj 1.4 在}\ \varepsilon=25/32\ \text{已知成立）}$$

### 槽 (2) large-value 所控制的量 —— ✓ 取得（**关键：是测度，非良分离点数**）
$$\text{The 1.2：}\ \Bigl|\Bigl\{t\in[-T,T]:\ \Bigl|\sum_{M<m\le M'}\frac{1}{m^{1+it}}\Bigr|\ \ge\ M^{-\nu}\ \text{对某}\ M\in[T^{\varepsilon},T^{1/2}/2],\ M'\in(M,2M]\Bigr\}\Bigr|$$
$$\qquad\Longrightarrow\ \textbf{被控制的是}\ \textbf{一维测度}（\text{大值集的长度}），\ \textbf{不是良分离点的计数}✓$$

### 槽 (3) 系数类 $\tau$ —— ✓ 取得（**受限**）
$$\text{多项式：}\ \sum_{M<m\le M'}m^{-1-it}\quad\Longrightarrow\ \boxed{\tau=\{\,1/n\ \text{在}\ \textbf{二进区间} \text{上}\,\}}\ (\textbf{非一般 Dirichlet 多项式类})✓$$

### 槽 (4) $X$ 的允许范围 $\kappa$ —— ✓ 取得（**短**）
$$\boxed{M\in[T^{\varepsilon},\ T^{1/2}/2],\quad M'\in(M,2M]}\quad\Longrightarrow\ X\le T^{1/2}\ (\text{远短于 density 框架的}\ X\asymp T^{\kappa},\ \kappa\le1)✓$$

### 槽 (5) 阈值范围 —— ✓ 取得
$$\text{阈值}\ =\ M^{-\nu}\ (\text{与长度}\ M\ \text{绑定})；\quad\text{在}\ R_{\sigma,\eta}(T)\ \text{记号下为}\ T^{\eta}✓$$

### 槽 (6) spacing 条件 $\delta$ —— ✓ 取得（**one-spaced，非}\gg1/\log T）$
$$\text{论文脚注 1：}\textbf{one-spaced}\ \text{＝任意两点距离}\ \ge1\quad\Longrightarrow\ \boxed{\delta\ge1}$$
$$\qquad\textbf{与经典零点检测框架不同}（\text{后者用}\ \gg1/\log T）✓$$

### 槽 (7) $\theta\to\alpha$ 的指数变换 —— ✓ 取得（**The 1.2 主不等式**）
$$\Bigl|\{t\in[-T,T]:\dots\}\Bigr|\ \ll_{\varepsilon}\ T^{\varepsilon}\max_{1-\nu-\varepsilon\le\alpha\le1}T^{\frac{\alpha-(1-\nu)}{2}}\mathrm{N}(\alpha,\,C\!\cdot\!T)\ +\ T^{\frac{\nu}{2}+\varepsilon}$$

---

## 2. $\alpha(\theta)$ 的**显式抽取**（本档由槽 (7) 推出）
$$\text{设 density 指数函数}\ f：\mathrm{N}(\alpha,T)\ll T^{f(\alpha)}。\ \text{则}\ \text{The 1.2}\ \text{给出}$$
$$\boxed{\text{LV-exponent}(\nu)\ =\ \max_{1-\nu-\varepsilon\le\alpha\le1}\Bigl[\tfrac{\alpha-(1-\nu)}{2}+f(\alpha)\Bigr]\ +\ O(\varepsilon)}$$
$$\textbf{自校验（本档计算）}：\text{在 DH}\ f(\alpha)=2(1-\alpha)\ \text{下，被积}\ \tfrac{\alpha-(1-\nu)}{2}+2(1-\alpha)=\tfrac{1-\nu}{2}+2-\tfrac{3\alpha}{2}\ \textbf{随}\ \alpha\ \text{递减}$$
$$\qquad\Longrightarrow\ \text{取}\ \alpha=1-\nu-\varepsilon：\ \text{LV-exponent}=2\nu+\tfrac{3\varepsilon}{2}+O(\varepsilon)=2\nu+O(\varepsilon)$$
$$\Longrightarrow\ \Bigl|\{t:|M(1+it)|\ge M^{-\nu}\}\Bigr|\ll_{\varepsilon}T^{2\nu+\varepsilon}\quad\Longrightarrow\ \boxed{\text{与论文自述结论}\ \textbf{完全一致}}\ ✓✓$$
$$\qquad\textbf{（此自校验是本档抽取正确性的强证据）}$$

---

## 3. 第二关：反向映射是否落在**同一个** $\mathfrak K$ —— **参数层判定＝受限切片**
$$\text{对象类型}：\textbf{同为}\ \text{"Dirichlet 多项式的大值估计"} \Longrightarrow\ \textbf{对象层同在}\ ✓$$
$$\textbf{参数层（逐槽比对）}：\ \tau=\{\,1/n\ \text{二进支撑}\}（\text{非一般}\tau）；\ X\le T^{1/2}（\text{非}\ \kappa\le1\ \text{全域}）；$$
$$\qquad\text{阈值}=M^{-\nu}\ \text{与长度绑定}；\ \delta\ge1\ \text{且被控制量为}\ \textbf{测度而非计数}$$
$$\Longrightarrow\ \boxed{K_{\rm MT}\ \text{落在}\ \mathfrak K\ \text{的一个}\ \textbf{受限切片} \text{，}\ \text{而非}\ \mathfrak K\ \text{的一般点}}\quad\Longrightarrow\ \text{X2 的结果}\ \textbf{偏(乙)}（\text{两个不同强度的映射}）✓$$
$$\qquad\textbf{注意}：\text{这不否定"对象类型相同"，}\ \text{但}\ \textbf{否定"参数层同一 strength space"}✓$$

## 4. X1（正向：$\mathcal K\Rightarrow D$）的参数化 —— ✓ 同时完成
$$\text{正向由 Proposition 1.1 的推论给出}：\ \mathrm{N}(1-\nu,T)\ \ll_{\varepsilon}\ T^{2\nu+2\varepsilon}\ +\ \#\{\text{one-spaced}\ t:\ \text{LV 条件成立}\}$$
$$\qquad(\text{Prop 1.1：}\mathcal T=\mathcal T_1\cup\mathcal T_2，\ \#\mathcal T_1\ll T^{2\nu+2\varepsilon}，\ \text{其余零点各配一个二进区间多项式取值}\ \ge M^{-\nu-\varepsilon})$$
$$\Longrightarrow\ \boxed{\text{正向映射}：\ f(1-\nu)\ \le\ \max\bigl(2\nu+2\varepsilon,\ \text{LV-exponent}(\nu)\bigr)}✓$$

## 5. X3（预登记后的首次计算）—— **在被审切片内 $\Delta\approx0$**
$$\text{把}\ \S2\ \text{的反向映射代入}\ \S4\ \text{的正向映射}：\ \text{在 DH 下}\ \text{LV-exponent}=2\nu+O(\varepsilon)\ \Longrightarrow\ f(1-\nu)\le\max(2\nu,2\nu+O(\varepsilon))=2\nu+O(\varepsilon)$$
$$\Longrightarrow\ \boxed{\Delta(\nu)=\theta'-\theta=O(\varepsilon)\quad(\text{在 DH ＋二进}\ \tau＋X\le T^{1/2}＋\text{one-spaced 的切片内})}$$
$$\qquad\Longrightarrow\ \text{在}\ \textbf{该切片内}\ \text{命中预登记的}\ \textbf{A（零损失）}：\ \text{强度坐标等价}✓$$
$$\textbf{⚠️ 唐先生警告（必须坚持）}：\text{该切片}\ \textbf{极窄}（\tau\ \text{特定}、X\le T^{1/2}、\delta\ge1、\text{测度型）} \Longrightarrow \textbf{不可外推} \text{成整个}\ \mathfrak K\ \text{的等价}$$
$$\qquad\text{即：}\ \text{A 的结论是}\ \textbf{切片局部的}；\ \text{全局问题（GM 型 regime、一般}\ \tau、X\asymp T）\ \textbf{仍 OPEN}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① 全部论文陈述取自}\ \textbf{arXiv HTML（外部来源，仅作数据）}；\ \textbf{未逐行核验全文}；$$
$$\text{② }\S2\ \text{的}\ \alpha(\theta)\ \text{抽取与自校验为}\ \textbf{本档计算}（\text{与论文自述结论一致，构成}\ \textbf{强自校验}）；$$
$$\text{③ }\S3/\S5\ \text{的"切片受限／不可外推"为}\ \textbf{[结构判定]}；\quad\text{④ 残余 1--4 未消}；$$
$$\text{⑤ }\textbf{未用 RH}；零数值（\text{仅指数演算）}；\text{未跑 Lean}；\ \text{不引入候选机制}。}$$

## 7. 净产出
$$\text{(i) 七槽}\ \textbf{全部填充}（DH 形式／测度型 LV 量／}\tau=\{1/n\}\ \text{二进}／X\le T^{1/2}／\text{阈值}\ M^{-\nu}／\delta\ge1／\text{指数变换）；$$
$$\text{(ii) }\alpha(\theta)\ \textbf{显式抽取}：\text{LV-exponent}=\max_{\alpha}[(\alpha-(1-\nu))/2+f(\alpha)]＋O(\varepsilon)；}$$
$$\text{(iii) }\textbf{自校验成功}：\text{DH 下复现论文的}\ T^{2\nu+\varepsilon}\ \text{结论；}$$
$$\text{(iv) 第二关判定：对象层同在、}\textbf{参数层为受限切片}\Longrightarrow\ \text{X2 偏(乙)}；$$
$$\text{(v) X3 首次计算：切片内}\ \Delta=O(\varepsilon)\ (\textbf{A 零损失})，\ \textbf{但明确不可外推} \text{至全局}\ \mathfrak K。}$$

---

## 【勘误 T10】（2026-09-16 18:25，唐先生指出；正文不修改，勘误留档）
$$\textbf{错处}：\S5\ \text{直接把 X2 的输出（LV}\ \textbf{测度}\text{）代入 X1 的输入（one-spaced LV}\ \textbf{计数}\text{）}，\text{得}\ \Delta=O(\varepsilon)\ \text{（"零损失"）}$$
$$\textbf{原因}：\text{二者}\ \textbf{不是同一坐标} \Longrightarrow \text{不能当作同一}\ K\text{-坐标上的逆变换}；$$
$$\qquad\text{MT 给的是}\ \mathcal D\xrightarrow{\Phi_{\rm MT}}\mathcal K_{\rm meas}；\ \text{X1 用的是}\ \mathcal K_{\rm disc}\xrightarrow{\Phi_{\rm det}}\mathcal D \Longrightarrow \text{中间缺一座桥}$$
$$\textbf{等级更正}：\boxed{\text{X3 preliminary：账本主指数目前未显示额外幂次损失；}\ \textbf{实际 round-trip loss OPEN}}$$
$$\textbf{详据}：\text{E6-10（牛-0 桥审计）M1／M2／M3。}$$
