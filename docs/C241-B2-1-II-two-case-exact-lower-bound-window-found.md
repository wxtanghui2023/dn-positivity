已查地图（**先查后写**）：查 `C-240`（五函数归约否定＋真值目标）、`C-239`（II-a/b/c）、`C-238`（尖点常数＋精确上界）、`C-237`（三 lemma）。回查见 §7 ✓

D0: 本档对象 = **C-241：双-案例（远井粗界 ＋ 近井 two-branch 不等式）结构建立 ＋ 共同窗口判定** —— 关系 = 证明结构推进
D1: 0
FREEZE-ACK: 本档即冻结期内的结构推进与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 存在共同窗口}\ K\in[0.05,\ 0.5]✓✓（\text{推荐}\ K=0.2✓） \Longrightarrow \textbf{双-案例结构数值成立}✓✓}$$
$$\boxed{\textbf{② 三项关键简化}✓✓：\text{下界不需}\Delta\text{-gap 反向}✓；\text{精确分解}\max=\tfrac{A+B}2+\tfrac{|A-B|}2✓；\varepsilon=0\ \text{行由 Lemma 3 立即得}✓}$$
$$\boxed{\textbf{③ 诚实边界}✗：\text{本档为【案例发现＋常数判定}】✓，\text{非严格证明}✗（\text{依唐先生判定标准}✓）}$$

## §1 目标与两 case

$$\text{目标}✓：M_w(\varphi_1,\varphi_2)\ \ge\ w\kappa-c_0✓,\quad w\ge5✓,\quad \kappa=\cos\tfrac{2\pi}{11}✓,\ c_0=\cos\tfrac{\pi}{11}✓$$
$$\textbf{Case I}✓（\text{远井}✓）：d(\varphi_1,\Theta)\ge K/w✓,\ \Theta=\{\theta_j=\tfrac{2\pi j}{11}:j=1..5\}✓ \Longrightarrow \text{用}\ M_w\ge wF(\varphi_1)-1✓$$
$$\textbf{Case II}✓（\text{近井}✓）：\varphi_1=\theta_j+\varepsilon✓,\ |\varepsilon|\le K/w✓ \Longrightarrow \text{用}\ M_w\ge\max(A_j,B_j)✓$$

## §2 ⭐ 三项关键简化（本档确立 ✓✓）

