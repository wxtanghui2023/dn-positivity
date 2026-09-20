已查地图（**先查后写**）：查 `C-194`（w=2 结构）、`C-192`（精确恒等式模式）、`C-152`（局部解析模板）。回查见 §5 ✓

D0: 本档对象 = **T13-B w=2 局部引理的归约**：三布尔图审计 ＋ 由 $S_6$ 切分后的剩余区域 $B$ **严格压成两个一维不等式** —— 关系 = 新构造（归约）＋ 审计更正
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 ⚠️ 两条逻辑更正（唐先生 2026-09-20 10:43 指出，全部采纳）

$$\textbf{① 覆盖的层级}：\text{"113 万点全覆盖"} \textbf{只说明数值采样覆盖}✗ \Rightarrow \textbf{不能推出解析区域覆盖}✗$$
$$\qquad \Longrightarrow \text{"局部覆盖"}\ \textbf{只能标为数值候选（ALIVE）}✓，\textbf{不能} \text{充当证明}✗✓$$
$$\textbf{② 独任区占比失效}：\text{上一轮的"独任区百分比"受}\ \texttt{priority assignment}\ \text{影响}✗ \Longrightarrow \textbf{不能作数学证据}✗✓$$
$$\qquad \Longrightarrow \text{已改为}\ \textbf{真三布尔图} \ I_k=\mathbf 1_{\{S_k\ge1\}}（k=1,5,6）✓，\text{统计全部}\ 2^3\ \text{个交集计数}✓$$

## §1 三布尔图审计（球 $r=0.10$，$1401^2$ 网格，球内 1,539,295 点）

| 码 $(I_1I_5I_6)$ | 点数 | 占比 |
|---|---|---|
| $000$ | $\mathbf 0$ | $\mathbf 0.000\%$ ✓ **无缺口** |
| $001$ | 262,027 | 17.023% |
| $010$ | 468,661 | 30.446% |
| $011$ | 41,000 | 2.664% |
| $100$ | 468,661 | 30.446% |
| $101$ | 49,321 | 3.204% |
| $110$ | $\mathbf 0$ | $\mathbf 0.000\%$ ← $S_1,S_5$ **从不同时**覆盖 ✓ |
| $111$ | 249,625 | 16.217% |

$$\Longrightarrow \ N_{000}=0✓\ （\text{数值}）；\qquad N_{110}=0✓\ ——\ \textbf{两区天然互斥}✓✓$$
$$\qquad \textbf{且}\ \{S_1\ge1\}\cup\{S_5\ge1\}\cup\{S_6\ge1\}\ \text{覆盖}=100.0000\%✓ \Longrightarrow \boxed{S_7\ \textbf{完全不需要}}✓✓$$

## §2 ⭐ $S_6$ 切分（恒等式 A 的精确形式，保留为核心）

$$S_6-1\ =\ 2\big[\sin^2(3\delta_2)-2\sin^2(3\delta_1)\big]✓\qquad\Longleftrightarrow\qquad \boxed{|\sin 3\delta_2|\ \ge\ \sqrt2\,|\sin 3\delta_1|}\ (A)✓✓$$
$$\text{数值核对}：\text{区域}\ B:=\{|{\sin3\delta_2}|<\sqrt2|{\sin3\delta_1}|\}\ \text{外}\ \Longrightarrow\ S_6\ge1\ \text{覆盖}\ 100.0000\%✓✓$$
$$\qquad B\ \text{内}：\ \max(S_1,S_5)\ \text{的最小值}=1.000073200\ \ge1✓✓\Longrightarrow \boxed{(B)\Longrightarrow(S_1\ge1)\lor(S_5\ge1)}\ \text{数值成立}✓$$

## §3 ⭐⭐ 归约：由 $B$ 到**两个一维不等式**

