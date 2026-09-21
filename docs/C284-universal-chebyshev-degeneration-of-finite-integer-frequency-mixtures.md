已查地图（**先查后写**）：`C-283`（A′ 第一刀：**整数比**代数退化 ＋ §6 存活面主张 **已被本档撤回**✓）、`C-282`（Δ–Γ 恒等式 ⟹ 桥≡混合核可分认证 ＋ 出口 GAP）、`C-281`（C_ε ＋ 路径宽度）、`C-280`（两对空交定理）、`C-276`（零点刻画 ＋ §3 奇偶比率）、`C-275`（组合空洞定理）。回查见 §7 ✓

D0: 本档对象 = **C-284：有限整数频率混合的通用切比雪夫退化（全族代数封口）**，**零计算（仅做恒等式数值校验）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{① ⭐ 通用退化定理}✓✓：\forall\ K=\{k_1,\ldots,k_r\}\subset\mathbb N\ \text{有限}，d:=\gcd K，k_i=dn_i✓ \Longrightarrow \cos(k_ix)=T_{n_i}(\cos dx)\ \forall x✓}$$
$$\qquad \Longrightarrow \textbf{频率向量分解}✓✓：v(x):=\big(\cos(k_1x),\ldots,\cos(k_rx)\big)=T(\cos dx)✓，\ T:=(T_{n_1},\ldots,T_{n_r})✓$$
$$\qquad \textbf{加强形式}✓✓：\forall\Phi:[-1,1]^r\to\mathbb R：\Phi\circ v=(\Phi\circ T)(\cos d\cdot)✓ \Longrightarrow \textbf{任意同点泛函都坍缩为单变量函数}✗✓$$
$$\boxed{\textbf{② }\delta_I\ \textbf{的通用闭式}✓✓：C_d(I):=\cos(d\cdot)(I)=[m_d,M_d]✓ \Longrightarrow \delta_I=\min_{[m_d,M_d]}P-\sum_i\lambda_i\min_{[m_d,M_d]}T_{n_i}✓（\text{只依赖}\ (m_d,M_d)✓✓）}$$
$$\boxed{\textbf{③ 增益来源诊断}✓✓：\text{单-}k\ \text{可分界只用}\ m_k✓（\text{值域}\textbf{下端}✓）；\text{混合核用整段值域} \Longrightarrow \textbf{额外信息＝上端}\ M_d✗✓；\text{而}\ H_\le\ \textbf{只约束下端}✗ \Longrightarrow \textbf{桥 GAP 的结构性原因闭环}✓✓}$$
$$\boxed{\textbf{④ 整个 A 出口降级}✓✓：\text{有限整数频率正混合族}\ \textbf{全部封口}✗ \Longrightarrow \text{一次性封掉}\ 1\le k\le25\ \text{的全部有限正混合}✓✓}$$
$$\boxed{\textbf{⑤ 边界}✓✓：\text{封的是「同点＋整数频率＋有限＋可写成频率向量泛函」的机制}✓；\textbf{不封} \text{非整数频率／非同点结构／}\mathbb R[\cos(dx)]\ \textbf{闭包之外的新对象}✓}$$

$$\textbf{纪律}✓：\text{不枚举}\ (2,3),(2,5)✗；\text{不做 B}✗；\text{不重跑 M=5}✗；\text{未读 pending}✗$$

## §1 通用退化定理（**证明**✓✓）

$$\textbf{切比雪夫恒等式}✓（\text{经典}✓）：T_n(\cos\theta)=\cos(n\theta)\ \forall n\in\mathbb N,\ \theta\in\mathbb R✓$$
$$\textbf{证明}✓：\text{令}\ \theta:=dx✓ \Longrightarrow \cos(k_ix)=\cos(dn_ix)=\cos(n_i\cdot dx)=T_{n_i}(\cos dx)✓ \Longrightarrow \text{①}✓ \blacksquare$$
$$\textbf{加强形式证明}✓：v(x)=T(\cos dx)✓ \Longrightarrow \Phi(v(x))=\Phi(T(\cos dx))=(\Phi\circ T)(\cos dx)✓（\text{逐点代入}✓） \blacksquare$$
$$\textbf{注}✓✓：\text{①不含}\ \lambda✗（\text{对任意权重成立}✓）；\text{不含}\ r✗（\text{任意有限}✓）；\text{不含}\ d\ \text{的特殊性}✗（\text{任意}\ K✓）$$

## §2 区间耦合量的直接后果（✓✓）

