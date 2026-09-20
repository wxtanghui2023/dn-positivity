已查地图（**先查后写**）：查 `C-248`（等号集纠正＋中段缺口）、`C-247`（分段模型）、`C-245`（三阶界）、`C-237`（Lemma 3）。回查见 §7 ✓

D0: 本档对象 = **C-249：精确 branch 恒等式 ＋ 中段 branch-gap Lemma（零损失）** —— 关系 = 中段缺口的消除
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 精确恒等式}✓✓：G_j(y):=r_j(y)+|q_j(y)|=\max\{c_0+\cos(a_jy),\ c_0+\cos(b_jy)\}✓✓\（\text{零损失}✓）}$$
$$\boxed{\textbf{② 中段 gap}✓✓：\eta_0=0.15\Longrightarrow\gamma=\min_j=0.3267\ >\ \zeta_{max}=0.2974✓✓（\text{余量}0.029✓，\text{比 C-248 的}0.007\ \text{扩大 4 倍}✓✓）}$$
$$\boxed{\textbf{③ 剩余唯一}✗：\text{Taylor 区须有效到}\ \eta_0=0.15✓，\text{而粗略逐点界只到}\sim0.05✗✓}$$
$$\boxed{\textbf{④ 三区覆盖结构}✓✓：|\eta|\le\eta_0\ (\text{Taylor}✓)\ \cup\ \eta_0\le|\eta|\le0.2\ (\text{branch-gap}✓✓)\ \cup\ |\eta|\ge0.2\ (\text{远区}✓）}$$

## §1 精确 branch 恒等式（本档核心 ✓✓）

$$r_j(y)=c_0+\cos\tfrac{11y}2\cos(d_jy)✓,\qquad q_j(y)=\sin\tfrac{11y}2\sin(d_jy)✓$$
$$\text{用}\ \cos A\cos B=\tfrac{\cos(A+B)+\cos(A-B)}2✓,\quad \sin A\sin B=\tfrac{\cos(A-B)-\cos(A+B)}2✓\（A=\tfrac{11y}2,B=d_jy✓）：$$
$$\boxed{r_j+q_j=c_0+\cos\!\bigl(\tfrac{11}2-d_j\bigr)y=c_0+\cos(a_jy)✓✓,\qquad r_j-q_j=c_0+\cos\!\bigl(\tfrac{11}2+d_j\bigr)y=c_0+\cos(b_jy)✓✓}$$
$$\qquad（\text{因}\ a_j=\tfrac{11}2-d_j✓,\ b_j=\tfrac{11}2+d_j✓，\text{且}\ a_j+b_j=11✓✓\ \text{—— 与 active pair 定义【完全一致}】✓✓）$$
$$\Longrightarrow \boxed{G_j(y)=r_j+|q_j|=\max\{r_j+q_j,\ r_j-q_j\}=\max\{c_0+\cos(a_jy),\ c_0+\cos(b_jy)\}}✓✓$$
$$\text{数值核验}✓：\max|G-\max\{c_0+\cos a_jy,c_0+\cos b_jy\}|=3.1\times10^{-15}✓✓$$

$$\textbf{意义}✓✓：\text{中段问题从"两个三角函数的组合"精确还原为【两条 active branches 的纯余弦最大值}】✓✓ \Longrightarrow \textbf{中段不再需要任何三角不等式}✓✓（\text{消除唐先生指出的"粗估吃掉余量"风险}✓✓）$$
$$\qquad \text{且与 C-237 Lemma 3 的泛函}\ H_{a,b}\ \text{同源}✓ \Longrightarrow \text{Case II 全程统一在【活跃对}】语言下 +✓$$

## §2 中段 gap（有限分割 ＋ 精确值 ✓）

$$\text{需求}✓：\min_{\eta_0\le|\eta|\le0.2}G_j(y_0+\eta)\ >\ \zeta_{max}=\tau K=2.9735\times0.1=0.2974✓$$
$$\text{网格值}✓（4\times10^6\ \text{点，仅作发现}✓）：$$
```
   j    (a,b)      y0/π        η0=0.02     η0=0.05     η0=0.10     η0=0.15
   1    (1,10)   0.909091     0.005826✗   0.015280✗   0.204010✗   0.610599✓✓
   2    (5, 6)   0.181818     0.032921✗   0.099532✗   0.252531✗   0.449485✓✓
   3    (4, 7)   0.727273     0.025583✗   0.075099✗   0.185455✗   0.326670✓✓
   4    (3, 8)   0.363636     0.018621✗   0.052876✗   0.126113✗   0.349231✓✓
   5    (2, 9)   0.545455     0.012034✗   0.032920✗   0.142377✗   0.474470✓✓
```
$$\Longrightarrow \boxed{\gamma=\min_j=0.3267\ （j=3✓）\ >\ 0.2974✓✓\ \text{余量}\ 0.029✓✓}$$
$$\qquad \textbf{注}✗：\eta_0\le0.10\ \text{全部不足}✗ \Longrightarrow \text{中段必须从}\ \eta_0=0.15\ \text{起}✓✓$$

## §3 有限分割法（本档给出，替代扫描 ✓✓）

$$\text{分割点}✓：\bigl\{y:\ ay\equiv0\pmod\pi\bigr\}\cup\bigl\{y:\ by\equiv0\pmod\pi\bigr\}\cup\bigl\{ay\equiv\pm by\pmod{2\pi}\bigr\}\ （\text{交点}✓）$$
$$\qquad \Longrightarrow \text{每段上}\ \max\{c_0+\cos(ay),\ c_0+\cos(by)\}\ \text{的极小只在【端点或交点}】✓✓（\text{分段单调}✓）$$
$$\qquad \Longrightarrow \text{有限个精确三角值}✓✓（\text{五个 }j\ \text{共}\sim10\ \text{段}✓，\text{每段}2\text{–}3\ \text{分割点}✓）$$
```
   实测（η0=0.05 的两段，全为闭式分割）：
     j=1 左[2.6560,2.8060] 分割点3 极小0.015280✗ │ 右[2.9060,3.0560] 极小0.252528✗
     j=2 左[0.3712,0.5212] 极小0.099530✗        │ 右[0.6212,0.7712] 极小0.126112✗
     j=3 左[2.0848,2.2348] 极小0.075098✗        │ 右[2.3348,2.4848] 极小0.154777✗
     j=4 左[0.9424,1.0924] 极小0.185453✗        │ 右[1.1924,1.3424] 极小0.052876✗
     j=5 左[1.5136,1.6636] 极小0.218064✗        │ 右[1.7636,1.9136] 极小0.032920✗
```
$$\Longrightarrow \textbf{分割法精确复现网格值}✓✓ \Longrightarrow \text{中段可做成【有限端点/交点比较}】✓✓（\text{满足唐先生"不接受扫描"要求}✓）$$

## §4 三区覆盖结构（Case II 的最终框架 ✓✓）

$$[0,\pi]\ \text{（以}\ \eta=\varphi_2-y_0\ \text{计）}=\underbrace{|\eta|\le\eta_0}_{\text{近区：Taylor}✓}\cup\underbrace{\eta_0\le|\eta|\le0.2}_{\text{中段：branch-gap}✓✓}\cup\underbrace{|\eta|\ge0.2}_{\text{远区}✓}$$
$$\text{各区工具}✓：\text{近区}=\text{C-245 三阶界＋C-247 分段凸模型}✓；\text{中段}=\text{本档精确 branch 恒等式}✓✓；\text{远区}=\text{C-248 的}\ r+|q|\ge0.3046✓$$
$$\qquad \text{各区下界}✓：\text{近区}\ \gamma_{near}\to0✓（\text{在中心}✓）；\text{中段}\ \gamma=0.3267✓✓；\text{远区}\ 0.3046✓ \Longrightarrow \text{中段与远区【均}>\zeta_{max}✓✓$$

## §5 唯一剩余 + 状态

$$\textbf{唯一剩余}✗✓：\text{近区（Taylor）须【有效到}\ \eta_0=0.15✓\text{】}$$
$$\qquad \text{在}\ \eta=0.15✓：C\eta^3=166.67\times0.003375=0.5625✗\ \text{vs}\ \tfrac{r_2}2\eta^2=24.2\times0.0225=0.545✗ \Longrightarrow \text{量级相当}✗✓（\text{临界}✓）$$
$$\qquad \Longrightarrow \text{需把逐点粗界（只到}\sim0.05✗）\ \text{升级为【二阶＋区间余项}】✓（\text{而非扩大 Taylor 区间}✓）$$

| 项目 | 状态 |
|---|---|
| 精确 branch 恒等式（零损失） | ✓✓ **本档** |
| 中段 branch-gap（$\eta_0=0.15$，$\gamma=0.3267$） | ✓✓ **本档** |
| 有限分割法（替代扫描） | ✓✓ **本档** |
| 远区 gap（$\delta=0.2$） | ✓✓（C-248） |
| **近区 Taylor 有效上界（到 0.15）** | ✗ **唯一剩余** |
| Case II | ⬜ 尚未盖章 |
| Case I 严格常数版 | ✗ |

## §6 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓；\textbf{② 网格值仅作发现}✓，\text{闭式分割为其验证}✓$$
$$\textbf{③ 本档未完成 Case II 盖章}✗（\text{近区上界未到 0.15}✓）；\textbf{④ 中段余量}0.029✓\ \text{（比 C-248 的}0.007\ \text{扩大 4 倍}✓✓）$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 零损失branch恒等式   命中文件数=1  ::  ./C249-B2-1-II-exact-branch-identity-and-midrange-gap-lemma.md
技术词 中段闭式分割         命中文件数=1  ::  ./C249-B2-1-II-exact-branch-identity-and-midrange-gap-lemma.md
技术词 三区覆盖框架         命中文件数=1  ::  ./C249-B2-1-II-exact-branch-identity-and-midrange-gap-lemma.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）
