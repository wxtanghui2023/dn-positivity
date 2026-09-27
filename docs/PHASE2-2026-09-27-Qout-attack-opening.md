已查地图：已跑 scripts/prework_map_check.sh Q_out 双通道 距离分布 Delsarte 换皮 ⟹ 执行自 `ABOUND-2026-09-27-phase1`（归约 ✓）＋ 唐先生 12:10（攻 $Q_{\rm out}$ ✓）；本档 = **第二阶段开刀：$Q_{\rm out}$ 的归约与换皮测试** ✓。
D0: 本档对象 = $Q_{\rm out}$ 的上界机制（$M=K$ 下）
D1: 1（新增：**覆盖-距离桥 $2A_{\le2}=2(A_1+A_2)$ ✓**；**换皮测试判定 ✓**）

# 第二阶段 · $Q_{\rm out}$ 开刀（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AE-1 覆盖-距离桥 ✓✓)}\ \sum_x\binom{b(x)}2=2A_{\le2}=2(A_1+A_2)\ \Longrightarrow\ \boxed{A_{\le2}=A_1+A_2}\ ✓\ \text{（}\equiv\text{距离}\le2\ \text{的码字对 ✓）}}$$
$$\qquad\Longrightarrow\ \boxed{Q=2(A_1+A_2)-E}\ ✓\ \text{—— \textbf{把 $Q$ 从"覆盖侧"接到"距离分布侧"} ✓✓}$$
$$\boxed{\textbf{(AE-2 换皮测试判定 ⚠️)}\ \text{朴素的 }Q_{\rm out}\ \text{界（经码字对计数）}\equiv\textbf{换皮} ✗\ \Longrightarrow\ \text{按 AMEND-30/31 立即 STOP} ✗}$$
$$\qquad\text{原因：}Q_{\rm out}=\sum_{x\notin C}\binom{b(x)-1}2\ \text{的"配对解释"}\ (=A_{\le2}\ \text{的一部分})\ \text{只给出总量恒等式 ✓，不含 }M=K\ \text{特异信息 ✗}$$
$$\boxed{\textbf{(AE-3 非换皮机制候选 ✓)}\ \text{唯一可用通道} = \textbf{距离分布侧}:\ \text{Delsarte/Krawtchouk 型 LP ＋ 覆盖（excess/Wu--Chen）耦合 ✓\ \text{（档案已有先例：Delsarte}\times\text{覆盖}\Rightarrow A_1\le49\ ✓）}}$$
$$
$$
```

---

## §1 覆盖-距离桥（**证明 ✓，一行**）

```
$$\sum_x\binom{b(x)}2=\#\{(\{c,c'\},x):\ x\in B_1(c)\cap B_1(c')\}=\sum_{\{c,c'\}}\big|B_1(c)\cap B_1(c')\big|\ ✓$$
$$\text{而 }|B_1(c)\cap B_1(c')|=\begin{cases}2,&d(c,c')\le2\\0,&d(c,c')\ge3\end{cases}\ ✓\ \text{（Hamming 球交叠 ✓，已在档案多次使用 ✓）}$$
$$\Longrightarrow\ \sum_x\binom{b(x)}2=2\cdot\#\{\text{距离}\le2\ \text{的对}\}=2(A_1+A_2)\ ✓\qquad\square$$
$$\textbf{数据核对（本机 ✓）}:\ n=4:A_1+A_2=2\ \Rightarrow 2\cdot2=4=2A_{\le2}\ ✓;\ n=5:6\to12\ ✓;\ n=6:12\to24\ ✓;\ n=9:73\to146\ ✓\ \text{（与档案 }2A_{\le2}=146\ ✓✓\text{）}$$
$$
$$
```

---

## §2 换皮测试（**纪律执行 ✓**）

```
$$\text{朴素路线}: \text{用"码字对"给 }Q_{\rm out}\ \text{上界 ⟹ 把 }Q_{\rm out}\ \text{化成 }A_{\le2}\ \text{的份额 ⟹ 得 }Q_{\rm out}\le2A_{\le2}\ ✓\ \text{型陈述}$$
$$\Longrightarrow\ \text{但这是 }\textbf{对任意码都成立的总量恒等式} ✗\ \text{（§1 ✓，无 }M=K\ \text{输入 ✓）}\ \Longrightarrow\ \textbf{换皮} ✗\ \Longrightarrow\ \textbf{STOP} ✓（AMEND-30/31 ✓）$$
$$\text{档案同类关闭 ✓}:\ \delta\text{-守恒}\ ✗;\ \text{private 总量＝剖面换皮}\ ✗;\ P_2\ ✗\ \text{（B-2026-09-26 §"已淘汰" ✓）}$$
$$\textbf{推论}:\ Q_{\rm out}\ \text{自身在 }M=K\ \text{下\textbf{没有独立机制} ⚠️ —— 必须借 }Q=2(A_1+A_2)-E\ \text{把问题\textbf{整体}转到距离分布侧 ✓（§3 ✓）}$$
$$
$$
```

---

## §3 非换皮机制（**主攻方向 ✓**）

```
$$\text{目标重写}:\ \boxed{M=K(n,1)\ \Longrightarrow\ A_1+A_2\ \text{被钉住（或锐上界）}}\ ✓\ \text{—— 这是\textbf{距离分布}命题 ✓，可用 LP/组合工具 ✓}$$
$$\text{可用工具（档案有先例 ✓）}:\ \text{(a) Delsarte/Krawtchouk 不等式（}A_i\ \text{的线性约束 ✓）};\ \text{(b) 覆盖条件的 excess/surfeit 表述（Wu--Chen ✓）};\ \text{(c) 二者耦合（档案：Delsarte}\times\text{覆盖}\Rightarrow A_1\le49\ ✓）}$$
$$\text{第二阶段第一步（可算 ✓）}:\ \text{对 }n=5,6,9\ \text{建 LP}:\ \min/\max(A_1+A_2)\ \text{s.t. Delsarte ＋ }\sum_iA_i=M\ \text{（＋覆盖的 excess 约束 ✓）}$$
$$\qquad\Longrightarrow\ \text{与实测 }(A_1+A_2=6,\ 12,\ 73\ ✓)\ \text{比对}:\ \text{若 LP 已把 }\max(A_1+A_2)\ \text{压到实测值 ⟹ 机制找到 ✓✓；若 LP 松 ⟹ 需 excess 耦合 ⚠️}$$
$$
$$
```

---

## §4 边界与下一步

```
$$\text{① §1 为恒等式 ✓（本机核算 ✓）；§2 为\textbf{纪律判定}（STOP 朴素路线 ✓）；§3 为\textbf{计划}（未执行 ⏳）}$$
$$\text{② 下一步（立即可算 ✓）}:\ n=5,6,9\ \text{的 }A_1+A_2\ \text{LP 上下界 ⟹ 判定 §3 是否成立 ✓}$$
$$\text{③ 若 LP 通过 ⟹ }Q\ \text{上界机制建立 ✓；若 LP 松 ⟹ 转 excess 耦合（Wu--Chen ✓）⟹ 若仍松 ⟹ STOP（避免循环 ✓）}$$
$$\text{未}主张任何机制已成功 ✗；\text{未}改动 119 UNKNOWN 状态 ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：覆盖-距离桥、换皮测试判定、$A_1+A_2$ 的 LP 化
- **档案已有（引用，不列为提出）**：$A_{\le2}$、$Q=2A_{\le2}-E$、球交叠常数、Delsarte、Wu--Chen excess、FAILSET


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 覆盖-距离桥 命中文件数=1    :: ./PHASE2-2026-09-27-Qout-attack-opening.md 
技术词 换皮测试判定 命中文件数=1    :: ./PHASE2-2026-09-27-Qout-attack-opening.md
```
- **本档新增**：覆盖-距离桥、换皮测试判定、$A_1+A_2$ 的 LP 化（见上方命中数；0 命中者为自造语／内部标签 ✓）
