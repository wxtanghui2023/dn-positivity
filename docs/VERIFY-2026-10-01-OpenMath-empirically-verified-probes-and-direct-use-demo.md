# VERIFY-2026-10-01 — **OpenMath 实操复现 ＋ 12 项破坏性探针 ＋ "直接用其代码"演示**（含对我三处纸面说法的修正）

已查地图：结论: 已查地图：命中 63 处 —— 先逐条判 已DEAD/已封/已登记；命中即引既有条目，不得开新案
D0: 本档对象 = 外部项目之实操验证（非数学命题；不主张任何新值）
D1: 0

## §0 我先前纸面说法 vs 实测（**三处修正** ✗→✓）

| 我先前的说法 | 实测 | 判定 |
|---|---|---|
| "atom 链给公理 P⇒Q 与 P 即得 proven" | **错** ✗：蕴含本身也须列为公理（**推理许可不可省**） | 工具**比我预想更严** ✓ |
| （隐含）变量有类型 | **错** ✗：`['var','pi']` 被当**整数变量**静默接受，归一为多项式 | 无类型检查 ⚠️ 危险点 |
| 担心性能指数爆炸 | 400 节点链 **9 ms** ✓ | 风险仅在**分支路线搜索**，非不动点 |

## §1 复现三件套 ✓

$$\text{Node }v24.14.0\ (\ge22\ ✓);\quad \texttt{node --test}\Longrightarrow \textbf{15/15 通过}\ (117\,\mathrm{ms});\quad \texttt{node examples/demo.js}\ \text{正常}\ ✓$$

## §2 12 项破坏性探针（自建 ✓）

| 探针 | 实测 |
|---|---|
| P1 自报 status/proven/confidence | **被忽略** ✓（unknown/null/0） |
| P2 二元环自证 | **不能** ✓ |
| P3 三前提路线 | **拒** ✗ "Only modus-ponens routes with two premise ids" ⟹ **硬限制** |
| P4 pow17／P6 除法 | 拒 ✓ |
| P5 不等式 `le` | 拒 ✓ |
| **P7 `pi` 作变量** | **静默接受** ✗ 归一为多项式（$\text{pi}^1-3$）⟹ 无类型/域检查 |
| P8 我方断言作 atom | 接受 ✓（不透明） |
| **P9 atom 链** | status=unknown ✓✓ **事实不能白拿**（`P` 须自身为公理） |
| P10 400 节点链 | **9 ms** ✓ |
| P11 外部改动已存声明 | 无影响 ✓ |
| P12 同陈述异公理集 | key 不同 ✓ |

## §3 "直接用其代码"实操演示 ✓（我方 K(10,1) 阶梯）

\`\`\`
id    status      conf  support  axiomDeps
sphere axiom       1     1        ["[\"atom\",\"球界: K>=94\"]"]
sdp    axiom       1     1        ["[\"atom\",\"SDP-3_Gijswijt-Polak2025: K>=106 [可复现]\"]"]
bow    axiom       1     1        ["[\"atom\",\"BOW2004: K>=107 [全文不可得]\"]"]
r103   proven      1     1        ["[\"atom\",\"vanWee1988: K>=103\"]","[\"implies\",[\"atom\",\"vanWee1988: K>=10
r106   proven      1     1        ["[\"atom\",\"SDP-3_Gijswijt-Polak2025: K>=106 [可复现]\"]","[\"implies\",[\"atom\"
r107   proven      1     1        ["[\"atom\",\"BOW2004: K>=107 [全文不可得]\"]","[\"implies\",[\"atom\",\"BOW2004: K>=
o103   unknown     null  0        []
o106   unknown     null  0        []
tgt    unknown     null  0        []
\`\`\`

$$\textbf{\text{读数}}:\ r107\ \textbf{\text{为 proven}},\ \text{而其 }axiomDependencies=[\texttt{BOW2004: K>=107 [全文不可得]},\ \texttt{implies(...)}]\ \Longrightarrow\ \textbf{\text{工具把我方"复现 107"之全部支撑暴露为一条\ \textbf{拿不到的原文}}}\ ✓✓$$

## §4 它**三次抓住我自己**（实证其价值 ✓✓）

\$\$\text{① 三前提路线被我当合法} ✗;\quad \text{② 公理串 }\texttt{SDP-3(Gijswijt-Polak2025): K>=106}\ \text{与断言串 }\texttt{SDP-3: K>=106}\ \textbf{\text{不一致}} ✗;\quad \text{③ 前提顺序（事实/蕴含）写错} ✗\$$
\$\$\Longrightarrow\ \text{这几次失败\ \textbf{恰是我方反复出现的"定义/陈述漂移"}}\ ✓\ \text{⟹ "逐字匹配 fail-closed"规则\ \textbf{对该病直接有效}}\ ✓✓\$$

## §5 硬限制清单（实测确认 ✗）

\$\$\text{① 路线\ \textbf{恰两前提}＋仅 modus-ponens ⟹ \textbf{我方非 MP、多前提推理无法表达} ✗;\quad \text{② 无持久化/无索引（lookup 全扫）} ✗;\quad \text{③ add-only 不可变图（改证据须重建）} ✗;\quad \text{④ \textbf{无类型/域检查}} ⚠️;\quad \text{⑤ 无 Lean（v0.3）、无反例检查器（v0.2）} ✗\$$

## §6 判决（"直接用" vs "自建"）

\$\$\boxed{\text{可用其代码作\textbf{记账层}，但必须 fork 扩展（或窄用）}}\ ✓;\quad \textbf{\text{不宜再自建一个"我自己的框架"（我上一轮之错）}} ✗\$$
\$\$\text{其免费给予者}:\ \text{① 强制显式登记假设（含\ \textbf{每步推理许可}）};\ \text{② 拒绝环};\ \text{③ 逐字 fail-closed};\ \text{④ 上下文 key 隔离};\ \text{⑤ 忽略自报状态};\ \text{⑥ 外部不可变}\ ✓\$$
\$\$\text{其不给予者}:\ \text{任何\ \textbf{数学内容验证}}（atom 不透明）⟹ \text{我方数学仍须自证}\ ✗\$$

## §7 边界与纪律

\$\$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{仓已本地重建并实跑（}/tmp/omrepo/\text{：}15/15\ \text{测试＋}12\ \text{探针＋演示）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓\$$

## §8 【技术词回查】

\`\`\`
技术词 推理许可     命中文件数=0    :: 
技术词 记账层        命中文件数=0    ::
\`\`\`
