# V2-13 — **$A\sim N^{1/2}$ 交叉与"支配区—uniform 有效区错位"**

> 唐先生 2026-09-16 21:11 拍板 **V2-13**（不做 $a_2$／不碰 C--S 变量释放；直接把 §3.4 全参数化代入）。
> 唐先生的关键逻辑点（采纳）：$$\boxed{\text{BC 给的是}\ T_1+T_2，\ \textbf{不是}\ T_2} \Longrightarrow \text{严格成立的只是}\ \textbf{分区估计}：A\lesssim N^{1/2}\Rightarrow\mathscr B\ll T_1；\ A\gtrsim N^{1/2}\Rightarrow\mathscr B\ll T_2✓$$
> 判死树：**A 单点路线**（统一用 $(\tfrac38,\tfrac12)$）／**B 分区路线**（按 $A$ 拆）✓

---

## 1. V2-12 的代数：**已登记为 VERIFIED**（唐先生确认）
$$T_2=(AMN)^{\frac38}(AM+AN)^{\frac18}\ \xrightarrow{M\asymp N}\ A^{\frac12}N^{\frac78}\ \Longrightarrow\ (r,t)=\Bigl(\tfrac38,\tfrac12\Bigr)；\ L=\tfrac{55}{8}=6.875<8✓$$
$$\frac{T_2}{T_1}\asymp A^{\frac3{20}}N^{-\frac3{40}}\Longrightarrow T_2\ge T_1\iff A\gtrsim N^{\frac12}✓\qquad(\text{以上三项}\ \textbf{代数成立})✓$$
$$\text{且}\ (r,t)=(\tfrac38,\tfrac12)\ \text{的 BCR 模板域}：A\ll(NM)^{\frac{1/16}{}+\varepsilon}\Longrightarrow \textbf{成立}✓$$

## 2. ⭐ 错位（两区间渐近不相交）
$$\text{取}\ M\asymp N：A\ll(NM)^{1/16}\Longrightarrow A\ll N^{1/8+o(1)}✓$$
$$T_2\ \text{支配区}：A\gtrsim N^{1/2}✓\qquad(r,t)=(\tfrac38,\tfrac12)\ \text{模板有效区}：A\ll N^{1/8+o(1)}✓$$
$$\Longrightarrow\ \boxed{\text{两区在}\ N\to\infty\ \textbf{渐近不相交}}\ ✓✓$$

## 3. ⭐⭐ §3.4 全参数化代入（本档核心计算）
$$\text{记}\ N_1=T^{\alpha},\ N_2=T^{\beta},\ d=T^{u},\ \text{应用}\ A=\frac{N_1N_2}{d}T^{\frac12-\varepsilon}\Longrightarrow \log_T A=\alpha+\beta-u+\tfrac12✓$$
$$\text{三线性侧}\ N_{\rm tri}\ \text{满足}\ \frac{N_i}{d}\le N_{\rm tri}\le T^{\theta_{\max}}\Longrightarrow \log_T N_{\rm tri}=\theta-u（\text{取}\ N_i\asymp N）✓$$
$$\textbf{支配配置（承 Q2-A2）}：\ \sup\ \text{在}\ (\alpha,\beta,u)=(\theta,\theta,0) \Longrightarrow \log_T A=2\theta+\tfrac12，\ \log_T N=\theta✓✓$$
$$\textbf{检查 1（}T_2\ \text{支配？）}：\ \log_T A\ge\tfrac12\log_T N \iff 2\theta+\tfrac12\ge\tfrac{\theta}{2}\iff \tfrac32\theta\ge-\tfrac12 \Longrightarrow \boxed{\text{对一切}\ \theta\ge0\ \textbf{成立}}✓✓$$
$$\qquad\Longrightarrow \boxed{\text{支配配置}\ \textbf{永远落在}\ T_2\ \text{支配区}}✓✓$$
$$\textbf{检查 2（}T_2\ \text{模板有效？）}：\ \log_T A\le\tfrac1{16}(\log_T N+\log_T M)=\tfrac1{16}(2\theta)=\tfrac{\theta}{8} \iff 2\theta+\tfrac12\le\tfrac{\theta}{8}\iff \tfrac{15}{8}\theta\le-\tfrac12 \Longrightarrow \boxed{\textbf{对任何}\ \theta\ge0\ \textbf{不可能}}✓✓$$
$$\Longrightarrow\ \boxed{\text{支配配置}\ \textbf{永远落在}\ (\tfrac38,\tfrac12)\ \text{模板有效区}\ \textbf{之外}}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{结论}：\text{误差最大的配置恰是}\ T_2\ \text{模板不可用的配置}}\ \Longrightarrow \textbf{"支配区—uniform 有效区错位"}✓✓$$

