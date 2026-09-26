已查地图：已跑 scripts/prework_map_check.sh 三角形 分类 μ 三阶矩 型分解 ⟹ 执行自 PROFILE-2026-09-26 档；本档为**三角形局部全分类＋T₃=#三角形普适定理＋型分解分叉（矩级刚性）**（唐先生 2026-09-26 16:33 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 三角形型分类（含 (1,2,2) 不可能性）、μ(τ) 分类、T₃=#三角形 的普适性、型分解分叉发现
D1: 1（新增：**(1,2,2) 被奇偶排除** ✓✓；**μ(τ)=1 局部定理** ✓✓；**T₃=#三角形 普适定理** ✓✓；**型分解分叉 ⟹ 矩级刚性** ✓✓）

# TRI-2026-09-26

## §1 ⭐ **三角形局部全分类（Hamming 几何 ✓）**

```
$$\text{三点两两距离}\le2 \Longrightarrow \text{F}_2\ \text{奇偶约束}: d(u,v)+d(v,w)\equiv d(u,w)\ (\mathrm{mod}\ 2)\ ✓$$
$$\begin{array}{c|c|c}
\text{型} & \text{是否存在} & \mu(\tau)=|B_1(u)\cap B_1(v)\cap B_1(w)|\\
\hline
(1,1,1) & \mathbf{不可能}\ ✗\ (\text{超立方体二部}\ ✓) & -\\
(1,2,2) & \mathbf{不可能}\ ✗\ (\text{奇偶}: 1+2=3\not\equiv2\ ✓✓) & -\\
(1,1,2) & \text{存在}\ ✓ & \mathbf{1}\ \text{（45/45 实测}\ ✓✓) \\
(2,2,2) & \text{存在}\ ✓ & \mathbf{1}\ \text{（60/60 实测}\ ✓✓) \\
\end{array}$$
$$\text{枚举}: \text{F}_2^6\ \text{内 105 个三元组（mod 平移+置换）}\ \Longrightarrow\ \textbf{μ=1 全部成立}\ ✓✓$$
$$\textbf{两情形两行证明}\ ✓: (2,2,2)\Rightarrow v,w\ \text{权 2 且交 1}\ \Rightarrow v=e_1{+}e_2,\ w=e_1{+}e_3\ \Rightarrow \cap=\{e_1\}\ ✓;\ (1,1,2)\Rightarrow \{e_1\}\ ✓$$
$$

## §2 ⭐⭐ **μ 分类（回答唐先生的关键提醒 ✓）**

```
$$\textbf{唐先生的提醒}: \text{"三球交}\le1\ \text{点"}\ne\text{"三球交}\ge1\ \text{点"}\ ✓\ ——\ \textbf{正确}\ ✓$$
$$\text{实测（14 个码，全部三元组）}: \mu\in\{0,\ 1\}\ \text{恒成立}\ ✓✓\ (\textbf{μ≥2 个数 = 0}\ ✓\ \text{全部实例}\ ✓)$$
$$\Longrightarrow\ \mu(\tau)=1\ \iff\ \text{两两距离}\le2\ ✓✓;\quad \mu(\tau)=0\ \text{否则}\ ✓\ (\text{某对距离}\ge3\Rightarrow B_1\ \text{交空}\ ✓)$$
$$\Longrightarrow\ \textbf{非空性来自\textbf{几何}，不需要覆盖性，也不需要极值性}\ ✓✓\ (\text{唐先生的 \S1 猜想被确认且更强}\ ✓)$$
$$

## §3 ⭐⭐⭐ **普适定理：T₃ = #三角形（对任意二元码 ✓✓）**

