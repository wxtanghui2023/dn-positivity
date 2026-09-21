已查地图（**先查后写**）：`C-282`（**Δ–Γ 恒等式**：Δ−Γ_λ=Σ_j c_j−½ ⟹ 桥≡混合核可分认证 ＋ 出口 GAP）、`C-281`（C_ε ＋ 路径宽度引理 ＋ **§8.4 C-282 预注册**）、`C-280`（两对空交定理 ＋ §9 退化勘误）、`C-277`／`C-278`（Type B／二倍族 DEAD）、`C-276`（零点刻画 ＋ **§3 奇偶比率二分** ＋ §4 常数 7/16）、`C-275`（组合空洞定理）。回查见 §7 ✓

D0: 本档对象 = **C-283（A′ 第一刀）：混合核是否产生新机制 —— q=2p, λ=½ 的解析结构审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{① ⭐ 代数退化定理（整数比）}✓✓：q=2p,\ \lambda=\tfrac12：h(x)=\tfrac12[\cos px+\cos 2px]=\tfrac12(2c-1)(c+1)=:\varphi(c)✓，\ c:=\cos px✓}$$
$$\qquad \Longrightarrow \textbf{混合核是单频变量}\ \cos(px)\ \textbf{的函数}✗（\text{两频率}\textbf{代数相关}✗：\cos 2px=2c^2-1✓）$$
$$\qquad \textbf{推广}✓✓：\text{整数比}\ q=mp \Longrightarrow \cos(mpx)=T_m(\cos px)（\text{切比雪夫}✓） \Longrightarrow \textbf{混合核＝}\cos(px)\ \textbf{的多项式}✓$$
$$\boxed{\textbf{② ⭐ }\delta_I\ \textbf{的闭式}✓✓：\text{记}\ C:=[m,M]=\cos(p\theta)\ \text{在}\ I\ \text{上的值域}✓ \Longrightarrow \boxed{\delta_I(p,2p;\tfrac12)=\min_{c\in C}\varphi(c)-\tfrac{m}{2}-d^2+\tfrac12}✓✓，d:=\operatorname{dist}(0,C)✓}$$
$$\qquad \Longrightarrow \delta_I\ \textbf{是}\ (m,M)\ \textbf{的显式函数}✓✓ \Longrightarrow \textbf{不含任何跨频率独立信息}✗✓$$
$$\boxed{\textbf{③ 两处交叉验证（精确）}✓✓：\text{Type B 区：}\delta_I=0✓；\text{极端 Type A（}m=-1,d=0\text{）：}\delta_I=\tfrac{7}{16}✓\ \textbf{精确复原}\ \texttt{C-276}\ \S4✓✓}$$
$$\boxed{\textbf{④ 判决（按 A′ 生死标准）}✓✓：\text{对}\textbf{整数比} \text{对}\ \textbf{没有出现「混合核特有」的区间几何定理}✗，\text{而是更强的}\textbf{退化}✗ \Longrightarrow \textbf{判 GAP／重包装}✓}$$
$$\qquad \textbf{但范围有限}✗：\text{仅覆盖}\ \textbf{整数比} \text{对}✓；\ \texttt{C-280}\ \text{所必需的两对}\ (1,2),(1,4)\ \text{皆为整数比}✗ \Longrightarrow \text{它们确属重包装}✓；\textbf{而}\ (2,3),(2,5)\ \text{为非整数比}✗ \Longrightarrow \textbf{不被本刀覆盖}✓$$
$$\boxed{\textbf{⑤ 存活面}✓✓：\text{非整数比（且非奇整数比）}✓ —— \text{因奇整数比已由}\ \texttt{C-276}\ \S3\ \text{证}\ \delta\equiv0✗ \Longrightarrow \textbf{搜索面大幅收窄}✓✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{未读 pending}✗；\text{未枚举}\ (p,q,\lambda)✗；\text{只做}\ q=2p,\lambda=\tfrac12✓$$

## §1 代数退化定理（**证明**✓✓）

$$\textbf{代数}✓：\text{令}\ c:=\cos(px)✓ \Longrightarrow \cos(2px)=2c^2-1✓ \Longrightarrow h=\tfrac12\big[c+(2c^2-1)\big]=c^2+\tfrac{c}{2}-\tfrac12=\tfrac12(2c-1)(c+1)=:\varphi(c)✓✓$$
$$\qquad \Longrightarrow h\ \textbf{只通过}\ c\ \text{依赖}\ x✓ \Longrightarrow \text{两频率}\textbf{不是两个独立通道}✗✓$$
$$\textbf{推论}✓✓：\cos(p\theta)\ \text{在}\ I\ \text{上连续}✓ \Longrightarrow \text{值域}\ C=[m,M]\ \text{是区间}✓ \Longrightarrow \min_I h=\min_{c\in C}\varphi(c)✓（\textbf{闭式}✓）$$
$$\qquad \text{且}\ \min_I\cos(2p\theta)=\min_{c\in C}(2c^2-1)=2d^2-1✓，\ d=\operatorname{dist}(0,C)✓$$
$$\Longrightarrow \delta_I=\min_{c\in C}\varphi(c)-\tfrac{m}{2}-\Big(d^2-\tfrac12\Big)=\boxed{\min_{c\in C}\varphi(c)-\tfrac{m}{2}-d^2+\tfrac12}✓✓ \blacksquare$$

## §2 交叉验证（**两处精确对上**✓✓）

$$\textbf{情形 B（Type B 型，见}\ \texttt{C-278}\ \S1✓）✓：I\subset(0,\tfrac{\pi}{2p}) \Longrightarrow c\ \text{递减}✓ \Longrightarrow C=[\cos p\beta,\cos p\alpha]✓，\ m=\cos p\beta>0✓$$
$$\qquad \Longrightarrow -\tfrac14\notin C \Longrightarrow \min_C\varphi=\varphi(m)=m^2+\tfrac{m}{2}-\tfrac12✓；\ d=m✓$$
$$\qquad \Longrightarrow \delta_I=\Big(m^2+\tfrac{m}{2}-\tfrac12\Big)-\tfrac{m}{2}-m^2+\tfrac12=\boxed{0}✓✓ \Longrightarrow \textbf{与}\ \texttt{C-276}\ \S1\ \text{零点刻画一致}✓✓$$
$$\textbf{情形 A（极端，含}\ \min\text{与}\ \max\text{）}✓：C=[-1,M]（M\ge-\tfrac14）\Longrightarrow m=-1✓，d=0✓，\min_C\varphi=\varphi(-\tfrac14)=-\tfrac{9}{16}✓$$
$$\qquad \Longrightarrow \delta_I=-\tfrac{9}{16}+\tfrac12-0+\tfrac12=\boxed{\tfrac{7}{16}}✓✓ \Longrightarrow \textbf{精确复原}\ \texttt{C-276}\ \S4\ \text{的常数}✓✓$$
$$\qquad \textbf{附带}✓：\varphi\ \text{在}\ \mathbb{R}\ \text{上的最小值}＝-\tfrac{9}{16}✓（\text{取}\ c=-\tfrac14✓） \Longrightarrow \textbf{全局下界}\ \min_Ih\ge-\tfrac{9}{16}✓✓$$

## §3 A′-1 判决：**它不是新核**（✗✓）

$$\textbf{唐先生判据}✓：\text{若只能通过对}\ h\ \text{做普通区间下界／端点／Lipschitz／Taylor／Fejér 等可分估计} \Longrightarrow \textbf{GAP／重包装}✗$$
$$\textbf{本刀结果更强}✗✓：\text{不需要任何估计}✓ —— h\ \textbf{就是}\ \cos(px)\ \text{的显式函数}✗ \Longrightarrow \text{所有关于}\ \min_Ih\ \text{的量都由}\ (m,M)\ \textbf{完全决定}✓✓$$
$$\qquad \Longrightarrow \textbf{「两个频率」的耦合不是两通道交互}✗，\text{而是}\ \textbf{单通道的非线性再编码}✓ \Longrightarrow \textbf{判重包装}✓（\text{对整数比}✓）$$
$$\textbf{与}\ \texttt{C-275}\ \text{的关系}✓：\text{组合空洞定理说「可分层面组合}\equiv\text{单}k」✓；\text{本刀说「整数比混合核}\equiv\text{单频非线性函数」}✓ \Longrightarrow \textbf{同一方向的更强退化}✓✓$$

## §4 A′-2：耦合量能否被独立几何量控制？（✓✓）

$$\textbf{问}✓（\text{唐先生}）：\delta_I\ \text{能否由}\ \Phi\big(\min_I\cos px,\min_I\cos qx,|I|\big)\ \text{强制控制}✓？$$
$$\textbf{答}✓✓：\textbf{能，而且更强}✓ —— \delta_I\ \textbf{恰等于}\ (m,M)\ \text{的显式函数}✓（\S1✓），\text{其中}\ m=\min_I\cos p\theta✓，\ M=\max_I\cos p\theta✓$$
$$\qquad \textbf{但这不是解救而是诊断}✗✓：\text{控制量}\textbf{存在却纯单频}✓ \Longrightarrow \text{耦合量}\textbf{不携带新的两频信息}✗ \Longrightarrow \textbf{仍判 GAP}✓$$
$$\qquad \textbf{注}✓：\delta_I\ \text{不依赖}\ I\ \text{的其余几何}✗（\text{如}\ \cos(2p\theta)\ \text{极小点的具体位置}✓），\text{只通过}\ (m,M)\ \text{依赖}✓$$

## §5 A′-3：能否控制 $\tfrac12-\tfrac{q_p+q_{2p}}{2}$？（**闭式桥条件**✓✓）

$$\textbf{由}\ \texttt{C-282}\ \text{恒等式}✓：\Delta-\Gamma_\lambda=\sum_jc_j-\tfrac12✓，\text{此处}\ c_j=\min_{C_j}\varphi✓ \Longrightarrow \textbf{桥的闭式形式}✓✓：$$
$$\qquad \boxed{\sum_{j=1}^{5}\ \min_{c\in C_j}\varphi(c)\ >\ \tfrac12}✓✓ \quad（C_j=\cos(p\theta)\ \text{在}\ I_j\ \text{上的值域}✓）$$
$$\textbf{一个强充分条件及其}\textbf{自毁}✓✓：\min_{C}\varphi\ge\tfrac12\iff C\subseteq[c_*,1]✓，\ c_*=\tfrac{\sqrt{17}-1}{4}\approx0.7808✓ \Longrightarrow \text{若五坐标皆如此则}\ \sum\ge\tfrac52>\tfrac12✓$$
$$\qquad \textbf{但}✗：\text{那要求}\ m_j\ge0.7808\ \forall j \Longrightarrow q_p=\sum_jm_j\ge3.90\gg\tfrac12 \Longrightarrow \textbf{B}\notin H_\le✗✓$$
$$\qquad \Longrightarrow \textbf{该充分路线在}\ H_\le\ \text{上为空}✗ \Longrightarrow \text{任何}\ H_\le\ \text{上的认证}\textbf{必须依赖某些坐标的负贡献}✓（\text{即「混合型」箱}✓）$$

## §6 判决与存活面（✓✓）

$$\textbf{降级}✗：\textbf{整数比混合核族}（\text{含}\ (1,2),(1,4),(1,8),\ldots）\ \text{＝单频非线性再编码}✓ \Longrightarrow \textbf{从主线候选中降级}✗✓$$
$$\qquad \Longrightarrow \texttt{C-280}\ \text{所必需的两对}\ (1,2),(1,4)\ \text{的「耦合」}\textbf{不再是独立机制}✗（\text{其定理仍成立}✓，\text{但解释变了}✓）$$
$$\textbf{存活}✓✓：\textbf{非整数比} \text{对}（\text{如}\ (2,3),(2,5)✓）：\cos(qx)\ \textbf{不是}\ \cos(px)\ \text{的函数}✗$$
$$\qquad \text{例}✓：\cos 3x=4\cos^3x-3\cos x✓ \Longrightarrow \text{以}\ \cos 2x\ \text{表之时出现}\ \cos x=\pm\sqrt{\tfrac{1+\cos2x}{2}}\ \textbf{双值}✗ \Longrightarrow \textbf{真正的两维交互}✓$$
$$\qquad \text{再排除}✓：\text{奇整数比}\ \delta\equiv0✗（\texttt{C-276}\ \S3✓） \Longrightarrow \textbf{存活面 ＝ 非整数比且非奇整数比}✓✓$$
$$\boxed{\textbf{因此}✓：\textbf{不应} \text{一刀切降级「有限频率正混合核」整个出口}✗；\text{应}\ \textbf{只降级整数比子族}✓，\text{并把搜索面收窄到非整数比}✓✓}$$

## §7 【技术词回查】输出（**先跑后写**✓）

```
技术词 代数退化定理 命中文件数=0    ::
技术词 闭式耦合量   命中文件数=0    ::
技术词 存活面收窄   命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{零点刻画}✓（\texttt{C-276}\ \S1✓）；\text{常数}\ \tfrac{7}{16}✓（\texttt{C-276}\ \S4✓）；\text{奇比率}\ \delta\equiv0✓（\texttt{C-276}\ \S3✓）；\text{组合空洞定理}✓（\texttt{C-275}✓）；\Delta-\Gamma\ \text{恒等式}✓（\texttt{C-282}✓）$$
$$\textbf{③ 边界}✓：\text{零计算}✗；\text{未读 pending}✗；\text{未枚举}\ (p,q,\lambda)✗；\text{只做}\ q=2p,\lambda=\tfrac12✓；\text{未用}\ RH✓；\text{未动}\ v4✗；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

---

## §8 勘误（**数学错误就地改正 ＋ 追加指针**✗✓，2026-09-21，唐先生指出，见 `C-284`）

$$\textbf{撤回}✗：\S6\ \text{称存活面为非整数比（例：(2,3),(2,5)）}\textbf{，完全错误}✗$$
$$\textbf{错因}✗✓：\text{我用的判据是「}\cos(qx)\ \text{是否为}\ \cos(px)\ \text{的函数}✓」；\textbf{正确判据}是「\text{两者是否}\textbf{同为} \cos(dx)\ \text{的函数}，d=\gcd(p,q)✓」 —— \textbf{恒为真}✓✓$$
$$\qquad \text{切比雪夫}✓：\cos(px)=T_{p/d}(\cos dx)✓，\ \cos(qx)=T_{q/d}(\cos dx)✓ \Longrightarrow \textbf{任意}\ p,q\ \text{皆退化为单变量}✗✓$$
$$\Longrightarrow \S6\ \text{的「存活集」}\textbf{为空}✗ \Longrightarrow \text{整个 A 出口由}\ \texttt{C-284}\ \text{统一封口}✓✓；\text{记为本轮自误}\#3✓$$
