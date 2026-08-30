# RH 判别判据：证明框架说明（Proof Framework Exposition）

> 完整框架说明——从 Hadamard 到主定理的连贯叙述——
> 状态：formally reconstructed candidate criterion——pending independent verification
> 日期：2026-08-31

---

## 1. 目标与结果

构造一个**候选等价判据**：存在泛函 $Q$ 与参考泛函 $Q'_{\mathrm{RH}}$，使得

$$Q = Q'_{\mathrm{RH}} \iff \delta_\rho = 0\ \forall \rho \iff \operatorname{Re}\rho = \tfrac12\ \forall \rho,$$

其中 $\rho = \tfrac12+\delta_\rho+i\gamma_\rho$ 遍历 $\zeta$ 的非平凡零点（重数 $m_\rho$）。

**状态声明**：这是**候选判据**——核心链内部形式化完成——**不是 RH 已证明**——外部验证（INVALID-first）待进行。

## 2. 框架总览（对象链）

```
Hadamard ──► S(t) ──► K^nat_ρ ──► H_0 ──► w_H(γ,δ) ──► P_γ(δ) ──► Q, Q'_RH ──► 主定理
 (C1)       (C1)      (O1)        (O2)      (O3)         (O4)        (O5)        (Thm)
```

| 环节 | 对象 | 角色 | 状态 |
|------|------|------|------|
| 1 | $S=\partial_t^2\log\|\xi(\tfrac12+it)\|$ | 谱分布（零点表示） | C1 正式化 |
| 2 | $K_\rho^{\mathrm{nat}}$（自然核） | S 的单零点贡献 | O1 定义 |
| 3 | $H_0$（测试对象） | 配对载体（$H_0''\in L^1$） | O2 定义 |
| 4 | $w_H(\gamma,\delta)=\langle K_\delta^{\mathrm{nat}},H_0\rangle$ | 配对权重 | O3 解析闭式 |
| 5 | $P_\gamma(\delta)$（成对偏离） | 正缺陷量（判别发动机） | O4 正系数因式分解 |
| 6 | $Q,\ Q'_{\mathrm{RH}}$ | 谱泛函 + 参考投影 | O5 逐项定义 |
| 7 | $Q=Q'_{\mathrm{RH}}\iff$ RH | 主定理 | 等号刚性 |

## 3. 环节一：Hadamard 与 S（C1——一页纸重算）

$\xi(s)=\tfrac12 s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)$，代入 $\zeta$ 的 Hadamard
表示后 $\Gamma(s/2)/\Gamma(s/2+1)=2/s$ 相消，得

$$\xi(s)=\tfrac12\pi^{-s/2}e^{bs}\prod_\rho(1-s/\rho)e^{s/\rho},\qquad b=\log2\pi-1-\tfrac\gamma2.$$

对 $s=\tfrac12+it$：显式项（$\log\tfrac12$、$-\tfrac s2\log\pi$、$bs$）的实部
均为常数（$t$-线性函数的实部——$\partial_t^2=0$）；零点项
$\operatorname{Re}\log(1-s/\rho)=\tfrac12\log(\delta_\rho^2+(t-\gamma_\rho)^2)-\text{const}$。
因此

$$S(t)=\partial_t^2\log|\xi(\tfrac12+it)|=\sum_\rho m_\rho
\frac{\delta_\rho^2-(t-\gamma_\rho)^2}{(\delta_\rho^2+(t-\gamma_\rho)^2)^2}
=\sum_\rho m_\rho K_\rho^{\mathrm{nat}}(t),\qquad S_{\mathrm{reg}}=0.$$

**关键**：无 Gamma 残留（相消）；trivial 零点不出现（其 $\Gamma$ 极点与
$\zeta$ 零点在 $\xi$ 中抵消）。$K^{\mathrm{nat}}$ 是 $S$ 的**自然单零点核**。

## 4. 环节二：测试对象 H_0（O2——构造来源）

$$H_0(t)=-\frac{1}{4\pi}\log(1+t^2)+\frac{1}{2\pi(1+t^2)}.$$

