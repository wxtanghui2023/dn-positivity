已查地图（**先查后写**）：`C-172`（近似周期引理；推论依赖 `m_M\le M-1`）、`C-159`（概率方法 `m_M\le\sqrt{2M\ln10M}`）、`C-173`/`C-174`（改进阈值）、`C-175`（四条归约路线失效）。关键词回查：`上界证书`=0、`精确有理角度`=0、`推论无条件化`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 19:00「补上」）**：**补上 `C-172` 推论链条上唯一的数值环节 —— `m_M\le M-1`（`M\le11`）严格化。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{洞已补}：\text{对}\ 2\le M\le11\ \text{给出}\ \textbf{显式配置 ＋ 区间算术证书} \Longrightarrow m_M\le M-1\ \textbf{严格成立}✓✓$$
$$\qquad \text{配}\ \text{`C-159`}\ \text{（}M\ge12：m_M\le\sqrt{2M\ln10M}\le M-1，\text{已严格）} \Longrightarrow \boxed{m_M\le M-1\ \ \textbf{对一切}\ M\ge2\ \textbf{严格成立}}✓✓$$
$$\textbf{(二)}\ \Longrightarrow \text{`C-172`}\ \text{的}\ \textbf{推论（单调性步）不再依赖数值输入}：\text{在近似周期假设下无条件成立}✓✓$$
$$\textbf{(三)}\ \text{副产品}：\text{`C-174`}\ \text{的加强阈值可用}\ \textbf{认证值}\ U_3=0.777171\ \text{（严格）替代数值}\ 0.7641✓$$
$$\textbf{(四)}\ \text{方法（严格性来源）}：\text{角度取}\ \textbf{3 位小数的度}（=\text{精确有理}\ d/1000）；k\varphi_j=kd\pi/180000 \Longrightarrow \textbf{唯一非精确对象是}\ \pi✓$$
$$\qquad \Longrightarrow \text{用}\ \texttt{mpmath.iv}\ \text{的区间表示}\ \pi/\cos/\text{求和}，\text{取每}\ k\ \text{的}\ \textbf{区间上端}，\text{再对}\ k\ \text{取最大}✓✓$$

FREEZE-ACK: 本档即冻结期内的证书与登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`m_M` 上界的区间算术证书（`M\le11`）＋ 推论无条件化 ＋ 脚本与数据入库** —— 关系 = 补洞与登记，非新机制
D1: 0

# C-176 · ⭐⭐ **`m_M\le M-1` 严格化（`M\le11`）—— 洞已补**

> **唐先生 2026-09-19 19:00**：补上 ✓

---

## §1 结果

$$\textbf{定理（本档）}：\text{对}\ 2\le M\le11：m_M:=\min_{\varphi\in[0,\pi]^M}\max_{1\le k\le5M}\sum_{j=1}^M\cos(k\varphi_j)\ \le\ M-1✓$$
$$\begin{array}{c|r|r|r}
M & \text{认证上界}\ U_M & M-1 & \text{余量}\\\hline
2 & 0.500000 & 1 & 0.500\\
3 & 0.777171 & 2 & 1.223\\
4 & 0.846053 & 3 & 2.154\\
5 & 0.944329 & 4 & 3.056\\
6 & 1.257351 & 5 & 3.743\\
7 & 1.357178 & 6 & 4.643\\
8 & 1.636991 & 7 & 5.363\\
9 & 1.762500 & 8 & 6.238\\
10 & 1.805161 & 9 & 7.195\\
11 & 2.187478 & 10 & 7.813\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{余量极大}（0.5\text{–}7.8）\ \Longrightarrow \text{证书不依赖精细优化}✓$$

## §2 方法：严格性来自何处

