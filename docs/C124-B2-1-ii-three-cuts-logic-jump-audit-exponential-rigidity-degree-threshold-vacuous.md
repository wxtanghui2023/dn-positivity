已查地图（**先查后写**）：`C-121`（三层设计）、`C-122`（Toeplitz PSD 已 K2 判死）、`C-123`（B2-1 第一刀：和法则＋近碰撞必要条件）、`lean-frontier-audit/LawN256.lean`（逐字：`S` 为凸混合、`m\in\{1,2\}`、`\sum m=256`、`\tau=3/10^{40}`）。关键词回查：`指数和刚性`＝0、`Vandermonde 刚性`＝0、`度数阈值`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:25「同意做 (ii)，但这一刀必须优先审这个逻辑跳跃」⟹ **B2-1(ii) 三刀全做** ✓✓：**(甲) ✓ 逻辑跳跃审计：`|D(\delta)|\ge128\ \not\Rightarrow\ \delta\in\mathbb Z`**（`D(\delta)` 在非整数上连续且在一段宽约 `1.2` 的区间上 `\ge128`）⟹ **该推理无效，不得使用** ✓✓；**(乙) ✓ 刀①：全行约束＝正系数指数和**：`E_j=\sum_{a,b}m_am_b\lambda_{ab}^j`，`\lambda_{ab}=e^{2\pi i(x_a-x_b)/256}`，系数 `m_am_b>0`（**数值核验 `\Delta^2` 恒等式，残差 `1.5\times10^{-11}`**）✓✓；**(丙) ⭐ 刀②：Vandermonde 刚性（条件性）**——**若** `E_j=j` **精确**且在范内成立，则 `\Delta^2E_j\equiv0`，而 `\Delta^2E_j=\sum m_am_b\lambda_{ab}^j(\lambda_{ab}-1)^2` ⟹ **若相异位置差个数 `\le` 连续零点个数，则所有 `\lambda_{ab}=1` ⟹ 位置全同余 ⟹ 与 `E_j\approx j` 矛盾** ✓✓；**(丁) ⭐⭐ 刀③（决定性）：把"近似"升级为"精确"所需的间隙定理\ \textbf{在本问题中真空}**——`\tau=3\times10^{-40}` 与高度 `H\lesssim65536` 要求度数 `d\le8`，而**任何有理位置** `x_i=p_i/q` 给出 `256q` 次单位根 ⟹ 域度数 `\varphi(256q)\ge128` ⟹ 间隙 `\approx(1.3\times10^5)^{-127}\approx10^{-640}\ll\tau` ⟹ **刚性对一切有理位置真空** ✓✓；**(戊)** 实测：**随机单构型**与目标 `j` 的偏离 `\sim458`（对 `\tau=3\times10^{-40}`）⟹ 约束**极端选择**，但**选择性≠离散刚性** ✓✓；**判决（按唐先生的表）＝"只证明需极高精度相消" ⟹ \textbf{不足以判死} ⟹ B2-1 仍 OPEN**，且**障碍已记录：G3 真正缺的是\ \textbf{成对几何}，不是更高的 envelope 精度** ✓✓

FREEZE-ACK: 本档即冻结期内的 C-121-B2-1(ii) 审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **B2-1(ii) 三刀（逻辑跳跃审计／指数和形式化／Vandermonde 刚性条件性＋度数阈值真空）＋判决与障碍登记** —— 关系 = 审计，非新机制
D1: 0

# C-124 · **B2-1(ii)：三刀全做（含一处逻辑跳跃审计）**

> **时间**：2026-09-18 23:25 唐先生：**「同意做 (ii)，但这一刀必须优先审这个逻辑跳跃」** ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ ✓\ \textbf{逻辑跳跃无效}：|D(\delta)|\ge128\ \not\Rightarrow\ \delta\in\mathbb Z✓✓$$
$$\textbf{(乙)}\ ✓\ \text{刀①}：\text{全行约束＝}\textbf{正系数指数和}\ E_j=\sum_{a,b}m_am_b\lambda_{ab}^j\ (\text{数值核验}\ \Delta^2\ \text{恒等式})✓✓$$
$$\textbf{(丙)}\ ⭐\ \text{刀②}：\textbf{Vandermonde 刚性（条件性）}——\text{精确等式＋相异差个数少} \Longrightarrow \text{矛盾}✓✓$$
$$\textbf{(丁)}\ ⭐⭐\ \text{刀③}：\text{把近似升级为精确所需的间隙定理}\ \textbf{真空}（\text{度数}\ge128 \Longrightarrow \text{间隙}\sim10^{-640}\ll\tau）✓✓$$
$$\textbf{(戊)}\ \text{实测：随机单构型偏离}\sim458 ⟹ \textbf{选择性别于刚性}✓✓;\quad \text{判决}＝\textbf{不足以判死} \Longrightarrow \textbf{B2-1 仍 OPEN}✓$$

