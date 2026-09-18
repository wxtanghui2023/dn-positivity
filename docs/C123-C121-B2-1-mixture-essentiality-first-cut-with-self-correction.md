已查地图（**先查后写**）：`C-121`（三层设计与第一行硬检查）、`C-122`（Toeplitz PSD 已 K2-repackaging）、`IMPL-3`、`lean-frontier-audit/LawN256.lean`（**逐字：S 为凸混合**）。关键词回查：`混合本质性`＝0、`近碰撞必要条`＝0、`和法则`＝0 ⟹ 均本档新增 ✓。**结论**：⭐ 唐先生 23:21「开。这个候选值得做」⟹ 执行 **C-121-B2-1**，**先撤回我自己第一版错误论证** ✓✓：**(甲) ⚠️ 撤回**——`\sum_{j=0}^{255}E_j=256\sum_a m_a^2` 型**整数性论证只在"位置差为整数"时成立**；一般位置差下交叉项＝**Dirichlet 核值** `D(\delta)=e^{i\pi\delta(1-1/256)}\sin(\pi\delta)/\sin(\pi\delta/256)\ne0` ⟹ 该论证**无效**（本会话**第 6 次同类自纠**）✓✓；**(乙) ✓ 有效结果（精确和法则）**：`\sum_{j=0}^{255}E_j=256\sum_a m_a^2+\sum_{a\ne b}m_am_bD(x_a-x_b)`，而行证书强制 `\sum_{j=0}^{255}E_j=98176+O(\tau)` ⟹ 交叉项 `=512(63.75-n_2)` ⟹ **`|\text{交叉项}|\ge128`** ✓✓；**(丙) ⭐ 由此得 G2 型必要条件**：任何**单一构型**实现必须含**近碰撞对**（位置差 `\lesssim0.6034\ (\mathrm{mod}\ 256)`）✓✓；**(丁)** 同时**干净复现**前沿的"整数位置不可能"（此时交叉项仅 `\delta\equiv0` 存活 ⟹ `\sum=256\sum_{\text{类}}M^2\equiv0\ (\mathrm{mod}\ 256)`，而 `98176\equiv128` ⟹ 矛盾）✓✓；**(戊) B2-1 判决＝未决（OPEN）**：未被杀、也未关闭，但已缩小为一个**带必要条件**的问题 ✓

FREEZE-ACK: 本档即冻结期内的 C-121-B2 审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **B2-1 的撤回＋精确和法则＋近碰撞必要条件（G2 型）＋整数位置不可能的干净复现** —— 关系 = 审计与必要条件提取，非新机制
D1: 0

# C-123 · **C-121-B2-1：混合本质性第一刀（含一处自纠）**

> **时间**：2026-09-18 23:21 唐先生：**「开。这个候选值得做」** ✓

---

## §0 结论（先行）

$$\textbf{(甲)}\ ⚠️\ \textbf{撤回}：\text{我第一版的"整数性矛盾"论证}\ \textbf{无效}（\text{交叉项在一般位置差下不为零}）✓✓$$
$$\textbf{(乙)}\ ✓\ \textbf{精确和法则}：\sum_{j=0}^{255}E_j=256\sum_a m_a^2+\sum_{a\ne b}m_am_b\,D(x_a-x_b);\quad \text{证书强制其}=98176+O(\tau)✓✓$$
$$\textbf{(丙)}\ ⭐\ \text{必要条件（G2 型）}：\text{单一构型必须含}\ \textbf{近碰撞对}（|\delta|\lesssim0.6034\ \mathrm{mod}\ 256）✓✓$$
$$\textbf{(丁)}\ \text{干净复现前沿的"整数位置不可能"}✓✓;\quad \textbf{(戊)}\ B2\text{-}1＝\textbf{OPEN}（\text{未被杀、未关闭}）✓$$

---

## §1 记号与逐字基础

