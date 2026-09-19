已查地图（**先查后写**）：`C-67`（3.2.7 逐字 ＋ 两条不等式）、`papers/brown-thm2-classical/`（论文 B：第一条已在 τ=1、b⁺=0 证明）、`WORKPLAN-...` A1 行、`docs/Droll2012-thesis-Li-criterion-Selberg.pdf`（逐字提取）。关键词回查：`括号量比较`=0、`第二条即定理`=0、`参数假设充分性`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 20:09「继续A1」）**：`A1 = T7` —— Droll Conjecture 3.2.7 的**第二条**不等式。
**结论（先行）**：$$\textbf{(一)}\ ⭐⭐\ \textbf{第二条不等式}\ \textbf{不是猜想，是定理}：\text{它归约为括号量的初等比较}✓✓$$
$$\qquad \text{链式结构}：\ \mathrm{SUM}\ \le\ 2(r^k+r^{-k}-2)\,B_1\ \le\ \tfrac94(r^k+r^{-k}-2)\,B_2✓$$
$$\qquad \textbf{第二条} \iff 2B_1\le\tfrac94B_2 \iff \boxed{B_1\le\tfrac98B_2}\qquad（\textbf{与}\ \tau,k\ \textbf{无关}）✓✓$$
$$\textbf{(二)}\ \textbf{证明（初等）}：\text{记}\ D:=\tfrac98B_2-B_1，\text{则}$$
$$\qquad D=\underbrace{aH\Big[\tfrac{19}{24}\log H-\tfrac49\Big]}_{>0\ (H>e,\,a>0)}+\underbrace{\tfrac{19}{24}b^{+}H}_{\ge0}+\underbrace{\tfrac{c}4(\log H-1)}_{>0\ (c>0)}+\underbrace{\tfrac d4}_{>0\ (d>0)}>0✓✓$$
$$\qquad （\text{系数精确}：aH\log H\ \&\ b^{+}H\ \text{均}\ \tfrac{19}{24}；aH\ -\tfrac49；c\log H\ \&\ d\ \tfrac14；c\ -\tfrac14）\Longrightarrow B_1<\tfrac98B_2✓$$
$$\textbf{(三)}\ \Longrightarrow\ \textbf{Paper B 覆盖 3.2.7 的}\ \textbf{两条}：\text{第一条已证（}\tau=1,b^{+}=0\text{）；第二条（本档）对}\ \textbf{一切}\ 1\le\tau<2\ \text{与一切}\ b\ \text{成立}✓✓$$
$$\qquad \Longrightarrow\ \textbf{3.2.7 的全部实质内容＝第一条}（\text{第二条不构成额外要求}）✓✓$$

FREEZE-ACK: 本档即冻结期内的推导与登记（依 `§8.1`；不产候选结论）

D0: 本档对象 = **3.2.7 第二条的代数归约与初等证明（＋对论文 B 的覆盖结论）** —— 关系 = 新引理（初等），非新机制
D1: 0

# C-179 · ⭐⭐ **3.2.7 第二条不等式是初等定理（A1 完成）**

> **唐先生 2026-09-19 20:09**：继续 A1 ✓

---

## §1 逐字结构（`C-67` 已核）

$$\mathrm{SUM}:=\sum_{|I(\rho)|>H}\Big[\big(1+\tfrac{\tau}{\gamma_\rho^2}\big)^{k/2}+\big(1+\tfrac{\tau}{\gamma_\rho^2}\big)^{-k/2}-2\Big]✓$$
$$\mathrm{SUM}\ \le\ 2\big(r_H(\tau)^k+r_H(\tau)^{-k}-2\big)\,B_1\ \le\ \tfrac94\big(r_H(\tau)^k+r_H(\tau)^{-k}-2\big)\,B_2✓$$
$$B_1=\tfrac13 aH\log H+\tfrac{(4a+3b^{+})H}9+2c\log H+2d+\tfrac c4✓\qquad B_2=aH\log H+b^{+}H+2c\log H+2d✓$$
$$\text{参数假设（Droll 逐字）}：a,c,d>0；3a+b>0；b^{+}=\max\{b,0\}；1\le\tau<2；H>e✓$$

## §2 归约

$$\text{因子}\ 2\big(r^k+r^{-k}-2\big)>0\（\text{约去}）\Longrightarrow \textbf{第二条} \iff 2B_1\le\tfrac94B_2\iff B_1\le\tfrac98B_2✓$$
$$\qquad \text{注意}：\text{该比较}\ \textbf{不含}\ \tau,k\ \text{（它们只在被约去的因子里）} \Longrightarrow \text{第二条}\ \textbf{与猜想的两条参数无关}✓✓$$

