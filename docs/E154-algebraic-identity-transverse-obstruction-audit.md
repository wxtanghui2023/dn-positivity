# E154 · ⭐⭐⭐⭐ **纯代数恒等式型 → 横向 obstruction → separation？**
### **未找到反例 ✗；且理由【决定性 ✓】：$i\mathbb R$ **不是代数集** ✗ ⟹ 纯代数条件无法【一般地】强制根落在其上 ✓**

> 委托 ✓ 唐先生 2026-09-14 12:31（**只做这一件 ✓：纯代数恒等式型的穷举式反例审计 ✓；判死测试 ✓**）
> 依据 ✓ `E153`（$C_2$ 独立 ✓）＋ 您 §4–§7（横向 obstruction ✓／五类列表 ✓）
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 判定（✓ 四条）

```
⭐⭐⭐⭐ **① 反例【未找到 ✗】—— 且有一个【决定性的结构理由 ✓】**
   $$\boxed{i\mathbb R=\operatorname{Fix}(\tau\sigma)\ \textbf{【不是代数集 ✗】}}（\text{由 }z+\bar z=0\ \text{定义 ✓，}\textbf{用了共轭/超越操作 ✗）}$$
   $$\Longrightarrow\ \text{【无】多项式 }P\ \text{的解集【等于】}i\mathbb R\ ✗\ \text{（乃至【等于】}i\mathbb R\cap\{\Xi\ \text{的根}\}\ ✗）$$
   $$\Longrightarrow\ ⭐\ \text{任何"纯代数"条件若强制"根}\subset i\mathbb R\text{" ✓，必是该对象【自身的特例 ✓】，}\textbf{而非【一般机制 ✗✓】}$$
🔴 **② 古典根定位理论【全部经正性/序 ✗】（逐条 ✓）**
   | 路径 ✓ | 判据形态 ✓ | 是否需正性/序 ✗ |
   |:--|:--|:--|
   | **Hermite–Biehler**（实根性 ⟺ Hankel/Toeplitz 型 PSD ✓） | **正定 ✗** | ✅ **需要 ✓** |
   | **Newton 不等式**（系数全正性 ✓） | **不等式 ✗** | ✅ **需要 ✓** |
   | **Hurwitz 判据**（Routh–Hurwitz ✓） | **符号 ✗** | ✅ **需要 ✓** |
   | **Sturm 振荡**（ODE ✓） | **比较不等式 ✗** | ✅ **需要 ✓** |
   | **判别式 det ✓** | 代数恒等式 ✓ | ❌ **不需 ✓ —— 但它只测【重数 ✗】，不测【位置 ✗】** |
   $$\Longrightarrow\ \textbf{唯一纯代数者（判别式 ✓）【不测位置 ✗】；能测位置者【全需正性/序 ✗】✓✓}$$
⭐ **③ 判死测试结果 ✓（依您 §7 ✓）**：**未找到**"不用正性/序/度量/范数、却能产生严格横向 obstruction ✗"的例子 ✓
   $$\text{（包括：无不等式 ✓、无正定型 ✓、无 Hilbert/Krein ✓、无 contraction/unitarity ✓、无变分原理 ✓、无概率正性 ✓、}\textbf{不把 }z+\bar z=0\ \text{当定义 ✗）}$$
   $$\Longrightarrow\ \text{依您的判据 ✓：}\textbf{separation 必然性方向【存活 ✓】，首次具备强形式雏形 ✓}$$
⭐ **④ 但【未证】必要归约 ✗**：\text{"任何 canonical 横向 obstruction 都归约为横向二次/分离型 ✗"}\ \textbf{仍开放 ✓}
```

## 1. 为什么"纯代数"路线在结构上【必败 ✗】（✓ 本轮核心论证 ✓）

$$\text{设纯代数条件 }P(z)=0\ ✓\ \text{（}P\ \text{由 FE 闭包与共轭闭包生成 ✓，系数在 }\mathbb Q\ \text{或相应代数域 ✓）}$$
$$\text{要它推出 }C_2\ ✓，\text{须：}\ \{\text{根集}\}\cap\{\Xi\ \text{的根}\}\subseteq i\mathbb R\ ✗\ \text{—— 特别地}\ \textbf{要求 }P\ \text{的解集【本身】落在 }i\mathbb R\ \text{上 ✓或至少在其中选根 ✗}$$
$$\textbf{而 }i\mathbb R\ \text{的方程是 }z+\bar z=0\ ✓\ ——\ \textbf{含【共轭】✗，}\text{不是 }\mathbb C\ \text{上的多项式方程 ✓✓}$$
$$\Longrightarrow\ \textbf{故 }P\ \text{不能"表示" }i\mathbb R\ ✗\ \Longrightarrow\ \text{任何有效的 }P\ \text{必【逐个对象特制 ✓】，}\textbf{非一般机制 ✗}$$
$$\text{（}\textbf{具体反例检验 ✓}：P(z)=z^2+1\ ✓\ \text{偶 ✓、实系数 ✓、纯代数 ✓、根 }\{\pm i\}\subset i\mathbb R\ ✓\ ——\ \textbf{但}\ \{\pm i\}\neq Z(\Xi)\ ✗\ \text{故失败 }C_1\ ✓✓}$$
$$\qquad\text{即：}E152\ \text{的有限反例【}i(\tau\sigma)\text{】在代数型里【同一现象 ✓】—— 它能锁轴 ✓，但}\textbf{锁的不是零点集 ✗✓）}$$

