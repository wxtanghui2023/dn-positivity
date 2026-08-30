# Theorem-Level Exposition: O5 and C3（最严格版本）

> 目标：把 O5（谱装配）和 C3（分布配对）从"候选"升级为
> **单向、逐层、每步有引理保证**的定理级表述——专门抵御
> "Q'_RH 是为了让差等于 P_γ 而构造"和"Parseval 一步跳跃"两类攻击。
> 状态：2026-08-30 深夜——INVALID-first 外部攻击前的正式版本。

---

## Part A — C3：分布配对的三个层次

### 层次 1：真正定义的对象

**定义 C3.1（逐项配对）.** 对每个零点 ρ = ½+δ_ρ+iγ_ρ，
$$w_H(\gamma_\rho,\delta_\rho) = \int_{\mathbb R}
\widehat K_{\delta_\rho}^{\mathrm{nat}}(u)\,\widehat H_0(u)\,
e^{-2\pi i u\gamma_\rho}\,du,$$
其中 $\widehat K_\delta^{\mathrm{nat}}(u)=2\pi^2|u|e^{-2\pi\delta|u|}$，
$\widehat H_0(u)=e^{-2\pi|u|}[\tfrac{1}{4\pi|u|}+\tfrac12]$，
乘积 $\widehat K_\delta^{\mathrm{nat}}\widehat H_0 =
\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}\in L^1$
（$a=1+\delta$）。积分是**良定义 Lebesgue 积分**（被积函数在 $L^1$）。

**引理 C3.2（解析求值）.** $w_H(\gamma,\delta)=
\dfrac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2}$，$a=1+\delta$。
*证明*：两个标准积分
$F^{-1}[e^{-2\pi a|u|}](\gamma)=\tfrac1\pi\tfrac{a}{a^2+\gamma^2}$、
$F^{-1}[|u|e^{-2\pi a|u|}](\gamma)=\tfrac{a^2-\gamma^2}{2\pi^2(a^2+\gamma^2)^2}$，
直接代入。

**定义 C3.3（逐项泛函）.** $Q:=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho)$；
$Q'_{\mathrm{RH}}:=-\sum_\rho m_\rho w_H(\gamma_\rho,0)$
（投影：$\delta_\rho\mapsto 0$，保持 $\gamma_\rho,m_\rho$；**无 RH 假设**）。

### 层次 2：辅助计算表达式（不用于定义）

- $\langle\log|\xi|,H_0''\rangle$ 是**分部积分的形式表达式**——不是定义的配对。
  事实上 $\log|\xi(\tfrac12+it)|\sim O(t\log t)$、$H_0''\sim 1/(2\pi t^2)$，
  乘积 $\sim \log t/t$ 不可积——**该表达式发散，不承载定义**。
- Parseval 恒等式在 C3.1 中作为**求值工具**出现（被积函数 $L^1$，
  非形式 Fourier 操作）。

### 层次 3：交换——逐条引理保证

**引理 C3.4（绝对可和）.** $\sum_\rho m_\rho|w_H(\gamma_\rho,\delta_\rho)|<\infty$
和 $\sum_\rho m_\rho|w_H(\gamma_\rho,0)|<\infty$。
*证明*：$|w_H|\sim|\delta|/(2\gamma^2)$（$\gamma\to\infty$），
$|w_H(\gamma,0)|=1/(1+\gamma^2)^2$；由
$\sum_\rho m_\rho\gamma_\rho^{-2}<\infty$（$N(T)=O(T\log T)$）。

**引理 C3.5（轨道重排合法）.** 引理 C3.4 的绝对收敛保证按函数方程轨道
（$\rho\sim 1-\bar\rho$）重排 $Q$、$Q'_{\mathrm{RH}}$ 及逐项差合法。

---

## Part B — O5：谱装配（单向展示——从定义到恒等式）

**引理 O5.1（轨道分组）.** 按轨道 $\rho\sim 1-\bar\rho$
（同 $\gamma$、反 $\delta$）分组：
$$Q=-\sum_{\rho/\sim} m_\rho\bigl[w_H(\gamma,\delta_\rho)+w_H(\gamma,-\delta_\rho)\bigr],$$
对离轴轨道；在线零点（$\delta=0$，自配对）贡献单个 $w_H(\gamma,0)$。

**引理 O5.2（逐项差）.** 由 C3.3 与 O5.1，
$$Q-Q'_{\mathrm{RH}}=-\sum_\rho m_\rho\bigl[w_H(\gamma_\rho,\delta_\rho)-w_H(\gamma_\rho,0)\bigr].$$

**引理 O5.3（成对量出现）.** 对离轴轨道，
$w_H(\gamma,\delta)+w_H(\gamma,-\delta)-2w_H(\gamma,0)=-P_\gamma(\delta)$，
其中 $P_\gamma(\delta):=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)$；
在线零点贡献 $w_H(\gamma,0)-w_H(\gamma,0)=0$。故
$$Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho).$$

