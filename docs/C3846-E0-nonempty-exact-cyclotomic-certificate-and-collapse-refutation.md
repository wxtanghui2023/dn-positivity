已查地图（**先查后写**）：`C-380-12`（**`E_0` 精确形式 ＋ 目标 C-380-12-A = ∅** ✓✓）、`C-380-13`（**线性 Fourier 对偶 sharp 封口** ✓✓）、`C-380-22`（**`\mathcal F_0 = \{(w_1..w_4) \in (S^1)^4 : \Re q_k \le -\tfrac12,\ k \le 6\}`** ✓✓）、`C-380-25／26`（**采样级：前四可行／前六"不可行"仅为网格级** ✓✓）、`C-380-44／45`（**坍缩 GAP ＋ 稳定性桥登记** ✓✓）、`C-380-22` M1–M5 过滤器 ✓✓。回查见 §5 ✓

D0: 本档对象 = **C-380-46：`E_0` 四点问题的精确可行性证书 ＋ 坍缩蕴含的反驳 ＋ 非配对模态精确仿射分解**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① ⭐⭐⭐ 主结果：}\mathcal F_0 \ne \varnothing\ \textbf{（精确证书）}✓✓：\ \omega = e^{2\pi i/9}✓,\ \boxed{S = \{1,2,3,4\} \subset \mathbb Z/9}✓✓,\ z_j := \omega^j\ (j \in S)✓ \Longrightarrow$$

$$\qquad \boxed{\Re \sum_{j \in S} z_j^k = -\tfrac12\qquad \text{对}\ k = 1,2,\dots,8\ \textbf{精确成立}}✓✓✓;\qquad k = 9\ \text{时}= 4✓$$

$$\qquad \Longrightarrow\ \text{六个约束}\ (k \le 6)\ \textbf{同时取等号成立}✓✓ \Longrightarrow\ \boxed{\textbf{C-380-12-A 的目标（} = \varnothing\text{）为假}}✗✗$$

$$\qquad \Longrightarrow\ \textbf{全链的第 2 层（"}\mathcal F_0 = \varnothing\text{"）}\ \textbf{被反驳}✗\ ——\ \textbf{不是"未证"，而是"假"}✓✓$$

$$\textbf{② 完整循环来源（穷举）}✓✓：n \le 24\ \text{全部 4-子集穷举}✓ \Longrightarrow\ \text{有解者}\ \textbf{仅}\ n = 9\ (\textbf{16 个})✓ \text{与}\ n = 18\ (\textbf{16 个，同一批的标号 2 倍})✓✓$$

$$\qquad n = 3,\dots,8;\ 10,\dots,17;\ 19,\dots,24\ \Longrightarrow\ \textbf{0 个}✓✓ \Longrightarrow\ \text{共振与}\ \textbf{9 阶循环结构} \text{不可分}✓✓$$

$$\textbf{③ 孤立性（局部刚性）}✓✓：\text{以}\ S = \{1,2,3,4\}\ \text{为基}✓,\ \varepsilon = 10^{-1},\dots,10^{-5}\ \text{各 4000 个随机方向}✓ \Longrightarrow\ \textbf{0 个仍可行}✗✓$$

$$\qquad \Longrightarrow\ \text{六个约束在该点}\ \textbf{同时取等号}✓ \Longrightarrow\ \boxed{\text{这类点是}\ \textbf{孤立点}}✓✓ \Longrightarrow\ \text{解释了为何}\ \textbf{一切随机采样都找不到它}✓✓$$

$$\textbf{④ 坍缩蕴含被反驳（关键逻辑升级）}✓✓：\ \boxed{\mathcal F_0 \ne \varnothing \Longrightarrow \mathcal F_0^{(2)} \ne \varnothing}\ \text{为}\ \textbf{假}✗✗$$

$$\qquad \text{因}\ \mathcal F_0 \ne \varnothing\ \text{（本档）而}\ \mathcal F_0^{(2)} = \varnothing\ \text{（`C-380-43` CLOSED）}✓✓ \Longrightarrow\ \textbf{C-380-44 的 GAP}\ \text{由「缺结构定理」}\ \textbf{升级为「路线被反驳」}✓✓$$

$$\qquad \Longrightarrow\ \textbf{不得}再把 Level 3 表述为"待补的桥"✗✓ \ ——\ \text{该蕴含}\ \textbf{原理上不成立}✓✓$$

$$\textbf{⑤ 稳定性桥（路线 II）亦死}✓✓：\text{固定}\ (m, P_2)\ \text{切片上}✓ \Longrightarrow\ \boxed{\dfrac{\partial Q_5}{\partial \Delta_4} = 320\,m}✓✓$$

$$\qquad \text{而}\ Q_1 = 4m \le -\tfrac12\ \text{强制}\ \boxed{m \le -\tfrac18 < 0}✓✓ \Longrightarrow\ \text{在整个可行域上}\ 320m \le -40 < 0✓✓$$

