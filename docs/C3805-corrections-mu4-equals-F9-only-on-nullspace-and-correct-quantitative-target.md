已查地图（**先查后写**）：`C-380-4`（**化简表 ＋ `\mu_4`** ✓✓）、`C-380-3`（`r_* = 4` ✓✓）、`C-371`（`\mathcal Z \cap E = \varnothing` ✓✓）、`C-349`（四阶 nullspace ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-5：`\mu_4` 与 `F_9` 关系勘误 ＋ 定量目标修正**，**有计算（数值核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① ⭐ 勘误一（关键）}✗✓：\ \boxed{F_9 = 256\,\mu_4\ \textbf{只在}\ \mathcal Z\ \text{上成立}}✓✓ \ —— \ E_{\mathrm{even}}\ \textbf{不在}\ \mathcal Z\ \text{上}✗✓$$
$$\qquad \textbf{正确恒等式}✓✓：\ \boxed{F_9 = 9\mu_0 - 120\mu_1 + 432\mu_2 - 576\mu_3 + 256\mu_4}✓✓（\text{数值差}\ \sim 10^{-14}✓✓）$$
$$\qquad \textbf{反例}✗✓：\text{在}\ \text{C-378}\ V_2\ \text{极值点}✓，\ \sigma = (1,1,1,1,1)✓：\ 256\mu_4 = +381.2314✓ \ \textbf{而}\ F_9 = -1.2466✗✓（\text{差}\ 382.5✓）$$
$$\qquad \Longrightarrow \ \textbf{「仅}\ 256\mu_4\ \text{」}\ \textbf{不能}作为\ F_9\ \text{的代理}✗✓$$
$$\textbf{② ⭐ 勘误二}✗✓：\ \boxed{\mu_4 = 0 \ \textbf{不能}推出}\ (x, \sigma) \in \mathcal Z✗✓ \ —— \ \text{须}\ \textbf{同时} \text{有}\ \mu_0 = \mu_1 = \mu_2 = \mu_3 = 0✓✓$$
$$\qquad \text{数值}✓✓：\text{找到}\ \mu_4 \approx 0\ \text{而}\ \mu_0 \ne 0\ \text{的点}✓（3\ \text{例}✓；\text{如}\ \mu_4 = 3.86 \times 10^{-4}✓，\mu_0 = 0.8164✓）$$
$$\qquad \Longrightarrow \ \textbf{勘误三}✗✓：\ \boxed{\delta_4 > 0\ \textbf{不能}由紧性 ＋}\ \mathcal Z \cap E = \varnothing\ \textbf{推出}✗✓ \ —— \ \text{须}\ \textbf{单独论证}✓✓$$
$$\textbf{③ 仍然成立的部分}✓✓：\text{递推}\ \mu_{m+5} = e_1\mu_{m+4} - e_2\mu_{m+3} + e_3\mu_{m+2} - e_4\mu_{m+1} + e_5\mu_m✓✓（\text{标准}✓）$$
$$\qquad \text{在}\ \mu_0 = \dots = \mu_3 = 0\ \text{下}✓：\mu_5 = e_1\mu_4✓，\ \mu_6 = (e_1^2 - e_2)\mu_4✓✓ \Longrightarrow \ \mu_m = h_{m-4}(x)\,\mu_4✓✓（\textbf{每个固定}\ x✓）$$
$$\qquad \Longrightarrow \ \boxed{\text{每个固定}\ x\ \text{的高阶方向空间是}\ \textbf{一维}}✓✓（\textbf{不是} \text{全参数空间单变量}✗✓）$$
$$\textbf{④ 化简表结论保持不变}✓✓：R_r\ \text{的}\ \deg \ge 4\ \text{部分}\ \text{给出}\ \operatorname{span}\{\mu_4, \dots, \mu_r\}✓，\ a_{r,r} = 2^{2r} \ne 0✓✓$$
$$\textbf{⑤ 修正后的定量目标（本档核心）}✓✓：\ \boxed{\inf_{x \in E_{\mathrm{even}}}\min_{\sigma \in \mathcal S}\max_{0 \le r \le 12}\Big|F_{2r+1}\Big| > \tfrac12}✓✓ \ —— \ \textbf{不能}退化为\ \delta_4✗✓$$
$$\qquad \text{即}\ \text{须}\ \text{控制}\ \textbf{完整组合}\ \sum_{m=0}^{4}b_m\mu_m✓（b = (9, -120, 432, -576, 256)✓）\ \text{而非}\ \mu_4\ \text{单项}✗✓$$
$$\textbf{⑥ 逻辑收益}✓✓：\text{虽勘误}\ \text{削弱了}\ C\text{-}380\text{-}4\ \text{的一个外推}✗✓，\ \textbf{但} \text{保留了}\ \textbf{一维结构}✓✓ \Longrightarrow \ \text{幅度问题仍是}\ \textbf{低维}✓（\mu_0..\mu_4\ \text{五个量}✓，\ \text{且}\ E_{\mathrm{even}}\ \text{约束}\ \text{给}\ S_m\ \text{而非}\ \mu_m✓✓）$$

