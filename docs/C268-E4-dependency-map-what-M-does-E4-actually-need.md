已查地图（**先查后写**）：`E4-palojarvi-finitely-many.md`（§3 Locus C／§5 扩展／§7 判词）、`E4-ENGINE-1`（§1 数值表）、`E4-ENGINE-2`（M=1 自足）、`E4-ENGINE-3`（衰减松弛＋残留逐字）、`E4-ENGINE-5`、`C-159`／`C-193`／`T13-A`／`C-265`（我方 M=1..4）。回查见 §5 ✓

D0: 本档对象 = **E4 依赖地图：E4 实际需要哪个 M** —— 关系 = 需求裁剪（决定阶梯去留）
D1: 0
FREEZE-ACK: 本档即冻结期内的依赖检索（依 §8.1；不产候选结论）

---

## §0 结论（一行 ✓✓）

$$\boxed{\textbf{E4 原定理只需}\ M=1✓✓，\text{且【早已自足}】✗✓；\text{扩展需}\ (\text{RP}_r)\ \text{于阈值}\ 3/40✓，r\le4\ \text{已被我方覆盖}✓✓}$$
$$\boxed{\textbf{故阶梯}\ M=5..11\ \text{对 E4}\ \textbf{无新增必要需求}✗✓（\text{仅为【条件性资产}】✓）}$$

## §1 依赖图（唐先生要的输出 ✓）

$$\textbf{E4（Palojärvi Thm 4.1 的} m\ \text{例外推广）}$$
$$\qquad \qquad \downarrow\ \text{引用}$$
$$\textbf{Montgomery Lemma 2.2}＝\text{Palojärvi p.6}＝\text{Ten Lectures Ch.5 Thm 11}✓：\ \max_{1\le n\le5M}\operatorname{Re}\sum_{j\le M}z_j^n\ge\tfrac1{20}✓$$
$$\qquad \qquad \downarrow\ \text{分两情形}$$
$$\textbf{① 原定理}\ (m=1)✓ \Longrightarrow \text{调用}\ \boxed{M=1}✓✓\（\texttt{E4-palojarvi}\ \S3\ \text{Locus C}\ \textbf{逐字}：「\text{The '5' here is exactly }5M\text{ of Lemma 2.2 with }M=1」\ ✓）$$
$$\qquad \Longrightarrow \textbf{状态}✓✓：\textbf{已自足}✓（\texttt{E4-ENGINE-2}：\text{初等覆盖引理}\textbf{替代}\ \text{Lemma 2.2 的}\ M=1\ \text{情形}✓，\textbf{常数}\downarrow10\ \text{倍}✓）\ \Longrightarrow \text{不需 Montgomery}✓✓$$
$$\textbf{② 扩展}\ (m\ge2)✓ \Longrightarrow \text{残留（}\texttt{E4-ENGINE-3}\ \S3\ \textbf{逐字}✓）：\text{等模长子集}\ K,|K|=r\ge2\ \text{需}$$
$$\qquad \qquad \exists k\le5r:\ \sum_{j\in K}\operatorname{Re}z_j^{k}\ \ge\ \tfrac1{20}+\tfrac1{40}\ =\ \boxed{\tfrac3{40}}\tag{$\star\star\star$}$$
$$\qquad \Longrightarrow \textbf{这正是}\ (\text{RP}_r)\ \text{在阈值}\ 3/40\ \text{处的需求}✓✓；\ r=|\{j:|w_j|=R'\}|✓（\text{并列最大模的例外零点数}✓）$$

## §2 我方覆盖 vs 需求（✓✓）

| 需求 | 阈值 | 我方状态 |
|---|---|---|
| $(\text{RP}_1)$ | $3/40$ | ✓✓ **已证且锐**：`C-159` 鸽笼 $\ge\tfrac12$（$=6.7\times$ 阈值）|
| $(\text{RP}_2)$ | $3/40$ | ✓✓ **已证**：`C-193`（值 $\tfrac12$ ＋等号集）；`C-152`/`C-153`；`C-199`/`C-200` |
| $(\text{RP}_3)$ | $3/40$ | ✓✓ **已证**：`T13-A`（$m_3=0.764$）；`C-216`–`C-219` |
| $(\text{RP}_4)$ | $3/40$ | ✓✓ **已证**：`C-265`（$\ge\tfrac12$，区间算术严格）|
| $(\text{RP}_5)$ | $3/40$ | ⬜ 慢版 M=5 正在跑（§4）|
| $(\text{RP}_6..11)$ | $3/40$ | ✗ 未做（阶梯）|

$$\textbf{数值余量巨大}✓（\texttt{E4-ENGINE-1}\ \S1\text{B}✓）：\text{窗口}5M\ \text{下}\ M=1\to0.500,\ 5\to1.272,\ 10\to2.236✓ \Longrightarrow \text{阈值}\ 0.075\ \text{被远超}✓✓$$

## §3 启下判定（按唐先生三条硬判据 ✓✓）

$$\textbf{① 独立性}✓：(\text{RP}_r)\ \text{是独立极值问题}✓$$
$$\textbf{② 启下性}✓✗：\text{对【原定理}】\ \text{启下＝已由}\ \texttt{ENGINE-2}\ \text{取得}✓✓（\text{不需阶梯}✗）；\text{对【扩展}】\ \text{启下}\ \textbf{被}\ \S7\ \text{判词阻断}✗✓$$
$$\qquad \S7\ \textbf{逐字}✓：\text{「a genuine, cheap generalization, but it buys nothing unless you can independently bound the number of off-line zeros」}✓$$
$$\qquad \Longrightarrow \text{扩展要变成【能力】，需【独立】离线零点个数界}✗\text{＝已知墙}✓\text{；未见此界前，}r\ge5\ \text{的覆盖＝}\textbf{条件性资产}✓$$
$$\textbf{③ 能力匹配}✓：（\text{RP}_r)\ \text{正是我方证书引擎的主场}✓✓（\texttt{C-267}\ v3✓）$$
$$\Longrightarrow \boxed{\textbf{判定}✓：\text{阶梯}\ M=5..11\ \textbf{非当前必要}✗✓；\text{但属【有明确条件的资产}】✓（一旦出现离线零点个数界，r\ \text{范围立即有用}✓）}$$

