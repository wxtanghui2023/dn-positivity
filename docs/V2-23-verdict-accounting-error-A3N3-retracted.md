# V2-23 — **逐行复核 (3.2) 权重账本** ⟹ 判定 **（乙）记账有误；$A^3N^3$ 撤回**

> 唐先生 2026-09-16 21:34 收口后「继续」（21:40）✓
> 唯一问题：$$\boxed{\Sigma_{\rm wd}\ \stackrel{?}{\asymp}\ A^3N^3LM\quad\text{vs}\quad LM^{1+\varepsilon}}$$
> 预登记两后果：重计／误差 $\Longrightarrow$ **缺口立即消失**；确认且覆盖同一对象 $\Longrightarrow$ 结构性落差✓

---

## 1. ⭐⭐⭐ 决定性逻辑判据（**不依赖乱码**）
$$\text{(3.2) 抽取显示权重为}\ \bigl(|n_1a_1|^2+|n_2a_2|^2\bigr)（\text{线性化记号}\ \texttt{jn1a1j2}）✓$$
$$\textbf{但它只能是系数幅度，不能是指标乘积——否则 (3.1) 自相矛盾}：$$
$$\qquad\text{若}\ |n_1a_1|^2＝(\text{指标}n_1)^2(\text{指标}a_1)^2：\ \sum_{n_1\asymp N}n_1^2\asymp N^3,\ \sum_{a_1\asymp A}a_1^2\asymp A^3 \Longrightarrow \text{界将含}\ A^3N^3✓$$
$$\qquad\textbf{但 (3.1) 逐字为}：D_b\ll\|\alpha\|^2\|\nu\|^2L\bigl[A(bLN)^{\frac12}+\tfrac{AM}{bN}+M\bigr]M^{\varepsilon} \Longrightarrow \textbf{只含}\ \|\alpha\|^2\|\nu\|^2，\ \textbf{无}\ A^3N^3✓$$
$$\qquad\text{而 (3.1) 是}\ \textbf{定理} \Longrightarrow \boxed{\text{权重必为}\ |\nu_{n_1}\alpha_{a_1}|^2\ \text{型系数幅度}}✓✓✓$$
$$\Longrightarrow\ \boxed{\text{本档 V2-22b 把}\ |\nu_{n_1}\alpha_{a_1}|^2\ \text{误读为}\ (n_1a_1)^2}✓✓\quad(\text{抽取丢失希腊字母所致})✓$$
$$\qquad(\text{此判据}\ \textbf{纯逻辑}，\ \text{不依赖 PDF 乱码是否消除})✓✓$$

## 2. 正确重算（用系数幅度）
$$\text{(3.2) 正确读法}：\ D_b\ll\sum_{\substack{\ell_1,\ell_2\asymp L;\ n_1,n_2\asymp N;\ a_1,a_2\asymp A\\ (b\eta,\ell_1\ell_2n_1n_2)=1;\ \ell_1n_1=\ell_2n_2}}\bigl(|\nu_{n_1}\alpha_{a_1}|^2+|\nu_{n_2}\alpha_{a_2}|^2\bigr)\sum_{\substack{m\asymp M\\ (m,b\ell_1\ell_2n_1n_2)=1}}e\bigl(\tfrac{\eta(a_1\ell_1-a_2\ell_2)m}{b\ell_1n_1}\bigr)✓$$
$$\text{退化子情形}\ a_1\ell_1=a_2\ell_2：\ \text{内层}\ m\ \text{-和}\asymp M \Longrightarrow D_b^{\rm deg}\ \ll\ M\sum_{\rm deg}|\nu_{n_1}\alpha_{a_1}|^2✓$$
$$\text{固定}\ (a_1,n_1)\ \text{后，满足}\ a_2\ell_2=a_1\ell_1\ \text{且}\ \ell_2n_2=\ell_1n_1\ \text{的}\ (a_2,\ell_1,\ell_2,n_2)\ \text{个数}\ \ll\ L^{1+o(1)}✓$$
$$\qquad（\text{由 V2-21／V2-22b 的参数化}：\ell_1=gu,\ a_2=ku,\ \text{给定}\ a_1=kv,\ n_1=vw\ \text{时}\ v|(a_1,n_1)\ \text{且}\ \#u\asymp v,\ \#g\asymp L/v）✓$$
$$\Longrightarrow\ D_b^{\rm deg}\ \ll\ M\Bigl(\sum_{a_1,n_1}|\nu_{n_1}\alpha_{a_1}|^2\Bigr)L^{1+o(1)}\ =\ \boxed{\|\alpha\|^2\|\nu\|^2\,L\,M\,M^{o(1)}}✓✓✓$$
$$\qquad\Longrightarrow\ \textbf{与 BC 的}\ \|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon}\ \textbf{完全一致}✓✓✓$$

