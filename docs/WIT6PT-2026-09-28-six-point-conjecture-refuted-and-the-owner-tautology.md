# WIT6PT-2026-09-28 — **C-531：✗✓"六点锁定"猜想\ \textbf{否证}（$\lvert C_{ij}\cap B\rvert\le1$；且 $c,z$ 为码字索引、距 $\ge4$，不可能属 $C_{ij}$）✓✓ 而\ \textbf{真正机制}为\ \textbf{点态 owner 排除}（$C_{ij}$ 中每点 owner$\ge4$）**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓。**词回查为写后补跑（据实记录 ⚠️，见 §4）**。
> **范围（照唐先生 2026-09-28 17:03 §3–§7 令 ✓）**：核六点锁定猜想；**不作路线裁定** ✗。

**已查地图：命中（接续 C-530／C-509／C-519，非新案 ✓）**：`WIT4TH-…`／`WITDOSSIER-…`／`WITGB-…`
D0: 本档对象 ＝ **档案已有**（$C_{ij}$/$B$/owner；无新数学对象 ✓）
D1: 1（**首次判定六点锁定猜想 $C_{ij}{=}B\cup\{c,z\}$ \textbf{为假}（$\lvert C\cap B\rvert\le1$）✗✓ ＋ 首次指出 $c,z$ 系码字索引、距 $\ge4$ ⟹ 几何上不可能属 $C_{ij}$✗✓ ＋ 首次\ \textbf{澄清}本档 owner-型为\ \textbf{恒等式}（$w\in C_{ij}\Rightarrow i,j\in\mathrm{own}(w)$ 按定义 ✓）⟹ 真正的信息在\ \textbf{大小}（$\ge4$，非 3）✓✓**）
**[RESEARCH]**

---

## §0 ★结论（**猜想否证 ✗✓；机制为点态 owner ✓✓**）

$$\textbf{设定 ✓}:\ \text{三正实例之第四槽 }(i,j);\ C_{ij}{:=}N_2(I_i)\cap N_2(I_j)\ (\lvert C\rvert{=}6\text{ 之 960 例});\ B{:=}N_2(x)\cap N_2(p)\cap N_2(q)\ ✓$$
$$\boxed{\textbf{(1) ✗✓六点锁定猜想\ \textbf{为假}}}:\ \lvert C_{ij}\cap B\rvert=\mathbf1\ (640)\ \text{或}\ \mathbf0\ (320)\ ✓✓\ \text{——\ }\textbf{非 }B\cup\{c,z\}✗✓$$
$$\qquad\textbf{（几何反证 ✓✓）}:\ c,z\ \text{系\ \textbf{码字索引}（}I_c,I_z\big);\ \text{码字间距离 }\ge4\ ✗\ \text{——\ 而 }C_{ij}\ \text{要求距恰 }2\ ✓\ ⟹\ I_c,I_z\notin C_{ij}\ \textbf{必}✗✓$$
$$\qquad\textbf{（另记 ✓）}:\ C\ \text{不含 }x,y\ (0/960)\ ✓$$
$$\boxed{\textbf{(2) ✓✓真正机制 ＝ 点态 owner 排除}}:\ \forall w\in C_{ij}:\ \lvert\mathrm{own}(w)\rvert\in\{4,5\}\ ✓✓\ \big(\text{型 }\{4{:}4,5{:}2\}\ ✓\big)$$
$$\qquad\textbf{（读法 ✓✓✓）}:\ \text{与 }(I_i,I_j)\ \text{同时距 2 之点，}\textbf{必亦与另外 }\ge2\ \text{个码字距 2}\ ✓✓\ \text{——\ \textbf{无一点恰 3 个}}✗✓$$
$$\qquad\Longrightarrow\ \boxed{C_{ij}\cap\mathcal S=\varnothing}\ ✓✓\ \text{——\ 纯点态（非计数 ✓）、且\ \textbf{不引用 }$F,G,\Sigma\lambda,\lVert T\rVert_1,\mathrm{OrbType}{\to}\lambda$\ ✓✓（绕开 C-528 之循环警告 ✓✓）}$$
$$\boxed{\textbf{(3) ⚠️据实澄清（防误记）}}:\ w\in C_{ij}\Rightarrow i,j\in\mathrm{own}(w)\ \text{系\ \textbf{按定义}（}C_{ij}\ \text{定义 ⟹ 距 2 ✓）——\ \textbf{非新信息}✗✓}$$
$$\qquad\Longrightarrow\ \text{故本档之}\ \text{"owner-型 }(4,(0,0,1,1))\ \text{／}(5,(0,0,0,1,1))\text{"}\ \text{须读作\ \textbf{大小信息}}\ ✓\ \text{（}\ge4\big),\ \text{而非位置信息 ✗✓}$$

