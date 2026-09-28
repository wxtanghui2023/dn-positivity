# WITGATE-2026-09-28 — **C-516：P0→P3 全链审计台账（C-448→C-515）＋ ✗✓两处结论级更正（含\ \textbf{门 3 作为所陈述者\ 不可成立}）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §5）**。
> **范围（照唐先生 2026-09-28 15:49 令 ✓）**：按 P0→P3 重排全链并审计；**不作路线裁定** ✗。

**已查地图：命中（接续 C-515／C-514／C-513，非新案 ✓）**：`WITCAPB-…`／`WITONER-…`／`WITDIAG-…`
D0: 本档对象 ＝ **档案已有**（全链已登对象；无新数学对象 ✓）
D1: 1（**首次给出 C-448→C-515 之\ \textbf{P0→P3 全链审计台账}（含 17 项状态）＋ 首次判定\ \textbf{门 3 作为所陈述者不可成立}（全四正 witness 皆 owner-3，4480/4480 ✗✓）＋ 首次指出门 2B 与"}$\lvert\bigcup W\rvert<\Sigma\lvert W\rvert$\textbf{"等价** ✓）
**[RESEARCH]**

---

## §0 ★两处结论级更正（**须先立 ✓✓**）

$$\boxed{\textbf{(更正一) ✗✓门 3 作为所陈述者}\ \textbf{不可成立}}:\ \text{唐先生 §9-C1（"四正}\Rightarrow\exists w:|\mathrm{own}|\ge4\text{"，且要求由\ \textbf{witness 侧}\ \text{迫出）}}$$
$$\qquad\textbf{（实测 ✓✓）}:\ \text{四正之全部 witness 元素\ \textbf{皆为 owner-3}}:\ \text{分布}=\{\mathbf3{:}4480\}\ \big(\text{C-515 ✓}\big)\ \text{——\ 因 }W_{ij}\subseteq\mathcal S\ \text{按定义 ✓}$$
$$\qquad\Longrightarrow\ \textbf{在 witness 世界内，"被迫第四 owner"\ 根本不可能发生 ✗✓};\ \text{且"}\exists\ \text{owner}\ge4\text{"}\ \textbf{于一切实例平凡真}\ \big(B\ \text{之点恒 owner }4\text{–}5✓\big)$$
$$\qquad\Longrightarrow\ \text{故}\ \boxed{\text{门 3 不能直接产出跨层定理}}✗✓;\ \textbf{须取消或改写}✓$$
$$\boxed{\textbf{(更正二) ✗✓}\Sigma\lvert W\rvert\le6\ \textbf{不能作为目标}}:\ \text{（C-515 ✓）}\ \text{且"每点}\le2\ \text{槽"}\ \textbf{不蕴含}\ \Sigma\lvert W\rvert\le6\ ✗✓$$
$$\qquad\qquad\textbf{（正确等价形式 ✓✓）}:\ \text{四正之}\ \boxed{\lvert\bigcup W_{ij}\rvert<\Sigma\lvert W_{ij}\rvert=7}\ \iff\ \text{存在重叠}\ ✓\ \big(\text{实测 }\lvert\bigcup W\rvert{=}6✓\big)$$

## §1 ★P0 → P3 全链审计台账（**17 项 ✓／△／✗**）

| # | 关卡 | 状态 | 闭合 | 依据 |
|---|---|---|---|---|
| 1 | $\mathcal S$：$w\in\mathcal S\Rightarrow\lvert\mathrm{own}\rvert{=}3$ | 定义/已确 | ✓ | 定义 |
| 2 | $\lvert W_{ij}\rvert=\lambda_{ij}$ | 全实例确 | ✓ | C-510 |
| 3 | 四正 $\Rightarrow\Sigma\lambda{=}7$ | 已确 | ✓ | C-511 |
| 4 | 四正 $\Rightarrow$ 四槽 $\lambda{=}\{1,2,2,2\}$ | 已确 | ✓ | C-511 |
| 5 | 四正 $\Rightarrow\lambda(ab){=}\lambda(uv){=}1$ | 已确 | ✓ | C-511 |
| 6 | 对角候选 $\Rightarrow\lvert\mathrm{own}\rvert\ge4$ | 机制已得 | **△** | C-514（书面化待） |
| 7 | $W_{11}\cap W_{22}{=}W_{12}\cap W_{21}{=}\varnothing$ | 由 #6 推出 | **△** | C-513/514 |
| 8 | $\lvert E(w)\rvert\le2$（owner-3 witness） | 由 #7 推出 | **△** | C-514 |
| 9 | 两槽重叠必共端点 | 由 #7 推出 | **△** | C-513 |
| 10 | $E(w)$ 多重集 $=(1^5,2^1)$ | 实测刚性 | **△** | C-515 |
| 11 | 四正 $\Rightarrow\exists$ 共端点 overlap | 对当实证 | **✗** | C-513（理论未证） |
| 12 | 共端点 overlap $\Rightarrow$ 四正 | 对当实证 | **✗** | C-513（理论未证） |
| 13 | $w^\ast$ 之 $\lvert\mathrm{own}\rvert{=}3$ | 定义直出 | ✓ | $W\subseteq\mathcal S$ |
| 14 | $w^\ast$ 三种 $R$-型 | census | **✗ 理论** | C-512 |
| 15 | 四正 $\Rightarrow$ 第四 owner | **不可成立** | **✗✓** | C-515（更正一） |
| 16 | 第四 owner $\Rightarrow C\ge4$ | 定义接口 | **△** | 待 $C$ 定义明确 |
| 17 | $C{=}3\Rightarrow\neg1111$ | 未闭合 | **✗** | — |
| 18 | $T_1,T_2$ 完整分类 | census only | **✗** | C-512（降为备用 ✓） |

