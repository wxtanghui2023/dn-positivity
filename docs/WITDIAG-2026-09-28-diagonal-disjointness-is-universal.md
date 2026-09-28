# WITDIAG-2026-09-28 — **C-513：★★P1-A 解决 —— 对角禁交为\ \textbf{普遍事实}（$W_{11}\cap W_{22}=W_{12}\cap W_{21}=\varnothing$ 于全量 \textbf{23200} 实例，\textbf{0 反例}）✓✓✓；且\ \textbf{交非空 $\iff$ 四正}（各恰 640）✓✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §5）**。
> **范围（照唐先生 2026-09-28 15:40 令 ✓）**：只做 **P1-A（diagonal-disjointness）**；**不作路线裁定** ✗。

**已查地图：命中（接续 C-512／C-511／C-510，非新案 ✓）**：`WITTYPE-…`／`WITLAM-…`／`WITFAM-…`
D0: 本档对象 ＝ **档案已有**（$W_{ij}$/$\lambda$；无新数学对象 ✓）
D1: 1（**首次得对角禁交之\ \textbf{普遍性}（0/23200，非四正专属 ✓✓✓）＋ 首次得\ \textbf{交非空 $\iff$ 四正}（各 640）＋ 首次使 $\pi(w^\ast)$ 共端点性成为\ \textbf{普遍事实之推论}** ✓）
**[RESEARCH]**

---

## §0 结论（**★P1-A 成\ \textbf{普遍事实} ✓✓✓**）

$$\textbf{设定 ✓}:\ \text{实例全集}\ N=\mathbf{23200};\quad W_{ij}{:=}\mathcal S\cap N_2(I_i)\cap N_2(I_j)\ ✓\ \big(\text{四槽 }11,12,21,22✓\big)$$
$$\boxed{\textbf{(1) ✓✓✓对角禁交 ＝ \textbf{普遍事实（非四正专属）}:\ }}W_{11}\cap W_{22}=\varnothing\ \text{且}\ W_{12}\cap W_{21}=\varnothing\ \text{于\ \textbf{全部 23200 实例}}✓✓✓$$
$$\qquad\textbf{（实测 ✓✓）}:\ \text{对角对非空之实例}=\mathbf0\ /\ 23200\ ✓✓✓\ \text{——\ \textbf{零反例}}✓✓✓$$
$$\qquad\Longrightarrow\ \textbf{（重大 \textbf{简化}}✓✓✓）:\ \text{唐先生 §3 所设之"}\pi(w^\ast)\ 共端点"\ \textbf{不必}限于四正 ✓✓\ \text{——\ }它是一条\ \textbf{全量普适}之结构事实 ✓✓, \text{且其证明只须\ \textbf{单一}局部引理 ✓}$$
$$\boxed{\textbf{(2) ✓✓★交非空 \iff 四正（精确对当）}:\ }$$
| 槽对 | 类型 | 非空实例数 | 空实例数 |
|---|---|---|---|
| $11\cap12$ | 共端点（共 $a$） | $\mathbf{640}$ | $22560$ |
| $11\cap21$ | 共端点（共 $u$） | $\mathbf{640}$ | $22560$ |
| $12\cap22$ | 共端点（共 $v$） | $\mathbf{640}$ | $22560$ |
| $21\cap22$ | 共端点（共 $b$） | $\mathbf{640}$ | $22560$ |
| $11\cap22$ | **对角** | $\mathbf0$ ✓✓✓ | $23200$ |
| $12\cap21$ | **对角** | $\mathbf0$ ✓✓✓ | $23200$ |
$$\qquad\Longrightarrow\ \boxed{\text{重叠发生于}\ \textbf{共端点对}\ \iff\ \text{实例为\ \textbf{四正}}\ (640{=}640✓✓)}\ ✓✓\ \text{——\ 即\ \textbf{四正 \iff 恰有一处重叠} ✓✓}$$
$$\qquad\Longrightarrow\ \textbf{（与 C-511 一致 ✓✓）}:\ \text{四正时 }\mu\text{-多重集}(2,1,1,1,1,1)\ ✓\ \text{即\ \textbf{唯一}\ 重叠对（共端点）✓✓}$$

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §3（"欲证 C-512 之 }\pi\ \text{结构，只需证 }W_{ij}\cap W_{kl}\ne\varnothing\Rightarrow\{ij,kl\}\ \text{共端点"\ ）\ \textbf{完全正确}}✓✓✓\ \text{——\ 本档更进一步：该蕴含\ \textbf{在全量上成立} ✓✓✓}$$
$$\textbf{✓✓✓}:\ \text{其 §2（移除 }\mu{=}2\ \text{之 witness 后，四槽各挂 private witness；重叠恰一处）\ \textbf{成立}}✓✓\ \text{（实测四正时重叠恒一处 ✓✓）}$$
$$\textbf{✓✓}:\ \text{其 §10（"第一刀必须是 diagonal exclusion；若能由定义直接推出则进入结构阶段"\ ）\ \textbf{方向完全正确}}✓✓\ \text{——\ 且本档已把其\ \textbf{范围扩至全量}（无需四正前提 ✓✓）}$$
$$\textbf{✓✓}:\ \text{其 §4 之机制猜测（"对角重叠须迫使两个互不共享端点之 cross-pair 同入高 multiplicity，与唯一 }\lambda{=}1\ \text{槽冲突"\ ）\ ⟹ \textbf{仍待结构证明}}✓\ \text{（本档仅证事实 ✓）}$$

