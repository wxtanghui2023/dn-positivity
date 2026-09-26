已查地图：已跑 scripts/prework_map_check.sh 剖面刚性 N4 饱和 三角形 ⟹ 执行自 EXTL-CENSUS-2026-09-26 档；本档为**剖面消元验证＋缺陷/三阶恒等式＋饱和引理（6/6）**（唐先生 2026-09-26 16:30 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = t=N₄ 单参数族、缺陷恒等式 defect=N₄、三阶恒等式 T₃=38+N₄、饱和引理 T₃=#三角形（6 实例）、第四阶约束的定位
D1: 1（新增：**t-族验证** ✓✓；**defect=N₄ 与 T₃=38+N₄** ✓✓；**饱和引理 6/6** ✓✓）

# PROFILE-2026-09-26

## §0 ⭐ **消元验证（唐先生 ✓ 确认正确 ✓）**

```
$$\text{假设 }b\le4:\quad N_1+N_2+N_3+N_4=512,\quad N_2+2N_3+3N_4=108,\quad N_3+3N_4=38$$
$$\Longrightarrow\ \boxed{N_3=38-3t,\quad N_2=32+3t,\quad N_1=442-t,\quad t:=N_4}\ ✓✓$$
$$\text{合法 }t\in\{0,\dots,12\}\ (\text{由 }N_3\ge0\ ✓);\quad \textbf{两码均 }t=10\ \Longrightarrow\ (432,62,8,10)\ ✓✓$$
$$\text{派生（全部随 }t\ \text{线性）}:\quad A_{\le2}\equiv73\ (\textbf{与 }t\ \text{无关}\ ✓),\quad T_3=38+t,\quad \mathrm{defect}=t$$
$$\Longrightarrow\ \boxed{\text{剖面刚性}\iff N_4=10\iff T_3=48\iff \mathrm{defect}=10}\ ✓✓\ (\text{四种等价写法}\ ✓)$$
$$

## §1 ⭐ 两个恒等式（实算 ✓✓）

```
$$\textbf{① 缺陷恒等式}: Q_2=(E-Q)+\mathrm{defect}\ (Q:=\#\{b\ge2\})\ \Longrightarrow\ \mathbf{defect}=t=N_4\ ✓✓$$
$$\qquad\text{两码实测}: \mathrm{defect}=10=N_4\ ✓\ (\text{defect}=\sum_{k\ge4}\binom{k-2}2N_k\ ✓)$$
$$\textbf{② 三阶恒等式}: T_3:=\sum_x\binom{b(x)}3=N_3+4N_4+(\text{高阶项})\ \Longrightarrow\ \mathbf{T_3}=38+t\ ✓✓$$
$$\qquad\text{两码实测}: T_3=48=38+10\ ✓$$
$$

## §2 ⭐⭐⭐ **饱和引理（本轮主成果，6/6 ✓✓✓）**

```
$$\boxed{\textbf{饱和引理}:\quad M=K(n,1)\ \Longrightarrow\ T_3=\#\text{三角形}(G_{\le2}(C))\ }\ ✓✓$$
$$\begin{array}{c|c|c|c|c}
\text{极值实例} & T_3 & \#\text{三角形} & \text{饱和} & \text{截面}\\
\hline
(4,4)=K & 0 & 0 & \checkmark & \max b=2\\
(5,7)=K & 2 & 2 & \checkmark & \max b=3\\
(6,12)=K\ \text{类#1} & 4 & 4 & \checkmark & \max b=3\\
(6,12)=K\ \text{类#2} & 4 & 4 & \checkmark & \max b=3\\
(9,62)=K\ \text{码#1} & \mathbf{48} & \mathbf{48} & \checkmark & \max b=4\\
(9,62)=K\ \text{码#2} & \mathbf{48} & \mathbf{48} & \checkmark & \max b=4\\
\end{array}$$
$$\textbf{几何含义}: \text{每个"两两距离}\le2\text{"的三元组都\textbf{恰有一个共同覆盖点}}\ ✓\ (\text{由三球交}\le1\ \text{点}\ ✓)$$
$$\qquad\Longrightarrow\ \text{三元组}\leftrightarrow\text{共同点 是\textbf{双射}}\ ✓✓\ \Longrightarrow\ T_3=\#\text{三角形 是"无浪费覆盖"的体现}\ ✓$$
$$

## §3 第四阶约束的定位（诚实 ✓）

```
$$\text{由饱和}: 38+t=T_3=\#\text{三角形}\ \Longrightarrow\ \boxed{N_4=10\iff\#\text{三角形}=48}\ ✓$$
$$\qquad\text{故第四个约束} = \textbf{对 }G_{\le2}\ \text{三角形数的上界}\ \#\text{tri}\le48\ ✗\ (\textbf{尚未证}\ ⚠️)$$
$$\text{已试无效}: \text{Kruskal–Katona 型界（}m=73\ \text{边}\Rightarrow\#\text{tri}\ \text{上限}\approx220\ \text{太弱}\ ✗);\ L2\ (N_{\ge3}\le54\ \text{太弱}\ ✗)$$
$$\text{可用结构}: G_1=\text{距离 1 图是\textbf{二部图}}\ ✓\ \Longrightarrow\ \textbf{无 (1,1,1) 三角形}\ ✓\ (\text{三角形至少含一条距离-2 边}\ ✓)$$
$$

## §4 与表示层的关系（关键对照 ✓✓）

```
$$\text{刚性（跨表示 ✓✓）}: E=108\ ✓,\ Q_2=38\ ✓,\ T_3=48\ ✓,\ \#\text{tri}=48\ ✓,\ (N_j)\ ✓,\ A_{\le2}=73\ ✓,\ d_{\max}=3\ ✓$$
$$\text{表示层（分叉 ✗）}: A_1\in\{7,26\}\ ✗,\ A_2\in\{66,47\}\ ✗,\ I\in\{6,27\}\ ✗,\ S\in\{126,67\}\ ✗,\ S_q\in\{0,3\}\ ✗$$
$$\Longrightarrow\ \boxed{\text{剖面的刚性\textbf{等价于} }\#\text{三角形数的刚性}\ ✓✓\ ——\ \text{而三角形数是\textbf{纯图论量}}\ ✓\ (\text{不依赖表示}\ ✓)}$$
$$

## §5 状态与下一刀

```
$$\textbf{靶心已精确化}: \text{证 }M=K(9,1)\Rightarrow\#\text{三角形}(G_{\le2})\le48\ ✓\ (\text{或先证饱和引理一般情形}\ ✓)$$
$$\text{下一刀（推荐）}: \text{① 先证\textbf{饱和引理}（无浪费覆盖};\ \text{可能由"三球交唯一"}\ ⇒\ \text{每三角形恰收费一次}\ ✓)$$
$$\qquad\text{② 对三角形按边型分类 }(2,2,2)/(1,1,2)/(1,2,2)\ \text{并按型计数上界}\ ✓$$
$$\qquad\text{③ switching 探针}: \text{记录 }(\Delta N_4,\Delta N_3,\Delta N_2,\Delta N_1)\ ✓\ (\text{两已知码已知同一 class}\ [L]\ ✓)$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §6 边界（诚实标注）

- §0–§2 为**实算**（6 实例全部验证覆盖 ✓）；§2 的饱和为**6/6 观察** ⟹ 登记为**引理（猜想级）** ⚠️（非已证 ✓）
- §3 明确标注**第四阶约束未找到** ✗（不虚报 ✓）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：单参数族、缺陷恒等式、饱和引理
- **档案已有（引用，不列为提出）**：剖面、三角形、T₃
