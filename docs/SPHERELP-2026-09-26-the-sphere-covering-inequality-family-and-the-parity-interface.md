已查地图：已跑 scripts/prework_map_check.sh sphere-covering 线性不等式 部分状态 奇偶 ⟹ 执行自 G-COVERED-2026-09-26 档；本档为**A5 最后一刀：sphere-covering 不等式族推导 ＋ 奇偶接口 ＋ 新刚性**（唐先生 2026-09-26 18:28 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = 球交表、奇偶引理的证明与验证、sphere-covering 不等式族（全局＋部分状态）、对偶、OC 分布刚性、A5 缺口状态
D1: 1（新增：**不等式族推导（含部分状态形式）** ✓✓；**奇偶引理证明 ⟹ 单球切割空 ⟹ LP 必须多球** ✓✓；**OC 分布刚性（两码全同）** ✓✓）

# SPHERELP-2026-09-26

## §1 ✅ **球交表（n=9, R=1）**

```
$$\begin{array}{c|cccccc} d(u,v) & 0 & 1 & 2 & \ge3\\ \hline |B(u)\cap B(v)| & 10 & 2 & 2 & 0\\ \end{array}\ ✓$$
$$\Longrightarrow\ \sum_{y\in B(x)}b(y)=10\cdot\mathbf 1_{\{x\in C\}}+2\big(d_1(x)+d_2(x)\big)\ \Longrightarrow\ \boxed{\textbf{恒为偶数}}\ ✓✓$$
$$
$$

## §2 ⭐⭐⭐ **奇偶引理（证明 ＋ 验证）—— 决定 LP 的形态** ✓✓

```
$$\boxed{\text{OC}(B(x)):=\sum_{y\in B(x)}\big(b(y)-1\big)\ \equiv\ 10\cdot\mathbf 1_{\{x\in C\}}+2(d_1+d_2)-10\ \equiv\ 0\ (\bmod 2)}\ ✓✓$$
$$\textbf{验证（两码）}: \text{OC 奇偶}=\{0\}\ \text{（全偶）}\ ✓;\quad \text{OC 分布}=\{0{:}156,2{:}234,4{:}76,6{:}34,8{:}8,10{:}4\}\ ✓$$
$$\Longrightarrow\ \boxed{\textbf{单球 over-coverage 恒偶} \Longrightarrow\ \text{"单球 }\ge1\text{" 型切割\textbf{在 }n=9\ \text{为空}}\ ✗\ (\text{只能得}\ \ge2\ ✓)}$$
$$\textbf{推论（关键 ✓✓）}: \text{OB 的 LP \textbf{不可能}靠\textbf{单球}不等式获得强度}\ ✗\ \Longrightarrow\ \text{必须用}\textbf{多球/子空间级聚合}\ ✓$$
$$\qquad\Longrightarrow\ \text{与 OB 原文 "distributions of codewords in }\textbf{subspaces}\text{" 完全吻合}\ ✓✓\ (\text{derivation 级一致性，非文献转述}\ ✓)$$
$$
$$

## §3 ⭐⭐ **sphere-covering 线性不等式族（A5 要恢复的对象 ✓）**

