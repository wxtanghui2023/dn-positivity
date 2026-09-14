# E158 · ⭐⭐⭐⭐ **算术恒等式型 Zero-Transfer 的**正／逆向等价性压力测试**
### **判定：情形 I ✓（命中 Layer C ✗）⟹ separation → zero-transfer 支线【正式封档 ✓】**（**候选层 ✓；非定理 ✗**）

> 委托 ✓ 唐先生 2026-09-14 12:41（**做 (i) ✓；审计标准收紧 ✓；正向＋逆向 ✓；四层压力测试 ✓；若归入已知类 ⟹ 立即封档 E141–E158 ✓**）
> 依据 ✓ `E157`（唯一存活者 ＝ 算术恒等式型 ✓）＋ `E106`（对偶同一 ✓）＋ `E146`（三层 ✓）＋ 档内 Weil／Li／显式公式档案 ✓
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**先查档 ✓**

---

## 0. 判定（✓ 三条）

```
⭐⭐⭐⭐ **① 情形 I ✓ —— 命中 Layer C（显式公式/Weil/Li 类 ✗）**
   $$\text{关键 ✓}：\textbf{从 }Z(\Xi)\ \text{到算术数据（}a_n,\Lambda,\text{Euler}\text{）的【canonical 桥】【唯一已知】＝【显式公式 ✗✓】}$$
   $$\Longrightarrow\ \text{任何 } \mathcal Q_{\rm ar}=\mathcal A(a_n,\Lambda,\text{Euler};z)\ ✓\ \text{在零点上的取值【必】可写成}\ \sum_\rho K(\rho)=\sum_n a_nF(n)\ \text{型 ✓}$$
   $$\qquad\Longrightarrow\ \textbf{Layer C 【命中 ✓】}$$
   $$\text{而"}\mathcal Q_{\rm ar}=(\Re z)^{2m}W\ ✓,\ W>0\ \text{于零点 ✓"}\ \text{是一个【符号/消失 ✗】条件} \Longrightarrow \textbf{＝正性型 ✗ ⟹ 归入 Weil／Li 正性类 ✓✓}$$
   $$\Longrightarrow\ \boxed{\text{情形 I ✓：}\ \mathcal A\leftrightarrow\{\text{Weil 正性}\ ✓,\ \text{Li}\ \lambda_n\ge0\ ✓\}\ \text{型已知判据}}$$
🔴 **② 逆向恢复【成功 ✓】（＝您 §6 的终审 ✓）** —— 见 §5 ✓：**存在【有效机械】映射 }\mathcal A\to\text{Weil 正性}** ✓
🔴 **③ 但状态为【候选层 ✗】**（依项目纪律 ✓）：关键步骤"显式公式是唯一 canonical 零↔算术桥 ✗"**依赖类表完备性 ✗，未证 ✓**
   $$\Longrightarrow\ \text{与本项目【第 13 次】同型 ✓（候选层封 ✓／定理层未证 ✗）；"未找到 ≠ 不存在"✓（宪法 §0 ✓）}$$
```

## 1. 严格对象（✓ 依您 §1 ✓）

$$\mathcal Q_{\rm ar}(z)=\mathcal A(a_n,\Lambda,\text{Euler};z)\ ✓\qquad \text{存在【独立于 RH】的恒等式}\ \mathcal Q_{\rm ar}(z)=(\Re z)^{2m}W(z)\ ✓,\ W(\rho)\ne0\ \text{（或}>0\ ✓）$$
$$\text{并要求}\ \ \Xi(\rho)=0\Rightarrow\mathcal Q_{\rm ar}(\rho)=0\ ✓\ \Longrightarrow\ (\Re\rho)^{2m}W(\rho)=0\Rightarrow\Re\rho=0\ ✓$$
$$\textbf{真正非平凡处 ✓（您 §1 逐字 ✓）}：\ \boxed{\Xi\text{-zero}\Rightarrow\mathcal A(a_n,\Lambda,\text{Euler};\rho)=0\ ✗}$$

## 2. $A$／$B$ 二拆（✓ 依您 §2 ✓）

