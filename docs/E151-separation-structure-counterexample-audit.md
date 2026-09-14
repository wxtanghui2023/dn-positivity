# E151 · ⭐⭐⭐⭐ **"轴定位 ⟹ 必须引入 separation structure"反例审计** ✓
### **未找到反例 ✗；且每个【真能锁定谱轴】的机制【都调用了某种配对/定/序结构 ✓（＝ separation ✓）】**

> 委托 ✓ 唐先生 2026-09-14 12:20（**改造强形式：轴定位 ⟹ separation structure ✓；先做反例穷举审计 ✓；警告"几何/动力/辛/守恒/PT/拓扑可能不需正性"✗**）
> 依据 ✓ `E150`（FE 提供中心 ✓）＋ `L1` 审计（五族 ✓）＋ `C-BC-D3`（KMS/模 ✓）＋ `POS1–3` ✓
> 执行 ✓ 小灵｜**纸面审计 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓；未跑 Lean ✓

---

## 0. 判定（✓ 三条）

```
⭐⭐⭐⭐ **① 反例【未找到 ✗】—— 且规律【反直觉地一致 ✓】**
   $$\boxed{\text{凡【真能】把谱锁定到【一条轴】的机制 ✓，}\textbf{都调用了某种配对/定/序结构 ✗（＝ separation ✓）}}$$
   $$\boxed{\text{凡【不调用】任何此类结构的机制 ✓，}\textbf{只能给出【对称性】✗，给不出【轴定位】✗✓}}$$
⭐⭐⭐ **② 一个【决定性的解读 ✓】**：**"正交/度量"本身就是 separation ✓**
   $$\text{您的关键问题 ✓}：\text{"一个算子凭什么知道 }i\mathbb R\ \text{是正确的谱轴？"✗}$$
   $$\text{最简答案 ✓}：T^*=-T\ \Longrightarrow\ \mathrm{Spec}(T)\subset i\mathbb R\ \textbf{✓✓（不需正性 ✗！）}$$
   $$\text{但 ✗}：\text{它【用的是】}\langle\cdot,\cdot\rangle\ \textbf{（内积 ✓＝度量 ✓＝ separation ✓）}\ \Longrightarrow\ \textbf{不是反例 ✓，而是【最纯的例证 ✓✓】}$$
   $$\text{（即 ✗：}\text{"反自伴"看似"不用正性"✓，实则【用了内积】✗ —— }\textbf{而内积正是 separation structure ✓}）$$
⭐ **③ 反例风险【未被排除 ✗】**：\text{"separation structure"【未形式化 ✗】（您的提案 ✓）；我的枚举【非穷举 ✗】}
```

## 1. 反例审计表（✓ 逐条 ✓）

| 机制 ✓ | 能锁【一条轴】✗？ | 用的是什么结构 ✓ |
|:--|:--|:--|
| **反自伴 $T^*=-T$** ✓ | ✅ **能**（$\subset i\mathbb R$ ✓） | **内积** ✓（度量 ✗）⟹ separation ✓ |
| **Hamiltonian ＋ 定 Hessian** ✓ | ✅ **能**（纯虚 ✓） | **定性** ✓（＝正定 ✗）⟹ separation ✓ |
| **辛结构【单独 ✓】** | ❌ **不能 ✗** | 给出 **$\lambda\leftrightarrow-\lambda$ 且 $\lambda\leftrightarrow\bar\lambda$** ✓（**四重对称 ✓，反而【更松 ✗】**） |
| **PT 对称** ✓ | ❌ **不能 ✗** | 给"实 或 共轭对"二择一 ✓；**可破缺 ✗** |
| **Krein/Pontryagin** ✓ | ⚠️ **几乎 ✗** | 实谱**至多有限例外** ✓（**非精确锁定 ✗**）；要"线"须**定子空间 ✓＝正定 ✗** |
| **$\mathcal J$-自伴** ✓ | ⚠️ **区域 ✗** | 关于实轴/带状 ✓（$L1$ 审计 ✓） |
| **数值域／伪谱** ✓ | ❌ **不能 ✗** | **区域** ✓（$L1$ ✓） |
| **KMS／Tomita（}C\text{-}BC\text{-}D3$）** ✓ | ⚠️ **只给实尺度 ✗** | $\Delta=S^*S\Longrightarrow\mathrm{Spec}(\Delta)\subset(0,\infty)$ ✓ —— **它给"实"✗，不给"虚"✓**；其正性＝正性 ✓ |
| **可积/反射正性** ✓ | ⚠️ **实谱 ✓** | **反射正性 ✓＝正性 ✗** |
| **拓扑/K-理论** ✓ | ❌ **不能 ✗** | 输出**整数** ✓ ⟹ **比"点"更粗 ✗** |
| **纯代数谱（无度量 ✗）** ✓ | ❌ **不能 ✗** | 无结构可证定位 ✓；FE 只给 $z\leftrightarrow-z$ ✓ ⟹ **$z^2-1$ 与 $z^2+1$ 不可区分 ✓✓（您的例子 ✓）** |

