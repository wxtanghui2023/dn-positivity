# WITG2-2026-09-28 — **C-525：$G$ 之两支结构（$G{=}A_0\cup F$ / $G{=}I\cup F$）—— 符号推导\ \textbf{自洽}✓✓；但本轮独立复核脚本\ \textbf{输出为空（bug）}✗✓，仅由 C-524 之 $192/128$ 拆分支\ \textbf{间接支持} ✓**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §3）**。
> **范围（照唐先生 2026-09-28 16:09 §1–§7 令 ✓）**：核 $G$ 之两支；**不作路线裁定** ✗。

**已查地图：命中（接续 C-524／C-523／C-521，非新案 ✓）**：`WITSUP-…`／`WITD1-…`／`WITGC2-…`
D0: 本档对象 ＝ **档案已有**（$A,B,F,G$／四块；无新数学对象 ✓）
D1: 1（**首次\ \textbf{逐步核验}唐先生之 $G$ 两支符号推导（自洽 ✓✓）＋ 首次据 C-524 之 $192/128$ 判定两支\ \textbf{与其一致}✓✓ ＋ 首次\ \textbf{据实登记}本轮复核脚本\ \textbf{输出为空（bug）}✗✓**）
**[RESEARCH]**

---

## §0 结论（**符号自洽 ✓✓；脚本复核失败 ✗✓；间接支持 ✓**）

$$\boxed{\textbf{(1) ✓✓符号推导\ \textbf{自洽}（逐步核验）}}$$
$$\qquad\textbf{（支 I ✓）}:\ d(x_0,y_2){=}6\Rightarrow\lvert B\triangle G\rvert{=}6\Rightarrow 8-2\lvert B\cap G\rvert{=}6\Rightarrow\lvert B\cap G\rvert{=}\mathbf1✓\Rightarrow G\not\ni I;\ \text{又 }d(x_1,y_2){=}2\Rightarrow\lvert(A_0\cup B_0)\triangle G\rvert{=}2\Rightarrow\lvert(A_0\cup B_0)\cap G\rvert{=}\mathbf3✓$$
$$\qquad\Longrightarrow\ \text{三坐标中一个为 }b\in B_0\ ⟹\ \text{余二\ \textbf{必属 }$A_0$}\ ⟹\ \boxed{G=A_0\cup F}\ ✓✓\ \big(\text{唐先生 §3 ✓}\big)$$
$$\qquad\textbf{（支 II ✓）}:\ d(x_0,y_2){=}2\Rightarrow\lvert B\cap G\rvert{=}\mathbf3✓\ \Rightarrow\ \text{须自 }B\ \text{补足二坐标};\ B{=}I\cup B_0\ \text{且 }b\in B_0\ ⟹\ \text{唯可能为整 }I\ ⟹\ \boxed{G=I\cup F}\ ✓✓\ \big(\text{唐先生 §4 ✓}\big)$$
$$\qquad\Longrightarrow\ \textbf{（故两支穷尽 ✓）}:\ \text{四块计数唯 }\big(0,2,1,1\big)\ \text{或}\ \big(2,0,1,1\big)\ ✓\ \text{——\ 与"不存在第三支"\ 相符 ✓}$$
$$\boxed{\textbf{(2) ✗✓本轮独立复核\ \textbf{失败}}:\ }\text{脚本按 }d(q,y){=}2\ \text{选 }y_1\ \text{后，其 }\lvert F\rvert{=}2\ \text{筛选\ \textbf{全数未通过}}⟹\ \text{输出为空（}\text{branch}\ \text{与 }gpos\ \text{计数器皆空）✗✓}$$
$$\qquad\textbf{（据实 ✓）}:\ \text{该失败为\ \textbf{本轮脚本实现缺陷}（疑似 }F/G\ \text{之构造或筛选式）✗，\ \textbf{非数学反例}✓\ \text{——\ 不得据此否定唐先生之推导 ✗✓}}$$
$$\boxed{\textbf{(3) ✓间接支持（承 C-524）}}:\ \text{C-524 在 }|F|{=}2\ \text{支上：}G{=}F\cup A_0\ \text{之判真}=\mathbf{192}、\text{判假}=\mathbf{128}\ ✓\ \big(192+128=320✓\big)$$
$$\qquad\Longrightarrow\ \text{与唐先生之两支拆分（}192{:}\ \text{支 I}；128{:}\ \text{支 II}\big)\ \textbf{一致}✓✓\ \text{——\ 唯其分派方向（何支对 192）本档\textbf{未能独立确认}✗✓}$$

