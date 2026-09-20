已查地图（**先查后写**）：查 `C-196`（归约到 (I)(II)）、`C-195`（区间证书模板）、`C-177`（一维区间证书先例）。回查见 §5 ✓

D0: 本档对象 = **C-196 归约中两个一维不等式的区间覆盖证书**（$f_I\ge0$、$f_{II}\ge0$ 于 $[0,R]$）—— 关系 = 缺口关闭（把局部引理由 ALIVE 升为 PROVED 的必要条件）
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 证书对象

$$f_I(t)=2\cos(5t-\tfrac\pi3)-1-\sin(5\,\delta_2^*(t))✓,\qquad f_{II}(t)=2\cos(\tfrac\pi3-t)-1-\sin(\delta_2^*(t))✓,\qquad 0\le t\le R=0.1✓$$
$$\delta_2^*(t)=\min\big(m(t),\ \sqrt{R^2-t^2}\big)✓,\qquad m(t)=\tfrac13\arcsin(\sqrt2\sin 3t)✓$$

$$\textbf{目标}：\inf_{[0,R]}f_I\ge0✓,\quad \inf_{[0,R]}f_{II}\ge0✓\qquad (\text{不是要求全区间统一正 margin})✓$$

## §2 ⭐ 关键简化：$m$ 只需**上界**，而 $\arcsin$ 可绕开

$$\text{本实现环境无}\ \texttt{mp.iv.asin}✗ \Longrightarrow \text{改用严格上界链条}（\text{只用到}\ \sin/\cos/\text{sqrt}✓）$$
$$\qquad \arcsin u\ \le\ \frac{u}{\sqrt{1-u^2}}\quad(0\le u<1)✓\ ——\ \text{由}\ (\arcsin)'=\frac1{\sqrt{1-u^2}}\ \text{递增}✓$$
$$\qquad \sin 3t\ \le\ 3t\quad(t\ge0)✓;\qquad \sqrt{1-2\sin^2(3t)}\ \ge\ \sqrt{1-2\sin^2(0.3)}=:c\quad(t\le0.1)✓$$
$$\Longrightarrow\ m(t)\ \le\ K\,t✓,\qquad c\ge0.90847983737102178✓,\qquad \boxed{K=\sqrt2/c\le1.5566812869128475}✓✓$$
$$\qquad ⚠️\ \text{用}\ Kt（\text{放大}）\ \text{使区域}\ B'\supseteq B✓ \Longrightarrow \textbf{结论更强}✓（\text{覆盖更大区域}）✓$$

## §3 ⚠️ 首次运行**无效**（必须记录）

$$\text{首版把}\ f_{II}\ \text{的单调方向写反}✗：\text{误以为}\ \cos(\tfrac\pi3-t)\ \text{在}\ t\ \text{上递减}✗$$
$$\qquad \text{实际}：\tfrac\pi3-t\ \text{递减}✓，\cos\ \text{在}\ [0,\pi]\ \text{递减}✓ \Longrightarrow \cos(\tfrac\pi3-t)\ \textbf{递增}✓ \Longrightarrow \textbf{最小值在}\ t=a✓（\text{非}\ t=b✗）$$
$$\qquad \text{后果}：\text{首跑用}\ t=b\ \text{得}\ f_{II}\ \text{的\textbf{过大}下界}✗ \Longrightarrow \text{"1 个箱即通过"}✓\ —— \textbf{这正是红旗}✓$$
$$\qquad \Longrightarrow \textbf{已修}✓，并把方向写成代码内断言（\texttt{assert}）✓⟹ \text{本次结果有效}✓✓$$
$$\qquad \textbf{教训}：\text{"证书通过"必须先审方向}✓；\text{通过得太容易 = 可疑}✓✓$$

## §4 ⭐ 结果（有理端点 ＋ 区间算术，方向断言在内）

