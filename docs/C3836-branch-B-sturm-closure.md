已查地图（**先查后写**）：`C-380-35`（**B 支线性化 ＋ 单点待补** ✓✓）、`C-380-34`（**Branch C CLOSED** ✓✓）、`C-380-30`（**端点原则** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-36：B-Branch Sturm Closure（注册＋核验）**，**有计算（精确 Sturm／有理核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 精确窗口（固定）}✓✓：\boxed{I_B = \Big[\tfrac18,\ \tfrac{1137}{4000}\Big] = [0.125,\ 0.28425]}✓✓ \ —— \ \text{由}\ C\text{-}380\text{-}35\ \text{的 B 支可行窗口}✓✓$$
$$\textbf{② 导数与端点符号（精确核验）}✓✓：\boxed{P_B'(t) = 786432t^5 - 491520t^3 - 15360t^2 + 46080t - 2109}✓✓$$
$$\qquad \boxed{P_B'\big(\tfrac18\big) = 2475 > 0}✓✓（\textbf{精确 True}✓）；\ \boxed{P_B'\big(\tfrac{1137}{4000}\big) = -\tfrac{316876084411629}{3906250000000} \approx -81.12 < 0}✓✓（\textbf{精确 True}✓）$$
$$\textbf{③ ⭐ Sturm 计数（核心）}✓✓：\boxed{\#\{t \in I_B : P_B'(t) = 0\} = 1}✓✓（\text{Sturm chain 长度}\ 6✓；\ \texttt{count\_roots} = 1✓✓）$$
$$\qquad \Longrightarrow \ \text{由 Sturm 定理，区间内}\ \textbf{恰有一个零点}✓✓ \ —— \ \textbf{封口的关键}✓✓$$
$$\qquad \Longrightarrow \ \text{配合端点符号}\ + \to -✓✓ \Longrightarrow \ \text{唯一临界点}\ \textbf{是极大值点}✓✓$$
$$\textbf{④ 端点值（精确）}✓✓：\boxed{P_B\big(\tfrac18\big) = \tfrac{135}{8} = 16.875 > 0}✓✓（\textbf{精确 True}✓）$$
$$\qquad \boxed{P_B\big(\tfrac{1137}{4000}\big) = \tfrac{11607824617202992609}{31250000000000000} \approx 371.45 > 0}✓✓$$
$$\textbf{⑤ ⭐ 封口推论}✓✓：P_B\ \text{在窗口内}\ \textbf{升后降}✓✓ \Longrightarrow \ \text{最小值只在}\ \textbf{两个端点}✓✓ \Longrightarrow \ \boxed{P_B(t) \ge \tfrac{135}{8} > 0}✓✓$$
$$\qquad \Longrightarrow \ Q_5 - \tfrac{341}{128} = \frac{P_B(t)}{1152t}✓✓（\text{分母}\ 1152t > 0✓） \Longrightarrow \ \boxed{Q_5 > \tfrac{341}{128}\ \text{on the entire B window}}✓✓$$
$$\qquad \textbf{精确余量}✓✓：\text{临界端点}\ t = \tfrac18\ \text{给}\ Q_5 = \tfrac{89}{32} = \tfrac{356}{128} = \tfrac{341}{128} + \boxed{\tfrac{15}{128}}✓✓；\ \text{另一端}\ Q_5 \approx 3.7984✓✓$$
$$\textbf{⑥ 辅助值（不入正式证明）}✓✓：\text{唯一内部根}\ t_* \approx 0.2827950224✓✓ \ —— \ \textbf{仅参照}✗✓，\ \textbf{不需}进入正式证明✓✓$$
$$\textbf{⑦ } \boxed{\textbf{Branch B CLOSED}}✓✓（\textbf{Sturm 认证}✓✓；\ \textbf{模窗口来源缺口}✓ \ —— \ \text{与 C 支同一性质}✓）$$
$$\qquad \Longrightarrow \ \text{B 支本身}\ \textbf{不再是 residual gap}✓✓$$
$$\textbf{⑧ 整体逻辑出口（唐先生指出）}✓✓：\textbf{A／B／C 三支皆 CLOSED}✓✓✓，\ \text{但}\ \textbf{整体}\ \mathcal F_0 = \varnothing\ \textbf{仍有逻辑出口待查}✓✓$$
$$\qquad \textbf{下一项}✓✓：\ \boxed{\text{A／B／C 合并后的整体逻辑缺口审计}}✓✓（\text{端点原则的完整性} ＋ \text{窗口来源缺口}✓✓）$$

## §1 核验记录（✓✓，全部精确）

$$\textbf{Sturm}✓✓：\texttt{count\_roots}(P_B', \tfrac18, \tfrac{1137}{4000}) = 1✓✓（\text{与唐先生}\ V = 2 \to 1\ \textbf{一致}✓✓）$$
$$\textbf{导数端点}✓✓：2475✓✓（\textbf{精确}✓）；-\tfrac{316876084411629}{3906250000000}✓✓（\textbf{精确}✓）$$
$$\textbf{函数端点}✓✓：\tfrac{135}{8}✓✓（\textbf{精确}✓）；\tfrac{11607824617202992609}{31250000000000000}✓✓（\approx 371.45✓）$$
$$\textbf{Q_5 对照}✓✓：t = \tfrac18 \Longrightarrow \tfrac{89}{32}✓✓；\ t = \tfrac{1137}{4000} \Longrightarrow \approx 3.7984✓✓；\ \text{差（对}\ \tfrac{341}{128}）\text{分别}\ \tfrac{15}{128}✓、\approx 1.134✓✓$$
$$\textbf{最小端点}✓✓：\min\big(P_B(\tfrac18),\ P_B(\tfrac{1137}{4000})\big) = \tfrac{135}{8}✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A** ✓ | **CLOSED（解析）** ✓✓✓ |
| **Branch B** ✓ | **本档：CLOSED（Sturm 认证；模窗口来源缺口）** ✓✓✓ |
| **Branch C** ✓ | **CLOSED（conditional；residual window-origin gap）** ✓✓ |
| **三支合并** ✓ | **皆闭合 —— 但整体逻辑出口待查** ✓✓ |
| Level 2 ✓ | **下一个审计对象：端点原则完整性 ＋ 窗口来源缺口** ✓✓ |
| `\inf Q_5 = \tfrac{341}{128}` ✓ | **尚未完成全局解析证明** ✗✓ |
| Level 3 ✓ | **禁止启动** ✗✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗；\ \text{Level 2 CLOSED}✗✓（\textbf{整体出口待查}✓）；\ \inf = \tfrac{341}{128}\ \text{全局已证}✗✓；\ \text{Bridge A 已闭合}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{Sturm 计数／端点值}\ \textbf{精确}✓✓；\ \text{B 支封口}\ \textbf{在给定窗口下成立}✓✓；\ \text{窗口来源缺口}\ \textbf{仍存}✗✓$$
$$\qquad \textbf{不}证\ t \ge \tfrac18\ \text{全局正性}✗✓；\ \textbf{不}碰 C 支✗✓；\ \textbf{符合}「窗口来源 \to 局部严格封口」纪律✓✓$$

## §4 本档**不**做的事（✓✓）

$$\textbf{不做}数值采样✗✓（\textbf{按唐先生指示}✓）；\textbf{不}碰 C 支✗✓；\textbf{不}启动 Level 3✗✓；\textbf{不}把\ t_*\ \text{小数入证}✗✓$$

## §5 边界（✓✓）

$$\textbf{有计算}✓（sympy Sturm／精确有理，已批准✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 Sturm            命中文件数=5    :: ./C3835-branch-B-critical-branch-and-polynomial-reduction.md ./E154-algebraic-identity-transverse-obstruction-audit.md ./C335-P2-chebyshev-moment-joint-constraints-five-parameter-reduction.md
技术词 计数封口     命中文件数=1    :: ./E183-T2a-verdict-projection-rigidity.md
技术词 唯一临界点  命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（sympy `P_B`／`P_B'`／`count_roots`／精细端点 `Fraction` 核验 ✓）
