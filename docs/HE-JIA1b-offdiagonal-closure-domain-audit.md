# 核-甲1b — **非对角闭合域审计**（$\theta$ 可推到哪里？）

> 唐先生 2026-09-16 19:38 拍板：开核-甲1b；**不做 V3，不碰 V316，不优化 $\Gamma_w$**。
> 目标（唐先生指定）：$$\boxed{\textbf{Kloosterman／非对角算术输入究竟还能把 mollifier 的闭合长度推进多远？}}$$
> **防偷换铁律**：$$\boxed{\text{mollifier length improvement}\ \ne\ \mathrm{RH}}$$（$\theta$ 改善首先改善的是 mollified moment／Levinson 型零点比例；接到 RH 须另建映射 $\theta\to100\%$ zeros）✓
> **任务**：(1) 重建 $\tfrac12\to\tfrac47$；(2) 检查 $\tfrac47\to1$；(3) 判定 $\theta=1$。

---

## 0. 载体与展开（唐先生形式）
$$V(s)=\sum_{n\le y}\frac{\mu(n)}{n^{s}}P\!\left(\frac{\log(y/n)}{\log y}\right),\qquad y=T^{\theta}$$
$$\int_T^{2T}|V(s)M(s)|^{2}dt\ \longrightarrow\ \sum_{m,n}\frac{a_m\overline{a_n}}{(mn)^{1/2}}\int_T^{2T}\left(\frac mn\right)^{it}dt$$
$$\textbf{对角}\ (m=n)：\text{主项}；\qquad \textbf{非对角}\ (m\ne n)：\ \int_T^{2T}(m/n)^{it}dt=\frac{(m/n)^{i2T}-(m/n)^{iT}}{i\log(m/n)} \Longrightarrow\ \textbf{尺度}\ \frac{T}{|\log(m/n)|}$$
$$\Longrightarrow\ \boxed{\theta\ \text{的推进}＝\text{允许更长的}\ m,n \Longrightarrow \text{须控制更长／更复杂的非对角项}}✓\quad(\text{这解释了 Kloosterman 技术为何能移动}\ \tfrac12\to\tfrac47)$$

## 任务 1 — 重建 $\tfrac12\to\tfrac47$（**变化的是哪一类非对角估计**）
$$\text{非对角项按几何位置}\ \textbf{三分}：$$
$$\qquad\textbf{(N) 近对角}：m-n\ \text{小}\ (\text{化为 divisor／}\sum_{d}\text{型和})$$
$$\qquad\textbf{(K) Farey／小分母}：m/n\ \text{接近有理数}\ a/q\ \text{且}\ q\ \text{小} \Longrightarrow \textbf{Kloosterman 和} \Longrightarrow\ \text{Deshouillers--Iwaniec 型估计}$$
$$\qquad\textbf{(G) 一般（minor arc）}：\textbf{大筛／Bombieri--Vinogradov 型}$$
$$\textbf{历史判断（本档 [结构判定]，依据唐先生提供的权威引文）}：$$
$$\qquad\text{Levinson}\ \theta<\tfrac12：\ \text{(G) 部分用}\ \textbf{经典大筛} \text{即可闭合}$$
$$\qquad\text{Conrey}\ \theta<\tfrac47：\ \text{突破归因于}\ \textbf{Deshouillers--Iwaniec 的 Kloosterman 和平均估计} \Longrightarrow \textbf{(K) 段被加强}$$
$$\qquad\text{进一步}\ \theta=9/17：\ \text{更多}\ \textbf{算术输入} \text{（Vaughan identity 型等）}$$
$$\Longrightarrow\ \textbf{结论}：\ \theta\ \text{每次推进，都对应}\ \textbf{某一类非对角估计被更强的算术输入替换}✓$$

## 任务 2 — 检查 $\tfrac47\to1$：把所需条件写成明确不等式／指数条件
$$\textbf{闭合判据}：\ \text{非对角总额}\ \mathcal E(\theta)=o(T)\ \text{（或不足以破坏主项渐近）} \Longrightarrow\ \boxed{\Theta_{\rm closure}=\sup\{\theta:\mathcal E(\theta)=o(T)\}}$$
$$\text{三段各自需达到的}\ \textbf{指数型条件（本档结构形式；常数须由文献定）}：$$
$$\qquad\text{(N)}\ \text{近对角和需}\ \textbf{divisor 型次幂节省}：\ \sum_{|h|\le H}\frac{\tau(\cdot)}{|h|}\text{型}\ \ll y^{1-\eta}\ (\eta>0\ \text{随}\ \theta\uparrow1\ \text{须}\to\ \text{更大})$$
$$\qquad\text{(K)}\ \text{Kloosterman 段需}\ \textbf{Kuznetsov／谱型} \text{界，且其节省须}\ \textbf{随}\ y\ \text{增大而保持}$$（Deshouillers--Iwaniec 型：\ $\sum_{q\le Q}\sum_{a}\text{Kl}(...)\ll$ 次幂节省）
$$\qquad\text{(G)}\ \textbf{瓶颈所在}：\ \text{一般情形需}\ \textbf{大筛的次幂改进}；经典大筛给}\ 1/\sqrt{N}\ \text{型节省，}\ \textbf{而}\ \theta\uparrow1\ \text{要求超越它}$$
$$\Longrightarrow\ \boxed{\text{当}\ \theta\ \text{增大时，瓶颈从}\ (N)/(K)\ \textbf{迁移至}\ (G)\ \textbf{（一般非对角／大筛）}} \quad(\textbf{[结构判定]})✓$$
$$\qquad\textbf{历史一致性}：\text{每次}\ \theta\ \text{突破都来自}\ \textbf{(K) 或架构（多段）} \text{的加强，}\ \textbf{而非}\ (G)\ \text{的加强} \Longrightarrow \text{暗示}\ (G)\ \text{是更深的水位}✓$$

