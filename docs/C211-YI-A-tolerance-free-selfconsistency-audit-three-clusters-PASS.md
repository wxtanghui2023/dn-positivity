已查地图（**先查后写**）：查 `C-210`（勘误 E1 ＋ 协议修正）、`C-206`（模块）、`C-207`（乙-4）、`C-209`（CENSUS-2）。回查见 §7 ✓

D0: 本档对象 = **甲：免容差自洽性审计**（三簇重跑）＋ 定量账本清洗（max 不等式错误 ＋ active spread 缺项的剥离）—— 关系 = 勘误落实 ＋ 定量账本封口准备
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 判据（免容差，唐先生指定）

$$\boxed{\ \exists\,y:\quad F(y)<F(x)\ \ \wedge\ \ 0<d_{S_3}(x,y)<\rho_{\rm upper}(x)\ \Longrightarrow\ x\ \textbf{不是局部极小}\ }✓✓$$
$$\qquad \textbf{逻辑强度}：\text{这是}\ \textbf{一票否决}✓（\text{找到即否}✓）；\text{找不到}\ \textbf{只说明自洽性检查通过}✓，\textbf{不能替代} \text{局部极小证明}✗✓$$
$$\qquad \textbf{优点}：\text{完全不依赖人为 active tolerance}✓✓（\text{与}\ \texttt{C-210}\ §4③\ \text{的建议一致}✓）$$

## §1 ⭐ 更正后的定量陈述（正式化）

$$F(x+\delta)\ \ge\ F(x)-\delta_A+c\|\delta\|-\tfrac R2\|\delta\|^2✓,\qquad \delta_A=F(x)-\min_{k\in A}S_k(x)✓$$
$$\text{严格正下界要求}\ c\,r-\tfrac R2r^2>\delta_A✓ \Longrightarrow \rho_{\rm lower}=\frac{\delta_A}c✓（\text{更严格时取二次根}\ \frac{c-\sqrt{c^2-2R\delta_A}}R✓）$$
$$\boxed{\ \rho_{\rm lower}<\|\delta\|\le\rho_{\rm upper}\ \Longrightarrow\ F(x+\delta)>F(x)\ }✓✓$$
$$\qquad \text{在}\ 0<\|\delta\|\le\rho_{\rm lower}\ \text{内【不声称】严格上升}✗，\text{只记录}\ F(x+\delta)\ge F(x)-\delta_A+\cdots✓ \text{与数值审计结果}✓$$

## §2 ⭐ 第一轮（未重收敛，出现一票否决）

| 簇 | $F(x)$ | $\rho_{\rm upper}$ | 球内采样 min $F$ | $\Delta F$ | 已知候选球内更低者 | 局部下降最低 |
|---|---|---|---|---|---|---|
| 0 | $0.7640811032$ | $1.466\times10^{-3}$ | $0.7641096322$ | $+2.853\times10^{-5}$ | **1 个** ✗ | $-2.417\times10^{-9}$ |
| 3 | $0.7755338917$ | $2.050\times10^{-4}$ | $0.7755463432$ | $+1.245\times10^{-5}$ | 0 个 | $-1.568\times10^{-13}$ |
| 5 | $0.7768817151$ | $1.858\times10^{-3}$ | $0.7769522554$ | $+7.054\times10^{-5}$ | 0 个 | $-1.306\times10^{-13}$ |

$$\textbf{簇 0 触发否决}✗：y\ \text{满足}\ F(y)=0.764081100754✓,\ \Delta F=-2.408\times10^{-9}✓,\ d_{S_3}=4.454\times10^{-9}✓$$
$$\qquad \textbf{诊断}：\text{位移与跌幅皆}\sim10^{-9}✓ \Longrightarrow \text{疑似【代表点未收敛】}✗（\text{簇 0 的代表来自早期 NM，未精修到机器精度}✓）$$

## §3 ⭐⭐ 第二轮（重收敛后重审计）：三簇全部通过

$$\text{协议}：\text{对每簇做 250 次多尺度抖动重精修（}\mathrm{scale}\ 10^{-7}\to10^{-4}✓，\text{maxiter}\ 6000✓）\ \to\ \text{在}\ x^*\ \text{球内采样 50 万点}\ \to\ 30\ \text{个最低点再局部下降}✓$$

| 簇 | 初始 $F$ | 重收敛后 $F^*$ | 改进 | 位移 | 球内采样 min $\Delta F$ | 30 点下降 $\Delta F$ | d（最近点） | 判定 |
|---|---|---|---|---|---|---|---|---|
| **0** | $0.764081103162726$ | $\mathbf{0.764081100745855}$ | $-2.417\times10^{-9}$ | $4.470\times10^{-9}$ | $+3.916\times10^{-5}$ | $+7.772\times10^{-15}$ | $5.629\times10^{-5}$ | ⭕ **通过** ✓ |
| **3** | $0.775533891695632$ | $0.775533891695632$ | $0$ | $0$ | $+1.481\times10^{-5}$ | $+4.992\times10^{-11}$ | $8.221\times10^{-6}$ | ⭕ **通过** ✓ |
| **5** | $0.776881715053449$ | $0.776881715053315$ | $-1.339\times10^{-13}$ | $1.598\times10^{-13}$ | $+7.435\times10^{-5}$ | $+1.787\times10^{-14}$ | $8.314\times10^{-5}$ | ⭕ **通过** ✓ |

