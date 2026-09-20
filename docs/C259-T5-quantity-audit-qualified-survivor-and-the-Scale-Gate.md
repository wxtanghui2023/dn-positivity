已查地图（**先查后写**）：`C258`（反证审计，survivor）、`C257`（第三族）、`PROTOCOL-minimax-closure-template.md` §12–§13、`C124`（固定无零区域不与 RH 等价）、`C125`/`C126`/`C127`（尺度墙）、`V122`（密度路线 DEAD）、`V283`（N(σ,T) 值面）、`V139`/`V140`（Brauer–Siegel 关闭 `V213`（另有【突破门】用法）。回查见 §7 ✓

D0: 本档对象 = **T5 quantity 审计：两级成功判定 ＋ 勘误 ＋ 新增硬门槛 Scale Gate** —— 关系 = 计数与定级（封存 T5 为 benchmark）
D1: 0
FREEZE-ACK: 本档即冻结期内的审计与门槛固化（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① T5 通过 SURVIVOR-5}✓✓，\textbf{但不通过「突破门」}✗✓：\text{两级成功}\ \begin{cases}\text{survivor}✓,\ \text{new quantity}✓\\ \text{new scale}✗,\ \text{new RH bridge}✗\end{cases}}$$
$$\boxed{\textbf{② 状态定性}✓✓：\textbf{QUALIFIED SURVIVOR ／ ADJACENT-THEOREM ASSET}✓（\textbf{不是} NO-GO✗，\textbf{也不是} RH 主线✗）}$$
$$\boxed{\textbf{③ 核心发现}✓✓：\text{「quantity changed}\Longrightarrow\text{scale changed」}\ \textbf{为假}✗✗ —— \text{本轮最重要的收获}✓✓}$$
$$\boxed{\textbf{④ 勘误}✓✓：\text{纯三角正性只给}\ 1/\log t\ \text{型尺度}✓；\ \tfrac1{(\log t)^{2/3}(\log\log t)^{1/3}}\ \textbf{不来自三角正性}✗（\text{来自指数和／估计机制}✓）}$$
$$\boxed{\textbf{⑤ 新硬门槛}✓✓：\textbf{Scale Gate}（写进 `PROTOCOL` §14）—— \text{quantity 变了但仍在旧尺度墙}\Rightarrow\textbf{不升 RH 主线}✗✓}$$

## §1 SURVIVOR-5 通过（逐条 ✓）

$$N\ ✓\（\text{de la Vallée Poussin 1899，非为 RH 倒造}✓）;\quad NR\ ✓\（\text{无条件定理，非 RH 判据}✓）;\quad A\ ✓\（\text{Euler 积／von Mangoldt}✓）$$
$$Q\ ✓\（\text{区的边界＋显式常数}\ c\ \text{是可计算新量}✓）;\quad R\ ✓\（R_2\ \text{型}✓：\text{对障碍本身敏感，且为 τ-Li 判据输入}✓）$$
$$\qquad 3+4\cos\theta+\cos 2\theta=2(1+\cos\theta)^2\ge0✓ \Longrightarrow \textbf{确实产生无条件、定量的 zero-free information}✓✓$$
$$\Longrightarrow \boxed{\textbf{T5 不得再归入 CLOSED}✗✓}$$

## §2 三个 quantity 层级（本档核心区分 ✓✓）

$$\textbf{A · zero-free boundary}✓：\sigma\ge1-\delta(t)✓；\text{经典正性给【显式}\ \delta(t)✓，\text{尺度属}\ \delta\asymp\tfrac1{\log t}\ \text{类}✓$$
$$\qquad ⚠️\ \textbf{勘误}✗✓：\text{真正的 Vinogradov–Korobov 型尺度}\ \tfrac1{(\log t)^{2/3}(\log\log t)^{1/3}}\ \textbf{来自不同机制}（\text{指数和／估计}✓）$$
$$\qquad \qquad \Longrightarrow \textbf{不得归因给单纯的三角正性}✗✓（\text{避免以后把两条机制混成一条}✓）$$
$$\textbf{B · zero-density}✓：N(\sigma,T)\ \text{确是新的 quantitative observable}✓；\text{但若仅作为 value-face 量控制零点数量}✓$$
$$\qquad \Longrightarrow \ Q_{density}\neq Q_{RH\ bridge}✓✓（\text{不自动产生新的 pointwise off-line exclusion}✗）$$
$$\textbf{C · oscillation／PNT error}✓：\psi(x)-x\ \text{或其振荡常数}✓\ \text{确改变了被测量}✓ \Longrightarrow \text{但与同一 analytic scale 紧密相连}✓$$
$$\qquad \Longrightarrow \textbf{「quantity changed」 不推出 「scale changed」}✗✓✓$$

