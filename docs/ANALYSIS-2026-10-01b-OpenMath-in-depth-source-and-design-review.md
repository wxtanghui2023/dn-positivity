# ANALYSIS-2026-10-01b — **OpenMath**(zhuhaichao518) 深度分析：源码＋设计＋测试＋路线图（逐层）

已查地图：结论: 已查地图：未覆盖（关键词: OpenMath|证明图|信任边界）—— 可开档，首行须照抄本行
D0: 本档对象 = 外部项目深度评审（非数学命题；不主张任何新值）
D1: 0

## §0 项目实况（硬数据 ✓）

$$\text{MIT};\ \text{建仓 }2026\text{-}09\text{-}29;\ \textbf{2 天龄};\ \text{约 }20\,\mathrm{KB};\ \text{纯 JS ESM};\ \texttt{node>=22};\ \textbf{零运行依赖};\ \star0;\ \text{11 文件}\ ✓$$

$$\texttt{docs/\{DESIGN,LANGUAGE,ROADMAP\}.md};\ \texttt{src/\{canonical,graph,index\}.js};\ \texttt{examples/demo.js};\ \texttt{test/core.test.js};\ \texttt{package.json(v0.1.0, private)} ✓$$

## §1 三层架构（逐层）

$$\textbf{(1) 规范化/指纹层 }\texttt{canonical.js}:\ \text{语言 }\texttt{OM-IR 0.1}\ \text{＝整数多项式片段}:\ \text{expr}\in\{\text{int},\texttt{["int","<十进制串>"]},\texttt{var},\texttt{add},\texttt{sub},\texttt{mul},\texttt{pow}(n\le16)\};\ \text{statement}\in\{\texttt{eq},\texttt{atom},\texttt{implies}\}\ ✓$$

- `polynomial()`：递归解析为 `Map<单项式键, BigInt>`，**全程精确无浮点**；预算 MAX_TERMS=2048／MAX_WORK=1e5／深度≤64；**除法整体拒绝** ✓
- `normalizeStatement()`：对 `eq` 取 $p-q$ 归零 → `["eq-zero", terms]`，并**符号归一**（$p=0$ 与 $-p=0$ 同键）✓
- $$\textbf{上下文指纹}:\ \texttt{claimKey}=\mathrm{SHA256}\big(\{\text{language},\text{domain}{=}Z,\text{normalizer},\textbf{axioms(排序去重)},\text{statement}\}\big)\ \Longrightarrow\ \textbf{\text{跨理论/跨公理集不复用}}\ ✓✓$$

$$\textbf{(2) 证明图层 }\texttt{graph.js}:\ \texttt{ProofGraph({axioms})};\ \texttt{add(\{id,statement,evidence?,routes?\})}\ \text{校验}: \text{id 唯一非空};\ \text{evidence 须 }\{passed,tested,source\}\ (0\le p\le t,\ t\ge1,\ \text{source 非空});\ \text{route 仅 }\texttt{modus-ponens}\ \text{且恰两前提};\ \textbf{\text{调用方自报的 status/proven/confidence 一律忽略}}\ ✓✓$$

- `analyze(id)` 四步：① 全边校验（前提陈述须逐字匹配，否则 fail-closed）；② 播种：公理节点＋多项式恒等节点；③ **最小不动点迭代**：前提全已证的路线方可证成 ⟹ **循环无法自证** ✓✓；④ `explore` 递归评分（见 §4）✓
- 返回：`{id,key,status,confidence,supportScore,scoreMeaning='search heuristic, not probability of truth',obligations,selectedRoute,axiomDependencies,checker,domain}` ✓
- 状态映射：公理→`axiom`；已证→`proven`；$\text{score}>0$→`conjectured`；否则 `unknown`；**confidence 仅在 proven/axiom 时为 1，否则 null** ✓✓

$$\textbf{(3) 导出层 }\texttt{index.js}:\ \text{仅 re-export};\ \text{无服务、无 MCP、无模型接口、无外部证明后端}\ ✗$$

## §2 信任边界与纪律（设计文档最锋利处 ✓✓）

$$\textbf{① 四量分离}:\ \texttt{status}（逻辑状态）／\texttt{confidence}（理论内是否闭合）／\texttt{supportScore}（\textbf{搜索排序启发式，非真值概率}）／\texttt{obligations}（未证前提）／\texttt{axiomDependencies}／\texttt{checker}\ ✓$$

$$\textbf{② 公理政策}:\ \text{"axiom policy must live \textbf{outside} the model-controlled input"};\ \text{逐字}:\ \textbf{\text{"Automatically allowing an LLM to approve its own new axioms would destroy the intended trust boundary"}}\ ✓✓$$

