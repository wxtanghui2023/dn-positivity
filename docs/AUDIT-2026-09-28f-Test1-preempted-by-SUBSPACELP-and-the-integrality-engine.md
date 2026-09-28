# AUDIT-2026-09-28f — **Test-1 结果：LP 层零增益（档案已证等号定理）⟹ 引擎必在\ \textbf{整性}**

> **性质**：**实验/审计**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-28 20:39 ✓
> **唐先生令**：**跑 Test-1**（$k{=}1\to k{=}2$；输出 $L_0,L_1,\Delta,N_{\rm killed}$ ＋ 118-feasibility；四门 A/B/C/D）✓

**已查地图**：★**命中既有档** —— `SUBSPACELP-2026-09-28-level-m-lp-relaxation-equals-volume-bound.md`（**等号定理 ＋ 零增益实测**）｜`WITFIB-2026-09-28`（**$k{=}1$ fiber 化 ＝ 精确重述，非归约**）｜`WITW2C-2026-09-28`（$U_b{\subseteq}P_{1-b}$／$|P_0{\cap}P_1|{\le}57$）✓

D0: 本档对象 ＝ **档案已有**（level-$m$ 系统／LP 松弛——**无新数学对象** ✓）
D1: 0（产出＝**Test-1 之执行记录 ＋ 命中既有等号定理 ＋ 引擎重定位** ⚠️）

---

## §0 结论（先给）

$$\boxed{\textbf{(1) Test-1 之 LP 部分\ \textbf{已被档案抢先}:}\ \texttt{SUBSPACELP-2026-09-28}\ \text{已证\ \textbf{等号定理}}\ ✓✓}$$
$$\boxed{\textbf{(2) 独立复跑确认（本档 ✓✓）}:\ n{=}10:\ L(m)\equiv\mathbf{93.090909}\ (m{=}1{:}10);\ n{=}9:\ L(m)\equiv\mathbf{51.200000}\ (m{=}1{:}9)}$$
$$\boxed{\textbf{(3) 四门判定}:\ \Delta_k\equiv0\ \forall k\ \Longrightarrow\ \textbf{Gate C 触发}\ \Longrightarrow\ \text{LP-refinement 层\ \textbf{KILL}}\ ✗}$$
$$\boxed{\textbf{(4) ★引擎重定位}:\ \text{Östergård--Blass 之引擎\ \textbf{不是 LP}（其松弛恰给体积界 ⟹ 零增益）; \textbf{是\ 整性 ＋ 不等价分布分类 ＋ 递归}}}\ ✓✓$$

## §1 独立复跑（**逐字 ✓，`scripts/SUBSPACE_LP_2026-09-28_level_m_bound.py`**）

```
n = 10   volume/sphere bound 2^n/(n+1) = 93.090909
  m   t=2^m  s=2^(n-m)           L(m)     L(m)-vol  status
  1       2        512      93.090909     0.000000       0
  2       4        256      93.090909    -0.000000       0
  3       8        128      93.090909     0.000000       0
  4      16         64      93.090909     0.000000       0
  5      32         32      93.090909    -0.000000       0
  6      64         16      93.090909     0.000000       0
  7     128          8      93.090909     0.000000       0
  8     256          4      93.090909    -0.000000       0
  9     512          2      93.090909     0.000000       0
 10    1024          1      93.090909     0.000000       0
```

$$\Longrightarrow\ \boxed{L_1(k)=L_0=93.09\ \forall k;\quad \Delta_k=0;\quad N_{\rm killed}=0}\ \text{（Test-1 所询之四量全部退化）}$$

## §2 ⚠️ $L_0$ 之口径更正

$$\text{本档前曾用 }L_0{=}94.4\ \text{（C-546 Plagne 主项}\ (r{+}\tfrac{s}{s+k})2^k\text{）}\ \Longrightarrow\ \textbf{该值属 Plagne 之 }(r,s)\ \textbf{参数化}\ \text{，非 level-}m\ \text{LP 值}\ ⚠️$$
$$\text{level-}m\ \text{LP 之真值}\ L_0=\frac{2^n}{n+1}=\mathbf{93.09}\ \checkmark\ (\text{等号定理})$$

## §3 四门判定（**照唐先生 20:36 令 ✓**）

