已查地图：已跑 scripts/prework_map_check.sh 机制 Q δ 钉住 最优性 ⟹ 执行自 QDELTA-2026-09-26 档；本档为**"什么是机制/什么只是改写"的逐项分类 ＋ 钉住现象的更锐刻画**（唐先生 2026-09-26 12:27 指令）；纯整理＋引用既有实算，未跑 solver ✓。
D0: 本档对象 = 本线各要素的"新性/机制性"分类，及钉住现象的极值刻画
D1: 1（新增：钉住 = 极值 M 现象 的刻画与既有数据核验；新增"空守恒"条目以防误用）

# MECHANISM-2026-09-26 · 钉住 = 极值 M 现象 ＋ 要素分类

## §1 逐项分类（防把恒等式当机制 ✗）

```
$$\begin{array}{c|c|c}
\text{要素} & \text{性质} & \text{能否当"新对象/机制"}\\
\hline
Q^*(n)\ \text{逐 }n\ \text{钉住} & \textbf{机器枚举发现的真现象}（n\le4\ \text{穷举}\ ✓) & \textbf{可以}\ ✓\ (\text{但需机制解释}\ ✗)\\
\delta_i(x)\ \text{层缺陷场} & \textbf{文献对象}（\text{van Wee/Struik/Haas}\ ✓) & \textbf{不可以}\ ✗\ (\text{非我方新造}\ ✓)\\
\delta_i(x)\ge0 & \text{= 覆盖条件的改写}\ ✓ & \text{已用，非新}\ ✗\\
\sum_i\delta_i(x)=E & \boxed{\textbf{空守恒}}（\text{对任意码成立}\ ✓) & \textbf{不可以}\ ✗\ (\text{恒等式，非机制}\ ✓)\\
Q\iff\sum\delta^2\iff\text{色散}\iff A_{\le2} & \textbf{等价改写}\ ✗ & \textbf{不可以}\ ✗\\
\text{尺寸最小性}\Rightarrow\text{私有点} & \textbf{我方证明的真引理}\ ✓\ (\text{无需分类}\ ✓) & \textbf{可以（接口候选）}\ ✓\\
\text{奇偶引理}\ Q\equiv E,\ \textbf{P1} & \textbf{我方推导的真结论}\ ✓ & \textbf{可以（弱通道）}\ ✓\\
\end{array}$$
$$\Longrightarrow\ \text{诚实结论}: \textbf{到目前为止，本线尚未产生"新算子/新机制"}\ ✗;\ \text{产出为\textbf{一个真现象}（钉住）＋ 若干等价坐标 ＋ 两条真引理}\ ✓$$
```

## §2 ⭐ 钉住现象的更锐刻画：**它是极值 M 现象**

```
$$\text{由我方穷举数据}（\text{已存档}\ ✓）:$$
$$\quad n=4:\ M=4{=}K:\ \textbf{40 个覆盖全部 }Q=0\ ✓\ (\text{钉住}\ ✓);\quad M=5:\ 560\ \text{个},\ Q\in\{1{:}480,\ 3{:}80\}\ ✗;\quad M=6:\ 2736\ \text{个},\ Q\in\{2,4,6\}\ ✗$$
$$\quad n=5:\ M=7{=}K:\ \textbf{320 个覆盖全部 }Q=2\ ✓\ (\text{钉住}\ ✓);\quad M=8:\ 8866\ \text{个},\ Q\in\{0{:}603,\ 2{:}5265,\ 4{:}2767,\ 8{:}231\}\ ✗$$
$$\boxed{\textbf{钉住}\iff M=K(n,1)\ (\text{极值});\quad M>K(n,1)\ \text{时 }Q\ \text{自由扩散}\ ✓✓}$$
$$\text{（附}: \text{各 }M\ \text{的 }Q\ \text{取值奇偶与 }Q\equiv E=M(n+1)-2^n\ (\mathrm{mod}\ 2)\ \text{完全一致}\ ✓✓\ ——\ \text{奇偶引理的独立佐证}\ ✓)$$
$$\textbf{意义}: \text{这把问题从"Q 是否 invariant"改写为 \textbf{"极值性（最小 }M\text{）如何单独产生刚性"}}\ ✓$$
$$\qquad\Longrightarrow\ \text{目标机制形态}: \boxed{\text{最小 }M\ \Longrightarrow\ \text{私有点结构}\ \Longrightarrow\ ?\ \Longrightarrow\ Q\ \text{唯一}}\ ✗\ (\text{中间箭头缺}\ ✗)$$
```

