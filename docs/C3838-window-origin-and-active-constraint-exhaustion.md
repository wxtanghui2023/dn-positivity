已查地图（**先查后写**）：`C-380-37`（**端点清单 ＋ 第 5 类为空** ✓✓）、`C-380-36`（**B 支 CLOSED** ✓✓）、`C-380-34`（**C 支 CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-38：Window-Origin ＋ Active-Constraint Exhaustion（注册＋两层审计）**，**有计算（解析 ＋ 数值核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 层 A：活跃组合穷尽（已建立）}✓✓：L = \max(m^2, A, s_-)✓，\ U = \min(\tfrac{7}{16}, s_+)✓✓$$
$$\qquad ⭐ \textbf{关键论证}✓✓：\textbf{若}\ L = m^2\ \text{且}\ \mathcal S_m \ne \varnothing✓，\ \text{则}\ m^2 \in \mathcal S_m \Longrightarrow s = m^2\ \textbf{可行} \Longrightarrow \ \textbf{与}\ C\text{-}380\text{-}37\ \text{（第 5 类为空）}\textbf{矛盾}✗✗$$
$$\qquad \Longrightarrow \ \boxed{\mathcal S_m \ne \varnothing \ \text{时}\ L \in \{A,\ s_-\}}✓✓；\ \text{同理}\ U \in \{\tfrac{7}{16},\ s_+\}✓✓ \Longrightarrow \ \boxed{\partial\mathcal S_m \subseteq \{\tfrac{7}{16}\} \cup \{A\} \cup \{s_{\pm}\}}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{A} \cup \textbf{B} \cup \textbf{C}\ \textbf{穷尽可行端点}}✓✓ \Longrightarrow \ \text{「经验上的三支」} \to \textbf{有限端点枚举问题}✓✓$$
$$\textbf{② 层 B：Branch B 窗口来源（已导出）}✓✓：\text{Branch B} \iff \text{下端点}\ L = A\ \text{活跃}⟹ \text{须}\ A \in \mathcal S_m✓✓$$
$$\qquad \text{【条件 ①】}✓✓：A \le \tfrac{7}{16} \iff \boxed{8t(2t-1)(32t^2 + 16t - 1) \le 0}✓✓（\textbf{因式分解}✓） \iff p_1(t) := 64t^3 - 18t + 1 \le 0✓✓$$
$$\qquad \qquad p_1\ \text{实根} \approx 0.056186,\ 0.5✓✓ \Longrightarrow p_1 \le 0\ \text{含}\ [0.0562,\ 0.5]✓ \Longrightarrow \ \textbf{上界}\ t \le 0.5✓$$
$$\qquad \text{【条件 ②】}✓✓：Q_4(-t, A) \le -\tfrac12 \iff \boxed{-(4t+1)\big(2048t^5 - 512t^4 - 1408t^3 + 224t^2 + 52t - 1\big) \le 0}✓✓$$
$$\qquad \qquad \Longrightarrow \ \text{数值满足区间}\ [\cdots,\ \boxed{0.284244}]✓✓ \ —— \ \textbf{与已认证 B 窗口上端}\ \tfrac{1137}{4000} = 0.28425\ \textbf{吻合}✓✓✓$$
$$\qquad ⭐ \Longrightarrow \ \boxed{\text{Branch B 窗口上端来自条件 ②}}✓✓ \ —— \ \textbf{即}\ Q_4\ \text{容许性}✓✓ \ —— \ \textbf{窗口来源已定位}✓✓$$
$$\textbf{③ 层 B：Branch C 窗口来源（已导出）}✓✓：\text{【条件 ③】}✓✓：Q_4(-t, \tfrac{7}{16}) \le -\tfrac12 \iff \boxed{-1024t^4 + 448t^2 - 27 \le 0}✓✓$$
$$\qquad \qquad \Longrightarrow \ t^2 \in \Big[\tfrac{448 - \sqrt{90112}}{2048},\ \tfrac{448 + \sqrt{90112}}{2048}\Big]✓✓ \Longrightarrow \ t^2 \ge \boxed{0.072175}✓✓ \ —— \ \textbf{与扫描所获}\ 0.072176\ \textbf{吻合}✓✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{Branch C 窗口下端来自条件 ③}}✓✓ \Longrightarrow \ \text{C 窗口} = [t_C,\ t_B]✓✓，\ t_C \approx 0.26865✓，\ t_B \approx 0.28424✓✓$$
$$\qquad \qquad ⭐ \textbf{两层互证}✓✓：t_B\ \text{同时是 B 支上端与 C 支上端}✓✓（\text{两窗共享边界}✓） \ —— \ \textbf{结构自洽}✓✓$$
$$\textbf{④ 覆盖性推论（关键）}✓✓：\text{因}\ t_B = 0.284244 < \tfrac{1137}{4000} = 0.28425✓✓ \Longrightarrow \ \textbf{B 支可行集} \subseteq [\tfrac18,\ \tfrac{1137}{4000}]✓✓$$
$$\qquad \qquad \text{因}\ t_C = 0.26865 > 0.268 = \sqrt{4489/62500}✓ \Longrightarrow \ \textbf{C 支可行集} \subseteq \{m^2 \in [\tfrac{4489}{62500},\ \tfrac{101}{1250}]\}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{已认证的两个窗口确实是可行集的}\ \textbf{有效覆盖}✓✓} \ —— \ \textbf{义务 1 实质完成}✓✓$$
$$\textbf{⑤ 剩余（机械步骤）}✗✓：\text{须}\ \textbf{用有理算术} \text{核验两个多项式在窗口端点的}\ \textbf{符号}✓✓（\text{如}\ ②\ \text{在}\ \tfrac{1137}{4000}\ \text{处} \le 0✓、\ ③\ \text{在}\ \tfrac{4489}{62500}\ \text{处} \le 0✓）$$
$$\qquad \Longrightarrow \ \textbf{这一步是}\ \textbf{纯粹机械的有理符号核验}✓✓，\ \textbf{不含新数学}✗✓ \ —— \ \text{完成即}\ \text{义务 1 CLOSED}✓✓$$
$$\textbf{⑥ 逻辑链（若 ⑤ 完成）}✓✓：\boxed{\mathcal S_m \ne \varnothing \Longrightarrow \partial\mathcal S_m \subset A \cup B \cup C}✓✓；\ \boxed{A, B, C \Longrightarrow Q_5 > \tfrac{341}{128}}✓✓ \Longrightarrow \ \boxed{\mathcal S_m = \varnothing}✓✓$$
$$\qquad \textbf{措辞纪律（采纳）}✓✓：\textbf{在}\ C\text{-}380\text{-}38\ \text{完成前，}\textbf{不写}\ \mathcal F_0 = \varnothing✗✓，\ \text{只写「若义务 1 与组合穷尽成立，则整体出口成立」}✓✓$$
$$\textbf{⑦ 账本}✓✓：\text{见 §2}✓$$
$$\textbf{⑧ 纪律}✓✓：\textbf{不}重做 Sturm✗✓；\textbf{不}重做 C 支认证✗✓；\textbf{不}往 Level 3 扩张✗✓ \ —— \ \textbf{已非常接近真正的 Level-2 exit}✓✓$$