> **单向性声明**：$Q$、$Q'_{\mathrm{RH}}$ 的定义（C3.3）**先于且独立于**
> $P_\gamma$。$P_\gamma$ 是 O5.3 中**推导的结果**（由 $w_H$ 的轨道差定义），
> 不是定义的输入。不存在"为了让 $Q-Q'_{\mathrm{RH}}$ 等于 $\sum P$ 而构造
> $Q'_{\mathrm{RH}}$"的步骤——$Q'_{\mathrm{RH}}$ 是"所有零点投影后通过同一
> $w_H$ 泛函"的独立对象。

**定理 O5.4（主定理）.**
$$Q=Q'_{\mathrm{RH}}\iff \delta_\rho=0\ \forall\rho
\iff \operatorname{Re}\rho=\tfrac12\ \forall\rho.$$
*证明*：O5.3 + 引理 C4（$P_\gamma\ge0$，$=0\iff\delta=0$）+ 非负可和级数
（C3.4/C3.5）⟹ $\sum m_\rho P=0$ 逐项为零 ⟹ $\delta_\rho=0$。

---

## Part C — 外部定理适用条件逐项表（Barner/Weil 框架）

| 外部定理条件 | $H_0$ 对应性质 | 证明位置 |
|---|---|---|
| real | ✓ 实系数闭式 | 引理 C2 |
| even | ✓ $t^2$ 依赖 | 引理 C2 |
| smoothness | ✓ $C^\infty$（闭式） | 引理 C2 |
| growth | ✓ $\sim\log|t|$（缓增） | 引理 C2 |
| temperedness | ✓ $\in\mathcal S'$ | 引理 C2 |
| derivative/integrability | ✓ $H_0''=O(t^{-2})\in L^1$ | 引理 C3.4 |
| required pairing | ✓ 乘积 $\widehat K\widehat H_0\in L^1$（逐项） | 定义 C3.1 |
| boundary term | ✓ 分部积分发散——不用于定义（逐项替代） | 引理 C3.4/C3.5 |

> 诚实边界：本表**逐项对应的是性质**；Barner 1981 原文的精确测试类
> 语句仍需第三方核对（v2.10.1 标注）。

---

## 状态

- **P_γ 是发动机——不是整辆车**：主定理 = O5.3 恒等式 + C4 等号刻画——
  两者缺一不可；$P_\gamma>0$ 单独不构成 RH 判别。
- **Provenance 是证据——不是证明**：正文定理完全独立于研究史；
  研究史作为 supplementary provenance 保留（research_history_provenance.md）。
- **INVALID-first 攻击点**：O5 的单向性、C3 的三层次区分、Barner 逐项表。

---

## O5 Single-Point-of-Failure Checklist（7 项——外部 Attack A 靶子）

| # | 检查点 | 文档位置 |
|---|--------|----------|
| 1 | Q 的定义来自预先存在的自然对象（w_H 配对值——非为目标式设计） | C3.1-C3.3 |
| 2 | Q'_RH 不是"把 δ=0 塞进去为得目标式而定义"（所有零点投影——同一 w_H 泛函） | C3.3 |
| 3 | Q 与 Q'_RH 使用同一个 functional（w_H——同一解析求值引理 C3.2） | C3.2/C3.3 |
| 4 | 轨道分解不改变原始谱量（绝对收敛 C3.4——重排合法 C3.5） | C3.4/C3.5 |
| 5 | 自配对（在线 δ=0）/重数/非自配对零点处理一致（在线贡献 0——计数已修） | O5.1 |
| 6 | 所有交换/重排/极限有独立合法性（逐条引理——非一步跳跃） | C3.4/C3.5/O5.2 |
| 7 | 无任何一步使用 RH 结论（Q'_RH 只依赖实际 γ_ρ——w_H(γ,0)=(1+γ²)⁻²） | C3.3 |

## External Attack Protocol（INVALID-first——四路）

- **Attack A（O5 单向性）**：不提供 provenance——只看 Q、Q'_RH 原始定义——
  若完全不知道 P_γ 的存在，能否独立推出 orbital decomposition？
- **Attack B（假 RH toy spectrum）**：构造满足所有形式假设但含离轴 δ≠0 的
  谱——从原始定义重新计算 Q−Q'_RH——验证必然等于正 ΣP_γ。
- **Attack C（函数空间）**：δ=0 附近核、Fourier 乘积、零频——重点检查
  "每个公式都对但组合成 distributional identity 不合法"的隐蔽断层。
- **Attack D（等价 vs 蕴含）**：两方向明确拆开——RH⟹Q=Q'_RH（容易）
  与 Q=Q'_RH⟹RH（关键——正项和+等号刻画）——互不混淆。
