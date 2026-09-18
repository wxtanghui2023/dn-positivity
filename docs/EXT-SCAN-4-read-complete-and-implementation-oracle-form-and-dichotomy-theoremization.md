已查地图（**先查后写**）：`EXT-SCAN-2/3`（bootstrap 方法论精读与三条结论）、`CEILING-AUDIT-3`（对偶证书）、`V316`／`V185`（67.2%／0.6818）、`V188` §2、`POS1`、`V248`、`C-122` 链 A。**本档新增输入**：`external_refs/` 四份 PDF（`2501.18711` 62 页／`0807.0004` 49 页／`1502.02033` 34 页／`2104.09518` navigator），并**已读 `0807.0004` 第 26–49 页**（核心）与 `2501.18711` 第 1–26 页；`2104.09518` 抽取未命中（标 `[未读成]`）。关键词回查：`二分定理化`＝0、`族上符号定泛函`＝0、`截断外校验`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:01「先读完，再实施」⟹ **(一) 读毕**：`0807.0004` 给出 bootstrap 的**原始二分**（逐字 `(5.12)/(5.13)`）＋**严格性的真正所在**（`\textbf{截断外校验}`）；`2501.18711` 给出 navigator 的**符号约定**（`\text{positive}\Rightarrow\text{无解}`）⟹ 它是**启发式，不是严格性所在** ✓✓；**(二) 实施**：写出我方问题的 **oracle 形式**（族／方程／正性／问题四要素）✓✓ 并指出**唯一有力目标**＝**把 `0.6818` 从"经验天花板"升级为\ \textbf{二分定理}**（仿 `(5.12)/(5.13)`：临界值＝"族上符号定泛函是否存在"的翻转点）✓✓

FREEZE-ACK: 本档即冻结期内的外部精读与实施设计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **读毕记录（RRTV 二分／navigator 符号约定／截断外校验）＋ oracle 形式与"二分定理化"实施目标** —— 关系 = 外部精读与实施设计，非新机制
D1: 0

# EXT-SCAN-4 · **读毕 ＋ 实施：oracle 形式与"二分定理化"**

> **时间**：2026-09-18 23:01 唐先生：**「先读完，再实施」** ✓

---

## §0 结论（先行）

$$\textbf{(一) 读毕}：\text{bootstrap 的严格性所在＝}\textbf{截断外的校验};\ \text{navigator 是}\ \textbf{启发式}✓✓$$
$$\textbf{(二) 实施}：\text{我方问题的}\ \textbf{oracle 形式} \text{四要素};\ \text{唯一有力目标＝}\textbf{把}\ 0.6818\ \text{升级为}\ \textbf{二分定理}✓✓$$

---

## §1 ⭐ `0807.0004`（RRTV 2008）第 26–49 页：**原始二分**（逐字）

$$\boxed{\Delta_{\min}>\Delta_c \iff \text{there IS a functional }\Lambda\ \text{such that }\Lambda(F_{d,\Delta,l})>0\ \forall \Delta,l\in\Sigma(\Delta_{\min})}\quad(5.12)✓✓$$
$$\boxed{\Delta_{\min}<\Delta_c \iff \text{there is }\textbf{NO}\ \text{functional }\Lambda\ \text{such that }\Lambda(F_{d,\Delta,l})\ge0\ \forall\Delta,l\in\Sigma(\Delta_{\min})}\quad(5.13)✓✓$$
$$\qquad \Longrightarrow ⭐\ \textbf{临界值＝"族上符号定泛函是否存在"的翻转点}✓✓$$
$$\textbf{无穷的来源（逐字，三处）}：\text{"there are infinitely many spins }l\text{; for each spin }l\ \text{the dimension }\Delta\ \text{can be arbitrary large; the dimension }\Delta\ \textbf{varies continuously}\text{"}✓$$
$$\textbf{截断与}\ \varepsilon：\text{"we truncate to a trial set ... linear programming ... }\textbf{do not work for strict inequalities}\text{"} \Longrightarrow \text{强化为}\ \Lambda\ge\varepsilon\quad(5.15)✓$$
$$\qquad ⭐⭐\ \textbf{严格性的真正所在（逐字）}：\text{"to claim that indeed}\ \Delta_{\min}>\Delta_c\text{, we have to }\textbf{check that the found }\Lambda\ \textbf{does not violate (5.12) for }\Delta,l\ \textbf{not included in the trial set}\text{"}✓✓$$
$$\qquad \Longrightarrow \text{即}\ \textbf{截断外校验}（\text{对}\ \textbf{连续族} \text{的其余部分）；由附录 D 的}\ \textbf{渐近}（\Delta\gg l^2\ \text{时符号随}\ n\ \text{的奇偶翻转}）完成✓✓$$

## §2 `2501.18711` 后段：navigator 是**启发式**（逐字）

$$\text{"the }\textbf{Navigator}\ \text{implements a quasi-Newton search for finding allowed points ... one constructs a function that is }\textbf{positive when there is no bootstrap solution, and negative where there is a solution}（\text{at a given derivative-order}）\text{"}✓✓$$
$$\qquad \text{两种：}\textbf{GFF navigator}（\text{把广义自由场解按系数加入}）／\textbf{sigma navigator}（\text{自动}）;\ \text{再用}\ \textbf{BFGS} \text{走到最小值}✓$$
$$\qquad ⚠️\ \text{另有}\ \textbf{Skydive}（\text{不逐点全解 SDP，加快移动}）;\ \text{原档自述"difficult to use"}✓$$
$$\Longrightarrow ⭐\ \text{navigator}\ \textbf{不是严格性所在} \Longrightarrow \textbf{严格性只在}\ §1\ \text{的泛函证书＋截断外校验}✓✓$$
$$\qquad \text{输出语（逐字）}：\text{"scaling dimensions }\textbf{rigorously confined to the intervals}\text{"}✓$$

