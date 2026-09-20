已查地图（**先查后写**）：查 `C-242`（Case II 分解＋关键条件）、`C-241`（双-案例）、`C-240`（五函数归约否定）、`C-239`（II-a/b/c）。回查见 §7 ✓

D0: 本档对象 = **C-243：Case II 的精确压缩（★ 修正版）＋ 二维→一维精确归约 ＋ 两个自我纠错** —— 关系 = 严格化推进
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 唐先生的"精确相消"洞察正确}✓✓：\Lambda+(|D|-|U|)=c_0+R+|D|✓\ \text{（零误差}✓）—— \text{但符号需修正}✗✓}$$
$$\boxed{\textbf{② 修正版 (★)}✓✓：\mathcal E_w=w[P(\varepsilon)-\kappa]+c_0+R(\eta)+\bigl|wT(\varepsilon)+U(\eta)\bigr|✓✓}$$
$$\boxed{\textbf{③ 二维→一维精确归约}✓✓：\mathcal E_w\ \ge\ w[P(\varepsilon)-\kappa]+\tilde\Psi\bigl(wT(\varepsilon)\bigr)✓✓\ \text{（先动这刀，比四阶更根本}✓）}$$
$$\boxed{\textbf{④ 一维不等式数值成立}✓✓：五 }j\times w\ \text{全部}\min=+8.0\times10^{-7}\sim+9.7\times10^{-6}✓（\text{网格零}✓）\ \text{且极小点在}\ u=0✓$$
$$\boxed{\textbf{⑤ 解析闭合未完成}✗：\text{存在【delicate cancellation}】✗✓（\text{单侧斜率近抵消}\lambda✓）\Longrightarrow \text{必须二阶闭合}✓}$$

## §1 修正版 (★)：精确相消（本档核心 ✓✓）

$$\text{正确定义}✓：P=\cos\tfrac{11\varphi_1}2\cos(d\varphi_1)✓,\quad T=\sin\tfrac{11\varphi_1}2\sin(d\varphi_1)✓,\quad R,U\ \text{同理于}\ \varphi_2✓$$
$$\qquad Q:=\tfrac{A+B}2=wP+R✓,\qquad D:=\tfrac{A-B}2=-wT-U✓✓\ \textbf{（两项都带负号！）}$$
$$\qquad \text{因}\ \cos a\varphi_2-\cos b\varphi_2=-2\sin\tfrac{11\varphi_2}2\sin(d\varphi_2)=-2U✓\ \textbf{（负号）}✗✓$$
$$\Longrightarrow \max(A,B)=Q+|D|=wP+R+|wT+U|✓✓$$
$$\Longrightarrow \boxed{\mathcal E_w=\max(A,B)-(w\kappa-c_0)=w[P(\varepsilon)-\kappa]+c_0+R(\eta)+\bigl|wT(\varepsilon)+U(\eta)\bigr|}✓✓$$
$$\qquad \textbf{相消机制}✓✓：\Lambda=c_0+R+|U|✓ \Longrightarrow \Lambda+\bigl(|wT+U|-|U|\bigr)=c_0+R+|wT+U|✓✓\ \text{（精确，零余项}✓\ \text{—— 唐先生洞察}✓）$$
$$\qquad \text{且}\ \varepsilon=0\ \text{时}：\mathcal E=c_0+R+|U|=\Lambda\ \ge\ 0✓（\text{Lemma 3}✓）✓$$

## §2 二维→一维精确归约（本档关键推进 ✓✓）

$$\text{固定}\ \varepsilon\ \text{后对}\ \eta\ \text{取最小}✓（\text{因}\ \eta\ \text{部分恰好是该极小化对象}✓）:$$
$$\boxed{\tilde\Psi(\zeta):=\min_{\varphi_2\in[0,\pi]}\Bigl[c_0+\cos\tfrac{11\varphi_2}2\cos(d\varphi_2)+\bigl|\zeta+\sin\tfrac{11\varphi_2}2\sin(d\varphi_2)\bigr|\Bigr]}✓✓$$
$$\Longrightarrow \boxed{\mathcal E_w\ \ge\ w\bigl[P(\varepsilon)-\kappa\bigr]+\tilde\Psi\bigl(wT(\varepsilon)\bigr)}✓✓\ \textbf{（精确，无损失}✓——\text{因}\ \tilde\Psi\ \text{就是}\ \eta\ \text{的最优值}✓）$$
$$\qquad \text{而且由 Lipschitz-1}：\tilde\Psi(\zeta)\ge\tilde\Psi(0)-|\zeta|=−|\zeta|✓（\text{粗界}✓）\ \Longrightarrow \text{粗界给}\ \lambda u-|\tau||u|✗（\text{退化}✗，\text{与 C-242 §4 一致}✓）$$

## §3 数值判定（一维 ✓✓）

