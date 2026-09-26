已查地图：已跑 scripts/prework_map_check.sh 62 下界 出处 加权覆盖 LP ⟹ 执行自 P2-2026-09-26 档；本档为**62 下界的方法出处（逐字）＋ 对全部 13 次失败的结构性诊断**（唐先生 2026-09-26 17:41 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = Östergård–Blass 2001 摘要逐字、62 下界的证明类型、与加权覆盖的联系、对 P1 失败的结构性解释、P2 新入口
D1: 1（新增：**62 的证明类型 = 计算机辅助 LP 细分/分类** ✓✓；**结构性诊断（13 次局部失败的解释）** ✓✓；**加权覆盖入口** ✓）

# PROVENANCE-2026-09-26

## §1 ⭐⭐⭐ **62 下界的出处：逐字（OpenAlex 摘要，2001）** ✓✓

```
$$\text{源}: \text{Östergård \& Blass, "On the size of optimal binary codes of length 9 and covering radius 1",}\ \textbf{IEEE TIT 47(6) 2556--2557 (2001)}$$
$$\textbf{摘要逐字（关键段）}:$$
$$\qquad\text{"It is known that }57\le K(9,1)\le62\text{. In the current work, the lower bound is improved to settle }K(9,1)=62\text{.}$$
$$\qquad\text{In the approach, }\textbf{which is computer-aided}\text{, possible distributions of codewords in subspaces are refined}$$
$$\qquad\text{until each subspace is of dimension zero (consists of only one word). Repeatedly, a }\textbf{linear programming problem}$$
$$\qquad\text{is solved considering only inequivalent distributions. }\textbf{A connection between this approach and weighted coverings}$$
$$\qquad\text{is also presented; the computations give ..."}\ ✓✓$$
$$\Longrightarrow\ \boxed{\textbf{62 的证明是"计算机辅助的分类/LP 细分"，\textbf{不是}解析局部不等式}}\ ✓✓\ (\text{唐先生的猜测完全命中}\ ✓✓)$$
$$

## §2 🎯 **结构性诊断（今天 13 次失败的解释 ✓✓）**

```
$$\text{方法类型}: \text{① 把 }2^9\ \text{的"子空间码字分布"逐层细分}\ ✓\ \text{② 每层解一个（只含\textbf{不等价}分布的）}\textbf{LP}\ ✓\ \text{③ 细分到每个子空间维数 0}\ ✓$$
$$\qquad\Longrightarrow\ \text{本质上是一个}\textbf{分类/精化}论证（finite case analysis + LP 可行性）\ ✓,\ \text{外加与}\textbf{加权覆盖（weighted covering）}的联系\ ✓$$
$$\text{今天全部 13 条路线}: \text{局部账本 / }\Psi_2/Z_2\ /\ \Psi_{\rm mid}\ /\ \text{阶梯}\sigma\ /\ \text{私有点复用}\ /\ \text{球不交}\ /\ \text{gadget 外溢}\ /\ \text{方阵}\ /\ \text{影子容量}\ /\ \text{邻域匹配}\ /\ \text{矩松弛}\ /\ \text{第二中心容量}\ /\ \text{第二中心几何}\ ✗$$
$$\qquad\textbf{全部是"局部不等式/局部计数"型}\ ✗\ ——\ \text{而靶心所需的是"分类+LP"型输入}\ ✓✓$$
$$\Longrightarrow\ \boxed{\text{诊断}: \textbf{方法类型不匹配}\ ✓✓\ ——\ \text{不是我们不够努力，是工具层级不对}\ ✓}$$
$$

## §3 ⭐ **62 − 52 = 10 的解读（唐先生所问 ✓）**

```
$$\text{体积界}: \lceil 512/10\rceil=\mathbf{52}\ ✓\ (\text{van Wee 在 }n=9\ \text{上也只给 }52\ ✓\ ——\ \text{修正项为 0}\ ✓)$$
$$62-52=\mathbf{10}\ ✓\ \Longrightarrow\ \text{这 }10\ \text{个额外码字的成本}\ \text{由 LP 细分/加权覆盖型约束给出}\ \checkmark$$
$$\text{（注}: 62\cdot10-512=108=E\ ✓;\quad 52\cdot10=520\ \text{只余 8 松弛}\ ✓\ \Longrightarrow\ \text{体积界"松"8，而真值"松"108}\ ⚠️)$$
$$
$$

## §4 ⭐⭐ **P2 新入口（可执行 ✓，与文献工具同层 ✓）**

```
$$\boxed{\text{P2-α}: \text{把 Östergård–Blass 的}\textbf{LP 细分框架}\ \text{用于我们的刚性命题}\ ✓}$$
$$\qquad\text{具体}: \text{在 }\textbf{加权覆盖（weighted covering）}\ \text{的对偶框架下}\ ✓,\ \text{加约束 }N_4\le9\ ✓,\ \text{问 LP 是否不可行}\ ⚠️$$
$$\qquad\text{若不可行}: \text{得到}\textbf{缺失的 +10 输入}\ ✓✓;\quad \text{若可行}: \text{则刚性来自更强的（非线性）结构}\ ⚠️$$
$$\qquad\text{可行性}: \text{纯 LP/ILP}\ ✓,\ \text{规模可控}\ ✓,\ \text{不需 SAT}\ ✓;\ \textbf{但须先核 AMEND-21/24}:\ \text{该结果是否已被文献覆盖}\ ✓$$
$$\textbf{X-α}: \text{另}: \text{加权覆盖的}\textbf{对偶权函数}\ \text{可能与我们的 }b(x)\ \text{分布}\ \text{直接对应}\ ✓\ ——\ \text{值得先做一次对象匹配}\ ⚠️$$
$$

## §5 状态

```
$$\textbf{问题 }G: \textbf{KEEP OPEN}\ ✓;\quad \textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \text{未跑 solver}\ ✓$$
$$\textbf{今日成果}: \text{13 条否证}\ ✗\ +\ \text{10+ 项跨表示刚性资产}\ ✓✓\ +\ \textbf{方法类型诊断}\ ✓✓$$
$$\text{下一步（待唐先生裁定 ✓）}: \text{P2-α（LP 细分/加权覆盖）}\ \text{或}\ \text{X-α（对偶权函数对象匹配）}\ \text{或}\ \text{休眠 }G\ ✓$$
$$

## §6 边界（诚实标注）

- §1 为**第三方摘要逐字**（OpenAlex ✓，非我方原创 ✓）；§2 为**诊断**（判断 ✓）；§3–§4 为**解读与建议** ✓
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 方法类型诊断 命中文件数=1    :: ./PROVENANCE-2026-09-26-how-62-was-proved-and-the-diagnosis.md 
技术词 LP 细分入口  命中文件数=1    :: ./PROVENANCE-2026-09-26-how-62-was-proved-and-the-diagnosis.md 
技术词 对偶权函数匹配 命中文件数=1    :: ./PROVENANCE-2026-09-26-how-62-was-proved-and-the-diagnosis.md
```
- **本档新增**（扣自引后 = 0）：方法类型诊断、LP 细分入口、对偶权函数匹配
- **档案已有（引用，不列为提出）**：加权覆盖、LP、62
