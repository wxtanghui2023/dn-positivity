已查地图（**先查后写**）：`C122`（β 通道非典范化·三要求；A/B 链条逐步审计）、`C263`（multiplicity-only GAP）、`C262`（占比结构性封口）、`C258`（M4 survivor＝类数公式）、`V237-D`（char p 的谱来自几何）、`V254`（非典范／尚未发明的来源）、`C107`（FZ-2 吸收目标）、`V188`（四通道）、`PROTOCOL` §12–§14。回查见 §6 ✓

D0: 本档对象 = **β-sensitive arithmetic channel census（新对象生成审计，三门）** —— 关系 = 新清单的入口审计（不产候选结论）
D1: 0
FREEZE-ACK: 本档即冻结期内的对象生成审计（依 §8.1）

---

## §0 结论

$$\boxed{\textbf{① 三门}✓✓（\text{唐先生给定}✓）：\text{G1 }\beta\ \text{原生}\mid\text{G2 arithmetic realization}\mid\text{G3 新 RH interface（非端点恒等）}}$$
$$\boxed{\textbf{② 与 `C-122` 的对应}✓✓：\text{G1／G2／G3 ＝ (i)／(ii)／(iii) ＋ `C263` 新增的【非重数】条件}✓✓}$$
$$\boxed{\textbf{③ 普查结果}✗✓：\text{枚举 6 类候选，}\textbf{通过三门者＝0}✗✓（\text{有限普查，非不可能性}✗）}$$
$$\boxed{\textbf{④ 结构判据}✓✓（\text{本档产出}✓）：\beta\ \text{必须以}\boxed{\text{位置／权重型}}\ \text{进入，}\textbf{不能以【计数型】进入}✗✓}$$
$$\boxed{\textbf{⑤ 纪律}✓✓：\textbf{先搜 β-sensitive arithmetic object，后问 RH}✓✓（\text{不得 RH}\to\text{已知判据}\to\text{重新包装}✗）}$$

## §1 三门 ＋ 与 C-122 的精确对应（✓✓）

$$\textbf{G1（}\beta\ \text{原生变量}）✓：\text{即使完全不知}\ \gamma，\text{该对象仍有独立算术定义，且}\ \beta\ \text{的出现【不是「零点重数」}】✓$$
$$\qquad \leftrightarrow\ \texttt{C-122}\ \text{(i)}✓（\text{由算术数据定义，不用零点}✓）\ +\ \texttt{C-263}\ \text{的【非重数】条件}✓✓\（\text{新增}✓）$$
$$\textbf{G2（arithmetic realization）}✓：\text{须存在}\ \mathcal A_{\rm arith}\overset{\Phi}{\to}\mathcal O(\beta)✓，\ \Phi\ \text{来自素数／Euler 因子／局部域／Hecke-Frobenius／idele-类群}✓$$
$$\qquad \leftrightarrow\ \texttt{C-122}\ \text{(ii)}✓（\text{横向奇点集＝}\{\operatorname{Re}\rho\}✓）$$
$$\textbf{G3（新 RH interface）}✓：\text{不得只得【端点恒等}】✓（\text{如}\ RH\iff N(\sigma,T)=0\ \text{或}\ RH\iff\kappa_\infty=1✗）$$
$$\qquad \text{须}\ \boxed{\text{arithmetic structure}\to\text{new constraint on}\ \beta\to\beta=\tfrac12}✓；\qquad \leftrightarrow\ \texttt{C-122}\ \text{(iii)}\ ＋\text{非端点要求}✓✓$$

## §2 普查表（✓✓）

| # | 候选类 | G1 $\beta$ 原生 | G2 算式化 | G3 新桥 | 归宿 |
|---|---|---|---|---|---|
| 1 | **Euler 乘性 Dirichlet 级数**（`C-122` A1–A4） | ✓ ✓（奇点＝零点**位置**，非重数 ✓） | ✓（$\zeta$／$L$） | ✗ 端点（$\sigma_c\le\tfrac12\iff$RH；无条件阈值 $=1$） | ✗ 缺口＝(iii) |
| 2 | **显式公式型** | ✗（用零点 ✓ 违反 G1） | ✗ | ✓ | ✗ 缺口＝G1 |
| 3 | **类数／Siegel 零点**（`C258` M4） | ✓（$h(D)$ 算术；$\beta_1$ 是**位置** ✓） | ✓✓（类数公式） | ✗（GRH 型；Brauer–Siegel 路线已封 `V139`/`V140`） | ✗ 缺口＝G3 |
| 4 | **char $p$ Frobenius 权重** | ✓✓（权重＝$\lvert\text{特征值}\rvert$，**非重数** ✓） | ✓✓（Frobenius／上同调） | ✗（无 char 0 移植：`V237-D` 谱来自**几何** ✓） | ✗ 缺口＝G3 |
| 5 | **零点统计类**（zero-density／mollifier／moment／rank–trace） | ✗（$\beta$ 只经**重数／计数** ✗✓） | ✓ | ✗ | ✗ **已冻结**（`C262`/`C263`） |
| 6 | **换核／换泛函型**（explicit-formula-only） | ✗ | ✓ | ✗ | ✗ **已冻结** |

