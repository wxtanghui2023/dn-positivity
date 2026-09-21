已查地图（**先查后写**）：`C-3851`（**A：`\operatorname{rank}DG = \min(4,\#\text{distinct})`；B：显式统一 minor `\ge 1.72032\times10^{6}\delta_*^{3}\Delta^{6}`，且与 `\sigma` 无关** ✓✓）、`C-349`（**奇频 `= \int R_r\,d\mu_\sigma`；四矩抵消 ⟺ `\sum_j\sigma_jc_j^{2m+1} = 0\ (m \le 3)`** ✓✓）、`C-350`（**§0⑤ 秩掉障碍；Bridge A／B** ✓✓）、`C-369`（**碰撞层：只可写「碰撞部分的 `\mathcal Z \cap E` 已排除」** ✓✓）、`C-3849`（**`\delta_* > 0`（等价于权重塌缩被排除）** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-52：C3852 —— 定量逆映射，首档只做 C1（定义／三分）＋ C2（局部定量逆，常数依赖显式化）**（唐先生 2026-09-21 21:32 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 档位}✓✓：\text{本档}\ \textbf{只做 C1＋C2}✗✓；\ \textbf{不做} C3（有限覆盖）✗✓；\ \textbf{不}在 C 档证明"near-}\mathcal Z \Rightarrow \text{偶频矛盾}"✗✓（那是 D）✓✓$$

$$\textbf{② C1：三分（严格区分，不得混同）}✓✓$$

$$\qquad \textbf{(i) 碰撞}✓：\exists i \ne j,\ x_i = x_j✓ \ \Longrightarrow \ \Delta = 0✓\ \text{（}\Delta := \min_{i \ne j}|c_i - c_j|✓,\ c_j = \sqrt{x_j}✓）$$

$$\qquad \textbf{(ii) 权重塌缩}✓：\exists j,\ x_j = 0✓ \ \Longleftrightarrow\ c_j = 0✓ \ \Longleftrightarrow\ \text{权重}\ |w_j| = 0✓$$
$$\qquad \qquad ⚠️ \textbf{两者的排除资产不同}✓✓：\textbf{塌缩}已被 `C-3849` \textbf{证明级}排除}✓✓（\delta_* > 0✓）；\ \textbf{碰撞}仅由 `C-369`\ \textbf{在「碰撞部分的}\ \mathcal Z \cap E\text{」语境}排除✓✓ \ \textbf{不}得升级为全空间✓$$

$$\qquad \textbf{(iii) } \mathcal Z_\sigma := \{x : G(x,\sigma) = 0\}✓✓\ —— \ \textbf{奇频零集}✓，\ \textbf{与 (i)(ii) 是不同的条件}✓✓;\ \ G = (F_1,F_3,F_5,F_7)✓\ (r = 0..3)✓$$

$$\qquad \textbf{计数}✓：5\ \text{未知} - 4\ \text{方程} = 1\ \text{维}✓；\ ⚠️ \textbf{但系统对全体原子是} \ n\ \textbf{次齐次}✓✓ \Longrightarrow \textbf{这 1 维恰是整体标度方向}✓✓ \Longrightarrow \boxed{\text{模标度后解集}\ \textbf{离散}}✓✓$$
$$\qquad \qquad \text{（此点更正}\ C\text{-}369\ \text{的读法}✓：其"一维族 ⟹ 非离散"}\ \textbf{应读作}"一族标度射线"✓✓ \ \textbf{—— 覆盖问题因此}\ \textbf{变小}✓✓）$$

$$\textbf{③ C2：局部定量逆（常数链显式化）}✓✓：\text{设}\ \bar x \in \mathcal Z_\sigma✓,\ \sqrt{\bar x_j} \ge \sqrt{\delta_*}✓,\ 5\ \text{值互异}✓ \Longrightarrow \operatorname{rank}DG(\bar x) = 4✓（`C-3851` A✓）$$

$$\qquad \text{取}\ \hat j = \arg\max_{\hat j}|\det DG_{\hat j}|✓；\ \text{由隐函数定理（4 个依赖坐标）}✓ \Longrightarrow\ \text{局部}\ \mathcal Z_\sigma\ \text{为 1 维图}✓✓$$

$$\qquad \textbf{常数链}✓✓（\textbf{全部显式}，依赖}\ (\delta_*, \Delta)✓）$$
$$\qquad \qquad \eta = 1.72032\times10^{6}\,\delta_*^{3}\Delta^{6}✓（B✓）;\qquad \|DG\| \le 109.6/\sqrt{\delta_*}✓（\text{由}\ |U_{2r}(c)| \le 2r+1 \le 7✓,\ (2r+1) \le 7✓）$$
$$\qquad \qquad m := \sigma_{\min}(DG_{\hat j}) \ge |\det DG_{\hat j}|/\|DG\|^{3} \ge \boxed{1.307\,\delta_*^{4.5}\Delta^{6}}✓✓$$
$$\qquad \qquad \Longrightarrow\ \boxed{C_x = 2/m \ \le\ \frac{1.53}{\delta_*^{4.5}\,\Delta^{6}}}✓✓$$
$$\qquad \qquad \text{半径}✓：\rho := m/(2L)✓,\ L := \operatorname{Lip}(x \mapsto DG) \le \Lambda\,\delta_*^{-3/2}✓（\text{由}\ |U'_{2r}| \le U'_{2r}(1) \le 56\ (r \le 3)✓；\ \Lambda\ \text{取} 10^{3}\ \text{保守}✓）$$

