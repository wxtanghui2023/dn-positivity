已查地图（**先查后写**）：`C-280`（**两对空交定理** H_≤∩Z_{1,2}∩Z_{1,4}=∅ ＋ 口径修正）、`C-279`（原点窗口＋无害化分离＋困难类）、`C-278`、`C-277`、`C-276`（零点刻画）、`C-272`（粗箱积压：抽查 70.3% 箱 L<1/2）、`C-181`（GAP-A）。回查见 §7 ✓

D0: 本档对象 = **C-281：两对互补供给的统一余量审计（紧性 → 连续性 → 正下界）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结期内的纯数学闭合（依 §8.1）

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{① L1}✓：\text{参数空间须取}\ \textbf{带宽度下限的箱类}\ \mathcal K_\varepsilon\ \text{（}\min_j(\beta_j-\alpha_j)\ge\varepsilon\text{）}\ \Longrightarrow \textbf{紧}✓✓ \Longrightarrow H_\le\cap\mathcal K_\varepsilon\ \textbf{闭}✓}$$
$$\qquad \textbf{为何必须有下限}✗✓：\S4\ \text{发现}\ \textbf{C-280 退化间隙} —— \text{退化坐标}\ \alpha_j=\beta_j\ \text{时}\ M_p=M_q=\{\beta_j\}\ \text{对}\ \textbf{一切}\ \text{频率对同时 Type B}✗ \Longrightarrow \text{全空间紧性路线失效}✗$$
$$\boxed{\textbf{② L2}✓✓：q_k\ \text{与}\ \Delta\ \text{连续}✓ —— \textbf{用 Hausdorff–Lipschitz 论证}✓，\textbf{不用 argmin 连续}✗（argmin 本身无须连续✓）}$$
$$\boxed{\textbf{③ L3}✓✓：\text{紧}\ \wedge\ \text{连续}\ \wedge\ \text{点态严格正} \Longrightarrow \inf_{\mathcal K_\varepsilon\cap H_\le}\Delta>0✓ \Longrightarrow \textbf{C 级达成（存在性）}✓✓，\textbf{不需求出}\ c_*✗}$$
$$\boxed{\textbf{④ 新缺口}✗✓：\texttt{C-280}\ \S3/\S4\ \text{需}\ \textbf{非退化坐标}；\text{退化情形}\ \textbf{等价于点态命题}（\text{弱于目标、经验支持、未证}✗）\Longrightarrow \text{已追加勘误}✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{未读 pending}✗；\text{未选权重}✗；\textbf{不计算}\ c_*✗；\textbf{不造反向序列}✗$$

## §1 L1：参数空间与紧性（✓✓）

$$\textbf{箱类}✓：\mathcal K_\varepsilon:=\Big\{B=\prod_{j=1}^5[\alpha_j,\beta_j]:\ 0\le\alpha_j,\ \alpha_j+\varepsilon\le\beta_j\le\pi\Big\}✓，\ \varepsilon>0\ \text{固定}✓$$
$$\textbf{紧性}✓✓：\text{每坐标参数}\ (\alpha_j,\beta_j)\ \text{落在闭三角}\ \{0\le\alpha_j,\ \alpha_j+\varepsilon\le\beta_j\le\pi\}✓（\text{闭}✓\ \text{有界}✓）\Longrightarrow \mathcal K_\varepsilon\ \text{是五个紧集的积}\Longrightarrow \textbf{紧}✓✓$$
$$\textbf{闭性}✓：\text{由}\ \S2\ \text{的}\ q_k\ \text{连续}✓（k=1..25\ \text{有限}✓）\Longrightarrow H_\le\cap\mathcal K_\varepsilon=\{B\in\mathcal K_\varepsilon:\max_kq_k\le\tfrac12\}\ \textbf{闭}✓✓$$

$$\textbf{宽度下限的正当性}✓✓（\textbf{不是偷换}✗）：\text{B\&B 只在【认证失败】时分裂}✓，\text{而分裂有深度上限}✓（v4\ \text{maxdep}✓）\Longrightarrow \text{实际被检查的箱}\ \textbf{恒满足}\ \min_j(\beta_j-\alpha_j)\ge\varepsilon_0>0✓$$
$$\qquad \varepsilon_0:=\big(\text{初始格宽}\big)\cdot2^{-\text{maxdep}}✓ \Longrightarrow \text{证书路径箱类}\ \subseteq\mathcal K_{\varepsilon_0}✓✓$$
$$\qquad \textbf{因此}✓：\text{在}\ \mathcal K_{\varepsilon_0}\ \text{上证明统一余量} \Longrightarrow \textbf{对实际证书路径成立}✓✓（\text{且是}\ \textbf{更强} \text{的陈述}✓，\textbf{不是扩大目标类}✗）$$
$$\qquad \textbf{同时诚实标注}✗：\text{退化／超薄箱不属于该论证范围}✓（见\ \S4✓）$$

## §2 L2：连续性（**不用 argmin 连续**✓✓）

$$\textbf{引理（min 的 Hausdorff–Lipschitz 性）}✓✓：f\ \text{为}\ L\text{-Lipschitz}✓，I,I'\ \text{非空紧}✓ \Longrightarrow \Big|\min_I f-\min_{I'}f\Big|\le L\cdot d_H(I,I')✓$$
$$\qquad \textbf{证明}✓：\text{取}\ \theta^*\in I'\ \text{使}\ f(\theta^*)=\min_{I'}f✓；\exists\theta\in I:\ |\theta-\theta^*|\le d_H(I,I')✓ \Longrightarrow \min_If\le f(\theta)\le f(\theta^*)+L\,d_H=\min_{I'}f+L\,d_H✓；\text{对称}✓ \blacksquare$$
$$\qquad \textbf{注}✓✓：\text{全程}\textbf{不提}\ \operatorname{argmin}\ \text{连续}✗（\text{argmin 可跳变}✓，\text{与结论无关}✓）$$

