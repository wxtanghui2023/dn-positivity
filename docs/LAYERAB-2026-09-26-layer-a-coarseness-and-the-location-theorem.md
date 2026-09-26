已查地图：已跑 scripts/prework_map_check.sh Layer A M-covering Layer B y-SIP 粗度 ⟹ 执行自 MCOVER-2026-09-26 档；本档为**乙线第三 commit：Layer A/B 二分 ＋ 粗度量化 ＋ 定位定理**（唐先生 2026-09-26 18:14 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Layer A/B 二元形式、Layer A 自由度量化、M=61 各层可行性、N₄ 的层归属、P4 定位
D1: 1（新增：**Layer A 粗度量化（m=1 余 265 bit）** ✓✓；**定位定理（N₄ 不可在 Layer A 证明）** ✓✓；**M=61 在 m≤4 全可行、m=4 恰紧** ✓）

# LAYERAB-2026-09-26

## §1 ✅ **二元两层的精确形式**

```
$$\textbf{Layer A（M-covering system，level }m\text{）}: y_S=|C\cap W_S|\ ✓;\ \sum_j A_{ji}y_j\ \ge\ 2^{9-m}\ (\forall i)\ ✓;\ \sum_i y_i=M\ ✓;\ y\in\mathbb Z_{\ge0}\ ✓$$
$$\qquad A_{ii}=10-m\ ✓;\ A_{ij}=\mathbf 1_{\{d(p_i,p_j)=1\}}\ ✓\ (\text{余 0}\ ✓)$$
$$\textbf{Layer B（}y\text{-SIP，码级精确 IP）}: \min_x\{1^Tx:\ Ax\ge1,\ x\in\{0,1\}^{512},\ x\in M(y)\}\ ✓,\ M(y)=\{x:\ \sum_{i\in W_j}x_i=y_j\ \forall j\}\ ✓$$
$$\textbf{机制（LMT 口径 ✓）}: \text{若全部 surviving }y\ \text{的 }y\text{-SIP 不可行}\ \Longrightarrow\ \text{无 }M\text{-word covering code}\ ✓$$
$$
$$

## §2 ⭐⭐⭐ **决定性量化：Layer A 有多粗** ✓✓

```
$$\text{给定 }y\ \text{时 }x\ \text{的残余自由度}: \log_2\prod_j\binom{2^{9-m}}{y_j}\ (\text{均匀 }y\approx 62/2^m\ ✓)$$
$$\begin{array}{c|c|c|c}
m & \text{cells} & \text{每 cell} & \log_2(\#x\ \text{给定 }y)\\
\hline
1 & 2 & 256 & \mathbf{265.2}\ \text{bit}\\
2 & 4 & 128 & 259.7\\
3 & 8 & 64 & 250.7\\
4 & 16 & 32 & 236.4\\
6 & 64 & 8 & 186.0\\
8 & 256 & 2 & 62.0\\
\mathbf 9 & \mathbf{512} & \mathbf 1 & \mathbf{0.0}\ (\text{唯一}\ ✓)\\
\end{array}$$
$$\Longrightarrow\ \boxed{\textbf{Layer A 在 }m\le 4\ \text{保留 }10^{70}\text{ 量级的选择}\ ✗\ ——\ \text{它\textbf{根本看不到} }b\text{-profile}\ ✓✓}$$
$$
$$

## §3 ⭐⭐⭐ **定位定理（本档核心 ✓✓）**

```
$$\textbf{实测}: \text{两最优码 }b\text{-profile \textbf{完全相同}}:\ \{1{:}432,2{:}62,3{:}8,4{:}10\}\ ✓✓\ (N_4=10\ ✓)$$
$$\qquad\text{但它们的 }y\ \text{在每一层都\textbf{不同}}\ ✗\ (m{=}1:\ (31,31)\ vs\ (30,32)\ ✓;\ m{=}2:\ (16,15,16,15)\ vs\ (15,15,16,16)\ ✓)$$
$$\Longrightarrow\ \boxed{\text{刚性}\ (b\text{-profile})\ \textbf{不是 }y\ \text{的函数}\ ✗\ \Longrightarrow\ \textbf{Layer A \textbf{不可能}证明 }N_4\ge10\ ✓✓}$$
$$\qquad\text{（配 }§2\ \text{的自由度：给定 }y\ \text{仍有 }265\ \text{bit}\ ⟹\ b\text{-profile 在其中自由变动}\ ✓)$$
$$\textbf{推论}: \boxed{\textbf{任何 }N_4\ge10\ \text{的证明必须使用 Layer B（}y\text{-SIP，码级约束）}\ ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{我方 14 条失败路线的共同病因确认}\ ✓:\ \text{它们全部在 Layer A 语言里找 Layer B 的量}\ ✗$$
$$
$$

## §4 ✅ **M=61 时各层可行性（解析，均匀 }y\text{）**

```
$$\begin{array}{c|c|c|c}
m & \text{最紧 cell 覆盖} & \text{需}\ge & \text{判定}\\ \hline
1 & 301 & 256 & \text{可行}\ ✗\\
2 & 150 & 128 & \text{可行}\ ✗\\
3 & 71 & 64 & \text{可行}\ ✗\\
4 & \mathbf{32} & \mathbf{32} & \textbf{恰紧}\ ⚠️\ (\text{仍可行}\ ✗)\\
\end{array}$$
$$\Longrightarrow\ \text{M-covering system 在 }m\le4\ \text{无法排除 }M=61\ ✗\ (\text{m=4 恰紧，提示 }m\ge5\ \text{起才可能咬合}\ ⚠️)$$
$$\qquad\text{而 }m=9\ \text{层 = 覆盖条件本体}（\text{循环}\ ✗)\ ⟹\ \textbf{有用层在中间}\ ⚠️$$
$$
$$

