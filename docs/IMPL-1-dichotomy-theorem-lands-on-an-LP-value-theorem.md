已查地图（**先查后写**）：`EXT-SCAN-2/3/4`（bootstrap 精读 ＋ oracle 形式 ＋ 二分定理化目标）、`CEILING-AUDIT-3`（定义 ＋ 前沿自陈唯一未证项 ＋ §4(γ) 路线）、`C-74`（主链与判词）、`V185`／`V186`（67.2%／0.6818287）、`V188` §2、`POS1`。关键词回查：`约束集化`＝0、`对偶确认`＝0、`主原构造`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:05「继续」⟹ 执行 (A)（把论证重写成族上符号定形式）**找到比我预想更好的落点** ✓✓：**(一) 我方二分结构已存在**——`CEILING-AUDIT-3` §4(γ) 的 **LP** 就是 bootstrap `(5.12)/(5.13)` 的我方对应物（约束集＝封闭区间 `enclosures`，目标＝simple fraction，`0.6818287`）✓✓；**(二) ⭐ 且它\ \textbf{绕过"正性公理"缺失}**——LP 对偶不需要正性公理，约束集由 **区间算术（机器可检）** 提供 ⟹ 这正是 bootstrap"参数无关约束"的我方实现 ✓✓；**(三) ⭐ 故二分定理的我方陈述＝\ \textbf{一个 LP 的取值定理}**：`p^{*}=\min\{\text{simple fraction}\}` over 约束集；**主原构造** ⟹ 推翻天花板；**对偶证书** ⟹ 独立确认天花板 —— **两种结局都是定理**（不是经验数值）✓✓

FREEZE-ACK: 本档即冻结期内的实施设计（依 `§8.1`；不产候选结论、不执行计算）

D0: 本档对象 = **把 bootstrap 的二分结构落到我方 LP（`CEILING-AUDIT-3` §4(γ)）上的实施设计**（含"绕过正性公理"与"两种结局皆定理"两条结论） —— 关系 = 实施设计，非新机制
D1: 0

# IMPL-1 · **二分定理的我方落点 ＝ 一个 LP 的取值定理**

> **时间**：2026-09-18 23:05 唐先生：**「继续」** ⟹ 执行 (A) ✓

---

## §0 结论（先行）

$$\textbf{(一)}\ \text{我方二分结构}\ \textbf{已存在}：\text{`CEILING-AUDIT-3` §4(γ) 的 LP ＝ bootstrap}\ (5.12)/(5.13)\ \text{的对应物}✓✓$$
$$\textbf{(二)}\ ⭐\ \text{它}\ \textbf{绕过"正性公理"缺失}：\text{LP 对偶不需正性公理};\ \text{约束集由}\ \textbf{区间算术（机器可检）} \text{提供}✓✓$$
$$\textbf{(三)}\ ⭐\ \text{二分定理的我方陈述＝}\textbf{一个 LP 的取值定理};\ \textbf{两种结局都是定理}✓✓$$

---

## §1 逐字基础（`CEILING-AUDIT-3`）

