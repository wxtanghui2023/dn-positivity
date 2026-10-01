# RESULT-2026-10-01 — **fork 扩展（三件）＋ 窄用实测**：27 条承重断言之假设依赖被机器暴露（7 处 ⚠／2 处 △）

已查地图：结论: 已查地图：未覆盖（关键词: fork|隐藏假设|窄用）—— 可开档，首行须照抄本行
D0: 本档对象 = 工具实操（fork 与窄用）；非数学命题，不主张任何新值
D1: 0

## §0 fork 三件（`om-ext`，基于原引擎 ✓ 不重写）

$$\textbf{① 多前提路线}:\ \text{新增 }\texttt{rule:'inference'}\ (\text{前提数}\ge1)\ +\ \textbf{\text{必须给出 license 蕴含}};\ \texttt{modus-ponens}\ \text{仍限两前提};\ \text{license 须\textbf{登记为公理}否则 fail-closed}\ ✓$$
$$\textbf{② 持久化＋索引}:\ \texttt{save(file)/load(file)}\ (\text{JSON: context+nodes})\ ⟹\ \text{往返后 analyze 结果一致}\ ✓$$

$$\textbf{③ claim 级 assumptions}:\ \texttt{add(\{...,assumes:[…]\})};\ \textbf{\text{未登记为公理者一律 fail-closed}}\ ⟹\ \text{analyze 返回新字段 }\texttt{assumptionDeps}\ ✓✓$$

**实测（`/tmp/om-ext`）**：三前提 inference → 可证 ✓；已登记 assumption → 进入 `assumptionDeps` ✓；save/load → 一致 ✓；未登记 assumption → **被拒** ✓

## §1 窄用：27 条承重断言（喂进扩展引擎）

\`\`\`
id        状态        支撑假设
F1        axiom      定义: 三层恒等式 T ; 枚举穷尽性: 62码与120码
F3        axiom      定义: μ(x)=|C∩N[x]| ; 枚举穷尽性: 62码与120码
F7        axiom      定义: μ(x)=|C∩N[x]|
LEM4      axiom      枚举穷尽性: 2^28 层 (F) ; 端点方程 t=6-a-b+c
H21       axiom      枚举穷尽性: 2^28 层 (F)
EMAX      axiom      FEAS(m,E) 判定式模型(84变量)
GAMMA     axiom      枚举穷尽性: 2^28 层 (F)
SPEC      axiom      枚举穷尽性: 2^28 层 (F)
T60       axiom      定义: μ(x)=|C∩N[x]|
GR        axiom      定义: μ(x)=|C∩N[x]|
SHQ       axiom      每 R-R 对至多两个 q
SCALE     axiom      随机分拆集中性(仅 i=45 验证) △单点验证
ARROW     axiom      L_q 代理定义 ⚠不可得/未证
K106      axiom      SDP-3 公开值 (Gijswijt-Polak2025)
K107      axiom      BÖW2004 全文不可得 ⚠不可得/未证
S103      axiom      vanWee1988 公式
S105      axiom      Zhang1991 pair (文献)
AUDIT106  axiom      SDP-3 公开值 (Gijswijt-Polak2025) ; vanWee1988 公式
PMER      axiom      Jensen 松弛合法 △单点验证 ; 枚举穷尽性: 2^28 层 (F)
SLACK6    axiom      W 下界缺失 ⚠不可得/未证
LAMBD     axiom      RH (历史循环论证处) ⚠不可得/未证
DEMAND    axiom      R/U 分拆准则未知 ⚠不可得/未证 ; W 下界缺失 ⚠不可得/未证
H18       axiom      枚举穷尽性: 2^28 层 (F)
H20       axiom      枚举穷尽性: 2^28 层 (F)
H24       axiom      枚举穷尽性: 2^28 层 (F)
ROUTE119  axiom      W 下界缺失 ⚠不可得/未证
DTRUE     axiom      D_true 枚举(r<=7 精确)

合计 27 条；⚠不可得/未证 7 处；△单点验证 2 处
✔ 未登记 assumption 被拒: Unregistered assumption for Z: must be declared as a
\`\`\`

## §2 ★ 它替我暴露的东西（这是本次最有用之产出 ✓✓）

| 断言 | 暴露之隐藏假设 | 性质 |
|---|---|---|
| **LAMBD（λ 差分 > 0）** | **RH** | ⚠ **正是历史循环论证事故** |
| **K107（复现 107）** | BÖW2004 全文不可得 | ⚠ 全部支撑＝拿不到的原文 |
| **ARROW（箭头实测）** | L_q 代理定义 | ⚠ 代理对象 |
| **DEMAND（需求侧）** | R/U 分拆准则未知 ＋ W 下界缺失 | ⚠⚠ 两块缺失 |
| **SCALE（2A₂(R) 标度律）** | 随机分拆集中性（仅 i=45 验证） | △ 单点 |
| **PMER（机制级不可行）** | Jensen 松弛合法 | △ 单点 |

$$\textbf{\text{统计}}:\ 27\ \text{条断言中}\ \textbf{7 处}\ \text{依赖 ⚠（不可得/未证/代理）},\ \textbf{2 处}\ \text{依赖 △（单点验证）}\ ✓$$

## §3 关键认识（引擎逼出的 ✓）

$$\text{对任何外部检查器而言，\textbf{我方"内部结论"也只是"我们接受的假设"}}\ ⟹\ \text{本演示中它们皆登记为 axiom（}\text{status=axiom}\text{）};\ \text{"proven"须由\ \textbf{路线＋已登记 license＋已登记前提} 三件齐备才成立}\ ✓✓$$

## §4 过程中被它抓住的三次（连续 ✓）

\$\$\text{① 把另一条\textbf{断言}当作"假设"低报 } ✗\ (\text{H21 假设列含"四步引理"})\ \Longrightarrow\ \text{逼出"假设 vs 推导"必须分清};\quad \text{② 未登记 assumption}\ ✗;\quad \text{③ 字符串漂移}\ ✗\ (\text{前档})\ ✓\$$

## §5 边界与纪律

\$\$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{fork 与窄用皆实跑（}/tmp/om-ext/\text{；输出并存 }/tmp/narrow.out\text{）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓\$$

## §6 【技术词回查】

\`\`\`
技术词 隐藏假设     命中文件数=7    :: ./C298-q-prime-closure-and-commuting-defect-chain-audit.md ./iteration-double-counting-round4.md ./three-lines-deep-analysis.md 
技术词 fork扩展       命中文件数=0    ::
\`\`\`