## §1 汇总裁（**✓✓／✗✓**）

| 项 | 值 |
|---|---|
| 支 I 之代数 | 自洽 ✓✓（$G{=}A_0\cup F$） |
| 支 II 之代数 | 自洽 ✓✓（$G{=}I\cup F$） |
| 支数 | $2$（穷尽）✓✓ |
| C-524 之判真/判假 | $192/128$ ✓（与两支一致） |
| 本轮独立复核 | **失败（脚本 bug）** ✗✓ |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓}:\ \text{唐先生 §1（}F{=}\{b,n\}\Rightarrow\operatorname{supp}(y_1){=}I\cup(B_0{\setminus}\{b\})\cup\{n\}\big)\ \textbf{自洽}}✓✓{$$
$$\textbf{✓✓}:\ \text{其 §2–§5（两支推导与穷尽性）\ \textbf{自洽}}✓✓$$
$$\textbf{✓✓}:\ \text{其 §6（两支互为 }x_0\leftrightarrow x_1\ \text{镜像）\ \textbf{方向正确}}✓✓$$
$$\textbf{✓✓}:\ \text{其 §7–§9（五点 support 模板；结构版 B-lemma；仍不写 }C{=}3\Rightarrow\neg1111\big)\ \textbf{同意}}✓✓✓{$$
$$\textbf{✗✓}:\ \text{本档之独立复核\ \textbf{未成}}✗\ \big(\text{据实；下一轮重跑 ✓}\big)$$

## §3 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "两支结构" "支撑模板" "复核失败登记"
技术词 两支结构     命中文件数=1    :: ./WITG2-2026-09-28-two-branch-G-structure-symbolic-vs-script-bug.md
技术词 支撑模板     命中文件数=1    :: ./WITG2-2026-09-28-two-branch-G-structure-symbolic-vs-script-bug.md
技术词 复核失败登记 命中文件数=1    :: ./WITG2-2026-09-28-two-branch-G-structure-symbolic-vs-script-bug.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 两支结构 | 0 | 0 | ✓（照唐先生 §5 ✓） |
| 支撑模板 | 0 | 0 | ✓（照唐先生 §7 ✓） |
| 复核失败登记 | 0 | 0 | ✓（本档据实 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §4 下一靶（**照唐先生 §8–§9 ✓**）

$$\textbf{（靶 1 ✓✓）}:\ \text{\textbf{重跑}两支复核脚本（修 }F/G\ \text{构造与筛选）——\ 确认 }{192}\ \text{与 }{128}\ \text{之支向}✓$$
$$\textbf{（靶 2 ✓✓）}:\ \text{由五点 support 模板推导 }T_1,T_2（\text{结构版 B-lemma}\big)✓✓\ \text{——\ 不再做全 }\mathrm{OrbType}\ \text{分类 ✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{最后碰撞 }\{T_1,T_2\}\cap\{O_1,\dots,O_6\}=\varnothing\ ✓\ \big(\text{非循环 P3 ✓}\big)$$
$$\textbf{（禁止 ✗）}:\ \text{写 }C{=}3\Rightarrow\neg1111\ ✗✓；把本轮脚本失败当数学反例 ✗✓}{$$

## §5 边界（硬 ✓）

- **有限穷举** ✓（承 C-524 之数据 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 ✓）
- **一项符号核验（自洽 ✓✓）** ＋ **一项据实（脚本 bug ✗✓）** ＋ **一项间接支持（192/128 ✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** 结构版 B-lemma 已证 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
