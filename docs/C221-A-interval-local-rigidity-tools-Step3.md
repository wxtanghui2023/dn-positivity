已查地图（**先查后写**）：查 `C-220`（闭合审计）、`C-206`（层 2 三件套）、`C-210`（E1 勘误：$\delta_A$ 项）、`C-211`（免容差自洽性）、`C-215` §2（内核缺口警告）。回查见 §8 ✓

D0: 本档对象 = **A：区间局部刚性工具（Step 3 区间化）** —— 关系 = 把层 2 三件套变为层 1 可拼接引理
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 范围（唐先生 2026-09-20 13:31 卡定）

$$\textbf{只做 Step 3}✓；\textbf{不碰} \text{interval Newton}（\text{属 B}）✗；\textbf{不碰} \text{盒外 B\&B}（\text{属 C}）✗$$
$$\textbf{逻辑护栏}：\textbf{禁止}在本档写\ \delta_A=0✗ —— \text{合法来源只有}\ \text{B 的 interval Newton}＋\text{KKT 严格包含}✓$$
$$\qquad \Longrightarrow \text{本档只交付}：\text{隔离数据}＋\text{一阶凸包}\ c\ ＋\text{二阶界}\ R✓（\text{全部区间可认证}✓）；\ \textbf{相切条件留作 B 的输入}✓$$

## §1 A 的引理（**条件式**，不含相切）

