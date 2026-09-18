已查地图（**先查后写**）：`C-121`（三层设计与第一行硬检查）、`IMPL-3`（Toeplitz 候选的来源）、`lean-frontier-audit/{LawN256,NumericCert,Defs}.lean`（**本档逐字读取 S 的定义**）、`lp/ceiling_lp_recompute.py`（本档实测变体）。关键词回查：`对角占优判据`＝0、`混合顶点性`＝0、`G3 审计`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:18「下一步严格进入 C-121-B」⟹ 执行 **第一个 G3 候选（Toeplitz PSD）的 K2 审计**，**判死（非独立）** ✓✓：**(甲)** `S` 的语义已逐字钉死（**凸混合**：`S(j)=\frac{1}{256}\sum_c w_c|\sum_i m_{c,i}e^{2\pi i j x_{c,i}/256}|^2`，`w_c\ge0`，`\sum_c w_c=1`，`m_{c,i}\in\{1,2\}`，`\sum_i m_{c,i}=256`）✓✓；**(乙) ⭐ K2 判定：Toeplitz PSD \textbf{不是独立必要条件}**——因 `S(0)=256`（精确，由 `\sum_i m=256`）而**非对角** `|S(j)|\le(255+\tau)/256<1` ⟹ **Gershgorin 严格对角占优**（行和 `\le254.0039<256`）⟹ PSD **自动成立**（实测最小特征值 `204.122903`）⟹ 它由点式 envelope **蕴含** ⟹ **repackaging** ✓✓；**(丙) ⭐ 由此得 G3 审计判据**：任何 G3 候选若被 `S(0)` 支配 ⟹ 惰性；有意义的 G3 **必须触及 envelope 完全未钉的东西**（相位／位置／支撑）✓✓

FREEZE-ACK: 本档即冻结期内的 C-121-B 审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **第一个 G3 候选（Toeplitz PSD）的 K2 审计结论 ＋ 由此得到的 G3 审计判据** —— 关系 = 审计与判据提取，非新机制
D1: 0

# C-122 · **C-121-B 第一刀：Toeplitz PSD 的 K2 审计 ＝ 判死（非独立）**

> **时间**：2026-09-18 23:18 唐先生：**「下一步应严格进入 C-121-B」** ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ S\ \text{的语义＝}\textbf{凸混合}（\text{逐字，见 §1}）✓✓$$
$$\textbf{(乙)}\ ⭐\ \textbf{Toeplitz PSD 判死（K2）}：\text{由}\ S(0)=256\ \text{与非对角}\le255/256 \Longrightarrow \textbf{严格对角占优} \Longrightarrow \text{PSD 自动成立}✓✓$$
$$\textbf{(丙)}\ ⭐\ \text{得}\ \textbf{G3 审计判据}：\text{被}\ S(0)\ \text{支配者惰性};\ \text{有意义的 G3 必须触及}\ \textbf{相位／位置／支撑}✓✓$$

---

## §1 `S` 的语义（逐字，`LawN256.lean` 首段）

