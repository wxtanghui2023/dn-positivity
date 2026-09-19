已查地图（**先查后写**）：`C-162`（每箱精确下界；均匀/自适应解析度）、`C-163`（`M=3` 认证）、`C-164`（`M=4` 认证）、`C-165`（误差模型核验）。关键词回查：`对偶间隙诊断`=0、`算力天花板`=0、`分辨率需求`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 14:36「结果？」）**：**`M=5` 结果 ＋ 失败原因诊断。**
**结论（先行）**：$$\textbf{(一)}\ M=5\ \text{超预算}：\text{评估}\ 9{,}000{,}001\ \text{箱、未决}\ 87{,}391、412\ \text{秒}\ \Longrightarrow \textbf{未获认证}✓$$
$$\textbf{(二)}\ ⭐\ \textbf{诊断}：\text{每箱下界的}\ \textbf{对偶间隙}\ \approx c_M\cdot h\ \text{（}\text{线性于箱宽}）：c_3\approx0.037,\ c_4\approx0.054,\ c_5\approx0.098✓$$
$$\qquad \text{"LB}<1/2\ \text{"的箱比例}：M=5\ \text{在}\ h=5^\circ\ \text{时}\ 3.75\%、h=2^\circ\ \text{时}\ 0\% \Longrightarrow \textbf{所需分辨率}\ \approx2^\circ⟹N\approx90✓$$
$$\qquad \Longrightarrow \text{箱数}\ \sim N^M：M=4\ (N\approx20\text{–}90)\ \text{可行}；M=5\ (N\approx90)\ \Rightarrow\sim10^7\text{–}10^8\ \text{箱}\ \textbf{超出当前预算}✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{判定}：M=5\ \textbf{不是} \text{数学上被卡，而是}\ \textbf{算力}：\text{当前实现为 Python 逐箱}\sim47\ \mu s/\text{箱}✓$$
$$\qquad \text{若重写为向量化／并行（}\sim100\times\text{），}M=5\ \text{的}\ \sim10^7\ \text{箱量级}\ \textbf{可达}✓；\ \text{渐近墙}\ N^M\ \text{在}\ M\gtrsim6\text{–}8\ \text{才真正致命}✓$$

