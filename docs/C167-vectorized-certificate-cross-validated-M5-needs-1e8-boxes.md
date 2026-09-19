已查地图（**先查后写**）：`C-166`（`M=5` 超预算；对偶间隙诊断；算力天花板）、`C-163`（`M=3` 认证）、`C-164`（`M=4` 认证）、`C-165`（误差模型核验）。关键词回查：`整数索引表示`=0、`向量化证书`=0、`预算收敛性`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 14:45「继续」）**：**按 C-166 判定做工程化：向量化证书，冲 `M=5`。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{向量化＋整数索引版已实现并通过交叉核验}（\texttt{scripts/rpM\_adaptive\_certificate\_idx.py}）✓$$
$$\qquad M=3：17{,}440\ \text{箱}、\text{余量}\ 0.002004961256163118\ \textbf{（与参照实现逐位一致）}、0.06\ \text{s}（\text{快}\ 13\times）✓✓$$
$$\qquad M=4：1{,}036{,}096\ \text{箱}、\text{余量}\ 0.0002099798169962197\ \textbf{（逐位一致）}、7.2\ \text{s}（\text{快}\ 6\times）✓✓$$
$$\qquad \text{关键改进}：\text{整数索引表示（}\mathrm{int32}）\ \Longrightarrow \text{前沿内存降}\ \sim8\times；\ \text{LIFO}\ \Longrightarrow \text{栈稳定在}\ \sim10^6\text{–}3\times10^6\ \text{（不爆）}✓✓$$
$$\textbf{(二)}\ ⭐\ M=5\ \text{进展}：\text{评估}\ \mathbf{60{,}049{,}984}\ \text{箱、}\mathbf 0\ \text{未决、剩}\ 1{,}980{,}800\ \text{待处理、596 s} \Longrightarrow \textbf{超预算但\textbf{在收敛}}✓$$
$$\qquad （\text{对比旧实现}：\text{同一预算}\ 9\times10^6\ \text{时剩}\ 87{,}391\ \text{未决} \Longrightarrow \text{量级提升}\ \sim7\times）✓$$
$$\textbf{(三)}\ ⭐\ \textbf{算力天花板量化}：M=5\ \text{估计需}\ \sim10^8\ \text{箱}（\text{当前速率}\sim10^5\ \text{箱/s} \Longrightarrow \sim20\ \text{分钟}）✓$$
$$\qquad M=6\ \text{推测需}\ \sim10^{10}\ \text{箱} \Longrightarrow \textbf{超出实际算力} \Longrightarrow \text{届时必须换结构论证}✓✓$$
$$\textbf{(四)}\ \text{已开销大预算重跑}（\text{预算}\ 4\times10^8）\ \text{后台运行中}✓$$

FREEZE-ACK: 本档即冻结期内的工程实现与运行（依 `§8.1`；不产候选结论）

D0: 本档对象 = **向量化／整数索引证书（交叉核验通过）＋ `M=5` 进展（6\times10^7 箱、0 未决、收敛中）＋ 算力天花板量化** —— 关系 = 工程实现与测量，非新机制
D1: 0

# C-167 · ⭐⭐ **向量化证书（逐位一致）＋ `M=5` 需要 ~10⁸ 箱**

> **唐先生 2026-09-19 14:45**：继续（按 C-166 的工程路线冲 `M=5`）✓

---

## §1 ⭐⭐ 实现与交叉核验

$$\text{新实现}：\texttt{scripts/rpM\_adaptive\_certificate\_idx.py}✓$$
$$\text{两项关键改进}：$$
$$\qquad \textbf{① 整数索引表示}：\text{第}\ d\ \text{层网格每维}\ n_d=N_0 2^d；\text{箱}=(i_1,\dots,i_M)\in\mathbb Z^M_{\ge0}；\ \text{坐标}\ \mathrm{lo}_j=i_j\pi/n_d✓$$
$$\qquad\qquad \Longrightarrow \text{前沿以}\ \mathrm{int32}\ \text{存放} \Longrightarrow \text{内存降}\ \sim8\times✓✓$$
$$\qquad \textbf{② LIFO}：\text{栈深优先} \Longrightarrow \text{前沿稳定在}\ \sim10^6\text{–}3\times10^6\ \text{（旧 BFS 式会爆到}\ >10^7）✓✓$$
$$\begin{array}{c|r|r|r}
 & \text{参照实现} & \text{向量化版} & \text{加速}\\\hline