$$\qquad \Longrightarrow\ \boxed{Q_5(X) \ge \tfrac{341}{128} + \Psi(\Delta_4)\ (\Psi > 0)\ \textbf{形式为假}}✗\ ——\ \text{沿保持}\ P_3\ \text{的配对方向}\ \Delta_4 \uparrow\ \text{使}\ Q_5 \downarrow✓✓$$

$$\qquad \Longrightarrow\ \textbf{同时解释} `C-380-26`\ \text{的}\ \Delta_4 \approx +0.000878 > 0\ \text{"数值反向"}✓✓（`C-380-44` §0④ 的未解之谜）$$

$$\textbf{⑥ 非配对模态 = 精确仿射（情形 B）}✓✓：\text{固定}\ Q_1, Q_2\ \text{的切片上}✓,\ \text{以}\ P_3 = \sum_j (X_j - m)^3✓,\ \Delta_4 = \tfrac{P_2^2}{16} - \prod_j (X_j-m)✓\ \text{为自由坐标}✓✓：$$

$$\qquad \boxed{Q_3 - q_3^{(2)} = 4P_3}✓✓;\qquad \boxed{Q_4 - q_4^{(2)} = 32m\,P_3 + 32\,\Delta_4}✓✓;\qquad \boxed{Q_5 - q_5^{(2)} = \big(160m^2 - 20 + \tfrac{40}{3}P_2\big)P_3 + 320m\,\Delta_4}✓✓$$

$$\qquad \Longrightarrow\ \textbf{一阶即为全部阶}✓✓ \Longrightarrow\ \text{「two-level ＋ 正惩罚项」}\ \textbf{不成立}✗✓；\ \text{且只用}\ Q_1,\dots,Q_5\ \text{的任何证书必落}\ \textbf{C-380-13 已封族}✗✓$$

$$\qquad \Longrightarrow\ \text{非配对模态的}\ \textbf{最低非零变分为一阶、不定号}✓✓ \Longrightarrow\ \text{按预登记判据}\ \boxed{\textbf{关闭 two-level 稳定性路线}}✓✓$$

$$\textbf{⑦ 判词}✓✓：\ \boxed{E_0\ \text{（四点松弛）}\textbf{非空}}✓✓ \Longrightarrow\ \text{该松弛}\ \textbf{不携带足以承载 RH 的算术信息}✓✓（9 次单位根解为}\ \textbf{非算术解}✓✓）$$

$$\qquad \Longrightarrow\ \boxed{\text{由}\ E_0\ \text{出发的"封口"路线}\ =\ \textbf{NO-GO}}✓✓;\ \text{继续的正确形态}\ =\ \boxed{\text{恢复被松弛掉的算术约束}}✓✓\ \text{而非在}\ E_0\ \text{内继续封口}✗✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 证书与初等机制（✓✓）

$$\textbf{(a) 定义}✓✓：f(k) := \sum_{j \in S}\cos(2\pi jk/9)✓,\ f(0) = 4✓;\ f(k) = f(-k)✓\ (\text{偶性})✓✓$$

$$\textbf{(b) 总体恒等式}✓✓：\sum_{k=0}^{8}f(k) = \sum_{j \in S}\sum_{k=0}^{8}\cos(2\pi jk/9) = 0✓\ (0 \notin S)✓ \Longrightarrow\ \sum_{k=1}^{8}f(k) = -4 = 8 \cdot (-\tfrac12)✓✓$$

$$\qquad \Longrightarrow\ \textbf{常数}-\tfrac12\ \text{与整体恒等式}\ \textbf{相容（共振饱和）}✓✓ \ ——\ \text{即}\ f\ \text{在}\ k = 1,\dots,8\ \text{上}\ \textbf{全平}✓✓$$

$$\textbf{(c) 实际判据}✓✓：\text{只需}\ f(1) = f(2) = f(3) = f(4) = -\tfrac12✓✓ \Longrightarrow\ \textbf{自动蕴含}\ f(k) = -\tfrac12\ \text{对}\ k = 1,\dots,8✓✓$$

$$\qquad \text{（故}\ \binom{9}{4} = 126\ \text{中恰 16 个解，与穷举一致}✓✓）$$

$$\textbf{(d) 具体例子}✓✓：S = \{1,4,6,7\} = \{1,4,7\} \cup \{6\}✓ \Longrightarrow\ \text{二次剩余}\ \{1,4,7\} = ((\mathbb Z/9)^\times)^2✓ \text{加}\ \omega^6 = e^{4\pi i/3}✓✓$$

$$\qquad \text{由}\ 3 \nmid k\ \text{时}\ \sum_{q \in \{1,4,7\}}\omega^{qk} = 0✓ \Longrightarrow\ q_k = \omega^{6k}✓ \Longrightarrow\ \Re q_k = \cos(4\pi k/3) = -\tfrac12✓✓$$

$$\qquad \text{由}\ 3 \mid k\ \text{时}\ \sum_{q}\omega^{qk} = 3\omega_3^{k}✓\ (\Re = -\tfrac32)✓ \text{加}\ \omega^{6k} = 1✓ \Longrightarrow\ \Re q_k = -\tfrac32 + 1 = -\tfrac12✓✓$$

