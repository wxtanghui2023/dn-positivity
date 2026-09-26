已查地图：已跑 scripts/prework_map_check.sh 第二中心 incidence 零交叉 α β ⟹ 执行自 P1LB4-2026-09-26 档；本档为**第二中心 incidence 结构 ＋ 零交叉预期纠正 ＋ 新可证恒等式**（唐先生 2026-09-26 16:53 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = H₃/H₄/α/β 实测、X₃→X₃ 匹配结构、零交叉反例（n=5,6）、Σp₂ 恒等式、容量不等式
D1: 1（新增：**H₃=8/H₄=16/α=1/β=4 两码全同** ✓✓；**零交叉非普适（n=5,6 反例）** ✗✓；**Σp₂=ΣC(b,2)−2A₁** ✓✓）

# P1LB4-2026-09-26

## §0 ⚠️ **降级（遵唐先生 ✓）**

```
$$\text{"可能就是 }+10\text{ 的来源"}\ \longrightarrow\ \textbf{降级为待证猜想}\ ⚠️\ ✓\ (\text{未证，不得当结论}\ ✓)$$
$$\text{已立的中间结构}:\ \boxed{b{=}3\ \text{中心}\ \to\ 3\ \text{个 distinct 第二中心}\ \to\ \text{全落 }b\ge3}\ ✓✓\ (\text{把 }X_3\ \text{与高重数层直接耦合}\ ✓)$$
$$

## §1 ⭐⭐⭐ **incidence 结构（两码完全一致 ✓✓）**

```
$$X_j:=\{x:b(x)=j\};\quad \Delta(x)=\text{第二中心集};\quad h_3(y)=|\{x\in X_3:y\in\Delta(x)\}|;\quad \sum_y h_3(y)=3N_3=24\ ✓$$
$$\begin{array}{c|c|c}
\text{量} & \text{码#1} & \text{码#2}\\
\hline
N_3,\ N_4,\ N_2 & 8,\ 10,\ 62 & 8,\ 10,\ 62\\
H_3=\sum_{y\in X_3}h_3(y) & \mathbf{8} & \mathbf{8}\\
H_4=\sum_{y\in X_4}h_3(y) & \mathbf{16} & \mathbf{16}\\
\alpha=\max_{y\in X_3}h_3(y) & \mathbf{1} & \mathbf{1}\\
\beta=\max_{y\in X_4}h_3(y) & \mathbf{4} & \mathbf{4}\\
h_3\ \text{分布(X}_3\text{)} & \{1{:}8\} & \{1{:}8\}\\
h_3\ \text{分布(X}_4\text{)} & \{0{:}6,\ 4{:}4\} & \{0{:}6,\ 4{:}4\}\\
\hline
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{又一层跨表示刚性}\ ✓✓\ ——\ \text{两码 incidence 结构完全相同}\ ✓✓}$$
$$

## §2 ⭐⭐ **α = 1 的强含义：X₃→X₃ 是完美匹配** ✓✓

```
$$\alpha=\max_{y\in X_3}h_3(y)=1\ \Longrightarrow\ \text{每个 }X_3\ \text{点至多是\textbf{一个}其它 }X_3\ \text{点的第二中心}\ ✓✓$$
$$\text{而 }H_3=8=N_3\ \Longrightarrow\ \textbf{每个 }X_3\ \text{点恰被命中一次}\ \Longrightarrow\ \boxed{X_3\to X_3\ \text{构成完美匹配}}\ ✓✓$$
$$\text{发射结构}: 8\ \text{个 }X_3\ \text{各发射 3 个第二中心}=24\ ✓:\ \textbf{8 落 }X_3\ (\text{匹配}\ ✓),\ \textbf{16 落 }X_4\ (\text{4 个点各收 4}\ ✓)$$
$$

## §3 ⛔ **零交叉预期被纠正（重要 ✗✓）**

```
$$\text{实测}: \text{n=9 两码}: \Delta(X_3)\cap X_2=\mathbf\varnothing\ ✓\ (\text{零交叉成立}\ ✓)$$
$$\textbf{但}: \text{n=5}: \Delta(X_3)\cap X_2=\mathbf 6\ \text{个}\ ✗;\quad \text{n=6}: \mathbf{12}\ \text{个}\ ✗;\quad \text{n=4}: \text{（无 }X_3\text{）}$$
$$\qquad\Longrightarrow\ \textbf{小 }n\ \text{时 }X_3\ \text{的第二中心\textbf{全部}落在 }X_2\ \text{上}\ ✗\ ——\ \textbf{与 }n=9\ \text{完全相反}\ ✗✓$$
$$\Longrightarrow\ \boxed{\text{"零交叉"}\ \textbf{不是普适律}}\ ✗✓\ ——\ \text{若证，只能证\textbf{n=9 专属版本}}\ ⚠️\ (\text{遵唐先生降级要求}\ ✓)$$
$$

