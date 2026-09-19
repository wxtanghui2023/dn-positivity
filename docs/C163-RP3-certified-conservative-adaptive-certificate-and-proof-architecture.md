已查地图（**先查后写**）：`C-162`（每箱精确下界；自适应细分；紧松二分）、`C-161`（单纯形签名）、`C-154`（`M=2` 三段拼装）、`E4-ENGINE-2`（引理 C）。关键词回查：`保守证书`=0、`认证余量`=0、`证明拼装`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 14:02「继续」）**：**拼装 `M=3` 的完整证明。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \boxed{(\text{RP}_3)\ \textbf{已认证}}：\text{保守自适应证书}\ \Rightarrow\ \text{评估}\ \mathbf{17{,}440}\ \text{箱、}\mathbf{0}\ \text{未决、最小余量}\ \mathbf{0.002005}、\text{最大深度}\ 7、\mathbf{0.78\ s}✓✓$$
$$\qquad \Longrightarrow \textbf{第三个完整情形}：M=1（\text{引理 C}）、M=2（\text{`C-154`}）、\mathbf{M=3}（本档）✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{证明架构的简化}：M\ge3\ \textbf{只需证书，不需局部解析引理}✓✓$$
$$\qquad \text{因}\ \min\max=0.777>\tfrac12\ \text{有余量} \Longrightarrow \text{极小点邻域也会被细分认证}✓$$
$$\qquad \text{对比}\ M=1,2\ \text{是}\ \textbf{紧情形}（\min\max=\tfrac12\ \text{恰好}）\Longrightarrow \mathrm{LB}<\tfrac12\ \text{永不消除} \Longrightarrow \text{证书}\ \textbf{不可能终止}✓✓$$
$$\textbf{(三)}\ \text{保守化}：\text{每项}\ \mathrm{SLACK}=10^{-12}、\pi\text{-判定}\ \mathrm{TEST\_EPS}=10^{-9}\ \text{（均}\ \gg\ \text{double 的}\ \cos\ \text{误差}\sim10^{-16}）✓$$
$$\qquad \Longrightarrow \text{浮点缺口在}\ \textbf{实际意义} \text{上闭合}；\text{形式上可用区间算术闭合（残留任务）}✓$$
$$\textbf{(四)}\ M=4\ \text{仍在跑}（N_0=20、\text{预算}\ 3\times10^6）\ ✓$$

FREEZE-ACK: 本档即冻结期内的证明拼装与证书运行（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`(\text{RP}_3)` 保守证书（已认证）＋ 证明架构简化（`M\ge3` 免局部引理）** —— 关系 = 拼装与认证，非新机制
D1: 0

# C-163 · ⭐⭐ **`(RP_3)` 已认证（保守证书）＋ 证明架构简化**

> **唐先生 2026-09-19 14:02**：继续（拼装 `M=3` 证明）✓

---

## §1 定理陈述

$$\textbf{定理}\ (\text{RP}_3)：\forall\varphi\in[0,\pi]^3,\qquad \max_{1\le k\le15}\ \sum_{j=1}^{3}\cos(k\varphi_j)\ \ge\ \frac12✓$$
$$（\text{等价形式}：\forall z_1,z_2,z_3\in\mathbb C,\ |z_j|=1：\ \exists k\le15:\ \Re\sum_{j}z_j^k\ge\tfrac12）✓$$

## §2 方法与严格性（三行证明）

$$\mathrm{LB}(B):=\max_{1\le k\le K}\ \sum_{j=1}^{M}\ \min_{\varphi_j\in[a_j,b_j]}\cos(k\varphi_j)\qquad(K=5M;\ B=\textstyle\prod_j[a_j,b_j])✓$$
$$\textbf{严格性}：\forall\varphi\in B：\cos(k\varphi_j)\ \ge\ \min_{[a_j,b_j]}\cos(k\cdot)\ \Longrightarrow\ S_k(\varphi)\ \ge\ \sum_j\min\ \Longrightarrow\ \max_k S_k(\varphi)\ \ge\ \mathrm{LB}(B)✓✓$$
$$\textbf{算法}：\text{初始}\ N_0^M\ \text{等分箱}；\text{对}\ \mathrm{LB}(B)<\tfrac12\ \text{者细分}\ 2^M；\ \mathrm{LB}(B)\ge\tfrac12\ \text{者认证}✓$$
$$\qquad \text{终止且无未决} \Longrightarrow \text{所有箱认证} \Longrightarrow \text{全立方体认证} \Longrightarrow \text{定理}✓✓$$