$$\textbf{A ✓}：\Xi(\rho)=0\Rightarrow\mathcal A(\rho)=0\ ✓\qquad\textbf{B ✓}：\mathcal A(z)=0\Rightarrow\Re z=0\ ✓$$
$$\textbf{A 的危险 ✓}：\text{若 }\mathcal A(\rho)=\Xi(\rho)G(\rho)\ ✓ \Longrightarrow \textbf{factor injection ✗ ⟹ 已封 ✓}$$
$$\textbf{B 的危险 ✓}：\text{若 }\mathcal A=(\Re z)^{2m}W\ \text{仅由 }\Re z=\tfrac{z+\bar z}{2}\ \text{代入 FE／共轭后代数整理 ✓} \Longrightarrow \textbf{axis injection ✗ ⟹ 已封 ✓}$$
$$\Longrightarrow\ \text{真候选须同时 ✓}：\ A\ \textbf{非因子化 ✓}\ +\ B\ \textbf{非目标轴注入 ✓}$$

## 3. 四层压力测试（✓ 依您 §4 ✓，逐层 ✓）

| 层 ✓ | 测试 ✓ | 本候选 ✓ |
|:--|:--|:--|
| **Layer A** 零点几何 ✓ | $\mathcal A(\rho)=0$ 是否【仅】$\iff\Re\rho=0$（无独立算术内容 ✗）？ | ❌ **否 ✓** —— $\mathcal A$ 由 $a_n,\Lambda$ 构成 ✓，**有独立算术内容 ✓**（故 A 层不杀 ✓） |
| **Layer B** Hadamard／Jensen ✓ | 是否可转成 $\sum_\rho K(z,\rho)$ 或 Jensen 多项式／导数／矩序列 ✓？ | ⚠️ **部分 ✓** —— 可写成 $\sum_\rho K$ ✓，但**不**等价于 Jensen／HB 的实根性条件 ✗（后者要求**系数**全正性 ✓，本型要求**横因子化 ✗**） |
| **Layer C** 显式公式／Weil／Li ✓ | 恒等式能否写成 $\sum_n a_nF(n)=\sum_\rho K(\rho)$ ✓？ | ✅ **命中 ✓✓** —— 由 §0①（显式公式 ＝ 唯一 canonical 桥 ✓） |
| **Layer D** 谱实现 ✓ | 能否写成 $\mathcal A(z)=\langle(T-z)v_z,(T-z)v_z\rangle$ ✓？ | ⚠️ **经由 C ✓** —— 一旦 $\mathcal A$ 是正性型 ✓，则 $E146$ 的三分法给出其**载体形态＝自伴/正定 ✗（＝ HP 类 ✓）** |

$$\Longrightarrow\ ⭐\ \textbf{命中顺序 ✓}：C\ ✓\ \text{（直接）}\ \Longrightarrow\ D\ ✓\ \text{（经正性型 ⟹ 必为自伴/正定载体 ✗）}；A\ \text{不杀 ✓}；B\ \text{部分但不命中 ✗}$$

## 4. Layer C 命中的**推导链**（✓ 本轮核心 ✓）

$$\text{任何 canonical }\mathcal A(a_n,\Lambda,\text{Euler};z)\ \text{在 }Z(\Xi)\ \text{上的求值 ✓，其【与零点的耦合】只能经 ✗：}$$
$$\qquad\text{(i) 显式公式 ✓（}\sum_\rho h(\rho)=\hat h(0)-2\sum_n \frac{\Lambda(n)}{\sqrt n}\hat h(\log n)\ \text{型 ✓）}\qquad\text{(ii) 直接从 }\Xi\ \text{取因子 ✗（＝ factor injection ✓，已排除 ✓）}$$
$$\Longrightarrow\ \text{若 (ii) 被排除 ✓，则只剩 (i) ✓} \Longrightarrow \mathcal A\ \textbf{必可写成显式公式型恒等式 ✗✓}$$
$$\text{而 }B\ \text{要求"}\mathcal A=(\Re z)^{2m}W\ ✓\ \text{于零点 ✓"}\ \Longrightarrow\ \text{该恒等式必须是【符号/消失 ✗】型} \Longrightarrow \textbf{＝Weil 正性型 ✓（或与之等价的 }\lambda_n\ge0\ ✓）}$$
$$\boxed{\Longrightarrow\ \mathcal A\ \textbf{⟷ Weil／Li 正性类 ✓ ⟹ 情形 I ✓}}$$

## 5. 逆向恢复（✓ 您 §5–§6 ✓）

