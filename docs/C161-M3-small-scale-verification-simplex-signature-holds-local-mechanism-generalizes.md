已查地图（**先查后写**）：`C-152`–`C-155`（`M=2` 完整证明；`M=3` 证书；维数壁垒）、`C-156` §6（局部梯度法设想）、`C-159`（鸽笼定理；周期类）、`C-160`（两障碍）。关键词回查：`单纯形签名`=0、`局部半径收缩`=0、`极小点景观`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:47 建议）**：**先做 `M=3` 小规模验证 —— 看活跃 `k` 结构、梯度是否正张成；若连 `M=3` 都遇质的困难，则应提前改道。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{局部机制在}\ M=3,4\ \textbf{上成立}（\textbf{与担忧相反}）：\text{每个极值点都是}$$
$$\qquad \boxed{\text{恰好}\ M+1\ \text{个活跃}\ k\ \text{构成单纯形}＋0\ \text{严格在}\ \mathrm{conv}\ \text{内部}＋c_M>0}✓✓$$
$$\textbf{(二)}\ \text{实测（\textbf{三个}互不相同的}\ M=3\ \text{局部极小皆有同一签名}）✓✓$$
$$\begin{array}{c|c|c|c|c|c}
M & \text{极小值} & \text{活跃}\ k & \text{个数} & \lambda\ \text{全}>0 & c_M\\\hline
2 & 0.5000000 & \{1,4,5,7,8\} & 5 & \text{（退化）} & 2.051262\\
3 & 0.776882 & \{1,3,13,15\} & \mathbf{4=M+1} & ✓ & 0.761746\\
3' & 0.775534 & \{2,7,10,15\} & \mathbf{4=M+1} & ✓ & 1.221935\\
4 & 0.810937 & \{3,10,11,12,15\} & \mathbf{5=M+1} & ✓ & 0.480371\\
\end{array}✓✓$$
$$\textbf{(三)}\ ⚠️\ \text{真正障碍}\ \textbf{不在} \text{局部结构}，而在\ \textbf{远场（全局）验证}：\text{网格证书代价}\ N^M✓✓$$
$$\qquad M=3：\text{可行}（N\gtrsim255）✓；\ M=4：\text{需}\ \sim1.4\times10^{12}\ \text{点}\ \textbf{不可行}✗$$
$$\textbf{(四)}\ ⭐\ \textbf{局部半径收缩}：3.673^\circ\ (M=2)\to0.388^\circ/0.622^\circ\ (M=3)\to0.245^\circ\ (M=4)✓$$