$$\textbf{推论}✓✓：\alpha_j,\beta_j\mapsto\min_{[\alpha_j,\beta_j]}\cos(k\theta)\ \text{连续}✓（\|(\cos k\cdot)'\|\le k✓） \Longrightarrow q_k\ \text{连续}✓$$
$$\qquad \delta_{I_j}(p,q;\lambda):=\min_{I_j}[\lambda\cos p\theta+(1-\lambda)\cos q\theta]-\lambda\min_{I_j}\cos p\theta-(1-\lambda)\min_{I_j}\cos q\theta\ \textbf{连续}✓（\text{三项皆连续}✓）$$
$$\qquad \Delta(B):=\alpha_{12}\sum_j\delta_{I_j}(1,2;\lambda_{12})+\alpha_{14}\sum_j\delta_{I_j}(1,4;\lambda_{14})\ \textbf{连续}✓✓（\text{有限和}✓）$$

## §3 L3：正下界（**C 级存在性**✓✓）

$$\textbf{点态严格正}✓：\text{由}\ \texttt{C-280}\ \text{主定理}✓：H_\le\cap Z_{1,2}\cap Z_{1,4}=\varnothing✓，\text{而}\ \Delta(B)=0\iff\delta_B(1,2)=\delta_B(1,4)=0\iff B\in Z_{1,2}\cap Z_{1,4}✓（\alpha>0,\ \delta\ge0✓）$$
$$\qquad \Longrightarrow \Delta(B)>0\ \ \forall B\in H_\le\cap\mathcal K_\varepsilon✓✓$$
$$\textbf{取值性}✓：H_\le\cap\mathcal K_\varepsilon\ \textbf{紧}✓ ＋ \Delta\ \textbf{连续}✓ \Longrightarrow \text{最小值在}\ B^*\ \text{取到}✓ \Longrightarrow \boxed{\inf_{H_\le\cap\mathcal K_\varepsilon}\Delta=\Delta(B^*)>0}✓✓$$
$$\textbf{结论}✓✓：\exists c_*>0:\ \Delta(B)\ge c_*\ \ \forall B\in H_\le\cap\mathcal K_\varepsilon✓ \Longrightarrow \textbf{C 级出口达成（存在性）}✓✓，\textbf{且不需求}\ c_*\ \text{的值}✗✓$$

