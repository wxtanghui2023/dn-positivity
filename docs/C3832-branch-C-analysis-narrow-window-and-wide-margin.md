已查地图（**先查后写**）：`C-380-31`（**Branch A CLOSED** ✓✓）、`C-380-30`（**三分支结构** ✓✓）、`C-380-29`（**凸性顶点** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-32：Branch C 分析（容许窗口 ＋ 余量）（注册）**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① C 支两根（精确）}✓✓：Q_4 = -\tfrac12 \Longrightarrow 8s^2 + (32m^2 - 8)s - 32m^4 + \tfrac98 = 0✓✓$$
$$\qquad \text{判别式} = \boxed{4(512m^4 - 128m^2 + 7)}✓✓ \Longrightarrow \boxed{s_{\pm}(m) = \tfrac12 - 2m^2 \pm \tfrac{\sqrt{512m^4 - 128m^2 + 7}}{8}}✓✓$$
$$\textbf{② ⭐ 等号点不在 C 支上}✓✓：F_{\pm}(-\tfrac18) = -\tfrac{435}{128} \mp \tfrac{15\sqrt{82}}{64} \ne 0✓✓ \Longrightarrow s = \tfrac{7}{16}\ \textbf{不属于}\ \text{C 支}✓✓$$
$$\qquad \text{与}\ Q_4(-\tfrac18) = -\tfrac{97}{32} \ll -\tfrac12✓✓\ \text{一致}✓ \Longrightarrow \ \textbf{唯一等号点在 A 支}✓✓$$
$$\textbf{③ ⭐⭐ C 支容许窗口（本档核心）}✓✓：\text{要求}\ s \in [\max(m^2, A(m)), \tfrac{7}{16}]✓ \ \text{且}\ Q_2, Q_3, Q_4 \le -\tfrac12✓✓$$
$$\qquad \Longrightarrow \ \boxed{m \in [-0.2842, -0.2687]}✓✓（\textbf{宽}\ \approx 0.0155✓，\textbf{极窄}✓✓）$$
$$\qquad \Longrightarrow \ \boxed{\min_{\text{C 支}}Q_5 = +3.6388}✓✓（\text{at}\ (m, s) = (-0.2687, 0.4372)✓） \ —— \ \text{比}\ \tfrac{341}{128} = 2.664\ \textbf{高}\ 0.9748✓✓$$
$$\qquad \Longrightarrow \ \textbf{C 支}\ \textbf{舒适地高于} \text{目标}✓✓ \ —— \ \textbf{余量宽阔}✓✓，\ \textbf{不是}临界情形✗✓$$
$$\textbf{④ 斜率结构（厘清）}✓✓：\boxed{\frac{\partial Q_5}{\partial s} = 80m(8s - 3)}✓✓，\ \textbf{零点}\ \boxed{s = \tfrac38}✓✓ \ —— \ \textbf{正是}\ B\ \text{的顶点}✓✓（\text{与}\ C\text{-}380\text{-}29\ \text{一致}✓）$$
$$\qquad \Longrightarrow \ \text{沿 C 支（s 由 m 决定}✓）\ \text{的增减性由}\ \textbf{s vs}\ \tfrac38\ \text{决定}✓✓$$
$$\textbf{⑤ 勘误级注记}✗✓：C\text{-}380\text{-}30\ \text{所述「斜率变号点}\ m = -\tfrac14」✓ \ —— \ \text{那是}\ \textbf{消元后的形式偏导}✓✓（\partial_sQ_5\big|_C = -80m(16m^2 - 1)✓）$$
$$\qquad \textbf{真正有意义的是}\ \text{沿 C 的}\ \tfrac{dQ_5}{dm}✗✓ \ —— \ \text{本档已厘清}✓✓，\ \textbf{不影响}\ C\text{-}380\text{-}30\ \text{的三分支结构结论}✓$$
$$\textbf{⑥ 战略评估}✓✓：C 支容许窗口\ \textbf{只有}\ 0.0155\ \text{宽}✓✓ \Longrightarrow \ \textbf{解析闭合看起来可行}✓✓（\text{在窄窗口上用单调性}✓）$$
$$\qquad \textbf{但}✗✓：\text{本档}\ \textbf{仅给数值证据}✓（\min = 3.6388✓），\ \textbf{未}写解析闭合✗✓$$
$$\textbf{⑦ 账本}✓✓：\text{见 §2}✓$$
$$\textbf{⑧ 纪律}✓✓：\textbf{仍不启动 Level 3}✗✓；\ \boxed{\text{two-level closure} \not\Rightarrow \mathcal F_0 = \varnothing}✓✓ \ —— \ \textbf{边界保持不变}✓✓$$

## §1 数值记录（✓✓）

$$\textbf{C 支容许点}✓：72✓（扫 4001 个 m✓）；\ \textbf{容许 m 范围} = [-0.2842, -0.2687]✓✓$$
$$\textbf{min}Q_5 = +3.63882094✓✓ \ \text{at}\ (m, s) = (-0.268719, 0.437247)✓；\ \text{与}\ \tfrac{341}{128}\ \text{差} = +9.748 \times 10^{-1}✓✓$$
$$\textbf{纯 m 形式}✓：F_{\pm}(m) = 3584m^5 - 640m^3 + 15m - \tfrac{341}{128} \pm \tfrac{\sqrt{512m^4 - 128m^2 + 7}}{8}(160m^3 - 10m)✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A** ✓ | **CLOSED（解析）** ✓✓✓ |
| **Branch B** ✓ | **OPEN（第二顺位）** ✗✓ |
| **Branch C** ✓ | **本档：容许窗口 `[-0.2842,-0.2687]`；`min Q_5 = 3.6388 \gg \tfrac{341}{128}`（数值）** ✓✓ |
| Level 2 ✓ | **仍 OPEN（剩 B ＋ C 解析闭合）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **未解析证明** ✗✓ |
| Level 3 ✓ | **尚未启动（纪律保持）** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓；\ \text{Branch C CLOSED}✗✓（\textbf{数值}✓）；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{等号点不在 C 支}\ \textbf{已解析确认}✓✓；\ \text{C 支为}\ \textbf{数值}✓；\ \text{形式偏导勘误已厘清}✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}启动 Level 3✗✓；\textbf{不}上\ SOS／Gram✗；\textbf{不}把\ C\ \text{支数值当解析闭合}✗✓；\textbf{不}从「边界被杀」跳到「完整模型被杀」✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy ＋ 4001 点扫描，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓（\textbf{注记另记}✓）；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 分支容许窗口 命中文件数=0    :: 
技术词 沿支导数     命中文件数=0    :: 
技术词 余量宽阔     命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 判別式／两根／F± ＋ 4001 点容许扫描 ✓）
