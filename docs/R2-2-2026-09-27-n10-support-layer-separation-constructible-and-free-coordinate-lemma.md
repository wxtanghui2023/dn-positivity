# R2-2-2026-09-27 — **$n=10$ 的 support 层分离**：可构造 ✓ ＋ **自由坐标引理**（决定其适用边界 ⚠️）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **本档范围（照唐先生 21:45 令 ✓）**：**只做 R2-2**；**不碰** excess／Habsieger／Van Wee／Fourier ✗；**不计算** 119/120-cover ✗。

**已查地图：命中（接续 P1-5／P12-PASS，非新案 ✓）**
所查：`docs/P1-5-2026-09-27-van-Wee-proof-decomposition-at-n10-and-R2-1-DROP.md`（**A 型输出＋两条件** ✓✓）｜`docs/P12-PASS-2026-09-27-bucket-divergence-with-identical-distance-distribution.md`（**$n=8$ 见证** ✓✓）｜`docs/119-ATTACK-R1-2026-09-27-…leverage-verdict.md`（含 §12 更新 ✓）｜`docs/HANDOFF-2026-09-27-119-line-session-handoff.md`｜`docs/CONCRETE-TOPIC-LIST-r2.md`（$K(9,1)=62$ 基准 ✓）
**强制查重门** ✓：`scripts/tech_word_check.sh`（六词，见 §6）
D0: 本档对象 ＝ **档案已有** R2-2 问题（$n=10$ 的 $A\Rightarrow J$?）的**构造性判定**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出 $n=10$ 分离的\textbf{构造}** ＋ **自由坐标引理** ⟹ 边界定位 ✓）
**[RESEARCH]**

---

## §0 结论（**照唐先生三分支落位** ✓）

$$\boxed{\textbf{分支①「发现 10D 分离」成立 ✓（构造性）}:\ \text{提升引理}+\text{P12-PASS 见证}\ \Longrightarrow\ \exists C,C'\subseteq\mathbb F_2^{10}\ \text{半径 1 覆盖},\ A(C)=A(C'),\ \text{但 support 指纹不同}}$$
$$\boxed{\text{但附带}\ \textbf{自由坐标引理}:\ \text{提升式分离}\ \textbf{必然落在最优范围之外}（|C|=128\gg120）\ ⟹\ \text{对 P1 的可用性另有其门 ⚠️}}$$
$$\boxed{\text{故下一刀必须收紧为}\ \textbf{R2-2}^{\prime}:\ \text{近最优范围（}|C|\le123,\ \text{即\textbf{无自由坐标}}）内的分离 ——\ \text{否则 }J\ \text{的不等式门无着力点}}$$

---

## §1 精确问题（照唐先生逐字 ✓）

