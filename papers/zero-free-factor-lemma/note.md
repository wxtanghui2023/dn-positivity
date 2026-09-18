D0: 本档对象 = "整因子乘法不移动零点"这一**初等分解事实**及其对**变形分类问题**的推论 —— 关系 = 独立小注记（引理本身初等；内容在推论），非 RH 相关新机制
D1: 0

FREEZE-ACK: 本档即冻结期内的独立小注记（依 `§8.1`；不产候选）

# 零点位置在"乘性变形"下的不变性 —— 一则初等观察及其推论

**作者**：Hui Tang ｜ **性质**：独立小注记（negative/expository）｜ **日期**：2026-09-18

---

## §0 范围（先声明本文**不**主张什么）

$$\text{本文证明一个}\ \textbf{初等} \text{的分解事实，}\ \text{并给出它对}\ \textbf{"变形类问题"} \text{的一个推论}✓$$
$$\qquad \textbf{不主张}：\text{引理是新的}（\text{它极可能是 folklore —— 见 §4}）;\ \textbf{不主张} \text{任何 RH 相关内容}✓$$
$$\qquad \textbf{主张}：\text{该事实}\ \textbf{一次性} \text{排除一整类"变形"}\ \text{（\text{乘性／完成化因子类}）}\ \text{作为"移动零点"的工具}✓✓$$

## §1 引理（含证明）

$$\textbf{引理 1}：\text{设}\ f\ \text{亚纯于}\ \mathbb C，\ g\ \text{整} \Longrightarrow Z(fg)=Z(f)\cup Z(g)\（\text{按重数计}\）,\quad \operatorname{Poles}(fg)=\operatorname{Poles}(f)✓$$
$$\textbf{证明}：\text{对}\ z_0\in\mathbb C，\operatorname{ord}_{z_0}(fg)=\operatorname{ord}_{z_0}f+\operatorname{ord}_{z_0}g;\ \text{而}\ g\ \text{整故}\ \operatorname{ord}_{z_0}g\ge0✓$$
$$\qquad \Longrightarrow \text{每个}\ f\ \text{的零点}\ \textbf{原地保留}（\text{阶数只增不减}）;\ \textbf{无任何零点发生位移}\quad\blacksquare✓$$

$$\textbf{推论 1（"乘性变形不移动零点"）}：\text{下列变形}\ \textbf{一律不改变}\ f\ \text{的零点位置}✓✓：$$
$$\qquad \text{(a)}\ f\mapsto f\cdot h\ \text{（}h\ \text{整}）;\qquad \text{(b)}\ \text{系数侧乘性卷积}\ f\ \text{的 DS}\ \mapsto\ \text{DS}(f)\cdot G(s)\（G\ \text{整}）;$$
$$\qquad \text{(c)}\ \text{任何"完成化因子"替换}（\Gamma\ \text{、指数、常数}\）—— \text{皆居}\ (a)✓$$
$$\Longrightarrow \text{此类变形}\ \textbf{能"看见"的零点，全是它自己带进来的}（h\ \text{或}\ G\ \text{的零点}）,\ \text{与原函数的零点位置}\ \textbf{无关}✓✓$$

## §2 推论 2：完成化变形在原理上不能触碰临界带零点

$$\Gamma\ \text{在}\ \mathbb C\ \text{无零点};\ q^{-s/2}\neq0\ \forall s \Longrightarrow \text{完成化因子}\ \textbf{整且零-free}✓$$
$$\qquad \Longrightarrow \text{改动完成化因子（含导子／}\Gamma\text{-移位）是}\ \textbf{保零集变换} \Longrightarrow \textbf{对零点结构性不可见}✓✓$$
$$\qquad \text{又：泛函方程}\ \Lambda(s)=\omega\Lambda(1-s)\ \text{给出的是}\ \textbf{对称轴}（\operatorname{Re}s=\tfrac12）,\ \textbf{不是点}✓$$
$$\Longrightarrow \text{故"经完成化／对称性编码"的路线}\ \textbf{只能给轨道}，\ \textbf{不能给对齐／定位}✓✓$$

## §3 推论 3：零点的"移动性"逼出非乘性操作

$$\text{要}\ \textbf{移动}\ f\ \text{的零点}，\ \text{必须}\ \textbf{非乘性} \text{地作用于}\ f\（\text{推论 1 的逆否}）✓✓$$
$$\qquad \text{已知的"移动零点"操作只有两类}：$$
$$\qquad \qquad \text{(i)}\ s\text{-空间卷积}（\text{如热流}\ f*G_t）—— \textbf{真移动零点}，\ \text{但属}\ \textbf{坐标型操作}✓✓$$
$$\qquad \qquad \text{(ii)}\ \text{系数侧截断／逐点非线性}—— \textbf{移动零点} \text{但}\ \text{极限／可控性另有代价}✓$$
$$\Longrightarrow \text{由此得到一个}\ \textbf{张力}：\text{"算术型（系数侧）"与"能移动零点"}\ \textbf{在乘性通道内不可兼得}✓✓$$
$$\qquad \text{这解释了为什么}\ \textbf{热流（de Bruijn–Newman）} \text{是}\ \textbf{唯一已知的典范变形}：\ \text{它是}\ (i)\ \text{型}✓✓$$

## §4 与文献的关系（诚实；投稿前必办）

$$\textbf{引理 1}\ \text{本身}\ \textbf{极可能是 folklore}：\ \text{它是}\ \text{"}\operatorname{ord}(fg)=\operatorname{ord}f+\operatorname{ord}g\text{"}\ \text{的直接改写}✓✓$$
$$\qquad \Longrightarrow \textbf{投稿前必办}：\text{检索}\ \text{"factorization zeros entire factor"／"Hadamard factorization"／}\text{复分析教科书};\ \textbf{若确为 folklore}，\ \text{本文定位应改为}\ \textbf{说明性注记}✓$$
$$\textbf{推论 2／3}\ \text{的内容量更大}，\ \text{但}\ \text{其各部分在文献中}\ \textbf{可能已散见}（\text{"完成化因子零-free"是常识}）✓$$
$$\qquad \Longrightarrow \text{本文可主张的}\ \textbf{唯一形态}：\text{把}\ (1)(2)(3)\ \text{组织为}\ \textbf{"变形分类"的一个判据}，\ \text{并明确指出}\ \textbf{非乘性＋系数侧的第四类尚未实例化}✓✓$$

## §5 何者可证伪本文的相关判断

$$\text{若出现}\ \textbf{一个乘性变形却改变了零点位置} \Longrightarrow \text{引理 1 有误}（\text{不可能：}\blacksquare\ \text{已证}）✓$$
$$\text{若出现}\ \textbf{一个非乘性、系数侧、且极限恢复零结构的典范操作} \Longrightarrow \text{§3 的"张力"是}\ \textbf{方法性} \text{而非}\ \textbf{结构性}✓✓$$

## §6 边界

- ⚠️ 引理 1 与推论 1 为**初等且完整证明**；**推论 2 的"零-free ⟹ 不可见"** 亦为证明级 ✓
- ⚠️ §3 的"已知操作只有两类"为**观察**（非穷尽性定理），标 `[结构性]` ✓
- ⚠️ **不涉及** RH 的真假；**未用** RH ✓
- ⚠️ §4 的 folklore 检索**尚未执行**，故本文**不得**对外声称新性 ✓
