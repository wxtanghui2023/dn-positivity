已查地图（**先查后写**）：`ls docs/ | grep -iE "template|模板|PROTOCOL"` ⟹ 现有 12 份 `PROTOCOL-*`，**无** minimax 闭合类模板 ✓ ⟹ 本档为首次建立 ✓。

D0: 本档对象 = **PROTOCOL-minimax-closure-template：可复用审计模板（由 T13-A/T13-B2/B2-1 三条闭合线提炼）** —— 关系 = 方法论沉淀
D1: 0
FREEZE-ACK: 本档为方法论模板，不产候选结论（依 §8.1）

---

# 审计模板：minimax 型常数的**闭合流水线**

> **适用对象**：形如 $\displaystyle C=\inf_{x\in\Omega}\max_{1\le k\le K}f_k(x)$ 的极小极大常数，
> 其中 $f_k$ 显式（三角/代数），目标是**精确确定** $C$ 及等号集。
> **不适用**：需要 RH/零点信息的对象（本模板**全程不使用** RH）。

## §0 三种交付等级（先声明，再动手）

$$\textbf{L1 数值}✗：\text{网格/多起点搜索给出}\ C\ \text{的近似值} \Longrightarrow \textbf{不得}✗\ \text{写作「已确定」}$$
$$\textbf{L2 夹逼}✓：[\text{严格下界}L,\ \text{严格上界}U]✓✓\ \text{且}\ U-L\ \text{很小} \Longrightarrow \text{可写「已夹逼到}\ \varepsilon」✓$$
$$\textbf{L3 精确}✓✓✓：U=L\ \text{（上界由合法构造达成，下界由全域覆盖达成）} \Longrightarrow \text{可写}\ C=F(x_0)✓✓$$
$$\Longrightarrow \textbf{纪律}✓：\text{每档必须显式标注等级}✗✓；\text{L1 冒充 L3 是最常见事故}✗✗$$

## §1 A+B+C 架构（闭合的三件套）

$$\boxed{\textbf{A 上界}✓：\text{显式构造一个合法点}\ x_0\Longrightarrow C\le F(x_0)✓\（\text{初等、可手算}✓）}$$
$$\boxed{\textbf{B 局部}✓：x_0\ \text{邻域内}\ F(x)\ge F(x_0)\ ✓\（\textbf{覆盖半径内}✓\ \text{的局部不等式}✓）}$$
$$\boxed{\textbf{C 全域}✓：\Omega\setminus B(x_0,\rho)\ \text{上}\ F\ge F(x_0)+\delta✓\（\delta>0\ \text{显式}✓）}$$
$$\Longrightarrow \text{A}+\text{B}+\text{C} \Longrightarrow C=F(x_0)✓✓ \Longrightarrow \textbf{L3}$$
$$\textbf{常见变体}✓：\text{多极小点}\Longrightarrow\ \text{C 只需排除}\ \bigcup_j B(x_j,\rho_j)✓\（\text{集合等式}\ \Omega=\bigcup B_j\sqcup \mathcal C✓\ \text{须精确}✓）$$

## §2 模板 A：**错误的统一界 → branch-consistent 结构 → 可证明门槛**

$$\textbf{病征}✗：\text{用统一常数}\ C_j=\max(\text{各分支参数})^2\ \text{惩罚所有方向} \Longrightarrow \text{门槛}\ cK-\tfrac{CK^2}5\ \text{怎么选}\ K\ \text{都不够}✗✓$$
$$\textbf{根因}✓：\text{极小点处各分支}\ f_k\ \text{的【活跃性不同}】✓ \Longrightarrow \text{各方向真正生效的分支不同}✓$$
$$\qquad \text{例}✓（\text{尖点}）：F(\theta_j+\varepsilon)-\kappa=s_j\max(-a_j\varepsilon,\ +b_j\varepsilon)+\cdots✓$$
$$\qquad \qquad \varepsilon<0\ \text{侧 binding}\ k=a_j \Longrightarrow \text{曲率}\ \tfrac{a_j^2\kappa}2✓；\varepsilon>0\ \text{侧}\ \tfrac{b_j^2\kappa}2✓✓$$
$$\qquad \qquad \text{统一取}\ \max(a,b)^2 \Longrightarrow \text{小侧高估}\ (b/a)^2\ \text{倍}✓（\text{实例}：j=1\ \text{高估}\sim100\times✗✗）$$
$$\textbf{修法}✓✓：\text{按【方向/符号}】\ \text{分支写不等式}✓：\ F-\kappa\ \ge\ \begin{cases}s_j(-a_j\varepsilon)-C^-_j\varepsilon^2✓\\ s_j(b_j\varepsilon)-C^+_j\varepsilon^2✓\end{cases},\quad C^\pm_j=\tfrac{(a_j\ \text{或}\ b_j)^2\kappa}2✓$$
$$\textbf{验收}✓：\text{门槛}\ \min_j\bigl[c_jK-\tfrac{\text{curv}_j}5K^2\bigr]\ \ge\ \text{need}✓✓\ \text{且}\ K\ \text{与另一侧（Case II）在【同一点}】\ \text{对接}✓✓$$

