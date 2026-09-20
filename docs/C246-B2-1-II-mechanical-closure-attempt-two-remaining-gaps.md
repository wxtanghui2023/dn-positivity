已查地图（**先查后写**）：查 `C-245`（常数链）、`C-244`（恒等式＋二阶判据）、`C-243`（一维归约）、`C-237`（Lemma 3 等号集）。回查见 §6 ✓

D0: 本档对象 = **C-246：Case II 机械闭合档（三阶界落 Lemma ＋ 远区封口尝试）** —— 关系 = 机械闭合尝试＋两处缺口的定位
D1: 0
FREEZE-ACK: 本档即冻结期内的机械闭合与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 三阶界闭式}✓✓：C_q=C_r=\dfrac{(\tfrac{11}2+|d|)^3}{6}✓✓（\text{二项式闭式}✓，\text{乘积法则逐项展开}✓）}$$
$$\boxed{\textbf{② 缺口一}✗：\text{简单二次模型}\ -\tfrac\lambda\tau\zeta+A\zeta^2-B|\zeta|^3\ \textbf{在全局不成立}✗（\text{只在小}|\zeta|\ \text{有效}✗）}$$
$$\boxed{\textbf{③ 缺口二}✗✓：\text{Lemma 3 等号点【不止}\ y_0✗\ \text{而是【整条 11-格等号集}】✓✓ \Longrightarrow \text{远区必须排除全部等号点邻域}✗}$$
$$\boxed{\textbf{④ 结论}✓：\text{Case II 【尚未闭合}】✗，\text{但两处缺口已【精确锁定}】✓✓（\text{非模糊}✓）}$$

## §1 A：三阶界的逐条导出（本档完成 ✓✓）