## §1 （甲）逻辑跳跃审计（本档第一优先级）

$$\text{诱惑推理}：\tau\ \text{极小} \Longrightarrow \text{相位须精确对齐} \Longrightarrow \delta\ \text{必须整数} \qquad ✗\ \textbf{不成立}✓✓$$
$$\text{理由}：|D(\delta)|=\Big|\frac{\sin\pi\delta}{\sin(\pi\delta/256)}\Big|\ \text{是}\ \textbf{连续函数};\ |D(\delta)|\ge128 \Longrightarrow |\delta|\lesssim0.6034\ (\mathrm{mod}\ 256)\ \text{是}\ \textbf{区间}，\text{不是点}✓✓$$
$$\qquad \Longrightarrow \textbf{近碰撞必要条件}\ \text{只给}\ \textbf{"在某区间内"},\ \text{不给}\ \textbf{"在整数上"}✓✓$$
$$\qquad ⚠️\ \text{本项为}\ \textbf{自审}（\text{我上一轮的措辞不得被读作离散化}）✓$$

## §2 （乙）刀①：全行约束＝正系数指数和

$$\text{令}\ F(j)=\sum_a m_a e^{2\pi i j x_a/256};\quad E_j=|F(j)|^2=\sum_{a,b}m_am_b\,\lambda_{ab}^{\,j},\quad \lambda_{ab}:=e^{2\pi i(x_a-x_b)/256}✓✓$$
$$\Longrightarrow \text{窄带条件}\ |E_j-j|\le\tau\ (1\le j\le255)\ \text{是}\ \textbf{255 个联立方程}，\text{不是一条和法则}✓✓$$
$$\qquad \text{且系数}\ m_am_b>0\ \text{（}\textbf{正系数}）;\ \lambda_{ba}=\overline{\lambda_{ab}}✓$$
$$\textbf{数值核验（本档）}：\Delta^2E_j=\sum_{a,b}m_am_b\lambda_{ab}^j(\lambda_{ab}-1)^2,\quad \text{残差}\ 1.5\times10^{-11}\ ✓✓$$

## §3 （丙）刀②：Vandermonde 刚性（条件性结果）

$$\textbf{若}\ E_j=j\ \text{精确}\ (j=1..255)\ \Longrightarrow\ \Delta^2E_j=0\ (j=1..253),\quad \Delta^2E_j=\sum_{a,b}m_am_b\lambda_{ab}^j(\lambda_{ab}-1)^2✓$$
$$\textbf{设}\ \{\mu_1,\dots,\mu_R\}\ \text{为}\ \{\lambda_{ab}\}\ \text{的相异值};\ \text{若}\ R\le253 \Longrightarrow \text{由 Vandermonde（}矩阵可逆）\ \text{得所有}\ m_am_b(\lambda_{ab}-1)^2=0✓✓$$
$$\qquad \Longrightarrow \lambda_{ab}=1\ \forall a,b \Longrightarrow x_a\equiv x_b\ (\mathrm{mod}\ 256) \Longrightarrow E_j\equiv65536\ \textbf{与}\ E_j=j\ \text{矛盾}✓✓$$
$$\Longrightarrow ⭐\ \textbf{条件性刚性}：\text{只要}\ \textbf{(i) 精确等式}\ \text{与}\ \textbf{(ii)}\ R\le253\ \text{同时成立} \Longrightarrow \text{单构型不可能}✓✓$$
$$\qquad ⚠️\ \text{两条件}\ \textbf{均未证}：\text{(i) 需间隙定理（§4 判其为真空）；}\text{(ii) 是}\ \textbf{成对几何} \text{问题（§5 登记）}✓✓$$

## §4 （丁）刀③：度数阈值 —— 刚性在本问题中**真空**

