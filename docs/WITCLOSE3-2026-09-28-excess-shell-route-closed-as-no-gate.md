# WITCLOSE3-2026-09-28 — C-539：★excess–shell 路线闭幕（285 → $N_1{+}N_2{\ge}143$ → $N_{AA}{\le}240$ → $m{\ge}11$，与 $\lvert R\rvert{=}79$ 相容，无闸门）

> **范围（照唐先生 2026-09-28 19:37 令 ✓）**：判定 excess-shell 路线是否可闭合；**不作路线裁定** ✗；空间 B 专用 ✓

**已查地图**：承 C-538/C-537/C-535（`WITCOVER-…`／`WITAR-…`／`WITCLOSE-…`），**非新案 ✓**

D0: 本档对象 ＝ **档案已有**（excess 恒等式／$N_1{+}N_2$／$N_{AA}$／$m$——无新数学对象 ✓）
D1: 1（**首次判定 excess–shell 路线无闸门（$m{\ge}11$ 与 $|R|{=}79$ 相容）✓✓ ＋ 首次确认 $N_3(I)$ 可被 79 个 residual center 合理覆盖 ✗✓**）
[R]

## §0 结论

$$285\text{ excess} \Longrightarrow N_1{+}N_2\ge143 \Longrightarrow N_{AA}\le240 \Longrightarrow m\ge11$$

$m{=}\lvert R\cap N_2\rvert{\ge}11$ 与 $\lvert R\rvert{=}79$ 完全相容。**此路线现无 contradiction gate。**

## §1 已闭合链

| 步 | 结论 |
|---|---|
| 球计数 | $\sum_x m(x){=}1309$, $\sum_x\delta_x{=}285$ |
| 重叠恒等 | $2(N_1{+}N_2){=}\sum_x{m(x)\choose2}$ |
| 一阶下界 | $N_1{+}N_2{\ge}143$ |
| $N_{AA}$ | $N_{AA}{=}\lvert E_{\rm full}\rvert{\le}240$ |
| $N_3$ 覆盖 | $m{\ge}11$（$4m{+}(79{-}m){\ge}112$） |

## §2 净结果

$$\boxed{\text{Excess–shell route CLOSED-AS-NO-GATE}}$$

**正结构事实 ✓**：$N_3(I)$ 之 112 点实际可被 79 个 residual center 覆盖。不可再视 $N_3$ 为隐藏容量瓶颈。

## §3 技术词回查

```
$ bash scripts/tech_word_check.sh "excess闭幕" "shell闸门" "N3不瓶颈"
技术词 excess闭幕     命中文件数=0    ::
技术词 shell闸门      命中文件数=0    ::
技术词 N3不瓶颈      命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（不计 ✗） | 本档新增 |
|---|---|---|---|
| excess闭幕 | 0 | 0 | ✓ |
| shell闸门 | 0 | 0 | ✓ |
| N3不瓶颈 | 0 | 0 | ✓ |

- 写后补跑 ⚠️ 据实 ✓

## §4 边界

- 不跨空间 ✓；**不作路线裁定** ✗；**明确否认** 119 不存在已证 ✗（V290）
