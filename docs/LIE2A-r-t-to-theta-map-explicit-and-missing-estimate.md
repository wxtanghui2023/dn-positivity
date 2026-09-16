# 猎-2A — **$(r,t)\to\theta_{\max}$ 映射的彻底拆解** ＋ 缺失的不可替代估计

> 唐先生 2026-09-16 19:47「继续」；按 REVIEW-20260916 登记的下一轮第一刀执行。
> 链条（唐先生指定）：$$(r,t)\ \to\ \text{Kloosterman 估计}\ \to\ \mathcal E_{\rm off}(\theta)\ \to\ \theta_{\max}$$
> 随后单独审计：$$\boxed{\theta<1\ \text{的 conjectural input 究竟缺哪一个不可替代的算术估计}？}$$

---

## 1. 映射的显式形式 ＋ **自校验**
$$\text{BCR 参数化（唐先生引文）}：\quad \boxed{\theta_{\max}(r,t)\ =\ \frac12\ +\ \frac{\frac12-r}{1+2(r+2t)}}$$
$$\textbf{自校验（本档计算，已验证）}：\ (r,t)=\left(\tfrac9{20},\tfrac7{20}\right)\Longrightarrow$$
$$\qquad \tfrac12-r=\tfrac1{20}；\ 1+2(r+2t)=1+2\cdot\tfrac{23}{20}=\tfrac{33}{10}；\ \frac{1/20}{33/10}=\frac{1}{66}\Longrightarrow \theta_{\max}=\frac12+\frac1{66}=\frac{17}{33}\ ✓✓$$
$$\qquad\textbf{与文献记录}\ \tfrac{17}{33}\ \textbf{完全一致} \Longrightarrow \text{映射形式正确}✓$$
$$\textbf{另一项（唐先生引文）}：\ (r,t)=\left(\tfrac{23}{48},\tfrac12\right)\Longrightarrow \theta_{\max}=\tfrac12+\tfrac{1}{190}\approx0.50526$$
$$\qquad\textbf{⚠️ 标注}：\text{该项}\ \textbf{不} \text{复现}\ \tfrac{17}{33} \Longrightarrow \text{或为不同版本的公式／归一化}\ \textbf{须核验}✓$$

## 2. ⭐ 单调性（本档计算）：映射是"节省转移"
$$\frac{\partial}{\partial r}\Bigl[\frac{\frac12-r}{1+2r+4t}\Bigr]=\frac{-2-4t}{(1+2r+4t)^{2}}<0\ ✓;\qquad \frac{\partial}{\partial t}\Bigl[\cdot\Bigr]=\frac{-4(\frac12-r)}{(1+2r+4t)^{2}}<0\ (r<\tfrac12)\ ✓$$
$$\Longrightarrow\ \boxed{\theta_{\max}\ \textbf{关于}\ r,t\ \textbf{均严格递减}} \Longrightarrow \boxed{\theta\ \text{增大}\iff (r,t)\ \text{减小}}$$
$$\text{即：}\ \textbf{Kloosterman 抵消增强}（(r,t)\ \text{变小}）\ \Longrightarrow\ \theta\ \text{增大} \Longrightarrow \text{与墙 A 的历史记录}\ \textbf{完全一致}✓$$

## 3. ⭐⭐ 关键：$\theta\to1$ **恰对应** $(r,t)\to(0,0)$
$$\text{代入}\ (r,t)=(0,0)：\ \theta_{\max}=\tfrac12+\tfrac{1/2}{1}=1 \Longrightarrow \boxed{\text{猜想型输入}＝\textbf{端点}\ (0,0)}✓$$
$$\textbf{即}：\ \text{BCR 所述"若 Kloosterman 猜想成立则可一直得到}\ \theta<1\text{"} \ \textbf{在此公式中表现为}\ (r,t)\to(0,0)✓$$
$$\Longrightarrow\ \boxed{\text{墙 A 的"能推到哪里"}\ \textbf{完全等价于} \text{"(r,t) 能被推到多小"}}✓$$
$$\qquad\textbf{这是一次}\ \textbf{坐标闭合}：\text{原来模糊的"还能推多远"}\ \text{变成了}\ \textbf{两个明确的非负指数的最小可达值}✓$$

## 4. 链条逐段落地（唐先生指定形式）
$$\boxed{(r,t)\ \xrightarrow{\ \text{Kloosterman 估计}\ }\ \mathcal E_{\rm off}(\theta)\ \xrightarrow{\ \text{闭合判据}\ \mathcal E_{\rm off}(\theta)=o(T)\ }\ \theta_{\max}=\tfrac12+\frac{\frac12-r}{1+2(r+2t)}}$$
$$\qquad\text{已知点}：\ (9/20,7/20)\Longrightarrow 17/33；\ \textbf{猜想端点}：\ (0,0)\Longrightarrow 1$$
$$\qquad\textbf{历史点（待核）}：\ (23/48,1/2)\Longrightarrow\tfrac12+\tfrac1{190}；\ \text{Conrey}\ 4/7\ \text{的}\ (r,t)\ \text{对应式尚未定位}$$

