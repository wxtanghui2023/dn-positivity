# V139 · ⭐⭐⭐⭐⭐ **材料 A ＋ 材料 B 审计：A ⟹ 退回箱 8 ✓（您的三项计算核对通过 ✓）；A_ideal ≡ B ⟹ B 也【双层塌缩 ✓✓】—— 定义层 ＝ Gram 行列式平方根（**按定义即 $D_1$ ✓**）；算术层 ＝ Brauer–Siegel **下界 ＝ GRH 强度 ✗**；架构层 ＝ **C4 失效 ✓✓**（1/2 来自二次型而非 rank/维数）⟹ 数域 discriminant 路线的 $\sqrt{}$ 【也没有独立来源 ✓】**
> 委托 ✓ 唐先生 2026-09-14 23:20（**"先审材料 A；再直接审材料 B：把 $\sqrt{|D_K|}$ 从定义一路剥到最底层"** ✓）
> 查图 ✓ `TWO-SCALE-compatibility-construction-material` §2 **材料 B 逐字即本题 ✓**，且自标"**这部分尚未审计**" ✓；§3 **约束 C1–C5 ✓**（C4 ＝ 1/2 须来自内禀整数 rank/维数 ✗）；§3 末尾 **E3 结构性提醒 ✓**（"守恒律＋交换 ⟹ 固定点"与 E3 重整化不动点**同型**；E3 判"仿射/可调 ⟹ 1/2 可自由插入" ✗）
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓（**且在 §2 指出该路线的 √ 下界恰为 GRH 强度 ✗**）；未跑 Lean ✓｜编号 ✓ V139 ✓

---

## §0 判定（✓ 四条 ✓）

$$\boxed{\text{① 材料 A：您的三项计算【核对通过 ✓】⟹ 标准二维格几何【全部退回箱 8 ✓】}}$$
$$\boxed{\text{② A 的残项（ideal-class／discriminant）【＝ 材料 B ✓】—— 二者汇合 ✓（您 §7 判断正确 ✓）}}$$
$$\boxed{\text{③ 材料 B：【双层塌缩 ✓✓】—— 定义层：}\sqrt{|D_K|}\ \textbf{按定义}就是 trace pairing 的 Gram 行列式平方根 ⟹ }D_1\ ✓✓}$$
$$\boxed{\text{④ ⭐ 本档新增（架构层 ✓✓）}：\text{材料 B 违反其【自身设计约束 C4】✗ —— 其中的}\tfrac12\ \textbf{不是来自 rank/维数}，\text{而是来自 trace form 的【二次性】✗✓}}$$

## §1 材料 A 核对（✓ 三项全过 ✓）

$$\textbf{(1) Smith 不变因子 ✓}：L=d_1\mathbb Z\oplus d_2\mathbb Z\ ✓,\ d_1\mid d_2\ ✓,\ d_1d_2=N\ ✓ \Longrightarrow \text{要 }d_1=d_2=\sqrt N\ \text{须【额外要求】}d_1=d_2\ ✗$$
$$\qquad\text{反例 ✓（您的 ✓）}：N=12\ ⟹ (d_1,d_2)=(1,12),(2,6),(3,4)\ ✓\ \text{—— 指数本身【完全不选】}\sqrt N\ ✗$$
$$\qquad\text{若强行加"最平衡"（}\Delta=|\log(d_1/d_2)|\to\min\ ✓\text{）}⟹ d_1=d_2=\sqrt N\ ✓\ \text{—— 但}\sqrt N\ \text{已来自【二次约束的最优化】}\ ✗（d_1d_2=N\ \&\ d_1=d_2\ ⟹\ d_1^2=N\ ✓）$$
$$\qquad\Longrightarrow\ \boxed{\text{来源 ＝ "乘积固定 ＋ 两向平衡" ＝ AM-GM／二次型 ⟹ }\textbf{箱 8}\ ✗}$$
$$\textbf{(2) 自对偶格 ✓}：L^\vee=\{x:\langle x,L\rangle\subset\mathbb Z\}\ ✓;\ [L^\vee:\mathbb Z^2]=1/N\ ✓;\ \text{任何 }A\in GL_2(\mathbb Z)\ \text{保指数}（\det A=\pm1\ ✓）$$
$$\qquad\Longrightarrow\ \text{self-duality 最终只给 determinant／discriminant 条件 ⟹ }\textbf{quadratic/discriminant 结构 ✗ ⟹ 箱 8／12}✓$$
$$\textbf{(3) Minkowski ✓}：\operatorname{covol}(L)=N\ ✓;\ \lambda_1\lambda_2\asymp N\ ✓;\ \text{若 }\lambda_1=\lambda_2\ ⟹\ \lambda_i\asymp\sqrt N\ ✓$$
$$\qquad\textbf{但整数格允许强各向异性 ✓（您的反例 ✓）}：L=\langle(1,0),(0,N)\rangle\ ⟹\ \lambda_1\asymp1,\ \lambda_2\asymp N\ ✗$$
$$\qquad\Longrightarrow\ \lambda_i\sim\sqrt N\ \textbf{不是算术必然，而是额外的 isotropy 条件 ✗ ⟹ 箱 8 ✓}$$
$$\textbf{小结 ✓（您的表格正确 ✓）}：\begin{array}{c|c}\text{构造}&\sqrt N\ \text{来源}\\\hline\text{Smith}&d_1d_2=N\ \&\ d_1=d_2\ ⟹\ \text{AM-GM}\\\text{二次型／自对偶}&\text{discriminant}\\\text{Minkowski}&\lambda_1\lambda_2\asymp N\ \&\ \lambda_1\sim\lambda_2\ ⟹\ \text{isotropy}\end{array}\ \Longrightarrow\ \textbf{全部需二次／极化／各向同性 ✗}$$

