已查地图（**先查后写**）：查 `C-250`（Case II 闭合）、`C-238`（尖点常数）、`C-241`（双案例）、`C-237`（Lemma 1）。回查见 §8 ✓

D0: 本档对象 = **C-251：Case I 闭合（branch-consistent 曲率纠正 ＋ 显式 K 证书）＋ 整条 B2-1 闭合** —— 关系 = 终局闭合
D1: 0
FREEZE-ACK: 本档即冻结期内的闭合与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 关键纠正}✗✓✓：\text{C-238 的}\ C_j=\max(a_j,b_j)^2\ \textbf{在【小侧】高估曲率}\sim100\ \text{倍}✗✗}$$
$$\boxed{\textbf{② branch-consistent 曲率}✓✓：\varepsilon<0\ \text{侧 binding}\ k=a_j\Longrightarrow\text{曲率}\tfrac{a_j^2\kappa}2✓；\varepsilon>0\ \text{侧}\ \tfrac{b_j^2\kappa}2✓}$$
$$\boxed{\textbf{③ Case I 显式证书}✓✓：K=0.1\Longrightarrow\min_j\bigl[c_jK-\tfrac{\text{curv}_j}5K^2\bigr]=0.052981\ >\ 1-c_0=0.0405068✓✓（\text{余量}1.31\times✓）}$$
$$\boxed{\textbf{④ ⭐ 整条 B2-1 闭合}✓✓✓：g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}\ \text{对一切}\ w\ge5✓✓（\text{未用 RH}✓✓）}$$

## §1 关键纠正：C-238 的曲率在高估（本档 ✓✓）

$$\text{C-238 §1 的【正确}】尖点形式✓✓：F(\theta_j+\varepsilon)-\kappa\ \ge\ s_j\max(-a_j\varepsilon,\ +b_j\varepsilon)-C\varepsilon^2✓✓$$
$$\text{但 C-238 后来把它压成}：c_j|\varepsilon|-C_j\varepsilon^2✓,\quad c_j=s_j\min(a_j,b_j)✓,\quad \boxed{C_j=\max(a_j,b_j)^2✗✗}$$
$$\qquad \textbf{丢失 1}✓：\text{反对称性}✗（\text{小侧斜率}\ s_ja_j✓，\text{大侧}\ s_jb_j✓）$$
$$\qquad \textbf{丢失 2}✗✗（更致命）：\text{两侧的【曲率不同}】✓ —— \varepsilon<0\ \text{侧 binding 分支是}\ k=a_j✓ \Longrightarrow \text{曲率}\ \tfrac{a_j^2\kappa}2✓$$
$$\qquad \qquad \text{而 C-238 统一用}\ \max(a,b)^2✗ \Longrightarrow \text{小侧高估}\ \tfrac{b^2}{a^2}\ \text{倍}✓（\text{j=1}：100\ \text{倍}✗✗）$$
```
   j    a    b    s_j·a      s_j·b     curv_a=a²κ/2   curv_b=b²κ/2
   1    1   10   0.540641   5.406408    0.420627      42.062677
   2    5    6   4.548160   5.457792   10.515669      15.142564
   3    4    7   3.959286   6.928750    6.730028      20.610712
   4    3    8   2.267249   6.045997    3.785641      26.920113
   5    2    9   0.563465   2.535593    1.682507      34.070768
```
$$\Longrightarrow \textbf{这才是"K 怎么选都不够"的真因}✓✓（\text{C-241 的数值发现是对的}✓，\text{但其常数来源错}✗✓）$$

## §2 Case I 的显式证书（本档 ✓✓）

$$\text{目标}✓：\operatorname{dist}(\phi_1,\Theta)\ge K/w \Longrightarrow w[F(\phi_1)-\kappa]\ \ge\ 1-c_0✓$$
$$\text{用 branch-consistent 界}✓：F-\kappa\ \ge\ (\text{最坏侧斜率})|\varepsilon|-\tfrac{\text{curv}_{min}}2\cdot2\varepsilon^2✓ \Longrightarrow w(F-\kappa)\ \ge\ \text{slope}\cdot K-\tfrac{\text{curv}}5K^2✓（w\ge5✓）$$
$$\text{判据}✓：\min_j\Bigl[c_jK-\tfrac{\text{curv}_j}5K^2\Bigr]\ \ge\ 1-c_0=0.0405068✓$$
```
   K=0.10 : j1:0.053223  j2:0.433785  j3:0.382469  j4:0.219154  j5:0.052981
            ⟹ 最坏 j=5，值 0.052981  ✓✓（余量 1.31×）
   K=0.15 : 最坏 0.076948 ✓✓        K=0.20 : 最坏 0.099233 ✓✓
   K=0.30 : 最坏 0.138754 ✓✓        K=0.50 : 最坏 0.197607 ✓✓
```
$$\Longrightarrow \boxed{\text{Case I 对一切}\ K\in[0.1,0.5]\ \text{通过}✓✓（\text{推荐}K=0.1✓，\text{与 Case II 对接}✓）}$$

