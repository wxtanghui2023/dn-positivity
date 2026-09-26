已查地图：已跑 scripts/prework_map_check.sh T3 下界 矩松弛 三角形 ⟹ 执行自 P1LB-2026-09-26 档；本档为**P1-LB 收束：可证下界 T₃≥Q₂=38、矩墙 ＋ 战略评估**（唐先生 2026-09-26 16:47 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = T₃ 的矩下界（可证）、矩松弛极值、与目标 48 的间隙、P1 线战略评估
D1: 1（新增：**T₃ ≥ Q₂ = 38 可证** ✓✓；**矩墙定位（差 +10）** ✓✓；**上轮 LP 脚本 bug 弃用** ✗✓）

# P1LB3-2026-09-26

## §1 ✅ **可证下界：T₃ ≥ Q₂ = 38** ✓✓

```
$$\textbf{命题}: T_3=\sum_j\binom j3N_j\ \ge\ \sum_j\binom{j-1}2N_j=Q_2\ ✓✓$$
$$\textbf{证明（一行 ✓）}: \binom j3\ge\binom{j-1}2\ \text{对一切 }j\ge0\ \text{成立}\ ✓;\ \text{且 }j\le2\ \text{时两者皆为 }0\ ✓$$
$$\text{（逐值核验 }j=0..10\ \text{全部通过}\ ✓✓:\ 1\ge1,\ 4\ge3,\ 10\ge6,\ 20\ge10,\ 35\ge15,\ 56\ge21,\ 84\ge28,\ 120\ge36\ ✓)$$
$$\Longrightarrow\ \boxed{T_3\ge Q_2=\mathbf{38}}\ ✓✓;\quad \textbf{取等}\iff N_j=0\ (j\ne3)\ \text{且 }N_1,N_2\ \text{任意}\ \Longrightarrow\ \text{剖面 }(442,32,38,0)\ ✓$$
$$

## §2 ⚠️ **矩墙定位：目标 48 与矩下界 38 差 +10** ✗

```
$$\text{矩松弛（仅用 }\sum N_j=512,\ \sum(j{-}1)N_j=108,\ Q_2=38\ \text{与 }N_j\ge0\ \text{）}: \min T_3=\mathbf{38}\ ✗$$
$$\qquad\text{（取等项 = 参数族 }t=N_4=0\ \text{成员}\ ✓;\ \text{矩可行族含 }N_4\in[0,\ 12.67]\ ✓)$$
$$\text{而目标}: T_3\ge48\iff N_4\ge10\ ✓\ \Longrightarrow\ \textbf{矩（前三阶）\textbf{给不出}} +10\ \text{中的任何部分}\ ✗$$
$$\Longrightarrow\ \boxed{\textbf{需第四阶/几何输入}\ ⚠️\ ——\ \text{与上界路线撞同一堵墙}\ ✓✓}$$
$$\text{（诚实 ✓）}: T_3\ge48\ \text{与}\ N_4\ge10\ \text{是\textbf{同一命题的两个坐标}\ ✗}\ ——\ \text{换坐标提供的是\textbf{工具}（图论/几何），不是新信息}\ ✓$$
$$

## §3 ✗✓ **流程更正（诚实 ✓）**

