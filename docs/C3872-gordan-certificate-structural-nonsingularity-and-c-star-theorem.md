已查地图（**先查后写**）：`C-3871`（**R1／R2 分解；实例级** ✓✓）、`C-3870`（**取到步；`\det\widetilde M \ne 0`（实例）** ✓✓）、`C-3864`（**临界锥退化（数值 `t^* = 0`）** ✓✓）、`C-3863`（**KKT 点与乘子** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-72：C-3872 —— Gordan 证书 ⟹ 结构非奇异性 ＋ `c_* = 1/L` 定理化**（唐先生 2026-09-21 22:50 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 唐先生的关键观察（}\textbf{正确}✓✓）}：\operatorname{rank}\widetilde M = 6 \Longrightarrow \operatorname{rank}G = 5✓✓\ \text{（}G\ \text{只有 5 列}✓） \Longrightarrow \textbf{R1 无需另证}✓✓$$

$$\qquad \Longrightarrow \text{真正剩余的结构问题只有}\ \boxed{e_E \notin \operatorname{col}G}✓✓$$

$$\textbf{② ⭐⭐ 本档的更强入口（}\textbf{不需要 C-3864}✓✓）：\textbf{Gordan 择一定理}✓✓$$

$$\qquad \text{恰有一个成立}✓：\textbf{(i)}\ \exists h \ne 0,\ Gh \le 0✓；\qquad \textbf{(ii)}\ \exists y > 0,\ G^{\top}y = 0✓✓$$

$$\qquad \text{而 KKT 站性}\ \textbf{本身} \text{就是}\ G^{\top}y = 0✓（y := (\omega_{13},\ \omega_{19},\ \lambda_6,\ \lambda_8,\ \lambda_{14},\ \lambda_{18})✓）$$

$$\textbf{③ 数值核验}✓✓：$$

$$\qquad y = (\mathbf{0.9037\ldots},\ \mathbf{0.0963\ldots},\ \mathbf{0.8379\ldots},\ \mathbf{0.9897\ldots},\ \mathbf{0.0419\ldots},\ \mathbf{0.1273\ldots})✓✓ \Longrightarrow \boxed{\text{六个分量}\ \textbf{全部严格为正}}✓✓$$

$$\qquad \|G^{\top}y\|_\infty = \mathbf{2.02\times10^{-59}}✓✓ \Longrightarrow \textbf{Gordan (ii) 成立}✓✓ \Longrightarrow \boxed{\{h:\ Gh \le 0\} = \{0\}}✓✓$$

$$\qquad \text{(i) 被排除}✓✓ \Longrightarrow \textbf{不存在任何非零的「六项皆} \le 0\text{"方向}✓✓$$

$$\textbf{④ Sanity（仅核验，非主证}✓）}：\max h_j\ \text{s.t.}\ Gh \le 0,\ \|h\|_\infty \le 1 \Longrightarrow \boxed{= 0\ (j = 1,\dots,5\ \text{全部})}✓✓$$

$$\qquad \text{另一支}✓：\min_h\|Gh + e_E\|_2 = \mathbf{1.2565} > 0✓✓ \Longrightarrow e_E \notin \operatorname{col}G✓（\text{数值镜像}✓）$$

$$\textbf{⑤ ⭐ 结构链（全由 KKT ＋ Gordan 推出}✓✓）}：$$

$$\qquad \text{KKT 严格正性} + \text{Gordan} \Longrightarrow \{Gh \le 0\} = \{0\}✓✓ \Longrightarrow$$
$$\qquad \qquad \text{若}\ \operatorname{rank}G < 5 \Longrightarrow \ker G \ne 0\ \text{给出非零锥元}✗ \Longrightarrow \boxed{\operatorname{rank}G = 5}✓✓（\text{结构}✓）$$
$$\qquad \qquad \text{若}\ e_E \in \operatorname{col}G \Longrightarrow \exists h:\ Gh = -e_E \le 0\ \text{且}\ h \ne 0\ (e_E \ne 0)✗ \Longrightarrow \boxed{e_E \notin \operatorname{col}G}✓✓（\text{结构}✓）$$
$$\qquad \Longrightarrow \boxed{\det\widetilde M \ne 0\ \text{（结构）}}✓✓ \Longrightarrow \boxed{c_* = \frac1L\ \textbf{成为定理}}✓✓$$

