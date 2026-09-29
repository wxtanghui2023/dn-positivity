# DIAGNOSIS（2026-09-29）—— **$\operatorname{Aut}$-不变性解释了全部 9 次失败**；下一步的正确形式＝有内容的对称破坏

> **性质**：**问题特化诊断**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 18:30 ✓
> **唐先生令**：从"套用资产"改为"针对本课题重新设计" ✓

**已查地图**：`CONNECTION-AUDIT`／`AUDIT-29zf`（$F_4$ 弱）／`CALIBRATE-K91*`／`PROTOCOL-T0-T7` ✓

D0: 本档对象 ＝ **档案已有**（不变性／对称破坏—经典 ✓）
D1: 0（产出＝**一条诊断 ＋ 一条方法结构判定** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 诊断}:\ 105.2223\to107\ \text{之差\ \textbf{必然是整性/非对称间隙};\ Aut-不变论证\ \textbf{结构上}不可能跨过}}$$
$$\boxed{\text{② 证据}:\ \text{本会话 9 条候选，7 条 Aut-不变（}\mu,P_j,\text{parity},\Lambda,\text{face},S_c,n_0\text{）\ \textbf{必然}失败}✗}$$
$$\boxed{\text{③ 反证（我方自测）}:\ \text{两次\ \textbf{打破}对称（}Q_5{\times}Q_5、F_4\text{-cell）给球界 94\ }\textbf{<}\text{ 不变 SDP 105.22}✗}$$
$$\boxed{\text{④ 方法结构}:\ \text{必须\ \textbf{有内容的}对称破坏（固定码字/轨道）＋ 枚举 ＋ 剪枝;\ 单纯固定坐标无效}}$$

## §1 诊断（✓ 核心）

$$\text{松弛族}:\ \text{Delsarte LP}／\text{SDP-3 (Terwilliger)}／\text{Habsieger 同余}\ \text{—— 全部}\ \operatorname{Aut}(Q_{10}){-}\textbf{不变}$$
$$\text{真值}:\ 107\ \text{由\ \textbf{具体}（非对称）覆盖达成};\ \text{且 }107>105.2223\ (\text{Aut-不变最优松弛})$$
$$\therefore\ \boxed{\text{间隙内容 ＝ 整数性/支撑非对称性；不变式方法之天花板\ \textbf{结构上}＝105.2223}\ ✗}$$

## §2 对本会话 9 条的判定（✓）

| # | 候选 | Aut-不变 | 结局 |
|---|---|---|---|
| $1$ | point-excess parity | 是 | 实测假 / 非独立 |
| $2$ | 粗 $p{=}11$ 同余 | 是 | 恒等式 |
| $3$ | $\Lambda$ | 是 | $=3\sum\binom{\mu}3$ |
| $4$ | $Q_5{\times}Q_5$ fiber | 否 | 精确重述 / 前提 $22\%$ |
| $5$ | face 矩 | 是 | $\in\operatorname{span}\{A_d\}$ |
| $6$ | $S_c/S_x$ | 是 | 真但弱 |
| $7$ | $n_0$ | 是 | 真但弱 |
| $8$ | 孤立容量 | 是 | 次线性 |
| $9$ | $F_4$-cell 对极 | 否 | 真但弱（$\Sigma\delta\ll$ 容量） |

$$\therefore\ \boxed{\text{7/9 为 Aut-不变}\Longrightarrow\textbf{必然}\ \text{不越 }105.2223};\ \text{2/9 破坏对称但\ \textbf{无内容}（固定坐标）}\Longrightarrow\ \text{反退化到球界}✗$$

## §3 方法结构判定（✓ 真正的"问题特化"结论）

$$\text{历史同型成功}:\ \text{Östergård--Blass}\ K(9,1){=}62:\ \textbf{固定局部构型} \to \textbf{等价类} \to \textbf{LP 细化} \to \text{零维}$$
$$\therefore\ \text{要 }107\ \text{必须走"对称破坏 ＋ 枚举 ＋ 剪枝"之\ \textbf{类型}，而非继续找不变式}✓$$
$$\text{我方已知障碍（实测）}:\ \text{（a）朴素 }2^{256};\ \text{（b）SDP 剪枝在 }M{=}106\ \textbf{无效}（105.2223<106）✗$$
$$\therefore\ \text{唯一未探之处}:\ \textbf{有内容的对称破坏是否能\ \textbf{压缩}枚举状态空间（而非仅减少常数）}$$

## §4 边界（硬 ✓）

- **不变性判定与 9 条分类均为档案可核 ✓**；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；本档系**诊断**，非结果 ✓