$$[K]：c\ge0.90847983737102178✓,\ K\le1.5566812869128475✓$$
$$[t=0]\ \text{精确}：f_I(0)=2\cos(-\tfrac\pi3)-1=0✓,\ f_{II}(0)=2\cos(\tfrac\pi3)-1=0✓\ （\text{区间取整残差}\sim1.1\times10^{-16}）✓\ \Longrightarrow \textbf{单独处理}✓$$
$$[\text{解析小端}\ 0\le t\le A_0=10^{-9}]\ f_I\ \ge\ 8.768476\times10^{-10}✓;\ f_{II}\ \ge\ 1.753695\times10^{-10}✓\ （\text{系数}\ 5\sqrt3-5K=+0.876848✓,\ \sqrt3-K=+0.175370✓）$$

| 函数 | all_certified | 评估箱 | 终端认证箱 | 最大深度 | 认证最小值 | 最小值所在箱 | 耗时 |
|---|---|---|---|---|---|---|---|
| $f_I$ | $\mathbf{True}$ ✓ | 503 | 252 | 30 | $+8.0377319\times10^{-11}$ | $[1.745058052\times10^{-9},\,1.931322565\times10^{-9}]$ | 0.15 s |
| $f_{II}$ | $\mathbf{True}$ ✓ | 481 | 241 | 30 | $+1.6075419\times10^{-11}$ | 同箱 | 0.12 s |

$$\Longrightarrow \boxed{\inf_{[0,R]}f_I\ \ge\ 0✓✓\qquad \inf_{[0,R]}f_{II}\ \ge\ 0✓✓}\qquad（[0,A_0]\ \text{解析}✓\ +\ [A_0,R]\ \text{区间认证}✓）$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 单调方向断言   命中文件数=0    ::
技术词 放大上界       命中文件数=0    ::
```
⟹ 两项**均本档首次命名** ✓（事后重跑会自命中本档，依 `C-168` §6 扣除 ✓）

## §6 结论与链条状态

$$\textbf{本轮关闭}：\text{C-196 的"唯一缺口"（两个一维不等式）}✓✓$$
$$\textbf{局部引理（}w=2\text{）链条}：\ \delta\ \text{在}\ 0.1\ \text{球内} \Longrightarrow \begin{cases}|\sin3\delta_2|\ge\sqrt2|\sin3\delta_1| &\Longrightarrow S_6\ge1✓\\ \text{否则}\ |\delta_2|<m(|\delta_1|)\le K|\delta_1| &\Longrightarrow S_5\ge1\ (\delta_1\ge0)\ \text{或}\ S_1\ge1\ (\delta_1<0)✓\end{cases}$$
$$\qquad \Longrightarrow \boxed{\max(S_1,S_5,S_6)\ \ge\ 1\ \text{于}\ 0.1\ \text{球}}✓✓\ \textbf{（局部引理 PROVED）}✓✓$$

$$\textbf{下一刀（唯一）}：\text{球外远场证书}（2\ \text{维}，\text{目标}\ F\ge1）✓ \Longrightarrow \text{合成}\ g_2(10)=1\ \text{的完整定理}✓$$
$$\qquad ⚠️\ \text{注意}：\text{远场若用"网格＋Lipschitz"}，\text{所需分辨率}\ h\sim\frac{\text{margin}}{\mathrm{Lip}}✓ \Longrightarrow \text{需先测球外 margin 再定方案}✓（\text{可能需两尺度}）✓$$

## §7 边界

- §4 是**区间算术证书**（严格 ✓），依赖 mpmath.iv 正确性 ✓；方向断言已写成代码内 `assert` ✓
- $\arcsin$ **未被区间包络**✗，而是被**严格上界**替代 ✓（$m$ 只以放大上界进入，逻辑更保守 ✓）
- §3 如实记录了**无效首跑**与修正 ✓；§4 的两次通过均来自**修正后**版本 ✓
- **未用** RH；**未改**他档 ✓
