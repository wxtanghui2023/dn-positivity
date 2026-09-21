已查地图（**先查后写**）：`C-380-41/42`（**B 扩大窗口 ＋ C 高带** ✓✓）、`C-380-37/38`（**端点完备性 ＋ 组合穷尽** ✓✓）、`C-380-34/36`（**C／B 认证** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-43：global endpoint coverage ⇒ Level 2 拼接（逻辑量词审计）**，**零新数值探索（按唐先生指示 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 量词链（核心）}✓✓：\text{目标}✓：\text{对}\ \textbf{每一点} \text{two-level 可行点}\ (m, s)✓，\ \text{证}\ Q_5 > \tfrac{341}{128}✓✓$$
$$\qquad \forall (m, s)\ \text{可行}✓：s \in \mathcal S_m✓ \Longrightarrow \min_{s \in \mathcal S_m}Q_5\ \text{在}\ \textbf{端点} \text{取得}✓✓（\text{见 ③}） \Longrightarrow \text{端点} \in \partial\mathcal S_m \subseteq \{\tfrac{7}{16}\} \cup \{A\} \cup \{s_{\pm}\}✓✓$$
$$\qquad \Longrightarrow \ \textbf{归约为}\ \textbf{四类端点实现}✓✓（\text{见 ②}），\ \text{逐类给出}\ Q_5 > \tfrac{341}{128}✓✓ \Longrightarrow \ \boxed{\forall\ \text{可行点}：Q_5 > \tfrac{341}{128}}✓✓$$
$$\textbf{② ⭐ 端点实现表（穷尽）}✓✓：U = \min(\tfrac{7}{16}, s_+)✓，\ L = \max(m^2, A, s_-)✓✓（m^2\ \text{已由}\ C\text{-}380\text{-}37\ \text{排除}✓）$$
$$\qquad \textbf{①}\ U = \tfrac{7}{16} \Longrightarrow \text{端点}\ (m, \tfrac{7}{16}) = \textbf{Branch A}✓✓（C\text{-}380\text{-}29／31✓）$$
$$\qquad \textbf{②}\ L = A \Longrightarrow \text{端点}\ (m, A(m)) = \textbf{Branch B}✓✓（C\text{-}380\text{-}35／36／41✓）$$
$$\qquad \textbf{③}\ U = s_+\ \text{或}\ L = s_- \Longrightarrow \text{端点}\ (m, s_{\pm}(m)) = \textbf{Branch C}✓✓（C\text{-}380\text{-}33／34／42✓）$$
$$\qquad \Longrightarrow \ \boxed{\text{A} \cup \text{B} \cup \text{C}\ \textbf{覆盖一切端点实现}}✓✓ \ —— \ \textbf{无第五类}✓✓$$
$$\textbf{③ 凸性步骤（严格，复核）}✓✓：Q_5 = 4m \cdot B(s)✓，\ m < 0✓ \Longrightarrow \min_{s \in \mathcal S_m}Q_5 = 4m \cdot \max_{s \in \mathcal S_m}B(s)✓✓$$
$$\qquad B\ \textbf{凸}✓ \Longrightarrow \max_{s \in [L, U]}B(s) = \max(B(L), B(U))✓✓（\textbf{闭区间端点}✓） \Longrightarrow \ \textbf{端点原则严格}✓✓$$
$$\qquad \text{前提}✓✓：\mathcal S_m = [L, U]\ \text{为}\ \textbf{闭区间}✓（\text{由}\ C\text{-}380\text{-}38\ \text{的四条区间条件}✓✓；\ \text{空集时无端点要求}✓）$$
$$\textbf{④ 各支证书的 m-范围覆盖（逐项核验）}✓✓：$$
$$\qquad \textbf{A}✓：\text{证书要求}\ t \le t_0 = 0.268653✓✓（C\text{-}380\text{-}31\ \text{的容许性}✓） \ —— \ \text{与}\ s = \tfrac{7}{16}\ \text{可行性一致}✓✓$$
$$\qquad \textbf{B}✓：\text{证书在}\ I_B = [\tfrac18, \tfrac{11371}{40000}]✓✓，\ \textbf{覆盖真实上端}\ t_B = 0.28425257✓✓（C\text{-}380\text{-}40／41✓）$$
$$\qquad \textbf{C}✓：\text{低带证书}\ m^2 \in [\tfrac{4489}{62500}, \tfrac{101}{1250}]✓✓；\ \text{高带}\ u \ge u_2\ \textbf{解析已杀}✓✓（C\text{-}380\text{-}42✓） \Longrightarrow \ \textbf{C 全窗口覆盖}✓✓$$
$$\textbf{⑤ ⭐ 主结论：two-level 五约束集为空}✓✓：\text{因}\ Q_5 > \tfrac{341}{128} > -\tfrac12✓✓ \Longrightarrow \ \text{可行点}\ \textbf{不能满足}\ Q_5 \le -\tfrac12✓✓$$
$$\qquad \Longrightarrow \ \boxed{\mathcal S_m \cap \{Q_5 \le -\tfrac12\} = \varnothing}✓✓ \Longrightarrow \ \boxed{\textbf{two-level 五约束集（}Q_1 \dots Q_5 \le -\tfrac12\text{）}\ \textbf{为空}}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{Level 2} = \textbf{CLOSED}}✓✓✓ \ —— \ \text{在}\ \textbf{two-level 族} \text{上}✓✓（\text{六约束亦空}✓，\text{因五约束已空}✓✓）$$
$$\textbf{⑥ ⚠️ 但}\ \mathcal F_0 = \varnothing\ \textbf{仍 OPEN}✗✓：\textbf{关键区别}✓✓：\text{本档结论限定于}\ \textbf{two-level 族}✓✓（X = \{m + a, m + a, m - a, m - a\}✓）$$
$$\qquad \text{而}\ \mathcal F_0\ \text{是}\ \textbf{一般四点} \text{上的集合}✓✓ \Longrightarrow \ \text{须补}\ \boxed{\text{一般四点} \to \text{two-level 的稳定性／坍缩}}✗✓ \ —— \ \textbf{即 Level 3}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\mathcal F_0 = \varnothing\ \textbf{仍 OPEN}}✗✓ \ —— \ \textbf{Level 3 继续 FROZEN}✗✓（\textbf{与唐先生口径一致}✓✓）$$
$$\textbf{⑦ 量词细节审计（三项）}✓✓：\textbf{(a)}✓ \text{端点原则须}\ \textbf{逐 m 成立}✓✓（\text{非对全部}\ (m, s)\ \text{一次性}✓）；\ \textbf{(b)}✓ \text{证书是}\ \textbf{窗口化} \text{的}✓✓，\ \textbf{须与覆盖性配对}✓✓（\text{已在}\ ④\ \text{逐项核验}✓）；$$
$$\qquad \textbf{(c)}✓ \ \textbf{不得}把「端点\ \ge \tfrac{341}{128}」\ \text{写成「全局}\ Q_5 \ge \tfrac{341}{128}\ \text{定理}」✗✓（\text{目标始终是}\ \textbf{可行集为空}✓✓，\ \textbf{而非独立极小值定理}✓✓）$$
$$\textbf{⑧ 账本}✓✓：\text{见 §2}✓$$

