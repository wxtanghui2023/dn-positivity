已查地图：已跑 scripts/prework_map_check.sh 球交叠 塌缩 A1/A2 分叉 独立性 ⟹ 执行自 `PHASE2-AUDIT-...-global-pair-collapse`（✓）＋ 唐先生 12:19（two-point 方向 ✓）；本档 = **球交叠塌缩定理 ＋ (A₁,A₂) 分叉的决定性证据** ✓。
D0: 本档对象 = 为何一切覆盖型量都塌缩到 $A_1+A_2$；以及是否存在独立坐标
D1: 2（新增：**球交叠塌缩定理（一行 ✓）**；**n=9 双码的 $(A_1,A_2)$ 分叉证据 ✓✓**）

# 球交叠塌缩定理 ＋ (A₁,A₂) 分叉（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AJ-1 塌缩定理 ✓✓)}\ \big|B_1(c)\cap B_1(c')\big|=\begin{cases}2,&d(c,c')\le2\\0,&d\ge3\end{cases}\ \Longrightarrow\ \textbf{一切球交叠型量只依赖 }A_1+A_2\ \text{（不区分 }d=1,2\text{）} ✗✓}$$
$$\qquad\Longrightarrow\ \text{excess}\ ✓,\ \text{surfeit}\ ✓,\ A_{\le2}\ ✓,\ Q\ ✓,\ \text{profile 方差}\ ✓\ \cdots\ \text{全部只能是 }(A_1+A_2)\ \text{的函数} \Longrightarrow\ \textbf{它们\textbf{必然}塌缩} ✓✓$$
$$\boxed{\textbf{(AJ-2 n=4,5 穷举刚性 ✓✓)}\ n=5,M=7:\ \text{全部 }C(32,7)\ \text{中恰 }\mathbf{320}\ \text{个极小覆盖码};\ \text{其 }\mathbf{全部}\ A=6\ ✓,\ \text{profile}\ \{(1,24),(2,6),(3,2)\}\ \text{唯一}\ ✓,\ T_3=2\ \text{唯一}\ ✓;\ n=4:\ 40\ \text{个，同理} ✓}$$
$$\qquad\text{（连 }S_2,S_{2b},H_H,P_2\ \text{等布置统计量也全部唯一} ✓ ⟹ n=5\ \text{处无布置自由度} ⚠️\text{（规模不足以判独立性）}）$$
$$\boxed{\textbf{(AJ-3 ⚡决定性：}(A_1,A_2)\ \textbf{分叉 ✓✓)}\ n=9,K=62\ \text{的两码}:\ \text{profile 全同}\ ✓,\ A_1+A_2=73\ \text{全同}\ ✓,\ T_3,T_4,S_2,S_{2b},H_H,P_2\ \text{全同}\ ✓}$$
$$\qquad\textbf{但}\ \boxed{(A_1,A_2)=(7,66)\ \text{vs}\ (26,47)}\ ✓✓\ \text{—— }\textbf{分裂量自由} ✓;\ \textbf{距离 }1\ \text{与 }2\ \text{的对数不可由覆盖数据决定} ✓$$
$$\boxed{\textbf{(AJ-4 程序边界 ✓)}\ \text{覆盖数据}\ \Longrightarrow\ \textbf{至多}\ \text{钉住 }A_1+A_2\ ✓;\ \text{更细坐标（}(A_1,A_2)\ \text{分裂、方阵 }I/S\ ✓\text{）}\ \textbf{自由} ✗ \Longrightarrow\ \text{与档案"support/几何层"缺口\textbf{完全一致}} ✓✓}$$
$$
$$
```

---

## §1 塌缩定理（**证明 ✓，一行**）

```
$$\text{对任意两点 }c,c'\in C:\ B_1(c)\cap B_1(c')\ \text{的元素个数} = \begin{cases}2,&d=1\\2,&d=2\\0,&d\ge3\end{cases}\ \text{（Hamming 几何 ✓）}$$
$$\Longrightarrow\ \text{任何形如}\ \sum_{x}\Phi(b(x))\ \text{或}\ \sum_{\{c,c'\}}\Psi\big(|B_1(c)\cap B_1(c')|\big)\ \text{的量}\ \textbf{只通过 }A_1+A_2\ \text{进入} ✓$$
$$\text{实例（本会话已验证 ✓）}:\ \sum_x\binom{b(x)}2=2(A_1+A_2)\ ✓;\ \sum\delta=E\ ✓;\ \sum\delta^2=4(A_1+A_2)-E\ ✓;\ \zeta=M(n^2+2n+2)-(n+2)2^n-4(A_1+A_2)\ ✓$$
$$\Longrightarrow\ \textbf{这解释了为何 excess 与 surfeit 两条路线必然塌缩} ✓✓\ \text{（不是技巧不足，而是球交叠的\textbf{结构性盲区} ✓——满足 G-PROGRESS α ✓）}$$
$$
$$
```

---

## §2 n=4,5 穷举刚性（**✓ 本机**）

```
$$\begin{array}{c|c|c|c|c|c}
n & M=K(n,1) & \#\{\text{极小覆盖码}\}\ (\text{穷举}\ \binom{2^n}{M}\ ✓) & A=A_1+A_2 & \text{profile} & T_3\\
\hline
4 & 4 & 40\ ✓ & 2\ \text{唯一} ✓ & \text{唯一} ✓ & \text{唯一} ✓\\
5 & 7 & \mathbf{320}\ ✓ & 6\ \text{唯一} ✓ & \{(1,24),(2,6),(3,2)\}\ \text{唯一} ✓ & 2\ \text{唯一} ✓\\
\end{array}$$
$$\text{布置统计量（}S_2=35,\ S_{2b}=70,\ H_H=397,\ P_2=21\ ✓\text{）在 320 个码上}\textbf{也全部唯一} ⚠️\ \Longrightarrow\ n=5\ \textbf{无法}判定独立性 ✓$$
$$
$$
```

---

## §3 ⚡决定性证据：$(A_1,A_2)$ 分叉（**n=9, K=62，档案双码 ✓**）

```
$$\text{数据源}:\ \texttt{work/k10/c62/K\_9\_1\_classif.txt}\ \text{（两码，}|C|=62\ ✓\text{）}$$
$$\begin{array}{c|c|c|c|c|c|c|c|c|c}
\text{码} & |C| & A_1 & A_2 & A_1{+}A_2 & T_3 & T_4 & S_2 & S_{2b} & H_H\\
\hline
\#0 & 62 & \mathbf 7 & \mathbf{66} & 73 & 48 & 10 & 558 & 2232 & 128099\\
\#1 & 62 & \mathbf{26} & \mathbf{47} & 73 & 48 & 10 & 558 & 2232 & 128099\\
\end{array}$$
$$\textbf{读数 ✓}:\ \text{profile 全同}\ ✓,\ A\ \text{全同}\ ✓,\ \text{全部球交叠统计量全同}\ ✓\ \Longrightarrow\ \text{\textbf{塌缩定理 (AJ-1) 的实证} ✓✓}$$
$$\qquad\textbf{但 }(A_1,A_2)\ \text{从 }(7,66)\ \text{变到}\ (26,47)\ ✓✓\ \Longrightarrow\ \textbf{分裂自由度存在} ✓\ \text{（这正是唐先生要找的"独立坐标"} ✓\text{）}$$
$$\text{与档案一致 ✓}:\ \text{C62 档记"I/S 分叉 ✓✓"（}\text{方阵量 ✓}\text{＝更细几何坐标 ✓）；本档补上：}\textbf{连 }(A_1,A_2)\ \text{分裂也分叉} ✓✓$$
$$
$$
```

---

## §4 程序边界与 STOP（**带解释的 STOP ✓，满足 G-PROGRESS α ✓**）

```
$$\boxed{\text{覆盖侧信息（一阶覆盖 }b\ge1\ \text{＋球交叠）}\ \Longrightarrow\ \textbf{至多决定 }A_1+A_2\ ✓;\ \text{再细就看不见} ✗}$$
$$\qquad\Longrightarrow\ \text{一切"用覆盖量去压 }A\ \text{"的路线（excess ✓ surfeit ✓ profile 矩 ✓ }\zeta\ ✓\text{）}\ \textbf{在结构上封顶} ✓\ \text{——不是执行不足 ✓（\textbf{解释了此前所有 NO-GO 的必然性} ✓✓）}$$
$$\text{反面（可用方向 ✓）}:\ \text{要见 }d=1\ \text{与 }d=2\ \text{之别，必须用}\textbf{比球交叠更细的几何} ✓:\ \text{方阵／2-面（}I,S\ ✓\text{）、}\binom{d}{2}\ \text{型关联、}\mathrm{Supp}\ \text{结构 ✓}$$
$$\qquad\text{但档案已记 }I/S\ \text{自由分叉 ✓（}\text{＝无约束力} ✗\text{）；且 119 线的"support 层"分析结论 = 十类点态函数族全被钉住 ✗（GAPTHEOREM ✓）}$$
$$\boxed{\textbf{判定}:\ \text{覆盖侧路线}\ \textbf{STOP（带结构解释）} ✓;\ \text{119 状态不变} = \text{OPEN} ✓}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 为**一行定理** ✓；§2 为**穷举计算** ✓（n=5：$C(32,7)$ 全枚举 ✓，320 个 ✓）；§3 为**档案数据复算** ✓✓（决定性 ✓）
- **未**声称解决 119 ✗；**未**声称新机制 ✗；**未**改动 UNKNOWN 状态 ✓
- 本档价值 ✓：把"塌缩"从**现象**升级为**结构性必然** ✓，并首次给出**分裂自由度的具体数据** ✓✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：球交叠塌缩定理、$(A_1,A_2)$ 分叉证据、覆盖侧程序边界
- **档案已有（引用，不列为提出）**：$A_{\le2}$、$\zeta$、excess、profile 刚性、I/S 分叉、GAPTHEOREM、G-PROGRESS


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 球交叠塌缩定理 命中文件数=1    :: ./PHASE2-KEY-2026-09-27-ball-collapse-theorem-and-the-A1-A2-split.md 
技术词 覆盖侧程序边界 命中文件数=1    :: ./PHASE2-KEY-2026-09-27-ball-collapse-theorem-and-the-A1-A2-split.md
```
- **本档新增**：球交叠塌缩定理、$(A_1,A_2)$ 分叉证据、覆盖侧程序边界（见上方命中数；0 命中者为自造语／内部标签 ✓）
