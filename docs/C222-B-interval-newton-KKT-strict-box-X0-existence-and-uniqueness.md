已查地图（**先查后写**）：查 `C-221`（A：局部刚性区间工具）、`C-220`（闭合审计，缺三件）、`C-212`（KKT 高精度解）、`C-210`（E1 勘误：$\delta_A$ 项）。回查见 §7 ✓

D0: 本档对象 = **B：KKT 系统的严格 interval-Newton 盒** $X_0$（存在性 ＋ 唯一性分列）—— 关系 = 消掉 $\delta_A$ 内核缺口，使引理 A 无条件化
D1: 0
FREEZE-ACK: 本档即冻结期内的收束与登记（依 §8.1；不产候选结论）

---

## §0 范围（唐先生 2026-09-20 13:39 卡定）

$$\textbf{只做 B}：\text{对 KKT 系统建立严格盒}\ X_0✓；\textbf{不碰} \text{盒外 B\&B}（\text{属 C}）✗；\textbf{不扩大战线}✓$$

## §1 自由度一致性（唐先生特别点出，必须写死）

$$\text{若把}\ \sum\lambda_k=1\ \text{当独立方程} \Longrightarrow 7\ \text{条方程}✗（\text{与"6 方程"歧义}✗）$$
$$\textbf{本档选择}✓✓：\text{取【7 方程 / 7 未知量】，\textbf{不做"消去某个}\ \lambda\ \text{"的不对称选择}}✓$$
$$z=(\varphi_1,\varphi_2,\varphi_3,\lambda_1,\lambda_2,\lambda_3,\lambda_4)\in\mathbb R^7,\qquad A=\{1,5,11,13\}$$
$$G(z)=\Big(\underbrace{\textstyle\sum_{k\in A}\lambda_k\nabla S_k(\varphi)}_{3},\ \underbrace{S_1-S_5,\ S_1-S_{11},\ S_1-S_{13}}_{3},\ \underbrace{\textstyle\sum_{k\in A}\lambda_k-1}_{1}\Big)\in\mathbb R^7$$
$$\textbf{优点}：\text{对称}✓、\text{无任意消元}✓、\text{归一化显式}✓、\text{Jacobian 块结构清晰}✓$$

## §2 算子与区间算术（自建，避开 \texttt{mpmath.iv} 摩擦）

$$\textbf{区间类}\ \texttt{Iv}✓：\text{mpf 端点 ＋ 每次运算外扩}\ \mathrm{SLK}=10^{-100}✓（\mathrm{dps}=120✓）；\cos/\sin\ \text{用【精确值域】}✓（\text{同}\ C-221✓，临界点判定✓）$$
$$\textbf{KKT Jacobian 块结构}✓：J=\begin{pmatrix} D(\varphi,\lambda)_{3\times3} & G_d(\varphi)_{3\times4}\\ T'(\varphi)_{3\times3} & 0\\ 0_{1\times3} & \mathbf 1_{1\times4}\end{pmatrix}$$
$$\qquad D=\mathrm{diag}\big(\!-\!\textstyle\sum_k\lambda_k k^2\cos(k\varphi_j)\big)✓（\text{因}\ \partial^2S_k/\partial\varphi_i\partial\varphi_j=0\ (i\ne j)✓）;\quad T'_{rj}=\partial(S_1-S_k)/\partial\varphi_j=-\sin\varphi_j+k\sin(k\varphi_j)✓$$
$$\textbf{数值基点}✓：120\ \mathrm{dps}\ \text{Newton 精修} \Longrightarrow \text{残差}\ \max|G|=1.45\times10^{-120}✓✓；\ \varphi/\pi=(0.11584425719970138111,\ 0.33188742342310058638,\ 0.7355764367410260154)✓$$
$$\qquad \lambda=(0.81582831255097778801,\ 0.10370188850320431125,\ 0.05441534828030017616,\ 0.026054450665517724573)✓,\ \sum\lambda-1=0✓（\text{与}\ C-212\ \text{完全一致}✓）$$
$$\qquad Y\approx J(m)^{-1},\quad \|YJ-I\|_{\max}=1.661\times10^{-124}✓✓（\text{数值层}✓）$$
$$\textbf{⭐ 关键发现}：\text{该系统【病态】}✓ —— \text{条件数}\ \sim2\times10^4✓（\lambda\ \text{跨}\ 0.026\text{–}0.82✓、\text{频率到}\ 13✓）$$
$$\qquad \Longrightarrow r=10^{-6}\ \text{时}\ \|I-YJ(X)\|_\infty\approx6>1✗ \Longrightarrow \textbf{必须用更小初始盒}✓（1=1.7\times10^{-7}）$$

