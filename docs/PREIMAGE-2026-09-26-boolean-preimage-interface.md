已查地图：已跑 scripts/prework_map_check.sh 119 Boolean preimage 整数性 局部相容 ⟹ 执行自 `FOURGATE-2026-09-26`（四门链 ✓）＋ `LGREEN1-2026-09-26`（核混号 ⟹ 仅杀连续路 ✓）；本档为**接口重定位并首攻**（唐先生 2026-09-26 22:21 令 ✓）；含精确计算 ✓。
D0: 本档对象 = $b\in\mathbb Z^{1024}_{\ge1},\ \sum b=1309,\ Gb\in\{0,1\}$ 的离散整数 preimage（既有对象，**重新定向** ✓）
D1: 1（新增：**精确有理核** ✓✓、$G^2$ 核与二阶必要条件 ✓、**局部整数性同余（非平凡 ✓）** ✓）

# PREIMAGE-2026-09-26 · Boolean preimage 接口

## §0 诊断重定位（唐先生 22:21 ✓）

```
$$\boxed{\text{119}:\quad A_1\text{-route BLOCKED}\ \ne\ \text{119 problem BLOCKED}}\ ✓$$
$$\qquad\text{理由}:\ \text{119 是\textbf{有限}存在性（}2^{10}=1024\text{）};\ A_1\le49\ \text{只是 consequence} \Longrightarrow\ \text{此前"只攻 }A_1\text{"是\textbf{人为收窄}}\ ⚠️$$
$$\qquad\textbf{Green NO-GO 的精确范围}:\ \text{仅杀死\textbf{连续／序结构}（positive kernel ⟹ maximum principle）};\ \textbf{离散整数 preimage 未审计}\ ✓✓$$
$$
$$
```

---

## §1 精确核（本档精确算出 ✓✓）

```
$$\text{递推}\ h_i+i\,h_{i-1}+(10-i)\,h_{i+1}=\delta_{i0}\ \text{（有理数精确解 ✓）}:$$
$$g_0=\tfrac1{11},\ g_1=\tfrac1{11},\ g_2=-\tfrac2{99},\ g_3=-\tfrac2{99},\ g_4=\tfrac8{693},\ g_5=\tfrac8{693},\ g_6=-\tfrac{16}{1155},\ g_7=-\tfrac{16}{1155},\ g_8=\tfrac{128}{3465},\ g_9=\tfrac{128}{3465},\ g_{10}=-\tfrac{256}{693}\ ✓$$
$$\textbf{公分母}\ D=\mathrm{lcm}=3465=5\cdot7\cdot9\cdot11\ ✓;\quad \textbf{系数}\ D g_i=(315,315,-70,-70,40,40,-48,-48,128,128,-1280)\ ✓$$
$$\qquad\text{（结构：}g_{2j}=g_{2j+1}\ ✓;\ \text{符号交替块 }\ +++---+++\ \text{型 }\ ✓\ \text{——\textbf{混号} ⟹ 无最大原理 }\ ✓\text{）}$$
$$
$$
```

---

## §2 二阶必要条件（本档新 ✓）

```
$$\langle b,G^2b\rangle=\langle f,f\rangle=|f|=119\ \Longrightarrow\ \langle\delta,G^2\delta\rangle=119-\tfrac{1024}{121}-\tfrac{2\cdot285}{121}=\mathbf{105.8264}\ ✓$$
$$\qquad(G^2\ \text{核}\ q_i\ \text{亦\textbf{混号}}:\ q_1=q_2<0,\ q_3=q_4>0,\ q_5=q_6<0,\ q_7=q_8>0,\ q_9=q_{10}<0\ ✓)$$
$$\textbf{判定}:\ \lambda_{\min}(G^2)\|\delta\|^2=\tfrac{287}{121}=2.37\ \le\ 105.83\ \le\ \lambda_{\max}(G^2)\|\delta\|^2=287\ ✓\ \Longrightarrow\ \textbf{不矛盾}\ ✗$$
$$
$$
```

---

## §3 ⭐ 局部整数性（**非平凡** ✓✓）