## §1 核验记录（✓✓）

$$\textbf{A}✓✓：F_9 = 9\mu_0 - 120\mu_1 + 432\mu_2 - 576\mu_3 + 256\mu_4✓ \ \text{数值差}\ 2.8 \times 10^{-14} \sim 4.5 \times 10^{-14}✓✓（6\ \text{组全通过}✓）$$
$$\textbf{B}✓✓：\Delta\ \text{极值点}\ \sigma = (1,-1,1,-1,1)✓：256\mu_4 = +142.3742✓ \ \textbf{而}\ F_9 = +3.0524✗✓（\text{差}\ 139.3✓）$$
$$\qquad \Longrightarrow \ \text{两例反例}\ \textbf{充分} \text{证明勘误一}✓✓$$
$$\textbf{读法}✓✓：\text{低阶}\ \mu_0, \dots, \mu_3\ \text{在}\ E_{\mathrm{even}}\ \text{上}\ \textbf{一般不消失}✗✓（\text{仅}\ \mathcal Z\ \text{上消失}✓），\ \text{且}\ \text{系数}\ (\pm120, \pm576✓)\ \textbf{远大于}\ 256✓$$
$$\qquad \Longrightarrow \ \text{低阶项在}\ F_9\ \text{中}\ \textbf{主导}✓✓ \ —— \ \text{故}\ \mu_4\ \text{单项}\ \textbf{无}代表性✗✓$$

## §2 修正后的任务链（✓✓）

$$\textbf{正确目标}✓✓：\ \inf_{x \in E_{\mathrm{even}}}\min_\sigma\max_r|F_{2r+1}| > \tfrac12✓✓（\text{与 C-380-2 原目标同构}✓）$$
$$\textbf{可用结构}✓：\text{① } F_{2r+1} = \sum_{m=0}^{r}a_{r,m}\mu_m✓（\text{由化简表}✓，a_{r,m}\ \text{已知}✓✓）；\ \text{② }\ \mu_m\ \text{由}\ \mu_0..\mu_4\ \text{与}\ x\ \text{决定}✓✓$$
$$\textbf{新提法}✓✓：\text{在}\ E_{\mathrm{even}}\ \text{上，}\ \text{奇频向量}\ = \ \textbf{五维线性泛函} \text{作用于}\ (\mu_0, \dots, \mu_4)✓✓$$
$$\qquad \Longrightarrow \ \text{问题} = \ \text{五维}\ \textbf{联合} \text{问题}✓，\ \textbf{不是} \text{一维}\ \delta_4✗✓$$

## §3 与原目标的关系（✓✓）

$$\textbf{与}\ \mathcal Z \cap E = \varnothing\ \text{的关系}✓✓：\text{该结论}\ \text{仍}\ \textbf{CLOSED}✓，\ \textbf{但} \text{它}\ \textbf{不}提供\ \delta_4 > 0✗✓；\ \text{它提供的是}\ \textbf{全部奇频不能同时为零}✓✓$$
$$\qquad \Longrightarrow \ \text{这正是}\ \max_r|F_{2r+1}| > 0\ \text{型结论}✓（\textbf{非}数值\ > \tfrac12✗✓）$$
$$\textbf{定量缺口}✓✓：\text{从}\ \max_r|F_{2r+1}| > 0\ \text{到}\ > \tfrac12✓ \ —— \ \textbf{正是} \text{Bridge A 的最后一公里}✓✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}4` 化简表 ✓ | **CLOSED（符号确认）** ✓✓ |
| 一维结构（每固定 `x`）✓ | **CLOSED** ✓✓ |
| `\mu_4 = 0 \iff \in \mathcal Z` ✓ | **勘误：须连同 `\mu_0..\mu_3 = 0`** ✗✓ |
| `\delta_4 > 0` ✓ | **未证（勘误三）** ✗✓ |
| `F_9 = 256\mu_4` ✓ | **勘误：仅 `\mathcal Z` 上** ✗✓ |
| `\inf_{E_{\mathrm{even}}}\min_\sigma\max_r\|F_{2r+1}\| > \tfrac12` ✓ | **OPEN ← 修正后的唯一目标** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\text{Bridge A 已闭合}✗；\ \delta_4\ \text{已证}\ > 0✗；\ F_9 = 256\mu_4\ \text{在}\ E_{\mathrm{even}}\ \text{上}✗；\ \text{紧性给出}\ \delta_4✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档为}\ \textbf{勘误档}✓；\ C\text{-}380\text{-}4\ \text{的}\ \textbf{化简表与一维结构保持}✓✓，\ \text{但}\ \text{其}\ \text{「单一量」外推}\ \textbf{被削弱}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 商空间等式仅局部 命中文件数=0    :: 
技术词 低阶未消项  命中文件数=0    :: 
技术词 定量目标修正 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（恒等式 `A` 6 组 ＋ 反例搜索 `B` ✓）
- **本档有计算**（数值核验，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
