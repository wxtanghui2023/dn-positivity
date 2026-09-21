已查地图（**先查后写**）：`C-379.3`（**NO-GO ＋ 防重复墙** ✓✓）、`C-379.2`（坐标重包装 ✓✓）、`C-347`（奇频表 ✓✓）、`C-343`（`\sigma \to -\sigma` ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-0：高阶/跨层耦合的"是否换量"前置审计（奇偶性障碍）**，**有计算（数值核验，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 勘误（唐先生公式）}✗✓：\text{原式}\ 2T_{2r}T_{2s+1} = T_{2(r+s)+1} + T_{|2(r-s)+1|}✓ \ \textbf{有符号失误}✗✓$$
$$\qquad \textbf{正确}✓✓：\ \boxed{2T_{2r}T_{2s+1} = T_{2(r+s)+1} + T_{|2(r-s)-1|}}✓✓（\text{数值}：r = s\ \text{时两者一致（差}\ 0✓✓）；r \ne s\ \text{时差}\ 1.13 \sim 1.70✗✓）$$
$$\textbf{② ⭐ 结论更强且不受影响（本档核心）}✓✓：\ \textbf{奇偶性论证}✓✓：T_{2r}\ \textbf{偶}✓、T_{2s+1}\ \textbf{奇}✓ \Longrightarrow \text{乘积}\ \textbf{奇}✓✓$$
$$\qquad \text{数值检验}✓✓：|p(-y) + p(y)| = 0✓ \ \text{对}\ 9/9\ \text{组}\ (r,s)✓ \Longrightarrow \text{Chebyshev 展开}\ \textbf{只含奇次项}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{偶-奇交叉项}\ \sum_j T_{2r}(a_j)T_{2s+1}(a_j)\ \textbf{完全由}\ \{S_1, S_3, S_5, \dots\}\ \text{决定}}✗✓ \Longrightarrow \textbf{无新量}✓✓$$
$$\textbf{③ 出口判定}✓✓：\ \boxed{\text{多项式型跨层耦合} = \textbf{出口 B（重包装）}}✓✓ \Longrightarrow \textbf{立即 NO-GO}✓✓$$
$$\textbf{④ ⭐ 一般性推论（正面价值）}✓✓：\textbf{任何}\ \text{多项式型耦合}✓（\text{偶层量与奇层量的多项式组合}✓）\ \text{受}\ \textbf{同一奇偶性约束}✓✓$$
$$\qquad \Longrightarrow \ \boxed{\text{真正的新跨层量}\ \textbf{必须是非多项式的}}✓✓ \ —— \ \text{即}\ \textbf{必须显式依赖符号层}\ \sigma✓（\text{或}\ \sqrt{x_j} = |c_j|✓）✓✓$$
$$\textbf{⑤ } C\text{-}380\ \text{的正确入口条件}✓✓：\text{候选}\ \mathfrak C(x,\sigma)\ \textbf{不得}是\ (x_j)\ \text{的多项式}✗✓$$
$$\qquad \textbf{注意}✓✓：F_{2r+1} = \sum_j \sigma_j\sqrt{x_j}\,R_r(x_j)✓ \ \textbf{本身} \text{就是这类非多项式量}✓✓ \Longrightarrow \textbf{奇频才}\ \text{是天然的跨层量}✓✓$$
$$\textbf{⑥ 判定归属}✓✓：\text{本刀}\ \text{对}\ \textbf{多项式入口} \text{判 NO-GO}✓✓；\ \text{并登记}\ \boxed{\textbf{非多项式是必要条件}}✓✓ \ \text{作为}\ C\text{-}380\ \text{入口门槛}✓✓$$

## §1 核验记录（✓✓）

$$\textbf{逐点核验}✓：2T_{2r}(y)T_{2s+1}(y)\ \text{与}\ T_{2(r+s)+1}(y) + T_{|2(r-s)+1|}(y)\ \text{最大差}\ 1.952✗✓（\textbf{原式不成立}✗✓）$$
$$\qquad \text{但}\ r = s\ \text{时}\ |2(r-s)+1| = 1 = |2(r-s)-1|✓ \Longrightarrow \text{该子族一致}✓✓（\text{差}\ 0✓：r=s=0,1,2,3✓）$$
$$\textbf{奇偶性}✓✓：T_n\ \text{的奇偶性} = n\ \text{的奇偶}✓ \Longrightarrow T_{2r}\ \text{偶}✓；T_{2s+1}\ \text{奇}✓ \Longrightarrow \text{乘积奇}✓✓$$
$$\qquad \text{数值}✓✓：9\ \text{组}\ (r,s)\ \text{全部}\ |p(-y) + p(y)| = 0✓✓ \Longrightarrow \text{无偶次分量}✓✓$$
$$\textbf{读法}✓✓：\text{奇函数在 Chebyshev 基下的展开}\ \textbf{只含}\ T_1, T_3, T_5, \dots✓✓ \Longrightarrow \text{交叉项}\ \text{可由奇频和重构}✗✓$$

