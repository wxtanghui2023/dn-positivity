已查地图（**先查后写**）：`C-380-39`（**覆盖性警告** ✓✓）、`C-380-38`（**窗口来源** ✓✓）、`C-380-36`（**B 支 Sturm 封口** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-40：B-Window Boundary Identity Audit（注册＋身份查明）**，**有计算（符号 ＋ 精确根，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 问题（唐先生定）}✓✓：\boxed{\text{到底是什么方程定义了 B 支真实上端？}}✓✓ \ —— \ \textbf{只回答这一个问题}✓✓$$
$$\textbf{② B 支上四个条件的边界根（s = A(-t) 下逐项化简）}✓✓：$$
$$\qquad \textbf{① }Q_2 \le -\tfrac12 \iff s \le \tfrac{7}{16} \iff p_1(t) = 64t^3 - 18t + 1 \le 0✓✓ \ —— \ \text{正根}\ \approx 0.056186,\ \mathbf{0.5}✓✓ \Longrightarrow t \le 0.5✓$$
$$\qquad \textbf{② }Q_4(-t, A) \le -\tfrac12 \iff R_B(t) \ge 0✓✓，\ R_B = 2048t^5 - 512t^4 - 1408t^3 + 224t^2 + 52t - 1✓✓$$
$$\qquad \qquad \textbf{实根}（在\ (0,1)\ 内）✓✓：\boxed{0.01799464,\ \mathbf{0.28425257},\ 0.86172964}✓✓$$
$$\qquad \textbf{③ }s \ge m^2 \iff A \ge t^2 \iff -32t^3 + 24t + 1 \ge 0✓✓ \ —— \ \text{实根} \approx \mathbf{0.886152}✓✓$$
$$\qquad \textbf{④ 判别式}\ D = 512t^4 - 128t^2 + 7 \ge 0✓✓ \ —— \ \text{正根} \approx \mathbf{0.28426366},\ 0.41133219✓✓（t^2 = \tfrac18 \mp \tfrac{\sqrt2}{32}✓）$$
$$\textbf{③ ⭐⭐ 身份查明（本档核心）}✓✓：\boxed{\text{绑定约束是 ②}}✓✓ \ —— \ \text{因其余三个的边界都}\ \textbf{远在}\ \text{外侧}✓✓：$$
$$\qquad ① \Longrightarrow t \le 0.5✓；\ ③ \Longrightarrow t \le 0.886✓；\ ④ \Longrightarrow t \le 0.28426366✓✓；\ \textbf{②} \Longrightarrow t \le \boxed{0.28425257}✓✓（\textbf{最小}✓）$$
$$\qquad \Longrightarrow \ \boxed{t_B = 0.28425257\ldots\ \text{是 B 支真实上端}}✓✓ \ —— \ \textbf{来自方程}\ R_B(t) = 0✓✓$$
$$\textbf{④ ⚠️⚠️ 认证窗口确实截断了可行集}✗✗：\boxed{1137/4000 = 0.28425 < t_B = 0.28425257}✗✗（\text{差}\ \mathbf{2.6 \times 10^{-6}}✓✓）$$
$$\qquad \textbf{各条件在}\ \tfrac{1137}{4000}\ \text{处仍全部成立}✓✓：p_1 = -2.6466 \le 0✓；\ R_B = \mathbf{+0.000365} \ge 0✓；\ A - t^2 = +0.2597 \ge 0✓；\ D = +0.000351 \ge 0✓✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{窗口}\ [\tfrac18,\ \tfrac{1137}{4000}]\ \textbf{确实截掉了可行集的一小段}}✗✓ \Longrightarrow \ \textbf{不是「小数误差」}✗✓ \Longrightarrow \ \textbf{须扩大窗口}✓✓$$
$$\qquad \qquad ⭐ \textbf{交叉核对}✓✓：C\text{-}380\text{-}33\ \text{扫描给上端}\ \mathbf{0.284253}✓✓ \ —— \ \textbf{与}\ R_B\ \text{根}\ 0.28425257\ \textbf{吻合}✓✓$$
$$\qquad \qquad \Longrightarrow \ \boxed{\textbf{扫描是对的，人工窗口是错的}}✗✓ \ —— \ \textbf{C-380-39 的警告被证实}✓✓$$
$$\textbf{⑤ 扩大方案}✓✓：\text{取有理上界}\ > t_B✓，\ \text{如}\ \boxed{11371/40000 = 0.284275}✓✓（\text{或}\ 0.2843✓）$$
$$\qquad \Longrightarrow \ \textbf{须在扩大后的窗口上}\ \textbf{重做 B 支 Sturm 封口}✗✓（P_B\ \text{的多项式正性}✓✓） \ —— \ \textbf{不可沿用旧窗口结论}✗✓$$
$$\textbf{⑥ ⚠️ C 支高带仍 OPEN}✗✓：R_C(u) = 1024u^2 - 448u + 27 \ge 0 \iff u \le 0.072175\ \textbf{或}\ u \ge 0.365325✓✓（\text{即}\ t \ge 0.6044✓）$$
$$\qquad \qquad \text{高带}\ t \ge 0.6044\ \textbf{不能被 ② 排除}✗✓ \ —— \ \text{因}\ R_B > 0\ \text{于}\ (0.28425,\ 0.86173)✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{C 支高带的}\ \textbf{解析排除仍 OPEN}}✗✓ \ —— \ \textbf{扫描的「0 个点」不足以封口}✗✓（\textbf{与唐先生一致}✓✓）$$
$$\textbf{⑦ 账本（采纳唐先生口径）}✓✓：\boxed{\text{A CLOSED}}✓✓；\ \boxed{\text{B CLOSED \textbf{only on its certified window}}}✓✓；\ \boxed{\text{C CLOSED \textbf{only on its certified window}}}✓✓$$
$$\qquad \boxed{\text{global coverage}\ \textbf{OPEN}}✗✓；\ \boxed{\mathcal F_0 = \varnothing\ \textbf{OPEN}}✗✓$$
$$\textbf{⑧ 纪律}✓✓：\textbf{不}碰\ \inf Q_5✗✓；\ \textbf{不}启动 Level 3✗✓；\ \textbf{不}为维持原路线而强行补证✗✓ \ —— \ \textbf{负结果有价值}✓✓：\textbf{暴露了窗口人为截断风险}✓✓$$