$$\text{逐字}：\text{"enclosures }lo_j\le K\cdot S(j)\le hi_j,\ j=1..256,\ \text{of the grid form factor}"✓$$
$$\qquad S(j)=\frac{1}{256}\sum_c w_c\Big|\sum_i m_{c,i}e^{2\pi i j x_{c,i}/256}\Big|^2✓✓$$
$$\qquad \text{"exact rational weights }w_c\ge0\ \text{summing to 1, rational positions }x_{c,i}\in[0,256),\ \text{marks }m_{c,i}\in\{1,2\}\ \text{with}\ \sum_i m_{c,i}=256"✓✓$$
$$\text{行证书（逐字）}：\big|256\cdot S(j)-j\big|\le\tau:=\tfrac{3}{10^{40}}\ (0<j<256);\quad |D(1)|\le\tfrac{82395317}{10^{8}}✓$$
$$p_0=1-a_N=\tfrac{10909258999421303588095230195816054408197}{16000000000000000000000000000000000000000}=0.68182868746\ldots✓$$
$$\qquad ⚠️\ \text{"verified outside Lean by interval arithmetic"};\ \text{下游全部 kernel-checked}✓$$

## §2 ⭐ K2 审计：Toeplitz PSD **不是**独立必要条件

$$\text{要审}：\text{矩阵}\ T_{ij}:=S(|i-j|)\ (i,j=0..255)\ \textbf{半正定}\ \text{是否只是点式 envelope 的线性推论}✓$$
$$\textbf{第一步（精确）}：S(0)=\frac{1}{256}\sum_c w_c\big|\sum_i m_{c,i}\big|^2=\frac{256^2}{256}=256\quad（\text{因}\ \sum_i m_{c,i}=256）✓✓$$
$$\textbf{第二步（精确）}：0<j<256 \Longrightarrow |S(j)|\le\frac{j+\tau}{256}\le\frac{255+\tau}{256}<1✓✓$$
$$\textbf{第三步（Gershgorin）}：\text{行非对角和}\ \le 255\cdot\frac{255+\tau}{256}=254.0039\ldots<256=|T_{ii}|✓✓$$
$$\Longrightarrow \textbf{严格对角占优} \Longrightarrow T\ \textbf{正定} \Longrightarrow \text{PSD}\ \textbf{自动成立}✓✓$$
$$\textbf{实测（本档）}：\lambda_{\min}(T)=204.122903>0;\quad \lambda_{\max}=344.9350✓✓$$
$$\Longrightarrow ⭐\ \text{PSD 是}\ \textbf{envelope 的推论}（\text{且余量极大}） \Longrightarrow \textbf{不增加任何信息} \Longrightarrow \boxed{\textbf{K2 命中（repackaging）}}✓✓$$

## §3 ⭐ 由此得到的 **G3 审计判据**（本档净产出）

$$\text{若某 G3 候选的可满足性被}\ S(0)=N\ \text{支配} \Longrightarrow \textbf{惰性} \text{（本档实例）}✓✓$$
$$\text{有意义的 G3}\ \textbf{必须触及 envelope 完全未钉的量}：\text{相位}（=\text{位置}\ x_{c,i}）、\ \textbf{支撑}、\ \textbf{marks 的整数结构}✓✓$$
$$\qquad \text{（envelope 钉的是}\ |\hat\mu|^2\ \text{的}\ \textbf{幅值} \text{与}\ S(0);\ \text{它}\ \textbf{不钉相位}）✓✓$$

## §4 ⭐ 新发现的 G3 入口（登记，未审计）：**混合的顶点性**

$$\text{因}\ S\ \text{是}\ \textbf{凸混合}（\text{权重}\ w_c）：\text{任何}\ \textbf{线性} \text{目标在}\ \textbf{顶点}（\text{单一构型}）\text{取到最优}✓✓$$
$$\Longrightarrow \textbf{混合是否本质} \Longleftrightarrow \text{行证书（宽}\ \tau=3\times10^{-40}\ \text{的窄带）}\ \textbf{能否由单一 marked 构型满足}✓✓$$
$$\qquad \text{若混合}\ \textbf{本质} \Longrightarrow p_0=\sum_c w_c p_c\ \text{是}\ \textbf{平均} \Longrightarrow \text{各构型的}\ p\ \text{有的大有的小}✓✓$$
$$\qquad \Longrightarrow ⭐\ \text{这是一个}\ \textbf{跨构型的联合结构}（\text{真正的 G3 型}）,\ \text{且}\ \textbf{不} \text{被}\ S(0)\ \text{支配}✓✓$$
$$\textbf{状态}：\textbf{未审计}（\text{下一刀候选}）;\ \text{审计法}：\text{判定行证书能否被单一构型满足（}\text{可零成本：}\text{若}\ \exists\ \text{单构型}\Longrightarrow \text{混合可去}\Longrightarrow \text{此入口关闭}）✓$$

## §5 判词（按唐先生的规则）

$$\text{若 G3 找不到独立必要条件} \Longrightarrow \textbf{关闭这条 LP 分支}✓$$
$$\text{当前状态}：\text{第一个 G3 候选（Toeplitz PSD）}\ \textbf{已被 K2 判定非独立} \Longrightarrow \text{须继续}\ G_1／G_2／\text{其它}\ G_3✓$$
$$\qquad \text{下一刀候选已命名}（\S4\ \text{的顶点性／混合本质性}）;\ \text{若它也非独立且}\ G_1／G_2\ \text{亦空} \Longrightarrow \textbf{关闭分支}✓$$

## §6 边界与回查

- ⚠️ §1 **逐字**（`LawN256.lean`）；§2 三步为**精确推导 ＋ 本档实测**（`\lambda_{\min}=204.122903`）✓
- ⚠️ §3／§4 为**本档判断与登记**（§4 **未审计**）✓
- ⚠️ **不声称**能找到独立 G3；**不声称**能 pin；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**前沿档案；**未覆盖**其 JSON ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；⚠️ 本档**未出现**结果异常 ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:1x）`[纪律]`（先跑后写）

```
技术词 对角占优判据     命中文件数=0  ⟹ 本档新增
技术词 混合顶点性       命中文件数=0  ⟹ 本档新增
技术词 G3 审计         命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
