已查地图：已跑 scripts/prework_map_check.sh private neighbor shadow Q_priv A2+3A3 Φ ⟹ 执行自 N6CENSUS-2026-09-26 档；本档为**shadow 路线的判别性淘汰 ＋ 一条真局部引理**（唐先生 2026-09-26 12:41 指令）；未跑 solver ✓。
D0: 本档对象 = private-neighbor shadow 量（Q_priv、A2+3A3、Φ）的极值特异性判定
D1: 1（新增：shadow 路线被判别性淘汰 ✗；新增可证局部引理 Φ(c)≥0 ✓）

# SHADOW-2026-09-26

## §1 符号与定义（按唐先生口径 ✓）

```
$$q(c)=\#\{i:\ b(c+e_i)=1\}\ ✓\ (\text{c 的 private 邻点数}\ ✓);\quad \varepsilon_c=\mathbf 1_{b(c)=1}\ ✓;\quad r(c)=\varepsilon_c+q(c)\ ✓$$
$$Q_{\mathrm{priv}}=\sum_c\binom{q(c)}2\ ✓;\quad \Phi(c)=d_2(c)+3d_3(c)-\binom{q(c)}2\ ✓\ (\text{唐先生候选局部量}\ ✓)$$
$$

## §2 判别结果：**shadow 量不是极值特异** ✗（按唐先生既定判据 ✓）

```
$$\begin{array}{c|c|c|c}
(n,M) & \text{钉住量}\ ✓ & \textbf{shadow 量} & \text{判定}\\
\hline
(4,4)=K & Q{=}0,A_{\le2}{=}2,N_1{=}12 & Q_{\mathrm{priv}}\in\{4,12\}\ ✗,\ A_{23}{=}A_2{+}3A_3\in\{6,14\}\ ✗,\ q_{\max}\in\{2,3\}\ ✗,\ \varepsilon\in\{0,4\}\ ✗ & \textbf{淘汰}\ ✗\\
(5,7)=K & Q{=}2,A_{\le2}{=}6,N_1{=}24 & Q_{\mathrm{priv}}{=}22\ ✓,\ A_{23}{=}34\ ✓ & \text{唯一轨道，无判别力}\ ✗\\
(6,12)=K & Q{=}4,A_{\le2}{=}12,N_1{=}48 & Q_{\mathrm{priv}}\in\{36,54\}\ ✗,\ A_{23}\in\{86,120\}\ ✗,\ q_{\max}\in\{3,4\}\ ✗,\ \varepsilon\in\{6,12\}\ ✗ & \textbf{淘汰}\ ✗\\
\end{array}$$
$$\boxed{\Longrightarrow\ \text{private-neighbor shadow 层（含 }q(c),Q_{\mathrm{priv}},A_2{+}3A_3,\Phi\text{）\textbf{不是极值特异性载体}}\ ✗\ \text{—— 干净淘汰}\ ✓✓}$$
$$\text{（唐先生判据原文}: \text{"如果没有，则这个 shadow 路线可以很干净地淘汰"}\ ✓\ \text{—— 现予执行}\ ✓）$$
$$

## §3 ⚠️ 方法警示：corr = ±1.0000 是**二值伪相关** ✗

```
$$n=4,M=4:\ \text{corr}(Q_{\mathrm{priv}},A_{23})=-1.0000\ ✗\quad n=6,M=12:\ -1.0000\ ✗$$
$$\textbf{原因}: \text{两者各自只有 2 个取值}\ ⟹\ \text{相关系数必为 }\pm1\ ✓\ \text{——\textbf{零信息}}\ ✗$$
$$\Longrightarrow\ \textbf{禁止}把此类"完美相关"当作机制证据\ ✗\ (\text{本轮险些误读}\ ✓)$$
$$

## §4 ✅ 意外收获：一条**真局部引理**（可证 ✓）

```
$$\boxed{\Phi(c)=d_2(c)+3d_3(c)-\binom{q(c)}2\ \ge\ 0}\ ✓✓\ (\text{全部测试无一为负}\ ✓;\ \text{最小值取 }0,1,2,3,\ldots\ ✗\ \text{即紧})\ ✓$$
$$\textbf{证明（我方推导 ✓）}: \text{设 }i,j\in S_c\ (S_c=\{i:b(c+e_i)=1\}\ ✓)\ \Longrightarrow\ e_i,e_j\notin C\ ✓$$
$$\quad\text{shadow }z_{ij}=c+e_i+e_j\ \text{须被某码字覆盖}\ ✓;\ \text{覆盖者与 }c\ \text{的距离}\in\{1,2,3\}\ ✓,\ \text{距离 1 者为 }e_i,e_j\ ✗\ \text{已排除}\ ✓$$
$$\quad\Longrightarrow\ \text{只能由距离 2 或 3 的码字覆盖}\ ✓;\quad d_2\ \text{型码字每个至多覆盖 1 个 }z_{ij}\ ✓;\ d_3\ \text{型至多覆盖 3 个}\ ✓$$
$$\quad\Longrightarrow\ \binom{q(c)}2\ \le\ d_2^{\subseteq S_c}(c)+3d_3^{\subseteq S_c}(c)\ \le\ d_2(c)+3d_3(c)\ ✓\ \Longrightarrow\ \Phi(c)\ge0\ ✓✓$$
$$\text{（此引理\textbf{不}极值特异}\ ✗\ ——\ \text{对一切码成立}\ ✓\ \text{—— 故是\textbf{资产}而非桥}\ ✓）$$
$$

## §5 结论与状态

```
$$\text{幸存（极值特异 ✓）}: Q,\ A_{\le2},\ N_1,\ \text{剖面}\ (N_j)\ ✗\ \text{—— 与 §2 的淘汰不冲突}\ ✓$$
$$\text{被淘汰（本轮 ✓）}: \text{shadow 层（}q,Q_{\mathrm{priv}},A_{23},\Phi\text{）}\ ✗;\ \text{更早}: P\ (\text{=}N_1\ \text{换皮}\ ✓),\ P_2\ ✗$$
$$\textbf{桥仍未打通}\ ✗:\ M=K\Longrightarrow A_{\le2}\ \text{钉住}\ ✗\ (\text{已知工具}: r(c)\ge1\ \text{仅给 }N_1\ge M\ ✓;\ \text{二次非负性仅给 }A_{\le2}\ge E/2\ ✓)$$
$$\textbf{119 保持 UNKNOWN}\ ✓;\ \textbf{不外推}\ ✗$$
$$

## 【技术词回查】（定稿前逐字输出）

```
技术词 private 邻点影子 命中文件数=0    :: 
技术词 局部影子不等式 命中文件数=0    :: 
技术词 极值特异性淘汰 命中文件数=0    :: 
技术词 二值伪相关  命中文件数=0    ::
```

- **本档新增**（命中数=0）：局部影子不等式、极值特异性淘汰、二值伪相关
- **档案已有（引用，不列为提出）**：—
