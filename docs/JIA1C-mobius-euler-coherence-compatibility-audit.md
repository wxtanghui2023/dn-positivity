# 甲-1C — **临界相干构型 vs Möbius／Euler 结构的相容性审计**（反证式）

> 唐先生 2026-09-16 19:32 裁定：开甲-1C；**第一刀不是造新估计**，而是审计
> $$\boxed{\zeta\ \text{的 Euler／Möbius 乘法结构}\ \stackrel{?}{\Longrightarrow}\ \text{排除}\ N^{1/2}\ \text{临界相干构型}}$$
> **纪律**：若退化成二阶相关量或 Euler-product 重写 ⟹ **立即挂回旧档**，不继续优化 ✓
> **措辞纠正（甲-1C-0，采纳）**：不寻找"点态压低"$|D|\ll N^{1/2-\eta}$（与二阶矩冲突）；真正可攻的是
> $$\boxed{\text{ζ 系数是否排除"}\textbf{持续达到}\ N^{1/2}\ \text{大小"的极值构型}}$$

---

## 1. 甲-1C-1：写出 extremiser（唐先生形式）
$$D(t)=\sum_{N<n\le2N}b_nn^{it},\ |b_n|\le1；\ \text{若}\ |D(t_0)|\ge cN^{1/2}\ \text{则旋转相位后}$$
$$\Re\bigl(e^{-i\theta}D(t_0)\bigr)=\sum_n|b_n|\cos(\arg b_n+t_0\log n-\theta)\gtrsim N^{1/2} \Longrightarrow \boxed{b_n\approx e^{-it_0\log n+i\theta}\ \text{在足够多}\ n\ \text{上相位匹配}}$$
$$\Longrightarrow\ N^{1/2}\ \text{不是神秘"随机墙"，而是}\ \textbf{大量单位向量部分相干时自然出现的尺度}✓$$

## 2. ⭐ 甲-1C-2 的**决定性观察**（本档核心）
$$\text{相位场}\quad \varphi_t(n)：＝e^{-it\log n}\ \text{的}\ \textbf{乘法性}：$$
$$\varphi_t(mn)=e^{-it\log(mn)}=e^{-it(\log m+\log n)}=e^{-it\log m}\cdot e^{-it\log n}=\varphi_t(m)\varphi_t(n)$$
$$\Longrightarrow\ \boxed{\varphi_t\ \text{是}\ \textbf{完全乘法函数}}\quad(\text{对}\ \textbf{一切}\ m,n,\ \text{无互素限制})✓$$
$$\textbf{而其"系数侧"的乘法结构}：\ \mu(mn)=\mu(m)\mu(n)\ ((m,n)=1)；\ \text{且}\ n^{-s}\ \text{本身即 Euler 积的局部因子形式}$$
$$\Longrightarrow\ \text{相干要求}\ a_{mn}\approx a_ma_n\ \text{与}\ \varphi_t\ \text{的完全乘法性}\ \textbf{同型} \Longrightarrow \boxed{\text{乘法结构}\ \textbf{不排除} \text{相干，反而}\ \textbf{与之一致}}✓$$

## 3. 三个预注册问题的逐项判定（唐先生 C1／C2／C3）
### C1 相干可实现性 —— **部分可实现（结构层）**
$$\text{取}\ b_n=\mu(n)\ (\text{GM 归一化：}|b_n|\le1\ \text{成立，squarefree 上}\ |b_n|=1)$$
$$\text{相干要求}\ \mu(n)\approx e^{-it_0\log n+i\theta}\ \text{需}\ \text{相位场与}\ \mu\ \text{的符号模式对齐}$$
$$\Longrightarrow\ \textbf{乘法层无矛盾}（\varphi_t\ \text{完全乘法，}\mu\ \text{乘法）}；\ \text{唯一阻碍来自}\ \mu\ \text{的}\ \textbf{符号伪随机性}$$
$$\longrightarrow\ \textbf{C1 判定}：\ \text{结构层}\ \textbf{可实现} \Longrightarrow \text{"ζ 的乘法结构排除 extremiser"}\ \textbf{这条最简单路线 DEAD}✓$$
$$\qquad（\text{唐先生预判的"危险情形"被确证}：\ \text{ζ 的算术结构}\ \textbf{不是排除极值，而是提供其所需的乘法相干}）$$

### C2 乘法闭包是否增强相干 —— **增强（不阻断）**
$$m,n,mn\in S\ \text{时}：\ \varphi_t(mn)=\varphi_t(m)\varphi_t(n)\ \text{恒成立} \Longrightarrow \text{相干}\ \textbf{在乘法下封闭}✓$$
$$\Longrightarrow\ \text{乘法闭包}\ \textbf{保持} \text{相干，}\ \textbf{不产生} \text{"不可实现性"} \Longrightarrow \text{C2 未给出排除}✓$$

