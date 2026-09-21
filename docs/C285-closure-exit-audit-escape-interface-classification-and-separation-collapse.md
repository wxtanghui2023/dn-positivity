已查地图（**先查后写**）：`C-284`（**通用切比雪夫退化**：任意有限整数频率同点泛函 ⊂ ℝ[cos(dx)] ＋ **增益来源诊断**）、`C-283`（A′ 第一刀，§6 已勘误）、`C-282`（Δ–Γ 恒等式 ＋ 桥 GAP）、`C-281`（C_ε ＋ 路径宽度）、`C-280`（两对空交）、`C-275`（组合空洞定理）、`C-257`（第三族＝量侧/换量）、`C-111`/`C-113`（β/γ 二分）、`V188` §4（四通道穷尽）。回查见 §8 ✓

D0: 本档对象 = **C-285：Closure-Exit Audit —— 逃逸接口分类 ＋ 分离坍塌定理**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{① 逃逸的形式化条件}✓✓：\text{在固定乘积箱}\ B=\prod_{j=1}^5I_j\ \text{上，\textbf{任何}「}\inf_B\sum_ja_j(\theta_j)>\tfrac12」\ \text{型证书}\ \textbf{必因子化}✗ \Longrightarrow \textbf{逃逸必须在「换问题」层面}✓✓}$$
$$\boxed{\textbf{② ⭐ 分离坍塌定理}✓✓：B\ \text{为乘积} \Longrightarrow \inf_B\sum_ja_j=\sum_j\inf_{I_j}a_j✓；\text{若各}\ a_j\ \text{属}\ \texttt{C-284}\ \text{类} \Longrightarrow \text{每个}\ \inf_{I_j}a_j\ \text{只是}\ \cos(d_j\theta_j)\ \textbf{值域} \text{的函数}✓✓}$$
$$\qquad \Longrightarrow \boxed{\text{当前架构（乘积箱＋逐坐标和式证书）内}\ \textbf{逃逸不可能}✗✓} \Longrightarrow \text{逃逸＝换量／换问题}✓$$
$$\boxed{\textbf{③ 四类候选判定}✓（表见\ \S3✓）：\text{更多}\ p,q,\lambda\ ✗\ \text{立即排除}✓；\text{有限整数频率同点}\ \Phi\ ✗\ \texttt{C-284}\ \text{封死}✓；\text{非同点／跨坐标}\ ✓\ \text{重点}✓；\text{非周期／算术对象}\ ✓\ \text{重点}✓}$$
$$\boxed{\textbf{④ 三接口首轮审计}✓✓：\text{I 加法结构}\ ✗\ \textbf{已被占用且封死}✓（\text{它就是当前架构}✓）；\text{II 乘法–加法混合}\ ✓\ \text{真逃逸＋算术内容}✓\ \textbf{但}\ \beta\ \text{界面被 parity 挡}✗；\text{III 模}\ m\ \text{关系型}\ ✓\ \text{逃逸但}\ ④⑤\ \text{不明}✗ \Longrightarrow \textbf{首轮无 survivor}✗✓}$$
$$\boxed{\textbf{⑤ 合法方向登记（非答案}✓）：\textbf{算术极大替换}✗✓ —— \text{把}\ \max_k（\text{频率}）\ \text{换成}\ \textbf{算术族上的}\max（\text{除数／素数／加法能量}✓），\text{检验其}\inf\ \text{是否}\textbf{结构性不可因子化}✓\ \text{且}\ \beta\text{-native}✓}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{零}\ RH\ \text{使用}✗；\textbf{零文献大搜}✗；\text{未读 pending}✗$$

## §1 闭包与逃逸的形式化（✓✓）

$$\textbf{闭包}✓（\texttt{C-284}✓）：\mathcal C_{\rm cheb}:=\bigcup_{K\subset\mathbb N\ \text{有限}}\mathbb R\big[\cos(d_Kx)\big]✓，\ d_K=\gcd K✓ \Longrightarrow \textbf{任意有限整数频率同点泛函}\in\mathcal C_{\rm cheb}✗✓$$
$$\textbf{证书的通式}✓（\text{当前架构}✓）：\text{取}\ a_j:\mathbb R\to\mathbb R✓，\text{证书＝}\inf_{\theta\in B}\sum_j a_j(\theta_j)>\tfrac12✓$$
$$\textbf{逃逸条件}✓✓（\text{唐先生表述}✓）：\text{存在}\ \mathcal A\ \text{使}\ \inf_B\mathcal A\ \textbf{不等于任何逐坐标 separable 下界}✓，\text{且}\ \mathcal A\notin\mathcal C_{\rm cheb}✗$$
$$\qquad \textbf{关键增补}✓✓：\text{不可分性必须有}\textbf{结构性来源}✓，\text{不能只是写成难算的表达式}✗$$