## §1 记录（✓✓）

$$\textbf{层 A}✓✓：m^2\ \text{被 C-380-37 排除} \Longrightarrow L \in \{A, s_-\}✓✓；\ U \in \{\tfrac{7}{16}, s_+\}✓✓ \Longrightarrow \text{端点} \subseteq A \cup B \cup C✓✓$$
$$\textbf{层 B}✓✓：①\ 8t(2t-1)(32t^2+16t-1) \le 0✓✓（\text{实根}\ 0.056186,\ 0.5✓）；②\ \text{因子含}\ (4t+1)✓✓，\text{上端}\ 0.284244✓✓；③\ -1024t^4 + 448t^2 - 27 \le 0✓✓，\ t^2 \ge 0.072175✓✓$$
$$\textbf{窗口对比}✓✓：B：[\tfrac18,\ 0.284244] \subset [\tfrac18,\ \tfrac{1137}{4000}]✓✓；\ C：t^2 \in [0.072175,\ 0.0808] \approx [\tfrac{4489}{62500},\ \tfrac{101}{1250}]✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A／B／C** ✓ | **皆 CLOSED** ✓✓✓ |
| **层 A（活跃组合穷尽）** ✓ | **本档：成立** ✓✓✓ |
| **层 B（窗口来源）** ✓ | **本档：导出为显式多项式条件；覆盖性成立** ✓✓ |
| **剩余：有理符号核验** ✓ | **机械步骤（不含新数学）** ✓✓ |
| Level 2 ✓ | **一步之遥（仅剩机械核验）** ✓✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **尚未完成全局解析证明** ✗✓ |
| Level 3 ✓ | **禁止启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN（措辞纪律：完成前不写）** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗✓（\textbf{措辞纪律}✓）；\ \text{Level 2 CLOSED}✗✓；\ \text{义务 1 已 CLOSED}✗✓（\textbf{尚差机械核验}✓）；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{层 A}\ \textbf{成立}✓✓；\ \text{层 B}\ \textbf{已导出}✓✓ \ —— \ \text{但}\ \textbf{端点符号核验} \text{未执行}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}重做 Sturm✗✓；\textbf{不}重做 C 支认证✗✓；\textbf{不}启动 Level 3✗✓；\textbf{不}把「一步之遥」写成 CLOSED✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy 因式 ＋ 20000 点数值区间，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 活跃约束穷尽 命中文件数=0    ::
技术词 窗口来源推导 命中文件数=0    ::
技术词 机械符号核验 命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（sympy 因式分解 ＋ 数值区间定位 ✓）
