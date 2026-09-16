# 猎-1B — **B0：$S_{A,M,N}\to R_{\rm GM}$ 严格可嵌入审计**

> 唐先生 2026-09-16 19:42 拍板：开猎-1B，但**第一刀不是算 $\rho$**，而是判定
> $$\boxed{\text{GM 的 scalar-LV 形式能否覆盖 BCR 的 Kloosterman 非对角块}}$$
> 判死点：**H3-A 结构根本不匹配／H3-B 可降维但收益被吃掉／H1 真接口**。
> **纪律**：$\textbf{只允许不等式，不允许"看起来像"}$ ✓

---

## 1. BCR 的核心对象与延伸机制（唐先生引文，本档未逐行核验）
$$S_{A,M,N}=\sum_a\sum_{(m,n)=1}\nu_a\alpha_m\beta_n\,e\!\left(\frac{a\bar m}{n}\right)\quad(\textbf{Kloosterman-fraction 三线性和})$$
$$\textbf{参数化（BCR）}：\ \theta<\frac12+\frac{0.5-r}{1+2(r+2t)}\quad(\text{输入＝Kloosterman 指数}\ (r,t))$$
$$\qquad(r,t)=\left(\tfrac{23}{48},\tfrac12\right)\ \text{对应 DFI}；\ (r,t)=\left(\tfrac9{20},\tfrac7{20}\right)\ \text{对应 Bettin--Chandee}；\ \textbf{猜想型 Kloosterman} \Longrightarrow \theta<1✓$$
$$\Longrightarrow\ \boxed{\text{墙 A 的历史运动＝"提高 Kloosterman 抵消}\to\text{扩大 mollifier 长度"}} \quad(\textbf{不是} \text{"提高 generic LV}\to\text{自动扩大 mollifier"})✓$$
$$\qquad\text{并记录：猜想型 Kloosterman}\Longrightarrow\theta<1 \Longrightarrow \text{Lindelöf}\ (\textbf{但}\ \textbf{仍}\ne\mathrm{RH})$$

## 2. B0 审计：三种降维尝试与失败点
$$\textbf{尝试 (i) Cauchy--Schwarz}：\ |S|^{2}\le\Bigl(\sum|\nu_a|^{2}\Bigr)\Bigl(\sum_a\Bigl|\sum_{(m,n)}\alpha_m\beta_n e(a\bar m/n)\Bigr|^{2}\Bigr)$$
$$\qquad\Longrightarrow\ \text{得到}\ a\text{-变量的}\ \textbf{L}^2\ \text{量，}\ \textbf{不是} \text{大值点数；且内层仍是 Kloosterman 型} \Longrightarrow \textbf{不产生}\ R_{\rm GM}✗$$
$$\textbf{尝试 (ii) 丢相位（绝对值化）}：\ \Bigl|\sum \nu_a\alpha_m\beta_n e(a\bar m/n)\Bigr|\le\sum|\nu_a\alpha_m\beta_n| \Longrightarrow \textbf{相位信息全失}，\text{只余计数} \Longrightarrow \textbf{不可能恢复 GM 收益}✗$$
$$\textbf{尝试 (iii) 压成 scalar}：\ \text{把多变量和压成}\ \sum b_nn^{it_r}\ \text{需先}\ \textbf{创造} \text{一个}\ t\text{-参数}$$

## 3. ⭐ 决定性结构事实（H3-A 的根据）
$$S_{A,M,N}\ \textbf{根本不含}\ t\ \text{变量}：\ \text{它是}\ (a,m,n)\ \text{上的}\ \textbf{有限算术和}$$
$$R_{\rm GM}=\#\{t_r\in[0,T]:\ \bigl|\sum b_nn^{it_r}\bigr|\ge V\}\ \text{的全部内容}\ \textbf{就是}\ t_r\ \text{的分布}$$
$$\Longrightarrow\ \text{两者在}\ \textbf{对象层面异类}：\ \text{一个无}\ t，\ \text{一个全在}\ t✓$$
$$\textbf{唯一的转换通道＝对偶装置}：\ \text{Kuznetsov／Poisson／Voronoi} \Longrightarrow \text{相位结构在}\ \textbf{对偶后被改写}$$
$$\qquad\text{而 GM 的假设（}|b_n|\le1，\ t_r\ \textbf{1-separated}\text{）是关于}\ \textbf{原变量侧} \text{的结构} \Longrightarrow \textbf{对偶后不能自动继承}✓$$
$$\textbf{更硬的旁证}：\ \text{BCR 的}\ \theta\ \text{公式}\ \textbf{只以 Kloosterman 指数}\ (r,t)\ \text{为参数}，\ \textbf{没有} \text{LV-输入的槽位}；$$
$$\qquad\text{且历史上}\ \theta\ \text{的每次推进都对应}\ (r,t)\ \text{改善} \Longrightarrow \textbf{结构上不存在"用 LV 估计换}\ \theta\ \text{"的接口}✓$$

