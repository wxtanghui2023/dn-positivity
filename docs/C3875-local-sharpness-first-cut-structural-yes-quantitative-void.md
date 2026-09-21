已查地图（**先查后写**）：`C-3874B`（**`GLOBAL-CERT-PARTIAL`；复合路线** ✓✓）、`C3874A`（**A 与二阶耦合** ✓✓）、`C-3872`（**Gordan ⟹ 锥 `= \{0\}`** ✓✓）、`C-3873`（**`c_* = 1/L`；LOCAL-ONLY 标签** ✓✓）、`C-3863`（**`x^*`** ✓✓）。回查见 §5 ✓

D0: 本档对象 = **C-380-76：C-3875 —— Local Sharpness Certificate（首刀：先 Gordan＋一阶余项，不先上 Hessian）**（唐先生 2026-09-21 23:00 发令）
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（七条 ✓✓）

$$\textbf{① 范围严格固定}✓✓：\sigma = (-1,1,1,-1,1)✓；\ C\text{-}3863\ \text{的}\ x^*✓；\ \text{邻域盒}\ B_\rho(x^*)✓（\text{半径由认证给出}✓）$$

$$\qquad \textbf{不}声称}\ \text{其他}\ \sigma\ \text{类}✗；\ \textbf{不}声称}\ \text{全部}\ E_{\mathrm{even}}✗；\ \textbf{不}声称}\ \text{全局}\ V_\sigma✗✓$$

$$\textbf{② 首刀框架}✓✓：\text{active signed}\ g_{13} = -F_{13}✓,\ g_{19} = F_{19}✓,\ g_q = F_q - \tfrac12\ (q \in \mathcal A)✓；\ \text{在}\ x^*：g_{13} = g_{19} = c_0✓,\ g_q = 0✓✓$$

$$\qquad \text{记}\ h = x - x^*✓,\ g_i(x^* + h) = g_i(x^*) + \nabla g_i(x^*)\cdot h + R_i(h)✓（G\ \text{的行即}\ \nabla g_i✓）$$

$$\textbf{③ ⭐ 结构性答案（唐先生的关键问题）}✓✓：\textbf{Gordan 直接给出}\ \boxed{\eta := \min_{\|u\| = 1}\max_i(Gu)_i > 0}✓✓$$

$$\qquad \textbf{证明（一行）}✓✓：\text{若}\ \eta = 0✓ \Longrightarrow \exists\ \text{单位}\ u:\ Gu \le 0✗\ \text{与}\ C\text{-}3872\ \text{的}\ \{h: Gh \le 0\} = \{0\}\ \text{矛盾} \square✓✓$$

$$\qquad \Longrightarrow \boxed{\text{C-3872 的正证书}\ \textbf{确实直接产生可认证的}\ \eta > 0}✓✓ \Longrightarrow \textbf{局部最优性是}\ \textbf{尖锐的一阶现象}✓✓$$

$$\qquad \Longrightarrow \boxed{\text{二阶需求}\ \textbf{很可能可被消掉}}✓✓\ \text{（\textbf{正是唐先生的猜想}✓✓）}$$

$$\textbf{④ 一阶余项界（}\textbf{显式、全局}✓✓）}：\phi\ \text{坐标下 Hessian}\ \textbf{对角}✓：$$

$$\qquad \text{偶频}\ |\partial^2/\partial\phi_j^2| = (4q)^2 \le 36^2 = \mathbf{1296}✓；\ \text{奇频} \le 23^2 = 529✓$$

$$\qquad \Longrightarrow \boxed{K := \tfrac12\cdot 1296 = \mathbf{648}}✓✓,\qquad |R_i(h)| \le K\|h\|_2^2✓✓\ \text{（\textbf{无需区间 Hessian 大矩阵}✓✓）}$$

$$\textbf{⑤ 封口条件}✓✓：\text{对}\ \|h\|_2 = r > 0✓：\max_i g_i(x^* + h) \ge c_0 + \eta\,r - K r^2✓✓ \Longrightarrow \boxed{r < \frac{\eta}{K}}\ \text{时严格} > c_0✓✓$$

$$\qquad \Longrightarrow \text{一旦}\ \eta\ \text{被认证}✓,\ \text{封口半径}\ \rho_{\mathrm{cert}} = \eta/K\ \textbf{显式}✓✓$$

$$\textbf{⑥ ⚠️ 定量认证：}\textbf{本档 VOID}✗✓（\text{四次 LP 形式自检失败}✗✓）$$

$$\qquad \text{(a) 漏掉}\ u = u^+ - u^-\ \text{的负部}✗；\ \text{(b) 归一化用}\ \le 1\ \text{而非等式}✗；\ \text{(c)}\ \ell_1\ \text{归一化}\ \textbf{退化}✓：u = 0\ \text{可由}\ u^+ = u^- > 0\ \text{取到}✓ \Longrightarrow \text{LP 恒有平凡最优}\ t = 0✗✗$$

