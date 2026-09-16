# Q2-A — **精确求 BCR 应用配置族的支配极限**

> 唐先生 2026-09-16 20:15 拍板：做 **Q2-A**（**不碰 $17r+t\ge8$**；不合并 Q2-B）。
> 前置修正（唐先生，采纳）：$$\boxed{\text{"支配性＝紧性"}\ \textbf{不} \text{已推出}\ \inf_{\mathfrak F}(17r+t)=8}$$ —— 本档只求支配极限✓
> 三档：**A1** 真正边界达到／**A2** 小 $d$ 只是粗略支配／**A3** 额外结构消掉小 $d$ 极端。

---

## 1. 设置：两参数归约
$$E(\mathcal C)=T^{\frac12+\varepsilon-t}(N_1+N_2)^{\frac12+r}(N_1N_2)^{t}d^{-\frac32-r-2t},\qquad A=\frac{N_1N_2}{d}T^{\frac12-\varepsilon}$$
$$\text{dyadic}\ N_1,N_2\asymp N=T^{\theta}\ (0<\theta\le\theta_{\max})；\ d=T^{u},\ u\in[0,\theta]；\ \varepsilon\to0✓$$
$$\Longrightarrow\ \log_T E\ =\ \underbrace{\tfrac12-t}_{\text{常数项}}\ +\ \theta\bigl(\tfrac12+r+2t\bigr)\ -\ \bigl(\tfrac32+r+2t\bigr)u\ :＝\ \Phi(\theta,u)✓$$
$$\textbf{约束（据唐先生核出的 §3.4）}：\ N\ \le\ T^{\frac12+\frac{0.5-r}{1+2(r+2t)}} \Longleftrightarrow \boxed{\theta\ \le\ \theta_{\max}=\frac{1+2t}{1+2r+4t}}✓$$
$$\qquad\textbf{注意（本档识别）}：\ \text{此}\ A\ \text{-范围约束}\ \textbf{就是}\ \text{Theorem 2 的}\ \theta\ \text{-上界本身} \Longrightarrow \textbf{第二次独立得到同一公式}✓$$

## 2. 支配极限的计算
$$\Phi\ \text{关于}\ u\ \textbf{严格递减}（\text{系数}\ \tfrac32+r+2t>0）\Longrightarrow \sup\ \text{在}\ u=0\ (\text{即}\ \mathbf{d=1})\ \text{处}✓$$
$$\Phi\ \text{关于}\ \theta\ \textbf{递增}（\text{系数}\ \tfrac12+r+2t>0）\Longrightarrow \sup\ \text{在}\ \theta=\theta_{\max}\ \text{处}✓$$
$$\Longrightarrow\ \boxed{\sup_{\mathcal C}\ \log_T E\ =\ \Phi(\theta_{\max},0)}✓$$

## 3. ⭐⭐ 恒等式（本档核心计算）
$$\textbf{关键}：\quad \tfrac12+r+2t\ =\ \frac{1+2r+4t}{2}\qquad(\textbf{恒等})✓$$
$$\Longrightarrow\ \theta_{\max}\cdot\bigl(\tfrac12+r+2t\bigr)=\frac{1+2t}{1+2r+4t}\cdot\frac{1+2r+4t}{2}=\frac{1+2t}{2}$$
$$\Longrightarrow\ \Phi(\theta_{\max},0)=\Bigl(\tfrac12-t\Bigr)+\frac{1+2t}{2}=\tfrac12-t+\tfrac12+t=\boxed{\mathbf{1}}\ ✓✓✓$$
$$\textbf{自校验（BC 点）}：\ (r,t)=(\tfrac9{20},\tfrac7{20})：\ \tfrac12+r+2t=1.65；\ \theta_{\max}=17/33\Longrightarrow 0.5152\times1.65=0.85；\ \tfrac12-t=0.15；\ \text{和}=\mathbf{1.0}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{支配配置的误差项}\ =\ T^{1+o(1)} \ =\ \textbf{主项的量级}}\ ✓✓\quad(\textbf{预算恰好饱和})$$

