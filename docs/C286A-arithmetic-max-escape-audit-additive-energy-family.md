已查地图（**先查后写**）：`C-285`（**分离坍塌定理** ＋ 逃逸接口分类 ＋ 四条件门 ＋ **§6 算术极大替换登记**）、`C-284`（通用切比雪夫退化 ＋ 增益来源诊断）、`C-283`、`C-282`（Δ–Γ 恒等式）、`C-275`（组合空洞定理）、`C-257`（第三族＝换量）、`C-113`（β/γ 二分）。回查见 §8 ✓

D0: 本档对象 = **C-286-A：Arithmetic-Max Escape Audit（加法能量族）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{① 判定}✗✓：\text{自然的算术-max 形}\ \mathcal T_{\mathcal A}(\theta)=\sup_{A\in\mathcal A}\mathcal F_A(\theta)\ \text{中，若}\ \mathcal F_A=\max_{k\in A}\sum_j\cos(k\theta_j)✓，\text{则其}\ \textbf{不可分性来源与原始问题}\textbf{同源}✗（\text{只有那个}\max✓） \Longrightarrow \textbf{架构内重包装}✗✓}$$
$$\boxed{\textbf{② 加法能量是标量}✗✓：E(A)=\#\{(a,b,c,d)\in A^4:\ a+b=c+d\}✓\ \textbf{只依赖集合}\ A✓，\textbf{完全不含}\ \theta✓ \Longrightarrow \textbf{无内在耦合接口}✗✓}$$
$$\boxed{\textbf{③ 条件⑥失败}✗✓：E(A)=\int_0^1\big|P_A(t)\big|^4dt=\big[P_A^2\ \text{的零次 Fourier 系数}\big]✓（\textbf{精确恒等式}✓，\textbf{非表示选择}✗） \Longrightarrow \textbf{经 Fourier 落回旧闭包}✗✓}$$
$$\boxed{\textbf{④ 条件③失败}✗✓：\text{要让加法结构}\textbf{进入泛函本身}✓，\text{必须}\textbf{人为构造} \mathcal F_A✗（\text{如把四元组结构塞进表达式}✓） \Longrightarrow \textbf{非独立算术来源}✗✓}$$
$$\boxed{\textbf{⑤ ⭐ 关系型耦合缺口（本刀强边界）}✓✓：\text{加法结构}\textbf{唯一} \text{能耦合坐标的途径＝坐标间}\ \theta_i+\theta_j=\theta_k+\theta_l✓；\text{而乘积箱}\ B=\prod I_j\ \textbf{不含任何关系}✗ \Longrightarrow \text{任何关系都是}\textbf{额外假设}✗；\text{已知关系源（零点相关／Montgomery）}\textbf{是 RH-条件性的}✗ \Longrightarrow \textbf{不可作为假设使用}✗✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{零}\ RH\ \text{使用}✗；\text{未读 pending}✗；\text{不跑 v4}✗；\text{不重碰 M=5}✗$$

## §1 两情形判据的形式化（✓✓）

$$\textbf{通式}✓（\text{唐先生}）：\mathcal T_{\mathcal A}(\theta):=\sup_{A\in\mathcal A}\mathcal F_A(\theta_1,\ldots,\theta_5)✓$$
$$\textbf{情形 I（逐项和）}✗：\mathcal F_A=\sum_jf_{A,j}(\theta_j) \Longrightarrow \inf_B\mathcal F_A=\sum_j\inf_{I_j}f_{A,j}✓ \Longrightarrow \sup_A\inf_B\mathcal F_A\le\inf_B\sup_A\mathcal F_A✓ \Longrightarrow \textbf{回到 max/min 交换墙}✓ \Longrightarrow \textbf{判架构内重包装}✗$$
$$\textbf{情形 II（算术对象连接多坐标）}✓：\mathcal F_A\ne\sum_jf_{A,j}(\theta_j)✓，\text{且不可分性}\textbf{来自}\ A\ \text{的算术关系}✗（\text{非人为加入}\ \theta_i-\theta_j✗）\ \text{—— 才可能逃出}\ \texttt{C-285}✓$$
$$\textbf{本刀适用}✓：\text{加法能量的候选嵌入}\ \mathcal F_A=\max_{k\in A}\sum_j\cos(k\theta_j)✓\ \textbf{不属情形 I}✗（\max\ \text{破坏可分}✓）\ \text{—— 但其}\max\ \textbf{与原始同源}✗✓（见\ \S3✓）$$

## §2 加法能量的精确定义与恒等式（✓✓）

$$\textbf{定义}✓：E(A):=\#\{(a,b,c,d)\in A^4:\ a+b=c+d\}✓=\sum_m r(m)^2✓，\ r(m):=\#\{(a,b)\in A^2:\ a+b=m\}✓$$
$$\textbf{精确恒等式}✓✓（\text{Parseval／Wiener}✓）：\text{令}\ P_A(t):=\sum_{a\in A}e^{2\pi iat}✓ \Longrightarrow E(A)=\int_0^1\big|P_A(t)\big|^4dt✓$$
$$\qquad \text{等价写法}✓：\big|P_A(t)\big|^4=\sum_mR(m)e^{2\pi imt}✓，\ R(m):=\#\{(a,b,c,d):a+b-c-d=m\}✓ \Longrightarrow E(A)=R(0)✓（\textbf{零次系数}✓）$$
$$\textbf{结构结论}✓✓：E(A)\ \text{是}\ \textbf{集合}\ A\ \text{的标量泛函}✓，\textbf{不含}\ (\theta_1,\ldots,\theta_5)✗ \Longrightarrow \textbf{与箱问题无接口}✗✓$$
$$\qquad \Longrightarrow \text{若要使用，必须}\textbf{外接} \text{耦合}✓ \Longrightarrow \textbf{立即违反「结构性来源」}✗✓$$

## §3 三问回答（✓✓）

### §3.1 问一：$\inf_B\sup_A\mathcal F_A$ 能否由逐坐标极小值确定？（✓）

$$\textbf{答}✓：\textbf{不能}✓（\text{确有非可分性}✓）—— \text{但}\textbf{来源与原始相同}✗✓$$
$$\qquad \text{由}\ \texttt{C-284}\ \text{推论}✓：\max_{k\in A}\sum_j\cos(k\theta_j)=\max_{k\in A}\sum_jT_{k/d_A}(c_j)✓，\ c_j:=\cos(d_A\theta_j)✓，\ d_A=\gcd A✓$$
$$\qquad \Longrightarrow \text{整个对象是}\ \textbf{五向量}\ (c_1,\ldots,c_5)\ \text{的函数}✓；\text{耦合}\textbf{完全来自那个}\max✗✓$$
$$\qquad \textbf{而原始目标}\ \mathcal T(\theta)=\max_{k\le25}\sum_j\cos(k\theta_j)\ \textbf{的同源结构完全相同}✗ \Longrightarrow \textbf{无新增不可分性来源}✗✓$$

### §3.2 问二：$\mathcal F_A$ 是否有独立算术定义？（✗）

$$\textbf{答}✗：\text{两条路都不通}✓：\text{① 取}\ \mathcal F_A=\max_{k\in A}\sum_j\cos(k\theta_j✓) \Longrightarrow A\ \text{只起}\textbf{筛选频率} \text{的作用}✓，\text{算术内容仅是「选了哪些}\ k」\ ✓ \Longrightarrow \textbf{非独立算术来源}✗$$
$$\qquad \text{② 把四元组结构塞进泛函}✓（\text{如}\ \sum_{a+b=c+d}\cos(\cdot)✓） \Longrightarrow \textbf{人为构造}✗✓ \Longrightarrow \text{违反}\ ③✓$$

### §3.3 问三：是否有可识别的 β-native channel？（✗）

$$\textbf{答}✗✓：E(A)\ \text{只依赖频率集合}\ A✓，\textbf{不含}\ \theta✓，\textbf{不含零点数据}✗ \Longrightarrow \textbf{无通往}\ \beta\ \text{的通道}✓$$
$$\qquad \text{更一般}✓：\text{计数／能量型对象＝}\textbf{量值侧} \text{量}✓ \Longrightarrow \text{与}\ \texttt{C-113}\ \text{的}\ \beta/\gamma\ \text{二分相容}✗ \Longrightarrow \textbf{仅触及频率侧}✓$$

## §4 条件⑥检验（**经 Fourier 落回旧闭包**✗✓）

$$\textbf{条件⑥}✓（\text{唐先生新增}✓）：\text{算术对象}\overset{\text{变换}}{\longrightarrow}\text{旧有限频率闭包} \Longrightarrow \textbf{淘汰}✗$$
$$\textbf{本刀检验}✗✓：E(A)\ \text{的 Fourier 形式}\ \int|P_A|^4\ \textbf{就是} \text{有限频率三角多项式}✓；\text{且}\ \big|P_A(t)\big|^4=\sum_mR(m)e^{2\pi imt}\ \textbf{是恒等式}✗（\text{非「表示选择」}✗）$$
$$\qquad \Longrightarrow \text{不存在「只看算术定义、回避 Fourier 表象」的余地}✗✓ \Longrightarrow \textbf{条件⑥失败}✗$$
$$\qquad \textbf{注}✓✓：\text{唐先生要求「追踪原始算术定义」}\ \textbf{已执行}✓ —— \text{结论是原始定义与 Fourier 形式}\textbf{互相确定}✗（\text{无隐藏内容}✓）$$

## §5 ⭐ 关系型耦合缺口（**本刀强边界**✓✓）

$$\textbf{论证}✓✓：\text{加法结构的几何意义}＝\text{坐标间}\textbf{关系}✓（\theta_i+\theta_j=\theta_k+\theta_l \Longrightarrow z_iz_j=z_kz_l✓，\ z_j=e^{i\theta_j}✓）$$
$$\qquad \Longrightarrow \text{这是}\ \textbf{唯一} \text{能让加法结构真正耦合五个坐标的途径}✓$$
$$\textbf{但}✗✓：B=I_1\times\cdots\times I_5\ \textbf{不含} \text{任何坐标间关系}✗（\text{笛卡尔积＝坐标独立}✓，\texttt{C-285}\ \S2✓）$$
$$\qquad \Longrightarrow \text{任何坐标关系都是}\textbf{额外假设}✗ \Longrightarrow \text{违反「结构性来源」}✓$$
$$\qquad \textbf{已知的算术关系源}✗✓：\text{零点相关性／Montgomery 对相关}✓ \Longrightarrow \textbf{RH-条件性}✗ \Longrightarrow \textbf{不可作为假设}✗✓（\text{否则循环}✓）$$
$$\Longrightarrow \boxed{\textbf{关系型耦合缺口}✓✓：\text{在乘积箱＋无条件输入下，加法结构}\textbf{无法提供坐标耦合}✗✓}$$

## §6 出口判定（✓✓）

$$\boxed{\textbf{A 出口（加法能量）＝淘汰}✗✓：\text{失败于}\ ③（\text{无独立算术来源}✓）\ \text{与}\ ⑥（\text{Fourier 落回闭包}✓）}$$
$$\qquad \textbf{且}⑤\ \text{亦失败}✓（\text{无}\ \beta\ \text{通道}✓）；\text{① 的「非可分性」}\textbf{与原始同源}✗ \Longrightarrow \textbf{无新增逃逸}✗✓$$
$$\textbf{信息价值}✓✓（\text{唐先生预判}✓）：\text{「算术极大」中最自然的}\textbf{加法关系} \text{也无法提供所需逃逸}✓ \Longrightarrow \text{这是}\textbf{强信息}✗✓$$
$$\textbf{登记纪律}✓：\text{本刀}\textbf{不} \text{写成「加法能量无用」}✗；\text{只写「在当前架构＋无条件输入下不能作为供给源」}✓$$
$$\textbf{下一步}✓（\text{按唐先生优先序}✓）：\text{转入}\ \texttt{C-286-B}\ \text{除数族}✓ \Longrightarrow \text{再}\ \texttt{C-286-C}\ \text{素数族}✓$$

## §7 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{零}\ RH\ \text{使用}✗；\text{未读 pending}✗；\text{不跑 v4}✗；\text{不重碰 M=5}✗$$
$$\textbf{② 结论强度}✓：\S2\ \text{的恒等式＝}\textbf{经典定理}✓；\S3／\S5＝\textbf{结构性论证}✓（\text{非定理}✗）；\S5\ \text{为}\textbf{边界主张}✓，\text{可随新证据修订}✓$$
$$\textbf{③ 不得} \text{写成}✗：\text{「加法能量数学上无用」}✗；\text{「所有算术极大都不可能」}✗（\text{只判 A}✓）；\text{「M=5 判死」}✗$$
$$\textbf{④ 未改他档正本}✓；\text{未动}\ v4✗；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

## §8 【技术词回查】输出（**先跑后写**✓）

```
技术词 同源不可分性   命中文件数=0    ::
技术词 加法能量标量化 命中文件数=0    ::
技术词 关系型耦合缺口 命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{分离坍塌定理}✓（\texttt{C-285}\ \S2✓）；\text{通用切比雪夫退化}✓（\texttt{C-284}✓）；\text{四条件门＋条件⑥}✓（\texttt{C-285}\ \S5✓／\text{唐先生}✓）；\text{β/γ 二分}✓（\texttt{C-113}✓）；\text{Parseval／Wiener 恒等式}✓（\text{经典}✓）$$
