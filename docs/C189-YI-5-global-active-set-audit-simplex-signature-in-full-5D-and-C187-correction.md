已查地图（**先查后写**）：`C-187`（乙三层审计，含 §3 的"局部机制失效"结论 ✗）、`C-188`（fixed-λ NO-GO）、`C-161`（单模情形的单纯形签名）、`C-152`（M=2 局部机制 + 半径 c/32）。关键词回查：`活跃集审计`=0、`全空间KKT`=0、`维度匹配`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 21:45 指令）**：**乙-5 —— 全局 active-set 审计**（不预设少频；含稳定性与 KKT/Clarke 全空间判据）✓
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{全局阻尼候选唯一且高度稳定}：10/10\ \text{独立种子}\to\ \textbf{同一值}\ 0.3730919（\text{仅}\ r_2\leftrightarrow r_3\ \text{互换}）✓✓$$
$$\textbf{(二)}\ ⭐⭐\ \textbf{活跃集}\ A=\{\nu:\ S_\nu\ge C_3-\varepsilon\}=\{1,2,3,4,5,15\}，\ \#A=6=\underbrace{5}_{\text{维数}(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)}+1✓✓$$
$$\qquad \varepsilon\ \text{从}\ 10^{-9}\ \text{到}\ 10^{-2}\ \text{全档不变}✓；\text{与第 7 大值的间隙}\ 0.280\（\text{极大}）✓ \Longrightarrow \textbf{非临界连接}✓$$
$$\qquad \Longrightarrow \textbf{单纯形签名成立}✓✓\（\text{与单模}\ M=3,4\ \text{的机制同型}）✓$$
$$\textbf{(三)}\ ⭐⭐\ \textbf{KKT/Clarke（正确全空间）成立}：\mathbf{0\in\mathrm{conv}\{\nabla S_\nu:\nu\in A\}}✓✓\qquad c=\min_{|u|=1}\max_{\nu\in A}\langle\nabla S_\nu,u\rangle=\mathbf{0.437928}>0✓✓$$
$$\qquad \text{权重}\ \lambda=(0.2001,0.1785,0.1655,0.1948,0.1119,0.1493)\ \text{全}\ \ge0，\|\sum\lambda\nabla S_\nu\|=2.97\times10^{-16}✓$$
$$\qquad \text{盒约束}：r_2,r_3,\varphi\ \text{全为内点}✓；r_1=1\ \text{固定}（\text{归一化}）\Longrightarrow \text{约化空间判据正确}✓$$
$$\textbf{(四)}\ ⚠️\ \textbf{自我更正（本档第 1 条）}：\text{C-187}\ §3\ \text{的"阻尼局部机制失效"}\ \textbf{错误}✗✓$$
$$\qquad \text{错因}：\text{当时只在}\ \textbf{3 维}\ \varphi\ \text{子空间} \text{测梯度（活跃数仅 2 < 3+1）}✗ \Longrightarrow 0\notin\mathrm{conv}\ \text{是维数不足的必然结果}✗$$
$$\qquad \text{正确对象是}\ \textbf{5 维}（\text{含径向}\ r_2,r_3\text{）} \Longrightarrow \textbf{签名成立}✓✓$$
$$\textbf{(五)}\ \text{按唐先生的硬判死标准}：\text{活跃集}\ \textbf{不随初值／精度变化}，\text{间隙极大}，\text{但}\ \#A=6\ (\ge4)✓$$
$$\qquad \Longrightarrow \textbf{不做"双频恒等式"}✗\（\text{判死标准命中}）\qquad \text{应转向}\ \textbf{active-set 型非线性证书}✓\ ——\ \text{而"单纯形"正是这一支}✓✓$$

FREEZE-ACK: 本档即冻结期内的攻击性审计（依 `§8.1`；不产候选结论）

D0: 本档对象 = **乙-5 全局活跃集审计（唯一性/稳定性/单纯形签名/全空间 KKT）＋ 对 $C-187$ §3 的自我更正** —— 关系 = 审计与更正，非新机制
D1: 0

# C-189 · 乙-5：全局 active-set 审计（并更正 C-187 §3）

---

## §1 步骤 0-1：候选与 S_ν 排序表