## §3 模板 B：**数值发现 → 有限分割证书**

$$\textbf{判据}✓✓：\text{若在相邻候选点之间}\ F=\max_k f_k\ \text{为【单一分支}】✓ \Longrightarrow \text{段内极小在端点}✓ \Longrightarrow \text{只需查有限点}✓✓$$
$$\boxed{\textbf{候选点集}=\{\text{全部分支交点}\}\ \cup\ \{\text{约束边界}\}\ \cup\ \{\text{区域端点}\}✓✓}$$
$$\qquad \text{分支交点}✓：f_k=f_{k'}\ \text{的解析解}✓（\text{如}\ \cos(k\varphi)=\cos(k'\varphi)\Longrightarrow\varphi=\tfrac{2\pi m}{k\mp k'}✓，\text{有限}✓）$$
$$\qquad \textbf{约束边界必入集}✗✓：\text{真最小点常在}\ \operatorname{dist}=\varepsilon_0\ \text{处}✓，\text{不是交点}✗✓$$
$$\textbf{闭集纪律}✗✓：\operatorname{dist}\ge\varepsilon_0\ \text{须用} \ge\varepsilon_0-\text{TOL}\ \text{（含边界}✓）\ \textbf{否则边界点被浮点过滤}✗$$
$$\textbf{验收}✓✓：\text{报告四件}：\text{(1) 候选点数}✓；\text{(2) 含切换段数}=0✓；\text{(3) }\min-\text{门槛}✓；\text{(4) 最接近门槛的点的位置类型}✓$$

## §4 陷阱清单（由 5 项 errata 泛化 ✓✓）

| # | 陷阱 | 症状 | 防御 |
|---|---|---|---|
| 1 | **符号配对** | 界给出系统性负值 | 用具体数值**逐项对质**（直接算 vs 分支算）✓ |
| 2 | **最优化顺序** | $\min_{(u,\eta)}$ 与 $\min_u\min_\eta$ 混用 | 写出对象定义式，标清哪个变量内层 ✓ |
| 3 | **单位混用** | 边界点位置错位、分段异常小 | 全程标注单位（$\varphi$ vs $\varphi/\pi$）✓ |
| 4 | **空值短路** | 枚举漏点（如 `y and (...)` 对 $y=0$ 返回 0） | 枚举后**计数校验**＋对称性校验 ✓ |
| 5 | **先提交后修正** | 不平衡花括号入库 | 提交前跑自检（花括号/行数），合格才 commit ✓ |

$$\Longrightarrow \textbf{共性}✓✓：\text{五类都是【实现层}】✓，\textbf{不污染数学}✓；\text{但会制造「伪障碍」（让人误判方向已死}✗）$$

## §5 停止条件（**判断式停止** ✓✓）

$$\textbf{允许}✓：\text{形式化（区间/代数数精确比较、机器检验}✓）｜\text{证明文本压缩}✓$$
$$\textbf{不允许}✗：\text{再推精度}✗｜\text{求更漂亮的常数}✗｜\text{重开已闭合环节}✗$$
$$\boxed{\text{停止的判据}=\text{证明链完整（A+B+C 齐备、等级 L3）}✓\ \textbf{而非}\ \text{算力见底或外部催促}✗}$$

## §6 两条已验证实例（模板出处 ✓✓）

$$\textbf{实例 1}（\text{论文 A 线}）：\text{T13-A}\ m_3\ \text{（C-216…C-220，夹逼到}\ 5\times10^{-14}✓）＋\text{T13-B2}\ g_2(10)=1✓✓（\text{等号集单点}✓）$$
$$\textbf{实例 2}（\text{B2-1 线}）：\forall w\ge5,\ g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}✓✓\ \text{（C-238＋C-250＋C-251/C-253＋C-254 冻结}✓✓）$$
$$\qquad \textbf{两实例共同点}✓：\text{上界初等}✓｜\text{分裂为「近-远」或「井内-井外」}✓｜\text{远区用有限分割证书}✓｜\text{全程无 RH}✓✓$$

