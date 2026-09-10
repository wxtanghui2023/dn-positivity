# D2 审计：**什么 Diophantine relation 会被算术"选中"？**（纯推导，未计算）

**依据**：唐先生 §17 的核心问题｜**约束**：不计算（明确禁止算 Markov/高维方程）；不输入 $1/2$；不构造模型｜**L2 未动**
**标注**：【推导】【引用】【已核验·本项目】

---

## §1 使 mutation 成为可能的条件：**二次性**【推导】
"根替换"（the other root）只在**对某变量二次**时无需选择 ⟹
$$\boxed{R\ \text{必须对每个被 mutation 的变量二次}}\qquad(\text{Vieta})$$
⟹ mutation 系统的可能来源 = **秩 2 的代数结构**（二次方程 = 秩-2 的 Cayley–Hamilton）✓

## §2 使 mutation **canonical** 的条件：Cayley–Hamilton【推导】
$$\text{2×2 矩阵 }M:\ \text{另一根}= \mathrm{tr}(M)I-M\quad\Longrightarrow\quad\textbf{Vieta 跳跃 = Cayley–Hamilton}$$
$$\boxed{\text{mutation 的 canonical 形式【就是】秩-2 的特征多项式根配对——这是【恒等式】，不是选择}}$$

## §3 于是 canonical 的来源只有两类【推导 + 引用】

> ⚠️ **收紧（唐先生 2026-09-10 21:18）**：本条是"**已识别 canonical 来源的压缩**"，**不是全称分类定理**。
> 作为全称命题还差一个证明（即：不存在其他 canonical 来源）。以下结论均在此边界内成立。
```
(a) 只要【环公理】本身（Z 的 + 与 ×）：
      T_a: x↦x+a 与 M_p: x↦px ⟹ T_aM_p−M_pT_a = 平移 a(1−p) ⟹ 生成 Aff(Z) ⟹ **可解** ✗（D1 §3 已核验同族）
(b) 2×2 矩阵 / 秩-2 序上的结构 ⟹ mutation 群是 SL_2(Z)、SL_2(Z[√n]) 或四元数序的单位群的子群
      ⟹ **算术格（arithmetic lattice）**，且 【非可解 ✓】（故 G1/G3 可以通过 ✓）
   【引用·经典】Markov: 与模环面（once-punctured torus）特征簇 / Farey 结构同源
   【引用·经典】Apollonian(Descartes): 与 Bianchi / 算术【thin】群相关（Graham–Lagarias–Mallows–Wilks–Yan）
```
$$\boxed{\text{两类 canonical 来源：环公理（可解）或 秩-2 算术群（非可解但【算术】）}}$$

## §4 这对 G5 的直接后果【推导 + 引用】
算术格 ⟹ 其解析理论是**自守的**：
```
· 四元数/GL_2 情形 ⟹ Jacquet–Langlands ⟹ 自守表示 ⟹ L-函数影子 ✗（§14）
· thin 情形 ⟹ Patterson–Sullivan ⟹ 临界指数 δ 与 **dynamical zeta** ✗（§14）
⟹ 与 ζ 的耦合只能经 L-值 或 dynamical zeta ⟹ **两者都已被 §14 判死** ✗
```
$$\boxed{\text{G5 在 canonical 来源上【失败】}}$$

## §5 G4 也没有 canonical 候选【推导】
```
此类系统里自然的临界参数是 Poincaré 指数 δ；其唯一的自然对偶是 s ↦ δ−s（resolvent/Patterson–Sullivan）
⟹ 强制的是【边界 δ】，【不是 1/2】；且 δ=1/2 在一般情况下不被强制 ✗
⟹ 若用 δ，则再次导入 dynamical-zeta 类 ✗
```

## §6 结论（对你 §17 的判死条件的回答）
$$\boxed{\text{canonicality}\Longrightarrow(\text{环公理}\Rightarrow\text{可解})\ \text{或}\ (\text{二次性}\Rightarrow\text{秩-2 算术群})\Longrightarrow\text{自守/dynamical 影子}\Longrightarrow\text{G5 失败}}$$
$$\boxed{\Longrightarrow\ \textbf{Markov / Pell / 二次型 / modular / Galois 确实"就是全部"（在已识别的 canonical 来源内）}\ \Longrightarrow\ \text{拟把整个 mutation 分支一并判死}}$$
**唯一逃生口（诚实标注，未证明）**：一个 **canonical 且【非算术】的 mutation 系统**（thin 非算术格）——
但**未发现任何 Diophantine-canonical 来源**；且上述论证暗示"canonical ⟹ 算术"（**是结构性论证，非定理**）✗

## §7 边界
```
· §1–§2 为推导；§3 的"秩-2 ⟹ 算术"对经典例子是【引用】（Markov/Apollonian 的算术性），非一般定理
· §4–§5 为结构性论证（非定理）
· 【未做】未计算（遵 §16）；未输入 1/2；未构造模型；未改 L2；未声称与 ζ 连接
· D1 §8 的边界同样适用：以上为"已识别 canonical 来源"内的结论，不写成全称不可能
```
