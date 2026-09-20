已查地图（**先查后写**）：`C-180`（A2 范围核实：剩余＝阻尼 (RP_M)）、`C-181`（阻尼缩放约化引理，已证）、`C-183`／`C-184`／`C-190`／`T13-Damped-M3`（阻尼线成果）、`C268`（E4 依赖地图）、`E4-ENGINE-2/3`、`C-156`–`C-159`（κ_N 线）。回查见 §7 ✓

D0: 本档对象 = **A 项（Turán–Cassels／有限极值族）的启下审计（四问）＋ C-268 对 M=5 的判定修正** —— 关系 = 立项审计（不产定理）
D1: 0
FREEZE-ACK: 本档即冻结期内的立项审计（依 §8.1）

---

## §0 四问答案 ＋ 一处自我修正（✓✓）

$$\boxed{\textbf{Q1 对象}✓：\text{阻尼}\ (\text{RP})\ ＝\ \text{Montgomery Lemma 2.2 的【一般形式}】\（|z_j|\le1,\ \max|z_j|=1）✓}$$
$$\boxed{\textbf{Q2 独立性}✗✓：\textbf{不是新对象} —— \text{它是我方【自己的残留}】✓（\texttt{C-180}(二)：\text{「A2 的真正剩余}\equiv\text{阻尼版}(\text{RP}_M)\text{」}✓）}$$
$$\boxed{\textbf{Q3 引擎复用}✓✓：\textbf{逐字可复用} —— \texttt{C-181} \text{已证【缩放约化引理}】：\text{阻尼情形}\to\text{单模}\ (\text{RP}_u),\ u\le5✓✓}$$
$$\boxed{\textbf{Q4 启下}✓✗：\textbf{有界的启下} —— \text{完成}\ u\le5\ \text{即补齐【档案自己声明的靶区}】✓；\text{更深的下游仍被外部项}\ \texttt{D2d}\ \text{阻断}✗}$$
$$\boxed{\textbf{⭐ 自我修正}✗✓：\texttt{C268}\ \text{说「M=5 对 E4 无必要」}\ \textbf{不完整}✗ —— \text{它是【阻尼线声明的}\ u\le5\ \text{靶区的承重输入}✓✓}$$

## §1 Q1 · 对象到底是什么（✓）

$$\texttt{C-180}\ (二)\ \textbf{逐字}✓：\text{「A2 的真正剩余}\ \equiv\ \textbf{阻尼版}\ (\text{RP}_M)\ \equiv\ \text{Montgomery Lemma 2.2 本体}✓：\text{我方}\textbf{只做了单模情形}✓」$$
$$\text{即}✓：\max_j|z_j|=1\Longrightarrow\max_{1\le n\le5M}\operatorname{Re}\sum_j z_j^n\ \ge\ \tfrac1{20}✓\（\text{允许}|z_j|<1✓）$$
$$\qquad \text{与}\ (\text{RP}_M)\ \text{的差别}✓：(\text{RP}_M)\ \text{是}\ \textbf{全单模}（|z_j|=1\ \forall j）✓；\text{阻尼＝【混合模长}】✓ \Longrightarrow \textbf{严格更一般}✓$$

## §2 Q2 · 是否与 (RP_M) 数学上独立（✗ 答案：不独立 ✓✓）

$$\textbf{判定}✗✓：\text{同一族（幂和极值}✓），\text{只把【等模长}】\ \text{放宽到【混合模长}】✓ \Longrightarrow \textbf{不是「新对象」，是【同族的严格推广}】✓$$
$$\qquad \text{依四判据}✓：\text{① 独立性}\ \textbf{不满足}✗（\text{同族}✓）\ \text{但}\ \textbf{② 资产相邻}\ \textbf{满足}✓✓（\text{排第二}✓）$$
$$\qquad \Longrightarrow \textbf{按唐先生标准}✓：\text{它【不是新问题}】✗ —— \text{不值得单独立项}✗✓$$

## §3 Q3 · 引擎能否复用（✓✓ 答案：逐字可复用 ✓）

