# E109 · ⭐⭐⭐ **(甲) 攻击面：char-0 共同载体的【最小模板】＋ 传输的机制性障碍** ✓

> 委托 ✓ 唐先生 22:20（"甲，这是我一再需要你提供协助的地方" ✓ —— 即 (甲) 发明新原理／构造 char-0 共同载体 ✓）
> 执行 ✓ 小灵｜方式 ✓ **不做无向搜索** ✗，而是**① 把 char p 机制拆到最小要素 ✓ ② 尝试传输 ✓ ③ 给出攻击面与判据 ✓**
> 纪律 ✓ 未用 RH ✓；未跑 Lean ✓；**本轮无计算 ✓**；⚠️ 全文标为【推导／机制】✗ **非定理** ✓

---

## 0. 结论（✓ 四条 ✓）

```
⭐⭐ **① char p 机制的最小要素只有【两条】** ✓（比项目现有表述更简 ✓）：
   $$Q\succ0\ \text{（正定）}\quad\text{＋}\quad F^{*}QF=qQ\ \text{（similitude）}\ \Longrightarrow\ \boxed{|\alpha|^{2}=q}$$
   （一行 ✓：$q\langle Qv,v\rangle=\langle QFv,Fv\rangle=|\alpha|^{2}\langle Qv,v\rangle$，$Qv,v\rangle>0$ ✓）
   ⟹ **不需要**先有上同调／Poincaré 对偶／Weil 配对 ✗ —— **它们只是【实现】$Q$ 与 $F$ 的方式** ✓✓
⭐⭐ **② 传输的机制性障碍（本轮核心 ✓）**：char 0 的"$F$"只有两种自然形态，**各撞一面墙** ✗：
   $$\text{(a)}\ \text{函数方程}\ \rho\leftrightarrow1-\bar\rho\ \text{是【反射】✗（阶 2、无乘子 ⟹ 只强制 }\varepsilon\text{ 的对称，不强制 }\varepsilon=0\ ✗）}$$
   $$\text{(b)}\ \text{archimedean Frobenius ＝【连续流】}U(t)\ \text{（Connes 缩放位点／Deninger flow ✓）是真缩放 ✓}$$
   $$\text{但：}U(t)^{*}QU(t)=e^{\lambda t}Q\ \text{与【特征向量】}\boxed{\text{不相容}}\ ✗$$
   $$\text{证 ✓：}U(t)v=e^{i\mu t}v\ \Longrightarrow\ Q(v,v)=Q(U(t)v,U(t)v)=e^{\lambda t}Q(v,v)\ \Longrightarrow\ \lambda=0\ \text{✗}$$
   $$\Longrightarrow\ \textbf{有真实乘子的 similitude ⟹ 【无特征向量】⟹ 无离散谱} ✗\checkmark$$
⭐⭐ **③ 于是得到"无共同载体"的【机制表述】✓✓**：
   $$\boxed{\text{取【局部单个算子】（Hecke ✓）⟹ similitude 成立 ✓ 但只有 Euler 因子数据 ✗（箱 4 ✗）}\quad\text{或}\quad\text{取【连续流】⟹ 看得到全局 ✓ 但无可离散谱 ✗（箱 6 ✗）}}$$
   ⟹ **这正是项目"正性与零点谱数据无共同载体"的【一行机制式证明草图】** ✓✓（**解释了为何箱 4 与箱 6 是唯二汇点** ✓）
⭐ **④ 攻击面（✓ 具体 ✓）**：共同载体必须**同时避开两端** ✗ —— 即
   $$\boxed{\text{一个 canonical 【全局】算子：既非【局部单个算子】（非 $p$-分解 ✗）、又非【连续流】（非常规群作用）✗，且带【正定 similitude 形式】✓}}$$
   —— **这是 (甲) 的唯一精确靶面** ✓✓
```

## 1. 拆解：char p 的两要素（✓ 与项目表述的对照 ✓）

