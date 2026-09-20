已查地图（**先查后写**）：`FREEZE-AUDIT-FZ1-FZ4.md`（六母机制）、`C257`（第三族判断，本档修正对象）、`C125`/`C126`/`C127`（尺度墙）、`C124`（固定无零区域不与 RH 等价）、`V139`/`V140`（Brauer–Siegel 关闭）、`POS1`（de la Vallée Poussin 正性恒等式）、`V161`（另有【反证审计】用法）、`E18`:46、`MASTER-STATUS`:13。回查见 §7 ✓

D0: 本档对象 = **FZ-1 反证审计：主动寻找一个满足 SURVIVOR-5 的 M1–M6 反例；结果＝找到（M3／M4／M5）** —— 关系 = 反证审计（修正 C-257）
D1: 0
FREEZE-ACK: 本档即冻结期内的反证审计（依 §8.1；不产候选结论）

---

## §0 结论（反证成功 ✓✓）

$$\boxed{\textbf{① 找到 survivor}✓✓：\textbf{M3（界定／正性）}、\textbf{M4（局部数据）}、\textbf{M5（双线性耦合）}\ \text{三格各有合格反例}✓✓}$$
$$\boxed{\textbf{② 故 C-257 的【强读法】被反证}✗✓：\text{「M1–M6 不能产出非平凡 RH 相关量」}\ \textbf{为假}✗✗}$$
$$\boxed{\textbf{③ 修正后的弱读法}✓✓：\text{(i) 我方【近期】产出定理的线全在第三族}✓；\text{(ii) M1–M6 的产出【有已知天花板}】✓（\text{尺度墙／log 退化／落在 RH 判据上}✓）}$$
$$\boxed{\textbf{④ 分红}✓✓：\text{最强 survivor（M3）恰是}\ \textbf{T5}（\text{显式无零区常数}✓，「最短可发表路径」✓）\Longrightarrow \text{审计与靶子清单【交叉印证}】✓✓}$$
$$\boxed{\textbf{⑤ 结论}✓：\text{第三族＝【近期实践观察}】✓，\textbf{不是结构律}✗✓ \Longrightarrow \text{(甲) 可恢复，但须按弱读法}✓}$$

## §1 审计协议（按唐先生规格 ✓）

$$\text{成功定义（严格}✓）——\text{以下【不算}】✗：\text{已有 RH 判据重包装}✗｜\text{显式公式／Weil 正性换符号}✗｜\text{仅得零点统计或数值相关}✗｜\text{只证邻近定理}✗｜\text{对象漂亮但无新量}✗$$
$$\boxed{\text{SURVIVOR-5}✓：\text{① Natural（非为 RH 倒造）② Non-redundant（非档案已有判据）③ Arithmetic（明确算术来源）④ Quantitative（产生新可计算量）⑤ RH-interface（严格可追踪的 RH 接口}）}$$
$$\textbf{每一格只需一个 survivor 即证伪本档}✓；\text{失败只记【该格 failed audit}】✗，\textbf{不得外推为「不存在」}✗✓（\text{遵唐先生原话}✓）$$
$$\textbf{量变判据}✓✓（\text{唐先生关键一刀}✓）：\text{必须问【该机制有没有改变被测量的 quantity}】✓ —— \text{若只是}\ \zeta\to\text{representation}\to\text{trace}\to\text{positivity}\ \text{则仍是对象侧重编码}✗✓$$

## §2 ⭐ Survivor 1 —— **M3（界定／正性）**：显式无零区域 ✓✓

