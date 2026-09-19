已查地图（**先查后写**）：`C-144`（Case A 引理已证；Case B 硬核；**B1/B2 草案**）、`C-143`（二阶矩余量实算）、`E4-ENGINE-4`（`M=2` 极值配置 `(60.06^\circ,90.02^\circ)`）、`E4-ENGINE-2`（引理 C）。关键词回查：`压力测试点`=0、`相干性条件`=0、`交错区`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:26 追问）**：**① M=2 极值配置在其他 `k` 上 `f(k)` 的完整取值表？② 候选不等式（如 `\sum_kf(k)^2>K/4`）在该配置上是否恰好取等？**
**结论（先行）**：$$\textbf{(一)}\ \textbf{完整表}\ (M=2,\ (60^\circ,90^\circ),\ K=10)：f=(0.5,-1.5,-1,0.5,0.5,0,-1.5,-1.5,-1,-1.5)\ \text{顺序见 §1}✓$$
$$\qquad \max_k f(k)=0.5000\ \textbf{恰饱和}✓✓$$
$$\textbf{(二)}\ ⭐\ Q:=\sum_kf(k)^2=7.7500\ \ \text{vs}\ \ K/4=2.5000 \Longrightarrow Q/(K/4)=\mathbf{3.10} \Longrightarrow \textbf{严格大于，余量 3.1 倍}✓✓$$
$$\qquad ⟹\ \textbf{该配置不构成二阶矩路线的紧点} \Longrightarrow \text{B2 的论证}\ \textbf{不需要锋利}✓✓$$
$$\textbf{(三)}\ \text{该配置}\ \textbf{属 B2}：\theta_1+\theta_2=150^\circ,\ \theta_1-\theta_2=-30^\circ；\ \text{交叉项}\ \sum_k\cos(k(\theta_1+\theta_2))=-0.134（\text{弱}）✓✓$$
$$\textbf{(四)}\ ⚠️\ \textbf{精化 B1}：\text{相干叠加的条件是}\ \theta_j\pm\theta_l\approx0\ (\mathrm{mod}\ 2\pi)；\ \theta_j+\theta_l\approx\pi\ \text{给}\ \textbf{交错}（\cos k\pi=(-1)^k）✓✓$$
$$\textbf{(五)}\ \text{真正的约束点是}\ Q\ \text{极小配置}：\theta=(14.796^\circ,317.427^\circ),\ \min Q=4.9375（\text{余量}\ 1.975\times）✓✓$$

