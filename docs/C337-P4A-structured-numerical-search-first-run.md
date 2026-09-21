已查地图（**先查后写**）：`C-336`（**CLOSED** ✓；`m_2 <= 11/4`✓；`m_2 - m_4 >= 9/16`✓；`m_4 >= 11/12`✓；幂和单调性 ✓）、`C-334`（低阶不咬；秩 n>=11 ✓）、`C-272`（`L` 中位 0.3827／`U` 中位 2.1766／真反例 0 ✓）、`C-318`／`C-319`（工程型缺口／运行相关 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-337：P4-A 结构化数值搜索（首次执行）**，**有计算（已批准 ✓）**
D1: 0
说明（D1 判定依档案纪律）: 本档为已批准计算的记录档；其内容为**数值证据**，**不构成新机制／新自由度** ✓
FREEZE-ACK: 本档即冻结审计
说明: 本档为已批准计算的记录档；结论仅作数值证据，不作证明 ✓

---

## §0 结论（五条 ✓✓）

$$\textbf{① 数值结果}✓✓：\ G_{min} \approx \textbf{0.9738}✓，\textbf{远高于}\ \tfrac12✓（\text{gap} = +0.474✓）\ \Longrightarrow \textbf{未找到反例}✗✓$$
$$\textbf{② active set 与预判不同}✗✓：\ \textbf{A} = \{5,\ 12,\ 14,\ 21\}✓，\textbf{不是}\ \{2,4,6\}✗✓（\text{C-336 的定向建议被否定}✓）$$
$$\textbf{③ 与可分证书的差距悬殊}✓✓：\text{真值}\ \approx 0.974✓ \ \text{vs}\ \text{可分界中位}\ 0.3827✓（\text{C-272}✓）\ \Longrightarrow \ \textbf{交换间隙是真正瓶颈}✓✓$$
$$\textbf{④ 性质}✓✓：\textbf{数值证据，非证明}✗✓ \ —— \ G_{min}\ \text{只是}\ \inf\ \text{的上界}✓（\text{启动点有限}✓）；\textbf{不}\ \text{升级为定理}✗$$
$$\textbf{⑤ P4 逻辑分支}✓：\textbf{未}\ \text{触发反例路线}✗（\text{非}\ G < \tfrac12✓）；\textbf{未}\ \text{触发极限构型审计}✗（\text{非逼近}\ \tfrac12✓）；\textbf{不}\ \text{启}\ SOS✗$$

## §1 P4-A 执行设定（✓✓，四类信息 ✓）

$$\textbf{目标}✓：G(c) = \max_{1 \le k \le 25} \sum_{j=1}^{5} T_k(c_j)✓，c \in [-1,1]^5✓（\theta = \arccos c✓ 为双射✓）$$
$$\textbf{方法}✓：\text{随机多起点}\ 60{,}000✓ \ \text{点} ＋ \textbf{模式搜索}（坐标方向、步长对半收缩✓）\ ＋ \ 4\ \text{个结构化起点}✓$$
$$\textbf{记录}✓：\text{① 目标值}✓；\text{② active set}\ A(c) = \{k: F_k \approx G\}✓；\text{③ 三个 moment slack}✓；\text{④ 节点几何}（排序、配对✓）$$

## §2 数值结果（✓✓）

$$\textbf{最优构型}✓：c_{sorted} = [-0.872005,\ -0.743812,\ -0.136776,\ +0.091438,\ +0.909945]✓$$
$$\qquad G_{min} = \textbf{0.973822735802}✓ \quad \text{target} = 0.5✓ \quad \text{gap} = +4.738 \times 10^{-1}✓$$
$$\textbf{active set}✓✓：A = \{5,\ 12,\ 14,\ 21\}✓（\text{四个}\ k\ \text{并列取最大}✓，F_5 = F_{12} = F_{14} = F_{21} = 0.973823✓）$$
$$\textbf{moment}✓：m_2 = 2.168716943✓；m_4 = 1.570292059✓；m_6 = 1.176673231✓$$
$$\qquad \text{slack}✓：11/4 - m_2 = +0.581283✓；m_2 - m_4 - 9/16 = \textbf{+0.035925}✓✓（\text{紧！}✓）；m_4 - 11/12 = +0.653625✓$$
$$\qquad \textbf{单调性}✓：m_2 \ge m_4 \ge m_6\ \textbf{成立}✓✓（与 C-336 的幂和单调性一致✓）$$
$$\textbf{节点几何}✓：\text{排序后}\ \text{无精确}\ c_i = -c_j\ ✗；\min_{i<j}|c_i + c_j| = 0.037940✓（\textbf{接近配对}⚠️，\text{未精确}✓）\ \Longrightarrow \text{呈「两负＋一接近零＋两正」结构}✓$$
$$\textbf{采样统计}✓：60k\ \text{随机点}\ G_{min} = 1.1935✓，\ G_{p1} = 1.7983✓，\ G_{median} = 2.9792✓ \Longrightarrow \text{低值区}\ \textbf{稀少}✓（\text{需局部精化}✓）$$
$$\textbf{top-5}✓：0.9738,\ 1.0012,\ 1.0223,\ 1.0313,\ 1.0365✓ \Longrightarrow \text{低值区}\ \textbf{平坦、无孤立尖锐极小}✓$$