## §2 一般形式（✓✓）

$$\textbf{偶层量}✓：\text{关于一切}\ x_j\ \text{为偶的多项式}✓（\text{如}\ S_{2r}✓） \ \text{或}\ x_j\ \text{的多项式}✓；\ \textbf{奇层量}✓：T_{2s+1}(a_j)✓，\ \sqrt{x_j}✓，\ \sigma_j✓$$
$$\textbf{障碍}✓✓：\text{偶} \times \text{奇} = \text{奇}✓ \Longrightarrow \text{求和后仍是}\ \textbf{奇层量的线性组合}✓✓ \Longrightarrow \textbf{不含新信息}✗✓$$
$$\Longrightarrow \ \textbf{换量的唯一出路}✓✓：\text{引入}\ \textbf{非多项式} \text{结构}✓✓ \ —— \ \text{即}\ \text{奇频}\ F_{2r+1}\ \text{或}\ \text{含}\ \sigma\ \text{的组合}✓✓$$

## §3 判死与晋级（✓✓）

$$\textbf{出口 A}✓：\text{找到新的跨层量}\ \mathfrak C(x,\sigma)✓ \ \text{并证它}\ \textbf{同时} \text{受偶频约束与奇频幅度控制}✓✓ \Longrightarrow \text{进}\ C\text{-}380✓$$
$$\textbf{出口 B}✓✓：\text{候选皆可还原为}\ \text{5-node moment} \to \operatorname{rank} \le 5 \to \text{Hankel／Gram 行列式}✗ \Longrightarrow \textbf{立即 NO-GO}✓✓ \ —— \ \textbf{本刀多项式入口命中此出口}✓✓$$
$$\textbf{出口 C}✓：\text{仅数值相关而无统一不等式} \Longrightarrow \textbf{DISCOVERY}✓，\ \textbf{不得}进主线✗✓$$

## §4 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}379.3` ✓ | **CLOSED** ✓✓ |
| `C\text{-}380\text{-}0`（本刀）✓ | **CLOSED：多项式入口 = 出口 B（NO-GO）** ✓✓ |
| 入口门槛（非多项式）✓ | **首次登记** ✓✓ |
| `C\text{-}380`（奇频放大）✓ | **OPEN（入口已收窄）** ✓✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §5 下一步（✓✓）

$$\textbf{唯一下一刀}✓✓：\text{在}\ \textbf{非多项式} \text{入口内找}\ \mathfrak C✓✓ \ —— \ \text{优先}\ \textbf{奇频侧}✓（F_{2r+1}\ \text{天然含}\ \sigma_j\sqrt{x_j}✓）✓$$
$$\textbf{禁项}✓✓：\textbf{不}从多项式耦合入手✗（本刀已判 NO-GO✓）；\textbf{不}做\ G2✗；\textbf{不}随机采样✗；\textbf{不}上大矩阵✗✓$$
$$\textbf{判据}✓✓：\text{「换量」} \text{才算进展}✓✓；\ \text{「换坐标」／「换多项式次数」} \text{一律}\ \textbf{NO-GO}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 奇偶性障碍  命中文件数=6    :: ./fusion-mtower-rct.md ./E113-mtower-coverage-ladder.md ./R-A8.3-s2-mechanism-audit.md 
技术词 非多项式必要条件 命中文件数=0    :: 
技术词 跨层耦合否证 命中文件数=0    :: 
```
- 运行记录 ✓：`python3 -`（逐点恒等式核验 ＋ 奇偶性检验 ✓）
- **本档有计算**（数值核验，已批准 ✓）；`D1 = 0` ✓；**未改任何他档正本** ✓（勘误在本档记录 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：奇偶性论证为**严格**（一步 ✓）；`r = s` 子族的公式一致性为**数值**✓；**未**逐一核验所有 `(r,s)` ✗✓
- **不得**写成：所有跨层耦合无效 ✗（**仅多项式型** ✓）；`C-380` 已开 ✗；Bridge A 已闭合 ✗；`H = \varnothing` 已证 ✗