$$\textbf{推论 1}✓：h(x)=\sum_i\lambda_i\cos(k_ix)=P(\cos dx)✓，\ P:=\sum_i\lambda_iT_{n_i}✓，\ \deg P\le\max_in_i✓$$
$$\textbf{推论 2}✓✓：\min_I h=\min_{c\in C_d(I)}P(c)✓，\ C_d(I)=\cos(d\cdot)(I)=[m_d,M_d]✓（\text{连续像}✓，\textbf{是区间}✓）$$
$$\qquad \textbf{含义}✓✓：\text{「跨频率耦合」}\equiv\textbf{单变量区间上的多项式极值问题}✓✓ \Longrightarrow \textbf{降为}\ \min_{[\xi,\eta]}P✓（\text{单变量}✓）$$
$$\textbf{推论 3}✓✓：\min_I\cos(k_ix)=\min_{c\in C_d(I)}T_{n_i}(c)✓ \Longrightarrow \textbf{整个}\ \delta_I\ \textbf{只是}\ (m_d,M_d)\ \text{的显式函数}✓✓$$
$$\qquad \Longrightarrow \text{五个坐标的耦合数据}\ \textbf{全部} \text{由}\ \big\{(m_{d,j},M_{d,j})\big\}_{j=1}^5\ \textbf{决定}✓✓ \Longrightarrow \textbf{单一基础频率}\ d\ \text{的值域信息}✓$$
$$\textbf{推论 4}✓✓：\text{任何}\ \Phi(\cos k_1x,\ldots,\cos k_rx)\ \text{型机制}\textbf{全部} \text{坍缩}✗ \Longrightarrow \textbf{非线性化也不逃逸}✗✓（\text{乘积、幂、任意光滑函数皆然}✓）$$

## §3 增益来源诊断（**与 C-282 闭环**✓✓）

$$\textbf{对照}✓✓：\text{单-}k\ \text{可分界}\ q_k=\sum_j\min_{I_j}\cos(k\theta_j)✓ \Longrightarrow \textbf{只用值域下端}✗（\text{每坐标一个数}✓）$$
$$\qquad \text{混合核证书}\ \sum_j\min_{C_{d,j}}P✓ \Longrightarrow \textbf{用整段值域}✓ \Longrightarrow \textbf{额外信息＝上端}\ M_{d,j}✗✓$$
$$\textbf{而}\ H_\le\ \text{只写}\ \max_kq_k\le\tfrac12✓ \Longrightarrow \textbf{只约束下端}✗ \Longrightarrow \text{混合核的杠杆}\textbf{作用于假设未约束的数据}✓$$
$$\qquad \Longrightarrow \boxed{\textbf{这正是}\ \texttt{C-282}\ \text{桥 GAP}\ \textbf{的结构性原因}✓✓}：\Delta\ge c_*>0\ \text{来自上端信息}✓，\text{而阈值}\ \Gamma\ \text{由下端定义}✓ \Longrightarrow \textbf{两者互不锁定}✓✓$$

## §4 `C-283` §6 勘误（**自误 #3**✗✓，2026-09-21 唐先生指出）

$$\textbf{错误}✗：\texttt{C-283}\ \S6\ \text{称}\ (2,3),(2,5)\ \text{为「非整数比 }\Longrightarrow \text{真正两维交互 }\Longrightarrow \text{存活」}✗$$
$$\textbf{判据选错}✗✓：\text{我检查的是「}\cos(qx)\ \text{是否为}\ \cos(px)\ \text{的函数}✓」（(2,3) 处双值✓），\text{故判存活}✗$$
$$\qquad \textbf{正确判据}✓✓：\text{「两者是否}\textbf{同为} \cos(dx)\ \text{的函数}✓，\ d=\gcd(p,q)✓」 —— \textbf{恒为真}✓✓$$
$$\textbf{反例校验}✓✓（\text{数值}✓，见\ \S7.2✓）：(2,3)：d=1，\cos 2x=T_2(\cos x)✓，\cos 3x=T_3(\cos x)✓ \Longrightarrow h=\lambda T_2(c)+(1-\lambda)T_3(c)✓ \Longrightarrow \textbf{单变量}✗✓$$
$$\textbf{处置}✓：\S6\ \text{的「存活面＝非整数比」}\textbf{撤回}✗；\textbf{存活集＝空}✓ \Longrightarrow \text{由本档}\ \S1\ \text{取代}✓$$
$$\textbf{责任}✓：\text{该错误应由作者自查发现}✗ —— \text{记为本轮自误}\#3✓（\text{正确判据＝「共同单变量」，非「彼此可表」✓}）$$

## §5 出口判定（✓✓）