```
$$\text{我上一轮 }\texttt{p1lb3.py}\ \text{（七重嵌套）超时被弃}\ ✗;\ \text{改写的 }\texttt{p1lb3b.py}\ \text{高斯消元有 bug（解不满足一阶矩）}\ ✗✓$$
$$\qquad\text{其误报"}\min T_3=0\text{"}\ ✗\ \text{已被本档 }\S1\ \text{的可证不等式推翻}\ ✓✓\ (\textbf{真值 38}\ ✓)$$
$$
$$

## §4 P1 线整体评估（诚实的战略结论 ✓）

```
$$\textbf{已确证的刚性（两码全同）}: E=108\ ✓,\ Q_2=38\ ✓,\ A_{\le2}=73\ ✓,\ (N_j)=(432,62,8,10)\ ✓,\ d_{\max}=3\ ✓,\ T_3=48\ ✓,\ \#\triangle=48\ ✓$$
$$\textbf{已否证/封存（本条线累计 12 项）}: \text{局部账本}\ ✗,\ \Psi_2/Z_2\ ✗,\ \Psi_{\rm mid}\ ✗,\ \text{阶梯}\sigma\ ✗,\ \text{私有点复用}\ ✗,\ \text{球不交计数}\ ✗,\ \text{gadget 外溢}\ ✗,\ \text{方阵线}\ ✗,\ \text{影子/容量}\ ✗,\ \text{邻域匹配}\ ✗,\ \text{矩松弛}\ ✗$$
$$\textbf{已证资产}: T_3=\#K_3(G_{\le2})\ \text{普适}\ ✓✓;\ T_3\ge Q_2\ ✓✓;\ p_2\ \text{分叉}\ ✓✓;\ h\le\binom b2\ ✓✓;\ \text{孤立影集不交}\ ✓✓;\ \text{型分解预测 4/4}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{靶心（}N_4\ge10\text{）在\textbf{每一个}已知坐标下都\textbf{恰好等价}，且都比矩层严格强 }\ +10\ ⚠️}$$
$$\qquad\text{即}: \text{这不是"方法不够多"}\ ✗;\ \text{而是\textbf{缺一个本质的新输入}}\ ⚠️\ ——\ \text{候选: 覆盖性的全局约束 / 最优性} M=K\ \text{的未用面}\ ✓$$
$$

## §5 建议（供唐先生裁定 ✓）

```
$$\text{① }\textbf{暂不继续换坐标}\ ✗\ (\text{已验 12 项，同一墙}\ ✓)$$
$$\text{② }\textbf{收束为阶段报告}\ ✓:\ \text{把 }\text{剖面刚性}=\text{矩层刚性}\ \text{这一结论 + 12 项否证 + 6 项资产完整归档}\ ✓$$
$$\text{③ }\text{若继续}: \text{唯一未充分勘探的方向} = \textbf{用 }M=K(n,1)\ \text{的"最优性"本身}\ \text{(van Wee 取等 / NP1CC 机制)}\ ⚠️$$
$$\qquad\text{注}: n=8\ \text{的 }b\le2\ \text{正是由 NP1CC（van Wee 取等 + 分类定理）得到}\ ✓\ ——\ n=9\ \text{是否也有"取等型"定理可用？}\ ⚠️\ \text{(K(9,1)=62 不取等 van Wee}\ ✗\ \text{——— 需检查)}\ ✓$$
```

## §6 边界（诚实标注）

- §1 为**证明＋逐值核验** ✓✓；§2 的矩极值经手算+可证不等式确认 ✓；§3 诚实登记脚本 bug ✗✓
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 三角形下界  命中文件数=1    :: ./P1LB3-2026-09-26-triangle-lower-bound-and-moment-wall.md 
技术词 矩墙           命中文件数=3    :: ./P1LB3-2026-09-26-triangle-lower-bound-and-moment-wall.md ./E10-rank-trace-inertia-joint.md ./C3899d-c3900-hold-and-gamma13-mechanism-precheck.md 
技术词 坐标等价性  命中文件数=1    :: ./P1LB3-2026-09-26-triangle-lower-bound-and-moment-wall.md
```
- **本档新增**（扣自引后 = 0，命中 1 = 自引 ✓）：三角形下界、坐标等价性
- **档案已有（引用，不列为提出）**：**矩墙**（命中 3 文件 ⟹ 非新 ✗，已在 `E10-rank-trace-inertia-joint.md`、`C3899d-c3900-HOLD-and-gamma13-mechanism-precheck.md`）｜T₃、Q₂、N₄
- **档案已有（引用，不列为提出）**：T₃、Q₂、N₄
