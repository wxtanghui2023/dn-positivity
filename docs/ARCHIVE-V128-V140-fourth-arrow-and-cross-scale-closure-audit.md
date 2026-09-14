# ARCHIVE · **V128–V140 ＝ Fourth-Arrow ＋ Cross-scale Closure Audit**（2026-09-14 23:38 归档 ✓）
> **本次扩展 ✓**：`V138`–`V140` 并入，且**不是三份追加报告**，而是**对 `V137` 的 $R_{\rm residual}$ 的一次【定界审计】✓** —— 即：把"第四箭头"与"跨尺度兼容"两条线**共同界定的残量边界**写清楚 ✓

> **用途 ✓**：以后任何新候选只要声称提供了**新的 $\sqrt{}$-正性、稳定性、或第四箭头**，**直接拿本档做前置审计** ✓ —— 而不必重走九轮 ✗
> **配套 ✓**：`CLOSED-ROUTES-MAP` §F（总入口决策树 ＋ 查重规则 ✓）｜`MASTER-STATUS-AND-CLOSURES` §0.1（J 裁定 ✓）／§4.2 ✓
> **纪律 ✓**：未用 RH ✓；未跑 Lean ✓；九轮皆为**纸面／零数值** ✓（除 `V129` 含一次小规模精确校验 ✓）｜T10 勘误留档 ✓（`V136` §6 ✓）
> **状态 ✓**：$$\boxed{\textbf{V137 ＝ SEARCH BRANCH CLOSED}}\quad\ne\quad\text{RH CLOSED}\ \checkmark$$

---

## §0 一句话判词（✓）

$$\boxed{\text{九轮（}V128\text{–}V136\text{）＋ }J\ \text{裁定（}V137\text{）＝ 一条}\textbf{可复用封口}：\text{全部逃逸口收敛到同一处，而该处【未被证明为空】}\ ✓}$$

---

## §1 ⭐ 三条**不可越界**标签（本档最重要的部分 ✓）

