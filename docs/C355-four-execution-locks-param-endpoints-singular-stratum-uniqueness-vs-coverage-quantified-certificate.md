已查地图（**先查后写**）：`C-354`（**branch completeness 为唯一审计量** ✓✓；三层分离 ✓）、`C-353`（三出口 ✓✓）、`C-352`（方系统 ✓）、`C-222`／`C-224`（Krawczyk ＋ 四门 B&B ✓）。回查见 §5 ✓

D0: 本档对象 = **C-355：执行四锁 ＋ 五件套 ＋ 升级门槛**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\textbf{① 证书链已严格}✓✓：\ \boxed{C\text{-}352 \to C\text{-}353 \to C\text{-}354 \to \textbf{branch-complete interval audit}}✓✓ \ —— \ \text{真正需防守的是}\ \textbf{最后一箭头}✓✓$$
$$\textbf{② 四细节锁死}✓✓：\text{见 §1}（\text{端点}✓、\text{奇异层}✓、\text{唯一性}\ne\text{覆盖}✓、\text{量化证书}✓）$$
$$\textbf{③ 执行目标＝五件套}✓✓：\text{见 §2}（\text{参数覆盖}✓＋\text{根盒隔离}✓＋\text{排除盒}✓＋\text{奇异层处理}✓＋\text{全支偶频下界}✓）$$
$$\textbf{④ 升级门槛}✓✓：\textbf{唯}\ \text{五件套齐备}\ \text{才允许升级到}\ \mathcal Z \cap E = \varnothing✓✓ \ —— \ \text{且}\ \textbf{即便成功仍停在精确抵消层}✓✓$$
$$\textbf{⑤ 下一道墙}✓✓：\ \text{小奇频} \Rightarrow \text{近}\ \mathcal Z \Rightarrow \text{偶频代价}✓（\textbf{Bridge A}✓） \ \Longrightarrow \ \textbf{不得}把「消灭一个反例子类」误写成「}\ H = \varnothing\ \text{已证」\ ✗✓$$

## §1 四细节逐条（✓✓）

$$\textbf{(1) 参数端点不得偷渡}✓✓：\beta \to 0^+✓ \ \textbf{不能}当普通内部区间✗✓ \Longrightarrow \textbf{分别审计}✓：\beta = 0✓、\ \beta = 1✓、\ \beta \to 0^+✓$$
$$\qquad \text{否则}\ \text{可能}\ \textbf{漏掉趋近边界的解支}✗✓$$
$$\textbf{(2) } a_i\ \text{碰撞必须单独分层}✓✓：a_i = a_j✓ \Longrightarrow \text{四方程}\ \textbf{Jacobian 秩可能下降}✗✓ \Longrightarrow \textbf{Krawczyk 唯一根逻辑不适用}✗✓$$
$$\qquad \Longrightarrow \ \text{登记为}\ \textbf{singular stratum}✓✓，\ \textbf{不得}把 Krawczyk 失败记成「无解」\ ✗✓$$
$$\textbf{(3) 唯一性}\ne\text{全支覆盖}✓✓：\text{盒内恰有一个根}✓ \ \not\Rightarrow \ \text{没有别的根}✗✓ \Longrightarrow \text{后者}\ \textbf{需整域排除／隔离覆盖}✓✓$$
$$\textbf{(4) 最终证书须量化}✓✓：\text{理想出口}\ \ne\ \text{「扫描了}\ \beta✓，\text{找到的支都}\ > \tfrac12」\ ✗✓$$
$$\qquad \text{而应是}\✓✓：\forall \beta \in (0,1]✓,\ \forall (a_1,a_2,a_3,b_2) \in \mathcal S_\beta✓,\ \max_{1 \le r \le 12} F_{2r} > \tfrac12✓,\ \text{其中}\ \mathcal S_\beta = \textbf{全部正解集}✓✓$$

## §2 执行五件套（✓✓）

$$\textbf{① 参数覆盖}✓：\beta\ \text{区间（含端点）}\ \text{细分}✓；\textbf{② 根盒隔离}✓：每格分支枚举 ＋ Krawczyk 唯一性✓；\textbf{③ 排除盒}✓：\text{无解格的} \text{区间证书}✓$$
$$\textbf{④ 奇异层处理}✓：a_i\ \text{碰撞}／a_i = 1／a_i \to 0\ \text{单独审计}✓✓（\text{与 C-353 出口 (c) 同源}✓）；\textbf{⑤ 全支偶频下界}✓：\text{沿}\ \textbf{全部已证实支} \text{核算}\ \max_{r \le 12} F_{2r}✓✓$$

## §3 升级门槛（✓✓）

$$\text{五件套齐备}✓ \ \Longrightarrow \ \mathcal Z \cap E = \varnothing✓✓ \ —— \ \textbf{此为}\ \text{唯一合法升级路径}✓✓；\textbf{不得}由采样／部分格／部分支升级✗✓$$
$$\textbf{且}✓✓：\text{即便}\ \mathcal Z \cap E = \varnothing\ \text{成立}✓，\ \textbf{仍停在精确抵消层}✓✓ \ —— \ \text{不推出}\ H = \varnothing✗✓（\text{C-353 §2 真值表}✓）$$

## §4 下一道墙（✓✓）

$$\text{真正的墙}\ ✓✓：\ \text{小奇频} \Rightarrow \text{近}\ \mathcal Z \Rightarrow \textbf{偶频代价}✓ \ —— \ \text{即}\ \textbf{Bridge A ＋ Bridge B}✓（\text{C-350 §5}✓）$$
$$\textbf{纪律}✓✓：\text{「消灭一个反例子类」}\ \ne\ \text{「}H = \varnothing\ \text{已证」}✗✓ \ —— \ \text{本阶段}\ \textbf{不}提前做\ Bridge\ A✗，\text{也}\ \textbf{不}把\ \text{五件套}\ \text{当作} \text{主线收口}✗✓$$

## §5 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 奇异层        命中文件数=0    :: 
技术词 端点审计     命中文件数=0    :: 
技术词 全支覆盖     命中文件数=1    :: ./C354-branch-completeness-as-core-audit-quantity-and-discovery-certificate-coverage-separation.md 
技术词 量化证书     命中文件数=2    :: ./C168-RP5-certified-fifth-complete-case-certificate-route-capped.md ./C167-vectorized-certificate-cross-validated-M5-needs-1e8-boxes.md 
```
- **零计算** ✗（执行协议档 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`\mathcal Z \cap E = \varnothing` 已证 ✗；`H = \varnothing` 已证 ✗；采样即覆盖 ✗；Krawczyk 失败＝无解 ✗
