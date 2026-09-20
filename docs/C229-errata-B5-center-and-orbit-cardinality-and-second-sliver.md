已查地图（**先查后写**）：查 `C-228`（D-C PASS）、`C-227`（B5）、`C-226`（D-B）。回查见 §6 ✓

D0: 本档对象 = **C-228 的两条勘误 ＋ 一处被漏掉的薄片修补**（B5 中心化表述 ✓／轨道基数 ✓／覆盖侧几何 ✓）—— 关系 = 更正与登记
D1: 0
FREEZE-ACK: 本档即冻结期内的更正与登记（依 §8.1；不产候选结论）

---

## §0 ⭐ 处置结论（先列）

$$\boxed{\text{勘误①（B5 中心）}：\textbf{接受}✓✓}\qquad \boxed{\text{勘误②（轨道基数）}：\textbf{不接受}✗\text{（附数值＋群论证据}✓）}\qquad \boxed{\text{薄片}：\text{唐先生漏了另一侧}✗，已修补 ✓✓}$$

## §1 ⭐ 勘误①（接受 ✓✓）：B5 的中心必须是唯一根 $z_*$，不是任意 $x\in X_{\rm ref}$

$$\textbf{正确形式}✓：F(z_*+\delta)\ \ge\ F(z_*)+c_X\|\delta\|-\tfrac R2\|\delta\|^2✓,\qquad 0<\|\delta\|\le\rho_g✓$$
$$\qquad \text{其中}\ c_X,R\ \text{由【参考球】}\ B(c_0,\rho_{\rm data})✓\ \text{上的区间数据统一给出}✓（\rho_{\rm data}=2.05\times10^{-3}\ge\rho_g+{\rm hd}✓）$$
$$\textbf{错误写法}✗（C-227 §2 ⑤ 的表述）：“\text{对 }x\in X_{\rm ref}\ \text{全部成立}\ F(x+\delta)\ge F(x)+\cdots”✗$$
$$\qquad \textbf{为何错}✓：\text{若对每个}\ x\in X_{\rm ref}\ \text{都成立，则}\ X_{\rm ref}\ \text{中每点都是严格局部极小}✗ \Longrightarrow \text{不可能}✓$$
$$\textbf{条件式（唯一可用的中间形式）}✓：F(x+\delta)\ \ge\ \min_{k\in A}S_k(x)+c_X\|\delta\|-\tfrac R2\|\delta\|^2✓,\quad x\in B(c_0,\rho_{\rm data})✓$$
$$\qquad \text{由 B4【唯一根满足六路 tie】} \Longrightarrow \min_{k\in A}S_k(z_*)=F(z_*)✓ \Longrightarrow \text{条件式在}\ z_*\ \text{处【无条件化}】✓✓$$
$$\qquad \textbf{即：常数在整个参考球上统一认证 ✓；增长不等式的中心必须是 }z_*\ \textbf{，不能是任意 }x\ ✗$$

## §2 ⭐ 勘误②（**不接受** ✗）：轨道基数在 $\Omega$ 中是 2，不是 6