```
$$\textbf{全局形式}: \forall S\subseteq Q_n:\quad \sum_{c}|B(c)\cap S|\ \ge\ |S|\ ✓\ (\text{等价于 }S\ \text{内每点被覆盖}\ ✓;\ \text{即覆盖约束的非负组合}\ ✓)$$
$$\textbf{部分状态形式（= 剪枝工具 ✓✓）}: \text{设已固定 }F\subseteq C\ \text{（partial code），剩余 }k\ \text{个待定}:$$
$$\qquad\boxed{\sum_{c\in C\setminus F}|B(c)\cap S|\ \ge\ |S|-\big|\{x\in S:\ x\ \text{被 }F\ \text{覆盖}\}\big|}\ ✓$$
$$\qquad\text{这是对"剩余码字分配变量"的\textbf{线性}不等式}\ ✓\ \Longrightarrow\ \text{LP 判定该节点是否可能继续}\ ✓\ \Longrightarrow\ \text{不可行 ⟹ 剪枝}\ ✓$$
$$\textbf{对偶（= weighted covering ✓）}: w(x)\ge0,\ \sum_{x\in B(c)}w(x)\le1\ (\forall c)\ \Longrightarrow\ M\ \ge\ \sum_x w(x)\ ✓$$
$$\qquad\text{（部分状态的对偶 = }\textbf{加约束的 weighted covering}，权重落在当前子树的状态上\ ✓）$$
$$
$$

## §4 ⭐⭐ **A5 重建终版（外层 ＋ 内层 ✓）**

```
$$\textbf{外层（文献确认 ✓）}: \text{M-covering system}\ \to\ \text{inequivalent }y\ \to\ m{=}1,\dots,9\ \text{refinement}\ \to\ \text{cell 维数 0}\ ✓$$
$$\textbf{内层（本档推导 ✓✓）}: \text{在每个 }\nu\ \text{上解}\ \textbf{sphere-covering 不等式族}\ \text{的 LP}\ \to\ \text{不可行则剪枝}\ ✓$$
$$\textbf{为何必须多球（本档证明 ✓✓）}: \text{单球切割在 }n=9\ \text{因奇偶而空}\ ✗\ \Longrightarrow\ \text{必须用子空间/multi-ball 聚合}\ ✓$$
$$\textbf{原假设的处置（唐先生纠正 ✓）}: \text{"OB-LP = }y\text{-SIP 的 LP 松弛"}\ \Longrightarrow\ \textbf{撤销}\ ✗\ (\text{y-SIP = LMT 后来加入的码级 IP}\ ✓)$$
$$\qquad\text{新工作假设}: \text{OB-LP = }\textbf{partial-state / distribution refinement 的 bounding LP}\ ✓\ (\text{与 2003 的 "sphere-covering inequalities" 描述一致}\ ✓)$$
$$
$$

## §5 ⭐ **新刚性（意外收获 ✓✓）**

```
$$\text{OC 分布}\ \{0{:}156,2{:}234,4{:}76,6{:}34,8{:}8,10{:}4\}\ \textbf{两码完全相同}\ ✓✓\ \Longrightarrow\ \text{又一跨表示不变量}\ ✓$$
$$\qquad\text{（比全局 }b\text{-profile 更细：它是\textbf{局部} }b\ \text{值的球和}\ ✓）$$
$$
$$

## §6 状态

```
$$\textbf{A5 缺口状态}: \text{外层 ✓✓ ＋ 内层\textbf{形式已恢复}（不等式族 + 部分状态 + 对偶）}\ ✓✓\ $$
$$\qquad\textbf{仍缺}: \text{OB 实现中 }\nu\ \text{的\textbf{确切状态变量}}（\text{分布 vs partial code}\ ⚠️)\ ——\ \text{需正文}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{未跑 solver/LP/SAT}\ ✓$$
$$

## §7 边界与一处文献提示（诚实 ✓）

- §1–§5 为我方**推导/实算** ✓；§3 的不等式族是**经典族**（我推导其部分状态形式 ✓），非我方首创 ✓
- ⚠️ **文献提示**：唐先生 [2] 的 TU Delft 链接标题为《The separability of standard cyclic N-ary gray codes》⟹ **与 2003 平衡码论文不匹配** ⚠️（预览页可能解析到同库另一文件）；建议核对原始出处 ✓
- **未跑 solver/LP/SAT** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 sphere-covering 不等式族 命中文件数=1    :: ./SPHERELP-2026-09-26-the-sphere-covering-inequality-family-and-the-parity-interface.md 
技术词 部分状态形式 命中文件数=1    :: ./SPHERELP-2026-09-26-the-sphere-covering-inequality-family-and-the-parity-interface.md 
技术词 OC 分布        命中文件数=1    :: ./SPHERELP-2026-09-26-the-sphere-covering-inequality-family-and-the-parity-interface.md
```
- **本档新增**（扣自引后 = 0）：sphere-covering 不等式族、部分状态形式、OC 分布
- **档案已有（引用，不列为提出）**：奇偶引理、weighted covering、y-SIP
