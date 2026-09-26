已查地图：已跑 scripts/prework_map_check.sh W 超图 G2 高阶交 T3 excess ⟹ 执行自 FAILSET-2026-09-26 档；本档为**覆盖者超图结构测量**（唐先生 2026-09-26 14:44 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = W 超图（G₂ 图、singleton–2-edge 关联、高阶交）的结构测量与候选路线判定
D1: 1（新增：**G₂ 非载体（判死 #1）✗**；**高阶交是 excess 载体（#3 证实）✓✓**；**新不等式对 Q_2≤T₃≤((n+1)/3)Q_2** ✓✓）

# WHYPER-2026-09-26

## §0 对象（唐先生 ✓）

```
$$\mathcal W:=\{W(x):\ x\in\mathbb F_2^n\}\ \text{—— 全局多重超图}\ ✓;\qquad \text{minimality}:\ \forall c\ \exists x:\ W(x)=\{c\}\ ✓$$
$$\text{目标形态}: \Phi(\mathcal W)\ge f(E)\ \text{且}\ \Phi(\mathcal W)\le g(A_{\le2})\ ✓;\ \text{若 }f(E)>g(2)\ \text{则打穿 P1}\ ✓$$
```

## §1 测量结果（我方 ✓）

```
$$\begin{array}{c|c|c|c|c|c|c|c|c}
(n,M) & E & Q_2 & N_1 & N_2 & N_{\ge3} & T_3 & |E(G_2)| & \text{孤立点}\\
\hline
(4,4)=K & 4 & 0 & 12 & 4 & 0 & 0 & 2 & 0\\
(4,5)>K & 9 & 1..3 & 8..9 & 6..7 & 1 & 1..4 & 5..6 & 0..1\\
(5,7)=K & 10 & 2 & 24 & 6 & 2 & 2 & 6 & 1\\
(5,8)>K & 16 & 4..8 & 19..24 & 0..11 & 2..8 & 4..8 & 0..10 & 0..8\\
(9,64)\ \text{我方} & 128 & 64 & 448 & \mathbf{0} & 64 & 64 & \mathbf{0} & \mathbf{64}\\
\end{array}$$
$$

## §2 ⛔ **#1 判死：G₂（2-edge 图）不是载体** ✗✓

```
$$\text{(9,64)}:\ |E(G_2)|=\mathbf{0}\ ✗,\ \text{全部 64 个码字在 }G_2\ \text{中\textbf{孤立}}\ ✗,\ \text{而 }Q_2=64>0\ ✓$$
$$\text{(5,7)}:\ |E(G_2)|=6\ \text{极小}\ ✓,\ \text{孤立点 1 个}\ ✓$$
$$\Longrightarrow\ \boxed{\text{"}e(c,c')>0\text{" 构成的 2-edge 图\textbf{不携带 excess}}\ ✗}\ ——\ \text{唐先生 #1（G}_2\ \text{的度/孤立点/连通分支）\textbf{问错了对象}}\ ✗✓$$
$$\qquad\text{注}: \text{这\textbf{不}否定 }\sum e=N_2\ \text{恒等式（已验 ✓），只否定 }G_2\ \text{作为\textbf{P1 载体}}\ ✓$$
```

## §3 ✅ **#3 证实：excess 活在\textbf{高阶交}里** ✓✓

```
$$\text{(9,64)}:\ \text{64 个 singleton 边 }+\ \mathbf{64\ \text{个 3-边}}\ ✓\ (b\equiv\{1,3\}\ ✓),\ T_3=64=Q_2\ ✓✓$$
$$\text{(5,7)}:\ N_{\ge3}=2,\ T_3=2=Q_2\ ✓$$
$$\Longrightarrow\ \boxed{\text{excess 的载体是 }|W(x)|\ge3\ \text{的高阶块}}\ ✓✓\ ——\ \text{与唐先生 #3 判断\textbf{完全一致}}\ ✓✓$$
$$\text{结构}: Q_2=\sum_{|T|\ge3}\binom{|T|-1}{2}N_T\ ✓;\quad T_3=\sum_{|T|\ge3}\binom{|T|}{3}N_T\ ✓$$
```

## §4 ✅ **新不等式对（我方推导＋数据核验 ✓✓）**

```
$$\text{逐块}: \binom{k}{3}=\frac{k}{3}\binom{k-1}{2}\ ✓;\quad 3\le k=|W(x)|\le n+1\ ✓$$
$$\Longrightarrow\ \boxed{Q_2\ \le\ T_3\ \le\ \frac{n+1}{3}Q_2}\ ✓✓$$
$$\textbf{数据}: (5,7):\ 2\le2\le3.33\ ✓;\quad (9,64):\ 64\le64\le213\ ✓;\quad (4,5):\ 3\le4\le5\ ✓$$
$$\qquad \textbf{系统核验}: \text{n=4}(M=4,5,6)+\text{n=5}(M=7)+\text{n=9}(M=64)\ \text{共 }\mathbf{100}\ \text{样本，}\textbf{0 违反}\ ✓✓$$
$$\text{意义}: \text{二阶 excess}(Q_2)\ \text{被\textbf{三次共点三元组数} }T_3\ \text{上下夹住}\ ✓\ ——\ \text{三阶量首次与 }E\ \text{结构对接}\ ✓$$
$$\qquad\text{（但仍为夹逼，未给 }Q_2\ \text{上界}\ ✗）$$
```

## §5 另一条被否的尝试（诚实记录 ✓）

```
$$\text{试}: 3T_3=\sum_{\text{pairs}}t(\text{pair})\le 2A_{\le2}(n-1)\ \Longrightarrow\ T_3\le\tfrac{2}{3}(n-1)A_{\le2}$$
$$\qquad\text{配合 }2A_{\le2}=E+Q_2\ \text{与 }Q_2\le T_3:\ \ Q_2\le\tfrac13(n-1)(E+Q_2)\ \Longrightarrow\ Q_2\le\frac{(n-1)E}{4-n}\ ✗\ (\text{n}\ge4\ \text{时无意义}\ ✗)$$
$$\Longrightarrow\ \textbf{该路线空转}\ ✗✓\ (\text{与 }ZB\ \text{批同样的失败模式：界太松}\ ✗)$$
```

## §6 观测到的其他结构（备用 ✓）

```
$$\textbf{O1}: \text{minimal 码上 }p(c)\ge1\ ✓;\ M>K\ \text{时出现 }p(c)=0\ ✗\ \Longrightarrow\ p\ge1\ \text{是\textbf{极值特异}}\ ✓\ (\text{承前，再确认}\ ✓)$$
$$\textbf{O2}: (9,64):\ p(c)=7\ \forall c\ \Longrightarrow\ N_1=M\cdot7=448\ ✓\ (\text{均匀情况}\ ✓)$$
$$\textbf{O3}: (5,7):\ \text{六个码字 }(p,\deg)=(3,2)\ ✓\ +\ \text{一个 }(p,\deg)=(6,0)\ ✓\ \Longrightarrow\ p\ \text{与 }\deg\ \text{似有补偿}\ \⚠️\ (\text{样本太小，不作数}\ ✗)$$
$$\textbf{O4}: \text{distinct }T=\{6\ (n{=}4,M{=}4),\ 15\ (n{=}5,M{=}7),\ 128\ (n{=}9,M{=}64)\}\ ✓\ ——\ (9,64):\ 64+64=128\ ✓\ (\text{全为 singleton 与 3-边}\ ✓)$$
```

## §7 状态与下一刀

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{入口 3 已启动}\ ✓;\quad \text{其中 #1 判死}\ ✗,\ \textbf{#3 证实}\ ✓✓$$
$$\text{下一刀候选}: \text{① 以 3-边（}|W(x)|=3\text{）与 4-边为对象测交结构}\ ✓;\ \text{② 追 }T_3\ \text{的几何上界（}T_3=\#\text{共点三元组}\ ⚠️);\ \text{③ 用 }Q_2\le T_3\ \text{转攻 }T_3\ \text{上界}\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓$$
```

## §8 边界（诚实标注）

- §1–§6 全部为**数值测量** ✓（n=4 全枚举 ✓、n=5 全枚举 ✓、n=9 我方构造 ✓）
- §4 的不等式对为**我方推导＋数据核验** ✓；§5 为**失败尝试记录** ✓（未掩盖 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 覆盖者超图测量 命中文件数=1    :: ./WHYPER-2026-09-26-coverer-hypergraph-measurements-and-G2-refutation.md 
技术词 共点三元组数 命中文件数=1    :: ./WHYPER-2026-09-26-coverer-hypergraph-measurements-and-G2-refutation.md 
技术词 高阶交载体  命中文件数=1    :: ./WHYPER-2026-09-26-coverer-hypergraph-measurements-and-G2-refutation.md 
技术词 2-边图判死   命中文件数=1    :: ./WHYPER-2026-09-26-coverer-hypergraph-measurements-and-G2-refutation.md
```
- **本档新增**（命中数=1 但**仅本档自身 = self-hit** ⟹ 扣自引后 = 0 ✓）：覆盖者超图测量、共点三元组数、高阶交载体、2-边图判死
- **档案已有（引用，不列为提出）**：minimality、excess、私有点
