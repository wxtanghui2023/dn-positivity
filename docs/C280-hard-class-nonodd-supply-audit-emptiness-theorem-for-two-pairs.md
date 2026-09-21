已查地图（**先查后写**）：`C-279`（原点窗口定理 ＋ 无害化分离 ＋ **困难类 H 定义**）、`C-278`（二倍族统一供给 DEAD ＋ §8 两条钉死）、`C-277`（Type A/B ＋ 阈值引理）、`C-276`（零点刻画 δ=0 ⟺ M_p∩M_q≠∅ ＋ §9 勘误）、`C-275`（组合空洞 ＋ 危险集）、`C-272`（粗箱积压）、`C-181`（u≤5，GAP-A）。回查见 §8 ✓

D0: 本档对象 = **C-280：困难类 H_≤ 的非奇比率供给审计（四对候选 · 几何零耦合集 ∩ H_≤）**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结期内的纯数学审计（依 §8.1）

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{① 口径修正（采纳唐先生}✓✓）：严格失效区}\ H_<:=\{\max_kq_k<\tfrac12\}\ \text{与边界}\ H_\le:=\{\max_kq_k\le\tfrac12\}\ \textbf{必须分开}✗✓$$
$$\qquad \text{真正未证区按}\ H_\le\ \text{考虑}✓；\textbf{逐箱正性}\ne\textbf{统一正下界}✗✓（\text{沿}\ q_k\to\tfrac12\ \text{边界，下确界可趋于 0}✓）$$
$$\boxed{\textbf{② 域内基本简化}✓✓：\text{在}\ [0,\pi]\ \text{上}\ \cos\theta\ \textbf{严格递减}✓ \Longrightarrow M_1(I_j)=\{\beta_j\}\ \textbf{恒成立}✓ \Longrightarrow q_1=\sum_j\cos\beta_j✓}$$
$$\boxed{\textbf{③ Type B(1,2) 的}\textbf{充要条件}✓✓：\beta_j\le\tfrac{\pi}{2}✓（\text{双向}✓）}$$
$$\boxed{\textbf{④ Type B(1,4)（在}\ \beta_j\le\tfrac{\pi}{2}\ \text{下）}\Longrightarrow \beta_j\le\tfrac{\pi}{4}✓（\text{必要性}✓）}$$
$$\boxed{\textbf{⑤ ⭐ 主定理}✓✓：H_\le\ \cap\ Z_{1,2}\ \cap\ Z_{1,4}\ =\ \varnothing✓ \Longrightarrow \textbf{出口＝空}✓✓（\text{且}\ \textbf{只用两对}✓）}$$

$$\textbf{纪律}✓：\text{零计算}✗；\text{未读 pending}✗；\text{未选权重／}\lambda✗；\text{零五维箱实验}✗；\text{不碰 GAP-A}✗$$

## §1 口径修正与反向判死（✓✓）

$$\textbf{口径}✓✓：H_<\ \text{开集}✓；H_\le\ \text{含边界}q_k=\tfrac12✓。\text{若某}\ k\ \text{有}\ q_k=\tfrac12，\text{严格证书}\ q_k>\tfrac12\ \textbf{未闭合}✗ \Longrightarrow \text{未证区}\supseteq H_\le✓$$
$$\textbf{陷阱}✗✓：\text{若只在}\ H_<\ \text{上逐箱证}\ \delta>0，\text{下确界可沿边界}\to0✗ \Longrightarrow \boxed{\text{逐箱正性}\ne\text{统一正下界}}✓✓$$
$$\textbf{反向判死}✓✓：\text{欲杀 C，}\textbf{不必} \text{找到}\ \Delta\equiv0\ \text{的箱}✗；\text{只需}\ \exists B_n\in H_\le:\ \Delta_{\mathcal P}(B_n)\to0✓ \Longrightarrow \textbf{该族不能升主线}✗✓$$

## §2 域内基本简化（✓✓）

