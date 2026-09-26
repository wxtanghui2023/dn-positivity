已查地图：已跑 scripts/prework_map_check.sh Q 通道分解 中点 Q=0 G2 ⟹ 执行自 D1CLUSTER-2026-09-26 档；本档为**精确通道分解的验证 ＋ 新的中点引理 ＋ Q=0 的 G₂ 结构实算**（唐先生 2026-09-26 13:07 指令）；未跑 solver ✓。
D0: 本档对象 = Q 的内/外通道分解、Q=0 的中点结构与 G₂ 形状
D1: 1（新增：通道分解数值锁定 ✓；**中点引理**（Q=0 时距离-2 对的中点为非码字且 b=2 且孤立）✓；Q=0 的 G₂ 形状（(4,4) 完美匹配 / (5,8) 二正则）✓）

# CHANNELS-2026-09-26

## §1 ✅ **精确通道分解**（唐先生推导，我方数值锁定 ✓✓）

```
$$\boxed{Q=Q_{\mathrm{in}}+Q_{\mathrm{out}}},\quad Q_{\mathrm{in}}=\sum_{c\in C}\binom{d_1(c)}2\ ✓,\quad Q_{\mathrm{out}}=\sum_{x\notin C}\binom{b(x)-1}2\ ✓$$
$$\textbf{数值核验（5 组数据）}: Q=Q_{\mathrm{in}}+Q_{\mathrm{out}}\ \textbf{全部成立}\ ✓✓$$
$$\text{几何意义（我方补充 ✓）}: x\notin C\ \text{时}\ C\cap B_1(x)\ \text{中码字两两距离}=2\ ✓\ \Longrightarrow\ S_x\ \text{是 }G_2\ \text{的团}\ ✓$$
$$

## §2 (Q_in, Q_out) 类型普查（**通道和刚性、通道分裂自由** ✓✓）

```
$$\begin{array}{c|c|c}
(n,M) & (Q_{\mathrm{in}},Q_{\mathrm{out}})\ \text{类型} & \text{判定}\\
\hline
(4,4)=K & \{(0,0){:}40\} & \text{双零 ✓}\\
(5,7)=K & \{(1,1){:}\textbf{320}\} & \textbf{分裂也刚性}\ ✓✓\\
(6,12)=K & \{(2,2){:}71,\ (0,4){:}19\} & \text{分裂自由 ✗，和刚性 ✓}\\
(5,8)>K & \{(0,2){:}44,(1,1){:}54,(0,0){:}34,(2,0){:}23,(1,3){:}7,(0,4){:}15\} & \text{全释放 ✗}\\
(4,5)>K & \{(3,0){:}64,(1,0){:}288,(0,1){:}192,(0,3){:}16\} & \text{全释放 ✗}\\
\end{array}$$
$$\boxed{\text{在 }M=K\ \text{处 }\textbf{Q 的和刚性}\ ✓\ \text{而}\ \textbf{通道分裂可自由}\ ✗\ (n{=}6\ \text{两种类型}\ ✓)}$$
$$\Longrightarrow\ \text{严格化此前的"距离-1 非普遍机制"}: \text{存在}\ Q_{\mathrm{in}}{=}0\ \text{但 }Q{=}4\ \text{的极值码}\ ✓\ (\text{超额全在外部团通道}\ ✓)$$
$$

## §3 ✅ **新引理：中点引理**（我方推导＋74 个 Q=0 码全验证 ✓✓）