## §3 关于"新算子 𝒟"的诚实评估（唐先生的框架 ✓）

```
$$\text{拟议}: \mathcal D:\ C\mapsto\{\delta_i(x)\}_{i,x}\ \text{把"全局最优性"变成"局部缺陷场"}\ ✓$$
$$\textbf{现状}: \text{该映射\textbf{对任意码都有定义}（无需最优性}\ ✓);\ \text{其两条已知性质中，一条是覆盖改写}\ ✓、\text{一条是空守恒}\ ✗$$
$$\qquad\Longrightarrow\ \text{它目前\textbf{并不}携带最优性信息}\ ✗;\ \text{真正缺的仍是"最优性接口"（唐先生難点 4）}\ ✓$$
$$\text{真正可称为"新"的候选（若做出）}: \boxed{\text{一条\textbf{只在最优码成立}、在 }M>K\ \text{时失效的恒等式/不等式}}\ ✓\ ——\ \textbf{可判别的最优性接口}\ ✓✓$$
$$\qquad\text{这类对象天然可测}: \text{用既有 }n=4,5\ \text{穷举数据（}M=K\ \text{vs}\ M>K\ ✓）\ \text{直接筛选}\ ✓$$
```

## §4 下一刀（具体、可判别、且不需新算力 ✓）

```
$$\text{① \textbf{钉住普查}（数据已在手 ✓）}: \text{在 }n=4,5\ \text{穷举集上，对一批统计量逐一判定"在 }M=K\ \text{恒定、在 }M>K\ \text{不恒定"}\ ✓$$
$$\qquad\text{候选统计量}: Q,\ A_{\le2},\ \sum\delta^2,\ \text{色散}\sum_{i\ge1}R_i,\ \text{私有点数},\ G_2\ \text{度数谱},\ \text{层向量 }(\delta_0,\dots,\delta_n)\ \text{的分布}\ ✓$$
$$\text{② 对"最钉住"的那些量，问\textbf{可证来源}}\ ✓\ (\text{优先用私有点引理}\ ✓)$$
$$\text{③ 形成候选} \boxed{\text{最优性接口}}:\ \text{一条只在 }M=K\ \text{成立的不等式}\ ✓\ \text{—— 这才是可写进定理的东西}\ ✓$$
$$\text{④ 纪律}: \textbf{不}跑更大 }n\ ✗;\ \textbf{不}把空守恒当机制\ ✗;\ \textbf{119 保持 UNKNOWN}\ ✓$$
```

## §5 三张表（更新）

```
$$\textbf{CLOSED}: \ldots;\ \textbf{钉住}=\text{极值 }M\ \text{现象（}n=4,5\ \text{数据}\ ✓）;\ \text{奇偶与实算一致}\ ✓;\ \text{尺寸最小性}\Rightarrow\text{私有点}\ ✓$$
$$\textbf{空守恒（新标注，禁止误用）}: \sum_i\delta_i(x)=E\ ✗;\quad \textbf{关闭的假桥}: \text{δ 线性守恒钉住 }Q\ ✗;\ \text{三进制同余}\ ✗;\ \Delta\to A_{\le2}\ ✗$$
$$\textbf{OPEN}: \textbf{最优性接口}（只在 }M=K\ \text{成立的不等式）;\ \text{极值 }M\ \text{刚性机制};\ \text{非取等 }n\ \text{的 }Q^*;\ n=9\ \text{数据点（待定）};\ \textbf{119 UNKNOWN}\ ✓$$
$$

## §6 边界（诚实标注）

- §2 的数据为**我方既有穷举**（已存档 ✓，本轮仅引用与核验奇偶一致性 ✓）
- §3–§4 为**方法论整理** ✓；**未**宣称任何新定理 ✗
- **未跑 solver** ✓；**未**触碰 119 结论 ✗

## 【技术词回查】（定稿前逐字输出）

```
技术词 机制候选     命中文件数=8    :: ./PROTOCOL-R6-support-ceiling.md ./p38-g18-analytic-rigidity.md ./p49-g27-char0-realization-audit.md 
技术词 极值 M 现象  命中文件数=0    :: 
技术词 钉住普查     命中文件数=0    :: 
技术词 空守恒        命中文件数=0    ::
```

- **本档新增**（命中数=0）：钉住普查、空守恒
- **档案已有（引用，不列为提出）**：机制候选
