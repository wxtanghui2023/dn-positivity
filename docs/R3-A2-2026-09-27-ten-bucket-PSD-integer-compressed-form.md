# R3-甲-P2/P3-2026-09-27 — 十桶＋PSD＋整数性：**数学压缩形式**（**不跑可行性计算** ✓）

> ⚠️ **空间隔离**：本档＝空间 B 之 119 线专用 ✓；不引 RH 链 ✗。
> **范围（照唐先生 22:07 令 ✓）**：R3-甲 判定确认（**总量版 DROP ✓／十桶＋PSD＋整数版 ALIVE ✓**）；**写出压缩形式**；**暂不跑可行性计算** ✗。

**已查地图：命中（接续 R3／R3-甲，非新案 ✓）**
所查：`docs/R3-2026-09-27-coordinate-labelled-excess-and-the-no-go-test.md`｜`docs/R3-A-2026-09-27-ten-coordinate-buckets-symbolic-verdict-total-version-dead.md`（**1555 上界／slack≥53** ✓✓）｜`docs/SECOND-ORDER-2026-09-25-near-pair-pressure-chain.md`｜`docs/P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md`（**模 11 定理／Booleanity** ✓✓）｜`docs/FOURIER-2026-09-26-convolution-reformulation-audit.md`｜`docs/R2-2prime-2026-09-27-…`
**强制查重门** ✓：`scripts/tech_word_check.sh`（五词，见 §6）
D0: 本档对象 ＝ **档案已有** R3-甲 系统的**压缩形式**（重命名：否 ✗；新对象：无 ✗）
D1: 1（**首次给出三条等价压缩形式**，并证明 **PSD 严格强于 Gershgorin＋桶约束**（−59.5 vs −83）⟹ PSD "有牙" ✓）
**[RESEARCH]**

---

## §0 结论（**判定确认 ＋ 压缩形式三条 ＋ PSD 有牙 ✓**）

$$\boxed{\text{判定}:\ \textbf{总量版 DROP}\ ✗\quad\big|\quad\textbf{十桶＋PSD＋整数版 ALIVE}\ ✓}$$
$$\boxed{\text{压缩形式三条（等价表述）}:\ \textbf{I 矩阵/谱}\ \big|\ \textbf{II }\mu\text{-线性（谱测度）}\ \big|\ \textbf{III 符号/相位（}covering\text{ 的完整重述）}}$$
$$\boxed{\textbf{PSD 有牙 ✓}:\ \text{要求 }\lambda_{\min}(\tilde Q)\ge-\tfrac m2=-59.5,\ \text{而 Gershgorin＋桶只给}\ \ge-83\ \Longrightarrow\ \text{PSD 严格更强（差 23.5）}}✓✓$$

---

## §1 系统清单（照唐先生给定 ✓，逐条落成公式）

$$(1)\ G\succeq0;\qquad (2)\ G_{ii}=119\ (=\gamma(0)=m);\qquad (3)\ G_{ij}=2q_{ij}\ (i\ne j);\qquad (4)\ q_{ij}\in\mathbb Z_{\ge0}✓$$
$$(5)\ B_i:=N_1^{(i)}+\sum_{j\ne i}q_{ij}\le83;\qquad (6)\ \sum_iB_i=\tfrac{A_1+2A_2}2\le777✓$$
$$(7)\ A_1+2A_2=285+Q-A_1\ \text{且}\ Q\le1270,\ Q\ \text{奇}\ \Longrightarrow\ [144,1555];\qquad (8)\ A_1=2N_1,\ A_2=2N_2✓$$
$$\text{（covering 诱导项见 §4 ✓）}$$

---

## §2 **压缩形式 I：矩阵／谱**（**PSD 有牙 ✓✓**）

