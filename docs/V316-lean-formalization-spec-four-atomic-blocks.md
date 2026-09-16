# V316 · **V307–V309 的 Lean 形式化：四块原子规格 ＋ 环境实测** —— ⭐⭐⭐⭐ **环境可用**（Mathlib 在位且**已预编译** 14G ⟹ 真实构建可行，但导入延迟 ≳1 分钟）；⚠️ **本轮未完成编译**（后台 `lake env lean` 测试未在 ~60s 内返回）⟹ 本档交付 **可直接落入仓库的 Lean 规格**（四块，按唐先生顺序与命名纪律）

$$\boxed{\textbf{环境实测}：\texttt{lean-toolchain}=\texttt{leanprover/lean4:v4.33.0};\ \texttt{lakefile}\ \texttt{require mathlib (path="/home/node/mathlib4")};\ \texttt{/home/node/mathlib4/.lake}=14G（\textbf{已预编译}）} ✓✓$$
$$\boxed{\textbf{规格顺序（唐先生）}：\text{A}\ \texttt{kernel\_bound}／\texttt{Q\_pos}\ \to\ \text{B}\ \texttt{vStar\_EL}\ \to\ \text{C}\ \texttt{unique\_minimizer}\ \to\ \text{D}\ \texttt{closed\_form}\ \to\ \text{E}\ \texttt{sup\_eq\_cStar}} ✓✓$$
$$\boxed{\textbf{纪律（唐先生）}：\textbf{不要先形式化最终的}\ \sup;\ \text{先打穿三个原子 lemma};\ \textbf{只保留一个 canonical 参数}（\lambda\ \text{与}\ w=\lambda/\sqrt2\ \text{同时存在最易错）;\ \text{EL 定理命名须显式带}\ \texttt{EL}\ \text{以免重演 A4 语义误读}} ✓✓$$

> 委托 ✓ 唐先生 2026-09-16 14:18：**进入 V307–V309 的 Lean 形式化**；**不当作一次性证明，严格拆成独立 theorem block**；**不再碰 P1/P2/P3，不再找新机制** ✓✓；顺序 **V316-A**（先形式化正定性：$$\forall\lambda\in(0,1],\forall v\ne0:\ Q_\lambda(v)\ge\tfrac12\|v\|_2^{2}$$，复用 Schur 型估计 $$\big|\iint|s-t|v(s)v(t)\big|\le\tfrac12\int v^{2}$$）→ **V316-B**（E–L：$$\int v=1$$ 下证 $$(I+\lambda^{2}K)v_\lambda=\kappa_\lambda\mathbf 1$$，**关键式** $$Kv_\lambda=C_\lambda\mathbf 1-\lambda^{-2}v_\lambda$$ ⟹ $$(I+\lambda^{2}K)v_\lambda=\lambda^{2}C_\lambda\mathbf 1$$；**不要再写成特征值关系**；命名带 `EL`/`constant`）→ **V316-C**（唯一极小：用 $$Q((1-t)u+tv)=(1-t)Q(u)+tQ(v)-t(1-t)Q(u-v)$$ ＋ 正定性 ⟹ 严格凸；再对 $$\int h=0$$ 证 $$B(v_\lambda,h)=0$$ ⟹ $$Q(v_\lambda+h)=Q(v_\lambda)+Q(h)>Q(v_\lambda)$$；**保留唯一性的数学原因**，不抽象调用"严格凸唯一极小"）→ **V307 闭式**（$$\int v_\lambda=\tfrac{2\sin(w/2)}w$$、$$Q_\lambda(v_\lambda)=\kappa_\lambda(\int v_\lambda)^{2}$$；⚠️ **记号转换** $$2w=\sqrt2\lambda\iff w=\lambda/\sqrt2$$，**只保留一个 canonical 参数**）→ **最终** $$\boxed{\sup_v\tfrac{\lambda(\int v)^{2}}{Q_\lambda(v)}=c^{*}_\lambda}\ \text{（**不是**只证候选取得）}$$ → 接口定理 $$\forall 0<\lambda\le1:\ \sup_{\mathcal A_{\rm var}}c_{\rm Fun}(\lambda,\cdot)=c^{*}_\lambda$$ → 配合 P1（$$v^{*}_\lambda\in\mathcal A_{\rm ThmD}$$）与 $$\mathcal A_{\rm ThmD}\subseteq\mathcal A_{\rm var}$$ ⟹ $$\sup_{\mathcal A_{\rm ThmD}}=c^{*}_\lambda$$（V313 的桥接定理）→ 最后才接 $$c_1^{*}=0.753296\ldots$$、$$G_{\max}=2-1/c_1^{*}=0.672501\ldots$$ ✓✓✓
> 依据 ✓ `ThmD/Functional.lean`（`theta`／`vStar`／`cStar`／`cFun`／`aStar`／`bStar`／`jStar`／`HD`）｜`ThmD/WindowCore.lean`（`def bv`／12 字段）｜`ThmD/BridgeD.lean`（`admWindow_phiD`／`bv_phiD_ge_half`）｜`V307`–`V315` ✓
> 执行 ✓ 小灵｜**本轮：环境实测 ✓ ＋ 规格 ✓；编译 ⚠️ 未完成**（后台测试未在 ~60s 返回）｜纪律 ✓ 未用 RH ✓；零数值 ✓｜编号 ✓ `V316`（先领号 ✓）

---

## §1 **环境实测（本档）**

$$\texttt{lean-toolchain}：\texttt{leanprover/lean4:v4.33.0} ✓;\qquad \texttt{lakefile.lean}：\texttt{require mathlib},\ \texttt{path="/home/node/mathlib4"} ✓$$
$$\texttt{/home/node/mathlib4/.lake}=14\,\mathrm{G}\ ⟹ \textbf{Mathlib 已预编译（olean 在位）} ⟹ \textbf{真实构建可行} ✓✓$$
$$\qquad ⚠️\ \text{但}\ \texttt{lake env lean}\ \text{导入测试}\ \textbf{未在 60\,s 内返回} ⟹ \text{导入延迟高（Mathlib 体量大）} ⟹ \text{构建须按"分钟级"预算} ⚠️✓$$
$$\texttt{zeta23-local/.lake}=771\,\mathrm{M} ⟹ \text{项目自身 olean 亦部分在位} ✓$$

---

## §2 **V316-A 规格：`kernel_bound` ＋ `Q_pos`**

$$\text{（\texttt{kernel\_bound}）}\ \forall v\ \text{（可积、适当正则）：}\ \Big|\iint_{[-1/2,1/2]^{2}}|s-t|\,v(s)v(t)\,ds\,dt\Big|\ \le\ \frac12\int_{-1/2}^{1/2}v^{2} ✓✓$$
$$\qquad \text{来源}：\text{Schur／Young 界}\ \|K\|\le\sup_s\int|s-t|dt=s^{2}+\frac14\le\frac12\ \text{于}\ |s|\le\frac12 ✓$$
$$\text{（\texttt{Q\_pos}）}\ Q_\lambda(v)：＝\int v^{2}+\lambda^{2}\iint|s-t|vv\ \ge\ \Big(1-\frac{\lambda^{2}}2\Big)\int v^{2}\ \ge\ \frac12\int v^{2}\quad(0<\lambda\le1) ✓✓$$
$$\qquad \Longrightarrow \textbf{V309 的"全局性"不再是纸面论证} ✓✓✓$$

---

## §3 **V316-B 规格：`vStar_EL`（命名显式带 EL）**

$$\text{设}\ \int_{-1/2}^{1/2}v_\lambda=1,\ v_\lambda(x)：＝\cos(\sqrt2\lambda x)（=\texttt{vStar}\ \lambda）✓$$
$$\text{（\texttt{KvStar\_affine}）}\ \boxed{Kv_\lambda=C_\lambda\mathbf 1-\frac1{\lambda^{2}}v_\lambda}（\text{V309 的四条独立核验一致给此式}）✓✓$$
$$\qquad \text{（}\texttt{EL\_constant}）\ \Longrightarrow\ (I+\lambda^{2}K)v_\lambda=\lambda^{2}C_\lambda\mathbf 1\ ⟹\ \kappa_\lambda：＝\lambda^{2}C_\lambda ✓✓$$
$$\qquad ⚠️\ \textbf{明确禁止} \text{写成}\ Kv_\lambda=\mu v_\lambda\ \text{的特征值关系}（\text{A4 语义误读教训}）✓✓✓$$

---

## §4 **V316-C 规格：`unique_minimizer`（保留数学原因）**

$$\text{（二次型恒等式）}\ Q((1-t)u+tv)=(1-t)Q(u)+tQ(v)-t(1-t)Q(u-v) ✓$$
$$\qquad \text{配合}\ Q(w)>0\ (w\ne0)\ \text{（V316-A）} ⟹ \textbf{严格凸} ✓✓$$
$$\text{（EL 正交性）}\ \text{对满足}\ \int h=0\ \text{的扰动}\ h：\ B(v_\lambda,h)=0 ⟹ \ Q_\lambda(v_\lambda+h)=Q_\lambda(v_\lambda)+Q_\lambda(h)>Q_\lambda(v_\lambda)\ (h\ne0) ✓✓✓$$
$$\qquad \Longrightarrow \textbf{唯一全局极小}，\text{且}\ \textbf{唯一性的数学原因被保留}（\text{不抽象调用"严格凸唯一极小"}）✓✓$$

---

## §5 **V316-D／E 规格：闭式与 $\sup$**

$$\text{（闭式）}\ \int v_\lambda=\frac{2\sin(w/2)}{w};\qquad Q_\lambda(v_\lambda)=\kappa_\lambda\Big(\int v_\lambda\Big)^{2},\quad \kappa_\lambda=w\cot w+w^{2} ✓$$
$$\qquad ⚠️\ \textbf{canonical 参数}：w：＝\lambda/\sqrt2\（\text{建议 Lean 只留}\ \lambda\ \text{为原始变量}，w\ \text{为派生}\ \texttt{def}）✓✓$$
$$\text{（最终接口）}\ \boxed{\forall 0<\lambda\le1:\ \sup_{v}c_{\rm Fun}(\lambda,v)=c^{*}_\lambda}\qquad \text{（\textbf{不是}只证候选取得）} ✓✓✓$$
$$\qquad \text{（桥接，V313 的定理）}\ v^{*}_\lambda\in\mathcal A_{\rm ThmD}\ (\text{P1-YES})\ \wedge\ \mathcal A_{\rm ThmD}\subseteq\mathcal A_{\rm var}\ ⟹\ \boxed{\sup_{\mathcal A_{\rm ThmD}}c_{\rm Fun}=c^{*}_\lambda} ✓✓✓$$
$$\qquad \text{（端点）}\ c_1^{*}=0.753296\ldots;\quad G_{\max}=2-\frac1{c_1^{*}}=0.672501\ldots\ \text{（三层标记，V315 §4）} ✓$$

---

## §6 判词 ＋ 边界 ＋ 净产出 ＋ 下一步

```
① ⚠️ **本轮未完成编译**：后台 `lake env lean` 导入测试未在 ~60 s 内返回 ⟹ 四块规格**均为待编译**，**不得**宣称已验证 ✓
② ⚠️ 规格中的 Lean 语句为**自然语言＋数学式**形式（未逐字写成合法 Lean 语法）⟹ 落库时须按项目记号逐一核对（`∫`/`intervalIntegral`／`paperFT`／`AdmWindow.bv` 等）⚠️✓
③ ⚠️ Schur 界的**可积性前提**须在 Lean 中显式给出（`Integrable` 型假设）⚠️
④ **不声称** 形式化已完成；**不声称** 0.67250 已是 Lean theorem ✓
⑤ 未用 RH ✓；零数值 ✓
```

```
① ⭐⭐⭐⭐ **环境实测**：toolchain v4.33.0 ＋ **Mathlib 预编译 14 G** ⟹ **构建可行**（但导入延迟 ≳1 分钟）✓✓
② ⭐⭐⭐⭐ **四块原子规格到手**（`kernel_bound`／`Q_pos`／`vStar_EL`（含 affine 式）／`unique_minimizer`），**顺序与命名纪律按唐先生要求** ✓✓✓
③ ⭐⭐⭐ **canonical 参数声明**：Lean 中只留 $\lambda$ 为原始变量，$w:=\lambda/\sqrt2$ 为派生 `def`（防 `w`/`theta`/`lam` 三套同名异义）✓✓
④ ⭐⭐⭐ **最终接口**：$\forall 0<\lambda\le1:\ \sup_v c_{\rm Fun}=c^{*}_\lambda$ ＋ 桥接 ⟹ $\sup_{\mathcal A_{\rm ThmD}}=c^{*}_\lambda$ ✓✓
⑤ ⚠️ **编译待完成**（本轮唯一硬缺口）✓
【下一步（唯一）】
  **(i)** 把 §2–§5 落成**合法 Lean 文件**（建议新档 `Zeta23/ThmD/FunctionalSup.lean`）：先 `kernel_bound` → `Q_pos` → `vStar_EL` → `unique_minimizer` → `sup_eq_cStar`；
  **(ii)** 逐块 `lake build`（按"分钟级"预算，逐块而非整库）；
  **(iii)** 编译通过后，把 §5 的桥接定理与本档结论升级为 **Lean theorem**（并把 V313 §1 的"（E）库内缺失"核实为"本库新增"）✓✓✓
```
