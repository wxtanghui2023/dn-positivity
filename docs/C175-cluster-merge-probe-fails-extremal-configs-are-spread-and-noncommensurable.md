已查地图（**先查后写**）：`C-174`（周期门槛；直接检验）、`C-173`（闭式阈值）、`C-172`（近似周期引理）、`C-147`/`C-149`/`C-150`（二阶矩与计数路线之死）、`C-159`（鸽笼定理）、`C-144`（Case A）。关键词回查：`结构性不可约`=0、`分散非通约`=0、`簇并归约`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 17:56「继续」）**：**① 收尾（`C-173` 更正指针 ＋ 论文骨架并入）② 换结构性思路的第一步：可行性探测。**
**结论（先行）**：$$\textbf{(一)}\ \text{收尾已完成（提交}\ \mathtt{410ccb5}\text{）}：\text{`C-173`}\ §8\ \text{更正指针}；\text{论文骨架并入第}\ 9/10\ \text{条贡献、§5′、周期门槛、OP-6、附录 B}✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{簇并归约（cluster-merge）}\ \textbf{同样够不到最硬点}✗：$$
$$\qquad \text{数值极小点的最小相邻间距}：M=2\to30.0^\circ,\ 3\to36.9^\circ,\ 4\to16.1^\circ,\ 5\to10.7^\circ \Longrightarrow \textbf{点很分散}✗$$
$$\qquad \text{簇并的误差预算}：\text{误差}\ \lesssim M\cdot K\cdot\delta=5M^2\delta \Longrightarrow \text{需}\ \delta\ll\tfrac1{5M^2}（M=5\ \text{时}\ \delta\ll0.46^\circ）✗$$
$$\qquad \Longrightarrow \text{观测到的}\ 10.7^\circ\ \text{比所需紧度粗}\ \sim23\ \text{倍} \Longrightarrow \textbf{该路线亦不可行}✗$$
$$\textbf{(三)}\ ⭐⭐\ \textbf{统一结构性刻画（本档核心）}：\text{极值配置}\ \textbf{分散且非通约} \Longrightarrow$$
$$\qquad \text{周期化}✗（\text{`C-174`}）；\ \text{簇并}✗（\text{本档}）；\ \text{计数/测度}✗（\text{`C-144`} §4、\text{`C-150`}）；\ \text{二阶矩/聚合}✗（\text{`C-147`}、\text{`C-149`}）✓$$
$$\qquad \Longrightarrow \text{四条"归约式"路线}\ \textbf{因同一结构原因全部失效}✓✓\ \Longrightarrow \text{成功论证必须是}\ \textbf{真正的多点、分散型不等式}✓$$

FREEZE-ACK: 本档即冻结期内的探测与结构刻画（依 `§8.1`；不产候选结论）

D0: 本档对象 = **簇并可行性探测 ＋ 四条路线失效的统一结构刻画 ＋ 收尾登记** —— 关系 = 探测、刻画与收尾，非新机制
D1: 0

# C-175 · ⭐⭐ **极值配置"分散且非通约"—— 四条归约路线同一原因失效**

> **唐先生 2026-09-19 17:56**：继续 ✓

---

## §1 收尾（已完成）

$$\text{`C-173`}\ \text{追加}\ §8\ \text{\textbf{更正·C-174} 指针}：\text{① "只差}\ 0.8\%\text{"撤回}；\text{② 充分条件过强} \Longrightarrow \text{阈值放宽到}\ \varepsilon\le\sim51^\circ；\text{③ 限制项＝周期门槛}✓$$
$$\text{论文骨架（}\mathtt{papers/rpM-window-cosines/OUTLINE.md}\text{）并入}：$$
$$\qquad \text{贡献第}\ 9\ \text{条（近似周期单调性引理）、第}\ 10\ \text{条（一维极小极大}\ \kappa_N(\lambda)\ \text{与闭式}\ 2-\sqrt3\text{）}✓$$
$$\qquad §4\ \text{新增"§5′-新节"；§6 新增\textbf{周期门槛}（}\varepsilon(P)\ge93^\circ\ \forall P\le6\text{）}；\text{OP-6；附录 B 补}\ \kappa_3(\lambda)\ \text{表}✓$$
$$\text{提交}\ \mathtt{410ccb5}；\text{两档自检：}\textbf{0 括号不平衡／0 TAB／0 控制符}✓$$

## §2 ⚠️ 实践教训复现：`\t`／`\v` 转义坑（本档又踩一次）

$$\text{用}\ \texttt{heredoc}\ \text{写 LaTeX 块时}：\texttt{\textbackslash text}\to\textbf{TAB}✗，\ \texttt{\textbackslash varepsilon}\to\textbf{VT}+\texttt{arepsilon}✗✗$$
$$\qquad \Longrightarrow \text{由"紧签名"检查捉到}（\text{与前次}\ 382\ \text{处同类}）✓；\text{整块改为}\ \textbf{纯文本重写}✓$$
$$\qquad ⚠️\ \text{纪律再确认}：\text{含 LaTeX 的写入}\ \textbf{必须} \text{用}\ \texttt{r'''...'''}\ \text{或 bash 引号 heredoc}✓$$

