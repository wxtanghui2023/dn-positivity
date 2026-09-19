已查地图（**先查后写**）：`C-159`（鸽笼定理；`m_M\le M-1` 的概率证明——本档**核验其常数**）、`C-158`（覆盖引理）、`C-144` §4／`C-150`（计数路线已证失败）、`C-152`–`C-154`（`M=2` 局部法）。关键词回查：`同时逼近障碍`=0、`宽松计数`=0、`宽度常数`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 13:43 两条）**：**① 核验 Hoeffding 常数（唯一外部输入）② 往"多点同时逼近"方向推。**
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{Hoeffding 常数核验结果：原用}\ -t^2/(2M)\ \textbf{正确}✓✓$$
$$\qquad \text{关键}：\cos(k\varphi_j)\in[-1,1]\ \text{的}\ \textbf{区间宽度}=2（\text{非}\ 1） \Longrightarrow \sum_i(b_i-a_i)^2=4M✓$$
$$\qquad \text{标准形式}\ \mathbb P(|\sum X_i-\mathbb E\sum X_i|\ge t)\le2e^{-2t^2/\sum(b_i-a_i)^2}=2e^{-2t^2/(4M)}=2e^{-t^2/(2M)}✓✓$$
$$\qquad \textbf{蒙特卡洛裁决}：\text{经验}\ \mathbb P(|S|\ge8)\approx6.3\times10^{-4}\ (k=1,7,23)\ ✓$$
$$\qquad\qquad \text{本档界}\ 0.139\ \textbf{成立}（\text{经验}\ll\text{界}）✓；\ \text{您提的常数}\ 4.66\times10^{-5}\ \textbf{被经验否定}（6.3\times10^{-4}>4.66\times10^{-5}）✓✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{多点方向：两道障碍（本档实算）}✓$$
$$\qquad \text{①}\ \textbf{同时逼近障碍}：\text{两点同时逼近到}\ 1/K\ \text{需}\ K\sim1/\delta^2=K^2（M=2\ \text{时}\ 100）\ \text{vs 窗口}\ 10 \Longrightarrow \textbf{不可能}✓✓$$
$$\qquad \text{②}\ \textbf{宽松计数障碍}：\text{"一点对齐（测度}\tfrac13\text{）＋其余}\ M-1\ \text{点}\ge-\tfrac12（\text{各}\tfrac23\text{）"}\ \text{的期望个数}$$
$$\qquad\qquad =5M\cdot\tfrac13\cdot(\tfrac23)^{M-1} \Longrightarrow M\ge8\ \text{时}\ <1 \Longrightarrow \textbf{计数法对}\ M\ge8\ \text{失效}✓✓$$

FREEZE-ACK: 本档即冻结期内的常数核验与障碍检验（依 `§8.1`；不产候选结论）

D0: 本档对象 = **Hoeffding 常数核验（含蒙特卡洛裁决）＋ 多点方向的两道障碍** —— 关系 = 核验与障碍定位，非新机制
D1: 0

# C-160 · ⭐ **Hoeffding 常数核验（原用正确）＋ 多点方向的两道障碍**

> **唐先生 2026-09-19 13:43**：① 核验 Hoeffding 常数 ② 往多点同时逼近推 ✓

---

## §1 ⭐ Hoeffding 常数核验（唐先生要求）

$$\text{被核验的量}：\mathbb P\Big(\big|\textstyle\sum_{j\le M}\cos(k\varphi_j)\big|\ge t\Big)\ \le\ 2e^{-t^2/(2M)}\qquad(\text{`C-159` §4 所用})✓$$
$$\textbf{重推（逐行）}：$$
$$\qquad \text{Hoeffding 引理}：X\in[a,b],\ \mathbb EX=0\Longrightarrow\mathbb Ee^{sX}\le e^{s^2(b-a)^2/8}✓$$
$$\qquad \text{本处}\ X=\cos(k\varphi_j)\in[-1,1] \Longrightarrow (b-a)=\mathbf 2 \Longrightarrow (b-a)^2=4✓$$
$$\qquad \text{和}：\mathbb Ee^{sS}\le e^{s^2\cdot4M/8}=e^{s^2M/2}\ ;\ \ \text{Chernoff}：\ \mathbb P(S\ge t)\le e^{-st+s^2M/2}\ \xrightarrow{s=t/M}\ e^{-t^2/(2M)}✓$$
$$\qquad \text{两侧}\Longrightarrow\boxed{2e^{-t^2/(2M)}}✓✓$$
$$\text{与标准形式对照}：\mathbb P\le2e^{-2t^2/\sum_i(b_i-a_i)^2}\ \text{且}\ \textstyle\sum_i(b_i-a_i)^2=4M \Longrightarrow 2t^2/(4M)=t^2/(2M)✓✓$$
$$\Longrightarrow \textbf{原常数正确}；"2t^2/M\text{"}\ \text{对应区间宽度}\ 1（\text{相当于}\ \cos\in[-\tfrac12,\tfrac12]），\ \text{与本处不符}✓$$

