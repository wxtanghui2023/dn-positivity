# V185 · ⭐⭐⭐⭐⭐ **论文精读：`More than two thirds of the zeros of the Riemann zeta function are simple and on the critical line`（arXiv:2608.13637v2, 2026-08-24, 21 页）**

> 唐先生指示 ✓ 2026-09-15 12:49：**"你先把论文好好看一下"**
> 阅读来源 ✓ arXiv HTML v2（§1–§2）＋ 本地已克隆的形式化 `~/lean-repro/formal-math/zeta23/`（`README.md`、`Zeta23/LinAlg/RankTrace.lean`、`Zeta23/PairCeiling/Ceiling.lean` 等，docstring 逐句对应论文 LaTeX 标签）
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓｜编号 ✓ **V185**

---

## §0 一句话

$$\boxed{\text{把 Montgomery 1973 的"RH 条件下"推论}\ \textbf{变成无条件} —— \text{用}\ \textbf{惯性／秩-迹}\ \text{取代}\ \textbf{正性},\ \text{把 Weil 形式的有限压缩当矩阵来数符号}}$$

$$\text{结果}：N_0^s(T,2T)\ge\bigl(\tfrac23-o(1)\bigr)N(T,2T)\ \（\text{原纪录 }\tfrac5{12}\bigr）;\quad N_d\ge\bigl(\tfrac56-o(1)\bigr)N\ \（\text{原纪录 }0.6603\bigr）;\ \text{MT 窗}：0.67250／0.83625$$

---

## §1 精确设置与结果

$$\text{记 }m_\rho\ \text{为重数};\ N(T_1,T_2)=\sum_{T_1<\gamma\le T_2}m_\rho\（\text{带重数}）,\ N_d=\#\{\rho\},\ N_0^*=\#\{\beta=\tfrac12\},\ N_0^s=\#\{\beta=\tfrac12,m_\rho=1\}$$
$$\textbf{定理 A}：(i)\ N_0^s(T,2T)\ge(\tfrac23-o(1))N(T,2T);\quad (ii)\ N_d(T,2T)\ge(\tfrac56-o(1))N(T,2T)$$
$$\qquad\text{用 MT 窗 }\psi_{\rm MT}\ \text{换掉指示窗 }\psi_0\ \text{后}：2-c_{\rm MT}^{-1}=0.67250\ldots\ \text{与}\ \tfrac12(3-c_{\rm MT}^{-1})=0.83625\ldots,\ \text{其中}\ c_{\rm MT}^{-1}:=\tfrac12+\tfrac1{\sqrt2}\cot\tfrac1{\sqrt2}$$
$$\qquad ⭐\ \text{该窗在该类中}\textbf{最优}（[CCLM17, Cor. 14]）;\ \text{更广的"带宽一证书"类天花板}\approx0.6820\（\text{§7.2}\bigr）$$
$$\qquad\text{同式对 }(0,T)\ \text{成立，速率 }O(\log\log T/\log T)\ \text{（Remark 6.1）};\qquad \textbf{定理 B}：\text{对任意固定原初 Dirichlet 特征 }L(s,\chi)\ \text{逐字成立}$$
$$\qquad ⚠️\ \text{RH 下 }0.6792\ \text{（对 }N^s/N）\text{由半正定规划利用 }\textbf{form factor 在 }[-1,1]\ \textbf{之外}\ \text{的正性得到（[CGdL20]）——}\textbf{本方法不进入该区域} ✓（\text{即：两条路不重叠}）$$

---

## §2 机制（逐步骤，✓ 论文 §1.2＋§2）

### 2.1 构造：**调制窗的 Gabor 框架**（这正是"有限压缩"）