$$\textbf{事实}✓：\theta_j\in[0,\pi]\ \text{且}\ \cos\ \text{在其上严格递减}✓ \Longrightarrow \min_{I_j}\cos(\theta_j)=\cos\beta_j✓ \Longrightarrow \boxed{q_1=\sum_{j=1}^{5}\cos\beta_j}✓$$
$$\Longrightarrow \textbf{推论}✓✓：B\in H_\le\Longrightarrow \sum_j\cos\beta_j\le\tfrac12 \Longrightarrow \text{多数}\ \beta_j\ \text{须}\ \textbf{接近}\ \pi✓（\text{即坐标区间须靠近}\ \pi✓）$$

## §3 Type B(1,2) 的充要条件（**双向**✓✓）

$$\textbf{命题}✓✓：\text{对}\ I_j=[\alpha_j,\beta_j]\subset[0,\pi]：\ M_1(I_j)\cap M_2(I_j)\ne\varnothing\iff \beta_j\le\tfrac{\pi}{2}$$
$$\textbf{必要性}✓：M_1=\{\beta_j\}✓ \Longrightarrow \beta_j\in M_2✓ \Longrightarrow \cos(2\beta_j)\le\cos(2\theta)\ \forall\theta\in I_j✓$$
$$\qquad \text{若}\ \beta_j>\tfrac{\pi}{2}：\text{① }2\alpha_j<\pi<2\beta_j\Longrightarrow \min=-1\Longrightarrow \cos(2\beta_j)=-1\Longrightarrow 2\beta_j=\pi\ \text{矛盾}✗；\text{② }2\alpha_j\ge\pi\Longrightarrow \text{区间}\subset[\pi,2\beta_j]\subset[\pi,2\pi]✓\ \text{上}\cos\ \textbf{递增}✓ \Longrightarrow \cos(2\beta_j)>\cos(2\alpha_j)✗\ \text{矛盾}✓$$
$$\textbf{充分性}✓：\beta_j\le\tfrac{\pi}{2}\Longrightarrow 2\theta\ \text{在}\ [2\alpha_j,2\beta_j]\subset[0,\pi]\ \text{上递减}✓ \Longrightarrow \min=\cos(2\beta_j)\Longrightarrow \beta_j\in M_2✓ \blacksquare$$

$$\Longrightarrow \textbf{箱级}✓：Z_{1,2}=\Big\{B:\ \beta_j\le\tfrac{\pi}{2}\ \forall j\Big\}✓（\text{因}\ \delta_B=\sum_j\delta_{I_j}✓，\text{零}\iff\text{每坐标零}✓）$$

## §4 Type B(1,4) 在 $\beta\le\tfrac{\pi}{2}$ 下的必要性（✓✓）

$$\textbf{命题}✓✓：\text{若}\ \beta_j\le\tfrac{\pi}{2}\ \text{且}\ \beta_j\in M_4(I_j)，\text{则}\ \beta_j\le\tfrac{\pi}{4}$$
$$\textbf{证明}✓：\beta_j\in M_4\Longrightarrow\cos(4\beta_j)\le\cos(4\theta)\ \forall\theta\in I_j✓。\text{若}\ 4\beta_j>\pi：$$
$$\qquad \text{① }4\alpha_j<\pi<4\beta_j\Longrightarrow \min=-1\Longrightarrow 4\beta_j=\pi\ \text{矛盾}✗；\qquad \text{② }4\alpha_j\ge\pi\Longrightarrow [4\alpha_j,4\beta_j]\subset[\pi,2\pi]\ \text{上}\cos\ \textbf{递增}✓ \Longrightarrow \cos(4\beta_j)>\cos(4\alpha_j)✗$$
$$\qquad \Longrightarrow \text{唯一可行为}\ 4\beta_j\le\pi\iff \boxed{\beta_j\le\tfrac{\pi}{4}}✓ \blacksquare$$

## §5 主定理：$H_\le\cap Z_{1,2}\cap Z_{1,4}=\varnothing$（✓✓✓）

