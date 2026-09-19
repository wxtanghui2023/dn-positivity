已查地图（**先查后写**）：`C-131`（非聚合 step 2 三型 ＋ 唯一实例 F3＝支撑大小刚性）、`C-130`（S1/S2/S3 三分类）、`C-125`（sumset 饱和／R1/R2 无上界）、`C-122`／`C-123`（Toeplitz PSD＝K2 repackaging；mixture essentiality）、`V188 §2`（支撑性质非线性；线性泛函只看见位置加权和）、`V193 §⑤`（残余形状）、`CLOSED-ROUTES-MAP:1092`（§4：设计 1／2 均 $\mathcal X_N=\prod_{p\le N}\mathcal X_{N,p}$ 等号成立 ⟹ **立即 DEAD**，即 **KILL-2＝素数直积因子化**）＋`:1095`（三难：有限记忆⟹周期⟹KILL-1／无限记忆⟹框架空洞／精确局部⟹表示刚性）＋`:1097`（判词 V205-A：DEAD）。关键词回查：`窗口隐形`=0、`幂等测度`=0（**新**）；`完整周期`=4（**沿用**，见 `C87`／`PAPERA-block-method` 等）。
**本档任务（唐先生 2026-09-19 11:25「继续攻，看看这个定理能不能攻击」）**：**攻 F3。**
**结论（先行）**：$$\textbf{(一)}\ \text{F3 作为\ \textbf{独立定理}\ \textbf{不成立}}\ \Longrightarrow\ \textbf{显式反例（窗口隐形测度）}✓✓$$
$$\qquad \text{窗口幅频偏差}\ \lesssim5\times10^{-12}\ \text{（浮点噪声）},\ \text{而秩}\ R:\ 47\to256\ ✓✓$$
$$\textbf{(二)}\ \text{反例被}\ \text{`B2-1`}\ \text{的}\ \textbf{整数质量约束}\ \textbf{堵死}（\text{整数均匀测度质量}＝256\ \Longrightarrow\ \text{加它破坏}\ \sum m＝256）✓✓$$
$$\textbf{(三)}\ ⭐\ \text{反例引擎}＝\textbf{完整周期／幂等测度}＝\text{档案已有的}\ \textbf{KILL-2（素数直积）}✓✓$$
$$\textbf{(四)}\ \text{攻击后剩存的真问题}＝\textbf{非加性形变}（\text{固定质量下改变秩}）＝\text{`B2-1`}\ \text{mixture essentiality／pairwise geometry}✓✓$$
$$\textbf{(五)}\ \text{失败发生在}\ \textbf{陈述层（假设缺失）}，\textbf{不是证明层}✓✓$$

FREEZE-ACK: 本档即冻结期内的定理攻击（构造反例）与陈述修正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **F3 的显式反例（窗口隐形测度）＋ 修正后真靶子 ＋ 反例引擎＝KILL-2 的跨线识别** —— 关系 = 攻击与修正，非新机制
D1: 0

# C-132 · **攻 F3：显式反例 ＋ 修正后的真靶子（引擎＝KILL-2 同一物）**

> **唐先生 2026-09-19 11:25**：**「继续攻，看看这个定理能不能攻击」** ✓

---

## §1 F3 的精确陈述（独立于 ζ）

$$F3：\text{设}\ \mu=\sum_i m_i\delta_{x_i}\ (m_i>0,\ x_i\in\mathbb Z/N)，\text{窗口数据}\ \{|\hat\mu(j)|^2\}_{j=1}^{W}\ \text{给定}；$$
$$\qquad \text{则}\ \forall\ \text{匹配该数据的正测度}：\ \#\operatorname{supp}\mu\ \le\ B(W)\ \ (\text{或秩}\ R\le B(W))✓$$

## §2 ⭐ 反例：**窗口隐形测度**（显式 ＋ 数值）

$$\text{取}\ u:=\frac1N\sum_{x\in\mathbb Z/N}\delta_x\ (\text{ℤ/N 上均匀测度})\ \Longrightarrow\ \hat u(j)=\begin{cases}1,&j\equiv0\ (N)\\0,&\text{else}\end{cases}✓✓$$
$$\qquad \Longrightarrow\ \textbf{窗口}\ 1\le j\le W<N\ \text{内}\ \hat u(j)\equiv0\ \text{（实测}\ \max_{1\le j\le255}|\hat u(j)|=9\times10^{-15}）✓✓$$
$$\text{故对任意}\ \mu\ \text{与任意}\ t>0：\ \mu_t:=\mu+t\,u\ \Longrightarrow\ \widehat{\mu_t}(j)=\hat\mu(j)\ (1\le j\le W)\ \textbf{幅频完全不变}✓✓$$

