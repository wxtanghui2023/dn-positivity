已查地图（**先查后写**）：查 `C-247`（分段模型＋等号集）、`C-246`（两缺口）、`C-245`（常数链）。回查见 §7 ✓

D0: 本档对象 = **C-248：等号集纠正（一个点）＋ 远区 gap 显式值 ＋ 中段缺口的精确定位** —— 关系 = 纠正＋缺口定位
D1: 0
FREEZE-ACK: 本档即冻结期内的纠正与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 纠正 C-247 Lemma B}✗✓：\mathcal E=\{y_0\}\ \textbf{【只有一个点}】✓✓（\text{非两点}✗）}$$
$$\boxed{\textbf{② 纠正 C-246 §2 与 C-247 的 }y_0\ \text{取值}✗✓：j=4,5\ \text{的}\ 2\pi m/11\ \textbf{越出}\ [0,\pi]✗ \Longrightarrow \text{须取}[0,\pi]\ \text{内代表元}✓✓}$$
$$\boxed{\textbf{③ 远区 gap 显式}✓✓：\delta=0.2\Longrightarrow\min(r+|q|)=0.304633\ >\ \zeta_{max}=0.2974✓✓（\text{余量}0.007✓）}$$
$$\boxed{\textbf{④ 唯一剩余缺口}✗✓：\textbf{中段}\ 0.05\lesssim|\eta|\lesssim0.2\ \text{既不能纯 Taylor 也不能纯 gap}✗✓}$$

## §1 纠正 1：等号集只有一个点（本档 ✓✓）

$$\text{C-247 的枚举代码错}✗：\texttt{r=y and (c0+...)}\ ✗ \Longrightarrow y=0\ \text{时短路返回}\ 0✗ \Longrightarrow |0-0|<10^{-9}\ \text{误通过}✗$$
$$\qquad \text{实际}✓：r(0)=c_0+\cos0\cdot\cos0=c_0+1=1.9595\ne0✗✗ \Longrightarrow \textbf{0 不是等号点}✗$$
$$\text{修正枚举}✓：\mathcal E=\{y\in[0,\pi]:q(y)=0\ \text{且}\ r(y)=0\}✓,\ q=0\iff\sin\tfrac{11y}2=0\ \text{或}\ \sin(dy)=0✓$$
$$\qquad \text{检查全部候选}（y=\tfrac{2\pi m}{11},\ m=0..5✓；y=\tfrac{\pi l}d✓） \Longrightarrow \boxed{|\mathcal E|=1✓✓}：$$
```
   j=1 : E = {0.909091π}  = {2π·5/11}
   j=2 : E = {0.181818π}  = {2π·1/11}
   j=3 : E = {0.727273π}  = {2π·4/11}
   j=4 : E = {0.363637π}  = {2π·2/11}
   j=5 : E = {0.545455π}  = {2π·3/11}
```
$$\Longrightarrow \textbf{每个 }j\ \text{只有【一个等号点}】✓✓ \Longrightarrow \text{远区只需排除}\ \textbf{一个}\ \text{邻域}✓✓（\text{比 C-247 更简}✓✓）$$

## §2 纠正 2：$y_0$ 必须取 $[0,\pi]$ 内代表元（本档 ✓✓）