## §1 拼接链（✓✓）

$$\mathcal S_m = [L, U]✓（C\text{-}380\text{-}38✓） \to \partial\mathcal S_m \subseteq \{\tfrac{7}{16}, A, s_{\pm}\}✓（C\text{-}380\text{-}37／38✓） \to \text{四类实现} \to A／B／C✓（各支认证✓）$$
$$\qquad \to \forall\ \text{可行}：Q_5 > \tfrac{341}{128}✓ \to \mathcal S_m \cap \{Q_5 \le -\tfrac12\} = \varnothing✓ \to \textbf{Level 2 CLOSED}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A／B／C** ✓ | **皆 CLOSED（含窗口覆盖）** ✓✓✓ |
| **endpoint `s = m^2`** ✓ | **CLOSED（infeasible）** ✓✓ |
| **combination exhaustion** ✓ | **CLOSED** ✓✓ |
| **global coverage** ✓ | **本档：闭合** ✓✓✓ |
| **Level 2（two-level 五约束为空）** ✓ | **CLOSED** ✓✓✓ |
| **`\mathcal F_0 = \varnothing`（一般四点）** ✓ | **OPEN —— 须 Level 3** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **不作为目标；不宣称已证** ✗✓ |
| Level 3 ✓ | **FROZEN** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗✓；\ \inf Q_5 = \tfrac{341}{128}\ \text{已证}✗✓；\ \text{Level 3 已启动／完成}✗✓；\ \text{本档结论适用于一般四点}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{Level 2}\ \textbf{CLOSED}✓✓（\textbf{限定 two-level 族}✓）；\ \mathcal F_0\ \textbf{仍 OPEN}✗✓；\ \text{三处量词细节已审}✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}做新数值探索✗✓；\ \textbf{不}启动 Level 3✗✓；\ \textbf{不}碰\ \inf Q_5✗✓；\ \textbf{不}把\ \text{two-level 结论} \text{外推到一般四点}✗✓$$

## §5 边界（✓✓）

$$\textbf{零新计算}✓（\text{逻辑拼接}✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 量词链审计  命中文件数=0    ::
技术词 端点实现表  命中文件数=0    ::
技术词 定义映射     命中文件数=1    :: ./E6-7-strength-coordinate-reformulation.md
```
- 运行记录 ✓：`scripts/tech_word_check.sh`✓（本档**零新数值探索** ✓）