### 标签 ① —— **已证明的**（✓ 可直接当筛子用 ✓）
$$\boxed{\text{具体机制}\ \Longrightarrow\ \text{已有 CLOSED route}\ \checkmark}$$
```
· finite-window ⟹ 至多【单侧】✗                      [V125；E148]
· 极限型 O = lim O_n（O_n 窗口型）⟹ O(Z₊) = O(Z₋) ⟹ 非 RH 等价 ✗   [V133 Theorem A ✓✓]
· k-点核 ⟹ FE 湮灭（只产 σ-偶 ∧ τ-偶＝|δ| 型）⟹ 单侧 ✗            [V130 ✓✓]
· 迹 ⟹ 显式公式 ✗；谱 ⟹ L1 NO-GO／N0 循环 ✗                        [E104②；L1；N0]
· 正性 ⟹ L3 0/15 ✗；能量 ⟹ 五类无排除型＋二阶变分为负 ✗             [V123]
· "canonical ⟹ stable" ⟹ **为假 ✗**（三反例）                       [V135 ✓]
· 稳定机制五类（收缩／Lyapunov／正性／谱隙／序型）⟹ 全已封或退回 D₁ ✗  [V135 §2]
· √ 来源 (i)–(iv)（二次型／有限极化／统计／FE）⟹ 全已封 ✗           [V136 §2]
```
### 标签 ② —— **条件分类的**（✓ 有定理骨架，前提写死 ✓）
$$\boxed{\text{canonicality}\ \not\Rightarrow\ \text{stability}\ \checkmark\qquad(\text{`V135` 三反例：}F(x){=}2x\ \text{／等变版／}\operatorname{diag}(2,\tfrac12)\ ✓)}$$
$$\boxed{\text{canonical}\ +\ \underbrace{\text{稳定机制}}_{\text{五类}}\ \Longrightarrow\ \text{本质正规}\ \Longrightarrow\ \text{谱定理}\ \Longrightarrow\ \text{正测度}\ \checkmark\qquad(\text{`E104` ③ 的后半步 ✓；前提：稳定机制存在 ✓)}$$
$$\boxed{\text{「稳定即序型」引理 ✓：稳定性 ⟺ 带符号不等式（}q{<}1\ /\ V(Fx){<}V(x)\ /\ \lambda{>}0\text{）⟹ **成本必落 }D_1\ ✓\qquad(\text{`V135` §3 ✓；结构性级 ⚠️）}}$$

### 标签 ③ —— **未证明的**（⚠️ **必须保留 —— 否则会把"搜索库空了"误写成"数学上不存在" ✗**）
$$\boxed{R_{\rm residual}\ =\ \text{未分类的 char-0 intrinsic polarization/purity mechanism}}$$
$$\boxed{R_{\rm residual}\ \neq\ \varnothing\quad\text{或}\quad R_{\rm residual}\ =\ \varnothing\qquad\textbf{两者均未证明}\ \checkmark}$$
```
· 已得 ✓：已知 char-0 结构 ⟹ 【未发现】purity mechanism               [V136 §6 勘误 ✓]
· 未得 ✗：已知 char-0 结构 ⟹ 【不存在任何可能的】purity mechanism      ✗（需完备分类定理，尚无 ✓）
· V136 §2 的"只有五种 √ 来源"为【枚举型（II 类证据）】✗ —— 不得升成否定性定理 ✓
```

---

## §1b ⭐⭐⭐ **定界审计：`V138`–`V140`（跨尺度兼容线）**（✓ 与第四箭头线互补 ✓）

$$\textbf{`V138`（查图 ✓）}：\text{跨尺度兼容 ＋ 缺陷复合律}\ \textbf{【已研究过】}\ ✓\ ——\ \text{三处独立注册（}`TWO-SCALE材料A/B`\ ✓／`R-CS-PRE1` 的 $X0$："非 cocycle 非 coboundary"\ \textbf{逐字相同}\ ✓／`SCALE-DYNAMICS` 的 $\Omega=T_{Y,Z}T_{X,Y}-T_{X,Z}$ ＝ 用户的 $\mathcal C_{m,n,k}$\ ✓）＋ 一次具体构造测试（`addmul-defect-test-death`：$\lambda_{\min}$ 与 $\gamma$ 完全无关 ⟹ 原因 ＝ \textbf{定理}：$D=|D|U(\gamma)$ 酉共轭保谱 ✓）$$
$$\textbf{`V139`（材料 A／B ✓）}：$$
$$\qquad\text{A（二维 lattice／不变因子）}：\text{Smith（$d_1d_2=N$ 需额外 $d_1{=}d_2$ ⟹ AM-GM）／自对偶（⟹ discriminant）／Minkowski（⟹ 需 isotropy）}\ \Longrightarrow\ \textbf{全部退回箱 8}\ ✗$$
$$\qquad\text{B（数域／ideal-class）}：\sqrt{|D_K|}\ \text{四层剥离 ⟹ 第 0 层}\textbf{按定义}＝\text{trace pairing Gram 行列式平方根 ⟹ }\textbf{定义性地 }D_1\ ✗;\ \text{第 2 层 }\tfrac12\ \text{非来自维数（应为 }1/d\text{）而来自二次性 ⟹ }\textbf{违反自身约束 C4}\ ✗;\ \text{第 4 层 Brauer–Siegel 下界 ＝ GRH 强度 ⟹ 循环}\ ✗$$
$$\qquad\Longrightarrow\ \text{A 的 ideal-class 部分 ≡ B ⟹ }\textbf{合流 ✗};\ \text{数域 discriminant 路线的 }\sqrt{}\ \textbf{无独立来源}\ ✓$$
$$\textbf{`V140`（固定基／非对角 transport ✓）}：\textbf{第一层即判死 ✗}$$
$$\qquad\text{(i) 相位来源}\textbf{已穷举}（`AOB1` §2 四源：互反符号／holonomy／2-上闭链 ⟹ character／Fourier–Mellin／L-值 ✗；第四种 Frobenius 型 ＝ 唯一不退化但 \textbf{char-}p\ \textbf{专属 ✗}）$$
$$\qquad\text{(ii) 本档二分定理 ✓}：T\ \text{含 }\gamma\ ⟹\ \text{相位 ＝ 算术频率}\times\gamma\ ⟹\ \gamma\ \text{是【输入】✗（Mellin 参数型）};\ T\ \text{不含 }\gamma\ ⟹\ \text{与 }\gamma\ \text{无关 ✗（谱＝}\{\gamma_j\}\ \text{须 HP ⟹ }N0\ \text{循环 ✗）}$$
$$\qquad\qquad\Longrightarrow\ \textbf{"non-diagonal}\ \ne\ \text{intrinsically }\gamma\text{-sensitive" 得证 ✓}$$
$$\qquad\text{(iii) ⭐⭐ 档案决定性 ✓}：\textbf{断裂双重}（`phase-source-search` ✓）＝ \text{Gate A（相位来源）＋ Gate B（权-1 宿主）};\ \text{Spec }\mathbb Z\ \textbf{两者皆缺}，\mathbb F_q\ \textbf{两者皆有且【同源】}（similitude $\Phi^\dagger Q\Phi=qQ$ ✓）$$
$$\Longrightarrow\ \boxed{\text{故 }V138\ \text{的三处未执行项}\textbf{全部关闭}：材料 A ✗／材料 B ✗／修复方向（固定基缺陷）✗✓✓}$$
$$\qquad\textbf{归档后纪律 ✓}：\textbf{不再沿 cross-scale／fixed-basis／transport 线搜索} ✗$$

## §2 总入口决策树（✓ 与 `CLOSED-ROUTES-MAP` §F 同源 ✓）

$$\boxed{\text{Fourth Arrow}\ \longrightarrow\ \begin{cases}\text{finite-window}&\to\ \text{`V133`}\ ✗\\[1pt]\text{limit program}&\to\ \text{`E104`}\ ✗\\[1pt]\text{trace／operator}&\to\ \text{`E104`／`L1`／`N0`}\ ✗\\[1pt]\text{canonical object}&\to\ \text{`V135`}\ ✗\text{(canonical}\not\Rightarrow\text{stable)}\\[1pt]\text{stability}&\to\ D_1\ ✗\\[1pt]\sqrt{\ }\text{-positivity}&\to\ \text{`V136`／G13}\ ✗\\[1pt]\text{O2／O3}^\star\text{／O5}&\to\ \text{`V130`–`V132`}\ ✗\end{cases}}$$
$$\textbf{最终节点统一指向 ✓}：\boxed{R_{\rm residual}=\text{未分类的 char-0 intrinsic polarization/purity mechanism}\ ⚠️}$$
$$\textbf{＋ 跨尺度线一并收束（}V138\text{–}V140\text{ ✓）：}\boxed{\text{Fourth Arrow / Cross-scale}\ \Longrightarrow\ R_{\rm residual}}$$
$$\qquad\text{四条支路 ✓}：\begin{array}{c}\text{二维 lattice／invariant-factor}\ \xrightarrow{V139}\ \text{quadratic／discriminant}\\[1mm]\text{number-field／ideal-class}\ \xrightarrow{V139}\ \text{Gram determinant／analytic class-number}\\[1mm]\text{fixed-basis non-diagonal transport}\ \xrightarrow{V140}\ \text{phase source}\end{array}$$
$$\textbf{故 }R_{\rm residual}\ \text{的等价表述 ✓（两条线的共同收束 ✓）}：\boxed{R_{\rm residual}=\underbrace{\text{char-0 Frobenius substitute}}_{\text{Gate A：相位来源}}+\underbrace{\text{weight-1 host}}_{\text{Gate B：}\beta=\frac12}}$$

---

## §3 ⭐ 最高优先级查重规则（✓ 新候选的**第一问** ✓）

$$\boxed{\text{任何新候选若声称"这是一个新的平方根来源" ⟹ }\textbf{第一问不是"它能不能工作"，而是"它的 }\sqrt{\ }\text{ 到底来自哪里？"}}$$
$$\qquad\textbf{强制落入下列七箱 ✓}：\text{quadratic/polarization}\ \Big|\ \text{finite purity}\ \Big|\ \text{statistical}\ \Big|\ \text{functional-equation}\ \Big|\ \text{spectral}\ \Big|\ \text{finite-window/limit}\ \Big|\ \text{order/stability}$$
$$\qquad\Longrightarrow\ \text{能归类 ⟹ 直接按对应 CLOSED route 处理 ✗（不必研究）}$$
$$\qquad\Longrightarrow\ \boxed{\text{若全部不能归类，\textbf{才允许进入 }R_{\rm residual}\ ⚠️}}$$
$$\qquad\textbf{本规则的作用 ✓}：\text{使 }V137\ \text{不只是"结束记录"，而成为下一阶段的}\textbf{入口过滤器}\ ✓✓$$

---

## §4 九轮清单（✓ 逐条判词与指针 ✓）

| 轮次 | 对象 | 判词 | 关键产出 |
|:--|:--|:--|:--|
| `V128` | 图内入口穷尽性核查 | **不成立 ✗**（未获许可） | 6×6 资源×载体表；六轮收敛观察 |
| `V129` | $O5$ 最硬子类（不可约高阶 primitive） | 第一关通过 ✓ **不封口** | $\Delta^3$ ＝ 经典 ANOVA/Hoeffding；障碍 ＝ **可知性** ✗ |
| `V130` | $O5$ 残量（可算 $k$-点对象） | 残量定位 ✓ | ⭐ **FE 湮灭定理** ✓✓（$k{=}1$ 特例 ＝ `V124` 引理 A） |
| `V131` | $O2$ 对应关系 | 封口定理正确 ✓ | **瓶颈是箭头，非对称性廉价** ✓ |
| `V132` | $O3^\star$ 分类命题 | **成立（结构性）** ✓ | **β-free 数据引理** ✓（$E103$ Lemma A 推论）；采集您的纠正 ✓ |
| `V133` | 第四箭头完备性 | 残量形态唯一化 ✓ | ⭐ **Theorem A（极限盲性）** ✓✓；关键问题答"否"＋两类形态 ✓ |
| `V134` | $V118(c)$ 可形式化性 | **可形式化且已形式化** ✓ | $E104$ 九类输出表 ＋ $E105$ 二分 ⟹ **T5 对可用载体坍缩** ✗ |
| `V135` | Canonicality–Stability | **"canonical ⟹ stable" 为假** ✗ | ⭐ **稳定即序型引理** ✓；五类修复机制逐条映射 ✓ |
| `V136` | G13-X（$k{=}2$ primitive audit） | **已审计结构内无逃脱** ✗ | ⭐ **五种 $\sqrt{}$ 来源** ✓；元数无关 ⟹ $k\ge3$ 免做 ✓ |
| `V137` | **J 裁定** | $u_1$ 未证明 ✓ | 三层结论；$R_{\rm residual}$ 命名 ✓；纪律写死 ✓ |

---

## §5 三层结论（✓ 引 `V137` §1 ✓）

```
Level 1（已证否定 ✓）：finite-window → limit → trace → spectral → positivity 逐项封闭
Level 2（条件分类 ✓）：canonicality ⟹̸ stability；任何稳定性须支付带符号/序结构；五类全封或退回 D₁
Level 3（真正未解决 ✓）：是否存在此前未分类的 char-0 intrinsic polarization/purity mechanism ⚠️
   （须避开：finite-level／quadratic／positive-kernel／spectral／explicit-formula／statistical／functional-equation／canonical-only）
```

---

## §5b ⭐⭐⭐ **最终双门图（Gate A ＋ Gate B）**（✓ `V140` ✓）

$$\boxed{\begin{array}{ccc}\text{Spec }\mathbb Z\\[1mm]\downarrow\\[-1mm]\underbrace{\text{arithmetic}}_{\text{输入}}&\xrightarrow{\ \text{Gate A}\ }&\underbrace{\gamma}_{\text{phase}}\\[2mm]&&\downarrow\text{ Gate B}\\[1mm]&&\underbrace{\beta=\frac12}_{\text{weight}}\end{array}}$$
$$\textbf{函数域 ✓（两个缺口被同一对象绑定 ✓）}：\Phi^\dagger Q\Phi=qQ\ ✓\ \Longrightarrow\ |\alpha|=\sqrt q,\ \alpha=\sqrt q\,e^{i\theta}\ ✓\ \Longrightarrow\ s=\frac12+\frac{i\theta}{\log q}\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\text{模}\Rightarrow\frac12,\qquad\text{辐角}\Rightarrow\gamma}\qquad\text{—— 二者}\textbf{不是两个独立机制}，而是}\textbf{同一个 Frobenius eigenvalue 的 modulus ＋ phase} ✓✓$$
$$\textbf{而 Spec }\mathbb Z\ \text{（✓ 两个独立缺口 ✓）}：\boxed{\text{weight-1 host}\ \textbf{缺}}\qquad\boxed{\text{arithmetic Frobenius}\ \textbf{缺}}$$
$$\Longrightarrow\ \boxed{\textbf{关键判断 ✓}：\text{过去九轮看似不同的失败，被压缩成一个}\textbf{干净的结构性问题}：\text{RH 的复谱模型需要同时解决}\textbf{两个独立的结构缺口} ✓}$$
$$\qquad\text{（}V140\ \textbf{不是又一条死路} ✓\ ——\ \text{它第一次把"为什么总掉回 }HP\text{／显式公式／}L\text{-值／有限 purity"}\text{压缩成上述双缺口 ✓）}$$

