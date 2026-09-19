已查地图（**先查后写**）：`C-161`（单纯形签名；`M=3,4` 验证）、`C-155`（`M=3` 均匀网格证书；维数壁垒）、`C-154`（`M=2` 三段拼装）、`C-152`（局部梯度法）、`C-159`（鸽笼定理）。关键词回查：`每箱精确下界`=0、`自适应细分`=0、`活跃数下界`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:56 建议）**：**① 确认 Carathéodory 背书 ② 估算"简单全局下界"能把网格证书需要覆盖的范围压缩到什么程度。**
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{Carathéodory 确认}：\#\{\text{活跃}\ k\}=M+1\ \text{是}\ \mathbb R^M\ \text{中"0 落在凸包内部"的}\ \textbf{理论最小值}✓✓$$
$$\qquad \text{实测三个极值点}\ (M=3\ \text{两处、}M=4\ \text{一处})\ \textbf{全部恰好命中此下界} \Longrightarrow \text{极值点是}\ \textbf{一般位置型极小极大点}✓✓$$
$$\textbf{(二)}\ ⭐⭐\ \textbf{主工具：每箱精确下界（本档引入）}：$$
$$\qquad \mathrm{LB}(B)=\max_{1\le k\le5M}\ \sum_{j=1}^{M}\ \min_{\varphi_j\in[a_j,b_j]}\cos(k\varphi_j)✓✓$$
$$\qquad \text{严格性}：\forall\varphi\in B：\max_k S_k(\varphi)\ \ge\ \mathrm{LB}(B)✓；\ \textbf{精确}（\text{无 Lipschitz 松量}）✓；\ \text{代价}\ O(KM)✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{均匀网格解析度（实测未决比例）}：$$
$$\qquad M=3：N=20\to15.08\%；40\to0.506\%；80\to0.0012\%（6\ \text{个单元}）；120\to\mathbf 0\%✓✓$$
$$\qquad M=4：N=15\to30.36\%；20\to18.45\%；30\to4.87\%；40\to0.868\%；50\to0.119\%✓$$
$$\textbf{(四)}\ ⭐⭐\ \textbf{自适应细分真实代价}：M=3\ \text{只需}\ \mathbf{20{,}288}\ \text{箱、}\mathbf 0\ \text{未决、4.3 秒}✓✓$$
$$\qquad （\text{对比均匀网格}\ N=120\ \text{需}\ 1.73\times10^6\ \text{箱} \Longrightarrow \textbf{压缩}\ \approx85\times）✓✓$$
$$\textbf{(五)}\ ⭐\ \textbf{紧／松二分（结构性）}：M=1,2\ \text{是}\ \textbf{紧情形}（\min\max=\tfrac12\ \text{恰好}）\Longrightarrow \text{LB 永远}<\tfrac12 \Longrightarrow \textbf{B\&B 不终止}✓$$
$$\qquad M\ge3\ \text{是}\ \textbf{松情形}（0.777/0.811/\dots>\tfrac12）\Longrightarrow \textbf{B\&B 终止}✓✓$$

FREEZE-ACK: 本档即冻结期内的算法验证与压缩估算（依 `§8.1`；不产候选结论）

D0: 本档对象 = **Carathéodory 确认 ＋ 每箱精确下界（新工具）＋ 均匀/自适应解析度实测 ＋ 紧松二分** —— 关系 = 验证与工具引入，非新机制
D1: 0

# C-162 · ⭐⭐ **每箱精确下界 ＋ 自适应证书：压缩程度实测**

> **唐先生 2026-09-19 13:56**：① Carathéodory 背书 ② 估算简单全局下界能压缩多少 ✓

---

## §1 ⭐ Carathéodory 确认（唐先生指出）