$$\Longrightarrow\ ⭐\ \textbf{表读法 ✓}：\text{"能锁轴者【皆调用】配对/定/序结构 ✓；不能锁轴者【皆缺之】✗"}\ —— \textbf{零反例 ✓✓}$$

## 2. 为什么"对称性"与"轴定位"是【两个层次 ✓】（✓ 您的观察被证实 ✓）

$$\text{FE ⟹ }z\mapsto-z\ \text{equivariance ✓} \Longrightarrow \text{只给 }F(-z)=\pm F(z)\ ✓\ \Longrightarrow\ \textbf{无法排除实轴根 ✗}$$
$$z^2-1\ ✓\ \text{与}\ z^2+1\ ✓\ \text{满足【同一】FE 型对称 ✓，根分别在 }\mathbb R\ \text{与}\ i\mathbb R\ ✓ \Longrightarrow \boxed{z\mapsto-z\ \not\Rightarrow\ z\in i\mathbb R\ ✓✓}$$
$$\text{而【分离】这两者所需的额外输入 ✓，恰好就是 separation structure ✓ —— 在本项目里对应：}\textbf{正性/序/度量 ✗}$$

## 3. 对本项目定稿规格的映射（✓）

$$\text{规格 }A+B+C_{\rm int}\ \text{中 ✓}：A+B\ \text{给【对称性/编码 ✓】（}FE\ \text{侧 ✓）；}\ \textbf{轴定位的责任在 }C_{\rm int}\ ✗$$
$$\Longrightarrow\ \textbf{改造后的强形式在本项目的形态 ✓}：\ \boxed{C_{\rm int}\ \text{若成立 ✓，则【必】引入 separation structure ✗}$$
$$\Longrightarrow\ \text{而 separation structure 的六类候选 ✓（您的分类 ✓）：正形式 ✓／Hilbert-Krein 度量 ✓／序结构 ✓／酉性-压缩 ✓／实根核 ✓／其它 ✗}$$

## 4. 边界与纪律（✓）

```
✅ **纸面 ✓（零数值 ✓）**；先查档 ✓（L1 ✓；C-BC-D3 ✓；POS1–3 ✓）
⚠️ **① 表【非穷举 ✗】** —— 我的枚举基于已知谱论 ✓；**未证明"六类分离结构穷尽"✗**（＝您指出的形式化缺口 ✓）
⚠️ **② "separation structure"【未形式化 ✗】** —— 本档只用其【直觉义 ✓】（"引入额外配对/定/序结构 ✓"）；**形式定义待立 ✗**
⚠️ **③ 唯一【未排除】的反例形态 ⚠️**：\text{"用【代数恒等式】锁定谱 ✗，且其定位证明【非构造性 ✓】"} ——
    $$\text{若能存在 ✓，则是【第四型机制 ✗】}\ \text{—— 本档【未找到 ✓】，但也【未排除 ✗】}$$
⚠️ **④ 本轮【不声称】改造后的强形式成立 ✗**
⚠️ **未用 RH** ✓；**未跑 Lean** ✓
⭐ **净产出 ✓**：① ⭐ **反例未找到 ✓，且规律一致：锁轴 ⟺ 调用 separation ✓**；② ⭐ **决定性解读：}T^*=-T\ \text{【不是反例 ✗】—— 它用的是内积 ✓**；
   ③ **对称性 ⟺ 轴定位两层次 ✓（}z^2\pm1\ \text{例 ✓）**；④ **映射到定稿规格：轴定位责任在 }C_{\rm int}\ ✗**
```

## 5. 下一步（✓ 依您"先反例穷举和形式化，再决定生死"✓）

$$\text{① 形式化 separation structure ✗（本方向的【真正入口 ✓】）；② 补全反例枚举（尤其"代数恒等式型 ✗"✓）；③ 若二者都过 ⟹ 强形式成定理 ✓✓}$$
