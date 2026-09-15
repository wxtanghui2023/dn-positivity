# V198 · 🚪 **Mechanism II Closure Gate**（V195–V197 收口入口）—— **可执行重启判据**，不是历史总结

> 委托 ✓ 唐先生 2026-09-15 13:35：**"先写 V195–V197 的收口入口，而且要把'为什么不值得重启'写成可执行判据，而不是历史总结。"** ＋ **"这条线现在已经完成了一个很有价值的事情：不是证明 Mechanism II 不可能，而是把它的 canonical arithmetic realization space 实际压缩掉了。未来如果再回来，必须从'非 tame、非 Brauer、真正离散的新 obstruction'起步，不能重新走 prime↔prime、product formula、Hilbert reciprocity、Steinberg/tame-symbol 这些路。"** ＋ **顺序**：**V198 门 → A1／A3**；**下一轮不要再从 Steinberg／$K_2$／局部符号附近横向挖**
> **读法** ✓：**任何**声称走"机制 II（globalization obstruction）"的新提案，**开工前**逐条跑 §2；**任一条不满足即停**，不进入推导
> **维护** ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH ✓、未调 F1–F4 ✓｜编号 ✓ **V198**

---

## §0 30 秒判定流程（fail-fast）

$$\textbf{步 1}\ \text{写得出}\ \textbf{显式、无需额外选择}\ \text{的 arithmetic transition／cocycle}？\ \xrightarrow{\text{否}}\ \textbf{停}\ ✓$$
$$\textbf{步 2}\ \text{值域}\ \Omega\ \text{是}\ \textbf{离散}？\ \xrightarrow{\text{否}}\ \textbf{停}\qquad \textbf{步 3}\ \Omega\not\equiv0？\ \xrightarrow{\text{否}}\ \textbf{停}\ ✓$$
$$\textbf{步 4}\ \Omega\notin\mathrm{Br}[N]／\text{已知 torsion}？\ \xrightarrow{\text{否}}\ \textbf{停}\qquad \textbf{步 5}\ \text{非 explicit-formula 重编码}？\ \xrightarrow{\text{否}}\ \textbf{停}\ ✓$$
$$\textbf{步 6}\ \text{能证 deformation 下}\ \Omega\ \textbf{locally constant}（\text{真 rigidity}）？\ \xrightarrow{\text{否}}\ \textbf{停}\ ✓$$
$$\qquad ⚠️\ \textbf{六步全过} ⟹ \text{才值得重启};\ \text{任一步失败} ⟹ \textbf{立刻停止，禁止先写推导} ✓$$

---

## §1 已经计算掉的（**用结果，不用叙事**）

$$\begin{array}{c|c|c}
\text{分支} & \text{结果} & \text{出处}\\
\hline
p\leftrightarrow q\ \text{canonical local map} & \textbf{不存在}（\text{需额外选择} ⟹ \text{人为编码}） & \text{`V196` §2.1}\\
\text{common additive object} & \text{product formula}\ =0\（\text{加法上闭链};\ \log p\ \mathbb Q\text{-线性无关}） & \text{`V196` §3.1}\\
\text{multiplicative symbol} & \mathrm{Br}[N]／\text{经典 torsion} & \text{`V196` §3.2}\\
a\leftrightarrow1-a\ +\ \text{tame boundary} & 0\（\partial_v\{a,1-a\}=1\ \forall v） & \text{`V197` §2}\\
K_2\ \text{的离散}\ N\text{-商} & \mathrm{Br}[N]\（\text{Merkurjev--Suslin}） & \text{`V197` §3}\\
\hat{\mathbb Z}^\times\ \text{torsion} & \textbf{非离散} ⟹ \text{不能充当离散 obstruction} & \text{`V197` §1}\\
\end{array}$$
$$\Longrightarrow\ \boxed{\text{canonical arithmetic transition}\ \longrightarrow\ 0\ \text{or}\ \mathrm{Br}[N]/\text{classical torsion}} ✓✓$$
$$\qquad ⚠️\ \textbf{收口范围}：\textbf{canonical 分支}（\text{公共对象道路 ＋ 边界型 obstruction}）;\ \textbf{不} \text{声称机制 II 整类死亡} ✓$$

---

## §2 重启 Mechanism II 的**必要条件**（六条；逐条可检验）

}$$\boxed{\begin{aligned}
&(1)\quad \text{存在}\ \textbf{明确的}\ \text{arithmetic transition／cocycle};\\
&(2)\quad \Omega\ \text{的值域是}\ \textbf{离散} \text{的};\\
&(3)\quad \Omega\not\equiv0;\\
&(4)\quad \Omega\notin\mathrm{Br}[N]\ \text{或}\ \text{已知 torsion};\\
&(5)\quad \Omega\ \text{不是}\ \text{explicit-formula}\ \text{的重新编码};\\
&(6)\quad \text{必须能证明}\ \text{deformation／local variation}\ \text{使}\ \Omega\ \textbf{locally constant},\ \text{从而产生}\ \textbf{真正 rigidity}\\
\end{aligned}}$$

