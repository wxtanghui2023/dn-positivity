已查地图（**先查后写**）：`C-3854`（**`\gamma^{(13)}` 靶与数值窗口 `(0,0.876]`** ✓✓）、`C-3850`（**`g = 0.876069` 上界** ✓✓）、`C-3853`（**退化轨迹：零原子层 ＋ 碰撞层** ✓✓）、`C-369`／`C-358`（**`\mathcal D_{\partial}`／`\mathcal D_{\mathrm{coll}}` 分层** ✓✓）、`C-380-13`（**线性对偶封口** ✓✓）。回查见 §4 ✓

D0: 本档对象 = **C-380-55：侦察刀 A —— 收紧 `\gamma^{(13)}` 数值窗口 ＋ 判定近极值是否趋向退化轨迹**（唐先生 2026-09-21 22:02 发令：A 为**侦察刀，非证明刀**）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 侦察结论（provisional）}✓✓：\text{两次独立优化的近极值构型}\ \textbf{都在内部}✓✓：$$

$$\qquad \text{(i)}\ C\text{-}3850\ \text{最优}\ x \approx (0.802,0.561,0.703,0.627,0.870)✓ \Longrightarrow \min_j x_j = 0.561✓；\qquad \text{(ii)}\ \text{本档最优}\ \min_j x_j = 0.551✓,\ \min|c_i - c_j| = 0.0415✓✓$$

$$\qquad \Longrightarrow\ \boxed{\text{近极值序列}\ \textbf{不贴}\ \mathcal D_{\partial}\cup\mathcal D_{\mathrm{coll}}}✓✓ \Longrightarrow\ \text{按唐先生判定规则}\ \boxed{\text{A} \Rightarrow \textbf{内部} \Rightarrow \text{转 B}}✓✓$$

$$\textbf{② 数值窗口}\ \textbf{未被收紧}✗✓：\text{本档最好}\ 0.9878 > C\text{-}3850\ \text{的}\ 0.876069✓ \Longrightarrow \textbf{上界仍取}\ \boxed{\gamma^{(13)} \le 0.876}✓✓$$

$$\qquad \text{（本档运行只是}\ \textbf{较弱的局部最优}✓，}\textbf{不}构成收紧}✗✓；\ \text{原窗口}\ \gamma^{(13)} \in (0,\ 0.876]✓ \textbf{不变}✓$$

$$\textbf{③ ⭐ 结构信号（有效）}✓✓：\text{极值构型上}\ \textbf{偶频余量很小}✓✓：\ \max_r F_{2r}\ \text{与}\ \tfrac12\ \text{的差} = +0.0072\ \text{（细调后）}✓,\ +0.0154／+0.0654\ \text{（粗阶段）}✓✓$$

$$\qquad \Longrightarrow\ \text{极值构型}\ \textbf{贴近偶频约束边界}✓✓ \Longrightarrow\ \text{偶约束在最优处}\ \textbf{binding}✓✓\ \text{（这是 A 唯一有效的新结构信息}✓；\text{与"必须实质使用}\ F_{2r} \le \tfrac12\text{"的防循环条款}\ \textbf{相容}✓✓）$$

$$\qquad \text{全部测得的候选构型}\ \textbf{均可行}✓（\max_r F_{2r} \le \tfrac12✓）\ \Longrightarrow\ \text{惩罚式优化}\ \textbf{未越界}✓✓$$

$$\textbf{④ ⚠️ 自检一（严重 bug，已修）}✗✓：\text{首版脚本写}\ \texttt{max(axis=(1,2))} \Longrightarrow \textbf{对}\ \sigma\ \textbf{取最大}✗✗$$

$$\qquad \text{而}\ \gamma\ \text{的定义是}\ \textbf{先对}\ r\ \text{取最大、再对}\ \sigma\ \textbf{取最小}}✓✓ \Longrightarrow \text{首版给出的}\ 3.76\sim3.85\ \textbf{全部作废}✗✓\ \text{（其为"最坏符号类"值}✓）$$

$$\qquad \text{修正}✓：G = \big|U @ S^{\top}\big|.\max(\text{axis}=1).\min(\text{axis}=1)✓✓ \Longrightarrow \text{修正后}\ 0.99\ \text{量级}✓ \text{（合理}✓）$$

$$\textbf{⑤ ⚠️ 自检二（自杀陷阱，已规避）}✗✓：\texttt{pkill -f c380\_55...}\ \textbf{杀掉了自己的 shell}✗✓\ \text{（`TOOLS.md` 已记录的同型陷阱，}\textbf{再次踩中}✗）$$

