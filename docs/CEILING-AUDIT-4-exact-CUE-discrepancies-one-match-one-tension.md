# 🔍 **审前沿天花板（第四步）**：近-CUE 数据的偏差量**精确算出** —— **一处吻合** ✓ ＋ **一处张力** ⚠️

> 依唐先生 14:35「继续」执行 (γ) 第一刀（可精确算的那一半）✓
> **本档＝实跑结果**（`fractions.Fraction` 精确有理数，$j=1..256$ 全验）✓✓

---

## §1 ⭐ 闭式（本档推出，并**精确验证通过**）
$$\text{若}\ S(j)=\frac{j}{N}：\quad T_j=\frac{j(j+1)}{2N},\qquad U_j=\frac{j(j^2-1)}{6N}✓$$
$$\Longrightarrow \boxed{\mathrm{Dright}_j=+\frac{j}{2N^2},\qquad \mathrm{Dleft}_j=-\frac{j}{2N^2},\qquad \mathrm{Egrid}_j=-\frac{j}{6N^3}}✓✓$$
$$\text{验证}：\text{对}\ j=1..256\ \text{逐条精确比对} \Longrightarrow \boxed{\textbf{True}}✓✓\qquad(\text{无一处不符})✓$$

## §2 由闭式得到的界（$N=256$，精确有理数）
$$\max_j|\mathrm{Dright}|=\max_j|\mathrm{Dleft}|=\frac{1}{2N}=\frac{1}{512}=0.001953125✓$$
$$\max_j|\mathrm{Egrid}|=\frac{1}{6N^2}=\frac{1}{393216}=\boxed{2.5431315104\ldots\times10^{-6}}✓✓$$
$$|D(1)|=\Big|\frac{T_N}{N}-\frac12\Big|=\frac{1}{2N}=\frac{1}{512}✓\qquad |E(1)|=|\mathrm{Egrid}_N|=\frac{1}{6N^2}✓$$
$$\sup|E|\le\frac{1}{6N^2}+\frac{1}{2N^2}=1.0172526\times10^{-5}✓$$

## §3 ⭐⭐ **吻合**（强证据）
$$\text{前沿天花板陈述里的}\ \textbf{stability 系数逐字}：0.824|r(1)|+2.55\times10^{-6}|r'(1)|+\int_0^1|r''|✓$$
$$\text{而本档算出}\quad\max_j|\mathrm{Egrid}_j|=\frac{1}{6N^2}=2.5431\times10^{-6}\quad\Longleftrightarrow\quad\text{前沿}\ 2.55\times10^{-6}✓✓✓$$
$$\Longrightarrow \boxed{\text{前沿的}\ 2.55\times10^{-6}\ \text{系数}\ \textbf{正是}\ \frac{1}{6N^2}\ \text{（近-CUE 网格的}\ E\ \text{上确界）}}✓✓✓$$
$$\qquad ⭐\ \text{这}\ \textbf{独立确认} \text{了：}\text{(i) 我的闭式正确；\ (ii) 前沿的证书确实按}\ S(j)=j/N\ \text{的近-CUE 数据标定}✓✓$$

## §4 ⚠️ **张力**（登记，不结论）
$$\text{前沿}\ \texttt{RowCert}\ \text{逐字}：|256S(j)-j|\le\tau:=3/10^{40}\ \textbf{且}\ |D(1)|\le82395317/10^8=0.82395317✓$$
$$\text{但本档算出}：\text{若}\ S(j)=j/256\ \text{则}\ |D(1)|=\frac{1}{2N}=\frac{1}{512}\approx0.00195✓$$
$$\Longrightarrow \boxed{0.8239\ \text{vs}\ 0.00195\ ——\ \textbf{相差约}\ 422\ \text{倍}}✓\ ⚠️$$
$$\text{三种可能}：\text{(i)}\ \texttt{RowCert}\ \text{的}"D(1)"\ \text{与}\ \texttt{Defs.lean}\ \text{的}\ \texttt{Dfun}(1)\ \textbf{归一化不同}（\text{极可能：前者或按}\ S\ \text{未除}\ N）✓✓$$
$$\qquad\text{(ii)}\ \text{网格索引／端点约定不同}（j=0..N\ \text{vs}\ 1..N）✓\quad\text{(iii)}\ \text{真实不一致}✓$$
$$\Longrightarrow \textbf{登记为待解项}（\text{需读}\ \texttt{RowCert.lean}\ \text{的定义段即可判}）✓✓$$

## §5 判词
$$\boxed{\text{① 近-CUE 偏差闭式}\ \textbf{已精确建立并验证}}✓✓✓$$
$$\boxed{\text{② 与前沿}\ 2.55\times10^{-6}\ \textbf{强吻合} \Longrightarrow \text{证书确实按近-CUE 标定}✓✓}$$
$$\boxed{\text{③ 新登记张力：}\ |D(1)|\ \text{的}\ 422\ \text{倍差（}\text{最可能为归一化约定差异）}✓}$$
$$\boxed{\text{④ 下一步可做}：\text{读}\ \texttt{RowCert.lean}\ \text{定义段} \Longrightarrow \text{判定张力性质}（\text{一次读取}）✓✓}$$

## §6 边界
$$\text{(i)}\ §1--§2、§4\ \text{的左式为}\ \textbf{实跑结果}（\text{精确有理数}）✓✓\quad\text{(ii)}\ §3／§4\ \text{的右式为前沿逐字}✓$$
$$\text{(iii)}\ \textbf{未用 RH}；\ \textbf{未取 JSON}；\ \textbf{不声称前沿有错}（\text{只登记张力}）✓✓$$
