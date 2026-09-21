已查地图（**先查后写**）：`C-3870`（**取到步；`c_* = 1/L`；`\det\widetilde M = -1.156\times10^7`** ✓✓）、`C-3869`（**单边桥引理** ✓✓）、`C-3867`（**六活跃顶点** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-71：C-3871 —— 六活跃矩阵的结构非奇异性审计（R1＋R2 分解）**（唐先生 2026-09-21 22:49 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 约定更正（}\textbf{正是唐先生警告的那类混淆}✓✓）}：\text{唐先生写"实际频率}\ \{6,8,13,14,18,19\}"✓；\ \text{但偶频那四个用的是}\ \textbf{标签}\ 2q✗✓$$

$$\qquad \text{在}\ \phi\ \text{坐标下}\ F_{2q} = \sum_j\cos(4q\phi_j)✓✓ \Longrightarrow \textbf{真实频率} = \boxed{\{12,16,28,36\}}✓✓（\text{奇频才是}\ 13,19✓）$$

$$\qquad \Longrightarrow \text{本档}\ \textbf{按真实频率建行}✓✓；\ \text{混用}\ r／k／2q\ \textbf{即前错之源}✗✓$$

$$\textbf{② 精确分解}✓✓：\ \widetilde M = [\,G\ \big|\ -e_E\,]✓,\ e_E = (0,0,1,1,1,1)^T✓,\ b = (-1,-1,0,0,0,0)^T✓✓$$

$$\qquad \boxed{\det\widetilde M \ne 0 \iff \text{R1}\ (\operatorname{rank}G = 5)\ \wedge\ \text{R2}\ (e_E \notin \operatorname{col}G)}✓✓\ \text{（标准线性代数}✓）$$

$$\textbf{③ R1（}\textbf{实例级坚固成立}✓✓）}：\text{奇异值}\ (69.6619,\ 42.7324,\ 39.4998,\ 25.5862,\ \mathbf{3.0594})✓✓ \Longrightarrow \sigma_{\min} = 3.06\ \text{远离 0}✓✓$$

$$\qquad \textbf{六个 5×5 子式全部非零}✓✓（\text{逐行剔除}✓）：$$

$$\qquad \qquad \text{drop}\ 13:\ -5234152.18315✓;\quad \text{drop}\ 19:\ -557646.264183✓;\quad \text{drop}\ 12:\ 4853046.75176✓✓$$
$$\qquad \qquad \text{drop}\ 16:\ -5732224.33157✓;\quad \text{drop}\ 28:\ 242405.222311✓;\quad \text{drop}\ 36:\ -737209.676056✓✓$$

$$\qquad \Longrightarrow \textbf{任取五行皆独立}✓✓ \Longrightarrow \text{R1}\ \textbf{比单个 6×6 行列式强得多}✓✓$$

$$\textbf{④ R2（}\textbf{实例级成立}✓✓）}：\operatorname{rank}\widetilde M = 6 > \operatorname{rank}G = 5✓✓ \Longrightarrow \boxed{e_E \notin \operatorname{col}G}✓✓$$

$$\qquad \text{绝对幅值}✓：|\det\widetilde M| = 11564885.981695✓（\text{与}\ C\text{-}3870\ \text{同幅}✓；\text{符号差来自}\ c\ \text{列约定}✓）$$

$$\qquad \textbf{几何含义（唐先生）}✓✓：\text{若}\ e_E \in \operatorname{col}G✓ \Longrightarrow \exists h\ \text{使}\ G_{13}h = G_{19}h = 0✓\ \text{且}\ G_6h = G_8h = G_{14}h = G_{18}h = 1✓✓$$
$$\qquad \qquad \Longrightarrow \text{一个}\ \textbf{odd 一阶为零、四个 even 同向增加} \text{的方向}✓✓ \Longrightarrow \textbf{直接的临界锥几何对象}✓✓\ \text{（R2 的价值所在}✓）$$

$$\textbf{⑤ ⚠️ Chebyshev 路线的正确边界（}\textbf{唐先生预判成立}✓✓）}：\text{降幂恒等式}✓：\sin(k\phi) = \sin\phi\,U_{k-1}(\cos\phi)✓✓$$

$$\qquad \Longrightarrow \text{行}\ G_k = -k\operatorname{diag}(\gamma_j\sin\phi_j)\,(U_{k-1}(z_j))_j✓✓ \Longrightarrow \text{行相关性} \iff (U_{k-1})\ \text{采样行相关性}✓（\sin\phi_j \ne 0✓,\ \gamma_j \ne 0✓）$$

$$\qquad \textbf{但}\ \textbf{不能} \text{由此推出 R1}✗✓：\sum_k a_kU_{k-1}\ \text{是}\ \textbf{次数} \le 18\ \text{的多项式}✓,\ \text{可在}\ \textbf{五个采样点} \text{同时消失}✗✓$$