$$\text{机制链}✓：\text{de la Vallée Poussin（1899）正性恒等式}\ 3+4\cos t+\cos 2t=2(1+\cos t)^2\ge0✓$$
$$\qquad \Longrightarrow \zeta(s)^3\zeta(s+it)^4\zeta(s+2it)\ \text{的组合非负性} \Longrightarrow \text{无零区域}\ \sigma>1-\tfrac{c}{\log t}✓✓$$
$$\qquad \text{显式化谱系}✓：\text{Rosser–Schoenfeld}→\text{Ford}→\text{Kadiri}→\text{Trudgian}→\text{Mossinghoff–Trudgian}✓（\text{最佳形}\ \tfrac{c}{(\log t)^{2/3}(\log\log t)^{1/3}}✓）$$
$$\textbf{SURVIVOR-5 逐项}✓✓：\text{① Natural}✓（\text{经典，非倒造}✓）\text{② Non-redundant}✓（\textbf{不是 RH 判据}✓，是\textbf{无条件定理}✓）\text{③ Arithmetic}✓（\text{Euler 积／von Mangoldt}✓）$$
$$\qquad \text{④ Quantitative}✓✓（\text{区的边界}＋\text{显式常数}\ c\ \textbf{是可计算的新量}✓✓）\text{⑤ RH-interface}✓（\text{无零区}\Rightarrow\text{PNT 误差项}✓；\text{且是 τ-Li 判据的输入}✓）$$
$$\Longrightarrow \boxed{\textbf{M3 有 survivor}✓✓；\text{且它就是}\ \textbf{T5}✓\ \text{（与靶子清单交叉印证}✓✓）}$$
$$\qquad ⚠️\ \text{但天花板已知}✓：\text{此类排除随}\ \log\ \text{退化}✓（\texttt{C-125}/\texttt{C-126}✓），\text{固定}\ \delta\ \text{型＝PNT 缺的幂次节省}✗$$

## §3 Survivor 2 —— **M4（局部数据）**：解析类数公式 ✓✓

$$\text{机制链}✓：\text{Dirichlet 解析类数公式}\ h(D)\cdot L(1,\chi)=\text{（显式因子）}✓ \Longrightarrow \text{局部算术数据（模数／特征）产生全局量}\ h(D)✓✓$$
$$\textbf{SURVIVOR-5}✓：\text{① Natural}✓\ \text{② Non-redundant}✓（\text{非 RH 判据}✓）\text{③ Arithmetic}✓✓（\text{类数／特征}✓）\text{④ Quantitative}✓✓（\ h(D)\ \text{与}\ L(1,\chi)\ \text{皆可计算}✓）\text{⑤ RH-interface}✓✓（\textbf{Siegel 零点}✓＝离轴零点的「最坏情形」类比；\text{无 Siegel 零点}＝\text{GRH 型断言}✓）$$
$$\qquad ⚠️\ \text{但档案已关闭【Brauer–Siegel 路线}】✗（\texttt{V139}/\texttt{V140}✓）—— \text{关闭的是【路线}】✓，\textbf{不是这个量}✗✓$$
$$\Longrightarrow \boxed{\textbf{M4 有 survivor}✓✓（\text{量真实存在}✓；\text{其一条经典路线已封}✗）}$$

## §4 Survivor 3 —— **M5（双线性耦合）**：Petersson／Kuznetsov 迹公式 ✓✓

$$\text{机制链}✓：\text{Petersson／Kuznetsov 迹公式（Hecke 本征值 ↔ Kloosterman 和}✓） \Longrightarrow \text{Hecke 本征值的等分布（Duke／Sarnak／Serre}✓）\ \text{与}\ \textbf{subconvexity}✓✓$$
$$\textbf{SURVIVOR-5}✓：\text{① Natural}✓\ \text{② Non-redundant}✓\ \text{③ Arithmetic}✓✓（\text{Hecke 本征值／Kloosterman}✓）\text{④ Quantitative}✓✓（\text{等分布速率}＋\text{subconvexity 指数}✓）\text{⑤ RH-interface}✓（\text{RH}\Rightarrow\text{Lindelöf}\Rightarrow\text{subconvexity}✓）$$

## §5 三格 failed audit（如实登记 ✓，不外推 ✗）

$$\textbf{M1（表示）}✗：\text{显式公式}\to N(T),S(T)✓ \Longrightarrow \text{项 ② 失败}✗（\ S(T)\ll\tfrac{\log T}{\log\log T}\iff RH\ \textbf{本身就是判据}✗）;\ N(T)\ \text{本身无条件且不对 RH 敏感}✗$$
$$\textbf{M2（对称化）}✗：\text{对偶／函数方程给【中心}】✓\ \text{不给【选择}】✗（\text{FZ-1 原话}✓）；\text{候选（Weil 正性／Brauer–Siegel）皆为重编码或已封}✗$$
$$\textbf{M6（运动）}✗：\text{DBN 热流}\to\Lambda✓ \Longrightarrow \text{项 ② 失败}✗（RH\iff\Lambda\le0\ \textbf{是判据}✗）；\text{其余「流」＝显式公式的重新参数化}✗$$