### C3 从局部排除到大值集合改善 —— **在}\ \sigma\to1/2\ \text{处被阻断**
$$\text{承接甲-1A §4}：\ V\approx N^{1/2}\ \text{是}\ \textbf{典型量级} \Longrightarrow\ \text{点数}\ R\ \text{可逼近平凡界}\ R\le T \Longrightarrow \textbf{无幂次节省}$$
$$\Longrightarrow\ \text{即使有局部排除，也}\ \textbf{只能给}\ T^{o(1)}\ \text{级改善} \Longrightarrow \textbf{不能移动 density exponent}✓$$

## 4. 残余阻碍的**性质**（关键：它落旧类）
$$\text{唯一可能的阻碍＝}\ \mu\ \text{的}\ \textbf{符号伪随机性}（\text{即"相位场无法与}\ \mu\ \text{的符号模式持续对齐"}）$$
$$\text{而经典事实}：\ \text{RH}\iff M(x)=O(x^{1/2+\varepsilon})\ \text{型}\ (\text{Möbius 求和界})\ ——\ \textbf{[标准事实，本档未重证]}$$
$$\Longrightarrow\ \boxed{\text{该阻碍}\ \equiv\ \text{Möbius 随机性}\ \equiv\ \textbf{RH 等价区}} \Longrightarrow \text{按唐先生纪律}\ \textbf{挂回旧档}✓$$
$$\qquad（\text{不是二阶相关量，也不是 Euler-product 重写，而是}\ \textbf{判据型 RH 等价} \to \text{分类③}）$$

---

## 判定：**甲-1C ＝ DEAD（且是唐先生预言的"干净 DEAD"）**
$$\text{按唐先生预注册决策树}：$$
$$\qquad\text{"关系可实现"分支} \Longrightarrow \boxed{\textbf{该路线 DEAD}}✓$$
$$\textbf{两重理由}：$$
$$\qquad\text{(1) }\textbf{结构层}：\varphi_t\ \text{完全乘法，与 Euler／Möbius 乘法结构}\ \textbf{同型} \Longrightarrow \text{乘法结构}\ \textbf{不排除} \text{相干；}$$
$$\qquad\text{(2) }\textbf{残余层}：\text{唯一阻碍＝Möbius 伪随机性}\ =\ \textbf{RH 等价} \Longrightarrow \text{落旧类（分类③）}✓$$
$$\textbf{且第三重（C3）}：\text{即使排除成立也}\ \textbf{不能} \text{移动 density exponent}（\sigma\to1/2\ \text{处}\ R\ \text{逼近平凡界）}$$

## 由本档得到的**正面**结构性结论（非 NO-GO）
$$\boxed{\text{large-values 路线在临界区（}\sigma\to\tfrac12\text{）的双重封锁}}：$$
$$\qquad\text{(i) }\textbf{尺度重合}：V\approx N^{1/2}\ =\ \text{典型量级} \Longrightarrow \text{无计数节省；}$$
$$\qquad\text{(ii) }\textbf{相干相容}：\text{极值所需相位场}\ \textbf{完全乘法} \Longrightarrow \text{Euler 结构不排除它}$$
$$\Longrightarrow\ \text{因此这条路线的天花板}\ \textbf{不是技术不足，而是}\ \text{(i)+(ii)}\ \text{的结构性重合}✓$$

## 边界（N1/N2 严守）
$$\text{① §2 的乘法性观察为}\ \textbf{初等且决定性}（\text{本档计算}）✓；\quad\text{② RH}\iff M(x)\ \text{界为}\ \textbf{[标准事实]，未重证}；$$
$$\text{③ §3 C3 承甲-1A §4 的}\ \textbf{[结构判定]}；\quad\text{④ }\textbf{未用 RH}；零数值（\text{仅指数与乘法性演算}）✓}$$

## 净产出
$$\text{(i) extremiser 写成相位匹配形式（}\ b_n\approx e^{-it_0\log n+i\theta}\ ）；$$
$$\text{(ii) ⭐ 决定性观察：相位场}\ \varphi_t(n)=n^{-it}\ \textbf{完全乘法}\ \Longrightarrow\ \text{乘法结构}\ \textbf{与相干同型，不排除之}；$$
$$\text{(iii) C1／C2／C3 逐项判定：C1 结构层可实现（最简单路线 DEAD）；C2 乘法闭包加强相干；C3 在}\ \sigma\to1/2\ \text{被阻断；}$$
$$\text{(iv) 残余阻碍＝Möbius 伪随机性＝}\textbf{RH 等价}\Longrightarrow \text{挂回旧档（分类③）}；$$
$$\text{(v) 判定}\ \textbf{DEAD}（\text{干净 DEAD）＋正面双重封锁结论（尺度重合＋相干相容）。}$$
