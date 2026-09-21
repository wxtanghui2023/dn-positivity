已查地图（**先查后写**）：`C-369`（**`\mathcal D_{\mathrm{reg}}` 注册** ✓✓；`\mathcal Z \cap E = \mathcal D_{\mathrm{reg}} \cap E` ✓✓）、`C-368`（碰撞判空 ✓✓）、`C-358`（`D_∂` ✓✓）、`C-355`（五件套 ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-370：`\mathcal D_{\mathrm{reg}}` 对称消元／Prony 型代数预审计**，**有计算（符号代数，已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（六条 ✓✓）

$$\textbf{① 消元链}✓✓：E_1 = -4e_2 s + 3e_3 + 3ps^2 = 0✓ \Longrightarrow \boxed{e_3 = \tfrac{4e_2 s - 3ps^2}{3}}✓✓ \Longrightarrow \text{消}\ e_3\ \text{得}\ F_2, F_3✓；\ \text{消}\ p\ \text{得曲线方程}\ C(e_2,s) = 0✓✓$$
$$\textbf{② ⭐ 曲线方程因式分解}✓✓：\ \boxed{C(e_2, s) = -\tfrac{5}{81}\,e_2^2\,s^{11}\,\big[81e_2^4 - 2358e_2^3s^2 + 16340e_2^2s^4 + 12696e_2s^6 + 2592s^8\big]}✓✓$$
$$\textbf{③ ⭐⭐ 齐次性 ⟹ 四元降维（本档核心）}✓✓：\text{方括号内}\ \textbf{按权重}\ \deg(e_2) = 2✓、\deg(s) = 1✓ \ \textbf{齐次（度 8）}✓ \Longrightarrow \text{设}\ r := \dfrac{e_2}{s^2}✓✓$$
$$\qquad \Longrightarrow \ \boxed{81r^4 - 2358r^3 + 16340r^2 + 12696r + 2592 = 0}✓✓ \Longrightarrow \ \text{``}r\text{''}\ \textbf{至多 4 个值}✓✓$$
$$\textbf{④ } q := p/s^2\ \text{二次确定}✓✓：\text{由}\ F_2✓ \Longrightarrow \boxed{30q^2 - 18rq + 3r^2 - 2r = 0}✓✓ \Longrightarrow \text{每}\ r\ \text{给} \le 2\ \text{个}\ q✓$$
$$\textbf{⑤ 尺度自由度}✓✓：\text{原系统}\ \textbf{齐次}（\text{度}\ 2r+1✓） \Longrightarrow \text{解族含}\ \textbf{平凡一维尺度}✓✓ \Longrightarrow \boxed{\mathcal D_{\mathrm{reg}} = \text{尺度} \times \text{离散形状}}✓✓（\textbf{非}真正一维曲线✗✓）$$
$$\textbf{⑥ 边界／碰撞因子分离}✓✓：e_3 = 0✓（a_i = 0✓）与\ \Delta = 0✓（\text{碰撞}✓）\ \textbf{均不在} \text{解族上}✓✓（\operatorname{Res}_p(F_2, \Delta) \ne 0✓；e_3 = 0\ \text{联立}\ \textbf{无解}✓） \Longrightarrow \text{与}\ \mathcal D_{\partial}／\mathcal D_{\mathrm{coll}}\ \text{已分离}\ \textbf{一致}✓✓$$

## §1 消元链（✓✓）

$$\textbf{设定}✓：a_1, a_2, a_3\ \text{为}\ x^3 - e_1x^2 + e_2x - e_3\ \text{的根}✓；\ e_1 = s = \beta + b_2✓（r = 0\ \text{条件}✓）；\ p = \beta b_2✓$$
$$\textbf{Newton 幂和}✓：P_k = e_1P_{k-1} - e_2P_{k-2} + e_3P_{k-3}✓ \Longrightarrow P_1 = e_1✓，P_3✓，P_5✓，P_7✓$$
$$\textbf{方程}✓：E_r := P_{2r+1} - (\beta^{2r+1} + b_2^{2r+1}) = 0✓，\ r = 1,2,3✓；\ \text{右端} = \sum_j(-1)^j\binom{2r+1}{j}s^{2r+1-j}p^j✓$$
$$E_1 = -4e_2s + 3e_3 + 3ps^2✓；\ E_2 = 7e_2^2s - 6e_2e_3 - 6e_2s^3 + 5e_3s^2 - 10p^2s^3 + 5ps^4✓；\ E_3\ \text{（10 项✓）}✓$$

## §2 消 `e_3` 与消 `p`（✓✓）