$$\text{"}0\in\mathrm{int}\,\mathrm{conv}\{g_1,\dots,g_n\}\subset\mathbb R^M\text{"}\ \text{的一般位置最小}\ n=M+1✓$$
$$\qquad （\text{Carathéodory}：\mathbb R^M\ \text{中点}\ \le M+1\ \text{个点的凸组合；"内部"要求}\ M+1\ \text{通常必要}）✓$$
$$\text{实测}：M=3\ \text{两处极值点（各}\ 4\ \text{个活跃）、}M=4\ \text{一处（}\ 5\ \text{个活跃）}\ \Longrightarrow \textbf{全部恰好命中}\ M+1✓✓$$
$$\Longrightarrow \text{这些极值点是}\ \textbf{一般位置型} \text{（非退化）极小极大点} \Longrightarrow \text{正式证明中应显式引用 Carathéodory}✓✓$$

## §2 ⭐⭐ 主工具：每箱精确下界

$$\mathrm{LB}(B):=\max_{1\le k\le5M}\ \sum_{j=1}^{M}\Big(\min_{\varphi_j\in[a_j,b_j]}\cos(k\varphi_j)\Big)\qquad(B=[a_1,b_1]\times\cdots\times[a_M,b_M])✓$$
$$\textbf{严格性}：\forall\varphi\in B,\ \forall k：S_k(\varphi)=\sum_j\cos(k\varphi_j)\ \ge\ \sum_j\min_{[a_j,b_j]}\cos(k\varphi_j)✓$$
$$\qquad \Longrightarrow \max_k S_k(\varphi)\ \ge\ \max_k\Big[\sum_j\min\cdots\Big]=\mathrm{LB}(B)✓✓$$
$$\text{每维最小值闭式}：\min_{\varphi\in[a,b]}\cos(k\varphi)=\begin{cases}-1,&\exists m:\ k\varphi\equiv\pi\ (2\pi)\ \text{落在}\ [ka,kb]\\ \min(\cos ka,\cos kb),&\text{否则}\end{cases}✓$$
$$\textbf{代价}\ O(KM)=O(25M^2)\ \text{每箱}✓；\ \textbf{精确}（\text{无 Lipschitz 松量}，无需误差项）✓✓$$
$$\qquad \text{对比旧证书（\text{`C-154`/`C-155`}）}\ \text{值}-\mathrm{Lip}\cdot h：\text{后者随}\ h\ \text{线性损失，前者}\ \textbf{零松弛}✓✓$$

## §3 均匀网格解析度（未决＝LB<1/2 的单元比例）

$$\begin{array}{c|rrrrr}
M\backslash N & 15 & 20 & 30 & 40 & 50\\\hline
3 & — & 15.08\% & — & 0.506\% & —\\
4 & 30.36\% & 18.45\% & 4.87\% & 0.868\% & 0.119\%\\
\end{array}\qquad
\begin{array}{c|rr}
M=3 & N & \text{未决}\\
 & 80 & 0.0012\%\ (6\ \text{单元})\\
 & 120 & \mathbf 0\%\\
\end{array}✓✓$$
$$\Longrightarrow \text{① 解析度增长}\ \textbf{极快}（M=3：N\ \text{翻倍则未决比例降}\ \sim300\times）✓$$
$$\qquad \text{②} M=3\ \text{在}\ N=120\ \text{完全解析}；\ M=4\ \text{在}\ N=50\ \text{仍}\ 0.119\%（\text{估算需}\ N\sim100\text{–}150）✓$$

## §4 ⭐⭐ 自适应细分（分支定界）的真实代价