## §3 两级成功 ＋ 状态定性（✓✓）

$$\boxed{\text{M3 survivor}\ \checkmark}\qquad\boxed{\text{new quantity}\ \checkmark\quad\text{new scale}\ \times}\qquad\boxed{\text{new RH bridge}\ \times}$$
$$\Longrightarrow \boxed{\textbf{QUALIFIED SURVIVOR ／ ADJACENT-THEOREM ASSET}✓✓}（\text{与档案既有分类吻合}✓）$$

## §4 C142 乙类的**新判据**（三门 ＋ 五档 ✓✓）

$$\boxed{\textbf{三门}✓✓：\text{Rule T}\to\text{SURVIVOR-5}\to\textbf{Scale Gate}}$$

| 层级 | 判定 |
|---|---|
| 只有 quantity 改变 | 保留，但不升主线 ✓ |
| quantity ＋ **新尺度** | **重点候选** ✓✓ |
| quantity ＋ 新尺度 ＋ 新 RH-interface | **真正主线候选** ✓✓✓ |
| quantity 改变但仍落旧尺度墙 | **邻近定理资产** ✓ |
| quantity 实际只是旧量重参数化 | **Rule T CLOSED** ✗ |

$$\boxed{\textbf{Scale Gate}✓✓：\text{若新 quantity 最终仍受既有}\ 1/\log T\ \text{或已知 value-face／log-degradation 天花板约束}\Rightarrow\textbf{不升 RH 主线}✗✓}$$
$$\qquad \text{目的}✓：\text{避免「发现漂亮新量}\to\text{兴奋开新线}\to\text{最后仍撞原墙」的循环}✗✓$$

## §5 T5 的**校准器**身份（✓✓）

$$\boxed{\text{T5 证明：}\ \textbf{SURVIVOR-5}\not\Longrightarrow\textbf{突破}✓✓} \Longrightarrow \text{以后必须再过 scale gate}✓$$
$$\qquad \text{T5 的职责已完成}✓：\text{反证 FZ-1}\to\text{确认 M3 有真 survivor}\to\text{检查 quantity}\to\text{发现 scale wall}✓✓$$
$$\qquad \Longrightarrow \textbf{已产生方法论资产}✓✓；\text{T5 保留为 benchmark}✓，\textbf{不再投主力}✗$$

## §6 措辞纪律（本档严格执行 ✓✓）

$$\textbf{禁止}✗✗：\text{写成「正性产生的所有 quantity 都必然 log-degrading」的}\textbf{无条件定理}✗$$
$$\textbf{正确}✓✓：\boxed{\textbf{本次已审计的 quantity classes 均未越过既有尺度墙}}✓ \Longrightarrow \text{仅为本次审计范围内的判定}✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 尺度门      命中文件数=0 :: 
技术词 校准器      命中文件数=0 :: 
技术词 两级成功    命中文件数=0 :: 
技术词 突破门      命中文件数=3 :: ./V213-*.md ./CLOSED-ROUTES-MAP.md ./MASTER-STATUS-AND-CLOSURES.md
```
$$\textbf{① 本档新增}✓：\text{「尺度门」（0）}✓、\text{「校准器」（0）}✓、\text{「两级成功」（0）}✓$$
$$\textbf{② 档案已有（引用，不列为本档提出）}✓✓：\textbf{「突破门」（3 命中}✓，\text{首见}\ \texttt{V213}✓，\text{另有总图／台账}✓）—— \text{本档沿用其义}✓，\textbf{不主张首次命名}✗$$
$$\textbf{③ 通用词（不计）}✓：\text{「quantity／scale／asset」}✓$$

## §8 边界

$$\textbf{① 本档为审计与定级}✓，\text{不产候选结论}✗；\textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ 不声称正性机制的潜力已穷尽}✗（\text{只判本次已审 quantity classes}✓）；\text{不声称 T5 无价值}✗（\text{它是合格 survivor ＋ 资产}✓）$$
$$\textbf{④}✓：\text{§2A 的勘误为机制归属级陈述}✓\text{，本档未逐条核原始文献}✗\text{（标 [需逐字核]}✓\text{）}$$