## §3 与可分证书的结构性对照（✓✓，本档最有价值 ✓）

$$\text{真值}\ \approx 0.9738✓ \quad \text{vs} \quad \text{可分证书}\ L(B)\ \text{中位}\ 0.3827✓（C-272✓）\ \Longrightarrow \ \textbf{间隙} \approx 0.59✓✓$$
$$\textbf{读法}✓✓：\text{命题}\ \textbf{远非紧}✓（\text{真值距}\ \tfrac12\ \text{有}\ 0.47\ \text{余量}✓）\ \text{而可分证书}\ \text{却}\ \textbf{卡在}\ \tfrac12\ \text{以下}✗ \Longrightarrow \textbf{瓶颈确为 max–min 交换}✓✓（\text{与 C-330 诊断一致}✓）$$

## §4 对 C-336 的勘误与注释（✓✓，唐先生指定 ✓）

$$\textbf{① 保留注释、不升级}✓✓：\text{C-336 §4 的「存在一个}\ |c_j| \approx 0.36 \sim 0.93✓，\text{其余偏小」}✓ \ \Longrightarrow \ \textbf{仅作搜索启发}✓，\textbf{不}\ \text{作数学推论}✗✓（\text{唐先生修正}✓）$$
$$\textbf{② 区间精确核算}✓✓：\text{由}\ c_j^2(1 - c_j^2) \ge \tfrac{9}{80}✓ \Longrightarrow c_j^2 \in [\tfrac{1-\sqrt{0.55}}{2},\ \tfrac{1+\sqrt{0.55}}{2}] = [\textbf{0.12919},\ \textbf{0.87081}]✓✓ \Longrightarrow |c_j| \in [\textbf{0.3595},\ \textbf{0.9332}]✓$$
$$\qquad \textbf{登记差异}⚠️：\text{唐先生给的}\ [0.1127,\ 0.8873]\ \text{与上述}\ \textbf{不符}✓（\text{对应}\ \sqrt{0.6}\ \text{而非}\ \sqrt{0.55}✓）\ —— \ \text{本档如实记录，\textbf{不}更改}\ C\text{-336 正本}✗✓$$
$$\textbf{③ 实测印证}✓：\text{最优构型的}\ |c_j|\ \text{值为}\ 0.091,\ 0.137,\ 0.744,\ 0.872,\ 0.910✓ \ \Longrightarrow \ \textbf{恰有两个落在}\ [0.3595,\ 0.9332]✓ \ —— \ \text{与「至少一个」的弱结论一致}✓，\textbf{不}\ \text{支持「其余偏小」}✗✓$$

## §5 P4 判定状态（✓✓）

$$\textbf{反例路线}✗：\textbf{未}\ \text{触发}✗（\text{非}\ G_{min} < \tfrac12✓）\ \Longrightarrow \ H \ne \varnothing\ \textbf{未出现}✓$$
$$\textbf{极限构型审计}✗：\textbf{未}\ \text{触发}✗（\text{非逼近}\ \tfrac12✓，\text{余量}\ 0.47✓）$$
$$\textbf{SOS}✗：\textbf{继续冻结}✓（\text{唐先生口径}✓）$$
$$\textbf{最有价值的下一步}✓✓：\text{既然真值}\ \approx 0.974 \gg \tfrac12✓ \Longrightarrow \textbf{目标应是}\ \text{把}\ \textbf{联合信息}（\text{PSD／递推／幂和单调性}✓）\ \text{变成可审计证书}✓，\textbf{而非} \text{证明紧界}✗✓$$

## §6 状态表（✓✓）

| 项 | 状态 |
|---|---|
| `C-336` ✓ | **CLOSED** ✓ |
| `P2-B` ✓ | **未闭合，但有效约束已提取** ✓ |
| `P4` ✓ | **已批准并执行（本档）** ✓ |
| `P3／SOS` ✓ | **继续冻结** ✗ |

## §7 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 P4-A             命中文件数=0    :: 
技术词 低值构型     命中文件数=0    :: 
技术词 活跃集        命中文件数=7    :: ./C194-T13-B-w2-degenerate-minimax-structure-and-proof-plan.md ./C220-closure-audit-what-is-missing-for-m3-equals-Fx0.md ./C188-YI-4-no-go-for-fixed-lambda-linear-certificates.md 
技术词 交换间隙     命中文件数=1    :: ./C271-M5-half-budget-not-closed-formal-record-and-failure-mode-precise-diagnosis.md 
```
- 运行记录 ✓：脚本 `/tmp/p4a.py` ✓；`60,000` 随机点 ＋ `16` 次局部精化 ＋ `4` 结构化起点 ✓；本档**未**写入仓库的数值资产（如需要可另立）⚠️
- **本档有计算**（已批准 ✓）；**`D1 = 0`** ✓（数值记录 ≠ 新机制 ✓）；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：`m_5 = 0.9738` 为定理 ✗（仅为 `inf` 的**上界** ✓）；M=5 已证 ✗；已找到反例 ✗；`{2,4,6}` 是绑定集 ✗
