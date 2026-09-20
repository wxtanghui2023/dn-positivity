已查地图（**先查后写**）：查 `C-214`（下界重估）、`C-195`／`C-178`／`C-177`（区间认证先例与四门）、`C-213`（三层账本）。回查见 §6 ✓

D0: 本档对象 = **甲：interval B&B @ $T=0.7640811$ 的启动登记** ＋ **边界收紧**（float 探针 ≠ 已证）＋ **三个 self-error 正式登记** ＋ **新证明架构** —— 关系 = 推进 ＋ 勘误登记
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 ⚠️ 边界收紧（唐先生 2026-09-20 12:13，全盘采纳）

$$\textbf{① 核心发现成立}：\text{此前的}\ 0.76\ \textbf{不能再视为结构性墙}✓✓ \Longrightarrow \textbf{撤销}"仍有}\ 4.08\times10^{-3}\ \text{困难全局缺口}"的读法}✓$$
$$\qquad \text{准确表述}：\boxed{\text{此前的}\ 0.76\ \text{是当前实现／工作量上的【停点】，而非已发现的解析墙}}✓✓$$
$$\textbf{② 但}\ T=0.76408110075\ \text{的 66 个 unresolved 要单独看}✓：\text{价值不在数量}✗，\text{而在}\ \textbf{空间集中性}✓✓（\min d\simeq2.740\times10^{-9}✓）$$
$$\qquad \text{⚠️ 该统计须先【严格固定】距离定义（箱代表点 vs 箱集合 ✓）之后才可引用为层 2 事实}✓$$
$$\textbf{③ 不能说"}\ T=0.76408110075\ \text{已经可证}\text{"}✗✗：\text{阶梯探针是}\ \textbf{float}✗ \Longrightarrow \text{只能记作}$$
$$\qquad \boxed{\text{【候选严格下界的计算探针／interval-B&B 待复现目标】}}✓✓$$
$$\qquad \textbf{严格账本（现版）仍为}：\boxed{0.76\ \le\ m_3\ \le\ 0.76408110074585388514756267472105}✓$$
$$\qquad \text{若四门 interval 逻辑跑通，方可升级为}\ 0.7640811\le m_3\le0.76408110074585\ldots✓ \text{（届时缺口}\ 7.4585\times10^{-9}✓，较原缩约\ 5.47\times10^6\ \text{倍}✓✓）$$
$$\qquad \text{⚠️ 该数字可报告，但必须标为}\ \textbf{预期的严格证书升级}✓\ \text{而非现成事实}✗$$

## §1 ⭐ 甲：interval B&B @ $T=0.7640811$（已启动）

$$\text{脚本}：\texttt{scripts/m3\_certificate\_interval\_arith.py}✓（\texttt{C-177}\ \text{的区间算术版}✓）$$
$$\qquad \textbf{无 SLACK、无浮点误差假设}✓✓：\text{箱边界为精确有理数（Fraction）✓；域取}\ [0,P]^3✓（P>\pi\ \text{有理上界}✓，\text{故含}\ [0,\pi]^3✓）；k a_j\ \text{为精确有理数}✓；\cos\ \text{用}\ \texttt{mpmath.iv}✓；\text{奇数倍}\ \pi\ \text{用}\ \pi\ \text{区间严格判定}✓（\text{不确定取}−1✓）$$
$$\text{启动参数}：\text{预算}\ 3{,}000{,}000\ \text{箱}✓,\ \text{最大深度}\ 60✓,\ M=3✓,\ \text{目标}\ \mathbf{0.7640811}✓\ \text{（}\texttt{repr}\ \text{保精确十进制}✓）$$
$$\qquad \text{日志}\ \texttt{/tmp/m3\_iv\_764.log}✓（\text{脚本仅结束时打印}✓）$$
$$\text{目标陈述（非"证明全局最优"）}：\boxed{\forall\varphi\in[0,\pi]^3:\ F_3(\varphi)\ \ge\ 0.7640811}✓$$
$$\qquad \text{若四门通过} \Longrightarrow \text{立即把层 1 下界从}\ 0.76\ \text{推到}\ 0.7640811✓✓$$

## §2 ⚠️ 乙的关键更正（唐先生的警告，完全采纳）

$$\textbf{不能因为 unresolved 区域只有}\ 10^{-9}\ \text{量级就宣布局部刚性已覆盖}✗✗$$
$$\qquad \text{因为}\ 10^{-9}<\rho_{\rm lower}^{(0)}\approx1.716\times10^{-7}✓ \Longrightarrow \text{修正后的局部增长不等式在【最靠近中心的那一小层】仍存在}\ \delta_A\ \text{缺口}✓✓$$
$$\qquad \delta_A^{(0)}\approx9.269\times10^{-8}✓,\qquad c^{(0)}=0.540247961✓,\qquad R=169✓$$
$$\Longrightarrow \textbf{乙真正要做的是}：\boxed{\text{把}\ x_0^*\ \text{内核}\ (0,\ \rho_{\rm lower}]\ \text{单独严格处理掉}}✓✓\ \text{——\ 这反而是【现在最明确、最小的剩余问题】}✓$$

