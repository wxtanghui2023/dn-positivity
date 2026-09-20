已查地图（**先查后写**）：查 `C-201`（M=3 结构审计）、`C-176`（旧上界 0.777171）、`C-195`（下界 0.76）、`C-176` 的区间认证脚本模板。回查见 §5 ✓

D0: 本档对象 = **T13-A 甲**：$M=3$ 新上界 $m_3\le0.76408110090337578$ 的区间算术认证 ＋ 账本冻结 —— 关系 = 已有对象（$m_3$ 上界）的**推进**
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §1 结果（区间算术，一个合法构型即上界证书）

$$\text{脚本}\ \texttt{scripts/t13a\_jia\_upper\_bound\_certify.py}✓（\text{π 取区间，}\mathrm{prec}=160\ \text{bit}✓）$$
$$\text{[1] 高精度精修}：F_{\rm float}=0.764081100833955✓$$
$$\text{[2] 有理构型（}\mathrm{DEN}=10^{10}\text{）}：\varphi/\pi=(0.1158442572,\ 0.3318874234,\ 0.7355764367)✓✓$$
$$\text{[3] 区间认证}：\text{逐}\ k\ \text{上界最大者}\ k=1✓\qquad \boxed{\ \max_{1\le k\le15}S_k(x_0)\ \le\ 0.76408110090337577613\ }✓✓$$
$$\qquad \text{最紧三项}：k=1:0.764081100903✓,\ k=11:0.764081100445✓,\ k=13:0.764081099902✓$$
$$\qquad \Longrightarrow \boxed{\ m_3\ \le\ 0.76408110090337577613\ }✓✓\qquad（\text{不声称}\ x_0\ \text{是 minimizer}✓）$$

## §2 账本冻结（新版本）

$$\text{旧}：0.76\le m_3\le0.777171✓\qquad（\text{宽}=1.7171\times10^{-2}）$$
$$\Longrightarrow \boxed{\ \textbf{新}：0.76\ \le\ m_3\ \le\ 0.76408110090337577613\ }✓✓\qquad（\text{宽}=\mathbf{4.0811\times10^{-3}}）$$
$$\qquad \text{收紧因子}=4.21\times✓✓（\text{与唐先生预估}\approx4.2\times\ \text{一致}✓）；\text{相对旧上界收紧}\ 1.30899\times10^{-2}✓$$

## §3 稳健性（$\mathrm{DEN}$ 扫描）

| $\mathrm{DEN}$ | 有理值（浮点） | 区间上界 $U$ |
|---|---|---|
| $10^{8}$ | — | $0.76408113372347474801$ |
| $10^{9}$ | $0.764081103836294$ | $0.76408110383629390672$ |
| $\mathbf{10^{10}}$ | $\mathbf{0.764081100903376}$ | $\mathbf{0.76408110090337577613}$ ✓ 最紧 |

$$\text{三者单调收敛}✓ \Longrightarrow \textbf{插值法有效}✓；\text{取}\ \mathrm{DEN}=10^{10}\ \text{作为冻结版本}✓$$

## §4 边界

- 认证为**区间算术**✓（$\pi$ 取区间；逐 $k$ 取上端点 ✓）；依赖 `mpmath.iv` 正确性 ✓
- $\max_k$ 的上界**不**要求 $x_0$ 是极小点 ✓ —— 这正是"上界只需一个合法构型"的用法 ✓✓
- §2 的新账本**取代** $\texttt{C-176}$ 的 $U_3=0.777171$ 作为**当前版本**✓（`C-176` 原文保留不改 ✓）
- ⚠️ 本档**不**改变下界 $0.76$ ✓（`C-195`）；**不**声称 $m_3$ 精确值 ✓
- **未用** RH；**未改** 他档（仅新增本档 ＋ 新脚本）✓

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 上界认证     命中文件数=1    ::  ./C202-T13-A-JIA-certified-upper-bound-0.76408110-ledger-frozen.md
技术词 账本冻结版本 命中文件数=1    ::  ./C202-T13-A-JIA-certified-upper-bound-0.76408110-ledger-frozen.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 两项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §6 本档抓到的一处自我失误

$$\textbf{变量名冲突}：\text{首版把分母写成}\ \texttt{D}✗，\text{与维数}\ \texttt{D}=3\ \text{同名覆盖}✓ \Longrightarrow \texttt{IndexError}✗$$
$$\qquad \Longrightarrow \text{改名}\ \texttt{DEN}✓\ \text{后通过}✓\ \Longrightarrow \textbf{实现错，非数学错}✓（\text{第}\ 19\ \text{次同类应验}）✓$$

## §7 下一步

$$\text{乙-0}：\text{最佳簇}\ x_0\（F=0.7640811,\ A=\{1,5,11,13\}\）\ \text{的}\ \textbf{局部刚性}✓$$
$$\qquad \text{装备已备}：|A|=M+1=4✓,\ \mathrm{rank}(\Delta)=3✓,\ \lambda_{\min}=+2.605\times10^{-2}>0✓,\ c=+0.560385>0✓$$
$$\qquad \text{待建}：\text{(i) active-set 隔离}✓；\text{(ii) 一阶凸包覆盖}✓；\text{(iii) 二阶 Hessian 余项}✓ ⟹ F(x_0+\delta)\ge F(x_0)+c'\|\delta\|✓$$
$$\qquad \text{⚠️ 不要求精确等号集}✓（\text{按唐先生指示}）✓$$