$$\qquad \text{规避}✓：\text{改用}\ \texttt{kill <PID>}✓；\ \text{排查用}\ \texttt{pgrep -f "c380\_55\_gamma\_knife[AB]"}✓（\textbf{方括号技巧}✓）$$

$$\textbf{⑥ 边界}✓✓：\text{本档结果为}\ \textbf{侦察信号}✓，\ \textbf{非}极值鉴定}✗✓\ \text{（细调未收敛}✓；}\textbf{不}声称}\ \gamma^{(13)}\ \text{的极值构型已确定}✗✓$$

$$\textbf{⑦ 账本（见 §2）}✓✓$$

## §1 数值记录（数字驱动 ✓✓）

```
修正后（σ 取最小）：
  phase1 随机起点 (N=6000, 600 it)：轨迹 2.3845 → 1.3912（200 it 后停滞）
        g = 1.391234 ; min_j x_j = 0.5481 ; min|c_i-c_j| = 0.0419 ; max_r F_2r = 0.4846 (r=9), 余量 +0.0154 ; 可行
  phase2 退化偏置 (near x_j=0 / near-collision, N=6000, 600 it)：轨迹 1.8443 → 1.3001
        g = 1.300077 ; min_j x_j = 0.0589 ; min|c_i-c_j| = 0.0577 ; max_r F_2r = 0.4346 (r=7), 余量 +0.0654 ; 可行
  phase3 细调 (N=1500, 1500 it)：轨迹 1.2122 → 0.9878
        g = 0.987800 ; min_j x_j = 0.5511 ; min|c_i-c_j| = 0.0415 ; max_r F_2r = 0.4928 (r=4), 余量 +0.0072 ; 可行
对照：C-3850 = 0.876069（其上界仍为当前最好）
作废（bug）首版：3.76~3.85（对 σ 取最大）
```
- 脚本 ✓：`scripts/c380_55_gamma_knifeA_v2.py`✓（首版 `c380_55_gamma_knifeA.py` 为慢版，已停 ✓）；输出 ✓：`scripts/out_c380_55_knifeA.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `\gamma^{(13)}` 上界 ✓ | **0.876（C-3850，未收紧）** ✓✓ |
| 近极值几何 ✓ | **内部（不贴退化轨迹）—— 两次独立优化一致** ✓✓ |
| 极值处偶频余量 ✓ | **很小（binding）** ✓✓ |
| A 的判定输出 ✓ | **内部 ⟹ 转 B** ✓✓ |
| 首版 bug ✓ | **已修（max/min over σ）** ✓✓ |
| `pkill` 自杀 ✓ | **再次踩中，已规避** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称 `\gamma^{(13)}` 的极值构型已确定（细调未收敛）✓
- **不**把 0.9878 当作新上界（它比 0.876 差）✓
- **不**声称 A 给出了任何证明性进展 ✓
- **不**因"内部信号"就跳过唐先生的 `\delta_*` 定量化选项（C 仍保留为可选）✓

## §4 【技术词回查】输出（**先跑后写** ✓）

```
技术词 侦察刀        命中文件数=0    :: 
技术词 内部极值     命中文件数=1    :: ./V227-ARS-root-spectrum-audit-realpart-not-modulus-invariant.md 
技术词 偶频余量     命中文件数=0    ::
```

## §5 下一步（须唐先生发令 ✓）

$$\textbf{按判定规则}✓✓：A \Rightarrow \textbf{内部} \Rightarrow \boxed{\text{转 B}}✓✓\ \text{（}\textbf{非线性奇/偶频耦合机制}✓）$$
$$\textbf{但须注意成本}✓：\text{唐先生明确"}\textbf{暂不开} \text{Fejér／Chebyshev 大证明工程}"✗✓ \Longrightarrow \text{建议 B}\ \textbf{先做小切口}✓✓：$$
$$\qquad \boxed{\text{在内部极值附近做}\ \textbf{局部展开}✓（\text{奇频受迫} \to \text{偶频二阶反应}✓）},\ \textbf{而非} \text{全局证书构造}✗✓$$
$$\textbf{备选}✓：\text{若 B 的小切口无果}✓ \Longrightarrow \text{回头做 C}（\delta_*\ \text{定量化}✓）\ \text{或}\ \text{收紧数值窗口}✓✓$$
