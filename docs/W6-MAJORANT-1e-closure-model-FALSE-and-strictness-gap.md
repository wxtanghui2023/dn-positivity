# ⚔️ W6-MAJORANT-1 **收口**：模型层跨墙 FAIL ＋ **严格化缺口精确定位**

> 依唐先生 12:47 指令：把第 8 步（$\Phi^2$ 近似误差做成严格下界）真正算出来 ✓
> **本档结果**：定量账采纳；**严格化撞上一个明确缺口＝窗口过渡层结构未给出** ✓✓

---

## §1 唐先生定量账（**照录采纳**）

$$\text{dyadic block}\ n\asymp X：\ \sum_{n\sim X}a_n^2\asymp\log X;\qquad \text{模型}\ |\alpha_n|\asymp\frac{c^2}{\log X}✓$$
$$\Longrightarrow\ \sum_{n\sim X}a_n^2|\alpha_n|^2\asymp\frac{c^4}{\log X} \Longrightarrow \|a\|_2\asymp(\log X)^{1/2},\quad \|a\alpha\|_2\asymp\frac{c^2}{(\log X)^{1/2}}✓$$
$$\Longrightarrow\ \boxed{\|a\|_2\|a\alpha\|_2\asymp c^2}\quad(\textbf{"}L\ \text{消失"的量化版本})✓✓$$

$$\text{但离散网格密度不变}：\frac{dn}{dy}=e^y\asymp X \Longrightarrow \sum_mS_B(y_n-y_m)z_m\sim X\!\int\!S_B\,z \Longrightarrow \boxed{\text{离散尺度}=X}✓✓$$
$$\text{调制}\ e^{\pm iTt/2}\ \textbf{只平移连续频带}\ [-3T/2,3T/2]\to[T,2T]，\ \textbf{不改变网格密度}✓$$
$$\Longrightarrow\ \boxed{\|K_T\|\gtrsim\frac{X}{\log X};\ \text{两侧}\ a_n\ \text{精确纳入后整体 bilinear 尺度}\ O(X)\ \textbf{而非}\ O(T)}✓✓$$
$$\boxed{\textbf{"}L\ \text{消失是真的；}X\ \text{消失没有发生"}}✓✓✓$$

$$\text{对照 MV}\ |O_1|_{\rm MV}\ll L^2X \to \text{最乐观}\ |O_1|\lesssim X(\log X)^{O(1)};\qquad D=\frac T\pi\sum a_n^2g(\log n)\asymp TL^2✓$$
$$\Longrightarrow\ \frac{|O_1|}{D}=T^{-1}X(\log T)^{-O(1)} \xrightarrow{\ X=T^{1+\eta}\ }\ \boxed{\frac{|O_1|}{D}\gtrsim\frac{T^\eta}{(\log T)^{O(1)}}}✓✓$$
$$\Longrightarrow\ \boxed{\log\text{-saving}\ \ll\ T^\eta\text{-saving}}\quad(\text{两个不同数量级层次})✓✓$$

## §2 振荡救不了（照录）
$$\frac L2\log n\ \text{的周期}\ \Delta y\asymp\frac1L；\ \text{网格}\ \Delta y\asymp\frac1X \Longrightarrow \textbf{每个}\ \alpha\text{-相干块含}\ \asymp\boxed{\frac XL}\ \textbf{个整点}✓✓$$
$$\Longrightarrow\ \text{可把测试向量限制在一个}\ \textbf{同号同相位局部块} ⟹ \textbf{"振荡}\Rightarrow\ell^2\ \text{自动幂级 cancellation"}\ \textbf{被摧毁}✓✓$$

## §3 ⭐⭐⭐ **第 8 步：严格化缺口（本档核心，逐行算）**

$$\text{§5.2 逐字}：\mathbf 1_{[-L/2+w,\,L/2-w]}\le\phi^2\le\phi\le\mathbf 1_{[-L/2,\,L/2]} \Longrightarrow \phi\equiv1\ \text{on}\ [-L/2+w,L/2-w]✓$$
$$\Phi=c\phi^2\Longrightarrow\Phi^2=c^2\phi^4,\qquad \text{记}\ \eta_4:=1-\phi^4\ (\operatorname{supp}\eta_4\subset\text{两层宽}\ w\ \text{的边界带})✓$$
$$\alpha_n=c^2\Big[\underbrace{\frac{2\sin(Ly_n/2)}{y_n}}_{\rm Main}-\underbrace{\widehat{\eta_4}(y_n)}_{\rm Err}\Big],\qquad y_n=\log n✓✓$$

### §3.1 误差的**可用界**
$$\text{只用 (§5.2) 能得到的只有}\ L^1\ \text{界}：|\widehat{\eta_4}(y)|\le\|\eta_4\|_{L^1}\le2w=\boxed{2}✓$$
$$\text{而}\ |\rm Main|\asymp\frac{2}{|\log n|}\ (\text{峰处})✓$$
$$\Longrightarrow\ \textbf{当}\ |\log n|\gg1\ \text{时}\ |\rm Err|\le2\ \textbf{与}\ |\rm Main|\ \textbf{同阶或更大} \Longrightarrow \textbf{无法给出}\ |\alpha_n|\gg\frac1{\log X}\ \text{的严格下界}✓✗✓$$