$$\text{单一构型}：E_j:=\Big|\sum_i m_i e^{2\pi i j x_i/256}\Big|^2,\quad m_i\in\{1,2\},\ \sum_i m_i=256,\ x_i\in[0,256)\ \text{有理}✓$$
$$\text{窄带行证书（逐字）}：\big|256\,S(j)-j\big|\le\tau=\tfrac{3}{10^{40}}\ (0<j<256) \Longrightarrow \big|E_j-j\big|\le\tau\ (0<j<256)✓$$
$$\qquad ⚠️\ S(j)=\tfrac1{256}\sum_c w_cE^{(c)}_j \Longrightarrow \text{混合情形为}\ \textbf{凸组合};\ \text{本档先问}\ \textbf{单一构型}✓$$

## §2 ⚠️ 撤回：何处出错（本会话第 6 次同类自纠）

$$\textbf{我第一版写法}：\sum_{j=0}^{255}E_j=\sum_{a,b}m_am_b\sum_{j=0}^{255}e^{2\pi i j(x_a-x_b)/256}\overset{?}{=}256\sum_a m_a^2✓$$
$$\qquad ⚠️\ \text{该等号}\ \textbf{只在}\ x_a-x_b\in\mathbb Z\ \text{时成立}（\text{内层为完整几何和}）✗$$
$$\textbf{一般情形（正确）}：\sum_{j=0}^{255}e^{2\pi i j\delta/256}=D(\delta)\ \text{＝Dirichlet 核}：\quad D(\delta)=e^{i\pi\delta(1-1/256)}\frac{\sin\pi\delta}{\sin(\pi\delta/256)}\neq0\ (\delta\not\equiv0)✓✓$$
$$\qquad \Longrightarrow \text{交叉项}\ \textbf{不消失} \Longrightarrow \text{整数性论证}\ \textbf{无效} \Longrightarrow \boxed{\textbf{撤回}}✓✓$$
$$\qquad ⚠️\ \text{教训（与历史 11 次同族）}：\text{"内层和＝0 或 N"}\ \text{是}\ \textbf{整数差} \text{的特权};\ \text{非整数差下它是有界非零的核值}✓✓$$

## §3 ✓ 有效结果：精确和法则 ＋ 必要条件