$$\text{(i)}\ \text{角度以}\ \textbf{3 位小数的度} \text{给出} \Longrightarrow \varphi_j=d_j/1000\ \text{度}\ \text{（}d_j\in\mathbb Z，\textbf{精确有理}）✓$$
$$\text{(ii)}\ k\varphi_j=\frac{k\,d_j}{180000}\pi \Longrightarrow \frac{k\,d_j}{180000}\in\mathbb Q\ \text{是}\ \textbf{精确有理数}（\text{整数运算}）✓$$
$$\qquad \Longrightarrow \textbf{唯一的非精确对象是}\ \pi\ \text{本身}✓✓$$
$$\text{(iii)}\ \text{用}\ \texttt{mpmath.iv}\ \text{（}60\ \text{位精度）}：\pi\ \text{取区间} \Longrightarrow \cos(k\varphi_j)\ \text{取区间} \Longrightarrow \text{求和取区间}✓$$
$$\text{(iv)}\ \text{对每个}\ k\ \text{取}\ \textbf{区间上端}，\text{再对}\ k\le5M\ \text{取最大} \Longrightarrow \text{严格上界}✓✓$$
$$\qquad \text{（不需要 Lipschitz 余项；不需要浮点误差模型 —— 误差全部由区间算术吸收）}✓✓$$

## §3 与 `M\ge12` 合并 ⟹ 全 `M`

$$\text{`C-159`}\ \text{（概率方法，已严格）}：m_M\ \le\ \sqrt{2M\ln(10M)}✓$$
$$\qquad M=12：\sqrt{2\cdot12\cdot\ln120}=10.72\ \le\ M-1=11✓；\ M=13：11.25\le12✓；\ \text{且该界随}\ M\ \text{增长慢于}\ M✓$$
$$\Longrightarrow \text{合并}：\ \boxed{m_M\le M-1\quad\text{对一切}\ M\ge2\ \text{严格成立}}✓✓$$
$$\qquad \text{（`M=1` 例外：}\ m_1=\tfrac12>0=M-1✓\ ——\ \text{与}\ \text{`C-171`}\ \text{的解剖一致}）✓$$

## §4 后果：`C-172` 推论无条件化

$$\text{`C-172`}\ \text{推论}：\varepsilon\le\sqrt{\tfrac2{9M}}\ \text{且}\ m_M\le M-1 \Longrightarrow \textbf{单调性步}\ m_{M+1}\ge m_M\ \text{在该配置上成立}✓$$
$$\qquad \text{原状态}：M\ge12\ \text{严格}；M\le11\ \textbf{数值}✗ \Longrightarrow \text{现在：}\textbf{全部严格}✓✓$$
$$\text{`C-174`}\ \text{加强阈值}：\text{原用数值}\ m_3\le0.7641；\text{现可用}\ \textbf{认证值}\ U_3=0.777171✓\ \text{（严格）}$$
$$\qquad \Longrightarrow \text{阈值}\ \varepsilon\le\sim51^\circ\ \text{的链条亦为严格（}U_3\ \text{略宽于}\ 0.7641，\text{阈值略紧，量级不变）}✓$$

## §5 复现与入库

```
脚本: scripts/mM_upper_bounds_certificate.py   （区间算术证书，自带复现说明）
数据: data/mM_configs_millideg.json            （10 组配置，角度×1000 的整数）
      data/mM_upper_bounds_certified.json      （认证上界）
运行: python3 scripts/mM_upper_bounds_certificate.py
输出: 每 M 的 U_M 与 OK；本档实测全 True（余量 0.5–7.8）
```

$$\text{配置示例（度，3 位小数）}：M=3:\ 113.334,\ 76.418,\ 20.216；\ M=11:\ 4.694,\ 131.680,\ 43.939,\ 11.698,\ 161.086,\ 77.595,\ 107.773,\ 147.746,\ 22.680,\ 49.492,\ 114.477✓$$

## §6 边界

- ⚠️ 证书依赖 `\texttt{mpmath.iv}`（标准区间算术实现）的正确性 ✓
- ⚠️ 配置为启发式搜索所得，**仅作上界用途**；不是 `m_M` 的精确值，也不是下界 ✓
- ⚠️ 本档**不证** `(\text{RP}_M)` 一般成立；**不证**单调性一般成立 ✓
- ⚠️ 只补了一处**数值输入** ⟹ 链条变为严格；**不改变** `C-174`/`C-175` 的结论（近似周期类仍到不了最硬点）✓
- **未用** RH；**未改**任何原档（`C-172` 状态可在后续统一加指针）✓
- **纪律**：先查后判（R-1 ✓）、**先跑后写** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 19:0x）`[纪律]`（先跑后写）

```
技术词 上界证书     命中文件数=0 ::  ⟹ 本档新增
技术词 精确有理角度  命中文件数=0 ::  ⟹ 本档新增
技术词 推论无条件化  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
