# ANALYSIS-2026-10-01 — **OpenMath(zhuhaichao518)** 与 **QED** 两项目分析 ＋ B/C 是否适用"理解"＋ 建议

结论: 已查地图：未覆盖（关键词: 证明图|OpenMath|QED）—— 可开档，首行须照抄本行
D0: 本档对象 = 外部项目分析与工具链建议（非数学命题；不主张任何新值）
D1: 0

## §1 OpenMath（zhuhaichao518/OpenMath）——**核实为真** ✓

$$\textbf{元数据}:\ \text{MIT};\ \text{建仓 }2026\text{-}09\text{-}29\ (2\ \text{天前});\ 20\,\mathrm{KB};\ \text{JS};\ \star0;\ 21\ \text{文件};\ \text{需 Node.js 22};\ \text{无第三方依赖}\ ✓$$

**核心理念（逐字）**：*"数学研究不应该只保存最后证明成功的答案。失败的尝试、条件性结论、反例搜索和未完成的分支，也应该成为下一次推理可复用的知识。"*
**组织方式**：**证明图** —— 节点＝命题，**超边**＝多前提到一结论之推导；同一结论可有**多条路线** ✓

**可信度分级（与我方纪律高度同构 ✓✓）**

| 状态 | 含义 | 100%? |
|---|---|---|
| axiom | 理论内明确接受之起点 | 是（相对该理论） |
| proven | 检查器已验证且前提成立 | 是（相对公理与检查器） |
| conjectured | 有计算/实验支持，仍有缺口 | **否** |
| unknown | 无有效支持 | 否 |

$$\text{并明文}:\ \text{"长期没找到反例"只记 }\texttt{supportScore}\ \text{（搜索启发式），**不冒充概率**、**不因试验次数自动升级为证明**};\ \text{未证明者 }\texttt{confidence=null}\ ✓✓\ \text{（＝我方"probe 偏差≠证据／不作不存在证据"} ✓)$$

**已实现**：BigInt 精确多项式归一化；**上下文相关检索**（指纹含语言版本＋定义域＋归一化版本＋**公理集合** ⟹ **防止跨理论错误复用** ✓✓ ＝ 我方 AMEND-27 空间 A/B 隔离之机器化）；多路线证明图＋启发式评分＋待证前提；最小检查器（多项式恒等＋modus ponens）；**防循环自证**（从公理与已检查恒等式迭代，互相引用之未证明节点不得 proven ✓✓ ＝ 我方循环论证审计）；示例＋自动测试 ✓
**未实现** ✗：自然语言自动形式化、Lean 集成、科学知识库、量词推理、**反例检查器**、校准过的可信度模型；**检查器自身未形式化验证** ✓
**六步长期工作流**：① 转成带语义/定义域/假设之形式命题并核忠实性 → ② 归一化＋索引检索（复use 已证/条件性/历史尝试）→ ③ 展开多路线、记录依赖与**缺失引理** → ④ 综合证据质量/缺口/成本选下一步 → ⑤ 调符号计算、反例搜索、形式化工具 → ⑥ 检查器核验并更新依赖链 ✓

## §2 QED（github.com/proofQED/QED；arXiv 2604.24021）——架构已核 ✓

$$\textbf{流水线}:\ \textbf{plan–prove–verify–regulate}\ (\text{六智能体}):\ \text{Decomposer}\to\text{Single Prover}\to\text{Structural Verifier}\to\text{Detailed Verifier}\to\text{Regulator}\to\text{Verdict}\ ✓$$
- **Decomposer** 产出 **YAML 证明计划＝中间断言之 DAG**，每步给：**依赖**＋**难度**＋**是否关键步**＋**引用来源**＋**强制自评**；并**可读先前计划与 Regulator 的失败原因** ⟹ 避免重复 ✗掉坑 ✓✓
- **Regulator 三种纠正动作**：`Revise_Proof`（不动计划，改证明）／`Revise_Plan`（改计划）／`Rewrite`（全新分解） ⟹ **正是"拆解失败后该怎么办"之制度化** ✓✓
- 运行方式：经 Codex／Claude／Gemini 之 CLI（bash 子进程），依赖极少 ✓
- 战绩：18 个研究级项目 → **5 项原创工作**（代数几何／流体 PDE／概率／反问题），**3 项达期刊难度**、专家认可 ✓
- 明示失败模式 **FM4＝不稳定证明计划**，decomposition mode 即为其对策 ✓

