已查地图（**先查后写**）：`C-265`（M=4 已证）、`C-216`–`C-219`（M=3 阶梯）、`E4-ENGINE-5`（§2 二阶矩族 M≳12 必死；§3b qM 线索）、`C-142`（(RP_M) 为乙类资产 #1）、`papers/rpM-window-cosines/main.md`（现含"数值 M≤11"＋M=2,3 定理）、`PROTOCOL`（四门／A+B+C）。回查见 §6 ✓

D0: 本档对象 = **(RP_M) 阶梯的工作计划：承上启下链 ＋ 自有优势 ＋ 成本预注册 ＋ kill 规则** —— 关系 = 工作计划（非审计、非结果）
D1: 0
FREEZE-ACK: 本档即冻结期内的工作计划（依 §8.1）

---

## §1 承上（这一步从哪来 ✓）

$$\text{论文A 现状}✓（逐字）：\text{「numerics } M\le11\text{」}\ ＋\ \text{M=2,3 定理}✓ \Longrightarrow \textbf{表里 M}\ge4\ \text{是【数值}】✗，\text{不是定理}✗✓$$
$$\text{本会话已补}✓✓：\text{M=4}\ \Longrightarrow\ m_4\ge\tfrac12\ \text{（区间算术严格}✓，\texttt{C-265}✓）$$
$$\texttt{E4-ENGINE-5}\ \S2\ \text{逐字}✓：\text{二阶矩族对}\ M\gtrsim12\ \textbf{可证不足}✗ \Longrightarrow \textbf{阶梯有天然终点}✓✓$$

## §2 逻辑（为什么做这个 ✓✓）

$$\boxed{\text{把论文A 的【数值表}】\ \text{升级为【定理表}】\ \text{for}\ M\le11✓✓}$$
$$\qquad \text{即}：\text{M}=5..11\ \text{各给一条【区间算术严格}】\ \text{证书}✓ \Longrightarrow \text{论文A 的}\ M\le11\ \text{行由「numerics」变成「theorem」}✓✓$$
$$\qquad \textbf{同时}✓：\texttt{E4}\ \text{引擎在}\ M\le11\ \text{上【免 Montgomery Lemma 2.2}】✓✓（\text{E4 自足化的原始目标}✓）$$

## §3 自有优势（凭什么我们做 ✓✓）

$$\textbf{① 四门区间 B\&B 流水线}✓✓（\text{本会话已成熟}：\texttt{C-216}–\texttt{C-219}、\texttt{C-224}、\texttt{C-265}✓）$$
$$\textbf{② 参数化脚本}✓✓：\texttt{m3\_certificate\_interval\_arith.py}\ \text{（}\texttt{M=int(sys.argv[3])}\ ✓，\text{lb\_box(a,b,M,K)}✓）\ \Longrightarrow \text{新 M 零开发}✓$$
$$\textbf{③ 无 RH、纯初等／严格区间}✓✓（\text{我方一贯风格}✓）；\ \textbf{④ 已有上界脚本}✓：\texttt{mM\_upper\_bounds\_certificate.py}\ \text{（M}\le11\ \text{的上界}✓）$$
$$\textbf{⑤ 负语料}✓（\text{知道}\ M\gtrsim12\ \text{不必试}✗）$$

## §4 预注册判据（成本与 kill ✓✓）

$$\textbf{第一步（本档）}✓✓：\textbf{先用【浮点探针】测箱数与可行性}✓ —— \text{M=4 的浮点版仅}45\ \text{秒／}1{,}036{,}096\ \text{箱}✓ \Longrightarrow \text{7 格探针总成本}\ \lesssim\ \text{十几分钟}✓$$
$$\qquad \textbf{kill 规则}✓：\text{浮点箱数}>2\times10^7\ \text{或单格}>5\ \text{分钟} \Longrightarrow \textbf{该 M 标为「不可行（浮点层）」}✓，\text{不投区间证书}✗$$
$$\textbf{第二步}✓：\text{仅对【浮点判为可行】的 }M\ \text{跑严格区间证书}✓\text{（同四门，target}=1/2✓\text{）}$$
$$\qquad \textbf{成功判据}✓：\text{未决}=0\ \text{且最小余量}>0✓ \Longrightarrow \text{该 M 入档为定理}✓$$
$$\textbf{绝不}✗：\text{无预注册就烧小时级 CPU}✗✓（\text{本档纠正}✓）$$

## §5 启下（做完之后接什么 ✓✓）