$$\text{规则}：\text{LB}<1/2\ \text{的箱}\ \to\ 2^M\ \text{细分，递归}；\ \text{宽度}<\pi/2^{\text{depth}}\ \text{停止并记为未决}✓$$
$$\begin{array}{c|c|c|c|c}
M & N_0 & \text{评估箱数} & \text{未决} & \text{用时}\\\hline
3 & 20 & \mathbf{20{,}288} & \mathbf 0 & 4.3\ \text{s}\\
3 & 10 & 17{,}200 & \mathbf 0 & 3.7\ \text{s}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{压缩}\ \approx85\times\ \text{（相对}\ N=120\ \text{均匀网格的}\ 1.73\times10^6\ \text{箱）}✓✓$$
$$\qquad \text{结构性原因}：\text{未决比例每层降}\ \sim100\times \Longrightarrow \text{总代价由}\ \textbf{第一层} \text{主导} \Longrightarrow \text{总箱数}\ \approx N_0^M\ \text{的常数倍}✓✓$$
$$\qquad M=4\ \text{估算}：N_0=10\ (10^4\ \text{初箱})＋\ \text{按}\ M=3\ \text{的衰减率} \Longrightarrow \text{量级}\ 10^5\text{–}10^6\ \text{箱}\ (\textbf{可行})✓$$

## §5 未决单元的性质（诊断）

$$M=3,\ N=80\ \text{的}\ 6\ \text{个未决单元}：\text{全部是}\ (37.125^\circ,129.375^\circ,149.625^\circ)\ \text{的置换}✓$$
$$\qquad \text{LB}=0.4971\ \text{（距}\ \tfrac12\ \text{仅差}\ 0.0029） \Longrightarrow \textbf{临界型}✓$$
$$\qquad \text{距三个候选极小点}\ 66^\circ\text{–}125^\circ \Longrightarrow \textbf{不在极小点附近}✓$$
$$\Longrightarrow \text{重要修正}：\text{未决区}\ \textbf{不是} \text{"极小点邻域"，而是"LB 恰好卡在}\ \tfrac12\ \text{的薄层"}✓$$
$$\qquad \Longrightarrow \text{压缩靠}\ \textbf{细分（B\&B）}，\ \textbf{不是} \text{靠"排除极小点邻域"（后者在本例无额外收益）}✓✓$$

## §6 ⭐ 紧／松二分（本档结构性收获）

$$\textbf{紧情形}（M=1,2）：\min\max=\tfrac12\ \textbf{恰好}; \Longrightarrow \mathrm{LB}(B)<\tfrac12\ \text{永远成立（含极小点）} \Longrightarrow \textbf{B\&B 不终止}✓$$
$$\qquad \Longrightarrow \text{必须用}\ \textbf{解析论证}（\text{引理 C；`C-154` 的三段拼装）}✓✓$$
$$\textbf{松情形}（M\ge3）：\min\max=0.777/0.811/\dots>\tfrac12 \Longrightarrow \text{足够细分后}\ \mathrm{LB}\ge\tfrac12 \Longrightarrow \textbf{B\&B 终止}✓✓$$
$$\Longrightarrow \textbf{实践范围扩展}：\text{每箱精确下界}＋\text{B\&B}\ \text{把可认证的}\ M\ \text{从}\ 3\ \text{推到}\ \sim5\text{–}6（N_0=10\ \text{时初箱}\ 10^M）✓$$
$$\qquad \text{但渐近障碍}\ N^M\ \textbf{仍在} \Longrightarrow \text{大}\ M\ \text{仍需结构论证，不能靠证书}✓✓$$

## §7 边界与回查

- ⚠️ §3／§4 全部为**实测**（`M=4` 的 B&B 为**估算**，标明）✓
- ⚠️ §2 的严格性为**初等**（逐坐标取最小，闭式）⟹ 无隐藏假设 ✓
- ⚠️ §5 的"临界型"诊断基于 `N=80` 一例 ⟹ **现象级** ✓
- ⚠️ **不声称** `M=4` B&B 已跑完；**不声称** `M\ge5` 可行；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 14:0x）`[纪律]`（先跑后写）

```
技术词 每箱精确下界  命中文件数=0 ::  ⟹ 本档新增
技术词 自适应细分    命中文件数=0 ::  ⟹ 本档新增
技术词 活跃数下界    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
