已查地图（**先查后写**）：`E4-palojarvi-finitely-many.md` §3/§4/§5/§5b/§7、`E4-ENGINE-3`（衰减松弛·可比性）、`E4-ENGINE-5` §3b（窗口放大线索）、`C-41` §3、`C142`（乙类表）。回查见 §4 ✓

D0: 本档对象 = **S1 两项的状态核验（Palojärvi 已闭合／(RP_M) 活跃）＋ qM 窗口开问题登记** —— 关系 = 状态核验（非新机制）
D1: 0
FREEZE-ACK: 本档即冻结期内的状态核验（依 §8.1）

---

## §0 结论

$$\boxed{\textbf{① S1 第二项（Palojärvi}\ m\ge2\text{）}\textbf{档案已全部闭合}✗✓：\text{扩展＋必要性＋剩余判定三件齐}✓}$$
$$\boxed{\textbf{② S1 第一项（(RP}_M\text{), M}\le11\text{）}\textbf{活跃}✓✓：\text{M}\le4\ \text{已证}✓（\text{M=4 本会话入档}✓）；\textbf{M=5 正在跑}✓}$$
$$\textbf{③ 一个新的具体开问题}✓✓\text{（非审计）：}\texttt{qM}\ \text{窗口放大线索}✓\text{（}\texttt{E4-ENGINE-5}\text{ §3b）}\textbf{尚未证明}✗$$
$$\boxed{\textbf{④ 纪律}✓：\text{本档只做状态核验}✗（\text{不产新审计}✓）；\text{随后立即回到计算}✓}$$

## §1 Palojärvi $m\ge2$：三件已闭合（✓✓）

$$\textbf{(a) 扩展本身}✓✓（\texttt{E4-palojarvi}\ \S5\ \text{，2026-09-12}✓）：\text{至多}\ m\ \text{个例外}\ |\rho/(\rho-\tau)|>1\ \text{时}✓，$$
$$\qquad \text{某零点}\ |\rho/(\rho-\tau)|\ge R\iff|\Re\lambda_F(n,\tau)|\ge(K_{F,1}+K_{F,4})n\log n\ \text{对某}\ n\in[N_m,5mN_m],N_m\mid n✓$$
$$\qquad N_m＝\text{公布}\ N\ \text{把}\ 40(0.5+K_{F,1}+K_{F,4})\ \text{换成}\ 40(K_{F,1}+K_{F,4})+20m✓；\ \textbf{m=1 一致性核验通过}✓✓$$
$$\qquad \text{且}\ \S4\ \text{指出}✓✓：\text{引擎 Lemma 2.2 本就是}\ M\ \text{个复数的陈述} \Longrightarrow \textbf{「至多一个」未保护引擎}✓$$
$$\textbf{(b) 必要性问}✓✓（\text{唐先生本次指定要问的那一问}✓）：\texttt{E4-ENGINE-3}\ \textbf{逐字}：$$
$$\qquad \text{「C-41 §3(甲) 的【模长可比】（}\sum_jD_j>M(M-1)/2\text{）}\textbf{不再是必要假设}✓ —— \text{只要把}\ N\ \text{取大到满足}\ (\star\star)\text{，非最大项自动衰减到可忽略}✓✓\text{。代价}：N_m\ \text{的定义需追加…」}$$
$$\qquad \text{（另见专档：收口 C-41 §3 遗留项，同结论}✓✓）$$
$$\textbf{(c) 剩余判定}✓（\S7\ \text{逐字}✓）：\text{「a genuine, cheap generalization, }\textbf{but it buys nothing unless you can independently bound the number of off-line zeros」}✓$$
$$\qquad \Longrightarrow \text{收益需【独立】界离线零点个数}✓\text{＝已知墙}✗✓$$
$$\Longrightarrow \boxed{\textbf{S1 第二项无可做}✗✓}$$

## §2 $(RP_M)$ 的活跃阶梯（✓）

$$\textbf{已证}✓✓：M=1（\texttt{C-159} 鸽笼）｜M=2（\texttt{C-152}/\texttt{C-153}；\texttt{C-199}/\texttt{C-200}）｜M=3（\texttt{T13-A}；\texttt{C-216}–\texttt{C-219}）｜\textbf{M=4}（\texttt{C-265}✓✓，\text{未决}=0，\text{余量}4.85\times10^{-5}✓）$$
$$\textbf{进行中}✓：M=5（\text{同参数化脚本}✓，\text{目标}\ 1/2✓）\qquad \textbf{待做}✗：M=6..11（\text{同法}✓）$$

## §3 新的具体开问题：$qM$ 窗口放大（✓✓）

$$\texttt{E4-ENGINE-5}\ \S3b\ \textbf{逐字}：\text{「下界随}\ q\ \text{总体上升}（M=2\ \text{由}\ 0.512\ \text{升到}\ 1.175）\Longrightarrow \text{对手的【5 阶错位】确实被更大窗口打破}✓」$$
$$\qquad \text{但}✗：\text{「非严格单调}\ldots\text{尚无证明」}✓；\ \text{代价}✓：\text{E4 的}\ N\ \text{需乘}\ q\ \text{因子，Montgomery 的}\ 5M\ \text{需改成}\ qM\ \text{重证}✓$$
$$\Longrightarrow \textbf{这是一个【具体的证明问题}】✓✓（\text{非审计}✓）：\text{证明}\ K=qM\ (q\ \text{与}\ 5\ \text{互素}，\text{如}\ q=6)\ \text{下的窗口极值下界}✓$$

## §4 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 状态核验档     命中文件数=0 ::
技术词 qM窗口放大的证明问题  命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{两项各 0 命中}⟹\textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{可比性非必要}（\texttt{E4-ENGINE-3}✓）；\text{qM 线索}（\texttt{E4-ENGINE-5}\ \S3b✓）；\text{(RP}_M)\ \text{状态}✓$$

## §5 边界

$$\textbf{① 本档为状态核验}✓，\text{不产新机制}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ 不重跑 M=4}✗，\text{不动 M=5 运行中任务}✓；\ \textbf{④ 不声称 S1 第二项的「收益」可实现}✗（\text{需独立离线零点界}✓）$$
