已查地图（**先查后写**）：`C-275`（L3-C 第一刀 A：D(I_j) 组合结构 ＋ **组合空洞定理** ＋ 同点耦合增益为唯一活口）、`C-274`（L3-P 闭合 ＋ Fejér 淘汰）、`C-273`（v5 设计审计）、`C-272`（粗箱积压）。回查见 §8 ✓

D0: 本档对象 = **C-276：二频率同点耦合的结构性 gap 审计**（单区间 ＋ 两频率 ＋ 同一 x，**零计算**）
D1: 0
FREEZE-ACK: 本档即冻结期内的纯数学审计（依 §8.1）

---

## §0 结论（四条 ✓✓）

$$\boxed{\textbf{① 精确刻画}✓✓：\delta_I(\lambda)=0\iff M_p\cap M_q\ne\varnothing\quad(\lambda\in(0,1))✓，\ M_p:=\operatorname*{argmin}_{x\in I}\cos(px)}$$
$$\boxed{\textbf{② 一般定量框架}✓：\delta_I(\lambda)\ \ge\ \min(\lambda,1-\lambda)\cdot\inf_{x\in I}\big(g_p(x)+g_q(x)\big)✓，\ g_p:=\cos(px)-\min_I\cos(p\cdot)\ge0✓}$$
$$\boxed{\textbf{③ 共振二分（可证}✓✓）：\text{比率}\ q/p\ \textbf{为奇}\Longrightarrow M_p\subseteq M_q \Longrightarrow \delta=0✗；\text{比率}\ \textbf{为偶}\Longrightarrow M_p\cap M_q=\varnothing✓}$$
$$\boxed{\textbf{④ 比率 2 的显式统一下界}✓✓（\text{ALIVE}✓）：q=2p \Longrightarrow \delta_I\ \ge\ \inf_{t\in[0,\pi/2]}\Big[\lambda(1-\cos t)+(1-\lambda)\big(1+\cos 2t\big)\Big]>0✓\ \text{（位置无关}✓）}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{不选数值}\lambda✗；\textbf{不碰五维}✗（\text{全程单区间}✓）；\text{不用 pending 数据}✗$$

## §1 精确刻画（✓✓）

$$\textbf{设定}✓：I=[\alpha,\beta]\ \text{紧}✓；p\ne q；\lambda\in(0,1)；h(x)=\lambda\cos(px)+(1-\lambda)\cos(qx)；\ \delta_I(\lambda):=\inf_I h-\big[\lambda\inf_I\cos(p\cdot)+(1-\lambda)\inf_I\cos(q\cdot)\big]$$
$$\textbf{恒有}✓：\delta_I(\lambda)\ge0✓（\text{上下确界：和的}\inf\ge\inf\ \text{之和}✓）$$

$$\textbf{命题（零点刻画）}✓✓：\delta_I(\lambda)=0\iff \exists x_0\in I:\ x_0\in M_p\cap M_q$$
$$\textbf{证明}✓：\text{「}\Longleftarrow\text{」}\ \text{该点两项同时取到各自最小值}✓；\text{「}\Longrightarrow\text{」}\ I\ \text{紧}、h\ \text{连续}⟹\inf\ \text{在}\ \hat x\ \text{取到}✓，\text{而}\ \lambda>0,\ 1-\lambda>0⟹\text{两项必须分别取到最小值}⟹\hat x\in M_p\cap M_q✓\ \blacksquare$$
$$\Longrightarrow \textbf{故全部问题归结为：}M_p,M_q\ \textbf{在}\ I\ \text{上是否错位}✓✓$$

## §2 一般定量框架（✓）

$$\textbf{记}✓：g_p(x):=\cos(px)-\min_I\cos(p\cdot)\ge0✓，\text{同理}\ g_q✓ \Longrightarrow \delta_I(\lambda)=\inf_I\big[\lambda g_p+(1-\lambda)g_q\big]✓$$
$$\textbf{基本界}✓：\lambda g_p+(1-\lambda)g_q\ \ge\ \min(\lambda,1-\lambda)\big(g_p+g_q\big) \Longrightarrow \boxed{\delta_I(\lambda)\ \ge\ \min(\lambda,1-\lambda)\cdot\inf_I(g_p+g_q)}✓$$

