已查地图（**先查后写**）：`C-3849`（**`E_0 \cap E_{\mathrm{even}} = \varnothing` ⟹ 资产 `x_j > 0`；Fejér 等号刚性** ✓✓）、`C-349`（**抵消理想：`F_{2r+1} = \int R_r\,d\mu_\sigma`；四矩小 ⟹ 近抵消** ✓✓）、`C-350`（**Bridge A／B 拆分；§0⑤ 矩映射在权重趋零／碰撞处秩掉 ⟹ 统一常数不可得** ⚠️✓）、`C-346`（**目标：`\inf\max_{r \le 12}|F_{2r+1}| > \tfrac12`** ✓✓）、`C-369`（**碰撞层 CLOSED** ✓✓）、`C-375`（**`E_{\mathrm{even}}` 定义** ✓✓）、`C-380-12 §2`（**若 `E_0` 关闭 ⟹ 资产** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-50：Bridge-A／奇频 discrepancy 首刀审计（立项 ＋ 类型审计 ＋ 有界数值探针）**（唐先生 2026-09-21 21:14 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（八条 ✓✓）

$$\textbf{① 资产升格（唐先生令）}✓✓：\ \boxed{\textbf{C3849-BL}：\ E_{\mathrm{even}} \subset [\delta_*,1]^5,\quad \delta_* := \min_{x \in E_{\mathrm{even}}}\min_j x_j > 0}✓✓$$

$$\qquad \text{由}\ C\text{-}3849\ \text{的}\ E_0 \cap E_{\mathrm{even}} = \varnothing✓ ＋ E_{\mathrm{even}}\ \text{紧}✓ ＋ x_j\ \text{连续}✓ \Longrightarrow \text{最小值达到且不为 0}✓✓$$

$$\qquad ⚠️ \textbf{只给存在性}✓✓：\textbf{本档不给}\ \delta_*\ \text{的数值下界}✗（唐先生明令）✓；经验值}\ \min_j x_j \approx 0.0039✓\ \text{（§3）仅示其}\ \textbf{可能很小}✓$$

$$\textbf{② 首刀问题（唐先生）}✓✓：\text{「偶频约束 ＋ }x_j \ge \delta_*\ \text{」能否产生}\ \boxed{\text{非偶、非重命名、严格的新信息}}✓✓\ ?\ \ \Longrightarrow\ \boxed{\textbf{答：能}}✓✓$$

$$\textbf{③ 类型审计：偶型 vs 奇型}✓✓$$

$$\qquad \textbf{(偶型 ＝ 重命名，立即封)}✗✓：\text{任何}\ \sigma\text{-不变且只依赖}\ x\ \text{的结论}✓\ \text{（`F_{2r}` 的再线性组合／}x\ \text{的单调性／凸性／一般矩不等式}✓） \Longrightarrow\ \textbf{判 repackaging，封}✓✓$$

$$\qquad \textbf{(奇型 ＝ 新信息)}✓✓：\text{节点}\ c_j := \sqrt{x_j} \in [\sqrt{\delta_*},1]✓,\ \boxed{F_{2r+1} = \sum_{j=1}^{5}\sigma_j\,T_{2r+1}(c_j)}✓✓\ \text{（由}\ T_{2r+1}(c) = c\,R_r(c^2)✓）$$

$$\qquad \text{等价测度形式}✓✓：\mu_\sigma = \sum_j \sigma_j c_j\,\delta_{x_j}✓,\ F_{2r+1} = \int R_r\,d\mu_\sigma✓✓\ \text{（`C-349` §2）} \Longrightarrow\ \text{奇型内容} = \textbf{带号测度的多矩可行性}✓✓$$

$$\qquad \text{自由度}✓✓：\sigma \in \{\pm 1\}^5 \Longrightarrow \textbf{16 类}✓\ \text{（全局符号对称}✓）；\ \text{故奇型问题}\ \textbf{不能} \text{被偶型不等式替代}✗✓$$

$$\textbf{④ ⭐ 关键机制：}\delta_* > 0\ \textbf{把 Bridge 的障碍之一移除}✓✓：\ C\text{-}350\ §0⑤\ \text{记载：矩映射在}\ \textbf{权重趋零} \text{处秩掉}⟹\ \textbf{统一常数不可得}✗✓$$

$$\qquad \text{而}\ \delta_* > 0 \Longrightarrow |w_j| = c_j \ge \sqrt{\delta_*} > 0✓✓ \Longrightarrow \textbf{权重塌缩退化被排除}✓✓；\ \text{碰撞层已由}\ C\text{-}369\ \textbf{CLOSED}✓✓$$