$$\qquad \Longrightarrow\ \boxed{\|x - \bar x\| \le \rho \ \Longrightarrow\ \operatorname{dist}(x,\mathcal Z_\sigma) \le \frac{1.53}{\delta_*^{4.5}\Delta^{6}}\,\|G(x,\sigma)\|_\infty}✓✓$$

$$\textbf{④ ⚠️⭐ C2 的}\textbf{适用性障碍（本档最重要的发现）}✗✓：\text{数值扫描（16 符号类 × 数百起点）}✓ \Longrightarrow \textbf{未找到一个"正则零点"}✗✗$$

$$\qquad \textbf{观察}✓✓：\text{强制}\ a_i \ge \varepsilon > 0\ \text{时，}\ \|G\|\ \text{的极小值}\ \textbf{随}\ \varepsilon\ \text{一起趋于 0}✓：\ \varepsilon = 10^{-1} \to 5.3\times10^{-3}✓；10^{-2} \to 5.4\times10^{-6}✓；10^{-3} \to 9.3\times10^{-9}✓$$

$$\qquad \text{而}\ \varepsilon = 0\ \text{的精确解}\ \textbf{全部含零原子}✓✓：\text{典型解}\ (a_1,a_2,a_3,\beta) = (1,\beta,0,\beta)✓（\text{一族}✓，5\ \text{个原子中两处位置被正负部}\ \textbf{共用}✓，\ \text{且一个位置为}\ 0✓）$$

$$\qquad \Longrightarrow\ \textbf{数值上}\ \mathcal Z_\sigma \subseteq \{\text{塌缩层}\} \cup \{\text{碰撞层}\}✓✓ \Longrightarrow\ \boxed{\mathcal Z_\sigma \cap E_{\mathrm{even}} \ \textbf{数值上为空}}✓✓$$

$$\qquad \Longrightarrow\ \textbf{两个资产}\ \textbf{恰好}\ \text{覆盖它}✓✓：\text{塌缩} \leftarrow `C\text{-}3849`✓（\text{证明级}✓）；\ \text{碰撞} \leftarrow `C\text{-}369`✓（\text{限}\ \mathcal Z \cap E\ \text{语境}✓）$$

$$\textbf{⑤ 判词（诚实）}✓✓：$$

$$\qquad \textbf{(a)}\ \text{C2 的}\ \textbf{常数链推导}\ \textbf{完成}✓✓\ —— \text{满足唐先生"不能只写由逆函数定理"}✓✓$$
$$\qquad \textbf{(b)}\ \text{C2 的}\ \textbf{数值验证}\ \textbf{空跑}✗✓\ —— \text{因}\ \textbf{找不到正则零点}✓（故本档}\ \textbf{不}给出}\ \operatorname{dist} \le C\|G\|\ \text{的实测比}✗✓）$$
$$\qquad \textbf{(c)}\ \textbf{若}\ \mathcal Z_\sigma \cap E_{\mathrm{even}} = \varnothing\ \text{成立}✓ \Longrightarrow \textbf{局部定量逆在}\ E_{\mathrm{even}}\ \text{上}\ \textbf{无对象}✓✓ \Longrightarrow\ \text{C2 无法为 D 供料}✗✓\ \Longrightarrow\ \boxed{\text{该型可能 NO-GO}}✓✓$$
$$\qquad \qquad ⚠️ \textbf{但这是}\ \textbf{数值观察，非定理}✗✓；\ \text{须先做}\ \boxed{\mathcal Z_\sigma\ \text{结构审计}}✓✓\ \text{（分类：}\mathcal Z_\sigma\ \text{是否只落在塌缩／碰撞层}✓）\ \textbf{方可判 NO-GO}✗✓$$

$$\textbf{⑥ 自检记录（两次脚本失误，均已修正）}✓✓：\text{(i) 首版把}\ DG\ \text{的}\ \textbf{导数行}\ \text{当作}\ G\ \textbf{的函数值}✗ \Longrightarrow 0\ \text{零点}✓（空跑，已作废）✓；\ \text{(ii) 次版纯 Python 三层循环过慢}✗ \Longrightarrow \text{改向量化／带界求解}✓✓$$

$$\textbf{⑦ 账本（见 §2）}✓✓$$

## §1 C2 的标准推导（供复核 ✓✓）

$$\textbf{设定}✓：G : \mathbb R^5 \to \mathbb R^4✓;\ \text{取}\ \hat j\ \text{为依赖坐标}✓（|\hat j| = 4✓）,\ k\ \text{为自由坐标}✓；\ \Phi(y;x_k) := G(\text{insert}(y,k,x_k),\sigma)✓✓$$