## §7 使用流程（五步）

```
  ① 定义对象 C=inf max f_k，写清 Ω、k 范围、单位          → 交付等级目标 L?
  ② A: 显式构造候选点 x_0，手算 F(x_0)                    → 上界 ✓
  ③ B: 在 x_0 邻域写分支一致的不等式，得显式 ρ、margin    → 局部门槛 ✓
  ④ C: 全域 = ∪B(x_j,ρ_j) ⊔ C，C 上用有限分割证书        → 全域覆盖 ✓
  ⑤ 自检: 等级标注 / 单位 / 闭集 / 分支单一切换段数=0      → 才可写 CLOSED
```

## §9 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 分支一致曲率 命中文件数=0    :: 
技术词 有限分割证书 命中文件数=8    :: ./ASSETS-REGISTRY.md ./C254-...md ./C252-...md ...
技术词 判断式停止  命中文件数=2    :: ./C254-...md ./PROTOCOL-minimax-closure-template.md
技术词 三条交付等级 命中文件数=0    ::
```

$$	extbf{① 本档新增}✓：	ext{「分支一致曲率」（0 命中）}✓、	ext{「三条交付等级」（0 命中）}✓$$
$$	extbf{② 档案已有（引用，不列为本档提出）}✓✓：	ext{「有限分割证书」（8 命中}✓，	ext{首见 C-252}✓）\ 	ext{「判断式停止」（2 命中}✓，	ext{首见 C-254}✓）$$
$$\qquad 	ext{本档对其【给出模板化定义}】✓，	ext{但不主张首次命名}✗✓\（	ext{依 MEMORY 硬规矩}✓）$$
$$	extbf{③ 通用词（不计）}✓：	ext{「候选点」/「段内单一分支」/「闭集」}✓$$

## §10 边界（续 §8）

$$\textbf{⑤ 回查后修正}✗✓：\text{原拟称「有限分割证书}】\text{与」判断式停止「为本档新名}✗，\text{回查否决}✗✓（\text{均已在档}✓）$$

## §8 边界

$$\textbf{① 本模板不产数学结论}✓，\text{仅约束【流程与措辞}】✓；\textbf{② 未用 RH}✓；\text{未改他档}✓$$
$$\textbf{③ 模板来源}✓：\text{C-216…C-220（T13-A）}✓、\text{C-193/C-199/C-200（T13-B2）}✓、\text{C-238…C-254（B2-1）}✓$$
$$\textbf{④ 待补}✗：\text{三条线的形式化（区间/机器检验）尚未做}✗（\text{属允许动作}✓，\text{非关闭条件}✓）$$

## §11 ⭐ **Rule T — Translation-before-launch**（2026-09-20 唐先生立规 ✓✓）

> **立规理由**：连续五次「候选命题 → 翻译成档案已有机制 → 查重/判墙」**当场省下整轮投入** ✓✓。
> 这不是一次对象的 CLOSED，而是一条**可迁移的前置筛选器** ✓。

$$\boxed{\text{候选命题}\ \to\ \text{翻译成档案已有机制}\ \to\ \text{查重／判墙}\ \to\ \text{若落入旧机制，}\textbf{禁止重新包装}}\ ✓✓$$

### 五步（开工前必做 ✓）

```
① 对象翻译：写出 arithmetic origin｜作用域｜尺度变量｜目标输出
② 机制翻译：明确它依赖 additive／multiplicative／spectral／local–global／
            explicit-formula 中【哪些已有通道】
③ 档案交叉搜索：逐项映射 V188 等既有分类表（含四通道穷尽表）
④ 最小解析闭合：优先【解析地】判定候选是否恒等化为
            gcd ／ 1_{(Z/qZ)^×} ／ Euler factor ／ finite Fourier support 等旧结构
