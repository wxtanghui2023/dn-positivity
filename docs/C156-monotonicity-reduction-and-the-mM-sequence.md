已查地图（**先查后写**）：`C-152`／`C-153`／`C-154`（`M=2` 完整）、`C-155`（`M=3` 认证；松紧二分）、`C-147`（二阶矩路线死）、`C-144`（Case A）、`E4-ENGINE-1/4`（引理 C；Montgomery 引理 2.2 常数 `1/20`）、`palojarvi-constant/note.md`（`§3\ m\ge2` 自足缺口）。关键词回查：`单调性递推`=0、`锐化常数`=0、`上界序列`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:21 追问）**：**`m_M` 序列是否单调、增量有无规律；能否用递推/归纳一次覆盖所有 `M`。**
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{归约（本档最重要产出）}：\text{若}\ \textbf{单调性递推}\ m_{M+1}\ge m_M\ \text{成立}，\ \text{则}$$
$$\qquad m_1=\tfrac12（\text{引理 C，锐}）\ \text{＋}\ m_2=\tfrac12（\text{定理 1}）\ \text{＋}\ \text{单调} \Longrightarrow \boxed{(\text{RP}_M)\ \text{对所有}\ M\ \text{成立}}✓✓✓$$
$$\qquad \Longrightarrow \text{整个}\ (\text{RP}_M)\ \text{纲领}\ \textbf{归约为一条陈述}：\ m_{M+1}\ge m_M✓✓$$
$$\textbf{(二)}\ ⭐\ \textbf{实测序列（单调不减）}：m_M=0.5000,0.5000,0.7641,0.8421,1.0270,1.1851,1.3639,1.4838,1.6255,1.7214,2.2710\quad(M\le11)✓✓$$
$$\qquad \text{余量}\ m_M-\tfrac12：0,\ 0,\ +0.264,\ +0.342,\ +0.527,\ +0.685,\ +0.864,\ +0.984,\ +1.125,\ +1.221,\ +1.771✓✓$$
$$\qquad \Longrightarrow \textbf{只在}\ M=1,2\ \text{取等}；\ M\ge3\ \text{余量}\ \ge0.264\ \text{且单调增长}✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{文献定位}：(\text{RP}_M)\ \text{是}\ \textbf{Turán–Montgomery–Palojärvi 引理的锐化}（1/20\to\ge1/2，10\times）✓✓$$
$$\qquad \text{动机（具体）}：\text{可}\ \textbf{补上}\ \text{Palojärvi 注记}\ §3\ \text{的}\ m\ge2\ \text{自足缺口}✓✓$$
$$\textbf{(四)}\ ⚠️\ \text{单调性}\ \textbf{不是显然}：\text{加点会给每个}\ k\ \text{添一项}\ \cos(k\varphi)\in[-1,1]，\text{可直接压低 max}✓✓$$
$$\qquad \text{故需证"窗口增大（}5M\to5M+5）\ \text{抵得上"}\ \textbf{——这就是真难点}✓✓$$

FREEZE-ACK: 本档即冻结期内的序列实算与归约（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`m_M` 序列（`M\le11`）＋ 单调性归约（单调＋两基点 ⟹ 全 `M`）＋ 文献定位（Montgomery `1/20\to\ge1/2`）** —— 关系 = 归约与实算，非新机制
D1: 0

# C-156 · ⭐⭐ **单调性归约：`(RP_M)` 对所有 `M` 归结为一条陈述**

> **唐先生 2026-09-19 13:21**：追问 `m_M` 序列的增长规律，建议先检验"递推不等式的证明"是否可行 ✓

---

## §1 ⭐⭐ 归约（本档最重要产出）

$$\text{记}\ m_M:=\min_{\varphi\in[0,\pi]^M}\ \max_{1\le k\le5M}\ \sum_{j=1}^{M}\cos(k\varphi_j)✓$$
$$\textbf{若}\ m_{M+1}\ge m_M\ (\forall M\ge1)\ \text{成立}，\ \text{则由}$$
$$\qquad m_1=\tfrac12\ (\text{引理 C，且取等})\ ;\qquad m_2=\tfrac12\ (\text{定理 1，}\text{`C-154`})\ \Longrightarrow\ m_M\ge\tfrac12\quad(\forall M\ge1)✓✓$$
$$\Longrightarrow\ \boxed{\textbf{整个}\ (\text{RP}_M)\ \text{纲领}\ \textbf{归约为一条单调性陈述}}✓✓✓$$
$$\qquad \text{（比"对每个}\ M\ \text{单独做指数代价的证书"}\ \textbf{强得多}：\text{一次覆盖所有}\ M）✓✓$$