## 5. ⭐ 缺失的不可替代估计（唐先生指定单独审计）
$$\textbf{问题}：\ \theta<1\ \text{的 conjectural input 究竟缺哪一个不可替代的算术估计？}$$
$$\textbf{本档判定（[结构判定]）}：\ \text{缺口}\ =\ \textbf{端点}\ (0,0)\ \text{的}\ \textbf{满强度 Kloosterman-fraction 抵消}$$
$$\qquad\text{即：对}\ S_{A,M,N}=\sum_a\sum_{(m,n)=1}\nu_a\alpha_m\beta_n e(a\bar m/n)\ \text{需要}\ \textbf{无余量的平方根型抵消}$$
$$\textbf{其性质的诚实标注}：\ \text{该端点在各已知实现中均经由}\ \textbf{谱／Kuznetsov 型装置} \text{获得} \Longrightarrow \text{其已知失败模式涉及}\ \textbf{例外特征值／谱隙} \text{问题}$$
$$\qquad\Longrightarrow\ \textbf{因此"缺失的不可替代估计"更可能是}\ \textbf{谱型输入} \text{（而非初等算术和）}——\ \textbf{但本档}\ \textbf{不宣告} \text{具体等价，\text{须逐项核验}}✓$$
$$\textbf{另一条明确可查的缺口}：\ \text{公式中}\ \theta\ \text{与}\ (r,t)\ \text{的}\ \textbf{分母}\ 1+2(r+2t)\ \text{结构本身} \text{可能对更强输入失效（}\text{需核验 BCR 是否给出}\ (r,t)\to(0,0)\ \text{时的公式有效性）✓$$

## 6. 防偷换（保留）
$$\boxed{\theta<1\ \Longrightarrow\ \text{Lindelöf}（\text{已验证的文献链）}\ \textbf{仍}\ \ne\ \mathrm{RH}}\quad(\theta=\infty\ \text{才}\Rightarrow\mathrm{RH})✓$$

## 7. 判定（本档落点）
$$\boxed{\text{猎-2 第一刀}\ \textbf{已完成}：\ (r,t)\to\theta_{\max}\ \text{映射显式化＋自校验通过}}$$
$$\qquad\text{(i) 映射形式获}\ \tfrac{17}{33}\ \text{验证}✓；\ \text{(ii) 单调性证明：}\theta\uparrow\iff(r,t)\downarrow✓；$$
$$\qquad\text{(iii) ⭐ 坐标闭合：}\ \theta\to1\iff(r,t)\to(0,0) \Longrightarrow \text{墙 A 的天花板＝}\textbf{两端点指数的可达下界}✓$$
$$\qquad\text{(iv) 缺口定位：}\ \textbf{端点}\ (0,0)\ \text{的满强度 Kloosterman 抵消}，\ \text{其实现路径}\ \textbf{疑似谱型输入}（\text{[结构判定]}）✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 公式与}\ (r,t)\ \text{数值为}\ \textbf{唐先生提供的 BCR 引文，本档未逐行核验}；$$
$$\text{② §1／§2／§3 的计算为}\ \textbf{本档计算}（\tfrac{17}{33}\ \text{已自校验}）✓；\quad\text{③ §5 的"谱型输入"为}\ \textbf{[结构判定]}，\ \textbf{未证}；$$
$$\text{④ }\textbf{未用 RH}；零数值（\text{仅分数演算）}；\ \text{未跑 Lean}✓$$

## 9. 净产出
$$\text{(i) 映射显式化并}\ \textbf{自校验通过}（\tfrac{17}{33}\ \text{精确复现}）；$$
$$\text{(ii) 单调性证明：}\theta\ \text{关于}\ (r,t)\ \text{严格递减} \Longrightarrow \text{"节省转移"结构}；$$
$$\text{(iii) ⭐⭐ }\theta\to1\iff(r,t)\to(0,0) \Longrightarrow \text{墙 A 的天花板}\ \textbf{化为两端点指数的可达下界}；$$
$$\text{(iv) 缺口定位：端点}\ (0,0)\ \text{的满强度 Kloosterman 抵消（疑似谱型，[结构判定]}）；$$
$$\text{(v) 待核项：}\ (23/48,1/2)\ \text{与}\ \tfrac{17}{33}\ \text{不一致；Conrey}\ 4/7\ \text{的}\ (r,t)\ \text{对应式未定位；猜想端点处公式有效性待核。}$$