FREEZE-ACK: 本档即冻结期内的失败记录与诊断（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=5` 超预算记录 ＋ 对偶间隙诊断（`\approx c_M h`）＋ 算力天花板判定** —— 关系 = 诊断，非新机制
D1: 0

# C-166 · ⭐ **`M=5` 超预算：对偶间隙诊断 —— 是算力，不是数学**

> **唐先生 2026-09-19 14:36**：结果？✓

---

## §1 `M=5` 运行结果（失败记录）

$$\begin{array}{c|c|c|c|c|c}
M & N_0 & \text{预算} & \text{评估箱数} & \text{未决} & \text{用时}\\\hline
5 & 10 & 9\times10^6 & 9{,}000{,}001 & 87{,}391 & 412\ \text{s}\ ✗\\
\end{array}✓$$
$$\text{参数哈希}：7943b863a3291024\quad(\mathrm{SLACK}=10^{-12},\ \mathrm{TEST\_EPS}=10^{-9})✓$$

## §2 ⭐ 对偶间隙诊断（本档核心）

$$\text{量}：\text{箱}\ B\ \text{上}\ \mathrm{gap}(B):=\Big[\min_{\varphi\in B}\max_k S_k(\varphi)\Big]-\mathrm{LB}(B)✓$$
$$\qquad （\text{恒}\ \ge0；\text{证书能认证}\ B\iff\mathrm{LB}(B)\ge\tfrac12\iff\text{gap 小到足以让 min-max 越过}\ \tfrac12）✓$$
$$\begin{array}{c|rrrrr|c}
M & h{=}10^\circ & 5^\circ & 2^\circ & 1^\circ & 0.5^\circ & \text{拟合}\\\hline
3 & 0.369 & 0.171 & 0.052 & 0.019 & 0.009 & \approx0.037\,h\\
4 & 0.544 & 0.324 & 0.109 & 0.052 & 0.024 & \approx0.054\,h\\
5 & 0.826 & 0.490 & 0.217 & 0.096 & 0.044 & \approx0.098\,h\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{gap}\ \approx c_M\cdot h\ \text{（\textbf{线性} 于箱宽）}；\ c_M\ \text{随}\ M\ \text{增长}（\text{粗}\ \sim\text{线性}）✓✓$$
$$\text{"}\mathrm{LB}<\tfrac12\text{"的箱比例}：$$
$$\begin{array}{c|rrrr}
M & 10^\circ & 5^\circ & 2^\circ & 1^\circ\\\hline
3 & 17.25\% & 0.00\% & 0\% & 0\%\\
4 & 19.25\% & 0.75\% & 0.00\% & 0\%\\
5 & 27.25\% & 3.75\% & 0.00\% & 0\%\\
\end{array}✓$$
$$\Longrightarrow \text{所需分辨率（使未决区近空）}：M=3\approx5^\circ；M=4\approx2\text{–}5^\circ；M=5\approx2^\circ⟹N\approx90✓$$

## §3 ⭐ 判定：算力天花板，非数学障碍

$$\text{箱数}\ \sim N^M：$$
$$\qquad M=3：N\approx36 \Rightarrow 4.7\times10^4；\quad M=4：N\approx36\text{–}90 \Rightarrow 1.7\times10^6\text{–}6.6\times10^7；\quad M=5：N\approx90 \Rightarrow \mathbf{5.9\times10^9}（\text{均匀}）✓$$
$$\qquad \text{自适应细分后（实测比例）}：M=5\ \text{估计}\ \sim10^7\text{–}10^8\ \text{箱}✓$$
$$\qquad \text{当前实现}：\text{Python 逐箱，}\sim47\ \mu s/\text{箱} \Longrightarrow 10^7\ \text{箱}\approx8\ \text{分钟}、10^8\ \text{箱}\approx80\ \text{分钟}（\text{超时/超预算}）✓$$
$$\Longrightarrow \textbf{结论}：$$
$$\qquad \text{①}\ M=5\ \textbf{不是} \text{"数学上不行"，而是}\ \textbf{实现速度}；\text{向量化／并行（}\sim100\times\text{）可望拿下}✓✓$$
$$\qquad \text{②}\ \textbf{渐近墙}\ N^M\ \text{在}\ M\gtrsim6\text{–}8\ \text{才真正致命} \Longrightarrow \text{那时必须换结构论证}✓✓$$

## §4 下一步（两条，明确）

$$\text{①}\ \textbf{工程}：\text{把证书内层}\ \textbf{向量化}（\text{批量箱同时评估}）\ \text{或}\ \text{用}\ \texttt{numba/C}\ \text{重写} ⟹ \text{冲}\ M=5✓$$
$$\text{②}\ \textbf{数学}：\text{降低}\ c_M（\text{即减小对偶间隙}）\ \text{或}\ \text{换非箱式覆盖}；\ \text{或}\ \text{直接攻一般}\ M\ \text{的结构论证}✓$$
$$\qquad \text{注}：c_M\ \text{的增长是}\ \textbf{"箱式分离界"的固有弱点}（\text{逐坐标取最小}\Longrightarrow\ \text{忽略坐标间相关性}）✓$$

## §5 边界与回查

- ⚠️ §1 为**失败记录**（`ok=false`）；§2 为**实算**（每格 400 个随机箱、每箱 400 点采样估 min-max）✓
- ⚠️ §3 的箱数估计为**量级估计**（非实测）✓
- ⚠️ **不声称** `(\text{RP}_5)`；**不声称**一般 `M`；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 14:4x）`[纪律]`（先跑后写）

```
技术词 对偶间隙诊断  命中文件数=0 ::  ⟹ 本档新增
技术词 算力天花板    命中文件数=0 ::  ⟹ 本档新增
技术词 分辨率需求    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