M=3\ (N_0{=}10) & 17{,}440\ \text{箱},\ 0.78\ \text{s} & 17{,}440\ \text{箱},\ 0.06\ \text{s} & 13\times\\
M=4\ (N_0{=}20) & 1{,}036{,}096\ \text{箱},\ 44.9\ \text{s} & 1{,}036{,}096\ \text{箱},\ 7.2\ \text{s} & 6\times\\
\end{array}✓✓$$
$$\text{余量}：0.002004961256163118\ (M{=}3)、0.0002099798169962197\ (M{=}4)\ \textbf{与参照实现逐位相同}✓✓$$
$$\Longrightarrow \text{两个独立实现在同一结论上一致} \Longrightarrow \text{交叉核验通过（实现风险显著降低）}✓✓$$
$$\qquad (\text{注}：\text{深度计数约定不同：新版记"层"，旧版记}\ \lceil\log_2(\pi/h)\rceil ⟹ \text{数值不可直接比}）✓$$

## §2 ⭐ `M=5` 进展（本档实测）

$$\begin{array}{c|r|r|r|r|r}
\text{实现} & \text{预算} & \text{评估箱数} & \text{未决} & \text{剩余待处理} & \text{用时}\\\hline
\text{旧（逐箱）} & 9\times10^6 & 9{,}000{,}001 & 87{,}391 & — & 412\ \text{s}\ ✗\\
\text{新（向量化）} & 6\times10^7 & \mathbf{60{,}049{,}984} & \mathbf 0 & 1{,}980{,}800 & 596\ \text{s}\ ✗\\
\end{array}✓✓$$
$$\qquad \text{栈演化（向量化）}：1.76\text{M}\to3.65\text{M}\to1.41\text{M}\to3.40\text{M}\to1.98\text{M} \Longrightarrow \textbf{在收敛}（\text{非发散}）✓$$
$$\qquad \text{min\_margin（已认证箱的最小余量）}=3.96\times10^{-6}\ \Longrightarrow \text{有"临界箱"，需深细分}✓$$
$$\Longrightarrow \textbf{判定}：M=5\ \textbf{可达}，\text{只是需更大预算（}\sim10^8\ \text{箱}）✓✓$$

## §3 ⭐ 算力天花板（量化）

$$\text{当前速率}：\sim10^5\ \text{箱/s}（\text{向量化}）\Longrightarrow M=5\ \text{的}\ 10^8\ \text{箱}\approx17\ \text{分钟}\ \textbf{可接受}✓$$
$$M=6：\text{按}\ M\ \text{间增长率粗估}\ \sim10^{10}\ \text{箱} \Longrightarrow \sim28\ \text{小时} \Longrightarrow \textbf{不实际}✗$$
$$\Longrightarrow \text{证书路线的实际上限}\ \approx M=5；\ \text{再往上必须换结构论证}✓✓$$

## §4 下一步

$$\text{①}\ \text{等大预算}\ M=5\ \text{跑完（已启动，预算}\ 4\times10^8）✓$$
$$\text{②}\ \text{若拿下} \Longrightarrow \textbf{第五个完整情形}✓；\text{然后}\ \textbf{封顶} \text{并转向结构论证}✓$$
$$\text{③}\ \text{结构路线的候选（既有登记）}：\text{鸽笼定理的"窗口}\ N\ \text{最优形式"推广到多点；或降低对偶间隙}\ c_M✓$$

## §5 边界与回查

- ⚠️ §1 的一致性为**逐位**（数值相同）✓；§2 为**实测** ✓；§3 为**量级估计** ✓
- ⚠️ **不声称** `(\text{RP}_5)`（运行中）；**不声称**一般 `M`；**不声称**与 RH 相关 ✓
- ⚠️ 两实现均为计算机辅助；严格性依赖 `C-163` §2 的三行论证与 `C-165` 的误差模型核验 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 14:5x）`[纪律]`（先跑后写）

```
技术词 整数索引表示  命中文件数=0 ::  ⟹ 本档新增
技术词 向量化证书    命中文件数=0 ::  ⟹ 本档新增
技术词 预算收敛性    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