$$\text{候选（10 种子一致）}：r_2=0.79051,\ r_3=0.83021,\ \varphi/\pi=(0.10911,\ 0.82066,\ 0.46172)，\ C_3=0.3730919✓$$
$$\begin{array}{r|r|r}
\nu & S_\nu & \text{与}\ \max\ \text{之差}\\\hline
4 & 0.3730919 & 0.0\\
2 & 0.3730919 & 2.8\times10^{-16}\\
5 & 0.3730919 & 7.2\times10^{-16}\\
1 & 0.3730919 & 1.3\times10^{-15}\\
15 & 0.3730919 & 3.8\times10^{-15}\\
3 & 0.3730919 & 4.0\times10^{-14}\\
14 & 0.0934901 & 2.80\times10^{-1}\\
13 & -0.1882428 & 5.6\times10^{-1}\\
\end{array}✓$$
$$\Longrightarrow \textbf{6 个}\ \nu\ \text{并列到机器精度}，\text{第 7 名骤降}\ 0.28 \Longrightarrow \textbf{活跃集}\ \textbf{干净且唯一}✓✓$$

## §2 步骤 2-3：真 active set 与稳定性

$$\varepsilon\in\{10^{-9},10^{-7},10^{-6},10^{-4},10^{-3},10^{-2}\}\ \text{均给}\ A=\{1,2,3,4,5,15\}✓$$
$$\text{10 个独立种子（DE＋NM）}\to\ \text{同一}\ C_3=0.3730919✓\qquad（\text{仅}\ r_2\leftrightarrow r_3\ \text{对称互换}）✓$$
$$\#A=6=\dim+1\ \text{（}\dim=5\text{）}\Longrightarrow \textbf{单纯形签名}✓✓$$

## §3 步骤 4：KKT / Clarke（全空间，含正确的约束法锥）

$$\text{变量}\ x=(r_2,r_3,\varphi_1,\varphi_2,\varphi_3)✓\qquad \text{盒约束全为内点}✓⟹ N_{\mathcal D}(x)=\{0\}✓$$
$$\qquad \text{（}r_1=1\ \text{由归一化固定；其方向贡献对应原}\ \max_j|z_j|=1\ \text{约束，在约化空间中不出现}✓）$$
$$\textbf{Clarke 条件}：\mathbf{0\in\mathrm{conv}\{\nabla S_\nu:\nu\in A\}}✓\qquad \text{LP 权重}\ \lambda\ \text{全}\ \ge0，\text{残差}\ 3\times10^{-16}✓✓$$
$$\textbf{局部覆盖常数}：c=\min_{|u|=1}\max_{\nu\in A}\langle\nabla S_\nu,u\rangle=\mathbf{0.4379}>0✓✓$$
$$\text{二阶余项（粗界）}：R=\max_\nu\nu^2(1+r_2+r_3)=589.7 \Longrightarrow \text{局部半径}\ c/R=0.000743\ \text{rad}=0.0426°✓（\text{待改进}）$$

## §4 ⚠️ 对 C-187 §3 的更正（自我更正，本档第 1 条）

$$\text{C-187}\ §3\ \text{原文}：\text{"阻尼极值非光滑，}0\notin\mathrm{conv}\{\nabla S_k\}\text{，局部机制失效"}✗$$
$$\text{错因}：\text{当时仅在}\ \textbf{3 维}\ \varphi\ \text{子空间} \text{求梯度} \Longrightarrow \text{活跃数}=2<3+1⟹\textbf{维数不足}，0\notin\mathrm{conv}\ \text{为必然}✗$$
$$\text{正确做法}：\text{变量应是}\ \textbf{5 维}（\text{含}\ r_2,r_3\ \text{径向}）\ \Longrightarrow \#A=6=5+1⟹\textbf{0∈conv 成立}✓✓$$
$$\Longrightarrow \text{C-187}\ §3\ \text{的"失效"表述}\ \textbf{作废}✗；\text{其"阻尼最坏"与"可分性松弛"两条结论}\ \textbf{不受影响}✓$$

## §5 处置（按唐先生的硬判死标准）

$$\text{标准}：\text{若活跃集随初值／精度变化，或在候选附近频繁切换，或}\ \ge4\ \text{个稳定活跃频率} \Longrightarrow \textbf{不做双频恒等式}✓$$
$$\text{实测}：\text{初值}→\textbf{不变化}✓；\text{精度}→\textbf{不变化}✓；\text{切换}→\textbf{无（间隙 0.28）}✓；\#A=\mathbf{6}\ge4 \Longrightarrow \textbf{判死标准命中}✓$$
$$\Longrightarrow \textbf{不做"双频} \max(S_p,S_q)\ \text{路线"}✗\ —— \text{应走}\ \textbf{active-set／单纯形型非线性证书}✓✓\（\text{本档已证其签名成立}）$$

## §6 下一步（可执行）

