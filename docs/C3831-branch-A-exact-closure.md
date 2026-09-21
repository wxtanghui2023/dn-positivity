已查地图（**先查后写**）：`C-380-30`（**三分支结构 ＋ A 因式分解** ✓✓）、`C-380-29`（**切片解析** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-31：Branch A exact closure（注册＋逐步核验）**，**有计算（符号核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 变量替换}✓✓：t = -m > 0✓；\ \text{分支 A}：s = \tfrac{7}{16}✓ \Longrightarrow -(8m+1) = 8t - 1 \ge 0✓（t \ge \tfrac18✓） \Longrightarrow \ \textbf{只需证}\ P(-t) > 0✓✓$$
$$\textbf{② ⭐ 关键策略（采纳）}✓✓：\textbf{用}\ Q_3, Q_4\ \text{的}\ \textbf{容许性}✓✓，\ \textbf{而不是}硬证\ P > 0✗✓ \ —— \ \text{把}\ P\ \text{的变号区间}\ \textbf{排除掉}✓✓$$
$$\qquad \textbf{(a) } Q_3\ \text{给上界}✓✓：Q_3\big|_A = 9m - 32m^3 = 32t^3 - 9t✓✓（\textbf{核验一致}✓） \Longrightarrow 32t^3 - 9t + \tfrac12 \le 0✓✓$$
$$\qquad \qquad 32t^3 - 9t + \tfrac12 = \boxed{(t - \tfrac12)(32t^2 + 16t - 1)}✓✓（\textbf{核验 True}✓） \Longrightarrow \textbf{二次因子正根}\ -\tfrac14 + \tfrac{\sqrt6}{8} \approx 0.056186 < \tfrac18✓✓$$
$$\qquad \qquad \Longrightarrow \ \text{对}\ t \ge \tfrac18\ \text{该因子} > 0✓ \Longrightarrow \ \boxed{t \le \tfrac12}✓✓$$
$$\qquad \textbf{(b) } Q_4\ \text{给更强上界}✓✓：Q_4 + \tfrac12\big|_A = -\tfrac18 h(t)✓✓，\ \boxed{h(t) = 1024t^4 - 448t^2 + 27}✓✓（\textbf{核验一致}✓） \Longrightarrow Q_4 \le -\tfrac12 \iff h(t) \ge 0✓✓$$
$$\qquad \qquad h'(t) = \boxed{128t(32t^2 - 7)}✓✓（\text{与唐先生}\ t(4096t^2 - 896)\ \textbf{等价}✓）；\ \text{驻点}\ t^* = \sqrt{7/32} \approx 0.467707✓✓$$
$$\qquad \qquad \Longrightarrow h\ \text{在}\ [\tfrac{27}{100}, \tfrac12]\ \textbf{先降后升}✓ \Longrightarrow \textbf{最大值在端点}✓✓；\ \boxed{h(\tfrac{27}{100}) = -\tfrac{84861}{390625}}✓✓（\textbf{精确}✓），\ \boxed{h(\tfrac12) = -21}✓✓$$
$$\qquad \qquad \Longrightarrow h < 0\ \text{于整个}\ [\tfrac{27}{100}, \tfrac12]✓✓ \Longrightarrow \ \textbf{容许性强制}\ \boxed{t < \tfrac{27}{100}}✓✓$$
$$\qquad \qquad ⭐ \textbf{精度补注}✓✓：h\ \text{实根} \approx \pm 0.268653, \pm 0.604422✓ \Longrightarrow \textbf{精确容许上界}\ t_0 = 0.268653\dots✓✓（\textbf{略小于}\ \tfrac{27}{100}✓）$$
$$\qquad \qquad \qquad \Longrightarrow \ \textbf{唐先生的}\ \tfrac{27}{100}\ \text{为}\ \textbf{有效的保守界}✓✓；\ h(\tfrac18) = \tfrac{81}{4} > 0✓ \Longrightarrow \text{可行}\ t \in [\tfrac18, t_0]✓✓$$
$$\qquad \textbf{(c) } P\ \text{下界}✓✓：P(-t) > 341 - 2496\big(\tfrac{27}{100}\big)^2 - 312\big(\tfrac{27}{100}\big) = \boxed{\tfrac{46751}{625} \approx 74.80 > 0}✓✓（\textbf{精确}✓）$$
$$\qquad \qquad \Longrightarrow \ \boxed{P(-t) > 0}✓✓（\text{丢弃正项}\ 4096t^4 + 512t^3 > 0✓ \ \textbf{合法}✓✓）$$
$$\textbf{③ 结论}✓✓：\ \boxed{Q_5 - \tfrac{341}{128} = \frac{(8t-1)P(-t)}{128} \ge 0}✓✓（\textbf{符号形式核验通过}✓✓）$$
$$\qquad \textbf{等号} \iff 8t - 1 = 0 \iff t = \tfrac18 \iff m = -\tfrac18✓✓ \Longrightarrow \ \text{结合}\ s = \tfrac{7}{16}\ \text{得}\ \textbf{唯一等号点}✓✓$$
$$\qquad \Longrightarrow \ \boxed{(m, s) = (-\tfrac18, \tfrac{7}{16})}✓✓ \Longrightarrow \ \boxed{\textbf{Branch A CLOSED}}✓✓✓$$
$$\textbf{④ 纪律符合（逐条）}✓✓：\textbf{无}\ SOS／Gram✗✓；\textbf{无}\ Fourier\ \text{线性对偶}✗✓；\textbf{无}\ \text{数值根}✗✓；$$
$$\qquad \textbf{没有}把\ P\ \text{的全局正性}\ \textbf{硬做成假命题}✗✓；\ \textbf{真正使用}了\ Q_3, Q_4\ \text{的}\ \textbf{可行性}✓✓，\ \text{把}\ P\ \text{的变号区间排除}✓✓$$
$$\qquad \Longrightarrow \ \textbf{正是}\ C\text{-}380\text{-}30\ \text{所说的}「容许性 ＋ 单调／边界」路线✓✓$$
$$\textbf{⑤ 范围说明（诚实标注）}✓✓：\text{本证明的适用范围} = \ s = \tfrac{7}{16} \in \mathcal S_m\ \text{的情形}✓✓（\text{若该端点不容许则不在边界集中}✓）$$
$$\textbf{⑥ 账本}✓✓：\ \boxed{\text{Branch A: CLOSED}}✓✓；\ \boxed{\text{Branch B: OPEN}}✗✓；\ \boxed{\text{Branch C: OPEN}}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\text{Level 2 仍 OPEN}}✓✓，\ \text{但剩余问题已从「三个未控的二维边界」降成}\ \textbf{两个明确的一维代数分支}✓✓$$
$$\textbf{⑦ 下一步优先}✓✓：\textbf{Branch C 的}\ m = -\tfrac14\ \text{斜率变号点}✓✓ \ —— \ \text{很可能须把 C 分成}\ -\tfrac18 \ge m \ge -\tfrac14\ \text{与}\ m < -\tfrac14\ \text{两区间}✓✓，$$
$$\qquad \text{再分别利用}\ Q_2／Q_3\ \text{的容许性}✓✓；\ \text{其次}\ \textbf{Branch B}✓（s = A(m)✓，Q_3 = -\tfrac12✓）$$
$$\textbf{⑧ 贡献定性}✓✓：\textbf{实质性结构性收缩}✓✓ \ —— \ \text{从「三个未控二维边界」到「两个一维代数分支」}✓✓$$