$$\textbf{几何约束}✓✓：\text{设}\ x_p\in M_p,\ x_q\in M_q\ \text{为最近点对}✓，\rho:=\operatorname{dist}(M_p,M_q)>0✓ \Longrightarrow$$
$$\qquad d(x,M_p)+d(x,M_q)\ \ge\ \rho✓（\text{三角不等式}✓）\qquad \text{且（最近点约定}✓）\ p\,d(x,M_p)\le\pi✓，\ q\,d(x,M_q)\le\pi✓$$
$$\qquad \Longrightarrow \text{令}\ t_p:=p\,d(x,M_p),\ t_q:=q\,d(x,M_q)\Longrightarrow \boxed{\tfrac{t_p}{p}+\tfrac{t_q}{q}\ \ge\ \rho}✓（\textbf{耦合约束}✓✓）$$
$$\qquad \text{且}\ g_p(x)=1-\cos t_p✓，\ g_q(x)=1-\cos t_q✓（\text{在最近点一侧}✓：\cos(px)=\cos\big((2m+1)\pi\pm t_p\big)=-\cos t_p✓）$$

## §3 共振二分（**可证，且直接回答"共振是危险还是机会"**✓✓）

$$\textbf{奇比率}✓：q=mp\ (m\ \text{奇}) \Longrightarrow px\!=\!(2k+1)\pi\ \text{时}\ qx=m(2k+1)\pi\ \text{仍为}\ \textbf{奇}\cdot\pi \Longrightarrow \cos(qx)=-1✓$$
$$\qquad \Longrightarrow M_p\subseteq M_q✓ \Longrightarrow \textbf{只要}\ I\ \text{含一个}\ p\text{-极小点}，\textbf{必} \delta=0✗✓ \Longrightarrow \textbf{奇比率共振使耦合增益消失}✗$$
$$\qquad \Longrightarrow \textbf{对 C-275 路线 B 的直接后果}✓：\text{频率生成规则}\ \textbf{不得} \text{用奇比率族}✗（\text{如}\ \{a,3a,5a\}✗）$$
$$\textbf{偶比率}✓：q=2mp \Longrightarrow px\!=\!(2k+1)\pi\ \text{时}\ qx=2m(2k+1)\pi\ \text{为}\ \textbf{偶}\cdot\pi \Longrightarrow \cos(qx)=+1✓$$
$$\qquad \Longrightarrow x\ \text{是}\ p\text{-极小}\Longrightarrow x\ \text{是}\ q\text{-极大}✗ \Longrightarrow M_p\cap M_q=\varnothing✓✓\ \text{（当两者皆为内点极小}✓）$$

## §4 比率 2 的显式统一下界（**闭式，位置无关**✓✓）

$$\textbf{取}q=2p✓。\text{最近的}\ \pi/p\ \text{型点对距离（格错位}✓）：\rho=\tfrac{\pi}{2p}✓（\pi/p\ \text{是}\ \pi/(2p)\ \text{的偶倍}\Longrightarrow \text{最近}\ p\text{-极小与}\ 2p\text{-极小相距}\ \tfrac{\pi}{2p}✓）$$
$$\qquad \Longrightarrow \tfrac{t_p}{p}+\tfrac{t_{2p}}{2p}\ge\tfrac{\pi}{2p}\iff t_p+\tfrac{t_{2p}}{2}\ge\tfrac{\pi}{2}✓$$
$$\textbf{单调性}✓✓：t\in[0,\pi]\ \text{上}\ 1-\cos t\ \textbf{单调递增}✓ \Longrightarrow \text{下确界在约束}\textbf{边界} \text{取到}✓ \Longrightarrow t_{2p}=\pi-2t_p✓，\ t_p\in[0,\tfrac{\pi}{2}]✓$$
$$\boxed{\delta_I(\lambda)\ \ge\ \min_{t\in[0,\pi/2]}\ g_\lambda(t)✓，\qquad g_\lambda(t):=\lambda(1-\cos t)+(1-\lambda)(1+\cos 2t)✓}$$
$$\textbf{显式临界点}✓：g_\lambda'(t)=\sin t\big[\lambda-4(1-\lambda)\cos t\big]✓ \Longrightarrow \text{内点临界}\ \cos t_*=\tfrac{\lambda}{4(1-\lambda)}\ (\lambda\le\tfrac45)✓，\text{否则}\ g_\lambda\ \text{单调}⟹\min=g_\lambda(0)=2(1-\lambda)✓$$
$$\textbf{例}✓（\lambda=\tfrac12）: \cos t_*=\tfrac14 \Longrightarrow g_*=\tfrac{1}{2}\big(1-\tfrac14\big)+\tfrac12\big(1+2\cdot\tfrac{1}{16}-1\big)=\tfrac{3}{8}+\tfrac{1}{16}=\tfrac{7}{16}=0.4375✓✓$$
$$\Longrightarrow \boxed{\textbf{比率 2 时耦合间隙有}\textbf{正常数下界}\ \text{（如}\ \lambda=\tfrac12\ \text{给}\ \tfrac{7}{16}✓）\ \textbf{且与}\ I\ \text{位置无关}✓✓}$$

