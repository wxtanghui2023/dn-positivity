已查地图（**先查后写**）：`C-367`（`P_5 \mid P_7` ✓✓；**本档勘误其 §2**✓）、`C-366`（证明责任锁定 ✓✓）、`C-364`（Jacobian 口径 ✓✓）、`C-358`（`D_∂` ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-368：判空依据的两步分解 ＋ `C-367 §2` 勘误**，**零计算（复核已跑 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 唐先生的逻辑区别正确}✓✓：\ P_5 \mid P_7\ \textbf{本身不判空}✗✓ \ —— \ \text{它只说明系统}\ \textbf{塌成单曲线}✓：\{E_5 = 0 \wedge E_7 = 0\} \iff \{P_5 = 0\}✓✓$$
$$\textbf{② 判空成立的真正依据（两步）}✓✓：\ \textbf{(a) 坍缩}✓ ＋ \textbf{(b) 因子上} \textbf{无零点}✓✓$$
$$\qquad \boxed{\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap \mathcal F = \{P_5 = 0\} \cap \mathcal F = \varnothing}✓✓ \ —— \ \text{因}\ \mathcal F \subset \{t, u > 0\}✓$$
$$\textbf{③ ⭐ 完整精确因式分解}✓✓：\ \boxed{P_5 = 2\cdot 5\cdot t^3 \cdot u \cdot (t+u)^2}✓✓ \ —— \ \text{内容}\ 10 = 2 \cdot 5✓；t, u, (t+u)\ \text{在}\ \mathbb{Q}[t,u]\ \textbf{不可约}✓✓ \Longrightarrow \text{分解}\ \textbf{完整}✓✓$$
$$\textbf{④ 精确商}✓✓：\ \boxed{P_7 = \tfrac{7}{5}\,\big(4t^3 + 3t^2u + 2tu^2 + u^3\big)\,P_5}✓✓ \ —— \ \textbf{数值复核确认}✓✓（见 §3✓）$$
$$\textbf{⑤ 可行域上严格正性}✓✓：\ \mathcal F \Longrightarrow t, u > 0✓；t + u > 0✓ \Longrightarrow \boxed{P_5 > 0}✓✓；\ \text{且}\ Q = 4t^3 + 3t^2u + 2tu^2 + u^3 > 0✓（\text{系数全正}✓）$$
$$\textbf{⑥ 结论}✓✓：\ \boxed{\mathcal D^{\mathrm{double}}_{\mathrm{coll}} \cap E = \varnothing}✓✓（\textbf{解析判空}✓✓） \ —— \text{证据：完整因式分解 ＋ 可行域严格正性}✓✓$$

## §1 ⭐ 勘误（`C-367 §2` 表述错误 ✓✓）

$$\textbf{原文（错）}✗✓：\ \text{「系统的零点集} = \{P_5 = 0\} \cup \{Q = 0\}」✗ \ —— \ \textbf{误把合取写成析取}✗✓$$
$$\textbf{正解}✓✓：\ E_5 = 0 \iff P_5 = 0✓（\text{唯一}✓，\text{因}\ s = 2t+u > 0✓）；\ E_7 = 0 \iff P_5 = 0 \vee Q = 0✓$$
$$\qquad \Longrightarrow \ \text{合取}\ \{E_5 = 0 \wedge E_7 = 0\} \iff \{P_5 = 0 \wedge (P_5 = 0 \vee Q = 0)\} \iff \boxed{\{P_5 = 0\}}✓✓$$
$$\qquad \Longrightarrow \ \textbf{对合取而言}\ Q\ \textbf{无关}✗✓（Q\ \text{只与}\ E_7 = 0\ \text{单独相关}✓） \ —— \ \text{本勘误为}\ \textbf{加法式追加}✓，\textbf{不覆盖} \text{C-367 原文}✗✓$$
$$\textbf{影响评估}✓✓：\text{该错误}\ \textbf{不影响} \text{判空结论}✓（\text{因}\ \{P_5 = 0\} \cap \mathcal F = \varnothing✓），\text{但}\ \textbf{必须} \text{留下勘误}✓✓$$

## §2 判空的两步结构（✓✓，可直接逐行审计 ✓）

