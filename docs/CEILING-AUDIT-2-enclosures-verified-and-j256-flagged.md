# 🔍 **审前沿天花板（第二步）**：256 组封闭区间**逐条核完** —— 行证书**算术自洽** ✓✓，但 **$j=256$ 一处偏离** ⚠️

> 依唐先生 14:30 选 (i)；**本档＝实际执行**（纯整数精确算术，Python 直读 `LawN256.lean`）✓
> **结果**：$j=1..255$ **完全自洽**（且精度高于声称）；$j=256$ **偏离模式** ⟹ 登记为待解项 ✓✓✓

---

## §1 LP 结构（本档推出，使"可本地重算"成立）
$$\text{对抗方}：\text{混合律}\ \{w_c\}\ \text{（有理权重，}\sum w_c=1）\ \text{于}\ \textbf{256-周期标记构型}✓$$
$$\text{约束（}\textbf{线性} \text{于}\ w_c）：\ \frac{1}{256}\sum_cw_c\Big|\sum_im_{c,i}e^{2\pi ijx_{c,i}/256}\Big|^2=\frac{j}{256}\quad(0<j<256)✓✓$$
$$\text{目标（}\textbf{线性} \text{于}\ w_c）：\ \min\ \sum_cw_c\cdot(\text{mark-1 比例})✓✓$$
$$\Longrightarrow \boxed{\text{这是一个 LP；证书}\ (c_0,r)\ \text{＝其对偶}} \Longrightarrow \text{两侧最优值相等} \Longrightarrow \textbf{可分别核（律给下界／证书给上界）}✓✓✓$$

## §2 执行：解析并逐条核（精确整数）
$$\text{解析成功}：256\ \text{组}\ [lo_j,hi_j]；\ K=2^{140}✓\qquad K/256=2^{132}=\texttt{5444517870735015415413993718908291383296}✓$$
$$\text{核}\ \textbf{包含性}：2^{132}j\ \in\ [lo_j,hi_j]\quad?\qquad\Longrightarrow\ 255/256\ \textbf{通过}，\ \textbf{仅}\ j=256\ \text{失败}✓✓$$
$$\text{且通过者形式极其规整}：\boxed{[lo_j,hi_j]=[2^{132}j-1,\ 2^{132}j]}\quad(j=1..255)✓✓✓$$
$$\Longrightarrow\ 256S(j)-j\ \in\ \Big[-\tfrac{256}{K},\ 0\Big]=[-1.8369\times10^{-40},\ 0] \Longrightarrow \boxed{|256S(j)-j|\le1.837\times10^{-40}}✓✓✓$$
$$\qquad ⭐\ \text{声称}\ \tau=3\times10^{-40} \Longrightarrow \textbf{实际优于声称}（\text{窄} \approx1.6\times）✓✓$$

## §3 ⚠️ 待解项：$j=256$ 偏离模式
$$j=256：\text{区间} = [294693210168748317632180492755635579620342098,\ \ldots099] \not\ni 2^{132}\cdot256=K✓✗$$
$$\Longrightarrow K\cdot S(256)\approx2.9469\times10^{44} \Longrightarrow S(256)\approx0.21145 \Longrightarrow \textbf{明显偏离模式}✓$$
$$\text{可能的解释}：\text{(i) 网格为}\ j=0..256\ \text{而}\ S(0)=256\ \text{应单独列（}\text{本档未见}\ j=0\ \text{项）}✓$$
$$\qquad\text{(ii)}\ j=256\ (= \alpha=1)\ \text{处形状因子本不在行证书范围（}\text{逐字：}\ 0<j<256）✓✓$$
$$\qquad\text{(iii)}\ \text{或为}\ \textbf{真实边界不一致}✓$$
$$\Longrightarrow \boxed{\text{登记为待解项，}\ \textbf{需定义／JSON 方能判定}}✓✓$$

## §4 ⚠️ 本档自我修正（诚实）
$$\text{我同时跑了一个"对称性}\ S(j)=S(256-j)"\ \text{检查，报 127 违背} \Longrightarrow \textbf{该检查本身错误}✗$$
$$\text{因}\ \alpha\text{-参数化下}\ S(j)=j/256\ \text{而}\ S(256-j)=(256-j)/256 \Longrightarrow \text{二者}\ \textbf{本不相等}（\text{sine-kernel:}\ F(\alpha)=\alpha\ \text{for}\ \alpha\le1）✓✓$$
$$\Longrightarrow \text{该}127\ \text{为}\ \textbf{伪发现}，\ \text{已撤回}✓✗$$

## §5 判词
$$\boxed{\text{① 前沿公布的封闭区间}\ \textbf{与行证书算术自洽}（\text{且更紧}）\ —— \text{本档独立核实}}✓✓✓$$
$$\boxed{\text{② 未核项仍为：律的}\ \textbf{存在性}（\text{简单点比例}\ 0.6818287）\ \text{与 LP 最优性} \Longrightarrow \text{需 JSON 或独立重算}}✓✓$$
$$\boxed{\text{③ 新登记：}j=256\ \text{偏离（}\text{待定义／JSON 判定}）}✓$$

## §6 边界
$$\text{(i)}\ §1\ \text{的 LP 结构为本档推出（与前沿"exact-rational LP"口径一致）}✓\quad\text{(ii)}\ §2--§3\ \text{为}\ \textbf{实跑结果}（\text{整数精确}）✓✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{未取 JSON}✓\quad\text{(iv)}\ §4\ \text{为自我修正}✓$$
