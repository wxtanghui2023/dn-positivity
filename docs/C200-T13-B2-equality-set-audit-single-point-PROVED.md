已查地图（**先查后写**）：查 `C-199`（全域定理 $g_2(10)=1$）、`C-197`（局部引理 PROVED）、`C-196`（归约）、`C-193`（$w=1$ 等号集）。回查见 §5 ✓

D0: 本档对象 = **T13-B2：$w=2$ 的等号集审计**（证明等号集 = 单点）—— 关系 = 已有定理（$g_2(10)=1$）的**刚性升级**
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 命题（⚠️ 先更正一处：**有序对**）

$$\text{唐先生原命题写为无序对}\ \{\phi_1,\phi_2\}=\{\tfrac\pi3,\tfrac\pi2\}✗\ —— \text{但}\ w=2\ \textbf{权重不对称}⟹\text{交换不是对称变换}✗$$
$$\qquad F_2(\tfrac\pi2,\tfrac\pi3)=\max_{k\le10}\big[2\cos\tfrac{k\pi}2+\cos\tfrac{k\pi}3\big]=\mathbf{1.5}>1✓（\text{由}\ k=4：2\cos2\pi+\cos\tfrac{4\pi}3=2-\tfrac12=\tfrac32✓）$$
$$\qquad ⚠️\ \textbf{我原先的理由错了}✗：\text{我只看了}\ k=1\ \text{得}\ 0.5<1✗\ —— \text{必须取}\ \max_{k}\ \text{才对}✓（\text{数值审计①纠正}）✓$$

$$\boxed{\ \textbf{定理(T13-B2)}：\ \max_{1\le k\le10}\big[2\cos k\phi_1+\cos k\phi_2\big]=1\ \iff\ (\phi_1,\phi_2)=\Big(\frac\pi3,\ \frac\pi2\Big)\ }✓✓$$
$$\qquad （\text{在}\ [0,\pi]^2\ \text{上}；\text{等号集为}\ \textbf{单点}✓，\text{非两点}✓）$$

## §2 证明（四步，全部严格）

$$\textbf{Step 1（远场，}\texttt{C-199}\ \text{改丢弃半径}\ \rho_{\rm disc}=0.098\text{）}：$$
$$\qquad 1{,}759\ \text{个终端箱的区间下界}\ \ge\ 1.000314949✓ \Longrightarrow \boxed{F>1\ \text{于全部终端箱之并}}✓✓$$
$$\qquad \text{终端箱之并}\ =\ D\setminus(\text{2 个丢弃箱})✓（\text{Phase3 体积逐位相等}✓）$$
$$\textbf{Step 2（等号点定位）}：\text{丢弃箱各角模长}\le0.098✓ \Longrightarrow \text{丢弃箱}\subseteq\{|\delta|\le0.098\}\subset B_{0.1}✓$$
$$\qquad \Longrightarrow \text{等号点（}F=1\text{）只能在}\ \{|\delta|\le0.098\}\ \text{内}✓\ —— ⚠️\ \textbf{关键}：\text{球面}\ |\delta|=0.1\ \text{上不存在丢弃箱}✓（\text{因}\ 0.1>0.098✓）$$
$$\qquad \qquad \Longrightarrow \text{球面全部落在终端箱内}\Longrightarrow F>1\ \text{于球面}✓✓（\text{旧}\ 0.1\ \text{版做不到这点}✗，\text{故本刀改半径}✓）$$