$$\textbf{蒙特卡洛独立裁决}（M=12,t=8.0,n=4\times10^5）：$$
$$\begin{array}{c|r|r|r}
k & \text{经验}\ \mathbb P(|S|\ge8) & \text{本档界}\ 2e^{-t^2/(2M)} & \text{"}2e^{-2t^2/M}\text{"}\\\hline
1 & 6.28\times10^{-4} & 0.138967\ ✓ & 4.66\times10^{-5}\ \textbf{✗（小于经验值）}\\
7 & 6.60\times10^{-4} & 0.138967\ ✓ & 4.66\times10^{-5}\ \textbf{✗}\\
23 & 5.90\times10^{-4} & 0.138967\ ✓ & 4.66\times10^{-5}\ \textbf{✗}\\
\end{array}✓✓$$
$$\Longrightarrow \textbf{经验值远大于您提的常数} \Longrightarrow \text{该常数}\ \textbf{为假}；\ \text{本档界}\ \textbf{成立}✓✓$$
$$\text{门槛复核}：M=12\ \text{时}\ t=\sqrt{2M\ln10M}=10.719\le M-1=11\ ✓；\ \text{并界}<1✓✓\ \text{（结论不变）}✓$$
$$\text{旁证}：M=12\ \text{经验}\ \max_k|S|\ \text{的}\ 50/90/99\%\ \text{分位}=7.93/9.68/11.47，\ \mathbb P(\max\le10.72)\approx0.973✓$$

## §2 ⚠️ 多点方向：两道障碍（本档实算）

$$\textbf{① 同时逼近障碍}：\text{要把}\ \textbf{两个}\ \text{点同时逼近到}\ 1/K：\ \text{Dirichlet/Minkowski 需}\ K\sim1/\delta^2=K^2✓$$
$$\qquad M=2：K^2=100\ \text{vs 窗口}\ 5M=10 \Longrightarrow \text{差}\ 10\ \text{倍}；\ \text{一般}\ M：\text{需}\ \sim(5M)^2\gg5M✓$$
$$\qquad \Longrightarrow \textbf{"两点同时在窗口内几乎对齐"是不可能事件} \Longrightarrow \text{多次鸽笼}\ \textbf{不可行}✓✓$$
$$\textbf{② 宽松计数障碍}：\text{退一步，只要求"一点强对齐＋其余不离谱"：}$$
$$\qquad g(k)：\cos\ge\tfrac12（\text{测度}\tfrac13）；\ b(k)：\cos\ge-\tfrac12（\text{测度}\tfrac23）✓$$
$$\qquad \text{期望个数}=5M\cdot\tfrac13\cdot\big(\tfrac23\big)^{M-1}：$$
$$\begin{array}{c|rrrrrr}
M & 3 & 5 & 7 & 8 & 10 & 12\\\hline
\mathbb E & 2.22 & 1.65 & 1.02 & 0.78 & 0.43 & 0.23\\
\end{array}✓✓$$
$$\qquad \Longrightarrow M\ge8\ \text{时}\ \mathbb E<1 \Longrightarrow \textbf{该计数路线对}\ M\ge8\ \text{失效}✓✓$$
$$\textbf{③ 对照}：\text{若把其余点的下限放宽到}\ -1：\text{期望}\ 5M/3\gg1\ \text{但结论只给}\ \tfrac12-(M-1)<0\ (M\ge3)✓$$

$$\Longrightarrow \textbf{净结论}：\text{"多维鸽笼／同时丢番图逼近"在"}\textbf{度量计数}" \text{形式下}\ \textbf{被阻塞}✓✓$$
$$\qquad \text{这与本项目早先结论一致}：\text{计数／鸽笼路线结构性失败}（\text{`C-144` §4、`C-150`}）✓$$

## §3 可证的"聚类"情形（诚实：范围很窄）

$$\text{若全部}\ M\ \text{点落在长度}\ \varepsilon\ \text{的弧内}：\text{鸽笼定理（对弧心）} \exists k\le5M:\cos(k\varphi_0)\ge\cos\tfrac{2\pi}{5M+1}✓$$
$$\qquad \cos\ \text{为 1-Lipschitz} \Longrightarrow \cos(k\varphi_j)\ge\cos\tfrac{2\pi}{5M+1}-k\varepsilon\ge\cos\tfrac{2\pi}{5M+1}-5M\varepsilon✓$$
$$\qquad \Longrightarrow S\ge M\big[\cos\tfrac{2\pi}{5M+1}-5M\varepsilon\big]\ \ge\ \tfrac12\quad\text{若}\ \varepsilon\lesssim\tfrac1{25M^2}✓$$
$$\qquad ⚠️\ \text{故仅覆盖}\ \varepsilon\lesssim1/M^2\ \text{的极小弧} \Longrightarrow \textbf{范围很窄，不解决问题}✓$$

## §4 方向判断（本档结论）

$$\text{多点情形}\ \textbf{不能} \text{靠度量计数（本档两障碍＋既有结论）} \Longrightarrow \text{需}\ \textbf{结构论证}：$$
$$\qquad \text{①}\ M=2\ \text{的}\ \textbf{局部梯度法}（\text{`C-152`：活跃}\ k\ \text{的梯度正张成}）\ \text{可推广到}\ M\ \text{维？}✓$$
$$\qquad \text{②}\ \textbf{周期／lcm 法}（\text{`C-159`：}\mathrm{lcm}\le5(M+1)\ \text{类已覆盖}）✓$$
$$\qquad \text{③}\ \text{未覆盖类}：\mathrm{lcm}>5(M+1)\ \text{（无理／大分母）} \Longrightarrow \text{仍需新工具}✓$$

## §5 边界与回查

- ⚠️ §1 的重推为**逐行**；蒙特卡洛为**实算**（`n=4\times10^5`，三个不同 `k`）⟹ 裁决为**经验级**（非证明），但足以否定 "2t^2/M" 这个常数（因其小于经验值）✓✓
- ⚠️ §2／§3 为**实算＋初等估计** ✓
- ⚠️ **不声称** 多点情形可证或不可证；**不声称** 一般单调性 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 13:5x）`[纪律]`（先跑后写）

```
技术词 同时逼近障碍  命中文件数=0 ::  ⟹ 本档新增
技术词 宽松计数     命中文件数=0 ::  ⟹ 本档新增
技术词 宽度常数     命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