$$\qquad \Longrightarrow\ \textbf{两个分支（}3 \mid k\ \text{与}\ 3 \nmid k\text{）}\ \textbf{给出同一值}-\tfrac12✓✓ \ ——\ \text{这就是"共振"的全部内容}✓✓$$

## §2 核验记录（数字驱动 ✓✓）

| 项目 ✓ | 结果 ✓ |
|---|---|
| 120 位 mpmath：`\Re q_k + \tfrac12`（k=1..8） | **±1e-120** ✓✓（k=9 时给 4.5 ✓） |
| 穷举 n = 3..24 全部 4-子集 | 有解 **仅 n = 9（16）与 n = 18（16，同构）** ✓✓ |
| 孤立性（S=(1,2,3,4)，4000 方向 × 5 个 ε） | **0/4000 可行**（ε = 1e-1..1e-5）✓✓ |
| 仿射分解残差（20000 元组 × 独立脚本 2 次） | Q3 / Q4 / Q5 = **5.3e-15 / 1.7e-14 / 5.2e-14** ✓✓ |
| 约定核验：`\sum_j T_k(X_j)` vs 档案 two-level 闭式 | 在 (-1/8, 7/16) **完全一致**，Q_5 = 341/128 ✓✓ |
| 采样对照（档案口径） | K=4 可行比例 **0.66%**（与 `C-380-25` 的 0.65% 一致 ✓✓）；K=5／K=6 **0/3e6** ✓✓ |

$$\textbf{脚本}✓：`scripts/c380_46_counterexample.py`✓、`scripts/c380_46_probe2.py`✓、`scripts/c380_46_probe3.py`✓、`scripts/c380_46_probe_final.py`✓；输出 `scripts/out_c380_46_*.txt`✓$$

$$\textbf{说明}✓✓：采样级"K=5／K=6 不可行"（0/3e6）与精确证书\ \textbf{并不矛盾}✓✓ ——\ \text{解为}\ \textbf{孤立点}✓，\ \text{随机采样测度为零}✓✓；\ \text{这正印证}\ C\text{-}380\text{-}26\ \text{的"网格级"限定是对的}✓✓$$

## §3 边界（不得声称 ✗）

- **不**声称算术原问题（RH 侧翼命题）的真值：本档只反驳**四点松弛** `E_0`（`C-380-12` 形式）的空性。
- **不**声称 `\mathcal F_0` 的完整解集已分类：只给出 **16 个孤立解**；n > 24 未扫；其余非循环（一般角）解未分类。
- **不**声称 Level 2 有误：`\mathcal F_0^{(2)} = \varnothing` 仍成立；本档只说明它与 `\mathcal F_0 = \varnothing` **无关**。
- **不**声称 `E_{\mathrm{coll}}`（`x_1 = x_2` 层）状态改变。
- ⚠️ **条件声明**：若档案中 `E_0` 实际含**额外算术约束**（`C-358` 的 `\mathcal Z`-限制／`E_{\mathrm{even}}` 的其余条件），则本证书必须**针对那些约束重检** —— **请唐先生确认目标约束集**。

## §4 本档**不**做的事（✓✓）

$$\textbf{不}开 Level 3✗；\textbf{不}做 C-380 补丁计算✗；\textbf{不}把本档写成"RH 进展"✗✓；\textbf{不}改他档正本✗（仅新增本档 ＋ 脚本）✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）＋ 边界

```
技术词 非配对模态  命中文件数=0    ::
技术词 仿射分解     命中文件数=0    ::
技术词 单位根证书  命中文件数=0    ::
技术词 循环共振     命中文件数=0    ::
技术词 坍缩反驳     命中文件数=0    ::
技术词 9次单位根    命中文件数=0    ::
技术词 孤立点        命中文件数=0    ::
技术词 稳定性桥     命中文件数=1    :: ./C3845-route-fork-and-stability-bridge-registration.md
技术词 偏离惩罚项  命中文件数=1    :: ./C3845-route-fork-and-stability-bridge-registration.md
```
- 运行记录 ✓：`bash scripts/tech_word_check.sh` ✓（**先跑后写** ✓）

## §6 纪律与下一步（须唐先生发令 ✓）

$$\textbf{建议①}✓：\text{把}\ E_0\ \text{松弛路线登记为}\ \textbf{NO-GO}✓✓\ \text{（证书在 §1，}\textbf{可复核}✓）$$
$$\textbf{建议②}✓：\text{若继续该项目}✓,\ \text{正确形态}\ =\ \textbf{恢复算术约束后的同一问题}✓✓\ \text{（而不是在}\ E_0\ \text{内封口}✗）$$
$$\textbf{建议③}✓：\textbf{不}开 Level 3✗；\ \textbf{不}再追}\ \Psi(\Delta_4)\ \text{稳定性桥}✗（§0⑤ 已否定其形式）✓✓$$
$$\textbf{复述}✓：\text{端点为窗口化结论✗；扫描只用于定位机制✗；行内引号用全角✓；}\ git\ add\ \text{显式路径}✓$$