## §6 边界（✓）

```
⚠️ 本档不宣称：RH 无突破口 ✗；char-0 purity mechanism 不存在 ✗；u₁ 不可判定 ✗
⚠️ 本档宣称（且仅宣称）：九轮结构审计完成 ✓；R_residual 已命名 ⚠️；其"不存在"未成为定理 ✗
⚠️ 若继续：需要【新的数学输入】✓（新定理／新结构），或对 R_residual 的存在性给出【构造】✓
⚠️ V137 的状态是 SEARCH BRANCH CLOSED ✓ —— 不是 RH CLOSED ✗
✅ 可复用性 ✓：本档 ＋ `CLOSED-ROUTES-MAP` §F ＋ `MASTER` §0.1／§4.2 ＝ 未来新候选的前置审计入口 ✓
```
### ⑥d 档案纪律（✓ 唐先生 2026-09-14 23:32 指示 ✓ **必守** ✓）

$$\boxed{R_{\rm residual}\ \text{是【当前审计体系下唯一未关闭的机制类别】}\ ✓}\qquad\textbf{而不是}\qquad\boxed{\text{"不存在其他机制"}\ ✗}$$
$$\qquad\text{理由 ✓（}V140\ \text{自留边界 ✓）}：\text{穷举的是}\textbf{当前定义的 phase-source taxonomy}，\textbf{不是数学宇宙} ✗✓$$

