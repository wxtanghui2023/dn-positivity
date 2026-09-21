已查地图（**先查后写**）：`C-380-36`（**Branch B CLOSED** ✓✓）、`C-380-34`（**Branch C CLOSED** ✓✓）、`C-380-30`（**端点原则** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-37：Endpoint-Decomposition Completeness Audit（注册＋审计）**，**有计算（解析 ＋ 验证扫描，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 两项义务（采纳唐先生）}✓✓：\textbf{义务 1}✓：\text{B／C 窗口来源}✓（\text{严格推出所有 B／C 候选落入已认证窗口}✓✓）；\ \textbf{义务 2}✓：\text{端点完备性}✓✓$$
$$\qquad \Longrightarrow \ \text{把}「\text{三支都正}」\ \textbf{提升为}\ \mathcal F_0 = \varnothing\ \text{所必需的}\ \textbf{结构性桥梁}✓✓$$
$$\textbf{② ⭐ } \mathcal S_m\ \text{的区间结构（已建立）}✓✓：\text{四条约束}\ \textbf{全部是区间条件}✓✓：$$
$$\qquad Q_2 \le -\tfrac12 \iff \boxed{s \le \tfrac{7}{16}}✓（\text{上界，常数}✓）；\ Q_3 \le -\tfrac12 \iff \boxed{s \ge A(m)}✓（\text{下界；系数}\ 48m < 0\ \text{翻转}✓✓）$$
$$\qquad Q_4 \le -\tfrac12 \iff \boxed{s \in [s_-(m),\ s_+(m)]}✓✓（\text{上开二次}✓）；\ \boxed{s \ge m^2}✓（a^2 \ge 0✓）$$
$$\qquad \Longrightarrow \ \boxed{\mathcal S_m = \big[\max(m^2, A, s_-),\ \min(\tfrac{7}{16}, s_+)\big]}✓✓ \Longrightarrow \ \textbf{至多两个端点}✓✓ \Longrightarrow \ \textbf{端点原则的前提成立}✓✓$$
$$\textbf{③ ⭐⭐ 本档关键发现（端点候选清单实为 5 类）}✗✓：\boxed{\text{候选清单} = \{\tfrac{7}{16},\ A(m),\ s_{\pm}(m),\ m^2\}}✓✓（\textbf{共 5 类}✓✓）$$
$$\qquad \Longrightarrow \ \textbf{A／B／C 只覆盖 4 类}✗✓ \Longrightarrow \ \boxed{\text{第 5 类}\ s = m^2\ \text{（即}\ a = 0\text{）须单独审计}}✓✓$$
$$\qquad \qquad ⭐ \textbf{这是本档的核心审计价值}✓✓：\text{若漏检，}\ \textbf{端点完备性会出现结构化空洞}✗✓$$
$$\textbf{④ ⭐⭐⭐ 第 5 类为空（解析证明）}✓✓✓：s = m^2 \iff a = 0 \iff \text{四点重合}\ X_j \equiv m✓✓（two-level 的退化边）$$
$$\qquad \text{代入}\ (m = -t,\ s = t^2)✓：Q_2 = 4(2t^2 - 1)✓；\ Q_3 = -4t(4t^2 - 3)✓；\ Q_4 = 4(8t^4 - 8t^2 + 1)✓✓$$
$$\qquad \text{约束}✓✓：Q_2 \le -\tfrac12 \Longrightarrow t^2 \le \tfrac{7}{16}✓；\ Q_4 \le -\tfrac12 \Longrightarrow \boxed{64t^4 - 64t^2 + 9 \le 0}✓ \Longrightarrow t^2 \in \big[\tfrac12 - \tfrac{\sqrt7}{8},\ \tfrac12 + \tfrac{\sqrt7}{8}\big]✓✓$$
$$\qquad \qquad \Longrightarrow \ t^2 \in \big[\tfrac12 - \tfrac{\sqrt7}{8},\ \tfrac{7}{16}\big] = [0.1693,\ 0.4375]✓✓ \Longrightarrow \ t \in [0.4114,\ 0.6614]✓✓$$
$$\qquad \qquad \Longrightarrow \ \text{该区间上}\ 4t^2 - 3 \in [-2.32,\ -1.25] < 0✓✓ \Longrightarrow \ Q_3 = -4t(4t^2 - 3) = 4t(3 - 4t^2) > 0✓✓$$
$$\qquad \qquad \Longrightarrow \ \boxed{Q_3 > 0 > -\tfrac12}✗✗ \Longrightarrow \ \textbf{第 5 类}\ \textbf{不可行}✓✓✓ \ —— \ \textbf{解析证明}✓✓，\ \textbf{非扫描}✗✓$$
$$\qquad \qquad \textbf{验证扫描}✓✓：200001\ \text{个}\ m\ \text{上可行点数} = 0✓✓ \ —— \ \textbf{与解析一致}✓✓$$
$$\textbf{⑤ 义务 2 的结论（模组合情形）}✓✓：\text{在一个}\ \textbf{非空} \mathcal S_m\ \text{上}\ \partial\mathcal S_m \subseteq \{\tfrac{7}{16},\ A,\ s_{\pm}\}✓✓ \Longrightarrow \ \textbf{A／B／C 穷尽可行端点}✓✓$$
$$\qquad ⚠️ \textbf{剩余细节}✗✓：\partial\mathcal S_m\ \text{是}\ \max／\min\ \text{的}\ \textbf{组合}✓✓ ⟹ \text{分支分解仍须处理「哪个约束活跃」的组合情形}✓✓（\textbf{登记}✓）$$
$$\textbf{⑥ ⚠️ 义务 1（B／C 窗口来源）仍未证}✗✓：\textbf{本档只解决义务 2}✓✓ \ —— \ \text{义务 1}\ \textbf{保持 OPEN}✗✓$$
$$\qquad \text{即}\ \text{B 支（窗口}\ [\tfrac18, \tfrac{1137}{4000}]✓）\ \text{与}\ \text{C 支（窗口}\ m^2 \in [\tfrac{4489}{62500}, \tfrac{101}{1250}]✓）\ \text{的}\ \textbf{覆盖性}✓✓\ \text{仍须严格推出}✗✓$$
$$\textbf{⑦ 账本}✓✓：\text{见 §2}✓$$
$$\textbf{⑧ 纪律}✓✓：\textbf{不}启动 Level 3✗✓；\textbf{不}加强 B／C 数值证书✗✓（\text{唐先生指示}✓）；\ \boxed{\text{two-level closure} \not\Rightarrow \mathcal F_0 = \varnothing}✓✓\ \text{仍保持}✓$$