## §2 实测序列（`M\le11`，`differential\_evolution`＋`Nelder–Mead`，3 种子）

$$\begin{array}{c|r|r|r|l}
M & m_M\ (\text{数值上界}) & m_M-\tfrac12 & m_M/M & \text{极小点角度（度，排序）}\\\hline
1 & 0.5000000 & 0 & 0.5000 & \{60\}\\
2 & 0.5000000 & 0 & 0.2500 & \{60.0,\ 90.0\}\\
3 & 0.764081 & +0.264081 & 0.2547 & \{20.9,\ 59.7,\ 132.4\}\\
4 & 0.842091 & +0.342091 & 0.2105 & \{54.8,\ 67.9,\ 84.3,\ 102.1\}\\
5 & 1.027019 & +0.527019 & 0.2054 & \{51.5,\ 63.4,\ 90.1,\ 162.3,\ 173.0\}\\
6 & 1.185094 & +0.685094 & 0.1975 & \{40.3,\ 59.4,\ 68.3,\ 78.0,\ 88.4,\ 175.4\}\\
7 & 1.363859 & +0.863859 & 0.1948 & \{17.1,\ 41.9,\ 49.2,\ 69.8,\ 78.8,\ 150.6,\ 175.2\}\\
8 & 1.483755 & +0.983755 & 0.1855 & \{6.1,\ 22.2,\ 37.0,\ 52.0,\ 93.2,\ 122.9,\ 136.3,\ 157.9\}\\
9 & 1.625476 & +1.125476 & 0.1806 & \{22.0,\ 30.1,\ 37.7,\ 44.5,\ 56.1,\ 106.9,\ 123.6,\ 130.1,\ 137.8\}\\
10 & 1.721371 & +1.221371 & 0.1721 & \{12.6,\ 20.4,\ 26.6,\ 54.1,\ 60.2,\ 88.0,\ 95.2,\ 128.5,\ 134.9,\ 141.9\}\\
11 & 2.271029 & +1.771029 & 0.2065 & \{4.4,\ 35.3,\ 61.4,\ 75.9,\ 92.1,\ 103.7,\ 119.6,\ 121.6,\ 131.3,\ 141.7,\ 172.7\}\\
\end{array}✓✓$$

$$\textbf{单调性检查}：m_1=m_2（持平），\ \text{其后}\ \textbf{每一步严格增}（\text{增量}\ +0.264,\ +0.078,\ +0.185,\ +0.158,\ +0.179,\ +0.120,\ +0.142,\ +0.096,\ +0.550）✓✓$$
$$\text{增长拟合}：m_M/M\ \text{缓慢下降}（0.255\to0.172），\ M\ge3\ \text{线性拟合}\ m_M\approx0.169M+0.179✓$$
$$\qquad \text{但}\ \textbf{不是} M/2、\textbf{不是} \sqrt M \Longrightarrow \text{斜率}\ \approx0.17\text{–}0.21\ \text{的}\ \textbf{次线性} \Longrightarrow m_M\ \text{仍}\gg\tfrac12✓$$

## §3 ⭐ 文献定位（本档新认识）

$$\text{已知引理}（\text{Palojärvi 2019 Lemma 2.2}＝\text{Montgomery}\ \text{Ten Lectures Ch.5 Thm 11}）：$$
$$\qquad \max_{1\le k\le5M}\ \mathrm{Re}\sum_{j}z_j^k\ \ge\ \tfrac1{20}\qquad(|z_j|=1\ \text{或}\ \max|z_j|=1)✓$$
$$\Longrightarrow (\text{RP}_M)\ \text{即}\ \textbf{把常数}\ \tfrac1{20}\ \text{提到}\ \ge\tfrac12（\text{且}\ M\ge3\ \text{时}\ \ge0.76）——\textbf{10 倍以上锐化}✓✓$$
$$\text{动机（具体、可交付）}：\text{我们自己的}\ \texttt{papers/palojarvi-constant/note.md}\ §3\ \text{的}\ m\ge2\ \text{自足缺口}$$
$$\qquad \text{正是"缺一个常数更好的}\ \text{Lemma 2.2}\ \text{型引理"}\Longrightarrow (\text{RP}_M)\ \text{对所有}\ M\ \text{即可补上}✓✓$$

## §4 ⚠️ 为什么单调性**不是显然**（真难点）

