已查地图（**先查后写**）：`C-216`–`C-219`（原区间阶梯）、`C-265`（M=4）、`C-177`（参数化脚本）、`E4-ENGINE-5`（§2 M≳12 必死）、`PLAN-RPM-ladder-logic-chain-and-cost-preregistration`（预注册判据）。回查见 §5 ✓

D0: 本档对象 = **(RP_M) 证书引擎 v3：向量化提速 ＋ 四项验收自检** —— 关系 = 工程实现（不改数学）
D1: 0
FREEZE-ACK: 本档即冻结期内的工程实现（依 §8.1；不产候选结论）

---

## §0 结论

$$\boxed{\textbf{① 提速}✓✓：\text{M}=3\ 392.5\ \text{s}\to\textbf{1.3 s}\ ✓；\text{M}=4\ 5501.8\ \text{s}\to\textbf{4.2 s}\ ✓ \Longrightarrow \sim300\text{–}1300\times✓}$$
$$\boxed{\textbf{② 两个已知结果均复现}✓✓：m_3\ge0.75✓；m_4\ge0.5✓（\text{未决均}=0✓）}$$
$$\boxed{\textbf{③ 四项验收已仪表化}✓✓（\text{唐先生指定}✓）：筛余量自检／贴线箱／铺满／参数齐全✓}$$
$$\boxed{\textbf{④ 严格性诚实标注}✗✓：v3＝\textbf{模显式浮点模型}✓；\textbf{慢版仍是金标准}✓✓（\text{无 SLACK、无浮点假设}✓）}$$
$$\boxed{\textbf{⑤ 加速}\neq\text{证明}✗✓：\text{阶梯仍未跑}✓；\text{每个}M\ \text{须逐项验收}✓}$$

## §1 引擎设计（v3 ✓）

$$\text{① pending-buffer}✓（\text{DFS 内存特征＋满批 15 万箱的 numpy 效率}✓）\ \text{—— 修 v2 的 BFS frontier 爆炸}✗（\text{M=5 曾冲}2.5\text{M 箱}✗）$$
$$\text{② 浮点筛}✓：\text{每项下移}\ \varepsilon_{\rm term}=10^{-11}✓（\text{≫最坏 1-ulp}✓）\Longrightarrow LB_{\rm true}\ge LB_{\rm float}-10^{-9}✓$$
$$\text{③ 安全带}✓：\text{margin}\in(0,10^{-9}]\ \text{与深限箱}\ \text{交【原已验收】}\ \texttt{core.lb\_box}\ \text{复核}✓$$
$$\text{④ 覆盖}✓：\text{初始网格【共享边}】✓＋\text{拆分【共享中点}】✓ \Longrightarrow \text{精确铺满}✓\（\text{旧版微缝}\sim10^{-16}\ \text{已修}✗）$$
$$\text{⑤ 资源}✓：\text{单进程}✓；\text{pending 上限按}M\ \text{自适应}（\approx300\ \text{MB}✓）$$

## §2 复现与验收（✓✓）

| 运行 | 评估箱数 | 筛认证 | 区间复核 | 未决 | 最小余量 | 体积自检 | 耗时 | 原版 |
|---|---|---|---|---|---|---|---|---|
| $M=3$／0.75 | 300,926 | 294,211 | **0** | **0** | $2.456\times10^{-5}$ | $1.1\times10^{-16}$ | **1.3 s** | 392.5 s |
| $M=4$／0.5 | 598,607 | 439,224 | **0** | **0** | $3.258\times10^{-5}$ | $1.5\times10^{-16}$ | **4.2 s** | 5501.8 s |

$$\textbf{自检}✓✓（M=5, 50 样本）：\textbf{筛值高于真值次数}=0✓（\text{永不越界}✓）；\text{最大低估}=5.0\times10^{-11}\le10^{-9}✓✓$$

## §3 四项验收对应（✓✓）

$$\textbf{(A) 浮点筛证余量}✓：\text{自检 PASS}✓（\text{越界}0✓，\text{低估}\le5\times10^{-11}✓）$$
$$\textbf{(B) 贴线箱／边界}✓：\text{区间复核次数}=0✓（\text{无箱落带内}✓）；\text{域用}\ P=\pi_{\rm hi}>\pi✓ \text{使}\ \pi\ \text{边界为内点}✓$$
$$\textbf{(C) 箱交覆盖}✓✓：\text{体积自检相对差}\sim10^{-16}✓（\text{共享边}＋\text{共享中点}✓）$$
$$\textbf{(D) 参数完整}✓：K=5M\ \text{全额}✓；\text{域}[0,P]^M\supset[0,\pi]^M✓；\text{反射约化}\ \varphi\to2\pi-\varphi\ \text{不变}✓ \Longrightarrow \varphi\in[0,\pi]\ \text{充分}✓$$
$$\textbf{(E) 资源}✓：\text{单进程}✓；\text{上限自适应}✓；\text{慢版 M=5 RSS}=16\ \text{MB}✓$$

## §4 本档发现并修掉的错误（✗✓）

$$\text{① v2 的 BFS frontier 爆炸}✗（\text{M=5 未决}3{,}116{,}630）\to\text{pending-buffer}✓$$
$$\text{② v3 的带条件写错}✗：\texttt{(Rm > -inf) \& (Rm<=BAND)} \Longrightarrow \textbf{所有待拆分箱都做慢速区间复核}✗（\text{M=3 从}1.4\ \text{s 劣化到}49.4\ \text{s}✗）\to\texttt{(Rm>0)\&(Rm<=BAND)}✓$$
$$\text{③ 网格微缝}✗：A_i+B_i\ \text{与}\ A_{i+1}\ \text{可差}\sim10^{-16}\to\text{共享边}✓$$
$$\text{④ 流程错}✗：\texttt{pkill -f} \text{模式含自身命令行}\Longrightarrow \textbf{自杀式杀 shell}✗（\text{本会话第二次}✓，改用显式 PID＋\texttt{ps -C}✓）$$

## §5 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写** ✓）

```
技术词 浮点筛证余量   命中文件数=0 ::
技术词 贴线箱安全带   命中文件数=0 ::
技术词 引擎提速验收   命中文件数=0 ::
```
$$\textbf{① 本档新增}✓：\text{三项各 0 命中}⟹\textbf{本档首次命名}✓$$
$$\textbf{② 档案已有（引用）}✓✓：\text{四门协议}✓（\texttt{C-216}✓）；\text{区间函数}✓（\texttt{m3\_certificate\_interval\_arith.py}✓）$$

## §6 边界

$$\textbf{① 本档为工程实现}✓，\text{不改数学、不产定理}✗；\ \textbf{② 未用 RH}✓；\text{未改他档正本}✓$$
$$\textbf{③ v3 的严格性＝}\textbf{模显式浮点模型}✗✓（\text{已声明}✓）；\textbf{金标准仍是慢版区间版}✓✓$$
$$\textbf{④ 阶梯（}M=5..11\text{）【尚未跑}】✗ —— \text{遵纪律「不另起并发」✓，待唐先生定序列}✓$$
$$\textbf{⑤ 慢版 M=5 继续跑}✓（\text{pid 3637}✓）\ \text{—— 它同时充当【独立实现交叉检验}】✓✓$$
