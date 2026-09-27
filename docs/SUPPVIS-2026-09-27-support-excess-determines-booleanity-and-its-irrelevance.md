已查地图：已跑 scripts/prework_map_check.sh support 可见性 δ|supp 决定 Booleanity ⟹ 执行自 `NONNEG-2026-09-27`（判死 ✓）＋ 唐先生 09:39 ✓；本档为 **D₀/support-visibility 线的收束**（含一个真结果 ＋ 一个无关性判定 ✓）。
D0: 本档对象 = (supp, δ|supp) 对 Booleanity 的决定性
D1: 1（新增：**(supp,δ|supp) 决定 Booleanity（n=4 穷举 ✓）**；**其对 P1-B 的无关性判定** ✓）

# SUPPVIS-2026-09-27 · δ|supp 决定 Booleanity，且与 P1-B 无关

## §0 结论（先给）

```
$$\boxed{\textbf{(FF-1 真结果)}\ n=4\ \text{穷举}:\ (|\mathrm{supp}|,\delta|_{\mathrm{supp}})\ \text{在}\ \mathrm{Aut}(Q_4)\ \text{轨道下}\ \textbf{完全决定 Booleanity}\ ✓✓}$$
$$\qquad\text{49 个规范轨道，}\textbf{0 个} \text{轨道内 Booleanity 不定};\ \text{纯非 Boolean 轨道 16};\ \text{纯 Boolean 轨道 33}\ ✓$$
$$\qquad\text{（并附：}D_0\ \text{同被 }(\mathrm{supp},\delta|_{\mathrm{supp}})\ \text{决定，0/49 变化 ✓）}$$
$$\boxed{\textbf{(FF-2 无关性 ⚠️)}\ \text{该机制\textbf{与 P1-B 无关}}\ ✗\ \text{——因 P1-A（Booleanity）已\textbf{永久关闭}}\ ✓:\ \text{平凡约束 }x\le1\ \text{即可强制 Boolean}\ ✓\ \text{⟹ 此机制无载荷} \ ⚠️}$$
$$\boxed{\textbf{(FF-3 收束)}\ \text{该线\textbf{封存}}\ ✗\ \text{（强度边界：n=4 穷举 ✓；未外推 }n=10\ ✗;\ \text{对规模下界无影响}\ ✗）}$$
$$
$$
```

---

## §1 (FF-1) 结果与证据（机器验证 ✓）

```
$$\text{数据}:\ n=4\ \text{非负整数 }f,\ \Sigma f\in[4,9],\ b\in[1,3]^{16}:\ \text{共 7860 个解}\ ✓$$
$$\text{标签}:\ (\mathrm{supp}(f),\ \delta|_{\mathrm{supp}})\ \text{规范化到 }\mathrm{Aut}(Q_4)\ \text{（阶 384: 坐标置换＋翻转 ✓）};\ \textbf{标签不含 }f\ ✗✓$$
$$\Longrightarrow\ \text{49 轨道，0 个 Booleanity 不定}\ ✓✓\ \text{（\textbf{首次}在该线上获得\textbf{通过 AMEND-35 而非循环}的结果 ✓）}$$
$$\text{另}:\ D_0=\Sigma f(f-1)\ \text{亦被同一标签决定（0/49 变化 ✓，此为修正后的有效版本 ✓）}$$
$$
$$
```

---

## §2 (FF-2) 为何它对 119 无载荷（关键诚实判定 ⚠️）