$$\textbf{第 (a) 步 坍缩}✓✓：P_5 \mid P_7✓ \Longrightarrow \{E_5 = E_7 = 0\} \iff \{P_5 = 0\}✓ \ —— \ \textbf{此步本身不判空}✗✓$$
$$\textbf{第 (b) 步 因子无零点}✓✓：\mathcal F: 0 < t, u \le 1✓（\text{其余条件} s^2 - 4p \ge 0✓、1 - s + p \ge 0✓\ \text{更弱}✓）$$
$$\qquad P_5 = 10 t^3 u (t+u)^2✓ \ \text{的零点集}\ = \{t = 0\} \cup \{u = 0\} \cup \{t = -u\}✓ \ —— \ \text{三者}\ \textbf{皆与}\ \mathcal F\ \text{矛盾}✗✓$$
$$\qquad \Longrightarrow \ \boxed{P_5 > 0\ \text{on}\ \mathcal F}✓✓ \Longrightarrow \{P_5 = 0\} \cap \mathcal F = \varnothing✓✓ \Longrightarrow \text{判空}✓✓$$
$$\textbf{关键教训}✓✓：\ \boxed{\text{两方程变一方程} \ \ne \ \text{无解}}✓✓（\text{唐先生口径}✓） \ —— \ \text{判空必由}\ \textbf{因子在可行域上无零点} \text{提供}✓✓$$

## §3 数值复核记录（✓✓）

$$\textbf{复核 1}✓✓：E_5 = \dfrac{10 t^3 u (t+u)^2}{s}✓✓（\text{sympy 逐字为零}✓）；\ E_7 = \dfrac{14 t^3 u (t+u)^2 Q}{s^2}✓✓$$
$$\textbf{复核 2}✓✓：\dfrac{P_7}{P_5} = \tfrac{28}{5}t^3 + \tfrac{21}{5}t^2u + \tfrac{14}{5}tu^2 + \tfrac{7}{5}u^3 = \tfrac{7}{5}Q✓✓ \ —— \ \text{与}\ \tfrac{7}{5}Q\ \textbf{精确相等}✓✓$$
$$\textbf{复核 3}✓✓：\text{四组有理点}（t,u） \in (0,1]^2✓ \ \text{皆得}\ E_5 \ne 0✓，E_7 \ne 0✓ \ —— \ \text{例}：t = \tfrac{1}{10}, u = \tfrac{3}{10} \Longrightarrow E_5 = \tfrac{3}{3125}✓，E_7 = \tfrac{609}{3906250}✓✓$$

## §4 后果与账本（✓✓）

$$\textbf{碰撞层闭合}✓✓：\mathcal D^{\mathrm{triple}}_{\mathrm{coll}} = \varnothing✓（C-361✓）＋ \mathcal D^{\mathrm{double}}_{\mathrm{coll}} = \varnothing✓（本档✓） \Longrightarrow \boxed{\mathcal D_{\mathrm{coll}} = \varnothing}✓✓$$
$$\textbf{边界}✓✓：\text{仍}\ \textbf{不}写\ \mathcal Z \cap E = \varnothing✗；\textbf{不}写\ H = \varnothing✗；\textbf{不}写\ \mathcal D_{\mathrm{reg}}\ \text{已处理}✗✓$$

| 层 ✓ | 状态 ✓ | 证据 ✓ |
|---|---|---|
| `\mathcal D_{\partial}` ✓ | **完整分类** ✓✓ | 解析 ✓ |
| `\mathcal D^{\mathrm{triple}}_{\mathrm{coll}}` ✓ | **`\varnothing`** ✓✓ | 解析消元 ✓ |
| `\mathcal D^{\mathrm{double}}_{\mathrm{coll}}` ✓ | **`\varnothing`** ✓✓ | **完整因式分解 ＋ 可行域严格正性** ✓✓ |
| `\mathcal D_{\mathrm{reg}}` ✓ | **OPEN** ✓ | 尚未进入 ✓ |
| `\mathcal Z \cap E` ✓ | **OPEN** ✓ | — ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ | — ✓ |

## §5 下一步（✓✓，登记不执行 ✓）

$$\text{碰撞层已闭合}✓✓ \Longrightarrow \text{下一目标}\ = \mathcal D_{\mathrm{reg}}✓（\text{一维非退化族}✓） \ —— \ \textbf{不}新增方法✗✓（\text{沿用 C-355 五件套}✓）$$
$$\textbf{禁项}✓✓：\textbf{不}跳\ Bridge\ A✗、\textbf{不}回 25 频全局优化✗、\textbf{不} SOS✗、\textbf{不}猜\ G_*✗$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 坍缩非判空  命中文件数=0    :: 
技术词 因式分解完整性 命中文件数=0    :: 
技术词 可行域严格正性 命中文件数=0    :: 
```
- **零计算** ✗（复核已跑 ✓）；`D1 = 0` ✓；**未覆盖** `C-367` 原文 ✓（加法式勘误 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：坍缩本身判空 ✗；`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗
