已查地图（**先查后写**）：`C-274`（L3-P 纯数学闭合：soundness ＋ 坐标分离 ＋ L3-P1/P2 ＋ Fejér 淘汰定理 ＋ L3-C 未做）、`C-273`（v5 设计审计，§7 勘误指针）、`C-272`（粗箱积压：宽度中位 0.262）、`C-271`、`C197`（一维覆盖证书已证）。回查见 §7 ✓

D0: 本档对象 = **L3-C 第一刀 A：危险频率集合 D(I_j) 的组合结构审计**（预注册三件事，**零计算**）
D1: 0
FREEZE-ACK: 本档即冻结期内的纯数学审计（依 §8.1）

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{① }D(I_j)\ \text{已严格定义}✓，\text{并给出四条基本事实}\ \text{F1–F4}✓（\text{全部可证}✓）}$$
$$\boxed{\textbf{② 组合空洞定理（可证}✓✓）：\text{在}\textbf{可分松弛} \text{层面，正权多-}k\ \text{组合}\ \Longleftrightarrow\ \text{单-}k\ \text{判据} \Longrightarrow \textbf{组合不产生任何增益}✗✓}$$
$$\boxed{\textbf{③ 唯一增益来源＝}\textbf{同点耦合增益}✓✓（\text{即}\ \inf_{I_j}h_\lambda\ \text{严格优于}\ \sum_k\lambda_k\inf_{I_j}\cos(k\cdot)✓），\text{Fejér 例为证}✓}$$
$$\boxed{\textbf{④ 判定}✗✓：\textbf{「避免危险频率」路线 DEAD}（\text{典型空集}✗ ＋ \text{即使非空亦无 L3-P 判据}✗）；\textbf{唯一活口＝同点耦合}✓，\text{移交下一刀}✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{不读 pending 样本}✗；\text{不选数值}\lambda✗；\text{不做 LP／数值优化}✗；\text{不提前碰 L3-D}✗$$

## §1 $D(I_j)$ 的定义与四条基本事实（✓）

$$\textbf{定义}✓：I_j=[a_j,b_j]，\mathcal D(I_j):=\Big\{k\in[1,25]:\ I_j\cap\Big\{\tfrac{(2m+1)\pi}{k}:m\in\mathbb Z\Big\}\ne\varnothing\Big\}$$
$$\textbf{F1（保证尾段}✓）：w_j\ge\pi/k\Longrightarrow k\in\mathcal D(I_j)✓ \quad（\text{长度}\ 2w_j\ \text{的区间必含间距}\ 2\pi/k\ \text{的格点}✓）$$
$$\textbf{F2（计数上界}✓）：|\mathcal D(I_j)|\le\sum_{k=1}^{25}\Big(\big\lfloor \tfrac{kw_j}{\pi}\big\rfloor+1\Big)✓$$
$$\textbf{F3（交的保证部分}✓）：\bigcap_{j=1}^{5}\mathcal D(I_j)\ \supseteq\ \big\{k:\ k\ge\pi/w_{\min}\big\}✓，\ w_{\min}:=\min_j w_j$$
$$\textbf{F4（无危险＝分离界紧}✓✓）：k\notin\bigcup_j\mathcal D(I_j)\Longrightarrow \inf_{x\in I_j}\cos(kx)=\min\big(\cos(ka_j),\cos(kb_j)\big)\ \forall j✓$$

$$\textbf{F4 的意义}✓✓：\text{对「在任一坐标都不危险」的}\ k，\text{分离式内界}\textbf{无}\ -1\ \text{强制项}✗✓ \Longrightarrow \text{该}\ k\ \text{的内界是紧的}✓$$

## §2 组合空洞定理（**本轮核心技术结果**✓✓）

$$\textbf{记}✓：q_k:=\sum_{j=1}^{5}\inf_{x\in I_j}\cos(kx)✓，\ h_\lambda(x)=\sum_{k\in K_B}\lambda_k\cos(kx)✓，\ \Lambda=\sum_k\lambda_k✓$$

$$\textbf{命题（组合空洞）}✓✓：\text{把内层}\ \inf_{I_j}h_\lambda\ \text{松弛为}\ \sum_k\lambda_k\inf_{I_j}\cos(k\cdot)\ \text{时}：$$
$$\qquad \sum_j\inf_{I_j}h_\lambda\ \ge\ \sum_k\lambda_k q_k \ >\ \tfrac12\Lambda\iff \exists k\in K_B:\ q_k>\tfrac12$$
$$\textbf{证明}✓：\text{「}\Longrightarrow\text{」}\ \sum_k\lambda_k\big(q_k-\tfrac12\big)>0✓ \text{是凸组合}⟹\text{必有一项}>0✓；\text{「}\Longleftarrow\text{」}\ \text{取}\ \lambda=e_k✓\ \blacksquare$$

$$\boxed{\textbf{推论}✓✓：\text{正权组合在【可分松弛】层面}\textbf{完全等价于单-}k\ \text{判据} \Longrightarrow \text{组合本身}\textbf{零增益}✗✓}$$
$$\qquad \Longrightarrow \text{「多-}k\ \text{组合若只靠分离式内界，就是 v4 的}\ \max_k\ \text{换了个写法」}✗✓$$

## §3 同点耦合增益（**唯一活口**✓✓）

$$\textbf{松弛误差（增益的精确来源}✓✓）：\ \delta_\lambda:=\sum_{j=1}^{5}\Big[\inf_{I_j}h_\lambda\ -\ \sum_{k}\lambda_k\inf_{I_j}\cos(k\cdot)\Big]\ \ge\ 0✓$$
$$\qquad \text{物理意义}✓：\text{同一坐标}\ x\ \text{必须同时服务所有}\ k⟹\textbf{同点耦合}✓✓$$

$$\textbf{Fejér 例（对照，出自}\ \texttt{C-274}\ \S6✓\text{）}：\lambda_k=K+1-k⟹\inf_{I_j}h_\lambda=-\tfrac12✓，\text{而}\ \sum_k\lambda_k\inf\cos(k\cdot)=-\Lambda✗$$
$$\qquad \Longrightarrow \delta_\lambda=\Lambda-\tfrac12>0✓✓ \Longrightarrow \textbf{同点耦合增益真实存在且可以很大}✓（\text{对宽区间，量级}\ \asymp\Lambda✓）$$

$$\textbf{L3-C 的真问题（重述}✓✓）：\text{不是「选哪些}\ k」，\text{而是}\ \boxed{\text{能否用}\ \textbf{结构性规则} \text{产生}\ \lambda\ \text{使}\ \delta_\lambda \text{ 足够大到越过阈值}✓？}$$

## §4 "避免危险频率"路线的定量判据（**期望层面**⚠️✓）

$$\textbf{思路}✓：\text{取}\ K_B\subseteq[1,25]\setminus\bigcup_j\mathcal D(I_j)✓（\text{由}\ F4，\text{这些}\ k\ \text{的内界紧}✓）$$

$$\textbf{期望计算}⚠️（\text{线性性}✓，\textbf{非定理}✗）：\text{均匀随机位置下}\ \mathbb E|\mathcal D(I_j)|=\sum_{k\le25}\min\big(1,\tfrac{kw_j}{\pi}\big)✓$$
$$\qquad w=0.131\ \text{（\texttt{C-272} 粗箱半宽量级}✓）：\approx0.0417\cdot276+2\approx\mathbf{13.5}✓ \Longrightarrow \text{单位密度}\approx54\%✓$$
$$\qquad \Longrightarrow \mathbb P\big(k\notin\bigcup_j\mathcal D(I_j)\big)\approx(1-0.54)^5\approx\mathbf{0.021}✓ \Longrightarrow \mathbb E\big|\,[1,25]\setminus\bigcup_j\mathcal D\,\big|\approx\mathbf{0.5}✗✓$$

$$\boxed{\textbf{判据}✗✓：\text{粗箱上「避免危险频率」的备选集合}\textbf{典型为空或仅 1 个元素}✗；\text{即使非空}，F4\ \text{只保证内界紧}✓，\textbf{不保证}\ q_k>\tfrac12✗}$$
$$\qquad \Longrightarrow \textbf{该路线既无供给（典型空集）又无判据（紧≠够大）} \Longrightarrow \textbf{判 DEAD}✗✓$$

## §5 出口判定（按预注册 ✓）

$$\textbf{结构定理？}✗：\text{本刀}\textbf{未发现}「\mathcal D\ \text{组合结构}\Longrightarrow\text{小支撑}\lambda」\ \text{的定理}✗✓$$
$$\qquad \text{反而得到两条}\textbf{否证}✓✓：\text{① 可分层面组合空洞}✓（\S2）；\text{② 危险规避路线典型无供给}✓（\S4）$$
$$\textbf{按预注册出口}✓：\text{「从 Loss II 推出结构性}\lambda」\ \text{这一分支}\ \textbf{判掉}✗✓（\text{无需实验}✓）$$
$$\textbf{唯一活口（移交}✓）：\text{同点耦合增益}\ \delta_\lambda✓（\S3）\ \text{—— 其结构性规则是否存在，属下一刀}✓$$

$$\textbf{注意}✓：\text{本刀}\textbf{不判}\ v5\ \text{死刑}✗；\text{只判「危险规避」这一支}✗✓；\text{也不声称}\ \delta_\lambda\ \text{可被结构性实现}✗$$

## §6 边界

$$\textbf{① 零计算}✗（\text{本档无任何运行}✓）；\text{未读 pending 样本}✓；\text{未选数值}\lambda✓$$
$$\textbf{② }\S4\ \text{为}\textbf{期望论证}⚠️✓，\textbf{不是定理}✗（\text{仅}\ F1\text{–}F3\ \text{为可证}✓）；\text{不得写成「粗箱必无安全}\ k」✗$$
$$\textbf{③ 未用}\ RH✓；\text{未改他档正本}✓；\text{未动}\ v4✓；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$
$$\textbf{④ 组合空洞定理的适用范围}✓：\text{仅针对}\ \textbf{可分松弛版}\ \text{的}\ L3\text{-P}✗；\text{不排除真}\ \inf_{B}H_\lambda\ \text{（含同点耦合}✓）\ \text{可行}✓$$

## §7 【技术词回查】输出（**先跑后写**✓）

```
技术词 危险频率集合   命中文件数=0    ::
技术词 组合空洞定理   命中文件数=0    ::
技术词 同点耦合增益   命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{正权组合证书／坐标分离}✓（\texttt{C-274}✓）；\text{Fejér 淘汰}✓（\texttt{C-274}\ \S6✓）；\text{粗箱积压}✓（\texttt{C-272}✓）$$
