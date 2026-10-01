已查地图：见 docs/TOPIC-INDEX.md（L1 课题级 · HN-C2 覆盖设计）
D0: 本档对象 = 试点状态（工具产物）；非数学命题，不主张任何新值
D1: 0
ASSUMES: N/A (状态档)

# pilot HN-C2 — $C(12,6,4)$ 试点状态（2026-10-01 15:3x）

## 已得 ✓

$$\text{[① n}\le41\text{]}:\ \textbf{FEASIBLE}\ (\text{CP-SAT}\ 1.7\,\mathrm{s},\ 16646\ \text{冲突},\ 972358\ \text{分支})\ \Longrightarrow\ \textbf{\text{41 块显式构造，覆盖 }495/495\ \text{完备}}\ ✓✓$$
⟹ **独立复现 best-known 上界 41，且带可复核证书**（41 个 6-块，见 `out/ljcr_c12_cpsat.log`）

## 结果（300 s 轮）⏳⟹加长重跑

$$\text{[② n}\le40\text{]}:\ \textbf{UNKNOWN}\ (300\,\mathrm{s}\ \text{用尽}:\ 3{,}456{,}004\ \text{冲突},\ 37{,}921{,}730\ \text{分支})\ \Longrightarrow\ \textbf{\text{未决（不作不存在证据）}};\ \text{已启动 }1800\,\mathrm{s}\ \text{长跑（仅 }n{=}40\text{）} ✓$$


## L2-a（LP 对偶权重法）—— **已实测：耗尽** ✗✗（2026-10-01 16:2x）

$$\max\sum_T w_T\ \text{s.t.}\ \forall B:\sum_{T\subset B}w_T\le1,\ w\ge0\ \Longrightarrow\ \lambda=33.0000000000\ (\text{均匀权 }w_T{=}1/15,\ 495\times\tfrac1{15}{=}33)$$
- 深零 13860；支撑 495；**924 块全部取等**
- **严格有理证书** ✓：$\sum=33/1$，整数算术逐块复核通过（`out/hnc2_lp_dual.log`）
- **判定**：$M\ge33$ —— **仅等于 Schönheim 界** ⟹ **LP 弛豫弱**，**不足以触及 40/41** ⟹ 路径 a **耗尽** ✗
- **推论（重要）**：库下限 40 **不可能来自一阶 LP/均匀权** ⟹ 必来自**更强方法**（递归 Schönheim／整数性／结构论证）⟹ **L2-c／L2-e 为下一刀**


## ★ 天花板前置分析（2026-10-01 16:2x，路径去留之先验裁定 ✓✓）

| 路径 | **天花板** | 来源 | 判定 |
|---|---|---|---|
| A 一阶 LP/均匀权 | **33** | **对称性**（$S_{12}$ 传递 ⟹ 群平均得均匀权 $c{=}1/15$；$495/15{=}33$）—— **与实测 λ=33 完全吻合** ✓ | **死** ✗（与 40 无关） |
| **C 递归 Schönheim** | **恰好 40** | $C(12,6,4)\ge\lceil\frac{12}{6}C(11,5,3)\rceil$，而 **$C(11,5,3){=}20$ 为库内已封闭精确值** ⟹ $2\times20{=}40$ —— **与库下限 40 精确吻合** ✓✓ | **只能到 40，够不到 41** ✗ |
| D ILP 最优性 | 无先验上限（精确法） | — | 计算难（1800 s UNKNOWN）⚠️ |
| E 核库下限出处 | — | **已查明 ＝ 递归 Schönheim（见 C）** ✓✓ | 已完成 |
| **J Johnson/Delsarte 型 LP** | **待算**（$\ge33$） | Johnson 方案 $J(12,6)$ 之线性规划界 | **下一刀** ✓ |

$$\boxed{\text{结论}：M\in\{40,41\}\ \text{且}\ 40\ \text{恰为 Schönheim 界}\ \Longrightarrow\ \text{证 }M\ge41\ \text{必须证\ \textbf{Schönheim 递归在此不紧}}（\text{需稳定性/整数性论证}）}$$

## 待决 ⏳

$$\text{[② n}\le40\text{]}:\ \text{CP-SAT 上限 }300\,\mathrm{s}\ \text{运行中};\ \text{三出口}:\ \textbf{FEASIBLE}\ (\text{上界 }41\to40,\ \text{记录改进})\ \mid\ \textbf{INFEASIBLE}\ (\Longrightarrow C(12,6,4)=41\ \text{精确},\ \text{gap 闭合})\ \mid\ \textbf{UNKNOWN}\ (\text{未决，不作不存在证据})$$

**工具** ✓：`scripts/ljcr_C12_6_4_cpsat.py`（CP-SAT）｜`scripts/ljcr_C12_6_4.py`（HiGHS 版，已因求最优过慢中止）
**数据** ✓：块 $=C(12,6)=924$；4-子集 $=C(12,4)=495$；Schönheim 下界 $=\lceil495/15\rceil=33$（**与库下限 40 相差 7** ⟹ 库下限来自更强方法，待核）

## 纪律

$$\textbf{(D1)}\ \text{不主张数学新值} ✓;\ \textbf{(D2)}\ \text{41 构造可秒级复核} ✓;\ \textbf{(D3)}\ \text{未取禁用原文／未碰 RH} ✓$$

## 【技术词回查】

```
技术词 试点状态     命中文件数=1    :: ./pilot-HN-C2-C12-6-4-STATE.md
```

ROUTE-CHECK: <全部>=NEW
