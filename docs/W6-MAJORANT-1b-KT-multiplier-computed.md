# ⚔️ W6-MAJORANT-1b · **$K_T$ 的乘子计算**：裸 Hilbert 障碍**不迁移**

> 依唐先生 12:27 指令：**下一刀＝算 $K_T$ 的 Fourier multiplier，而不是再写一遍 MV** ✓
> 已查地图 ✓｜承接 `W6-MAJORANT-1`（卡点＝MV 步）✓

---

## §1 目标（唐先生给定的算子形式）
$$B(x,z;H)=\sum_{n\ne m}x_n\overline{z_m}H(y_n-y_m),\qquad H(t)=\frac{1}{it}✓$$
$$\text{MV（Lemma 2.2）用的是}\ |B|\le\frac{\pi}{\delta}\|x\|_2\|z\|_2\ \text{＋}\ \delta_n^{-1}\le2n✓$$
$$\textbf{唐先生两步结论（本档采纳）}：\text{① 点态 majorant 不够}（H(-t)=\overline{H(t)}，\widehat H\propto\mathrm{sgn}(\xi)）⟹ \text{须}\ \textbf{二次型序}\ K_+-H\succeq0✓✓$$
$$\qquad\text{② 若}\ \mathrm{supp}\widehat{K_+}\subset[-S,S]\ \text{则}\ |\xi|>S\ \text{处}\ \widehat{K_+}-\mathrm{sgn}=-\mathrm{sgn}\ \textbf{不能非负} ⟹ \textbf{裸 Hilbert 无有限带宽 PSD majorant}✓✓✓$$
$$\textbf{③ 唐先生猜测}：\text{但 Prop 5.4 里出现的不是裸}\ H，\text{而是带}\ T\text{-相位的完整}\ K_T；\ T\text{-相位可能把 sign 乘子}\ \textbf{平移到有限频带附近}✓✓$$

---

## §2 ⭐⭐⭐ **本档计算：$K_T$ 的相位频带（结果：猜测成立）**

$$\text{原式（`W6-MAJORANT-1 §2.3`）}：O_1=\frac{1}{2\pi^2}\mathrm{Re}\sum_{n\ne m}\frac{a_na_m}{i\,t}\Big[\underbrace{e^{2iTt}}_{\rm I}(\alpha_m^++\alpha_n^-)-\underbrace{e^{iTt}}_{\rm II}(\alpha_n^++\alpha_m^-)\Big],\qquad t:=y_n-y_m✓$$
$$\alpha_n^+=\int_0^{T}\Phi(x)^2e^{iy_nx}dx,\qquad \alpha_n^-=\int_{-T}^{0}\Phi(x)^2e^{iy_nx}dx✓$$

$$\text{把}\ t=y_n-y_m\ \text{代回，四项各写成}\ \int\Phi^2\,e^{i[p\,y_n+q\,y_m]}dx\ \text{形式}：$$

| 项 | 指数 | $p$ | $q$ |
|:--|:--|:--|:--|
| $\rm I\cdot\alpha_m^+$ | $e^{i[2Ty_n+(x-2T)y_m]}$，$x\in[0,T]$ | $2T$ | $x-2T\in[-2T,-T]$ |
| $\rm I\cdot\alpha_n^-$ | $e^{i[(2T+x)y_n-2Ty_m]}$，$x\in[-T,0]$ | $2T+x\in[T,2T]$ | $-2T$ |
| $\rm II\cdot\alpha_n^+$ | $e^{i[(T+x)y_n-Ty_m]}$，$x\in[0,T]$ | $T+x\in[T,2T]$ | $-T$ |
| $\rm II\cdot\alpha_m^-$ | $e^{i[Ty_n+(x-T)y_m]}$，$x\in[-T,0]$ | $T$ | $x-T\in[-2T,-T]$ |

$$\Longrightarrow\ \boxed{\textbf{四项全部满足}\ p\in[T,2T],\qquad -q\in[T,2T]}✓✓✓$$

$$\text{再作}\ (y_n+y_m,\ y_n-y_m)\ \text{分解}：py_n+qy_m=\tfrac{p+q}{2}(y_n+y_m)+\tfrac{p-q}{2}\,t$$
$$\Longrightarrow\ \text{每项}\ =\ e^{i(p+q)\bar y}\cdot\frac{e^{i\omega t}}{i\,t},\qquad \omega:=\frac{p-q}{2}✓$$
$$\text{乘子}\ =\ \textbf{平移的 sign}\ \mathrm{sgn}(\xi-\omega)\ \text{（在}\ t\text{-侧）}✓$$

