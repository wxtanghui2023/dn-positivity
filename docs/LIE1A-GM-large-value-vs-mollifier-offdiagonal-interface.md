# 猎-1A — **GM-large-value → mollifier off-diagonal interface**

> 唐先生 2026-09-16 19:40 拍板：开猎-1A（**不开猎-2**；**不做宽搜技术名词**）。
> 唯一问题：$$\boxed{\text{GM 2026 的大值估计，是否能严格压低 mollifier 非对角一般块}\ E_G\ ?}$$
> **两处校准（采纳）**：$\theta$ 的延伸有**两条不同路线**；$(G)$ 只是**候选**瓶颈，**不得**断言为已定瓶颈✓

---

## 0. 历史校正（唐先生提供，本档未逐行核验）
$$\text{路线 I}：\ \tfrac12\ \xrightarrow{\ \textbf{Kloosterman／trilinear forms}\ }\ \tfrac{17}{33}\quad(\text{Bettin--Chandee--Radziwiłł：}\textbf{一般 Dirichlet 多项式}\text{的 mollified second moment})$$
$$\text{路线 II}：\ \tfrac12\ \xrightarrow{\ \textbf{特殊 mollifier}\ +\ \text{Deshouillers--Iwaniec／Vaughan}\ }\ \tfrac47\quad(\text{Conrey})$$
$$\Longrightarrow\ \boxed{\text{两条}\ \textbf{不同的} \text{延伸路线} \Longrightarrow \text{不得把}\ \tfrac47\to\tfrac{17}{33}\ \text{读作"}(K)\to(G)\ \text{已被推进"}✓$$
$$\textbf{文献记录的}\ \theta\ \text{结构（唐先生引文）}：\theta<\tfrac12\ \text{仅用 diagonal}；\ \theta>\tfrac12\ \text{non-diagonal 出现}；\ \theta<1\ \text{＝著名}\ \theta=1\ \text{猜想}；\ \theta>1\ \text{完整一般公式}\ \textbf{失败}$$
$$\qquad\text{且：}\ \text{"The}\ \theta=\infty\ \text{conjecture implies RH"}（\text{Bettin 发表列表}）\Longrightarrow \text{推进链真实存在，但}\ \textbf{改善}\ \theta\ne\mathrm{RH}✓$$

## 1. 先把 $(G)$ 写死
$$\mathcal E(\theta)=E_N(\theta)+E_K(\theta)+E_G(\theta)；\ \text{要攻的是}\ \boxed{E_G(\theta)=o(T)}\ \text{的可达范围}$$
$$\textbf{（G) 的当前地位}：\ \text{候选瓶颈} \text{（历史突破全来自}(N)/(K)/\text{架构侧）}，\ \textbf{未证} \text{为最终瓶颈}✓$$

## 2. ⚠️ 防偷换铁律（唐先生指定）
$$\boxed{\text{Dirichlet-polynomial large values}\ \ne\ \text{mollified second-moment off-diagonal}}$$
$$\text{后者展开后是}\ (m,n,d,e)\ \text{等多重变量的}\ \textbf{相关和}；\ \text{GM 的 Thm 1.1 是对}\ \sum b_nn^{it_r}\ \text{的}\ \textbf{大值点数}\ R\ \text{给界}$$
$$\Longrightarrow\ \text{真正的接口}\ \textbf{不是} \text{"GM 很强}\to\text{可延长 mollifier"}，\ \textbf{而是}：\ \boxed{\text{GM large-value inequality}\ \Longrightarrow\ E_G(\theta)\ \text{的次幂下降}}\quad(\text{须}\ \textbf{算}，\text{无现成结论})✓$$

## 3. 接口计算的规定形式（唐先生指定）
$$\text{设经}\ \text{Vaughan／functional equation／dyadic decomposition}\ \text{后，某一般非对角块化为}\ \boxed{\mathcal E_G\lesssim\sum_\nu W_\nu R(N_\nu,V_\nu,T_\nu)}$$
$$\text{代入 GM：}\ \mathcal E_G\lesssim T^{o(1)}\sum_\nu W_\nu\Bigl(N_\nu^{2}V_\nu^{-2}+N_\nu^{18/5}V_\nu^{-4}+T_\nu N_\nu^{12/5}V_\nu^{-4}\Bigr)$$
$$\boxed{\textbf{突破判据}：\ \exists\ \text{一个原本导致}\ \mathcal E_G\ne o(T)\ \text{的 block，使 GM 代入后变成}\ o(T)}✓$$

## 4. ⭐ 决定性单项：阈值比的落点（唐先生指定先查）
$$\text{GM 的有效窗口（前言原文）}：\ \text{GM 强于经典界当}\ N^{7/10+\epsilon}<V<N^{8/10-\epsilon}\ \text{且}\ N\le T^{5/6-\epsilon}$$
$$\Longrightarrow\ \text{有效判据为}\ \textbf{阈值比}：\quad \boxed{\rho_\nu：＝\frac{\log V_\nu}{\log N_\nu}\in(0.7,\ 0.8)}\quad(\text{最优点}\ \rho\approx\tfrac34)✓$$
$$\textbf{要算的（本档注册）}：\ \theta\uparrow1\ \text{时，各主导}\ (G)\text{-block 的}\ \rho_\nu\ \text{落在何处}$$
$$\qquad\text{(i) 若某主导 block 满足}\ \rho_\nu\approx\tfrac34 \Longrightarrow \boxed{\text{GM 的}\ N^{3/4}\ \text{机器}\ \leftrightarrow\ \text{mollifier}\ G\text{-block 的临界几何}}\ \text{（真桥）}$$
$$\qquad\text{(ii) 若所有主导 block 满足}\ V_\nu\ll N_\nu^{3/4}\ \text{或}\ \gg N_\nu^{3/4} \Longrightarrow \textbf{GM 打不中 mollifier 墙}$$