$$\Longrightarrow \boxed{\ \textbf{三簇均未发现反例}✓✓\ —— \text{免容差自洽性检查全部通过}✓\ }$$
$$\qquad \textbf{簇 0 的首轮否决确认为【收敛伪影】}✓✓：\text{重收敛后位移}\ 4.47\times10^{-9}✓，\text{球内再无更低点}✓（\text{采样}\ \Delta F=+3.9\times10^{-5}✓，\text{下降仅}\ +7.8\times10^{-15}✓）$$
$$\qquad \textbf{附带收获}：x_0^*\ \text{的}\ F^*=0.764081100745855✓\ \textbf{低于已认证上界}\ 0.76408110090337578✓\ \text{达}\ 1.58\times10^{-10}✓ \Longrightarrow \text{乙可再收紧}✓$$

## §4 定量账本清洗（max 不等式错误 ＋ δ_A 缺项的剥离）

$$\text{原}\ \texttt{C-203}\ \text{／}\ \texttt{C-205}\ \text{／}\ \texttt{C-206}\ \text{声明}：(0,\rho_{\rm upper}]\ \text{上严格线性上升}✗✗ $$
$$\text{更正后}：\boxed{(\rho_{\rm lower},\rho_{\rm upper}]\ \text{上严格线性上升}}✓✓\qquad（\text{本期勘误的实施方式}✓）$$

| 簇 | $\delta_A$ | $\rho_{\rm lower}$（二次根） | $\rho_{\rm lower}$（$\delta_A/c$） | $\rho_{\rm upper}$ |
|---|---|---|---|---|
| 0 | $9.269\times10^{-8}$ | $1.7157\times10^{-7}$ | $1.7157\times10^{-7}$ | $1.465756\times10^{-3}$ |
| 3 | $1.603\times10^{-12}$ | $1.3157\times10^{-12}$ | $1.3157\times10^{-12}$ | $2.050227\times10^{-4}$ |
| 5 | $3.440\times10^{-12}$ | $4.5841\times10^{-12}$ | $4.5841\times10^{-12}$ | $1.858471\times10^{-3}$ |

$$\qquad （\text{两式在本例数值上一致到 5 位}✓，\text{因}\ 2R\delta_A\ll c^2✓）$$

## §5 诚实边界（唐先生要求的分寸）

$$\textbf{① 通过 ≠ 证明}：\text{自洽性检查只有【否决】功能}✓；\text{未发现反例}\ \textbf{不等于} \text{已证局部极小}✗$$
$$\qquad \text{本次球内 50 万点采样 ＋ 30 次局部下降均为}\ \textbf{数值}✓，\textbf{不穷尽}✗$$
$$\textbf{② 首轮否决的教训}：\text{否决检验必须施加于【已收敛】的代表点}✓ \Longrightarrow \text{否则会因代表点自身未收敛而平凡触发}✗✓（\text{协议条目}✓）$$
$$\textbf{③ 本地结论仍受}\ \texttt{C-209}\ \text{的协议限定}✓：\text{不声称穷尽极小构型}✗$$
$$\qquad \text{账本不变}：0.76\le m_3\le0.764081100903\ldots✓$$

## §6 与乙的衔接（待唐先生指示）

$$\textbf{乙}：\text{对}\ x_0^*\ \text{（或更优代表）重做【区间算术上界认证】}✓ \Longrightarrow \text{账本上界可望从}\ 0.764081100903\ \text{降到}\ \approx0.76408110075✓$$
$$\qquad \text{做法照}\ \texttt{C-202}\ \text{模板}✓（\text{有理化}\ \to\ \text{区间上端点}✓）；\text{目标不再是搜索，而是攻击}\ \mathbf{0.7640811}\ \text{这个数本身}✓✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 免容差审计   命中文件数=1    ::  ./C211-YI-A-tolerance-free-selfconsistency-audit-three-clusters-PASS.md
技术词 收敛伪影     命中文件数=1    ::  ./C211-YI-A-tolerance-free-selfconsistency-audit-three-clusters-PASS.md
技术词 定量账本清洗 命中文件数=1    ::  ./C211-YI-A-tolerance-free-selfconsistency-audit-three-clusters-PASS.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 本档自我失误

$$\textbf{① 首轮用未收敛代表点}✗ \Longrightarrow \text{平凡触发否决}✗✓ \Longrightarrow \text{须先重收敛}✓（\text{第 30 次同类应验}✓）$$
$$\qquad \text{其余：脚本首次因未加背景启动而阻塞}✗⟹\text{改 nohup}✓$$
