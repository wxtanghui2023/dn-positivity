# E6-10（牛-0）— **$K_{\rm meas}\leftrightarrow K_{\rm one-spaced}$ 桥审计**（M1／M2／M3）

> 唐先生 2026-09-16 18:25 裁定：**牛-0 前置**（先审桥，再谈 GM 校准）。
> 起因：E6-9 的"$\Delta\approx0$"**不成立** —— X2 输出为**测度型**对象，X1 输入为 **one-spaced 离散计数**，二者**不是同一坐标**。

---

## 0. E6-9 勘误（T10，正文不修改）
$$\textbf{错处}：\text{E6-9 §5 直接把}\ \text{X2 的输出（LV 测度）}\ \text{代入}\ \text{X1 的输入（one-spaced LV 计数）}，\text{得}\ \Delta=O(\varepsilon)$$
$$\textbf{原因}：\text{MT The 1.2 给的是}\ \boxed{\text{大值集}\ \textbf{测度}}\ (\text{连续对象})；\ \text{X1（Prop 1.1 推论）输入的是}\ \boxed{\text{one-spaced 大值点数}}\ (\text{离散对象})$$
$$\qquad\text{两者}\ \textbf{不是同一个坐标} \Longrightarrow \text{不能把两个箭头当成同一}\ K\text{-坐标上的逆变换}✗$$
$$\textbf{更正确的结构}：\quad\boxed{\mathcal D\ \xrightarrow{\ \Phi_{\rm MT}\ }\ \mathcal K_{\rm meas}}\qquad\text{与}\qquad\boxed{\mathcal K_{\rm disc}\ \xrightarrow{\ \Phi_{\rm det}\ }\ \mathcal D}$$
$$\qquad\text{目前只知道}\ \mathcal K_{\rm meas}\ne\ \text{显然等于}\ \mathcal K_{\rm disc} \Longrightarrow \text{缺一座桥}✓$$
$$\textbf{MT 原文自身的提示}：\text{Prop 1.1 先把}\ \mathcal T=\mathcal T_1\cup\mathcal T_2\ (\#\mathcal T_1\ll T^{2\nu+2\varepsilon})，\ \textbf{只有}\ \mathcal T_2\ \text{才对应 one-spaced 大值点}$$
$$\qquad\text{且 The 1.2 的}\ R_{\sigma,\eta}(T)\ \text{是}\ \textbf{测度}，\ \text{证明中还出现}\ T^{(1-\sigma)/2}\ \text{型额外项} \Longrightarrow \textbf{不能} \text{把这些项塞进}\ O(\varepsilon)✓$$
$$\textbf{E6-9 最终等级更正为}：\boxed{\text{X3 preliminary：账本主指数目前未显示额外幂次损失；}\ \textbf{实际 round-trip loss OPEN}}$$

---

## M1：测度 → one-spaced 点数（**覆盖方向**）
$$\text{设}\ E\subseteq[-T,T]\ \text{为大值集}，\ |E|\le T^{\alpha}；\ \text{取}\ E_{\rm sep}\subseteq E\ \textbf{极大的 one-spaced 子集}$$
$$\textbf{关键：极大性给覆盖}：\ \forall t\in E,\ \exists t_j\in E_{\rm sep}:\ |t-t_j|\le1 \Longrightarrow E\subseteq\bigcup_j(t_j-1,\ t_j+1)$$
$$\Longrightarrow\ |E|\ \le\ \sum_j2\ =\ 2\,R\qquad(\text{每个}\ t_j\ \text{邻域长 2，且}\ E_{\rm sep}\ \text{互不相交意义下})$$
$$\Rightarrow\ \boxed{R\ \ge\ |E|/2}\qquad\textbf{（此步是集合论证，}\textbf{不需要} \text{阈值稳定性）}✓$$
$$\text{注}：\text{唐先生指出的"}\#E_{\rm sep}\le|E|+O(1)\ \textbf{不自动成立}"}\ \text{是对的}（\text{反例：稀疏大间隔点集）}；\ \text{但}\ \textbf{反方向}\ |E|\le2R\ \text{由极大性给出}\ ✓$$

## M2：one-spaced 点数 → 测度（**稳定性方向，含真实损失源**）
$$\text{需局部稳定性}：\ \exists r>0:\ |D(t)|\ge V\ \Longrightarrow\ |D(s)|\ge V/2\ \text{for}\ |s-t|\le r$$
$$\textbf{稳定性半径的来源}：\text{Dirichlet 多项式的}\ t\text{-导数界}：\ \bigl|\partial_tD\bigr|\ \ll\ (\log X)\sup|D| \Longrightarrow r\ \asymp\ \frac{1}{\log X}\ (\asymp\tfrac1{\log T})$$
$$\Longrightarrow\ \text{互不相交的}\ r\text{-邻域给}\ |E|\ \gtrsim\ r\,R \Longrightarrow \boxed{R\ \lesssim\ |E|\cdot\log T}$$
$$\qquad\textbf{即}\ \boxed{\ell_{\rm bridge}\ \le\ \log T\ =\ O(\varepsilon)\ \text{（指数意义）}}\quad(\text{在}\ X\le T^{1/2}\ \text{的 MT 范围内导数界成立})✓$$
$$\textbf{残余}：r\asymp1/\log X\ \text{的论证为}\ \textbf{[结构判定]}，\ \textbf{未} \text{向 MT 证明框架核验}✓$$

## M3：代回 X3
$$\boxed{\Delta\ =\ \underbrace{\ell_{\rm bridge}}_{\le\log T}\ +\ \underbrace{\ell_{\rm detection}}_{\text{The 1.2 的}\ T^{\nu/2+\varepsilon}\ \text{项}}\ +\ O(\varepsilon)}$$
$$\text{DH 情形}：\text{主项}\ T^{2\nu+\varepsilon}\ \text{vs 检测项}\ T^{\nu/2+\varepsilon}：\ \text{对}\ \nu\in[0,\tfrac12]，\ 2\nu\ge\nu/2 \Longrightarrow \textbf{主项支配} \Longrightarrow \ell_{\rm detection}\ \text{被吸收}✓$$
$$\Longrightarrow\ \boxed{\Delta=O(\varepsilon)\ \text{（在 MT 切片内，}\textbf{且条件于} M1／M2\ \text{两条桥条件）}}$$
$$\qquad\textbf{但}\ \text{这}\ \textbf{不等于} \text{"往返映射零损失"}：\text{它是}\ \textbf{切片内＋条件于桥审计} \text{的结论}✓$$

---

## 状态更新（唐先生指定格式）
$$\boxed{\begin{aligned}X1&:\quad \text{基本完成}\\ X2&:\quad \text{完成，但得到的是受限}\ \mathcal K_{\rm meas}\ \text{切片}\\ X3&:\quad \text{主指数闭合，但}\ \textbf{实际 round-trip loss OPEN}\\ \mathrm{GM}&:\quad \textbf{暂缓}\end{aligned}}$$

## 牛-1（GM 校准）为何仍暂缓
$$\text{GM 会}\ \textbf{同时} \text{改变五项}：\text{coefficient architecture／polynomial length／large-value threshold／geometric regime／detection mechanism}$$
$$\Longrightarrow\ \text{若此时出现}\ \Delta>0，\ \textbf{无法判断} \text{损失来自}\ \text{strength coordinate 本身}\ \text{还是}\ \text{measure/discrete 桥}\ ✗$$
$$\textbf{正确顺序}：\ \boxed{\text{牛-0}\ \longrightarrow\ \text{牛-1 GM calibration}}✓$$

## 边界（N1/N2 严守）
$$\text{① M1 为}\ \textbf{集合论证}（严格）；\ \text{M2 的稳定性半径论证为}\ \textbf{[结构判定]}；\ \text{M3 的}\ \ell_{\rm det}\ \text{吸收为}\ \textbf{指数演算}；$$
$$\text{② E6-9 的"}\Delta=O(\varepsilon)\ \text{（零损失）}"\ \textbf{已勘误}（\text{见 §0}）；\quad\text{③ MT 原文细节（正文 2 章后）}\ \textbf{未逐行核验}；$$
$$\text{④ }\textbf{未用 RH}；零数值；\text{未跑 Lean}；\ \text{不引入候选机制}。}$$

## 净产出
$$\text{(i) E6-9 勘误（T10）：测度≠离散坐标，}\Delta\approx0\ \text{不能那样推；等级改为"preliminary／round-trip loss OPEN"；}$$
$$\text{(ii) 正确结构：}\mathcal D\xrightarrow{\Phi_{\rm MT}}\mathcal K_{\rm meas}\ \text{与}\ \mathcal K_{\rm disc}\xrightarrow{\Phi_{\rm det}}\mathcal D\ \text{（两个不同靶）；}$$
$$\text{(iii) M1（覆盖，严格）}\Longrightarrow R\ge|E|/2；\ \text{M2（稳定性）}\Longrightarrow R\lesssim|E|\log T，\ \ell_{\rm bridge}=O(\log T)；$$
$$\text{(iv) M3：}\Delta=\ell_{\rm bridge}+\ell_{\rm detection}+O(\varepsilon)，\text{DH 下}\ \ell_{\rm det}\ \text{支配性吸收；}$$
$$\text{(v) 状态四行更新＋GM 暂缓理由（五项同时变化 ⟹ 损失不可定位）。}$$

---

## 【更正 T10】（2026-09-16 18:27，唐先生指出；正文不修改，更正留档）
$$\textbf{原（§M2／M3）}：\ \ell_{\rm bridge}\le\log T=O(\varepsilon)\quad\textbf{不严谨}$$
$$\textbf{更正}：\ \log T=T^{o(1)} \Longrightarrow \text{若}\ r\asymp(\log T)^{-1}，\ \text{则}\ r^{-1}\asymp\log T=T^{o(1)} \Longrightarrow \boxed{\ell_{\rm bridge}=0\ (\text{幂指数层级})\ \text{或}\ o(1)}$$
$$\qquad\ \textbf{不得} \text{写}\ O(\varepsilon)\ ——\ \varepsilon\ \text{为固定小参数，}\ o(1)\ \text{为}\ T\to\infty\ \text{渐近量，两者不同层级。}$$
$$\textbf{另}：\text{经 E6-11（虎-1）核验，}\textbf{MT 未使用该桥}（\text{判定 M2-C}）\Longrightarrow r\asymp1/\log T\ \text{仅为独立结构判定。}$$