- $H_0\in C^\infty\cap\mathcal S'$（光滑——缓增）——**但 $H_0\notin L^1$**（对数增长）
- $H_0''(t)=O(t^{-2})\in L^1$——配对关键性质
- **来源**：$H_0=F^{-1}[\widehat w_{\mathrm{target}}/\widehat K_0]$——由参考权重
  $w_{\mathrm{target}}(\gamma)=(1+\gamma^2)^{-2}$ 与核 $K_0$ 的频率构造——
  2π convention（$\widehat H(u)=\int H(t)e^{-2\pi iut}dt$）下
  $\widehat H_0(u)=e^{-2\pi|u|}[\tfrac{1}{4\pi|u|}+\tfrac12]$
- **历史修正**：早前版本的 $H_0$ 第二项符号错误（$-\tfrac{1}{2\pi(1+t^2)}$）——
  经独立重建（$\widehat w/\widehat K$ 逆变换）修正为 $+$——这是结构发现非润色

## 5. 环节三：配对权重 w_H（O3——解析闭式）

逐项配对（**不是**整体配对——见 C3）通过 Parseval 乘积：

$$\langle K_\delta^{\mathrm{nat}}(\cdot-\gamma),H_0\rangle
=\int_{\mathbb R}\widehat K_\delta^{\mathrm{nat}}(u)\widehat H_0(u)e^{-2\pi iu\gamma}du,$$

其中 $\widehat K_\delta^{\mathrm{nat}}(u)=2\pi^2|u|e^{-2\pi\delta|u|}$，
乘积 $\widehat K_\delta\widehat H_0=\tfrac\pi2 e^{-2\pi a|u|}+\pi^2|u|e^{-2\pi a|u|}\in L^1$
（$a=1+\delta$——$u=0$ 处有限）。两个标准积分给出

$$\boxed{\,w_H(\gamma,\delta)=\frac{a^2(a+1)+\delta\gamma^2}{2(a^2+\gamma^2)^2},\qquad a=1+\delta.}$$

**关键**：$\delta$ 是**实际**实部偏离（可负）——**不是** $|\delta|$。
早前版本偷换 $|\delta|$ 导致逐点正性虚假——经零背景重建修正。

## 6. 环节四：成对偏离 P_γ（O4——判别发动机）

$$P_\gamma(\delta)=2w_H(\gamma,0)-w_H(\gamma,\delta)-w_H(\gamma,-\delta)
=\frac{\delta^2 M_2(\gamma,\delta^2)}{2U^2 D_+ D_-},\qquad U=1+\gamma^2,$$

$$M_2=8U^2(5\gamma^2-1)+4(5U^2-16U+16)\delta^2+16(U-2)\delta^4+4\delta^6,$$
$$D_\pm=\bigl((1\pm\delta)^2+\gamma^2\bigr)^2.$$

对 $|\delta|<\tfrac12$、$|\gamma|\ge\gamma_1=14.1347\ldots$（$U\ge200$）：
$5\gamma^2-1>0$、$5U^2-16U+16>0$、$U-2>0$——**$M_2$ 每项系数为正**；
分母 $2U^2D_+D_->0$ 是平方积。故

$$P_\gamma(\delta)\ge0,\qquad P_\gamma(\delta)=0\iff\delta=0.$$

**关键结构发现**：逐点正性（$w_H(\gamma,\delta)-w_H(\gamma,0)>0$）**不成立**
（$\delta<0$ 时为负——成对和也负）——**真正成立的是函数方程轨道上的
成对正性** $P_\gamma$——这是独立重建摧毁逐点结构后由轨道结构重新涌现的。

## 7. 环节五：泛函 Q 与 Q'_RH（O5——谱装配）

**逐项定义**（绝对收敛）：

$$Q=-\sum_\rho m_\rho w_H(\gamma_\rho,\delta_\rho),\qquad
Q'_{\mathrm{RH}}=-\sum_\rho m_\rho w_H(\gamma_\rho,0)\quad(\text{投影 }\delta_\rho\mapsto0).$$

- $Q'_{\mathrm{RH}}$ 用**实际** $\gamma_\rho$（$w_H(\gamma,0)=(1+\gamma^2)^{-2}$）——
  **定义阶段无 RH 假设**——参考谱
- **绝对收敛**：$|w_H|\sim|\delta|/(2\gamma^2)$——$\sum m_\rho\gamma_\rho^{-2}<\infty$
  （$N(T)=O(T\log T)$）

**轨道装配**（函数方程轨道 $\rho\sim 1-\bar\rho$——同 $\gamma$ 反 $\delta$；
在线 $\delta=0$ 自配对——贡献 0）：

