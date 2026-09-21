已查地图（**先查后写**）：`C-338`（P4-B：`A = {5,12,14}`，21 近邻 ✓；`5+21 = 12+14` ✓）、`C-337`（P4-A ✓）、`C-336`（幂和单调性 ✓）、`C-330`（缺口＝max-min 交换 ✓）、`C-284`（gcd 坍缩 ✓，本处 `gcd = 1` ⟹ 不适用 ✓）。回查见 §6 ✓

D0: 本档对象 = **C-339：P4-C（三频核心的解析审计 ＋ 活跃数下界）**，**有计算（已批准 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（四条 ✓✓）

$$\textbf{① ⭐ 解析结论（本档最有价值）}✓✓：\text{内部极小点}\ \Longrightarrow \textbf{活跃频率数}\ m \ge 6✓✓（\text{因梯度空间}\ 5\ \text{维}✓，\text{权}\ \lambda \in \Delta^m\ \text{有}\ m-1\ \text{个自由度}✓ \Longrightarrow m-1 \ge 5✓）$$
$$\textbf{② 冠军非精确 KKT}✗✓：\text{数值冠军}\ \textbf{只有}\ 4\ \text{个近并列}✗（gaps ≤ 1.4 \times 10^{-7}✓）\ \Longrightarrow \ \textbf{不是} \text{精确内部极小点}✗ \Longrightarrow \text{真极小点}\ \textbf{或} \text{有} \ge 6\ \text{活跃}✓，\textbf{或在边界上}✓$$
$$\textbf{③ 唐先生恒等式已数值验证}✓✓：\ F_5 + F_{21} = F_{12} + F_{14}✓（\text{差}\ -3.86 \times 10^{-8}✓）\ \text{且因式分解}\ 2\sum_j \cos(13\theta_j)[\cos(8\theta_j) - \cos(\theta_j)]✓（= -3.86 \times 10^{-8}✓）\ \textbf{逐字成立}✓✓$$
$$\textbf{④ 三频共同根不精确}✗：\text{冠军五节点}\ \textbf{只有两个} \text{是}\ Q\ \text{的近似根}✓（-0.872↔-0.873✓；0.910↔0.907✓）\ \text{另两个}\ (-0.137,\ +0.091)\ \textbf{无对应根}✗$$

## §1 冠军的近并列结构（✓✓）

$$\text{（8 位小数）}G_{num} = 0.973822815769✓；\text{容差}\ 10^{-6}\ \text{下}\ A = \{5,\ 12,\ 14,\ 21\}✓$$
$$\text{gaps}✓：F_5 - G = -1.352 \times 10^{-7}✓；F_{12} - G = -8.309 \times 10^{-8}✓；F_{14} - G = -1.356 \times 10^{-8}✓；F_{21} - G = 0✓$$
$$\Longrightarrow \textbf{近并列（near-tie）结构确凿}✓✓ \Longrightarrow \ \textbf{活跃集随容差漂移}✓（10^{-6}\ \text{四个}✓，10^{-9}\ \text{三个}✓）$$

## §2 ⭐ 活跃数下界（✓✓，本档核心 ✓）

$$\textbf{KKT}✓：\text{内部极小点须}\ 0 \in \operatorname{conv}\{\nabla F_k : k \in A\}✓ \Longrightarrow \exists \lambda_k > 0✓，\sum_k \lambda_k = 1✓，\sum_k \lambda_k \nabla F_k = 0✓$$
$$\textbf{维数计数}✓✓：\ \nabla F_k \in \mathbb{R}^5✓（\text{变量}\ c \in [-1,1]^5✓）\ \Longrightarrow \text{未知数}\ \lambda\ \text{有}\ m-1\ \text{个自由}✓ \ ——\ \text{方程}\ 5\ \text{个}✓ \Longrightarrow \boxed{m - 1 \ge 5 \iff m \ge 6}✓✓$$
$$\textbf{注}✓：\text{此}\ \textbf{不}\ \text{依赖}\ C\text{-284 或任何频率结构}✓ \ —— \ \text{纯粹是}\ \textbf{维数／凸性}\ \text{条件}✓✓$$
$$\textbf{可检验预测}✓✓：\text{真极小点}\ \text{若在内部}\ \Longrightarrow\ \textbf{至少 6 个}\ F_k\ \text{并列}✓；\text{否则在边界}✓ \Longrightarrow \text{下轮可据此定向}✓✓$$

