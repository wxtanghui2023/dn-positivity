已查地图（**先查后写**）：`C-380-38`（**两层审计** ✓✓）、`C-380-37`（**第 5 类为空** ✓✓）、`C-380-35/33`（**窗口扫描** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-39：Rational Endpoint Sign Closure（注册＋核验＋覆盖性警告）**，**有计算（精确有理 ＋ Sturm，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓，含**关键警告** ⚠️）

$$\textbf{① 层 A 记为 CLOSED（采纳）}✓✓：\text{由}\ C\text{-}380\text{-}38：\ L = m^2 \land \mathcal S_m \ne \varnothing \Longrightarrow m^2 \in \mathcal S_m✓，\ \text{与}\ C\text{-}380\text{-}37\ \text{矛盾}✗✗ \Longrightarrow L \in \{A, s_-\}✓✓$$
$$\qquad \Longrightarrow \ \text{端点确无第五类}✓✓ \ —— \ \textbf{层 A CLOSED}✓✓✓$$
$$\textbf{② ⚠️ B 支符号核验结果与预期相反}✗✗：\boxed{R_B(t) = 2048t^5 - 512t^4 - 1408t^3 + 224t^2 + 52t - 1}✓✓$$
$$\qquad \boxed{R_B\big(\tfrac{1137}{4000}\big) = \tfrac{182598168457}{500000000000000} \approx \mathbf{+0.000365} > 0}✗✗ \ —— \ \textbf{而非负}✗\ —— \ \textbf{与唐先生预期相反}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{提议的符号论证不成立}}✗✓（\text{因}\ ②\ \text{在该点仍}\ \textbf{成立}✓）：\ \text{不能由}\ R_B(\tfrac{1137}{4000}) < 0\ \text{推出}\ t_B < \tfrac{1137}{4000}✗✓$$
$$\textbf{③ ⚠️ 区间无根结论亦不成立}✗✗：\boxed{\texttt{count\_roots}(R_B,\ \tfrac{1137}{4000},\ 1) = 2}✗✗ \ —— \ \textbf{非}\ 0✗✓$$
$$\qquad \Longrightarrow \ \text{该区间上}\ R_B\ \text{的符号}\ \textbf{无简单结论}✗✓ \ —— \ \text{不能}\ \text{用「单根 ＋ 端点符号」}\ \text{完成覆盖}✗✗$$
$$\qquad \text{参考值}✓：R_B(\tfrac18) = \tfrac{99}{16} \approx 6.1875 \gg 0✓✓ \Longrightarrow \ \textbf{下端}\ t = \tfrac18\ \text{处}\ ②\ \text{充裕成立}✓✓$$
$$\textbf{④ C 支符号核验（如预期）}✓✓：R_C(u) = 1024u^2 - 448u + 27✓✓（u = t^2✓）$$
$$\qquad \boxed{R_C\big(\tfrac{4489}{62500}\big) = \tfrac{25718619}{244140625} \approx \mathbf{+0.1053} > 0}✓✓ \ —— \ \textbf{符号如预期}✓✓$$
$$\qquad ⚠️ \textbf{但}✗✓：R_C \ge 0 \iff u \le u_1\ \textbf{或}\ u \ge u_2✓✓，\ u_1 = \tfrac{7}{32} - \tfrac{\sqrt{22}}{32} \approx 0.072175✓，\ u_2 = \tfrac{7}{32} + \tfrac{\sqrt{22}}{32} \approx \mathbf{0.365325}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{正集是两带}✗✓ \Longrightarrow \ \textbf{仅凭}③\ \text{不能}\ \text{排除上带}\ [u_2,\ \tfrac{7}{16}]✗✓ \Longrightarrow \ \textbf{C 支覆盖未完成}✗✓$$
$$\textbf{⑤ 上带排除（数值）}✓：\ \text{在 A 支上、}u \in [0.3654,\ 0.4375]\ \text{的双约束可行点数} = \boxed{0／20001}✓✓$$
$$\qquad \textbf{对照}✓：\text{同区段 A 支对称性下}\ Q_2\ \text{可行点亦}\ 0✓✓ \Longrightarrow \ \textbf{上带确被排除}✓✓$$
$$\qquad \qquad ⚠️ \textbf{诚实标注}✗✓：\textbf{这是数值}，\ \textbf{须补解析证明}✗✓$$
$$\textbf{⑥ B 支窗口下端来源（解析）}✓✓：Q_1 \le -\tfrac12 \iff 4m \le -\tfrac12 \iff m \le -\tfrac18 \iff \boxed{t \ge \tfrac18}✓✓ \ —— \ \textbf{解析}✓✓$$
$$\textbf{⑦ ⚠️⚠️ 关键发现：覆盖性未获证明，且很可能不成立}✗✗：\text{两处扫描端点差异}✓：C\text{-}380\text{-}33\ \text{给}\ 0.284253✓；\ C\text{-}380\text{-}35\ \text{给}\ 0.284250✓✓$$
$$\qquad \Longrightarrow \ \textbf{B 窗上限}\ \tfrac{1137}{4000} = 0.28425\ \text{与可行集上端（\approx 0.284253）之差}\ \textbf{仅}\ 3 \times 10^{-6}✗✗$$
$$\qquad \qquad \Longrightarrow \ \boxed{\textbf{「可行集} \subseteq \text{已认证窗口」}\ \textbf{未获证明}}✗✓，\ \textbf{且}\ \text{很可能}\ \textbf{不成立}✗✓（\textbf{若上端真实值}\ > \tfrac{1137}{4000}✓）$$
$$\qquad \qquad \Longrightarrow \ \textbf{须重新确定 B 窗上端的}\ \textbf{真实来源}✓✓ \ —— \ \text{不能沿用现有认证窗口}✗✓$$
$$\textbf{⑧ 因此本档未完成，Level 2 仍未 CLOSED}✗✓：\text{两个符号检查中}：\ \textbf{一个（B）与预期相反}✗✗；\ \textbf{另一个（C）不足以排除上带}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\text{义务 1 仍 OPEN}}✗✓；\ \boxed{\text{Level 2 仍 OPEN}}✗✓ \ —— \ \textbf{诚实登记}✓✓$$