## §2 ⭐⭐ 材料 B：$\sqrt{|D_K|}$ 的四层剥离（✓ 本档核心 ✓）

$$\textbf{第 0 层（定义层 ✓ 决定性 ✓）}：D_K=\det\big(\operatorname{Tr}_{K/\mathbb{Q}}(\omega_i\omega_j)\big)\ ✓$$
$$\qquad\Longrightarrow\ \boxed{\sqrt{|D_K|}\ \textbf{按定义}＝ \text{trace pairing 的 Gram 行列式的平方根}\ ✓✓}\ \Longrightarrow\ \boxed{D_1\ \textbf{由定义即成立 ✗}}$$
$$\qquad\textbf{您 §8 的判死条件 ✓ 在此【被定义本身满足】✓}：\text{"若 }\sqrt{|D_K|}\ \text{只是 }\operatorname{Tr}(xy)\ \text{的 Gram 行列式平方根 ⟹ 直接 }D_1\text{"}\ ✓✓$$
$$\textbf{第 1 层（几何层 ✓）}：\operatorname{covol}(\mathfrak a)=2^{-r_2}\sqrt{|D_K|}\,N(\mathfrak a)\ ✓（\text{`TWO-SCALE` §2 逐字 ✓）—— \text{协体积 ＝ }\textbf{行列式型}（列向量构成的多重线性量 ✓）⟹ \textbf{仍属格兰姆/行列式族 ✗}$$
$$\textbf{第 2 层（"指数 }1/2\text{"的来历 ✓✓ 决定性 ✓）}：\text{若 }\sqrt{}\ \text{来自【维数】，应为 }|D_K|^{1/d}\ （d=r_1+2r_2\ ✓）\ ✗$$
$$\qquad\text{而经典归一化给的是 }|D_K|^{1/2}\ ✓\ —— \textbf{为什么是 }1/2\ ?\ \text{因为 }D_K\ \text{是【二次型】的行列式 ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{约束 C4 失效 ✗✓}：\text{（`TWO-SCALE` §3 原文）"1/2 必须由【对象的内禀整数】(rank／arity／维数) 给出 ✗ ⟹ 此处由【二次性】给出 ⟹ \textbf{违反 C4} ✗}}$$
$$\textbf{第 3 层（算术层 ✓ 特征／分歧）}：\text{二次域中 }D_K\ =\ \text{二次特征的模（fundamental discriminant）✓ —— 确为\textbf{算术对象} ✓；}$$
$$\qquad\text{但其 }\sqrt{}\ \text{进入数学的方式只有两条 ✓}：(a)\ \text{解析类数公式 ✓}；(b)\ \text{Brauer–Siegel 量级 ✓ —— 见第 4 层 ✓}$$
$$\textbf{第 4 层（Brauer–Siegel ✓✓ 决定性 ✗）}：h_K\asymp\sqrt{|D|}\cdot\log|D|\ ✓$$
$$\qquad\textbf{上界 ✓ 无条件 ✓；下界 ✗ \textbf{等价于无 Siegel 零点（⟸ GRH ✓）✗✓}}$$
$$\qquad\Longrightarrow\ \boxed{\text{该路线唯一"非定义性"的机制（两尺度量级竞争 ⟹ 固定尺度）其下界 ＝ }\textbf{GRH 强度 ✗✓}\ —— \text{即【循环】（RH-strength 输入）✓}}$$
$$\qquad\textbf{解析类数公式层 ✓ 亦不独立}：h_KR_K=\frac{w_K\sqrt{|D_K|}}{2^{r_1}(2\pi)^{r_2}}\operatorname{Res}_{s=1}\zeta_K(s)\ ✓\ \text{—— 它}\textbf{把 }\sqrt{|D_K|}\ \textbf{与 }L\ \text{函数绑在一起 ✓，故其"由定理给出"恰恰意味着它经由【解析侧】✗}$$

## §3 材料 A 残项 ＝ 材料 B（✓ 二者汇合 ✓）

$$\text{A 中未由此关闭的 }ideal\text{-}class／discriminant\ \text{结构 ✓}\ \equiv\ \text{材料 B ✓}\ \text{（您 §7 判断正确 ✓）}$$
$$\textbf{故 A 与 B 一并处理完毕 ✓}：\text{A 的标准格几何 ⟹ 箱 8 ✗；A 的理想类部分 ≡ B ⟹ §2 四层塌缩 ✗✓}$$
$$\textbf{E3 结构性提醒核对 ✓}：\text{本形状（守恒律 ＋ 交换 ⟹ 固定点）与 E3 重整化不动点同型 ✓；}\text{`TWO-SCALE` §3 自注 ✓："成败系于 C1/C2"}\ ✓$$
$$\qquad\Longrightarrow\ \text{而本档显示 }\textbf{C4 已然失效 ✗✓}\ \text{（1/2 来自二次性而非维数 ✓）} \Longrightarrow\ \textbf{该路线在其【自身约束】下即不合格 ✗✓✓}$$

## §4 判词（✓ 您要的"更硬结果"成立 ✓✓）

$$\boxed{\textbf{材料 B 塌缩 ✓}\ ——\ \text{不仅 }\mathbb Z^2\ \text{格几何，}\textbf{数域 discriminant 路线的 }\sqrt{}\ \text{也没有独立来源}\ ✓✓}$$
$$\qquad\textbf{两个来源，皆已映射 ✓}：\text{(i) 定义层 ＝ Gram 行列式平方根 ⟹ }D_1\ ✗（\text{您 §5 的 }"polarization/isotropy\ \text{产物}"\ ✓，本档把它变成【定义性等式 ✓】）；\text{(ii) 算术层 ＝ Brauer–Siegel ⟹ 下界 GRH 强度 ✗（循环 ✓）}$$
$$\qquad\textbf{架构层 ✓（本档新增）}：C4 失效 ✓ —— \tfrac12\ \text{不是内禀整数（rank／维数）的产物 ✓，而是【二次型】的签名 ✓（与 }V136\ \text{的"}\sqrt{}=\text{极化签名"}\ \text{完全一致 ✓✓）}$$
$$\textbf{唯一未封项 ⚠️（与您 §8 的预期一致 ✓）}：\textbf{不经 trace pairing 的 }ideal\text{-}class\ compatibility\ defect\ ✗\ —— \text{未找到 ✓，但【未证不存在】✗ ✓}$$
$$\qquad\text{（同纪律 ✓：}\text{"未找到"}\ne\text{"不存在"}\ ✓\ ——\ \text{与 }R_{\rm residual}\ \text{同级 ✓）}$$

## §5 更新与边界（✓）

$$\text{`CLOSED-ROUTES-MAP` §F.3b ✓}：\text{材料 A ⟹ }\textbf{已审 ✓ 退回箱 8};\ \text{材料 B ⟹ }\textbf{已审 ✓ 四层塌缩（含 C4 失效 ✓）};\ \text{故三处未执行项中【两处已关闭 ✗】}，\text{仅剩【修复方向（固定基缺陷）】⛔}$$
```
⚠️ §2 第 4 层的"下界 ＝ GRH 强度"为【结构性/文献级 ✓】（Brauer–Siegel 的标准地位 ✓）
⚠️ §2 第 2 层（C4 失效）为本档新增论证 ✓ —— 其依据是"维数给 1/d、二次性给 1/2"这一形式对比 ✓（II 类证据 ✓）
⚠️ 本档【不】声称 ideal-class 路线不存在新机制 ✗（仅未找到 ✓）
✅ 净产出 ✓：① 材料 A 三项核对 ✓；② 材料 B 四层剥离 ✓✓；③ C1–C5 中 C4 失效的定位 ✓✓；④ E3 提醒核对 ✓；⑤ 两处未执行项关闭 ✓
```
$$\boxed{\text{V139 ✓：材料 A 退回箱 8（Smith 需 }d_1{=}d_2\ ⟹\ \text{AM-GM}；自对偶 ⟹ discriminant；Minkowski ⟹ 需 isotropy，各向异性反例 }\langle(1,0),(0,N)\rangle\ ✓）；\text{A }ideal\ \text{部分 ≡ 材料 B ⟹ 四层剥离：第 0 层 }\sqrt{|D_K|}\ \textbf{按定义}＝trace pairing Gram 行列式平方根 ⟹ }\textbf{定义性地 }D_1\ ✓✓；\text{第 2 层 }\tfrac12\ \textbf{非来自维数}（应为 }1/d\text{）而来自\textbf{二次性} ⟹ \textbf{C4 失效 ✓✓}；\text{第 4 层 Brauer–Siegel 下界 ＝ GRH 强度 ⟹ 循环 ✗✓ ⟹ }\textbf{数域 discriminant 路线 }\sqrt{}\ \text{无独立来源 ✓}；\text{唯一未封 ＝ 非 trace pairing 的 }ideal\text{-}class\ defect\ ⚠️（未找到，未证不存在 ✓）}$$