## 4. ⭐ 三个结论（全部由计算得出）
$$\textbf{(a) 支配配置}＝\ (\theta=\theta_{\max},\ d=1)\ \text{的}\ \textbf{角点}，\ \text{且}\ \textbf{唯一}✓$$
$$\qquad(\text{任何}\ \theta<\theta_{\max}\ \text{或}\ u>0\ \text{都}\ \textbf{严格降低} \text{误差指数}）✓$$
$$\textbf{(b) 二次独立验证}：\ \text{误差项的}\ \textbf{预算饱和身份}\ \Phi(\theta_{\max},0)=1\ \text{与}\ \text{A 范围约束}\ \theta\le\theta_{\max}\ \text{给出}\ \textbf{同一公式}✓$$
$$\qquad\Longrightarrow\ \theta\ \text{-公式}\ \textbf{就是"误差＝主项"的等式陈述}（\text{与猎-3B §4 的第一次推导}\ \textbf{一致}）✓✓$$
$$\textbf{(c) ⭐ }\textbf{"支配性＝紧性重合"由计算确认}：\ \text{支配配置（}u=0\text{）}\ \textbf{同时} \text{饱和}\ (r,t)\ \text{的适用边界（}\theta=\theta_{\max}\text{）}✓✓$$

## 5. 判定：**A1**（真正边界达到）
$$\boxed{\textbf{A1}}\：\ \text{同一配置极限}\ (\theta=\theta_{\max},\ d=1)\ \textbf{同时决定} \text{误差主项与}\ (r,t)\ \text{适用边界}✓$$
$$\qquad\Longrightarrow\ \text{按唐先生：}\boxed{\text{"支配性＝紧性重合"从}\ \textbf{结构判断} \ \text{升级为}\ \textbf{真正的刚性候选}}✓✓$$
$$\textbf{A2 排除（在报告形式的范围内）}：\ \text{加入完整约束后}\ \sup\ \text{仍在角点；}\ u\ \text{与}\ \theta\ \text{方向单调性}\ \textbf{相互独立} \text{且同向收紧}✓$$
$$\textbf{A3 排除（在报告形式的范围内）}：\ d=1\ \text{项}\ \textbf{确实存在}（\text{重数}\ \ge1，\text{权重}\ d^{-\frac32-r-2t}\big|_{d=1}=1\text{）}\ \text{且}\ \sum_d\ \text{收敛，故总和}\ \asymp\ \text{角点量级}\times O(1)✓$$
$$\qquad\Longrightarrow\ \text{极端}\ \textbf{不是} \text{记账假象，而是}\ \textbf{真实的项}}✓$$

## 6. 由 A1 得到的结构性后果（**不进入 Q2-B**）
$$\text{误差预算}\ \textbf{在最优}\ (r,t)\ \text{处恰好饱和} \Longrightarrow \boxed{\text{任何}\ (r,t)\ \text{改进都}\ \textbf{直接} \text{转化为}\ \theta\ \text{的改进}}\ —\ \text{反之亦然}✓$$
$$\qquad\Longrightarrow\ \text{“找更强的估计”与“更大的}\ \theta\text{”在}\ \textbf{该架构内是同一件事}✓$$
$$\qquad\textbf{但}：\ \text{这}\ \textbf{不} \text{说明}\ \inf(17r+t)=8（\text{唐先生修正，本档遵守}）——\ \text{该问题留给 Q2-B}✓$$

## 7. 残余（不得省略）
$$\text{残余 1：}E(\mathcal C)\ \text{的形式与}\ A\ \text{范围约束由}\ \textbf{唐先生核出的 §3.4 转述}，\ \textbf{本档未读原文} \Longrightarrow \text{§2／§5 为}\ \textbf{结构性计算}✓$$
$$\text{残余 2：}\ N_1,N_2\ \text{是否}\ \textbf{严格} \text{两者皆}\ \asymp N（\text{或存在不平衡情形}）\ \textbf{未核} \Longrightarrow \text{若允许}\ N_1\gg N_2，\ \text{则}\ (N_1+N_2)^{\frac12+r}\ \text{的归约需修正}✓$$
$$\text{残余 3：残余 A--D（跨轮结转）不变}✓$$

## 8. 边界（N1/N2 严守）
$$\text{① 不碰}\ 17r+t\ge8（\text{唐先生指定}）；\ \text{不合并 Q2-B}；\quad\text{② }\textbf{未用 RH}；\text{零数值（\text{仅指数量级与恒等式演算}）}✓$$

## 9. 净产出
$$\text{(i) 两参数归约}\ \Phi(\theta,u)=\tfrac12-t+\theta(\tfrac12+r+2t)-(\tfrac32+r+2t)u；\ \text{约束}\ \theta\le\theta_{\max}\ \textbf{即}\ \text{Theorem 2 上界（二次独立得到）}；$$
$$\text{(ii) }\Phi\ \text{关于}\ u\ \text{递减、关于}\ \theta\ \text{递增} \Longrightarrow \sup\ \text{在角点}\ (\theta_{\max},0)✓$$
$$\text{(iii) ⭐⭐ 恒等式}\ \tfrac12+r+2t=\tfrac{1+2r+4t}{2}\Longrightarrow\Phi(\theta_{\max},0)=\mathbf{1} \Longrightarrow \textbf{误差项＝主项量级（预算饱和）}；$$
$$\text{(iv) 判定}\ \textbf{A1}（\text{A2／A3 在报告范围内排除}）\Longrightarrow \textbf{支配性＝紧性重合升级为计算}✓$$
$$\text{(v) 结构后果：该架构内"更强估计"}\equiv\text{"更大}\ \theta\text{"（预算恰好饱和）；}\inf(17r+t)\ \text{留给 Q2-B。}$$