## 2. 对您五类列表的**逐类裁决**（✓ 依您 §5 ✓）

$$\textbf{I. 代数恒等式 ✗}：\text{本轮审计 ✓ —— 唯一纯代数者（判别式 ✓）不测位置 ✗（§0② ✓）}\ \textbf{不构成反例 ✓}$$
$$\textbf{II. 度量型 ✓}：\text{本征向量 }2\Re\lambda\|v\|^2=0\ \Longrightarrow\ \Re\lambda=0\ ✓\ —— \text{obstruction}=\|v\|^2>0\ ✓\ \textbf{明确属 separation ✓}$$
$$\textbf{III. 序型 ✓}：Q(z)\ge0\ \wedge\ Q=c(\Re z)^2\ ✓\ \textbf{仍是 separation ✓（未显式写内积 ✓，但同构 ✓）}$$
$$\textbf{IV. 几何型 ✓}：\text{守恒量 }H\ ✓\ \text{若 }H(z)-H(\kappa z)\ \text{控制 }(\Re z)^2\ ✓ \Longrightarrow \textbf{仍给横向 obstruction ✓（＝ separation 的一种 ✓）}$$
$$\textbf{V. 拓扑型 ✗}：n\in\mathbb Z\ ✓\ \textbf{只区分分支 ✗，不给出 }\Re z=0\ ✓\ \text{（除非耦合到连续参数 ✓ —— 那时须审耦合是否【重引入】度量/序 ✓）}$$
$$\Longrightarrow\ \textbf{五类中：I 不构成反例 ✓；II–IV 皆 separation 变体 ✓；V 太粗 ✗✓}$$

## 3. 候选定理（✓ 您的 Transverse Obstruction Lemma ✓）

$$\boxed{\textbf{TOL（候选 ✓）}：\text{若 canonical 机制 }M\ \text{能从 }\Xi\ \text{结构证明 }Z(\Xi)\subseteq\operatorname{Fix}(\kappa)\ ✓，\text{且对每个 }z\notin\operatorname{Fix}(\kappa)\ \text{给出排除 ✓，}}$$
$$\qquad\qquad\text{则它【必然】产生横向非退化 obstruction}\ \mathcal O(z)\ ✓,\ \mathcal O(z)=0\Rightarrow z\in\operatorname{Fix}(\kappa)\ ✓}$$
$$\text{（}\textbf{TOL 本身近乎逻辑 ✓}：}\text{"排除 }z"\ \text{与"给出非零见证"在构造性数学下等价 ✓）}$$
$$\Longrightarrow\ ⭐\ \textbf{实质步【只在下一句 ✓】}：\ \boxed{\text{"任何 canonical obstruction 都可归约为【横向二次/分离型 ✗】？"}}$$
$$\qquad\text{—— 本轮【未证 ✗】，但【未找到反例 ✓】（§0③ ✓）}\ \Longrightarrow\ \textbf{这是当前最锐的可攻靶 ✓}$$

## 4. 边界与纪律（✓）

```
✅ **纸面 ✓（零数值 ✓）**；按您指定只做一件 ✓（纯代数恒等式型 ✓）
⚠️ **① 审计【非穷举 ✗】** —— "未找到"≠"不存在" ✓（宪法 §0 ✓）；我只覆盖【已知根定位理论 ✓】的判据形态 ✓
⚠️ **② "}i\mathbb R\ \text{不是代数集 ✗"是【精确事实 ✓】**（由 }z+\bar z=0\ \text{定义 ✓）；由此"无多项式解集等于 }i\mathbb R\ ✗\ \text{"✓ 为直接推论 ✓
⚠️ **③ 本轮【不声称】TOL 成立 ✗**，也不声称"separation 必然性"已证 ✓
⚠️ **④ 未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① ⭐ **决定性理由：}i\mathbb R\ \text{非代数集 ⟹ 纯代数路线【结构性必败 ✗】**；② **五类逐类裁决 ✓（I 非反例 ✓；II–IV separation ✓；V 太粗 ✗）**；
   ③ ⭐ **判死测试【未找到反例 ✓】⟹ separation 必然性方向【存活 ✓，首次具强形式雏形 ✓】**；④ **最锐可攻靶 ＝ "obstruction 是否必归约为横向二次型 ✗"**
```

## 5. 一句话总结（✓）

$$\boxed{\text{纯代数恒等式型【不能】产生一般性横向 obstruction ✓ —— 因 }i\mathbb R\ \text{非代数集 ✗；}\textbf{故 separation 必然性【未被推翻 ✓】，最锐靶转为"归约性"✗}}$$
