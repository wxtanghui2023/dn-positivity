已查地图（**先查后写**）：`C-152`（`M=2` 闭合；`c=2.0512` 为数值扫描 —— 本档**精确化**）、`C-151`（远场 0.5278）、`C-144`（Case A）、`E4-ENGINE-2`（引理 C）。关键词回查：`精确覆盖常数`=0、`对偶权重`=0、`符号可核`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:56 建议 ①）**：**把 `c` 从数值扫描升级为精确值（LP／代数数）**。
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \text{梯度是}\ \textbf{代数数}：\ g_k=(-k\sin\tfrac{k\pi}3,\ -k\sin\tfrac{k\pi}2)\in\mathbb Q(\sqrt3)^2✓$$
$$\qquad g_1=(-\tfrac{\sqrt3}2,-1),\ g_4=(2\sqrt3,0),\ g_5=(\tfrac{5\sqrt3}2,-5),\ g_7=(-\tfrac{7\sqrt3}2,7),\ g_8=(-4\sqrt3,0)✓✓$$
$$\textbf{(二)}\ ⭐⭐\ \boxed{c\ =\ \frac{28\sqrt{1677}}{559}\ =\ \frac{28\sqrt3}{\sqrt{559}}\ \approx\ 2.0512224201}\qquad(c^2=\tfrac{2352}{559})✓✓$$
$$\qquad \text{切点}\ u^*=\Big(\tfrac{14}{\sqrt{559}},\ \tfrac{11\sqrt3}{\sqrt{559}}\Big)\approx(0.5921369,\ 0.8058374)\ \text{（}\textbf{精确}：}\langle g_4,u^*\rangle=\langle g_7,u^*\rangle=c)✓✓$$
$$\textbf{(三)}\ ⭐\ \text{共线关系有}\ \textbf{代数原因}：\text{对}\ k+k'=12\ \text{有}\ k'g_k+k\,g_{k'}=0\ \textbf{恒成立}✓✓$$
$$\qquad (\text{因}\ \sin\tfrac{k\pi}3+\sin\tfrac{(12-k)\pi}3=0\ \text{且}\ \sin\tfrac{k\pi}2+\sin\tfrac{(12-k)\pi}2=0\ \text{——}12\ \text{是}\ 6\ \text{与}\ 4\ \text{的公倍数})✓✓$$
$$\qquad \Longrightarrow 7g_5+5g_7=0\ \text{与}\ 8g_4+4g_8=0\ \text{都是}\ (k,k')=(5,7),(4,8)\ \text{的\ 特例}✓✓$$
$$\textbf{(四)}\ ⭐\ \text{局部引理现为}\ \textbf{纯符号可核}：|\delta|\le\tfrac c{32}=\tfrac{7\sqrt{1677}}{4472}=0.0641007\ \mathrm{rad}=3.6726996^\circ>\;1^\circ（\text{比值}\ 3.673）✓✓$$

FREEZE-ACK: 本档即冻结期内的精确化（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`c` 的精确值 `28\sqrt{1677}/559` ＋ 共线的代数原因（`k+k'=12`）＋ 局部引理符号化** —— 关系 = 精确化，非新机制
D1: 0

# C-153 · ⭐⭐ **`c` 的精确值：`28\sqrt{1677}/559`；局部引理现为纯符号可核**

> **唐先生 2026-09-19 12:56**：建议 ① 把 `c` 精确重算（LP 对偶／有理算术），把证明从"计算机辅助"升级为"纯符号可核" ✓

---

## §1 五个梯度（**代数数**，符号验证）

$$g_k=\nabla F_k(0)=\Big(-k\sin\tfrac{k\pi}3,\ -k\sin\tfrac{k\pi}2\Big)\in\mathbb Q(\sqrt3)^2✓$$
$$\begin{array}{c|r|r|r}
k & g_k & |g_k| & \text{方向}\\\hline
1 & (-\tfrac{\sqrt3}2,\ -1) & \tfrac{\sqrt7}2=1.3229 & 229.11^\circ\\
4 & (2\sqrt3,\ 0) & 2\sqrt3=3.4641 & 0^\circ\\
5 & (\tfrac{5\sqrt3}2,\ -5) & \tfrac{5\sqrt7}2=6.6144 & 310.89^\circ\\
7 & (-\tfrac{7\sqrt3}2,\ 7) & \tfrac{7\sqrt7}2=9.2601 & 130.89^\circ\\
8 & (-4\sqrt3,\ 0) & 4\sqrt3=6.9282 & 180^\circ\\
\end{array}✓✓$$
$$\textbf{模长结构}：k\ \text{奇}\ \not\equiv0\ (\mathrm{mod}\ 3)\Rightarrow|g_k|=\tfrac{k\sqrt7}2；\ k\ \text{偶}\ \not\equiv0\ (\mathrm{mod}\ 3)\Rightarrow|g_k|=\tfrac{k\sqrt3}2✓✓$$

## §2 ⭐⭐ `c` 的精确值

$$\text{切点条件}\ \langle g_4,u\rangle=\langle g_7,u\rangle=:c\ \text{（两形同时极大）}\Longrightarrow\ y=\tfrac{11\sqrt3}{14}x✓$$
$$x^2+y^2=1\Longrightarrow x=\tfrac{14}{\sqrt{559}},\ y=\tfrac{11\sqrt3}{\sqrt{559}}\Longrightarrow u^*=\Big(\tfrac{14}{\sqrt{559}},\tfrac{11\sqrt3}{\sqrt{559}}\Big)✓✓$$
$$\boxed{c=\langle g_4,u^*\rangle=2\sqrt3\cdot\tfrac{14}{\sqrt{559}}=\frac{28\sqrt3}{\sqrt{559}}=\frac{28\sqrt{1677}}{559}\approx2.0512224201}✓✓$$
$$\qquad \text{精确核验}：\langle g_4,u^*\rangle=\tfrac{28\sqrt3}{\sqrt{559}}=\langle g_7,u^*\rangle=-\tfrac{7\sqrt3}2\cdot\tfrac{14}{\sqrt{559}}+7\cdot\tfrac{11\sqrt3}{\sqrt{559}}=\tfrac{-49\sqrt3+77\sqrt3}{\sqrt{559}}✓✓$$

## §3 为何 `c` 就是**全局**最小值（严格，有限弧覆盖）

$$\text{对每个}\ k，\text{"好集"}\ \{u:\langle g_k,u\rangle\ge c\}\ \text{是单位圆上的一段}\ \textbf{弧}：\text{中心}\ \mathrm{dir}(g_k)，\text{半宽}\ \arccos(c/|g_k|)✓$$
$$\begin{array}{c|r|r|r}
k & \text{中心} & \text{半宽} & \text{弧}\\\hline
4 & 0.00^\circ & 53.691^\circ & [-53.69,\ 53.69]\\
7 & 130.89^\circ & 77.202^\circ & [53.69,\ 208.10]\\
8 & 180.00^\circ & 72.778^\circ & [107.22,\ 252.78]\\
5 & 310.89^\circ & 71.934^\circ & [238.96,\ 382.83]\\
\end{array}✓✓$$
$$\text{并集}=[-53.69^\circ,382.83^\circ]=\text{整圆}✓✓\quad(\text{两处关键：}53.69^\circ=0+53.691=130.89-77.202\ \textbf{恰好相接}；$$
$$\qquad 238.96^\circ<252.78^\circ\ \text{与}\ 306.31^\circ<382.83^\circ\ \text{均有度级余量})✓✓$$
$$\Longrightarrow \forall u,\ \exists k:\ \langle g_k,u\rangle\ge c \Longrightarrow \min_{|u|=1}\max_k\langle g_k,u\rangle=c=\tfrac{28\sqrt{1677}}{559}✓✓$$
$$\qquad \text{注}：g_1\ \textbf{永不活跃}（|g_1|=\tfrac{\sqrt7}2=1.3229<c）✓$$

## §4 ⭐ 共线关系的**代数原因**（唐先生 12:56 追问）

$$\text{恒等式}：\ \text{若}\ k+k'=12，\ \text{则}\ k'g_k+k\,g_{k'}=0\ \textbf{恒成立}✓✓$$
$$\qquad \text{因}\ \sin\tfrac{k\pi}3+\sin\tfrac{(12-k)\pi}3=0\quad\text{且}\quad\sin\tfrac{k\pi}2+\sin\tfrac{(12-k)\pi}2=0✓✓$$
$$\qquad (12=\mathrm{lcm}(6,4)：\tfrac{k\pi}3\ \text{与}\ \tfrac{k'\pi}3\ \text{关于}\ 2\pi\ \text{对称}；\ \tfrac{k\pi}2\ \text{与}\ \tfrac{k'\pi}2\ \text{关于}\ 3\pi\ \text{对称})✓✓$$
$$\Longrightarrow 7g_5+5g_7=0\ \text{与}\ 8g_4+4g_8=0\ \text{均为}\ (k,k')=(5,7),(4,8)\ \text{的特例}✓✓$$
$$\qquad ⟹ \textbf{不是数值巧合}，\text{而是}\ k\ \text{与}\ 12-k\ \text{的}\ \textbf{对偶权重} \text{结构}✓✓$$

## §5 局部引理（**现为纯符号可核**）

$$\forall|\delta|\le\varepsilon:\quad \max_{k\in\{1,4,5,7,8\}}\Big[\cos k\varphi_1+\cos k\varphi_2\Big]\ \ge\ \tfrac12+c|\delta|-32|\delta|^2✓$$
$$\text{取}\ \varepsilon=\tfrac c{32}=\frac{7\sqrt{1677}}{4472}=0.0641007006\ \mathrm{rad}=3.6726996^\circ✓✓$$
$$\qquad \text{与远场邻域}\ 1^\circ\ \text{之比}：3.673\times✓✓\quad(c/32>1^\circ\ \text{为}\ \textbf{严格} \text{不等式，已符号核})✓$$
$$\Longrightarrow \textbf{局部部分已完全脱离数值}（\text{除}\ \arccos\ \text{端点比较，可用有理区间收紧}）✓✓$$

## §6 状态与剩余

$$\begin{array}{c|l|l}
\text{环节} & \text{内容} & \text{状态}\\\hline
\text{中心值} & F_k(0)=\tfrac12\ (k=1,4,5,7,8) & \text{精确}\ ✓\\
\text{梯度} & g_k\in\mathbb Q(\sqrt3)^2 & \text{精确}\ ✓\\
\text{覆盖常数} & c=\tfrac{28\sqrt{1677}}{559} & \textbf{本档精确}\ ✓\\
\text{全局最小性} & \text{四弧覆盖整圆} & \text{有限核对}\ ✓\\
\text{局部半径} & \tfrac c{32}=3.6727^\circ>1^\circ & \text{精确}\ ✓\\
\text{远场} & |\delta|>1^\circ\Rightarrow g\ge0.5278 & \text{计算机辅助（网格＋Lipschitz）}\\
\end{array}✓✓$$
$$\Longrightarrow \text{`M=2` 只剩}\ \textbf{一处} \text{数值成分（远场证书）}；\ \text{且}\ \text{远场半径可任意细化（无损）}✓✓$$

## §7 边界与回查

- ⚠️ §1–§5 均**符号计算**（`sympy` 精确核验：`7g_5+5g_7=(0,0)`、`c^2=2352/559`、`u^*` 精确形式）✓
- ⚠️ §3 的弧端点比较用浮点**度数**（余量≥1°）；正式版可用有理区间收紧 ✓
- ⚠️ **不声称** 远场已符号化；**不声称** `M\ge3` 已证 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:0x）`[纪律]`（先跑后写）

```
技术词 精确覆盖常数  命中文件数=0 ::  ⟹ 本档新增
技术词 对偶权重      命中文件数=0 ::  ⟹ 本档新增
技术词 符号可核      命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
