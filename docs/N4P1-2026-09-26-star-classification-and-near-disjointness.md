已查地图：已跑 scripts/prework_map_check.sh N4 星结构 相容性 不交 ⟹ 执行自 TRI-2026-09-26 档；本档为**P1 第 1-2 步：星结构分类 ＋ 两中心相容性 ＋ 近不交发现**（唐先生 2026-09-26 16:36 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = b=4 中心的星型分类（A/B 型）、型分解预测检验、中心间距离与星集交叠、"近不交"结构、可用界盘点
D1: 1（新增：**星型分类 A/B** ✓✓；**型分解预测 4/4 吻合** ✓✓；**近不交结构 40/36** ✓✓）

# N4P1-2026-09-26

## §1 ⭐ **b=4 中心的星型分类（唐先生 ✓ 确认正确 ✓）**

```
$$\text{中心 }x,\ b(x)=4\Longrightarrow S_x=C\cap B_1(x),\ |S_x|=4\ ✓;\ \text{平移 }x\mapsto0\ \text{后四点权}\le1\ ✓$$
$$\boxed{\text{A 型}\ (x\in C):\ S_x=\{x,\ x{+}e_i,\ x{+}e_j,\ x{+}e_k\}\ \text{—— 星型 3-face}\ ✓\ (d_1(x)=3\ ✓)}$$
$$\boxed{\text{B 型}\ (x\notin C):\ S_x=\{x{+}e_i\}_{i\in I},\ |I|=4\ \text{—— 四个单位向量}\ ✓\ (\text{两两距离}\ 2\ ✓)}$$
$$\text{实测}: \text{码#1}\ (A,B)=(2,8)\ ✓;\quad \text{码#2}\ (A,B)=(7,3)\ \mathbf{✗\ \text{分叉}}\ ✓\ (\text{连精细结构也不刚性}\ ✗)$$
$$

## §2 ⭐⭐ **型分解预测：4/4 完全吻合** ✓✓

```
$$\text{每个 b=4 中心贡献 4 个三角形}:\ \text{A 型}\Rightarrow 3\times(1,1,2)+1\times(2,2,2)\ ✓;\ \text{B 型}\Rightarrow 4\times(2,2,2)\ ✓$$
$$\text{每个 b=3 中心贡献 1 个}:\ x\in C\Rightarrow(1,1,2)\ ✓;\ x\notin C\Rightarrow(2,2,2)\ ✓$$
$$\Longrightarrow\ \boxed{T_{112}=3N_4^{A}+N_3^{A}\ ✓;\quad T_{222}=N_4^{A}+4N_4^{B}+N_3^{B}\ ✓}$$
$$\begin{array}{c|c|c|c}
\text{实例} & \text{预测} & \text{实测} & \text{判定}\\
\hline
(6,12)\ \text{类#1} & (0,\ 4) & \{(2,2,2){:}4\} & \checkmark\\
(6,12)\ \text{类#2} & (0,\ 4) & \{(2,2,2){:}4\} & \checkmark\\
(9,62)\ \text{码#1} & (6,\ 42) & \{(2,2,2){:}42,\ (1,1,2){:}6\} & \checkmark\\
(9,62)\ \text{码#2} & (27,\ 21) & \{(2,2,2){:}21,\ (1,1,2){:}27\} & \checkmark\\
\end{array}$$
$$\Longrightarrow\ \textbf{型分解分叉的\textbf{根源}被定位}: \text{来自}\ (N_4^{A},N_4^{B},N_3^{A},N_3^{B})\ \text{的分叉}\ ✓✓\ (\text{而非几何新现象}\ ✓)$$
$$

## §3 ⭐⭐⭐ **近不交结构（本轮主发现 ✓✓）**

```
$$\text{码#1}: 10\ \text{个星}\times4=40\ \text{次命中，仅覆盖}\ \mathbf{36}\ \text{个不同码字}\ \Longrightarrow\ \text{重叠仅}\ 40-36=4\ \text{次}\ ✓✓$$
$$\text{码#2}: \text{同样}\ 40\ \text{命中}\ /\ \mathbf{36}\ \text{不同码字}\ ✓✓\ (\textbf{两码同值}\ ✓)$$
$$\text{交叠规则（两码一致 ✓）}:\ |S_x\cap S_y|=2\ \text{当}\ d(x,y)\le2\ ✓;\quad =0\ \text{当}\ d(x,y)\ge3\ ✓✓$$
$$\text{（与球交公式一致}: |B_1(x)\cap B_1(y)|=2\ (d{=}1),\ 2n\ (d{=}2),\ 0\ (d\ge3)\ ✓;\ \text{对码集交还需压缩}\ ✓)$$
$$\text{中心间距离分布}: \text{码#1}\ \{2{:}2,3{:}10,4{:}8,5{:}9,6{:}10,7{:}2,9{:}4\}\ ✓;\ \text{码#2}\ \{1{:}1,2{:}1,3{:}3,4{:}15,5{:}15,\dots\}\ ✓$$
$$\Longrightarrow\ \boxed{\text{星集\textbf{近乎不交}（40/36）}\ ✓✓\ ——\ \text{这就是唐先生要找的"不可重复资源"的候选}\ ✓}$$
$$

## §4 ✗ **可用上界盘点（全部太弱 ✗，诚实 ✓）**

```
$$\text{① }3N_4\le E\ \Longrightarrow\ N_4\le36\ ✗$$
$$\text{② }6N_4\le2A_{\le2}\ \Longrightarrow\ N_4\le24\ ✗\ (\text{每对星内码字被至多 2 个中心共用}\ ✓)$$
$$\text{③ }3N_4^{A}\le A_1\ \Longrightarrow\ N_4^{A}\le A_1/3\ ✓\ (\text{码#1}\le2\ ✓;\ \text{码#2}\le8\ ✓)\ ——\ \text{但 }A_1\ \text{不刚性}\ ✗$$
$$\text{④ 纯不交界 }4N_4\le62\ \Longrightarrow\ N_4\le15\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{N}_4\le10\ \text{仍未得到}\ ✗\ ——\ \text{需新的几何输入}\ ⚠️}$$
$$

## §5 状态与下一刀

```
$$\textbf{已立}: \text{星型分类}\ ✓✓;\quad \text{型分解预测（4/4）}\ ✓✓;\quad \textbf{近不交（40/36，两码同值）}\ ✓✓$$
$$\textbf{已证}: T_3=\#K_3(G_{\le2})\ \text{普适}\ ✓✓;\quad \text{剖面}\iff\text{三阶矩}\iff N_4=10\ ✓✓$$
$$\text{下一刀（遵唐先生 ✓）}: \text{① 用"近不交"造 charging}: \text{星命中 40 ⟹ 4N}_4\le|\bigcup S_x|+\text{重叠}\ ✓\ \text{但需先卡 }|\cup S_x|$$
$$\qquad\text{② 关键：}\textbf{两星重叠}\Rightarrow\text{中心距离}\le2\Rightarrow\text{消耗额外的 }E/Q_2\ \text{预算}\ ——\ \text{待量化}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §6 边界（诚实标注）

- §1–§3 为**实算**（4 个码 ✓）；§4 明确标注**上界未得** ✗（不虚报 ✓）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 星型分类     命中文件数=1    :: ./N4P1-2026-09-26-star-classification-and-near-disjointness.md 
技术词 近不交结构  命中文件数=1    :: ./N4P1-2026-09-26-star-classification-and-near-disjointness.md 
技术词 型分解预测  命中文件数=1    :: ./N4P1-2026-09-26-star-classification-and-near-disjointness.md
```
- **本档新增**（扣自引后 = 0）：星型分类、近不交结构、型分解预测
- **档案已有（引用，不列为提出）**：N₄、三阶矩、三角形