### ⑥e 下一轮搜索对象（✓ 若继续 ✓）

$$\boxed{\text{搜索对象【直接提升】到：}\quad \textbf{Frobenius substitute}\ +\ \textbf{weight-1 host}}$$
$$\qquad\textbf{第一道审计（不是"能不能产生 RH"✗）}：\boxed{\text{在 char 0，是否存在一个}\textbf{不借助 }\zeta\text{-零点定义}\text{、又同时具有【算术膨胀 similitude ＋ 权 1 极化】的 canonical structure？}}$$
$$\qquad\textbf{禁用 ✗}：\text{再沿 cross-scale／fixed-basis／transport 线搜索（`V138`–`V140` 已关闭 ✓）}$$

$$\boxed{\text{ARCHIVE-V128-V140 ✓ ＝ Fourth-Arrow ＋ Cross-scale Closure Audit：三条不可越界标签（① 已证明 ⟹ CLOSED route ✓；② 条件分类：canonical}\not\Rightarrow\text{stable ＋ 稳定即序型 ✓；③ 未证明：}R_{\rm residual}\ne\varnothing\ \text{或}\ =\varnothing\ \text{均未证 ✗）＋ 总入口决策树 ＋ 最高优先级查重规则（}\sqrt{\ }\text{七箱 ⟹ 不能归类才入 }R_{\rm residual}\text{）＋ 九轮清单 ⟹ }\textbf{V137 ＝ SEARCH BRANCH CLOSED}\ ✓\ne\ \text{RH CLOSED}\ ✗}$$