$$G=mI+2\tilde Q,\qquad \tilde Q_{ii}=0,\ \tilde Q_{ij}=q_{ij}\ (i\ne j)\ \Longrightarrow\ \boxed{G\succeq0\iff\lambda_{\min}(\tilde Q)\ge-\tfrac m2=-59.5}✓✓$$
$$\text{trace}(\tilde Q)=0\ \Longrightarrow\ \lambda_{\min}\le0\ \Longrightarrow\ \boxed{|\lambda_{\min}(\tilde Q)|\le59.5}✓$$
$$\textbf{对照（无 PSD 时）}:\ \text{Gershgorin}\ \Longrightarrow\ \lambda_{\min}(\tilde Q)\ge-\max_i\sum_{j\ne i}q_{ij}\ge-83\ \Longrightarrow\ \textbf{PSD 严格更强}\ ✓（\text{差 }83-59.5=23.5）✓✓$$
$$\text{二阶推论}:\ q_{ij}\le m/2=59\ \ (\text{由 }2\times2\ \text{主子式}\ m^2-(2q_{ij})^2\ge0)✓$$
$$\text{三阶及高阶}:\ \text{各 }k\times k\ \text{主子式}\ \ge0\ \text{（给出 }q\ \text{的三次及以上耦合约束）}✓$$

---

## §3 **压缩形式 II：$\mu$-线性（谱测度）**（**支撑层是 }$\mu$\text{ 的线性泛函 ✓✓**）

$$\mu(u):=|\widehat C(u)|^2\ \ (\ge0)\ ✓;\qquad \gamma(v)=\frac1{1024}\sum_u\mu(u)(-1)^{u\cdot v}\ ✓\ \Longrightarrow\ \boxed{q_{ij}=\frac1{2048}\sum_u\mu(u)(-1)^{u\cdot(e_i\oplus e_j)}}\ ✓✓$$
$$\text{故 }N_1^{(i)}=\gamma(e_i)/2\ \text{与 }q_{ij}\ \textbf{皆为 }\mu\ \text{的线性泛函} \Longrightarrow \textbf{桶约束 }(5)\ \text{是 }\mu\ \text{的线性不等式}✓✓$$
$$\textbf{约束}:\ \mu(0)=m^2=14161✓;\quad \sum_u\mu(u)=1024\,m✓\ (\text{Parseval});\quad \boxed{\widehat C(u)=m-2k(u),\ k(u)\in\mathbb Z\cap[0,m]\Longrightarrow\mu(u)=(m-2k(u))^2}✓✓$$
$$\text{层和（给定层）}:\ \sum_{|v|=i}\gamma(v)=A_i\ \Longleftrightarrow\ \mu\ \text{的层平均约束}✓$$
$$\Longrightarrow\ \boxed{\text{距离层}:\ A_i=\tfrac1{1024}\sum_u\mu(u)K_i(u)\ (\text{Krawtchouk 线性泛函});\quad \text{支撑层}:\ q_{ij}=\tfrac1{2048}\sum_u\mu(u)(-1)^{u\cdot(e_i\oplus e_j)}}\ ✓\ \text{—— \textbf{二者皆为 }\mu\text{ 的线性泛函} ⟹ \textbf{二阶全部可见}}✓✓$$

---

## §4 **压缩形式 III：符号／相位（covering 的完整重述）**（✓✓ 无松弛）

$$g:=\sum_{i=0}^{10}\mathbf 1_{C\oplus e_i}=b\ ✓;\qquad \widehat g(u)=(11-2|u|)\widehat C(u)✓\qquad(\text{模 11 定理的算子 }T\ \text{即此乘子}✓)$$
$$\text{covering}\iff g(x)\ge1\ \ \forall x✓;\qquad \text{码}\iff \mathbf 1_C=F^{-1}(\widehat C)\in\{0,1\}^{1024}✓$$
$$\Longrightarrow\ \boxed{\textbf{完整重述（无松弛 ✓）}:\ \text{找 }\widehat C:\mathbb F_2^{10}\to\mathbb Z\ \text{使}\ (i)\ F^{-1}(\widehat C)\in\{0,1\},\ (ii)\ F^{-1}\big((11-2|u|)\widehat C\big)\ge1\ \text{且整数}✓✓}$$
$$\textbf{三分读数 ✓}:\quad \textbf{距离层}=A=\mu\ \text{的 Krawtchouk 层泛函}\ \big|\ \textbf{支撑层}=q_{ij}=\mu\ \text{的坐标泛函}\ \big|\ \textbf{covering}=\widehat C\ \text{的\textbf{符号}}（\mu\ \text{看不见 ✓）}$$
$$\Longrightarrow\ \text{经典（}\mu\text{-型）理论天花板之所以有限，正因为 }(i)(ii)\ \text{对 }\widehat C\ \textbf{的符号} \text{敏感，而 }A_i\ \text{与 }\mu\ \text{对其盲}✓✓$$

