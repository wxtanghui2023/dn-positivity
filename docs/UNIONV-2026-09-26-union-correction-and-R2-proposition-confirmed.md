已查地图：已跑 scripts/prework_map_check.sh 并集 交集 R2 命题 见证 ⟹ 执行自 MULTWIT-2026-09-26 档；本档为**U(v) 交集修正＋R₂ 命题确认＋失败定位**（唐先生 2026-09-26 16:11 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = U(v) 的交集公式、R₂ 命题的确认、全局式在 M≫K 处的失败根因（方阵搭档被重复计入）
D1: 1（新增：**|U(v)|=n−|∩dirs|（0 违反）** ✓✓；**R₂ 命题成立（0 违反）** ✓✓；**失败根因定位** ✓✓）

# UNIONV-2026-09-26

## §1 ⚠️→✅ **修正：|U(v)| = n − |∩dirs|**（交集，非并集 ✗）

```
$$U(v)=\bigcup_{Q\ni v}\mathrm{Sh}_Q(v)\ ✓;\quad v+e_k\in U(v)\iff\exists Q\ni v:\ k\notin\mathrm{dirs}(Q)\iff k\notin\bigcap_{Q\ni v}\mathrm{dirs}(Q)\ ✓✓$$
$$\Longrightarrow\ \boxed{|U(v)|=n-\Big|\bigcap_{Q\ni v}\mathrm{dirs}(Q)\Big|}\ ✓✓\ ——\ \textbf{不是}\ n-|\cup|\ ✗\ (\text{并集公式会\textbf{少算} }U(v)\ ✗)$$
$$\textbf{核验}: (4,6),(4,7),(4,8),(9,64)\ \text{共 78 个顶点}: 通过 78/\textbf{违反 0}\ ✓✓$$
$$

## §2 ✅ **R₂ 命题成立**（唐先生 ✓✓，0 违反 ✓✓）

```
$$\textbf{命题}: \big|\bigcap\mathrm{dirs}\big|=2\ \wedge\ d_C(v)=2\ \Longrightarrow\ U(v)\ \text{中无码字壳点（故非 private 点全为 }S\text{-见证}\ ✓)$$
$$\text{理由}: d_C(v)=2\ \Longrightarrow\ v\ \text{的码字邻居恰为两个方阵搭档}\ ✓\ \Longrightarrow\ \text{壳点若入码即为第 3 个邻居}\ ✗\ \Longrightarrow\ \text{壳点}\notin C\ ✓$$
$$\qquad\text{再由见证引理}: \text{非 private 壳点}\Longrightarrow\ \exists c',\ d(c',v)=2\ \Longrightarrow\ (y,\{v,c'\})\ \text{计入 }S\ ✓✓$$
$$\textbf{核验}: (4,7):\ 4\ \text{个顶点通过}\ ✓,\ \textbf{0 违反}\ ✓;\quad (9,64):\ 64\ \text{个通过}\ ✓,\ \textbf{0 违反}\ ✓✓$$
$$

## §3 ⛔ **全局式仍失败，但根因已定位** ✗✓

```
$$\begin{array}{c|c|c|c|c|c|c}
\text{实例} & |V_\square| & L & S & I_{\rm nw} & S+I_{\rm nw} & L\le S+I_{\rm nw}\\
\hline
(4,6) & 4 & 5 & 4 & 2 & 6 & \checkmark\\
(4,7) & 6 & 10 & 6 & 4 & 10 & \checkmark\ (\text{紧}\ ✓)\\
\mathbf{(4,8)} & 8 & \mathbf{24} & 0 & 16 & 16 & \mathbf{\✗}\ ✗✓\\
(9,64) & 64 & 0 & 0 & 0 & 0 & \checkmark\\
\end{array}$$
$$\textbf{根因（本轮定位 ✓✓）}: (4,8)\ \text{中 }|\cap\mathrm{dirs}|=0\ \text{的顶点有 3 个"码字壳点"},\ \text{但它们\textbf{恰是方阵搭档本身}}\ ✓\ (\text{并集恰 }=\{e_1,e_2,e_3\}=N_C(v)\ ✓)$$
$$\qquad\Longrightarrow\ \textbf{逐 (Q,k) 计数把方阵搭档重复计入}\ ✗\ \Longrightarrow\ \text{应改为\textbf{按顶点去重}（U(v) 中 distinct 非 private 点）}\ ✓✓$$
$$

## §4 决定性定位（诚实 ✓）

```
$$\textbf{关键观察}: \text{所有 }M=K\ \text{或极值实例}: L_\square=\mathbf{0}\ ✓\ ((9,64)\ \text{及小的 }M=K\ \text{情形}\ ✓)$$
$$\qquad\Longrightarrow\ \text{该机制在\textbf{极值壳上是空的}（vacuous）}\ ✗\ ——\ \text{全部非平凡 }L_\square\ \text{出现在 }M\gg K\ \text{的非极小码}\ ✓$$
$$\qquad\Longrightarrow\ \textbf{诚实定位}: \text{shell/}L_\square\ \text{结构是\textbf{非极小现象}}\ ✗;\ \text{对 }M=K\ \text{无直接贡献}\ ⚠️$$
$$

## §5 状态

```
$$\textbf{已立}: |U(v)|\ \text{公式}\ ✓✓;\ \text{R₂ 命题}\ ✓✓;\ \text{见证引理}\ ✓✓;\ \text{重复见证机制}\ ✓✓$$
$$\textbf{已否}: L_\square\le S+I_{\rm nw}\ \text{朴素版}\ ✗✓;\ \text{逐 (Q,k) 计数}\ ✗✓\ (\text{改为按顶点去重}\ ✓)$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad (9,62)\ \text{全码}: \text{仍未获得}\ ✗$$
$$

## §6 边界（诚实标注）

- §1/§2 为**我方证明＋核验（0 违反 ✓✓）**；§3 为**反例＋根因定位** ✓✓；§4 为**诚实定位**（机制在极值壳上为空 ✓）
- **未跑 solver** ✓；**119** 仍 **UNKNOWN** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：交集公式、搭档重复计入、按顶点去重
- **档案已有（引用，不列为提出）**：shell、见证、方阵、I_nw