FREEZE-ACK: 本档即冻结期内的压力测试实算与定义精化（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=2` 极值配置的完整 `f` 表与 `Q` 压力测试（余量 3.1 倍）＋ B1 相干性条件的精化 ＋ 约束点定位** —— 关系 = 实算与精化，非新机制
D1: 0

# C-145 · **`M=2` 极值的压力测试：`Q` 严格超出 `K/4` 达 3.1 倍；B1 定义精化**

> **唐先生 2026-09-19 12:26**：① 该配置在其余 `k` 上的 `f(k)` 完整表？② 候选不等式是否**恰好取等**？✓

---

## §1 完整压力测试表（`M=2`，`(60^\circ,90^\circ)`，`K=5M=10`）

$$\begin{array}{c|rrrrrrrrrr}
k & 1 & 2 & 3 & 4 & 5 & 6 & 7 & 8 & 9 & 10\\\hline
f(k) & 0.500 & -1.500 & -1.000 & 0.500 & 0.500 & 0.000 & 0.500 & 0.500 & -1.000 & -1.500\\
f(k)^2 & 0.250 & 2.250 & 1.000 & 0.250 & 0.250 & 0.000 & 0.250 & 0.250 & 1.000 & 2.250\\
\end{array}✓✓$$
$$\max_kf(k)=0.5000\ (\text{在}\ k=1,4,5,7,8\ \text{五处}\ \textbf{同时} \text{取到}) \Longrightarrow \textbf{恰饱和}✓✓$$
$$Q=\sum_kf(k)^2=7.7500;\qquad K/4=2.5000;\qquad \boxed{Q/(K/4)=3.100}✓✓$$
$$\text{扰动版}\ (60.06^\circ,90.02^\circ)：\max f=0.5036,\ Q=7.7264,\ \text{比值}\ 3.091\quad(\text{结论不变})✓$$

## §2 ⭐ 回答唐先生的核心问题

$$\text{若}\ Q\ \text{在该配置}\ \textbf{恰好取等}\ (Q=K/4=2.5) \Longrightarrow \text{B2 必须}\ \textbf{锋利到不损常数}；$$
$$\text{实算给出}\ Q=7.75\ \textbf{严格大于}\ 2.5\ (\times3.10) \Longrightarrow \boxed{\text{B2 的论证可以有一点操作空间}}✓✓$$
$$\qquad \text{机制（为何有余量）}：\text{该配置在}\ k=2,3,9,10\ \text{处}\ f\ \text{很负}（-1.5,-1,-1,-1.5），$$
$$\qquad \qquad \text{这些负值把}\ Q\ \text{推高} \Longrightarrow \text{"}\max f\ \text{饱和"与"}\ Q\ \text{有余量"}\ \textbf{在同一配置上并存}✓✓$$

## §3 B1／B2 判定（唐先生判断正确：属 **B2**）

$$\theta_1+\theta_2=60^\circ+90^\circ=150^\circ,\qquad \theta_1-\theta_2=-30^\circ$$
$$\text{交叉项相干性}：\sum_{k\le10}\cos\big(k(\theta_1+\theta_2)\big)=-0.134\ (\textbf{弱});\quad \sum_{k\le10}\cos\big(k(\theta_1-\theta_2)\big)=-1.866✓$$
$$\Longrightarrow\ \text{两个交叉项}\ \textbf{都不相干} \Longrightarrow \text{该配置}\ \textbf{属 B2}（\text{一般位置}）✓✓$$
$$\qquad ⟹\ \textbf{难度排序修正}：\text{B1 可期、B2 是硬核；而}\ (\text{60}^\circ,\text{90}^\circ)\ \text{正是 B2 的}\ \textbf{压力测试点}✓✓$$

## §4 ⚠️ B1 定义精化（本档发现）

$$\textbf{相干叠加（reinforcement）的条件是}\ \theta_j\pm\theta_l\approx0\ (\mathrm{mod}\ 2\pi)✓$$
$$\qquad \text{而}\ \theta_j+\theta_l\approx\pi\ \text{给的是}\ \textbf{交错}：\cos(k\pi)=(-1)^k \Longrightarrow \sum_k\ \text{部分抵消}✓✓$$
$$\Longrightarrow\ 150^\circ\ (\text{距}\ \pi\ \text{仅}\ 30^\circ)\ \text{落在}\ \textbf{交错区}，\ \text{故对}\ Q\ \text{贡献小}（\text{实测}-0.134）✓✓$$
$$\qquad \textbf{故 B1 应定义为}：\exists j\ne l:\ \mathrm{dist}(\theta_j+\theta_l,2\pi\mathbb Z)\le\delta \vee \mathrm{dist}(\theta_j-\theta_l,2\pi\mathbb Z)\le\delta✓$$

## §5 约束点定位（真正的紧点在哪）

$$\text{对抗搜索}\ Q\ \text{极小配置}：\theta=(14.796^\circ,\ 317.427^\circ),\quad \min Q=4.9375✓$$
$$\qquad \text{该配置}\ f=(1.703,0.954,0.103,-0.473,-0.564,-0.230,0.235,0.468,0.235,-0.437),\quad \max f=1.703✓$$
$$\qquad \text{余量}\ Q/(K/4)=1.975\ \Longrightarrow \textbf{约束点在别处}，\ \text{但余量仍}\ \approx2\times✓✓$$
$$\text{全}\ M\ \text{读数}：\text{余量最小者为}\ M=1\ (1.31\times,\ \text{但}\ M=1\ \text{已有直接证明})，\ \text{随}\ M\ \text{增至}\ 9.74\times✓✓$$
$$\Longrightarrow\ \boxed{\text{二阶矩路线的障碍是}\ \textbf{可证性}，\ \textbf{不是} \text{余量}}✓✓$$

## §6 边界与回查

- ⚠️ §1／§3／§5 为**实际运行**（`/tmp` 脚本：`f` 表逐项；对抗搜索 Nelder–Mead × 200 起点）✓
- ⚠️ §4 为**定义精化**（本档），`B1` 的 `\delta` 阈值待定 ✓
- ⚠️ **不声称** B2 可闭合；**不声称** `(RP_M)` 已证 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:3x）`[纪律]`（先跑后写）

```
技术词 压力测试点   命中文件数=0 ::  ⟹ 本档新增
技术词 相干性条件   命中文件数=0 ::  ⟹ 本档新增
技术词 交错区      命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