## §1 记录（✓✓）

$$\textbf{根清单}✓✓：R_B：0.01799464,\ 0.28425257,\ 0.86172964✓✓；p_1：0.056186,\ 0.5✓；A - t^2：0.886152✓；D：0.28426366,\ 0.41133219✓✓$$
$$\textbf{1137/4000 处四条件}✓✓：\text{全部成立}✓✓（p_1 = -2.6466✓；R_B = +0.000365✓；A - t^2 = +0.2597✓；D = +0.000351✓）$$
$$\textbf{身份}✓✓：\min(0.5,\ 0.886,\ 0.28426366,\ 0.28425257) = 0.28425257 = t_B✓✓ \Longrightarrow \textbf{绑定者 = ②}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **A** ✓ | **CLOSED** ✓✓✓ |
| **B** ✓ | **仅在其认证窗口上 CLOSED；真实上端 `t_B = 0.28425257 > 窗口上端`** ✗✓ |
| **C** ✓ | **仅在其认证窗口上 CLOSED；高带解析排除 OPEN** ✗✓ |
| **B 窗扩大** ✓ | **本档：需要（有理上界 `11371/40000`）；须重做 Sturm** ✗✓ |
| **global coverage** ✓ | **OPEN** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✗✓ |
| Level 3 ✓ | **禁止启动** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗✓；\ \text{global coverage CLOSED}✗✓；\ \text{Level 2 CLOSED}✗✓；\ \text{B 窗无需调整}✗✗（\textbf{须调整}✓）$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{证实}\ \text{窗口截断}✓✓；\ \text{扫描值正确}✓✓；\ \text{C 支高带}\ \textbf{仍 OPEN}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}碰\ \inf Q_5✗✓；\ \textbf{不}启动 Level 3✗✓；\ \textbf{不}强行补证原覆盖命题✗✓；\ \textbf{不}把扫描当解析排除✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy 精确根，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 边界身份审计 命中文件数=0    ::
技术词 窗口截断     命中文件数=2    :: ./RESEARCH-CONSTITUTION.md ./M-NOGO-P1f-P1g.md
技术词 绑定约束     命中文件数=4    :: ./C335-P2-chebyshev-moment-joint-constraints-five-parameter-reduction.md ./C115-calibration-is-endpoint-degeneracy-a-new-wall.md ./E204a-large-window-capacity-decay-robust.md
```
- 运行记录 ✓：`python3 -`（sympy 四条件边界根 ＋ `1137/4000` 处符号核验 ✓）
