已查地图：已跑 scripts/prework_map_check.sh b(c)=1+d1 Q 下界 奇 n 缺口 ⟹ 执行自 BRIDGE-2026-09-26 档；本档为**可导出新下界 ＋ 奇 n 目标收窄**（唐先生 2026-09-26 13:01 指令）；未跑 solver ✓。
D0: 本档对象 = Q 的距离-1 聚集下界及其对 C1 奇 n 缺口的作用
D1: 1（新增：恒等式 b(c)=1+d₁(c) ✓；不等式 Q ≥ Σ_c C(d₁(c),2) ✓；Q=0 ⟹ 距离-1 图为匹配 ✓）

# D1CLUSTER-2026-09-26

## §1 唐先生重写：**确认正确** ✓

```
$$\text{① 偶 }n:\ Q\equiv E\equiv M\ (\mathrm{mod}\ 2)\ ⟹ K\ \text{奇}\Rightarrow Q\ge1\ ✓\ (\text{= 已有 P1}\ ✓)$$
$$\text{② 奇 }n:\ E=M(n+1)-2^n\ \text{偶}\ ✓\ ⟹ Q\ \text{偶}\ ⟹ Q=0\ \textbf{不被奇偶排除}\ ✗\ ⟹ \textbf{真正的 C1 缺口 = 奇 }n\ ✓✓$$
$$\text{③ 桥等价形式}:\ M=K\Longrightarrow\exists x:\ b(x)\ge3\iff Q\ge1\ ✓✓\ (\text{因 }Q=\sum_x\binom{\delta(x)}2\ ✓)$$
$$\text{④ 唐先生 §2--⑤ 的各步（}Q{=}0\Rightarrow b\in\{1,2\}\Rightarrow N_1{=}2^n{-}E,N_2{=}E\Rightarrow N_2{=}2A_{\le2}\ \text{一一对应}\ ✓)\ \text{全部正确}\ ✓$$
$$

## §2 ✅ **本轮新恒等式 ＋ 新不等式**（可证 ✓，已数值核验 ✓）

```
$$\boxed{\textbf{恒等式}:\ \forall c\in C,\quad b(c)=1+d_1(c)}\ ✓✓\ (\text{因 }B_1(c)\ni c\ \text{自身 ＋ 距离-1 码字}\ ✓)$$
$$\qquad\text{数值核验}: \text{全部 4 组数据无一例外}\ ✓✓$$
$$\boxed{\textbf{新不等式}:\ Q=\sum_x\binom{\delta(x)}2\ \ge\ \sum_{c\in C}\binom{d_1(c)}2}\ ✓✓$$
$$\qquad\text{数值核验}: \text{全部 4 组数据成立}\ ✓✓\ (\text{紧性}: (4,4)\ \text{平凡 100\%};\ (4,5)\ 62.9\%;\ (5,7),(6,12)\ 0\%\ ✓)$$
$$\boxed{\textbf{推论}:\ Q=0\ \Longrightarrow\ d_1(c)\le1\ \forall c\in C}\ ✓✓\ (\text{即距离-1 图是\textbf{匹配}}\ ✓)$$
$$

## §3 本轮数据表（极值壳 vs 非极值壳 ✓）