## §1 核验记录（✓✓）

$$\textbf{B}✓：R_B(\tfrac{1137}{4000}) = \tfrac{182598168457}{500000000000000} \approx +0.000365✗✗（\textbf{精确}✓）；\ R_B(\tfrac18) = \tfrac{99}{16}✓✓；\ \text{根数}\ [\tfrac{1137}{4000}, 1] = 2✗✓$$
$$\textbf{C}✓：R_C(\tfrac{4489}{62500}) = \tfrac{25718619}{244140625} \approx +0.1053✓✓（\textbf{精确}✓）；\ \text{根} = \tfrac{7}{32} \mp \tfrac{\sqrt{22}}{32} \approx 0.072175,\ 0.365325✓✓$$
$$\textbf{上带}✓：\text{可行点}\ 0／20001✓✓（\textbf{数值}✗✓）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A／B／C 局部证书** ✓ | **CLOSED** ✓✓✓ |
| **层 A（组合穷尽）** ✓ | **CLOSED** ✓✓✓ |
| **层 B（窗口来源）** ✓ | **B 下端解析✓；B 上端来源未定✗；C 下端＋上带未闭合✗** ✗✓ |
| **义务 1（覆盖性）** ✓ | **OPEN —— 且很可能不成立（3e-6 差）** ✗✗ |
| Level 2 ✓ | **仍 OPEN** ✗✓ |
| `\inf Q_5` 全局 ✓ | **不追** ✗✓（\text{唐先生指示}✓） |
| Level 3 ✓ | **禁止启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗✓；\ \text{Level 2 CLOSED}✗✓；\ \text{义务 1 已完成}✗✓；\ R_B(\tfrac{1137}{4000}) < 0✗✗（\textbf{实为正}✓）$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{推翻} \text{提议的 B 支符号论证}✗✓；\ \textbf{发现覆盖性风险}✗✓；\ \text{上带排除为数值}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}追\ \inf Q_5\ \text{全局}✗✓；\ \textbf{不}启动 Level 3✗✓；\ \textbf{不}重做 Sturm✗✓；\ \textbf{不}把覆盖性风险写成已解决✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（精确有理 ＋ Sturm ＋ 20001 点，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 有理端点符号 命中文件数=0    ::
技术词 覆盖性反例  命中文件数=0    ::
技术词 上带排除     命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（精确有理符号 `R_B`／`R_C` ＋ `count_roots` ＋ 20001 点上带扫描 ✓）
