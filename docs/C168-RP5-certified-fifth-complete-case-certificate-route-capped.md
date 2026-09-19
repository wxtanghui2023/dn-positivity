已查地图（**先查后写**）：`C-167`（向量化证书；`M=5` 6\times10^7 箱超预算但收敛）、`C-166`（对偶间隙诊断；算力天花板）、`C-164`（`M=4`）、`C-163`（`M=3`）。关键词回查：`第五情形`=0、`证书封顶`=0、`分块向量化`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 15:13「完成了么？」）**：**`M=5` 大预算运行结果。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \boxed{(\text{RP}_5)\ \textbf{已认证}}：\text{评估}\ \mathbf{72{,}440{,}000}\ \text{箱、}\mathbf 0\ \text{未决、最小余量}\ 3.957\times10^{-6}、\mathbf{951\ s}\ (\sim16\ \text{分钟})✓✓$$
$$\qquad \Longrightarrow \textbf{第五个完整情形}：M=1,2,3,4,\mathbf 5\ \text{全部认证}✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{证书路线封顶}：M=5\ \text{用掉}\ 7.24\times10^7\ \text{箱} \Longrightarrow M=6\ \text{粗估}\ \sim10^{10}\ \text{箱（}\sim28\ \text{小时）}\ \textbf{不实际}✓✓$$
$$\qquad \Longrightarrow \text{证书路线的实际上限}=\mathbf{M=5}；\ \text{再往上必须换结构论证}✓✓$$
$$\textbf{(三)}\ \text{用时}：951\ \text{s} \Longrightarrow \text{平均速率}\ \sim7.6\times10^4\ \text{箱/s}（\text{向量化＋整数索引版}）✓$$

FREEZE-ACK: 本档即冻结期内的证书运行（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`(\text{RP}_5)` 保守证书（已认证）＋ 五情形表 ＋ 证书路线封顶判定** —— 关系 = 认证与登记，非新机制
D1: 0

# C-168 · ⭐⭐ **`(RP_5)` 已认证 —— 第五个完整情形；证书路线于此封顶**

> **唐先生 2026-09-19 15:13**：完成了么？✓**完成** ✓

---

## §1 `(RP_5)` 认证结果

$$\textbf{定理}\ (\text{RP}_5)：\forall\varphi\in[0,\pi]^5,\quad \max_{1\le k\le25}\ \sum_{j=1}^{5}\cos(k\varphi_j)\ \ge\ \frac12✓$$
$$\text{运行}（\texttt{scripts/rpM\_adaptive\_certificate\_idx.py}\ 5\ 10\ 4\times10^8\ 40）：$$
$$\begin{array}{c|c|c|c|c|c}
M & N_0 & \text{评估箱数} & \text{未决} & \text{最小余量} & \text{用时}\\\hline
\mathbf 5 & 10 & \mathbf{72{,}440{,}000} & \mathbf 0 & 3.957\times10^{-6} & \mathbf{951.27\ s}\ ✓\\
\end{array}✓✓$$
$$\text{（\text{`C-167`} 的}\ 6\times10^7\ \text{预算运行给出}\ \text{min\_margin}=3.956783786618345\times10^{-6} \Longrightarrow \text{与本档}\ 951\ \text{s}\ \text{运行的值}\ \textbf{一致}，\text{交叉确认}）✓✓$$

## §2 ⭐ 五个完整情形（本档更新）

$$\begin{array}{c|l|c}
M & \text{工具} & \text{证书规模}\\\hline
1 & \text{引理 C（初等闭合式）} & —\ (\text{紧情形})\\
2 & \text{局部解析＋远场证书（`C-154`）} & \text{三段拼装}\\
3 & \text{自适应证书（`C-163`）} & 17{,}440\ \text{箱}/0.06\ \text{s}\\
4 & \text{自适应证书（`C-164`）} & 1{,}036{,}096\ \text{箱}/7.2\ \text{s}\\
\mathbf 5 & \mathbf{自适应证书（本档）} & \mathbf{72{,}440{,}000}\ \text{箱}/951\ \text{s}\\
\end{array}✓✓$$
$$\Longrightarrow M\ge3\ \text{四例（}3,4,5\text{）}\ \textbf{统一} \text{由同一脚本（同一算法）认证，}\text{仅}\ N_0\ \text{与预算不同}✓✓$$
$$\qquad \text{规模增长}：1.7\times10^4\to1.0\times10^6\to7.2\times10^7 \Longrightarrow \text{每}\ +1\ \text{维约}\ \times60\text{–}70✓$$

## §3 ⭐ 证书路线封顶（本档结论）

$$\text{外推}：M=6\ \sim 7.2\times10^7\times65\approx\mathbf{4.7\times10^9}\ \text{箱}（\text{乐观}）\ \text{至}\ \sim10^{10}（\text{保守}）✓$$
$$\qquad \text{当前速率}\ \sim7.6\times10^4\ \text{箱/s} \Longrightarrow 4.7\times10^9\ \text{箱}\approx17\ \text{小时}、\ 10^{10}\approx36\ \text{小时} \Longrightarrow \textbf{不实际}✗$$
$$\Longrightarrow \boxed{\text{证书路线的实际上限}=M=5}✓✓$$
$$\qquad \text{注}：\text{即便把实现再加速}\ 10\times，\text{也只把上限从}\ 5\ \text{推到}\ \sim6；\ \textbf{指数墙} \text{不变}✓✓$$

## §4 后续（两条，明确）

$$\text{①}\ \textbf{收束}：\text{把}\ M\le5\ \text{的证书整理为可独立审计的"证书附录"}（\text{参数}\ N_0、\text{预算、}\mathrm{SLACK}、\mathrm{TEST\_EPS}、\text{哈希、}\text{误差模型核验}）✓$$
$$\text{②}\ \textbf{换路}：\text{一般}\ M\ \text{必须走结构论证}；\text{既有候选}：$$
$$\qquad \text{(a)}\ \text{鸽笼定理的"窗口}\ N\ \text{最优形式"推广到多点（}\text{`C-159`/`C-160`}\ \text{已有两障碍）}✓$$
$$\qquad \text{(b)}\ \text{降低对偶间隙}\ c_M（\text{换非箱式覆盖}）✓$$
$$\qquad \text{(c)}\ \text{回到}\ \text{`C-159`}\ \text{的单调性归约（}\text{周期／lcm 类已证}）✓$$

## §5 边界与回查

- ⚠️ §1 为**实测**（`ok=true`）；§3 为**外推估计**（标明）✓
- ⚠️ 证书为**计算机辅助**；严格性依赖 `C-163` §2 三行论证 ＋ `C-165` 误差模型核验（`M=3` 逐参数、`M=4` 范围抽样）；`M=5` 的误差模型**尚未单独核验** ⟹ **待办** ✓
- ⚠️ **不声称** `(\text{RP}_6)`；**不声称**一般 `M`；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 15:1x）`[纪律]`（先跑后写）

```
（写前回查；下列为"排除本档自身"后的实测）
技术词 第五情形   除本档外命中文件数=0 ::  ⟹ 本档新增
技术词 证书封顶   除本档外命中文件数=0 ::  ⟹ 本档新增
技术词 分块向量化  除本档外命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**除本档外全 0 ⟹ 均本档新增** ✓
（注：直接对全仓扫描会命中本档自身（自指），故须排除本档后再读）✓