$$\boxed{\,Q-Q'_{\mathrm{RH}}=\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho).\,}$$

**单向性**：$Q$、$Q'_{\mathrm{RH}}$ 的定义**先于且独立于** $P_\gamma$——
$P_\gamma$ 是轨道差的**结果**——不是定义的输入——不存在"为得目标式而构造
$Q'_{\mathrm{RH}}$"。

**计数注意**（历史修正）：$Q'_{\mathrm{RH}}$ 必须是"所有零点投影"
（$-\sum_\rho m_\rho w_H(\gamma_\rho,0)$）——在线零点（自配对）只算 1 个——
早前版本按轨道 $\times2$ 会在在线零点处计 2 倍（RH 情形 $Q\neq Q'_{\mathrm{RH}}$）——已修复。

## 8. 主定理与证明

$$Q=Q'_{\mathrm{RH}}\iff \delta_\rho=0\ \forall\rho\iff \operatorname{Re}\rho=\tfrac12\ \forall\rho.$$

**方向 1（RH ⟹ 等号）**：$\delta_\rho=0\Rightarrow P_{\gamma_\rho}(0)=0$
（O4）——逐项 $\Rightarrow Q=Q'_{\mathrm{RH}}$。

**方向 2（等号 ⟹ RH）**：$Q=Q'_{\mathrm{RH}}$（O5）$\Rightarrow
\sum_{\rho/\sim}m_\rho P_{\gamma_\rho}(\delta_\rho)=0$——$m_\rho>0$、$P\ge0$
（O4）——非负可和级数 $\Rightarrow$ 逐项 $P_{\gamma_\rho}(\delta_\rho)=0$
$\Rightarrow$ $\delta_\rho=0$（O4 等号刻画）——**RH**。

**等号刚性机制**：正项和 + 逐项等号——不需要 uniform 下界——
$P_\gamma$ 是"发动机"（提供逐项正性）——主恒等式 O5 是"整辆车"
（把正性接到 $Q=Q'_{\mathrm{RH}}$ 上）——两者缺一不可。

## 9. 关键机制总结

1. **成对正性**（O4）：函数方程轨道 $\rho\sim1-\bar\rho$ 上——
   $P_\gamma(\delta)=\delta^2\cdot(\text{正系数})/(\text{正})$——每个离轴轨道贡献严格正
2. **等号刚性**（O5+O4）：正项和 $\Rightarrow$ 等号 $\iff$ 全 $\delta_\rho=0$
3. **无循环**：$Q'_{\mathrm{RH}}$ 定义只用实际 $\gamma_\rho$（无 $\beta_\rho$）——
   RH 只作为等号条件出现——不在定义中
4. **逐项卫生**（C3）：$H_0\notin L^1$——整体配对 $\langle\log|\xi|,H_0''\rangle$
   **发散**——不用——改逐项 Parseval 乘积（$L^1$）——绝对可和

## 10. 验证状态与边界

| 环节 | 状态 | 待外部确认 |
|------|------|-----------|
| C1（Hadamard→S） | 🟢 正式化 | — |
| C2（Fourier） | 🟢 正式化 | convention 复核 |
| C3（分布配对） | 🟢 正式化 | **函数空间/交换——最值得攻击** |
| C4（P_γ 正性） | 🟢 正系数闭式 | 代数复核 |
| O5/C5（装配） | 🟢 正式化 | **O5 定义合法性/无 RH——最值得攻击** |
| 主定理 | 🟢（框架内） | 等价性/循环 |

**学术边界**：formally reconstructed candidate criterion——pending
independent verification——**非 RH 已证明**。

## 11. 与已知 criterion 的关系（文献同构——初步）

- **Weil positivity**（一族测试函数正性）vs 我们（单一泛函等号）——结构不同——深层同属显式公式家族
- **Li criterion**（逐零点序列 $\lambda_n\ge0$）vs 我们（逐轨道成对正性）——结构不同
- **Nyman-Beurling**（$L^2$ 逼近）——框架不同
- **初步判断**：形式上非直接重写——$P_\gamma$ 成对正缺陷机制可能新——
  **最终判断权在领域专家**（A/B 盲测核心问题）

---

*附：本框架对应的完整推导与检查见 `verification/first_package/manuscript.md`、
`verification/theorem_level_o5_c3.md`；研究史（内部）见
`verification/research_history_provenance.md`。*
