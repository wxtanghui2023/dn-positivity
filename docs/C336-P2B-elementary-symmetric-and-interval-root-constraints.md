已查地图（**先查后写**）：`C-335`（五参数化 ；Newton 不等式 ✓）、`C-334`（低阶 PSD 不咬；秩 n>=11 ✓）、`C-153`（M=2 覆盖型精确代数 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-336：P2-B（`e_1..e_5` 递推 ＋ 区间实根约束 ＋ 矩上界联立）**，**零计算（解析推演）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① B1 完成}✓：\text{已把}\ F_1,F_2,F_3\ \text{显式写成}\ e_r\ \text{的低阶式}✓（\text{见 §2}✓）$$
$$\textbf{② B2 关键发现（诚实）}✓✓：\textbf{端点条件自动成立、无信息}✗✓（\text{因}\ 1 \mp c_j \ge 0\ \text{恒真}✓）\ —— \text{与唐先生预期不同，须如实登记}✓$$
$$\textbf{③ B2 新增有效条件}✓✓：\ \textbf{幂和单调性}\ m_{2r} \ge m_{2r+2}✓（\text{来自}\ |c_j| \le 1✓）\ —— \ \textbf{这是}\ C\text{-335 三条约束之外的独立约束}✓✓$$
$$\textbf{④ B3 定量窗口}✓✓：\ m_4 \in [0.917,\ 2.1875]✓（\text{非空}✓）\ \Longrightarrow \textbf{未出现矛盾}✗ \Longrightarrow \textbf{命中第三出口（约束仍有自由度）}✓$$
$$\textbf{⑤ P4}✓：\textbf{未批准}✗✓（\text{等}\ P2\text{-B 指明该找何种构型后再定}✓）；\textbf{不}\ \text{跑数值}✗、\textbf{不}\ \text{启}\ SOS✗、\textbf{不}\ \text{展开}\ \det T_{11}✗$$

## §1 B1：Newton--Girard 与 `e_r`（✓✓）

$$\textbf{幂和}✓：m_r = \sum_j c_j^r✓；\ p(x) = \prod_j (x - c_j) = x^5 - e_1x^4 + e_2x^3 - e_3x^2 + e_4x - e_5✓$$
$$\textbf{低阶 Newton--Girard}✓：m_1 = e_1✓；m_2 = e_1^2 - 2e_2✓；m_3 = e_1^3 - 3e_1e_2 + 3e_3✓；m_4 = e_1^4 - 4e_1^2e_2 + 2e_2^2 + 4e_1e_3 - 4e_4✓$$
$$\textbf{完整递推}✓：m_r = e_1m_{r-1} - e_2m_{r-2} + e_3m_{r-3} - e_4m_{r-4} + e_5m_{r-5}✓（r \ge 6✓）\Longrightarrow \text{全部}\ F_k\ (k \le 25)\ \text{由五参数决定}✓✓$$

## §2 显式低阶关系（✓✓）

$$F_1 = m_1 = e_1✓ \Longrightarrow F_1 \le \tfrac12 \Rightarrow e_1 \le \tfrac12✓$$
$$F_2 = 2m_2 - 5 = 2e_1^2 - 4e_2 - 5✓ \Longrightarrow F_2 \le \tfrac12 \Rightarrow \boxed{e_2 \ge \tfrac{2e_1^2 - 5.5}{4}}✓；\text{代}\ e_1 \le \tfrac12 \Rightarrow \textbf{e_2 \ge -1.25}✓✓$$
$$F_3 = 4m_3 - 3m_1 = 4e_1^3 - 12e_1e_2 + 12e_3 - 3e_1✓ \Longrightarrow F_3 \le \tfrac12 \Rightarrow e_3 \le \tfrac{1/2 + 3e_1 - 4e_1^3 + 12e_1e_2}{12}✓（\text{上界}✓）$$

## §3 B2：区间实根条件（✓✓）

$$\textbf{端点条件（诚实判定）}✓✓：p(1) = \prod_j (1 - c_j) \ge 0✓；(-1)^5p(-1) = \prod_j (1 + c_j) \ge 0✓ \ —— \ \textbf{在}\ |c_j| \le 1\ \text{下恒真}✗ \Longrightarrow \textbf{零信息}✗✓$$
$$\textbf{根位条件（有效）}✓：\text{全部根}\ \le 1 \iff q(y) := p(1 - y)\ \text{全部根} \ge 0✓ \Longrightarrow \text{系数}\ \textbf{交替}✓✓（\text{实根＋非负根的必要条件}✓）$$
$$\qquad \text{由此}\✓：4e_1 - 3e_2 + 2e_3 - e_4 \le 5✓；6e_1 - 3e_2 + e_3 \le 10✓；e_2 \ge 4e_1 - 10✓（\text{代}\ e_1 \le \tfrac12 \Rightarrow e_2 \ge -8✓）$$
$$\textbf{比较}✓✓：\text{由}\ F_2\ \text{得}\ e_2 \ge -1.25✓ \ \textbf{强于}\ \text{由根位得}\ e_2 \ge -8✓ \Longrightarrow \textbf{该路线不追加信息}✗✓$$
$$\textbf{⭐ 新增有效条件（幂和单调性）}✓✓：\ |c_j| \le 1 \Longrightarrow c_j^{2r} \ge c_j^{2r+2}✓（\text{逐项}✓）\ \Longrightarrow \ \boxed{m_{2r} \ge m_{2r+2} \ge 0}✓✓ \Longrightarrow m_2 \ge m_4 \ge m_6 \ge \cdots✓$$

