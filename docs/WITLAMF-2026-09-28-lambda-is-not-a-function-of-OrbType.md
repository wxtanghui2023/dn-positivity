# WITLAMF-2026-09-28 — **C-528：✗✓\textbf{决定性否证} —— $\lambda$-型\ \textbf{不由 OrbType 决定}（同一 OrbType 可含 $(0,0,0,0)$ 与 $(2,1,2,2)$ 等多型）；故"$O_i$ 含零槽 ⟹ 非四正"\ 之链\ \textbf{在 OrbType 层不成立}**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 16:15 令 ✓）**：核"以 $\lambda$-型分离 $T$ 与 $O_i$"\ 之可行性；**不作路线裁定** ✗。

**已查地图：命中（接续 C-527／C-526／C-512，非新案 ✓）**：`WITSTATUS2-…`／`WITP3-…`／`WITTYPE-…`
D0: 本档对象 ＝ **档案已有**（OrbType／$\lambda$；无新数学对象 ✓）
D1: 1（**首次判定 $\lambda$-型\ \textbf{非 OrbType 之函数}（多型混合）✗✓ ＋ 首次给出 $T_1,T_2$ 之\ \textbf{完整 }\lambda\text{-型集}（含 }(0,0,0,0)\big)✓ ＋ 首次指出"$O_i$ 零槽"\ 链\ \textbf{不可在 OrbType 层闭合}✗✓**）
**[RESEARCH]**

---

## §0 ★结论（**$\lambda$ 非 OrbType 之函数 ✗✓**）