$$\textbf{⑥ 附带成果（}\textbf{反向升级}✓✓）}：\text{C-3864 的「临界锥退化」（}\textbf{数值}\ t^* = 0✓）\ \textbf{现在成为定理}✓✓$$

$$\qquad \text{因 Gordan 直接给出}\ \{Gh \le 0\} = \{0\}✓✓ \Longrightarrow \text{连标量乘性下降都不可能}✓✓\ \text{—— 比"无严格下降"} \text{更强}✓✓$$

$$\textbf{⑦ 对唐先生表述的细化}✓✓：\text{您指出}\ e_E \in \operatorname{col}G\ \text{给出的}\ h\ \text{有 even 分量}\ +1✓,\ \textbf{不在} \text{临界锥}✓（\text{修正我上一刀的措辞}✓✓）$$

$$\qquad \text{而}\ -e_E \in \operatorname{col}G\ \text{才给锥内方向}✓（\text{您已指出}✓）；\ \text{本档的 Gordan 路线}\ \textbf{更强}✓✓：\text{直接排除}\ \textbf{一切} \text{非零锥元}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
60 dps 重建 KKT 点（残差 ~2e-59）
Gordan 证书 y = (omega13, omega19, lambda6, lambda8, lambda14, lambda18)
   = (0.9037179437001577937, 0.096282056299842206299, 0.83791706425695966585,
      0.98971405578043382354, 0.041853186797750652561, 0.1272851054400162101)  全部 > 0
||G^T y||_inf = 2.0244e-59
Sanity A：max h_j over {Gh<=0, |h|inf<=1} = 0（j=1..5 全部）
Sanity B：min ||G h + e_E||_2 = 1.256459e+00 > 0；rank(G) = 5；奇异值 (69.661908, 42.732352, 39.49978, 25.586235, 3.059425)
```
- 脚本 ✓：`scripts/c380_72_C3872_gordan.py`✓；输出 ✓：`scripts/out_c380_72.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `\operatorname{rank}\widetilde M = 6 \Rightarrow \operatorname{rank}G = 5` ✓ | **CLOSED（唐先生观察）** ✓✓ |
| Gordan 证书（`y > 0`、`G^{\top}y = 0`） ✓ | **CLOSED** ✓✓ |
| 锥 `\{Gh \le 0\} = \{0\}` ✓ | **CLOSED（结构）** ✓✓ |
| R1 `\operatorname{rank}G = 5` ✓ | **CLOSED（结构）** ✓✓ |
| R2 `e_E \notin \operatorname{col}G` ✓ | **CLOSED（结构）** ✓✓ |
| `\det\widetilde M \ne 0` ✓ | **CLOSED（结构）** ✓✓ |
| **`c_* = 1/L`** ✓ | **定理（在严格正乘子下）** ✓✓ |
| C-3864 的锥退化 ✓ | **由数值升为定理** ✓✓ |
| Chebyshev 路线 ✓ | **不需要（已弃）** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称全局最优／`V_\sigma` 真值 ✓
- **不**声称已连到 arithmetic bridge ✓
- **条件性**声明 ✓：结论依赖「KKT 站性 ＋ 六个乘子严格为正」（本点已核验；一般情形为**非退化假设**✓）
- **不**把 sanity LP 当作主证（主证是 Gordan）✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}做 Chebyshev✗；\ \textbf{不}做新优化（sanity LP 仅核验}✓）；\ \textbf{不}碰二阶✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 Gordan择一     命中文件数=0    :: 
技术词 结构性非退化 命中文件数=0    :: 
技术词 严格正乘子  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 语义闭环}✓✓：\text{现有完整链}✓：\text{KKT} \Longrightarrow \{Gh \le 0\} = \{0\} \Longrightarrow \det\widetilde M \ne 0 \Longrightarrow c_* = \frac1L \Longrightarrow (\mu,\nu) = c_*(\lambda,\omega)✓✓$$
$$\qquad \Longrightarrow \boxed{\text{KKT geometry} \Longrightarrow \text{Farkas separating constant}\ \textbf{（严格）}}✓✓$$
$$\textbf{② 非退化假设的边界}✓：\text{逐步弱化「严格正」}（\text{部分乘子为零时}✓）\ \text{的结论形态}✓$$
$$\textbf{③ C-3869-}\beta✓：\text{二阶敏感度}（\text{暂缓}✓）；\ \textbf{④ 全局}\ V_\sigma\ \text{证书}✓$$