$$\textbf{前沿自陈唯一未证项（`NumericCert.lean` 逐字）}：$$
$$\boxed{\text{"What is NOT proved here: }\textbf{that the true form factor of a given configuration lies in the enclosures}\text{ — for a concrete law those come from an }\textbf{interval-arithmetic computation outside Lean}\text{"}}✓✓✅$$
$$\Longrightarrow \textbf{唯一未证项＝一条不等式}：\text{对抗律的真实形状因子}\in\text{封闭区间}✓✓$$
$$\textbf{§4(γ) 路线（逐字）}：\text{把封闭区间当作}\ \textbf{约束集}，\ \text{问}$$
$$\boxed{\min\{\text{simple fraction}\}\ \text{over marked configs with form-factor grid}\in\text{enclosures}\ \stackrel{?}{=}\ 0.6818287}✓✓$$
$$\qquad \text{"若我们能构造出更小 simple fraction 的律}\ \Longrightarrow \textbf{天花板被推翻}";\quad \text{"若不能，且我们能给出}\ \textbf{匹配的对偶证书}\ \Longrightarrow \textbf{天花板被独立确认}\text{"}✓✓$$
$$\qquad \text{可行性（逐字）}：\text{"约束集（256 行）}\ \textbf{已在手}；\ \text{目标＝简单点比例（线性）}\Longrightarrow\ \text{一个}\ \textbf{可在本地求解的 LP}\text{"}✓✓$$

## §2 ⭐ 映射（bootstrap ↔ 我方 LP）

| bootstrap | 我方（`CEILING-AUDIT-3` §4(γ)） |
|:--|:--|
| 谱族 $\Sigma(\Delta_{\min})$（含连续参数） | **约束集** $\mathcal C:=\{\text{configs}: \text{form-factor grid}\in\text{enclosures}\}$ |
| 一致性方程（crossing） | **enclosures**（256 行，区间算术给出，机器可检） |
| 临界值 $\Delta_c$ | **simple fraction 的最小值** $p^{*}$（$0.6818287$） |
| $(5.12)$ 存在符号定泛函 ⟹ 排除 | **对偶证书** ⟹ **天花板被独立确认** |
| $(5.13)$ 不存在 ⟹ 可行 | **主原构造**（更小 simple fraction 的律）⟹ **天花板被推翻** |
| 截断外校验（严格性所在） | **区间算术的封闭性**（`cert_of_check`：`check d = true` ⟹ 对**区间的每一条实序列**成立） |

$$\Longrightarrow ⭐\ \text{两边}\ \textbf{同型}：\text{都是"给约束集，问某线性目标的极值"}✓✓$$

## §3 ⭐ 为什么它**绕过"正性公理"缺失**

$$\text{bootstrap 需要参数无关正性公理（unitarity）；}\ \text{ζ 没有}（\text{`EXT-SCAN-3`}\ \text{§2}）✗$$
$$\text{但}\ \textbf{LP 对偶不需要正性公理}：\text{线性规划的对偶证书}\ \text{由}\ \textbf{约束集本身的凸性} \text{给出}✓✓$$
$$\qquad \Longrightarrow \text{约束集由}\ \textbf{区间算术} \text{提供（}\texttt{cert\_of\_check}\ \text{已是机器可检的）}⟹ \textbf{"参数无关约束"的我方实现}✓✓$$
$$\qquad ⚠️\ \text{代价（诚实）}：\text{该 LP 只关于}\ \textbf{方法类的天花板}（\text{bandwidth-one 证书类}），\ \textbf{不是 RH}✓✓$$

## §4 ⭐ 二分定理的**我方陈述**（目标形态）

$$\textbf{定义}：\mathcal C\ \text{＝满足 256 行封闭区间约束的构型集};\quad p^{*}:=\min_{\text{cfg}\in\mathcal C}\{\text{simple fraction}\}✓$$
$$\textbf{目标（二分）}：\quad \boxed{p^{*}\ =\ 0.6818287\ \text{（定理级）}}✓✓$$
$$\qquad \textbf{(主原)}\ \text{构造}\ \text{cfg}^{*}\in\mathcal C\ \text{达}\ p^{*}（\text{或更低}） \Longrightarrow \textbf{天花板被推翻}（\text{若更低}）✓$$
$$\qquad \textbf{(对偶)}\ \text{给出对偶可行解}\ \Longrightarrow p^{*}\ \textbf{不可低于}\ 0.6818287 \Longrightarrow \textbf{天花板被独立确认}✓✓$$
$$\Longrightarrow ⭐\ \textbf{两种结局都是定理}：\text{不是"我们测到}\ 0.682"，\ \text{而是"}\textbf{该证书类下界}\ =0.6818287"\ ✓✓$$
$$\qquad \text{这正是}\ \text{`EXT-SCAN-4`}\ \text{§5 想要的形式}（\text{把经验天花板升级为二分临界值}）✓✓$$

## §5 执行清单（尚未执行；待唐先生批准）

$$\text{(1)}\ \textbf{数据}：256\ \text{行封闭区间（}\text{"已在手"}\text{，前档已核：}[lo_j,hi_j]=[2^{132}j-1,2^{132}j],\ j=1..255）✓$$
$$\text{(2)}\ \textbf{变量}：\text{简单点比例（线性目标）};\ \text{约束}：256\ \text{行}\ \pm\ \text{网格关系}✓$$
$$\text{(3)}\ \textbf{求解}：\text{本地 LP（可用}\ \texttt{scipy.optimize.linprog}\text{）}✓$$
$$\text{(4)}\ \textbf{提取对偶证书}：\texttt{linprog}\ \text{返回}\ \texttt{marginals}（\text{对偶变量}）⟹ \textbf{即证书}✓✓$$
$$\text{(5)}\ \textbf{判词}：\text{若}\ p^{*}<0.6818287\ (\text{数值显著}) \Longrightarrow \text{先怀疑自己的实现（历史 11 次教训）}✓✓$$

## §6 边界与回查

- ⚠️ §1 全部**逐字**（`CEILING-AUDIT-3`），§2 映射／§4 陈述／§5 清单为**本档设计**（**未执行**）✓
- ⚠️ **不声称**天花板有错；**不声称**能办到；**不声称**该 LP 与 RH 有关（它只关于证书类）✓
- **未用** RH 作推导；**未取** JSON；**未**求解 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）✓
- ⚠️ 与 `C-116` 一致：本档是**定理目标的设计**，不是归纳结论 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:0x）`[纪律]`（先跑后写）

```
技术词 约束集化      命中文件数=0  ⟹ 本档新增
技术词 对偶确认      命中文件数=0  ⟹ 本档新增
技术词 主原构造      命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
