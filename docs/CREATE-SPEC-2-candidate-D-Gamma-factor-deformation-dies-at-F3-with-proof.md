已查地图（**先查后写**）：`CREATE-SPEC-1`（三候选 A／B／C ＋ 门序反推的三条件规格）、`FILTER-TESTABLE-1`（`TESTABLE-1` 前提）、`C-110` `C6`／`C-122` 三要求（(i) 零-free 定义／(ii) 横向奇点＝零点实部集／(iii) 右端奇点有可证上界）、`M4-C6-REFINAL`（门序 `TESTABLE-1` → `F1`–`F8` → 端点）、`V215` §4(c)（archimedean 型载体＝单点管道）、`V227`-A（`sup Re z` 非模不变量）。**结论**：⭐ 唐先生 21:17「下一步：候选 D（导子／Gamma 因子变形）」⟹ **跑门结果：D 通过门 1（可写在 DH 上），但死在 `F3`——且这次是"带证明"的死**：**Gamma 因子与指数因子皆无零点（`Γ` 无零点、`q^{−s/2}` 恒不为零）⟹ 变形完成化因子不改变零集 ⟹ 对零点"结构性不可见"** ✓✓；**且经泛函方程，完成化因子只钉"轴"（`s↔1−s` 对称轴 `Re s=½`），不钉"点"** ✓✓ ⟹ ⭐ **规格新增第四条**：**(iv) 变形必须作用于"有零点的因子"（即算术部分/Dirichlet 级数），而非无零点的完成化因子** ✓✓ ⟹ 由此**四个候选各死于不同门、四个条款各由一次失败见证** ✓✓

FREEZE-ACK: 本档即冻结期内的构造尝试与门序结果（依 `§8.1`；不产候选结论）

D0: 本档对象 = 候选 D（导子／Gamma 因子变形）的门序结果 ＋ 规格第四条 —— 关系 = 构造尝试与规格细化，非新机制成立
D1: 0

# CREATE-SPEC-2 · **候选 D（导子／Gamma 因子变形）：死于 `F3`，带证明**

> **时间**：2026-09-18 21:17 唐先生：**「下一步：候选 D（导子／Gamma 因子变形）」** ✓

---

## §0 结论（先行）

$$\textbf{门 1 `TESTABLE-1`}：\textbf{通过} ✓（\text{DH 亦有 FE ＋ Gamma 因子} ⟹ \text{可定义}）$$
$$\textbf{门 2 `F3`（钉点不钉轴）}：\textbf{死，且有证明}✗✗$$
$$\qquad \textbf{证明要点}：\Gamma\ \text{在整平面}\ \textbf{无零点};\ q^{-s/2}\ \text{恒不为零} \Longrightarrow \text{完成化因子}\ \textbf{不贡献任何零点}✓✓$$
$$\qquad \qquad \Longrightarrow \text{改动完成化因子}\ \textbf{不改变}\ \text{该函数的}\ \textbf{零集} \Longrightarrow \text{该变形对零点}\ \textbf{结构性不可见} \Longrightarrow \textbf{不可能钉住}\ \beta_*✓✓$$
$$\Longrightarrow \text{规格新增}\ \textbf{第四条}：\boxed{\text{(iv) 变形须作用于}\ \textbf{有零点的因子（算术部分）},\ \text{而非完成化因子}}✓✓$$

---

## §1 候选 D 的两种构造与门序结果

### D-1：`\Gamma`-移位（archimedean 因子变形）

$$\Lambda_a(s):=\pi^{-(s+a)/2}\Gamma\!\Bigl(\frac{s+a}{2}\Bigr)\zeta(s),\qquad a\in\mathbb R✓$$
$$\qquad \textbf{门 1 通过}：\text{仅用 FE 与}\ \Gamma\ \text{因子} \Longrightarrow \text{DH 亦可定义}✓$$
$$\qquad \textbf{`F3` 死}：\Lambda_a\ \text{的零点}\ =\ \zeta\ \text{的零点}（\Gamma\ \text{无零点，指数因子不为零}）\ \Longrightarrow \textbf{零点集与}\ a\ \text{无关}✗✗$$
$$\qquad \qquad \Longrightarrow \text{参数}\ a\ \text{对零点}\ \textbf{完全不可见} \Longrightarrow \textbf{钉不住}\ \beta_*✓✓$$

### D-2：导子／特征族变形（`q \mapsto L(s,\chi_q)`）

