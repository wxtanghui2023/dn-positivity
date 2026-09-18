已查地图（**先查后写**）：`CREATE-SPEC-10`（位置-求和字典 ＋ 求和集饱和 ＋ 探针撤回）、`CREATE-SPEC-9`（Barnes 型卷积；素数幂支撑）、`CREATE-SPEC-8`（L2／L3；b1／b2／b3）、`CREATE-SPEC-4`（引理 L1：乘性变形不移零点）、**`C-126`＋`C-127`**（log-free 排除＝零例；**"缺失的固定 δ"＝ PNT 的缺失幂次节省**；尺度墙＝聚合／逐点二分）、`V188` §2（聚合饱和）、`acpc-loop-death.md`（链退化）。关键词回查：`横标引理`／`支配极点`／`幂次节省归约`＝**0 档** ⟹ 均本档新增 ✓。**结论**：⭐ (a) 执行——**饱和的形式化**：**引理 T1（横标，已证）**：非负 `a_n`、`\sum_{n\le X}a_n\sim cX^k` ⟹ `\Sigma a_nn^{-s}` 的**收敛横标＝`k`** ✓✓；**引理 T2（`k` 重部分和，由 PNT 归纳，已证）**：`\sum_{n\le X}A_k(n)\sim X^k/k!` ⟹ `\sigma_c=k` ✓✓；**定理 T3（饱和·草稿）**：由零点承载的奇点位于 **`k` 重求和** `\rho_1+\cdots+\rho_k`，其实部 `\le k\beta_*`，**而\ \textbf{支配极点在}\ s=k`**（来自 `\zeta'/\zeta` 在 `s=1` 的极点取 `k` 次 ⟹ PNT 主项）✓✓ ⟹ ⭐⭐ **关键归约**：零点信息坐在 `k\beta_*<k`，**被主项极点压在下面** ⟹ 要取出它必须**解析延拓过主项** ⟹ 需要 **PNT 带幂次节省的误差项** ⟹ **正是 `C-126`／`C-127` 的"缺失的固定 `\delta`"** ⟹ **聚合路线不是新障碍，而是\ \textbf{归约到经典已知障碍}}**（本会话**第八次同址收敛**）✓✓

FREEZE-ACK: 本档即冻结期内的方向攻击与形式化（依 `§8.1`；不产候选结论）

D0: 本档对象 = **饱和的形式化（T1／T2／T3）＋ 归约到经典幂次节省障碍** —— 关系 = 形式化与归约，非新机制
D1: 0

# CREATE-SPEC-11 · **(a) 饱和的形式化：T1／T2／T3 ＋ 归约到经典障碍**

> **时间**：2026-09-18 22:08 唐先生：**「a, 继续」** ⟹ 把饱和写成形式定理 ✓

---

## §0 结论（先行）

