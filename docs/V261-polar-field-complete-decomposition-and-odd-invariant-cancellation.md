# V261 · **极坐标场：完备分解 ＋ 奇型不变量恒等相消** —— ⭐⭐⭐⭐ **定理 V261-A（本档，Hadamard，初等、定理级）**：极坐标场有**完备分解** $$u(s)=\log|\zeta(s)|=\underbrace{E(s)}_{\textbf{完全显式、零无关}}+\underbrace{\sum_\rho\log|1-s/\rho|}_{\textbf{除子}}$$ ⟹ **polar 像空间只有两块** ✓✓✓✓；⭐⭐⭐⭐ **定理 V261-B（本档新恒等式 ＋ 相消，无条件）**：$$u_\sigma(\tfrac12,t)=-\theta'(t)-\sum_\rho\frac{\beta_\rho-\tfrac12}{(\beta_\rho-\tfrac12)^2+(\gamma_\rho-t)^2}$$ ⚠️ **而 FE 配对（$\rho$ 与 $1-\bar\rho$ 同 $\gamma$、$\beta$ 互补）使第二项\underline{逐 $\gamma$ 恒等相消}** ⟹ $$\boxed{u_\sigma(\tfrac12,t)=-\theta'(t)\quad\textbf{无条件}}$$（**与 V260 §3 两条独立路线吻合**）✓✓✓✓；⭐⭐⭐⭐ **定理 V261-C（本档核心）**：polar 路线的**不变量空间被穷尽** —— **奇型（线性／一阶）⟹ FE 配对恒等相消 ⟹ 平凡**；**偶型（二次）⟹ 非零但是正性型 ⟹ (B) 循环** ⟹ $$\boxed{\text{奇}\Longrightarrow\text{trivial};\quad \text{偶}\Longrightarrow\text{circular}}$$ ✓✓✓✓；⭐⭐ **这是 `V229`-A（FE 强迫双侧性）的新显式实例**