## §4 B3：定量窗口（✓✓，本档核心 ✓）

$$\textbf{由}\ F_2 \le \tfrac12✓：m_2 \le \tfrac{11}{4} = 2.75✓$$
$$\textbf{由}\ F_4 \le \tfrac12✓：8m_4 - 8m_2 + 5 \le \tfrac12 \Longrightarrow \boxed{m_2 - m_4 \ge \tfrac{9}{16} = 0.5625}✓✓$$
$$\qquad \textbf{结构读法}✓✓：m_2 - m_4 = \sum_j c_j^2(1 - c_j^2) \ge \tfrac{9}{16}✓ \Longrightarrow \text{不可能}\ \text{「全部靠近 0」}\ ✗ \ \text{或} \ \text{「全部靠近} \pm1\text{」}✗✓$$
$$\qquad \textbf{鸽笼推论}✓✓：\exists j:\ c_j^2(1 - c_j^2) \ge \tfrac{9}{80}✓ \Longrightarrow c_j^2 \in [0.128,\ 0.872]✓（\text{区间解}✓）\ \Longrightarrow \text{某个}\ |c_j| \in (0.36,\ 0.93)✓（\text{量级}✓）$$
$$\textbf{由}\ F_6 \le \tfrac12✓（T_6(c) = 32c^6 - 48c^4 + 18c^2 - 1✓）：32m_6 \le 48m_4 - 18m_2 + 5.5✓ \Longrightarrow 48m_4 - 18m_2 + 5.5 \ge 0 \Longrightarrow \textbf{m_4 \ge 0.917}✓$$
$$\textbf{合成窗口}✓✓：\ m_2 \in [?,\ 2.75]✓，m_4 \in [0.917,\ 2.1875]✓ \ \Longrightarrow \ \boxed{\textbf{窗口非空}}✓ \Longrightarrow \textbf{无矛盾}✗✓$$

## §5 B3 三出口判定（✓✓）

$$\text{① } P \ge 0 \wedge P < 0\ \text{冲突}✗：\textbf{未}\ \text{出现}✗；\text{② 合法}\ (e_1,\dots,e_5)\ \text{已被构造}✗：\textbf{未}\ \text{构造}✗；\text{③ }\textbf{约束仍明显有自由度}✓✓ \ \Longrightarrow \textbf{命中第三出口}✓$$
$$\textbf{纪律}✓✓：\textbf{不}\ \text{把「低阶自然构型失败」当作极小值证据}✗✓；\textbf{不}\ \text{把 Newton 不等式称作充分条件}✗✓$$

## §6 下一步（给 P4 的定向建议 ✓，不批准 ✓）

$$\textbf{由本档结构推出的搜索目标}✓✓：\text{应找}\ \text{使}\ m_2 - m_4\ \text{接近其下界}✓、\text{且}\ m_2\ \text{靠近上界}✓ \text{的构型}✓ \Longrightarrow \text{即}\ \textbf{存在一个}\ |c_j| \approx 0.36 \sim 0.93✓、\text{其余偏小}✓$$
$$\qquad \textbf{另一提示}✓：\ F_4 \le \tfrac12\ \text{的等式化}\ \text{与}\ F_2,F_6\ \text{的紧缩同时发生}✓ \Longrightarrow \text{active 集大概率含}\ k = 2,4,6✓（\text{可验证}✓）$$
$$\textbf{批准前不执行}✗✓（\text{唐先生口径}✓）$$

## §7 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 幂和单调性  命中文件数=0    :: 
技术词 端点条件     命中文件数=4    :: ./V306-kernel-identification-and-full-integral-BC-frequency-mismatch.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md 
技术词 区间实根条件 命中文件数=0    :: 
技术词 自由度判定  命中文件数=0    :: 
```
- 本档新增 ✓：`幂和单调性`／`区间实根条件`（依上表判 ✓）
- **零计算** ✗（仅解析 ✓）；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：P2-B 已通 ✗；端点条件有信息 ✗（**自动成立** ✓）；已找到反例 ✗；Newton 不等式充分 ✗