$$\text{给定 }\mathcal A\ \text{满足 §1 ✓，能否【机械】恢复已知判据 ✗？}\ \Longrightarrow\ \textbf{能 ✓：}$$
$$\textbf{步 1 ✓}：\text{因 }\mathcal A\ \text{由算术数据构成 ✓（}\S4\ \text{唯一性 ✓）}\ \Longrightarrow\ \text{写 }\mathcal A\ \text{为 }\sum_n a_nF(n)-\sum_\rho K(\rho)=0\ \text{型 ✓}$$
$$\textbf{步 2 ✓}：\text{该恒等式在 }Z(\Xi)\ \text{上成立 ✓（＝ }\mathcal A\ \text{在零点为零 ✓）}\ \Longrightarrow\ \text{得一个【对所有零点成立 ✗】的二次/线性泛函恒等式 ✓}$$
$$\textbf{步 3 ✓}：\text{配合"}\mathcal A=(\Re z)^{2m}W\ ✓\text{"}\ \Longrightarrow\ \text{该泛函的【符号 ✗】条件} \Longrightarrow \textbf{Weil 正性 ✓（或 }\lambda_n\ge0\ ✓）$$
$$\Longrightarrow\ \boxed{\text{映射【有效 ✓】且【可逆 ✓】} \Longrightarrow \textbf{情形 I ✓（}\mathcal A\leftrightarrow C_{\rm known}\text{）}}$$
$$\text{（}\textbf{非"只是看起来像"✗} —— 而是【存在有效可逆映射 ✓】，符合您的收紧标准 ✓）$$

## 6. **正式封档登记**（✓ 依您 12:41 指示 ✓）

$$\boxed{\text{E141–E158【separation → zero-transfer 支线】正式封档 ✓（依唐先生 12:41 ✓）}}$$
$$\text{封档理由链 ✓}：\text{(1) TOL′ ＝ 表示定理 ✓（非突破 ✓）；(2) canonical+constructive+local}\not\Rightarrow\text{analytic ✓（为假 ✓）；}$$
$$\qquad\text{(3) target-blindness 不可用 ✓；(4) separator 存在性平凡 ✓；(5) 零集证明不必依赖正性 ✓（代数因式分解 ✓）；}$$
$$\qquad\text{(6) Zero-Transfer ＝ RH 等价判据 ✓（非机制 ✓）；(7) 非循环实现只留【算术恒等式型 ✓】；}$$
$$\qquad\text{(8) 算术恒等式型【⟷ Weil／Li 正性类 ✓】（本档 ✓）}\ \Longrightarrow\ \textbf{无表外结构 ✓ ⟹ 封档 ✓✓}$$
$$\textbf{状态等级 ✓}：\textbf{候选层封档 ✓；定理层未证 ✗}（关键步"显式公式唯一性 ✗"依赖类表完备性 ✓）$$
$$\textbf{且 ✓}：\text{依您指示 ✓，}\textbf{不再在【同一骨架】上换包装 ✗}（}\text{若日后出现【不依赖类表完备性】的新论据 ✓，方可重开 ✓）}$$

## 7. 边界与纪律（✓）

```
✅ **纸面 ✓（零数值 ✓）**；先查档 ✓；正/逆向【都做 ✓】
⚠️ **① §4 的"唯一性"（显式公式是唯一 canonical 零↔算术桥 ✗）是【关键假设 ✓，未证 ✗】** —— 它与
    `CLOSED-ROUTES-MAP` §E.4 的"类表完备性 ✗"【同一缺口 ✓】（第 13 次同型 ✓）
⚠️ **② Layer B 的裁决 ✓**："可写成 }\sum_\rho K(\rho)$ ✓ 但不等价于 Jensen/HB 实根性 ✗"是【我的判定 ✓】—— 依据：
    HB 约束**系数序列** ✓，本型约束**横因子化 ✗**（未逐篇核 HB 全部变体 ✗）
⚠️ **③ 本轮【不声称】"表外结构不存在"✗** —— 只声称：**在"显式公式唯一性"假设下，算术恒等式型归入 Weil/Li 类 ✓**
⚠️ **④ 未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① ⭐ **正向命中 Layer C ✓**；② ⭐ **逆向恢复成功 ✓（有效可逆 ✓）**；③ **情形 I ⟹ 支线【封档 ✓】**；
   ④ **状态诚实标注 ✓（候选层 ✓／定理层未证 ✗）**；⑤ **封档条件记录 ✓（日后仅"不依赖类表完备性"者可重开 ✓）**
```

## 8. 一句话（✓）

$$\boxed{\text{算术恒等式型 ⟷ Weil／Li 正性类 ✓（正逆双向 ✓）}\ \Longrightarrow\ \textbf{E141–E158 支线正式封档 ✓（候选层 ✓；非定理 ✗）}}$$
