# 甲-1A — **$3/4$ 临界机制解剖**：它是**代数交叉点**，不是几何障碍

> 唐先生 2026-09-16 19:30 拍板：开甲，**直接打结构性临界点**；顺序 甲-1A→1B→1C，不许跳。
> 取证：Guth–Maynard, *New large value estimates for Dirichlet polynomials*（arXiv:2405.20552；Annals 2026 正式发表）—— **外部来源，仅作数据**；本档只取引言层＋定理陈述层。
> **纪律**：不得把"GM 移动了墙"等同于"$\lambda$ 被推到 $>1$"（E6 未建立两坐标映射）✓

---

## 1. GM 定理 1.1（原文陈述，数据引用）
$$\textbf{Thm 1.1}：|b_n|\le1，\ (t_r)_{r\le R}\subset[0,T]\ \text{为}\ \textbf{1-separated}，\ \Bigl|\sum_{n=N}^{2N}b_nn^{it_r}\Bigr|\ge V\ \ \forall r\le R \Longrightarrow$$
$$\boxed{R\ \le\ T^{o(1)}\Bigl(\underbrace{N^{2}V^{-2}}_{\text{对角／MVT}}\ +\ \underbrace{N^{18/5}V^{-4}}_{\text{新项 A}}\ +\ \underbrace{T\,N^{12/5}V^{-4}}_{\text{新项 B}}\Bigr)}$$
$$\textbf{前最佳（MVT＋Montgomery--Halász--Huxley，式 (1.1)）}：\ R\le T^{o(1)}\Bigl(N^{2}V^{-2}+T\min\bigl(NV^{-2},\ N^{4}V^{-6}\bigr)\Bigr)$$

## 2. ⭐ 甲-1A 的核心答案：$3/4$ 是**代数交叉**，不是几何障碍
$$\textbf{关键恒等式（本档计算）}：\ \min(NV^{-2},\ N^{4}V^{-6})\ \text{的两项在}\quad N^{4}V^{-6}=NV^{-2}\iff N^{3}=V^{4}\iff\boxed{V=N^{3/4}}\ \text{处相等}$$
$$\Longrightarrow\ \textbf{临界}\ \sigma=3/4\ (\text{即}\ V=N^{\sigma}=N^{3/4})\ \textbf{就是经典两项的交叉点}✓$$
$$\textbf{同理 GM 新项与邻项的交叉点（本档计算）}：$$
$$\qquad N^{18/5}V^{-4}\ =\ N^{2}V^{-2}\iff V^{2}=N^{8/5}\iff V=N^{4/5}\ (=N^{8/10})$$
$$\qquad N^{18/5}V^{-4}\ \text{在}\ V=N^{3/4}\ \text{处给出}\ N^{18/5}N^{-3}=N^{3/5}\quad(\text{与原文"GM 给出约}\ N^{3/5}+TN^{-3/5}\text{"一致}\ ✓\ \text{自校验通过})$$
$$\qquad TN^{12/5}V^{-4}\ \text{在}\ N=T^{4/5},\,V=N^{3/4}\ \text{处给出}\ T\,N^{-3/5}=T^{1-12/25}=T^{13/25}\quad(\text{与原文}\ T^{13/25}\ \text{一致}\ ✓✓)$$
$$\Longrightarrow\ \boxed{\text{整个"临界"结构＝指数记账：}3/4\ \text{来自}\ N^{3}=V^{4}；\ 3/5\ \text{来自}\ T N^{-1/2}\ (N=T^{4/5})；\ 13/25\ \text{来自}\ T N^{-3/5}}$$
$$\qquad\textbf{结论}：\ \text{没有任何"几何／维数／正交性障碍"在产生}\ 3/4 \Longrightarrow \textbf{3/4 是可移动的记账产物}$$

## 3. 由此得到墙的**正面表述**（甲-1A 的实质产出）
$$\text{墙}\ =\ \boxed{\text{"当前可证项"的}\ \textbf{有效范围}\ (V\ \text{区间})}；\ \text{GM 的贡献＝}\text{证出一个}\ \textbf{有效范围更宽} \text{的新项}$$
$$\qquad(\text{GM 比较：}\ V<N^{7/10}\ \text{或}\ V>N^{8/10}\ \text{时旧界至少不弱；GM 在}\ N^{7/10}<V<N^{4/5}\ \text{取胜})$$
$$\Longrightarrow\ \textbf{移动临界点＝证出在小}\ V\ \text{区有效的新项}\ (V\ll N^{3/4})✓$$