## §3 B／C 是否适用"**理解**"（唐先生问）✓

$$\textbf{(B) 是} ✓✓:\ \text{OMDoc 自述}:\ \text{"\textbf{柔性形式化}——覆盖从"非形式但严格"到"完全形式"之全谱"，**无需承诺任一形式化或基础**};\ \text{其 theory inclusion／view 正为"同一对象之多视角"而设}\ ✓$$
$$\textbf{+ 更贴切者 ＝ KnowTeX}（arXiv 2601.15294）:\ \text{"\textbf{Infer mode}: 从**普通 LaTeX**抽取依赖图，**无标注、无证明助手、无形式化**"} ✓✓\ \text{（＝纯"理解/结构"工具；与 Lean Blueprint 兼容）$$
$$\textbf{(C) 部分} ⚠️:\ \text{Stacks Project 是\ \textbf{语料＋工具}（21,446 tags；每个陈述有 tag；官方自动依赖子图 API）} ⟹ \text{其\ \textbf{方法论}（tag 化＋按 tag 互引＋自动子图）**可复制**，但其\ \textbf{语料} 是代数几何专用 ✗ ⟹ 只作\ \textbf{模板}}\ ✓$$

## §4 建议（借 schema／借流程，不依赖其代码 ✓）

$$\textbf{(P1) 借 OpenMath 之\ \textbf{数据模型}}:\ \text{给档案建"证明图"层 —— 节点＝已有断言\ (V\text{-}/C\text{-}/F1\text{–}F9),\ \textbf{超边＝推导},\ 状态＝\text{proven/conjectured/unknown/DEAD},\ 路线元数据＝工具/代价/失败原因};\ \text{**增量** ＝ 机器可读依赖边＋路线评分＋防循环自证＋上下文指纹}\ ✓\ \text{（可用薄脚本自建，小时级）}$$
$$\textbf{(P2) 借 QED 之\ \textbf{流程}}:\ \text{每次开攻目标先出\ \textbf{YAML 计划 DAG}（依赖/难度/关键步/引用/自评）};\ \text{失败必须走}\ \textbf{Regulator 三分支};\ \text{并强制查 }NO\text{-}GO\ \text{地图 ⟹ 制度化"不再掉坑"}\ ✓✓$$
$$\textbf{(P3) 理解层}:\ \text{KnowTeX／OMDoc／sTeX（无需形式化）};\ \textbf{(P4)}:\ \text{Argdown 画路线/NO-GO 论证图（低成本）};\ \textbf{(P5)}\ \text{D 不需要（Lean/Mathlib 已装 ✓）；E 只取其\ \textbf{流程}，不装其代码}\ ✓$$

## §5 诚实提醒 ⚠️

$$\text{① OpenMath\ \textbf{仅 2 天龄、}\star0\text{、原型} ⟹ **勿依赖其代码**，只借 schema} ✗✓;\quad \text{② QED 需 Codex/Claude/Gemini CLI（我方或缺）} ⟹ \text{借架构不借实现} ✓;\quad \text{③ 两者都\ \textbf{不会替我们做数学}} ✓$$

## §6 更正（唐先生指出 ✓）

$\text{Lean 与 Mathlib **已安装**（应记）；前档"Mathlib 未装 ✗"作废}\ ✓$

## §7 边界与纪律

$$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{OpenMath 元数据/README/文件树经 GitHub API 直取；QED 细节经 arXiv v4 与仓页} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## §8 【技术词回查】

```
技术词 证明图        命中文件数=1    :: ./CHAIN-REAUDIT-2026-09-27-per-link-difficulty-decomposition.md 
技术词 调节器        命中文件数=0    :: 
```