```
$$f(x)\in\{0,1\}\ \Longrightarrow\ D\,f(x)=\sum_i (Dg_i)\,N_i(x)\ \equiv\ 0\ (\mathrm{mod}\ D)\ ✓\quad N_i(x)=\sum_{d(x,y)=i}b(y)\ ✓$$
$$\textbf{非平凡性检验（本档 ✓）}:\ \text{对"均匀型"配置 }N_i(x)=c\,\binom{10}{i}\ (c=1,2,3):\quad \sum_i(Dg_i)\binom{10}{i}c=315c\ \not\equiv 0\ (\mathrm{mod}\ 3465)\ ✗$$
$$\qquad\Longrightarrow\ \text{均匀 }b\ \text{型被\textbf{排除}}\ ✓\ \Longrightarrow\ \text{该同余\textbf{确有内容}（非恒真 ✓）}\ ✓✓$$
$$\textbf{与既有关系}:\ \text{它\textbf{弱于} }f\in\{0,1\}\ ✓\ \text{但\textbf{强于}空条件};\ \text{等价物＝"}\mathbb Z\ \text{可解性"（整数 preimage 的一阶必要条件 ✓）}$$
$$
$$
```

---

## §4 moment 探针塌缩（诚实 ✗）

```
$$\langle f,f\rangle=119\iff|f|=119\ \text{（已给定）}\ ✗;\qquad \langle f,A^kf\rangle=\text{长度-}k\ \text{walk 数}\iff\{A_j\}\ \text{距离分布}\ \Longrightarrow\ \textbf{回到 A-族}\ ⚠️$$
$$\Longrightarrow\ \textbf{moment 探针坍缩};\ \text{未坍缩者只剩}:\ \text{(i) 精确 }0/1\ \text{条件（＝原问题 ⚠️）};\ \text{(ii) \textbf{局部整数性}（§3 ✓）}$$
$$
$$
```

---

## §5 判定与下一步（四门链适用 ✓）

```
$$\textbf{本档四项的四门判定}:\quad \text{精确核}\ (\text{工具}\,✓);\ \text{二阶条件}\ (N\,✓\ I\,✓\ \text{敏感}\,✓\ \text{方向：等式 ✓}\ \Longrightarrow\ \textbf{过四门，但不 bite}\ ✗)$$
$$\qquad\text{局部整数性同余}:\ N\,✓;\ I\,✓;\ \text{敏感}\,✓\ (\text{依赖 }N_i(x)\notin\langle A_1,A_2\rangle\ ✓);\ \text{方向}:\ \text{等式（双侧）}✓ \Longrightarrow\ \boxed{\textbf{过四门，bite 待定}\ ⚠️✓}$$
$$\textbf{未坍缩的活口}:\ \boxed{\text{局部整数性}:\ \text{在 }b\in\{1,2,3\}^{1024},\ \sum b=1309\ \text{＋ profile 下，同余 }D f(x)\equiv0\ \text{是否可满足？}}\ ✓$$
$$\qquad\textbf{下一步候选（有界 ✓）}:\ \text{对 §3 的同余做\textbf{可行性判定}（可用小规模 ILP／CP，或先做代数分析 ⚠️）—— 这是本线首次出现"}\boxed{\text{整数性}}{\text{型}}$ 障碍候选 ✓$$
$$
$$
```

---

## §6 边界（诚实标注）

- §1 为**精确有理数解** ✓（可独立复核 ✓）；§2、§3 为**本档计算** ✓
- §3 的"非平凡"仅指**排除均匀型** ✓，**未**证明它对真实 profile bite ✗（待 §5 ✓）
- §4 的"坍缩"为**本档判定** ✓；**未**主张 preimage 接口无用 ✗（只主张其 moment 探针坍缩 ✓）
- **未**排除 $Q=1$ ✗、**未**排除 119 ✗；本轮未跑 solver ✓（仅精确线性代数 ✓）

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 精确有理核  命中文件数=1    :: ./PREIMAGE-2026-09-26-boolean-preimage-interface.md 
技术词 Boolean preimage 接口 命中文件数=1    :: ./PREIMAGE-2026-09-26-boolean-preimage-interface.md 
技术词 局部整数性同余 命中文件数=1    :: ./PREIMAGE-2026-09-26-boolean-preimage-interface.md
```
- **本档新增**：精确有理核、Boolean preimage 接口、局部整数性同余（见上方命中数；0 命中者为自造语 ✓）
- **档案已有（引用，不列为提出）**：Green 核（LGREEN1）、四门链（AMEND-32）、profile (740,283,1)、$|f|=119$
