# WITSUP-2026-09-28 — **C-524：$F$-位置断言\textbf{证实}（恰 $(0,0,1,1)$）✓✓；但 $G{=}F\cup A_0$ \textbf{只对 192/640} ✗✓（据实）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §3）**。
> **范围（照唐先生 2026-09-28 16:07 §1–§5 令 ✓）**：核**联合支撑引理**之两项坐标断言；**不作路线裁定** ✗。

**已查地图：命中（接续 C-523／C-522／C-521，非新案 ✓）**：`WITD1-…`／`WITGC3-…`／`WITGC2-…`
D0: 本档对象 ＝ **档案已有**（$A$/$B$/$F$/$G$／支撑；无新数学对象 ✓）
D1: 1（**首次确认 $F$ 之四块位置恰 $(0,0,1,1)$（$|F|{=}2$ 规范下）✓✓ ＋ 首次判定 $G{=}F\cup A_0$ \textbf{只对 }$192/640$（\textbf{非全} ✗✓）＋ 首次得 $(|F|,|G|)\in\{(2,4),(4,2)\}$ 镜像各 $320$**）
**[RESEARCH]**

---

## §0 ★结论（**一项证实 ✓✓ ＋ 一项部分否定 ✗✓**）

$$\textbf{设定 ✓}:\ x_0{\mapsto}0;\ A{=}\mathrm{supp}(x_0\oplus x_1);\ B{=}\mathrm{supp}(x_0\oplus q);\ F{=}\mathrm{supp}(q\oplus y_1);\ G{=}\mathrm{supp}(q\oplus y_2)✓$$
$$\boxed{\textbf{(1) ✓✓$A,B$ 骨架与 C-523 一致}}:\ (\lvert A\rvert,\lvert B\rvert,\lvert A\cap B\rvert)=(4,4,2)\ \text{于\ \textbf{全部 }640}\ ✓✓$$
$$\boxed{\textbf{(2) ✓✓★$F$-位置断言\ \textbf{证实}}:\ }\text{在 }|F|{=}2\ \text{之规范（即取 }d(q,y_1){=}2\ \text{者）下}:$$
$$\qquad\big(\lvert F\cap I\rvert,\lvert F\cap A_0\rvert,\lvert F\cap B_0\rvert,\lvert F\cap N\rvert\big)=\mathbf{(0,0,1,1)}\ ✓✓\ \big(320/320✓✓\big)$$
$$\qquad\Longrightarrow\ \boxed{F=\{b,n\},\ b\in B_0,\ n\in N}\ ✓✓\ \text{——\ \textbf{唐先生 §3 之断言完全成立}}✓✓✓$$
$$\boxed{\textbf{(3) ✗✓$G{=}F\cup A_0$\ \textbf{只对部分}}}:\ \text{实测 True}:\mathbf{192}\ /\ 640;\ \text{False}:448\ ✗✓\ \text{——\ \textbf{非全成立}}✗✓$$
$$\qquad\textbf{（镜像结构 ✓）}:\ (\lvert F\rvert,\lvert G\rvert)\in\{(2,4)\ (\text{含 }F\subseteq G),\ (4,2)\}\ \text{各 }320\ ✓\ \big(\text{即 }y_1\leftrightarrow y_2\ \text{镜像}\big)$$
$$\qquad\Longrightarrow\ \text{唐先生 §4 之 }G{=}F\cup A_0\ \text{须\ \textbf{附加条件}（本档之混合口径下仅 }192\ \text{例成立）✗✓}\ \text{——\ 据实标注 ✓}$$
$$\qquad\textbf{（另记 ✓）}:\ F\ \text{之四块位置另见 }(2,0,1,1)\ (192)\ \text{与}\ (0,2,1,1)\ (128)\ \text{——\ 皆属 }|F|{=}4\ \text{之镜像支（当取另一 }y\text{）✓}$$

## §1 汇总裁（**✓✓／✗✓**）

