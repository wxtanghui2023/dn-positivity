已查地图：已跑 scripts/prework_map_check.sh Ψ2 Z2 Q=0 拼接 doubling product ⟹ 执行自 ODDENGINE-2026-09-26 档；本档为**二阶候选淘汰 ＋ 可拼接性测试 ＋ 一处读法纠正**（唐先生 2026-09-26 13:24 指令）；未跑 solver ✓。
D0: 本档对象 = 二阶泛函 Ψ₂/Z₂ 的 Q=0 特异性判定，及 Q=0 的可拼接性测试
D1: 1（新增：Ψ₂/Z₂ **非 Q=0 特异 ⟹ 淘汰** ✗；doubling 破 Q=0 ✗；乘积非半径-1 覆盖 ✗）

# PSI2-2026-09-26

## §1 ⚠️ 读法纠正（必须先行 ✓）

```
$$\text{唐先生说"n=5 也有 Q=0；n=6 也有 Q=0"}\ ⚠️\ ——\ \text{这只在 }M>K\ \text{时成立}\ ✓,\ \text{在 }M=K\ \text{时\textbf{不成立}}\ ✗$$
$$\textbf{M=K 处实测}: n=4:\ Q=0\ ✓\ (40/40);\quad \textbf{n=5}:\ Q=2\ \textbf{（无 }Q=0\ \text{码）}\ ✗;\quad \textbf{n=6}:\ Q=4\ \textbf{（无 }Q=0\ \text{码）}\ ✗;\quad n=7,8:\ Q=0\ ✓$$
$$\Longrightarrow\ \text{"奇 }n\Rightarrow Q\ge1"\ \textbf{恰恰在小维度就显现}\ ✓\ (n=5,\ E=10>0,\ Q>0\ ✓)\ ——\ \text{唐先生"没显现"的推断源于 }M\ \text{的读法}\ ✗$$
$$

## §2 ⛔ 二阶候选 Ψ₂/Z₂：**非 Q=0 特异 ⟹ 淘汰** ✗

```
$$\Psi_2(C)=\sum_{\substack{x,y\notin C\\ d(x,y)=2}}o(x)o(y)\ ✓,\qquad Z_2=\#\{x,y\notin C:\ d(x,y)=2,\ o(x)=o(y)=0\}\ ✓,\quad o(x)=\mathrm{OC}(B_1(x))\ ✓$$
$$\begin{array}{c|c|c|c}
(n,M) & \text{Q=0 组} & \text{Q>0 组} & \text{判定}\\
\hline
(4,4)=K & \Psi_2\in\{24,26\}\ ✗,\ Z_2=0 & - & \textbf{组内已变化}\ ✗\\
(5,7)=K & - & \Psi_2=184\ ✓,\ Z_2=12\ ✓ & \text{恒定}\ ✓\\
(6,12)=K & - & \Psi_2\in\{924,936\}\ ✗ & \text{组内变化}\ ✗\\
(5,8)>K & \Psi_2=576\ ✓,\ Z_2=0 & \Psi_2\in\{320,536\}\ ✗ & \text{两组分开但随 }E,M\ \text{变}\ ✗\\
(4,5)>K & - & \Psi_2\in\{69,108\}\ ✗ & -\\
\end{array}$$
$$\textbf{按唐先生判据 C}: \text{"若 }\Psi_2\ \text{只随 }E,M\ \text{或普通距离分布变化，就只是另一个统计量，应立即淘汰"}\ ✓$$
$$\Longrightarrow\ \boxed{\Psi_2,Z_2\ \textbf{不携带 Q=0 特有指纹}\ ✗\ —— \textbf{淘汰}}\ ✗✓\ (\text{Q=0 组内自己就变}\ ✗)$$
$$

## §3 ⛔ 可拼接性测试：两个否定 ＋ 一处我方错误被数值抓住 ✓

```
$$\textbf{① doubling}\ (C\mapsto\{(c,0),(c,1)\}\ ✓):\ n=4\ Q=0\ \text{码}\ \longrightarrow\ n=5,M=8:\ \textbf{Q=8}\ ✗$$
$$\qquad\text{理}: b'(x,t)=b(x)+[x\in C]\ ✓\ (\text{推导}\ ✓)\ \Longrightarrow\ \text{码字处重数 }+1\ ✗\ \Longrightarrow\ \text{破 }Q=0\ ✗✓$$
$$\textbf{② product}（\text{我方原以为保覆盖}\ ✗）: \text{实测\textbf{根本非半径-1 覆盖}}\ ✗✓$$
$$\qquad\text{理}: d((x,y),(c_1,c_2))=d(x,c_1)+d(y,c_2)\le2\ \text{一般}\ ✗\ \Longrightarrow\ \text{乘积码覆盖半径为 2}\ ✗\ (\text{我方假设错误，被数值抓住}\ ✓✓)$$
$$\textbf{③ 对照 Hamming}(7,16)\ \text{完美码}: Q=0\ ✓,\ E=0\ ✓,\ o\ \text{分布}=\{0{:}112\}\ ✓\ (\text{与 }E=0\Rightarrow b\equiv1\ \text{一致}\ ✓)$$
$$Z_2\ \text{在极值壳钉住（}0,12,0\ \text{for }n=4,5,6\ ✓\ \text{T1 通过}\ ✓）\ \text{但\textbf{不区分 }Q=0/Q>0}\ ✗\ (n=4\ \text{与 }n=6\ \text{同为 0，}Q\ \text{不同}\ ✗)$$
$$\Longrightarrow\ \textbf{未找到保 }Q=0\ \text{的拼接操作}\ ✗\ \Longrightarrow\ \text{既无 coupling 证据，也无 decoupling 证据}\ ✓$$
$$

## §4 状态与可选下一步

```
$$\textbf{桥仍未打通}\ ✗;\quad \textbf{119 UNKNOWN}\ ✓$$
$$\textbf{候选 ①（generic 球对）已淘汰}\ ✗;\quad \textbf{候选 ③（中点对泛函）尚未测}\ ✗\ (\text{唯一\textbf{已证}特殊几何在 }d(c,c')=2\ ✓)$$
$$\text{选项 A}: \text{测\textbf{中点对泛函 }}\Psi_{\mathrm{mid}}=\sum_{d(c,c')=2}F(m_1,m_2)\ ✓\ (\text{现有代码可测}\ ✓);\ \text{若再无指纹 ⟹ 二阶路线整体降级}\ ✗$$
$$\text{选项 B}: \text{直接攻 }n=9\ \text{数据点}（(9,62)_1\ \text{码，cost 高 ⚠️}）\ ——\ \text{它同时是 C1 与"生死测试"的唯一判决}\ ✓$$
$$
$$

## §5 边界（诚实标注）

- §1 为**实测纠正** ✓（M=K 处 n=5,6 均无 Q=0 码 ✓）；§2–§3 为**数值测试** ✓
- §3② 的我方错误（以为乘积保覆盖 ✗）**已被数值否定** ✓（记录 ✓，未掩盖 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 二阶指纹淘汰 命中文件数=0    :: 
技术词 拼接测试     命中文件数=0    :: 
技术词 乘积非覆盖  命中文件数=0    :: 
技术词 极限壳分界  命中文件数=0    ::
```

- **本档新增**（命中数=0）：二阶指纹淘汰、拼接测试、乘积非覆盖、极限壳分界
- **档案已有（引用，不列为提出）**：—
