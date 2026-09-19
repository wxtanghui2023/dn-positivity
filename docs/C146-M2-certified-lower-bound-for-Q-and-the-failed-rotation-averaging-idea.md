已查地图（**先查后写**）：`C-145`（M=2 压力测试：Q=7.75 vs K/4=2.5，余量 3.1×；B1 精化；约束点在别处）、`C-144`（Case A 已证）、`C-143`（二阶矩余量实算）。关键词回查：`认证下界`=0、`旋转平均`=0、`反例集不变性`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:28「结果？」→ 继续 ①）**：**把 M=2 的余量从启发式升级为【认证下界】；并检验"符号问题"的一个候选思路。**
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{认证下界（M=2）}：\inf_\theta Q\ \ge\ 4.2467\ >\ K/4=2.5000\quad(1.70\times)✓✓$$
$$\qquad \text{方法}：2000\times2000\ \text{网格}\ +\ \text{Lipschitz 常数}\ L=\sqrt M\cdot MK(K+1)=311.1;\ \text{误差}\le0.691✓✓$$
$$\qquad ⟹\ \textbf{认证} \text{任意}\ M=2\ \text{配置}：\max_k|f(k)|\ \ge\ \sqrt{4.2467/10}=0.6517\ >\ \tfrac12✓✓$$
$$\textbf{(二)}\ \text{余量结论（回答唐先生）}：\text{二阶矩路线}\ \textbf{不需要锋利}；\ \text{约束点}\ \text{余量}\ \ge1.70\times\ (\text{认证})✓✓$$
$$\textbf{(三)}\ ⚠️\ \textbf{符号问题仍在}：\text{认证只给}\ \max_k|f|\ge0.65，\ \text{未给}\ \max_k f\ge\tfrac12✓$$
$$\textbf{(四)}\ ⚠️\ \textbf{本档诚实记录一个失败的思路}：\text{"旋转平均"}\ \text{不可用（\text{反例集并非旋转不变}）✓✓$$

FREEZE-ACK: 本档即冻结期内的认证计算与失败思路记录（依 `§8.1`；不产候选结论）

D0: 本档对象 = **`M=2` 的 `Q` 认证下界（1.70× 余量）＋ 符号问题的未解状态 ＋ 一个失败思路的记录** —— 关系 = 认证与记录，非新机制
D1: 0

# C-146 · **`M=2` 的认证下界（1.70× 余量）＋ 一个失败思路的诚实记录**

> **唐先生 2026-09-19 12:28**：**「结果？」** ✓

---

## §1 ⭐ 认证下界（不再是启发式）

$$\text{方法}：\text{对}\ (\theta_1,\theta_2)\in[0,2\pi)^2\ \text{取}\ 2000\times2000\ \text{网格}（h=3.142\times10^{-3}），\text{直接求}\ \min_{\text{grid}}Q✓$$
$$\qquad \text{Lipschitz}：\Big|\frac{\partial Q}{\partial\theta_j}\Big|\le 2M\sum_{k\le K}k=MK(K+1)\Longrightarrow \|\nabla Q\|\le\sqrt M\,MK(K+1)=311.1✓$$
$$\qquad \text{认证误差}\le L\cdot h\sqrt M/2=0.691✓✓$$
$$\min_{\text{grid}}Q=4.9379\quad\Longrightarrow\quad \boxed{\inf_\theta Q\ \ge\ 4.2467\ >\ K/4=2.5000\ (1.70\times)}✓✓$$
$$\Longrightarrow\ \textbf{认证}：\text{任意}\ M=2\ \text{配置}\ \max_k|f(k)|\ge\sqrt{4.2467/10}=0.6517>\tfrac12✓✓$$

## §2 回答唐先生："是否需要锋利"——**不需要**

$$\text{极值配置}\ (60^\circ,90^\circ)：Q=7.75\ (3.10\times)✓$$
$$\text{认证意义上的最坏配置}：\inf Q\ge4.2467\ (1.70\times)✓✓$$
$$\Longrightarrow\ \text{二阶矩路线在}\ M=2\ \text{上}\ \textbf{处处有余量}（\ge1.70\times）\ \Longrightarrow\ \textbf{不需要常数锋利}✓✓$$

## §3 ⚠️ 剩余唯一障碍：符号（`\max|f|` → `\max f`）

$$\text{认证给}：\exists k:\ |f(k)|\ge0.6517；\ \text{目标}：\exists k:\ f(k)\ge\tfrac12✓$$
$$\qquad \text{若最大值只落在}\ \textbf{负侧}，即}\ \min_kf(k)\le-0.65 \Longrightarrow \text{结论未得}✓✓$$

## §4 ⚠️ 本档诚实记录：**"旋转平均"思路失败**

$$\text{想法}：\text{若}\ \theta\ \text{是反例}（\max_k\mathrm{Re}\,S_0(k)<\tfrac12），\ \text{则对每个旋转}\ \psi\ \text{也应有}\ \max_k\mathrm{Re}\,S_\psi(k)<\tfrac12；$$
$$\qquad \text{于是}\int M(\psi)\,d\psi<\tfrac12\ \text{与}\ \text{Jensen}\ ⟹\ \int M\ge\frac1{\sqrt K}\sqrt{\tfrac12\sum_k|S(k)|^2}\ \text{可给矛盾}✓$$
$$\textbf{失败点}：\text{"反例"只约束}\ \psi=0：\ \text{旋转后的配置}\ \textbf{不必} \text{是反例} \Longrightarrow \text{反例集}\ \textbf{并非旋转不变}✓✓$$
$$\qquad ⟹\ \int M(\psi)d\psi<\tfrac12\ \textbf{不成立} \Longrightarrow \text{该思路作废}✓$$

## §5 下一步（两条并行）

$$\text{①}\ M\ge3\ \text{的严格下界}：\text{网格不可行}（\text{维数}\ M\ge3） \Longrightarrow \text{改用}\ \textbf{区间分支定界} \text{或}\ \textbf{SOS/SDP} \text{表示}✓$$
$$\qquad \text{或找}\ \textbf{解析} \text{下界}：\text{利用}\ Q=\tfrac12\sum_{j,l}[D_K(\theta_j-\theta_l)+D_K(\theta_j+\theta_l)]\ \text{的精确结构}✓$$
$$\text{②}\ \text{符号问题}：\text{候选}＝\textbf{簇分解}：\text{近簇}\ (|\theta_j-\theta_l|\ \text{小})\ \text{行为}\ \text{如}\ \textbf{加权单点} \Longrightarrow \text{可接引理 C}；\ \text{远簇用二阶矩}✓✓$$
$$\qquad \text{这解释了数值事实}：\text{紧配置}\ \textbf{总是近退化} \text{的}✓$$

## §6 边界与回查

- ⚠️ §1 为**实际运行**（网格 `2000\times2000`；Lipschitz 常数按 `|f(k)|\le M` 保守估计；认证误差 `0.691`）✓
- ⚠️ §3／§4 为**诚实状态**（符号未解；一个思路失败并已作废）✓
- ⚠️ **不声称** B2 可闭合；**不声称** `(RP_M)` 已证 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:3x）`[纪律]`（先跑后写）

```
技术词 认证下界     命中文件数=0 ::  ⟹ 本档新增
技术词 旋转平均     命中文件数=0 ::  ⟹ 本档新增
技术词 反例集不变性  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
