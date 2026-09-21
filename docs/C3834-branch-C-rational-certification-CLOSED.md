已查地图（**先查后写**）：`C-380-33`（**有理窗口 ＋ 路线** ✓✓）、`C-380-31`（**Branch A CLOSED** ✓✓）、`C-380-13`（**Fourier-dual CLOSED** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-34：Branch C 有理认证（封口）（注册）**，**有计算（精确有理 `Fraction` 认证，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 窗口（有理）}✓✓：u = m^2 \in \Big[\tfrac{4489}{62500},\ \tfrac{101}{1250}\Big]✓✓（0.071824 \sim 0.0808✓）；\ |m| \in \Big[\tfrac{67}{250},\ \tfrac{569}{2000}\Big]✓✓（0.268 \sim 0.2845✓）$$
$$\qquad c(m) = -64u^2 + 40u + 5✓ \ —— \ \text{顶点}\ u = \tfrac{5}{16} = 0.3125\ \textbf{在窗口外}✓ \Longrightarrow c\ \text{在窗口上}\ \textbf{递增}✓✓$$
$$\qquad \Longrightarrow \ c(m) \in \Big[\tfrac{1841504891}{244140625},\ \tfrac{3052409}{390625}\Big]✓✓（7.542804 \sim 7.814167✓，\textbf{精确}✓）$$
$$\textbf{② 三个有理不等式（逐项精确认证）}✓✓：$$
$$\qquad \textbf{【1】}✓✓：\boxed{|m| \ge \tfrac{67}{250} = 0.268}✓✓$$
$$\qquad \textbf{【2】}✓✓：B(\tfrac{7}{16}) = c(m) - \tfrac{175}{16} \le c_{\mathrm{hi}} - \tfrac{175}{16} = \boxed{-\tfrac{19520831}{6250000} = -3.123333}✓✓ \ \Longrightarrow \ \le -\tfrac{29}{10}✓✓（\text{余量}\ 0.223✓）$$
$$\qquad \textbf{【3】}✓✓：A(|m|) \in \Big[\tfrac{16921729}{50250000},\ \tfrac{1162720009}{3414000000}\Big]✓✓（0.336751 \sim 0.340574✓，\text{驻点}\ 2^{2/3}/8 \approx 0.1984\ \textbf{在窗口外}✓）$$
$$\qquad \qquad \Longrightarrow \ s_{\mathrm{lo}} = \max(m^2, A) = A✓（\text{因}\ A \approx 0.34 > m^2 \approx 0.08✓）；\ \text{s 部分}\ 80s^2 - 60s\ \textbf{在}\ s < \tfrac38\ \text{上递减}✓✓$$
$$\qquad \qquad \Longrightarrow \ B(s_{\mathrm{lo}}) \le 80A_{\mathrm{lo}}^2 - 60A_{\mathrm{lo}} + c_{\mathrm{hi}} = \boxed{-\tfrac{104751997320059}{31563281250000} = -3.318793}✓✓ \ \Longrightarrow \ \le -\tfrac{29}{10}✓✓（\text{余量}\ 0.419✓）$$
$$\textbf{③ 统一负界}✓✓：\max\big(B(\tfrac{7}{16}), B(s_{\mathrm{lo}})\big) \le \boxed{-\tfrac{19520831}{6250000} = -3.123333}✓✓ \ \Longrightarrow \ B \le -3.123333✓✓（\textbf{亦满足}\ \le -3✓ \le -\tfrac{29}{10}✓）$$
$$\textbf{④ ⭐ 结论（封口）}✓✓：Q_5 = 4m \cdot B(s) = 4|m| \cdot (-B) \ge 4 \cdot \tfrac{67}{250} \cdot 3.123333 = \boxed{\tfrac{1307895677}{390625000} = 3.348213}✓✓$$
$$\qquad \Longrightarrow \ \boxed{Q_5 > 3 > \tfrac{341}{128}}✓✓（\text{对}\ 3\ \text{余量}\ 0.348✓；\text{对}\ \tfrac{341}{128}\ \text{余量}\ 0.684✓✓）$$
$$\qquad \Longrightarrow \ \boxed{\textbf{Branch C CLOSED}}✓✓✓ \ —— \ \text{等号点自动排除}✓✓（\text{因}\ Q_5 > 3 \gg \tfrac{341}{128}✓）$$
$$\textbf{⑤ 凸性端点引用的前提（已核）}✓✓：\text{逻辑成立的前提是}\ s\ \text{确实被限制在}\ [s_{\mathrm{lo}}, \tfrac{7}{16}]✓✓ \ —— \ \text{而凸函数在闭区间上的}\ \textbf{最大值确实在端点取得}✓✓$$
$$\qquad \Longrightarrow \ \textbf{不需}重新研究\ s_+(m)\ \text{的导数}✗✓，\ \textbf{不需}处理\ s_+'(m)✗✓ \ —— \ \textbf{这是目前最干净的路线}✓✓$$
$$\textbf{⑥ ⚠️ 诚实标注（残余小缺口）}✗✓：\textbf{「可行性} \Longrightarrow m\ \text{在窗口内」这一步}\ \textbf{依赖}\ \text{数值扫描} ＋ \text{有理包络}✓✓（C\text{-}380\text{-}33\ 33A✓）$$
$$\qquad \textbf{完全严格的版本} \text{需}\ \textbf{代数地导出} \text{容许}\ m\text{-范围}✗✓ \ —— \ \textbf{登记为残余小缺口}✓✓，\ \textbf{不影响} \text{本档三不等式的严格性}✓✓$$
$$\textbf{⑦ 账本}✓✓：\text{见 §2}✓$$
$$\textbf{⑧ 纪律}✓✓：\textbf{C 不再扩展}✗✓ \Longrightarrow \ \textbf{下一档直接 Branch B}✓✓；\ \textbf{Level 3 禁止启动}✗✓；\ \boxed{\text{two-level closure} \not\Rightarrow \mathcal F_0 = \varnothing}✓✓$$