## §2 ⭐ 分离坍塌定理（**证明**✓✓）

$$\textbf{定理}✓✓：\text{设}\ B=\prod_{j=1}^5I_j\ \text{为乘积}✓，\ a_j\ \text{任意}✓ \Longrightarrow \inf_{\theta\in B}\sum_{j=1}^5a_j(\theta_j)=\sum_{j=1}^5\inf_{I_j}a_j✓$$
$$\qquad \textbf{证明}✓：\text{坐标独立}✓；\geq\ \text{显然}✓；\text{取各坐标最小值点} \Longrightarrow =\ ✓ \blacksquare$$
$$\textbf{推论}✓✓：\text{若各}\ a_j\in\mathcal C_{\rm cheb}✓ \Longrightarrow \inf_{I_j}a_j=\min_{c\in C_{d_j}(I_j)}P_j(c)✓，\ C_{d_j}(I_j)=\cos(d_j\cdot)(I_j)\ \textbf{为区间}✓（\texttt{C-284}\ \S2✓）$$
$$\qquad \Longrightarrow \boxed{\text{证书的全部内容＝五组 }\cos(d_j\theta_j)\ \textbf{值域} \text{的函数}✗✓} \Longrightarrow \textbf{不含跨坐标信息}✗✓$$
$$\textbf{推论（本档主结论）}✓✓：\text{故在当前架构内，\textbf{任何}「更好的证书」} \text{都只能是}\ \textbf{值域数据的重新组合}✗ \Longrightarrow \textbf{逃逸}\textbf{不可能}✗✓$$
$$\qquad \Longrightarrow \textbf{任何未来候选必须表述为}\ \textbf{不同的极小化问题}✓✓，\text{而非「更好的证书」}✗ \Longrightarrow \textbf{预筛掉一整类提案}✓✓$$
$$\textbf{注}✓✓：\text{目标}\ \mathcal T(\theta)=\max_{1\le k\le25}\sum_j\cos(k\theta_j)\ \textbf{本身} \text{不可分}✗（\max\ \text{破坏可分}✓） \Longrightarrow \text{困难正源于此}✓；\text{v4 的证书＝放弃不可分性}✓（\max_k\sum_j\min_{I_j}\le\min_B\max_k\sum_j\cos✓）$$

## §3 四类候选 ＋ 四条件门（✓✓）

| 类别 | 逃出 C-284？ | 首轮判断 |
|---|---:|---|
| 更多 $p,q,\lambda$ | ✗ | **立即排除** ✓ |
| 有限整数频率的任意同点 $\Phi$ | ✗ | **C-284 封死** ✓ |
| 非同点／跨坐标结构 | ✓ | **重点检查** ✓ |
| 非周期／算术对象 | ✓ | **重点检查** ✓ |

$$\textbf{四条件门}✓✓（\text{缺一即停}✓）：\textbf{Escape}✓\ ∧\ \textbf{Independent arithmetic content}✓\ ∧\ \textbf{New quantitative invariant}✓\ ∧\ \textbf{Potential RH interface}✓$$
$$\textbf{危险墙}✓✓（\text{唐先生预置}✓）：\text{不可用}\ \theta_i-\theta_j,\ \cos(\theta_i-\theta_j),\ e^{i(\theta_i-\theta_j)}\ \textbf{直接宣布成功}✗$$
$$\qquad \text{因}\ B\ \text{是笛卡尔积}✓ \Longrightarrow \text{若}\ \inf\ \text{时仍可独立取各坐标}✓ \Longrightarrow \textbf{跨坐标项重新退化为可分}✗✓（\S2✓）$$

## §4 三接口首轮审计（✓✓）

$$\textbf{I 加法结构（}n_1+\cdots+n_r=N\text{）}✗✓：\text{这}\textbf{正是} \text{当前架构}✓（\text{同点相位和}✓＝\text{Turán 幂和}✓）；\text{且}\ \texttt{C-284}\ \text{已封}✗ \Longrightarrow \textbf{已被占用且封死}✗$$
$$\textbf{II 乘法–加法混合（}ab=c,\ a+b=N\text{）}✓✗：\textbf{真逃逸}✓（\text{乘性结构不在三角函数闭包内}✓）＋\textbf{算术内容}✓（\text{素性／除子结构}✓）；$$
$$\qquad \text{但}\ \textbf{界面被 parity 挡}✗✓：\text{结构性分解}\（\mu^2(n)=\sum_{d^2\mid n}\mu(d)✓）\ \text{与素数缺少该分解}✗ \Longrightarrow \textbf{条件}\ ⑤\ \text{失败}✗$$
$$\textbf{III 模}\ m\ \text{关系型（}x_i\equiv x_j\bmod m\text{）}✓⬜：\text{逃逸}✓（\text{关系型约束非可分}✓）＋\text{算术来源}✓（\text{同余}✓）；\text{但}\ ④\ \text{（可量化 invariant}）\ \text{与}\ ⑤\ \text{（}\beta\ \text{接口}）\ \textbf{均不明}✗ \Longrightarrow \textbf{不得当作 survivor}✗$$
$$\Longrightarrow \boxed{\textbf{首轮 verdict}✓：\textbf{无 candidate 通过四条件门}✗ —— \text{但}\ \textbf{边界已划清}✓✓（\text{本刀目标达成}✓）}$$

