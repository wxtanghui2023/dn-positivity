已查地图：已跑 scripts/prework_map_check.sh 下界 X2 注入 Hall ⟹ 执行自 P15-2026-09-26 档；本档为**P1-LB 首刀：等价链验证 ＋ C→X₂ 接口否证**（唐先生 2026-09-26 16:45 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = 下界等价链、代数纠错、C→X₂ 二部匹配检验、n=5 反例核对
D1: 1（新增：**等价链验证** ✓✓；**C→X₂ 接口在 n=9 被否证（46/62）** ✗✓）

# P1LB-2026-09-26

## §0 ⚠️ **代数纠错（先纠后算 ✓）**

```
$$\text{唐先生写 }N_1+2N_2+3N_3+4N_4=9M=558\ ✗\ \Longrightarrow\ \textbf{正确}: \sum_j jN_j=M(n+1)=\mathbf{620}\ ✓✓$$
$$\text{实测 4 例}: n=9,M=62:\ 620\ ✓\ (E=108)\ ✓;\ n=6,M=12:\ 84\ ✓\ (E=20)\ ✓;\ n=5,M=7:\ 42\ ✓\ (E=10)\ ✓;\ n=4,M=4:\ 20\ ✓\ (E=4)\ ✓$$
$$\text{（唐先生的最终关系仍正确}\ ✓\ ——\ 仅中间量 558/46 是笔误}\ ✓)$$
$$

## §1 ⭐⭐ **等价链验证** ✓✓

```
$$\boxed{N_4\ge10\iff N_3=38-3N_4\le8\iff N_2=32+3N_4\ge\mathbf{62}=M\iff N_1=442-N_4\le432}\ ✓✓$$
$$\text{四者严格等价（由 }E=108,\ Q_2=38\ \text{与守恒式}\ ✓)$$
$$

## §2 ✗✓ **唐先生的 C→X₂ 接口：在 n=9 上被否证** ✗

```
$$X_2:=\{x:b(x)=2\},\ |X_2|=N_2=62=M\ ✓;\quad \text{自然映射}: c\mapsto B_1(c)\cap X_2\ ✓$$
$$\begin{array}{c|c|c|c}
\text{实例} & N_2\ \text{vs}\ M & \text{每码字 }b{=}2\ \text{邻域数} & \text{二部匹配}\\
\hline
(9,62)\ \text{码#1} & 62=62\ ✓ & \mathbf{\min=0},\ \max=4 & \mathbf{46/62}\ \mathbf{✗✓}\\
(9,62)\ \text{码#2} & 62=62\ ✓ & \mathbf{\min=0},\ \max=4 & \mathbf{46/62}\ \mathbf{✗✓}\\
(6,12)\ \text{类#1} & 12=12\ ✓ & \min=2,\ \max=2 & 12/12\ ✓✓\\
(6,12)\ \text{类#2} & 12=12\ ✓ & \min=2,\ \max=2 & 12/12\ ✓✓\\
(4,4)=K & 4=4\ ✓ & \min=2,\ \max=2 & 4/4\ ✓✓\\
(5,7)=K & \mathbf{6<7}\ ✗ & \min=0,\ \max=2 & 6/7\ ✗\\
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{自然注入/完美匹配在 }n=9\ \textbf{不存在}}\ ✗✓\ (\text{仅 46/62}\ ✓;\ \mathbf{16\ \text{个码字无任何 }b{=}2\ \text{邻点}}\ ✓)$$
$$\text{（有趣分叉}: n=4,6\ \text{完美匹配}\ ✓\ \text{但 }n=5,9\ \text{失败}\ ✗\ ——\ \text{与 }N_2\ge M\ \text{的成立与否同步}\ ✓)$$
$$

## §3 结论与影响（诚实 ✓）

```
$$\text{① 等价链成立}\ ✓✓\ \Longrightarrow\ \text{"}N_2\ge M\text{"是 }N_4\ge10\ \text{的合法改写}\ ✓\ (\text{但只是改写，非新信息}\ ✗)$$
$$\text{② }\textbf{但"每个码字需要一个 }b{=}2\ \text{witness"的\textbf{自然机制不存在}}\ ✗✓\ ——\ 16/62\ \text{个码字没有 }b{=}2\ \text{邻点}\ ✓$$
$$\text{③ 故下界路线需要\textbf{不同机制}}\ ⚠️\ ——\ \text{不能是邻域型注入}\ ✗$$
$$\text{④ 保留}: \text{等价链}\ ✓✓;\ \text{匹配检验方法}\ ✓;\ \text{分叉表（与 }N_2\ge M\ \text{同步）}\ ✓$$
$$

## §4 状态

```
$$\textbf{封存}: P1.3\text{--}P1.5\ \text{局部几何上界路线}\ ✓\ (\text{已登记 CLOSED-ROUTES-MAP }\S\ \text{P1-LOCAL-GEOMETRY}\ ✓)$$
$$\textbf{新主线}: P1\text{-LB}:\ N_4\ge10\iff N_3\le8\iff N_2\ge62\iff N_1\le432\ ✓✓$$
$$\qquad\text{首刀结果}: \text{自然注入路被否}\ ✗✓\ \Longrightarrow\ \text{需新机制}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §5 边界（诚实标注）

- §0–§2 为**实算**（6 例 ✓）；§2 明确标注**接口被否** ✗✓
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 下界等价链  命中文件数=1    :: ./P1LB-2026-09-26-x2-interface-refuted.md 
技术词 邻域注入否证 命中文件数=1    :: ./P1LB-2026-09-26-x2-interface-refuted.md 
技术词 匹配分叉表  命中文件数=1    :: ./P1LB-2026-09-26-x2-interface-refuted.md
```
- **本档新增**（扣自引后 = 0）：下界等价链、邻域注入否证、匹配分叉表
- **档案已有（引用，不列为提出）**：X₂、Hall、N₂
