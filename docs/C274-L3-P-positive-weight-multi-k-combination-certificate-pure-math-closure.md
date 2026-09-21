已查地图（**先查后写**）：`C-273`（v5 设计审计：损失 I/II 分离 ＋ 五机制审计）、`C-272`（failure mode：零反例 ＋ 粗箱积压 ＋ 间隙 1.83）、`C-271`（账本钉死）、`C197-T13-B-w2-one-dimensional-cover-certificates-PROVED.md`（**一维覆盖证书已证**✓）、`v4` 引擎。回查见 §9 ✓

D0: 本档对象 = **L3-P（正权多-k 组合证书）的纯数学闭合**：Loss II 修正 ＋ soundness ＋ 坐标分离 ＋ 第一可验证充分条件（**零计算**）
D1: 0
FREEZE-ACK: 本档即冻结期内的纯数学闭合（依 §8.1）

---

## §0 交付与结论（**四件，按唐先生指定**✓）

$$\boxed{\textbf{① Loss II 修正}✓✓：\text{危险点是}\ \theta_j\equiv\frac{(2m+1)\pi}{k}\ (\mathrm{mod}\ 2\pi)✓ \Longrightarrow \textbf{它是}\ k\text{-依赖的}✓，\text{不是「奇数倍}\ \pi\text{、与}\ k\ \text{无关」}✗}$$
$$\boxed{\textbf{② Soundness}✓：\inf_{B}\sum_{k\in K_B}\lambda_kF_k>\tfrac12\Lambda \Longrightarrow \forall\theta\in B:\ \max_{k\in K_B}F_k(\theta)>\tfrac12✓（\text{紧性可升级为}\ \inf_B\max_k>\tfrac12✓）}$$
$$\boxed{\textbf{③ 坐标分离}✓：\inf_{\theta\in B}\sum_k\lambda_kF_k(\theta)=\sum_{j=1}^{5}\inf_{x\in I_j}\ h_\lambda(x)✓，\ h_\lambda(x):=\sum_{k\in K_B}\lambda_k\cos(kx)}$$
$$\boxed{\textbf{④ 第一可验证充分条件}✓：\text{(L3-P1)}\ \text{—— 并显式标注}\textbf{充分非等价}✗✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\textbf{不选}\ \lambda✗；\textbf{不测成功率}✗；\text{不跑 pending 箱}✗$$

## §1 Loss II 修正（**k-依赖**✓✓）

$$\text{对固定}\ k：\ \cos(k\theta)=-1\iff k\theta\equiv\pi\ (\mathrm{mod}\ 2\pi)\iff \theta=\frac{(2m+1)\pi}{k}✓$$
$$\textbf{正确表述}✓（\texttt{C-273}\ \text{原表述「含奇数倍}\ \pi\text{、与}\ k\ \text{无关」为误}✗；\text{见}\ \S1.1\ \text{勘误指针}）$$
$$\qquad \text{对某固定}\ k，\text{若某坐标区间}\ I_j\ \text{含}\ (2m+1)\pi/k \Longrightarrow \text{该坐标对该}\ k\ \text{的最坏项达}\ -1✗$$
$$\Longrightarrow \textbf{正向意义}✓✓：\text{不同}\ k\ \text{的坏区间位置不同} \Longrightarrow \textbf{这正是 v5 要利用的信息}✓（\texttt{C-273}\ \S1\ \text{的「损失 I／II 分离」因此更精确}✓）$$

### §1.1 对 `C-273` 的勘误指针（**追加不覆盖**✓）

$$\texttt{C-273}\ \S1\ \text{中「损失 II（内层坐标）：某坐标区间含}\ \pi\ \text{的奇数倍}⟹\text{该项被强制}\ -1（\text{与}\ k\ \text{无关}）」\ \textbf{应改为}\ \S1\ \text{的}\ k\text{-依赖表述}✓$$
$$\qquad \text{实质结论不变}✓（\text{损失源仍是「逐坐标最坏化」}✓）；\text{变更点＝坏点位置随}\ k\ \text{移动}✓$$

## §2 Soundness（**一行证明 ＋ 紧性升级**✓）

$$\textbf{设定}✓：K_B\subset[1,25]，\lambda_k\ge0，\Lambda:=\sum_{k\in K_B}\lambda_k>0，\ H_\lambda(\theta)=\sum_{k\in K_B}\lambda_kF_k(\theta)，\text{盒}\ B=\prod_j[c_j-w_j,c_j+w_j]✓$$

$$\textbf{命题（L1-sound）}✓：\text{若}\ \inf_{\theta\in B}H_\lambda(\theta)>\tfrac12\Lambda\ \text{则}\ \forall\theta\in B:\ \max_{k\in K_B}F_k(\theta)>\tfrac12$$
$$\textbf{证明}✓：\text{若存在}\ \theta\in B\ \text{使}\ \forall k\in K_B:\ F_k(\theta)\le\tfrac12，\text{则}\ H_\lambda(\theta)\le\tfrac12\sum_k\lambda_k=\tfrac12\Lambda，\text{与}\ \inf_BH_\lambda>\tfrac12\Lambda\ \text{矛盾}✓\ \blacksquare$$

$$\textbf{紧性升级}✓✓：B\ \text{紧}✓、\max_{k\in K_B}F_k\ \text{连续}✓ \Longrightarrow \text{最小值在}\ \theta^*\in B\ \text{取到}✓ \Longrightarrow \max_kF_k(\theta^*)>\tfrac12\ \text{严格} \Longrightarrow \min_{\theta\in B}\max_{1\le k\le25}F_k(\theta)>\tfrac12✓$$
$$\qquad \textbf{注意}✓：\text{逐点严格}>\tfrac12\ \text{只给}\ \inf\ge\tfrac12✗；\textbf{要「}>」\text{必须用取值性}✓（\text{本档补齐}✓）$$

## §3 坐标分离（✓✓）

$$H_\lambda(\theta)=\sum_{k\in K_B}\lambda_k\sum_{j=1}^{5}\cos(k\theta_j)=\sum_{j=1}^{5}\underbrace{\Big(\sum_{k\in K_B}\lambda_k\cos(k\theta_j)\Big)}_{=:\ h_\lambda(\theta_j)}✓$$

$$\textbf{命题（分离等式）}✓：\inf_{\theta\in B}H_\lambda(\theta)=\sum_{j=1}^{5}\inf_{x\in I_j}h_\lambda(x)$$
$$\textbf{证明}✓：\text{①}\ \text{「}\ge\text{」逐坐标取下调}✓；\text{②}\ \text{「}\le\text{」用取值性}✓：h_\lambda\ \text{连续}✓、I_j\ \text{紧}✓ \Longrightarrow \inf\ \text{在}\ x_j^*\in I_j\ \text{取到}^*\ ✓ \Longrightarrow \theta^*=(x_1^*,\dots,x_5^*)\in B\ \text{且}\ H_\lambda(\theta^*)=\sum_j\inf_{I_j}h_\lambda✓ \Longrightarrow \text{等式}✓\ \blacksquare$$
$$\qquad {}^*\ \text{即}\ h_\lambda(x)=\sum_{k\in I_j}\cdots\ \text{（}K_B\ \text{有限⟹}h_\lambda\ \text{为有限三角多项式，连续}✓\text{）}$$
$$\Longrightarrow \textbf{五维盒问题被压成 5 个一维加权三角多项式的区间下界}✓✓$$

## §4 第一可验证充分条件（L3-P1）（**充分非等价**✗✓）

$$|h_\lambda'(x)|\le\sum_{k\in K_B}\lambda_kk=:L✓ \Longrightarrow \forall x\in I_j:\ h_\lambda(x)\ge h_\lambda(c_j)-w_jL✓$$
$$\Longrightarrow \inf_BH_\lambda\ \ge\ \sum_k\lambda_k\sum_j\cos(kc_j)\ -\ L\sum_jw_j$$
$$\boxed{\textbf{(L3-P1)}✓：\ \sum_{k\in K_B}\lambda_k\Big[\sum_{j=1}^{5}\cos(kc_j)\ -\ k\sum_{j=1}^{5}w_j\ -\ \tfrac12\Big]\ >\ 0\ \Longrightarrow\ \min_{\theta\in B}\max_{1\le k\le25}F_k(\theta)>\tfrac12}$$

$$\textbf{勘误}✓（\S4.1）\text{唐先生}\ \text{(L3-P1')}\ \text{原写}\ \tfrac52\ ✗，\textbf{应为}\ \tfrac12✓\ \text{（阈值是}\ \Lambda/2✓）$$
$$\qquad \text{验算}✓：|K_B|=1，\lambda_k=1 \Longrightarrow \text{条件退化为}\ \sum_j\cos(kc_j)-k\sum_jw_j>\tfrac12✓\ \text{（即 v4 的分离式＋一阶缓冲}✓）$$

### §4.1 勘误说明（**性质：偏保守，非 soundness 问题**✓）

$$\text{用}\ \tfrac52\ \text{会使条件}\ \textbf{更严}✗ \Longrightarrow \text{仍 sound}✓\ \text{但会}\textbf{漏掉有效证书}✗ \Longrightarrow \text{已改为}\ \tfrac12✓$$

## §5 二阶余量版本（L3-P2）（✓）

$$h_\lambda(x)-h_\lambda(c)-h_\lambda'(c)(x-c)\ \text{≤}\ \tfrac12\Big(\sum_k\lambda_kk^2\Big)(x-c)^2✓（\text{Taylor 余项}✓）$$
$$\Longrightarrow \inf_{I_j}h_\lambda\ \ge\ h_\lambda(c_j)-w_j\big|h_\lambda'(c_j)\big|-\frac{w_j^2}{2}\sum_{k}\lambda_kk^2✓$$
$$\boxed{\textbf{(L3-P2)}✓：\ \sum_k\lambda_k\sum_j\cos(kc_j)-\sum_jw_j\Big|\sum_k\lambda_kk\sin(kc_j)\Big|-\frac{\sum_jw_j^2}{2}\sum_k\lambda_kk^2\ >\ \tfrac12\sum_k\lambda_k}$$

## §6 一个**可证的淘汰结果**（Fejér／均匀权重必失败 ✓✓）

$$\textbf{取均匀权重}✓：K_B=\{1,\dots,K\}，\lambda_k=K+1-k \Longrightarrow \Lambda=\tfrac{K(K+1)}{2}✓$$
$$h_\lambda(x)=\sum_{k=1}^{K}(K+1-k)\cos(kx)=\tfrac12\big[(K+1)F_K(x)-1\big]✓（F_K=\text{Fejér 核}\ge0✓）\Longrightarrow h_\lambda\ge-\tfrac12✓，\text{且}\ h_\lambda=-\tfrac12\iff x=\tfrac{2\pi m}{K+1}\ (m\not\equiv0)✓$$
$$\textbf{定理（均匀权重淘汰）}✓：\text{若}\ \forall j:\ \operatorname{diam}(I_j)>\tfrac{2\pi}{K+1}\ \text{则每个}\ I_j\ \text{含一个}\ \tfrac{2\pi m}{K+1}✓ \Longrightarrow \sum_j\inf_{I_j}h_\lambda=-\tfrac52\ ✓$$
$$\qquad \text{而}\ (L3-P)\ \text{要求}\ -\tfrac52>\tfrac{\Lambda}{2}=\tfrac{K(K+1)}{4}✗ \Longrightarrow \text{对一切}\ K\ge2\ \textbf{失败}✓✓$$
$$\Longrightarrow \boxed{\textbf{结论}✓✓：\lambda\ \textbf{必须集中}（\text{小支撑／非均匀}）✗；\text{Fejér/均匀权重在粗盒上}\textbf{可证无效}✓}$$

## §7 任务表（L3-A…D，**全部纯数学**✓）

| 任务 | 内容 | 本档状态 |
|---|---|---|
| L3-A | 正权组合证书的 soundness | **已证** ✓（§2）|
| L3-B | 一阶／二阶区间下界的 soundness | **已证** ✓（§4／§5）|
| L3-C | 是否存在**不依赖计算结果**的结构性 $\lambda$ 选择规则 | **未做** ⬜（§6 给出一条排除：均匀权重 ✗）|
| L3-D | 一阶太松时用二阶余量（$h_\lambda''=-\sum\lambda_kk^2\cos(kx)$）| **已列式** ✓（§5），未深入 ⬜ |

## §8 边界

$$\textbf{① 零计算}✗（\text{本档无任何运行}✓）；\textbf{不选}\ \lambda✗；\textbf{不测成功率}✗；\text{不跑 pending 箱}✗$$
$$\textbf{② 不声称 v5 能闭合}\ M=5✗；\text{不声称}\ (L3-P1)\ \text{是等价刻画}✗（\textbf{只是充分条件}✓）$$
$$\textbf{③ }\texttt{C197}\ \text{只证明「覆盖证书这一类机制有先例」}✓，\textbf{不推出}\ 1D\to5D\ \text{可行}✗✓（\text{已按唐先生收紧}✓）$$
$$\textbf{④ 未用}\ RH✓；\text{未改}\ v4✓；\text{未改他档正本}✓（\S1.1\ \text{为追加指针}✓）；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

## §9 【技术词回查】输出（**先跑后写**✓）

```
技术词 正权组合证书   命中文件数=0    ::
技术词 坐标分离证书   命中文件数=0    ::
技术词 集中权重必要性 命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{覆盖证书}✓（\texttt{C197}✓，\text{一维已证}✓）；\text{认证间隙／交换损失}✓（\texttt{C-271}✓）；\text{粗箱积压}✓（\texttt{C-272}✓）$$