$$F_2 = -\tfrac{s}{3}\big(3e_2^2 - 18e_2ps - 2e_2s^2 + 30p^2s^2\big)✓；\ F_3 = \tfrac{s}{9}\big(18e_2^3 - 81e_2^2ps - 14e_2^2s^2 + 48e_2ps^3 + 12e_2s^4 + 315p^3s^3 - 126p^2s^4\big)✓$$
$$\textbf{两式皆含因子}\ s✓，\textbf{公共} \text{并约去}✓（s = \beta + b_2 > 0✓） \Longrightarrow \text{消}\ p\ \text{得}\ C(e_2,s)✓✓（\text{总次数}\ 21✓）$$

## §3 四元降维（✓✓）

$$\textbf{权重齐次}✓✓：\text{方括号} = s^8 \cdot \big[81r^4 - 2358r^3 + 16340r^2 + 12696r + 2592\big]✓（r = e_2/s^2✓） \Longrightarrow \text{四次}✓✓$$
$$\textbf{结构含义}✓✓：\mathcal D_{\mathrm{reg}}\ \text{的}\ \textbf{形状} \text{由}\ r\ \text{的}\ \le 4\ \text{个根} \text{决定}✓✓；\text{每个}\ r\ \text{再由}\ q = p/s^2\ \text{的} \le 2\ \text{个根} \text{补全}✓✓$$
$$\qquad \Longrightarrow \ \text{组合数} \le 8✓ \Longrightarrow \text{真正需要处理的是}\ \textbf{有限形状} \times \textbf{一维尺度}✓✓，\ \textbf{不是} 一维曲线覆盖✗✓$$

## §4 与既有分层的一致性（✓✓）

$$\textbf{碰撞}✓：\Delta = 18e_1e_2e_3 - 4e_1^3e_3 + e_1^2e_2^2 - 4e_2^3 - 27e_3^2✓ \ \text{（代入}\ e_3✓）\ \text{与}\ F_2\ \text{的结式} \ne 0✓✓ \Longrightarrow \text{碰撞不在}\ \mathcal D_{\mathrm{reg}}\ \text{上}✓✓$$
$$\textbf{边界}✓：e_3 = 0 \iff p = \tfrac{4e_2}{3s}✓ \ \text{与}\ (F_2, F_3)\ \text{联立}\ \textbf{无解}✓✓ \Longrightarrow a_i = 0\ \text{不在}\ \mathcal D_{\mathrm{reg}}\ \text{上}✓✓$$
$$\qquad \Longrightarrow \ \text{与}\ C\text{-}358／C\text{-}361／C\text{-}368\ \text{的解析清除} \textbf{逻辑一致}✓✓（\text{互不重叠}✓）$$

## §5 下一步（✓✓，登记不执行 ✓）

$$\textbf{登记}✓✓：\text{对}\ \le 4\ \text{个}\ r\ \text{根}\ \text{（四次方程✓）}\ \text{依次}：\text{① 判定}\ r\ \text{的}\ \textbf{实性／正性}✓✓（\text{决定是否有实解}✓）；\text{② 由二次式取}\ q✓；\text{③ 由}\ (s, r, q) \ \text{反解}\ (e_2, e_3, p)✓$$
$$\qquad \text{④ 恢复}\ (a_i, \beta, b_2)✓ \ \text{并核}\ a_i > 0✓、\text{互异}✓；\ \text{⑤ 沿}\ \textbf{尺度} \text{扫} \text{并算}\ \max_{r \le 12}F_{2r}✓✓（\text{判}\ > \tfrac12✓）$$
$$\textbf{优势}✓✓：\text{该项若成，}\ \text{「1D 完备区间覆盖」}\ \text{可}\ \textbf{大幅缩短}✓✓ \ —— \ \text{正是唐先生所预期}✓✓；\ \textbf{仍不新增方法}✗✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 对称消元坍缩 命中文件数=0    :: 
技术词 齐次尺度分离 命中文件数=0    :: 
技术词 四次形状方程 命中文件数=0    :: 
技术词 正则有因     命中文件数=0    :: 
```
- 运行记录 ✓：`/tmp/c370.py`（Newton 幂和 ＋ 结式 ✓）、`/tmp/c370b.py`（消 `e₃`／消 `p`／判别式检查 ✓）；**sympy** 精确符号 ✓
- **本档有计算**（符号代数，已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **诚实标注** ⚠️✓：`r` 的**实性／正性未判** ✓（四次方程的实根数待定 ✓）；`\le 4` 为**至多** ✓，非精确计数 ✗✓
- **不得**写成：`\mathcal D_{\mathrm{reg}} \cap E = \varnothing` 已证 ✗；`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；四次方程已解 ✗
