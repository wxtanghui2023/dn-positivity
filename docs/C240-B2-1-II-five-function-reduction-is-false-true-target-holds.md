已查地图（**先查后写**）：查 `C-239`（II-a/b/c＋§4 归约）、`C-238`（上界精确＋预判）、`C-237`（三 lemma）。回查见 §6 ✓

D0: 本档对象 = **C-240：五函数归约的否定 ＋ 真值目标的数值确认 ＋ 两条恒等式核验** —— 关系 = 否定＋边界澄清
D1: 0
FREEZE-ACK: 本档即冻结期内的判定与登记（依 §8.1；不产候选结论）

---

## §0 结论（一项决定性否定 ✗✗ ＋ 一项确认 ✓✓）

$$\boxed{\textbf{① 唐先生两条恒等式全部核验通过}✓✓（见 §1）}$$
$$\boxed{\textbf{② §4 五函数归约}\ \max_j[wH_j(x)+H_j(y)]\ge w\kappa-c_0\ \textbf{为【假}】✗✗（见 §3）}$$
$$\boxed{\textbf{③ 真值目标}\ \min_{x,y}M_w\ge w\kappa-c_0\ \textbf{数值成立}✓✓（w=5,6,10,20,100✓，见 §4）}$$
$$\boxed{\textbf{④ 诊断}✓：\text{归约"有效但太弱"✗ —— 分组平均抹掉了"max 由哪一支取到"的信息}✗✓}$$

## §1 两条恒等式的独立核验（全部通过 ✓✓）

$$\textbf{恒等式 1}✓✓：11H_j(t)=b_j\cos(a_jt)+a_j\cos(b_jt)=11\cos\tfrac{11t}2\cos(d_jt)+(b_j-a_j)\sin\tfrac{11t}2\sin(d_jt)✓,\quad d_j=\tfrac{b_j-a_j}2✓$$
$$\qquad \text{推导}✓：a=\tfrac{11}2-d✓,\ b=\tfrac{11}2+d✓ \Longrightarrow b\cos(at)+a\cos(bt)=\tfrac{11}2[\cos(A-B)+\cos(A+B)]+d[\cos(A-B)-\cos(A+B)]✓$$
$$\qquad \qquad =11\cos A\cos B+2d\sin A\sin B✓（A=\tfrac{11t}2,B=dt✓） \Longrightarrow \text{与唐先生所给一致}✓✓$$
$$\qquad \text{数值}✓：j=1..5\ \text{全部}\ \max|\text{LHS}-\text{RHS}|\le8.1\times10^{-15}✓✓$$
$$\qquad d_j\ \text{取值}✓：\{\tfrac92,\tfrac12,\tfrac32,\tfrac52,\tfrac72\}✓ \Longrightarrow \text{覆盖全部奇半整数}✓✓$$

$$\textbf{恒等式 2}✓✓：\sum_{j=1}^5 11H_j(t)=\sum_{k=1}^{10}(11-k)\cos(kt)✓$$
$$\qquad \text{核验}✓：\text{系数逐项}：k\to11-k✓（1\to10,\ 2\to9,\ 3\to8,\ 4\to7,\ 5\to6,\ 6\to5,\ 7\to4,\ 8\to3,\ 9\to2,\ 10\to1✓）$$
$$\qquad \text{数值}✓：\max|\sum_j11H_j-\sum_k(11-k)\cos kt|=2.7\times10^{-15}✓✓$$
$$\qquad \textbf{结构意义}✓✓：\text{五个 }H_j\ \text{共同覆盖}\ 1..10\ \text{全部频率}✓（\text{唐先生 §③}✓）\ \text{—— 不是"随便选的五个测试函数"}✓$$

## §2 $D(x)=\max_jH_j(x)$ 结构（C-240-A ✓）

$$\min_{x\in[0,\pi]}D(x)=0.162853038323\ldots✓\quad \text{在}\ x/\pi=0.44658500\ldots✓$$
$$\qquad \text{对照}\ \kappa=0.841253532831\ldots✓ \Longrightarrow \min D<\kappa✓（\text{单-}j\ \text{路线失败已由 C-239 §5 确认}✓，此处给出【最小值位置】✓）$$
$$\textbf{active-set 切换点}✓：\text{仅【4 个}】✓：x/\pi=0.304925✓,\ 0.446585✓,\ 0.609135✓,\ 0.809370✓ \Longrightarrow \text{五分段结构}✓✓$$
$$\qquad \Longrightarrow D(x)\ \text{由 5 个显式三角函数分段给出}✓ \Longrightarrow \text{可逐段代数化}✓✓$$

## §3 ⚠️ §4 五函数归约为假（决定性否定 ✗✗）

