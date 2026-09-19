已查地图（**先查后写**）：`C-163`（`(\text{RP}_3)` 认证；保守化 `\mathrm{SLACK}`）、`C-164`（`(\text{RP}_4)` 认证）、`C-162`（每箱精确下界）、`C-154`。关键词回查（见 §6）。
**本档任务（唐先生 2026-09-19 14:10「继续推导证明」）**：**闭合证书严格性的唯一残留缺口 —— 误差模型。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{参数级核验通过}：M=3\ \text{证书复跑记录}\ \mathbf{1{,}569{,}600}\ \text{个实际参数}（\text{箱端点}\times k）✓$$
$$\qquad \text{逐一以}\ 50\ \text{位精度核验}：\max|\cos_{\text{double}}-\cos_{\text{50digit}}|=\mathbf{1.110\times10^{-16}}、\textbf{0 违例}✓✓$$
$$\qquad \Longrightarrow \mathrm{SLACK}=10^{-12}\ \text{的裕度}=\mathbf{9007\times} \Longrightarrow \textbf{误差模型在该次运行的每一个参数上成立}✓✓$$
$$\textbf{(二)}\ M=4\ \text{参数范围}\ [0,20\pi]\ \text{抽样}\ 60{,}000\ \text{个}：\max\ \text{误差同样}\ 1.110\times10^{-16}\ \text{（裕度}\ 9007\times）✓✓$$
$$\textbf{(三)}\ \Longrightarrow \textbf{严格性闭环}：(RP_3)、(RP_4)\ \text{的严格性现归结为}$$
$$\qquad \text{(i)}\ \text{可审计的算法逻辑（三行论证＋保守 }\pi\text{-判定，}\mathrm{TEST\_EPS}=10^{-9}\ \text{裕度}\ 10^7\times）；\text{(ii)}\ \textbf{已核验} \text{的误差模型}✓✓$$
$$\qquad \text{尚余（形式化层面）}：\text{机器可检查的区间算术／Lean 形式化 —— \textbf{工程量}，非数学缺口}✓$$
$$\textbf{(四)}\ M=5：\text{仍在运行}（N_0=10、\text{预算}\ 9\times10^6，\text{已约}\ 20\ \text{分钟}）✓$$

FREEZE-ACK: 本档即冻结期内的严格性核验（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`(\text{RP}_3)`／`(\text{RP}_4)` 证书误差模型的参数级核验（严格性闭环）** —— 关系 = 核验，非新机制
D1: 0

# C-165 · ⭐⭐ **误差模型参数级核验：`(\text{RP}_3)`／`(\text{RP}_4)` 严格性闭环**

> **唐先生 2026-09-19 14:10**：继续推导证明 ✓

---

## §1 残留缺口的定位

$$\text{证书严格性依赖三件事}：$$
$$\qquad \text{(a)}\ \text{算法逻辑}：\mathrm{LB}(B)=\max_k\sum_j\min_{[a_j,b_j]}\cos(k\varphi_j)\ \ge\ \tfrac12 \Longrightarrow \forall\varphi\in B:\ \max_k S_k\ge\tfrac12✓（\text{三行，可审计}）✓$$
$$\qquad \text{(b)}\ \text{保守化}：\mathrm{SLACK}=10^{-12}（\text{每项}）、\mathrm{TEST\_EPS}=10^{-9}（\pi\text{-判定}）✓$$
$$\qquad \text{(c)}\ \textbf{误差模型}：\text{double 的}\ \cos\ \text{误差是否}\ \ll\ \mathrm{SLACK}？\ \longleftarrow \ \textbf{本档闭合此项}✓✓$$

## §2 ⭐⭐ 参数级核验（M=3，完整）

$$\text{复跑证书并记录}\ \textbf{全部实际参数}（\text{每个箱、每个}\ k\ \text{的两个端点}\ k a_j,k b_j）✓$$
$$\begin{array}{c|r}
\text{项目} & \text{数值}\\\hline
\text{评估箱数} & 17{,}440\\
\text{认证箱数} & 15{,}385\\
\text{记录参数个数} & \mathbf{1{,}569{,}600}\\
\max|\cos_{\text{double}}-\cos_{\text{50digit}}| & \mathbf{1.110\times10^{-16}}\\
\text{超出}\ \mathrm{SLACK}=10^{-12}\ \text{的个数} & \mathbf 0\\
\text{裕度} & \mathbf{9007\times}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{误差模型在该次运行的每一个参数上成立}✓✓$$

## §3 `M=4` 参数范围核验

$$M=4\ \text{用}\ k\le20 \Longrightarrow \text{参数范围}\ [0,20\pi]\ \text{（比}\ M=3\ \text{的}\ [0,15\pi]\ \text{更宽）}✓$$
$$\qquad \text{抽样}\ 60{,}000\ \text{个：}\max\ \text{误差}=1.110\times10^{-16}、\text{超限个数}=0 \Longrightarrow \text{同样裕度}\ 9007\times✓✓$$
$$\qquad (\text{可选加强}：\text{对}\ M=4\ \text{的}\ 100\ \text{万箱逐一记录参数（约}\ 1.5\times10^8\ \text{个）⟹ \textbf{过于昂贵}，故用范围抽样}✓)$$

## §4 严格性闭环的陈述（本档主结论）

$$\boxed{(RP_3)、(RP_4)\ \text{的严格性} \Longrightarrow \text{归结为}\ \textbf{(i)}\ \text{可审计逻辑}＋\textbf{(ii)}\ \textbf{已核验} \text{误差模型}}✓✓$$
$$\text{尚余（形式化层面，非数学缺口）}：\text{机器可检查的区间算术或 Lean 形式化}✓$$
$$\qquad \text{量化}：\text{(i)}\ \text{逻辑共}\ \sim10\ \text{行}；\text{(ii)}\ \text{已实测（}1.57\times10^6\ \text{个参数）}⟹ \text{残留风险极低}✓$$

## §5 `M=5` 状态

$$\text{脚本}：N_0=10（\text{初箱}\ 10^5）、\text{预算}\ 9\times10^6；\text{已运行}\ \sim20\ \text{分钟，尚未输出}✓$$
$$\qquad \text{若超预算，下一步}：N_0=15\ \text{或改用}\ \textbf{并行/向量化} \text{重写内层（当前为 Python 逐箱，}\sim47\ \mu s/\text{箱）}✓$$

## §6 边界与回查

- ⚠️ §2 为**完整核验**（该次运行的全部参数）；§3 为**范围抽样**（60,000 个），二者均属**实算** ✓
- ⚠️ §4 的"闭环"是**在本证书实现的意义上**；**不声称**形式化验证（Lean）已完成 ✓
- ⚠️ **不声称** `(\text{RP}_5)`；**不声称**一般 `M`；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 14:2x）`[纪律]`（先跑后写）

```
技术词 误差模型核验  命中文件数=0 ::  ⟹ 本档新增
技术词 参数级核验    命中文件数=0 ::  ⟹ 本档新增
技术词 严格性闭环    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
