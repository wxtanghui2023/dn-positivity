已查地图（**先查后写**）：`C-278`（二倍族统一供给 DEAD ＋ §8 两条钉死）、`C-277`（Type A/B ＋ 阈值引理 ＋ 几何不强制 r≥1）、`C-276`（零点刻画 δ=0 ⟺ M_p∩M_q≠∅ ＋ §9 勘误）、`C-275`（组合空洞 ＋ 危险频率集合 D(I_j) ＋ ∪_j D 覆盖判据）、`C-274`、`C-272`、`C-181`（u≤5，GAP-A）。回查见 §8 ✓

D0: 本档对象 = **C-279 第一刀：共同坏窗口／最小值同步结构审计**（对任意有限频率族，**零计算**）
D1: 0
FREEZE-ACK: 本档即冻结期内的纯数学审计（依 §8.1）

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{① 原点窗口定理（对}\textbf{任意}\text{有限频率族}✓✓）：\text{设族内最大频率为}\ Q，\varepsilon:=\tfrac{\pi}{Q}✓。\text{则}\ \forall I=[\alpha,\beta]\subset(0,\varepsilon)：\text{族内}\ \textbf{每一对}\ \text{均}\ \delta_I\equiv0✗}$$
$$\qquad \Longrightarrow \textbf{预注册出口 A 对「全体区间」口径}\textbf{命中}✗✓（任何有限族都无法做到「所有区间都有供给」）$$
$$\boxed{\textbf{② 但该区域对证书}\textbf{无害}✓✓：\text{五坐标皆}\ I_j\subset(0,\tfrac{\pi}{25})\ \text{时，}\ q_1=\sum_j\min_{I_j}\cos(\theta_j)\ \ge\ 5\cos\tfrac{\pi}{25}\approx4.96\gg\tfrac12✓}$$
$$\qquad \Longrightarrow \text{该类箱由}\ \textbf{k=1 的可分界直接认证}✓✓ \Longrightarrow \text{耦合机制在此}\textbf{不被需要}✗✓$$
$$\boxed{\textbf{③ 故必须}\textbf{重定义目标类}✓✓：\text{取}\ \textbf{困难类}\ \mathcal H:=\{B:\ \max_{1\le k\le25}q_k(B)<\tfrac12\}✓（\text{证书失效的箱}✓，\textbf{结构性定义}✓，\text{非搜索结果}✓）}$$
$$\qquad \Longrightarrow \mathcal H\ \cap\ \{\text{全窄近原点}\}=\varnothing✓（\text{由}\ \text{②}✓） \Longrightarrow \text{出口 A}\ \textbf{不适用于}\ \mathcal H✗✓$$
$$\boxed{\textbf{④ 遗留问句}✓：\text{在}\ \mathcal H\ \text{上，耦合族是否有}\textbf{统一供给}✓？\ \textbf{未决}✗ \Longrightarrow \text{下一刀}✓；\textbf{B 不是成功}✗，\textbf{C 才是}✓✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{未读 pending 样本}✗；\text{未选权重}✗；\textbf{未碰五维箱实验}✗；\text{不碰 GAP-A}✗$$

## §1 原点窗口定理（**证明**✓✓）

$$\textbf{定理}✓✓：\text{设}\ \mathcal P\ \text{为有限频率对族}，\text{全部频率}\le Q✓。\varepsilon:=\tfrac{\pi}{Q}✓。\text{则}\ \forall I=[\alpha,\beta]\subset(0,\varepsilon)\ \text{与}\ \forall(p,q)\in\mathcal P：M_p(I)=M_q(I)=\{\beta\}\Longrightarrow\delta_I(p,q)=0✓$$
$$\textbf{证明}✓：\forall x\in I，\forall k\le Q：kx\in(0,k\beta)\subset\big(0,k\tfrac{\pi}{Q}\big]\subseteq(0,\pi]✓ \Longrightarrow \cos(kx)\ \textbf{在}\ I\ \text{上严格递减}✓$$
$$\qquad \Longrightarrow \operatorname*{argmin}_I\cos(k\cdot)=\beta\ \ \forall k\le Q✓ \Longrightarrow M_p=M_q=\{\beta\}✓ \Longrightarrow M_p\cap M_q\ne\varnothing✓ \Longrightarrow \delta=0✓（\texttt{C-276}\ \S1✓）\ \blacksquare$$
$$\textbf{注}✓：\text{结论}\textbf{不依赖}\ \lambda✗（\lambda\in(0,1)\ \text{任意}✓），\text{也不依赖}\ p,q\ \text{的比率}✓ \Longrightarrow \textbf{一切有限族都被同一窗口击穿}✗✓$$
$$\qquad \Longrightarrow \text{这直接回答了唐先生预判}✓✓：\text{若目标类含任意靠近 0 的窄区间，统一供给}\textbf{不可能}✗$$

## §2 该窗口确实在 B\&B 目标类中出现（✓）

$$\textbf{事实}✓：\text{二分产生}\ \big[\tfrac{j\pi}{2^k},\tfrac{(j+1)\pi}{2^k}\big]✓；k\ge5\ \text{时首格}\ [0,\tfrac{\pi}{32}]\subset\big(0,\tfrac{\pi}{25}\big)✓（\tfrac{\pi}{32}<\tfrac{\pi}{25}✓）$$
$$\Longrightarrow \text{该类箱}\ \textbf{必然被搜索到}✓ \Longrightarrow \text{出口 A 的「合法性」无争议}✓$$

## §3 为什么它无害（**关键正面结果**✓✓）

$$\textbf{命题}✓✓：\text{若}\ I_j\subset\big(0,\tfrac{\pi}{25}\big)\ \forall j，\text{则}\ B\ \notin\mathcal H✓$$
$$\textbf{证明}✓：\min_{I_j}\cos(\theta_j)=\cos(\beta_j)✓（\text{递减}✓）\ge\cos\big(\tfrac{\pi}{25}\big)✓ \Longrightarrow q_1\ \ge\ 5\cos\tfrac{\pi}{25}\approx5\times0.9921=\mathbf{4.96}\gg\tfrac12✓ \blacksquare$$
$$\Longrightarrow \textbf{分离性}✓✓：\text{原点窗口（耦合为零}✗）\ \text{与}\ \text{困难类}\ \mathcal H（\text{需耦合}✓）\ \textbf{互不相交}✗✓$$
$$\qquad \text{直观}✓：\textbf{耦合机制该干活的地方，正是它没被原点窗口压住的地方}✓✓$$

## §4 目标类重定义：困难类 $\mathcal H$（✓✓）

$$\boxed{\mathcal H:=\Big\{B:\ \max_{1\le k\le25}q_k(B)<\tfrac12\Big\}✓，\ q_k=\sum_{j=1}^{5}\min_{I_j}\cos(k\theta)✓}$$
$$\textbf{性质}✓：\mathcal H＝\textbf{v4 可分证书失效的箱}✓；\textbf{结构性}✓（仅用箱的解析数据✓，不用搜索结果✗） \Longrightarrow \text{符合}\ \texttt{C-275}\ \S0\ \text{的规则要求}✓$$
$$\textbf{结构性刻画}✓（\text{由}\ \texttt{C-275}\ \text{的}\ D\ \text{语言}✓）：B\in\mathcal H\Longrightarrow \forall k\ \exists j:\min_{I_j}\cos(k\cdot)\ \text{被压低}✓ \Longrightarrow \textbf{危险集覆盖}：\bigcup_j\mathcal D(I_j)\ \text{在低端被推满}✓$$
$$\qquad \text{与}\ \texttt{C-275}\ \S4\ \text{的「典型全覆盖」}✓\ \text{一致}✓ \Longrightarrow \mathcal H\ \text{恰是那个「}\cup_j\mathcal D\ \text{覆盖}\ [1,25]」\ \text{的情形}✓✓$$

## §5 出口判定（按预注册 ✓✓）

$$\textbf{A（DEAD）}✗：\text{对}\ \textbf{全体区间} \text{口径}\ \textbf{成立}✓（\S1✓，且对任意有限族成立✓）\ —— \text{但}\ \textbf{不适用于}\ \mathcal H✗（\S3✓）$$
$$\textbf{B（ALIVE 但非主线）}⬜：\text{需在}\ \mathcal H\ \text{上证明「每箱有某 pair 正耦合」}✓ \Longrightarrow \textbf{未做}✗$$
$$\textbf{C（升级候选）}⬜：\text{需}\ \exists c_*>0:\ \sum_\nu\alpha_\nu\delta_I\ge c_*\ \forall I\in\mathcal H✓ \Longrightarrow \textbf{未做}✗$$
$$\boxed{\textbf{纪律}✓✓：\textbf{B 不是成功}✗；\textbf{只有 C 才是供给机制}✓✓；\text{且 C 须}\ \textbf{统一正下界}✓，\text{不得只逐箱存在某 pair}✗}$$

## §6 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{未读 pending}✓；\text{未选权重}✓；\text{全程单区间／箱级结构}✓$$
$$\textbf{② 本刀只证}\ \S1\ \text{（一般窗口）与}\ \S3\ \text{（无害化分离）}✓；\textbf{未解}\ \mathcal H\ \text{上的供给问句}✗$$
$$\textbf{③ 不声称}✓：\text{不声称}\ \mathcal H\ \text{上存在统一供给}✗（\text{未做}✓）；\text{不声称}\ \mathcal H\ \text{非空}✗（\text{其非空性由}\ \texttt{C-272}\ \text{的积压现象经验支持}⚠️✓）$$
$$\textbf{④ 未用}\ RH✓；\text{未改他档正本}✓；\text{未动}\ v4✓；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

## §7 【技术词回查】输出（**先跑后写**✓）

```
技术词 原点窗口定理 命中文件数=0    ::
技术词 困难类       命中文件数=0    ::
技术词 无害化分离   命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{零点刻画}✓（\texttt{C-276}\ \S1✓）；\text{危险频率集合}\ \mathcal D✓（\texttt{C-275}\ \S1✓）；\text{粗箱积压}✓（\texttt{C-272}✓）；\text{可分下界}\ q_k✓（\texttt{C-277}✓）$$