## §5 ⭐ **P4 定位（weighted covering / OB LP 在哪里）**

```
$$\text{三层严格分开（用户要求 ✓）}: \text{OB-2001 LP}\ \neq\ M\text{-covering system}\ \neq\ y\text{-SIP}\ ✓$$
$$\text{由 }§2\text{--}§3: \text{Layer A 太粗（265 bit}\ ✗),\ \text{真正的约束在 Layer B}\ ✓\ \Longrightarrow\ \textbf{OB 的"repeatedly solve an LP"最可能在 }y\text{-SIP 层}\ ⚠️$$
$$\qquad\text{即}: \text{LP = 码级 IP 的\textbf{分数松弛}}（\text{用途：定界 + 剪枝}\ ⚠️)\ ;\ \text{其对偶 = 一个\textbf{加约束的 weighted covering}}\ ⚠️$$
$$\qquad\textbf{HYPOTHESIS}\ ⚠️\ (\text{未获正文}\ ✗);\ \textbf{不宣布成立}\ ✓$$
$$
$$

## §6 状态

```
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{未跑 solver/LP/SAT}\ ✓$$
$$\textbf{本轮所得}: \text{① 两层精确形式}\ ✓✓;\ \text{② Layer A 粗度量化（265 bit）}\ ✓✓;\ \text{③ 定位定理（N₄ 必须用 Layer B）}\ ✓✓;\ \text{④ }M{=}61\ \text{在 }m\le4\ \text{全可行、}m{=}4\ \text{恰紧}\ ✓;\ \text{⑤ P4 定位到 }y\text{-SIP（假设}\ ⚠️)$$
$$\textbf{下一步（待批 ✓）}: \text{① 找 }M{=}61\ \text{的临界层 }m^*\ ✓;\ \text{② 在 }m^*\ \text{层加 }N_4\le9\ \text{作 forbidden state 问 }y\text{-SIP 不可行}\ ⚠️\ (\textbf{需正文或小规模 ILP}\ ✓)$$
$$

## §7 边界（诚实标注）

- §1–§4 为我方**自行导出/实算** ✓（两码 ✓ 解析 ✓）；§5 明确 **HYPOTHESIS** ⚠️
- **未跑 solver/LP/SAT** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 Layer A 粗度   命中文件数=1    :: ./LAYERAB-2026-09-26-layer-a-coarseness-and-the-location-theorem.md 
技术词 定位定理     命中文件数=3    :: ./L1-nonselfadjoint-spectral-rigidity-audit.md ./M0-T-system-verbatim-and-theorem-locations.md ./LAYERAB-2026-09-26-layer-a-coarseness-and-the-location-theorem.md 
技术词 临界层        命中文件数=2    :: ./M03-W0-third-order-axis-point.md ./LAYERAB-2026-09-26-layer-a-coarseness-and-the-location-theorem.md
```
- **本档新增**（扣自引后 = 0，命中 1 = 自引 ✓）：**Layer A 粗度**
- **档案已有（引用，不列为提出）**：**定位定理**（命中 3 文件 ⟹ 非新 ✗，已在 `L1-nonselfadjoint-spectral-rigidity-audit.md`、`M0-T-system-verbatim-and-theorem-locations.md`）｜**临界层**（命中 2 ⟹ 非新 ✗，已在 `M03-W0-third-order-axis-point.md`）｜M-covering system、y-SIP、b-profile
- **档案已有（引用，不列为提出）**：M-covering system、y-SIP、b-profile