### §3.2 论文确实**没有**提供更强的过渡层信息
$$\text{(5.3) 逐字}：|\hat\phi(r)|\le\vartheta(r)=\min(L,\ \tfrac2{|r|},\ \tfrac{C_\chi w}{r^2}) \Longrightarrow \text{中段只按}\ \frac2{|r|}\ \text{衰减}$$
$$\qquad\Longrightarrow\ \phi\ \textbf{本质上是"锐利指示函数"}（w=1\ \text{窄过渡}），\ \mathbf{其傅里叶衰减与主项}\ \frac{2\sin(Ly/2)}{y}\ \textbf{同阶}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{主项与误差项同阶} \Longrightarrow \text{论文假设内}\ \textbf{无法分离}}✓✓✓$$

## §4 **判定**（照录并采纳唐先生的状态表）

| 项 | 状态 |
|:--|:--|
| 裸 Hilbert 障碍 | **FALSE**（已消除 ✓） |
| 纯带限降阶 | **FALSE** |
| $\alpha$-权消除 $L$ | **TRUE** ✓ |
| $\alpha$-振荡产生幂级 cancellation | **FALSE（模型层面）** |
| $X=T^{1+\eta}$ 所需 power saving | **未获得** |

$$\boxed{\textbf{W6-majorant-1}\ =\ \textbf{LOCAL ALIVE}，\ \text{但跨越}\ X>T\ \textbf{的主机制 FAIL}}✓✓$$
$$\qquad(\text{不是 W6 整体 FALSE；而是}\ \textbf{该机制精准化失败})✓$$

## §5 ⚠️ 严格化的**精确缺口**（须登记，不得省略）
$$\text{唐先生要求}：\Phi^2=c^2\mathbf 1_{[-L/2,L/2]}+E_L，\ \text{证在一个相干块}\ \mathcal I\ \text{上}\ |\widehat{E_L}(\log n)|\le\tfrac12|\widehat{c^2\mathbf 1}(\log n)|✓$$
$$\textbf{本档结果}：\text{该不等式}\ \textbf{不能} \text{由 (§5.2)--(5.4) 推出}——\text{因}\ |\widehat{\eta_4}|\le2\ \textbf{不衰减} \text{，而主项}\asymp\frac2{\log n}✓✗✓$$
$$\Longrightarrow\ \boxed{\text{严格 FALSE 只能达到}\ \textbf{模型层}（\phi\ \text{取锐利指示}，w\to0）}✓✓$$
$$\qquad\text{模型层}：\eta_4\equiv0,\ |\alpha_n|=\frac{2c^2|\sin(Ly_n/2)|}{y_n} \Longrightarrow \text{相干块}\ (|\sin|\gg1)\ \text{上}\ |\alpha_n|\gg\frac1{\log X}✓✓$$
$$\qquad\Longrightarrow\ \lambda_{\max}\gtrsim\frac{X}{(\log X)^{O(1)}}\ \textbf{可写成严格命题（模型层）}✓✓$$

## §6 **jam 位置（TACTICAL ATTACK 的四结果标注）**
$$\boxed{\textbf{C 工具失效}，\ \text{卡点＝}\textbf{缺失输入}：\Phi^2\ \text{过渡层结构（决定}\ \widehat{\eta_4}\ \text{能否与主项分离）}\ \textbf{未在论文 (§5.2)--(5.4) 中给出}}✓✓✓$$
$$\text{两种收口方式}：\text{(i)}\ \text{把}\ \phi\ \text{的过渡层额外假设写入（}\phi\in C^\infty\ \text{且过渡宽}\ w\gg\frac1L？\text{）} \Longrightarrow \widehat{\eta_4}\ \text{快衰} \Longrightarrow \text{严格 FALSE}✓$$
$$\qquad\text{(ii)}\ \textbf{绕过}\ \alpha_n\ \text{下界} \text{，改用}\ \textbf{均方＋Parseval 型} \text{论据（dyadic block 上}\ \sum_{n\sim X}|\alpha_n|^2\ \text{与}\ \int|\Phi^2|^2\ \text{的关系）}✓✓$$

## §7 边界
$$\text{(i)}\ §1--§2\ \text{照录唐先生 12:47}✓\quad\text{(ii)}\ §3\ \text{为本档计算（}(5.2)\to\phi\equiv1\ \text{内区＋}\ L^1\ \text{界}\ \le2w）✓$$
$$\text{(iii)}\ \text{(5.3) 的"锐利指示"读法为}\ [\textbf{结构}]✓\quad\text{(iv)}\ \textbf{未用 RH／HL／pair correlation}；\ \textbf{零数值}✓$$
