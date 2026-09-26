已查地图：已跑 scripts/prework_map_check.sh Δ(x) 内部几何 强制构型 ⟹ 执行自 P1LB4-2026-09-26 (incidence) 档；本档为**Δ(x) 内部几何终判 ＋ P1-LB.4 封存**（唐先生 2026-09-26 16:55 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Δ(x) 的 b 值模式、距离向量、三点两两距离、X₄ 接收者结构、封存判定
D1: 1（新增：**(3,4,4) 模式刚性两码全同** ✓✓；**度量分叉** ✗✓；**封存判定** ✓）

# P1LB4FINAL-2026-09-26

## §1 ⭐⭐⭐ **组合模式：完全刚性（两码全同 ✓✓）**

```
$$\begin{array}{c|c|c}
\text{量} & \text{码#1} & \text{码#2}\\
\hline
\Delta(x)\ \text{的 }b\ \text{值模式} & \mathbf{\{(3,4,4){:}8\}} & \mathbf{\{(3,4,4){:}8\}}\ \checkmark\checkmark\\
|\Delta(x)\cap X_3| & \{1{:}8\} & \{1{:}8\}\ \checkmark\\
X_4\ \text{接收者数} & \mathbf 4 & \mathbf 4\ \checkmark\\
\text{每接收者收到} & \{4{:}4\} & \{4{:}4\}\ \checkmark\\
H_3/H_4/\alpha/\beta & 8/16/1/4 & 8/16/1/4\ \checkmark\\
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{每个 }X_3\ \text{点恰有 1 个第二中心落 }X_3\ \text{、2 个落 }X_4}\ ✓✓\ (\text{严格刚性}\ ✓✓)$$
$$
$$

## §2 ⛔ **度量几何：分叉（无强制度量构型 ✗）**

```
$$\Delta(x)\ \text{到 }x\ \text{的距离向量}: \text{码#1}\ \mathbf{\{(2,2,2){:}8\}}\ ✓\quad\text{vs}\quad \text{码#2}\ \mathbf{\{(1,1,2){:}6,\ (2,2,2){:}2\}}\ ✗$$
$$\Delta(x)\ \text{三点两两距离}: \text{码#1}\ \{(2,2,2){:}8\}\quad\text{vs}\quad \text{码#2}\ \{(1,1,2){:}6,\ (2,2,2){:}2\}\ ✗$$
$$\Longrightarrow\ \textbf{无强制度量构型}\ ✗\ ——\ \text{组合刚性不延伸到度量层}\ ✗✓$$
$$

## §3 ✗ **计数路线不足（封存的直接理由 ✓）**

```
$$\text{由 (3,4,4) 模式}: H_4=2N_3\ ✓;\ \beta=4\ \Longrightarrow\ 2N_3\le4N_4\ \Longrightarrow\ N_3\le2N_4$$
$$\text{联立 }N_3=38-3N_4:\ 38-3N_4\le2N_4\ \Longrightarrow\ N_4\ge 7.6\ \Longrightarrow\ \boxed{N_4\ge8}\ ✗\ \textbf{不足 10}\ ✗$$
$$\text{敏感性}: \beta\le3\Rightarrow N_4\ge9\ ✗;\quad \beta\le2\Rightarrow N_4\ge9.5\Rightarrow N_4\ge10\ ✓\ ——\ \textbf{但实测 }\beta=4\ ✗$$
$$\Longrightarrow\ \textbf{计数墙定位}: \text{瓶颈是 }\beta=4\ (\text{每个 }X_4\ \text{最多收 4 个 }X_3\text{-incidence})\ ✗\ ——\ \text{且它可能已是紧的}\ ⚠️$$
$$

## §4 ✅ **封存判定（按唐先生预设判据 ✓）**

```
$$\text{预设判据}: \text{"若只产生可自由实现的局部型，则第二中心线整体封存"}\ ✓$$
$$\text{实测}: \text{① 组合模式刚性}\ ✓✓\ \text{但}\ \text{② 度量层可分叉}\ ✗\ \text{且}\ \text{③ 计数只给 }N_4\ge8\ ✗$$
$$\Longrightarrow\ \boxed{P1\text{-LB.4} = \textbf{ARCHIVED}}\ ✓\ (\text{已登记 CLOSED-ROUTES-MAP}\ ✓)$$
$$\text{同时登记}: P1\text{-LB second-center total-capacity} = \textbf{NO-GO}\ ✗\ (2A_1\le32+3N_4\ \text{不界}\ N_4\ ✓;\ A_1\ \text{无统一正下界（n=6: }A_1=0\ ✓)$$
$$
$$

## §5 保留资产（跨表示刚性层清单 ✓✓）

```
$$\text{i. }\textbf{第二中心 incidence 刚性层}\ ✓✓: (3,4,4)\ \text{模式};\ \alpha=1;\ \beta=4;\ H_3=8;\ H_4=16\ ——\ \textbf{两码全同}\ ✓✓$$
$$\text{ii. }X_3\to X_3\ \textbf{完美匹配}\ ✓✓$$
$$\text{iii. }\boxed{\sum_z p_2(z)=\sum_z\binom{b(z)}2-2A_1}\ ✓✓\ (\text{可证恒等式}\ ✓)$$
$$\text{iv. }b{=}3\ \text{点 }3/3\ \text{不同第二中心}\ ✓$$
$$\text{v. }\textbf{跨 n 反转}\ ✓✓: n=5,6:\ \Delta(X_3)\subseteq X_2\ ✗;\quad n=9:\ \Delta(X_3)\cap X_2=\varnothing\ ✓\ \Longrightarrow\ \textbf{零交叉非普适}\ ✗✓$$
$$
$$

## §6 状态（全线 ✓）

```
$$\textbf{已证}: T_3=\#K_3(G_{\le2})\ \text{普适}\ ✓✓;\ T_3\ge Q_2=38\ ✓✓;\ \Sigma p_2\ \text{恒等式}\ ✓✓;\ \text{等价链}\ ✓✓;\ \text{型分解预测 4/4}\ ✓✓$$
$$\textbf{跨表示刚性层}: \{E,\ Q_2,\ A_{\le2},\ (N_j),\ d_{\max},\ T_3,\ \#\triangle,\ \text{第二中心模式}\}\ ✓✓$$
$$\textbf{表示层分叉}: \{A_1,A_2,I,S,S_q,|V_\square|,L_\square,N_3/N_4\ \text{型分解},\ \text{度量几何}\}\ ✗$$
$$\textbf{累计否证（本条线）}: \text{局部账本},\ \Psi_2/Z_2,\ \Psi_{\rm mid},\ \text{阶梯}\sigma,\ \text{私有点复用},\ \text{球不交},\ \text{gadget 外溢},\ \text{方阵线},\ \text{影子/容量},\ \text{邻域匹配},\ \text{矩松弛},\ \text{第二中心容量},\ \text{第二中心几何}\ ✗$$
$$\textbf{靶心}: N_4\ge10\ (\iff N_3\le8\iff N_2\ge62)\ \textbf{仍未得}\ ✗;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$
$$

## §7 边界（诚实标注）

- §1–§3 为**实算**（两码 ✓）；§4 按唐先生预先设定的判据执行封存 ✓（非主观决定 ✓）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 (3,4,4) 模式   命中文件数=0    :: 
技术词 度量分叉     命中文件数=1    :: ./P1LB4FINAL-2026-09-26-delta-internal-geometry-verdict-and-archive.md 
技术词 计数墙定位  命中文件数=1    :: ./P1LB4FINAL-2026-09-26-delta-internal-geometry-verdict-and-archive.md
```
- **本档新增**（扣自引后 = 0）：(3,4,4) 模式、度量分叉、计数墙定位
- **档案已有（引用，不列为提出）**：第二中心、α、β、N₃/N₄
