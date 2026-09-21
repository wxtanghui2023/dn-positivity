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