```
$$\text{设 }Q=0\ ✓,\ \{c,c'\}\ \text{为距离-2 对}\ ✓\ (\text{中点 }=N[c]\cap N[c']\ \setminus C\ \text{的两个点}\ ✓)$$
$$\boxed{\text{(i) 两个中点均为\textbf{非码字}};\quad \text{(ii) 其中点重数恰为 }b=2\ (\text{仅被 }c,c'\ \text{覆盖});\quad \text{(iii) 除 }c,c'\ \text{外无码字距其中点为 1}}$$
$$\text{证明}: \text{若中点 }m\in C\ \text{或另有码字 }c''\ \text{距 }m\ \text{为 1}\ \Longrightarrow\ b(m)\ge3\ \Longrightarrow\ Q\ge1\ ✗\ \text{矛盾}\ ✓$$
$$\text{推论}: b(m)=2\ \text{唯一确定覆盖它的码字对}\ ✓\ \Longrightarrow\ \text{不同距离-2 对的\textbf{中点集互不相交}}\ ✓✓$$
$$\textbf{数值核验}: (4,4)\ \text{的 }40\ \text{个}\ ✓\ +\ (5,8)\ \text{的 }34\ \text{个}\ ✓\ \text{Q=0 码}\ \textbf{全部成立}\ ✓✓$$
$$

## §4 Q=0 时 G₂(C) 的形状（实算 ✓）

```
$$(4,4),\ Q=0:\ G_2\ \text{边数}=2,\ \text{度数谱}=(1,4)\ ⟹\ \textbf{完美匹配}\ ✓\ (\text{极大度}\le1\ ✓)$$
$$(5,8),\ Q=0:\ G_2\ \text{边数}=8,\ \text{度数谱}=(2,8)\ ⟹\ \textbf{二正则（若干圈之并）}\ ✓\ (\text{极大度}\le1=\text{False}\ ✗)$$
$$\qquad\text{且: 每个 }c\ \text{的距离-2 邻域内 pair 的 }|\mathrm{supp}\cap\mathrm{supp}'|\ \text{分布}=\{0{:}64\}\ ⟹\ \textbf{支撑两两不交}\ ✓✓$$
$$\text{（对称性}: n=2^m\ \text{情形 }G_2\ \text{可退化为匹配}\ ✓;\ n=5\ \text{则否}\ ✗\ ——\ \text{与 }Q^*\ \text{的 }0/nonzero\ \text{分界\textbf{一致}}\ ✓\ \text{但样本少，不可外推}\ ✗）$$
$$

## §5 状态与下一步

```
$$\textbf{桥仍未打通}\ ✗;\ \text{但目标已被两通道\textbf{精确拆开}}\ ✓: M=K\Longrightarrow Q_{\mathrm{in}}+Q_{\mathrm{out}}\ge1\ ✓$$
$$\text{要排除的配置}: \bigl[G_1(C)\ \text{是匹配}\bigr]\ \wedge\ \bigl[\forall x\notin C:\ b(x)\le2\bigr]\ ✓$$
$$\text{新的可用约束（本档）}: \text{中点引理}\ ✓\ (\text{距离-2 对消耗 2 个"孤立的 }b{=}2\ \text{非码字"}\ ✓);\ \text{通道和刚性}\ ✓$$
$$\text{下一步}: \text{① 用中点引理做\textbf{计数}（距离-2 对消耗 }2A_2\ \text{个非码字}\ ✓\ \text{与 }E\ \text{预算对表}\ ✗\ hmm）\text{② 奇 }n\ \text{专属}: \text{是否存在 matching/奇偶型障碍}\ ✗$$
$$\textbf{119 保持 UNKNOWN}\ ✓;\ \textbf{不外推}\ ✗$$
$$

## §6 边界（诚实标注）

- §1–§4 均为**我方数值核验**（n=4,5 全枚举 ✓；n=5 M=8、n=6 M=12 采样 ✓）；§3 的证明为**我方推导** ✓
- 通道分解本身是**恒等式（等价改写）** ✗ —— 其价值在**拆开目标**（§5）与**支撑中点引理**（§3）✓
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 通道分解     命中文件数=2    :: ./D1CLUSTER-2026-09-26-new-lower-bound-and-odd-n-target.md ./E76-two-channel-verdict.md 
技术词 中点引理     命中文件数=0    :: 
技术词 通道和刚性  命中文件数=0    :: 
技术词 二正则结构  命中文件数=0    ::
```

- **本档新增**（命中数=0）：中点引理、通道和刚性、二正则结构
- **档案已有（引用，不列为提出）**：通道分解
