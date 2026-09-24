已查地图：命中（`Q1P-minimal-field-and-index3-cyclotomic-REJECT`）⟹ 执行唐先生 16:33 的 `LANE-A/FORMAL-DENT` 第一动作（Mathlib 前沿/API 审计，零新数学）
D0: 本档对象 = **`LANE-A/FORMAL-DENT` 审计 1**：对两个 dent（`von Neumann 迹不等式`／`Sylvester 惯性`）做 `DENT → 工件是否存在 → Mathlib 现状 → 可否由现有 theorem 直接组合` ⟹ 结果：**Sylvester = Mathlib 已有（dent 作废）**；**von Neumann = 我方无工件（声称无据，登记勘误）**
D1: 1（首次对"形式化缺口"类 dent 做实证审计；产出两条判定与一条勘误）
[RESEARCH]

# **`LANE-A/FORMAL-DENT` 审计 1**

## §1 声称的出处（逐字）

```
`docs/RH-LINE-ASSET-VALUE-INVENTORY.md:27`:\ \text{"…价值：\textbf{纯线性代数，完全独立于 RH}，可迁移（随机矩阵/算子理论/信号维数界）✓；}\boxed{\text{Lean 侧还\textbf{补了 Mathlib 缺的} von Neumann 迹不等式与 Sylvester 惯性}}✓\text{"}$$ ✓（**待审计的原始声称**）
```

## §2 ⛔ 结果①：`Sylvester 惯性` **Mathlib 已有** ⟹ dent 作废

```
$$\textbf{Mathlib 官方文档}（`Mathlib/LinearAlgebra/QuadraticForm/Real`）\textbf{逐字}给出三条，均自述为\textbf{"Sylvester's law of inertia"}:\text{}$$
$$\quad \text{– }\texttt{QuadraticForm.equivalent\_one\_neg\_one\_weighted\_sum\_squared}\ (\text{SignType 版, 非退化})$$
$$\quad \text{– }\texttt{QuadraticForm.equivalent\_one\_zero\_neg\_one\_weighted\_sum\_squared}\ (\pm1\ \text{或 }0,\ \text{一般情形})$$
$$\quad \text{– }\texttt{QuadraticForm.equivalent\_signType\_weighted\_sum\_squared}$$
$$\Longrightarrow\ \boxed{\text{"Sylvester 惯性"在 Mathlib 中已形式化（二次型／SignType 形式）}\ \Longrightarrow\ \textbf{该 dent 作废}}$$ ✓✓✓
```

## §3 ⛔ 结果②：`von Neumann 迹不等式` **我方无 Lean 工件**（登记勘误）

```
$$\text{全库扫描（排除 }fn\_backup/fupeng/github/quant\text{-}system\text{）}:\ \text{全部 }\texttt{.lean}\ \text{文件中}$$
$$\boxed{\texttt{vonNeumann}\ /\ \texttt{Sylvester}\ /\ \texttt{inertia}\ /\ \texttt{signature}\ /\ \texttt{singularValues}\ /\ \texttt{trace\_mul}\ \textbf{命中数}=0}$$ ✓✓
$$\text{已查目录}:\ \texttt{dn-project/lean/}\ (\text{PB-* 与 PA-*：Abel／Stieltjes／Lemma1-3／S4 族}),\ \texttt{tldc-lean/}\ (\text{TLDC 骨架}),\ \texttt{lean-frontier-audit/},\ \texttt{external/liouville-goldbach/}$$ ✓
$$\text{"von Neumann" 仅在}\ \textbf{两处文档}（`RH-LINE-ASSET-VALUE-INVENTORY.md`、`V185/V186` 的论文阅读笔记）\ \text{出现 —— 属\textbf{文献引用}，非我方工件}$$ ✓
$$\Longrightarrow\ \boxed{\text{声称"Lean 侧补了 Mathlib 缺的 von Neumann 迹不等式"}\ \textbf{在本仓库无工件支持}}$$ ✗✗
$$\textbf{最可能来源}:\ \text{该不等式是 }arXiv{:}2608.13637\ (\text{惯性机制})\ \text{的\textbf{数学工具};\ 声称或为"论文阅读笔记"与"我方 Lean 工件"的\textbf{混淆}}$$ ⚠️
```

## §4 结果③：Mathlib 现状与"可否直接组合"（未定论）

```
$$\text{本次检索\textbf{未能确定} Mathlib 是否已含 von Neumann 迹不等式（} \texttt{Matrix.trace\_mul\_le} \text{ 类）}$$ ⚠️
$$\text{且判据须为（照您 §危险点）}:\ \boxed{\text{"Mathlib 无此 theorem"}\ \ne\ \text{"数学上不能由现有 theorem 直接推出"}}$$
$$\Longrightarrow\ \text{即便工件存在，也须先查：能否由 } \texttt{Matrix}/\texttt{InnerProductSpace}\ \text{现有 API（谱定理／奇异值／秩-迹）}\ \textbf{直接组合}$$ ⚠️
```

## §5 判词（照您预设的 EXIT）

```
$$\boxed{\text{两个 dent: 一个已覆盖（Sylvester）、一个无工件（von Neumann）}}$$ ✓✓
$$\text{按您 §EXIT}:\ \text{"若发现任一其实已有完整 theorem}\Longrightarrow\text{立即换另一个 dent"}\ ——\ \text{现已换到 von Neumann},\ \text{但其\textbf{工件不存在}}$$ ⚠️
$$\text{下一步的合法分叉}:\ (i)\ \textbf{找回工件}（\text{可能在被清理的临时目录 ⟹ 本仓库无}）;\ (ii)\ \textbf{重做}（= 真 }RUN:\ \text{在 }Lean\ \text{中形式化 von Neumann 迹不等式，}\textbf{但必须先核 Mathlib 现状}）;\ (iii)\ \text{若 }Mathlib\ \text{已有 ⟹ 形式化缺口\textbf{两例皆不可用}}$$ ✓
$$\textbf{诚实标注}:\ \text{目前证据\textbf{尚不足以}宣布"形式化缺口不能作为天然优势" —— 缺的是"Mathlib 是否已有 von Neumann"这一步检索}$$ ⚠️
```

## §6 勘误（对 `RH-LINE-ASSET-VALUE-INVENTORY.md`）

```
$$\textbf{勘误}:\ \text{原声称"Lean 侧补了 Mathlib 缺的 von Neumann 迹不等式与 Sylvester 惯性"}\ \Longrightarrow\ \text{应改为}$$
$$\qquad \boxed{\text{"Sylvester 惯性：Mathlib \textbf{已有}（二次型/SignType 形式）"};\quad \text{"von Neumann 迹不等式：}\textbf{本仓库无工件，声称待核"}}$$ ✓✓
$$\text{（依据：本档 §2／§3 的实跑扫描与官方文档逐字）}$$ ✓
【⛔ 纪律】 本轮**零新数学计算**；`U_{2,3}` 暂停；**不回 RH** ✓
【数据】 扫描命令与目录清单见 §2／§3；Mathlib 引用为**官方文档页（档级）** ✓
【边界】 §4 的 Mathlib 现状未定论；§5(iii) 为**条件性**判断 ✓

## §附 【技术词回查】（补录）
```
技术词 formalization    命中文件数=14   :: ./E7-A3-2-bandwidth-check.md ./CAPMIX1A-I-vs-truth-sound-but-incomplete.md ./EXPLORATION-POINTS-REGISTER.md 
技术词 gap              命中文件数=240  :: ./pfe-archive.md ./grh-goldbach-paper-draft-v2.md ./r3-death-sentence-2026-09-09.md 
```