## §1 核验记录（✓✓）

$$\textbf{核验 1}✓✓：Q_3\big|_A = -32m^3 + 9m✓ \Longrightarrow 32t^3 - 9t✓；\ \text{因式}\ (t - \tfrac12)(32t^2 + 16t - 1)✓ \ \textbf{一致 True}✓✓$$
$$\textbf{核验 2}✓✓：32t^2 + 16t - 1\ \text{根} = -\tfrac14 \pm \tfrac{\sqrt6}{8}✓；\ \text{正根} \approx 0.056186 < \tfrac18✓✓$$
$$\textbf{核验 3}✓✓：h(\tfrac{27}{100}) = -\tfrac{84861}{390625}✓ \ \textbf{精确 True}✓✓；\ h(\tfrac12) = -21✓；\ h(\tfrac18) = \tfrac{81}{4}✓✓$$
$$\textbf{核验 4}✓✓：h' = 128t(32t^2 - 7)✓；\ \text{驻点} \approx 0.467707✓；\ \text{实根} \approx \pm 0.268653, \pm 0.604422✓ \Longrightarrow t_0 = 0.268653✓✓$$
$$\textbf{核验 5}✓✓：P(-t)\ \text{下界} = \tfrac{46751}{625}✓ \ \textbf{精确 True}✓✓；\ Q_4 + \tfrac12\big|_A = -128t^4 + 56t^2 - \tfrac{27}{8} = -\tfrac18h✓✓$$
$$\textbf{核验 6}✓✓：Q_5(m, \tfrac{7}{16}) - \tfrac{341}{128} = \frac{(8t-1)(4096t^4 + 512t^3 - 2496t^2 - 312t + 341)}{128}✓✓；\ Q_5(-\tfrac18, \tfrac{7}{16}) = \tfrac{341}{128}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}30` ✓ | **三分支结构** ✓✓ |
| **Branch A** ✓ | **本档：CLOSED（解析）** ✓✓✓ |
| Branch B ✓ | **OPEN** ✗✓ |
| Branch C ✓ | **OPEN（`m = -\tfrac14` 变号点优先）** ✗✓ |
| Level 2 ✓ | **仍 OPEN（剩两个一维分支）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **未解析证明** ✗✓ |
| Level 3 ✓ | **尚未启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓（\textbf{仅 A 支}✓）；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{Branch A}\ \textbf{解析 CLOSED}✓✓；\ B／C\ \textbf{仍 OPEN}✗✓；\ \text{精度补注}\ t_0 < \tfrac{27}{100}✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}做\ B／C✗（\text{本档只封 A}✓）；\textbf{不}上\ SOS／Gram✗；\textbf{不}把\ P\ \text{全局正性硬做假命题}✗✓；\textbf{不}从「边界被杀」跳到「完整模型被杀」✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy 核验，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 分支精确闭合 命中文件数=0    :: 
技术词 容许性排除  命中文件数=0    :: 
技术词 保守界        命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 六项核验：因式／根／`h` 值／`P` 下界／符号形式 ✓）
