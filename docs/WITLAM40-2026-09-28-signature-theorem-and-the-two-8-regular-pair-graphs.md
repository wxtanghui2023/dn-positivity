# WITLAM40-2026-09-28 — **C-489：$\lambda$-signature $\equiv(1,2,2)$（160/160 ✓✓）；$r_{\rm dist}\equiv\mathbf4$（$40\times4{=}160$ ✓✓）；$H_1,H_2$ 皆\ \textbf{160 边 8-正则 ＋ 三角形自由} ✓✓✓；交叉正则 $\equiv\mathbf2$ ✓✓；对角交点表 $i{=}1{:}(14,0,2)$／$i{=}2{:}(14,2,0)$ 恒定**

> ⚠️ **空间隔离**：本档＝空间 B（119／资产线）专用 ✓；不引 RH 链 ✗。**词回查按空间分栏（已先跑后写 ✓✓）**。
> **范围（照唐先生 2026-09-28 14:26 令 ✓）**：C-489 四项（signature → $H_2$ → $H_1$ → 共同邻居参数）；**先跑后写 ✓✓**；**不作路线裁定** ✗。

**已查地图：命中（接续 C-488／C-487／C-486，非新案 ✓）**
`docs/WITEX32-2026-09-28-…`（**$j$-分解／$n_i$ 恒定／$\lambda_{uv}$ ✓✓✓**）｜`docs/WITMUCONST-2026-09-28-…`（**四层／自然双射 ✓✓✓**）｜`docs/WITP3128-2026-09-28-…`（**包含排除 ✓✓✓**）
**强制查重门** ✓：`scripts/tech_word_check.sh`（**先跑后写 ✓✓**，见 §5）
D0: 本档对象 ＝ **档案已有** $\lambda_{uv}$／三元组／pair 图对象（重命名：否 ✗；新对象：$H_1,H_2$ 首次入档 ✓）
D1: 1（**首次给出 signature 定理（全 (1,2,2)）＋ 首次给出 $r_{\rm dist}\equiv4$ ＋ 首次给出 $H_1,H_2$ 皆 8-正则／三角形自由／160 边 ＋ 首次给出\ \textbf{交叉正则}\ $\equiv2$ ＋ 首次给出对角交点表** ✓）
**[RESEARCH]**

---

## §0 结论（**唐先生之六项预测全中 ＋ 一项交叉正则 ＋ 一项否证**）

