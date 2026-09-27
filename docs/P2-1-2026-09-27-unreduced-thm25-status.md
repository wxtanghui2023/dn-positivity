已查地图：已跑 scripts/prework_map_check.sh SDP Thm2.5 un-reduced 校准 ⟹ 执行自 `DLP1B-2026-09-27`（P0/P1 ✓）＋ 唐先生 11:11（Table 4 oracle ✓）；本档 = **P2-1 未约化实现现状**（模型未改 ✓，仅工程修复 ✓）。
D0: 本档对象 = 未约化 Theorem 2.5 实现与论文 Table 4 外部锚点比对
D1: 1（新增：**本机未约化 harness ＋ 阶梯数据** ✓；**锚点差距 0.0820 的定位假设** ✓）

# P2-1 · 未约化 Thm 2.5 现状（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(LL-1 外部锚点确认)}\ \text{论文 Table 4（}q=2,R=1\text{）}: n=4:3.9999\ |\ n=5:6.6721\ |\ \mathbf{n=6:11.5980}\ |\ \mathbf{n=7:15.9999}\ |\ n=8:31.9999\ |\ n=9:55.3464\ |\ n=10:105.2223\ ✓}$$
$$\boxed{\textbf{(LL-2 Level 0 通过)}\ \text{本机 }n=4:\ \mathbf{L=4.0000}\ \text{vs 论文 }3.9999\ ✓\ \text{（容差内 ✓）}}$$
$$\boxed{\textbf{(LL-3 Level 1 未过)}\ \text{本机 }n=6:\ \mathbf{L=11.5160}\ \text{vs 锚点 }11.5980\ ✗\ \text{（差 }\mathbf{0.0820}\text{）}\ \Longrightarrow\ \textbf{按规程不进 P3}\ ✗}$$
$$
$$
```

---

## §1 实现阶梯（全部为**工程修复**，模型未改 ✓）

```
$$\begin{array}{c|c|c}
\text{配置} & L\ (n=6) & \text{修复内容}\\
\hline
\text{sphere-only} & 11.3716 & \text{（基线）}\\
\text{sphere＋VW，按距离归约 (iv)} & 11.5026 & \text{补 VW 族（论文同款两族 ✓）}\\
\text{sphere＋VW，按 }S_n\text{-对轨道归约 (iv)} & \mathbf{11.515994} & \text{修 (iv) 族归约（含 }M'_{u,w}\text{ 项 ⟹ 平移不保持 ✗）}\\
\hline
\textbf{论文 Table 4} & \mathbf{11.5980} & \text{差 }\mathbf{0.0820}\ ⚠️
\end{array}$$
$$\Longrightarrow\ \text{单调逼近 ✓ 但未命中 ⟹ 继续定位（\textbf{不改模型}} ✗\text{）}$$
$$
$$
```

---

## §2 定位假设（首要 ✓）

```
$$\text{论文自述（}\S1\ \text{末 ✓）}:\ \text{"we focus on a 3-point bound and its symmetry reduction, and }\textbf{strengthen it as much as we can by introducing additional constraints and optimizing the choice of objective function}"\ ✓$$
$$\Longrightarrow\ \text{Table 4 数值 = }\S4.1\ \textbf{强化后}的 Thm 4.9 模型，\textbf{未必}等于未强化的 Thm 2.5\ ⚠️$$
$$\text{故 0.0820 的差额\textbf{很可能}来自 }(\S4.1\ \text{的额外约束／目标优化})\ ✔️\ \text{而非 Thm 2.5 转录错 ✗ —— 待 }\S4.1\ \text{精读 diff 定案 ✓}$$
$$
$$
```

---

## §3 已落地的工程要点（可复用 ✓）

```
$$\text{① 变量 = 3-集轨道（}\mathrm{orb}(u,v)=\mathrm{sort}(d(u,v),|u|,|v|)\ ✓\ \text{Prop 2.1(iv) 全群轨道 ✓；自动含 }M'_{u,u}=M'_{0,u}\ ✓\text{）}$$
$$\text{② 常数矩阵线性组合}\ M'=\sum_t x_tB_t,\ M''=\sum_t x_t(D_t-B_t),\ N=\sum_t x_tH_t\ ⟹ \text{避免 CVXPY 表达式树爆炸 ✓（旧版 MemoryError 已废 ✗）}$$
$$\text{③ }H_t=-\beta D_t+\sum_\ell\lambda_\ell\sum_{w\in S_\ell(0)}E_{\ell,w,t}\ \text{预计算 ⟹ 仿射矩阵映射 ✓}$$
$$\text{④ (iv) 四族按 }S_n\text{-对轨道归约（平移不保持 ⟹ 不可按距离 ✓）}$$
$$\text{⑤ 两族 }(\lambda,\beta)\ \text{并用（sphere ＋ VW ✓，与论文一致 ✓）；}\lambda\ \text{支撑须齐（VW 需 }\ell\le2\ ✓\text{）}$$
$$
$$
```

---

## §4 验证分级（唐先生 11:11 ✓）与当前站位

```
$$\text{Level 0 数学 sanity：}n=4\to4.0000\ ✓\ \textbf{已过}$$
$$\text{Level 1 外部锚点：}n=6\to11.5980\ ?\ \text{（本机 }11.5160\ ✗\text{）};\ n=7\to15.9999\ ?\ \text{（在跑 ✓）}$$
$$\text{Level 2 结构交叉：sphere／VW 分别跑 ✓ 与并用 ✓（已做 ✓）}$$
$$\text{Level 3 两 formulation 吻合：未约化 vs }\S4\ \text{约化}\ \Longrightarrow\ L_{\rm unred}=L_{\rm reduced}\ ?\ \text{（未做 ⚠️）}$$
$$\text{Level 4 推进 }n=10\ ⟹\ 105.2223\ \text{（未到 ⚠️，且禁 brute-force ✗）}$$
$$
$$
```

---

## §5 边界（诚实标注）

- §0–§1 为**本机计算** ✓（SCS，纯工程修复 ✓，**未改模型** ✓）；$n=7$ 结果**未出** ⚠️
- §2 为**假设** ⚠️（未定案 ✓）；**未**主张论文数值有误 ✗
- **自我更正记录** ✓：本轮我曾用 `pkill -f "sdp2[5]\.py"` 触发**自匹配**杀掉自己的 shell ✗（TOOLS.md 明令禁止 ✓）；已改为**按 PID** ✓
- **未**排除 119 ✗；本档不触及 open cell 计算 ✓

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：未约化 Thm 2.5 harness、阶梯数据（11.3716→11.5026→11.5160）
- **档案已有（引用，不列为提出）**：Theorem 2.5/4.9、orbit-basis、Lasserre、matrix cuts、Table 4 锚点


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 未约化 harness 命中文件数=1    :: ./P2-1-2026-09-27-unreduced-thm25-status.md 
技术词 阶梯数据     命中文件数=1    :: ./P2-1-2026-09-27-unreduced-thm25-status.md
```
- **本档新增**：未约化 Thm 2.5 harness、阶梯数据（见上方命中数；0 命中者为自造语／内部标签 ✓）