```
   j    pair      Ψ̃(0)         w=5/10/100 的 min         极小组
   1   ( 1,10)  8.0463e-07    +8.046302e-07 (u=0)         ✓✓
   2   ( 5, 6)  9.6561e-06    +9.656079e-06 (u=0)         ✓✓
   3   ( 4, 7)  9.6561e-06    +9.656079e-06 (u=0)         ✓✓
   4   ( 3, 8)  9.6561e-06    +9.656079e-06 (u=0)         ✓✓
   5   ( 2, 9)  8.0463e-07    +8.046302e-07 (u=0)         ✓✓
```
$$\Longrightarrow \textbf{一维不等式全部成立}✓✓（\text{值}\approx0\ \text{即网格分辨率}✓，\text{真值}=0✓\ \text{因 Lemma 3 等号点}✓）$$

## §4 ⚠️ 两个自我纠错（本档记录 ✓✓）

$$\textbf{纠错 1}✗✓\ （\text{C-242 的符号错误}✓）：\text{C-242 写}\ D=-wT+U✗ \Longrightarrow \text{其 }(\star)\ \text{写成}\ |U-wT|✗$$
$$\qquad \text{正确}：D=-wT-U✓ \Longrightarrow |wT+U|✓✓\ \text{（数值核验}：\max|E_1-E_2|=0.51✗\ \text{在旧式}✓，\text{修正后为零}✓）$$
$$\qquad \textbf{影响面}✓：\text{C-242 的【数值结论不受影响}】✓（\text{那里直接验}\max(A,B)-(w\kappa-c_0)✓）；\text{但系数表与一阶条件需按新式重读}✗✓$$

$$\textbf{纠错 2}✗✓\ （\text{斜率配对 bug}✓）：\text{初版用}\ |\tau|\ \text{配单侧斜率}✗ \Longrightarrow \text{误判 j=2/5 失败}✗$$
$$\qquad \text{正确}：\text{系数}=\lambda+\tau\cdot\tilde\Psi'(0^\pm)✓（\text{按}\ \tau u\ \text{的符号选侧}✓）$$

## §5 ⭐ 真正的难点：delicate cancellation（本档新发现 ✓✓）

$$\text{用修正配对计算}✓：j=1：u>0\ \text{方向系数}=+0.0062✓；u<0\ \text{方向}=-0.0058✗$$
$$\qquad \textbf{近相消}✗✓：|\lambda|=2.4329✓\ \text{而}\ |\tau\tilde\Psi'|=2.9735\times0.82=2.4379✓ \Longrightarrow \text{相差仅}\ 0.24\%✗$$
$$\Longrightarrow \textbf{线性近似在}\ u\approx0\ \textbf{处失效}✗✓ \Longrightarrow \text{必须以二阶项闭合}✓$$
$$\qquad \text{二阶项的量级}✓：w(P-\kappa)\ \text{的二阶}\ \sim u^2/w✓；|wT+U|\ \text{的二阶}\ \sim u^2/w✓ \Longrightarrow \text{在}\ |u|\le0.1✓,\ w\ge5✓\ \text{时约}\ 2\times10^{-3}✓ \gg \text{近相消余量}0.0058\times|u|\approx6\times10^{-4}✓✓$$

## §6 状态（依唐先生通过标准 ✓）

| 项 | 状态 |
|---|---|
| (★) 修正版（精确相消） | ✓✓ 建立 |
| 二维→一维精确归约 | ✓✓ 建立（核心推进） |
| 一维不等式（数值） | ✓✓ 五者全部，值 ≈ 0 且极小在 $u=0$ |
| 一阶线性判据 | ✗ 存在 delicate cancellation（0.24%） |
| **一维不等式的解析证明** | ✗ **未完成**（需二阶闭合） |
| C-242 §2 系数表 | ✗ 需按 (★) 修正版重读 |

$$\text{唐先生标准}✓：\textbf{通过}＝|\varepsilon|\le K/w\Longrightarrow\mathcal E_w\ge0\ \text{的逐步解析证明}✓；\ \textbf{不通过}＝\text{只有数值}✗\ \text{或}\ \ge-C/w✗$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 精确相消压缩        命中文件数=1  ::  ./C243-B2-1-II-eta-minimization-exact-1D-reduction.md
技术词 一维精确归约        命中文件数=1  ::  ./C243-B2-1-II-eta-minimization-exact-1D-reduction.md
技术词 近相消阈值          命中文件数=1  ::  ./C243-B2-1-II-eta-minimization-exact-1D-reduction.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界与下一步

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓；\textbf{② 本档含两个自我纠错}✓（§4✓）$$
$$\textbf{③ 归约的价值}✓✓：\text{问题从二维降为}\ \textbf{一维}✓✓（\varphi_2\ \text{已被精确消去}✓）；\text{剩余对象}=\tilde\Psi\ \text{的显式性质}✓$$
$$\textbf{④ 下一步}✓：\text{只需}\ \tilde\Psi\ \text{在}\ [-\tau K,\tau K]\ \text{上的【显式下界}】✓（\text{一维、有限}✓）\ \text{—— 这是比四阶 Taylor 更小的对象}✓✓$$