---

## §5 可行性问题的**精确陈述**（P2/P3 的可计算形式；本档**不跑** ✗）

$$\boxed{\text{问 R3-}\text{甲}\text{-P2/P3}:\ \text{是否存在 }\tilde Q\ (\text{零对角、非负整数、}\sum_{i<j}q_{ij}=N_2)\ \text{满足}\ \lambda_{\min}(\tilde Q)\ge-59.5\ \text{与 }(5)(6)✓}$$
$$\text{若\textbf{不可行}}\ \Longrightarrow\ \boxed{K(10,1)\ge120}\ ✓\ \text{（因任一 119-cover 必给该系统的可行点 ✓）}$$
$$\text{若\textbf{可行}}\ \Longrightarrow\ \text{只说明\textbf{二阶（含 PSD）不足} ⟹ 进三阶（乙）}✓\ \text{—— \textbf{不}推出 119 存在 ✗✓（重要方向性 ✓）}$$
$$\textbf{注 ✓}:\ \S4\ \text{的完整重述无松弛 ⟹ 任何\textbf{松弛}层级的不可行性都是\textbf{真 P1}；反之可行仅表明该层不足 ✓$$

---

## §6 技术词回查（先跑后写 ✓）

```
$ bash scripts/tech_word_check.sh "谱测度"
技术词 谱测度          命中文件数=16   :: ./CANDIDATE-SCAN-1-mathematical-content-review.md ./p4-dilation-audit.md ./ASSETS-REGISTRY.md
$ bash scripts/tech_word_check.sh "压缩形式"
技术词 压缩形式        命中文件数=2    :: ./V193-arithmetic-to-inverse-spectral-map-audit-and-self-erratum.md ./E10-rank-trace-inertia-joint.md
$ bash scripts/tech_word_check.sh "符号谱"
技术词 符号谱          命中文件数=0    ::
$ bash scripts/tech_word_check.sh "Gershgorin"
技术词 Gershgorin       命中文件数=3    :: ./C122-C121-B-first-cut-Toeplitz-PSD-K2-audit-verdict-not-independent.md ./p59-positivedefinite-audit.md ./EXTERNAL-DEMAND-SCAN-cross-domain.md
$ bash scripts/tech_word_check.sh "可行性"
技术词 可行性          命中文件数=137  :: ./AUDIT-direction-depth.md ./C3820B-R0-T-semantic-closure.md ./RH-YM-obstruction-parallel.md
```
- **本档新增**：**0** 个术语 ✓（`符号谱` 命中 0 ⟹ 本档自造标签，作**结构命名**，不作新性主张 ✓；`谱测度`／`压缩形式`／`Gershgorin`／`可行性` 均为档案已有 ✓）
- **注** ✓：本档实质＝**§2 的 PSD 有牙判定（−59.5 vs −83）＋ §3/§4 的两条压缩形式**（**推导性** ✓），非术语级新性 ✓

## §7 边界（硬 ✓）

- **未跑可行性计算** ✓（照令 ✓）；**零计算** ✓；**未开门②** ✓；**未改门** ✓；**不跨空间** ✓
- **PSD 有牙**只说明"PSD 较 Gershgorin＋桶严格更强"✓ —— **不**说明"不可行" ✗（须真跑或符号证）
- **完整重述（§4）无松弛** ✓ 这一事实**必须**与"可见性"陈述一同引用（防把"二阶可见"读成"二阶充分" ✗）
- 不写 $K(10,1)\ge120$ ✗（V290 ✓）；方向性（不可行⟹P1／可行⟹该层不足）已显式标注 ✓