## §1 认证记录（✓✓，全部精确有理）

$$\textbf{c 界}✓✓：c_{\mathrm{lo}} = \tfrac{1841504891}{244140625} = 7.542804✓；\ c_{\mathrm{hi}} = \tfrac{3052409}{390625} = 7.814167✓✓$$
$$\textbf{A 界}✓✓：A_{\mathrm{lo}} = \tfrac{16921729}{50250000} = 0.336751✓；\ A_{\mathrm{hi}} = \tfrac{1162720009}{3414000000} = 0.340574✓✓$$
$$\textbf{【2】}✓✓：B(\tfrac{7}{16}) \le -\tfrac{19520831}{6250000}✓✓（\textbf{精确}✓）；\textbf{【3】}✓✓：B(s_{\mathrm{lo}}) \le -\tfrac{104751997320059}{31563281250000}✓✓$$\
$$\textbf{Q_5 下界}✓✓：\tfrac{1307895677}{390625000} = 3.348213✓✓ \ —— \ \textbf{对}\ 3\ \text{余量}\ 0.348213✓；\ \text{对}\ \tfrac{341}{128}\ \text{余量}\ 0.684150✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A** ✓ | **CLOSED（解析）** ✓✓✓ |
| **Branch C** ✓ | **本档：CLOSED（精确有理认证）** ✓✓✓ |
| **Branch B** ✓ | **OPEN —— 唯一剩余分支** ✗✓ |
| Level 2 ✓ | **OPEN（仅剩 B）** ✗✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **尚未完成全局解析证明** ✗✓ |
| Level 3 ✓ | **禁止启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓（\textbf{剩 B}✓）；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓；\ \text{Bridge A 已闭合}✗✓；\ \text{窗口容纳性已完全严格}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{三个不等式}\ \textbf{精确有理}✓✓；\ \text{窗口容纳性}\ \textbf{依赖扫描}✗✓（\textbf{残余小缺口}✓）；\ \text{Branch C 封口}\ \textbf{在给定窗口下成立}✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不}碰 Branch B✗✓（\textbf{下一档}✓）；\textbf{不}启动 Level 3✗✓；\textbf{不}优化常数✗✓（\textbf{目标}\ > 3\ \text{足够}✓）；\textbf{不}把\ 3.348\ \text{当最优}✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（精确有理认证，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 逐项有理认证 命中文件数=0    ::
技术词 统一负界     命中文件数=0    ::
技术词 端点凸性     命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（`Fraction` 精确认证：窗口／`c` 界／`A` 界／两处 `B` 界／统一界／`Q_5` 下界 ✓）
