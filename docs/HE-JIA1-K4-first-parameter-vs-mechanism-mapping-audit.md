# 核-甲1 — **K4 先行**：$\theta_{\rm moll}$ vs $\lambda_{\rm V316}$ 的参数映射／机制映射审计

> 唐先生 2026-09-16 19:36 拍板：做核-甲1，**先查 K4，再查 K1--K3**。
> **先纠正（唐先生，权威资料）**：$\theta=\tfrac12$ **是历史技术屏障，不是普适平方根硬墙** ✓
> $$\text{Levinson：}\theta<\tfrac12\ \longrightarrow\ \text{Conrey：}\theta<\tfrac47\ \longrightarrow\ \text{进一步算术输入：}\theta=\tfrac9{17}>\tfrac12$$
> **故癸-甲2A 的"平方根型屏障"须降级为}\ \textbf{历史技术屏障}，不得作结构定理✓**

---

## K4（先行）：为什么文献已有 $\theta>1/2$，V316 的 $\lambda\le1$ 仍成立？
$$\textbf{答（本档计算）}：\ \text{二者并不矛盾，因为}\ \theta>1/2\ \text{仍}\ \textbf{远小于}\ 1$$
$$\theta_{\rm Conrey}=\tfrac47\approx0.571；\ \theta=\tfrac9{17}\approx0.529\ \Longrightarrow\ \textbf{均在}\ \theta<1\ \text{之内}✓$$
$$\text{若把二者都读作"载体长度}\div T\ \text{（对数尺度）"}：\ \theta=\frac{\log y}{\log T},\ \lambda=\frac{\log X}{\log T}$$
$$\Longrightarrow\ \text{历史瓶颈}\ \tfrac12\ \text{是}\ \textbf{Levinson 论证的技术限制}，\ \text{不是}\ X\le T\ \text{的结构边界；}\ \textbf{结构边界在}\ \theta=1✓$$
$$\Longrightarrow\ \boxed{\text{K4 解决}：\ \text{无矛盾}；\ \text{但因此}\ \textbf{不得} \text{拿历史的}\ \theta=\tfrac12\ \text{去硬配}\ \lambda=1✓}$$

## K1 — 参数映射 $\lambda=F(\theta,\text{carrier data})$？
$$\text{候选阅读（本档提出）}：\ \text{两者同为}\ \textbf{"载体长度}\div T\text{"的对数比} \Longrightarrow \text{同}\ \textbf{类型} \text{的参数}$$
$$\qquad\text{但}\ \textbf{归一化不同}：\theta\ \text{以}\ T\ \text{为基准（}\log y/\log T\text{）；}\lambda\ \text{以}\ L\ \text{为基准（V316 的}\lambda=L/\ell_1\ \text{型）}$$
$$\Longrightarrow\ \textbf{K1 判定}：\ \textbf{未建立显式映射}（\text{仅有"同类型"观察}）\ \Longrightarrow\ \text{不得写}\ \theta=\lambda\ \text{或}\ \theta>1\iff\lambda>1✓$$