$$\textbf{重要澄清}✓✓：\text{本刀}\textbf{不} \text{再需要「造序列}\ \Delta(B_n)\to0」\ \text{来反向判死}✗ —— \text{紧性＋连续性}\Longrightarrow \textbf{该通道自动关闭}✓✓（\text{唐先生判断正确}✓）$$

## §4 新发现的退化间隙 ＋ `C-280` 勘误（✗✓）

$$\textbf{缺口}✗✓：\texttt{C-280}\ \S3\ \text{断言}\ \text{Type B}(1,2)\iff\beta_j\le\tfrac{\pi}{2}✓ —— \textbf{该等价对退化区间失效}✗：$$
$$\qquad \text{若}\ \alpha_j=\beta_j\ \text{则}\ I_j\ \text{是单点} \Longrightarrow M_p=M_q=\{\beta_j\}\ \forall p,q \Longrightarrow \textbf{对一切频率对同时 Type B}✗（\text{与}\ \beta_j\ \text{无关}✓）$$
$$\qquad \Longrightarrow \texttt{C-280}\ \S3/\S4\ \text{须补前提}\ \boxed{\alpha_j<\beta_j}✓ \Longrightarrow \S5\ \text{的主定理}\ \textbf{成立于非退化箱类}✓$$
$$\textbf{退化情形的等价化}✓✓：\text{全退化}\ B=\{\theta\}\in H_\le \iff \max_{1\le k\le25}\sum_j\cos(k\theta_j)\le\tfrac12✓，\textbf{即点态命题}✓$$
$$\qquad \textbf{性质}✓：\text{该点态命题}\ \textbf{弱于}\ m_5\ge\tfrac12✗（\text{仅一点处}✓），\textbf{未被本刀证明}✗ \Longrightarrow \text{登记为遗留}✓$$
$$\qquad \textbf{经验支持}⚠️✓：\texttt{C-272}\ \text{抽查}\ 100\%\ \text{箱的采样点上}\ \max_k\sum\cos>\tfrac12✓ \Longrightarrow \text{未发现反例}✓$$

$$\textbf{勘误处置}✓（追加不覆盖✓）：\texttt{C-280}\ \text{追加}\ \S9\ \text{勘误指针}✓，\S3/\S4\ \text{补}\ \alpha_j<\beta_j✓$$

## §5 出口判定（✓✓）

$$\boxed{\textbf{C 级达成}✓✓（\text{在}\ \mathcal K_\varepsilon\ \text{上，}\varepsilon>0\ \text{任意固定}✓）：\exists c_*>0:\ \Delta\ge c_*\ \text{于}\ H_\le\cap\mathcal K_\varepsilon✓}$$
$$\qquad \textbf{虚警防护}✓：\text{若}\ H_\le\cap\mathcal K_\varepsilon=\varnothing\ \text{则命题}\textbf{空洞真}✗；\text{经验上}\ H_<\ \text{非空}⚠️✓（\texttt{C-272}\ \text{抽查}\ 70.3\%\ \text{箱}\ L<\tfrac12✓）$$
$$\textbf{两个问题必须分开}✓✓（唐先生纪律）：\text{① 结构性统一供给＝本刀已得}✓；\text{② }c_*\ \text{多大／是否够实用阈值}\ \tfrac12-\tfrac{q_p+q_q}{2}✗＝\textbf{后续独立问题}✓ \Longrightarrow \textbf{本刀不碰}✗$$