## §1 审计记录（✓✓）

$$\textbf{区间结构}✓✓：\text{四约束皆区间}✓ \Longrightarrow \mathcal S_m\ \text{至多两端点}✓✓；\ \text{候选}\ 5\ \text{类}✓✓$$
$$\textbf{第 5 类}✓✓✓：t^2 \in [0.1693, 0.4375]✓ \Longrightarrow t \in [0.4114, 0.6614]✓ \Longrightarrow Q_3 = 4t(3 - 4t^2) > 0✓✓ \Longrightarrow \textbf{不可行}✓✓$$
$$\qquad \qquad \textbf{扫描核验}✓：200001\ \text{点} \Longrightarrow \text{可行}\ 0✓✓；\ \text{与解析一致}✓✓$$
$$\textbf{Q_4 层精确解}✓✓：64t^4 - 64t^2 + 9 = 0 \Longrightarrow t^2 = \tfrac12 \pm \tfrac{\sqrt7}{8}✓✓（0.1693,\ 0.8307✓）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A／B／C** ✓ | **皆 CLOSED** ✓✓✓ |
| **义务 2（端点完备性）** ✓ | **本档：成立（模活跃约束组合细节）** ✓✓ |
| **第 5 类 `s = m^2`** ✓ | **本档：解析为空** ✓✓✓ |
| **义务 1（B／C 窗口来源）** ✓ | **OPEN —— 唯一剩余义务** ✗✓ |
| Level 2 ✓ | **OPEN（仅剩义务 1 ＋ 组合细节）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **尚未完成全局解析证明** ✗✓ |
| Level 3 ✓ | **禁止启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓；\ \text{义务 1 已完成}✗✓；\ \text{端点完备性已完全无缺}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{新增}\ \text{第 5 类审计}✓✓（\textbf{核心价值}✓）；\ \text{义务 1}\ \textbf{仍未解}✗✓；\ \text{组合细节}\ \textbf{未处理}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}启动 Level 3✗✓；\textbf{不}加强 B／C 数值证书✗✓；\textbf{不}碰 Level 3 相关✗✓；\textbf{不}把义务 2 当义务 1✗✓$$
$$\textbf{不}把\ \text{三支皆正} \text{直接写成}\ \mathcal F_0 = \varnothing✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（解析 ＋ 200001 点验证扫描，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 端点分解完备性 命中文件数=0    ::
技术词 第五候选类  命中文件数=0    ::
技术词 窗口来源义务 命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（sympy 层解析 `Q_k(-t,t^2)` ＋ 200001 点可行性扫描 ✓）
