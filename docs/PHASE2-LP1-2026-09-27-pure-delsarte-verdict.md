已查地图：已跑 scripts/prework_map_check.sh Delsarte LP A1+A2 锐界 ⟹ 执行自 `PHASE2-2026-09-27-Qout-attack-opening`（✓）＋ 唐先生 12:12（跑 LP ✓）；本档 = **纯 Delsarte 第一层判定（负结果 ＋ 基线表 ✓）**。
D0: 本档对象 = 纯 Delsarte 约束下 $A_1+A_2$ 的可行区间（对 $M=K(n,1)$）
D1: 1（新增：**基线表 ✓**；**上界方向不可达的判定 ✓**；**LP 自检通过 ✓**）

# 纯 Delsarte LP 判定（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(AF-1 自检通过 ✓)}\ \text{全部实测值落在纯 Delsarte 可行区间内}\ ✓\ \Longrightarrow\ \text{LP 与约定无误 ✓}\ \text{（含有序/无序 ×2 标度 ✓）}}$$
$$\boxed{\textbf{(AF-2 判定：未钉住 ✗)}\ \text{纯 Delsarte }\textbf{不能}给 }A_1+A_2\ \text{的锐界} ✗\ \text{（按唐先生标准 (4)：}\textbf{不登记为"机制找到"} ✗）$$
$$\qquad\text{上界方向（}Q\ \text{所需 ✓）彻底无效 ✗：}n=9:\ 706\ \text{vs 实测 }73\ (10\times)\ ✗;\ n=6:\ 51\ \text{vs }12\ (4\times)\ ✗;\ n=8:\ 256\ \text{vs }16\ (16\times)\ ✗$$
$$\qquad\text{下界方向部分有效 ✓（但仅"偶尔紧" ✓）：}n=4:\ 2=2\ ✓;\ n=8:\ 16=16\ ✓\ (\text{van Wee 取等族 ✓});\ n=5,6,9\ \text{均松} ✗$$
$$
$$
```

---

## §1 LP 设定（**纯 Delsarte ✓，无 excess ✓，按唐先生 (1)(2) ✓**）

```
$$\text{变量}:\ A_0,\ldots,A_n\ \text{（}\textbf{有序}距离分布 ✓）;\quad A_0=M\ ✓;\ \sum_iA_i=M^2\ ✓;\ A_i\ge0\ ✓$$
$$\text{Delsarte/Krawtchouk}:\ \sum_iA_iK_k(i)\ge0\ (k=0..n)\ ✓,\quad K_k(i)=\sum_j(-1)^j\binom ij\binom{n-i}{k-j}\ ✓$$
$$\text{目标}:\ \min/\max\ (A_1+A_2)/2\ \text{（}\textbf{无序} ✓，与实测口径一致 ✓）；方法: HiGHS LP ✓（无整数约束 ✓）}$$
$$
$$
```

---

## §2 基线表（**校正标度后 ✓**）

```
$$\begin{array}{c|c|c|c|c|c|c}
n & M=K(n,1) & E & \text{实测 }A_{\le2} & \text{LP 无序 }[{\rm lo},{\rm hi}] & \lceil E/2\rceil & \text{判定}\\
\hline
4 & 4 & 4 & 2 & [2.000,\ 6.000] & 2 & \text{下界紧 ✓／上界松 ✗}\\
5 & 7 & 10 & 6 & [5.250,\ 19.250] & 5 & \text{两端皆松 ✗}\\
6 & 12 & 20 & 12 & [9.000,\ 51.000] & 10 & \text{两端皆松 ✗}\\
7 & 16 & 0 & 0 & [0.000,\ 87.111] & 0 & \text{平凡 ✓}\\
8 & 32 & 32 & 16 & [16.000,\ 256.000] & 16 & \text{下界紧 ✓／上界松 ✗}\\
9 & 62 & 108 & 73 & [56.188,\ 706.219] & 54 & \text{两端皆松 ✗}\\
\end{array}$$
$$\textbf{自检（✓ 必须 ✓）}:\ n=4,5,6,7,8,9\ \text{的实测值全部 }\in\ \text{LP 区间}\ ✓✓\ \Longrightarrow\ \text{无约定/标度错误 ✓}$$
$$
$$
```

---

## §3 读数与结构性推论（**按 AMEND-31/32 纪律 ✓**）

```
$$\text{① 上界方向（}Q\ \text{所需）✗}:\ \text{纯 Delsarte 的 }hi\ \text{比实测大 }4\times\sim16\times\ ✗\ \Longrightarrow\ \textbf{不可用} ✗\ \text{（Delsarte 本质是"稀疏码"约束 ✓，对密集覆盖码无力 ✓）}$$
$$\text{② 下界方向 ✓ 部分}:\ \max({\rm lo},\lceil E/2\rceil)\ \text{在 }n=4,8\ \text{处恰 = 实测 ✓✓（van Wee 取等族 ✓）；}n=5,6,9\ \text{处仍低于实测 ✗}$$
$$\qquad\Longrightarrow\ \text{与档案一致 ✓（}n\in\{2^m,2^m-1\}\Longrightarrow Q^*=0\ ✓\ \text{走 nearly-perfect ✓）}$$
$$\text{③ 方向结论（结构性 ✓）}:\ \textbf{唯一所需方向（上界）不可由纯 Delsarte 得到} ✗\ \Longrightarrow\ \text{机制必须来自\textbf{覆盖特异}输入 ✓}$$
$$\qquad\text{下步按唐先生 (5) ✓}:\ \text{加入 \textbf{excess/surfeit}（Wu--Chen ✓）耦合 ⟹ 但须先过}\textbf{换皮测试} ✗（若只是 profile 等价重写 ⟹ STOP ✓）}$$
$$
$$
```

---

## §4 边界（诚实标注）

- §1–§2 为本机 LP（HiGHS ✓）＋ 自检 ✓；§3 为判定与结构推论 ✓
- **未**登记任何"机制找到" ✗（按标准 (4) ✓）；**未**改动 119 UNKNOWN ✓
- ⚠️ 更正 ✓：首跑时我误把 LP 输出的**有序**量直接与**无序**实测比对 ✗ ⟹ 已校正（×2 ✓）并加自检门 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：纯 Delsarte 基线表、上界方向不可达判定、LP 自检门
- **档案已有（引用，不列为提出）**：Delsarte/Krawtchouk、$\lceil E/2\rceil$、van Wee 取等、nearly-perfect、Wu--Chen excess


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 纯 Delsarte 基线表 命中文件数=1    :: ./PHASE2-LP1-2026-09-27-pure-delsarte-verdict.md 
技术词 LP 自检门     命中文件数=1    :: ./PHASE2-LP1-2026-09-27-pure-delsarte-verdict.md
```
- **本档新增**：纯 Delsarte 基线表、上界方向不可达判定、LP 自检门（见上方命中数；0 命中者为自造语／内部标签 ✓）