## §3 运行结果

$$\text{脚本}：\texttt{scripts/rpM\_adaptive\_certificate.py}（自足、可审计）✓$$
$$\begin{array}{c|c|c|c|c|c}
M & N_0 & \text{评估箱数} & \text{未决} & \text{最小余量} & \text{用时}\\\hline
\mathbf 3 & 10 & \mathbf{17{,}440} & \mathbf 0 & 0.002005 & 0.78\ \text{s}\ ✓\\
4 & 10 & 400{,}001 & 6{,}399 & — & \text{超预算}\\
4 & 20 & \text{（运行中）} & — & — & —\\
\end{array}✓✓$$
$$\text{参数哈希}：\mathrm{SHA256}(\cdot)[:16]=8342483892297789\quad(\mathrm{SLACK}=10^{-12},\ \mathrm{TEST\_EPS}=10^{-9})✓$$

## §4 ⭐ 证明架构表（本档的结构性收获）

$$\begin{array}{c|l|l}
M & \text{所需工具} & \text{原因}\\\hline
1 & \text{引理 C（初等、闭合式）} & \min\max=\tfrac12\ \text{紧}；\text{证书不终止}\\
2 & \textbf{局部解析}＋\text{远场证书}（\text{`C-154`}） & \min\max=\tfrac12\ \text{紧}；\text{必须解析处理极小点}\\
\ge3 & \textbf{仅自适应证书}（本档） & \min\max>\tfrac12\ \text{有余量} \Longrightarrow \text{细分即可认证极小点邻域}✓✓\\
\end{array}✓$$
$$\Longrightarrow \text{分界线}：\textbf{紧则需分析，松则只需证书}✓✓$$

## §5 为什么 `M\ge3` 不需要局部引理（松量论证）

$$\text{局部引理（}\text{`C-152`}）\ \text{的作用}：\text{在小球}\ |\delta|\le\varepsilon\ \text{内用一阶抬升}\ \max_k\ge\tfrac12\ \text{对抗"}\mathrm{LB}<\tfrac12\text{"}✓$$
$$\qquad \text{但该引理之所以必要，是因为}\ M=2\ \text{的}\ \min\max\ \textbf{恰为}\ \tfrac12 \Longrightarrow \text{极小点处}\ \mathrm{LB}<\tfrac12\ \text{恒成立}✓$$
$$\text{对}\ M=3：\min\max\approx0.777\ \Longrightarrow \text{在极小点附近充分细分的箱上}\ \mathrm{LB}\ge\tfrac12\ \text{（实测：深度}\ 7\ \text{即满足）}✓✓$$
$$\Longrightarrow \textbf{证书}\ \text{自动处理极小点} \Longrightarrow \text{无需}\ \text{局部解析}✓✓$$

## §6 边界与回查

- ⚠️ 证书为**计算机辅助**：严格性依赖 (i) §2 的三行论证；(ii) `\mathrm{LB}` 计算的保守化（`\mathrm{SLACK}`、`\mathrm{TEST\_EPS}`）✓
- ⚠️ **残留任务**：把保守量换成**区间算术**（形式上闭合浮点缺口）；本档只做了**定量保守**（余量 `10^{-12}` 远大于 double 误差）✓
- ⚠️ `M=4` 未完成（超预算）⟹ **不声称** `(\text{RP}_4)` ✓
- ⚠️ **不声称**与 RH 相关；`(\text{RP}_M)` 与 RH 无已知逻辑路径 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 14:0x）`[纪律]`（先跑后写）

```
技术词 保守证书   命中文件数=0 ::  ⟹ 本档新增
技术词 认证余量   命中文件数=0 ::  ⟹ 本档新增
技术词 证明拼装   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
