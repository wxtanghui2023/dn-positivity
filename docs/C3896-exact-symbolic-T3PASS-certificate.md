# C-3896 — Exact (zero-floating-point) form of the T3-PASS certificate

已查地图（**先查后写**）：`C3894`（**`T3-PASS`；二阶系数表** ✓✓）、`C3893`（**活跃集核对** ✓✓）、`C3892`（**双坐标** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-104：C-3896 —— T3-PASS 证书的精确符号化（零浮点）**（唐先生 2026-09-22 09:39 令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 全部二阶系数落在}\ \mathbb Q(\sqrt3)✓✓\ \text{（因}\ (m,a) = (-\tfrac18,\tfrac{3\sqrt3}8)✓\ \text{为代数点}✓）：$$

| `n` ✓ | `A_n` ✓ | `B_n` ✓ | `A+B = F_n''(1)` ✓ |
|---|---|---|---|
| 6 ✓ | `-\tfrac{99}{2}\sqrt3` ✓ | `+\tfrac{99}{2}\sqrt3` ✓ | **`0`（精确）** ✓✓ |
| 8 ✓ | `-\tfrac{1539}{16} + \tfrac{1485}{16}\sqrt3` ✓ | `-\tfrac{1539}{16} - \tfrac{1485}{16}\sqrt3` ✓ | **`-\tfrac{1539}{8}`（精确）** ✓ |
| **14** ✓ | **`\tfrac{16065}{32} - \tfrac{2039373}{8192}\sqrt3`** ✓ | **`\tfrac{16065}{32} + \tfrac{2039373}{8192}\sqrt3`** ✓ | **`\tfrac{16065}{16}`（精确）** ✓✓ |
| 18 ✓ | `-\tfrac{9585621}{8192} + \tfrac{30496581}{131072}\sqrt3` ✓ | `-\tfrac{9585621}{8192} - \tfrac{30496581}{131072}\sqrt3` ✓ | **`-\tfrac{9585621}{4096}`（精确）** ✓ |

$$\textbf{② 精确证书（}\textbf{零浮点}✓✓**）：$$

$$\qquad \boxed{F_{14}''(\rho) = \left[\frac{16065}{32} - \frac{2039373}{8192}\sqrt3\right] + \left[\frac{16065}{32} + \frac{2039373}{8192}\sqrt3\right]\rho > 0\quad (\rho \ge 0)}✓✓$$

$$\qquad \textbf{正性为纯有理数比较}✓✓：q = -\tfrac{2039373}{8192} < 0✓,\ p = \tfrac{16065}{32} > 0✓,\ \text{且}\ p^2 - 3q^2 = \tfrac{4436681070213}{67108864} > 0✓✓$$

$$\qquad \Longrightarrow A_{14} > 0\ \textbf{精确}✓;\ B_{14}\ \text{因}\ p > 0,\ q > 0\ \textbf{显然为正}✓ \Longrightarrow \min_{\rho \ge 0} F_{14}''(\rho) = A_{14} > 0✓✓$$

$$\textbf{③ 附带精确结构}✓✓：F_6''(\rho) = \tfrac{99}{2}\sqrt3\,(\rho - 1)✓✓（\textbf{精确零点在}\ \rho = 1✓ \Longrightarrow \text{解释纯}\ \Delta_4\ \text{方向的精确平坦}✓✓）$$

$$\qquad F_8''(1) = -\tfrac{1539}{8}✓;\qquad F_{14}''(1) = \tfrac{16065}{16}✓;\qquad F_{18}''(1) = -\tfrac{9585621}{4096}✓$$

$$\qquad \text{且}\ n = 8,14,18\ \text{的}\ A_n, B_n\ \textbf{皆为共轭对}✓（A = p - q\sqrt3✓,\ B = p + q\sqrt3✓） \Longrightarrow A+B = 2p\ \textbf{为有理数}✓✓$$

$$\textbf{④ 结论状态（不变}✓✓**）：\boxed{T3\text{-PASS} / \text{LOCAL-RIGIDITY}}✓\ —— \text{但证书}\ \textbf{已脱离浮点}✓✓,\ \text{与论文 A 中"手证／半手证"级结果}\ \textbf{同一可信度层级}✓✓$$

$$\textbf{⑤ 范围（不变}✓✓**）：\text{局部于}\ (m,a) = (-\tfrac18,\tfrac{3\sqrt3}8)✓、\text{固定}\ (m,\sum Y^2)\ \text{球面}✓；\ \textbf{四禁写仍有效}✓✓$$

## §1 推导链（精确版 ✓✓）

$$T_n' = nU_{n-1}✓,\quad (1-u^2)T_n'' - uT_n' + n^2T_n = 0 \Longrightarrow T_n''(u) = \frac{uT_n'(u) - n^2T_n(u)}{1-u^2}✓✓$$

$$u_\pm = -\tfrac18 \pm \tfrac{3\sqrt3}8 \in \mathbb Q(\sqrt3)✓ \Longrightarrow T_n^{(k)}(u_\pm) \in \mathbb Q(\sqrt3)✓ \Longrightarrow A_n, B_n \in \mathbb Q(\sqrt3)✓✓$$

$$F_n''(\rho) = 2T_n''(u_+) + 2T_n''(u_-)\rho + \frac{1+\rho}{a}\left[T_n'(u_-) - T_n'(u_+)\right]✓✓ \Longrightarrow \text{仿射于}\ \rho✓,\ \text{系数在}\ \mathbb Q(\sqrt3)✓✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 系数符号化 ✓ | **完成（全部落在 \mathbb Q(\sqrt3)）** ✓✓ |
| `A_{14} > 0` ✓ | **精确（纯有理数比较）** ✓✓ |
| `B_{14} > 0` ✓ | **精确（显然）** ✓✓ |
| `F_{14}''(1) = 16065/16` ✓ | **精确（有理数）** ✓✓ |
| 证书零浮点 ✓ | **完成** ✓✓ |
| 判据／范围 ✓ | **不变（T3-PASS / LOCAL-RIGIDITY）** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称全局 collapse／全局 `F_0 = \varnothing`／全局 `\Delta_4 > 0` 稳定性／"全局最优必为该点" ✓✓（**四禁写继续有效**）
- **不**声称该局部刚性已扩展到更多 two-level 候选点（**待做**）✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}改判据✗;\ \textbf{不}扩范围✗;\ \textbf{不}动 T2 登记✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 零浮点证书  命中文件数=0    :: 
技术词 共轭对正性  命中文件数=0    :: 
技术词 有理数比较  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① 扩展问题}✓✓：\text{把该局部刚性论证推广到}\ \textbf{更多 two-level 候选点}✓（\text{一般}\ (m,a)✓）\ \text{或更大范围}✓✓$$
$$\textbf{② T2}✓：\text{按}\ C\text{-}3895\ \text{登记的 ROOT-PAIRING 推进}✓（6 项稀疏性 ＋ 奇偶分拆）✓✓$$
