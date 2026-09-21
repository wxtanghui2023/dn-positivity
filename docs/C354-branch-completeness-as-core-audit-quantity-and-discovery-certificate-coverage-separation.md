已查地图（**先查后写**）：`C-353`（**逻辑层封口** ✓；三出口 ✓✓）、`C-352`（方系统方案 ✓）、`C-222`／`C-224`（**Krawczyk 存在性／唯一性 + 严格区间 B&B 四门** ✓✓ 可复用）、`C-190`（**v1／v3 数据混用禁令** ✓）。回查见 §6 ✓

D0: 本档对象 = **C-354：branch completeness 审计量 ＋ 三层分离协议**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 封口确认}✓✓：C\text{-}353\ \text{已排除三类误判}✓（\text{存在性}✓、\text{维数}✓、\text{蕴含方向}✓）\ \Longrightarrow \text{可视为}\ \textbf{逻辑层封口完成}✓✓$$
$$\textbf{② ⭐ 核心审计量}✓✓：\ \boxed{\textbf{branch completeness}}✓✓ \ —— \ \textbf{不是} \text{「找到了多少根」}✗✓，\text{而是}\ \text{「所有正解支是否被枚举／隔离 ＋}\ \beta\ \text{区间是否被覆盖」}✓✓$$
$$\textbf{③ 三件事严格分离}✓✓：\textbf{发现}（Newton \Rightarrow \text{candidate branch}✓）\ \ne\ \textbf{证书}（\text{区间 Newton／Krawczyk} \Rightarrow \text{存在性／唯一性}✓）\ \ne\ \textbf{覆盖}（\text{全支}✓）$$
$$\textbf{④ 禁止三级升级}✓✓：\text{即便扫过很多}\ \beta✓，\ \textbf{不能}把有限采样升级为「所有解支已覆盖」✗✓$$
$$\textbf{⑤ 真实要求}✓✓：\text{要得}\ \mathcal Z \cap E = \varnothing✓ \ \text{需要}\ \textbf{全部正解支的覆盖}✓✓（\text{而非若干漂亮的数值分支}✗）$$

## §1 三层分离表（✓✓）

| 层 ✓ | 手段 ✓ | 产出 ✓ | 能否升级 ✓ |
|---|---|---|---|
| 发现 ✓ | Newton（数值）✓ | candidate branch ✓ | **否** ✗ |
| 证书 ✓ | 区间 Newton／Krawczyk ✓ | 存在性／唯一性 ✓✓ | 局部可 ✓ |
| 覆盖 ✓ | 区间排除 ＋ 分支‐与‐界 ✓ | 全支覆盖 ✓✓ | **唯一可给出** `\mathcal Z \cap E = \varnothing` ✓ |

$$\textbf{纪律}✓✓：\text{发现层的结果}\ \textbf{只}能当候选✗✓；\text{证书层的结论}\ \textbf{仅}覆盖其区间✓；\text{覆盖层才谈全局}✓✓$$

## §2 覆盖所需对象（✓✓）

$$\textbf{对象一}✓：\beta \in (0,1]✓ \ \text{的}\ \textbf{区间细分 ＋ 排除证书}✓（\text{每格给}\ \textbf{无解} \text{或}\ \textbf{分支计数}✓）$$
$$\textbf{对象二}✓：\text{每}\ \beta\ \text{格的}\ \textbf{分支枚举 ＋ 区间隔离}✓（\text{Krawczyk 给唯一性}✓✓）$$
$$\textbf{对象三}✓✓：\textbf{退化点单独处理}✓：a_i\ \text{碰撞}✓、a_i = 1✓ \text{边界}✓、a_i \to 0✓ \ \Longrightarrow \ \text{对应}\ C\text{-}353\ \text{出口 (c)}✓（\textbf{moment-map singularity}✓✓）$$
$$\textbf{域}✓✓：\text{解域为}\ (0,1]^4✓（\text{有界}✓，\text{因}\ |c_j| \le 1✓）\ \Longrightarrow \text{覆盖在}\ \textbf{原则上有限}✓✓$$

## §3 结构增益（✓✓）

$$3+2\ \text{族}✓：4\ \text{方程} \times 4\ \text{未知}✓ \times 1\ \text{维参数}\ \beta✓ \Longrightarrow \ \boxed{\text{有限维、原则上可判定}}✓✓$$
$$\textbf{对比}✓✓：\text{原问题}\ E \subset [0,1]^5✓（\text{五维}✓）；\text{本路线}\ \textbf{降到一维参数 ＋ 四维代数}✓✓ \ —— \ \textbf{这是}\ C\text{-}352／C\text{-}353\ \text{带来的真正降维}✓✓$$
$$\textbf{可复用资产}✓✓：\text{现有}\ \textbf{区间 Krawczyk ＋ 四门 B\&B}✓（C\text{-}222／C\text{-}224✓）\ \text{与}\ \textbf{区间算术实现}✓ \ \Longrightarrow \text{无需新框架}✓✓$$

## §4 证书链（✓✓）

$$\text{C-352}（\text{方系统方案}✓） \ \longrightarrow \ \text{C-353}（\text{逻辑方向}✓＋\text{三出口}✓） \ \longrightarrow \ \text{C-354}（\textbf{完备性口径}✓✓） \ \longrightarrow \ \text{执行}✓$$
$$\textbf{出口映射}✓✓：\text{覆盖成功且全支} > \tfrac12✓ \Longrightarrow \mathcal Z \cap E = \varnothing✓；\text{出现}\ \le \tfrac12✓ \Longrightarrow \textbf{精确候选}✓✓；\text{出现退化}✓ \Longrightarrow \textbf{奇异性审计}✓✓$$
$$\textbf{目标}✓✓：\text{形成干净的}\ \textbf{证书链}✓，\textbf{不}再滑回「数值找到若干点} \to \text{猜全局结构」\ \text{的老路}✗✓$$

## §5 边界（✓✓）

$$\textbf{不得}写成✗：\mathcal Z \cap E = \varnothing\ \text{已证}✗；3+2\ \text{已空}✗；H = \varnothing\ \text{已证}✗；\text{采样即覆盖}✗$$
$$\textbf{诚实标注}⚠️✓：\text{本档为}\ \textbf{口径与协议档}✓，\textbf{零计算}✗，\textbf{不产生} \text{任何数学结论}✗✓；\text{覆盖任务}\ \textbf{尚未开始}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 分支完备性  命中文件数=0    :: 
技术词 区间隔离     命中文件数=1    :: ./C190-execution-checklist-local-simplex-analyticization-for-damped-M3.md 
技术词 排除证书     命中文件数=2    :: ./CLOSED-ROUTES-MAP.md ./V151-e4-direct-attack-counterexample-skeleton-certification-principles.md 
技术词 覆盖义务     命中文件数=0    :: 
```
- **零计算** ✗（协议档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **过程注记** ⚠️：本档起采用**防游离括号写法**（整句置于 `\text{...}` 内 ✓）＋ 提交前**深度解析自净**（仅删深度 0 的 `` ✓）