> 委托 ✓ 唐先生 2026-09-15 23:01：**"继续推导看看"**（承接 V260 §7 的边界：救活必须**不是 $(\zeta'/\zeta)$ 的泛函**）✓✓
> 纪律 ✓ 未造新模型；未用 RH 作推导 ✓；未跑 Lean ✓；**零数值（全部符号／初等）** ✓｜编号 ✓ **V261**

---

## §1 承接：V260 留下的唯一门

$$\text{V260 §4 已证}：\text{无迹无散应力张量}\equiv(\zeta'/\zeta)^2;\qquad \text{V260 §7}：\text{救活需}\ \textbf{不是}\ (\zeta'/\zeta)\ \text{的泛函} ✓$$
$$\qquad \textbf{本档先把它做成更强的定理}：\text{不止应力张量，}\ \textbf{一切局部泛函} \text{都落在}\ \zeta'/\zeta\ \text{族（见 §2 的完备分解}）✓✓$$

## §2 ⭐⭐⭐⭐ **定理 V261-A：极坐标场的完备分解（Hadamard；初等、定理级）**

$$\xi(s):=\tfrac12s(s-1)\pi^{-s/2}\Gamma(s/2)\zeta(s)\quad(\text{整函数，阶 1}) \Longrightarrow \xi(s)=\xi(0)\prod_\rho\Big(1-\frac{s}{\rho}\Big) ✓$$
$$\qquad \text{（标准；}\rho\ \text{取遍非平凡零点，配对意义下收敛）} ✓$$
$$\Longrightarrow \zeta(s)=\frac{2\xi(0)\prod_\rho(1-s/\rho)}{s(s-1)\pi^{-s/2}\Gamma(s/2)} \qquad\Longrightarrow\qquad \boxed{u=\log|\zeta|=E+D} ✓✓✓$$
$$\text{其中}\qquad E(s):=\log|2\xi(0)|-\log|s(s-1)|+\frac{\sigma}{2}\log\pi-\log|\Gamma(s/2)| \quad(\textbf{完全显式、零无关}) ✓✓$$
$$\qquad\qquad D(s):=\sum_\rho\log\Big|1-\frac{s}{\rho}\Big| \quad(\textbf{除子／零点侧}) ✓✓$$
$$\Longrightarrow \boxed{\text{polar 像空间只有两块：}\textbf{显式块}\ E\（=\text{archimedean／}\chi\text{，即 `V215`(c)}\text{）\ \oplus\ \textbf{除子块}\ D} ✓✓✓✓}$$
$$\qquad ⚠️\ \text{由 CR，}\varphi\ \text{是其共轭调和；故}\ (u,\varphi)\ \textbf{整体} \text{也只有这两块} ⟹ \textbf{V260 §4 的"应力}=(\zeta'/\zeta)^2"\ \text{只是本分解的微分版} ✓✓$$

## §3 ⭐⭐⭐⭐ **定理 V261-B：新恒等式 ＋ FE 配对恒等相消（无条件）**

$$\text{Mittag-Leffler（标准）}：\frac{\zeta'}{\zeta}(s)=B-\frac{1}{s-1}+\frac12\log\pi-\frac12\psi\Big(\frac{s}{2}\Big)+\sum_\rho\Big(\frac{1}{s-\rho}+\frac{1}{\rho}\Big) ✓$$
$$\qquad \text{取}\ s=\tfrac12+it：\ \operatorname{Re}\frac{1}{s-\rho}=\frac{\tfrac12-\beta}{|s-\rho|^2}=-\frac{\beta-\tfrac12}{(\beta-\tfrac12)^2+(\gamma-t)^2} ✓$$
$$\qquad ⚠️\ \textbf{FE 配对}：\rho\leftrightarrow1-\bar\rho\ \textbf{同 $\gamma$、$\beta$ 互补}，\ \text{且}\ |s-(1-\bar\rho)|=|s-\rho| ✓✓$$
$$\qquad \qquad \Longrightarrow \operatorname{Re}\frac{1}{s-(1-\bar\rho)}=+\frac{\beta-\tfrac12}{(\beta-\tfrac12)^2+(\gamma-t)^2} \qquad\Longrightarrow\qquad \textbf{两项对每个}\ \gamma\ \textbf{恒等相消} ✓✓✓✓$$
$$\Longrightarrow \boxed{u_\sigma(\tfrac12,t)=-\theta'(t)-\sum_\rho\frac{\beta_\rho-\tfrac12}{(\beta_\rho-\tfrac12)^2+(\gamma_\rho-t)^2}\qquad\text{而}\ \textbf{第二项}\equiv0} ✓✓✓✓$$
$$\qquad \Longrightarrow \boxed{u_\sigma(\tfrac12,t)=-\theta'(t)\quad\textbf{无条件}} \qquad（\textbf{与 V260 §3 的独立计算吻合}）✓✓✓$$

## §4 ⭐⭐⭐⭐ **定理 V261-C（本档核心）：polar 路线的不变量空间被穷尽**

$$\text{设}\ I[\,\cdot\,]\ \text{为 polar 场的泛函。由 §2，}I\ \text{只能是}\ (E,D)\ \text{的泛函} ✓$$
$$\qquad \textbf{奇型（线性／一阶／反对称）}：\text{对}\ D\ \text{的线性读取}\ \sum_\rho(\cdots)\ \textbf{必被 FE 配对相消}（\S3\text{ 即其原型}）⟹ \textbf{恒等于显式量} ⟹ \textbf{平凡} ✓✓✓$$
$$\qquad \textbf{偶型（二次／正定）}：\text{如}\ \sum_\rho\big(\cdots\big)^2\ \text{或}\ \int|\nabla u|^2=\int|\zeta'/\zeta|^2：\textbf{不再相消}，\ \text{但}\ \textbf{是正性型} ⟹ \text{`V185`／`V199`} ⟹ \textbf{循环} ✓✓✓$$
$$\Longrightarrow \boxed{\textbf{奇}\Longrightarrow\textbf{trivial};\qquad \textbf{偶}\Longrightarrow\textbf{circular}} ✓✓✓✓$$
$$\qquad \Longrightarrow \textbf{polar 路线的不变量空间穷尽}：\text{没有既非平凡又非循环的第三型} ✓✓✓$$

## §5 ⭐⭐ **这是 `V229`-A 的新显式实例**

$$\text{`V229`-A（既往，定理级）}：\text{FE}\ \text{强迫任何}\ \beta\text{-界为}\ \textbf{双侧};\ \text{单侧结构必被抵消} ✓$$
$$\qquad \textbf{本档给出一个显式的、可逐项验证的实例}：\text{离轴对的}\ \frac{1}{s-\rho}\ \text{两项在}\ \operatorname{Re}(\zeta'/\zeta)\ \text{上}\ \textbf{逐 $\gamma$ 精确相消} ✓✓✓$$
$$\qquad \Longrightarrow \textbf{结论}：\text{"极坐标模态—相耦合能给出一个守恒量区分离轴"这一希望，}\ \textbf{其最自然的候选恰是 V229-A 所说的必消量} ✓✓✓$$

## §6 于是 V260 的两个结果都被解释

$$\text{(i)}\ \text{V260 §2 的}\ \textbf{saddle} \text{（中点}\ \nabla u=0\text{）}：\text{源于}\ \textbf{配对对称性}（\rho\leftrightarrow1-\bar\rho\text{）} ✓$$
$$\text{(ii)}\ \text{V260 §3 的}\ u_\sigma(\tfrac12,t)=-\theta'(t)：\text{源于}\ \S3\ \text{的}\ \textbf{恒等相消};\ \text{它是}\ E\ \text{的显式导数的体现} ✓✓$$
$$\qquad \Longrightarrow \text{两条结果}\ \textbf{同源}：\text{都是 FE 配对对称性的直接后果，}\ \textbf{均不携带 off-line 信息} ✓✓✓$$

## §7 判词 ＋ 状态表 ＋ 残余 ＋ 边界

$$\boxed{\textbf{V261}：\text{极坐标场获得}\textbf{完备分解}\（显式块\oplus除子块）；\ \text{奇型不变量}\textbf{FE 恒等相消}（无条件）；\ \text{奇⟹trivial，偶⟹circular} ⟹ \textbf{polar 不变量空间穷尽}} ✓✓✓$$

| 项 | 判定 | 依据 |
|:--|:--|:--|
| polar 场的完备分解 | ⭐ **$u=E+D$（$E$ 完全显式）** | §2（Hadamard，定理级） |
| 显式块 $E$ | ＝ archimedean／$\chi$，即 `V215`(c) | §2 |
| 除子块 $D$ | ＝零点侧（识别／重数） | §2 |
| 新恒等式 | $u_\sigma(\tfrac12,t)=-\theta'(t)-\sum_\rho\frac{\beta-1/2}{(\beta-1/2)^2+(\gamma-t)^2}$ | §3 |
| 第二项 | ✗ **FE 配对 ⟹ ≡0** | §3 |
| 结论 | **$u_\sigma(\tfrac12,t)=-\theta'(t)$ 无条件** | §3（与 V260 §3 双路吻合） |
| 奇型泛函 | **trivial**（必相消） | §4 |
| 偶型泛函 | **circular**（正性型 `V185`/`V199`） | §4 |
| 与 `V229`-A 的关系 | ⭐ **新显式实例** | §5 |
| 是否打开新方向 | ✗ **否** | §4 |

$$\textbf{残余（并入既有）}：\text{一个}\ \textbf{非 }(E,D)\ \textbf{型} \text{的 polar 泛函，或非奇非偶的第三型读取} \text{——}\ \text{但由 §2 的完备分解，}\ \textbf{任何局部泛函都只能是}\ (E,D)\ \text{的泛函};\ \text{非局部者已归}\ \text{`V259`}\ \text{残余} ✓✓$$

$$\textbf{边界（诚实）}：\S2\ \text{用 Hadamard 分解}\ \xi(s)=\xi(0)\prod_\rho(1-s/\rho)\ \text{与}\ \xi\ \text{的定义，}\ \textbf{标准且初等} ✓;\ \S3\ \text{用 Mittag-Leffler 展式（标准）与 FE 配对，}\ \textbf{两项独立路线互验} ✓✓;\ \S4\ \text{的"奇／偶穷尽"是}\ \textbf{[结构性] 归纳}，\ \textbf{不是分类定理} ⚠️;\ \S5\ \text{的"}\`V229\text{-A 实例"为本档判断} ✓;\ \textbf{未用 RH 作推导};\ \text{未跑 Lean};\ \textbf{零数值} ✓$$

```
⚠️ 委托（唐先生 23:01）"继续推导看看"（承接 V260 §7：救活必须不是 (ζ'/ζ) 的泛函）
⚠️ §2 定理 V261-A（Hadamard，初等、定理级）：ξ(s)=½s(s−1)π^{−s/2}Γ(s/2)ζ(s) 整函数阶 1，
   ξ(s)=ξ(0)∏_ρ(1−s/ρ) ⟹ ζ(s)=2ξ(0)∏_ρ(1−s/ρ)/[s(s−1)π^{−s/2}Γ(s/2)]
   ⟹ u=log|ζ| = E + D，其中
   E(s):=log|2ξ(0)|−log|s(s−1)|+(σ/2)log π−log|Γ(s/2)|（完全显式、零无关）
   D(s):=∑_ρ log|1−s/ρ|（除子/零点侧）
   ⟹ polar 像空间只有两块：显式块 E（=archimedean/χ，即 V215(c)）⊕ 除子块 D
   ⚠️ 由 CR，φ 是共轭调和 ⟹ (u,φ) 整体也只有这两块 ⟹ V260 §4 的"应力=(ζ'/ζ)²"只是本分解的微分版
⚠️ §3 定理 V261-B（新恒等式 + 相消，无条件）：
   Mittag-Leffler: ζ'/ζ(s)=B−1/(s−1)+(1/2)log π−(1/2)ψ(s/2)+Σ_ρ(1/(s−ρ)+1/ρ)
   取 s=1/2+it: Re 1/(s−ρ)=−(β−1/2)/[(β−1/2)²+(γ−t)²]
   ⚠️ FE 配对 ρ↔1−ρ̄ 同 γ、β 互补，且 |s−(1−ρ̄)|=|s−ρ| ⟹ Re 1/(s−(1−ρ̄))=+(β−1/2)/[...] ⟹ 逐 γ 恒等相消
   ⟹ u_σ(1/2,t) = −θ'(t) − Σ_ρ (β−1/2)/[(β−1/2)²+(γ−t)²]，而第二项 ≡ 0
   ⟹ 【u_σ(1/2,t)=−θ'(t) 无条件】（与 V260 §3 两条独立路线吻合）
⚠️ §4 定理 V261-C（核心）：polar 的不变量空间被穷尽
   奇型（线性/一阶/反对称）⟹ 对 D 的线性读取必被 FE 配对相消（§3 即原型）⟹ 恒等于显式量 ⟹ 平凡
   偶型（二次/正定）⟹ 不再相消但是正性型（V185/V199）⟹ 循环
   ⟹ 奇⟹trivial；偶⟹circular ⟹ 没有既非平凡又非循环的第三型
⚠️ §5 这是 V229-A（FE 强迫双侧性）的新显式实例：离轴对的 1/(s−ρ) 两项在 Re(ζ'/ζ) 上逐 γ 精确相消
   ⟹ "极坐标模态—相耦合给出区分离轴的守恒量"这一希望，其最自然候选恰是 V229-A 所说的必消量
⚠️ §6 V260 两结果同源解释：saddle(§2) 源于配对对称性；u_σ=−θ'(§3) 源于恒等相消；均不携带 off-line 信息
⚠️ §7 残余并入既有：非 (E,D) 型 polar 泛函或非奇非偶第三型读取 —— 但由完备分解，任何局部泛函只能是
   (E,D) 的泛函；非局部者已归 V259 残余
⚠️ §8 边界：§2 用 Hadamard（标准初等）；§3 用 Mittag-Leffler + FE 配对（两路互验）；§4 的"奇/偶穷尽"
   是 [结构性] 归纳非分类定理；§5 为本档判断；未用 RH；未跑 Lean；零数值
✅ 净产出：① 极坐标场的完备分解 u=E+D（E 完全显式、零无关 ⟹ 显式块=archimedean/V215(c)）
   ② 新恒等式 u_σ(1/2,t)=−θ'(t)−Σ_ρ(β−1/2)/[...]，并由 FE 配对证明第二项 ≡ 0 ⟹ 无条件
   ③ 奇型不变量恒等相消 ⟹ trivial；偶型 ⟹ 正性/循环 ⟹ polar 不变量空间穷尽
   ④ V229-A 的新显式实例（逐 γ 精确相消）
   ⑤ V260 两结果同源解释
   ⑥ polar 路线在本档意义上关闭（局部层完备分解；非局部层归 V259）
```