## §1 汇总裁（**✗✓／✓✓**）

| 项 | 值 |
|---|---|
| $\lvert C\cap B\rvert$ | $\le1$ ✗✓（非 $B\cup\{c,z\}$） |
| $c,z\in C$ ? | **不可能**（码字距 $\ge4$）✗✓ |
| $C$ 含 $x,y$ | 否（$0/960$）✓ |
| $C$ 之 owner-大小 | 恒 $\{4{:}4,5{:}2\}$ ✓✓ |
| 是否恰 3 | **从不**（$0/960$）✓✓ |

## §2 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §1 之 (G) 形式（}C_{ij}{=}\varnothing\ \text{或 }\forall c:\ \mathrm{own}(c)\ge4\big)\ \textbf{成立且正确}}✓✓✓{$$
$$\textbf{✗✓}:\ \text{其 §3／§7 之"六点锁定 }C_{ij}{=}B\cup\{c,z\}"\ ⟹ \textbf{为假}✗✓\ \text{（本档 (1)）}$$
$$\textbf{✓✓}:\ \text{其 §5–§6（"若成立则闭环；并解释 4-way"\ ）\ \textbf{推理正确}}✓✓\ \text{——\ 唯前提\ \textbf{不成立}✗✓}$$
$$\textbf{✓✓✓}:\ \text{其 §8（须区分 }C_{ij}\ \text{与 }W_{ij}\ \text{两层）\ \textbf{完全正确且关键}}✓✓✓$$
$$\textbf{✓✓}:\ \text{其 §6 之机制表述（"前三槽把外部几何锁到六点候选集，而这六点全落高-owner 层"\ ）\ \textbf{正确}}✓✓✓\ \text{——\ 唯该六点\ \textbf{非 }B\ ✗✓}$$

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓✓）}:\ \text{把 (G) 写为\ \textbf{结构命题}}:\ \text{"}w\ \text{与 }I_i,I_j\ \text{同时距 2}⟹\ \lvert\mathrm{own}(w)\rvert\ge4\text{"}\ ✓✓\ \text{——\ 纯\ \textbf{码字-邻域}层 ✓✓}$$
$$\textbf{（靶 2 ✓✓）}:\ \text{查该六点之\ \textbf{真实 owner 集}（4-owner 与 5-owner 之形态）——\ 是否含固定码字（如索引 25 频现 ✓）✓✓}$$
$$\textbf{（靶 3 ✓）}:\ \text{重跑两支复核（修 C-525 脚本 bug）✓}$$
$$\textbf{（禁止 ✗）}:\ \text{再用 }B\cup\{c,z\}\ ✗✓；纯计数 ✗✓；由 }F,G\ \text{反推 ✗✓}{$$

## §4 技术词回查（**写后补跑 ⚠️ 据实；空间分栏 ✓**）

```
$ bash scripts/tech_word_check.sh "六点锁定" "点态owner排除" "码字邻域层"
技术词 六点锁定     命中文件数=1    :: ./WIT6PT-2026-09-28-six-point-conjecture-refuted-and-the-owner-tautology.md
技术词 点态owner排除 命中文件数=1    :: ./WIT6PT-2026-09-28-six-point-conjecture-refuted-and-the-owner-tautology.md
技术词 码字邻域层  命中文件数=1    :: ./WIT6PT-2026-09-28-six-point-conjecture-refuted-and-the-owner-tautology.md
```

| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 六点锁定 | 0 | 0 | ✓（照唐先生 §7 ✓） |
| 点态owner排除 | 0 | 0 | ✓（本档新命名 ✓） |
| 码字邻域层 | 0 | 0 | ✓（本档新命名 ✓） |

- **（本条为\ \textbf{写后补跑} ⚠️——据实记录 ✓）**

## §5 边界（硬 ✓）

- **有限穷举** ✓（960 例之 $C_{ij}$／$B$／owner 全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§4 ✓）
- **一项✗✓否证（六点猜想）** ＋ **一项✓✓（点态机制）** ＋ **一项⚠️据实（owner-位置为定义式）** 已显式标注 ✓✓
- **不作路线裁定** ✗；**不声称** (G) 之结构证明已完成 ✗；**明确否认** $C{=}3\Rightarrow\neg1111$ 已证 ✗（V290）；**明确否认** $128{=}145{-}17$ 已证 ✗（V290）