## §5 五条件成功标准（**预注册**✓✓）

$$\boxed{\text{① 明确的新对象}\ \mathcal A✓；\quad \text{② 证明}\ \mathcal A\notin\mathcal C_{\rm cheb}✓；\quad \text{③ 有独立算术问题／定理作为来源}✓；\quad \text{④ 存在可量化 invariant}✓；\quad \text{⑤ 能解释它为何可能接触}\ \beta\ \text{而非只接触}\ \gamma✓}$$
$$\textbf{门槛}✓✓（\text{唐先生设定}✓）：\textbf{只满足①②不算 survivor}✗；\text{③④⑤ 缺一即停}✓$$
$$\qquad \Longrightarrow \textbf{防止再现} \text{「数学上有新表达式}\to\text{漂亮}\to\text{发现无 arithmetic content」}\ \text{的循环}✗✓$$

## §6 合法方向登记（**非答案**✓）

$$\textbf{方向}✓✓：\textbf{算术极大替换}✗✓ —— \text{把目标的}\ \max_{1\le k\le25}\ \text{换成}\ \textbf{算术族上的极大}✓$$
$$\qquad \text{候选极大族}✓：\text{除子}\ d\mid n✓；\text{素数}\ p\le P✓；\text{加法能量}\ r_{2}(n)✓；\text{特征}\ \chi\bmod q✓$$
$$\textbf{检验要点}✓✓：\text{① 其}\ \inf_B\ \text{是否}\ \textbf{结构性不可因子化}✓（\S2✓）；\text{② 是否}\ \beta\text{-native}✓（\text{非仅}\ \gamma✓）；\text{③ 是否违反}\ \texttt{V188}\ \S4\ \text{四通道}\✗✓$$
$$\qquad \textbf{注}✓：\text{本方向}\textbf{尚未} \text{被本档证明可行}✗；\text{仅登记为}\ \textbf{合法入口}✓，\text{且必须先过四条件门}✓$$

## §7 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{零}\ RH\ \text{使用}✗；\textbf{零文献大搜}✗；\text{未读 pending}✗$$
$$\textbf{② 本档结论强度}✓：\S2\ \textbf{定理}✓（\text{分离坍塌}✓）；\S3\ \text{分类＝}\textbf{判定}✓，\text{非定理}✗；\S4\ \text{接口审计＝}\textbf{首轮}✓，\text{可随新证据修订}✓$$
$$\textbf{③ 不得} \text{写成}✗：\text{「所有新对象都不可能」}✗（\text{本档只封当前架构}✓）；\text{「III 已死」}✗（\text{仅「④⑤不明」}✓）；\text{「M=5 判死」}✗（\text{不涉及}✓）$$
$$\textbf{④ 未改他档正本}✓；\text{未动}\ v4✗；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

## §8 【技术词回查】输出（**先跑后写**✓）

```
技术词 分离坍塌定理 命中文件数=0    ::
技术词 逃逸接口     命中文件数=0    ::
技术词 算术极大替换 命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{通用切比雪夫退化 ＋ 增益来源诊断}✓（\texttt{C-284}✓）；\text{组合空洞定理}✓（\texttt{C-275}✓）；\text{第三族＝换量}✓（\texttt{C-257}✓）；\text{β/γ 二分}✓（\texttt{C-113}✓）；\text{四通道穷尽}✓（\texttt{V188}\ \S4✓）$$

## §9 附：本档与主线的关系（✓）

$$\text{链条}✓✓：\texttt{C-283/C-284}\ \text{（同点整数频率闭包）} \Longrightarrow \textbf{A 出口整体封锁}✗ \Longrightarrow \texttt{C-285}\ \textbf{（逃逸接口划界）}✓ \Longrightarrow \text{先找 genuinely non-separable arithmetic object}✓ \Longrightarrow \text{再查}\ \beta\text{-native interface}✓ \Longrightarrow \textbf{只有通过者进入构造／计算}✓$$
