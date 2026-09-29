# RESULT-d（2026-09-29）—— **fiber 净收益公式 $\tfrac{(j-1)(j+2)}2$ 实测成立 ✓✓；我的"修正"被推翻并撤回** ✗

> **性质**：**问题特化续（含自查纠错）**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 19:15 ✓

**已查地图**：`RESULT-c`（两来源恒等式）／`RESULT-b`（母式）／`RESULT`（$[47,59]$）✓

D0: 本档对象 ＝ **档案已有**（双重计数／纤维—经典 ✓）
D1: 0（产出＝**一公式获证 ＋ 我一处错误撤回 ＋ 一数据** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✗ 我的"修正"被推翻}:\ \sum(2r_x-1)\ \text{仅 }32/50\ \text{成立（有反例）}}$$
$$\boxed{\text{② ✓✓ 唐先生原式成立}:\ \sum_{x\in L}\tfrac{(r_x-1)(r_x+2)}2\ \text{—— }50/50\ ✓\ (\text{我撤回修正})}$$
$$\boxed{\text{③ 我之错因}:\ \text{把 }T\text{-成本写成 }\tbinom{r_x-1}2;\ \text{但 }x\in L\Rightarrow\mu_A(x)-1=r_x\Rightarrow\text{成本}=\tbinom{r_x}2}$$
$$\boxed{\text{④ ✓ 定义滑动之提醒仍有效}:\ \S2\ \text{用距离-1 私有};\ \text{上轮 }N_1^*\ \text{用 }B_2\ \text{私有}\ ——\ \text{须固定}}$$
$$\boxed{\text{⑤ 数据}:\ a{=}53\Rightarrow|P|{=}27,|Q|{=}26,F(A)=\mathbf{78}>71\ (\text{纤维上限})\ ✓}$$

## §1 实测（✓ 双向对照）

| 版本 | 50 样本中成立 |
|---|---|
| $\sum_{x\in L}\max(0,2r_x-1)$（我提出） | $\mathbf{32/50}$ ✗（反例：$a{=}50$ 时 $F-F(P){=}75<81$） |
| $\sum_{x\in L}\tfrac{(r_x-1)(r_x+2)}2$（唐先生） | $\mathbf{50/50}$ ✓✓ |

$$\therefore\ \boxed{\text{§7 公式成立；我方修正作废}}✓$$

## §2 我之错误定位（✓ 诚实记录）

$$\text{我写}:\ \Delta T_L=\sum\tbinom{r_x-1}2\ ✗\qquad\text{正确}:\ \Delta T_L=\sum\tbinom{r_x}2$$
$$\because\ T(A)\ \text{中 }x\ \text{之项}=\tbinom{\mu_A(x)-1}2=\tbinom{(\mu_P(x)+r_x)-1}2=\tbinom{1+r_x-1}2=\tbinom{r_x}2\ ✓$$
$$\therefore\ \text{净收益}=\underbrace{2r_x}_{2E_{PQ}}+\underbrace{\tbinom{r_x}2\cdot 2-\tbinom{r_x}2}_{\text{待精化}}\ \text{—— 唐先生之合并式经实测无误}$$

## §3 数据（✓ 有约束力）

$$62\text{-码之 }53\text{-子集}:\ |P|{=}27,|Q|{=}26,\ F(A)=78,\quad\text{上限 }9a-406=71\ \Longrightarrow\ 78>71\ ✓$$
$$\therefore\ \boxed{\text{真实稠密子集之 }F\ \text{天然超上限}\ ⟹\ \text{纤维条件\ \textbf{有约束力}}✓\ (\text{启示性})}$$

## §4 下一目标（不变）

$$\boxed{\text{证}:\ F(A)=2(A_1+A_2)-T\ >\ 9a-406\ \text{对某 }a\ \text{必成立，或互补对上总有一侧成立}}$$
$$\text{工具}:\ \text{唐先生之 fiber 净收益式（已实测）};\quad \text{待补}:\ |L|\ \text{或 fiber-weight 之统一下界}$$

## §5 边界（硬 ✓）

- **双向实测（$32/50$ vs $50/50$）** ✓；**我方错误已如实记录并撤回** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）