```
$$\textbf{证明（两行 ✓）}:\quad T_3=\sum_x\binom{b(x)}3=\sum_{\tau\subseteq C,|\tau|=3}\mu(\tau)\ \overset{\S2}{=}\ \#\{\tau:\text{两两}\le2\}=\#\triangle(G_{\le2}(C))\ ✓✓$$
$$\textbf{实测（14 码全覆盖 ✓✓）}:\ \text{极值}\ 6\ \text{码}\ ✓;\ \text{非极值覆盖码}\ 7\ \text{个}\ ✓;\ \text{任意非覆盖码}\ 5\ \text{个}\ ✓\ \Longrightarrow\ \textbf{恒等 14/14}\ ✓✓$$
$$\text{（注意：非极值/非覆盖码也成立}\ \Longrightarrow\ \textbf{该恒等式与最优性无关}\ ✗\ ✓\ ——\ \text{修正我此前的"极值饱和"框架}\ ⚠️)$$
$$

## §4 ⭐⭐⭐ **剖面刚性 = 三阶矩刚性（精确化 ✓✓）**

```
$$\text{前两阶矩被}(M,E,Q_2)\ \text{钉死}\ ✓:\quad \sum_jN_j=512\ ✓;\quad \sum_jjN_j=M(n{+}1)=620\ ✓;\quad \sum_j\binom j2N_j=2A_{\le2}=146\ ✓$$
$$\text{三阶矩}: T_3=\sum_j\binom j3N_j=N_3+4N_4=38+N_4\ \Longrightarrow\ \boxed{\text{剖面刚性}\iff\textbf{三阶矩刚性}\iff\#\triangle=48}\ ✓✓$$
$$\text{第四阶矩}: \sum_j\binom j4N_j=N_4=t\ \text{（与三阶矩同参}\ ✓)$$
$$

## §5 ⭐⭐⭐ **新发现：型分解分叉，而总数刚性** ✓✓

```
$$\begin{array}{c|c|c|c}
\text{实例} & T_3=\#\triangle & (2,2,2){:}(1,1,2) & \text{共同中心}\ x\in C{:}x\notin C\\
\hline
(5,7)=K & 2 & 1{:}1 & 1{:}1\\
(6,12)=K\ \text{类#1} & 4 & 2{:}2 & 2{:}2\\
(6,12)=K\ \text{类#2} & 4 & \mathbf{4{:}0}\ ✗ & \mathbf{0{:}4}\ ✗\\
(9,62)=K\ \text{码#1} & 48 & \mathbf{42{:}6} & \mathbf{8{:}40}\\
(9,62)=K\ \text{码#2} & 48 & \mathbf{21{:}27}\ ✗ & \mathbf{34{:}14}\ ✗\\
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{刚性的只是"总数}\ T_3=48\ ✓;\ \text{型分解与中心类型\textbf{全部分叉}}\ ✗✓}$$
$$\textbf{锐利结论}: \text{剖面刚性是}\textbf{纯粹"矩级"刚性}\ ✓✓\ ——\ \text{不是结构级}\ ✗$$
$$\qquad\Longrightarrow\ \text{这解释了我们此前为何屡屡失败}\ ✗: I,\ S,\ A_1,\ A_2,\ S_q,\ \text{方阵——都是\textbf{表示/结构层}的量}\ ✗\ \text{而刚性在\textbf{矩层}}\ ✓✓$$
$$

## §6 状态与下一刀

```
$$\textbf{已证}: \text{局部 }\mu\ \text{分类}\ ✓✓;\quad T_3=\#\triangle\ \text{普适}\ ✓✓;\quad \text{剖面}\iff\text{三阶矩}\ ✓✓$$
$$\textbf{未决}: \#\triangle\le48\ ✗\ (\text{纯图论，但非 edge-count 界可及}\ ✗)$$
$$\text{下一刀（遵唐先生：不跑 solver ✓）}: \text{① 找"三角形不可复用收费"——但注意}\ \S5\ \text{说明型分解不可用}\ ✗,\ \text{只能用\textbf{总数}}$$
$$\qquad\text{② 换角度}: \text{三阶矩的上界可否由覆盖性} + \text{二阶矩给出？}\ \text{即 }T_3\le F(E,\ Q_2,\ A_{\le2},\ n)\ \text{型不等式}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1/§3/§5 为**实算+证明**（14 码全覆盖 ✓）；§3 的普适性**修正了我此前"极值专属"的框架** ⚠️（诚实记录 ✓）
- §5 的"分叉"为**两码直接对照** ✓（含 n=6 的独立例证 ✓）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 型分解分叉  命中文件数=1    :: ./TRI-2026-09-26-typography-mu-universal-identity-and-moment-level-rigidity.md 
技术词 矩级刚性     命中文件数=1    :: ./TRI-2026-09-26-typography-mu-universal-identity-and-moment-level-rigidity.md 
技术词 局部 μ 分类 命中文件数=1    :: ./TRI-2026-09-26-typography-mu-universal-identity-and-moment-level-rigidity.md
```
- **本档新增**（扣自引后 = 0，命中 1 = 仅本档自引 ✓）：型分解分叉、矩级刚性、局部 μ 分类
- **档案已有（引用，不列为提出）**：三角形、三阶矩、剖面
