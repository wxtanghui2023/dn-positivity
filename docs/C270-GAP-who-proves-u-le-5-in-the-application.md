已查地图（**先查后写**）：`C-181`（阻尼缩放约化引理；u∈[1,5] 假定）、`C-180`（A2 剩余＝阻尼 (RP_M)）、`C-186`（Andersson 适用性审计：Fejér 在 5n 可用但常数封顶 1/20）、`C-183`/`C-184`/`C-190`、`C268`/`C269`（依赖地图与 A 项审计）。回查见 §6 ✓

D0: 本档对象 = **审计"谁证明了应用中的 u≤5"** —— 关系 = GAP 登记（不产定理、不脑补来源）
D1: 0
FREEZE-ACK: 本档即冻结期内的缺口登记（依 §8.1）

---

## §0 结论

$$\boxed{\textbf{① 答案：档案中}\textbf{没有任何地方}\ \text{证明【应用侧}\ u\le5\text{】}✗✓ —— \text{它是【引理假定}】✓✓}$$
$$\boxed{\textbf{② }u\le5\ \text{的真实来源＝}\textbf{我们自己的常数覆盖范围}✗✓：c_u=\tfrac12\ \text{仅对}\ u\le5\ \text{已知}✓（\texttt{C-181}✓）}$$
$$\boxed{\textbf{③ 故}\ \text{必须标为}\textbf{缺口}✗✓：}(RP_5)\Rightarrow\text{阻尼引理条件补齐}✓\ \textbf{但}\ \not\Rightarrow\text{应用链闭合}✗✓$$
$$\boxed{\textbf{④ 顺带发现（更一般}✓✓）：\text{单模}\ (\text{RP}_M)\ \text{在}\ \mathbf{1/20\ \text{级}}\ \textbf{对一切}\ M\ \text{已证}✓✓（\texttt{C-186}✓）}$$

## §1 审计问题与证据（✓）

$$\textbf{问}✓：\text{在实际阻尼／Palojärvi 配置中，究竟哪一步推出}\ u\le5？$$
$$\texttt{C-181}\ \text{line 4}\ \textbf{逐字}：\boxed{c_u=\tfrac12\ (1\le u\le5)}✓$$
$$\texttt{C-181}\ \text{line 32}\ \textbf{逐字}：\text{「(ii) 由}\textbf{单模结果}（u\le5，\text{引理 C}／\text{定理 1}／\text{证书}\Longrightarrow c_u=\tfrac12）」✓$$
$$\texttt{C-181}\ \text{§2 (i) 逐字}：K_0:=\lfloor M/u\rfloor\ge1\ \text{（}\textbf{因}\ u\le M\text{）}✓ \Longrightarrow \text{引理只用到【平凡}】\ u\le M✓，\textbf{从未推出}\ u\le5✗✓$$
$$\text{而应用侧}✓（\texttt{E4-ENGINE-3}\ \text{§3}✓）：\text{只给}\ r=|K|\ge2\ \text{（下界}✓），\ \textbf{未给上界}✗✓$$
$$\Longrightarrow \boxed{\textbf{判定}✗✓：u\le5\ \textbf{既非应用结构性上界，也非引理可推} —— \text{它是【已知常数}】c_u=\tfrac12\ \text{的【覆盖范围}】✓✓}$$

## §2 该"覆盖范围"的机制（✓）

$$\text{阻尼引理的条件}✓（\texttt{C-181}\ \text{§3}）：(M-u)\rho^{\lfloor M/u\rfloor}<c_u-\tfrac1{20}✓$$
$$\qquad \text{当}\ c_u=\tfrac12\ \text{时}：\text{右侧}=0.45✓（\text{可满足}✓）；\text{若} c_u=\tfrac1{20}\ \text{级}：\text{右侧}\approx0✗ \Longrightarrow \textbf{引理几乎失效}✗✓$$
$$\Longrightarrow \textbf{所以}\ u\le5\ \text{不是「应用给的}✗，\text{而是【}\tfrac12\ \text{级覆盖到哪，引理就用到哪}】✗✓$$