$$\text{① 论文A}✓：\text{M}\le11\ \text{由数值变定理}✓ \Longrightarrow \text{论文A 的「rigour」注记可升级}✓$$
$$\text{② E4}✓：\text{引擎在}\ M\le11\ \text{自足}✓ \Longrightarrow \text{E4 免引 Lemma 2.2 的范围扩大}✓$$
$$\text{③ 若全部通过且成本可控}✓：\text{才考虑}\ \texttt{qM}\ \text{窗口放大（}\S3b\ \text{的【证明】问题}✓，\text{那是真正的新数学}✓）$$
$$\qquad ⚠️\ \text{(RP}_M\text{)}\ M>11\ \textbf{不试}✗（\texttt{ENGINE-5}\ \S2\ \text{已判必死}✓✓）$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 浮点探针预注册   命中文件数=0 ::
技术词 阶梯成本kill规则  命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{两项各 0 命中}⟹\textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓：\text{四门}✓（\texttt{C216}✓）；\text{参数化脚本}✓（\texttt{C-177}✓）；\text{M}\gtrsim12\ \text{必死}✓（\texttt{ENGINE-5}✓）$$

## §7 边界

$$\textbf{① 本档为工作计划}✓，\text{不产结果}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ 浮动探针【不是证书}】✗✓（\text{只作成本预判}✓）；\text{结论以区间证书为准}✓$$
$$\textbf{④ M=5 的严格证书【已在跑}】✓（\text{本会话启动}✓）—— \text{它同时充当「第一步可行性」的实测}✓$$

---

## §8 【唐先生锁定·2026-09-20 22:30】执行协议（甲 ＋ L1 分层）

$$\boxed{\textbf{批准：甲}✓（\text{等慢版 M=5 自然结束}✓）＋\textbf{L1}✓（\text{v3 全扫}\to\text{成功格金标准复核}✓）}$$
$$\boxed{\textbf{单任务纪律}✓：\text{此刻唯一运行＝慢版 M=5}✓；\textbf{不并发}✗；\textbf{不提前启动}M=6✗；\textbf{不恢复 400MB 残留}✗}$$

### 8.1 执行序（锁定 ✓）

$$\text{慢版 M=5 完成}\to\text{v3：}M=5\to6\to7\to8\to9\to10\to11\to\textbf{候选定理表}\to\text{慢版逐格复核}M=6..11✓$$

### 8.2 STOP 条件（预注册 ✓✓）

$$\text{v3 PASS} \Longrightarrow \text{该格进慢版认证}✓；\qquad \text{v3 FAIL} \Longrightarrow \boxed{\text{该格直接结束，不开慢版}}✗✓$$
$$\text{v3 任一自检失败} \Longrightarrow \boxed{\text{先审 v3，不进慢版}}✗✓ \Longrightarrow \textbf{慢版预算只花在真有希望成定理的格}✓$$

### 8.3 语义分层（本轮最重要的不是速度，而是这条 ✓✓）

$$\boxed{\text{v3 ＝ 发现／筛选}✓\qquad \text{慢版 ＝ 最终认证}✓✓}$$
$$\text{故：仅 v3 通过的格只能叫}\ \textbf{"v3 证书结果"}✗；\text{只有慢版复核通过才能写}\ \textbf{"无浮点假设定理"}✓✓$$
$$\text{理由}✓：\text{目标是把它从【数值表】升级为【定理表}】✓；\text{若留 }M=6..11\text{ 未复核} \Longrightarrow \text{最后一步没做完}✗$$

### 8.4 已识别风险（待观察 ✓）

$$\text{慢版 M=5 只在【结束时}】\text{打印}✗ \Longrightarrow \text{若 4 小时 timeout（14400 s）触发} \Longrightarrow \textbf{无任何输出}✗✓$$
$$\text{参考}✓：\text{M=4 慢版用}92\ \text{分钟}✓ \Longrightarrow \text{M=5 预计}1.5\text{–}4\ \text{小时}✓（\text{边界紧}⚠️）$$
$$\text{若被 timeout 杀死}✓：\text{金标准锚点缺失}✗（\text{但 v3 仍能给候选}✓） \Longrightarrow \text{是否重跑须唐先生批准}✗✓$$

### 8.5 当前禁止项（✗）

$$\text{① 再优化速度}✗（\text{唐先生：重点＝语义分层}✓）\qquad \text{② 任何并发}✗\qquad \text{③ 未经批准的 kill／启动}✗$$