## §2 ★修订后之门表（**由 3 门 → 2 门 ＋ 1 项重写**）

$$\boxed{\textbf{门 1（P1-A 书面化）}}:\ \text{由\ \textbf{纯距离/支撑}推出}\ w\in D_1\cup D_2\Rightarrow|\mathrm{own}(w)|\ge4\ ✓\ \big(\text{现为 0 反例 ＋ 机制 ✓；书面化未竟 ✗}\big)$$
$$\boxed{\textbf{门 2（结构等价，两向分开）}}:\ \textbf{(2A)}\ \text{共端点 overlap}\Rightarrow\text{四正}\ ✗;\quad \textbf{(2B)}\ \text{四正}\Rightarrow\lvert\bigcup W\rvert{<}\Sigma\lvert W\rvert\ ✗\ \big(\text{= 存在重叠 ✓}\big)$$
$$\boxed{\textbf{门 3（\textbf{重写}}✓\big)}:\ \text{原陈述\ \textbf{不可成立} ✗✓\ ⟹ 须改为\ \textbf{非-witness 侧}之强制量，或\ \textbf{整体放弃} ✗✓\ \text{——\ 否则无法接 }C\ge4\ ✓}$$
$$\qquad\Longrightarrow\ \textbf{（唯一仍闭合之路线 ✓）}:\ \text{类型级有限命题（C-512：四正}\Rightarrow\text{type}\in\{T_1,T_2\}\big)\ ✓\ \text{——\ 亦为}\ \textbf{门 2B 之替代接口}✓$$

## §3 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生 §五（"每点}\le2\ \text{槽}\not\Rightarrow\Sigma\lvert W\rvert\le6"\ ）\ \textbf{完全正确}}✓✓\ \text{——\ 本档以等价形式重述 ✓✓$$
$$\textbf{✓✓✓}:\ \text{唐先生 §九-C1 与 §十三 之\ \textbf{问题意识\ 正确}}✓✓✓\ \text{——\ 唯其\ \textbf{所在层}（witness 侧）不可成立 ✗✓（更正一）}$$
$$\textbf{✓✓}:\ \text{唐先生 §十一（命题 A／B 须分清；最干净形式为 }C{=}3\wedge1111\Rightarrow\bot\big)\ \textbf{成立且应采纳}}✓✓✓\ \text{——\ 本档建议照此书写 ✓$$
$$\textbf{✓✓}:\ \text{唐先生 §七／§八（四正 \iff 共端点 overlap 之两向须分开证）\ \textbf{完全正确}}✓✓\ \text{（门 2A/2B ✓）}$$
$$\textbf{✓✓}:\ \text{唐先生 §十（P2 降为备用）\ \textbf{同意}}✓✓$$

## §4 汇总裁（**✓／△／✗**）

| 项 | 值 |
|---|---|
| 审计项 | 18 |
| ✓ 闭合 | 6（#1–5、13） |
| △ 机制/待书面 | 7（#6–10、16） |
| ✗ 未证 | 4（#11、12、14、17） |
| ✗✓ 不可成立 | 1（#15，门 3） |

## §5 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "全链审计台账" "门表重写" "非witness强制量"
技术词 全链审计台账 命中文件数=1    :: ./WITGATE-2026-09-28-full-chain-audit-ledger-and-two-conclusion-level-corrections.md
技术词 门表重写     命中文件数=1    :: ./WITGATE-2026-09-28-full-chain-audit-ledger-and-two-conclusion-level-corrections.md
技术词 非witness强制量 命中文件数=1    :: ./WITGATE-2026-09-28-full-chain-audit-ledger-and-two-conclusion-level-corrections.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 全链审计台账 | 0 | 0 | ✓（本档新命名 ✓） |
| 门表重写 | 0 | 0 | ✓（本档新命名 ✓） |
| 非witness强制量 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §6 边界（硬 ✓）

- **有限穷举** ✓（引 C-510…C-515 之实测 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 ✓）
- **两项更正（门 3 不可成立 ✗✓；$\Sigma|W|\le6$ 不可作目标 ✗✓）** ＋ **一张 18 项台账** ＋ **修订门表（3→2＋1 重写）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** 门 1／2 已闭合 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