```
$$\text{119 的目标（已锁定 ✓）}:\ \text{P1-B}:\ f\in\{0,1\}^{1024}\ \wedge\ Af\ge1\ \Longrightarrow\ \Sigma f\ \ge120?\ \text{（规模下界 ✓）}$$
$$\text{而我们刚证的是 P1-A 侧的事}:\ (C,\delta|_{\mathrm{supp}})\ \text{决定"C 是集合"}\ ✓\ ——\ \text{但 C 本来就是集合}\ ✗$$
$$\qquad\Longrightarrow\ \text{对\textbf{松弛}（非负整数 }f\text{）它确实能把 }f\ \text{压回 Boolean ✓；}\ \text{但 P1-A 已关闭（}x\le1\ \text{即可）}\ ✗\ \text{⟹ 该机制\textbf{不提供规模信息}}\ ✗$$
$$\qquad\boxed{\text{即}:\ \text{"看得见 support"}\ \ne\ \text{"看得见规模"}}\ ✓\ \text{（本轮最重要的边界判定 ✓）}$$
$$
$$
```

---

## §3 (FF-3) 封存与强度边界（AMEND-34 三件套 ✓）

```
$$\textbf{封存}:\ \text{D₀／support-visibility 线}\ ✗$$
$$\textbf{① 证明了}\ ✓:\ n=4\ \text{穷举下 }(\mathrm{supp},\delta|_{\mathrm{supp}})\ \text{决定 Booleanity 与 }D_0\ \text{（0/49 变化 ✓），且标签不含 }f\ ✓$$
$$\textbf{② 因此可判}\ ✓:\ \text{该机制在 support-visibility 意义上\textbf{成立}，但对 119 的}\textbf{唯一靶心（规模下界）}\ \text{无载荷}\ ✗$$
$$\textbf{③ 没有证明}\ ✗:\ n=10\ \text{情形}\ ✗;\ \text{任何规模信息}\ ✗;\ 119\ \text{不存在}\ ✗$$
$$
$$
```

---

## §4 本轮全景（09-27 上午，诚实 ✓）

```
$$\begin{array}{c|c}
\text{项} & \text{状态}\\
\hline
\text{M-1 BQP 提升} & \textbf{KILL}\ ✗\ (\text{循环: }f_u\le1\ \text{改写})\\
\text{M-2A refined-weight LP} & \textbf{KILL}\ ✗\ (\text{档案已做，}=1024/11)\\
\text{M-2A′ surfeit} & \textbf{无入口}\ ✗\ (\text{B 割有效性未证 ＋ pair 链不闭合})\\
\text{M-2B supercode} & \textbf{无入口／DROP}\ ✗\ (\text{嵌入非强迫、非典范})\\
\text{D₀／support-visibility} & \textbf{真结果但无载荷}\ ✓⚠️\ (\text{§2})\\
\hline
\mathbf{P1-A\ Booleanity} & \mathbf{永久关闭}\ ✓✓\\
\mathbf{P1-B\ 规模下界} & \mathbf{唯一靶心}\ ✓\ \text{（}K(10,1)\ge120?\text{）}\\
\mathbf{119} & \mathbf{OPEN}\ ✓
\end{array}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §1 为 **n=4 穷举机器验证** ✓（7860 解、384 阶 Aut、标签不含 $f$ ✓）；规模小 ⚠️，**未外推** ✗
- §2 的"无载荷"为**本档判定** ✓（依据 P1-A 关闭 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；**未**主张该机制在别处无用 ✗
- 本轮未跑 SAT／CP-SAT ✓（穷举为主 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 决定 Booleanity 命中文件数=3    :: ./M2B-2026-09-27-embedding-gate-and-m2ap-status.md ./M2-PREWORK-2026-09-27-refined-weight-lp-already-closed.md ./SUPPVIS-2026-09-27-support-excess-determines-booleanity-and-its-irrelevance.md 
技术词 support-visibility 与规模无关 命中文件数=1    :: ./SUPPVIS-2026-09-27-support-excess-determines-booleanity-and-its-irrelevance.md
```
- **本档新增**：(supp,δ|supp) 决定 Booleanity、support-visibility 与规模无关判定（见上方命中数；0 命中者为自造语／内部标签 ✓）
- **档案已有（引用，不列为提出）**：D₀ 修正版、AMEND-34/35、P1-A 关闭、problem form lock