$$\boxed{\textbf{A 出口整体降级}✓✓：\text{有限整数频率正混合族}\ \textbf{一次性封口}✗ \Longrightarrow \text{不再枚举}\ (2,3),(2,5),\ldots✓}$$
$$\qquad \textbf{机制}✓：\text{频率组合}\longrightarrow\text{单一基础频率}\ d\ \text{的切比雪夫多项式}✗ \Longrightarrow \textbf{未产生新的独立 arithmetic／spectral 坐标}✗✓$$
$$\textbf{与}\ \texttt{C-275}\ \text{的关系}✓✓：\texttt{C-275}\ \text{说「可分层面组合}\equiv\text{单}k」✓；\text{本档说「任意有限整数频率泛函}\equiv\text{单变量}\cos(dx)\ \text{的函数」}✗ \Longrightarrow \textbf{更强、更彻底的封口}✓✓$$
$$\textbf{手续}✓：\text{不做 B}✗；\text{不枚举}✗；\text{不重跑 M=5}✗；\text{下一步须由唐先生重新指定方向}✓$$

## §6 边界（**救援必须引入什么**✓✓）

$$\textbf{封锁范围}✓：\text{同点}\ ∧\ \text{整数频率}\ ∧\ \text{有限}\ ∧\ \text{频率向量泛函}✓$$
$$\textbf{未封锁}✓：\text{① 非整数频率}（\text{如}\ \cos(\sqrt2x)✓）—— \text{但我们的设计空间是}\ \{1,\ldots,25\}\ \text{整数}✗ \Longrightarrow \textbf{该空间内无剩余}✗✓$$
$$\qquad \text{② 非同点结构}✓（\text{跨坐标耦合}✗）—— \text{但箱是乘积}✓，\text{坐标独立} \Longrightarrow \text{可分}✓ \Longrightarrow \text{无空间}✗$$
$$\qquad \text{③ }\mathbb R[\cos(dx)]\ \textbf{闭包之外的新对象}✓（\text{唐先生指示}✓）\Longrightarrow \textbf{救援的唯一方向}✓$$
$$\textbf{不得} \text{写成}✗：\text{「全部同点耦合已死」}✗（\text{本档只封上述交集}✓）；\text{「M=5 已判死」}✗（\text{不涉及}✓）$$

## §7 【技术词回查】输出（**先跑后写**✓）

### §7.1 技术词回查

```
技术词 通用切比雪夫退化 命中文件数=0    ::
技术词 基础频率值域     命中文件数=0    ::
技术词 增益来源诊断     命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{切比雪夫恒等式}✓（\text{经典}✓）；\text{组合空洞定理}✓（\texttt{C-275}✓）；\text{零点刻画}✓（\texttt{C-276}✓）；\Delta-\Gamma\ \text{恒等式}✓（\texttt{C-282}✓）$$

### §7.2 恒等式数值校验（**仅校验，非证明**✓）

```
(1,2): d=1, a=1, b=2 | cos(px)-T_a(cos dx) maxerr=0.00e+00 | cos(qx)-T_b maxerr=2.22e-16
(1,4): d=1, a=1, b=4 | cos(px)-T_a(cos dx) maxerr=0.00e+00 | cos(qx)-T_b maxerr=8.88e-16
(2,3): d=1, a=2, b=3 | cos(px)-T_a(cos dx) maxerr=2.22e-16 | cos(qx)-T_b maxerr=5.55e-16
(2,5): d=1, a=2, b=5 | cos(px)-T_a(cos dx) maxerr=2.22e-16 | cos(qx)-T_b maxerr=1.33e-15
(3,5): d=1, a=3, b=5 | cos(px)-T_a(cos dx) maxerr=5.55e-16 | cos(qx)-T_b maxerr=1.33e-15
(7,11): d=1, a=7, b=11 | cos(px)-T_a(cos dx) maxerr=2.55e-15 | cos(qx)-T_b maxerr=5.55e-15
```
$$\textbf{结论}✓✓：\text{全部机器精度成立}✓ \Longrightarrow \textbf{唐先生的补刀被证实}✓✓；\texttt{C-283}\ \S6\ \text{的「存活面」确实不存在}✗✓$$

## §8 边界（总）

$$\textbf{零计算}✗（\S7.2\ \text{仅为恒等式校验}✓，\text{非拟合／非搜索}✓）；\text{未读 pending}✗；\text{未改他档正本}✓（\texttt{C-283}\ \text{为追加勘误}✓）$$
$$\textbf{未用}\ RH✓；\text{未动}\ v4✗；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$