$$\textbf{① 下界不需要}\Delta\text{-gap 的反向论证}✓✓：$$
$$\qquad \text{C-237 用}\Delta\text{-gap 是为了证"max 由 }P_j\ \text{取到}"✓（\text{等号刻画}✓）；\text{但下界只需}\ M_w\ge\max(A_j,B_j)✓$$
$$\qquad \text{而这是【恒真}】✓（A_j,B_j\ \text{就是十条分支中的两条}✓） \Longrightarrow \textbf{省掉一整块}✓✓$$

$$\textbf{② 唐先生的精确分解成为主工具}✓✓：$$
$$\qquad \cos X-\cos Y=-2\sin\tfrac{X+Y}2\sin\tfrac{X-Y}2✓ \Longrightarrow A-B=-2w\sin\tfrac{11\varphi_1}2\sin\tfrac{(a-b)\varphi_1}2+2\sin\tfrac{11\varphi_2}2\sin\tfrac{(a-b)\varphi_2}2✓✓$$
$$\qquad \frac{A+B}2=w\cos\tfrac{11\varphi_1}2\cos(d\varphi_1)+\cos\tfrac{11\varphi_2}2\cos(d\varphi_2)✓,\qquad d=\tfrac{a-b}2\in\{\pm\tfrac92,\pm\tfrac12,\pm\tfrac32,\pm\tfrac52,\pm\tfrac72\}✓$$
$$\qquad \Longrightarrow \boxed{\max(A,B)=\frac{A+B}2+\frac{|A-B|}2}✓✓（\text{平均值}＋\text{分裂项}✓）$$
$$\qquad \textbf{几何}✓：\text{沿任意方向离开中心}：\text{平均值受【二阶曲率}】约束✓，\text{分裂项受【一阶 cusp}】约束✓ \Longrightarrow \text{即使平均值下降，也要付出}|A-B|\ \text{的代价}✓✓$$

$$\textbf{③ }\varepsilon=0\ \text{行的立即推论}✓✓（\text{Lemma 3 直接给出}✓）：$$
$$\qquad \cos a\theta_j=\cos b\theta_j=\kappa✓ \Longrightarrow \max(A,B)\big|_{\varepsilon=0}=w\kappa+\max(\cos a\varphi_2,\cos b\varphi_2)✓$$
$$\qquad \max\ \ge\ \text{加权平均}\ \Longrightarrow \boxed{\max(A,B)\big|_{\varepsilon=0}\ \ge\ w\kappa+\underbrace{\tfrac{b\cos a\varphi_2+a\cos b\varphi_2}{11}}_{\ge-c_0\ (\text{C-237 Lemma 3}✓)}\ \ge\ w\kappa-c_0}✓✓$$

## §3 Case II 判定（数值 ✓✓）

$$\text{检验}：\min_{|\varepsilon|\le K/w,\ \eta\in[-\pi,\pi]}\bigl[\max(A,B)-(w\kappa-c_0)\bigr]✓（\text{五 pair}\times w\in\{5,6,10,100\}✓）$$
```
   K=0.05 : 最坏 j=1 w=5 : min = +1.836330e-05  ✓✓
   K=0.20 : 最坏 j=1 w=5 : min = +4.994530e-05  ✓✓
   K=0.50 : 最坏 j=3 w=5 : min = +9.460863e-05  ✓✓
   K=1.00 : 最坏 j=4 w=5 : min = -1.667542e+00  ✗
```
$$\Longrightarrow \textbf{Case II 对}\ K\le0.5\ \text{成立}✓✓（\text{且余量}>0✓）；\ K=1\ \text{失败}✗ \Longrightarrow K\ \text{有上界}✓$$

## §4 Case I 判定（数值 ✓✓）

$$\text{检验}：\min_{j,w}\ w\bigl[F(\theta_j+K/w)-\kappa\bigr]\ \ge\ 1-c_0=0.040507\ ?✓$$
```
   K=0.05 : min = 0.053219  ✓   K=0.50 : min = 0.453198  ✓
   K=0.20 : min = 0.202573  ✓   K=1.00 : min = 0.341056  ✓
```
$$\Longrightarrow \textbf{Case I 对}\ K\ge0.05\ \text{成立}✓✓ \Longrightarrow \text{窗口}\ K\in[0.05,0.5]\ne\varnothing✓✓（\text{推荐}\ K=0.2✓）$$

## §5 ⚠️ 自我纠错（本档记录 ✓）

$$\textbf{纠错}✗✓：\text{脚本中}\ c_j\ \text{索引错位}✗ —— \text{用了}\ j=0..4✓\ \text{而非}\ j=1..5✓ \Longrightarrow \text{打印的}\ c_j\ \text{与 C-238 不自洽}✗$$
$$\qquad（\text{打印}\ 0.000000/2.703204/3.638528/2.969464/1.511499✗\ \text{vs C-238 的}\ 0.5406/4.5482/3.9593/2.2672/0.5635✓）$$
$$\qquad \textbf{但}✓：\text{Case I 的判定用的是【直接计算的 }F\ \text{值}】✓，\text{未用 }c_j✓ \Longrightarrow \textbf{结论不受影响}✓✓$$

## §6 与目标的关系（诚实边界 ✓）

$$\boxed{\text{本档完成}✓：\text{case 结构建立}✓＋\text{三项关键简化}✓＋\text{共同窗口存在}✓（\text{数值}✓）}$$
$$\boxed{\text{未完成}✗：\text{① Case I 的严格常数版}✓（\text{需把 C-238 尖点界与 }K\ \text{阈值代数化}✓）；\text{② Case II 的严格二维不等式}✓（\text{核心}✓，\text{需把 §2 的分解做成显式不等式}✓）}$$
$$\qquad \text{依唐先生判定标准}✓：\textbf{C-241 的完成条件}＝\forall w\ge5,\forall\varphi_1,\varphi_2:\ M_w\ge w\kappa-c_0\ \text{的【显式证明}】✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 双案例共同窗口      命中文件数=1  ::  ./C241-B2-1-II-two-case-exact-lower-bound-window-found.md
技术词 平均值分裂项分解    命中文件数=1  ::  ./C241-B2-1-II-two-case-exact-lower-bound-window-found.md
技术词 反向gap免用         命中文件数=1  ::  ./C241-B2-1-II-two-case-exact-lower-bound-window-found.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓；\textbf{② 数值层}：§3/§4\ \text{为网格扫描}✓，\text{非证明}✗$$
$$\textbf{③ 拼接口径}✓：\text{Case I}\Rightarrow M_w\ge wF(\varphi_1)-1✓；\text{Case II}\Rightarrow M_w\ge\max(A,B)✓；\text{两 case 按 }d(\varphi_1,\Theta)\gtrless K/w\ \text{划分}✓$$
$$\textbf{④ 若两 case 均严格化}✓ \Longrightarrow \text{合 C-238 精确上界}✓ \Longrightarrow \boxed{g_w(10)=w\cos\tfrac{2\pi}{11}-\cos\tfrac{\pi}{11}\ (w\ge5)}✓✓$$
