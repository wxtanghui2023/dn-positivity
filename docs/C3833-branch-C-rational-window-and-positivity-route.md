已查地图（**先查后写**）：`C-380-32`（**C 支窗口 ＋ 余量** ✓✓）、`C-380-31`（**Branch A CLOSED** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-33：Branch C 有理窗口 ＋ 严格正性路线（注册）**，**有计算（符号 ＋ 数值，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 33A 有理窗口（已严格）}✓✓：\text{可行 C 支点数}\ 6240✓；\ \text{数值}\ \boxed{m \in [-0.284253, -0.268655]}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{有理包络窗口}\ m \in [-0.2845, -0.2680]}✓✓ \ \text{覆盖全部可行点}✓✓（\textbf{核验 True}✓）$$
$$\qquad \qquad \textbf{更紧的纯有理界}✓✓：\boxed{m^2 \in \Big[\tfrac{4489}{62500},\ \tfrac{101}{1250}\Big]}✓✓（\approx 0.071824 \sim 0.0808✓，\ \textbf{全有理}✓✓）$$
$$\textbf{② ⭐ 判别式严格正（精确有理）}✓✓：D = 512m^4 - 128m^2 + 7✓ \ —— \ \text{令}\ u = m^2✓，\ D(u) = 512u^2 - 128u + 7✓ \ \textbf{在}\ u \le \tfrac18\ \text{上递减}✓✓$$
$$\qquad \Longrightarrow \ \text{窗口上}\ D\ \text{最小值在右端}✓✓：\boxed{D\big(\tfrac{101}{1250}\big) = \tfrac{103}{390625} > 0}✓✓（\textbf{精确}✓）；\ D\big(\tfrac{4489}{62500}\big) = \tfrac{109320247}{244140625}✓✓$$
$$\qquad \Longrightarrow \ \boxed{D > 0\ \text{全程严格}}✓✓ \Longrightarrow \ \text{C 支在整个窗口上}\ \textbf{良定}✓✓$$
$$\textbf{③ 相关支}✓✓：\text{全部可行点落在}\ \boxed{s_+}\✓（s > \tfrac12 - 2m^2✓，\ \text{占比}\ 1.0✓✓） \Longrightarrow \ \text{只需研究}\ s_+(m)✓✓$$
$$\textbf{④ 33B 消元（已严格）}✓✓：\text{用}\ Q_4 = -\tfrac12\ \text{消}\ s^2✓✓：\boxed{s^2 = 4m^4 - 4m^2s + s - \tfrac{9}{64}}✓✓$$
$$\qquad \Longrightarrow \ \boxed{R\big|_C := Q_5\big|_C - \tfrac{341}{128} = -\frac{-131072m^5 + 163840m^3s - 20480m^3 - 10240ms + 3200m + 341}{128}}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{关于}\ s\ \textbf{线性}✓✓（\text{形式斜率}\ -80m(16m^2 - 1)✓）
$$
$$\textbf{⑤ 33C 余量（数值）}✓✓：\boxed{\min Q_5 = +3.6365}✓✓（\text{at}\ m = -0.2687✓） \ —— \ \boxed{\ge 3\ \text{余量} +0.636}✓✓；\ \boxed{-\tfrac{341}{128} = +0.972}✓✓$$
$$\textbf{⑥ ⭐ 33C 严格化路线（本档建立）}✓✓：Q_5 = 4m \cdot B(s)✓，\ B(s) = 80s^2 - 60s + c(m)✓，\ c(m) = -64m^4 + 40m^2 + 5✓✓$$
$$\qquad \textbf{关键不等式}✓✓：\text{因}\ B\ \textbf{凸}（\text{顶点}\ \tfrac38✓）⟹ \boxed{B(s) \le \max\big(B(s_{\mathrm{lo}}),\ B(\tfrac{7}{16})\big)}✓✓（\text{其中}\ s_{\mathrm{lo}} = \max(m^2, A(m))✓）$$
$$\qquad \textbf{有理界（窗口上）}✓✓：c(m) \in [7.454, 7.902]✓；\ \boxed{B(\tfrac{7}{16}) \in [-3.48, -3.03]}✓✓；\ \boxed{B(s_{\mathrm{lo}}) \in [-3.70, -3.23]}✓✓$$
$$\qquad \qquad \Longrightarrow \ B \le -3.03✓✓ \Longrightarrow Q_5 = 4|m|\cdot(-B) \ge 4(0.2686)(2.792) \approx \boxed{2.999}✓✓$$
$$\qquad \qquad \Longrightarrow \ \boxed{2.999 > \tfrac{341}{128} = 2.664}✓✓（\textbf{充足余量}✓✓） \Longrightarrow \ \textbf{解析路线可行}✓✓$$
$$\textbf{⑦ 诚实状态}✗✓：\textbf{33A 已严格}✓✓；\ \textbf{33B 已严格}✓✓；\ \textbf{33C 路线已建立}✓，\ \textbf{逐项有理区间认证未完成}✗✓$$
$$\qquad \Longrightarrow \ \boxed{\textbf{Branch C 尚未 CLOSED}}✗✓（\text{与唐先生一致}✓：\text{不把数值当闭合}✓✓）$$
$$\textbf{⑧ 账本}✓✓：\text{见 §2}✓$$