$$\text{C-246 §2 / C-247 的测试对 }j=4,5\ \text{用了}\ y_0=2\pi m/11✗：$$
```
   j=4 : m=9  → y0/π=1.636364 > 1 ✗（越域）
   j=5 : m=8  → y0/π=1.454545 > 1 ✗（越域）
```
$$\qquad \text{故 C-246 §2 的"远区 min≈0 对任何}\eta_0"✗\ \text{与 C-247 的}\ \mathcal E\ \text{含 0}✗\ \textbf{均由此越域引起}✗✓$$
$$\text{正确代表元}✓：j=4\Rightarrow\tfrac{4\pi}{11}=0.363636\pi✓；j=5\Rightarrow\tfrac{6\pi}{11}=0.545455\pi✓（\text{即}\ 2\pi(11-m)/11✓）$$
$$\qquad \text{与 §1 枚举的}\ \mathcal E\ \textbf{完全一致}✓✓$$

## §3 远区 gap 的显式值（本档 ✓✓）

$$\text{远区需求}✓：|\eta|\ge\delta\Longrightarrow r(y_0+\eta)+|q(y_0+\eta)|\ \ge\ \zeta_{max}=\tau K=2.9735\times0.1=0.2974✓$$
$$\qquad \text{则}\ \Phi_\zeta=r+|\zeta+q|\ \ge\ r+|q|-|\zeta|\ \ge\ 0.2974-0.2974=0✓✓\（\text{唐先生指出的最干净估计}✓）$$
```
   用正确 y0 的 j=1,2,3（全网格 4×10^6 点）：
     δ=0.05 → 0.015280 ✗     δ=0.10 → 0.204010 ✗
     δ=0.20 → 0.304633 ✓✓    δ=0.30 → 0.304633 ✓
```
$$\Longrightarrow \boxed{\text{远区在}\ \delta\approx0.2\ \text{处【通过}】✓✓（\text{余量}0.007✓）}$$
$$\qquad \textbf{注}✓：\text{该}\ \zeta_{max}\ \text{是【保守}】✓（\text{实际}|\zeta|=|wT(\varepsilon)|\le\tau K+O(w^{-1})✓，\text{且远区}\ |\zeta+q|\ge|q|-|\zeta|\ \text{本身有损}✓）$$

## §4 ⚠️ 唯一剩余缺口：中段（本档精确定位 ✓✓）

$$\text{近区}（\text{Taylor}✓）：\text{须}\ C_{q,r}\eta^3\ \text{被}\ \tfrac{r_2}2\eta^2\ \text{压制} \Longrightarrow \eta\lesssim\tfrac{r_2}{2C}✓（\text{e.g.}\eta\lesssim0.15✓）$$
$$\text{远区}（\text{gap}✓）：\text{须}\ \delta\ge0.2✓（§3✓）$$
$$\text{在}\ \eta=0.2✓：C\eta^3=166.67\times0.008=1.33✗\ \text{vs}\ \tfrac{A}1\eta^2=10.09\times0.04=0.40✗ \Longrightarrow \textbf{三阶项【反超}】✗✓$$
$$\Longrightarrow \boxed{\textbf{中段}\ 0.05\lesssim|\eta|\lesssim0.2\ \text{既不能纯 Taylor 也不能纯 gap}✗✓} \Longrightarrow \textbf{这是唯一剩余缺口}✓✓$$
$$\textbf{候选出路}✓（\text{本档不声称可行}✗）：$$
$$\qquad（\text{i}）\text{把逐点 Taylor 换成【区间 Taylor}】✓（\text{在}\eta\ \text{区间上取余项最小}✓）；$$
$$\qquad（\text{ii}）\text{中段用}\ r+|q|\ \text{的【实际函数}】✓\ \text{的显式下界}✓（\text{一维显式}✓，\text{非数值极小化}✓）；$$
$$\qquad（\text{iii}）\text{把窗口}\ K\ \text{从}\ 0.1\ \text{收紧到使}\ \zeta_{max}\ \text{下降}✓（\text{与 Case I 的门槛}K\ge0.05\ \text{比对}✓）$$

## §5 状态

| 项目 | 状态 |
|---|---|
| 等号集（**一个点**） | ✓✓ **本档纠正** |
| $y_0$ 代表元（$[0,\pi]$ 内） | ✓✓ **本档纠正** |
| 远区 gap（$\delta=0.2$，余量 0.007） | ✓✓ **本档给出** |
| 近区（$[0,y_0]$ 局部模型 ＋ 三阶余项） | ✓✓ 基本具备（C-245/C-247） |
| **中段（$0.05\lesssim\|\eta\|\lesssim0.2$）** | ✗ **唯一剩余缺口** |
| **Case II** | ⬜ 尚未盖章 |
| Case I 严格常数版 | ✗ |

$$\textbf{本档价值}✓✓：\text{把剩余缺口从"两处模糊"收敛到【一处精确}】✓✓（\text{中段}✓，\text{且已给出三条候选出路}✓）$$

## §6 诚实边界

$$\textbf{① 两处自我纠错}✓（§1、§2✓）；\textbf{② 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓$$
$$\textbf{③ 远区余量仅}0.007✗\ \text{（薄}✓），\text{但}\ \zeta_{max}\ \text{与三角不等式均有损}✓（\text{实际余量更大}✓）$$
$$\textbf{④ 本档未完成 Case II 盖章}✗（\text{中段未决}✓）$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 中段缺口定位        命中文件数=1  ::  ./C248-B2-1-II-corrected-equality-set-one-point-and-midrange-gap.md
技术词 代表元越域纠正      命中文件数=1  ::  ./C248-B2-1-II-corrected-equality-set-one-point-and-midrange-gap.md
技术词 区间泰勒候选        命中文件数=1  ::  ./C248-B2-1-II-corrected-equality-set-one-point-and-midrange-gap.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