## §3 ⭐ 结果（Krawczyk 迭代 $X\leftarrow K(X)\cap X$）

$$\textbf{迭代}：\text{it}=0:\ \text{宽}\ 2.0\times10^{-7},\ \|I-YJ\|\le1.15\times10^{-5}✓,\ K\subset\mathrm{int}X✓；\text{it}=1:\ \text{宽}\ 2.3\times10^{-12}✓,\ 2.87\times10^{-11}✓；\text{it}=2:\ \text{宽}\ 1.1\times10^{-23}✓,\ 1.18\times10^{-22}✓$$
$$\textbf{终盒}：\text{最大坐标宽}=\mathbf{1.198\times10^{-46}}✓✓ \Longrightarrow \textbf{远小于 A 所需}\ X_{\rm ref}\ \text{半宽}\le10^{-6}✓✓$$

$$X_0\ \text{各坐标（严格包含）}：$$
$$z_0=[0.36393546737914837231,\ \cdot]\ ✓（\text{宽}\ 3.6\times10^{-48}✓）,\quad z_1=[1.0426550912448578709,\ \cdot]✓,\quad z_2=[2.3108815298193646024,\ \cdot]✓$$
$$z_3=[0.81582831255097778801,\ \cdot]✓（\text{宽}\ 1.2\times10^{-46}✓）,\quad z_4=[0.10370188850320431125,\ \cdot]✓,\quad z_5=[0.05441534828030017616,\ \cdot]✓,\quad z_6=[0.026054450665517724573,\ \cdot]✓$$
$$\varphi/\pi:\quad [0.1158442571997]✓,\ [0.3318874234231]✓,\ [0.73557643674103]✓$$

## §4 ⭐ 验收记录（唐先生指定的 7 项，逐项）

| # | 项目 | 结果 |
|---|---|---|
| ① | 初始盒 | $r_0=10^{-7}$（中心＝120 dps 精修根，残差 $1.45\times10^{-120}$）✓ |
| ② | 算子与包含关系 | $K(X)=m-YG(m)+(I-YJ(X))(X-m)$，$Y\approx J(m)^{-1}$；$\|YJ-I\|_{\max}=1.66\times10^{-124}$ ✓ |
| ③ | $X_0$ 各坐标宽度 | 最大 $\mathbf{1.198\times10^{-46}}$；$\varphi$ 三分量宽 $\sim10^{-48}$ ✓ |
| ④ | 可逆性/收缩 | $\|I-YJ(X_0)\|_\infty\le\mathbf{1.086\times10^{-45}}<1$ ✓✓ |
| ⑤ | $\lambda$ 严格正性 | $\min\lambda_{\rm lo}=0.02605445067>0$ ✓；$\sum\lambda\in[1.0,1.0]$ ✓ |
| ⑥ | 三条相切差包含 | $S_1-S_5\in[-2.42,2.42]\times10^{-47}$ ✓；$S_1-S_{11}\in[-3.86,3.86]\times10^{-47}$ ✓；$S_1-S_{13}\in[-6.0,6.0]\times10^{-47}$ ✓（**均含 0** ✓✓） |
| ⑦ | **存在性 vs 唯一性** | **存在性** ✓（$K\subset\mathrm{int}X$）；**唯一性** ✓（$\|I-YJ(X_0)\|_\infty<1$）—— **两者【分列】✓✓** |

## §5 ⭐⭐ A ＋ B 合成：局部核缺口一次性消掉