## §3 三频 KKT 数值检验（✓✗）

$$A = \{5, 12, 14\}✓；\ \lambda\ \text{由最小二乘解}✓：\lambda = (0.03231438,\ 0.00995265,\ 0.01072418)✓ \ —— \ \textbf{和} = 0.052991 \ne 1✗✓（\textbf{说明无法同时满足梯度与归一}✓）$$
$$\text{梯度残差}✓（前五项）＝ [-0.018749,\ -0.061759,\ +0.104056,\ +0.183244,\ -0.040142]✓ \ \Longrightarrow \ \textbf{相对残差} \approx 5 \times 10^{-4}✓（\text{梯度尺度} \approx 182✓）$$
$$\textbf{读法}✓：\text{冠军}\ \textbf{不}\ \text{是}\ \text{精确三频 KKT 点}✗；\text{但其残差}\ \textbf{不大}✓ \Longrightarrow \text{与「数值候选＋近并列」一致}✓✓$$

## §4 `5+21 = 12+14` 的代数审计（✓✓）

$$\textbf{唐先生因式分解}✓✓：\cos a\theta + \cos b\theta = 2\cos\tfrac{(a+b)\theta}{2}\cos\tfrac{(a-b)\theta}{2}✓ \Longrightarrow F_5 + F_{21} = 2\sum_j \cos(13\theta_j)\cos(8\theta_j)✓；F_{12} + F_{14} = 2\sum_j \cos(13\theta_j)\cos(\theta_j)✓$$
$$\Longrightarrow \textbf{等价于}\ \boxed{\sum_j \cos(13\theta_j)[\cos(8\theta_j) - \cos(\theta_j)] = 0}✓✓$$
$$\textbf{数值验证}✓✓：\text{该和} = -1.930 \times 10^{-8}✓；\ 2\times = -3.860 \times 10^{-8}✓ \ \text{与}\ (F_5+F_{21}) - (F_{12}+F_{14}) = -3.860 \times 10^{-8}✓ \ \textbf{完全一致}✓✓$$
$$\textbf{定位}✓✓：\text{这是}\ \textbf{候选极值结构}✓，\textbf{不}\ \text{是}\ \text{「冠军必须满足的恒等式」}✗✓（\text{唐先生口径}✓）\ —— \ \text{可作}\ \textbf{候选解释变量}✓，\textbf{不}\ \text{直接塞进证明}✗✓$$

## §5 三出口判定（✓✓）

$$\text{① 得到可证明的}\ G > \tfrac12\ \text{下界}✗：\textbf{未}\ \text{获得}✗（\text{本档未产生下界}✓）$$
$$\text{② 得到新的明确约束}✓✓：\textbf{获得}✓ \ —— \ \boxed{\text{内部极小} \Longrightarrow m \ge 6}✓✓（\text{维数／凸性}✓）\ ＋\ \text{恒等式}\ 5+21=12+14\ \text{已验证}✓$$
$$\text{③ 证明该机制不足以产生解析下界}✗：\textbf{未}\ \text{下该结论}✗ \Longrightarrow \text{保留}✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 内部驻点条件 命中文件数=0    :: 
技术词 活跃数下界  命中文件数=1    :: ./C162-exact-per-box-bound-and-adaptive-certificate-compression-measured.md 
技术词 近并列结构  命中文件数=0    :: 
```
- 运行记录 ✓：脚本 `/tmp/p4c2.py` ✓（手写 Chebyshev `U/T` 递推；`np.linalg.lstsq` ✓；`np.roots` ✓）
- **本档有计算**（已批准 ✓）；`D1 = 0` ✓；未改他档正本 ✓；未动 v4 ✗；`C-181` 的 `u<=5` 仍 **GAP-A** ✓
- **不得**写成：`m >= 6` 是极小点的充要条件 ✗（**仅内部必要条件** ✓）；`5+21=12+14` 已是定理 ✗；M=5 已证 ✗；`G_min` 已定 ✗