## §3 ⚠️ 簇并归约的可行性探测（`(乙)` 第一步）

$$\text{思路}：\text{若某簇内点足够近，可并成一点（权重＝簇大小）} \Longrightarrow \text{归约到更少点}✓$$
$$\text{探测 1（极小点是否成团）}：$$
$$\begin{array}{c|r|r|r|r}
M & \text{角（度）} & \text{最小间距} & \text{平均} & \text{成团？}\\\hline
2 & 60,\ 90 & 30.0^\circ & 30.0^\circ & 否\\
3 & 20.2,\ 76.4,\ 113.3 & 36.9^\circ & 46.5^\circ & 否\\
4 & 29.8,\ 105.2,\ 121.2,\ 171.8 & 16.1^\circ & 47.3^\circ & 否\\
5 & 51.5,\ 63.4,\ 90.1,\ 162.3,\ 173.0 & 10.7^\circ & 30.4^\circ & 否\\
\end{array}✓$$
$$\Longrightarrow \textbf{极小点分散}（最小间距\ 16^\circ\text{–}37^\circ）✗，\ \text{只有}\ M\ \text{大时才略紧（}10.7^\circ）✓$$
$$\text{探测 2（误差预算）}：\text{簇并误差}\ \lesssim M\cdot K\cdot\delta（K=5M） \Longrightarrow \text{需}\ \delta\ll\tfrac1{5M^2}✓$$
$$\qquad M=5：\delta\ll\tfrac1{125}=0.008\ \text{rad}=0.46^\circ✗\qquad \text{观测}\ 10.7^\circ\ \text{比所需粗}\ \mathbf{\sim23\ \text{倍}}✗$$
$$\Longrightarrow \textbf{簇并归约同样够不到最硬点}✗$$

## §4 ⭐⭐ 统一结构性刻画（本档核心产出）

$$\text{极值配置}\ \textbf{分散且非通约}：\text{① 在全部准入}\ P\ \text{上}\ \varepsilon(P)\ge93^\circ（\text{`C-174`}\ §5）✓；\text{② 最小相邻间距}\ \ge10^\circ\ \text{（本档）}✓$$
$$\begin{array}{c|l|l}
\text{归约式路线} & \text{失败原因} & \text{出处}\\\hline
\text{周期化（小}\ P\text{）} & \text{无可用}\ P：\varepsilon(P)\ge93^\circ & \text{`C-174`}\\
\text{簇并（少点）} & \text{点分散：最小间距}\ge10^\circ，\text{需}\ \delta\ll0.46^\circ & \text{本档}\\
\text{计数/测度} & n_k\ \text{平均}\ \approx M/3<\tfrac{2M}3+\tfrac13 & \text{`C-144`}\ §4、\text{`C-150`}\\
\text{二阶矩/聚合} & \text{交叉项}\ M^2\log K\ \text{吃掉全部余量} & \text{`C-147`}、\text{`C-149`}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{四条"归约式"路线因同一结构原因（极值分散＋非通约）全部失效}✓✓$$
$$\qquad \Longrightarrow \textbf{成功论证必须是真正的"多点、分散型"不等式} \Longrightarrow \text{这正是}\ \text{OP-3（联合靶子）} \text{的形态}✓✓$$

## §5 判定与建议

$$\textbf{①}\ \text{论文范围（按唐先生 15:32 决定）}：M\le5\ \text{严格}＋\text{全}\ M\ \text{部分结果}＋§6\ \text{困难分析}✓\ —— \textbf{四路失败的统一刻画使 §6 更强}✓✓$$
$$\textbf{②}\ \text{若继续攻一般}\ M：\text{唯一未死的形态是}\ \textbf{联合靶子（OP-3）}，\ \text{且现在知道}\ \textbf{为何} \text{归约类必失败}✓$$
$$\textbf{③}\ \text{不投入}：\text{任何"把多点问题归约成少点/周期问题"的路线（已有四次失败先例）}✗$$

## §6 边界与回查

- ⚠️ §3 的探测为**数值**（极小点来自启发式优化；`M=5` 的配置为早期数值结果，可能非全局极小）✓
- ⚠️ §4 的四路失败**均有档可依**，但统一刻画本身是**结构判断**（非定理）✓
- ⚠️ **不声称** `(\text{RP}_M)` 一般成立；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档（`C-173`／骨架为追加更正指针与并入）✓
- **纪律**：先查后判（R-1 ✓）、**先跑后写** ✓；本档复现一次转义坑并已修正 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 18:0x）`[纪律]`（先跑后写）

```
技术词 结构性不可约  命中文件数=0 ::  ⟹ 本档新增
技术词 分散非通约   命中文件数=0 ::  ⟹ 本档新增
技术词 簇并归约    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