## K2 — 机制映射 $\mathsf C_{\rm moll}(\theta)\iff\mathsf C_{\rm var}(\lambda)$？
$$\text{mollifier 侧}\ \mathsf C_{\rm moll}：\text{被mollified 矩的渐近公式可闭合}；\ \text{V316 侧}\ \mathsf C_{\rm var}：Q_\lambda\ \text{获严格 gap／coercivity}$$
$$\textbf{决定性差异（本档判定）}：$$
$$\qquad\text{(i) mollifier 的}\ \theta\ \text{天花板}\ \textbf{依赖算术输入}（\text{Kloosterman 和、Vaughan identity 等}\ \text{可延长}\ \theta）——\ \text{唐先生指出，且文献支持✓$$
$$\qquad\text{(ii) V316 的}\ \lambda\le1\ \text{来自}\ \textbf{MV／均值域}\（\log X\le L\iff X\le T\text{）——}\ \text{而 V300 已证 MV 输入}\ \textbf{不含算术内容}（\text{纯调和分析}）✓$$
$$\Longrightarrow\ \boxed{\text{K2：}\textbf{未建立}；且存在}\ \textbf{机制不同的正面证据}（\text{算术输入依赖}\ \text{vs}\ \text{解析域约束）✓$$

## K3 — 临界点映射 $\theta_{\rm crit}\leftrightarrow\lambda_{\rm crit}=1$？
$$\text{若同墙，须解释}\ \theta_{\rm crit}\leftrightarrow\lambda_{\rm crit}=1；\ \text{但}\ \text{K4 已示历史}\ \theta=\tfrac12\ \textbf{不可} \text{硬配}\ \lambda=1$$
$$\Longrightarrow\ \textbf{K3：未建立}（\text{缺临界点对应}）✓$$

---

## 判定：**两个不同的承重机制**（唐先生预判的第二种分支）
$$\text{K4}\ \textbf{解决}（\text{无矛盾}）；\ \text{K1}\ \textbf{未建立}（\text{仅同类型"}）；\ \text{K2}\ \textbf{未建立＋有机制差异证据}；\ \text{K3}\ \textbf{未建立}$$
$$\Longrightarrow\ \boxed{\text{"显式映射不存在／机制不等价"} \Longrightarrow \text{得到两个真正不同的墙}}✓$$
$$\qquad\textbf{唐先生判断（采纳）}：\text{"这比强行证明它们相同更重要"}✓$$
$$\text{故}\ \Gamma_w\ \text{与}\ \lambda\ \text{的关系应为}：\ \boxed{\text{形状相似（同为"载体强度"型参数），机制不等价}}✓$$

## 【勘误 T10】对癸-甲2A（正文不修改）
$$\textbf{错处 1}：\S3\ \text{称}\ \Gamma_w\le1\iff\text{"平方根型屏障"} \Longrightarrow \textbf{降级为}\ \textbf{历史技术屏障}（\text{Levinson}\ \theta<1/2\ \text{已被 Conrey}\ 4/7\ \text{与}\ 9/17\ \text{超越}）$$
$$\textbf{错处 2}：\S4\ \text{称}\ \Gamma_w\ \textbf{候选同一} \text{于 V316 的}\ \lambda \Longrightarrow \textbf{降级为"尚未建立"}（\text{仅同类型观察}）$$
$$\textbf{保留}：\Gamma\leftrightarrow\theta\ \textbf{有结构类比}；\ \text{整体缩放恒等（§1）与三者链动（§2）}\ \textbf{不受影响}✓$$

## 由此得到的正面结论（本档新信息，非 NO-GO）
$$\boxed{\text{今天的审计第一次给出}\ \textbf{两个机制上不同的承重墙}}\：$$
$$\qquad\text{(墙 A)}\ \textbf{算术输入依赖型}：\theta_{\rm moll}\ \text{型——可被 Kloosterman／Vaughan 等算术输入延长}；$$
$$\qquad\text{(墙 B)}\ \textbf{解析域约束型}：\lambda\le1\ \text{型——来自 MV 均值域（}\log X\le L\ \text{，算术-free）}$$
$$\Longrightarrow\ \text{这解释了为什么}\ \text{"改进算术输入"}\ \text{与}\ \text{"改进解析估计"}\ \text{是}\ \textbf{两条不同路线}，\ \text{而非同一堵墙的两面}✓$$

## 边界（N1/N2 严守）
$$\text{① K1--K3 的"未建立"＝}\textbf{未证}，\ \textbf{非"已证不同"}；\quad\text{② §K2 的"机制差异证据"为}\ \textbf{[结构判定]}；$$
$$\text{③ 文献引文（Levinson／Conrey／9/17）为}\ \textbf{唐先生提供的权威资料，本档未逐行重验}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}✓$$

## 净产出
$$\text{(i) K4 先行并解决：}\theta>1/2\ \text{但}\ \theta<1 \Longrightarrow \text{与}\ \lambda\le1\ \textbf{无矛盾}（\text{历史}\ \tfrac12\ \text{不可硬配}\ \lambda=1）✓$$
$$\text{(ii) K1／K2／K3 皆}\ \textbf{未建立}：\text{仅"同类型"（长度/T 的对数比）；机制不同（算术输入依赖 vs 解析域）}；$$
$$\text{(iii) 勘误 T10：两处降级（平方根}\to\text{历史技术屏障；Γ}\leftrightarrow\lambda\ \text{候选同一}\to\text{尚未建立）}；$$
$$\text{(iv) ⭐ 正面结论：}\textbf{两个机制不同的承重墙}（算术输入依赖型 vs 解析域约束型）——\text{解释了两条路线的真正差别}；$$
$$\text{(v) 保留：}\Gamma\leftrightarrow\theta\ \text{结构类比；整体缩放恒等与三者链动}