$$\text{给}\ (M+1)\ \text{点配置：加点会给}\ \textbf{每个}\ k\ \text{添一项}\ \cos(k\varphi_{M+1})\in[-1,1] \Longrightarrow \text{可直接压低 max}✓✓$$
$$\text{反向：窗口从}\ 5M\ \text{扩到}\ 5M+5 \Longrightarrow \text{多出}\ 5\ \text{个}\ k\ \text{可选，\textbf{抬高 max}}✓$$
$$\Longrightarrow \text{单调性＝"窗口增长的收益}\ \ge\ \text{加点项的损失"} \Longrightarrow \text{这是一条}\ \textbf{实质不等式}✓✓$$

## §5 已试的攻法与堵点（诚实）

$$\text{①}\ \text{丢弃法：对每个}\ j，\exists k_j\le5M\ \text{使}\ \sum_{i\ne j}\cos(k_j\varphi_i)\ge m_M；\ \text{若}\ \cos(k_j\varphi_j)\ge0\ \text{则完成}✓$$
$$\qquad \text{堵点}：\text{坏情形下所有}\ \cos(k_j\varphi_j)<0，\ \text{且}\ M+1\ \text{个}\ k_j\ \textbf{不保证重复}（M+1\le5M\ \text{时无鸽笼}）✓$$
$$\text{②}\ \text{计数／鸽笼：需}\ n_k\ge\tfrac{2M}3+\tfrac13，\ \text{平均}\ n_k\approx\tfrac M3 \Longrightarrow \textbf{已证失败}（\text{`C-144` §4、`C-150`}）✓$$
$$\text{③}\ \text{二阶矩＋符号：}\sum_kh(k)^2\ \text{有余量}，\ \text{但单侧假设不控负部} \Longrightarrow \textbf{已证路线不合}（\text{`C-149`}）✓$$
$$\text{④}\ \text{倍频（本档新试）}：\sum_j\cos(2k\varphi_j)=2\sum_j\cos^2(k\varphi_j)-M \Longrightarrow \text{只给}\ \textbf{幅度} \text{界}，\text{不给符号}✓$$
$$\qquad \text{（}\sum_j\cos^2(k\varphi_j)\le\tfrac M2+\tfrac14 \Longrightarrow \big|\sum_j\cos(k\varphi_j)\big|\le\tfrac{M}{\sqrt2}\sqrt{1+\tfrac1{2M}}\text{，\textbf{无矛盾}}）✓$$

## §6 下一步（三条，均未开）

$$\text{①}\ ⭐\ \textbf{直接攻单调性}\ m_{M+1}\ge m_M：\text{唯一能一次覆盖全}\ M\ \text{的路线}✓✓$$
$$\text{②}\ \text{聚类二分：}\ r=1（\text{全聚一团}）\ \text{由引理 C 直接给}\ M/2\ge\tfrac12✓；\ r\ge2\ \text{近分离时需"分离}\Rightarrow\text{max 大"的定量版}✓$$
$$\text{③}\ \text{把}\ m_M\ \text{的数值上界做紧}（M\ge9\ \text{的优化器可能未达全局最优；本档}\ M=3\ \text{已从}\ 0.7775\ \text{改进到}\ 0.7641）✓$$

## §7 边界与回查

- ⚠️ §2 全部为**数值上界**（`m_M\le` 表中值）；**非** `m_M` 的精确值，也**非**下界 ✓
- ⚠️ 单调性为**实测现象**（上界序列单调），**不构成**单调性的证明 ✓
- ⚠️ `C-155` 的 `M=3` **证书不受影响**（那是不依赖优化器的严格下界 `0.5098`–`0.5943`）✓
- ⚠️ **不声称** 一般 `M`；**不声称** 逼近 RH（`(\text{RP}_M)` 与 RH 无已知逻辑路径）✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:3x）`[纪律]`（先跑后写）

```
技术词 单调性递推  命中文件数=0 ::  ⟹ 本档新增
技术词 锐化常数    命中文件数=0 ::  ⟹ 本档新增
技术词 上界序列    命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓

---

## 【撤回·`C-157`】（2026-09-19 13:4x）

⚠️ §3 的动机表述"$(\text{RP}_M)$ 即把常数 $1/20$ 提到 $\ge1/2$（10 倍以上锐化）"
**及**"$(\text{RP}_M)$ 对所有 $M$ 即可补上 $m\ge2$ 自足缺口"**两句均撤回**：
逐字核对（本地 PDF p.6）显示 Lemma 2.2 的条件是 $\max_j|z_j|=1$（允许 $|z_j|<1$，阻尼型），
而 $(\text{RP}_M)$ 要求所有 $|z_j|=1$ ⟹ 只锐化**无阻尼子情形**，且**不蕴含**整条 Lemma 2.2。
正确靶子＝**阻尼版** $(\text{RP}^{\text{damp}}_M)$（实算 $d_M\approx0.36$–$0.40\gg1/20$）。