$$\textbf{单调性依据}：\text{因}\ |3\delta_i|\le0.3<\tfrac\pi2✓，|\sin 3\cdot|\ \text{在}\ [0,0.3]\ \text{严格增且正}✓$$
$$\qquad \Longrightarrow B\iff \sin(3|\delta_2|)<\sqrt2\sin(3|\delta_1|)\iff |\delta_2|<m(|\delta_1|)✓,\qquad m(t):=\tfrac13\arcsin(\sqrt2\sin3t)✓$$
$$\qquad \text{又球约束}\ |\delta_2|\le\sqrt{R^2-\delta_1^2}=:\mathrm{cap}✓ \Longrightarrow \ \textbf{最坏}\ \delta_2^*=\min(m,cap)✓$$
$$\textbf{又}：\text{因}\ |5\delta_2|\le0.5<\tfrac\pi2✓，|\sin 5\cdot|\ \text{在}\ [-0.5,0.5]\ \text{严格增}✓ \Longrightarrow -\sin(5\delta_2)\ \text{在}\ \delta_2\ \text{上严格减}✓$$
$$\qquad \Longrightarrow \text{对固定}\ \delta_1，\text{最坏情形取}\ \delta_2=\delta_2^*✓（\text{上确界一侧}）✓$$

$$\boxed{\ \textbf{(I)}\ \ \delta_1=+t\in[0,R]:\quad 2\cos(5t-\tfrac\pi3)-1-\sin(5\delta_2^*(t))\ \ge\ 0\ }$$
$$\boxed{\ \textbf{(II)}\ \delta_1=-t\in[-R,0]:\quad 2\cos(\tfrac\pi3-t)-1-\sin(\delta_2^*(t))\ \ge\ 0\ }$$
$$\qquad \text{（(I) 判}\ S_5\ge1；\text{(II) 判}\ S_1\ge1）✓$$

$$\textbf{数值}（2\times10^6\ \text{点}）：\min(I)=0.000000000000\ (\text{于}\ t=0)✓；\ \min(II)=0.000000000000\ (\text{于}\ t=0)✓ \Longrightarrow \textbf{两者均成立}✓✓$$
$$\qquad \text{小}\ t\ \text{行为}：(I)\approx5(\sqrt3-\sqrt2)\,t>0✓ \Longrightarrow t=0\ \text{是}\ \textbf{孤点}✓\ \text{可单独处理}✓$$
$$\qquad \text{端点值}：t=0.01\to(I)=+0.01465,(II)=+0.00313✓；t=0.1\to(I)=+0.7080,(II)=+0.1679✓$$

## §4 本档抓到并修掉的两处自我 bug（全在归约推导里）

$$\textbf{bug ①}：\text{首版漏了球半径截断}✗ —— \text{用}\ \delta_2^*=m(t)\ \text{而非}\ \min(m,cap)，\text{导致}\ \delta_1=-0.1\ \text{处}\ m=0.1438>R\ \text{的不可能取值}✗$$
$$\qquad \Longrightarrow \text{报出假失败}\ (II)=-0.3211✗\ \Longrightarrow \text{已修}✓$$
$$\textbf{bug ②}：\text{(II) 中把}\ \cos(\tfrac\pi3-t)\ \text{误写成}\ \cos(t+\tfrac\pi3)✗ ⟹ \text{报出假失败}\ -0.2036✗\ \Longrightarrow \text{已修}✓$$
$$\qquad \Longrightarrow ⚠️\ \textbf{两次"失败"都是我的实现错，不是数学错}✓（\text{项目第 12／13 次同类应验}✓）$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 三布尔图     命中文件数=0    ::
技术词 一维归约     命中文件数=0    ::
技术词 球半径截断   命中文件数=0    ::
```
⟹ 三项**均本档首次命名** ✓（事后重跑会自命中本档 1 次，依 `C-168` §6 扣除 ✓）

## §6 状态与下一步

$$\textbf{局部数值覆盖}：\text{ALIVE}✓\qquad \textbf{解析覆盖引理}：\textbf{尚未证明}✗$$
$$\Longrightarrow \text{下一步（唯一一刀）}：\textbf{严格证明 (I)(II)}✓ —— \text{二者是}\ \textbf{一维}✓ \Longrightarrow \text{区间算术 eps-覆盖即可}✓（廉价）✓$$
$$\qquad \text{随后}：\text{球外远场证书}（2\ \text{维网格＋Lipschitz}）✓ \Longrightarrow \text{合成}\ g_2(10)=1\ \text{的完整定理}✓$$
$$
\textbf{边界}：\text{§1–§3 的数值部分仅作定位}✓；\text{§3 的单调性依据是严格的}✓；\text{归约的}\ \textbf{有效性} \text{已用二维真值互校}（B\ \text{内}\ \max(S_1,S_5)\ge1.0000732✓\ \text{与归约给出的下界}\ \ge1\ \text{相容}）✓；\text{未用 RH}✓；\text{未改他档}✓$$