$$\textbf{数值核验}✓（6\ \text{个配对置换的}\ F\ \text{值全相等}✓）：$$
```
(0,1,2) r=[1, 0.790513, 0.830207]  F=0.373091892895817
(0,2,1) r=[1, 0.830207, 0.790513]  F=0.373091892895817
(1,0,2) r=[0.790513, 1, 0.830207]  F=0.373091892895817
(1,2,0) r=[0.790513, 0.830207, 1]  F=0.373091892895817
(2,0,1) r=[0.830207, 1, 0.790513]  F=0.373091892895817
(2,1,0) r=[0.830207, 0.790513, 1]  F=0.373091892895817
⟹ 未归一空间：6 点 ✓（唐先生此点正确 ✓）
⟹ 归一到 Ω（r₁=1 置于首位）后【不同点】数 = 2 ✓✓
   (r₂,r₃,φ₂,φ₃) = (0.79051323, 0.83020729, 0.82066π, 0.46172π)
   (r₂,r₃,φ₂,φ₃) = (0.83020729, 0.79051323, 0.46172π, 0.82066π)
```
$$\textbf{群论理由}✓：\text{6 个置换中 4 个把 }r=1\ \text{的点挪到位置 2/3} \Longrightarrow \text{重新归一化（把 }r=1\ \text{放回首位）后与 id 或 }\sigma\ \text{重合}✓$$
$$\qquad \Longrightarrow \text{在坐标卡 }\Omega=[0,1]^2\times[0,\pi]^3\ \text{中，轨道}={z_*,\sigma z_*}✓（2 点 ✓，非 6 ✗）$$
$$\textbf{证否"仅换 }\varphi_j"\text{的另一条}✓：F(\text{仅换}\varphi_1\leftrightarrow\varphi_2)=1.126876598534850\neq F(z_*)=0.373091892895817✗（\text{差}0.7538✗）$$
$$\qquad \Longrightarrow \varphi\ \text{单独置换【不是对称】}✗；\text{正确对称群}=\{\mathrm{id},\sigma\}✓,\ \sigma:(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)\mapsto(r_3,r_2,\varphi_1,\varphi_3,\varphi_2)✓$$
$$\textbf{两个陈述可共存}✓：\arg\min_{\Omega}F=\{z_*,\sigma z_*\}✓\ \text{（}\Omega\ \text{内，2 点}✓）；\text{未归一构型空间的} S_3\text{-轨道}=6\ \text{点}✓$$
$$\qquad \text{因 }C_3\ \text{的定义域是 }\Omega\ \text{（登记定义}✓） \Longrightarrow \textbf{登记口径用 2 点}✓$$

## §3 ⭐ 薄片：唐先生第 4 条只覆盖了一侧 ✗

$$\text{旧 run 的丢弃判据}✗：\text{"远角距离}\le\rho_g\text{"} \Longrightarrow \text{被丢箱}\subseteq B(c_0,\rho_g)✗$$
$$\text{覆盖所需}✓：\text{被丢箱}\subseteq B(z_*,\rho_g)✓ \Longrightarrow \text{必须}\ \mathrm{far}(X,c_0)+{\rm hd}(X_0)\le\rho_g✓$$
$$\text{若 }{\rm hd}(X_0)>0\ \text{则 }B(c_0,\rho_g)\not\subseteq B(z_*,\rho_g)\ ✗ \Longrightarrow \text{另一侧薄片}\ B(c_0,\rho_g)\setminus B(z_*,\rho_g)✗\ \text{既未被 C1 认证、也不在 }B(z_*,\rho_g)\ \text{内}✗✓$$
$$\qquad \text{（唐先生第 4 条只讨论了 }B(z_*,\rho)\setminus B(c_0,\rho)✓\ \text{这一侧}✓，\text{漏了对称的另一侧}✗）$$
$$\textbf{修补}✓✓（两步）：$$
$$\qquad \textbf{(i) 取极紧 }X_0✓：\text{D-B 用 }r_0=10^{-12}\ \text{重跑}✓ \Longrightarrow \text{箱宽}\sim4\times10^{-22}✓ \Longrightarrow {\rm hd}(X_0)\le10^{-21}✓ \Longrightarrow \text{薄片}\sim10^{-21}✓（\text{实质为零但非零}✓）$$
$$\qquad \textbf{(ii) 同时收紧判据＋压低 }T_C✓：\text{丢弃半径}\ \rho_g-10^{-9}✓；T_C=\sup F(X_0)+10^{-9}=F(z_*)+10^{-9}✓（\text{旧值}+2.6\times10^{-6}✓）$$
$$\qquad \textbf{推论}✓：\text{因 }T_C^{\rm new}<T_C^{\rm old}✓，\text{旧的认证箱【仍全部有效}】✓（F\ge T_C^{\rm old}>T_C^{\rm new}✓） \Longrightarrow \textbf{无需重跑认证侧}✓$$

## §4 C2 修补结果（float 层 ✓）

```
F(z*)          = 0.373091892895817
T_C（新）      = 0.373091893895817      （T_C − F(z*) = 1.0e-9 ✓）
丢弃半径        = ρ_g − 1e-9 = 0.0019782234
评估 472,766   认证 252,282   丢弃 485   分裂 219,999   未决 0 ✓✓
认证最小余量    = 4.628931e-08 ✓
丢弃箱最远角 max = 0.001978039980  ≤ DISC_R ✓✓  ⟹ 每个被丢箱 ⊆ B(z*, ρ_g) ✓✓
```
$$\Longrightarrow \text{覆盖侧漏洞已闭}✓：\Omega=\mathcal C_{\rm cert}\cup\bigcup_{\sigma}B(\sigma z_*,\rho_g)✓,\ \text{两级各有证书}✓$$
$$\qquad \text{区间层复核（C2 严格版）正在后台运行}✓\（\text{脚本}\ \texttt{scripts/dC2iv\_strict.py}✓）$$

## §5 修正后主定理的书写（待区间层通过后采用 ✓）

$$\boxed{\Omega=\underbrace{\mathcal C_{\rm cert}}_{\text{C1/C2：}F\ge T_C}\ \cup\ \underbrace{\bigcup_{\sigma}B_{\sigma}(\rho_g)}_{\text{B5：中心 }z_*}}✓,\qquad T_C=F(z_*)+10^{-9}✓$$
$$\textbf{① }x\in\mathcal C_{\rm cert} \Longrightarrow F(x)\ge T_C>F(z_*)✓$$
$$\textbf{② }0<\|x-z_*\|\le\rho_g \Longrightarrow F(x)\ge F(z_*)+c_X\|x-z_*\|-\tfrac R2\|x-z_*\|^2>F(z_*)✓$$
$$\Longrightarrow \boxed{\arg\min_{\Omega}F=\{z_*,\sigma z_*\}✓✓},\qquad C_3=F(z_*)=0.373091892895816\ldots✓$$

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 中心化勘误     命中文件数=1  ::  ./C229-errata-B5-center-and-orbit-cardinality-and-second-sliver.md
技术词 覆盖侧薄片     命中文件数=1  ::  ./C229-errata-B5-center-and-orbit-cardinality-and-second-sliver.md
技术词 归一化塌缩     命中文件数=1  ::  ./C229-errata-B5-center-and-orbit-cardinality-and-second-sliver.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §7 本档自我失误（第 43 次）

$$\textbf{43a 丢弃判据的两球心聚合写错}✗✗：\text{把"远角距离"写成对两球心取 }\max✗ \Longrightarrow \text{要求箱同时在两球交集内}✗ \Longrightarrow \text{首跑"丢弃 0、未决 378"}✗$$
$$\qquad \text{已改为【取 }\min\text{（在任一个球内即可）}】✓ \Longrightarrow \text{丢弃 485、未决 0}✓✓$$
$$\textbf{教训}：\text{"在某个球内"是析取}✓，\text{聚合子必须是 }\min✗\ \text{不是 }\max✗✓$$
$$\textbf{43b D-B 脚本标签未随计算同步}✗（sed 改了计算用 best[-1]，但打印仍写 best[0]✗） \Longrightarrow \text{日志形如"采纳 r0=1e-4"而实际是 }10^{-12}✗；\text{已在本档显式更正}✓$$

## §8 边界

$$\textbf{① 勘误①接受}✓：\text{表述改正}✓，\text{数值（}c_X=0.0988,R=99.90,\rho_g=1.9782244\times10^{-3}\text{）不变}✓$$
$$\textbf{② 勘误②不接受}✗：\text{已给出数值＋群论证据}✓（\Omega\ \text{内 2 点}✓）；\text{若唐先生要求以【未归一构型空间】为口径，则应为 6 点}✓——\text{两种陈述各自正确，只是空间不同}✓$$
$$\textbf{③ 覆盖侧}：\text{float 层已闭}✓；\text{区间层后台运行}✓；\text{未决=0 才算 PASS}✓$$
$$\textbf{④ 未用 RH}✓；\text{未改他档}✓（\text{本档为勘误，原 C-227/C-228 保留}✓）$$
