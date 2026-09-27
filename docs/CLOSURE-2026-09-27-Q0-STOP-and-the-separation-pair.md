已查地图：已跑 scripts/prework_map_check.sh Q0 STOP separation pair A₁−A₂ ⟹ 执行自 `PHASE2-Q0-...-verdict`（✓）／`CLOSURE-...-covering-side-ceiling`（✓）＋ 唐先生 12:26（STOP ＋ 升级 witness ✓）；本档 = **Q0 正式 STOP ＋ separation pair 资产登记** ✓。
D0: 本档对象 = Q0 收口判据；以及下一阶段的分离测试集
D1: 1（新增：**separation pair 正式登记（含 sha256 ＋ 17 项判据清单 ✓）**；**methodological asset ✓**）

# Q0 STOP ＋ separation pair（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AY-1 Q0 = STOP ✓)}\ \zeta+(2^n-M)=(n+1)E-4A\ \text{（码层，无新局部交叉项 ✓）};\ \text{且} = \sum_x\delta(x)(n-\delta(x))\ \text{（δ 矩关系 ✓）}\ \Longrightarrow\ \textbf{不建 QCQP/SDP} ✓}$$
$$\qquad\text{登记类别（唐先生指定 ✓）}:\ \boxed{\textbf{valid / non-profile-appearing quadratic constraint, but no leverage beyond the linear bound }(n+1)E/4}\ ✓$$
$$\boxed{\textbf{(AY-2 方法学资产 ✓✓)}\ \boxed{\text{quadratic appearance}\ \not\Rightarrow\ \text{quadratic information}}\ ✓\ \text{——与 A-BALLCOLLAPSE-1 合并理解 ✓}}$$
$$\boxed{\textbf{(AY-3 判据升级 ✓)}\ U_{\rm new}<U_{\rm Delsarte}\ \text{过弱（闭式界已满足 6/6 ✓ 却无杠杆 ✗）} \Longrightarrow\ \text{新判据}:\ \textbf{必须实质逼近/跨越 }K(n,1)\ \text{所需阈值} ✓}$$
$$\boxed{\textbf{(AY-4 separation pair ✓✓)}\ n=9,K=62\ \text{两码正式升级为下一阶段测试集};\ \text{盲区类 12 项自动淘汰 ✓，分离类 9 项为候选 ✓}$$
$$
$$
```

---

## §1 Q0 收口（**已完成 ✓，见 `4590f89`**）

```
$$\text{Q0-a（是否只是 pair-distance 计数？）}:\ \text{码层 }q\equiv(n+1)E-4A\ ✓\ \text{仅含 }(M,E,A)\ \Longrightarrow\ \textbf{命中} ⟹ \text{STOP} ✓$$
$$\text{Q0-b（是否只是 }\delta^2\ \text{重写？）}:\ q=n\sum\delta-\sum\delta^2\ ✓\ \text{（由逐点 }\delta\le n\ \text{平凡即得）}\ \Longrightarrow\ \textbf{命中} ⟹ \text{STOP} ✓$$
$$\text{均匀点读数（复核 ✓）}:\ x_c=1/11\ \text{处 }M_{\rm relax}=2^n/(n+1)=93.09\ ✓,\ \zeta_{\rm unif}=-1861.82<-930.91\ ✓\ \text{（确有切割力 ✓，但不进入 SDP ✓）}$$
$$\text{正确界（更正后 ✓）}:\ A_1+A_2\le\frac{(n+1)E}{4}\ \text{（}n=4..9:\ 5,\ 15,\ 35,\ 0,\ 72,\ 270\ ✓\ \text{均} <U_{\rm Delsarte}\ \text{但} 2.5\times\sim4.5\times \text{高于实测 ✗）}$$
$$
$$
```

---

## §2 separation pair（**正式资产 ✓✓**）

```
$$\textbf{数据源}:\ \texttt{work/k10/c62/K\_9\_1\_classif.txt}\ \text{（两码，}|C|=62=K(9,1)\ ✓\text{）}$$
$$\text{指纹（可复现 ✓）}:\ \text{码#0}\ \texttt{3639c34b…}\ ✓;\ \text{码#1}\ \texttt{a2fed1d7…}\ ✓$$
$$\begin{array}{c|c|c}
\text{量} & \text{码#0} & \text{码#1}\\
\hline
A_1 & 7 & 26\\
A_2 & 66 & 47\\
A=A_1{+}A_2 & \mathbf{73} & \mathbf{73}\ \text{（相同 ✓）}\\
D=A_1{-}A_2 & \mathbf{-59} & \mathbf{-21}\\
N_2\ (\text{面普查 }q_F{=}2) & 104 & 192\\
N_3 & 6 & 15\\
N_4 & 0 & 3\\
I & 6 & 27\\
S & 126 & 67\\
\sum_F\binom{q_F}2=(n{-}1)A_1{+}A_2 & 122 & 255\\
\end{array}$$
$$\textbf{盲区类（12 项，两码相同 ⟹ 未来候选若同值则自动 DROP ✓）}:$$
$$\qquad\text{profile},\ \sum b,\ \sum b^2,\ A,\ T_3,\ T_4,\ S_2,\ S_{2b},\ H_H,\ P_2,\ \sum\delta(n-\delta),\ N_{\ge5}$$
$$\textbf{分离类（9 项，两码不同 ⟹ 候选 ✓）}:\ A_1,\ A_2,\ D,\ N_2,\ N_3,\ N_4,\ I,\ S,\ \sum_F\binom{q_F}2$$
$$\textbf{用法（β gate ✓）}:\ \text{任何新不变量 }J:\ \text{先在两码上求值};\ J(C_0)=J(C_1)\Longrightarrow J\in\text{盲区（DROP ✓）};\ J(C_0)\ne J(C_1)\Longrightarrow \text{可入 P1/P2 ✓}$$
$$
$$
```

---

## §3 下一阶段 P1（**唯一入口 ✓**）

```
$$\boxed{\text{P1}:\ \textbf{什么最小的 support-level 几何量能看见 }A_1-A_2\ ?\ ✓\ \text{（唐先生 12:26 ✓）}}$$
$$\text{已知可行（分离类 ✓）但不构成机制 ⚠️}:\ N_2,N_3,N_4\ \text{（面普查 ✓——依赖 }A_1\ \text{仿射 ⚠️）};\ I,S\ \text{（自由分叉 ✗ 无约束力 ✓）};\ (n-1)A_1+A_2\ ✓$$
$$\text{必须携带的新信息（判据 ✓）}:\ J\ \text{既需区分两 witness} ✓,\ \text{又需其依赖}\textbf{不可由 }(A_1,A_2)\ \text{解释} ✓$$
$$\text{不再挖（已封顶 ✓）}:\ \zeta,\ \text{excess},\ \text{surfeit},\ \text{profile 矩},\ \text{QCQP/SDP（同层换语言 ✗）}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1 为**收口判据 ＋ 复核** ✓；§2 为**资产登记（含 17 项判据清单 ✓）**；§3 为**下一轮入口** ✓
- **未**声称解决 119 ✗；**未**改动 UNKNOWN ✓；**未**跑未授权的 QCQP ✓（遵唐先生 STOP ✓）
- 本档净收益 ✓：把两个 witness 从"证据"升级为**可复用的 separation pair ＋ 判据清单** ✓；并沉淀方法学资产 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：Q0 STOP 收口、separation pair 登记、判据清单（盲区/分离）、方法学资产
- **档案已有（引用，不列为提出）**：$\zeta$、excess、profile 矩、$I/S$、FACE 档、G-PROGRESS、BALLCOLLAPSE


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 separation pair  命中文件数=1    :: ./CLOSURE-2026-09-27-Q0-STOP-and-the-separation-pair.md 
技术词 判据清单     命中文件数=4    :: ./CLOSURE-2026-09-27-Q0-STOP-and-the-separation-pair.md ./M03-LS-ES-specialization-and-region-subtraction.md ./AUDIT-local-vs-global-satisfiability.md
```
- **本档新增**：Q0 STOP 收口、separation pair 登记、判据清单（盲区/分离）、方法学资产（见上方命中数；0 命中者为自造语／内部标签 ✓）
