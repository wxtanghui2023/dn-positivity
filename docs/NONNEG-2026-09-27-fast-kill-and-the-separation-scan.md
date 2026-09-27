已查地图：已跑 scripts/prework_map_check.sh 非负性 反例约束 区分不变量 Booleanity ⟹ 执行自 `SEAL-2026-09-27`（封存＋AMEND-34 ✓）＋ 唐先生 2026-09-27 09:29 ✓；本档为**终止性实验（两次判停）＋ 区分量扫描**；含穷举 ✓。
D0: 本档对象 = "非负性（$f\ge0$）能否加强格＋盒"与"自然不变量能否分离反例"
D1: 0（两次否定 ＋ 一条尖锐诊断）

# NONNEG-2026-09-27 · 快速判死与区分扫描

## §0 结论（先给）

```
$$\boxed{\textbf{(CC-1 判死)}\ f\ge0\ \textbf{不能}加强格＋盒:\ n=4\ \text{穷举}\ \Sigma f=4..9\ \Longrightarrow\ \text{满足 }b\in[1,3]\ \text{的非负解 }7860\ \text{个，其中 \textbf{2720 个非 Boolean}}\ ✗}$$
$$\qquad\textbf{最小反例}:\ f=(2,1,0,\dots,0,1,1)\ (\Sigma f=5)\ ✓;\ b=(3,3,2,1,2,1,1,1,2,1,1,1,1,1,2,2)\in[1,3]^{16}\ ✓$$
$$\boxed{\textbf{(CC-2 尖锐诊断)}\ \text{在 7 个自然不变量下，Boolean 与非 Boolean \textbf{全部重叠}}\ ✗;\ \text{\textbf{唯一分离量}＝}\max f\ (\text{即 Booleanity 本身})\ ⟹ \textbf{循环}\ ✗✗}$$
$$\qquad\text{即}:\ \text{反例族在一切统计坐标中与 Boolean 族\textbf{相邻}} ⟹ \text{分离必须来自\textbf{非统计}对象}\ ✓\ (\text{与 GAPTHEOREM 诊断一致 ✓})$$
$$
$$
```

---

## §1 (CC-1) 非负性判死（穷举 ✓）

```
$$\text{非负整数 }f\ (\Sigma f\in[4,9])\ \text{穷举}:\ \text{满足 }b\in[1,3]^{16}\ \text{者}\ \mathbf{7860};\ \text{其中非 Boolean}\ \mathbf{2720}\ (34.6\%)\ ✗$$
$$\qquad\Longrightarrow\ \text{按唐先生预设判据（"若连 }f\ge0\ \text{都能产生非 Boolean 反例 ⟹ 该方向迅速判死"）\ } \boxed{\textbf{判死}}\ ✗$$
$$
$$
```

---

## §2 (CC-2) 区分量扫描（§反例驱动循环的"提取被违反结构"步 ✓）

```
$$\begin{array}{c|c|c|c}
\text{不变量} & \text{Boolean 值域} & \text{非 Boolean 值域} & \text{能否分离}\\
\hline
\Sigma f & 4..8 & 5..7 & \text{重叠}\ ✗\\
\Sigma f^2 & 4..8 & 7..10 & \text{重叠}\ ✗\\
\Sigma b & 20..40 & 25..35 & \text{重叠}\ ✗\\
\Sigma b^2 & 28..87 & 47..89 & \text{重叠}\ ✗\\
\#\{b=3\} & 0,1,2,4,5,7 & 2,3,4,5,6,8 & \text{重叠}\ ✗\\
\mathrm{supp}(f) & 4..8 & 4..6 & \text{重叠}\ ✗\\
\text{cut}(f) & 12..22 & 16..24 & \text{重叠}\ ✗\\
\hline
\max f & 1 & 2 & \textbf{完全分离}\ ✓\ \text{——但是\textbf{循环}（}\max f\le1\ \equiv\ \text{Boolean}\ ✗✗\text{）}
\end{array}$$
$$\Longrightarrow\ \boxed{\text{反例驱动循环在此坐标集上\textbf{终止}:\ 无"更弱但仍有效"的约束可得}}\ ✗$$
$$
$$
```

---

## §3 判定与封存（AMEND-34 三件套 ✓）

```
$$\boxed{\text{封存}:\ \text{"以非负性／自然不变量加强格＋盒"方向}}\ ✗$$
$$\textbf{① 证明了}\ ✓:\ n=4\ \text{穷举下}\ f\ge0\ \text{不足（}2720\ \text{反例 ✓）};\ 7\ \text{个自然不变量皆不分离 ✓（唯 }\max f\ \text{分离且循环 ✗）}$$
$$\textbf{② 因此可判}\ ✓:\ \text{该加强方向\textbf{无独立研究入口};\ 反例驱动循环在本坐标集上\textbf{无出口}}\ ✓$$
$$\textbf{③ 没有证明}\ ✗:\ n=10\ \text{情形}\ ✗;\ 119\ \text{不存在}\ ✗;\ \text{"不存在任何非统计分离量"}\ ✗\ \text{（只证所试 7 项不足 ✓）}$$
$$\Longrightarrow\ 119\ \text{仍}\ \mathbf{OPEN}\ ✓$$
$$
$$
```

---

## §4 本刀的两条正面副产品（诚实 ✓）

```
$$\text{① }\textbf{诊断再确认}\ ✓:\ \text{Boolean 族与非 Boolean 族在全部自然统计坐标上\textbf{相邻}}\ ⟹\ \text{gap 是}\textbf{support／全局}型}\ ✓\ \text{（第 3 次独立确认 ✓）}$$
$$\text{② }\textbf{反例驱动循环可判停}\ ✓:\ \text{本档给出其"无出口"的实例} ——\ \text{该循环仅在存在"更弱且不循环"的分离量时可用 ✓（否则立即终止 ✗）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0–§2 为 **n=4 穷举** ✓（$\Sigma f\in[4,9]$ ✓，7860 解 ✓）；规模小 ⚠️，未外推 ✗
- §3 的封存为**机制级** ✓（非"119 不可解" ✗）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；未跑 SAT/CP-SAT ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 非负性判死  命中文件数=1    :: ./NONNEG-2026-09-27-fast-kill-and-the-separation-scan.md 
技术词 区分量扫描  命中文件数=1    :: ./NONNEG-2026-09-27-fast-kill-and-the-separation-scan.md
```
- **本档新增**：非负性判死、区分量扫描（7 项）（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：格＋盒 (LOCAL＝LATTICE)、n=4 证人、GAPTHEOREM 诊断、AMEND-34