| 项目现有表述（AOB3 ✓）| 本模板 ✓ |
|:--|:--|
| "有 canonical 生成元 ＋ 需 canonical polarization $Q$ 使 $\Phi^{\dagger}Q\Phi=NQ$" ✓ | **同一件事 ✓**，但**去掉**上同调/相交形式/Weil 配对的包装 ✓ |
| 结论：char 0 缺 polarization ✗ | **补上**【为何缺】的机制 ✓：见 §2 |

$$\text{关键 ✓}：\text{只要 }(\mathrm{i})\ Q\succ0\ \text{✓}\ \text{（正定，非仅"非退化" ✗）},\quad (\mathrm{ii})\ F^{*}QF=qQ\ \text{✓}\ \text{（乘子为【实正数】✓）}$$
$$\Longrightarrow\ \text{【全部】特征值 }|\alpha|=\sqrt q\ \text{✓ —— 这就是纯度（purity ✓）的【全部内容】}$$

## 2. 传输：两条自然路径各撞一墙（✓ 本轮核心 ✓）

### (a) 函数方程是**反射**，不是缩放 ✗

$$\rho=\tfrac12+\varepsilon+i\gamma\ \xrightarrow{\ \text{FE}\ }\ 1-\rho=\tfrac12-\varepsilon-i\gamma\ \Longrightarrow\ \varepsilon\mapsto-\varepsilon\ \checkmark$$
$$\text{它强制的是【}\varepsilon\text{ 的对称】✗，\textbf{不是 }\varepsilon=0}\ ✗$$
$$\text{而 char p 的 }q/\alpha\text{ 强制的是}\mathbf{模长}\ ✗\ \text{—— 二者【类型不同】（反射 vs 缩放 ✓）}$$
$$\Longrightarrow\ \text{光有 FE，得不出 }|\alpha|=\sqrt q\ \text{的对应物（即 }\Re\rho=\tfrac12\text{）}\ ✗\checkmark$$
（⭐ 这解释了为何"函数方程 ＋ 共轭"给出的轨道 $\{\rho,1-\rho,\bar\rho,1-\bar\rho\}$ **不退化** ✓
   —— 与 `final-structural-conclusion` 的"缺重数强制"✓ **完全一致** ✓）

### (b) 连续流：有真缩放 ✓，但与离散谱**不相容** ✗

$$\text{archimedean Frobenius ＝ 缩放作用 }U(t)\ \text{（}\mathbb R_+\ \text{流 ✓；Connes 缩放位点 ✓／Deninger flow ✓）}$$
$$\text{若 }U(t)^{*}QU(t)=e^{\lambda t}Q\ \text{（}Q\succ0\text{ ✓，}\lambda\ne0\text{ ✓）}\ \text{且 }U(t)v=e^{i\mu t}v\ \text{（}\text{特征向量 ✓）}$$
$$\Longrightarrow\ Q(v,v)=Q(U(t)v,U(t)v)=\bigl(U(t)^{*}QU(t)\bigr)(v,v)=e^{\lambda t}Q(v,v)\ \Longrightarrow\ e^{\lambda t}=1\ \Longrightarrow\ \boxed{\lambda=0}\ ✗$$
$$\Longrightarrow\ \textbf{故【有真实乘子的 similitude】与【特征向量】不可共存} ✗\ \Longrightarrow\ \textbf{连续流路线【必然】放弃离散谱} ✗\checkmark$$

## 3. ⭐⭐ 于是："无共同载体"的机制表述（✓ $2\times2$ 二择一 ✓）

| 选择 | similitue／正性 | 谱／零点 | 归宿 |
|:--|:--|:--|:--|
| **局部单个算子**（Hecke $\mathbb T_p$ ✓、mod-$p$ Frobenius ✓） | ✓ 成立（Petersson 正定 ＋ Deligne 界 ✓；purity ✓） | ✗ **只有 Euler 因子数据**（$\sigma>1$ 窗口 ✗） | **箱 4** ✗ |
| **连续流**（archimedean 缩放 ✓） | ✗ **与离散谱不相容**（§2(b) ✓） | ✓ 看得到全局零点 ✓ | **箱 6** ✗ |