## §4 当前运行项处置建议（不擅自行动 ✓）

$$\text{慢版 M=5}✓：\text{已跑}\sim1\text{h}20\text{m}✓，\text{RSS}\ 16\ \text{MB}✓，\text{只在结束时打印}✗$$
$$\qquad \text{按新判据}✓：\text{它对 E4}\ \textbf{无必要需求}✗（r=5\ \text{属条件性资产}✓）\ \Longrightarrow \textbf{可停可留}✓，\text{由唐先生定}✓$$
$$\qquad \textbf{我的建议}✓：\text{让它跑完}✓\text{（机时已沉没，且可得 }r=5\ \text{ 的金标准）}\ \text{但}\ \textbf{不启动} M=6..11✗✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 依赖地图检索   命中文件数=0 ::
技术词 需求裁剪       命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{两项各 0 命中}⟹\textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{Lemma 2.2 调用点}✓（\texttt{E4-palojarvi}\ \S3✓）；\text{残留}(\star\star\star)✓（\texttt{ENGINE-3}✓）$$

## §6 边界

$$\textbf{① 本档为依赖检索}✓，\text{不产定理}✗；\ \textbf{② 未用 RH}✓（\text{仅引 Palojärvi 结构}✓）；\text{未改他档正本}✓$$
$$\textbf{③ 不声称阶梯无价值}✗ —— \text{它是【条件性资产}】✓（\text{条件＝独立离线零点个数界}✓）$$
$$\textbf{④ 未验证}\ r\ \text{的上界}✗（r\le m✓，\text{而}\ m\ \text{本身无界}✗）$$