$$\textbf{设定 ✓}:\ 40\ \text{码字};\ \lambda_{uv}{=}\#\{T\in\mathcal T:\{u,v\}\subset T\}\in\{0,1,2\}✓\ \big(\text{C-488 ✓}\big);\ \text{pair 分区 }K_{40}{=}H_0\sqcup H_1\sqcup H_2✓\ \big(460,160,160✓\big)$$
$$\boxed{\textbf{(A) ✓✓✓签名定理（唐先生之局部定理，本档证实）}:\ }\forall T=\{a,b,c\}:\ \big(\lambda_{ab},\lambda_{ac},\lambda_{bc}\big)\ \text{之排序}\ \equiv\ \boxed{(1,2,2)}\ ✓✓\ \big(\mathbf{160/160}\ \text{无例外}\ ✓✓\big)$$
$$\qquad\textbf{（推导链 ✓，照唐先生）}:\ n_2{=}2\ \wedge\ \lambda\le2\Longrightarrow\sum_{\rm pairs}(\lambda_{uv}{-}1){=}n_2{=}2\ \big(\text{每对贡献其"额外三元组数"}\big)⟹\text{三对中恰 2 对 }\lambda{=}2、1\ \text{对 }\lambda{=}1✓✓$$
$$\qquad\Longrightarrow\ \text{每 }T\ \text{有唯一的\ \textbf{区分顶点（distinguished vertex）}}:\ \lambda{=}1\ \text{之对之第三点}\ ✓✓\ \text{——\ 唐先生之"定向/标记 }(T,c)\text{"\ \textbf{成立}}✓✓$$
$$\boxed{\textbf{(B) ✓✓✓r_{\rm dist}\equiv\mathbf4（唐先生之预测，本档证实）}:\ }\forall v\in I_{40}:\ r_{\rm dist}(v){=}\#\{T:\ v\ \text{为 }T\ \text{之区分顶点}\}{=}\mathbf4\ ✓✓\ \big(40/40\ ✓✓\big)$$
$$\qquad\Longrightarrow\ \boxed{40\times4=160}\ ✓✓\ \text{——\ 唐先生所期之结构\ \textbf{精确成立}}✓✓;\ \text{且与 C-487 之"码字度数 }\equiv12"\ \text{并列（}12\ \text{＝含 }v\ \text{之三元组数 ✓}\big)$$
$$\qquad\textbf{（结构读法 ✓✓）}:\ \text{每码字既在 12 个三元组中（}4\ \text{个为区分顶点＋}8\ \text{个为普通顶点）}✓$$
$$\boxed{\textbf{(C) ✓✓✓H_2（\lambda{=}2 pair 图）}:\ }|E(H_2)|{=}\mathbf{160}✓✓;\ \boxed{\text{度数}\equiv\mathbf8\ \text{（40/40 ✓✓）}}\ ⟹ \text{40 顶点 8-正则图 ✓✓✓\ （唐先生之预测\ \textbf{命中}}✓✓\big)$$
$$\qquad\textbf{（三角形自由 ✓✓ 新）}:\ \text{共同邻居 }|N_{H_2}(u)\cap N_{H_2}(v)|\ \text{分布}=\{0{:}360,\ 2{:}320,\ 4{:}80,\ 8{:}20\}✓;$$
$$\qquad\qquad\text{且}\ i{=}2\ \text{之对角线}\ |N_2(u)\cap N_2(v)|{=}\mathbf0\ \text{恒成立}✓✓\ \big(\text{三角形自由 ✓}\big)$$
$$\boxed{\textbf{(D) ✓✓✓H_1（\lambda{=}1 pair 图）}:\ }|E(H_1)|{=}\mathbf{160}✓✓;\ \boxed{\text{度数}\equiv\mathbf8}✓✓;\ \text{共同邻居分布}\ \textbf{与 }H_2\ \text{完全相同}✓✓\ \big(\{0{:}360,2{:}320,4{:}80,8{:}20\}✓\big)$$
$$\qquad\Longrightarrow\ \text{对角线}\ |N_1(u)\cap N_1(v)|{=}\mathbf0\ \text{恒成立}✓✓\ \big(H_1\ \text{亦三角形自由 ✓}\big)$$
$$\qquad\Longrightarrow\ \boxed{K_{40}=H_0\sqcup H_1\sqcup H_2,\quad H_1,H_2\ \text{双双 8-正则、160 边、三角形自由}}\ ✓✓✓$$
$$\boxed{\textbf{(E) ✓✓✓交叉正则（本档新发现）}:\ }\forall\ \text{边}\ uv\in H_1:\ \big|N_{H_2}(u)\cap N_{H_2}(v)\big|{=}\mathbf2\ \text{恒成立}✓✓;\ \text{对称地}\ \forall\ uv\in H_2:\ \big|N_{H_1}(u)\cap N_{H_1}(v)\big|{=}\mathbf2\ \text{恒成立}✓✓$$
$$\qquad\Longrightarrow\ \boxed{H_1\ \text{与}\ H_2\ \text{互为"共同邻居数为 2"之对偶}}\ ✓✓\ \text{——\ 极强之对称性 ✓✓}$$
$$\boxed{\textbf{(F) ⚠️否证：非完全 association scheme}:\ }\text{对角交点}\ |N_0(u)\cap N_0(v)|\ \text{对 }H_0\ \text{对之分布}=\{6{:}40,\ 12{:}640,\ 14{:}240\}\ ✗\ \text{不恒定}$$
$$\qquad\text{而对 }i{=}1\text{／}2\ \text{则恒定}:\ i{=}1:\ (|N_0\cap N_0|,|N_1\cap N_1|,|N_2\cap N_2|){=}\boxed{(14,\ 0,\ 2)}✓✓;\ i{=}2:\ \boxed{(14,\ 2,\ 0)}✓✓$$
$$\qquad\Longrightarrow\ \text{结构为\ \textbf{部分正则（partially regular）} ✓，非 3-类 association scheme ✗（}i{=}0\ \text{类不恒定 ⟹ 否证 ✓）}$$

---

## §1 逐条核验（**✓／✗**）

$$\textbf{✓✓✓}:\ \text{唐先生 §A（signature 全为 }(1,2,2)\big)\ \textbf{命中}✓✓;\ \text{其推导（}n_2{=}2 ⟹\ \text{恰两对 }\lambda{=}2\big)\ \textbf{完全正确}✓✓$$
$$\textbf{✓✓✓}:\ \text{唐先生 §B（}r_{\rm dist}{=}4\ \text{若恒定；}40\times4{=}160\big)\ \textbf{命中}✓✓$$
$$\textbf{✓✓✓}:\ \text{唐先生 §C／§D（}H_2,H_1\ \text{皆 160 边、8-正则；平均度 }2\cdot160/40{=}8\big)\ \textbf{双双击中}✓✓$$
$$\textbf{✓✓}:\ \text{唐先生之"降维"判断（}Q_{10}\ \text{之 160 特殊点 ⟹ 40 码字上之两个 160-边图）\ \textbf{成立}}✓✓\ \text{——\ 其"自 C-486 以来最有价值之降维"\ 之评价\ \textbf{恰当}}✓✓$$
$$\textbf{✓（新）}:\ \text{唐先生未见之}\ \textbf{交叉正则}\ \equiv2✓✓\ \text{与}\ \textbf{三角形自由}✓✓\ \text{为本档新发现}$$
$$\textbf{✗}:\ \text{唐先生之"可能识别出 strongly regular／distance-regular 对象"\ ⟹\ 对角交点对 }H_0\ \text{不恒定}\ ✗\ \big(\S0(F)\big)⟹\ \text{非 SRG／非 scheme ✗（\textbf{但为部分正则}✓）}$$