$$q(\varphi)=\sin\tfrac{11\varphi}2\sin(d\varphi)=f(\varphi)g(\varphi)✓,\qquad f=\sin\tfrac{11\varphi}2✓,\ g=\sin(d\varphi)✓$$
$$f'=\tfrac{11}2\cos\tfrac{11\varphi}2✓,\ f''=-(\tfrac{11}2)^2\sin\tfrac{11\varphi}2✓,\ f'''=-(\tfrac{11}2)^3\cos\tfrac{11\varphi}2 \Longrightarrow |f'''|\le(\tfrac{11}2)^3✓$$
$$g'=d\cos(d\varphi)✓,\ g''=-d^2\sin(d\varphi)✓,\ g'''=-d^3\cos(d\varphi) \Longrightarrow |g'''|\le|d|^3✓$$
$$q'''=f'''g+3f''g'+3f'g''+fg''' \Longrightarrow |q'''|\ \le\ (\tfrac{11}2)^3+3(\tfrac{11}2)^2|d|+3\tfrac{11}2d^2+|d|^3=\Bigl(\tfrac{11}2+|d|\Bigr)^3✓✓$$
$$\text{同理}✓（r=c_0+FG✓,\ F=\cos\tfrac{11\varphi}2✓,\ G=\cos(d\varphi)✓，|F'''|\le(\tfrac{11}2)^3✓,\ |G'''|\le|d|^3✓）：$$
$$\boxed{C_q=C_r=\frac{1}{6}\Bigl(\frac{11}2+|d|\Bigr)^3}✓✓\qquad（\text{统一粗界}✓，\textbf{不声称最优}✗✓）$$
```
   j    |d|      C_q = C_r
   1    4.5      166.6667
   2    0.5       36.0000
   3    1.5       57.1667
   4    2.5       85.3333
   5    3.5      121.5000
```
$$\Longrightarrow |\mathcal R_q|,|\mathcal R_r|\le C_{q,r}|\eta|^3✓✓\ \text{—— A 项完成}✓✓$$

## §2 ⚠️ 缺口一：简单二次模型的适用域过小（本档发现 ✗✓）

$$\text{局部模型}✓：\tilde\Psi_{model}(\zeta)=-\tfrac\varrho\upsilon\zeta+\tfrac\rho{2\upsilon^2}\zeta^2✓\ \text{要求}\ t^*=0\ \text{最优} \iff |\zeta|\le\tfrac{\upsilon^2}\rho\Bigl(1-\tfrac{|\varrho|}{|\upsilon|}\Bigr)✓$$
$$\qquad \text{数值}✓（j=1✓）：\tfrac{\upsilon^2}\rho=\tfrac{2.4011}{48.454}=0.04956✓,\ 1-\tfrac{|\varrho|}{|\upsilon|}=1-0.8182=0.1818 \Longrightarrow \textbf{有效区间}\approx0.00901✓✓$$
$$\qquad \textbf{而}\ \zeta_{max}=\tau K=2.9735\times0.1=0.2974✗ \Longrightarrow \textbf{差 33 倍}✗✗$$
$$\text{全局核验}✓：\min_\zeta\bigl[\tilde\Psi(\zeta)-model(\zeta)\bigr]\ \text{（}|\zeta|\le0.297✓）：$$
```
   j=1: -4.425e-03   j=2: -4.168e-02   j=3: -2.760e-02   j=4: -1.713e-02   j=5: -8.913e-03
   （失败点在小 |ζ| ≈ 0.02–0.06）
```
$$\Longrightarrow \textbf{简单模型在全局为【过高}】✗（\tilde\Psi<model✗） \Longrightarrow \text{必须用【精确分段模型}】✓✓：$$
$$\qquad \min_\eta\Bigl\{\varrho\eta+\tfrac{r_2}2\eta^2+\bigl|\zeta+\upsilon\eta+\tfrac{q_2}2\eta^2\bigr|\Bigr\}✓\ \text{的【精确解}】✓（\text{分段二次}✓，\text{最优点随}\zeta\ \text{移动}✓）$$
$$\qquad \textbf{注}✓：\text{这不否定 C-245 的常数链结论}✓（\text{那里只在}\ |u|\to0\ \text{的局部用}✓），\text{但}\ \textbf{C-245 的适用域声明不完整}✗✓$$

## §3 ⚠️⚠️ 缺口二：等号点是整条 11-格集（本档重要发现 ✓✓）

$$\text{远区所需}✓：|\eta|\ge\eta_0 \Longrightarrow r(y_0+\eta)+|q(y_0+\eta)|\ \ge\ \delta_0>\zeta_{max}=0.2974✓$$
$$\text{数值结果}✓（\text{对任何}\eta_0\in\{0.05,\dots,0.5\}✓）：$$
```
   j=1: η0=0.05→0.00000✗  0.10→0.00000✗  0.20→0.00000✗  0.30→0.00000✗  0.50→0.00000✗
   j=2..5: 全部 ≈1e-5 ✗
```
$$\textbf{根因}✓✓：\text{Lemma 3 的等号点【不止}\ y_0✗ —— \textbf{是整条 11-格等号集}✓✓（\text{在}[0,\pi]\ \text{内有多个}✓）$$
$$\qquad \Longrightarrow \text{"远离}y_0\text{"}\ne\text{"}r+|q|>0\text{"}✗✓ \Longrightarrow \boxed{\textbf{远区必须【同时排除全部等号点的邻域}】✓✓}$$
$$\qquad \text{正确结构}✓：（\text{i}）\text{枚举全部等号点}\ \mathcal E=\{y_0^{(1)},\dots,y_0^{(s)}\}✓；$$
$$\qquad \qquad（\text{ii}）\text{在每个等号点作局部 Taylor}✓（\text{同一套系数结构}✓）；$$
$$\qquad \qquad（\text{iii}）\text{在}\ [0,\pi]\setminus\bigcup_{s}(\text{邻域})✓\ \text{上给统一正 gap}✓✓$$
$$\qquad \textbf{关键}✓✓：\text{每个等号点的局部结构【同类}】✓（\text{同一}\ \lambda=\varrho\tau/\upsilon\ \text{型恒等式}✓✓） \Longrightarrow \text{机械可复制}✓✓$$

## §4 适用域审计（唐先生四点 ✓）

$$\textbf{(1) }\varepsilon\ \text{仍在第 }j\ \text{井内}✓：|\varepsilon|=\tfrac{|u|}w\le\tfrac{0.1}5=0.02✓⟹ \text{需核对各井间距}✓（\Theta\ \text{间距}\ \ge2\pi/11=0.571✓ \gg0.02✓✓）$$
$$\textbf{(2) }\zeta=wT(\varepsilon)\ \text{落在控制区间}✓：|\zeta|\le0.2974✓✓（\text{已用于判定}✓）$$
$$\textbf{(3) 近区＋远区【必须真正划分全部}\eta\in[0,\pi]✓✓：\text{本档发现原划分不足}✗（\text{缺口二}✓）$$
$$\textbf{(4) 五个 }j\ \text{的代表元}✓：\text{五井中心}2\pi j/11✓\ \text{互不重合}✓；\text{但等号集【跨井}】✓⟹ \text{须统一枚举}✓（\text{§3}✓）$$

## §5 状态（本档定档 ✓）

| 项目 | 状态 |
|---|---|
| Exact upper bound | ✓✓ |
| Case II 精确分解 | ✓✓ |
| 二维→一维 | ✓✓ |
| 线性恒等消去 | ✓✓ |
| 二阶正性（局部） | ✓✓ |
| 三阶显式余项（闭式） | ✓✓ **本档完成** |
| 模型—真实逐点夹逼（局部） | ✓✓ |
| 近区常数链 | ✓✓ |
| **模型适用域（全局）** | ✗ **缺口一**（须用精确分段模型） |
| **远区全域封口** | ✗ **缺口二**（须排除全部等号点邻域） |
| **Case II** | ⬜ **尚未盖章** |
| Case I 严格常数版 | ✗ |

$$\textbf{本档核心价值}✓✓：\text{把"机械闭合"具体化后，暴露出【两个精确缺口}】✓✓（\text{非模糊}✓）—— 且缺口二的根源（\text{等号集是整条 11-格}✓）\ \text{对后续【可机械复制}】✓✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 三阶界二项式闭式    命中文件数=1  ::  ./C246-B2-1-II-mechanical-closure-attempt-two-remaining-gaps.md
技术词 模型适用域缺口      命中文件数=1  ::  ./C246-B2-1-II-mechanical-closure-attempt-two-remaining-gaps.md
技术词 等号集全域枚举      命中文件数=1  ::  ./C246-B2-1-II-mechanical-closure-attempt-two-remaining-gaps.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