```
$$\begin{array}{c|c|c|c|c}
(n,M) & Q & \sum_c\binom{d_1(c)}2 & \max_c d_1(c) & 2A_1\\
\hline
(4,4)=K & 0\ ✓ & 0\ ✓ & \le1\ ✓ & 0\ \text{或}\ 4\\
(5,7)=K & 2\ ✓ & \textbf{1（恒定）}\ ✓ & \textbf{2（恒定）}\ ✓ & 4\ ✓\\
(6,12)=K & 4\ ✓ & \textbf{0 或 2}\ ✗ & \textbf{0 或 2}\ ✗ & 0\ \text{或}\ 8\ ✗\\
(4,5)>K & 1\ \text{或}\ 3 & 0,1,3\ ✗ & 0..3\ ✗ & 0,2,4,6\ ✗\\
\end{array}$$
$$

## §4 ⭐ 路线评估：**"∃c:\ d₁(c)≥2" 是充分非必要** ✗（诚实否定 ✓）

```
$$\text{充分性}\ ✓:\ d_1(c)\ge2\ \text{某处}\ \Longrightarrow\ Q\ \ge\ 1\ ✓\ (\text{桥达成}\ ✓)$$
$$\text{在 }n=5\ (\text{奇},\ K)\ \text{处它}\ \textbf{被强制}\ ✓✓:\ \sum_c\binom{d_1}2=1\ \text{对全部 320 个码}\ ✓$$
$$\text{但在 }n=6\ (\text{偶},\ K)\ \text{处}\ \textbf{不被强制}\ ✗:\ \sum_c\binom{d_1}2\in\{0,2\}\ ✓,\ \text{却有}\ Q=4\ \text{恒定}\ ✓$$
$$\Longrightarrow\ \text{该路线只能覆盖"以距离-1 聚集实现超额"的码}\ ✗;\ \text{存在"零距离-1 聚集但仍有 }Q>0"\ \text{的码}\ ✓\ (\text{超额经距离-2 通道实现}\ ✓)$$
$$\Longrightarrow\ \textbf{结论}: \text{不能把"距离-1 聚集"当作桥的普遍机制}\ ✗\ (\text{但作为\textbf{充分条件资产}保留}\ ✓)$$
$$

## §5 奇 n 缺口的下一步（按可执行性 ✓）

```
$$\text{① \textbf{奇 }n\ \text{专属}: \text{证"}M=K\ \text{且}\ n\ \text{奇}\ (\text{非 }2^m{-}1)\Longrightarrow\exists c:\ d_1(c)\ge2"\ ✗\ —— \text{局部、具体}\ ✓$$
$$\qquad\text{但注意}: n=7\ (\text{奇},\ \text{完美码})\ \text{有}\ \max d_1=0\ ✗\ ⟹\ \text{命题须排除完美码情形}\ ✓\ (\text{即排除 }Q=0\ \text{的 }2^m{-}1\ ✓)$$
$$\text{② \textbf{距离-2 通道}}: \text{在 }n=6\ \text{上已有"零距离-1 聚集但 }Q>0"\ \text{的码}\ ✓\ \Longrightarrow\ \text{须同时处理距离-2 通道}\ ✓$$
$$\text{③ \textbf{通道分解猜想}}: Q=\sum_c\binom{d_1}2+\ \text{(距离-2 贡献)}\ ✓\ —— \text{是否存在精确分解？}\ ✗\ (\text{待查}\ ✓)$$
$$\text{④ 纪律}: \text{不盲跑 }n=9\ ✗;\ \textbf{119 保持 UNKNOWN}\ ✓$$
$$

## §6 资产/淘汰台账（更新 ✓）

```
$$\textbf{新增资产}: \text{恒等式 }b(c)=1+d_1(c)\ ✓;\ \textbf{不等式 }Q\ge\sum_c\binom{d_1}2\ ✓;\ Q=0\Rightarrow\text{距离-1 匹配}\ ✓$$
$$\textbf{新增淘汰}: \text{"距离-1 聚集"作为桥的\textbf{普遍}机制}\ ✗\ (\text{充分非必要}\ ✓;\ n=6\ \text{反证}\ ✓)$$
$$\textbf{极值特异存活（不变）}: Q,\ A_{\le2},\ N_1,\ \text{剖面}\ ✓;\quad \textbf{119 UNKNOWN}\ ✓$$
$$

## §7 边界（诚实标注）

- §1 为**唐先生推导的确认** ✓（逐条核对 ✓，未发现错误 ✓）
- §2–§4 为**我方推导＋数值核验** ✓（n=4,5 全枚举 ✓；n=6 采样 92 码 ✓）
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 距离1聚集下界 命中文件数=0    :: 
技术词 码字点恒等式 命中文件数=0    :: 
技术词 匹配推论     命中文件数=0    :: 
技术词 充分非必要  命中文件数=3    :: ./C3899i-gamma13-M3-first-cut-gates-G-D-and-M3alpha-registration.md ./lindelof-breakthrough-analysis.md ./p512c1-spectrum-counterexample.md
```

- **本档新增**（命中数=0）：距离1聚集下界、码字点恒等式、匹配推论
- **档案已有（引用，不列为提出）**：充分非必要