$$\text{四类的平移}\ \omega：\ \rm I\cdot\alpha_m^+:\ 2T-\tfrac x2\ (x\in[0,T])\in[\tfrac{3T}{2},2T];\quad \rm I\cdot\alpha_n^-:\ 2T+\tfrac x2\ (x\in[-T,0])\in[\tfrac{3T}{2},2T]$$
$$\qquad \rm II\cdot\alpha_n^+:\ T+\tfrac x2\ (x\in[0,T])\in[T,\tfrac{3T}{2}];\quad \rm II\cdot\alpha_m^-:\ T-\tfrac x2\ (x\in[-T,0])\in[T,\tfrac{3T}{2}]$$
$$\Longrightarrow\ \boxed{\text{全部平移}\ \omega\in[T,\,2T]\quad\text{（带宽恰}\ \asymp T\text{，且与窗口长度对齐）}}✓✓✓$$

---

## §3 ⭐⭐⭐ 结论：**裸 Hilbert 障碍不迁移 ⟹ 路线重开**

$$\text{裸}\ H=1/(it)：\text{乘子}\ \propto\mathrm{sgn}(\xi)\ \textbf{延展到所有频率} ⟹ \text{无有限带宽 PSD majorant}✓$$
$$\text{实际}\ K_T：\text{乘子＝四个}\ \textbf{被}\ \Phi^2\ \textbf{抹平} \text{的平移 sign，}\textbf{全部跳变落在}\ [T,2T]✓✓$$
$$\Longrightarrow\ \boxed{\text{在}\ [T,2T]\ \text{之外，全部四个 sign 取值}\ \textbf{同号（常数）} ⟹ \text{目标乘子在那里是}\ \textbf{常数}}✓✓$$
$$\qquad\Longrightarrow\ \text{取}\ \mathrm{supp}\widehat{K_+}\supset[T,2T]\ \text{并在外部}\ \widehat{K_+}=0：\text{外部要求}\ 0\ge\widehat{K_T}=0\ \textbf{自动满足}✓✓$$
$$\qquad\Longrightarrow\ \boxed{\textbf{唐先生②的障碍在}\ K_T\ \textbf{上不存在}} ⟹ \textbf{对偶正性 majorant 路线}\ \textbf{未被判死}}✓✓✓$$

## §4 剩下的**定量**问题（唐先生的两路判据，照录）
$$\text{须把窗口从}\ X\lesssim TL\ \text{推到}\ X=T^{1+\eta},\ \text{即压低}\ \frac{|O_1|}{D}\asymp\frac{X}{TL}\to\boxed{\frac{T^\eta}{L}}\asymp\boxed{\frac{T^\eta}{\log T}}✓✓$$
$$\Longrightarrow\ \textbf{绝非常数优化}（\pi\to0.9\pi\ \text{无意义）；须}\ \textbf{幂级改善}✓✓$$
$$\textbf{FALSE 路径}：\text{任何有限带宽 PSD majorant 皆}\ \|K_+\|_{\rm dual}\gtrsim\frac1\delta\（\text{MV 已达同阶最优}）⟹ \text{关闭}✓$$
$$\textbf{ALIVE 路径}：\exists K_+\ \text{使}\ \|K_+\|_{\rm dual}\le\frac1\delta T^{-\eta}\ \text{或任何足以补偿}\ \frac{T^\eta}{\log T}\ \text{的因子}✓$$

## §5 下一刀（**唯一**）
$$\boxed{\text{算}\ K_T\ \text{在}\ [T,2T]\ \text{内的}\ \textbf{精确抹平乘子}\（\Phi^2\ \text{权重＋窗口测度）\ ＋其}\ \textbf{extremal majorant 误差}}✓✓$$
$$\qquad\text{即：}\ \text{在带宽}\ S\asymp T\ \text{的频带上，对被}\ \Phi^2\ \text{抹平的平移 sign 求最优 PSD majorant 的}\ L^1/\text{dual 误差}✓$$
$$\qquad\text{若该误差}\ \gtrsim T^{-\eta}\ \text{级（}\eta\ \text{不足）} \Longrightarrow \textbf{FALSE}；\ \text{若}\ \lesssim T^{-1}\ \text{级} \Longrightarrow \text{再核算术侧饱和性}✓✓$$

## §6 边界
$$\text{(i)}\ §2\ \text{为本档计算（初等相位记账，可逐行核）}✓\quad\text{(ii)}\ §1\ \text{的三条结论照录唐先生 12:27}✓$$
$$\text{(iii)}\ §4--§5\ \text{的 extremal 误差}\ \textbf{本轮未算}✓\quad\text{(iv)}\ \textbf{未用 RH／HL／pair correlation}；\ \textbf{零数值}✓$$