$$\textbf{引理 A}：\text{设}\ X_{\rm ref}\ \text{为}\ x^*\ \text{附近半宽}\ \le10^{-6}\ \text{的参考盒}✓,\ A=\{1,5,11,13\}✓,\ R=\max_{k\in A}k^2=169✓,\ c_X=0.319306988✓,\ \rho_{\rm up}=1.4658\times10^{-3}✓$$
$$\qquad \text{则}\ \forall x\in X_{\rm ref}\ \text{与}\ \forall\|\delta\|\le\rho_{\rm up}：$$
$$\boxed{\ F_3(x+\delta)\ \ge\ \min_{k\in A}S_k(x)\ +\ c_X\|\delta\|\ -\ \tfrac{R}{2}\|\delta\|^2\ }✓$$
$$\qquad \textbf{若另有相切}\ S_k(x)=S_{k'}(x)\ \forall k,k'\in A（\textbf{由 B 提供}✓），\text{则升级为}$$
$$\boxed{\ F_3(x+\delta)\ \ge\ F_3(x)\ +\ c_X\|\delta\|\ -\ \tfrac{R}{2}\|\delta\|^2\ \ge\ F_3(x)+2.87\times10^{-4}\ >\ F_3(x)\ }✓✓（0<\|\delta\|\le\rho_{\rm up}✓）$$
$$\qquad \text{即：}\ \rho_{\rm up}<\rho_{\rm iso}\ \text{故二次项不绑定}✓ \Longrightarrow \text{边界裕量}\ c_X\rho_{\rm up}-\tfrac{R}{2}\rho_{\rm up}^2=2.87\times10^{-4}>0✓✓$$

## §2 区间机械（本档实际做的）

$$\textbf{(i) 精确可分区间求值}✓✓（\text{不用粗糙 Lipschitz 界}✗）$$
$$\qquad S_k\ \text{在盒上的极值}=\sum_j\min/\max_{\varphi_j\in[c_j-H,c_j+H]}\cos(k\varphi_j)✓（\text{临界点：奇/偶倍}\pi✓）$$
$$\qquad \nabla S_k\ \text{各分量}=-\ k\sin(k\varphi_j)\ \text{的值域}✓（\text{临界点：}\tfrac{\pi}{2}+2m\pi\ /\ \tfrac{3\pi}{2}+2m\pi✓）$$
$$\qquad \Longrightarrow \text{与 B\&B 用同一套精确求值}✓✓；\textbf{值域抽样核验}：45\ \text{组}\times2000\ \text{点，越界}\ \mathbf{0}✓✓$$
$$\textbf{(ii) 一阶凸包}\ c：\text{facet 法（正确符号约定}✓：0\ \text{与 apex 同侧为内部}✓）＋\text{扰动界}✓$$
$$\qquad c_X=c(\text{中点})-\varepsilon✓,\quad \varepsilon=\max_{k\in A}\|\text{半宽向量}\|_2✓ \Longrightarrow \text{含}\ \textbf{containment 证书}✓（0\in\mathrm{int}\,\mathrm{conv}✓，\texttt{C-210}\ §4④\ \text{的教训}✓）$$
$$\textbf{(iii) 二阶界}：R=\max_{k\in A}k^2=169✓（\textbf{解析严格}✓✓，无需区间）$$

## §3 ⭐ 关键修正：**两个半径必须分开**

$$\textbf{层 2 版（}\texttt{C-206}\text{）}：\text{用同一个球半径同时算隔离与覆盖}✗ \Longrightarrow \Delta\ \text{被【球上的 sup/inf】吃小}✗ \Longrightarrow \text{自洽与不自洽混在一起}✗$$
$$\textbf{正确版}✓✓：\textbf{隔离}用【参考盒】\ X_{\rm ref}\ \text{的 sup/inf}✓（\text{因}\ x\in X_{\rm ref}\ \text{而}\ x+\delta\in X_{\rm ref}\oplus B(0,\rho)✓ \Longrightarrow S_k(x+\delta)\le\sup_{X_{\rm ref}}S_k+L_k\|\delta\|✓）；$$
$$\qquad \textbf{覆盖}必须用【球】\ B(0,\rho)\ \text{的均值形式}✓（\text{因均值形式要}\ \nabla S_k\ \text{在【中间点】}✓，\text{而中间点在球内}✓）$$
$$\qquad \Longrightarrow \Delta_{\rm ref}=0.071085496✓（\text{几乎就是点值}✓）,\ \rho_{\rm iso}=\Delta_{\rm ref}/(L_{\rm non}+L_{\rm act})=1.4658\times10^{-3}✓$$
$$\qquad \Longrightarrow \text{定点迭代}\ \rho=\min(\rho_{\rm iso},\ 2c(\rho)/R)✓ \Longrightarrow \rho_{\rm up}=1.4658\times10^{-3}✓ \text{（受隔离限制✓，非二次项✓）}$$
$$\qquad \textbf{结论}：\texttt{C-206}\ \text{的}\ 1.4658\times10^{-3}\ \textbf{数值幸存}✓✓，\text{但其【理由】必须按本节修正}✓（\text{这是我上一版代码混用半径后自查发现的}✓）$$

## §4 本档数值（$\texttt{/tmp/c221\_A.json}$）

| 量 | 值 | 严格性 |
|---|---|---|
| $\Delta_{\rm ref}$ | $0.071085496$ | 区间（精确可分求值）✓ |
| $\rho_{\rm iso}=\Delta_{\rm ref}/(L_{\rm non}+L_{\rm act})$ | $1.4658\times10^{-3}$ | 区间 ✓ |
| $c(\text{ball})$ | $0.540242563$ | facet ＋ 抽样核验 ✓ |
| $\varepsilon$（球上梯度半宽） | $2.2094\times10^{-1}$ | 区间 ✓ |
| $c_X=c-\varepsilon$ | $0.319306988$ | **含 containment** ✓ |
| $R$ | $169$ | 解析 ✓ |
| $\rho_{\rm up}$ | $1.4658\times10^{-3}$ | 定点 ✓ |
| 边界裕量 $c_X\rho_{\rm up}-\tfrac{R}{2}\rho_{\rm up}^2$ | $2.87\times10^{-4}$ | $>0$ ✓✓ |

## §5 本档**不**主张（护栏）

$$\text{✗ 不写}\ \delta_A=0（\text{属 B}✓）；\ \text{✗ 不写}\ x_0^*\ \text{是极小}✗；\ \text{✗ 不写}\ m_3=F(x_0^*)✗；\ \text{✗ 不写唯一性}✗$$
$$\qquad \text{本档只备好}\ (c_X,R,\rho_{\rm up},X_{\rm ref}\ \text{接口})✓，\text{等 B 注入相切后即可升级}✓$$

## §6 本档自我失误（第 38 次，三条）

$$\textbf{38a 单位错}✗✗：\text{把}\ \varphi/\pi\ \text{当}\ \varphi\ \text{用}✗（\texttt{a=k*(c±H)}\ \text{漏因子}\ \pi✗） \Longrightarrow \text{梯度与值域全错}✗（\text{表现为}\ \Delta\approx-3.2✓、c\approx0.137✓） \Longrightarrow \text{修正}：x_c=(\nicefrac{p}{q})\cdot\pi✓$$
$$\textbf{38b 替换吞行}✗：批量替换把\ \texttt{mn=min(...)}\ \text{并进注释}✗ \Longrightarrow \texttt{UnboundLocalError}✗ \Longrightarrow \text{单行修掉}✓$$
$$\textbf{38c 半径混用}✗✗（\textbf{最实质}）：\text{用同一}\ H\ \text{既算隔离又算覆盖}✗ \Longrightarrow \text{误得"无自洽档"✗} \Longrightarrow \text{分开后}\ \rho_{\rm up}=1.4658\times10^{-3}✓✓$$
$$\qquad \textbf{教训}：\text{隔离与覆盖的【取值域】不同}✓ —— \text{前者参考盒}✓，\text{后者球}✓；\text{混用会同时高估与低估}✗$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 区间局部刚性 命中文件数=1    ::  ./C221-A-interval-local-rigidity-tools-Step3.md
技术词 两个半径分开 命中文件数=1    ::  ./C221-A-interval-local-rigidity-tools-Step3.md
技术词 参考盒       命中文件数=1    ::  ./C221-A-interval-local-rigidity-tools-Step3.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界与下一步

$$\textbf{边界}：§1 引理为【条件式】✓（相切未证✗）；$c_X$ 依赖 facet 法与抽样核验✓，\text{尚未做第二独立实现}⚠️；$$
$$\qquad \text{值域函数已抽样核验}✓（45\times2000✓，越界 0✓），\text{但\{i\}的严格性最终仍需】区间重写}⚠️（\text{留待 A 定稿}✓）$$
$$\qquad \text{未用 RH}✓；\text{未改他档}✓；\text{丙（全域 cover）仍不开}✓$$
$$\textbf{下一步}：\textbf{B}：\text{interval Newton 求严格盒}\ X_0✓（\text{同时注入相切、消掉}\ \delta_A\ \text{内核缺口}✓✓） \Longrightarrow \text{引理 A 自动升级为【无条件局部增长】}✓✓$$