## 4. 判死树逐条
$$\textbf{A（单点路线，统一用}\ (\tfrac38,\tfrac12)\text{）}：\ \text{应用域须}\ \subseteq\{A\ll N^{1/8}\}，\ \text{但}\ \S3\ \text{显示支配配置}\ \textbf{不满足} \Longrightarrow \boxed{\text{T2-单点路线}\ \textbf{DEAD}（有效域与支配域错位}）✓✓$$
$$\textbf{B（分区路线，按}\ A\ \text{拆）}：\ \text{在}\ \textbf{(1.3) 模板框架内} \text{，分区}\ \textbf{不能拯救} \text{——因}\ T_2\ \text{的模板在支配配置处}\ \textbf{本就不可用}✓✓$$
$$\qquad\Longrightarrow\ \text{故}\ \boxed{\text{在模板框架内，两条路线同时失败}}✓\quad(\text{这就是唐先生预期的"错位墙"})✓$$

## 5. ⭐ 但仍有一条**未被关闭**的路线（本档识别）
$$\text{BC 定理 1 的}\ \textbf{原始两项界} \text{对}\ \textbf{所有}\ A\ \text{成立}（\text{含支配配置}）：\ \mathscr B\ll(1+\tfrac{|\vartheta|A}{MN})^{\frac12}(T_1+T_2)✓$$
$$\qquad\text{且支配配置处}\ \frac{|\vartheta|A}{MN}\asymp\frac{N^{1/2+\text{小}}}{N^{2}}\ll1 \Longrightarrow \text{前因子}\approx1 \Longrightarrow \text{该处界}\approx T_2✓✓$$
$$\Longrightarrow\ \boxed{\text{决定性问题变成本档的真正残余}：\ \text{BCR §3.4 能否}\ \textbf{绕过 (1.3) 模板}，\ \text{直接用 BC 原始两项界？}}✓✓$$
$$\qquad\text{若}\ \textbf{能} \Longrightarrow \text{支配配置处用}\ T_2 \Longrightarrow \text{误差指数改变} \Longrightarrow \text{可能}\ \theta>\tfrac{17}{33}✓✓$$
$$\qquad\text{若}\ \textbf{不能}（\text{模板是本质的}）\ \Longrightarrow \text{错位墙成立} \Longrightarrow \text{得到}\ \textbf{"墙为什么在那里"}✓$$

## 6. 判定
$$\boxed{\text{A 路线}\ \textbf{DEAD}（错位）；\ \text{B 路线在模板框架内亦失败；}\ \text{但"原始两项界"路线}\ \textbf{OPEN}}✓$$
$$\qquad\text{本档}\ \textbf{不宣称} \text{破墙，亦}\ \textbf{不宣称} \text{容量墙成立——}\ \text{而是把问题}\ \textbf{精确压缩} \text{为 §5 的单一问句}✓$$

## 7. 残余（不得省略）
$$\text{残余 1：§5 的"原始两项界"路线须核 §3.4 对 (1.3) 的}\ \textbf{实际用法} \text{（模板是本质还是仅为叙述方便）}✓$$
$$\text{残余 2：}\ N_i\asymp N\ \text{的归约为}\ \textbf{承 Q2-A2 结论}（\text{不平衡不产生更大指数}）✓$$
$$\text{残余 3：}\ T_2\ \text{的模板}\ A\ \text{范围公式}\ (NM)^{1/16}\ \text{承 V2-12，}\ \textbf{已由唐先生核}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 只做 §3.4 全参数化代入；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值}✓$$

## 9. 净产出
$$\text{(i) V2-12 代数三项登记为 VERIFIED}✓$$
$$\text{(ii) 错位成立：}T_2\ \text{支配区}\ \{A\gtrsim N^{1/2}\}\ \big|\ (\tfrac38,\tfrac12)\ \text{模板有效区}\ \{A\ll N^{1/8}\} \Longrightarrow \textbf{渐近不相交}✓✓$$
$$\text{(iii) ⭐⭐ } \S3\ \text{全参数化：支配配置}\ \log_T A=2\theta+\tfrac12,\ \log_T N=\theta \Longrightarrow \text{支配区成立（}\forall\theta\text{）但模板有效不可能（}\forall\theta\text{）} \Longrightarrow \textbf{误差最大的配置恰是}\ T_2\ \text{不可用处}✓✓$$
$$\text{(iv) A 路线 DEAD；B 路线在模板框架内亦失败} \Longrightarrow \textbf{"错位墙"}✓$$
$$\text{(v) ⭐ 但"BC 原始两项界"路线}\ \textbf{OPEN} \Longrightarrow \text{问题精确压缩为：§3.4 能否绕过 (1.3) 模板}✓✓$$
