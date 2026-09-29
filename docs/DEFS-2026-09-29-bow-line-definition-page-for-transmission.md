# DEFS-2026-09-29 — **定义页（可转交）**：BOW-107 线所用全部对象与已验证恒等式

**已查地图**：`scripts/prework_map_check.sh "定义页" "S3" "球excess" "delta"` ⟹ 命中 223（多为 RH 线 $\delta_T$／$S3$ 无关项）⟹ 本档对象 $S_3,\delta_{N[v]},a_j$ **属 B 线已登记对象**（`INV2`／`INV3`／`AUDIT-29j`），**非新案** ✓

D0: 本档对象 = **档案已有**（$\mu,e,a_j,\delta,A_k,P,H,E$——无新数学对象 ✓）
D1: 0（产出 = **一页定义表 ＋ $M{=}106$ 之账 ＋ 缺口之精确形式** ⚠️✓）

> 空间 B｜非 C 号｜唐先生 23:57「把含 INV2/INV3、$\delta(v),a_1(v),a_2(v)$ 的那一页给出，不凭符号猜」｜**不主张任何新值**（V290）

## §1 对象（**μ／闭邻域框架**，$C\subseteq Q_{10}$，覆盖半径 1，$|C|=M$）

$$S_1(x)=\{x\oplus e_i\}\ (10\ \text{点}),\qquad N[x]=\{x\}\cup S_1(x)\ (11\ \text{点})$$
$$\mu(x):=|C\cap N[x]|\ \ge1\ (\textbf{闭}球计数);\qquad e(x):=\mu(x)-1\ \ge0\ (\textbf{点} excess)$$
$$a_j(v):=\#\{c\in C:\ d(c,v)=j\}\ (j=0,1,2,\dots);\qquad \bigl(x\notin C\Rightarrow \mu(x)=a_1(x)\bigr)$$
$$\boxed{\delta(v):=\delta_{N[v]}:=\sum_{y\in N[v]}\bigl(\mu(y)-1\bigr)}\quad(\textbf{球} excess\ =\ 点 excess 在闭邻域上求和)$$
$$E:=\sum_x e(x)=(n+1)M-2^n;\qquad A_k:=\#\{\{c,c'\}\subseteq C:\ d=k\};\qquad N_{\le2}:=A_1+A_2$$
$$P:=\sum_{y\in C}\binom{a_1(y)}2;\qquad H:=\sum_{x\notin C}\binom{\mu(x)}2$$
**约定警示（三次同型纠错后固化）**：$\delta$ 之对象是**球 excess**，**不是** $\mu(v)-1$ ✗；且 $\delta$ 非"开启/闭合"可随意替换（$r_q{=}2t_q$ 仅在**开**邻域成立 ✓）。

## §2 已验证恒等式（**逐条实测**）

$$\textbf{(I1)}\ \boxed{\delta_{N[v]}=11\cdot\mathbf1_{v\in C}+2a_1(v)+2a_2(v)-11}\quad(\text{120-码 }1024/1024\ \text{零不符}\ ✓✓)$$
$$\qquad\Longrightarrow\ v\notin C:\ \delta=2(a_1+a_2)-11\ (\textbf{必奇});\quad v\in C:\ \delta=2(a_1+a_2)\ (\textbf{必偶})\ \text{（自动，无需结构）}$$
$$\textbf{(I2)}\ \sum_{x\in V}\sum_{y\in N[x]}e(y)=11E\quad(3256=11\cdot296\ ✓);\qquad \textbf{(I3)}\ \sum_{x\in C}\sum_{y\in N[x]}e(y)=4N_{\le2}\quad(796=4\cdot199\ ✓)$$
$$\textbf{(I4)}\ \sum_{v\notin C}\delta_{N[v]}=11E-4N_{\le2}\quad(2460\ ✓)$$
$$\textbf{(I5) }F9:\ 2A_2=H+P;\qquad \textbf{(I6) }F3:\ \sum_x\binom{\mu(x)}2=2N_{\le2}$$
$$\textbf{(I7)}\ E+\sum_x e(x)^2=4N_{\le2}\quad(292=4\cdot73\ ✓,\ 796=4\cdot199\ ✓)$$
$$\textbf{(I8)}\ \sum_{x\notin C}\bigl(\mu(x)-1\bigr)=E-2A_1\quad(\Longrightarrow \equiv E\equiv0\bmod2\ \text{恒为偶}\ ✓)$$

## §3 $M{=}106$ 时之账（**本档顺手算好**）

$$E=142;\quad N_{\le2}=A_1+A_2=71+\text{(松弛)};\quad A_1\le59;\quad \#\{v\notin C\}=918$$
$$S_3:=\{v\notin C:\ \delta(v)\ge3\}=\{v\notin C:\ a_1(v)+a_2(v)\ge7\},\qquad m:=|S_3|$$
$$\textbf{INV2 之等价形式}:\quad v\notin C\Rightarrow a_1(v)+a_2(v)\ \ge\ 6\ (\iff\delta\ge1)\ ✓$$
$$\sum_{v\notin C}\delta\ \overset{(I1)}{=}\ 2\underbrace{\sum_{v\notin C}(a_1+a_2)}_{=55M-2N_{\le2}}-11\cdot918\ =\ 121M-11264-4N_{\le2}\ \overset{M=106}{=}\ \boxed{1562-4N_{\le2}}$$
$$\textbf{用 }\delta\ge1\ (\text{每点})\ \text{与}\ \delta\ge3\ (\text{仅}S_3\text{ 内}):\quad 1562-4N_{\le2}\ \ge\ 918+2m\ \Longrightarrow\ \boxed{m\ \le\ 322-2N_{\le2}}$$
$$\qquad\Longrightarrow\ \textbf{这条记账只给\ 上界}\ \left(N_{\le2}{=}71\Rightarrow m\le180\ \text{，与 }AUDIT\text{-}29j\ \text{逐字一致}\right)\ ✗$$

## §4 缺口之**精确形式**（供下一刀）

$$\text{要证\ \textbf{下界}\ }|S_3|\ge N:\ \text{记账法不足（§3 只给上界）} \Longrightarrow \text{须用\ \textbf{局部相容性}（而非总量）}$$
$$\text{可用之局部材料}:\ (a)\ \delta\ \text{之三分类（}v\in C\Rightarrow\text{偶};\ v\notin C\Rightarrow\text{奇）};\ (b)\ \text{每点 }\delta=2(a_1{+}a_2){-}11\ \text{之\ 5 点局部结构};\ (c)\ a_1,a_2\ \text{之逐点容量（}\le10,\le45\text{）}$$
$$\text{目标形式}:\ \exists\ \text{局部构型}\ \mathcal L\Rightarrow \#\{v:\delta(v)\ge3\}\ \text{增长} \Longrightarrow |S_3|\ \ge\ 322-2N_{\le2}\ \text{之\ 反向界}$$