$$\qquad \Longrightarrow\ \text{`C-349` §3 的待证步（}\textbf{四矩小 ⟹ 近加倍结构}\text{）}\ \textbf{第一次成为良态问题}✓✓ \Longrightarrow\ \boxed{\text{这是真正的新信息（非偶、非重命名）}}✓✓$$

$$\textbf{⑤ 反重命名过滤器（登记，后续档强制适用）}✓✓：\text{候选新信息必须同时满足}$$

$$\qquad \textbf{M1}\ \text{真正使用}\ \sigma\ \text{（}\sigma\text{-变量）}✓;\quad \textbf{M2}\ \text{不是}\ F_{2r}\ \text{的线性重组}✓;\quad \textbf{M3}\ \text{使用}\ |w_j| \ge \sqrt{\delta_*}\ \text{或碰撞层信息}✓$$

$$\qquad \textbf{M4}\ \text{在}\ (x,\sigma)\ \text{层面严格缩小可行集}✓;\quad \textbf{M5}\ \textbf{不}产出"还有希望的残余"型结论}✗✓$$

$$\textbf{⑥ 有界数值探针（非大规模）}✓✓：$$

$$\qquad \textbf{(a)}\ E_{\mathrm{even}}\ \textbf{是大区域}✓✓：20000\ \text{随机起点中}\ \textbf{9678 可行}✓ \Longrightarrow\ \textbf{非薄集}✓✓\ \text{（与}\ C\text{-}342\ \text{的"出口 B"一致}✓）$$

$$\qquad \textbf{(b)}\ \text{可行样本的}\ \min_j x_j \approx \mathbf{0.003925}✓ \Longrightarrow\ \delta_*\ \text{可能很小}✓✓$$

$$\qquad \textbf{(c)}\ g := \max_{0 \le r \le 12}|F_{2r+1}|✓：\text{16 符号类中最优}\ \boxed{g = 0.903917}✓✓\ \text{（3+2 分裂}\ \sigma = (+,+,-,-,+)✓）$$

$$\qquad \textbf{(d)}\ \text{局部极小化}\ g\ \text{（3000 起点）}✓ \Longrightarrow\ \boxed{g = 0.876069}✓✓\ \text{（}x \approx (0.802,0.561,0.703,0.627,0.870)✓,\ \text{可行}✓,\ \min_j x_j = 0.561✓）$$

$$\qquad \Longrightarrow\ \boxed{\textbf{未找到}\ g \le \tfrac12\ \text{的点}}✓✓ \Longrightarrow\ \text{Bridge A 目标（}\inf g > \tfrac12\text{）}\ \textbf{数值上成立且有余量}✓✓$$

$$\qquad \qquad \text{当前最优上界}\ 0.876\ \text{vs 阈值}\ 0.5✓ \Longrightarrow\ \textbf{余量} \approx 0.376✓✓$$

$$\textbf{⑦ 判词}✓✓：\ \boxed{\text{奇频类型}\ \textbf{首刀通过}\ \text{（未被封死）}}✓✓\ \text{且获得}\ \textbf{明确机制入口}✓✓（\delta_* ⟹ 矩映射良态化）$$

$$\qquad ⚠️ \text{但}\ \textbf{不允许} \text{直接进入大规模消元}✗✓：\text{下一步应是}\ \textbf{定量矩单射性引理}✓✓\ \text{（一个解析目标，不是搜索）}✓$$

$$\textbf{⑧ 账本（见 §2）}✓✓$$

## §1 翻译（偶频／奇频的精确形式 ✓✓）

$$\textbf{节点}✓：c_j := \sqrt{x_j} \in [\sqrt{\delta_*},1]✓,\ \phi_j := \arccos c_j \in [0,\phi_{\max}]✓✓ \Longrightarrow\ \textbf{节点不逼近}\ \phi = \tfrac{\pi}{2}✓✓$$

$$\textbf{偶频}✓✓：F_{2r} = \sum_{j=1}^{5}T_{2r}(2x_j - 1) = \sum_{j=1}^{5}\cos(4r\phi_j) \le \tfrac12✓✓\ (r = 1,\dots,12) \Longrightarrow\ \text{只涉及}\ 4\mathbb Z\ \text{倍频}✓✓$$

$$\textbf{奇频}✓✓：F_{2r+1} = \sum_{j=1}^{5}\sigma_j\cos((2r+1)\phi_j)✓\ (r = 0,\dots,12)✓✓\ \text{（纯奇频}✓）$$

