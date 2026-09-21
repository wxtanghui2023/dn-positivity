已查地图（**先查后写**）：`C-351`（三分裂 ✓✓；`3+2` 为唯一核心 ✓）、`C-350`（**`\mathcal Z \cap E \ne \varnothing \Rightarrow H \ne \varnothing`** ✓✓）、`C-348`（反称成本 ✓）。回查见 §5 ✓

D0: 本档对象 = **C-352：`3+2` 族参数化首刀 ＋ 方系统方案**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 首刀未找到解}⚠️✓：40 起点（对数参数化 ＋ 模式搜索，容差 10^{-20}✓）\ \textbf{找到零矩解} = \textbf{0}✗✓ \ —— \ \textbf{「未找到」 ≠ 「不存在」}✗✓$$
$$\qquad \textbf{方法偏弱}⚠️：\text{一维族嵌在五维中}✓，\text{随机下降}\ \textbf{难以命中}✗✓ \Longrightarrow \text{本档}\ \textbf{不}据此判 3+2\ \text{为空}✗$$
$$\textbf{② 维数核算}✓✓：\text{未知}\ (a_1,a_2,a_3,b_1,b_2) = 5✓；\text{方程}\ 4✓（r = 1,3,5,7✓）\ \Longrightarrow \textbf{预期一维族}✓✓ \Longrightarrow \text{解}\ \textbf{应当存在}✓$$
$$\textbf{③ 下步方系统}✓✓：\textbf{固定}\ b_1✓ \Longrightarrow \text{未知}\ (a_1,a_2,a_3,b_2) = 4✓，\text{方程}\ 4✓ \Longrightarrow \textbf{方系统}✓✓ \Longrightarrow \text{离散解族}✓（\text{可用 Newton／区间法}✓）$$
$$\textbf{④ ⭐ 逻辑锁死（重要）}✓✓：\ \mathcal Z \cap E = \varnothing \ \Longrightarrow\ \text{只排除}\ \textbf{精确抵消型} \text{反例}✓，\ \textbf{不}直接推出\ H = \varnothing✗✓$$
$$\qquad \text{因}\ C\text{-}350\ \text{的等价仅为}\ \text{单向}✓：\mathcal Z \cap E \ne \varnothing \Rightarrow H \ne \varnothing✓；\text{逆否为}\ H = \varnothing \Rightarrow \mathcal Z \cap E = \varnothing✓，\textbf{不可反用}✗✓$$
$$\textbf{⑤ 纪律}✓✓：\textbf{不}做\ Bridge\ A✗、\textbf{不}拆\ SOS✗、\textbf{不}盲搜索✗、\textbf{不}扩频率✗$$

## §1 首刀计算记录（✓✓）

$$\textbf{设定}✓：3+2\ \text{分裂}✓：a_1,a_2,a_3 > 0✓，b_1,b_2 > 0✓，\ |a_i|, |b_j| \le 1✓（\text{因}\ |c_j| \le 1✓）$$
$$\textbf{条件}✓：\sum_{i \le 3} a_i^r = \sum_{j \le 2} b_j^r✓（r = 1,3,5,7✓）$$
$$\textbf{目标函数}✓：R(a,b) = \sum_{r \in \{1,3,5,7\}} \big(\sum_{i \le 3} a_i^r - \sum_{j \le 2} b_j^r\big)^2✓$$
$$\textbf{搜索}✓：对数参数化（保持正性 ✓）＋ 40 起点 ＋ 模式搜索 900 轮 ✓；\textbf{判据}：R < 10^{-20}✓$$
$$\textbf{结果}✓：\textbf{0 个}解✗✓ \ —— \ \text{但}\ \textbf{不能}据此下结论✗✓（\text{见 §0①／§0③}✓）$$

## §2 维数与方系统（✓✓）