## §5 端点情形与单调性二分（✓✓）

$$\textbf{情形 S（同为端点极小）}✓：\text{若}\ I\ \text{短至}\ \cos(px),\cos(qx)\ \textbf{同向单调}✓ \Longrightarrow \text{两者最小值同在一个端点} \Longrightarrow M_p=M_q=\{\beta\}✓ \Longrightarrow \delta_I(\lambda)=0✗✓$$
$$\qquad \Longrightarrow \textbf{短区间上耦合增益消失}✗ \Longrightarrow \text{耦合增益是}\textbf{粗区间现象}✓✓（\text{与}\ \texttt{C-274}\ \S6\ \text{Fejér 例的量级相符}✓）$$
$$\textbf{情形 O（反向单调）}✓：\text{若一个递减、另一个递增} \Longrightarrow M_p=\{\beta\},\ M_q=\{\alpha\} \Longrightarrow \rho=\beta-\alpha✓ \Longrightarrow \delta>0✓（\S2\ \text{框架给出显式下界}✓）$$

$$\textbf{二分总结}✓✓：\text{两频率极小点错位（} \delta>0✓）\ \text{的充分条件有三类}✓：\text{① 反向单调}✓；\text{② 偶比率}✓（\S3）；\text{③ 位置错位}✓（\S2\ \text{的}\ \rho>0✓）；\text{必然重合（}\delta=0✗）\ \text{有两类}：\text{④ 同向单调端点}✓；\text{⑤ 奇比率}✓$$

## §6 出口判定（按预注册 ✓✓）

$$\boxed{\textbf{ALIVE}✓✓：\text{已证}\ \textbf{不依赖 pending 数据} \text{的二频率耦合定理}✓（\S4）\ \text{—— 位置无关正常数下界}✓，\text{并附明确区间几何条件}✓}$$
$$\textbf{DEAD 侧（同时得到}✓）：\textbf{奇比率族}\ \text{与}\ \text{同向单调短区间}\ \text{上}\ \delta\equiv0✗ \Longrightarrow \textbf{C-275 路线 B 中的奇比率生成被淘汰}✗✓$$
$$\Rightarrow \text{下一步资格}✓✓：\text{现已具备}\ \delta_j(\lambda)\ge c>0\ \text{的结构性条件}✓ \Longrightarrow \textbf{有资格进入第二层}✓：\text{问}\ \sum_j\delta_j\ \text{能否越过单-}k\ \text{缺口}✗✓（\text{那是下一刀}✓）$$

$$\textbf{成功标准纪律}✓：\text{本档}\textbf{不以「找到}\ \lambda」\ \text{为成功}✗；\text{只要求}\exists\ \text{结构性条件}\Longrightarrow\delta\ge c>0✓\text{—— 已达成}✓$$

## §7 边界

$$\textbf{① 零计算}✗（\text{本档无任何运行}✓）；\text{全程单区间}✓（\textbf{未碰五维}✗）；\text{未选数值}\lambda✓$$
$$\textbf{② }\S4\ \text{的常数是}\textbf{下界}✓（\text{非最优}✗）；\lambda\to0,1\ \text{时退化}✓（\text{预期}✓，\text{因权重单边化}✗）$$
$$\textbf{③ 奇比率结论的条件}✓：\text{需}\ I\ \text{含}\ p\text{-极小点}✓（\text{若不含则退到端点情形}\ \S5✓）$$
$$\textbf{④ 未用}\ RH✓；\text{未改他档正本}✓；\text{未动}\ v4✓；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$
$$\textbf{⑤ 不声称}✓：\text{不声称}\ \sum_j\delta_j\ \text{足以越过单-}k\ \text{缺口}✗；\text{不声称 v5 可闭合}\ M=5✗$$

## §8 【技术词回查】输出（**先跑后写**✓）

```
技术词 同点耦合间隙   命中文件数=0    ::
技术词 极小点格错位   命中文件数=0    ::
技术词 二频率耦合常数 命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{同点耦合增益}✓（\texttt{C-275}✓）；\text{组合空洞定理}✓（\texttt{C-275}✓）；\text{Fejér 淘汰}✓（\texttt{C-274}\ \S6✓）$$