$$\text{验证对象}✓：G_w(x):=\min_{y}\max_{j=1..5}\bigl[wH_j(x)+H_j(y)\bigr]\ \stackrel{?}{\ge}\ w\kappa-c_0✓$$
```
   w      min_x G_w(x)          wκ-c0              差          失败点 (x/π, y/π)
   5      0.407692787903      3.246774690541    -2.8391e+00    0.459550, 0.727273
  10      1.215744349318      7.453042354697    -6.2373e+00    0.452877, 0.713928
  20      2.864919920448     15.865577683009    -1.3001e+01    0.449541, 0.702252
 100     15.972887955530     83.165860309504    -6.7193e+01    0.447039, 0.680567
```
$$\Longrightarrow \boxed{\text{§4 归约【为假}】✗✗ \Longrightarrow \text{不能作为证明路线}✗}$$
$$\textbf{根因}✓✓：\text{与 §2 的}\ \min_xD=0.16285\ \text{完全对应}✓ —— \text{在}\ x/\pi\approx0.447✓\ \text{处五个}\ H_j(x)\ \textbf{全小}✗$$
$$\qquad \Longrightarrow \text{加权平均}\ \tfrac{bA+aB}{11}\le\max(A,B)✓\ \text{的【松弛】在此处极大}✗ \Longrightarrow \text{五函数耦合只能给}\ 0.408✗$$
$$\qquad \textbf{信息论诊断}✓：M_w\ \text{的真值由【究竟是哪一支取到 max}】决定✓，\text{而分组平均恰恰抹掉该信息}✗✓$$
$$\qquad \text{注}✓：\text{归约本身仍有效}✓（\text{它是 }M_w\text{ 的合法下界}✓），\text{只是太弱}✗ \Longrightarrow \text{不能替代原问题}✓$$

## §4 真值目标的数值确认（完整 10 分支 ✓✓）

$$\text{验证对象}✓：\min_{(x,y)\in[0,\pi]^2}M_w(x,y)\ \stackrel{?}{\ge}\ w\kappa-c_0✓（\text{全域粗网格}+\text{局部细化}✓）$$
```
   w      min M_w               wκ-c0              差           位置 (x/π, y/π)
   5      3.246806335780      3.246774690541    +3.1645e-05   0.1817272, 0.9099313
   6      4.088091736182      4.088028223373    +6.3513e-05   0.5455152, 0.7265670
  10      7.453162989090      7.453042354697    +1.2063e-04   0.1817272, 0.9107134
  20     15.865720649505     15.865577683009    +1.4297e-04   0.7272424, 0.3625065
 100     83.168812527193     83.165860309504    +2.9522e-03   0.7272424, 0.3585085
```
$$\Longrightarrow \boxed{\text{目标【成立}】✓✓（差}>0\ \text{且随 }w\ \text{缓增}=\text{网格分辨率误差}✓，\text{非违反}✓）$$
$$\qquad \text{位置读数}✓✓：\text{全部落在}\ 11\ \text{格极值点附近}✓（0.1818=2/11✓,\ 0.909=10/11✓,\ 0.727=8/11✓,\ 0.545=6/11✓,\ 0.3625\approx4/11✓）$$
$$\qquad \Longrightarrow \text{与 C-236/C-239 的 extremizer 结构【一致}】✓✓$$

## §5 意义与下一步

$$\textbf{本档的真正贡献}✓✓：\text{把"两条路"分开}✓ —— \boxed{\text{真值目标成立}✓\quad\text{但归约太弱}✗}\ \text{—— 避免把弱归约当成证明}✗$$
$$\textbf{对证明路线的含义}✓：\text{必须【直接用 10 分支结构}】✓，\text{不能只依赖五函数分组}✗（\text{分组只在【局部井内】有效}✓，\text{因那里两分支确实 binding}✓）$$
$$\textbf{下一步候选}✓：\text{(i) 五分段逐段代数化（§2 的 4 个切换点}✓\text{，每段内 }D(x)\text{ 显式}✓\text{）；(ii) 双-案例结构：远离五井}\Rightarrow\text{用}\ \max_k\cos(kx)\ \text{的直接界}✓\text{；近井}\Rightarrow\text{局部对分析}✓\text{（C-239}✓\text{）；(iii) 对偶/LP 证书}✓$$
$$\qquad \textbf{但}✗：\text{(i)(ii)(iii) 均为【候选}】✓，\text{本档不声称任一可行}✗$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 归约有效性分离      命中文件数=1  ::  ./C240-B2-1-II-five-function-reduction-is-false-true-target-holds.md
技术词 五分段active结构    命中文件数=1  ::  ./C240-B2-1-II-five-function-reduction-is-false-true-target-holds.md
技术词 分组平均信息损失    命中文件数=1  ::  ./C240-B2-1-II-five-function-reduction-is-false-true-target-holds.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓；\textbf{② 本档含一项【决定性否定}】✗（§3✓），\text{已如实登记}✓$$
$$\textbf{③ 数值层}：§3/§4\ \text{为浮点全域搜索加局部细化}✓，\text{非证明}✗；\textbf{④ 未证}✗：\text{真值目标的严格证明}✓；\text{一般 }M／\text{窗 }N✗$$