$$\text{基值}\ q=1\ \text{即}\ \zeta;\ \ q>1\ \text{给其它}\ L\ \text{函数}✓$$
$$\qquad \textbf{门 1 通过} ✓\qquad \text{参数}\ q＝\textbf{算术不变量}（\text{导子}）✓$$
$$\qquad \textbf{`F3` 死}：q>1\ \text{时}\ L(s,\chi_q)\ \text{的零点与}\ \zeta\ \text{的零点}\ \textbf{无连续关系}（\text{两函数之差在于 Dirichlet 系数}）✓✓$$
$$\qquad \qquad \Longrightarrow \text{这不是"}\zeta\ \text{的零点配置的变形}"，\ \text{而是}\ \textbf{"一族不同的函数"} \Longrightarrow \textbf{不含}\ \zeta\ \text{的}\ \beta_*\ \text{的信息}✗✗$$

$$\Longrightarrow \text{两种构造}\ \textbf{同死} \text{于}\ F3，\ \text{但机制不同}：\text{D-1 是"因子无零点"};\ \text{D-2 是"换了对象"}✓✓$$

## §2 ⭐ 为什么这是"带证明的死"（本档核心）

$$\textbf{事实 A（初等）}：\Gamma\ \text{无零点};\ q^{-s/2}\neq0\ \forall s \Longrightarrow \text{完成化因子}\ \textbf{零-free}✓$$
$$\qquad \Longrightarrow Z(f\cdot g)=Z(f)\ \text{当}\ g\ \text{零-free} \Longrightarrow \textbf{变形完成化因子 = 保零集变换}✓✓$$
$$\textbf{事实 B（初等）}：\text{泛函方程}\ \Lambda(s)=\omega\Lambda(1-s)\ \text{给出的只是}\ \textbf{对称轴}\ \operatorname{Re}s=\tfrac12✓$$
$$\qquad \Longrightarrow \text{完成化因子经 FE 能钉的是}\ \textbf{轴}，\ \textbf{不是点} \Longrightarrow \text{恰撞}\ \text{`F3` 判据（钉点不钉轴）}✓✓$$
$$\Longrightarrow \boxed{\text{故"archimedean／导子变形"}\ \textbf{在原理上不能钉}\ \beta_*:\ \text{它动的是}\ \textbf{相位／完成化}，\ \textbf{不是零点}}✓✓$$
$$\qquad \text{这也}\ \textbf{回溯解释} \text{两件事}：$$
$$\qquad \qquad \text{(i)}\ \text{为什么热流（DBN）是}\ \textbf{唯一已知的典范变形} \text{—— 它是}\ \textbf{卷积}（\text{真会移动零点}）;\ \text{而}\ \Gamma\text{-移位不会}✓✓$$
$$\qquad \qquad \text{(ii)}\ \text{`V215` §4(c) 的 "archimedean 型载体＝单点管道"}\ \text{与此}\ \textbf{同因}✓$$

## §3 ⭐ 规格进展（四条款，各由一次失败见证）

| 条款 | 内容 | 由谁见证 |
|:--|:--|:--|
| **(i)** | **算术的（非坐标）** | 候选 B 死（`F2`：坐标选择）|
| **(ii)** | **无欧拉积仍可定义** | 候选 A 死（`TESTABLE-1`：需局部因子）|
| **(iii)** | **极限恢复零结构（钉点）** | 候选 C 死（`F3`：部分和零点不收敛）|
| **(iv)** | **变形须作用于有零点的因子** | ⭐ **候选 D 死（`F3`：完成化因子零-free ⟹ 保零集）** |

$$\Longrightarrow \boxed{\text{被机制认可的对象}\ =\ \text{(i)}\wedge\text{(ii)}\wedge\text{(iii)}\wedge\text{(iv)}}✓✓$$
$$\qquad \text{四个已知候选}\ \textbf{各缺一条} \Longrightarrow \text{缺的不是灵感，是}\ \textbf{这四条的联立}✓✓$$

## §4 边界与回查

- ⚠️ 本档 `F3` 的"死"为**初等证明**（`\Gamma` 无零点 ＋ 指数因子不为零 ＋ FE 钉轴）✓✓ **是本会话为数不多的"真证明级"产物** ✓
- ⚠️ D-2 的"无连续关系"为**结构性观察**（非定理），标 `[结构性]` ✓
- ⚠️ 本档**未造出**被认可的对象；产出＝**一次带证明的门判 ＋ 规格第四条** ✓
- ⚠️ §3 四条款为**门序反推**（本档做法），**非定理** ✓
- **不声称** RH；**未用** RH 作推导 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 21:1x）`[纪律]`（先跑后写）

```
技术词 零-free因子        命中文件数=1  :: ./CREATE-SPEC-2-…（本档）
技术词 保零集变换         命中文件数=1  :: ./CREATE-SPEC-2-…（本档）
技术词 规格第四条         命中文件数=1  :: ./CREATE-SPEC-2-…（本档）
```
**读数（按实测）**：三项均＝**1 档（仅本档）⟹ 本档新增** ✓