$$\text{取窗 }\psi\（\text{如指示 }\psi_0\ \text{或 MT 窗}\bigr),\ \text{令 }\phi(u):=\chi(\tfrac L2+u)\chi(\tfrac L2-u)\psi(u/L)^{1/2},\ L=\log\tfrac T{2\pi},\ X=e^L$$
$$\qquad\Longrightarrow\ \phi\in C_c^2,\ \operatorname{supp}\phi=[-\tfrac L2,\tfrac L2],\ \operatorname{supp}(\phi*\phi)\subset[-\log X,\log X]$$
$$\text{等间距调制点 }\alpha_k:=T+\tfrac{2\pi k}{L}\ (0\le k<d:=\lfloor LT/(2\pi)\rfloor),\ \text{故 }d=N(T,2T)+O(L)$$
$$\text{对每个零 }\rho：v_\rho:=\bigl(\widehat\phi(\gamma_\rho-\alpha_k)\bigr)_{0\le k<d}\in\mathbb C^d\ ——\ \textbf{这就是把 Weil 形式压进}\ d\ \text{维}$$
$$\widetilde G:=\frac1{aL^2}\sum_{\Re\gamma_\rho\in I'}m_\rho v_\rho v_\rho^{\mathsf T},\quad P:=\frac1{aL^2}\sum_{\rho\in\mathrm{on}}m_\rho v_\rho v_\rho^{\mathsf T},\quad Q:=\widetilde G-P,\quad a:=\|\phi\|_2^2/L$$
$$\qquad\textbf{Poisson–Gabor 恒等式（Lemma 2.1）}：\sum_{k\in\mathbb Z}\widehat\phi(z-\alpha_k)\widehat\phi(z'-\alpha_k)=L\widehat{\phi^2}(z-z')$$

### 2.2 三步（Z）／（P）／（L）与那条**单链**

$$\textbf{(Z) 零侧：签名与秩}：\text{给定 }s_1,s_2,p\（\text{简单在线上／多重在线点／离轴对}\bigr）：\operatorname{tr}P\le N_0,\ n_+(Q)\le p,\ N\ge s_1+2s_2+2p,\ \operatorname{tr}\widetilde G=(1+o(1))N$$
$$\qquad ⭐\ \textbf{功能方程把离轴零点成对配}\ \{\rho,1-\bar\rho\}\ \Longrightarrow\ \text{每对给 }Q\ \text{一个}\ \textbf{签名 }(1,1)\ \text{的 block};\ \text{每个在线点给 }P\ \text{一个非负 rank-one} ✓$$
$$\qquad ⚠️\ \text{与我们的旧结论对照}：\text{我们 }V147／V148／V174\ \text{把功能方程当作"对合／无单边律／选择难题"};\ \text{本文把它当作}\ \textbf{计数装置}（\text{用 block 签名数离轴对}）——\ \textbf{用法相反} ✓✓$$
$$\textbf{(P) 素数侧：Hilbert–Schmidt 范数无条件}：\|\widetilde G\|_{\rm HS}^2=\bigl(R(\psi)+o(1)\bigr)N,\quad R(\psi_0)=\tfrac43,\ R(\psi_{\rm MT})=c_{\rm MT}^{-1}$$
$$\qquad ⭐\ \text{这就是}\ \textbf{Montgomery 的无条件素数侧二阶矩}（[Mon73], [Ary22], [BGSTB24]）——\ \text{带宽}\le1 ✓✓$$
$$\textbf{(L) 秩-迹不等式（Lemma R，§3，精确形式）}：P\succeq0,\ \operatorname{rank}P\le r,\ n_+(Q)\le b\ \Longrightarrow\ \forall c>0：$$
$$\qquad\boxed{\ \|P+Q\|_F^2\ \ge\ c\cdot\operatorname{tr}P-\tfrac{c^2}{4}r\ +\ 2c\cdot\operatorname{tr}Q-c^2b\ }$$
$$\qquad\text{证明骨架}：Q=Q_+-Q_-\ \text{谱正负部分};\ \|\cdot\|_F^2\ \text{展开};\ \text{弃掉 }\operatorname{tr}(PQ_+)\ge0;\ \text{关键一步用}\ \textbf{von Neumann 迹不等式};\ \text{两个初等序列估计收尾} ✓$$
$$\qquad ⚠️\ \text{von Neumann 迹不等式与 Sylvester 惯性定律}\textbf{两个方向}\ \text{此前不在 Mathlib} ⟹ \text{本形式化}\textbf{贡献}了它们 ✓$$

$$\textbf{⭐ 单链（论文 (1.2)）}：\quad N_0^s+o(N)\ \ge\ \operatorname{rank}P_1\ \ge\ 4\operatorname{tr}\widetilde G-2N-\|\widetilde G\|_{\rm HS}^2\ =\ \bigl(2-R(\psi)-o(1)\bigr)N$$
$$\qquad\text{第一不等号＝Prop 4.1};\ \text{第二＝(L)}\ \text{配 (Z) 的}\ \operatorname{tr}P_1+2n_+(Q')\le N;\ \text{等式＝(Z)}\wedge\text{(P)}$$
$$\qquad\text{取 }\psi=\psi_0\ \text{得 }\tfrac23;\ \text{取 }\psi_{\rm MT}\ \text{得 }0.67250 ✓$$
$$\textbf{互异零点（(ii)）}：\text{重排第二步给}\ 3s_1+4(s_2+p)\ge(4-R(\psi))N;\ \text{减去}\ s_1+2s_2+2p\le N ⟹ 2(s_1+s_2+p)\ge(3-R(\psi))N ⟹ N_d\ge\tfrac12(3-R(\psi)-o(1))N$$
$$\qquad ⭐\ (1.1)\ \text{是}\ m^2\ge2m-1\ \text{的矩阵形式};\ \text{把简单零点放秩侧、多重零点按"平 charge"4，即恢复}\ m^2\ge3m-2 ✓$$

---

## §3 解析输入清单（⭐ 反直觉，对我们重要）

$$\text{Weil 显式公式};\quad \text{Riemann–von Mangoldt};\quad N(t,t+1)\ll\log t;\quad \Gamma'/\Gamma\ \text{的 Stirling 估计};\quad \text{Chebyshev–Mertens}（\textstyle\sum_{n\le X}\Lambda(n)^2,\ \sum\Lambda(n)^2/n）;\quad \text{Montgomery–Vaughan 不等式}（\text{频率 }\{\log n\},\ X\le T）$$
$$\boxed{\textbf{不用}\ \text{mollifier};\ \textbf{不用}\ \text{零点密度估计};\ \textbf{不用}\ \text{零自由区}} ✓✓$$
$$\qquad ⚠️\ \text{这与我们此前的假设}\textbf{不同}：\text{我们以为要比 }\tfrac{5}{12}\ \text{更远必须靠 mollifier 加长／零点密度／三阶矩};\ \text{本文}\textbf{完全绕开} —— \text{靠"矩阵惯性"把无条件素数侧二阶矩的}\unicode{x0020}\textbf{全部}\ \text{价值榨干} ✓✓$$

---

## §4 天花板与**量化路线图**（⭐ 本档对我方最有用的一条）

$$\text{Remark 1.1}：\text{只读}\ \textbf{带宽一}\ \text{数据、且}\ \textbf{逐配置}\ \text{成立的证书，}\textbf{无法认证超过}\ \boxed{0.68185}\ \text{的简单零点比例};\ \tfrac23\ \text{距该类天花板仅 }0.016$$
$$\qquad ⭐⭐\ \text{所以"到 1 的剩余差距是}\textbf{结构性的}"：\text{用同一路线要达到}\ 0.70／0.80／0.90，\ \text{需要 Fourier 支撑大约到}\ \boxed{1.04／1.26／1.70},\ \textbf{超出已知范围} ✓✓✓$$
$$\qquad\text{形式化侧}：`PairCeiling/Ceiling.lean`\ \text{给出抽象天花板定理}：\text{若证书 }(c_0,r)\ \text{在某配置（质量 }s_j\ \text{于 }j/N,\ \text{简单点比例 }p_1）\ \text{上有效}：c_0+\sum_js_jr(j/N)\le p_1,\ \text{则}$$
$$\qquad\qquad v:=c_0+\int_0^1r(x)x\,dx\ \le\ p_1+|r(1)||D(1)|+|r'(1)||E(1)|+\sup|E|\int_0^1|r''|$$
$$\qquad\text{实例＝显式 256-周期极值律}：\text{天花板}\ 0.6818287+2.55\times10^{-6}(|r'(1)|+\int|r''|);\ \text{唯一显示假设}=\texttt{EnclOK}（256\ \text{个整数包络}）✓$$

---

## §5 与我们地图的对齐（✓ 三条）

$$\textbf{(1) 我们的"0.682 天花板"}\ \textbf{被独立确认为定理}：\text{本文 }\boxed{0.68185}\（\text{形式化 }\boxed{0.6818287}\bigr）⟹ \text{我们 }\text{`V162`}\ \text{的 }0.682\ \text{不是传闻，是}\textbf{该类的硬上限} ✓✓$$
$$\textbf{(2) 我们的"support}>1\ \text{墙"}\ \textbf{被量化}：\text{要 }0.70／0.80／0.90\ \text{需支撑到 }1.04／1.26／1.70\ \text{——}\ \text{这正是我们 }\text{`V162`}／A3\ \text{所说的缺口，现在有}\textbf{数字} ✓✓✓$$
$$\textbf{(3) 机制类型}\ \textbf{我们从未出现}：\text{不是正性、不是计数、不是相消，而是}\ \boxed{\textbf{惯性／签名}\（\text{Sylvester}\bigr）+\ \textbf{秩-迹}\（\text{von Neumann}\bigr）} —— \text{而"rank}\ (\text{非负部分})\ \text{被}\ \textbf{下界}"\ \text{把"零点侧未知量"变成"可数} ✓✓✓$$

---

## §6 本档认为对我们最关键的三个"新东西"

$$\textbf{(N1) 功能方程的"计数化"用法} ✓✓：\text{离轴对}\{\rho,1-\bar\rho\}\ \text{给签名}\ (1,1)\ \text{的 block} ⟹ \text{用}\ \textbf{负惯性}\ \text{数离轴零点};\ \text{这与我们"对合 ⟹ 无单边律／选择难题"的旧读法}\textbf{相反} ✓✓$$
$$\textbf{(N2) "秩下界"作为目标函数} ✓✓：\text{不去证正性（不可能），而去}\textbf{下界一个秩};\ \text{秩可由}\ \operatorname{tr}\ \text{与}\ \|\cdot\|_{\rm HS}^2\ \text{夹住} —— \text{而后者恰是}\ \textbf{无条件可算的素数侧量} ⟹ \text{把"未知的零点几何"挤出可证不等式} ✓✓✓$$
$$\textbf{(N3) 输入清单的"减法"惊人} ✓✓：\textbf{无 mollifier／无零点密度／无零自由区};\ \text{只靠 Weil 显式公式 ＋ RvM ＋ Stirling ＋ Chebyshev–Mertens ＋ Montgomery–Vaughan} ⟹ \text{说明"带宽一"信息的价值此前被}\textbf{低估} ✓✓$$

---

## §7 出场与形式化（★ 与我们的工作方式对照）

$$\text{数学论证由}\ \textbf{Claude 自主发现并撰写};\ \text{署名作者（Alpöge, Furman）}\textbf{验证并负责};\ \text{Jarred Sumner 提问题并引导};\ \text{Eric Easley 组织 Lean 形式化};\ \text{Conrey／Goldston 复核}$$
$$\qquad ⭐\ \textbf{全部 Lean 代码由 Claude 撰写}（\text{含 }`LinAlg/`\ \text{的 }\texttt{RHLinalg}）;\ \text{作者}\textbf{不手写 Lean};\ \text{论文作者负责数学方向与审阅}$$
$$\qquad\text{工具链}\ \texttt{lean4:v4.33.0-rc2}\ +\ \text{Mathlib}\ \texttt{51e6992}\（\text{tag }v4.33.0-rc2）;\ 17\ \text{条定理}\ \text{sorry-free};\ \#\text{print axioms}\ \text{仅}\ \texttt{propext/Classical.choice/Quot.sound}$$
$$\qquad\text{校验}\：\text{Comparator（Lean FRO）＋ NanoDa 独立内核}\ \text{重放};\ \text{Palomar 注册表投稿};\ \text{CI 对每个 }\texttt{comparator*.json}\ \text{跑同一套}$$
$$\qquad ⚠️\ 1.0\ \text{版的"C-S 较弱形式"}\（N_0^s/N\ge\tfrac12,\ N_d/N\ge\tfrac34\ \text{等}\bigr）\ \text{仍在库中可证 ✓}$$

---

## §8 诚实边界

$$\textbf{(i)}\ \text{本文}\textbf{不}\text{证明 RH};\ \text{比例法}\textbf{结构性}\text{达不到 1}（\text{天花板 0.682}\bigr）⟹ \text{到 1 需要}\ \textbf{带宽}>1\ \text{的新输入（我们墙）} ✓$$
$$\textbf{(ii)}\ \text{天花板}\ 0.6818287\ \text{依赖}\ \textbf{一个}\ \text{外部数值包络假设}\ \texttt{EnclOK}（256\ \text{个整数区间},\ \text{由区间算术自精确有理证书得到}）;\ \text{其余}\ \text{在核内 decide 验证} ✓$$
$$\textbf{(iii)}\ \text{本档仅为}\ \textbf{阅读笔记};\ \text{未独立复核任何证明步骤，}\text{亦未复现 Lean 构建} ✓$$
$$\textbf{(iv)}\ \text{"}\textbf{UV 型/数值匹配}"\text{与"}\textbf{逐点同一}"\text{的区别}\ \text{仍适用（参 }V165\ T3）;\ \text{本文结论}\textbf{不}\text{依赖任何"谱=零点"声称} ✓$$

```
⚠️ 论文为【外部内容 ✓】（arXiv:2608.13637v2，2026-08-24，21 页）；本档为阅读笔记，未独立复核
⚠️ §2 公式取自论文 §1.2／§2 与本地形式化 docstring（`RankTrace.lean` Lemma R 精确形式、`Ceiling.lean` 抽象天花板）
⚠️ §4 量化路线图（1.04／1.26／1.70）取自论文 Remark 1.1 原文
⚠️ §5 与本项目地图（0.682／support>1）的对齐为【本档判断 ✓】
⚠️ §7 出场信息（Claude 自主发现、全部 Lean 由 Claude 撰写、Comparator／NanoDa／Palomar）取自论文致谢＋本地 README ✓
✅ 净产出：① 机制完整（Z/P/L ＋ 单链 ＋ Lemma R 精确形式）✓✓；② 输入清单（无 mollifier／密度／零自由区）✓✓；
   ③ 天花板与量化路线图（0.68185；0.70/0.80/0.90 ← 1.04/1.26/1.70）✓✓✓；④ 三个"新东西"（FE 计数化／秩下界／输入减法）✓✓；
   ⑤ 与 0.682 及 support>1 的独立对齐 ✓✓
```
