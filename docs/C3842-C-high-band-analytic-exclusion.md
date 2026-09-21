已查地图（**先查后写**）：`C-380-39`（**`R_C` 两带** ✓✓）、`C-380-38`（**条件 ① 因式分解** ✓✓）、`C-380-40`（**身份审计** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-42：C 支高带解析排除**，**有计算（符号 ＋ 核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 目标（唐先生定）}✓✓：\textbf{不}继续盯\ R_C\ \text{的符号}✗✓（\text{已知两带}✓），\ \text{而}\ \textbf{逐项代入完整 feasibility 不等式}✓✓，\ \textbf{优先测试}\ A(-t) - \tfrac{7}{16}\ \text{的符号}✓✓$$
$$\textbf{② ⭐⭐ 首选机制成立（本档核心）}✓✓✓：\text{高带}\ u \ge u_2 = \tfrac{7 + \sqrt{22}}{32} \approx 0.365325✓ \Longrightarrow t \ge \sqrt{u_2} = 0.604422✓✓$$
$$\qquad \textbf{精确}✓✓：u_2 > \tfrac14 \iff \tfrac{\sqrt{22} - 1}{32} > 0✓✓（\text{显然}✓） \Longrightarrow \boxed{t > \tfrac12}✓✓$$
$$\qquad \text{条件 ① 的因式分解}✓✓（C\text{-}380\text{-}38✓）：A \le \tfrac{7}{16} \iff 8t(2t - 1)(32t^2 + 16t - 1) \le 0✓✓$$
$$\qquad \qquad t > \tfrac12 \Longrightarrow (2t - 1) > 0✓；\ 32t^2 + 16t - 1 > 0 \iff t > \tfrac{-1 + \sqrt6}{8} \approx 0.181186✓✓ \Longrightarrow \text{三者皆正}✓✓$$
$$\qquad \Longrightarrow \ \boxed{A(-t) > \tfrac{7}{16}\ \text{于整个高带}}✓✓✓ \Longrightarrow \ Q_2\ \text{给}\ s \le \tfrac{7}{16}✓ \ \textbf{而}\ s \ge A > \tfrac{7}{16}✗✗$$
$$\qquad \Longrightarrow \ \boxed{\textbf{高带为空（严格解析矛盾）}}✓✓✓ \ —— \ \textbf{单多项式符号证书}✓✓，\ \textbf{不做根排序}✗✓$$
$$\textbf{③ 核验}✓✓：A(-\sqrt{u_2}) = 0.510784 > 0.4375 = \tfrac{7}{16}✓✓；A(-1) = 0.927083✓✓；A(0.6044216) = 0.510784✓✓$$
$$\qquad \textbf{数值抽样（高带）}✓✓：t = 0.6045 \Longrightarrow Q_2 = +0.0868✓；0.62 \Longrightarrow +0.1845✓；0.64 \Longrightarrow +0.3147✓；0.6614 \Longrightarrow +0.4591✓✓$$
$$\qquad \qquad \Longrightarrow \ Q_2 \le -\tfrac12\ \textbf{全部失败}✗✓ \ —— \ \textbf{与解析结论完全一致}✓✓$$
$$\textbf{④ 低带对照（诚实标注）}✓✓：\text{低带}\ u \le u_1 = \tfrac{7 - \sqrt{22}}{32} \approx 0.072175✓ \Longrightarrow t \le 0.268653✓ \Longrightarrow A = 0.33689 < \tfrac{7}{16}✓✓$$
$$\qquad \Longrightarrow \ \textbf{低带不被机制 1 排除}✗✓（\text{其由 C 支认证处理}✓✓） \ —— \ \textbf{两带性质不同}✓✓$$
$$\textbf{⑤ 因此 C 支高带 CLOSED}✓✓✓：\ \boxed{\text{C 高带}\ \textbf{解析排除}}✓✓ \ —— \ \textbf{未使用扫描作为结论}✗✓（\text{扫描仅用于定位机制}✓✓，\text{与唐先生一致}✓✓）$$
$$\textbf{⑥ 后续（global coverage → } \mathcal F_0 = \varnothing✓）✓✓：\textbf{下一步} = \text{总账拼接}✓✓：\ \text{endpoint completeness} ＋ B\ \text{coverage} ＋ C\ \text{coverage} ＋ A／B／C\ \text{positivity} \Longrightarrow \mathcal S_m = \varnothing✓✓$$
$$\qquad \textbf{并须检查}✓✓：\mathcal S_m = \varnothing \iff \mathcal F_0 = \varnothing\ \text{是否只是定义展开}✓，\ \textbf{还是} \text{存在额外的参数域／量词出口}✗✓$$

## §1 记录（✓✓）

$$\textbf{高带}✓✓：u_2 = \tfrac{7 + \sqrt{22}}{32} = 0.36532549✓；\ \sqrt{u_2} = 0.60442162 > \tfrac12✓✓；\ A(\sqrt{u_2}) = 0.510784 > 0.4375✓✓$$
$$\textbf{机制 1}✓✓：A > \tfrac{7}{16}\ \text{于}\ t > \tfrac12✓✓ \Longrightarrow \text{与}\ Q_2\ \text{矛盾}✓✓；\ \textbf{低带}✓：A(0.268653) = 0.33689 < 0.4375✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| **Branch A／B** ✓ | **CLOSED（B：certified enlarged window）** ✓✓✓ |
| **Branch C 低带** ✓ | **CLOSED** ✓✓ |
| **Branch C 高带** ✓ | **本档：CLOSED（解析）** ✓✓✓ |
| **endpoint `s = m^2`** ✓ | **CLOSED（infeasible）** ✓✓ |
| **endpoint-combination exhaustion** ✓ | **CLOSED** ✓✓ |
| **global coverage** ✓ | **本档：最后一步拼接待做** ✓✓ |
| `\mathcal F_0 = \varnothing` ✓ | **OPEN** ✗✓ |
| `\inf Q_5` ✓ | **OPEN（\textbf{不作为目标}）** ✗✓ |
| Level 3 ✓ | **FROZEN** ✗✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal F_0 = \varnothing\ \text{已证}✗✓；\ \inf Q_5 = \tfrac{341}{128}\ \text{已证}✗✓；\ \text{用扫描当解析结论}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{高带排除}\ \textbf{解析}✓✓；\ \text{低带靠认证}✓✓；\ \text{扫描仅为定位}✓✓$$

## §4 本档**不**做的事（✓✓）
$$\textbf{不}继续盯\ R_C\ \text{符号}✗✓；\textbf{不}用扫描当结论✗✓；\textbf{不}启动 Level 3✗✓；\textbf{不}碰\ \inf Q_5✗✓$$

## §5 边界（✓✓）
$$\textbf{有计算}✓；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 扩大窗口重封口 命中文件数=0    ::
技术词 低带高带     命中文件数=0    ::
技术词 单多项式符号证书 命中文件数=0    ::
```
- 运行记录 ✓：`python3 -`（sympy `u_2`／`A − 7/16` 因式 ＋ 高带抽样 ✓）
