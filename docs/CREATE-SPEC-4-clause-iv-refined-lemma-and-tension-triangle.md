已查地图（**先查后写**）：`CREATE-SPEC-1/2/3`（四条款规格 + A/B/C/D/E 五候选的门序结果）、`V227` §5（**构造性 vs 涌现性**：Selberg 模板成功因零点由特征值**定义**（构造性）；ζ 的零点**涌现**）、`viii-monodromy-derivation`（`P(s)=\sum_p p^{-s}` 奇点＝缩放轨道 `\{\rho/k\}`，延拓必经 `\log\zeta`）、`C-122` 三要求、`acpc-loop-death`（链退化）、`euclid-k2-death`（乘性卷积 ⟹ Euler 塌缩）。**结论**：⭐ 攻 (iv) 得**两条真结果** ✓✓：**(一)** 原 (iv) 表述**不准确**（欧拉积的局部因子**本身零-free**；ζ 的零点是**涌现**的，非任何因子之零点）⟹ 正确表述应为 **(iv') 变形必须"移动对象自身的零点"** ✓✓；**(二) ⭐ 引理（初等，可证明）**：**若 `g` 整，则 `Z(f\cdot g)=Z(f)\cup Z(g)`** ⟹ **乘性／整因子变形只能"增加"零点，`f` 的零点位置\ \textbf{完全不动}** ⟹ **一切"乘性算术变形"（完成化移位、特征扭转、乘性卷积）在原理上不能移动 ζ 的零点** ✓✓；（三）由此得到**张力三角**：**算术的（系数侧）⟹ 不能移零点**（引理）；**能移零点 ⟹ 是 `s`-空间操作 ⟹ 坐标**（候选 B 死 `F2`）；**保乘性 ⟹ 欧拉积回归 ⟹ 违 (ii)**（候选 A 死门 1）✓✓ ⟹ **四条款的张力，现有一个角是\ \textbf{证明级}，另两角为见证级** ✓✓

FREEZE-ACK: 本档即冻结期内的构造尝试与门序结果（依 `§8.1`；不产候选结论）

D0: 本档对象 = (iv) 的**表述修正** ＋ **一条初等引理** ＋ **张力三角** —— 关系 = 规格修正与初等结果，非新机制成立
D1: 0

# CREATE-SPEC-4 · **攻 (iv)：一条初等引理 ＋ 张力三角**

> **时间**：2026-09-18 21:28 唐先生：**「继续乙」** ⟹ 攻四条款中最未碰过的 **(iv) 作用于有零点的因子** ✓

---

## §0 结论（先行）

$$\textbf{(一)}\ ⚠️\ \text{原 (iv) 表述}\ \textbf{不准确}：\text{欧拉积的局部因子}\ (1-p^{-s})^{-1}\ \textbf{本身零-free} \Longrightarrow \text{ζ 的零点}\ \textbf{不是任何因子之零点}，\ \text{而是}\ \textbf{涌现}（\text{`V227` §5}）✓✓$$
$$\qquad \Longrightarrow \text{正确表述}\ \textbf{(iv$'$)}：\boxed{\text{变形必须}\ \textbf{移动对象自身的零点}}✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{引理（初等，可证明）}：\text{若}\ g\ \text{整，则}\ \boxed{Z(f\cdot g)=Z(f)\cup Z(g)} \Longrightarrow \textbf{乘性变形只能"加"零点，}\ \textbf{不动}\ f\ \text{的零点}✓✓$$
$$\qquad \Longrightarrow \textbf{一切乘性算术变形}\（\text{完成化移位、特征扭转、乘性卷积}\）\ \textbf{在原理上不能移动 ζ 的零点}✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{张力三角}（\text{四条款的张力}\ \textbf{一角为证明级}）：$$
$$\qquad \text{算术的（系数侧）} \Longrightarrow \textbf{不能移零点}（\text{引理}）;\quad \text{能移零点} \Longrightarrow \boldsymbol{s}\text{-空间} \Longrightarrow \textbf{坐标}（\text{候选 B 死}）;\quad \text{保乘性} \Longrightarrow \textbf{欧拉积回归}（\text{候选 A 死}）✓✓$$

---

## §1 修正：为什么原 (iv) 是错的（重要）

$$\text{原 (iv) 写的是"变形须作用于}\ \textbf{有零点的因子}\text{"}⟹ \textbf{此说在欧拉积上自相矛盾}✓✓$$
$$\qquad \text{局部因子}\ (1-p^{-s})^{-1}\ \text{无零点}（\text{其倒数}\ 1-p^{-s}\ \text{的零点}\ s=2\pi ik/\log p\ \text{变成其}\ \textbf{极点}\text{）}✓$$
$$\qquad \Longrightarrow \text{ζ 的临界带零点}\ \textbf{不由任何局部因子产生}，\ \text{而由}\ \textbf{无穷积的解析延拓} \text{产生} \Longrightarrow \textbf{涌现性}✓✓$$
$$\qquad \Longrightarrow \text{这正是}\ \text{`V227` §5 的}\ \textbf{构造性 vs 涌现性}：\text{Selberg 模板成功，正因其零点由特征值}\ \textbf{定义}（\text{构造性}）✓✓$$
$$\Longrightarrow \textbf{故 (iv) 的正确定形是 (iv$'$)}：\boxed{\text{变形须}\ \textbf{移动该对象自身的零点}}（\text{而非"作用于某个有零点的因子"}）✓✓$$

## §2 ⭐ 引理：乘性变形不能移动零点（带证明）

$$\textbf{引理}：\text{设}\ f\ \text{亚纯}，\ g\ \text{整} \Longrightarrow Z(fg)=Z(f)\cup Z(g)\（\text{按重数计}）;\quad \operatorname{Poles}(fg)=\operatorname{Poles}(f)✓$$
$$\textbf{证明}：\text{在}\ \textbf{零点与极点之外}，\ fg\neq0;\ \text{在}\ f\ \text{的零点}\ z_0\ \text{处}\ fg\ \text{的零阶}\ =\ \operatorname{ord}_{z_0}f+\operatorname{ord}_{z_0}g;\ \text{而}\ g\ \text{整故}\ \operatorname{ord}g\ge0✓$$
$$\qquad \Longrightarrow \text{每个}\ f\ \text{的零点}\ \textbf{原地保留}\（\text{阶数只增不减}\text{）};\ \textbf{无任何零点发生位移}\quad\blacksquare✓✓$$

$$\textbf{推论}：\text{以下全部属于"乘性变形"}\ \Longrightarrow \textbf{一律不移动 ζ 的零点}✓✓$$
$$\qquad \text{(a)}\ \text{完成化移位}\ \pi^{-(s+a)/2}\Gamma\bigl(\tfrac{s+a}{2}\bigr)\zeta(s)\ \text{（候选 D-1）};\quad \text{(b)}\ \text{特征／导子扭转（候选 D-2）}\ \textbf{（严格说非'乘 g'，而是}\textbf{换对象}\text{ ⟹ 另因失败）};$$
$$\qquad \text{(c)}\ \text{乘性 Dirichlet 卷积}\ \zeta*g\ \text{（DS}\ =\zeta(s)G(s)\text{）};\quad \text{(d)}\ \text{乘任意整函数}\ \zeta(s)\cdot h(s)$$
$$\Longrightarrow \textbf{它们能"看见"的零点，全是它们自己带进来的（}g\ \text{或}\ h\ \text{的零点）}，\ \text{与 ζ 的零点位置}\ \textbf{无关}✓✓$$

## §3 ⭐ 张力三角（(i) 与 (iv$'$) 的可证冲突）

$$\textbf{角 A（系数侧／算术）}：\text{算术}\ ✓(i),\ \text{无欧拉积}\ ✓(ii)\ \text{可能};\quad \textbf{但}\ \text{引理} \Longrightarrow \textbf{不移零点}\ ✗(iv$'$)✓✓$$
$$\qquad \text{实例}：\text{ACPC（加性卷积）}——(i)(ii) 真通过，\ \text{死于}\ (iii)✓$$
$$\textbf{角 B（}s\text{-空间）}：\text{能移零点}\ ✓(iv$'$);\quad \textbf{但是坐标操作}\ ✗(i)✓✓$$
$$\qquad \text{实例}：\text{DBN 热流（候选 B）}——\text{门 1 通过、报火，死于}\ F2✓$$
$$\textbf{角 C（保乘性）}：\text{欧拉积结构}\ ✓;\quad \textbf{但}\ \text{违}\ (ii)（\text{需局部因子}）✗✓✓$$
$$\qquad \text{实例}：\text{部分欧拉积（候选 A）}——\text{死于}\ \text{`TESTABLE-1`}✓$$
$$\Longrightarrow \boxed{\text{三角：任一候选只能选一角，}\ \textbf{必死于对角}}✓✓$$
$$\qquad \text{其中}\ \textbf{角 A ↔ 角 B 的冲突}\ \text{由}\ §2\ \text{引理}\ \textbf{证明};\ \text{另两侧为}\ \textbf{见证级}✓✓$$

## §4 由 (乙) 得到的**精确缺口命名**

$$\text{要满足}\ (i)\wedge(ii)\wedge(iii)\wedge(iv')\ \text{，需要}\ \textbf{一个非乘性的、系数侧的、能移动零点的典范算术操作}✓✓$$
$$\qquad \text{已知的系数侧操作分类}：$$
$$\qquad \qquad \text{(a) 乘性}（\text{乘一整因子}） \Longrightarrow \textbf{不移零点}（引理）✗$$
$$\qquad \qquad \text{(b) 非线性逐点}（a_n\mapsto a_n^2\ \text{等}） \Longrightarrow \textbf{移零点}\ ✓\ \text{但乘性}\ a_n\ \text{被保持} \Longrightarrow \textbf{欧拉积回归}\ ✗(ii)✓✓$$
$$\qquad \qquad \text{(c) 非乘性线性}（\text{加性卷积}） \Longrightarrow (i)(ii)\ ✓\ \text{但}\ \textbf{链退化}（`acpc-loop-death`）✗(iii)✓✓$$
$$\Longrightarrow \textbf{三个子类各死于一处} \Longrightarrow \text{缺口＝"非乘性 ＋ 系数侧 ＋ 移零点 ＋ 极限恢复"}\ \text{的}\ \textbf{第四子类};\ \textbf{候选数 0}✓✓$$

## §5 边界与回查

- ⚠️ §2 引理为**初等且完整证明** ⟹ 本会话第二条**真证明级**产物（第一条：候选 D 的 `F3` 死）✓✓
- ⚠️ §1 的"ζ 零点涌现性"为 `V227` §5 的**引用**（非本档首提）✓
- ⚠️ §3 张力三角为**本档综合**（引理 ＋ 三次门序见证），**非定理**；仅角 A↔B 的冲突有证明 ✓
- ⚠️ §4 的三子类分类为**本档判断**（可能不完备：如"卷积极限""再生核"等未逐一列入）✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:2x）`[纪律]`（先跑后写）

```
技术词 张力三角          命中文件数=1  :: ./CREATE-SPEC-4-…（本档）
技术词 移零点           命中文件数=1  :: ./CREATE-SPEC-4-…（本档）
技术词 乘性变形不移动零点   命中文件数=1  :: ./CREATE-SPEC-4-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增** ✓；并**依纪律标注**：(b) 类（扭转）**不属**引理所辖，另有失败因（换对象）✓
