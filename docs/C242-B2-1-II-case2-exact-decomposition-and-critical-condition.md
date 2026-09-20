已查地图（**先查后写**）：查 `C-241`（双-案例＋共同窗口）、`C-240`（五函数归约否定）、`C-239`（II-a/b/c）、`C-238`（尖点＋精确上界）、`C-237`（三 lemma）。回查见 §7 ✓

D0: 本档对象 = **C-242：Case II 二维不等式的精确分解＋危险流形系数＋关键条件（有限检查）＋数值确认** —— 关系 = 严格化推进
D1: 0
FREEZE-ACK: 本档即冻结期内的推导与判定（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 精确分解}✓✓：\mathcal E_w(u,\eta)=w[P(\varepsilon)-\kappa]+\Lambda(\eta)+\bigl[|U(\eta)-wT(\varepsilon)|-|U(\eta)|\bigr]✓✓}$$
$$\boxed{\textbf{② 关键条件}✓✓：|\lambda|\le c_\Lambda|r|✓\（r=\tau/\upsilon✓）\ \textbf{五个 }j\ \textbf{全部满足}✓✓ \Longrightarrow \textbf{有限显式常数检查}✓✓}$$
$$\boxed{\textbf{③ 数值（50 位）}✓✓：K=0.1/0.2✓，五 }j\times w\in\{5,100\}✓：\min\mathcal E=10^{-49}\sim10^{-48}✓（\text{机器零}✓）\ \text{且极小点全在}(0,0)✓✓$$
$$\boxed{\textbf{④ 诚实警示}✗✓：\text{一阶粗界会退化}✗ \Longrightarrow \text{必须保留}|U-wT|\ \text{与}\ \Lambda\ \text{的耦合}✓（\text{唐先生预警方向}✓）}$$

## §1 精确分解（本档核心工具 ✓✓）

$$\varphi_1=\theta+\varepsilon✓,\quad \varphi_2=y_0+\eta✓,\quad u=w\varepsilon✓,\quad |u|\le K✓,\quad d=\tfrac{a-b}2✓$$
$$Q:=\tfrac{A+B}2=wP(\varepsilon)+R(\eta)✓,\quad D:=\tfrac{A-B}2=-wT(\varepsilon)+U(\eta)✓$$
$$P(\varepsilon)=\cos\tfrac{11(\theta+\varepsilon)}2\cos(d(\theta+\varepsilon))✓,\quad T(\varepsilon)=\sin\tfrac{11(\theta+\varepsilon)}2\sin(d(\theta+\varepsilon))✓$$
$$R(\eta)=\cos\tfrac{11(y_0+\eta)}2\cos(d(y_0+\eta))✓,\quad U(\eta)=\sin\tfrac{11(y_0+\eta)}2\sin(d(y_0+\eta))✓$$
$$\max(A,B)=Q+|D|✓ \Longrightarrow \boxed{\mathcal E_w=\max(A,B)-(w\kappa-c_0)=w[P-\kappa]+\Lambda(\eta)+\bigl[|U-wT|-|U|\bigr]}✓✓$$
$$\qquad \Lambda(\eta):=c_0+R(\eta)+|U(\eta)|✓ \Longrightarrow \Lambda(0)=0✓,\ \Lambda\ \ge\ 0✓（\text{因}\ c_0+R+|U|=c_0+\max(\cos a\varphi_2,\cos b\varphi_2)\ \ge0✓，\text{Lemma 3}✓）$$
$$\qquad \textbf{物理解读}✓：\text{第 1 项}=\text{第一坐标的驱动}✓；\Lambda=\text{中心线的安全裕量}✓；\text{方括号}=D\ \text{的补偿}✓$$

## §2 危险流形 $D=0$ 的系数（精确 ✓）

$$D=0 \Longleftrightarrow U(\eta)=wT(\varepsilon)✓ \Longrightarrow \eta\approx\tfrac{\tau}{\upsilon}u=:r\,u✓,\quad \tau=(-1)^j\tfrac{11}2\sin(d\theta)✓,\ \upsilon=(-1)^m\tfrac{11}2\sin(dy_0)✓$$
$$\text{一阶系数}✓：w[P-\kappa]\approx\lambda u✓,\ \lambda:=-(-1)^jd\sin(d\theta)✓;\qquad \Lambda(\eta)\ \ge\ c_\Lambda|\eta|✓,\ c_\Lambda=R'(0)+|\upsilon|✓$$
```
   j     r=τ/υ        λ (Q 线性)     c_Λ·r          λ+c_Λ·r
   1    1.9189859      2.4328837     5.4064082      7.8392919
   2   -1.9189859     -0.2703204    -3.2438449     -3.5141653
   3    1.9189859      0.8109612     3.7844857      4.5954469
   4    1.9189859      1.3516020     4.3251265      5.6767286
   5   -1.9189859     -1.8922429    -4.8657674     -6.7580102
```
$$\boxed{\text{一阶条件}✓✓：|\lambda|\ \le\ c_\Lambda|r|✓} \Longrightarrow \text{对两个符号方向的 }u\ \text{均给正驱动}✓$$
$$\qquad \text{逐项核验}✓：j=1:\ 2.4329\le5.4064✓；j=2:\ 0.2703\le3.2438✓；j=3:\ 0.8110\le3.7845✓；j=4:\ 1.3516\le4.3251✓；j=5:\ 1.8922\le4.8658✓$$
$$\qquad \Longrightarrow \textbf{五个 }j\ \text{全部满足}✓✓ \Longrightarrow \text{有限显式常数检查}✓✓（\text{非扫描}✓）$$