## §1 数值记录（✓✓）

$$\textbf{33A}✓：\text{扫}\ 20001\ \text{个}\ m \in [-0.30, -0.25]✓；\ \text{可行}\ 6240✓；\ m \in [-0.284253, -0.268655]✓✓；\ m^2 \in [0.072176, 0.080799]✓✓$$
$$\textbf{33C}✓：\min Q_5 = +3.63645695✓✓ \ \text{at}\ m = -0.268655✓；\ \text{余量（对}\ 3） = +0.636457✓；\ \text{（对}\ \tfrac{341}{128}）= +0.972394✓✓$$
$$\textbf{窗口端点 R 值}✓（s_- 支对照）：m = -0.276 \Longrightarrow Q_5 = +3.2921✓；\ m = -0.2687 \Longrightarrow Q_5 = +3.0929✓；\ m = -0.268 \Longrightarrow Q_5 = +3.0767✓✓$$
$$\qquad \textbf{注}✓：\text{可行点为}\ s_+\ \text{支}✓；\ \text{上表为}\ s_-\ \text{支对照}✓，\ \textbf{两支}\ Q_5 > 3✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A** ✓ | **CLOSED（解析）** ✓✓✓ |
| **Branch B** ✓ | **OPEN（第二顺位）** ✗✓ |
| **Branch C：窗口** ✓ | **本档：严格（有理）** ✓✓ |
| **Branch C：`D > 0`** ✓ | **本档：严格（精确有理）** ✓✓ |
| **Branch C：消元** ✓ | **本档：严格（线性化）** ✓✓ |
| **Branch C：正性** ✓ | **路线建立；逐项认证未完成** ✗✓ |
| Level 2 ✓ | **仍 OPEN（剩 B ＋ C 正性）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **未解析证明** ✗✓ |
| Level 3 ✓ | **尚未启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓；\ \textbf{Branch C CLOSED}✗✓（\textbf{尚未}✓）；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{窗口／判别式／消元为}\ \textbf{严格}✓✓；\ \text{正性为}\ \textbf{路线＋数值}✓；\ \textbf{不}把\ 3.6365\ \text{当闭合}✗✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}碰 Branch B✗✓；\textbf{不}启动 Level 3✗✓；\textbf{不}上\ SOS／Gram✗；\textbf{不}为优化常数\ 3.6388\ \text{而深挖}✗✓（\textbf{目标}\ > \tfrac{341}{128}\ \text{足够}✓✓）$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy ＋ 20001 点扫描，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 有理窗口     命中文件数=0    :: 
技术词 判别式严格正 命中文件数=0    :: 
技术词 端点凸界     命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（sympy 消元 ＋ 20001 点扫描 ＋ 有理判别式核算 ✓）
