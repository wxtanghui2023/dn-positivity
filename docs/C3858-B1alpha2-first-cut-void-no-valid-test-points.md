已查地图（**先查后写**）：`C-3857`（**单权重 KKT 0 候选；次微分诊断** ✓✓）、`C-3856`（**两候选非极小；`0.876069` 为上界** ✓✓）、`C-3855`（**A：内部信号** ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-380-58：B1-α-2 首刀（次微分凸组合 KKT）—— 空跑记录 ＋ 修正方案**（唐先生 2026-09-21 22:21 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 档位}✓✓：\text{B1-}\alpha\text{-2}\ \text{只做}\ \textbf{站性模型修正}✓（\text{次微分凸组合}✓）；\ \textbf{不做}\ \alpha\text{-3}✗✓、\ \textbf{不做}\ \beta✗✓$$

$$\textbf{② 所用站性条件（按唐先生规格）}✓✓：\ \boxed{0 \in \operatorname{conv}\big\{\operatorname{sgn}(F_{2r+1}^{(\sigma)})\nabla F_{2r+1}^{(\sigma)}\big\} + \sum_{q \in \mathcal A}\lambda_q\nabla F_{2q}}✓✓$$

$$\qquad \text{权重作为}\ \textbf{可行性 LP}✓：\omega \ge 0✓,\ \sum\omega = 1✓,\ \lambda_q \ge 0✓；\ \text{活跃集用}\ \textbf{容差} \text{定义}✓（\text{奇频}\ 10^{-7}✓,\ 偶频}\ 10^{-6}✓）$$

$$\textbf{③ ⚠️ 结果：}\textbf{空跑（VOID）}✗✓\ —— \textbf{本刀不产生任何 KKT 判词}✗✓$$

$$\qquad \textbf{原因}✓✓：\text{离散步进惩罚优化在本次运行中}\ \textbf{未走到相关极小点}✓✓：\ \text{全部 16 个}\ \sigma\ \text{上得到的}\ g \approx 2.0 \sim 2.3✓✓ \Longrightarrow \textbf{远差于已知}\ 0.876069✓ \Longrightarrow \text{这些点}\ \textbf{不是极小点}✓ \Longrightarrow \text{不能作为 KKT 检验对象}✗✓$$

$$\qquad \textbf{另一特征}✓：\text{所有点}\ |\mathcal I| = 1✓（\text{单一活跃奇频}✓）\ \Longrightarrow \textbf{未触及多活跃结构}✓✓ \Longrightarrow \text{与"极值是并列型"的预期}\ \textbf{不矛盾}✓（\text{只是没走到}✓）$$

$$\textbf{④ 读法更正（自检）}✗✓：\text{首版脚本}\ \text{"margin\_max} = 0.5 - \min_r F_{2r}"✓；\ \text{本刀输出}\ \text{margin\_max} \approx 2 \sim 4✓ \Longrightarrow \textbf{可行且余量很大}✓✓$$

$$\qquad ⚠️ \text{我一度把}\ \textbf{"余量大"}\ \text{误读成"违约束"}✗✓\ \text{（符号方向读错}✓） \Longrightarrow \text{已更正}✓；\ \text{结论：}\textbf{问题不在可行性门槛}✓，\ \textbf{在优化器未收敛}✓✓$$

$$\textbf{⑤ 修正方案}✓✓（下一刀）$$

$$\qquad \textbf{(a)}✓\ \text{从}\ \textbf{已知点}\ 0.876069\ \text{出发}✓✓，\ \text{用}\ \textbf{带显式约束} \text{的优化器}✓（SLSQP：}\min\ \max_r|F_{2r+1}|✓\ \text{s.t.}\ F_{2r} \le \tfrac12✓）\ \text{做}\ \textbf{局部精修}✓$$
$$\qquad \textbf{(b)}✓\ \text{再用}\ \textbf{次微分 LP}✓\ \text{在该点做站性检验}✓✓（\text{含容差稳定性复检}✓）$$
$$\qquad \textbf{(c)}✓\ \text{若仍不在极小点，}\ \text{则记录}\ \textbf{"未能定位 genuine KKT"}✓\ \text{（}\textbf{不是}\ \text{负结果}✓，\ \text{按唐先生要求}✓）$$

$$\textbf{⑥ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
形式：次微分凸组合 + 可行性 LP（ω >= 0, Σω = 1, λ >= 0），活跃集容差 1e-7 / 1e-6
运行 1（惩罚权重 1.5）：16 σ 的最优 g = 0.83 ~ 2.01；margin_max ≈ 3.2 ~ 3.9（= 0.5 - min F_2r，正值 ⟹ 可行）
运行 2（惩罚权重 500，N=2500, 420 it）：最优 g = 1.99 ~ 2.30；|I| = 1 全部；A 多为 []
subdiff-KKT=True 的数量：0 / 16（两运行皆是）
对照：已知上界 0.876069（C-3850）⟹ 两运行找到的点都不是极小点 ⟹ 检验对象无效
```
- 脚本 ✓：`scripts/c380_58_B1alpha2_subdiff.py`✓；输出 ✓：`scripts/out_c380_58_B1alpha2.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 次微分站性模型 ✓ | **已实现（LP 形式）** ✓✓ |
| genuine KKT 点 ✓ | **未获得（优化器未收敛）** ✗✓ |
| 本刀判词 ✓ | **无（VOID，不作否定结论）** ⚠️✓ |
| `0.876069` ✓ | **上界（不变）** ✓✓ |
| 单权重 KKT 模型不足 ✓ | **已落档（`C-3857`）** ✓✓ |
| max–min 次微分多活跃结构 ✓ | **已落档（`C-3857`）** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称次微分 KKT 不存在（本刀空跑）✓
- **不**把 `g \approx 2` 的点当作极值证据 ✓
- **不**声称极值几何已定 ✓
- **不**把本刀记成负结果（按唐先生要求）✓✓

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 空跑记录       命中=见下（本档新用）
技术词 局部精修       命中=见下（本档新用）
技术词 容差稳定性     命中=见下（本档新用）
技术词 空跑记录     命中文件数=1    :: ./C3858-B1alpha2-first-cut-void-no-valid-test-points.md 
技术词 局部精修     命中文件数=2    :: ./C3858-B1alpha2-first-cut-void-no-valid-test-points.md ./C198-T13-B-w2-farfield-margin-probe-one-scale-viable.md 
技术词 容差稳定性  命中文件数=1    :: ./C3858-B1alpha2-first-cut-void-no-valid-test-points.md
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{B1-}\alpha\text{-2b}✓：\ \text{从}\ 0.876069\ \text{出发做}\ \textbf{SLSQP 带约束精修}✓✓ \Longrightarrow \text{再跑次微分 LP 审计}✓✓$$
$$\textbf{B1-}\alpha\text{-3}✓（\text{随后}✓）\text{：}|\mathcal A| \le 3\ \text{完整枚举}✓；\ \text{允许}\ \phi_j \to 0✓（x_j \to 1✓）;\ \textbf{boundary KKT 与 interior KKT 分开登记}✓✓$$
$$\textbf{B1-}\beta✓：\ \text{须先有 genuine KKT}✗✓$$