## §4 ✅ **新可证恒等式（本轮副产品 ✓✓）**

```
$$\sum_z p_2(z)=\sum_{z\in C}q(z)+\sum_{z\notin C}\binom{b(z)}2=\sum_z\binom{b(z)}2-\sum_{c\in C}(b(c)-1)=\boxed{\sum_z\binom{b(z)}2-2A_1}\ ✓✓$$
$$\text{核验}: \text{码#1}: 146-2\cdot7=132\ ✓;\ \text{码#2}: 146-2\cdot26=94\ ✓\ (\text{与实测 }Σp_2\ \text{吻合}\ ✓✓)$$
$$\text{合并负载}: \sum_z(h_3+h_4)=3N_3+6N_4=84\ ✓\ \le\ \Sigma p_2\ ✓\ (\text{码#1}\ 132,\ \text{码#2}\ 94\ ✓)$$
$$\qquad\Longrightarrow\ 3N_3+6N_4\le 146-2A_1\ \Longrightarrow\ \textbf{2A}_1\le32+3N_4\ ✗\ (\text{不界 }N_4\ ✗)$$
$$

## §5 状态与下一刀

```
$$\textbf{新立}: H_3{=}8/H_4{=}16/\alpha{=}1/\beta{=}4\ \text{两码全同}\ ✓✓;\ X_3\to X_3\ \text{完美匹配}\ ✓✓;\ \Sigma p_2\ \text{恒等式}\ ✓✓$$
$$\textbf{已纠}: \text{零交叉非普适（n=5,6 反例）}\ ✗✓\ \Longrightarrow\ \text{降级为"n=9 待证猜想"}\ ⚠️$$
$$\text{下一刀}: \text{① 攻 }X_3\to X_4\ \text{的局部构型（现成数据: 4 个 }X_4\ \text{点各收 4}\ ✓\ \Longrightarrow\ \text{为何恰是 4？}\ ⚠️)$$
$$\qquad\text{② 欲得 }N_3\le8: \text{需"每 }X_3\ \text{至少 2 个第二中心落 }X_4"\ \Longrightarrow\ 2N_3\le H_4\le4N_4\ \Longrightarrow\ N_4\ge8\ ✗\ (\text{不足 10}\ ⚠️)$$
$$\qquad\text{③ 或证 }X_3\to X_3\ \text{匹配 + }X_4\ \text{接收上限的更强组合}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §6 边界（诚实标注）

- §1–§4 为**实算**（5 码 ✓）；§3 明确登记**预期被反例推翻** ✗✓；§5 明确标注 N₄≥10 **仍未得** ✗
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 第二中心 incidence 结构 命中文件数=1    :: ./P1LB4-2026-09-26-incidence-structure-and-zero-crossing-correction.md 
技术词 X₃ 完美匹配 命中文件数=1    :: ./P1LB4-2026-09-26-incidence-structure-and-zero-crossing-correction.md 
技术词 零交叉非普适 命中文件数=1    :: ./P1LB4-2026-09-26-incidence-structure-and-zero-crossing-correction.md
```
- **本档新增**（扣自引后 = 0）：第二中心 incidence 结构、X₃ 完美匹配、零交叉非普适
- **档案已有（引用，不列为提出）**：α、β、h₃、X₃