| 项 | 值 |
|---|---|
| $\lvert A\rvert,\lvert B\rvert,\lvert A\cap B\rvert$ | 恒 $(4,4,2)$ ✓✓ |
| $F$ 位置（$\lvert F\rvert{=}2$ 规范） | 恒 $\mathbf{(0,0,1,1)}$ ✓✓✓ |
| $F{=}\{b,n\}$，$b\in B_0,n\in N$ | **成立** ✓✓ |
| $G{=}F\cup A_0$ | 仅 $192/640$ ✗✓ |
| 镜像 | $(2,4)/(4,2)$ 各 320 ✓ |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §1（四块分解 }I,A_0,B_0,N\text{，各 }2\big)\ \textbf{成立}}✓✓{$$
$$\textbf{✓✓✓}:\ \text{其 §2（}\lvert F\rvert{=}2,\ \lvert G\rvert{=}4,\ \lvert F\triangle G\rvert{=}2\Rightarrow F\subset G\big)\ \textbf{成立}}✓✓\ \big(\text{在 }|F|{=}2\ \text{支}\big){$$
$$\textbf{✓✓✓}:\ \text{其 §3（}F{=}\{b,n\}\ \text{之精确位置}\big)\ \textbf{完全成立}}✓✓✓\ \big(320/320✓\big){$$
$$\textbf{✗✓}:\ \text{其 §4（}G{=}F\cup A_0\big)\ ⟹ \textbf{仅 }192/640\text{ 成立} ✗✓\ \text{（须附加条件或换规范）}$$
$$\textbf{✓✓}:\ \text{其 §6（}F\ \text{模坐标稳定子唯一；}2{\times}2\ \text{实现同构}\big)\ \textbf{成立}}✓✓{$$
$$\textbf{✓✓}:\ \text{其 §7–§9（联合支撑 → 结构版 B-lemma；仍不写 }C{=}3\Rightarrow\neg1111\big)\ \textbf{同意}}✓✓✓{$$

## §3 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "四块坐标分解" "嵌套支撑" "联合支撑引理"
技术词 四块坐标分解 命中文件数=1    :: ./WITSUP-2026-09-28-F-position-confirmed-G-claim-only-partial.md
技术词 嵌套支撑     命中文件数=1    :: ./WITSUP-2026-09-28-F-position-confirmed-G-claim-only-partial.md
技术词 联合支撑引理 命中文件数=1    :: ./WITSUP-2026-09-28-F-position-confirmed-G-claim-only-partial.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 四块坐标分解 | 0 | 0 | ✓（照唐先生 §1 ✓） |
| 嵌套支撑 | 0 | 0 | ✓（照唐先生 §2 ✓） |
| 联合支撑引理 | 0 | 0 | ✓（照唐先生 §8 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §4 下一靶（**照唐先生 §9 ✓，据实修正**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{在 }|F|{=}2\ \text{规范下}\ F{=}\{b,n\}\ \text{已\ \textbf{确证}}✓✓\ ⟹\ \text{可作结构引理之坐标基点 ✓✓}$$
$$\textbf{（靶 2 ✗✓）}:\ G\ \text{之定位须\ \textbf{重做}}（G{=}F\cup A_0\ \text{仅 }192/640\big)\ \text{——\ 建议：先固定 }|F|{=}2\ \text{支，再逐块求 }G\ \text{之四块位置 ✓✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{由 }(F,G)\ \text{模板推 }T_1,T_2（\text{结构版 B-lemma}\big)✓✓$$
$$\textbf{（禁止 ✗）}:\ \text{新 census ✗✓；把 }192/640\ \text{当全成立 ✗✓；owner-计数容量 ✗✓}$$

## §5 边界（硬 ✓）

- **有限穷举** ✓（640 实例之支撑分解 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§3 ✓）
- **一项证实（$F{=}\{b,n\}$ ✓✓✓）** ＋ **一项部分否定（$G{=}F\cup A_0$ 仅 192 ✗✓）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** 结构版 B-lemma 已证 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
