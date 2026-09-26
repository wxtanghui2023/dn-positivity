已查地图：已跑 scripts/prework_map_check.sh Φ 零集 原子分解 shadow ⟹ 执行自 SHADOW-2026-09-26 档；本档为**shadow 主路线正式关闭 ＋ Φ 的可证原子分解 ＋ 按判据降级 Φ**（唐先生 2026-09-26 12:53 指令）；未跑 solver ✓。
D0: 本档对象 = Φ(c) 的非负原子分解与其零集刚性判定
D1: 1（新增：Φ 的**可证非负二原子分解** ✓；并按唐先生判据**将 Φ 由路线降级为资产** ✗）

# PHI-2026-09-26

## §1 Shadow 主路线：**NO-GO**（正式关闭 ✓）

```
$$\textbf{判定（唐先生四层口径 ✓）}: \text{private 邻点影子：无现有资产命中};\ \text{局部影子不等式：无现有资产命中};\ \text{极值特异性淘汰：成立};\ \text{二值伪相关：已识别}\ ✓$$
$$\boxed{\text{Shadow mechanism = NO-GO}}\ ✗\ (\text{术语新 ≠ 推进力}\ ✓\ \text{—— 不因术语新而扩张}\ ✓)$$
$$

## §2 ✅ **Φ 的可证非负原子分解**（本轮真收益 ✓）

```
$$\text{记 } S_c=\{i:b(c+e_i)=1\}\ ✓,\ q=|S_c|\ ✓;\ \text{pairs}={S_c\choose2}\ ✓,\ m=\binom q2\ ✓$$
$$\text{对 } w\in C\ \text{且 }d(c,w)\in\{2,3\}:\ \kappa(w)=\#\{\text{pairs }\{i,j\}:\ d(w,\ c+e_i+e_j)\le1\}\ ✓\ (\le1\ \text{当 }d{=}2;\ \le3\ \text{当 }d{=}3\ ✓)$$
$$\boxed{\Phi(c)=\underbrace{\bigl[d_2(c)+3d_3(c)-\textstyle\sum_w\kappa(w)\bigr]}_{A_1\ \text{（浪费容量）}\ \ge0}+\underbrace{\bigl[\textstyle\sum_w\kappa(w)-\binom q2\bigr]}_{A_2\ \text{（覆盖松弛）}\ \ge0}}\ ✓✓$$
$$\textbf{证明要点}: \text{① 每个 shadow 必被某个 }d(c,w)\in\{2,3\}\ \text{的码字覆盖}\ ✓\ \Longrightarrow\ \binom q2\le\sum_w\kappa(w)\ ✓\ (A_2\ge0)$$
$$\qquad\quad\ \text{② 每个 }d{=}2\ \text{码字 } \kappa\le1\ ✓,\ d{=}3\ \kappa\le3\ ✓\ \Longrightarrow\ \sum_w\kappa\le d_2+3d_3\ ✓\ (A_1\ge0)$$
$$\textbf{数值核验}: \text{全部 }4\ \text{组数据 }A_1,A_2\ \textbf{无一为负}\ ✓✓;\ \text{且 }\Phi=0\iff A_1=A_2=0\ ✓$$
$$\text{零条件含义（精确 ✓）}: \Phi(c)=0\iff\ \text{每个 }d{=}2/3\ \text{码字\textbf{满容量}}（\kappa{=}1/3）\ \text{且 每个 shadow \textbf{恰被覆盖一次且全覆盖}}\ ✓$$
$$

## §3 ⛔ **零集判定：松散 → 按判据降级 Φ** ✗

```
$$\begin{array}{c|c|c}
(n,M) & \Phi\ \text{取值分布（中心样本）} & \text{判定}\\
\hline
(4,4)=K & \{0{:}64,\ 6{:}96\}\ (160) & \text{仅 }40\%\ \text{取 }0\ ✗\\
(5,7)=K & \{0{:}320,\ 2{:}320,\ 7{:}640,\ 10{:}960\}\ (2240) & \text{仅 }14.3\%\ \text{取 }0\ ✗\\
(6,12)=K & \{3{:}130,\ 7{:}260,\ 14{:}390,\ 17{:}120\}\ (900) & \boxed{\Phi=0\ \textbf{从不出现}（0/900）}\ ✗✓\\
\end{array}$$
$$\Longrightarrow\ \textbf{零集既非强制亦非刚性}\ ✗\ (\text{且在 }n=6\ \text{极值壳上完全为空}\ ✗)$$
$$\Longrightarrow\ \text{按唐先生判据原文（"如果零条件完全松散，就立即把 Φ 也降级"）}\ ✓\ \boxed{\Phi\ \text{由\textbf{路线}降级为\textbf{资产}（局部不等式）}}\ ✗✓$$
$$

## §4 唯一漂亮的结构数据（记录 ✓，但不可外推 ✗）

```
$$\text{在 }(4,4)\ \text{与 }(5,7)\ \text{上，}\Phi=0\ \text{的中心\textbf{结构完全一致}}: (d_2,d_3,q,m)=(0,1,3,3)\ ✓$$
$$\text{即}: \text{恰好 3 个 private 邻点}\ ✓\ \text{＋ 恰好 1 个 }d{=}3\ \text{码字\textbf{完美覆盖}全部 }3\ \text{个 shadow}\ ✓\ (A_1=A_2=0\ ✓)$$
$$\text{但 }n=6\ \text{无零集}\ ✗\ \Longrightarrow\ \textbf{不可外推为机制}\ ✗\ (\text{仅作为局部型的登记}\ ✓)$$
$$

## §5 资产/淘汰台账（截至本轮 ✓）

```
$$\textbf{极值特异存活}: Q,\ A_{\le2},\ N_1,\ \text{剖面 }(N_j)\ ✓\ (\text{桥}\ M{=}K\Rightarrow A_{\le2}\ \text{仍未证}\ ✗)$$
$$\textbf{资产（真引理，非极值特异）}: \text{私有点引理}\ (L(c)=r(c)\ge1\ ✓);\ \text{奇偶引理}+P1\ ✓;\ \textbf{Φ 的原子分解}\ ✓\ (\text{本档新增}\ ✓)$$
$$\textbf{已淘汰}: P\ (\text{=}N_1\ \text{换皮});\ P_2;\ \text{n=8 三进制同余};\ \Delta\to A_{\le2}\ \text{传递};\ \textbf{shadow 路线};\ \textbf{Φ 作为路线}\ ✗$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓\ (\text{隔离保持}\ ✓)$$
$$

## §6 边界（诚实标注）

- §2 的分解为**我方推导＋数值核验** ✓（A₁,A₂ 无一为负 ✓）；§3 的分布为**实算** ✓（n=4 全枚举 ✓、n=5 M=7 全枚举 ✓、n=6 M=12 采样 75 码 ✓）
- §3 的降级决定严格依唐先生预置判据 ✓（非临场判断 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗；**未**开 n=9 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 原子分解     命中文件数=0    :: 
技术词 浪费容量     命中文件数=0    :: 
技术词 覆盖松弛     命中文件数=0    :: 
技术词 零集松散     命中文件数=0    ::
```

- **本档新增**（命中数=0）：原子分解、浪费容量、覆盖松弛、零集松散
- **档案已有（引用，不列为提出）**：—