## §3 ⭐ 新证明架构（甲、乙各自成功后）

$$\boxed{\ \text{全域}\ =\ \underbrace{\text{B\&B 可分区域}}_{\Rightarrow F\ge0.7640811} \ \cup\ \underbrace{\text{极小}\ x_0^*\ \text{内核}}_{\Rightarrow F\ge F(x_0^*)\ (\text{或}\ \ge 0.7640811)} \ }✓✓$$
$$\qquad \text{这与"搜索找到一个漂亮点"有本质区别}✓✓：\text{第一次形成}\ \boxed{\text{global exclusion}\ +\ \text{local analytic closure}}\ \text{的闭环}✓$$
$$\qquad \text{若乙进而能证}\ x_0^*\ \text{在内核内唯一极小}✓，\text{并与严格上界点衔接} \Longrightarrow \text{才有资格写}\ m_3=F(x_0^*)✓（\text{现在仍不能提前宣布}✗）$$

## §4 ⭐⭐ T13-A 战略状态（唐先生指定格式）

$$\boxed{\ \begin{array}{c} \textbf{原判断：}\\ 0.76\to0.7640811\ \text{是一个可能的全球困难缺口}\\ \Downarrow\\ \textbf{新判断：}\\ \text{B\&B 已可计算地推进至}\ m_3-10^{-9}\ \text{量级，}\\ \text{剩余困难高度集中于}\ x_0^*\ \text{的极小内核} \end{array}\ }✓✓$$

## §5 三个 self-error 正式登记（唐先生要求保留，不淡化）

$$\textbf{①（最重要）}：\text{把【阻尼】}M{=}3\ \text{的}\ T=0.765\ \text{爆炸错误外推到当前 undamped 问题}✗✗$$
$$\qquad \text{直接导致了错误的战略判断"0.76 附近存在墙"}✗ \Longrightarrow \textbf{已被实验性推翻}✓✓（\texttt{C-214}\ §3②✓）$$
$$\qquad \textbf{教训}：\text{不同问题（阻尼／无阻尼）的"墙"记录}\ \textbf{不得互相搬用}✗；\text{且须先核对}\ T\ \text{与真值的序关系}✓$$
$$\textbf{②}：\text{Fraction 精确算术实现的性能判断失真}✗（\texttt{cosmin}\ \text{首版用 Fraction ⟹ 慢到阻塞}✓）$$
$$\qquad \textbf{教训}：\text{【探测】与【证书】分档}✓ —— 探测用 float ✓，只有证书才需要精确算术 ✓$$
$$\textbf{③}：\text{第二次出现}\ \texttt{pgrep -f "含自身命令行的字符串"}\ \text{自杀式误杀}✗（\texttt{TOOLS.md}\ \text{已明确记录}✓）$$
$$\qquad \Longrightarrow \text{改"先查后杀"分离写法}✓；\textbf{硬记}：\text{任何}\ \texttt{pgrep/pkill -f}\ \text{前先确认模式不出现于本命令行}✓$$
$$\qquad \text{合计：第}\ 33\text{–}35\ \text{次同类应验}✓\（\text{全为实现／判断错，非数学错}✓）$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 边界收紧     命中文件数=1    ::  ./C215-JIA-interval-BB-launched-at-0.7640811-and-boundary-tightening.md
技术词 极小内核     命中文件数=1    ::  ./C215-JIA-interval-BB-launched-at-0.7640811-and-boundary-tightening.md
技术词 局部解析闭合 命中文件数=1    ::  ./C215-JIA-interval-BB-launched-at-0.7640811-and-boundary-tightening.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 边界

- 甲的结果**尚未产出**（脚本运行中 ✓）⟹ 本档**不含**任何新下界主张 ✗
- 探针的 66 个 unresolved 的**距离统计定义待固定** ⚠️（引用前须冻结定义 ✓）
- ⚠️ **不**声称 $m_3$ 精确值 ✗；**不**声称 $x_0^*$ 唯一极小 ✗
- **未用** RH；**未改** 他档（本档为边界收紧的唯一出处 ✓）

## §8 下一步

$$\textbf{甲}：\text{等区间运行结束}✓ \Longrightarrow \text{四门核验}✓ \Longrightarrow \text{通过则升级层 1 下界}✓✓$$
$$\textbf{乙}：\text{内核}\ (0,\rho_{\rm lower}]\ \text{的严格处理}✓（\text{甲成功后开}✓）$$
$$\textbf{丙}：\text{全域 cover}✗\ \textbf{仍不开}✓✓（\text{架构已改写，规模已量化}✓）$$