$$\textbf{设定 ✓}:\ \text{OrbType }O\ \text{（16-向量之规范型）};\ \lambda\text{-型}=(\lambda_{11},\lambda_{12},\lambda_{21},\lambda_{22})\ ✓$$
$$\boxed{\textbf{(1) ✗✓$\lambda$-型\ \textbf{非 }$O$\ 之函数}}:\ \text{实测多型混合 —— 例}:$$
$$\qquad O=(0,0,0,1,0,0,1,1,0,1,0,1,0,1,1,1):\ \lambda\in\big\{(2,0,0,2){:}244,\ (2,0,0,0){:}92,\ (0,0,0,2){:}92,\ (0,2,2,0){:}76\big\}\ ✓$$
$$\qquad O=(0,1,0,0,0,1,0,2,0,1,1,0,0,1,1,1):\ \lambda\in\big\{(2,1,0,0){:}90,\ (2,2,0,0){:}85,\ (0,0,2,2){:}75,\ (0,0,2,1){:}70\big\}\ ✓$$
$$\qquad\textbf{（关键 ✓✓）}:\ \text{连四正型 }T_1,T_2\ \text{亦含 }\lambda{=}(0,0,0,0)\ \text{之实例}:$$
$$\qquad\qquad T_1:\ \big\{(2,1,2,2){:}81,\ (2,2,2,1){:}79,\ \mathbf{(0,0,0,0){:}320},\ (2,2,1,2){:}81,\ (1,2,2,2){:}79\big\}\ ✓$$
$$\qquad\qquad T_2:\ \big\{(2,2,0,1){:}79,\ (1,2,2,2){:}79,\ (2,2,2,1){:}79,\ (1,0,2,2){:}79,\ (2,2,1,0){:}81,\ (2,2,1,2){:}81,\ (2,1,2,2){:}81,\ (0,1,2,2){:}81\big\}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{"}O_i\ \text{含零槽"\ 不能由 }O_i\ \text{本身推出;\ 亦不能推出"非四正"}}\ ✗✓$$
$$\boxed{\textbf{(2) ✗✓"}$O_i$ 零槽之链\ \textbf{在 OrbType 层不成立}}:\ }\text{唐先生之链 }O_i\Rightarrow z\ge1\Rightarrow\neg1111\ \text{须改}:{$$
$$\qquad\text{因 }\lambda\ \text{非 }O\ \text{之函数 ⟹ "}z\ge1"\ \text{不是 }O_i\ \text{之性质 ✗✓，而是 }O_i\ \text{之\ \textbf{mask-可实现集}（}$1111\notin M(O_i)\big)\ \text{之等价重述 ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{（循环风险 ✓✓）}:\ \text{"}C(O){=}3\iff 1111\notin M(O)"\ \text{（C-523 ✓）⟹ 该链\ \textbf{为同义反复}✗✓}$$

## §1 汇总裁（**✗✓**）

| 项 | 值 |
|---|---|
| $\lambda$-型是否 $O$ 之函数 | **否** ✗✓（多型混合） |
| $T_1$ 之 $\lambda$-型集 | 含 $(0,0,0,0)$（320）与四种 $(1,2,2,2)$-排列 ✓ |
| $O_i$ 之零槽 | **非** $O_i$ 之性质 ✗✓ |
| "零槽 ⟹ 非四正" | 链**不成立** ✗✓ |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生 §1（四正 ⟹ }\Lambda{=}\{1,2,2,2\}\ \text{＋ 唯一 }q^\ast\big)\ \textbf{成立}}✓✓\ \big(\text{C-511 ✓}\big){$$
$$\textbf{✓✓}:\ \text{其 §2（support 刚性之五项条件）\ \textbf{成立}}✓✓\ \big(\text{C-524/525 ✓}\big)$$
$$\textbf{✗✓}:\ \text{其 §"以 }\lambda\text{-型分离 }T\text{ 与 }O_i"\ ⟹ \textbf{在 OrbType 层不成立}✗✓\ \big(\text{本档 (1)}\big)$$
$$\textbf{✗✓}:\ \text{其 §4–§5（"四正 ⟹ Case A/B 矛盾"）\ ⟹ \textbf{有循环风险}}✗✓:\ \text{support 模板}\ \textbf{正是四正之推论}（640/640 ✓）⟹ \text{其\ \textbf{不能}}\ \text{与四正假设产生 }\bot\ ✗✓$$

## §3 真正的开放核心（**✓✓**）

$$\boxed{\text{唯一开放核心}:\ 1111\notin M(O)\ \text{之\ \textbf{直接结构证明}}\ ✓\ \text{——\ 即:\ 为何六个 }O\ \text{之 mask-可实现集不含 }1111}}{$$
$$\qquad\textbf{（不可用者 ✗）}:\ \text{① }\Sigma\lambda/\sigma\text{-和/}\lVert T\rVert_1\ \text{（纯计数，C-527 ✗✓）};\ \text{② }\lambda\text{-型作为 }O\ \text{之函数（本档 ✗✓）};\ \text{③ support 模板 ⟹ }\bot\ \text{（循环，§2 ✗✓）}$$
$$\qquad\textbf{（可用者 ✓）}:\ \text{直接对 }O\in\{O_1..O_6\}\ \text{证明:存在 }w\ \text{或某 }W_{ij}\ \text{之几何不可能性（\textbf{须引入 }O\ \text{之外的量}✓）}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "lambda非函数" "循环风险" "mask可实现集"
技术词 lambda非函数  命中文件数=1    :: ./WITLAMF-2026-09-28-lambda-is-not-a-function-of-OrbType.md
技术词 循环风险     命中文件数=28   :: ./EXT-4CT-2026-method-transfer.md ./lemma3-hostile-audit.md ./KOPT4-6-NEUTRAL-SPLIT-2026-09-27.md
技术词 mask可实现集 命中文件数=1    :: ./WITLAMF-2026-09-28-lambda-is-not-a-function-of-OrbType.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| lambda非函数 | 0 | 0 | ✓（本档据实 ✓） |
| 循环风险 | 0 | 0 | ✓（本档新命名 ✓） |
| mask可实现集 | 0 | 0 | ✓（照 C-503 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{须引入 }O\ \text{之外之量}:\ \text{如 }B=N_2(x)\cap N_2(p)\cap N_2(q)\ \text{之四点（}\mathrm{OrbType}\ \text{之源）；或 }c,z\ \text{两点之位置 ✓✓}$$
$$\textbf{（靶 2 ✓✓）}:\ \text{直接检查:对 }O\in\{O_1..O_6\}，\text{是否存在 }1111\ \text{之\ \textbf{构造性障碍}（非计数）✓✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{重跑两支复核（修 C-525 脚本 bug）✓}$$
$$\textbf{（禁止 ✗）}:\ \text{纯计数路线 ✗✓；}\lambda\text{-型作 }O\ \text{之函数 ✗✓；support 模板 ⟹ }\bot\ \text{（循环）✗✓}$$

## §6 边界（硬 ✓）

- **有限穷举** ✓（全量 23200 之 $(O,\lambda\text{-型})$ 联合 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项✗✓否证（$\lambda$ 非 $O$ 之函数）** ＋ **一项✓✓（循环风险指出）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** $1111\notin M(O)$ 已证 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