$$\texttt{C-181}\ \text{§2 引理（**已证**，四行 ✓）}：|z_j|\le1,\ u:=\#\{j:|z_j|=1\}\in[1,5],\ \rho:=\max\{|z_j|:|z_j|<1\}$$
$$\qquad \Longrightarrow\ \max_{1\le k\le5M}\operatorname{Re}\sum_j z_j^k\ \ge\ c_u-(M-u)\rho^{\lfloor M/u\rfloor},\quad \boxed{c_u=\tfrac12}✓$$
$$\qquad \text{证明(ii) 逐字}✓：\text{「由}\textbf{单模结果}（u\le5，\text{引理 C}／\text{定理 1}／\text{证书}\Longrightarrow c_u=\tfrac12）」✓✓$$
$$\Longrightarrow \boxed{\textbf{阻尼所需计算输入＝单模}\ (\text{RP}_u),\ u\le5\ \Longrightarrow \textbf{v3 引擎逐字适用}✓✓（\text{无需改核心逻辑}✓）}$$
$$\qquad \text{现状}✓✓：u=1\（\texttt{C-159}✓）、u=2\（\texttt{C-193}✓）、u=3\（\texttt{T13-A}✓）、u=4\（\texttt{C-265}✓）、\boxed{u=5＝正在跑的慢版 ✓}$$
$$\qquad ⚠️\ \textbf{未决}✗：\texttt{C-181}\ \text{§1 称「对}\ M\le5\ \text{证到}\ \tfrac12\text{」}\ \textbf{过高}✗（\text{当时}\ M=5\ \text{未证}✓）；\ u\le5\ \text{是【引理假定}】✓\ \text{还是【应用真上界}】✗ \textbf{档案未给}✗✓$$

## §4 Q4 · 完成后让什么成为可能（✓✗ 有界 ✓）

$$\text{立即}✓：\text{完成}\ u\le5 \Longrightarrow \text{补齐【档案自己声明的靶区}】✓（\texttt{C-181}\ \text{的}\ u\in[1,5]✓）\ \text{且}\ u=5\ \text{是其中唯一缺口}✓✓$$
$$\text{更深}✗：\texttt{C-180}\text{ (三) }\textbf{逐字}✓\text{：剩余依赖外部开放项（}\texttt{D2d}\text{）}✓ \Longrightarrow \textbf{扩展侧仍被【独立离线零点界】阻断}✗✓\text{（＝}\texttt{C-268}\text{ §3 的同址）}✓$$
$$\Longrightarrow \textbf{启下分级}✓：\text{①（立即可得）补齐声明靶区}\ u\le5✓✓；\text{②（条件性）扩展侧}\ ✓\ \text{待}\ \texttt{D2d}✗$$

## §5 ⭐ C-268 判定修正（必须发出 ✓✓）

$$\texttt{C268}\ \text{原判}✗：\text{「M=5 身份＝独立资产／交叉验证，非 E4 必需品」}✗$$
$$\text{据}\ \texttt{C-181}\ \text{修正}✓✓：\textbf{M=5 是【阻尼线声明的}\ u\le5\ \text{靶区的承重输入}】✓✓ —— \text{不是机会性额外项}✗$$
$$\qquad \Longrightarrow \text{慢版 M=5 应当【跑完}】✓✓（\text{唐先生已定「继续」✓，此处给出依据}✓）$$
$$\qquad \texttt{C268}\ \text{对}\ M=6..11\ \text{的 STOP}\ \textbf{不变}✓✓：\text{它们在}\ u\le5\ \text{的声明靶区【之外}】✗，\text{且应用侧需}\ \texttt{D2d}✗$$

## §6 判定（四问结果 ✓✓）

$$\boxed{\textbf{A 作为【新项目】：不立项}✗✓ —— \text{①独立性不满足}✗；\text{对象＝我方自己的残留}✓}$$
$$\boxed{\textbf{A 作为【引擎第二实例】：已存在}✓✓ —— \text{阻尼线（}\texttt{C-181}\ \text{约化＋}\texttt{C-183/C-184/C-190/T13-Damped-M3}✓）\ \textbf{已在数学上不同的对象上复用引擎}✓✓}$$
$$\qquad \Longrightarrow \textbf{唐先生要的「}\exists Q\neq RP_M\ \text{可复用同一架构}」\ \textbf{已由阻尼线满足}✓✓ \Longrightarrow \textbf{无需为此新立项}✗✓$$
$$\boxed{\textbf{唯一实质待办}✓：\text{把}\ u=5\ \text{那格跑完}✓（\text{正在进行}✓）＋ \text{写清阻尼线的复用记录}✓}$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 第二实例已存在 命中文件数=0 ::
技术词 阻尼承重输入   命中文件数=0 ::
技术词 声明靶区       命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{「第二实例已存在」（0）}✓、\text{「声明靶区」（0）}✓$$
$$\textbf{② 档案已有（引用，不列为本档提出）}✓✓：\textbf{「阻尼承重输入」（1 命中}✓，\text{见}\ \texttt{C-181}✓\text{）}$$

## §8 边界

$$\textbf{① 本档为立项审计}✓，\text{不产定理、不跑计算}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ 不声称阻尼线已完整}✗（u=5\ \text{缺口}✓、u\le5\ \text{来源未定}✗）；\text{不声称}\ \texttt{C268}\ \text{整体错}✗（\text{仅}M=5\ \text{一格需修正}✓）$$
$$\textbf{④ }M=5\ \text{慢版仍在跑}✓；\text{未追加任何计算}✓$$