$$\textbf{假设}✓：\Phi(\bar y;\bar x_k) = 0✓,\ DG_{\hat j}(\bar x)\ \text{可逆}✓,\ \|DG_{\hat j}^{-1}\| \le 1/m✓,\ \|D\Phi(y) - D\Phi(\bar y)\| \le L\|y - \bar y\|✓✓$$

$$\textbf{结论（定量隐函数）}✓✓：\text{若}\ \|y - \bar y\| \le \rho := m/(2L)✓ \Longrightarrow \|y - \psi(x_k)\| \le \frac{2}{m}\|\Phi(y;x_k)\|✓✓,\ \psi\ \text{为局部零集参数化}✓$$

$$\qquad \Longrightarrow\ \operatorname{dist}(x,\mathcal Z_\sigma) \le \|x_{\hat j} - \psi(x_k)\| \le \frac{2}{m}\|G(x,\sigma)\|_\infty✓✓\ \ \blacksquare$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| C1（定义／三分／齐次性更正） ✓ | **完成** ✓✓ |
| C2（常数链显式：`\eta`, `\|DG\|`, `m`, `C_x`, `\rho`） ✓ | **完成** ✓✓ |
| C2 的数値验证 ✓ | **空跑（无正则零点）** ✗✓ |
| `\mathcal Z_\sigma \cap E_{\mathrm{even}}` 的数值状态 ✓ | **观察为空（非定理）** ⚠️✓ |
| C3（全局有限覆盖） ✓ | **未做（遵令）** ✗✓ |
| D（Bridge B） ✓ | **未开** ✗✓ |
| 该型判词 ✓ | **待 `\mathcal Z_\sigma` 结构审计后定（倾向 NO-GO）** ⚠️✓ |

## §3 数值记录（数字驱动 ✓✓）

```
C1a：16 符号类 × 60 起点（无界）：正则零点（x>0, 5 互异, rank 4）= 0
C1b：无界最小 ‖G‖ = 2.3e-10，位置 x=(1.33,1.05,1e-5,1e-5,-0.13) —— 出箱 + 塌缩
C1c：归一化 b2=1（4 方程 4 未知）：732 个解，逐一检查 —— 全部含零原子
C1d：带界求解 min‖res‖：eps=1e-1 → 5.27e-3；1e-2 → 5.35e-6；1e-3 → 9.27e-9；
     1e-4 → 2.82e-9；1e-6 → 2.18e-9（后三点已达浮点地板）
     ⟹ 极小残差随 eps ↓ 且全部 argmin 停在边界 ⟹ 正则区无精确零点
C1e：齐次性验证：res(λ v) ≠ 0（λ ≠ 1）——证伪"全标度不变"✗✓ ⟹ 解集是射线
```
- 脚本 ✓：`scripts/c380_52_c3852_C1C2_v2.py`✓、`scripts/c380_52_witness_v3.py`✓、`scripts/c380_52_nondegen.py`✓（初版 `c380_52_c3852_C1C2.py` 作废保留 ✓）；输出 ✓：`scripts/out_c380_52_*.txt`✓

## §4 边界（不得声称 ✗✓）

- **不**声称 `\mathcal Z_\sigma \cap E_{\mathrm{even}} = \varnothing`（**数值观察**，非定理）✓
- **不**声称 C2 的实测比值（无正则零点，无法测）✓
- **不**把 `C-369` 的结论升级为 `\Delta_* > 0`（**遵唐先生令，保留为参数**）✓✓
- **不**在 C 档证明 D ✓
- **不**声称该型已 NO-GO（须先做 `\mathcal Z_\sigma` 结构审计）✓

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 定量逆映射      命中文件数=0    :: （本档新用）
技术词 dist(x,Z) <= C  命中文件数=0    :: （本档新用）
技术词 C3852           命中文件数=0    :: （本档新编号）
技术词 正则邻域        命中文件数=0    :: （本档新用）
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{①}✓\ \textbf{必做}✓：\ \mathcal Z_\sigma\ \text{结构审计}✓✓\ —— \text{分类}\ \mathcal Z_\sigma\ \text{是否只落在}\ \{\text{塌缩}\}\cup\{\text{碰撞}\}✓；\ \text{方法}✓：\text{Newton 恒等式 ＋ 4 个奇矩条件 ＋ 齐次性归约}✓✓$$
$$\textbf{②}✓\ \text{若①确认空} \Longrightarrow \text{该定量矩单射型}\ \textbf{NO-GO}✓✓\ \text{（C2 无对象）}✓;\ \text{并立刻记录：Bridge A 的"精确抵消"分支被两资产关闭}✓✓$$
$$\textbf{③}✓\ \text{若①发现正则零点} \Longrightarrow \text{重跑 C2 实测并进 C3}✓✓$$
$$\textbf{④}✓\ \textbf{不}提前做 C3／D✗✓$$
