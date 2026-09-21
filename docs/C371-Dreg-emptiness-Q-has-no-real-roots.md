已查地图（**先查后写**）：`C-370`（**四次方程** ✓✓；**尺度 × 离散形状** ✓✓）、`C-369`（`\mathcal Z \cap E = \mathcal D_{\mathrm{reg}} \cap E` ✓✓）、`C-368`（碰撞判空 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-371：`\mathcal D_{\mathrm{reg}}` 判空（`Q(r)` 无实根）**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① ⭐ 精确结果}✓✓：\ \boxed{Q(r) = 81r^4 - 2358r^3 + 16340r^2 + 12696r + 2592\ \text{在}\ \mathbb{R}\ \text{上无实根}}✓✓$$
$$\qquad \text{证据}✓✓：\text{Sturm 实根计数}\ \texttt{count\_roots()} = 0✓；\text{判别式} = 110333176842427564032 > 0✓；\text{数值最小} = 250.479 > 0✓（\text{于}\ r \approx -0.360✓）$$
$$\qquad \Longrightarrow \ Q(r) > 0\ \text{对一切}\ r \in \mathbb{R}✓✓$$
$$\textbf{② 不可行因子被正性排除}✓✓：s = 0 \Longrightarrow \beta = b_2 = 0✗（\text{与正性矛盾}✓）；\ e_2 = 0 \Longrightarrow a_1a_2 + a_1a_3 + a_2a_3 = 0✗（\text{三项皆正}✓） \Longrightarrow e_2 > 0✓✓$$
$$\textbf{③ 判空}✓✓：C(e_2,s) = -\tfrac{5}{81}e_2^2s^{11}Q(r)✓；\text{由 ①②} \Longrightarrow C(e_2,s) \ne 0\ \text{对一切}\ \textbf{实可行}\ (e_2,s)✓✓$$
$$\qquad \Longrightarrow \ \operatorname{Res}_p(F_2, F_3) \ne 0✓ \Longrightarrow F_2, F_3\ \textbf{无公共实根}\ p✓✓ \Longrightarrow \ \boxed{\mathcal D_{\mathrm{reg}}\ \text{无实数解} \Longrightarrow \mathcal D_{\mathrm{reg}} = \varnothing}✓✓$$
$$\textbf{④ 维数一致性（解释明显异常 ✓）}✓✓：\text{原系统}\ \textbf{齐次}（\text{度}\ 2r+1✓） \Longrightarrow \text{形状空间}\ 4\ \text{维}✓、\text{方程}\ 4✓ \Longrightarrow \textbf{形状为 0 维}✓✓ \Longrightarrow \text{「有限解或}\ \textbf{无解}\text{」}\ \text{皆属一般位置}✓✓$$
$$\qquad \textbf{自误更正}✗✓：\text{我此前}\ \text{「一维族」}\ \text{读法}\ \textbf{混入了尺度方向}✗✓ \ —— \ \text{C-370 已修正为「尺度} \times \text{离散形状」✓✓；故「无实解」}\ \textbf{不}异常✗✓$$
$$\textbf{⑤ 推论（exact-cancellation 整体排除）}✓✓：\ \boxed{\mathcal Z \cap E = \mathcal D_{\mathrm{reg}} \cap E = \varnothing}✓✓（\mathcal D_{\mathrm{reg}} = \varnothing✓）$$
$$\textbf{⑥ 边界}✓✓：\textbf{仍不得}写\ H = \varnothing✗✓（\mathcal Z \cap E = \varnothing \not\Rightarrow H = \varnothing✓，已锁定✓）；\text{下一目标}\ = \textbf{Bridge A}✓✓$$

## §1 判空链（✓✓）