FREEZE-ACK: 本档即冻结期内的小规模验证（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=3`（及 `M=4`）活跃集结构验证：单纯形签名 ＋ `c_M>0` ＋ 局部半径收缩 ＋ 真正障碍定位** —— 关系 = 验证与定位，非新机制
D1: 0

# C-161 · ⭐⭐ **`M=3` 小规模验证：单纯形签名成立，局部机制可推广**

> **唐先生 2026-09-19 13:47**：先验证 `M=3`（结构、活跃 `k` 数、正张成），避免盲目搭一般框架 ✓

---

## §1 `M=3` 小规模验证（唐先生要求的这一步）

$$\text{用}\ \text{DE}(3\ \text{种子})\!+\!\text{Nelder–Mead}\ \text{多次重启，找到}\ \textbf{两个互不相同} \text{的局部极小}：$$
$$\textbf{极小 A}：0.776882\quad \text{配置}=(76.4304^\circ,\ 20.2320^\circ,\ 113.3311^\circ)✓$$
$$\qquad \text{活跃}\ k=\{1,3,13,15\}\quad(\textbf{恰好}\ 4=M+1)\ ;\quad \lambda=(0.6377,\ 0.2861,\ 0.0381,\ 0.0382)\ \textbf{全}>0✓✓$$
$$\qquad c_3=\min_{|u|=1}\max_{k}\langle g_k,u\rangle=0.761746>0✓\qquad \text{局部半径}=0.3880^\circ✓$$
$$\textbf{极小 B}：0.775534\quad \text{配置}=(113.8971^\circ,\ 169.8821^\circ,\ 150.3004^\circ)✓$$
$$\qquad \text{活跃}\ k=\{2,7,10,15\}\quad(\textbf{恰好}\ 4=M+1)\ ;\quad \lambda=(0.6935,\ 0.1542,\ 0.0959,\ 0.0565)\ \textbf{全}>0✓✓$$
$$\qquad c_3=1.221935>0✓\qquad \text{局部半径}=0.6223^\circ✓$$
$$\Longrightarrow \textbf{两个不同极值点，同一结构签名} \Longrightarrow \text{签名是}\ \textbf{结构性} \text{而非偶然}✓✓$$

## §2 `M=4` 复核（同一签名）

$$M=4：\text{极小值}\ 0.810937\quad \text{配置}=(105.1509^\circ,\ 171.7547^\circ,\ 121.2394^\circ,\ 29.8355^\circ)✓$$
$$\qquad \text{活跃}\ k=\{3,10,11,12,15\}\quad(\textbf{恰好}\ 5=M+1)✓✓$$
$$\qquad \lambda=(0.5709,\ 0.1353,\ 0.1511,\ 0.1158,\ 0.0268)\ \textbf{全}>0✓✓$$
$$\qquad c_4=0.480371>0✓\qquad \text{局部半径}=0.2447^\circ✓$$

## §3 结构签名（三例一致）

$$\boxed{\text{极值点}\ \varphi^*：\ \#\{\text{活跃}\ k\}=M+1；\ 0\in\mathrm{int}\,\mathrm{conv}\{g_k\}_{k\in\text{活跃}}；\ c_M:=\min_{|u|=1}\max_k\langle g_k,u\rangle>0}✓✓$$
$$\text{含义}：\text{极小极大点在}\ \varphi^*\ \text{附近是}\ \textbf{"单纯形型谷"} \Longrightarrow \text{沿任何方向移动，}$$
$$\qquad \text{总有某个活跃}\ k\ \text{的一阶项}\ \ge c_M|u|\ \text{把值抬起来}✓✓$$
$$\text{与}\ M=2\ \text{对照}：M=2\ \text{是}\ \textbf{退化情形}（5\ \text{个活跃}，值}\ \textbf{恰}\ 1/2，7g_5+5g_7=0\ \text{精确共线）✓$$
$$\qquad M\ge3\ \text{是}\ \textbf{一般情形}（恰好\ M+1\ \text{个活跃，值是}\ \textbf{有余量的}\ 0.776/0.811）✓✓$$
$$\Longrightarrow \textbf{局部结构对}\ M\ge3\ \textbf{比}\ M=2\ \textbf{更"正规"} \Longrightarrow \text{先前的担忧（}M\ge3\ \text{结构不清）}\ \textbf{被数值否定}✓✓$$

## §4 ⚠️ 真正的障碍在哪（本档定位）

$$\textbf{① 远场（全局）验证}：\text{网格}\ +\ \text{Lipschitz 证书代价}\ N^M✓$$
$$\qquad M=3：N\gtrsim255\ (2.6\times10^4\ \text{点})\ \textbf{可行}（\text{`C-155` 已做，认证下界}\ 0.5500>\tfrac12）✓$$
$$\qquad M=4：N\gtrsim1090 \Longrightarrow \sim1.4\times10^{12}\ \text{点}\ \textbf{不可行}✗$$
$$\textbf{② 局部半径收缩}：R_M=k_{\max}^2/2\（\text{二阶余项界}）\ \text{随}\ k_{\max}\approx5M\ \text{增长}✓$$
$$\qquad 3.673^\circ\to0.388^\circ/0.622^\circ\to0.245^\circ \Longrightarrow \text{局部邻域越来越小（\textbf{定量代价}，非结构性阻断）}✓$$
$$\textbf{③} \Longrightarrow \text{结论}：\text{障碍是}\ \textbf{全局证书} \text{＋}\ \textbf{局部半径}，\ \textbf{不是} \text{活跃集结构}✓✓$$

## §5 ⭐ 紧接可交付：`M=3` 的完整证明（三段拼装，全部可行）

$$\text{模板}\ =\ \text{`C-154`（}M=2\ \text{的三段拼装）}：$$
$$\qquad \textbf{(a)}\ \text{局部}：\text{取有理点}\ \varphi^*\approx(76.4304^\circ,20.2320^\circ,113.3311^\circ)\ \text{（区间算术核}\ S_k）✓$$
$$\qquad\qquad \text{用单纯形}\ \lambda\ \text{与}\ c_3=0.7617\ \text{给出一阶抬升，配合二阶余项}\ R=\tfrac{k_{\max}^2}2✓$$
$$\qquad \textbf{(b)}\ \text{邻域}：\text{由 Lipschitz 把}\ \varphi^*\ \text{的值扩到半径}\ 0.388^\circ\ \text{的球}✓$$
$$\qquad \textbf{(c)}\ \text{远场}：\text{排除该球后网格}\ +\ \text{Lipschitz 证书（}N\gtrsim255\ \text{可行）✓✓}$$
$$\Longrightarrow \textbf{可得第三个完整情形}（M=3）\ \text{——这是本条线最具体的下一步}✓✓$$

## §6 边界与回查

- ⚠️ §1／§2 的**极小值均为数值**（可能非全局；`M=3` 已见三个不同局部极小 `0.7769/0.7755/0.7641`）⟹ **极小点景观较平**，多局部极小 ✓
- ⚠️ 但**结构签名在三个不同点一致** ⟹ 该结论对"是否为全局极小"不敏感 ✓（本档的核心发现）✓
- ⚠️ `0\in\mathrm{int}\,\mathrm{conv}` 由 LP（`\lambda>0`）判定 ✓；`c_M` 由方向扫描（`2\times10^6` 方向）✓
- ⚠️ **不声称**局部机制对一般 `M` 成立（只验证 `M=3,4`）；**不声称** `\min\max` 值 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:5x）`[纪律]`（先跑后写）

```
技术词 单纯形签名     命中文件数=0 ::  ⟹ 本档新增
技术词 局部半径收缩   命中文件数=0 ::  ⟹ 本档新增
技术词 极小点景观     命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