$$\textbf{Step 3（球内，}\texttt{C-197}\ \text{＋拆分）}：\text{在}\ \{|\delta|\le0.098\}\ \text{内证}\ F\ge1\ \text{且等号仅原点}✓$$
$$\qquad \textbf{(a)}\ B'\cap\{\delta_1\ne0\}：\text{C-197 的两个一维证书给出}\ \textbf{严格正余量}\ (\min=1.6075\times10^{-11})✓ \Longrightarrow F>1✓✓$$
$$\qquad \textbf{(b)}\ \{|\delta|\le0.098\}\setminus B'：\text{此处}\ |\delta_2|\ge\min(K|\delta_1|,\ \mathrm{cap}(\delta_1))✓，\mathrm{cap}=\sqrt{0.01-\delta_1^2}✓$$
$$\qquad \qquad \text{若}\ \min=\mathrm{cap}：\text{需}\ |\delta_2|\ge\mathrm{cap}✓，\text{但}\ |\delta|\le0.098\Longrightarrow|\delta_2|\le\sqrt{0.098^2-\delta_1^2}<\mathrm{cap}✗\ \textbf{矛盾}✓$$
$$\qquad \qquad \Longrightarrow \text{只能}\ \min=K|\delta_1| \Longrightarrow |\delta_2|\ge K|\delta_1|>m(|\delta_1|)\ \Longrightarrow\ \textbf{（精确等价式）}\ S_6>1✓✓$$
$$\qquad \textbf{(c)}\ \text{原点}：F(0,0)=2\cos\tfrac\pi3+\cos\tfrac\pi2=1✓\ \textbf{精确}✓$$
$$\textbf{Step 4（合成）}：F>1\ \text{于}\ (D\setminus\{|\delta|\le0.098\})✓\ \text{与}\ \{|\delta|\le0.098\}\setminus\{0\}✓ \Longrightarrow \textbf{等号集}=\{0\}✓✓$$
$$\qquad \Longleftrightarrow\ (\phi_1,\phi_2)=\big(\tfrac\pi3,\tfrac\pi2\big)✓✓\qquad\square$$

## §3 数值审计（五项，互相印证；均为探索性）

| # | 量 | 结果 | 结论 |
|---|---|---|---|
| ① | $F(\tfrac\pi2,\tfrac\pi3)$（交换点） | $1.500000000000$ | $>1$ ⟹ 非等号点 ✓ |
| ② | $S_6{=}1$ 曲线在球内（115,079 点） | $\min F=1$（仅 $t{=}0$ 处） | 曲线上除原点 $F>1$ ✓ |
| ③ | 例外点 $m(t){=}\mathrm{cap}(t)$ | 唯一根 $t=0.057539386$，$\vert\delta\vert=0.1$ 精确；四象限 $F\in\{1.0527,1.8480,2.1406,1.1796\}$ | 均 $>1$ ✓ |
| ④ | 球面 $\vert\delta\vert=0.1$ 上 $\min F$ | $1.019486582$ @ $(0.0542244,0.0840221)$ | $>1$ ✓（与 C-198 探针 $1.0195$ 一致 ✓） |
| ⑤ | 球内 $B'$ 之外 $\min F$ | $1.000000$ @ 原点 | 仅原点 ✓ |

$$\Longrightarrow \text{且}\ \textbf{例外点③已不再需要单独处理}✓✓\ —— \text{它落在球面上}✓，\text{由 Step 1 直接得到}\ F>1✓$$

## §4 本档抓到并修掉的两处自我失误

$$\textbf{失误 ①}：\text{我原以}\ k=1\ \text{单点判交换点非等号}✗ —— \text{理由错}✗（\text{须取}\ \max_k✓）\qquad \text{结论对}✓（k=4\ \text{给}\ 1.5✓）$$
$$\textbf{失误 ②}：\texttt{R2}\ \text{分数写成}\ 49/5000=0.0098✗（\text{注释却写}\ 0.098^2=0.009604✗） \Longrightarrow \text{已改为精确}\ 9604/10^6✓\ \text{并重跑}✓$$
$$\qquad \textbf{教训}：\text{把"结论对"当成"理由对"是危险习惯}✓✓；\text{注释与代码数字必须同源}✓$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 等号集审计    命中文件数=1    ::  ./C200-T13-B2-equality-set-audit-single-point-PROVED.md
技术词 有序对刚性    命中文件数=1    ::  ./C200-T13-B2-equality-set-audit-single-point-PROVED.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 两项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §6 边界

- Step 1／3(a) 依赖**区间算术证书** ✓（$\rho_{\rm disc}=0.098$ 版，0 违反，体积逐位守恒 ✓）；Step 3(a) 的严格余量很小（$1.6\times10^{-11}$）但**为正**✓
- Step 2／3(b) 是**解析推理**（模长比较 ＋ $\sqrt2<K$ ＋ 精确等价式 ✓）
- §3 全部为**探索性数值** ✓，只作印证，不作证明 ✓
- 本档结论**仅对** $w=2$、$M=2$、窗口 $10$ ✓；**不外推**到 $g_w=w/2$ ✗（$\texttt{C-193}$ 已显示 $w=1.2/1.5$ 不满足 ✓）
- **未用** RH；**未改**他档 ✓
