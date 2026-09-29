# RESULT-g（2026-09-29）—— **$u$-lemma 归约为 9 坐标上的线性三元组图**（三条归约 $30/30$ ✓✓）

> **性质**：**问题特化续（自测）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:45 ✓

**已查地图**：`RESULT-f`（$r_q{=}2t_q$）／`RESULT-e`／`RESULT-c` ✓

D0: 本档对象 ＝ **档案已有**（Steiner／线性超图—经典 ✓）
D1: 0（产出＝**三条归约 ＋ 局部形式** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓✓ 坐标归约}:\ t_q=0\iff\nexists\{i,j,k\}:p\oplus\{i,j,k\}\in P\quad(q=p\oplus e_i)}$$
$$\boxed{\text{② ✓✓ 邻居必私有}:\ \forall q\in Q\cap N_1(P):\ s_q=1\ (\text{因 }d(p,p'){=}2\ \text{不可能})}$$
$$\boxed{\text{③ ✓✓ }T_p\ \text{线性}:\ T_p=\{S\subseteq[9]:|S|{=}3,\ p\oplus S\in P\}\ \text{两两交}\le1}$$
$$\boxed{\text{④ 于是 }u=\sum_{p\in P}\#\{i:\ i\notin\textstyle\bigcup T_p,\ p\oplus e_i\in Q\}\ ——\ \textbf{纯 9-坐标局部量}}$$
$$\boxed{\text{⑤ 实测}:\ |T_p|\in[1,9]\ (\text{STS}(9)\ \text{界 }12);\quad u\in[1,6]}$$

## §1 三条归约（✓ 实测 $30/30$）

$$\textbf{（甲）}:\ q=p\oplus e_i\in Q;\ \text{找}\ p'\in P\ \text{使}\ d(q,p')=2.\ \text{写 }p'=p\oplus S,\ |S|\ge3\ (\text{packing})$$
$$d(e_i,S)=2\iff|S|=3\ \wedge\ i\in S\qquad(\text{若}\ i\notin S:\ |S|+1\ge4\neq2)✓$$
$$\therefore\ t_q=0\iff\text{无三元组过 }i✓\qquad\text{实测 }30/30✓✓$$
$$\textbf{（乙）}:\ p'\ \text{邻接}\ p\oplus e_i\Rightarrow d(p,p')=2\ \text{与 packing 矛盾}\Rightarrow s_q=1\ \forall q\in Q\cap N_1(P)✓\ (\text{实测 }30/30)$$
$$\textbf{（丙）}:\ S,S'\in T_p\Rightarrow d(p\oplus S,p\oplus S')=|S\triangle S'|\ge3\Rightarrow|S\cap S'|\le1✓\ (\text{实测 }30/30)$$

## §2 $u$-lemma 之最终局部形式（✓）

$$\boxed{\text{证明}:\ \sum_{p\in P}\#\{i\notin\textstyle\bigcup T_p:\ p\oplus e_i\in Q\}\ \le\ U\ (\text{统一常数})}$$
$$\text{结构输入（尚未使用）}:\ \text{slice 条件}\ |Q_9\setminus N_1(A)|\le106-a\ (\text{$A$ 近似覆盖})$$
$$\text{或}:\ T_p\ \text{之覆盖度}\ |\textstyle\bigcup T_p|\ \text{之下界（来自 3-packing 密集性）}$$

## §3 数值（✓）

$$|T_p|\in[1,9]\quad(\text{STS}(9)\ \text{存在，界 }12;\ \text{实测最大 }9)$$
$$u\in[1,6]\quad(\text{本回样本});\quad R=2\sum_q t_q\ge2(|Q|-u)✓$$

## §4 下一目标（✓ 更窄了）

$$\boxed{\text{（甲）证}\ u\le U\ (\text{常数});\quad\text{或（乙）证}\ |\textstyle\bigcup T_p|\ \text{之统一下界}}$$
$$\text{关键}:\ T_p\ \text{是 }9\ \text{点上的线性 }3\text{-图}\Longrightarrow\ \text{可用 Steiner/线性超图之极值结果}$$
$$\text{潜在联系}:\ \text{那个未解释的"}-1/\text{fiber}"\ \text{或与此局部结构同源}⚠️$$

## §5 边界（硬 ✓）

- **三条归约实测 $30/30$** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；$u\le U$ **未证**（如实标注）⚠️