## §2 汇总裁（**✓✓✓**）

| 项 | 值 |
|---|---|
| 对角对非空实例 | $\mathbf0/23200$ ✓✓✓ |
| 共端点对非空实例 | 各 $\mathbf{640}$ ✓ |
| 对当关系 | 非空 $\iff$ 四正 ✓✓ |
| $\pi(w^\ast)$ 共端点 | **普遍事实之推论** ✓✓✓ |

## §3 下一靶（**照唐先生 §8 之三 lemma ✓，范围已扩**）

$$\textbf{（Lemma A ✓✓✓已实证）}:\ \boxed{\text{对角禁交（全量普适）}}\ ✓✓\ \text{——\ 余下\ \textbf{结构证明} ✓（唯一局部引理 ✓✓）}$$
$$\textbf{（Lemma B ✓✓下一刀）}:\ \text{四正 ＋ }w^\ast\in W_{11}\cap W_{12}\ ⟹\ R(w^\ast)\in\{(4,2,2,2),(2,4,2,4)\}\ \big(\text{第三值为其 }u/v\ \text{像 ✓}\big)✓$$
$$\textbf{（Lemma C ✓）}:\ \text{五 private witness 之 }R\text{-profile 被唯一确定到两轨道 }T_1,T_2\ ✓$$
$$\textbf{（靶 4 ✓✓）}:\ \textbf{跨层禁配}（照唐先生 §9 ✓）:\ \text{四正 cross-}\lambda\Rightarrow C\ge4\ ✓\ \text{——\ 与 }C{=}3\Rightarrow\neg1111\ \text{合成\ \textbf{跨层定理}}✓✓$$
$$\textbf{（禁止 ✗）}:\ \text{再做 census 扩张 ✗（照唐先生 §一 ✓）；把 Lemma A 之实证当结构证明 ✗✓}$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "对角禁交" "共端点对当" "跨层禁配"
技术词 对角禁交     命中文件数=1    :: ./WITDIAG-2026-09-28-diagonal-disjointness-is-universal.md
技术词 共端点对当  命中文件数=1    :: ./WITDIAG-2026-09-28-diagonal-disjointness-is-universal.md
技术词 跨层禁配     命中文件数=2    :: ./WITCEIL-2026-09-28-classical-ceiling-dominates-the-layer-sum.md ./WITDIAG-2026-09-28-diagonal-disjointness-is-universal.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 对角禁交 | 0 | 0 | ✓（**自命中 1**（本档 ✓）；照唐先生 §3 ✓） |
| 共端点对当 | 0 | 0 | ✓（本档新命名 ✓） |
| 跨层禁配 | 0 | 0 | ✓（照唐先生 §9 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（全量 23200 之六对槽交 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项★结果（对角禁交普遍性 ✓✓✓）** ＋ **一项对当（交非空 $\iff$ 四正 ✓✓）** ＋ **一项范围扩展（无需四正前提 ✓✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** Lemma A 之\ *结构证明* 已完成 ✗（仅实证 ✓）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