## §6 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{未读 pending}✓；\text{未选权重}✗（\lambda,\alpha\ \text{任意固定即成立}✓）；\textbf{未计算}\ c_*✗$$
$$\textbf{② 结论范围}✓：\text{只覆盖两对}\ (1,2),(1,4)✓\ \text{与}\ \mathcal K_\varepsilon\cap H_\le✓；\textbf{不覆盖退化／超薄箱}✗（\S4✓）$$
$$\textbf{③ 未用}\ RH✓；\text{未改他档正本}✓（\texttt{C-280}\ \text{为追加勘误}✓）；\text{未动}\ v4✓；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$
$$\textbf{④ 不声称}✓：\text{不声称}\ c_*\ \text{足够大}✗；\text{不声称退化情形已解}✗；\text{不声称}\ M=5\ \text{可闭合}✗$$

## §7 【技术词回查】输出（**先跑后写**✓）

```
技术词 带下限箱类 命中文件数=0    ::
技术词 退化间隙   命中文件数=0    ::
技术词 存在性闭合 命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{min 的 Lipschitz 性}✓（\text{经典}✓）；\text{零点刻画}✓（\texttt{C-276}✓）；\text{两对空交定理}✓（\texttt{C-280}✓）；\text{困难类}✓（\texttt{C-279}✓）$$

---

## §8 定理范围降级 ＋ 路径宽度封死 ＋ 新缺口（2026-09-21 唐先生指令 ✓）

### §8.1 C 级降级为 $C_\varepsilon$（**严格表述**✓✓）

$$\textbf{正确表述}✓✓（\textbf{不得}简称「无条件 C 级统一余量」✗）：$$
$$\qquad \boxed{\forall\varepsilon>0,\ \exists c_*(\varepsilon)>0:\ \Delta(B)\ge c_*(\varepsilon)\quad\forall B\in H_\le\cap\mathcal K_\varepsilon}✓$$
$$\qquad \textbf{而非}✗：\inf_{B\in H_\le}\Delta(B)>0\quad（\text{退化点会摧毁全空间统一余量}✗，见\ \S4✓）$$
$$\textbf{定名}✓：\textbf{带宽度下限箱类上的统一 coupling gap}（记\ C_\varepsilon✓），\text{不得写成无条件 C}✗$$

### §8.2 路径宽度下限引理（**已按代码封死**✓✓）

$$\textbf{代码证据}✓✓（\texttt{scripts/rpm\_certificate\_v4.py}）：$$
$$\qquad \text{L142：}\texttt{jm = argmax(wid)} \Longrightarrow \textbf{只取最宽维}✓；\qquad \text{L143：}\texttt{mid = (A+B)/2} \Longrightarrow \textbf{只取中点}✓$$
$$\qquad \text{L144–146：两子箱共享 mid，}Dn=Dq+1 \Longrightarrow \textbf{每次分裂恰把一个坐标二等分}✓$$
$$\qquad \Longrightarrow \textbf{无} \text{非均匀分裂}✗、\textbf{无} \text{提前按坐标细分}✗、\textbf{无} \text{重切／合并}✗✓$$
$$\textbf{引理}✓✓：\text{叶箱深度}\ d\le D_{\max} \Longrightarrow \text{每个坐标被二等分}\le d\ \text{次} \Longrightarrow \min_j(\beta_j-\alpha_j)\ \ge\ h\cdot2^{-D_{\max}}\cdot(1-\delta_{\rm fp})✓$$
$$\qquad h=\tfrac{P_f}{N_0}✓（\text{初始格宽}✓）；\delta_{\rm fp}＝中点浮点舍入累积余量✓ \Longrightarrow \textbf{取}\ \varepsilon_0:=h\cdot2^{-(D_{\max}+2)}>0✓✓$$
$$\qquad \Longrightarrow \text{L137–139：超限箱计未决并丢弃}✓ \Longrightarrow \textbf{成功运行（未决=0）中所有认证箱}\subseteq\mathcal K_{\varepsilon_0}✓✓$$
$$\textbf{实参}✓：\text{M=5 运行}\ (N_0=12,\ P_f\approx\pi,\ D_{\max}=80) \Longrightarrow h\approx0.2618 \Longrightarrow \varepsilon_0\approx5.4\times10^{-26}>0✓$$

### §8.3 ⚠️ 新缺口：域端点 $P_f$ 略小于 $\pi$（✗✓ **v4 回归**）

$$\textbf{事实}✗✓：\texttt{L94}\ P_f=\texttt{float(Decimal(}\pi\texttt{))}=\texttt{math.pi}=3.141592653589793✓，\text{而}\ \pi=3.141592653589793238\ldots \Longrightarrow P_f<\pi\ \text{差}\approx1.22\times10^{-16}✓$$
$$\qquad \Longrightarrow \text{域}\ [0,P_f]^5\subsetneq[0,\pi]^5✓ \Longrightarrow \textbf{漏掉薄片}\ \{\varphi:\ \exists j\ \varphi_j\in(P_f,\pi]\}✗$$
$$\textbf{对照}✓：\texttt{scripts/m3\_certificate\_interval\_arith.py}\ \text{用}\ P=\texttt{PI\_HI}=\tfrac{3141592653589794}{10^{15}}>\pi✓（\text{严格覆盖}✓）；\texttt{C-224}\ \text{亦如此}✓$$
$$\qquad \Longrightarrow \textbf{这是 v4 引入的回归}✗✓（\text{老证书无此问题}✓）$$
$$\textbf{后果}✗：\text{v4 的「}\forall\varphi\in[0,P_f]^5」\ \textbf{不足以} \text{推出}\ \forall\varphi\in[0,\pi]^5✗ \Longrightarrow \textbf{须修复}✓$$
$$\qquad \textbf{修法}✓：P_f\leftarrow\texttt{nextafter}(\pi,+\infty)✓\ \text{或直接复用有理}\ \texttt{PI\_HI}✓ \Longrightarrow \textbf{需重跑}✓ \Longrightarrow \text{登记为遗留}✓$$
$$\qquad \textbf{性质}⚠️✓：\text{不影响本档的}\ C_\varepsilon\ \text{结论}✓（\text{那是在抽象箱类上证的}✓）；\text{只影响 v4 的数值证书覆盖}✗$$

### §8.4 `C-282` 预注册（**阈值桥审计**，暂不执行 ✓）

$$\textbf{桥}✓：\text{由 pair}\ (p,q)\ \text{的证书需}\ \Delta(B)>\Gamma_{p,q}(B):=\tfrac12-\tfrac{q_p(B)+q_q(B)}{2}✓（\text{即}\ \inf_B H_\lambda>\tfrac12\Lambda✓，见\ \texttt{C-281}\ \S3✓）$$
$$\qquad \Longrightarrow \text{真正待证}✓：\boxed{\inf_{B\in H_\le\cap\mathcal K_{\varepsilon_0}}\big[\Delta(B)-\Gamma(B)\big]\ >\ 0\ ?}✓$$
$$\textbf{预注册判据}✓✓（\text{进入计算前必须先写}✗）：\text{① 成功＝给出显式正下界或严格闭合的紧性论证}✓；\text{② 失败＝只能给数值证据}✗；\text{③ 禁止无界数值搜索}✗；\text{④ 先定}\ \varepsilon_0\ \text{与}\ \Gamma\ \text{的定义域}✓$$
$$\textbf{战略链条}✓✓：H_\le\stackrel{\texttt{C-280}}{\Longrightarrow}\text{两对不能同时零耦合}\stackrel{\texttt{C-281}}{\Longrightarrow}\Delta\ge c_*(\varepsilon)>0✓$$
$$\qquad \textbf{但}\ \textbf{不得} \text{写成「M=5 已可证」}✗ —— \text{所缺正是}\ c_*(\varepsilon)\ \text{vs}\ \Gamma(B)\ \text{这道阈值桥}✗✓$$
