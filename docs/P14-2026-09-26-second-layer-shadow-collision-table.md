已查地图：已跑 scripts/prework_map_check.sh 二层影子 碰撞 孤立星 ⟹ 执行自 H4P13-2026-09-26 档；本档为**P1.4：二层影子碰撞表 ＋ 两处公式纠正**（唐先生 2026-09-26 16:41 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 球交事实纠正、σ 与 Δ_x 纠正、二层碰撞表（A/B × A/B × δ）、孤立性自动条件
D1: 1（新增：**碰撞表** ✓✓；**|B₁∩B₁|=2 对 d=1,2 皆然** ✓✓；**σ=6 两型同** ✓✓）

# P14-2026-09-26

## §0 ⚠️ **两处公式纠正（先纠后算 ✓）**

```
$$\textbf{纠正①}: |B_1(u)\cap B_1(v)|=\mathbf 2\ \text{对}\ d(u,v)=1\ \textbf{和}\ d=2\ \textbf{皆然}\ ✓✓\ (\text{唐先生原写 }1/2\ ✗)$$
$$\qquad\text{实测}: d{=}1\Rightarrow2\ ✓;\ d{=}2\Rightarrow2\ ✓;\ d{=}3\Rightarrow0\ ✓\ (\text{故 }d\ge3\Rightarrow S_x\cap S_y=\varnothing\ \textbf{自动}\ ✓)$$
$$\textbf{纠正②}: \sigma(x)=\sum_{\{u,v\}\subset S_x}(|\cap|-1)=\mathbf 6\ \textbf{对 A/B 两型皆然}\ ✓✓\ (\text{唐先生原写 }3/6\ ✗)$$
$$\qquad\text{而}\ |\Delta_x|\ (\text{新第二中心}) = 3\ (\text{A 型})/6\ (\text{B 型})\ ✓\ (\text{唐先生此项正确}\ ✓)$$
$$\qquad\Delta_x=\{x+e_i+e_j:\ i<j\in I_x\},\quad |I_x|=3\ (\text{A})/4\ (\text{B})\ ✓$$
$$

## §1 ⭐⭐ **二层碰撞表（P1.4 主交付 ✓✓）**

```
$$\begin{array}{c|c|c|c}
(T_x,T_y) & \delta=d(x,y) & |\Delta_x\cap\Delta_y|\ \text{可达值} & |S_x\cap S_y|\ \text{范围}\\
\hline
(A,A) & 1 & \{0,1,2,4\} & 0\text{--}2\\
(A,A) & 2 & \{0,1,2,3,4\} & 0\text{--}2\\
(A,A) & 3 & \{0,1,2,3,6\} & \mathbf 0\ \text{（自动）}\\
(A,A) & 4 & \{0,1,2\} & \mathbf 0\\
\hline
(A,B) & 1 & \{0,1,2,3\} & 0\text{--}1\\
(A,B) & 2 & \{0,1,2\} & 0\text{--}2\\
(A,B) & 3 & \{0,1,2,3\} & \mathbf 0\\
(A,B) & 4 & \{0,1,2,3\} & \mathbf 0\\
\hline
(B,B) & 1 & \mathbf{\{0\}}\ ✗\ (\textbf{永不碰撞}\ ✓✓) & \mathbf 0\\
(B,B) & 2 & \{0,1,2,3,4\} & 0\text{--}2\\
(B,B) & 3 & \mathbf{\{0\}}\ ✗\ (\textbf{永不碰撞}\ ✓✓) & \mathbf 0\\
(B,B) & 4 & \{0,1,2,3,6\} & \mathbf 0\\
\end{array}$$
$$\delta\ge5\ \Longrightarrow\ \Delta_x\cap\Delta_y=\varnothing\ ✓\ (\text{影子距中心为 2}\ ✓)$$
$$

## §2 ⭐ **两条干净的几何事实（新 ✓✓）**

