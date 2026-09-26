已查地图：已跑 scripts/prework_map_check.sh Wille 指纹 对照 分叉 ⟹ 执行自 C62-AUDIT-RESULT-2026-09-26 档；本档为**真实 Wille C₆₂ 恢复＋两码决定性对照**（唐先生 2026-09-26 16:25 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Kéri CD 第二个 listing 的 Wille 指纹检验、两已知 (9,62) 码的完整对照、Q₂ 刚性 vs I/S 分叉的判决
D1: 1（新增：**Wille 四词全中（码#2）** ✓✓✓；**钉住集 = {E, Q₂, A≤2, 剖面, d_max, N₁}** ✓✓；**I/S 分叉** ✓✓）

# C62-WILLE-RECOVERED-2026-09-26

## §1 ⭐⭐⭐ **Wille 指纹检验：码#2 全中** ✓✓✓

```
$$\text{指纹（唐先生 ✓）}: \text{Kéri 论文给出的 Wille 方阵四词}\ \{000001010,\ 000101010,\ 001001010,\ 001101010\}\ ✓$$
$$\textbf{码#1}\ (\texttt{K\_9\_1.txt}):\ \text{直接命中}\ \mathbf{1/4}\ ✗\ (\text{仅 }001001010\ ✓)$$
$$\textbf{码#2}\ (\texttt{K\_9\_1\_classif.txt}\ \text{第二个 listing}):\ \text{直接命中}\ \mathbf{4/4}\ ✓✓✓$$
$$\Longrightarrow\ \boxed{\text{码#2 = Wille 的 }C_{62}\ (\text{或其 }B_n\ \text{像})\ ——\ \textbf{真实 Wille 对象已恢复}}\ ✓✓✓$$
$$\text{（且两个验证}: |C|=62\ ✓\ \text{且覆盖}\ \mathbb F_2^9\ ✓✓)$$
$$

## §2 ⭐⭐⭐ **两个已知 (9,62) 码的完整对照（决定性 ✓✓）**

```
$$\begin{array}{c|c|c|c}
\text{指标} & \text{码#1 (K\_9\_1.txt)} & \text{码#2 (\textbf{Wille 型} ✓)} & \text{判决}\\
\hline
E & 108 & 108 & \textbf{钉住}\ ✓✓\\
Q_2 & \mathbf{38} & \mathbf{38} & \textbf{钉住}\ ✓✓\\
A_{\le2} & \mathbf{73} & \mathbf{73} & \textbf{钉住}\ ✓✓\\
d_{\max} & 3 & 3 & \textbf{钉住}\ ✓✓\\
N_1 & 432 & 432 & \textbf{钉住}\ ✓✓\\
(N_j) & \{1{:}432,2{:}62,3{:}8,4{:}10\} & \text{同上} & \textbf{钉住}\ ✓✓\\
\hline
A_1 & 7 & 26 & \textbf{分叉}\ ✗\\
A_2 & 66 & 47 & \textbf{分叉}\ ✗\\
I & 6 & 27 & \textbf{分叉}\ ✗\\
S & 126 & 67 & \textbf{分叉}\ ✗\\
S_q & 0 & 3 & \textbf{分叉}\ ✗\\
|V_\square| & 0 & 10 & \textbf{分叉}\ ✗\\
I_{\rm nw} & 6 & 17 & \textbf{分叉}\ ✗\\
\end{array}$$
$$

## §3 ⭐⭐⭐ **判决：Q₂ 刚性 ✓✓；I / S 分叉 ✗✓**

```
$$\boxed{\textbf{极值壳 }M=K(9,1)=62\ \text{的刚性量} = \{E,\ Q_2,\ A_{\le2},\ (N_j),\ d_{\max},\ N_1\}\ ✓✓}$$
$$\boxed{\textbf{非刚性（分叉）} = \{A_1,\ A_2,\ I,\ S,\ S_q,\ |V_\square|,\ I_{\rm nw}\}\ ✗✓}$$
$$\Longrightarrow\ \text{① }\textbf{Q}_2\ \text{与剖面刚性}\ \textbf{获真实最优对象双码验证}\ ✓✓✓\ (\text{早期 C-380 靶心正确}\ ✓)$$
$$\Longrightarrow\ \text{② }\textbf{I}\ \text{根本不是极值壳的不变量}\ ✗✓\ \Longrightarrow\ \text{中段"控制 }I\text{"整条路线\textbf{方向错误}}\ ✗✓$$
$$\Longrightarrow\ \text{③ }\textbf{S}\ \text{亦然}\ ✗\ \Longrightarrow\ \text{"}L_\square\le S+I_{\rm nw}\text{"类的式子注定不成立}\ ✗\ (\text{已被 }(4,8)\ \text{反例证实}\ ✓)$$
$$

## §4 ⚠️ **对 shell 归档决定的部分修正**（诚实 ✓）

```
$$\textbf{曾判}: \text{"shell 线在 }M=K\ \text{上为空（vacuous）"}\ ✗\ ——\ \textbf{依据只有 }(9,64)\ (\text{非最小})\ ✓$$
$$\textbf{现纠正}: \text{真实 Wille 码 }(\text{码#2},\ M=K=62\ ✓)\ \textbf{有 3 个方阵}\ ✓,\ |V_\square|=10\ ✓\ \Longrightarrow\ \text{方阵\textbf{共享顶点}}\ ✓$$
$$\qquad\Longrightarrow\ \text{shell/}r(v)\ \text{机制在真实极值壳上\textbf{非空}}\ ✓✓\ \Longrightarrow\ \textbf{归档决定需部分回滚}\ ⚠️$$
$$\qquad\text{且 }d_{\max}=3\ \text{与我们的"重复见证}\Rightarrow d_C\ge3\text{"机制\textbf{一致}}\ ✓✓$$
$$

## §5 状态与下一刀

```
$$\textbf{C}_{62}:\ \textbf{两个真实对象均在手（免费可得}\ ✓✓)$$
$$\text{下一刀}: \text{对 \textbf{Wille 码（码#2）} 做 shell/}L_\square\ \text{审计}\ ✓:\ \text{三态分类、}\Phi\ \text{见证、重数、}U(v)\ \text{交集公式}\ ✓$$
$$\qquad\text{检验}: \text{已否的 }L_\square\le S+I_{\rm nw}\ \text{在真实极值对象上是否也失败}\ ⚠️;\ \text{以及 }r(v)\ge3\ \text{是否给出 }d_C\ge3\ ✓$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §6 边界（诚实标注）

- §1/§2 为**实算**（两码均验证覆盖 ✓）；指纹为**唐先生提供**且与 Kéri 论文一致 ✓
- §4 为**对既有归档决定的部分修正** ⚠️（诚实记录 ✓）
- **未跑 solver** ✓；**未扩大任何模型** ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**（扣自引后 = 0）：Wille 指纹全中、刚性集判决、归档部分回滚
- **档案已有（引用，不列为提出）**：Q₂、剖面、switching class、方阵


---

## §7 ⭐⭐⭐ **在真实 Wille 码上：shell 机制被"实际实现"** ✓✓（追加 ✓）

```
$$	ext{Wille 码（码#2}，M=K=62\ ✓):\ |C|=62,\ 	ext{方阵}=3\ ✓,\ |V_\square|=10\ ✓,\ I=27,\ S=67,\ I_{m nw}=17\ ✓$$
$$	ext{十个方阵顶点}: 	extbf{2 个 }|\cap\mathrm{dirs}|=1\ (	ext{即在 2 个方阵中}\ ✓)\ 	ext{且其 }d_C=\mathbf{3}\ ✓✓;\ 	ext{其余 8 个 }|\cap|=2,\ d_C\in\{2,3\}\ ✓$$
$$\Longrightarrow\ oxed{	extbf{"}|\cap|<2\ \Longrightarrow\ d_C\ge3	ext{" 在真实极值对象上	extbf{成立}}\ ✓✓\ (	ext{重复见证机制被实现}\ ✓✓)}$$
$$	extbf{更强读数}: 	ext{该码中 }d_C=3\ 	ext{的码字	extbf{恰是}落在 2 个方阵中的那两个顶点}\ ✓✓$$
$$\qquad\Longrightarrow\ oxed{h>0\ 	ext{（即 }d_{\max}=3	ext{）在 }M=K(9,1)\ 	ext{上由	extbf{方阵重叠直接解释}}\ ✓✓}$$
$$	ext{shell 三态}: P=60,\ M=6,\ C=6\ ✓\ \Longrightarrow\ L_\square=\mathbf{12}>0\ ✓\ (	ext{故 shell 线在 }M=K\ 	extbf{非空}\ ✓✓\ ——\ \S4\ 	ext{的回滚得到确认}\ ✓)$$
$$	ext{已否不等式在此成立}: L_\square=12\le S+I_{m nw}=84\ ✓\ (	ext{但 }(4,8)\ 	ext{反例使其	extbf{非定理}}\ ✗)$$
$$

## §8 修正后的最终图景

```
$$	extbf{刚性（真实对象双码验证}\ ✓✓)}: E,\ Q_2=38,\ A_{\le2}=73,\ (N_j),\ d_{\max}=3,\ N_1=432$$
$$	extbf{非刚性（分叉}\ ✗)}: A_1,\ A_2,\ I,\ S,\ S_q,\ |V_\square|,\ I_{m nw}$$
$$	extbf{机制（已验证}\ ✓✓)}: 	ext{方阵重叠}\ \Longrightarrow\ d_C\ge3\ \Longrightarrow\ h>0\ ✓\ (	ext{在真实极值对象上实现}\ ✓✓)$$
$$\Longrightarrow\ 	extbf{正确靶心}: oxed{	ext{为何 }Q_2\ 	ext{与 }(N_j)\ 	ext{刚性，而 }I/S\ 	ext{分叉}}\ ✓✓\ ——\ 	ext{而非"控制 }I	ext{"}\ ✗✓$$
$$