$$\boxed{\text{两端各得一半 —— 这正是"char 0 中正性与零点谱数据无共同载体"的【机制式证明草图】}\ \checkmark}$$
$$\text{并且它【解释了】为何箱 4（L-值/Euler）与箱 6（谱/HP）是唯二【汇点】✓✓（项目地图的独立印证 ✓）}$$

## 4. ⭐ 攻击面（✓ 具体、可判死活 ✓）

$$\boxed{\text{共同载体 ＝ canonical 【全局】算子，同时：}\begin{cases}\text{非【局部单个算子】✗（即非 }p\text{-分解／非 Euler 因子型 ✓）}\\[1mm]\text{非【连续流】✗（非常规一参数群作用 ✓）}\\[1mm]\text{带【正定 similitude 形式】}Q\succ0,\ F^{*}QF=qQ\ \checkmark\end{cases}}$$

**需要核对的候选形态** ✓（逐一 ✓）：
| 候选形态 | 是否避开两端 | 状态 |
|:--|:--|:--|
| 非交换 crossed product（C*-代数 ✓） | ✗ 含连续流 | 箱 6 ✗ |
| adelic 动力学 ✓ | ✗ 连续 | 箱 6／箱 3 ✗ |
| Hecke 代数的**非标量乘子**扩张 ✓ | ? | ⭐ **未审计** ✓（**攻击面上的第一个点** ✓） |
| **global 算子的"乘积"**（$\prod_p\mathbb T_p$ ✓） | ✗ 无穷积**不是算子**（无谱 ✗） | ✗ |
| **算术算子（如平移/卷积在 $\mathbb Z$ 上）** ✓ | ? | ⭐ **未审计** ✓（**第二个点** ✓） |
| 范畴／模型论层（非算子 ✓） | ✗ 类 VI ✗（可定义性 ⟹ 最终周期 ⟹ 回 congruence ✓） | ✗ |

## 5. 判据（✓ 可证伪 ✓）

```
【判据 D1 ✓】任何候选若其"$F$"是常规一参数群 ✓ ⟹ **直接关闭** ✗（§2(b) 的论证适用 ✓）
【判据 D2 ✓】任何候选若其"$F$"按素数分解（$F=\prod_p F_p$ ✓） ⟹ **直接关闭** ✗（只有 Euler 因子数据 ✓）
【判据 D3 ✓】任何候选若其"$Q$"只是**非退化**而非**正定** ⟹ 无效 ✗（§1 的一行证明需要 $Q\succ0$ ✓）
【判据 D4 ✓】**唯一存活形状 ✓**：$F$ **不分解于素数** ＋ **非连续群** ＋ $Q\succ0$ 且 $F^{*}QF=qQ$ ✓
```

## 6. 边界与纪律（✓ 诚实 ✓）

```
⚠️ **全文为【推导／机制】** ✗ —— §2(b) 的一行论证是**严格的局部事实** ✓，但"char 0 的 $F$ 只有两种自然形态"是**分类陈述** ✗（**未证穷尽** ✓）
⚠️ **未宣布任何证明** ✗；**未宣布 Berry–Keating 正确** ✗；**未宣布共同载体存在或不存在** ✗
✅ **本轮相对项目的增益 ✓**：① **把 char p 机制拆到两要素** ✓（$Q\succ0$ ＋ similitude ✓ —— 去掉上同调包装 ✓）；
   ② **给出传输障碍的【一行论证】** ✓（连续流的 similitude 与特征向量不相容 ✓ —— 这是我未在既有档案中检索到的形态 ✓）；
   ③ **把"无共同载体"重述为 $2\times2$ 二择一** ✓，并**独立解释了箱 4／箱 6 为何是唯二汇点** ✓；
   ④ **给出四个判据 ＋ 两个未审计的攻击点** ✓（Hecke 非标量乘子扩张 ✓／$\mathbb Z$ 上算术算子 ✓）
⚠️ **待核 ✓**：§2(b) 的"连续流必然放弃离散谱"是否已在既有档案（`arith-frob-flow-final`／`connes-2026-full-audit`／`hp-audit-final` ✓）中记过 ✗ —— **下一步应先核这三份，再动手** ✓
```
