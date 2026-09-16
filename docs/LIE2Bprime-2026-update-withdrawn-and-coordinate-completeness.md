# 猎-2B′ — **2026 Kloosterman 更新的取证结果 ＋ $(r,t)$ 坐标完整性审计**

> 唐先生 2026-09-16 19:49 拍板：开猎-2B′（不开放-1；暂不开"谱隙天花板"强命题）；第一目标＝"把 2026 新结果放进或排除出 $(r,t)$ 坐标系"。
> **取证结果（本档）：该 2026 论文已被作者撤回，所声称的改进不成立。** —— 见 §1。

---

## 1. ⚠️ 取证：2026 论文**已撤回**（arXiv:2601.00292，外部来源，仅作数据）
$$\textbf{页面状态（原文）}：\ \text{"This paper has been withdrawn by Dirk Zeindler"}；\ \text{v2 于 2026-01-05 提交（1 KB，withdrawn）}$$
$$\textbf{撤回说明（原文）}：\text{"We accidentally missed a factor of}\ L^{2}\ \text{in equation (2.53), which turns}\ L^{5}\ \text{into}\ L^{7}.$$
$$\qquad\text{The rest of the argument is still valid, but}\ \boxed{\text{does not lead to an improved bound as claimed}}\text{."}\ (\text{致谢 Alexandru Pascadi 发现该错误})$$
$$\Longrightarrow\ \boxed{\text{所声称的}\ \delta=\tfrac1{46}\ (\theta=\tfrac{12}{23})\ \textbf{不成立}} \Longrightarrow \textbf{该"2026 新推进"不存在}✓$$
$$\textbf{原声称内容（摘要，现已失效）}：\ \text{bilinear Kloosterman fractions}\ \sum\sum\alpha_m\beta_n e(a\bar m/(bn))；\ \text{称改进 DFI 与 Bettin--Chandee；}$$
$$\qquad\text{平衡情形节省}\ 1/12\%\ (\text{对比 DFI 的}\ 1/48)；\ \text{应用称达}\ T^{1/2+\delta},\ \delta=\tfrac1{46}；\ \text{称"extending beyond the previously limiting}\ \theta=\tfrac12\ \text{barrier established by BCR"}$$
$$\textbf{⚠️ 我方的核验教训}：\ \text{这是一例}\ \textbf{"看起来发表级"的新结果实为撤回稿"}；\ \text{本档}\ \textbf{不得} \text{据其更新任何}\ (r,t)\ \text{或}\ \theta\ \text{记录}✓$$

## 2. 对 猎-2A 的两处更正（唐先生指定）
$$\textbf{更正 1（升级为已核实）}：\ (r,t)=\left(\tfrac{23}{48},\tfrac12\right)\Longrightarrow \delta=\tfrac1{190}\ \textbf{恰为 BCR 文中的较弱 DFI 结果}$$
$$\qquad\Longrightarrow\ \text{猎-2A §1 的"待核"}\ \textbf{升级为}\ \textbf{已核实}；\ \text{并非公式错误}✓$$
$$\textbf{更正 2（降级）}：\ \text{猎-2A §5 的"(r,t)}\to(0,0)\ \text{缺失的是谱型／Kuznetsov／谱隙"}\ \textbf{降级为}\ \textbf{OPEN}}$$
$$\qquad\text{理由}：\text{BCR 的猜想（Conjecture 1）}\ \textbf{直接对三线性}\ S_{A,M,N}\ \text{提出}（A\le(NM)^{1/2+\varepsilon}\ \text{范围内平方根型抵消）}，\ \textbf{未} \text{等同为任何具体谱隙猜想}$$
$$\qquad\textbf{纪律（今日已确立）}：\ \boxed{\text{"由某种工具实现"}\ \ne\ \text{"缺口本身等价于该工具的极限"}}✓$$

## 3. ⭐ 由取证得到的两个**存活**的结构性发现
### 发现 1：$(r,t)\to\theta$ 是 **2D → 1D（多对一）**
$$\text{给定}\ \theta，\ \text{解集是一条}\ \textbf{曲线}：\ \text{以}\ \theta=\tfrac{12}{23}\ \text{为例（本档计算，仅作结构演示）}：$$
$$\qquad \frac{\frac12-r}{1+2(r+2t)}=\frac1{46}\iff 23-46r=1+2r+4t\iff \boxed{t=\frac{11-24r}{2}}\ (r\le\tfrac{11}{24})$$
$$\Longrightarrow\ \boxed{\theta\ \textbf{单独不能决定}\ (r,t)} \Longrightarrow \text{判定"是否属于}\ (r,t)\ \text{族"}\ \textbf{必须在估计层面} \text{做，}\ \textbf{不能在}\ \theta\ \text{数值层} \text{做}✓$$
### 发现 2：**形式类型**（bilinear vs trilinear）可能是分期点
$$\text{BCR 的}\ (r,t)\ \text{坐标服务于}\ \textbf{三线性}\ S_{A,M,N}=\sum_a\sum_{(m,n)}\nu_a\alpha_m\beta_n e(a\bar m/n)$$
$$\qquad\text{（已撤回的）2026 稿处理的是}\ \textbf{bilinear}\ \sum\sum\alpha_m\beta_n e(a\bar m/(bn)) \Longrightarrow \textbf{不同的形式类型}$$
$$\Longrightarrow\ \text{若任一（已发表且未撤回的）bilinear 结果}\ \textbf{不能} \text{无损归入三线性族} \Longrightarrow \boxed{(r,t)\ \text{是 BCR 架构内部坐标，而非墙 A 的完备坐标}}✓$$
$$\qquad\textbf{⚠️ 但须诚实标注}：\ \text{该测试的}\ \textbf{测试用例已撤回} \Longrightarrow \text{发现 2}\ \textbf{仍是未检验假设}（\text{OPEN}），\ \text{不得写成结论}✓$$

## 4. 当前墙 A 的真实前沿（据现有未撤回资料）
$$\text{最新}\ \textbf{已发表} \text{点（唐先生引文）}：\ (r,t)=\left(\tfrac9{20},\tfrac7{20}\right)\Longrightarrow \delta=\tfrac1{66}\Longrightarrow \theta<\tfrac{17}{33}\approx0.5152$$
$$\text{DFI 点}：\left(\tfrac{23}{48},\tfrac12\right)\Longrightarrow \delta=\tfrac1{190}\Longrightarrow \theta<\tfrac12+\tfrac1{190}\approx0.5053$$
$$\Longrightarrow\ \boxed{\text{2026 年未产生（未撤回的）新推进；前沿未移动}} \Longrightarrow \text{墙 A}\ \textbf{仍 ALIVE}，\ \text{但}\ \textbf{无 2026 增量}✓$$

## 5. ⭐ 本档最重要的方法学教训（值得登记）
$$\text{本档是一次}\ \textbf{活体检查}：\text{"2026 新攻击结果"}\ \text{在取证后}\ \textbf{实为撤回稿}，\ \text{且撤回原因}\ \textbf{恰为技术错误（漏因子）}$$
$$\Longrightarrow\ \text{验证了今日长期坚持的纪律}\ \textbf{确有实效}：$$
$$\qquad\text{(i) 文献}\ \textbf{未逐行核验} \text{的标注}\ \textbf{不可省}；\quad\text{(ii) "看起来发表级"}\ \ne\ \text{"已发表"}；$$
$$\qquad\text{(iii) 任何}\ \textbf{据文献更新坐标} \text{的动作}\ \textbf{必须先取证原页}✓$$

## 6. 判定与下一步
$$\boxed{\text{猎-2B′ 第一目标}\ \textbf{已达成}：\ \text{2026 结果}\ \textbf{被排除}（\text{理由＝已撤回，}\textbf{非} \text{坐标不匹配）}}$$
$$\qquad\textbf{注意}：\ \text{这}\ \textbf{不是} \text{发现 2 的证据（因测试用例失效）} \Longrightarrow \text{发现 2}\ \textbf{仍需} \text{新的（未撤回的）测试用例}✓$$
$$\textbf{下一步（三个候选，待唐先生裁定）}：$$
$$\qquad\text{(N1)}\ \text{找}\ \textbf{已发表且未撤回} \text{的非三线性 Kloosterman 结果，检验发现 2}；$$
$$\qquad\text{(N2)}\ \text{直接做}\ \textbf{B2（}(r,t)\ \text{是否完备坐标）} \text{的结构分析}（\text{不依赖某个具体新结果）}；$$
$$\qquad\text{(N3)}\ \text{回头做}\ (K)\ \text{侧天花板审计}（\text{现有未撤回前沿}\ \tfrac{17}{33}\ \text{的上限在哪）}✓$$

## 7. 边界（N1/N2 严守）
$$\text{① 本档取证为}\ \textbf{arXiv 原页（外部来源，仅作数据）}，}\textbf{撤回事实与说明逐字引用}✓；$$
$$\text{② §3 发现 1 为本档计算}（\text{多对一}）；\ \text{发现 2 为}\ \textbf{[结构判定]} \text{且}\ \textbf{未检验}；$$
$$\text{③ }\textbf{未用 RH}；零数值（\text{仅分数演算）}；\ \text{未跑 Lean}✓$$

## 8. 净产出
$$\text{(i) ⚠️ 取证推翻前提：2026 稿}\ \textbf{已撤回}，\ \delta=\tfrac1{46}\ \textbf{不成立}（\text{撤回说明逐字引用}）✓$$
$$\text{(ii) 猎-2A 两处更正：DFI 项}\ \textbf{升级为已核实}；\ \text{§5 谱隙判断}\ \textbf{降级为 OPEN}；$$
$$\text{(iii) ⭐ 存活发现 1：}\ (r,t)\to\theta\ \text{为}\ \textbf{2D}\to\text{1D 多对一} \Longrightarrow \text{族成员判定须在估计层}；$$
$$\text{(iv) 存活发现 2（未检验）：形式类型（bilinear vs trilinear）可能分期——}\textbf{测试用例失效，仍 OPEN}；$$
$$\text{(v) 前沿未移动（}\tfrac{17}{33}\ \text{仍为最新已发表点）＋方法学教训（活体检查的价值）。}$$