$$\text{由 } E_0=|\sum_i m_i|^2=256^2=65536\ \text{（精确）与}\ \sum_{j=1}^{255}j=32640：$$
$$\text{证书强制}\quad \sum_{j=0}^{255}E_j=65536+32640+O(255\tau)=98176+O(10^{-37})✓✓$$
$$\text{另一方面}\quad \sum_{j=0}^{255}E_j=256\sum_a m_a^2+\underbrace{\sum_{a\ne b}m_am_bD(x_a-x_b)}_{=:\,\mathrm{X}}✓$$
$$\text{而}\quad \sum_a m_a^2=256+2n_2\ (n_2:=\#\{i:m_i=2\}\in\mathbb Z_{\ge0}) \Longrightarrow 256\sum_a m_a^2=65536+512n_2✓$$
$$\Longrightarrow \mathrm{X}=98176-65536-512n_2=512(63.75-n_2)\quad \Longrightarrow \quad \boxed{\ |\mathrm{X}|\ge128\ }✓✓$$
$$\qquad （\text{因}\ n_2\in\mathbb Z \Longrightarrow 63.75-n_2\ \text{是}\ \tfrac14 \text{的奇数倍} \Longrightarrow |63.75-n_2|\ge0.25）✓✓$$
$$\Longrightarrow ⭐\ \textbf{G2 型必要条件}：\text{单一构型实现}\ \textbf{必须} \text{让交叉项达}\ \ge128 \Longrightarrow \text{须有}\ \textbf{近碰撞对}✓✓$$
$$\qquad \text{因}\ |D(\delta)|\ge128 \Longrightarrow |\sin(\pi\delta/256)|\le\tfrac1{128} \Longrightarrow |\delta|\lesssim0.6034\ (\mathrm{mod}\ 256)✓✓$$

## §4 ✓ 顺带：干净复现"整数位置不可能"

$$\text{若所有}\ x_i\in\mathbb Z：\ D(\delta)=256\cdot\mathbf 1[\delta\equiv0] \Longrightarrow \sum_{j=0}^{255}E_j=256\sum_{\text{碰撞类}}M_{\text{类}}^2\equiv0\ (\bmod\ 256)✓✓$$
$$\qquad \text{而证书给}\ 98176\equiv128\ (\bmod\ 256)\ \text{且}\ \tau=3\times10^{-40}\ \textbf{远不足以} \text{跨越 128}✓✓$$
$$\Longrightarrow \textbf{整数位置构型不可能}（\text{本档给出更干净的和法则证明；}\text{与前沿"若整数位置则}\ S(256)=256"\ \text{的论证同向}）✓✓$$

## §5 B2-1 判决与下一步

$$\boxed{\ B2\text{-}1＝\textbf{OPEN}\ }：\text{未找到单一构型（未杀）};\ \text{也未证明不存在（未关闭）}✓$$
$$\text{已缩小为}：\text{"能否找到含}\ \textbf{近碰撞对} \text{且}\ |E_j-j|\le\tau\ (\forall 0<j<256)\ \text{的单一构型？"}✓✓$$
$$\textbf{可零成本推进的两条}：$$
$$\qquad \text{(i)}\ \text{数值搜索}：\min_{\text{单构型}}\max_{0<j<256}|E_j-j|\ \text{（非凸；可先试结构化族：幂律位置／}\text{GUE 采样式位置}）✓$$
$$\qquad \text{(ii)}\ ⭐\ \text{把}\ §3\ \text{的必要条件加强}：\text{若近碰撞对}\ \textbf{强制} \text{位置差}\ \textbf{有理整数化} \Longrightarrow \text{回到}\ §4\ \text{矛盾} \Longrightarrow \textbf{关闭 B2-1（Case B）}✓✓$$

## §6 预注册（唐先生的三层 ＋ K5）

$$\text{B2-1}：\text{单一构型能否满足窄带 envelope}？\ \text{能}\to\textbf{KILL}✓$$
$$\text{B2-2}：\text{若不能，能否}\ \textbf{严格证明} \text{混合可行？}\ \text{不能}\to\textbf{KILL}✓$$
$$\text{B2-3}：\text{不可约混合是否}\ \textbf{改变 primal}\ p？\ \text{不改变}\to\textbf{G3 关闭}✓$$
$$K_5：\textbf{"混合不可去"}\ \neq\ \textbf{"混合对}\ p\ \text{有决定性作用"}✓✓$$
$$\qquad ⚠️\ \text{故即使 B2-1／B2-2 成立，}\ \textbf{仍须} \text{检验}\ p_{\text{mix}}<p_{\text{single}}\ \text{是否成立，否则只是表示论上的非退化}✓✓$$
$$\text{并保留}：\textbf{Toeplitz PSD 已正式 K2-repackaging，不再回来}✓$$

## §7 边界与回查

- ⚠️ §2 为**本档自纠**（**本会话第 6 次同类**）；§3／§4 为**本档精确推导**（含 $|\mathrm X|\ge128$）✓
- ⚠️ §5 为**登记**（未执行搜索）✓；§6 中 B2-1/2/3 与 K5 为**唐先生逐字**✓
- ⚠️ **不声称** B2-1 的答案；**不声称**混合本质；**不声称**与 RH 相关 ✓
- **未用** RH；**未改**前沿档案 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）；⚠️ 自纠**先于**落档（未把错误论证写成结论）✓

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-18 23:2x）`[纪律]`（先跑后写）

```
技术词 混合本质性       命中文件数=0  ⟹ 本档新增
技术词 近碰撞必要条     命中文件数=0  ⟹ 本档新增
技术词 和法则        命中文件数=0  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
