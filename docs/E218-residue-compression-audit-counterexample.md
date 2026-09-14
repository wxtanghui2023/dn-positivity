# E218 · ⭐⭐⭐⭐⭐ **residue-compression 审计：命题「$A$ 无限 ⟹ $\sum_p\nu_p/p^2=\infty$」【被证伪 ✗✓】—— 显式反例 $A=\{Q_{2^n}\}$ 使 $\mathcal C(A)<\infty$ ⟹ $B(A)$ 有【正密度 ✓✓】｜但二难转为【量化权衡】✗**
> 依唐先生 2026-09-14 20:19 裁定 ✓（**先统一参数化 ✓；不打散点图 ✗；核心命题：无限 ⟹ $\sum\nu_p/p^2=\infty$ ✓；措辞修正：非"唯一活口"而"当前已知机制中唯一未封类别"✓**）
> 纪律 ✓ 未用 RH ✓；未涉 ζ ✓；未跑 Lean ✓；数值＝numpy（$M=Q^2$ ✓）

---

## §0 精确参数化（✓ 您的框架 ✓，以下为形式化 ✓）

$$\nu_p(A):=\big|\{a\bmod p^2:a\in A\}\big|\ ✓;\qquad \text{单素数局部存活比【精确】}=\ 1-\frac{\nu_p(A)}{p^2}\ ✓$$
$$\text{CRT ✓}：P=\prod_{p\le y}p^2\ \Longrightarrow\ \text{一个完整周期内允许的 }b\ \text{恰为}\ P\prod_{p\le y}\Big(1-\frac{\nu_p}{p^2}\Big)\ ✓$$
$$\Longrightarrow\ \boxed{\text{"相关性"＝各 }p\ \text{上的 residue compression 的乘积 ✓}}\ ✓;\qquad \log\prod_p\Big(1-\frac{\nu_p}{p^2}\Big)=-\sum_p\frac{\nu_p}{p^2}+O\Big(\sum_p\frac{\nu_p^2}{p^4}\Big)$$
$$\Longrightarrow\ \boxed{\textbf{真正的资源是}\ \mathcal C(A)=\sum_p\frac{\nu_p(A)}{p^2}}\ ✓;\qquad \prod_p\Big(1-\frac{\nu_p}{p^2}\Big)>0\iff\mathcal C(A)<\infty\ ✓$$
$$\textbf{极端解释 ✓}：\text{随机 }A\Rightarrow\nu_p\approx\min(k,p^2)\ \text{（约束独立 ✗）};\quad A\subseteq a_0+Q_7\mathbb Z\Rightarrow\nu_p=1\ (p\le7)\ \text{（坍缩 ✓）}$$

## §1 ⭐⭐ 核心命题被【证伪 ✗✓】（✓ 显式反例 ✓）

$$\textbf{待检验命题 ✓}：A\ \text{无限}\ \Longrightarrow\ \mathcal C(A)=\sum_p\nu_p/p^2=\infty\ ✓\ \big(\text{若真 ⟹ }B(A)=\varnothing\ ⟹\ \text{相关性路线全死 ✓}\big)$$
$$\textbf{反例构造 ✓}：\text{取 }P_n=2^n\ ✓,\ a_n:=Q_{P_n}=\prod_{p\le2^n}p^2\ ✓,\ A:=\{a_n:n\ge1\}\ ✓\ \text{（无限 ✓）}$$
$$\qquad\textbf{关键性质 ✓}：n\ge j\ \Longrightarrow\ a_n\equiv0\bmod Q_{P_j}\ ✓\ \text{（因 }Q_{P_j}\mid Q_{P_n}\ ✓）\ \Longrightarrow\ \text{对 }p\le P_j\ ✓,\ \text{所有 }a_n\ (n\ge j)\ \text{同余 }0\ ✓$$
$$\qquad\Longrightarrow\ \nu_p(A)\le j\ \text{对 }p\in(P_{j-1},P_j]\ ✓\qquad\big(\text{仅前 }j-1\ \text{个元素贡献额外残类 ✓}\big)$$
$$\textbf{求和 ✓}：\mathcal C(A)\le\sum_j j\sum_{p\in(2^{j-1},2^j]}\frac{1}{p^2}\le\sum_j j\cdot 2^{j-1}\cdot\frac{1}{4^{j-1}}=\sum_j\frac{j}{2^{j-1}}<\infty\ ✓✓$$
$$\Longrightarrow\ \boxed{\textbf{存在无限 }A\ \text{使 }\mathcal C(A)<\infty\ ⟹\ \prod_p(1-\nu_p/p^2)>0\ ⟹\ \boxed{B(A)\ \textbf{有正密度 ✓✓}}}\ ✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{命题【假 ✗】}：\text{"无限集合必使各区约束饱和"不成立 ✓；}\textbf{residue-compression 路线【未死 ✗】}}\ ✓$$
$$\qquad\textbf{（自纠 ✓）}：\text{我先前误估 }\sum_j j\cdot\pi(2^j)/2^{2j}\ \text{发散 ✗；正确用 }\#\{p\in\text{级}\}\le2^{j-1}\ \text{与 }1/p^2\le2^{-2(j-1)}\ \text{得收敛 ✓✓}$$

## §2 数值验证（✓ 压缩优势确实存在 ✓）

$$\text{塔式 }A=\{0,36,936,45036,89136\}\ ✓（|A|=5\ ✓，递推差 }Q_4,Q_6,Q_7,Q_7\ ✓）$$
```
|B(A)| = 399293 = 0.811|S_M|   ✓✓
随机同尺寸（10 个）：0, 55362, 55365, 58651, 69184, 69227, 74302, 111405, 146541, 148879
⟹ 中位 69205 = 0.141|S| ⟹ 塔式【5.8 倍优势 ✓✓】
ν_p 审计 ✓：ν_2=1, ν_3=1, ν_5=2, ν_7=3, ν_p=5 (p≥11) —— 与"压缩"预测模式一致 ✓
```