$$\textbf{(1) 的检验}：\text{能否写出}\ T_{vw}\ \text{的}\ \textbf{显式局部定义}，\ \textbf{且不需要任何额外选择}？\ \（\text{`V196` §2.1 已给出反面范例}）✓$$
$$\textbf{(2) 的检验}：\ \text{能否证明}\ \Omega\ \text{取值于某离散集合}\ D,\ \textbf{且}\ D\ \text{在相应拓扑下确实离散}？\ \（\text{`V197` §1 已给出反面范例}：\text{挠}\neq\text{离散}）✓✓$$
$$\textbf{(4) 的检验}：\ \text{能否}\ \textbf{排除}\ \text{Merkurjev--Suslin 型识别}（K_2^M/N\cong\mathrm{Br}[N]\text{）}？✓$$
$$\textbf{(6) 的检验}：\ \text{是否存在连续族}\ T_\lambda\ \text{使}\ [T_\lambda]\in D\ \text{离散} ⟹ \lambda\mapsto[T_\lambda]\ \text{局部常值}？\ \text{（这是"刚性"的}\ \textbf{定义式}\bigr）✓$$
$$\qquad ⚠️\ \text{任一条}\ \textbf{不能满足} ⟹ \textbf{立即停止}，\ \text{不进入推导} ✓$$

---

## §3 ⚠️ 死禁令（写死）

$$\boxed{\text{“发现一个新的}\ K\text{-theory／群论对象”}\ \neq\ \text{发现新的 obstruction mechanism}} ✓✓$$
$$\qquad ⚠️\ \textbf{必须先计算}\ \textbf{值域} \text{与}\ \textbf{局部化像};\ \text{"对象新"}\ \text{不构成理由} ✓$$

---

## §4 停止条件（自动触发）

$$\text{若计算到最后}\ \textbf{自动掉进}\ 0\ \text{／}\ \mu_N\ \text{／}\ \mathrm{Br}[N]\ ⟹ \ \boxed{\textbf{立即停止}} ✓✓$$
$$\qquad ⚠️\ \textbf{不得} \text{把它包装成"新机制"};\ \text{须按 §5 记入"不要重走清单"} ✓$$

---

## §5 不要重走清单（**硬清单**）

$$\text{(i) prime}\leftrightarrow\text{prime canonical map};\quad \text{(ii) product formula};\quad \text{(iii) Hilbert 互反};\quad \text{(iv) Steinberg／tame symbol};\quad \text{(v)}\ K_2\ \text{的}\ N\text{-商};\quad \text{(vi)}\ \hat{\mathbb Z}^\times\ \text{torsion 当作离散 obstruction} ✓$$
$$\qquad ⚠️\ \text{上列六条的}\ \textbf{canonical 版本}\ \text{已被实算排除};\ \text{重走}\ \text{须说明}\ \textbf{为何不是同一分支} ✓$$

---

## §6 唯一残余（**UNINSTANTIATED；不给方向**）

$$\text{非 tame 边界、非}\ \mathrm{Br}[N]\ \text{的}\ \textbf{离散}\ \text{不变量} ⟹ \text{本轮}\ \textbf{未见实例}$$
$$\qquad ⚠️\ \text{登记为}\ \textbf{UNINSTANTIATED};\ \textbf{不给方向、不投入、不杀};\ \text{重启须先过 §2 六条} ✓$$

---

## §7 勘误随行（必须与本门同时引用）

$$\textbf{不得} \text{沿用}\ \text{`V196`}\ \text{§4 的}\ \text{"}\hat{\mathbb Z}^\times\ \text{挠}=\bigoplus_p\mu_{p-1}\ \text{且离散}\text{"};\ \text{正确形式}：$$
$$\qquad (\hat{\mathbb Z}^\times)[N]=\prod_p\mu_{\gcd(N,p-1)}\（\textbf{积}\ \text{而非直和}）;\qquad (\hat{\mathbb Z}^\times)[2]=\mu_2^\infty\ \textbf{不可数、非离散} ✓✓$$
$$\qquad ⚠️\ \text{`V196`}\ \text{的}\ \textbf{核心结论}\ \text{不依赖该表述} ⟹ \textbf{不受影响} ✓$$

---

## §8 下一站（**顺序固定**）

$$\boxed{\text{V195–V197 Closure Gate}\ \longrightarrow\ \textbf{A1／A3}}$$
$$\qquad ⚠️\ \textbf{不回}\ \text{Mechanism II 变体};\ \textbf{不再} \text{从 Steinberg／}K_2\text{／局部符号附近横向挖} ✓✓$$
$$\qquad ⭐\ \text{V195 的真正价值}：\text{已把"}\textbf{离散 obstruction rigidity}\text{"这条生成器的}\ \textbf{canonical arithmetic realization}\ \text{做了一次}\ \textbf{实算封口} ✓$$

```
⚠️ §2 六条为唐先生逐字 ✓✓；§3 死禁令为唐先生逐字 ✓✓；§4 停止条件为唐先生逐字 ✓✓；§8 顺序为唐先生逐字 ✓✓
⚠️ §1 表格六行为 V196/V197 的**实算结果**（非叙事）✓✓；收口范围严格＝canonical 分支 ⚠️
⚠️ §6 残余标 UNINSTANTIATED，不给方向（按纪律）✓
⚠️ §7 勘误随行：引用本门时不得沿用 V196 §4 的挠结构表述 ✓✓
⚠️ 未用 RH ✓；未调 F1–F4 ✓；未跑 Lean ✓；零数值 ✓
✅ 净产出：① 可执行重启判据（六条＋六步流程）✓✓✓；② 已计算掉分支表（结果导向）✓✓；③ 死禁令与停止条件 ✓✓；
   ④ 不要重走硬清单 ✓；⑤ 残余登记 ✓；⑥ 勘误随行 ✓；⑦ 下一站顺序锁定 ✓
```