## 5. 本档的结构性初判（[结构判定]，须以 §4 的计算确认或推翻）
$$\text{承接甲-1A §4 与甲-1C}：\ \text{经典非对角处理的阈值位于}\ \textbf{典型尺度附近}（V\asymp N^{1/2}\ \text{量级，即}\ \rho\approx\tfrac12）$$
$$\qquad\text{而 GM 的增益恰在}\ \textbf{高阈值区}（\rho\in(0.7,0.8)，最优}\ 0.75）$$
$$\Longrightarrow\ \boxed{\text{初判：}\textbf{阈值区错位} \Longrightarrow \text{H2／H3 更可能}（\text{GM 打不中）}}\quad(\textbf{须算，不得据此收兵})✓$$
$$\qquad\text{若此初判成立}：\ \text{则解释了"GM 移动了}\ 3/4\ \text{却不动}\ \sigma\to1/2" \Longrightarrow \text{与甲-1A §4 的"典型尺度重合"}\ \textbf{互相印证}✓$$

## 6. 三个判死点（唐先生指定）
$$\textbf{H1 可嵌入}：E_G\ \text{严格化为 GM 型大值问题且}\ \textbf{全部} \text{假设（系数／长度／阈值／spacing）满足} \Longrightarrow \textbf{ALIVE}$$
$$\textbf{H2 可嵌入但无净收益}：\ \text{代入后}\ E_G^{GM}\asymp E_G^{old}\ \text{或仅}\ T^{o(1)}\ \text{改善} \Longrightarrow \textbf{WALL}$$
$$\textbf{H3 类型不匹配}：\ \text{非对角项必须保留}\ \textbf{Kloosterman／shifted-convolution／多重相关结构}，\ \text{无法降为标量大值问题} \Longrightarrow \textbf{GM 路线 DEAD，但}\ G\ \text{墙仍活着}✓$$
$$\textbf{H3 的价值}：\ \text{它会精准告诉我们}\ \boxed{G\ \text{不是"需要更强的大值估计"，而是"需要保持算术相关结构的另一种工具"}}✓$$

## 7. 判定（本档诚实的落点）
$$\text{§4 的计算}\ \textbf{本档未能完成}（\text{须在真实 mollifier block 上逐块做 Vaughan/FE/dyadic 归约 —— 属文献级工作）⟹ \text{H1／H2／H3}\ \textbf{未定}$$
$$\textbf{但本档产出}：$$
$$\qquad\text{(a) 把接口}\ \textbf{化为一个单项计算}：\ \rho_\nu=\log V_\nu/\log N_\nu\ \text{的落点（有效窗口}\ (0.7,0.8)）；$$
$$\qquad\text{(b) 结构性初判：阈值区错位（典型}\ \rho\approx0.5\ \text{vs GM 需}\ \rho\in(0.7,0.8)）⟹ H2／H3 更可能；}$$
$$\qquad\text{(c) H3 的精确含义已登记（G 需"保持算术相关结构的工具"）。}$$
$$\Longrightarrow\ \textbf{若初判被计算确认} \Longrightarrow \boxed{\text{GM 接口}\ \textbf{关闭}（\text{不再投入）}}；\ \text{但}\ G\ \text{墙}\ \textbf{仍活}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 历史归因（BCR 17/33／Conrey 4/7／DI／Vaughan）为}\ \textbf{唐先生提供的权威引文，本档未逐行核验}；$$
$$\text{② GM 有效窗口}\ (0.7,0.8)\ \text{取自其前言原文（外部来源）}；$$
$$\text{③ §5 的"阈值区错位"为}\ \textbf{[结构判定]}，\ \textbf{未证}；\quad\text{④ }\textbf{未用 RH}；零数值（\text{仅指数演算）}✓$$

## 9. 净产出
$$\text{(i) 历史校正：}\tfrac47\ \text{与}\ \tfrac{17}{33}\ \text{为两条不同路线；(G) 仅为候选瓶颈}；$$
$$\text{(ii) 防偷换：DP-大值}\ \ne\ \text{mollified 非对角（多重相关和）}；$$
$$\text{(iii) 接口形式}\ \mathcal E_G\lesssim\sum_\nu W_\nu R(N_\nu,V_\nu,T_\nu)\ \text{＋突破判据（}\exists\ \text{block 变}\ o(T)\text{）}；$$
$$\text{(iv) ⭐ 决定性单项＝阈值比}\ \rho_\nu\ \text{落点（有效窗口}\ (0.7,0.8)，最优}\ 0.75\text{）}；$$
$$\text{(v) 初判为阈值区错位（H2／H3 更可能）＋H1／H2／H3 三档与 H3 的精确含义登记。}$$