$$\textbf{假设}✓：B\in Z_{1,2}\cap Z_{1,4} \Longrightarrow \text{每坐标既 Type B(1,2) 又 Type B(1,4)}✓$$
$$\qquad \mathop{\Longrightarrow}^{\S3,\S4} \beta_j\le\tfrac{\pi}{4}\ \ \forall j✓ \Longrightarrow q_1=\sum_j\cos\beta_j\ \ge\ 5\cos\tfrac{\pi}{4}=5\cdot\tfrac{\sqrt2}{2}\approx\mathbf{3.54}\ \gg\ \tfrac12✓$$
$$\qquad \text{而}\ B\in H_\le\Longrightarrow \max_kq_k\le\tfrac12\ \text{尤其}\ q_1\le\tfrac12✗ \Longrightarrow \textbf{矛盾}✓ \Longrightarrow \boxed{H_\le\cap Z_{1,2}\cap Z_{1,4}=\varnothing}✓✓ \blacksquare$$

$$\textbf{含义}✓✓：\forall B\in H_\le：\textbf{至少}\ (1,2),(1,4)\ \textbf{中之一} \text{有}\ \delta_B>0✓ \Longrightarrow \textbf{出口＝空}✓✓$$
$$\qquad \textbf{附带}✓✓：\text{结论}\textbf{不需要}\ \text{第三、第四对}（2,3),(2,5)✗ \Longrightarrow \text{只靠低频偶倍两对即可}✓（\text{更省}✓）$$
$$\qquad \textbf{统一余量}✓：\text{空性来自}\ q_1\ge3.54\ \text{这一}\ \textbf{一致界}✓，\text{但}\ \delta\ \text{的}\textbf{大小}\ \text{无一致下界}✗ \Longrightarrow \textbf{C 未达}✗✓$$

## §6 出口判定（按预注册表 ✓✓）

| 结果 | 本刀 |
|---|---|
| 交集非空 ⟹ DEAD | ✗ **未发生** ✓ |
| **空，但无统一余量 ⟹ B／局部资产** | ✅ **命中** ✓✓ |
| 空且推出统一 $\Delta\ge c_*>0$ ⟹ C／升级候选 | ⬜ **未达** ✗（$\delta$ 大小无一致下界 ✓）|

$$\boxed{\textbf{判定}✓：\textbf{B 级}✓（每箱必有某 pair 真耦合）——\textbf{但 B 不是成功}✗，\textbf{C 才是}✓✓}$$
$$\textbf{下一步}✓：\text{C 级需证}\ \inf_{B\in H_\le}\Delta_{\mathcal P}(B)>0✓，\text{或按}\ \S1\ \text{用序列}\ B_n\ \text{反向判死}✓$$

## §7 边界

$$\textbf{① 零计算}✗（\text{无任何运行}✓）；\text{未读 pending}✓；\text{未选权重}✓；\text{未碰五维箱实验}✗$$
$$\textbf{② 结论范围}✓：\text{只判}\ (1,2),(1,4)\ \text{两对与}\ H_\le\ \text{的交集}✗；\text{不判整体耦合机制}✗；\text{不判 C}✗$$
$$\textbf{③ 域限制}✓：\text{全部结论在}\ [0,\pi]\ \text{内（}\cos\ \text{严格递减}✓）\ \text{成立}✓；\text{若换域须重审}✓$$
$$\textbf{④ 未用}\ RH✓；\text{未改他档正本}✓；\text{未动}\ v4✓；\texttt{C-181}\ \text{的}\ u\le5\ \text{仍为 GAP-A}✗✓$$

## §8 【技术词回查】输出（**先跑后写**✓）

```
技术词 域内递减化     命中文件数=0    ::
技术词 端点最大化障碍 命中文件数=0    ::
技术词 硬类空交定理   命中文件数=0    ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中} \Longrightarrow \textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{零点刻画}✓（\texttt{C-276}\ \S1✓）；\text{Type B}✓（\texttt{C-277}✓）；\text{原点窗口／困难类}✓（\texttt{C-279}✓）；\text{组合空洞}✓（\texttt{C-275}✓）$$