## 4. ⭐ 但小 $V$ 区有一个**真正的硬墙（性质完全不同）**
$$\text{RH 需要}\ \sigma\to\tfrac12 \Longrightarrow V=N^{\sigma}\approx N^{1/2}\quad(\text{“小 }V\text{ 区”})$$
$$\textbf{该区的真实性态}：\ \text{长度}\ N\ \text{的多项式在单点的}\ \textbf{典型量级} \text{为}\ N^{1/2} \Longrightarrow V\approx N^{1/2}\ \text{时}\ \text{“大于}\ V\text{”是}\ \textbf{典型行为，不是稀有事件}}$$
$$\qquad\Longrightarrow\ \text{此时点数}\ R\ \text{可逼近}\ \textbf{平凡上界}\ T \Longrightarrow \textbf{不存在计数型节省}✓$$
$$\textbf{验证（本档计算）}：\text{经典界在}\ V=N^{1/2}\ \text{处给}\ N^{2}V^{-2}=N\ \text{与}\ T\,N\,V^{-2}=T \Longrightarrow R\le T\ (\text{平凡})✓$$
$$\Longrightarrow\ \boxed{\text{large-values 路线的密度结果}\ \textbf{在}\ \sigma\to\tfrac12\ \text{时必定退化}}\quad(\text{与 E5 型 I 的机制天花板一致，但现在有}\ \textbf{定量根因})✓$$
$$\qquad\textbf{这是正面硬墙（非 NO-GO）：}\text{它说明该路线的天花板来自}\ \textbf{典型量级与阈值的重合}，\ \textbf{不是技术不足}✓$$

## 5. 甲-1B／1C 的精确提法（唐先生指定，本档只定位不改写）
$$\textbf{甲-1B}：\text{一般 extremiser 的结构}——在}\ V\approx N^{1/2}\ \text{区，极值构型是}\ \textbf{典型／随机型} \text{系数}$$
$$\textbf{甲-1C（关键）}：\ \boxed{\zeta\ \text{的系数结构能否}\ \textbf{排除} \text{该 extremiser}？}$$
$$\qquad\zeta\ \text{的系数（Möbius／Dirichlet 型）}\ \textbf{不是}\ \text{典型型，而带}\ \textbf{算术结构} \Longrightarrow \text{问题＝}\ \tau\ \text{（系数类）依赖性}$$
$$\qquad\textbf{此时目标不是"更强的一般大值估计"，而是}\ \boxed{\zeta\text{-special arithmetic exclusion}}\ :\ \text{一般 extremiser}\ \notin\ \zeta\text{-admissible class}✓$$
$$\qquad\textbf{且这与 RH 的关系是}\ \textbf{间接} \text{的：它只可能改善 density exponent，}\ \textbf{不能} \text{直接证 RH（除非另建映射）}✓$$

## 6. 边界（N1/N2 严守）
$$\text{① GM 陈述取自公开检索片段（外部来源）}\ \textbf{未逐行核验全文}；\quad\text{② §2／§4 的指数计算为}\ \textbf{本档计算}（\text{已自校验两项与原文一致}）✓$$
$$\text{③ §4 的"典型量级"论证为}\ \textbf{[结构判定]}，\ \textbf{未} \text{引用定理}；\quad\text{④ }\textbf{未用 RH}；零数值（\text{仅指数演算}）✓$$

## 7. 净产出
$$\text{(i) GM Thm 1.1 与前最佳 (1.1) 的精确形式（含 GM 的两个新项）；}$$
$$\text{(ii) ⭐ 核心答案：}\ 3/4\ \textbf{＝}\ N^{3}=V^{4}\ \text{的}\ \textbf{代数交叉}，\ \text{非几何障碍（可移动）}；$$
$$\text{(iii) 自校验：}N^{3/5}／T^{13/25}\ \text{与原文数字一致} ⟹ \text{解剖正确}；$$
$$\text{(iv) 墙的正面表述＝当前可证项的}\ \textbf{有效范围}；\ \text{移动临界点＝在小}\ V\ \text{区证出新项；}$$
$$\text{(v) ⭐ 小}\ V\ \text{区的真硬墙：}\ V\approx N^{1/2}\ \text{是}\ \textbf{典型量级}，\ \text{平凡上界}\ R\le T\ \text{近似达到} \Longrightarrow \text{large-values 路线在}\ \sigma\to\tfrac12\ \textbf{必退化}；$$
$$\text{(vi) 甲-1C 的精确提法：}\zeta\ \text{系数（}\tau\text{）能否排除一般 extremiser} \Longrightarrow \zeta\text{-special arithmetic exclusion}。}$$