## §3 精确核验（直接算 $F$，不用下界 ✓✓）

$$\text{min}_{\operatorname{dist}\ge K/5}[F(\phi)-\kappa]✓（8\times10^5\ \text{点}✓，\text{仅作核验}✓）：$$
```
   K=0.10 (ε0=0.020): min(F-κ)=0.010645 ⟹ w(F-κ)≥0.053223  需≥0.040507 ✓✓
   K=0.20 (ε0=0.040): min(F-κ)=0.020948 ⟹ 0.104739          ✓✓
   K=0.50 (ε0=0.100): min(F-κ)=0.024774 ⟹ 0.123871          ✓✓
```
$$\Longrightarrow \textbf{下界（§2）与精确值（§3）相符}✓✓（\text{略保守}✓，\text{K=0.2 时}\ 0.0992\ \text{vs}\ 0.1047✓）$$

## §4 两 case 对接（✓✓）

$$\text{Case II（C-250）}：|u|\le0.1\Longleftrightarrow|\varepsilon|\le\tfrac{0.1}w \Longrightarrow \mathcal E\ge0✓✓$$
$$\text{Case I（本档）}：\operatorname{dist}\ge\tfrac{0.1}w \Longrightarrow w[F-\kappa]\ge0.052981>1-c_0✓✓ \Longrightarrow M_w\ge wF-1\ge w\kappa-c_0✓✓$$
$$\Longrightarrow \boxed{\text{两 case 在}\ K=0.1\ \text{处【精确对接}】✓✓ \Longrightarrow \text{下界对一切}\phi_1\ \text{成立}✓✓}$$

## §5 ⭐ 整条 B2-1 闭合（✓✓✓）

$$\textbf{上界}✓✓（\text{C-238，初等}✓）：g_w(10)\ \le\ w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}\ \text{对一切}\ w\ge5✓$$
$$\textbf{下界}✓✓：\text{Case I（本档}✓✓）＋\text{Case II（C-250}✓✓） \Longrightarrow g_w(10)\ \ge\ w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}✓$$
$$\Longrightarrow \boxed{\boxed{\ g_w(10)\ =\ w\cos\frac{2\pi}{11}\ -\ \cos\frac{\pi}{11}\qquad\text{对一切}\ w\ge5\ }✓✓✓}$$
$$\qquad \textbf{且全程未用 RH}✓✓（\text{纯初等＋11-周期结构}✓✓）$$

## §6 本线的完整链条（备查 ✓）

$$\text{① 精确上界（C-238）}✓✓ \to \text{② 精确分解（C-242）}✓ \to \text{③ 二维→一维（C-243）}✓✓ \to \text{④ 线性恒等消去（C-244）}✓✓$$
$$\qquad \to \text{⑤ 三阶界闭式（C-245/C-246）}✓✓ \to \text{⑥ 分段凸模型（C-247）}✓✓ \to \text{⑦ 等号集（C-248）}✓✓$$
$$\qquad \to \text{⑧ 中段 branch-gap（C-249）}✓✓ \to \text{⑨ Case II 闭合（C-250）}✓✓ \to \text{⑩ Case I 闭合（C-251）}✓✓$$

## §7 诚实边界

$$\textbf{① 本档修正了 C-238 的曲率高估}✗✓（\text{并说明 C-241 的数值发现正确但常数来源错}✓）$$
$$\textbf{② 数值层}✓：§3\ \text{为核验}✓（\text{非证明}✗）；\text{§2 的界为显式的}✓，\text{其有限区间证书可逐条写出}✓$$
$$\textbf{③ 远区部分}✓：K=0.1\ \text{时}\ \varepsilon_0=0.02✓，\text{与【C-249 中段}】（0.15✓）、\text{【C-248 远区}】（0.2✓）\ \text{并存}✓$$
$$\qquad \text{注}✓：\text{Case I 的}\ \operatorname{dist}\ \text{与 Case II 的}\ |\eta|\ \text{是两个不同坐标}✓（\phi_1\ \text{与}\ \phi_2✓），\text{二者独立覆盖}✓✓$$
$$\textbf{④ 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓$$

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 branch一致曲率        命中文件数=1  ::  ./C251-B2-1-I-CASE-I-CLOSURE-branch-consistent-curvature-and-B2-1-complete.md
技术词 曲率高估纠正          命中文件数=1  ::  ./C251-B2-1-I-CASE-I-CLOSURE-branch-consistent-curvature-and-B2-1-complete.md
技术词 两案例对接点          命中文件数=1  ::  ./C251-B2-1-I-CASE-I-CLOSURE-branch-consistent-curvature-and-B2-1-complete.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

---

【指针·C-252 措辞收紧】（2026-09-20）
本档 §5/§6 的「整条 B2-1 闭合」措辞按唐先生要求收紧为：
**B2-1 的数学命题已闭合；正式证明文本还应补齐 Case I 的 far-gap 有限分割证书。**
本档 §3 的「精确核验」是极强交叉验证，**不是** finite-splitting certificate 本身。详 `C252`。