$$\Longrightarrow\ \text{偶／奇}\ \textbf{在}\ \phi\ \text{频率上}\ \textbf{完全分离}✓✓ \Longrightarrow\ \text{"把偶频重新线性组合成另一个偶频不等式"}\ \textbf{永远无法}\ \text{触及奇频}✗✓\ \text{（这正是 M2 的数学内容}✓✓）$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 边界层 `E_0` ✓ | **CLOSED（证明级）** ✓✓ |
| two-level 子族 ✓ | **CLOSED** ✓✓ |
| 9 次循环伪解 ✓ | **CLOSED** ✓✓ |
| `\inf_j x_j > 0` ✓ | **资产升格（存在性）** ✓✓ |
| 原始 `E_{\mathrm{even}}` ✓ | **OPEN（且为大区域）** ✓ |
| **Bridge A 奇频类型** ✓ | **首刀通过（未封死）** ✓✓ |
| Bridge A 目标 `\inf g > \tfrac12` ✓ | **数值支持（最优上界 0.876）** ✓✓ |
| Level 3 ✓ | **FROZEN** ✓✓ |
| `\Psi(\Delta_4)` ✓ | **DEAD** ✓✓ |

## §3 数值记录（数字驱动 ✓✓）

```
A：E_even 可行性 9678/20000；经验 min_j x_j = 0.003925
B：16 符号类最优 g = 0.903917（x ≈ 0.333/0.178/0.248/0.412/0.478，σ = (+,+,-,-,+)）
C：局部极小化 g（3000 起点）= 0.876069（x ≈ 0.802/0.561/0.703/0.627/0.870，max(F_2r-1/2) = -1.6e-4，min x_j = 0.561）
   未找到 g <= 1/2 的点
```
- 脚本 ✓：`scripts/c380_50_bridgeA_v2.py`✓；输出 ✓：`scripts/out_c380_50_bridgeA.txt`✓
- ⚠️ 自检 ✓：首版 `c380_50_bridgeA_entrance.py` 为**纯 Python 循环**，过慢被中止 ✓（未产出数据，不计）⟹ 已改向量化 ✓

## §4 边界（不得声称 ✗✓）

- **不**声称 `\inf g > \tfrac12` 已证（本档为**数值**，且非穷尽）✓
- **不**声称 `\delta_*` 的任何数值下界（只给存在性）✓
- **不**声称 Bridge A 已闭合／已封死 ✓
- **不**声称矩单射性引理已证（仅指出其**良态化**）✓
- **不**声称 Bridge B 成立 ✓

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 奇频           命中文件数=31   :: C348／C3811／C3802 等（档案已有概念 ✓ 引用，不计提出）
技术词 discrepancy    命中文件数=22   :: grh-goldbach-paper-draft-v2／C3811 等（已有 ✓）
技术词 符号类         命中文件数=0    :: （本档新用）
技术词 矩单射性       命中文件数=0    :: （本档新用）
技术词 重命名过滤器   命中文件数=0    :: （本档新用）
技术词 C3849-BL       命中文件数=0    :: （本档新登记）
技术词 δ_             命中文件数=134  :: 通用记号，不计
```

## §6 本档**不**做的事 ✓✓

$$\textbf{不}做 13 频大规模消元✗；\ \textbf{不}重开 two-level／\Psi(\Delta_4)／Level 3／截断／9 次循环族✗✓；\ \textbf{不}把偶频再组合当新信息✗✓$$

## §7 下一步（须唐先生发令 ✓）

$$\textbf{建议①}✓：\text{攻}\ \textbf{定量矩单射性引理}✓✓：\text{在}\ x \in E_{\mathrm{even}}✓、|w_j| \ge \sqrt{\delta_*}✓、无碰撞✓\ \text{的条件下}✓,\ \text{证}\ \operatorname{dist}(x,\mathcal Z) \le C(\delta_*)\max_{r \le 3}|F_{2r+1}|✓✓$$
$$\textbf{建议②}✓：\text{若①成功} \Longrightarrow \text{Bridge B}\ \text{的定量版本}✓✓\ \text{（}\textbf{近抵消 ⟹ 近加倍结构 ⟹ 偶频成本}\text{）}✓$$
$$\textbf{建议③}✓：\text{数值侧可加固}✓：\text{把} g\ \text{的局部极小化扩展到更多起点／更多结构族}✓\ \text{（但}\textbf{不是}\text{大规模消元}✓）$$