**数值（`W=255`，`N=256`）**：
$$\text{稀疏}\ \mu_0：8\ \text{个原子}，\sum m=100，R(\mu_0*\tilde\mu_0)=47✓$$
$$\begin{array}{c|c|c|c}
t & \text{窗口幅频最大偏差} & \text{总质量} & \text{秩}\ R\\\hline
0.3 & 4.55\times10^{-12} & 100.30 & \mathbf{256}\\
1.0 & 4.55\times10^{-12} & 101.00 & \mathbf{256}\\
5.0 & 6.37\times10^{-12} & 105.00 & \mathbf{256}\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{同一窗口幅频下，秩可任意增大至满群（47}\to256）\ \Longrightarrow\ \textbf{F3 无约束版 FALSE}}✓✓$$

## §3 为什么 `B2-1` 不塌：**整数质量约束**

$$\text{`B2-1`}\ \text{的族}：m_i\in\{1,2\},\ \sum_i m_i=256\ \text{（}\textbf{整数质量}＋\textbf{总量固定}）✓$$
$$\qquad \text{整数均匀测度}\ u_{\text{int}}:=\sum_{x}\delta_x\ \text{的质量}＝256\ \Longrightarrow\ \text{加它}\ \textbf{破坏}\ \sum m＝256\ ✗✓$$
$$\qquad \Longrightarrow\ \textbf{加法逃逸被封};\ \text{且此约束下}\ \#\operatorname{supp}\le\sum m=256\ \text{（平凡上界）}✓✓$$
$$\Longrightarrow\ \boxed{\textbf{整数性＋固定总量＝F3 成立所必需的额外输入}（\text{缺失则反例立即生效}）}✓✓$$

## §4 ⭐⭐ 反例引擎的识别（**跨线同一物**）

$$\text{反例的引擎}＝\text{"}\textbf{完整周期测度／幂等测度}"（u*u=u，\hat u\ \text{在窗口内恒 0}）✓$$
$$\qquad \text{对照}\ \text{`CLOSED-ROUTES-MAP:1092`}\ \text{的}\ \textbf{KILL-2}：\text{运算结构}\ \textbf{因子化于素数}（\mathcal X_N=\prod_{p\le N}\mathcal X_{N,p}\ \text{等号成立}\Longrightarrow\text{DEAD}）$$
$$\qquad \Longrightarrow\ \textbf{无法产生全局刚性}✓✓$$
$$\Longrightarrow\ \boxed{\text{同一个障碍在两条线上再现}：\textbf{周期/直积退化}＝\text{KILL-2}}✓✓$$

## §5 修正后的**真靶子**（攻击的唯一净产出）

$$\boxed{\text{真靶子（F3 修正版）}：\ \text{固定总量}\ \sum m_i=N\ +\ \text{整数质量}\ m_i\in\mathbb Z_{>0}\ +\ \text{窗口幅频数据}\ \Longrightarrow\ \text{秩}\ R\le B(W)\ ?}✓✓$$
$$\qquad \text{而加法方向已被封} \Longrightarrow \text{只剩}\ \textbf{非加性形变}（\text{固定质量、保持窗口数据、改变秩}）✓✓$$
$$\qquad ⟹\ \text{这正是}\ \text{`C-122`／`C-123`}\ \text{的}\ \textbf{mixture essentiality} \text{与}\ \textbf{pairwise geometry}✓✓$$
$$\text{四条线汇合}：\text{`B2-1`}\ \text{缺口}＝\text{`C-131`}\ F3＝\text{`C-125`}\ \text{的 pairwise geometry}＝\text{本节真靶子}✓✓$$

## §6 边界与回查

- ⚠️ §2 反例为**构造性＋数值实测**（数值在 `N=256, W=255`；一般 `N>W` 同理）✓
- ⚠️ **不声称** F3 修正版可证；**不声称** 反例穷尽所有逃逸通道 ✓
- ⚠️ §4 的 KILL-2 同一物为**结构识别**（非定理级）✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 11:2x）`[纪律]`（先跑后写）

```
技术词 窗口隐形    命中文件数=0 ::  ⟹ 本档新增
技术词 幂等测度    命中文件数=0 ::  ⟹ 本档新增
技术词 完整周期    命中文件数=4 :: ./C87-...md ./E218-...md ./PAPERA-block-method.md ⟹ 沿用
```
**读数（按实测）**：`窗口隐形`／`幂等测度` 为**本档新增**；`完整周期`为**沿用** ✓

---

## 【定位修正·`C-135`】（2026-09-19 11:40）

⚠️ 本档 §4／§5 的**反例引擎识别**须按 `C-135` 修正：所谓"窗口隐形测度"**就是** FRI／湮灭滤波器框架（Vetterli–Marziliano–Blu, IEEE TSP **50**(6):1417–1428, 2002）里**采样算子零空间**的同一对象（`dim ker = N−2W`）；
⟹ **机制不新**，反例仍成立但**不得主张机制新颖**；分级带子标签 **T-I(c)**（经典机制）。

---

## 【更正·`C-136`】（2026-09-19 11:45）

⚠️ §5／§3 关于"缺失假设＝分离下界"的定位**须修正**：FRI／超分辨率文献（Candès–Fernandez-Granda：
"There is no separation requirement if all $d_i$ are positive"）表明**正性可替代分离**；我方正性成立 ⟹ 分离本不是障碍。
**真正的缺口是"相位"**（我方数据仅模长）。反例与核维数判据均不变。