## 3. 判定：**(乙) 记账有误 ⟹ 缺口消失**
$$\boxed{\textbf{(乙)}}\ \Longrightarrow\ \boxed{\Sigma_{\rm wd}\ \ll\ \|\alpha\|^2\|\nu\|^2LM^{1+\varepsilon}\ =\ \text{BC 的界}}✓✓\quad(\textbf{A}^3\textbf{N}^3\ \text{撤回})✓✓$$
$$\qquad\Longrightarrow\ \text{按唐先生预登记}：\ \text{"一旦发现}\ A^3N^3\ \text{是重复计算了已含于}\ \|\alpha\|^2\|\nu\|^2／归一化／支撑的自由度，}\boxed{\text{整个"缺口"立即消失}}✓✓✓$$
$$\qquad\textbf{（更准确地说：是指标／系数读法错误，}\ \text{非"重计"）}✓$$

## 4. ⭐⭐ 顺带得到**更强的结论**（超出预期）
$$\text{重算显示：}D_b^{\rm deg}\ \text{被 BC 的界}\ \textbf{恰好覆盖}（\text{差}\ M^{o(1)}\text{）} \Longrightarrow \boxed{\text{退化族在现有约束下}\ \textbf{已被精确计数}}✓✓$$
$$\qquad\Longrightarrow\ \text{V2-21 的"限制退化以压低}\ F_3\text{"}\ \textbf{不能产生幂次节省}}✓✓$$
$$\qquad\Longrightarrow\ \text{按 V2-21 预登记判据}\ \mathrm{DEAD}：\ \boxed{\text{"限制退化"只是重用已有的 coprimality／range／counting}}✓✓$$
$$\Longrightarrow\ \boxed{F_3\ \textbf{不是纸墙}，\ \text{而是}\ \textbf{现有约束下的真实计数墙}}✓✓✓\quad(\text{唐先生之预期，现由})\ \textbf{计算确认})✓$$

## 5. 随之撤回的产物
$$\textbf{撤回}：\ \text{"有界比值支配"}（\zeta(2)\ \text{收敛} \text{——那是错误权重的产物）✓✓$$
$$\textbf{保留}：\ \text{(3.2) 的组合参数化}\ (k,u,v,g,w)\ \text{（}n_1=vw,\ n_2=uw\text{）\ \textbf{成立}}✓（\text{组合事实，与权重无关}）✓$$
$$\textbf{保留}：\ \ell_1n_1=\ell_2n_2\ \text{＋}\ a_1\ell_1=a_2\ell_2\ \text{的双退化结构描述}✓$$

## 6. 残余（不得省略）
$$\text{残余 1：}\ \#\{(a_2,\ell_1,\ell_2,n_2)\ |\ \text{固定}(a_1,n_1)\}\ll L^{1+o(1)}\ \text{为}\ \textbf{[结构判定]}（\text{由参数化}\ \#u\cdot\#g\asymp v\cdot L/v=L\ \text{推得}），\ \textbf{未} \text{逐行核 §3 的计数陈述}✓$$
$$\text{残余 2：}\ \alpha,\nu\ \text{的归一化约定}\ \textbf{未核}（\text{不影响本档结论，因比较在}\ \|\alpha\|^2\|\nu\|^2\ \text{同一基准上}）✓$$
$$\text{残余 3：}\ D_b\ \text{与}\ C_b\ \text{之间的}\ M/L\ \text{因子}\ \text{承 V2-6b 四项验证}✓\quad\text{残余 4：A--D 不变}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 只做 (3.2) 权重账本复核；}\quad\text{② }\textbf{未用 RH}；\ \text{零数值（计数量级）}✓$$

## 8. 净产出
$$\text{(i) ⭐⭐⭐ 决定性逻辑判据：权重必为}\ |\nu_{n_1}\alpha_{a_1}|^2\ \text{型（否则 (3.1) 自相矛盾）} \Longrightarrow \text{本档 V2-22b 系}\ \textbf{读法错误}✓✓✓$$
$$\text{(ii) 重算：}D_b^{\rm deg}\ll\|\alpha\|^2\|\nu\|^2LM^{1+o(1)} \textbf{＝ BC 的界}✓✓$$
$$\text{(iii) 判定}\ \boxed{\textbf{(乙)}}：\ A^3N^3\ \textbf{撤回}，\ \text{"缺口"}\ \textbf{消失}✓✓$$
$$\text{(iv) ⭐⭐ 更强结论：退化族已被}\ \textbf{精确计数} \Longrightarrow \text{"限制退化"}\ \mathrm{DEAD} \Longrightarrow \boxed{F_3\ \textbf{是真实计数墙，不是纸墙}}✓✓✓$$
$$\text{(v) 撤回：}\ \text{"有界比值支配"（}\text{错误权重产物）；保留：参数化＋双退化结构}✓$$
