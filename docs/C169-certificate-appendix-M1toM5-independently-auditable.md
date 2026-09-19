已查地图（**先查后写**）：`C-163`（`M=3`）、`C-164`（`M=4`）、`C-168`（`M=5`）、`C-165`（误差模型核验）、`C-167`（向量化实现）、`E4-ENGINE-2`（引理 C）、`C-154`（`M=2`）。关键词回查：`证书附录`=1（`C-168` 已用该词 ⟹ **复用**）、`独立复核`=36（**通用词**）、`复现清单`=0（**本档新增**）。
**本档任务（唐先生 2026-09-19 15:15「继续」）**：**把 `M\le5` 收成一册可独立复核的证书附录。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{证书附录已建立}：\texttt{cert\_appendix/manifest.json}（含五情形参数、结果、哈希、复现命令）✓$$
$$\qquad \text{manifest 哈希}：\mathrm{SHA256}[:16]=\mathtt{7404cb37e7258940}✓$$
$$\textbf{(二)}\ \text{五情形全部}\ \mathbf{ok=true}（0\ \text{未决}）：M=1（\text{引理 C}）、2（\text{`C-154`}）、3、4、5✓✓$$
$$\textbf{(三)}\ \text{误差模型核验已补齐：}\text{三档参数范围}\（[0,15\pi],[0,20\pi],[0,25\pi]）\ \text{全部}\ 9007\times\ \text{裕度、0\ 违例}✓✓$$
$$\qquad （M=3\ \text{另有}\ \textbf{逐参数} \text{核验：}1{,}569{,}600\ \text{个，0 违例}）✓✓$$