$$\text{四奇矩条件}✓ \Longrightarrow \ e_1 = s = \beta + b_2✓，\ e_2 = r s^2✓，\ p = q s^2✓（\text{C-370 的四次／二次结构}✓✓）$$
$$\qquad \Longrightarrow \ \text{曲线条件}\ C(e_2,s) = 0 \iff e_2 = 0 \ \vee\ s = 0 \ \vee\ Q(r) = 0✓✓$$
$$\qquad \Longrightarrow \ \text{三者}\ \textbf{皆不可行}✗✓（\text{前两者由正性}✓，\text{后者由无实根}✓） \Longrightarrow \ \mathcal D_{\mathrm{reg}} = \varnothing✓✓$$

## §2 形状参数化（✓✓，C-370 结构 ✓）

$$y := \dfrac{X}{s}✓ \Longrightarrow \text{无尺度三次式}\ y^3 - y^2 + ry - \kappa(r) = 0✓（\text{三正根要求}✓）；\ \dfrac{a_i}{s} = y_i(r)✓✓$$
$$\dfrac{\beta}{s}, \dfrac{b_2}{s} = \text{纯函数}(r)✓ \Longrightarrow (a_i, \beta, b_2) = s\,(A_i(r), B_1(r), B_2(r))✓✓（\text{唐先生形式}✓）$$
$$\qquad \textbf{但本档说明}✓✓：\text{因}\ Q(r)\ \text{无实根}✓，\ \textbf{不存在} \text{实形状}\ r✓ \Longrightarrow \text{该参数化}\ \textbf{空}✗✓$$

## §3 独立复核（⚠️ 在跑 ✓）

$$\textbf{数值最小二乘}✓：\text{直接对}\ (a_1, a_2, a_3, \beta, b_2) \in (0,1]^5✓ \ \text{极小化}\ \sum_r\big(\sum a_i^{2r+1} - \beta^{2r+1} - b_2^{2r+1}\big)^2✓（\text{归一化}✓）$$
$$\qquad \text{起点数}\ 4000✓；\ \text{另设两组对照}✓（\text{三条件系统}✓；\text{放宽正性}✓） \ —— \ \textbf{结果待回}⚠️✓$$
$$\qquad \textbf{诚实标注}⚠️✓：\text{若复核给出残差可达}\ 0✓ \Longrightarrow \text{本档判空}\ \textbf{有误}✗✓，\text{须立即勘误}✓$$

## §4 与既有分层的一致性（✓✓）

$$\mathcal D_{\partial} = \text{归}\ (2+2)✓；\ \mathcal D_{\mathrm{coll}} = \varnothing✓；\ \mathcal D_{\mathrm{reg}} = \varnothing✓（\text{本档}✓） \Longrightarrow \ \textbf{exact-cancellation 类}\ \mathcal Z \cap E = \varnothing✓✓$$
$$\qquad \textbf{注意}✓✓：\text{此为}\ \textbf{强于} \text{C-369 的「碰撞部分排除」}✓✓（\text{那时}\ \mathcal D_{\mathrm{reg}}\ \text{仍 OPEN}✓）$$

## §5 下一步（✓✓）

$$\textbf{Bridge A}✓✓：\text{小奇频} \Longrightarrow \text{近}\ \mathcal Z \Longrightarrow \text{偶频代价} > \tfrac12✓ \ —— \ \text{现}\ \mathcal Z \cap E = \varnothing\ \text{已闭合}✓✓，\text{故}\ \text{此箭头}\ \textbf{才} \text{有意义}✓✓$$
$$\textbf{禁项}✓✓：\textbf{不}写\ H = \varnothing✗；\textbf{不}跳步✗；\textbf{不}把\ \mathcal Z \cap E = \varnothing\ \text{升级为}\ H = \varnothing✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 无实根判空  命中文件数=0    :: 
技术词 形状空间零维 命中文件数=0    :: 
技术词 尺度剥离     命中文件数=0    :: 
```
- 运行记录 ✓：`/tmp/c370.py`／`/tmp/c370b.py`（消元 ✓）；本档复核脚本（最小二乘 ✓，**在跑** ⚠️）
- **本档有计算**（符号 ＋ 数值，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`H = \varnothing` 已证 ✗；`\mathcal Z \cap E = \varnothing` 已获**独立数值复核** ✗（**待回** ⚠️）；四次方程已解析求解 ✗
