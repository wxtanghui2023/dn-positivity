已查地图（**先查后写**）：`C-356`（**执行分层** ✓✓；`Krawczyk 不收敛 \not\Rightarrow 无根` ✓✓）、`C-355`（四锁 ✓✓）、`C-353`（**出口 (c)** ✓✓）、`C-352`（方系统 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-357：branch-complete audit 执行首轮（`\mathcal D_{\mathrm{reg}}`）＋ 奇异层命中**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① 有界搜索：根数 0}✗✓：\text{约束}\ a_i, b_2 \in (0,1]✓，\ \beta \in \{0.001, \dots, 1.0\}✓，\text{每}\ \beta\ \text{至多} 400\ \text{起点}✓ \Longrightarrow \textbf{零根}✗（\beta \le 0.4\ \text{已跑完}✓）$$
$$\textbf{② 放开上界后：正根存在}✓✓：\text{仅要求正性}✓ \Longrightarrow \beta = 0.1\ \text{得} 21\ \text{根}✓，\beta = 0.3\ \text{得} 16\ \text{根}✓，\ \textbf{且存在全部}\ \le 1\ \text{的根}✓✓$$
$$\textbf{③ ⭐ 奇异层命中}✓✓：\text{已发现解}\ \textbf{全部退化}✓（\text{某}\ a_i \to 0✓）\ \Longrightarrow \text{退回}\ \textbf{2+2／反称结构}✓✓（\text{如}\ a = (0.1, 0.278, 0)✓\ \text{与}\ \beta = 0.1, b_2 = 0.278✓）$$
$$\qquad \Longrightarrow \ \text{命中}\ C\text{-}353\ \text{出口 (c)}✓✓／C\text{-}355\ \text{锁 (2)}✓✓：\textbf{退化点即 singular stratum}✓✓，\textbf{不得}记为「无根」✗✓$$
$$\textbf{④ 执行层判定}✓✓：\ \mathcal D_{\mathrm{coll}}／\mathcal D_{\partial}（a_i \to 0✓）\ \textbf{必须先做降阶／对称化}✓✓；\ \mathcal D_{\mathrm{reg}}\ \text{的非退化}\ 3+2\ \text{分支}\ \textbf{仍未发现}✗$$

## §1 首轮执行记录（✓✓）

$$\textbf{轮次 A（有界）}✓：z = (a_1,a_2,a_3,b_2) \in (0,1]^4✓；\beta\ \text{扫描}\ 0.001 \sim 1.0✓；\text{Newton（阻尼＋域投影）}✓；\text{容差}\ 10^{-11}✓$$
$$\qquad \textbf{结果}✓：\beta = 0.001,\ 0.01,\ 0.05,\ 0.1,\ 0.2,\ 0.3,\ 0.4\ \text{全部}\ \textbf{根数} = 0✗✓$$
$$\textbf{轮次 B（仅正性，放开}\ \le 1✓）✓✓：\beta = 0.1\ \to 21\ \text{根}✓；\beta = 0.3\ \to 16\ \text{根}✓；\textbf{存在全部}\ a_i, b_2 \le 1\ \text{的根}✓✓$$
$$\qquad \text{示例}✓：a = (0.1,\ 0.278,\ \mathbf{0})✓，\ b_2 = 0.27804✓ \Longrightarrow \text{第 3 个原子}\ \textbf{消失}✓ \Longrightarrow \text{实为}\ \textbf{2+2}✓$$

## §2 奇异性诊断（✓✓）

$$\textbf{机制}✓✓：\text{退化点}\（a_i \to 0✓）\ \text{处}\ \text{四方程的}\ \textbf{Jacobian 秩下降}✗✓ \Longrightarrow \text{Newton 收敛速率崩塌}✗✓ \Longrightarrow \text{有界搜索}\ \textbf{系统性错过}✓✓$$
$$\qquad \Longrightarrow \text{这}\ \textbf{正是}\ C\text{-}355\ \text{锁 (2) 预言的危险逻辑}✓✓：\textbf{不收敛}\ \ne\ \text{无根}✗✓$$
$$\textbf{结构含义}✓✓：\text{退化解}\ \textbf{退回}\ (2+2)✓，\text{而}\ (2+2)\ \text{已证}\ \text{偶频成本} \ge 1.4677✓（C-348✓）\ \Longrightarrow \text{退化支}\ \textbf{不产生新反例}✓✓$$
$$\textbf{但}✗✓：\text{非退化}\ 3+2\ \text{分支（全部}\ a_i \ge \varepsilon > 0✓）\ \textbf{仍未发现}✗ \ —— \ \textbf{既不证实也不否证}✓$$

## §3 下一执行步（✓✓）

$$\textbf{步一}✓✓：\mathcal D_{\mathrm{reg}}\ \text{内}\ \textbf{排除退化邻域}✓（\text{要求}\ \min_i a_i \ge \varepsilon✓，\text{如}\ \varepsilon = 10^{-3}✓）\ \text{后重跑}✓$$
$$\qquad \text{判读}✓：\text{若}\ D_{\mathrm{reg}}\ \text{出现解支}✓ \Longrightarrow \text{沿支核算}\ \max_{r \le 12} F_{2r}✓（C\text{-}355\ \text{五件套⑤}✓）；\text{若无解支}✓ \Longrightarrow \text{仍}\ \textbf{不能}直接升级✗✓，\text{须先}\ \text{区间排除证书}✓✓$$
$$\textbf{步二}✓✓：\mathcal D_{\mathrm{coll}}（a_i = a_j✓）\ \text{与}\ \mathcal D_{\partial}（a_i \to 0,\ 1✓；\beta \to 0^+,\ \beta = 1✓）\ \text{各做}\ \textbf{降阶／边界分析}✓✓$$
$$\textbf{步三}✓：\text{覆盖账本}✓（\text{参数域}\ ✓＋\ \text{根盒隔离}✓＋\ \text{排除盒}✓＋\ \text{奇异层}✓）✓$$

## §4 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal Z \cap E = \varnothing\ \text{已证}✗；3+2\ \text{已空}✗；H = \varnothing\ \text{已证}✗；\textbf{有界搜索零根}\ ＝\ \text{「无根」}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{轮次 A 的零根}\ \textbf{只是}\ \text{发现层结果}✓，\text{且已由轮次 B 证明}\ \textbf{是方法性缺失}✓✓（\text{非数学空缺}✗✓）$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 执行记录     命中文件数=2    :: ./RESEARCH-CONSTITUTION.md ./FREEZE-2-coordinate-system-audit-novelty-ratio-and-retrieval-blind-spot.md 
技术词 退化解        命中文件数=10   :: ./REVIEW-V2H-freeze-V2-33-second-cut.md ./E185-T2d-double-closure-degenerates-density-criterion.md ./ARCHIVE-E180-E216-mechanism-exclusion-lineage.md 
技术词 有界无根     命中文件数=0    :: 
技术词 奇异层命中  命中文件数=0    :: 
```
- 运行记录 ✓：`/tmp/ex1.py`（有界 ✓，日志 `/tmp/ex1.log`✓）；`/tmp/ex2.py`（仅正性 ✓，日志 `/tmp/ex2.log`✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