$$\textbf{B 的产出不只是"更小的小数点"}✓，\text{而是【严格相切关系}】✓✓：$$
$$\qquad \forall x\in X_0:\ S_1(x)=S_5(x)=S_{11}(x)=S_{13}(x)✓ \Longrightarrow \boxed{\delta_A\equiv0\ \text{于}\ X_0}✓✓（\S4\ \text{⑥ 的直接后果}✓）$$
$$\textbf{于是 C-221 的条件式升级为【无条件】}✓✓：$$
$$\boxed{\ \forall x\in X_0,\ \forall 0<\|\delta\|\le\rho_{\rm up}=1.4658\times10^{-3}:\quad F_3(x+\delta)\ \ge\ F_3(x)+c_X\|\delta\|-\tfrac{169}{2}\|\delta\|^2\ \ge\ F_3(x)+2.87\times10^{-4}\ >\ F_3(x)\ }✓✓$$
$$\qquad \text{其中}\ c_X=0.319306988✓（\text{含 containment}✓）、R=169✓（\text{解析}✓）$$
$$\qquad \textbf{接口自洽}：X_0\ \text{宽}\ 1.2\times10^{-46}\ll10^{-6}✓ \Longrightarrow X_0\subset X_{\rm ref}\subset B(x^*,\rho_{\rm up})✓✓$$
$$\textbf{结论}：\text{局部核（}\delta_A\ \text{缺口）}\ \textbf{确实被一次性消掉}✓✓；\text{但【不】声称全局极小}✗（\text{那是 C}✓）$$

## §6 本档自我失误（第 39 次，五条）

$$\textbf{39a 矩阵求逆 API}✗：\texttt{lu\_solve(J,\ eye(7))}\ \text{报 IndexError}✗ \Longrightarrow \text{改}\ \texttt{J**-1}✓$$
$$\textbf{39b Jacobian 未初始化}✗✗：\text{梯度行的【非对角}\ \varphi\ \text{项】没置 0}✗ ⟹ \texttt{NoneType}\ \text{比较错}✗ \Longrightarrow \text{整块先}\ \texttt{Iv.pt(0)}✓$$
$$\textbf{39c ⭐ 病态性初判误}✗✗（\textbf{最有价值}）：r=10^{-6}\ \text{时}\ \|I-YJ\|\approx6✗\ \text{我一度怀疑 Jacobian 写错}✗；\text{诊断后确认}：$$
$$\qquad \text{条件数}\sim2\times10^4✓ \Longrightarrow \text{收缩门槛}\ r<1.7\times10^{-7}✓ \Longrightarrow \text{改小初始盒后立即收敛}✓✓（\text{教训：先算条件数，再定初始盒}✓）$$
$$\textbf{39d 迭代式误写}✗：\text{一度用"宽}\ /\ 2"\ \text{更新半径}✗ \Longrightarrow \text{改为标准}\ X\leftarrow K(X)\cap X✓$$
$$\textbf{39e 索引混用}✗：\text{打印"相切差"时用了【变量】索引}✗（\text{应为}\ G\ \text{在盒上的【方程】分量}✓） \Longrightarrow \text{修正后三差均含 0}✓✓$$

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，**先跑后写**）

```
技术词 Krawczyk 算子     命中文件数=1    ::  ./C222-B-interval-newton-KKT-strict-box-X0-existence-and-uniqueness.md
技术词 自由度一致性     命中文件数=1    ::  ./C222-B-interval-newton-KKT-strict-box-X0-existence-and-uniqueness.md
技术词 存在性唯一性分列 命中文件数=1    ::  ./C222-B-interval-newton-KKT-strict-box-X0-existence-and-uniqueness.md
```
⚠️ 实测各 1 命中且均为本档自身（检查在落档后执行）✓ ⟹ **扣除后 0 命中** ⟹ 三项**本档首次命名** ✓（依 `C-168` §6 惯例）

## §8 边界与下一步

$$\textbf{边界}：① X_0\ \text{的存在性/唯一性针对【KKT 系统】}✓，\textbf{不}等于"是全局极小"✗；② \text{interval 算术为自建}✓（\mathrm{SLK}=10^{-100}✓），\text{尚未做第二独立实现}⚠️；$$
$$\qquad \text{③ 病态性}\sim2\times10^4✓\ \text{是事实}✓，\text{但不影响包含证书}✓（\text{已收缩到}\ 10^{-46}✓）；④ \text{未用 RH}✓；\text{未改他档}✓；\text{丙仍不开}✓$$
$$\textbf{下一步}：\textbf{C}：\text{盒外 B\&B @}\ T=F(x_0)✓（\text{球外有正裕量}✓，\text{预计几千～几万箱}✓） \Longrightarrow \text{唯一性 ＋}\ m_3=F(x_0)\ ✓✓$$