## 4. 判定：**H3-A（结构根本不匹配）**
$$\boxed{\text{GM 接口}\ \textbf{DEAD}}\quad(\text{非 H2 的阈值问题，而是}\ \textbf{相位／对象类型} \text{问题})$$
$$\boxed{G\ \text{墙}\ \textbf{仍 ALIVE}}：\ \text{其下一件工具必须}\ \textbf{保留 Kloosterman／shifted-correlation 结构}✓$$
$$\qquad\textbf{唐先生的判别（采纳）}：\ \text{"失败于相位保留}\ne\text{失败于阈值"}\ ——\ \text{本档属}\ \textbf{前者}✓$$

## 5. ⭐ 由此得到今日一条干净的新结论
$$\boxed{\text{GM 的}\ N^{3/4}\ \text{新机器确实推进了 large-value 墙，}\ \textbf{但它不攻击 mollifier 非对角墙；两墙是不同机制}}$$
$$\Longrightarrow\ \text{与核-甲1（墙 A 算术输入依赖型 vs 墙 B 解析域型）}\ \textbf{互相印证}：\ \text{今日共得}\ \textbf{三条机制上不同的墙}✓$$
$$\qquad\text{(i) 墙 B：}\lambda\le1\ \text{（MV 解析域，算术-free）}；\ \text{(ii) 墙 A：mollifier 非对角（}\textbf{Kloosterman 结构}）$$
$$\qquad\text{(iii) GM 的 large-value 临界（}\rho\approx0.75\ \text{高阈值区）——}\text{与 (ii)}\ \textbf{对象异类}✓$$

## 6. 猎-1 的结账与未完成项
$$\textbf{已完成}：\text{(a) 接口形式}\ \mathcal E_G\lesssim\sum W_\nu R(N_\nu,V_\nu,T_\nu) \text{（猎-1A）}；\ \text{(b) B0 判定 H3-A（本档）}$$
$$\textbf{未完成（不在本档范围）}：\ \rho_\nu\ \text{计算}\ \textbf{已无必要} \text{（B0 已失败）}✓$$
$$\textbf{仍可做（若唐先生要）}：\ (K)\ \text{侧天花板审计（Kloosterman／谱型输入还剩多少空间）——其唯一已知上限为猜想型 Kloosterman（}\Longrightarrow\theta<1\Longrightarrow\text{Lindelöf）}$$

## 7. 边界（N1/N2 严守）
$$\text{① BCR 的对象、}\theta\ \text{公式与}\ (r,t)\ \text{输入均为}\ \textbf{唐先生提供的引文，本档未逐行核验}；$$
$$\text{② §2／§3 的降维失败为}\ \textbf{结构性论证}（\text{非形式化证明）}；\quad\text{③ }\textbf{未用 RH}；零数值（\text{仅指数演算）}✓$$

## 8. 净产出
$$\text{(i) BCR 核心对象}\ S_{A,M,N}\ \text{与其}\ \theta\ \text{参数化（Kloosterman 指数}\ (r,t)\ \text{驱动）}；$$
$$\text{(ii) B0 三种降维尝试的失败点（Cauchy--Schwarz／丢相位／压 scalar）}；$$
$$\text{(iii) ⭐ 决定性结构事实：}\ S\ \textbf{无}\ t\ \text{变量，}\ R_{\rm GM}\ \text{全在}\ t \Longrightarrow \textbf{对象异类}；对偶不能自动继承 GM 假设；}$$
$$\text{(iv) 判定}\ \textbf{H3-A}：\text{GM 接口 DEAD（相位／类型问题，非阈值问题）}；\ G\ \text{墙 ALIVE}；$$
$$\text{(v) 干净新结论：GM 的}\ N^{3/4}\ \text{机器与 mollifier 非对角墙}\ \textbf{机制不同；今日共得三条不同机制的墙}。}$$