## §3 数值确认（50 位精确 ✓✓）

$$\text{网格}：u=K\cdot\tfrac i{60}✓（i=-60..60✓），\eta=0.06\cdot\tfrac l{60}✓（l=-60..60✓）✓$$
```
   K=0.2 : j=1..5, w=5 与 w=100 全部 min E = 1.07e-50 ~ 1.03e-48（机器零），极小点 (0,0)
   K=0.1 : 完全相同
```
$$\Longrightarrow \boxed{\mathcal E_w\ \ge\ 0\ \text{在窗口内成立}✓✓，\textbf{且等号只在中心}(0,0)✓✓}（\text{强于"数值为正但接近零"}✓）$$

## §4 ⚠️ 诚实警示：一阶粗界会退化（唐先生预警方向 ✓）

$$\text{若只用反向三角}：|U-wT|-|U|\ \ge\ -|wT|✓ \Longrightarrow \mathcal E\ \ge\ \lambda u-|\tau||u|+c_\Lambda|\eta|-\cdots✓$$
$$\qquad \text{在}\ \eta=0✓,\ u<0✓\ \text{时}：j=1\ \text{给}\ \lambda-|\tau|=2.4329-2.9735=-0.5406<0✗ \Longrightarrow \textbf{粗界为负}✗$$
$$\qquad \text{而精确值}\ \mathcal E\ge0✓ \Longrightarrow \textbf{必须保留}\ |U-wT|\ \text{与}\ \Lambda\ \text{的【耦合}】✓✓（\text{不可只取反向三角}✗）$$
$$\qquad \textbf{正确用法}✓：\text{固定 }u\ \text{后对 }\eta\ \text{优化}✓ —— \text{方括号在}\ U\approx wT\ \text{（即 }\eta\approx ru✓\text{）时达最小}✓，\text{而此时}\ \Lambda\ \text{已被激活}✓（\eta\ne0\Longrightarrow\Lambda>0✓）✓$$

## §5 保守 $K$（依唐先生审计点 ✓）

$$\text{数值上}\ K=0.1\ \text{与}\ 0.2\ \text{均通过}✓✓ \Longrightarrow \text{取}\ \boxed{K=0.1}✓（\text{保守值}✓，\text{不需要最优}K✓）$$
$$\qquad \text{配合 C-241 Case I（\text{对 }K\ge0.05\ \text{成立}✓）} \Longrightarrow \text{窗口仍非空}✓✓$$

## §6 状态与完成标准

| 项 | 状态 |
|---|---|
| 精确分解 $\mathcal E=w[P-\kappa]+\Lambda+[\cdot]$ | ✓✓ 建立 |
| 危险流形系数表 | ✓✓ 精确 |
| 关键条件 $\|\lambda\|\le c_\Lambda\|r\|$ | ✓✓ 五者全满足（有限检查） |
| 数值确认 $\mathcal E\ge0$（50 位） | ✓✓ 且等号只在 $(0,0)$ |
| 一阶粗界 | ✗ 会退化（已警示） |
| **$\mathcal E\ge0$ 的解析证明** | ✗ **未完成**（需精确控制二阶余项与耦合） |

$$\text{依唐先生判定标准}✓：\textbf{通过条件}＝|\varepsilon|\le K/w\Longrightarrow\max(A,B)\ge w\kappa-c_0\ \text{的逐步可核验解析证明}✓；$$
$$\qquad \textbf{不通过}＝\text{只得数值正值}✗\ \text{或}\ \max(A,B)\ge w\kappa-c_0-C/w✗$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 中心线安全裕量      命中文件数=1  ::  ./C242-B2-1-II-case2-exact-decomposition-and-critical-condition.md
技术词 危险流形一阶条件    命中文件数=1  ::  ./C242-B2-1-II-case2-exact-decomposition-and-critical-condition.md
技术词 耦合保留警示        命中文件数=1  ::  ./C242-B2-1-II-case2-exact-decomposition-and-critical-condition.md
```
⚠️ 实测各 1 命中且均为本档自身 ✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界

$$\textbf{① 未用 RH}✓；\text{未改他档}✓；\text{未塞回 }C_\infty✓；\textbf{② 数值层}：§3 为 50 位网格}✓，\text{非证明}✗$$
$$\textbf{③ 本档含一项【诚实警示}】✗（§4✓）；\textbf{④ 未证}✗：\mathcal E\ge0\ \text{的解析证明}✓（\text{二阶余项＋耦合}✓）；\text{Case I 的严格常数版}✓$$