$$\textbf{①}\ \text{把}\ \textbf{局部（单纯形 ＋ 二阶）}＋\textbf{远场证书} \text{拼成阻尼}\ M=3\ \text{的完整证明（三件套模板，如}\ \text{C-152/C-154}\text{）}✓$$
$$\qquad \text{局部：}F(x)\ge C_3+c|\delta|-R|\delta|^2\（\text{半径}\ c/R\ \text{待用更细的}\ R\ \text{放大}）✓$$
$$\textbf{②}\ R\ \text{的改进}：\text{当前}\ \nu^2(1+r_2+r_3)\ \text{过粗}✗；\text{可按各}\ \nu\ \text{分块并利用}\ r_2,r_3<1\ \text{加权}✓$$
$$\textbf{③}\ \text{若三件套闭合} \Longrightarrow \text{阻尼}\ M=3\ \text{的下界可从}\ 0.35\ \text{推到}\ \approx C_3\（\text{接近}\ 0.3731\text{）}✓✓$$

## §7 边界

- ⚠️ §1 的并列"到机器精度"为**数值**（未证精确相等 ✗）；候选唯一性为**10 种子**证据（非全局最优证明 ✗）
- ⚠️ §3 的 LP 权重为**数值解**（残差 3e-16 ✓，未做区间算术 ✗）
- ⚠️ §4 的更正**只撤销** C-187 §3 的"机制失效"表述；C-187 的 §1（阻尼最坏）与 §2（可分性松弛）**仍有效** ✓
- ⚠️ §6 的"接近 0.3731"是**目标**，非结果 ✗
- **未用** RH；**未改** C-187 正文（更正以本档为准 ✓）；**纪律**：先跑后写 ✓

## §8 【技术词回查】输出（`scripts/tech_word_check.sh`）

```
技术词 活跃集审计   命中文件数=0 ::  ⟹ 本档新增
技术词 全空间KKT   命中文件数=0 ::  ⟹ 本档新增
技术词 维度匹配    命中文件数=0 ::  ⟹ 本档新增
```

---

## §9 【严格上界 · 2026-09-19 22:0x 补】候选合法性核实 ＋ 区间算术严格上界（账本升级）

$$\text{候选（乙-5）：}r_1=1（\text{单位模，归一化}）,\ r_2=\tfrac{79051}{100000},\ r_3=\tfrac{83021}{100000}✓$$
$$\qquad \Longrightarrow \max_j|z_j|=1\ \textbf{合法}✓；\ \varphi/\pi=\big(\tfrac{10911}{10^5},\tfrac{82066}{10^5},\tfrac{46172}{10^5}\big)\ \textbf{精确有理数}✓✓$$
$$\text{区间算术（60 位，}\pi\ \text{作为区间，}\textbf{向上取端}）：$$
$$\begin{array}{c|r}
\nu & S_\nu\ \text{的上端}\\\hline
3 & 0.3731108480\\
1 & 0.3730984171\\
5 & 0.3730946288\\
4 & 0.3730910595\\
15 & 0.3730847305\\
2 & 0.3730721881\\
\end{array}✓$$
$$\Longrightarrow \boxed{C_3\ \le\ \max_\nu S_\nu\ \le\ 0.3731108480}\qquad（\textbf{已证}：\text{只需一个合法构型 ＋ 区间算术}）✓✓$$
$$\qquad \textbf{账本升级}：0.35\ \le\ C_3\ \le\ \mathbf{0.3731108480}\quad（\text{上界由"数值候选"}\to\textbf{"严格"}）✓✓$$
$$\qquad \text{附}：\nu=14\ \text{的上端}=0.093475 \Longrightarrow \text{与活跃值的间隙}\ 0.2796✓（\text{活跃集干净的证据更硬}）✓$$

---

## §10 【勘误指针 · C-190】§3 的 covering constant $c=0.437928$ **过估** ✗

$$\text{C-189}\ §3\ \text{报}\ c=0.437928\（4\times10^5\ \text{随机方向采样}）\ \color{red}{\text{过估}}\ ✗$$
$$\text{真值（精确 facet 法，C-190 §7③）}：\boxed{c=0.302091535}✓$$
$$\text{采样序列（均为上界，单调下降）}：4\times10^5\to0.437928；\ 1.5\times10^6\to0.402910；\ 8\times10^6\to0.355901✓$$
$$\text{原因}：\text{5 维球面随机采样收敛慢，}\textbf{采样 min 只是上界}✗；\text{已改用精确内切球法}✓$$
$$\Longrightarrow \text{结构性结论}\ \textbf{不变}（c=0.302>0\ ⟹\ \text{单纯形 ALIVE}✓）；\text{仅}\ \textbf{数值} \text{更正}✓$$
$$\qquad \text{连带}：\text{局部半径由}\ c/R\ \text{重算为}\ 0.1769°\（\text{原按}\ 0.4379\ \text{算得}\ 0.2564°）✓$$