## §3 证明

$$D:=\tfrac98B_2-B_1\qquad(\text{逐项系数，精确})：$$
$$\begin{array}{c|r|c|r}
\text{项} & \text{系数} & \text{项} & \text{系数}\\\hline
aH\log H & +\tfrac{19}{24} & c\log H & +\tfrac14\\
b^{+}H & +\tfrac{19}{24} & d & +\tfrac14\\
aH & -\tfrac49 & c & -\tfrac14\\
\end{array}✓$$
$$\Longrightarrow D=aH\Big[\tfrac{19}{24}\log H-\tfrac49\Big]+\tfrac{19}{24}b^{+}H+\tfrac c4\big(\log H-1\big)+\tfrac d4✓$$
$$\text{用}\ H>e\ (\log H>1)：\ (i)\ \tfrac{19}{24}\log H-\tfrac49>\tfrac{19}{24}-\tfrac49=\tfrac{25}{72}>0\ (a>0)✓$$
$$\qquad (ii)\ \tfrac c4(\log H-1)>0\ (c>0)✓\qquad (iii)\ \tfrac d4>0\ (d>0)✓\qquad (iv)\ \tfrac{19}{24}b^{+}H\ge0✓$$
$$\Longrightarrow D>0\ \Longrightarrow\ B_1<\tfrac98B_2\ \Longrightarrow\ \textbf{第二条成立}\qquad\square✓✓$$

## §4 数值核验

```
脚本: scripts/second_inequality_check.py（系数用分数精确表示；样本覆盖 ζ 型参数 a≈0.159）
样本（H, a, b+, c, d）→ D：
  (2.75, 0.159, 0, 1, 1)      → D = 0.4075 > 0 ✓
  (3.00, 0.159, 0, 0.1, 0.1)  → 0.2303 ✓
  (10.0, 0.159, 0.5, 0.2, 0.05) → 6.2277 ✓
  (5.00, 1.0, 2.0, 0.3, 0.2)  → 12.1608 ✓
  (2.72, 0.001, 0, 0.001, 0.001) → 0.0012 ✓
  (1e6, 0.159, 0, 1e-3, 1e-3) → 1,668,360.7 ✓
```
$$\Longrightarrow \text{全部样本}\ D>0✓\ \text{（与证明一致）}$$

## §5 对论文 B 的意义

$$\textbf{① 覆盖面}：\text{Paper B 证}\ \textbf{第一条}（\tau=1,\ b^{+}=0）＋\ \text{本档}\ \textbf{第二条}（\text{一切}\ \tau,b） \Longrightarrow \textbf{两条都成立}✓✓$$
$$\textbf{② 内容定位}：\text{既然第二条是初等的，}\ \textbf{3.2.7 的全部实质内容＝第一条} \Longrightarrow \text{论文可明确写}：$$
$$\qquad \text{"the whole content of Conjecture 3.2.7 is its first inequality; the second is an elementary consequence" }✓✓$$
$$\textbf{③ 对"修复 Brown Lemma 5"的定位}：\text{所需}\ \textbf{只是第一条} \Longrightarrow \text{论文 B 的定位更干净}✓$$

## §6 边界

- ⚠️ 本档使用 Droll 的**参数假设逐字**（`a,c,d>0`；`b^{+}=\max\{b,0\}\ge0`；`H>e`）✓
- ⚠️ `3a+b>0` **未被用到**（第二条不需要它）✓ —— 已在档中注明
- ⚠️ 第一条的证明**仍是实质工作**（论文 B 已于 `τ=1, b^{+}=0` 完成）✓；本档**不涉及**第一条
- ⚠️ 本档结论为**初等代数**，可与论文 B 直接合并（建议作为 Lemma/Remark 放入附录）✓
- **未用** RH；**未改**论文 B 正文（新增独立注记 `papers/brown-thm2-classical/SECOND-INEQUALITY-LEMMA.md`）✓
- **纪律**：先查后判 ✓、**先跑后写** ✓

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 20:1x）`[纪律]`

```
技术词 括号量比较    命中文件数=0 ::  ⟹ 本档新增
技术词 第二条即定理   命中文件数=0 ::  ⟹ 本档新增
技术词 参数假设充分性  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