$$\textbf{自由参数}✓：5\ \text{未知} - 4\ \text{方程} = 1✓ \Longrightarrow \text{一维曲线}\ t \mapsto (a(t), b(t))✓✓$$
$$\textbf{方系统策略}✓✓：\text{固定}\ b_1 = \beta✓（\text{扫描}\ \beta \in (0,1]✓）\ \Longrightarrow \text{解}\ F_\beta(a_1,a_2,a_3,b_2) = 0✓（4 \times 4✓）$$
$$\qquad \Longrightarrow \text{每个}\ \beta\ \text{给离散解集}✓ \Longrightarrow \text{沿解支}\ \text{核算}\ F_{2r}✓✓ \ —— \ \text{这是}\ \textbf{定向} \text{结构计算}✓，\textbf{不是}盲搜索✗✓$$
$$\textbf{端点障碍（C-351）}✓✓：M \le \sqrt{3.3} \approx 1.817✓ \Longrightarrow \text{潜在}\ E\ \text{交点}\ \textbf{只能在中间紧致区间}✓✓；\text{且}\ a,b \to 0\ \text{端被}\ F_4 \to 5✗\ \textbf{排除}✓✓$$

## §3 ⭐ 逻辑锁死（✓✓，本档重要更正 ✓）

$$\textbf{C-351 的表述}✗：\text{「若找到明确}\ c_0 > \tfrac12✓，\text{立即得}\ \mathcal Z \cap E = \varnothing✓\ \textbf{并进一步推出}\ H = \varnothing」✗✓$$
$$\textbf{问题}✓✓：\text{后一步}\ \textbf{不成立}✗ \ —— \ \text{因}\ C\text{-}350\ \text{只给单向蕴含}✓✓：\mathcal Z \cap E \ne \varnothing \Rightarrow H \ne \varnothing✓$$
$$\qquad \text{其逆否}\ H = \varnothing \Rightarrow \mathcal Z \cap E = \varnothing✓\ \text{为真}✓，\text{但}\ \textbf{不可反用}✗✓ \Longrightarrow \ \mathcal Z \cap E = \varnothing \ \textbf{推不出}\ H = \varnothing✗✓$$
$$\textbf{正确链条}✓✓：\mathcal Z \cap E = \varnothing \Longrightarrow \text{排除}\ \textbf{精确抵消型} \text{反例}✓✓；\text{要证}\ H = \varnothing✓ \ \textbf{仍须} \text{Bridge A 型论证}✓（\text{即}\ \text{「近抵消」}\ \text{也要付出偶频成本}✓）$$
$$\Longrightarrow \ \textbf{战略含义}✓✓：\text{本阶段}\ \textbf{可以先独立完成}\ \mathcal Z \cap E\ \text{审计}✓（\text{有价值}✓），\text{但}\ \textbf{不要}以为 \text{它就等于主线收口}✗✓$$

## §4 下一步（✓✓，登记不执行 ✓）

$$\textbf{优先}✓✓：\text{实施}\ \textbf{方系统} \text{策略}✓（固定\ b_1✓、Newton／区间法解 4 \times 4✓）\ \Longrightarrow \text{得到解支}✓ \Longrightarrow \text{沿支核算}\ \max_{r \le 12} F_{2r}✓$$
$$\textbf{判据}✓：\text{若沿支}\ \max_{r \le 12} F_{2r} > \tfrac12✓ \Longrightarrow \textbf{排除精确抵消型反例}✓✓；\text{若出现}\ \le \tfrac12✓ \Longrightarrow \textbf{反例候选}✓✓ \Longrightarrow \text{转高精度复核}✓$$
$$\textbf{禁止}✓✓：\textbf{不}把\ \text{「0/40 未找到」}\ \text{当作}\ \text{「3+2 空」}✗✓；\textbf{不}跳过方系统直接宣告✗$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 方系统        命中文件数=0    :: 
技术词 维数核算     命中文件数=0    :: 
技术词 精确抵消型反例 命中文件数=0    :: 
技术词 逻辑锁死     命中文件数=1    :: ./C349-cancellation-ideal-and-bridge-inequality-candidate.md 
```
- 运行记录 ✓：脚本 `/tmp/p4k.py` ✓（40 起点；日志 `/tmp/p4k.log` ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`3+2` 已空 ✗（**未找到** ✓）；`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；`\mathcal Z` 已分类 ✗
