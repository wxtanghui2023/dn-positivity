# R2-2$'$-2026-09-27 — **近最优不可约 support 分离**：**机制构造**（零计算）＋ 缺口定位

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 21:49 令 ✓）**：**只做 R2-2$'$**（$119\le|C|\le123$ 的近最优不可约分离）；**不进门②** ✗；**不开新候选课题** ✗；**不重审已关闭四路线** ✗；**零计算** ✓。

**已查地图：命中（接续 R2-2 与 P12-PASS，非新案 ✓）**
所查：`docs/R2-2-2026-09-27-n10-support-layer-separation-constructible-and-free-coordinate-lemma.md`（**提升引理＋自由坐标引理** ✓✓）｜`docs/P12-PASS-2026-09-27-…`（$n=8$ 见证 ✓✓）｜`docs/P1-5-2026-09-27-…`（A 型＋两门 ✓✓）｜`docs/119-ATTACK-R1-2026-09-27-…`（四方向普查 ✓）｜`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §8）
D0: 本档对象 ＝ **档案已有** R2-2$'$ 问题的**机制构造与缺口定位**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次把 $A$-不变性归约到等距切换并给出 3 行证明** ＋ **平移对载体** ⟹ 缺口精确定位 ✓）
**[RESEARCH]**

---

## §0 结论（**分支落位 ＋ 机制已得 ✓**）

$$\boxed{\textbf{机制成立（可证 ✓）}:\ \text{等距切换}\ \Longrightarrow\ \textbf{保持全部距离层、只改坐标支撑分配}}$$
$$\boxed{\text{载体}:\ \textbf{平移对族}\ C=D\cup(D+x),\quad |C|=2|D|\in\{120,122\}\ \subseteq[119,123]\ ✓\ \text{（\textbf{不受}自由坐标引理排除 ✓）}}$$
$$\boxed{\text{缺口}:\ \textbf{存在性}（D,\rho,t,x\ \text{使双平移并覆盖且 }C\ \text{不可分}）——\ \text{机制非缺口，存在性是缺口}}$$
$$\boxed{\text{分支落位}:\ \textbf{③ HOLD（但为"带具体机制的 HOLD"）}}:\ \text{既未构造出}\ [119,123]\ \text{的分离对，也未能证明其不存在}\ ✓$$

---

## §1 目标（照唐先生逐字 ✓）

$$\boxed{119\le|C|\le123,\qquad A(C)=A(C'),\qquad J(C)\ne J(C'),\quad \text{二者均\textbf{半径 1 覆盖}且\textbf{坐标不可约}}}✓$$
$$\text{排除的伪路线（自由坐标引理 ✓）}:\ C=D\times\mathbb F_2\Longrightarrow|C|\ge2K(9,1)=124\ \Longrightarrow\ \textbf{8D 见证}\times\mathbb F_2^k\ \text{不可用}\ ✗✓$$

---

## §2 框架：**层和 vs 坐标向量上的限制**（本档的语言 ✓✓）

$$\gamma_C(v):=\#\{(a,b)\in C^2:\ a\oplus b=v\}\ ✓\quad(\text{自相关});\qquad A_i(C)=\sum_{|v|=i}\gamma_C(v)\ ✓$$
$$\textbf{关键}:\ A\ \textbf{只固定 }\gamma\ \text{的\textbf{层和}}\ \Big(\sum_{|v|=i}\gamma(v)\Big)\ ✓;\qquad \textbf{支撑层 }＝\ \gamma\ \text{限制在\textbf{坐标向量}}\ \{e_i\}_{i}\cup\{e_i\oplus e_j\}_{i<j}\ ✓✓$$
$$q_{ij}=\tfrac12\gamma_C(e_i\oplus e_j)\ ✓;\qquad d_1\ \text{数据}=\gamma_C(e_i)\ ✓$$
$$\Longrightarrow\ \boxed{\text{分离问题}\ \equiv\ \gamma\ \text{在坐标向量上的取值能否变，而层和不变}？}\ ✓✓\ \text{（相位语言：}A=|Ĉ|^2\ \text{型数据；支撑}=\text{相位可见部分}\ ✓）$$

---

## §3 载体：**平移对族**（$|C|=120,122$ ✓）

$$C=D\cup(D+x)\ (x\ne0)\ \Longrightarrow\ |C|=2|D|\ \Longrightarrow\ |D|=60\Rightarrow|C|=120;\ |D|=61\Rightarrow|C|=122✓$$
$$\gamma_C(v)=2\gamma_D(v)+2\gamma_D(v\oplus x)\ \Longrightarrow\ \boxed{A_i(C)=2\big[A_i(D)+A_i(D,x)\big]}\ ✓\ \big(A_i(D,x):=\textstyle\sum_{|v|=i}\gamma_D(v\oplus x)\big)$$
$$\Longrightarrow\ \boxed{A(C)=A(C')\iff A_i(D,x)=A_i(D,x')\ \ \forall i}\ ✓✓\ \text{（把 }A\text{-等价\textbf{归约到"移位剖面相等"}}✓)$$
$$\text{支撑数据}:\ q_{ij}(C)=\gamma_D(e_i\oplus e_j)+\gamma_D(e_i\oplus e_j\oplus x)\ ✓\ \Longrightarrow\ \text{只依赖 }\{\gamma_D(\cdot\oplus x)\}\ \text{在坐标向量上的限制 ✓}$$

---

## §4 ★**机制（A-不变性，3 行可证 ✓✓）**

$$\text{设 }\sigma\ \text{为 Hamming 等距（}\text{permute coords}\rtimes\text{translate}\text{）},\ \text{且 }\sigma(D)=D\oplus t\ (\text{仿射保 }D)\ ✓;\quad x':=\sigma(x)\ ✓$$
$$\text{(i) 层和不变 ✓}:\ A_i(D,x')=A_i\big(\sigma(D),\sigma(x)\big)=A_i(D,x)✓\ \text{（}\sigma\ \text{等距 ⟹ 保权重 ✓）};\ \text{再由 }\sigma(D)=D\oplus t\ \text{与平移不变性 ✓}$$
$$\text{(ii) 支撑变 ✓}:\ q_{ij}(C')-q_{ij}(C)=\gamma_D(e_i\oplus e_j\oplus x')-\gamma_D(e_i\oplus e_j\oplus x)\ \text{—— 当 }\sigma\ \text{不保坐标向量集时\textbf{一般非零}}✓$$
$$\Longrightarrow\ \boxed{\text{取 }C=D\cup(D+x),\ C'=D\cup(D+x')\ \text{（同一 }D\text{！）}:\ A(C)=A(C')\ \text{而 support 不同}}\ ✓✓$$
$$\textbf{（与 }n=8\ \text{同构 ✓）}:\ \text{那里的切换参数是"两半对齐 }(\pi,e)\text{" ✓；此处是"等距 }\sigma\text{" ✓ —— \textbf{同一机制，换载体} ✓✓}$$

---

## §5 与自由坐标引理的关系（**此族不被排除 ✓**）

- 平移对 $C=D\cup(D+x)$ **不是** $E\times\mathbb F_2$ 形式 ⟹ 自由坐标引理**不适用** ⟹ $|C|=120,122$ **可以做近最优** ✓✓
- **但不可分性必须逐例核** ✓（可核判据：$\exists i$ 使 $C=E\times\mathbb F_2$ ⟺ 第 $i$ 坐标在 $C$ 上"自由" ⟺ $C$ 的两个第 $i$ 坐标半空间相等 ✓）

---

## §6 缺口定位（**机制 ≠ 缺口** ✓）

| 项 | 状态 |
|---|---|
| **A-不变性机制** | ✅ **已得**（§4 三行证明 ✓） |
| **支撑可分离性** | ✅ **已得**（同 $D$、异 $x$ ✓） |
| **存在性**（$D$ ＋ $\sigma,t,x$，使 $D\cup(D+x)$、$D\cup(D+x')$ **均覆盖** $\mathbb F_2^{10}$） | ⚠️ **未得** ⟹ **本档缺口** |
| **不可分性** | ⚠️ 须逐例核（§5） |
| **奇偶观察** ✓ | 平移对族只给**偶数** $|C|$ ⟹ **$|C|=119$（奇）须换载体**（如三元组 $D\cup(D+x)\cup\{y\}$，$|C|=121,123$ 亦可由 $|D|=60,61$ 加一元得 ✓） |
$$\Longrightarrow\ \text{分支落位（照唐先生三分支 ✓）}:\ \text{未构造 ⟹ 非①};\ \text{未证不存在 ⟹ 非②} \Longrightarrow \boxed{\textbf{③ HOLD（带机制）}}✓$$

---

## §7 与门②的接口（**下一步的精确形态** ✓）

$$\text{门②需要}:\ |C|=119\Longrightarrow J\in\mathcal J_{\rm impossible}\ ✓;\qquad \text{本档给出的接口}:\ \text{把 }J\ \text{写成 }\gamma\ \text{在坐标向量上的线性/二次泛函 ⟹ 与 \textbf{§4 的 }A\text{-不变性方向正交 ✓}$$
$$\text{（即：}A\text{-纤维（固定层和的自相关族）内的 }J\text{-变化 = 门② 的作用域 ✓）}$$

---

## §8 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "平移对"
技术词 平移对          命中文件数=3    :: ./PLAN-2026-09-25-K10-1-next-direction-and-difficulty-breakdown.md ./P2-2026-09-26-structure-probe-and-deletion-verdict.md ./B1b-owner-structure-engine-and-results-d1-d4.md
$ bash scripts/tech_word_check.sh "等距移位"
技术词 等距移位        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "自同构切换"
技术词 自同构切换      命中文件数=0    ::
$ bash scripts/tech_word_check.sh "层和"
技术词 层和            命中文件数=6    :: ./CAPMIX1A-10-char-expansion-verified-and-reencoding-verdict.md ./ASSETS-REGISTRY.md ./C123-C121-B2-1-mixture-essentiality-first-cut-with-self-correction.md
$ bash scripts/tech_word_check.sh "不可约码"
技术词 不可约码        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "切换机制"
技术词 切换机制        命中文件数=0    ::
```
- **本档新增**：**0** 个术语 ✓（`等距移位`／`自同构切换`／`不可约码`／`切换机制` 命中 0 ⟹ 为**本档自造标签**，作**结构命名**，**不作新性主张** ✓；`平移对`（3）／`层和`（6）为档案已有 ✓）
- **注** ✓：本档实质内容是 **§2 框架 ＋ §3 归约 ＋ §4 三行机制证明**（**推导性** ✓），非术语级新性 ✓

## §9 边界（硬 ✓）

- **零计算** ✓；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- 不写"该分离不存在" ✗（只写"未构造"，分支③ ✓，V290）
- §4 的三行证明为**充分**机制（$\sigma$ 保 $D$ ⟹ $A$ 不变 ✓）；**其逆不主张** ✗（$A$-不变的其他来源未排除 ✓）
- 外部无新依赖 ✓（只用本线既有：P12-PASS／自由坐标引理／$K(9,1)=62$ ✓）