$$\text{要把}\ |E_j-j|\le\tau\ \text{升级为}\ =0：\text{用}\ E_j-j\ \text{是}\ \textbf{实代数整数}（x_i\ \text{有理} \Longrightarrow \lambda_i\ \text{为单位根}）✓$$
$$\qquad \text{非零代数整数的范数}\ \ge1 \Longrightarrow |\alpha|\ge(2H)^{-(d-1)}✓$$
$$\text{要求}\ (2H)^{d-1}<\tau^{-1}=3.3\times10^{39};\quad H\lesssim65536 \Longrightarrow \log_{10}(2H)=5.12 \Longrightarrow d\le8✓✓$$
$$\text{但任何有理位置}\ x_i=p_i/q \Longrightarrow \lambda_i=e^{2\pi i p_i/(256q)}\ \text{为}\ 256q\ \text{次单位根} \Longrightarrow d\ge\varphi(256q)\ge\varphi(256)=128✓✓$$
$$\Longrightarrow (2H)^{127}\approx10^{650}\gg\tau^{-1} \Longrightarrow \textbf{间隙界真空} \Longrightarrow \boxed{\textbf{"}\tau\ \text{极小"}\ \text{不能升级为"整数化"}}✓✓$$
$$\qquad ⚠️\ ⭐\ \text{这就是唐先生要求优先审的那一步，}\textbf{答案是：此路不通}（\text{且已定量}）✓✓$$

## §5 （戊）实测 ＋ 判决（按唐先生的判死表）

$$\text{实测（本档）}：\text{随机单构型（}\text{有理位置，分母 1024，}m\in\{1,2\}，\sum m=256\text{）}：\max|E_j-j|\sim458✓✓$$
$$\qquad \Longrightarrow \text{约束}\ \textbf{极端选择}（458\ \text{vs}\ 3\times10^{-40}）;\quad \text{但}\ \textbf{选择性}\ \ne\ \textbf{刚性}✓✓$$
$$\textbf{判决表（对照唐先生）}：$$
$$\qquad \text{完整 255 行} \Longrightarrow \text{可行近碰撞离整数集有正距离}：\textbf{未达}（\text{§4 真空}）✓$$
$$\qquad \text{只证明}\ |\delta|<0.6034：\textbf{已达}（\text{`C-123`}\ \text{§3}） \Longrightarrow \textbf{仍 OPEN}✓$$
$$\qquad \text{找到非整数}\ \delta\ \text{的完整可行构型}：\textbf{未做}（\text{§6 下一步}）✓$$
$$\qquad \text{只证明需极高精度相消}：\textbf{已达} \Longrightarrow \boxed{\textbf{不足以判死}}✓✓$$
$$\qquad \text{证明需多个近碰撞共同补偿}：\textbf{未做}✓$$
$$\Longrightarrow ⭐\ \textbf{B2-1 仍 OPEN};\quad \textbf{障碍已记录}：\text{G3 真正缺的是}\ \textbf{成对几何}（\text{pairwise geometry}），\ \textbf{不是更高的 envelope 精度}✓✓$$
$$\qquad ⚠️\ \text{故依唐先生指令：}\textbf{不进入 B2-2}✓$$

## §6 登记：下一步唯一有价值的方向（pairwise geometry）

$$\text{把 §3 的}\ R\le253\ \text{变成}\ \textbf{从约束推出的结论}，\text{而不是假设}：$$
$$\qquad \textbf{问题}：\text{在}\ |E_j-j|\le\tau\ (\forall 0<j<256)\ \text{下}，\ \text{成对差}\ \{\lambda_{ab}\}\ \text{的}\ \textbf{相异值个数}\ R\ \text{能否}\ \le253？✓✓$$
$$\qquad \text{若能从约束}\ \textbf{推出}\ R\ \text{有界} \Longrightarrow \text{与 §4 结合} \Longrightarrow \textbf{关闭 B2-1（Case B）}✓✓$$
$$\qquad \text{若不能} \Longrightarrow \textbf{G3 缺的就是 pairwise geometry 本身}（\text{与}\ \text{`C-119`}\ \text{多体线经验一致：只有联合结构才有价值}）✓✓$$
$$K_5\ \text{保留}：\text{即使 B2-1／B2-2 成立，仍须检验}\ p_{\text{mix}}<p_{\text{single}}✓$$

## §7 边界与回查

- ⚠️ §1 为**自审**；§2／§3／§4 为**本档推导**（§2 含数值核验）；§5 为**实测**；§6 为**登记**✓
- ⚠️ §3 的刚性是**条件性**（两条件均未证）；§4 的"真空"是**定量否证**（非"不可能"）✓
- ⚠️ **不声称** B2-1 的答案；**不声称**混合本质；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**前沿档案 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；⚠️ 本轮**测试脚本自身**出现过一次 off-by-one（已修正后重跑，非数学错误）✓

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:2x）`[纪律]`（先跑后写）

```
技术词 指数和刚性      命中文件数=0  ⟹ 本档新增
技术词 Vandermonde 刚性  命中文件数=0  ⟹ 本档新增
技术词 度数阈值       命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