$$\textbf{③ 诚实限定}:\ \text{"未找到反例"只记 supportScore，\textbf{不冒充概率}、\textbf{不因试验次数自动升级为证明};\ \text{未证者 confidence=null};\ \text{"不同键不证明不等价"};\ \text{检查器自身\ \textbf{未形式化验证}} ✓✓$$

## §3 测试固化的 soundness 边界（17 组 ✓）

归一化等价（展开↔因式）｜**超 $2^{53}$ 精确性**｜等式对称但不同断言不同键｜**键隔离公理上下文并忽略顺序/重复**｜不支持语法 fail-closed｜拒绝非恒等｜**仅"显式公理＋已检推理"可达 100%**｜**报 998 次测试仍为 conjectured、confidence=null、supportScore=0.99、obligations=['a']**｜**循环推理不能造出证明**｜独立路线可闭合循环｜坏边/缺前提 fail-closed｜外部改对象不影响已存声明/策略｜重复 id、自造规则("trust-me")、畸形证据皆拒 ✓✓

## §4 打分政策（含自我限定）

$$\texttt{evidenceSupport}=\min(0.99,(p+1)/(n+2));\quad \texttt{routeSupport}=\min(\text{premiseSupports});\quad \texttt{claimSupport}=\max(\text{ownEvidence},\text{routeSupports})\ ✓$$

$$\text{自述限定}:\ \text{平滑通过率启发式，\textbf{不宣称校准};\ 重复/相关试验会误导;\ 路线聚合是\textbf{排序约定}而非概率演算;\ 平局保留更早者;\ \textbf{不最小化剩余步数}}\ ✓$$

## §5 路线图（v0.2 / v0.3）

$$\textbf{v0.2}:\ \text{版本化 schema＋序列化＋存储＋索引检索}\mid\ \textbf{\text{不可变证据记录（含出处/搜索域/可复现元数据）}}\mid\ \textbf{\text{导出并重放完整证明证书}}\mid\ \textbf{\text{反例见证校验＋"被反驳"状态}}\mid\ \text{增量更新/预算/路线代价}\ ✓$$

$$\textbf{v0.3}:\ \text{隔离 Lean 后端校验精确目标陈述}\mid\ \text{审计公理＋记录 prover/工具链/库版本}\mid\ \text{带类型 binder 与显式假设（保留条件性结论）}\mid\ \textbf{\text{LLM 工具契约}}:\ \texttt{formalize},\texttt{canonicalize},\texttt{lookup},\texttt{propose\_route},\texttt{search\_counterexample},\texttt{verify\_proof},\texttt{next\_obligations}\ (\text{拟 MCP})\ ✓$$

## §6 为什么**不能直接用**（局限 ✗）

$$\text{① 论域＝\textbf{整数多项式＋modus ponens}}\ \Longrightarrow\ \text{无量词/无实数分析/无集合/无定义/无 }\alpha\text{-等价}\ \Longrightarrow\ \text{我方（覆盖码、解析数论）\textbf{\text{整体落在片段之外}}}\ ✗✗$$

$$\text{② 无反例检查器（v0.2 才规划）、无 Lean（v0.3）}\ \Longrightarrow\ \text{当前 "proven" \textbf{对我方几乎无意义}}\ ✗;\quad \text{③ add-only 不可变图（改证据须重建）};\quad \text{④ 大分支图疑指数、无持久化/索引};\quad \text{⑤ 2 天龄、单作者、v0.1.0}\ ✓$$

## §7 我们能借什么（具体到字段与检查 ✓✓）

$$\textbf{(a) 节点/边 schema}:\ \text{每断言 }\{id,\ statement,\ status\in\{\text{axiom,proven,conjectured,unknown},\textbf{DEAD/NO-GO}\},\ obligations,\ selectedRoute,\ \textbf{axiomDependencies},\ checker/provenance,\ fingerprint(context)\}\ ✓$$

$$\textbf{(b) ★最关键}:\ \textbf{\text{每条断言必须显式登记其 assumptions/axiomDependencies}}\ \Longrightarrow\ \text{直击我方最大复发性失效——\textbf{未声明假设}（如循环论证事故：}\lambda\ \text{差分暗用 RH）}\ ✓✓$$

$$\textbf{(c) confidence=null 除非已证 ＋ supportScore 非概率};\quad \textbf{(d) 反循环不动点检查}（找出"仅由环支撑"的断言};\quad \textbf{(e) fail-closed 路线校验（前提须逐字匹配）}\ ✓$$

## §8 判决

$$\boxed{\textbf{\text{理念高度对齐、技术远不足承载我方数学}}}\ ✓\ \Longrightarrow\ \text{借其 schema 与信任边界设计，在既有 ID-CLAIMS/档案之上自建薄层（小时级）}\ ✓$$

## §9 边界与纪律

$$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{源码/文档/测试经 GitHub API 逐字取回并本地存盘（}/tmp/om/\text{）} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## §10 【技术词回查】

```
技术词 信任边界     命中文件数=0    :: 
技术词 上下文指纹  命中文件数=1    :: ./ANALYSIS-2026-10-01-OpenMath-and-QED-two-projects-for-math-problem-decomposition.md
```

$$\textbf{分类}：\textbf{本档新增}：\text{「信任边界」（实测 0 档 ⟹ 本档首次命名）} ✓;\quad \textbf{会话内已有（前档引用，不列为新）}：\text{「上下文指纹」（1 档＝本会话 2026-10-01 前档）} ✓;\quad \textbf{通用词（不计）}：\text{“源码／测试”裸词} ✓$$
