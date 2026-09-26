已查地图：已跑 scripts/prework_map_check.sh 第二中心 刚性层 N3 稀少 ⟹ 执行自 P1LB3-2026-09-26 档；本档为**P1-LB.3 正式收束 ＋ 新刚性层发现（第二中心分布）**（唐先生 2026-09-26 16:51 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = P1-LB.3 状态锁、N₃≤8 改写、b=3 点局部结构、第二中心 b 值分布（新刚性层）
D1: 1（新增：**第二中心分布两码全同** ✓✓；**N₄≥10 ⟺ N₃≤8（三重覆盖点稀少）** ✓✓；**b=3 点全部 3 个不同第二中心** ✓✓）

# P1LB4-2026-09-26

## §0 ✅ **P1-LB.3 状态锁（唐先生裁定 ✓）**

```
$$\text{moment identities}\ \longrightarrow\ T_3\ge38\ \checkmark\ (\text{精确松弛最优}\ ✓)\ \longrightarrow\ \text{target }48\ ✗\ \longrightarrow\ \text{需 Hamming 几何/覆盖输入}\ ⚠️$$
$$\boxed{\min_{\rm moment}T_3=Q_2=\mathbf{38}}\ ✓✓\ (\text{由形式剖面 }(442,32,38,0)\ \text{达界}\ ✓)$$
$$\text{目标 }48\ \Longrightarrow\ \textbf{间隙}+10\ ✓✓;\quad T_3\ge48\ \text{与}\ N_4\ge10\ \text{同一命题两坐标}\ ✗\ (\text{换坐标给工具，非新信息}\ ✓)$$
$$

## §1 ⭐⭐ **关键改写：N₄ ≥ 10 ⟺ N₃ ≤ 8（三重覆盖点"稀少"）**

```
$$N_3=38-3N_4\ \Longrightarrow\ \boxed{N_4\ge10\iff N_3\le8}\ ✓✓$$
$$\text{而矩松弛允许 }N_3=38\ (t=0)\ \Longrightarrow\ \textbf{间隙 30}\ ✗\ \text{（比 }T_3\ \text{视角的 }10\ \text{更具冲击力}\ ✓)$$
$$\text{实测}: \text{两码均 }N_3=8,\ N_4=10\ ✓✓\ \Longrightarrow\ \textbf{最优码的三重覆盖点极少}\ ✓✓\ (\text{而四重覆盖点更多}\ ✓)$$
$$

## §2 ⭐⭐⭐ **新刚性层：第二中心 b 值分布（两码完全一致 ✓✓）**

```
$$\text{定义}: \text{对点 }x\ (b(x)\ge3)\ \text{与其球内码字对 }\{u,v\}\subset C\cap B_1(x):\ \text{第二中心} = B_1(u)\cap B_1(v)\setminus\{x\}\ ✓$$
$$\begin{array}{c|c|c}
\text{对象} & \text{码#1} & \text{码#2}\\
\hline
N_3\ \text{点类型} & \textbf{B 型 8} & \textbf{A 型 6 + B 型 2}\ ✗\ (\text{分叉}\ ✗)\\
N_3\ \text{点的第二中心 }b\text{ 值} & \mathbf{\{4{:}16,\ 3{:}8\}} & \mathbf{\{4{:}16,\ 3{:}8\}}\ \checkmark\checkmark\\
\text{每 }N_3\ \text{点的不同第二中心数} & 3/3 & 3/3\ \checkmark\\
N_4\ \text{点的第二中心 }b\text{ 值} & \mathbf{\{2{:}40,\ 3{:}16,\ 4{:}4\}} & \mathbf{\{2{:}40,\ 3{:}16,\ 4{:}4\}}\ \checkmark\checkmark\\
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{第二中心分布是新的刚性层}\ ✓✓\ ——\ \text{比剖面更细，且\textbf{跨表示不变}}\ ✓✓}$$
$$\text{（对照 }n=6: N_3\ \text{点的第二中心 }b\ \text{值} = \{2{:}12\}\ \text{全为 }b{=}2\ ✓\ ——\ \text{与 }n=9\ \text{的 }\{4,3\}\ \text{形成鲜明对比}\ ✓)$$
$$

## §3 ⭐ **两个可证/可用的局部事实**

```
$$\text{① }\textbf{每个 }b{=}3\ \text{点恰有 3 个\textbf{不同}第二中心}\ ✓✓\ (\text{两码 }8/8\ \text{均 }3/3\ ✓)\ \Longrightarrow\ \text{无重合}\ ✓$$
$$\text{② }\textbf{N}_3\ \text{点的第二中心全部落在 }b\ge3\ \text{点上}\ ✓✓\ (\text{零个落在 }b{=}2)\ ✗\ ——\ \text{而 }N_4\ \text{点有 }40\ \text{个落在 }b{=}2\ ✓$$
$$\qquad\Longrightarrow\ \text{机制候选}: \textbf{三重覆盖点被迫把第二中心"压给"高重数点}\ ⚠️\ ——\ \text{可能是 }+10\ \text{的来源}\ ✓$$
$$

## §4 状态与下一刀

```
$$\textbf{已证}: T_3=\#K_3\ \text{普适}\ ✓✓;\ T_3\ge Q_2\ ✓✓;\ \text{等价链}\ ✓✓;\ \text{型分解预测 4/4}\ ✓✓;\ p_2\ \text{分叉}\ ✓✓$$
$$\textbf{新立（本档）}: N_4\ge10\iff N_3\le8\ ✓✓;\ \textbf{第二中心分布刚性}\ ✓✓;\ b{=}3\ \text{点 }3/3\ \text{不同第二中心}\ ✓✓$$
$$\text{下一刀（遵唐先生 ✓）}: \text{研究 }b{=}3\ \text{点的第二中心如何消耗高重数容量}\ ⚠️\ \Longrightarrow\ \text{尝试 }N_3\le8\ \text{的 charging}\ ✓$$
$$\qquad\text{关键}: N_3\ \text{点的 }3N_3\ \text{个第二中心全在 }b\ge3\ \text{点}\ ✓\ \Longrightarrow\ \text{与 }N_4\ \text{互锁}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §5 边界（诚实标注）

- §1–§3 为**实算**（3 码 ✓）；§2 的"新刚性层"为**两码对照** ✓（n=3 数据点，弱于全类 ✓，但强于型分解 ✗）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 第二中心分布 命中文件数=1    :: ./P1LB4-2026-09-26-second-center-rigid-layer-new.md 
技术词 三重覆盖点稀少 命中文件数=1    :: ./P1LB4-2026-09-26-second-center-rigid-layer-new.md 
技术词 容量互锁     命中文件数=1    :: ./P1LB4-2026-09-26-second-center-rigid-layer-new.md
```
- **本档新增**（扣自引后 = 0）：第二中心分布、三重覆盖点稀少、容量互锁
- **档案已有（引用，不列为提出）**：T₃、N₃、N₄