## §3 顺带发现：1/20 级对一切 M 已证（✓✓）

$$\texttt{C-186}\ \text{line 39}\ \textbf{逐字}：$$
$$\qquad \forall M\ge1,\ \forall|z_k|=1：\ \max_{1\le\nu\le5M}\operatorname{Re}\sum_k z_k^{\nu}\ \ge\ \frac{M+1}{20M}\ >\ \frac1{20}✓✓$$
$$\Longrightarrow \textbf{单模}\ (\text{RP}_M)\ \text{在}\ \mathbf{1/20\ \text{级}}\ \textbf{是一致定理}✓✓（\text{Fejér／Andersson 路线}✓，\text{非证书路线}✓）$$
$$\qquad \Longrightarrow \text{对【E4 原需求}】\（\text{只需}\ \tfrac1{20}✓）：\textbf{自足性已完整}✓✓，\text{与}\ M\ \text{无关}✓$$
$$\qquad \Longrightarrow \text{对【阻尼引理}】✗：\tfrac1{20}\ \text{级不足}✗（\S2）\ \Longrightarrow \textbf{故}\ \tfrac12\ \text{级（}u\le5\text{）是真需求}✓✓$$

## §4 缺口登记（C-269 型 GAP ✓✓）

$$\boxed{\text{GAP-A：}\textbf{应用侧}\ u\le5\ \text{缺证}✗✓ —— \text{即：在阻尼／Palojärvi 应用中，}\ u\ \text{的结构性上界未建立}✗}$$
$$\qquad \text{后果}✓：\text{只能写}\ (RP_u)\ (u\le5)\Rightarrow\text{阻尼引理【条件成立}】✓；\ \textbf{不能}写\Rightarrow\text{应用链闭合}✗✓$$
$$\qquad \text{处置}✓：\text{登记为 GAP}✓；\textbf{不得脑补来源}✗✓；\text{若日后要闭合应用链，须【独立】证明}\ u\ \text{的有界性}✓$$
$$\qquad \text{与}\ \texttt{C-180}(三)\ \text{的关系}✓：\text{该档已把更深下游归到外部开放项}\ \texttt{D2d}✗ \Longrightarrow \text{本条 GAP 与之同址}✓✓$$

## §5 对当前运行与计划的影响（✓✓）

$$\text{① M=5 慢版}✓：\textbf{继续}✓ —— \text{它补齐}\ c_u=\tfrac12\ \text{在}\ u=5\ \text{的覆盖}✓（\text{档案声明的靶区最后一格}✓）$$
$$\text{② M=6..11}✗：\textbf{STOP 不变}✓ —— \text{在}\ \tfrac12\ \text{级覆盖范围之外}✗，\text{且应用侧}\ u\le5\ \text{本身就缺证}✗✓$$
$$\text{③ 新能力表述}✓（修正版）：\text{可写}\ \textbf{「单模证书}\to\text{阻尼情形（}u\le5\text{，条件性}）」✓；\ \textbf{不可写} 「\to\text{E4／}\tau\text{-Li 应用}」✗✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 应用侧上界缺证 命中文件数=0 ::
技术词 常数覆盖范围   命中文件数=0 ::
技术词 级差缺口       命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中}⟹\textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{阻尼缩放约化引理}✓（\texttt{C-181}✓）；\text{1/20 级一致定理}✓（\texttt{C-186}✓）$$

## §7 边界

$$\textbf{① 本档为缺口登记}✓，\text{不产定理、不跑计算}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ 不声称}\ u\le5\ \text{在应用中【不可能}】✗（\text{只是未证}✓）；\text{不声称}\ \texttt{C-181}\ \text{有错}✗（\text{其引理正确}✓，\text{只是被当成了应用侧结论}✗）$$
$$\textbf{④ M=5 慢版仍在跑}✓；\text{未追加计算}✓$$