> 是否存在两个 $n=10$ 半径 1 覆盖码 $C,C'$，满足 $A_i(C)=A_i(C')\ \forall i$，但某个 support-sensitive invariant 不同，例如 $J(C)\ne J(C')$？✓
**外加第二关（唐先生 ✓）**：须证明该 $J$ **能进入覆盖条件**，形成 $|C|=119\Longrightarrow J\in\mathcal J_{\rm impossible}$ 之类的约束；否则仍只是**结构性资产**，不是 P1 ✓

---

## §2 ★**提升引理**（**3 行，index-free ✓✓**）

$$\text{设 }C\subseteq\mathbb F_2^n\ \text{为半径 1 覆盖码};\quad \widetilde C:=C\times\mathbb F_2=\{(c,b):c\in C,\ b\in\{0,1\}\}\subseteq\mathbb F_2^{n+1}$$
$$\textbf{(L-1 覆盖 ✓)}\ \forall(x,b):\ \exists c\in C,\ d(x,c)\le1\Longrightarrow d\big((x,b),(c,b)\big)\le1\ ✓;\quad |\widetilde C|=2|C|✓$$
$$\textbf{(L-2 距离分布（逐字公式 ✓）)}\ d\big((c,b),(c',b')\big)=d(c,c')+\mathbf 1[b\ne b']\ \Longrightarrow\ \boxed{A_i(\widetilde C)=2\big[A_i(C)+A_{i-1}(C)\big]}\ ✓✓$$
$$\qquad\Longrightarrow\ A(C)=A(C')\ \Longrightarrow\ A(\widetilde C)=A(\widetilde C')\ ✓\ \text{——\textbf{等价关系被提升} ✓（且公式可逆 ⟹ 是双射级 ✓）}$$
$$\textbf{(L-3 支撑层（逐字公式 ✓）)}\ \text{邻域}:\ N\big((x,b)\big)=\{(x,1-b)\}\cup\{(x\oplus e_i,b):i\in S_C(x)\}✓;\quad d_1\big((x,b)\big)=1+d_1(x)✓$$
$$\qquad q_{ij}(\widetilde C)=2\,q_{ij}(C)\ \ (i<j\le n)✓;\qquad \boxed{q_{i,n+1}(\widetilde C)=2\,m_i(C)}\ \ \big(m_i(C):=\#\{x\in C:i\in S_C(x)\}\big)✓$$
$$\qquad m_i(\widetilde C)=2m_i(C)\ (i\le n)✓;\qquad m_{n+1}(\widetilde C)=2|C|✓$$
$$\Longrightarrow\ \textbf{支撑指纹（}q\text{-多重集）的提升}:\ \{q_{ij}(\widetilde C)\}=2\Big(\{q_{ij}(C)\}_{i<j\le n}\cup\{m_i(C)\}_{i\le n}\Big)\ ✓✓$$

---

## §3 应用：**$n=10$ 分离成立** ✓✓

$$\text{起点（P12-PASS ✓✓）}:\ \text{三个两两不等价的最优 }(8,32)_1\ \text{码}\ C_1,C_2,C_3\subseteq\mathbb F_2^8,\quad \textbf{全距离分布相同},\ \text{而}\ J_7\in\{64,128,256\}✓$$
$$\qquad\text{其 }q\text{-多重集\textbf{已不同}}:\ J_7{=}64\Rightarrow\{4,4,4,4\};\quad 128\Rightarrow\{8,8\};\quad 256\Rightarrow\{16\}\ ✓✓$$
$$\text{两次提升（照 §2 ✓）}:\ \boxed{C=\widetilde{\widetilde{C_1}}=C_1\times\mathbb F_2^2,\qquad C'=C_2\times\mathbb F_2^2}\ \subseteq\mathbb F_2^{10}\ ✓$$
$$\Longrightarrow\ \text{(i) 二者均为 }\mathbb F_2^{10}\ \text{半径 1 覆盖码 ✓（由 L-1 连用 ✓）};\quad |C|=|C'|=4\cdot32=\mathbf{128}✓$$
$$\qquad\text{(ii) }A(C)=A(C')\ ✓\ \text{（由 L-2 连用 ✓）};\qquad \text{(iii) support 指纹不同 ✓（由 L-3：}q\text{-多重集 }=4\big(\{q_{ij}\}\cup\{m_i\}\cup\{|C_1|\}\big)\ \text{且 }\{q_{ij}\}\ \text{已不同 ✓✓）}$$
$$\boxed{\textbf{故}\ A\not\Rightarrow J\ \ \textbf{在 }n=10\ \text{成立}✓✓\ \text{（构造性、零计算、显式 }C=C_1\times\mathbb F_2^2\text{）}}$$

---

## §4 ★★**自由坐标引理**（**本档第二产出；决定可用性边界 ⚠️**）

$$\textbf{定义}:\ \text{称 }C\subseteq\mathbb F_2^n\ \text{沿某坐标\textbf{可分}（split）},\ \text{若 }C=D\times\mathbb F_2\ (D\subseteq\mathbb F_2^{n-1})✓$$
$$\textbf{引理 ✓}:\ C=D\times\mathbb F_2\ \text{为半径 1 覆盖码}\ \Longrightarrow\ D\ \text{亦为半径 1 覆盖码，且}\ |C|=2|D|\ge 2K(n-1,1)✓\ \text{（3 行 ✓）}$$
$$\qquad\Longrightarrow\ \boxed{n=10\ \text{且}\ |C|\le123\ \Longrightarrow\ C\ \textbf{不可分（无自由坐标）}}✓✓\quad(\text{用 }K(9,1)=\mathbf{62}✓)$$
$$\text{理由}: |C|\le123\Longrightarrow|D|\le61.5<62=K(9,1)\ ✗\ \text{矛盾}✓$$
$$\Longrightarrow\ \boxed{\text{§3 的分离\textbf{必然}落在可分族（}|C|=128\ \text{），即} \textbf{与 P1 相关范围（}119\text{–}120\text{）不相交}}✗\ ⚠️$$
$$\text{附赠（初等级，合法资产 ✓）}:\ \textbf{任何}\ \le123\ \text{词的 }\mathbb F_2^{10}\ \text{覆盖码都是\textbf{坐标不可约}的}✓\ \text{（等价于 }K(10,1)\ge2K(9,1)\ \text{的构造侧对偶 ✓）}$$

---

## §5 与 P1 的距离（**两门，诚实 ✓**）

| 门 | 状态 | 说明 |
|---|---|---|
| **门①：近最优范围内的分离** | ⚠️ **未决** | §3 分离在可分族（$|C|=128$）；**§4 证明它不可能进入 $|C|\le123$** ⟹ 近最优版**须另找构造**（**R2-2′**）|
| **门②：$J$ 进覆盖条件** | ⚠️ **未决（原状）** | 仍未得 $|C|=119\Longrightarrow J\in\mathcal J_{\rm impossible}$；**且**门②须建立在门①之上（否则约束只作用于 $|C|\ge124$ 的族，对 119 无着力 ✗）|
$$\Longrightarrow\ \textbf{停判（照唐先生三分支 ✓）}:\ \text{分支①成立 ✓ ⟹ 「继续寻找 }J\ \text{的覆盖不等式」};\ \textbf{但}须先补 \textbf{R2-2}^{\prime}（近最优分离），否则门②空转 ⚠️$$

---

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "提升引理"
技术词 提升引理        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "自由坐标"
技术词 自由坐标        命中文件数=5    :: ./C3815-four-unit-circle-nodes-Newton-self-inversive-elimination-audit.md ./L4-2026-09-27-source-structure-of-beta.md ./C3852-quantitative-inverse-local-C1-C2-and-zero-set-degeneracy.md
$ bash scripts/tech_word_check.sh "q-多重集"
技术词 q-多重集        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "近最优"
技术词 近最优          命中文件数=3    :: ./E26A-result.md ./A23D4-ARCHIVE-2026-09-26.md ./A4-M1-normalization-reconciliation.md
$ bash scripts/tech_word_check.sh "支撑指纹"
技术词 支撑指纹        命中文件数=0    ::
$ bash scripts/tech_word_check.sh "分离定理"
技术词 分离定理        命中文件数=7    :: ./RIGOR-AUDIT-1-three-candidates-rigor-audit-and-V248-selected.md ./V225-language-separation-and-interface-theorem.md ./G-COVERED-2026-09-26-final-judgment-and-closure.md
```
- **本档新增**：**0** 个术语 ✓（`提升引理`／`q-多重集`／`支撑指纹` 命中 0 ⟹ 为**本档自造标签**，仅作**结构命名**，**不作新性主张** ✓；`自由坐标`（5 档，他处语境）／`近最优`（3）／`分离定理`（7）为档案已有 ✓）
- **注** ✓：本档的实质新内容是 **§2 三条公式 ＋ §4 引理**（**推导性**，可 3 行自证 ✓），**非**术语级新性 ✓

## §7 边界（硬 ✓）

- **未动算** ✓（★ 本档结论为**构造性推导**，未跑任何搜索／未枚举 ✓）；**未改门** ✓；**不碰** excess／Habsieger／Van Wee／Fourier ✓（照令 ✓）
- 只用 **P12-PASS 既有见证**（$n=8$）＋ **$K(9,1)=62$**（档案基准 ✓）；**未**引入新外部依赖 ✓
- 措辞 ✓：**不写**"近最优分离不存在" ✗（**只写"§3 的构造不可能落在该范围"，门①仍 OPEN** ✓，V290）
- **门①／门② 必须与"分支①成立"一同引用** ✗ 不得只引"已有 10D 分离" ✓
