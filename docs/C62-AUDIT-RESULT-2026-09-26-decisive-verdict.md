已查地图：已跑 scripts/prework_map_check.sh C_62 K_9_1 审计 剖面 Q2 ⟹ 执行自 C62-AUDIT-PROTOCOL-2026-09-26 档；本档为**(9,62) 真实极值对象的完整审计与决定性判决**（唐先生 2026-09-26 16:18 裁定 ✓）；未跑 solver ✓。
D0: 本档对象 = Kéri CD 附录中的 K_9_1 码（2 个已知最优码）的十项不变量、共享/不共享判决、四个猜想的生死
D1: 1（新增：**C₆₂ 获得并验证** ✓✓；**Q₂ 与 b-剖面钉住** ✓✓；**d_max=3 / I≤2 / b≤3 三猜想被否** ✗✓）

# C62-AUDIT-RESULT-2026-09-26

## §0 对象来源（免费可得 ✓✓）

```
$$\text{源}: \text{Kéri CD 附录在线镜像}\ ✓\ \texttt{https://old.sztaki.hu/\textasciitilde keri/codes-hu/lemez/Binary/}\ ✓$$
$$\qquad\text{文件}: \texttt{K\_9\_1.txt}（1 个 62 码）\ ✓;\quad \texttt{K\_9\_1\_classif.txt}（\textbf{2 个} 62 码 ✓）$$
$$\text{（Kéri 论文原文写明 CD 附录 demo 位于 }codes-hu/\text{，其下 }lemez/\ = CD\ \text{内容}\ ✓✓)$$
$$\textbf{两码均已验证}: |C|=62\ ✓\ \text{且}\ \textbf{覆盖}\ \mathbb F_2^9\ (0\ \text{未覆盖点})\ ✓✓$$
$$

## §1 ⭐⭐ **十项不变量（两码对照）**

```
$$\begin{array}{c|c|c|c}
\text{不变量} & \text{已知码 #1} & \text{已知码 #2} & \text{判决}\\
\hline
E & 108 & 108 & \textbf{钉住}\ ✓✓\\
Q_2 & \mathbf{38} & \mathbf{38} & \textbf{钉住}\ ✓✓✓\\
(N_j)\ \text{剖面} & \{1{:}432,\ 2{:}62,\ 3{:}8,\ 4{:}10\} & \text{同上} & \textbf{钉住}\ ✓✓✓\\
d_{\max} & \mathbf{3} & \mathbf{3} & \textbf{钉住}\ ✓✓\\
\hline
I & 6 & 27 & \textbf{不钉}\ ✗\\
S & 126 & 67 & \textbf{不钉}\ ✗\\
A_1 & 7 & 26 & \textbf{不钉}\ ✗\\
A_2 & 66 & 47 & \textbf{不钉}\ ✗\\
S_q & 0 & 3 & \textbf{不钉}\ ✗\\
|V_\square| & 0 & 10 & \textbf{不钉}\ ✗\\
I_{\rm nw} & 6 & 17 & \textbf{不钉}\ ✗\\
\end{array}$$
$$\textbf{两个恒等式在两码上均验证}\ ✓✓:\quad 2A_{\le2}=E+Q_2=146\ \checkmark;\qquad 2A_2=I+S\ \checkmark\ (132\ \text{与}\ 94)$$
$$

## §2 ⭐⭐ **决定性判决：四个猜想的生死**

```
$$\textbf{① b-剖面钉住 —— 活}\ ✓✓✓:\ (N_j)=\{1{:}432,2{:}62,3{:}8,4{:}10\}\ \text{两码完全相同}\ ✓✓$$
$$\qquad\Longrightarrow\ \text{"极值壳剖面刚性"（我们最早的母猜想）在 }n=9\ \text{上\textbf{存活}}\ ✓✓$$
$$\qquad\text{且 }T_3=Q_2+H/3\ \text{亦钉住}:\ H=\sum_{k\ge4}(k-3)\binom{k-1}2N_k=3\cdot10=30\ \Longrightarrow\ T_3=38+10=48\ ✓$$
$$\textbf{② }b_{\max}\le3\ \text{（M=K）—— \textbf{死}}\ ✗✓:\ b_{\max}=\mathbf{4}\ ✓\ (N_4=10>0\ ✓)$$
$$\textbf{③ }d_C\le2\ \text{（即 }h=0\text{）—— \textbf{死}}\ ✗✓:\ d_{\max}=\mathbf{3}\ ✓\ (\text{两码均有 }d_C=3\ \text{的码字}\ ✓)\ \Longrightarrow\ \boxed{h\ge1}\ ✗$$
$$\textbf{④ }M=K\Rightarrow I\le2\ ——\ \textbf{死}}\ ✗✓:\ I\in\{6,\ 27\}\ \text{均}>2\ ✓$$
$$

## §3 判据表（审计协议预决策的落点）

```
$$\text{(i) }d_{\max}\le2\ ?\quad \textbf{否}\ ✗\ \Longrightarrow\ h>0\ \text{在真实极值对象上成立}\ ✓✓$$
$$\text{(ii) }I_{\rm nw}=0\ ?\quad \textbf{否}\ \uparrow\ (6\ \text{与}\ 17)\ ✗$$
$$\text{(iii) }S_q>0\ ?\quad \text{码#1}\ 0\ ✓\text{否};\ \text{码#2}\ 3\ ✓\text{是}\ \Longrightarrow\ \text{方阵\textbf{非}刚性}\ ✗$$
$$\text{(iv) 恒等式自洽}\ ?\quad \textbf{是}\ ✓✓$$
$$\text{(v) }L_\square=0\ ?\quad \text{码#2 有方阵}\ \Longrightarrow\ \text{可对照检验 shell 资产}\ ⚠️$$
$$

## §4 结论（本轮最重要）

```
$$\boxed{\textbf{极值壳 }M=K(9,1)=62\ \text{的\textbf{刚性量是 }Q_2\ \text{与 }b\text{-剖面}\ ✓✓;\ \textbf{不}是 }I,\ S,\ A_2,\ \text{方阵数}\ ✗✓}$$
$$\Longrightarrow\ \textbf{① 早期 C-380 线的靶心（}Q_2\ \text{钉住）\textbf{得到最强外部验证}}\ ✓✓\ (\text{真实最优码上 }Q_2\equiv38\ ✓)$$
$$\Longrightarrow\ \textbf{② 中段把靶心换成 }I\ \text{是\textbf{方向性错误}}\ ✗✓\ (\text{真实极值对象上 }I\ \text{不钉}\ ✗)$$
$$\Longrightarrow\ \textbf{③ 但 }h>0\ \text{在 }M=K\ \text{上\textbf{确实成立}}\ ✓\ \Longrightarrow\ \text{"极值壳 }\Rightarrow\ d_C\le2\text{" 从一开始就是错的}\ ✗✓$$
$$\qquad\ \text{意味着：把 }h=0\ \text{当成目标（前面大量工作）方向错误}\ ✗;\ \text{应改为研究 }Q_2/\ \text{剖面为何钉住}\ ✓✓$$
$$

## §5 状态与下一刀

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{C}_{62}: \textbf{已获得并验证}\ ✓✓$$
$$\text{下一刀}: \text{回到 }Q_2\ \text{与 }b\text{-剖面的钉住机制}\ ✓\ (\text{真实对象在手，可直接做 }switching\ \text{轨道检验}\ ✓)$$
$$\qquad\text{具体}: \text{码#1 与码#2 在同一 switching class}\ [L]\ ✓\ \Longrightarrow\ \text{测 switching 下 }Q_2/\ \text{剖面是否恒定}\ ⚠️$$
$$

## §6 边界（诚实标注）

- 全部数值为**实算** ✓（两个 62 码均验证覆盖 ✓）；对象来源**免费可得** ✓（Kéri CD 镜像 ✓）
- **未跑 solver** ✓；**未扩大任何模型** ✓（遵唐先生 ✓）
- `switching` 轨道检验**未做** ⚠️（下一步 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 极值对象审计判决 命中文件数=1    :: ./C62-AUDIT-RESULT-2026-09-26-decisive-verdict.md 
技术词 刚性量判决  命中文件数=1    :: ./C62-AUDIT-RESULT-2026-09-26-decisive-verdict.md 
技术词 方向性错误修正 命中文件数=1    :: ./C62-AUDIT-RESULT-2026-09-26-decisive-verdict.md
```
- **本档新增**（扣自引后 = 0）：极值对象审计判决、刚性量判决、方向性错误修正
- **档案已有（引用，不列为提出）**：Q₂、剖面、h、I_nw、switching class