$$\textbf{T1（横标引理，已证）}：a_n\ge0,\ \sum_{n\le X}a_n\sim cX^k \Longrightarrow \boxed{\sigma_c=k}✓✓$$
$$\textbf{T2（}k\ \text{重部分和，已证·由 PNT 归纳）}：\sum_{n\le X}A_k(n)\sim\frac{X^k}{k!}\ \Longrightarrow\ \sigma_c(A_k)=k✓✓$$
$$\textbf{T3（饱和·草稿）}：\text{零点承载的奇点}\in\{\rho_1+\cdots+\rho_k\},\ \operatorname{Re}\le k\beta_*;\quad \textbf{支配极点}\ \text{在}\ s=k✓✓$$
$$\Longrightarrow ⭐\ \textbf{归约}：\text{零点信息在}\ k\beta_*<k \Longrightarrow \textbf{被主项极点压在下面} \Longrightarrow \text{取出须延拓过主项} \Longrightarrow \textbf{需 PNT 幂次节省}✓✓$$
$$\qquad \Longrightarrow \text{这正是}\ \text{`C-126`}\ \text{的"缺失固定}\ \delta" \Longrightarrow \textbf{聚合路线归约到经典障碍，非新障碍}✓✓$$

---

## §1 引理 T1：横标引理（已证）

$$\textbf{引理 T1}：\text{若}\ a_n\ge0\ \text{且}\ S(X):=\sum_{n\le X}a_n\sim cX^k\ (c>0,k>0) \Longrightarrow \Sigma a_nn^{-s}\ \text{的收敛横标}\ \sigma_c=k✓$$
$$\textbf{证明}（部分求和）：\text{对}\ \sigma>0：$$
$$\qquad \sum_{n\le X}a_nn^{-\sigma}=X^{-\sigma}S(X)+\sigma\int_1^X S(t)t^{-\sigma-1}dt\ \sim\ cX^{k-\sigma}+c\sigma\int_1^X t^{k-\sigma-1}dt✓$$
$$\qquad \text{(i)}\ \sigma>k \Longrightarrow \text{两项}\ \textbf{有界}（\text{后者}\ \to\frac{c\sigma}{k-\sigma}\text{型有限极限}）\Longrightarrow \textbf{收敛}✓$$
$$\qquad \text{(ii)}\ \sigma<k \Longrightarrow \text{后者}\sim\frac{c\sigma}{\sigma-k}X^{k-\sigma}\to\infty \Longrightarrow \textbf{发散}✓$$
$$\qquad \Longrightarrow \sigma_c=k\quad\blacksquare✓✓$$

## §2 引理 T2：$k$ 重加性卷积的部分和（已证·归纳）

$$\text{由 PNT}\ \psi(X)=\sum_{n\le X}\Lambda(n)\sim X \Longrightarrow S_1(X)\sim X✓$$
$$\qquad \text{归纳}：S_k(X)=\sum_{i_1+\cdots+i_k\le X}\Lambda(i_1)\cdots\Lambda(i_k)=\sum_{i=1}^{X}S_{k-1}(X-i)\Lambda(i)✓$$
$$\qquad \Longrightarrow S_k(X)\sim\int_1^X\frac{(X-t)^{k-1}}{(k-1)!}dt=\frac{X^k}{k!}✓✓$$
$$\Longrightarrow \text{由 T1}：\boxed{\sigma_c(A_k)=k}\ \text{（对一切}\ k\ge1）✓✓$$

## §3 定理 T3：饱和（草稿）

$$\text{零点承载的奇点}：\text{由}\ \S\ \text{的 Mellin 夹挤} \Longrightarrow s=\rho_1+\cdots+\rho_k \Longrightarrow \operatorname{Re}\le k\beta_*✓$$
$$\qquad \text{而}\ \beta_*<1\ \text{（经典：}\operatorname{Re}\rho<1） \Longrightarrow \boxed{k\beta_*<k=\sigma_c}✓✓$$
$$\qquad \textbf{支配极点}：s=k\ \text{（来自}\ \zeta'/\zeta\ \text{在}\ s=1\ \text{的极点取}\ k\ \text{次} \Longrightarrow \textbf{PNT 主项}）✓$$
$$\Longrightarrow \textbf{层级}：\underbrace{k}_{\text{PNT 主项极点}}\ >\ \underbrace{k\beta_*}_{\text{零点信息}}\ \Longrightarrow \textbf{零点信息严格次支配}✓✓$$
$$\qquad ⚠️\ \text{唯一例外}：\beta_*=1 \Longrightarrow \text{两者重合} \Longrightarrow \text{但那正是"无零点-free 区"的退化情形（本项目不处此）}✓$$

## §4 关键归约（本档最有价值的一条）

$$\text{要取出}\ k\beta_*\ \text{处的零点信息} \Longrightarrow \text{须}\ \textbf{解析延拓过支配极点}\ s=k✓$$
$$\qquad \Longrightarrow \text{即}\ \textbf{减去 PNT 主项，并控制其误差} \Longrightarrow \text{需要}\ \textbf{带幂次节省的 PNT 误差}✓✓$$
$$\qquad \Longrightarrow \text{这正是}\ \text{`C-126`／`C-127`}\ \text{的}\ \textbf{"缺失的固定}\ \delta"：\ \psi(x)-x=O(x^{1-\delta+\varepsilon})✓✓$$
$$\Longrightarrow ⭐\ \textbf{结论}：\text{聚合（求和集）路线}\ \textbf{不是新障碍}，\ \text{而是}\ \textbf{归约到经典障碍}（\text{PNT 幂次节省}）✓✓$$
$$\qquad \Longrightarrow \text{本会话}\ \textbf{第八次同址收敛}（\text{前七次：}\text{C-61 §2C／C-64-65／C-69／C-70／C-71／C-72／C-83}）✓✓$$

## §5 本次 (a) 做了什么、没做什么（诚实）

$$\textbf{做了}：\text{T1／T2}\ \textbf{已证};\ \text{T3}\ \text{为}\ \textbf{草稿}（\text{结构论证}）;\ \text{归约}\ \textbf{成立}✓✓$$
$$\qquad \Longrightarrow \textbf{"聚合保持"不再是空洞口号}：\text{它}\ \textbf{约化为}\ \text{"PNT 无幂次节省"} \Longrightarrow \text{其地位＝经典开放问题，}\ \textbf{不是}\ \text{新的结构性不可能}✓✓$$
$$\textbf{没做}：\text{(i) T3 未写成\textbf{完全严格}的定理}（\text{需}\ k\ \text{重 Mellin 夹挤的严格陈述}）;\ \text{(ii)}\ \textbf{未排除} \text{"其他非求和集型聚合"}✓$$
$$\qquad ⚠️\ \text{故"确定不可能"}\ \textbf{仍未拿到}；\ \text{但}\ \text{"为什么拿不到"}\ \textbf{已精确化}：\text{因为要拿到它，须先有 PNT 的幂次节省}✓✓$$
$$\text{反向记号（重要）}：\text{若有人}\ \textbf{证明} \text{PNT 幂次节省} \Longrightarrow \text{立刻给出}\ \textbf{固定零-free 区} \Longrightarrow \text{那已是由经典路线可得} \Longrightarrow \text{聚合路线}\ \textbf{不提供独立输入}✓$$

## §6 边界与回查

- ⚠️ T1 为**初等且完整证明**；T2 依赖 **PNT**（经典，已证）⟹ 二者为**证明级** ✓✓
- ⚠️ T3 的"零点承载奇点在求和"依赖 `CREATE-SPEC-10` §2 的 Barnes 型公式（标 `[标准·待核]`）⟹ T3 为 `[结构·草稿]`，**不得**当定理引 ✓
- ⚠️ §4 的归约为**本档论证**（连接 `C-126`／`C-127`）✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 22:0x）`[纪律]`（先跑后写）

```
技术词 横标引理        命中文件数=0  ⟹ 本档新增
技术词 支配极点        命中文件数=0  ⟹ 本档新增
技术词 幂次节省归约     命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