$$\Longrightarrow \boxed{\text{通过三门者＝0}✗✓；\text{6 类中 4 类与档案已封线重合}✓（\text{正是「先查后判」的作用}✓）}$$

## §3 结构判据（本档产出 ✓✓）

$$\boxed{\beta\ \text{进入方式二分}✓✓：\text{位置／权重型（location／weight-type）}\ \textbf{vs}\ \text{计数型（counting／multiplicity-type）}}$$
$$\qquad \textbf{位置／权重型}✓\text{（类 1、3、4）：}\beta\ \text{以【零点的实部本身】或【算术特征值的模】的方式进入}✓ \Longrightarrow \textbf{过 G1}✓$$
$$\qquad \textbf{计数型}✗（\text{类 5、6}）：\beta\ \text{只经重数／退化计数}✗ \Longrightarrow \textbf{过不了 G1}✗✓（\text{＝} `C262`/`C263`\ \text{的封口}✓）$$
$$\Longrightarrow \textbf{所以 G1 的真实内容}✓✓：\text{筛掉「所有靠数零点来感知}\ \beta\ \text{」的对象}✗✓ \text{—— 与}\ \texttt{V188}\ \text{的线性通道饱和}✓\ \text{同址}✓$$

## §4 G3 的普遍困难（端点结构 ✓✓）

$$\text{注意到}✓✓：\text{三个过 G1 的类（1、3、4）}\textbf{都在 G3 失败}✗，\text{且失败方式【同型}】✓：$$
$$\qquad \text{类 1}✓：\sigma_c\le\tfrac12\iff RH；\qquad \text{类 3}✓：\text{Siegel 零点不存在}\iff\text{GRH 型}；\qquad \text{类 4}✓：\text{char}\ p\ \text{的类比成功但【缺 char 0 几何}】✓$$
$$\Longrightarrow \boxed{\text{规律}✓✓：\text{凡}\ \beta\ \text{原生通道，其自然接口【都是端点恒等}】✗\ \text{或【缺 char 0 载体}】✗}$$
$$\qquad \Longrightarrow \text{这正是}\ \texttt{C-122}\ \text{缺口（(i)}\wedge\text{(ii)}\wedge\text{(iii)}）\ \textbf{在对象层的重现}✓✓$$

## §5 本轮固定的纪律（✓✓）

$$\boxed{\textbf{先搜 β-sensitive arithmetic object，后问 RH}✓✓}\qquad\text{而非}\qquad \text{RH}\to\text{已知判据}\to\text{重新包装}✗$$
$$\textbf{已冻结（不得作为候选}）✗：\text{zero-density}\mid\text{mollifier}\mid\text{moment}\mid\text{rank–trace}\mid\text{纯零点计数}\mid\text{explicit-formula-only}\mid\text{换核／换泛函}✓$$
$$\textbf{新前置筛选}✓（\text{承 `C263` §7}✓）：\text{仍属上述族且未引入新 β-sensitive channel}\Rightarrow\textbf{直接筛掉}✗$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 原生变量门      命中文件数=0 ::
技术词 算式化门        命中文件数=0 ::
技术词 新桥门          命中文件数=0 ::
技术词 位置型与计数型  命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{四项各 0 命中}⟹\textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{「非典范化三要求」（}\texttt{C-122}✓\text{）}；\text{「重数／计数」（}\texttt{C263}✓\text{）}；\text{「非典范／尚未发明的来源」（}\texttt{V254}✓\text{）}$$

## §7 边界

$$\textbf{① 本档为普查与判据}✓，\text{不产候选结论}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ 这是【有限普查}】✗✓（\text{枚举 6 类}✓），\textbf{不是不可能性定理}✗✓（\text{遵 }C-116✓）；\text{不排除第 7 类}✓$$
$$\textbf{④ }C263\ \text{的 GAP 保持原样}✓（\text{不补洞}✓，\text{遵唐先生指定}✓）—— \text{它以「证明我们尚未拥有}\ \beta\text{-only-multiplicity 一般定理」的身份，支撑本轮「必须从定义真正的}\ \beta\text{-sensitive 对象开始」}✓✓$$