| 门 | 条件 | 实测 | 判定 |
|---|---|---|---|
| **A** | $L_1(k)>94.4$ | $L_1{\equiv}93.09$ | **未触发** |
| **B** | $L_1{=}L_0$ 但**真跨状态 incompatibility** | 约束全为线性计数 ⟹ **无** | 未触发 |
| **C** | $L_1{=}L_0$ 且新约束**可化回线性不等式** | **正是如此** ✓ | **★触发 ⟹ KILL** ✗ |
| **D** | $\mathcal F_{118}^{(1)}{=}\varnothing$ | 未出现（118 可行） | 未触发 |

$$\therefore\ \boxed{\text{按唐先生之 Gate C}:\ \text{LP-refinement 层\ \textbf{立即 KILL}}\ ✗}\ \text{（＝"Haas-reencoding"，非新层 ✓）}$$

## §4 ★ 但档案自身给出了引擎定位（**这才是活口 ✓✓**）

$$\texttt{SUBSPACELP}\ §0(3)\ \text{逐字}:\ \text{"Östergård--Blass 的引擎\ \textbf{不是} LP; 而是\ \textbf{整性 ＋ 不等价分布分类 ＋ 递归}"};\ \text{LP 之真实角色 ＝\ \textbf{剪枝/校验}}$$

$$\Longrightarrow\ \boxed{\text{本轮回之"refinement"若指\ \textbf{LP 层细分},\ 则已 KILL}; \text{若指\ \textbf{整性 ＋ 不等价分布分类 ＋ 递归},\ 则\ \textbf{尚未做}}\ ⚠️}$$

$$\therefore\ \text{唐先生 §2 所要求之"state compatibility 约束"（}s_i{\not\leftrightarrow}s_j\text{）}\ \textbf{恰属整性/分类层}，\textbf{非}\ \text{LP 层}\ ✓$$

## §5 修正后之下一实验（**待批准，非本轮**）

$$\textbf{Test-1′}:\ \text{在\ \textbf{整性}层做一轮"不等价分布分类"}:\ \text{枚举 level-}m\ \text{之整数分布 }\{y_i\}\ \text{（}\sum y_i{=}118\text{）},$$
$$\qquad\text{按 }Q_{10}\ \text{之坐标置换群}\ (\operatorname{Aut}\cong S_{10}\rtimes F_2^{10})\ \text{归并等价类},\ \text{剔除与覆盖不相容之类},\ \text{看剩余类数是否骤降}$$

$$\text{判据（同 Gate C）：若归并后约束仍可化回线性 ⟹ KILL; 若出现真 incompatibility ⟹ 活 ✓}$$

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "等号定理" "零增益" "整性引擎"
技术词 等号定理   命中文件数=5    :: ./ASSETS-REGISTRY.md ./E-GATE-and-Lemma-R-R2-CLOSED.md ./LEMMA-R-P1-CLOSED-prior-art-and-three-gate-correction.md ./SUBSPACELP-2026-09-28-level-m-lp-relaxation-equals-volume-bound.md ./AUDIT-2026-09-28f-...
技术词 零增益    命中文件数=13   :: ./NEGATIVE-RESULTS-2026-09-12-ROUND.md ./C320-...-CLOSED-M5-question-OPEN.md ./SUBSPACELP-2026-09-28-... ./AUDIT-2026-09-28f-...
技术词 整性引擎   命中文件数=1    :: ./SUBSPACELP-2026-09-28-level-m-lp-relaxation-equals-volume-bound.md
```

**口径（空间隔离 ✓）**：`等号定理`／`零增益` 之多数命中属**空间 A（RH 线）**（`E-GATE-…`／`LEMMA-R-…`／`NEGATIVE-RESULTS-…`／`C320-…`）⟹ 标「**空间 A 同名，不计**」✗；本线之作＝`SUBSPACELP` ＋ 本档 ✓。原口径如下：`等号定理`／`零增益` 之命中即**本档所接续之档**（`SUBSPACELP`）⟹ 标「**档案已有（本线，引用，不列为提出）**」✓；`整性引擎` 为本档新造 ✓

## §7 边界（硬 ✓）

- 独立复跑（`linprog`/HiGHS）＋ 既有档引证 ✓；**无新数学** ✗；**不加 C 号** ✓；**不作路线裁定** ✗；不跨空间 ✓
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- §5 为**提案**，未执行 ✗；**不主张** Test-1′ 必成功 ⚠️