$$\qquad \Longrightarrow \boxed{\text{R1 仍需}\ \textbf{具体采样结构} \text{（五点位置 ＋ 等抵消／偶频可行性条件）}}✓✓\ \text{—— 与唐先生"不是一句 Chebyshev 独立性就能封口"}\ \textbf{一致}✓✓$$

$$\qquad ⚠️ \textbf{自检}✗✓：本档核验行把降幂写成}\ U_{k-2}\ \text{（指数笔误}✗） \Longrightarrow \text{该行打印的}\ 21.43\ \textbf{作废}✗✓；\ \text{恒等式本身标准}✓✓$$

$$\textbf{⑥ 判词（按唐先生分层）}✓✓：\ \text{A（R1＋R2 结构证明）}\ \textbf{未达}✗✓；\ \text{B（记录}\ \text{rank}G = 5✓）\ \textbf{已达}✓✓；\ \text{C（仅当前点行列式）}\ \textbf{已超越}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{结构非奇异性}\ \textbf{未 CLOSED}}⚠️✓;\ \ \text{但}\ \boxed{\text{分解为 R1／R2 ＋ 六个子式全非零 ＋ R2 秩判据}}\ \textbf{已是坚固的实例级证书}✓✓$$

$$\qquad \Longrightarrow \ C\text{-}3870\ \text{的}\ c_* = 1/L\ \textbf{保持实例级}✓✓（\text{不升级为一般定理}✗）$$

$$\textbf{⑦ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
60 dps 重建点：x 22 位稳定
R1：奇异值 (69.6619077168, 42.7323518037, 39.4997801442, 25.5862345169, 3.05942491899) -> rank = 5
    六个 5x5 子式（逐行剔除）：
      drop 13: -5234152.18315 ; drop 19: -557646.264183 ; drop 12: 4853046.75176
      drop 16: -5732224.33157 ; drop 28: 242405.222311  ; drop 36: -737209.676056
R2：rank[M] = 6 > rank[G] = 5 ; det(M) = 11564885.981695
Chebyshev 降幂：G_k = -k diag(gamma_j sin phi_j) (U_{k-1}(z_j))_j（恒等式标准；核验行有指数笔误，已作废）
```
- 脚本 ✓：`scripts/c380_71_C3871_structure.py`✓；输出 ✓：`scripts/out_c380_71.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 分解 `\det\widetilde M \ne 0 \iff` R1∧R2 ✓ | **CLOSED（符号）** ✓✓ |
| R1 `\operatorname{rank}G = 5` ✓ | **实例级成立（六个子式全非零）** ✓✓ |
| R2 `e_E \notin \operatorname{col}G` ✓ | **实例级成立（秩判据）** ✓✓ |
| R2 的临界锥几何含义 ✓ | **已登记** ✓✓ |
| Chebyshev → R1 的结构证明 ✓ | **不可行（次数 ≤ 18 可在五点消失）** ✗✓ |
| 结构非奇异性 ✓ | **未 CLOSED（判词 B）** ⚠️✓ |
| `c_* = 1/L` ✓ | **保持实例级** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称结构非奇异性已证 ✓
- **不**用"频率不同 ⟹ 线性独立"跳步 ✓✓
- **不**把当前 `\det \ne 0` 反推为一般频率定理 ✓
- **不**声称 R1 的结构证明已完成 ✓
- **不**引用本档核验行作废的 21.43 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}新 LP✗；\ \textbf{不}新优化✗；\ \textbf{不}把数值行列式当结构证明✗；\ \textbf{不}碰二阶✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 结构非奇异性 命中文件数=0    :: 
技术词 子式全非零  命中文件数=0    :: 
技术词 降幂恒等式  命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{① R1 的结构来源}✓✓（\text{真正的开放问题}✓）：\text{利用}\ \textbf{五个采样点的具体位置} \text{＋ 等抵消／偶频可行性}✓ \text{证明不存在}\ \sum a_kU_{k-1}\ \text{在}\ z_j\ \text{全消失}✓✓$$
$$\qquad \text{候选工具}✓：\text{离散正交性／Christoffel–Darboux（在同一采样集上）}✓；\ \text{或}\ \text{频率差结构}\ \{12,16,28,36\}\ \text{与}\ \{13,19\}\ \text{的}\ \textbf{错位}✓✓$$
$$\textbf{② R2 的结构来源}✓：\text{证明}\ e_E \notin \operatorname{col}G\ \text{在}\ \textbf{任何} \text{六活跃 KKT 点成立}✓（\text{几何：不存在 odd 平坦＋even 同增方向}✓）$$
$$\textbf{③ C-3869-}\beta✓：\text{二阶敏感度}（\text{暂缓}✓）$$