⑤ 只有出现 genuinely new residue，才允许实验／扩展
```

$$\boxed{\text{硬附加条}✗✓：\textbf{「新对象」不等于「新机制」}\ —— \text{必须证明 }\textbf{mechanism-level novelty}✓✓}$$

### 五次实例（本规则的经验来源 ✓）

| # | 候选 | 翻译结果 | 归宿 | 出处 |
|---|---|---|---|---|
| 1 | N1／N2（非紧致臂／非投射臂） | N1≡唯一缺口的换词；N2≡已登记 UNINSTANTIATED | ✗ 非新方向 | `V264`（09-16） |
| 2 | A1-3（Palojärvi 推广） | 已验证原文那档（`E4`）早有分析 | ✗ 推荐降级 | `V291`（09-16，T10 勘误） |
| 3 | B2-ARITH（四条要求） | 逐条＝独立算术上界／KILL-2／饱和判据／识别接口残余 | ✗ 四墙合取 | `C255`（09-20） |
| 4 | Ramanujan 谱分支＋第一代非线性族 | 恒等化为单位群指示谱；非线性族只依赖 n mod q | ✗ 解析预检闭合 | `C256`（09-20） |
| 5 | B2-2 盲验证 q=13,17,19 ／ Palojärvi m≥2 | A/B 已是定理（`C-159`／`C-191`／`C-192`）／已有判词「buys nothing」 | ✗ 会重推已知 | 09-20 复核 |

### 与既有纪律的关系

$$\textbf{① 与「先查后写」}✓：\text{Rule T 是其【开工前】版本（先查后写管文档，Rule T 管候选}✓）$$
$$\textbf{② 与 }\texttt{C-116}✓：\text{查重结果【不构成否决}】✓，\text{只禁止【重新包装】}✗✓；\text{若候选确有新残量，照开}✓$$
$$\textbf{③ 与 }\texttt{V188}✓：\text{四通道穷尽表＝Rule T 第③步的【第一道分类器}】✓✓$$

### 反向使用（下一步工作包的形状 ✓✓）

$$\boxed{\text{不再是「哪个数学对象有趣」}\ \longrightarrow\ \text{而是「}\texttt{V188}\text{ 六类之外的机制有哪些」}\ \to\ \text{再找承载它的算术对象}}✓✓$$
$$\qquad \text{第一问}✓：\text{是否存在一种自然算术操作，Fourier／谱化之后【既不退化成 }\gcd/\text{Euler，也不等价于已有六类】，且产生【可检测的跨尺度耦合}】？✓$$

## §12 ⭐ FZ-1 修正后的**逻辑层级**（唐先生 2026-09-20 定规 ✓✓，三层）

> **立规理由**：由【近期成功案例】归纳机制优先级，极易把「实践优势」误读成「机制排他性」✓。
> 本层级的目的是让后续恢复枚举时**不能**再犯此误 ✓✓。

### 层 1 · Rule T（保留 ✓，见 §11）

$$\boxed{\text{新对象}\neq\text{新机制}}✓✓\qquad \text{先翻译／查重／最小解析闭合，再决定是否实验}✓$$

### 层 2 · **Rule F — Falsification-before-generalization**（新增 ✓✓）

$$\boxed{\text{观察性归纳}\ \xrightarrow{\text{SURVIVOR-5}}\ \begin{cases}\text{找到 survivor} &\Rightarrow\ \textbf{撤销强读法}✓✓\\ \text{未找到} &\Rightarrow\ \textbf{仅保留弱读法}✓\end{cases}}$$

$$\textbf{禁止}✗✗：\text{从 } N=4\ \text{个成功案例推出「该机制结构上更有能力」}✗$$
$$\textbf{当前唯一允许的表述}✓✓：\boxed{\text{第三族}\ =\ \text{近期实践观察}\ +\ \text{已有对象侧路线的天花板对照}}✓$$
$$\qquad （\text{不得写成「第三族是唯一有效机制」}✗）$$

### 层 3 · **SURVIVOR-5 硬门槛**（✓✓）

$$\boxed{N\wedge NR\wedge A\wedge Q\wedge R}✓✓：\text{N Natural｜NR Non-redundant｜A Arithmetic origin｜Q 新的 quantitative observable｜R 严格 RH-interface}$$
$$\boxed{\text{任何一项失败}\Rightarrow\text{不能作为反例}✗；\qquad\text{五项全过}\Rightarrow\textbf{立即修正当前机制判断}✓✓}$$
$$\textbf{R 的二级标签}✓✓（唐先生 2026-09-20 追加）：\boxed{R_1=\text{RH 导出型}\qquad R_2=\text{RH 障碍敏感型}}\ \text{——}\textbf{不得混用强度}✗✓$$

### 实例链（本层级的来源 ✓）

| 档 | 内容 | 后果 |
|---|---|---|
| `C257` | 机制空间搜索：第三族（量侧／换量） | 提出强读法 |
| `C258` | 反证审计：M3／M4／M5 找到 survivor | 强读法**撤销**，弱读法保留 |
| R 强度 | M3＝R₂（无零区＝障碍敏感）；M4 ≥ R₂（Siegel 零点接口）；M5＝R₁（目前仅 RH 导出） | 避免强度混用 |

## §13 （甲）恢复 `C142` 枚举时的**审查链**（唐先生指定 ✓✓）

$$\boxed{\text{已有 survivor}\ \to\ \text{quantity 是否真正改变}\ \to\ \text{是否越过已知尺度墙}\ \to\ \text{才考虑 RH bridge}}✓✓$$
$$\textbf{禁止}✗✗：\text{survivor}\Rightarrow\text{「优先路线已确认」}✗ —— \text{survivor 只意味着【允许进入候选池】}✓$$
$$\textbf{对 T5 的具体问法}✓✓：\text{能否从现有 de la Vallée Poussin 型正性结构中获得【新的 quantity】}✗，\text{而不是继续优化}\ c/(\log t)^{2/3}(\log\log t)^{1/3}✓$$
$$\qquad \text{若答案只是优化常数或已知同类零区} \Longrightarrow \textbf{仍只是邻近定理资产}✓（\text{优秀 survivor，但非 RH 路线}✓）$$

## §14 ⭐ **Scale Gate**（新增硬门槛，唐先生 2026-09-20 定规 ✓✓）

> **立规理由**：本轮（`C257`→`C258`→`C259`）发现 **"quantity changed ⟹ scale changed" 为假** ✗✗ ——
> 新量常常仍受同一 analytic scale 约束 ✓。若无此门，会重演
> 「发现漂亮新量 → 兴奋开新线 → 最后才发现仍撞原墙」的循环 ✗✓。

$$\boxed{\text{三门（C142 乙类候选必过）}✓✓：\textbf{Rule T}\ \to\ \textbf{SURVIVOR-5}\ \to\ \textbf{Scale Gate}}$$

$$\boxed{\text{Scale Gate}✓✓：\text{若新 quantity 最终仍受既有 }1/\log T\ \text{或已知 value-face／log-degradation 天花板约束}\ \Longrightarrow\ \textbf{不升 RH 主线}✗✓}$$

### 五档判定表（按 novelty 层级 ✓）

| 层级 | 判定 |
|---|---|
| 只有 quantity 改变 | 保留，但不升主线 ✓ |
| quantity ＋ **新尺度** | **重点候选** ✓✓ |
| quantity ＋ 新尺度 ＋ 新 RH-interface | **真正主线候选** ✓✓✓ |
| quantity 改变但仍落旧尺度墙 | **邻近定理资产** ✓ |
| quantity 实际只是旧量重参数化 | **Rule T CLOSED** ✗ |

### 校准器实例：T5（`C259` ✓）

$$\text{T5}\ \Longrightarrow\ \text{QUALIFIED SURVIVOR ／ ADJACENT-THEOREM ASSET}✓（\text{两级成功：survivor}✓\ \text{quantity}✓\ \text{scale}✗\ \text{bridge}✗）$$
$$\textbf{校准器身份}✓✓：\text{T5 证明 }\textbf{SURVIVOR-5}\not\Longrightarrow\textbf{突破}✓✓\ \text{—— 故其后必须再过 Scale Gate}✓$$

### 措辞纪律（`C259` §6 ✓✓）

$$\textbf{禁止}✗✗：\text{「正性产生的所有 quantity 都必然 log-degrading」}（\text{无条件定理形式}）✗$$
$$\textbf{正确}✓✓：\textbf{本次已审计的 quantity classes 均未越过既有尺度墙}✓\（\text{仅限本次审计范围}✓）$$

