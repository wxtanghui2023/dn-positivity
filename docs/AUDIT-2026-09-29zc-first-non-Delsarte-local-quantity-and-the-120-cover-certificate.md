# AUDIT-2026-09-29zc —— **首个通过 P-b 的非 Delsarte 局部量** $S_c,S_x$ ＋ **120-cover 证书存盘**

> **性质**：**审计＋最小实验＋证书**——**不占 C 号** ✓；**不作路线裁定** ✗；空间 B ✓
> **时间**：2026-09-29 16:10 ✓

**已查地图**：`AUDIT-29z`（kam.txt 截断）／`AUDIT-29zb`（120-cover 副产品）／三预检 ✓

D0: 本档对象 ＝ **档案已有**（多重度矩／Delsarte—皆经典；证书为新存档文件 ✓）
D1: 0（产出＝**一非 Delsarte 量 ＋ 一证书** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① 恒等式}:\ 2A_2=S_c+S_x,\quad S_c=\sum_{c}\tbinom{s(c)}2,\ S_x=\sum_{x\notin C}\tbinom{\mu(x)}2\ ✓\ (\text{实测全成立})}$$
$$\boxed{\text{② P-b 预检}:\ S_c,S_x\ \textbf{不在}\operatorname{span}\{A_1..A_5,\text{const}\}\ (\text{精确残差}=4.08>0)\ \Longrightarrow\ \textbf{真非 Delsarte}\ ✓✓}$$
$$\boxed{\text{③ 机理}:\ S_c=\text{distance-1 图的\ \textbf{樱桃数}};\ \text{樱桃数不由边数/度序列决定}\ ✓}$$
$$\boxed{\text{④ 证书}:\ \texttt{sources/K10-1-120-cover-CERTIFICATE.txt},\ |C|{=}120,\ \text{覆盖 }1024/1024\ ✓✓}$$

## §1 恒等式（✓ 实测）

$$2A_2=S_c+S_x\qquad(\text{每对距离-2 码字恰 2 公共邻点};\ \text{按码字端/非码字端分裂})$$
$$\text{实测 }12\ \text{码全部成立（例：}S_c{=}34,\ S_x{=}608,\ 2A_2{=}642\ ✓)$$
$$\therefore\ 2A_2\ \text{本身 Delsarte-固定}\ ✓;\ \textbf{但分裂不固定}\ ✓$$

## §2 P-b 预检（✓✓ 关键）

$$\text{精确值（无抽样）};\ \text{最小二乘于 }\{A_1..A_5,1\}:\ \text{残差}=\mathbf{4.08}>0$$
$$\therefore\ \text{由精确数据的线性代数：}\boxed{S_c\notin\operatorname{span}\{A_1..A_5,1\}\ \Longrightarrow\ \textbf{非 Delsarte 量}\ ✓✓}$$
$$\text{机理}:\ \sum_c\tbinom{s(c)}2\ =\ (\text{distance-1 图的樱桃数});\ \text{樱桃数}\notin\sigma(\text{边数})✓$$
$$\textbf{警示}:\ \text{仅排除 }A_1..A_5;\ \text{未排除 }A_1..A_{10}\ (\text{样本数不足})\ ⚠️$$

## §3 120-cover 证书（✓✓ 真实资产）

$$\text{来源}:\ \text{截断的 }118\ \text{词} \to \text{确定性修补} \to |C|{=}\mathbf{120}$$
$$\text{验证}:\ \text{全部 }1024\ \text{点距 }C\le1\ ✓\ \Longrightarrow\ K(10,1)\le120\ \text{可重跑证书}\ ✓✓$$
$$\text{用途（唐先生令）}:\ \text{未来候选的\ \textbf{杀手}——用它实测否证，而非凭想象设计结构}✓$$

## §4 下一步（供唐先生定）

$$\text{问}:\ M{=}106\ \text{是否被迫满足关于 }S_c/S_x\ \text{的约束？（若 }S_x\ \text{须大、}S_c\ \text{须小，而 }2A_2\ \text{固定 ⟹ 可能矛盾）}$$
$$\text{或}:\ \text{用 120-cover 抽更多非 Delsarte 局部关系}✓$$

## §5 边界（硬 ✓）

- **实测（恒等式、12 码精确最小二乘、证书覆盖校验）** ✓；**不占 C 号** ✓
- **不主张** $107$ 可达/不可达 ✗（V290）；$S_c$ 之非 Delsarte 性**仅对 $A_1..A_5$ 已证** ⚠️