## 任务 3 — 判定 $\theta=1$（唐先生的三分支）
$$\textbf{关键事实（唐先生提供）}：\ \theta=1\ \textbf{不是} \text{目前可直接宣布的算术硬墙}；文献讨论过}\ \theta\ \text{不同范围与多段架构；且经典文献把}\ \theta=\infty\ \text{作为理想极限（若能实现即触及 RH）}$$
$$\Longrightarrow\ \text{因此三分支判定为}：$$
$$\qquad\text{(a) 可跨}\ \theta>1 \Longrightarrow \text{墙 A＝}\textbf{可破墙}；\quad\text{(b) 到}\ 1\ \text{卡住} \Longrightarrow \text{找}\ \textbf{算术临界机制}；\quad\text{(c) 早于}\ 1\ \text{卡住} \Longrightarrow \text{定位新指数墙}$$
$$\textbf{本档判定}：\ \boxed{\text{当前证据支持}\ \textbf{(a)/(b) 之间的"可推进墙"}}：$$
$$\qquad\text{(i) }\Theta_{\rm arith}>\tfrac12\ \textbf{已由文献确证}（\text{Levinson}\to\text{Conrey}\to9/17）⟹ \textbf{墙 A 是}\textbf{会动的墙}✓$$
$$\qquad\text{(ii) }\theta=1\ \textbf{未被证明是上限}；\ \text{文献把}\ \theta=\infty\ \text{当理想极限} \Longrightarrow \textbf{不得} \text{宣布}\ \theta=1\ \text{为算术硬墙}✓$$
$$\qquad\text{(iii) }\textbf{瓶颈已定位}：\ \theta\uparrow1\ \text{时}\ (G)\ \textbf{一般非对角／大筛} \text{成为限制项} ⟹ \textbf{下一个可攻的具体对象}✓$$

## ⭐ 判定与产出（本档实质结论）
$$\boxed{\text{墙 A（mollifier／非对角）＝}\textbf{可推进墙：其上限未定，且已被证明可由新算术输入移动}}$$
$$\qquad\text{对比}\ \text{墙 B（V316 的}\ \lambda\le1\text{）＝}\textbf{解析域约束型} \text{（MV 域，算术-free；V316-FREEZE §7／V317 已审为 DEAD）}$$
$$\Longrightarrow\ \boxed{\text{今日第一次得到一条}\ \textbf{与 V316 无关、且有明确可推进方向的活墙}} \Longrightarrow \text{这正是唐先生要找的}\ \textbf{活墙}✓$$
$$\textbf{下一个具体可攻对象（本档命名）}：\ (G)\ \textbf{一般非对角项（minor-arc／大筛段）的次幂改进} ——\ \text{因为在}\ \theta\uparrow1\ \text{时它是限制项}$$

## 边界（N1/N2 严守）
$$\text{① §任务 1 的历史归因（Deshouillers--Iwaniec / Vaughan）为}\ \textbf{唐先生提供的权威引文，本档未逐行核验}；$$
$$\text{② §任务 2 的三段指数条件为}\ \textbf{结构形式}（\text{未写具体常数——须由文献定）}；\quad\text{③ §任务 3 的判定为}\ \textbf{[结构判定]}，\ \textbf{未证} \text{任何上限；}$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}；\ \textbf{不碰 V316，不做 V3}✓$$

## 净产出
$$\text{(i) 非对角三分：}\ (N)\ \text{近对角／}(K)\ \text{Farey-Kloosterman／}(G)\ \text{一般（大筛）}；$$
$$\text{(ii) 任务 1：}\ \tfrac12\to\tfrac47\ \text{的实质＝}\textbf{(K) 段被 Kloosterman／谱型算术输入加强}；$$
$$\text{(iii) 任务 2：闭合判据}\ \mathcal E(\theta)=o(T)，\ \Theta_{\rm closure}=\sup\{\theta:\mathcal E(\theta)=o(T)\}；\ \textbf{瓶颈随}\ \theta\uparrow1\ \text{迁移到}\ (G)；$$
$$\text{(iv) 任务 3：}\ \theta=1\ \textbf{非已证硬墙}；\ \text{墙 A＝}\textbf{可推进墙}（\text{与墙 B 不同类）}；$$
$$\text{(v) 命名下一个可攻对象：}\ (G)\ \text{一般非对角／大筛段的次幂改进。}$$