$$\qquad \text{(b)+(c) 的同一病根}✓：\text{用}\ (u^+,u^-)\ \text{表示}\ u\ \text{时}\ \textbf{未施加}\ |u_j|\ \text{的精确性}✓✓$$

$$\qquad \text{数值旁证（}\textbf{仅为上界}✓）}：\text{随机}\ 2\times10^5\ \text{方向上}\ \min\max_i(Gu)_i = \mathbf{0.448803}✓✓ \Longrightarrow 0 < \eta \le 0.4488✓（\textbf{不构成认证}✗✓）$$

$$\textbf{⑦ 判词}✓✓：\ \boxed{\textbf{VOID（定量）}}✗✓\ \text{＋}\ \boxed{\textbf{结构 YES：}\eta > 0\ \text{且二阶可省}}✓✓$$

## §1 记录（数字驱动 ✓✓）

```
x* (40 dps): x = [0.8009302155414330192646, 0.5611431997255226913605, 0.7024571606623587274759,
                0.6261014034243929958332, 0.8688438905530294285225]
             phi/pi = [0.1472131729733695487, 0.23048867882095517497, 0.18365067170450866496,
                       0.20942249633500208877, 0.1179588313706160604]
Gordan => eta > 0（结构，CLOSED）
K = 0.5 * 1296 = 648.0（对角 Hessian 界，phi 坐标）
随机方向最小 max_i(Gu)_i = 0.448803（上界，非认证）
四次 LP 形式：全部 VOID（负部遗漏／不等式归一化／L1 退化）
```
- 脚本 ✓：`scripts/c380_76_C3875_sharpness.py`、`c380_76b_..._fix.py`、`c380_76c_C3875_eta.py`✓（均标注失败形式 ✓）；输出 ✓：`out_c380_76.txt`、`out_c380_76b.txt`✓

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| 范围固定（`\sigma`, `x^*`） ✓ | **CLOSED** ✓✓ |
| `\eta > 0`（结构） ✓ | **CLOSED（Gordan 一行）** ✓✓ |
| `K`（余项界） ✓ | **CLOSED（显式 648）** ✓✓ |
| 封口半径公式 `\rho_{\mathrm{cert}} = \eta/K` ✓ | **CLOSED（条件式）** ✓✓ |
| **定量** `\eta_1` ✓ | **未认证（LP 形式错误 VOID）** ✗✓ |
| 一阶尖锐封口 ✓ | **未 CLOSED（待定量）** ✗✓ |
| `c_* = 1/L` 用法 ✓ | **仅 LOCAL-ONLY 组件（本档未用）** ✓ |
| **判词** ✓ | **VOID（定量）＋ 结构 YES** ✓✓ |

## §3 边界（不得声称 ✗✓）

- **不**声称已封口（定量未认证）✓
- **不**把随机方向值 0.4488 当 `\eta` 的认证值 ✓
- **不**把 `c_* = 1/L` 写成 `E_{\mathrm{even}}` 上的 universal constant ✓
- **不**声称其他 `\sigma` 类或全局 ✓

## §4 本档**不**做的事 ✓✓

$$\textbf{不}上 Hessian 大矩阵✗（\text{按唐先生令}✓）；\ \textbf{不}碰二阶临界锥✗；\ \textbf{不}做全局部分✗✓$$

## §5 【技术词回查】输出（**先跑后写** ✓）

```
技术词 一阶尖锐性  命中文件数=0    :: 
技术词 符号型枚举  命中文件数=0    :: 
技术词 局部封口半径 命中文件数=0    ::
```

## §6 下一步（须唐先生发令 ✓）

$$\textbf{修正方案（已定位病根）}✓✓：\text{按}\ \textbf{32 个符号型}\ s \in \{\pm1\}^5\ \text{枚举}✓：u = s \odot w✓,\ w \ge 0✓,\ \sum_jw_j = 1✓ \Longrightarrow \text{每个是}\ \textbf{规范 LP}✓✓$$
$$\qquad \Longrightarrow \eta_1 = \min_{s}\ \text{(32 个 LP 的最小值)}✓✓\ \text{（\text{或直接用对偶证书取严格下界}✓）$$
$$\textbf{随后}✓：\text{取}\ \rho_{\mathrm{cert}} = \eta_1/K✓ \Longrightarrow \text{得到}\ \textbf{LOCAL-SHARP-CLOSED}✓✓\ \text{（非空盒}✓）$$
$$\textbf{拼装（唐先生⑤）}✓✓：E_{\mathrm{even}} = (E_{\mathrm{even}}\setminus B_\rho) \cup (E_{\mathrm{even}}\cap B_\rho)✓；\ \text{远区＝全局排斥（未来）}✓,\ \text{近区＝本档}✓✓$$