## §3 ⚠️ 但二难【未解 ✗】—— 它被【量化】了 ✓✓

$$\text{反例 }A=\{Q_{2^n}\}\ \text{的稀疏度 ✓}：a_n\approx\exp(2\cdot2^n)\ ⟹ \text{在 }[0,M]\ \text{内只有}\ \approx\log_2\log M\ \text{个元素 ✗}$$
$$\qquad M=810000=e^{13.6}\ ⟹ |A\cap[0,M)|=\#\{n:2\cdot2^n\le13.6\}\approx3\ ✗✗$$
$$\textbf{覆盖需求 ✓}：S_M\subseteq A+B\ \text{需 }|A\cap[0,M)|\cdot|B|\gtrsim|S_M|\approx0.6M\ ✓;\quad |B|\approx e^{-\mathcal C(A)}M\ ✓$$
$$\Longrightarrow\ \boxed{\text{需}\ |A\cap[0,M)|\ \gtrsim\ 0.6\,e^{\mathcal C(A)}\ ✓}\quad\textbf{—— 压缩越好（}\mathcal C\ \text{小）⟹ 需要越多元素；而压缩本身要求…元素稀疏 ✗}}$$
$$\qquad\text{本例 ✓}：\mathcal C\approx4\ ✓\ \text{⟹ 需 }|A\cap[0,M)|\gtrsim0.6e^4\approx33\ ✗\ \text{而实有 }\approx3\ ✗\ \text{（差 10 倍 ✗）};\quad 3\cdot e^{-4}M=0.055M\ll0.6M\ ✗$$
$$\qquad\Longrightarrow\ \boxed{\textbf{二难仍未解 ✓，但已从定性变为【定量权衡 ✓】}}\ ✓：\text{需在 }(\mathcal C(A),\ |A\cap[0,M)|)\ \text{平面上找可行区 ✓}$$

## §4 判词（✓）

$$\boxed{\textbf{E218 判词 ✓}：\text{命题 NO（已证伪 ✓）};\ \text{但}\ \textbf{不是"相关性路线死亡"✗ —— 而是转为量化的压缩-覆盖权衡 ✓}}$$
```
✅ 证伪 ✓：无限 A 可保持 C(A)<∞ ⟹ B(A) 正密度（新正面结果 ✓✓）
✅ 数值 ✓：压缩优势 5.8 倍（塔式 0.811|S| vs 随机中位 0.141|S| ✓）
✗ 未解 ✓：覆盖侧需求 |A∩[0,M)| ≳ 0.6 e^{C(A)} 与"压缩要求稀疏"冲突 ✗
⚠️ 措辞修正 ✓（按您 ✓）：非固定模结构是【当前已知机制中唯一未封类别 ✓】，不是"唯一活口"✓
```

## §5 归档补强 + (E219) 建议（✓）

```
【ARCHIVE 层 2 补强 ✓】新增两条：
 · 封死：固定模相关性（E217-B ✓）
 · 未封：非固定模压缩 ✓【本轮证明其存在性 ✓，并量化为 (C(A), |A∩[0,M)|) 权衡 ✓】
★ E219 建议 ✓（唯一明确的下一步）：
   在 (C(A), m=|A∩[0,M)|) 平面审计可行区 ✓：
   ① 对给定 m ✓，最小可能的 C(A) 是多少 ✓？（即 inf_C over |A∩[0,M)|=m ✓）
   ② 反之 ✓：对给定 C ✓，最大可能的 m ✓？
   ③ 判活 ✓：若存在 (C, m) 同时满足 C < ∞ 且 m ≳ 0.6 e^C ✓ ⟹ 覆盖可行 ✓✓
   ④ 判死 ✓：若 inf m over C=O(1) 严格小于 0.6e^C ✓ ⟹ 非固定模路线也封 ✗
   —— 这将是构造侧最后的自由度审计 ✓
```

## §6 边界与一句话（✓）

```
✅ 精确参数化 ✓（ν_p ✓，CRT 乘积 ✓，C(A) ✓）；证伪 ✓（显式反例 + 收敛证明 ✓）；数值 ✓（5.8 倍 ✓）
⚠️ 反例的 C(A) 只有上界估计 ✓（未精确算 ✓）；数值塔式用多项式模数 ✗（仅有限近似 ✓）
⚠️ 不声称覆盖可行 ✗；不声称覆盖不可行 ✗（二难转为定量权衡 ✓）
⭐ 净产出 ✓：① 证伪核心命题 ✓✓（含自纠 ✓）；② 无限 A 可保持正密度 B ✓✓；③ 权衡量化 ⟹ E219 ✓
```
$$\boxed{\text{命题「}A\text{无限⟹}\sum\nu_p/p^2=\infty\text{」【假 ✗】——反例 }A=\{Q_{2^n}\}\ \text{给 }\mathcal C\le\sum_j j/2^{j-1}<\infty\ ✓✓\ \text{⟹ }B(A)\ \text{正密度 ✓✓；数值压缩优势 5.8 倍 ✓；但覆盖需 }|A\cap[0,M)|\gtrsim0.6e^{\mathcal C}\ ✗\ \text{与稀疏性冲突 ⟹ 二难转为【定量权衡】(}C,m)\ ✓\ \text{⟹ E219：在 }(C,m)\ \text{平面审可行区 ✓}}$$