## §6 对 C-257 的修正（按唐先生规则 ✓✓）

$$\textbf{原（强）}✗：\text{「M1–M6 不能产出非平凡 RH 相关量」} \Longrightarrow \textbf{被本档反证}✗✗（\text{M3／M4／M5 各有 survivor}✓✓）$$
$$\textbf{修正（弱）}✓✓：\boxed{\text{(i) 我方【近期】产出定理的线全在第三族}✓（\text{事实}✓，\text{N=4 条线}✓）；\text{(ii) M1–M6 的产出【有已知天花板}】✓（\text{尺度墙／log 退化／落在 RH 判据上}✓）}$$
$$\qquad \Longrightarrow \boxed{\text{第三族＝【近期实践观察 ＋ 天花板对照}】✓，\textbf{不是结构律}✗✓}$$
$$\textbf{对优先级的影响}✓：(甲)\ \text{可恢复}✓（\text{但按弱读法}✓）；\text{(丙) 写入 Protocol 时【必须写成弱读法}】✓✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 SURVIVOR     命中文件数=0 :: 
技术词 反证审计     命中文件数=3 :: ./V161-*.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md
技术词 量变判据     命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{「SURVIVOR-5」（0）}✓、\text{「量变判据」（0）}✓$$
$$\textbf{② 档案已有（引用，不列为本档提出）}✓✓：\textbf{「反证审计」（3 命中}✓，\text{首见}\ \texttt{V161}✓，\text{另有总图／台账两处}✓）—— \text{本档用法为「反证性审计」（沿用）}✓，\textbf{不主张首次命名}✗$$
$$\textbf{③ 通用词（不计）}✓：\text{「serender／天花板／对象侧」}✓$$

## §8 边界

$$\textbf{① 本档为反证审计}✓，\text{不产候选结论}✗；\textbf{② 未用 RH}✓；\text{未改他档正本}✓（\text{仅追加 C-257 指针}✓）$$
$$\textbf{③ 本档【不声称】M1–M6 中未找到 survivor 的三格不可能}✗（\text{只记 failed audit}✓，\text{遵唐先生原话}✓）$$
$$\textbf{④ survivor 的「结算」限于【是否产出非平凡量}】✓，\textbf{不含「能否推到 RH」✗}（\text{后者由天花板栏负责}✓）$$

---

## §9 【追加·唐先生 2026-09-20 20:57 修正】SURVIVOR-5 第五项的**二级标签**

$$\textbf{问题}✗✓：\text{本档 §4 对 M5 只写了 } RH\Rightarrow\text{Lindel\"o}f\Rightarrow\text{subconvexity}✓，\text{这是【单向 RH-interface}】✓—— \text{若第五项只要求「严格可追踪的 RH 接口」，M5 可过}✓；\textbf{但不得与「直接产生 RH 障碍敏感量」混为一谈}✗✓$$

$$\boxed{\text{第五项的二级标签}✓✓：\quad R_1=\text{RH 导出型}；\qquad R_2=\text{RH 障碍敏感型}}$$

| 格 | 本档判定的强度 | 依据 |
|---|---|---|
| **M3** | $R_2$ ✓✓ | 无零区域＝对**障碍本身**（零点位置）敏感；且是 τ-Li 判据的输入 |
| **M4** | $\ge R_2$ ✓ | Siegel 零点接口＝障碍敏感（Siegel 零点即最坏情形零点） |
| **M5** | $R_1$ ✓ | 目前只展示 RH $\Rightarrow$ Lindelöf $\Rightarrow$ subconvexity（导出型） |

$$\Longrightarrow \textbf{本档 §4 的 M5 survivor 判定不变}✓（\text{它仍然满足第五项}）；\text{但强度须标为 }R_1✓，\textbf{不得与 M3／M4 并列}✗✓$$
$$\qquad \text{该二级标签已写入 }\texttt{PROTOCOL}\ \S12\ \text{层 3}✓✓（\text{避免以后强度混用}）$$