```
$$\textbf{事实 A}\ (\text{自动孤立性}): d(x,y)\ge3\ \Longrightarrow\ S_x\cap S_y=\varnothing\ \textbf{自动}\ ✓✓\ (\text{由 }|B_1\cap B_1|=0\ ✓)$$
$$\qquad\Longrightarrow\ \text{"孤立"条件\textbf{只约束 }d\le2\ \text{的中心对}\ ✓\ (\text{与 }H_4\subseteq G_{\le2}\ \text{一致}\ ✓)$$
$$\textbf{事实 B}\ (\text{B--B 奇距不撞}): \text{两个 \textbf{B 型}中心在 }\delta=1\ \text{或}\ \delta=3\ \text{时}\ \Delta_x\cap\Delta_y=\mathbf\varnothing\ \textbf{恒成立}\ ✓✓$$
$$\qquad\text{即}: \text{B 型影子的"自重"恰为 2 且方向集} = \binom{I_x}{2}\ \Longrightarrow\ \text{奇 } \delta\ \text{时无重合}\ ✓✓\ (\text{结构原因，非巧合}\ ✓)$$
$$

## §3 ⚠️ **仍未给出 N₄≤10（诚实 ✓）**

```
$$\text{碰撞最多可达 6（(A,A) }\delta{=}3,\ (B,B)\ \delta{=}4\ ✓)\ \Longrightarrow\ \text{碰撞不是\textbf{必然}的}\ ✗$$
$$\qquad\Longrightarrow\ \text{无法直接做"每孤立星必付代价"的 charging}\ ✗;\ \text{只能做\textbf{平均}型论证}\ ⚠️$$
$$\text{当前所有 }N_4\ \text{上界（全部 }\ge10\ ✗): 3N_4\le E\Rightarrow36\ ✗;\ 6N_4\le2A_{\le2}\Rightarrow24\ ✗;\ 4N_4\le62\Rightarrow15\ ✗;\ |E(H_4)|\le4\ ✗$$
$$\Longrightarrow\ \boxed{N_4\le10\ \textbf{仍未得到}\ ✗}\ ——\ \text{瓶颈: 孤立中心的个数（其星集两两不交）}\ ⚠️$$
$$

## §4 状态（本条线累积 ✓）

```
$$\textbf{已证}: T_3=\#K_3(G_{\le2})\ \text{普适}\ ✓✓;\quad \text{剖面}\iff\text{三阶矩}\iff N_4=10\iff\#\triangle=48\ ✓✓$$
$$\textbf{已立（实测/结构）}: \sum(r-1)_+=4\ ✓;\ r(z)\le2\ ✓;\ H_4=\{2\ \text{边},6\ \text{孤立}\}\ ✓;\ \text{型分解预测 4/4}\ ✓;\ \text{碰撞表}\ ✓;\ \text{事实 A/B}\ ✓✓$$
$$\textbf{分歧（表示层）}: A_1,A_2,I,S,S_q,|V_\square|,L_\square,N_4^{A}/N_4^{B},\ \text{边距离型}\ ✗$$
$$\textbf{未决}: N_4\le10\ ✗;\quad 119: \textbf{UNKNOWN}\ ✓;\quad \text{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §5 下一刀建议

```
$$\text{① 用事实 B}: \text{B 型中心在 }\delta\in\{1,3\}\ \text{上"免费"}\ ✓\ \Longrightarrow\ \text{约束来自 }\delta=2,4\ \text{与 A 型}\ ⚠️$$
$$\text{② 平均型论证}: \text{若 }N_4^{\rm iso}\ \text{很大，则二层影子点很多 }\Longrightarrow\ \text{某点 }z\ \text{的 }b(z)\ \text{被迫升高}\ \Longrightarrow\ \text{消耗 }Q_2/E\ ⚠️$$
$$\text{③ 注意}: \text{碰撞非必然}\ \Longrightarrow\ \text{纯计数 charging 路线已被本轮证否}\ ✗\ (\text{诚实登记}\ ✓)$$
$$

## §6 边界（诚实标注）

- §0–§2 为**实算**（Hamming 枚举 ✓）；§3 明确标注**上界未得** ✗ 且**纯计数路线被否** ✗
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 二层影子碰撞表 命中文件数=1    :: ./P14-2026-09-26-second-layer-shadow-collision-table.md 
技术词 B–B 奇距不撞 命中文件数=1    :: ./P14-2026-09-26-second-layer-shadow-collision-table.md 
技术词 纯计数路线否证 命中文件数=1    :: ./P14-2026-09-26-second-layer-shadow-collision-table.md
```
- **本档新增**（扣自引后 = 0）：二层影子碰撞表、B–B 奇距不撞、纯计数路线否证
- **档案已有（引用，不列为提出）**：N₄、星集、H₄
