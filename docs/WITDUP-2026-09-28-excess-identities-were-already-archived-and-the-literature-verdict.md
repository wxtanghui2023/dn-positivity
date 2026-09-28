# WITDUP-2026-09-28 — C-540：⚠️**纪律事故（第四次同型）**：$\delta$-场恒等式族（一/二/三阶）**已于 2026-09-25 入库**；本档如实记录重复 ＋ 登记**文献状态账**

> **范围**：如实记录重复劳动 ＋ 文献判定；**不作路线裁定** ✗（沿用唐先生 19:51 令）
> **空间 B** 专用 ✓

**已查地图**：`scripts/tech_word_check.sh` 命中 `三阶恒等式` → **3 档**（`EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md` ／ `PLAN-2026-09-25-…` ／ `PROFILE-2026-09-26-…`）⟹ **按纪律先读档，确认已覆盖** ✓
接续：`EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md`

D0: 本档对象 ＝ **档案已有**（$\delta$-场／二/三阶恒等式／$N_1{+}N_2$／文献下界——**无新数学对象** ✓）
D1: 0（**本档不产生新数学自由度**；产出＝纪律事故记录 ＋ 文献状态账更正）⚠️
[R]

---

## §0 ⚠️ **纪律事故（如实记录）**

**事实**：我在 2026-09-28 的两轮中"重新推出"了下列全部内容，**而它们已在 `EXCESS-2026-09-25` 中**：

| 我 9-28 "推出" | `EXCESS-2026-09-25` 原位 |
|---|---|
| $\sum_x\delta_x{=}285$ | 同（§3 硬约束）✓ |
| $4(A_1{+}A_2){=}285{+}\sum\delta^2$（含**系数 4** 修正） | **同式已列**（§2 二阶恒等式）✓ |
| 三阶恒等式（球交枚举形式） | **同式已列**（§2 三阶；且已在真实 120-码上枚举校验 $\sum\binom m3{=}138$ ✓） |
| "恒等式族**不排除** 119" | **同结论已列**（§3 结论）✓ |
| 三球交表（$(1,1,2){\to}1$，$(2,2,2){\to}1$） | §2 球交事实（$\kappa_1{=}\kappa_2{=}2$；三阶交已枚举）✓ |
| "下一步走 Krawtchouk/全局" | **`Layer 2+` 已标为下一步**（§7.5）✓ |

**唯一新增**：$285{+}6\,\mathrm{Tri}(S)$ 这一**三角形计数的打包写法**（旧档为 $\binom{m}{3}$ 形式；代数同源）。

**根因**：未按 `PROTOCOL-pre-work-map-check` 先跑 `tech_word_check` 全部关键词（我只跑了新造词，未跑 `三阶恒等式` 这类**已存在术语**）。
**这是同类第 4 次**（前三次：C-451／C-452／C-453 系列先写后跑）。**本档即为其记录**。

## §1 文献状态账（**本档唯一新增内容 ✓**）

$$\boxed{1997\ \text{survey（Cohen–Litsyn–Lobstein–Mattson, AAECC 8(3):173–239）Table A}:\quad 105\le K(10,1)\le120}$$

**口径纪律 ✓**：Table A 之 $105$ 带文献标记 **e**（表下注明对应不同文献）⟹ **不得**写成"Prop 2.6 给出 105" ✗；正确表述＝**"1997 该期已知状态为 $105\le K(10,1)\le120$"** ✓

**与时序一致 ✓**：

| 年 | 下界 | 来源 |
|---|---|---|
| $1997$ | $105$ | 本 survey Table A |
| $2004$ | $\mathbf{107}$ | BÖW（OEIS A000983 ✓，与 C-427 一致） |
| 本届自算 | $105.2223$ | SDP（C-474 ✓，**低于** $107$） |
| 上界 | $120$ | 已知构造 ✓ |

⟹ **119 未被 1997 经典 excess machinery 排除 ✓**（历史区间 $105{\le}K{\le}120$）。

## §2 路线地位（**修正，不作裁定**）

$$\text{sphere-covering}\ \to\ \text{counting excess（§2.5）}\ \to\ \text{refined lower-bound}\ \to\ \text{LP/SDP}$$

$$\boxed{\text{C-539 之 }285\text{-excess 一阶路线}\ \subset\ \text{Cohen §2.5 经典 excess family}}$$

**含 §7 已做者**：Haas 2013 层式恒等式 → **LP${=}93.09$（不足 ✗，已校准 ✓）**。
**尚未做者**（旧档已标）：**`Layer 2+`＝子空间耦合变量 ＋ incidence ＋ 整数可行性** ⟸ **与唐先生 19:51 之"Krawtchouk/全局约束"为同一层** ✓

## §3 技术词回查（**本轮严格先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "重复劳动" "Layer2+" "文献状态账"
技术词 重复劳动     命中文件数=23   :: ./V106-L3-Q3-independent-sqrt-positivity-audit.md ./WITDUP-2026-09-28-excess-identities-were-already-archived-and-the-literature-verdict.md ./ASSETS-REGISTRY.md
技术词 Layer2+          命中文件数=1    :: ./WITDUP-2026-09-28-excess-identities-were-already-archived-and-the-literature-verdict.md
技术词 文献状态账  命中文件数=1    :: ./WITDUP-2026-09-28-excess-identities-were-already-archived-and-the-literature-verdict.md
```


| 词 | 本线他档命中 | 跨空间同名（不计 ✗） | 本档新增 |
|---|---|---|---|
| 重复劳动 | 22（通用词，**不计** ✓） | 0 | —（通用词） |
| Layer2+ | 0 | 0 | ✓ |
| 文献状态账 | 0 | 0 | ✓ |

**关键回查（本轮事故之检出手段）**：

```
$ bash scripts/tech_word_check.sh "三阶恒等式"
技术词 三阶恒等式   命中文件数=3    :: ./PROFILE-2026-09-26-… ./PLAN-2026-09-25-… ./EXCESS-2026-09-25-K10-1-delta-field-and-subspace-counting.md
```

⟹ **若我在 9-28 首轮即跑此词，即会立即发现重复** ✓（纪律教训 ✓）

## §4 边界（硬 ✓）

- 不改门 ✓；不开门② ✓；不跨空间 ✓；**不作路线裁定** ✗
- **明确否认** $C{=}3{\Rightarrow}{\neg}1111$ 已 ✗；**明确否认** $128{=}145{-}17$ 已 ✗；**明确否认** 119 不存在已 ✗（V290）
- 本档**不**主张任何数学新性 ✓