FREEZE-ACK: 本档即冻结期内的收束与核验（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M\le5` 证书附录（manifest＋复现命令＋误差模型核验记录＋残留缺口清单）** —— 关系 = 收束与登记，非新机制
D1: 0

# C-169 · ⭐⭐ **证书附录（`M=1..5`）：可独立复核**

> **唐先生 2026-09-19 15:15**：继续（把 `M\le5` 收成一册）✓

---

## §1 定理族与状态

$$\textbf{目标}\ (\text{RP}_M)：\forall\varphi\in[0,\pi]^M,\qquad \max_{1\le k\le5M}\ \sum_{j=1}^{M}\cos(k\varphi_j)\ \ge\ \frac12✓$$
$$（\text{等价}：\forall z_j\in\mathbb C,\ |z_j|=1：\exists k\le5M,\ \Re\sum_j z_j^k\ \ge\ \tfrac12）✓$$
$$\begin{array}{c|l|c|c}
M & \text{工具} & \text{证书规模} & \text{状态}\\\hline
1 & \text{引理 C（初等闭合式，}\cos\tfrac{2\pi}{6}=\tfrac12\text{）} & —\ (\text{紧}) & ✓\\
2 & \text{局部解析（单纯形}\lambda\text{）＋ 远场证书} & \text{三段拼装} & ✓\\
3 & \text{自适应证书} & 17{,}440\ \text{箱}/0.06\ \text{s} & ✓\\
4 & \text{自适应证书} & 1{,}036{,}096\ \text{箱}/5.6\ \text{s} & ✓\\
5 & \text{自适应证书} & 72{,}440{,}000\ \text{箱}/951\ \text{s} & ✓\\
\end{array}✓✓$$

## §2 算法与严格性（三行证明）

$$\mathrm{LB}(B):=\max_{1\le k\le5M}\ \sum_{j=1}^{M}\Big(\min_{\varphi_j\in[a_j,b_j]}\cos(k\varphi_j)\Big)\qquad(B=\textstyle\prod_j[a_j,b_j])✓$$
$$\textbf{(i)}\ \forall\varphi\in B：\cos(k\varphi_j)\ \ge\ \min_{[a_j,b_j]}\cos(k\cdot)\ \Longrightarrow\ S_k(\varphi)\ \ge\ \sum_j\min\ \Longrightarrow\ \max_k S_k(\varphi)\ \ge\ \mathrm{LB}(B)✓$$
$$\textbf{(ii)}\ \text{算法}：\text{初始}\ N_0^M\ \text{等分}；\mathrm{LB}(B)<\tfrac12\ \Longrightarrow\ \text{细分}\ 2^M；\mathrm{LB}(B)\ge\tfrac12\ \Longrightarrow\ \text{认证}✓$$
$$\textbf{(iii)}\ \text{终止且未决}=0 \Longrightarrow \text{立方体全覆盖} \Longrightarrow (\text{RP}_M)✓✓$$
$$\text{保守化}：\text{每项}\ \mathrm{SLACK}=10^{-12}；\pi\text{-判定}\ \mathrm{TEST\_EPS}=10^{-9}✓$$

## §3 证书表（manifest 摘录）

$$\begin{array}{c|r|r|r|r|r}
M & N_0 & \text{评估箱数} & \text{未决} & \text{最小余量} & \text{用时}\\\hline
3 & 10 & 17{,}440 & 0 & 0.002004961256163118 & 0.06\ \text{s}\\
4 & 20 & 1{,}036{,}096 & 0 & 0.0002099798169962197 & 5.55\ \text{s}\\
5 & 10 & 72{,}440{,}000 & 0 & 3.956783786618345\times10^{-6} & 951.27\ \text{s}\\
\end{array}✓✓$$
$$\text{全部}\ \mathtt{ok=true}✓；\ \text{manifest}：\texttt{cert\_appendix/manifest.json}；\ \text{哈希}\ \mathtt{7404cb37e7258940}✓$$

## §4 复现（逐条命令）

$$\texttt{python3 scripts/rpM\_adaptive\_certificate\_idx.py 3 10 20000000 40}\quad(\to17{,}440\ \text{箱})✓$$
$$\texttt{python3 scripts/rpM\_adaptive\_certificate\_idx.py 4 20 20000000 40}\quad(\to1{,}036{,}096\ \text{箱})✓$$
$$\texttt{python3 scripts/rpM\_adaptive\_certificate\_idx.py 5 10 400000000 40}\quad(\to72{,}440{,}000\ \text{箱}，\sim16\ \text{分钟})✓$$
$$\texttt{python3 scripts/cert\_appendix\_run.py 3 4}\quad(\text{生成 manifest})✓$$
$$\text{参照实现（独立第二实现，供交叉核验）}：\texttt{scripts/rpM\_adaptive\_certificate.py}✓$$

## §5 误差模型核验记录

$$\textbf{(a)}\ M=3：\textbf{逐参数}（\text{该次运行全部}\ 1{,}569{,}600\ \text{个参数}）：\max|\Delta\cos|=1.110\times10^{-16}、\text{违例}\ 0、\text{裕度}\ 9007\times✓✓$$
$$\textbf{(b)}\ \text{三档范围抽样（各}\ 50{,}000，\text{共}\ 150{,}000）：$$
$$\begin{array}{c|c|c|c}
M & \text{范围} & \max|\Delta\cos| & \text{超}\ \mathrm{SLACK}\ \text{个数}\\\hline
3 & [0,15\pi] & 1.110\times10^{-16} & 0\\
4 & [0,20\pi] & 1.110\times10^{-16} & 0\\
5 & [0,25\pi] & 1.110\times10^{-16} & 0\\
\end{array}✓✓$$
$$\Longrightarrow \mathrm{SLACK}=10^{-12}\ \text{在全部三档上都有}\ 9007\times\ \text{裕度}✓✓$$

## §6 残留缺口（诚实清单）

$$\text{①}\ \textbf{M=5 未做逐参数核验}（\text{箱数}\ 7.2\times10^7 \Longrightarrow \text{参数}\ \sim10^9\ \text{个，}\text{不可全验}）⟹ \text{仅范围抽样}✓$$
$$\text{②}\ \text{形式化层面}：\text{区间算术代替}\ \mathrm{SLACK}\ \text{断言}；\text{或}\ \text{Lean 形式化}✓$$
$$\text{③}\ \text{独立实现交叉核验}：\text{已在}\ M=3,4\ \text{上做（逐位一致）}；M=5\ \text{仅单实现}✓$$
$$\text{④}\ \text{证书路线上限}：M=5（M=6\ \text{粗估}\ \sim10^{10}\ \text{箱}\Longrightarrow\text{不实际}）✓$$

## §7 边界与回查

- ⚠️ 本档为**收束与登记**（不产新结论）；所有数值可回溯到 `C-163`/`C-164`/`C-165`/`C-168` ✓
- ⚠️ **不声称** `(\text{RP}_6)`；**不声称**一般 `M`；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；回查须**排除本档自身**（`C-168` 记录的修正）✓

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 15:1x）`[纪律]`（先跑后写）

```
技术词 证书附录   命中文件数=1 :: ./C168-...md                    ⟹ 复用（C-168 已用）
技术词 独立复核   命中文件数=36 :: ./V186-...md ./CEILING-...md ...  ⟹ 通用词（不计）
技术词 复现清单   命中文件数=0 ::                                 ⟹ 本档新增
```
**读数（按实测）**：`证书附录`＝**复用**；`独立复核`＝**通用词**；`复现清单`＝**本档新增** ✓