## §3 `1502.02033`（SDPB）：严格性＝对偶证书

$$\text{"a new }\textbf{rigorous high-precision bound}\text{ ...}\ \Delta_\sigma=0.518151(6)";\ \text{PMP／primal-dual／duality gap／Slater／内点法}✓$$
$$\qquad \Longrightarrow \text{与}\ \text{`CEILING-AUDIT-3`}\ \text{的"对偶证书"}\ \textbf{同名同物}✓✓$$
$$\qquad ⚠️\ \text{`2104.09518`（navigator 原论文）}\ \textbf{抽取未命中} \Longrightarrow \text{标}\ `[未读成]` \text{（不影响 §2 的结论，因其内容已在 }2501.18711\ \text{中被转述）}✓$$

## §4 ⭐ 实施（一）：我方问题的 **oracle 形式**

$$\textbf{族（Family）}：\text{测试函数族}\ \{\varphi_\alpha\},\ \alpha\ \text{＝连续参数}（\text{我方＝}\textbf{尺度／支撑参数}）✓$$
$$\textbf{方程（Equations）}：\text{显式公式（算术↔谱一致性）＋ 泛函方程}（＝\text{crossing symmetry 的对应物}）✓$$
$$\textbf{正性（Positivity）}：⚠️\ \textbf{缺失} \Longrightarrow \text{现用代理＝}\text{`V316` 的 rank–trace／惯性不等式}（\text{一个}\ \textbf{relaxation}）✓✓$$
$$\textbf{问题（Question）}：\text{"存在}\beta>\tfrac12+\delta\ \text{的自洽配置吗"} \Longleftrightarrow \text{"某}\ \textbf{间隙假设}\ \text{可满足吗"}✓✓$$
$$\Longrightarrow \text{我方阈值}\ 0.6818\ ＝\ \textbf{该 relaxation 的临界值}✓✓$$
$$\qquad \text{（对照 bootstrap：其}\ \Delta_c\ \text{＝}\textbf{完整正性} \text{下的临界值；正性越弱，临界值越"松"}）✓$$

## §5 ⭐⭐ 实施（二）：唯一有力目标＝把 `0.6818` **二分定理化**

$$\textbf{仿}\ (5.12)/(5.13)\ \text{写我方版本}：$$
$$\boxed{\ p^{*}>\text{某值} \iff \text{存在族上符号定泛函（在我方正性代理类内）}\ }✓✓$$
$$\qquad \Longrightarrow \text{若成立}：\text{则}\ 0.6818\ \text{不再是"经验天花板"，而是}\ \textbf{一个二分定理的临界值}✓✓$$
$$\qquad \qquad \text{价值}：\text{① 把"饱和"变成}\ \textbf{定理};\ \text{② 明确"抬界需要什么"}（\text{换更强的正性类}）;\ \text{③ 与文献同型，}\ \textbf{可对外}✓✓$$
$$\textbf{需要什么（诚实清单）}：$$
$$\qquad \text{(a)}\ \text{把我方}\ \text{`V316`}\ \text{的泛函／惯性论证写成}\ \textbf{族上的符号定陈述}（\text{含}\ \textbf{连续参数}）✓$$
$$\qquad \text{(b)}\ \text{给出}\ \textbf{截断外校验} \text{的对应物}（\text{bootstrap 靠}\ \Delta\to\infty\ \text{渐近};\ \text{我方须给出我方族的}\ \textbf{边界渐近}）✓✓$$
$$\qquad \text{(c)}\ \text{证明二分}\ \textbf{双向}（\text{文献中}\ (5.12)\ \text{方向需截断外校验；}\ (5.13)\ \text{方向较易}）✓$$
$$\qquad ⚠️\ \text{我方劣势：}\text{(b) 的"边界渐近"}\ \text{在我方受}\ \text{`V188` §2 饱和} \text{限制，}\ \text{这正是}\ \text{`bandwidth\le1`}⟹ \textbf{同一处}✓✓$$
$$\qquad \text{(d)}\ ⚠️\ \text{且依}\ \text{`C-116`}：\text{该目标是}\ \textbf{定理目标}，\ \text{不是归纳结论}✓$$

## §6 边界与回查

- ⚠️ §1 `(5.12)/(5.13)` 与"截断外校验"句为**逐字抽取**（`[抽取级]`）；附录 D 的渐近仅读到摘要句 ✓
- ⚠️ §2 navigator 描述为 `2501.18711` 的**转述**（其原论文 `2104.09518` `[未读成]`）✓
- ⚠️ §4／§5 为**本档设计**（非定理；尚未实施到可陈述的形式）✓
- **不声称**可完成二分定理；**不声称** RH ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:0x）`[纪律]`（先跑后写）

```
技术词 二分定理化        命中文件数=0  ⟹ 本档新增
技术词 族上符号定泛函     命中文件数=0  ⟹ 本档新增
技术词 截断外校验        命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