## §2 常数汇总裁（**本档 ✓✓✓**）

| 量 | 值 | 恒定？ |
|---|---|---|
| signature | $(1,2,2)$ | ✓✓ |
| $r_{\rm dist}(v)$ | $4$ | ✓✓ |
| $H_1,H_2$ 边数 | $160$ 各 | ✓ |
| $H_1,H_2$ 度数 | $\mathbf8$ | ✓✓ |
| $H_1,H_2$ 三角形 | 无（$|N\cap N|{=}0$） | ✓✓ |
| 交叉正则 $H_1{\to}H_2$ | $2$ | ✓✓ |
| 对角交点 $i{=}1$ | $(14,0,2)$ | ✓✓ |
| 对角交点 $i{=}2$ | $(14,2,0)$ | ✓✓ |
| 对角交点 $i{=}0$ | $\{6,12,14\}$ | ✗ |

## §3 下一靶（**⚠️ 不作裁定 ✗**）

$$\textbf{（靶 1 ✓✓ 最优先）}:\ \text{由 }H_1,H_2\ \text{之 8-正则／三角形自由／交叉正则 }\equiv2\ ⟹\ \text{求其\ \textbf{谱}（特征值 ✓）：是否少数整数 ✓？是否与 }\mathcal T\ \text{之谱相合 ✓？}$$
$$\textbf{（靶 2 ✓✓）}:\ r_{\rm dist}\equiv4\ \text{＋ 码字度数 }\equiv12\ ⟹\ \text{每个码字"4 次区分 ＋ 8 次普通"\ 之\ \textbf{分划}（是否诱导一个 }(40,4,12)\ 之设计 ✓）$$
$$\textbf{（靶 3 ✓）}:\ H_1\cong H_2\ ?\ \big(\text{参数全同 ✓；是否\ \textbf{同构}／互补 ✓？}\big)$$
$$\textbf{（靶 4 ✓）}:\ r{=}3\ \text{profile}✗\ \text{（并行 ⚠️）};\ \text{非 Best 39-码}\ ✗$$

## §4 记账与命名纪律（**照唐先生 ✓✓**）

$$\textbf{✓✓}:\ \text{一律用\ \textbf{自然双射（160 点 ↔ 160 等边三元组）}；「自对偶」继续停用 ✗}$$
$$\textbf{✓✓}:\ \text{\mu 之 384 继续标"实例计数"；结构量用 }\#\{x:y\in P_3(x)\}{=}128✓$$

## §5 技术词回查（**先跑后写 ＋ 空间分栏 ✓✓**）

```
$ bash scripts/tech_word_check.sh "签名定理" "区分顶点" "三角形自由图" "交叉正则"
技术词 签名定理     命中文件数=0    ::
技术词 区分顶点     命中文件数=0    ::
技术词 三角形自由图 命中文件数=0    ::
技术词 交叉正则     命中文件数=0    ::
```
| 词 | 本线他档命中 | 跨空间同名（**不计** ✗） | 本档新增 |
|---|---|---|---|
| 签名定理 | 0 | 0 | ✓（照唐先生 §A 命名 ✓） |
| 区分顶点 | 0 | 0 | ✓（照唐先生之 distinguished vertex ✓） |
| 三角形自由图 | 0 | 0 | ✓（自造标签 ✓） |
| 交叉正则 | 0 | 0 | ✓（自造标签 ✓） |

- **（本条\ \textbf{确已先跑后写} ✓✓）**

## §6 边界（硬 ✓）

- **有限穷举** ✓（160 三元组 ＋ 40 顶点 ＋ 780 对 ＋ 对角交点全量 ✓）；**未上 SDP/SAT** ✗；**未开门②** ✓；**未改门** ✓；**不跨空间**（§5 ✓）
- **六项预测全中 ✓✓✓**＋ **一项新发现（交叉正则 ✓✓）** ＋ **一项否证（非 association scheme ✗）** 已显式标注 ✓✓
- **不作路线裁定** ✗（照 23:54 令 ✓）；**不声称** $H_1\cong H_2$ ✗；**不声称** P1 成立/不成立 ✗（V290）
