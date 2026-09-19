已查地图（**先查后写**）：`C-144` §4（"计数／鸽笼路线结构性失败：需 `n_k\ge2M/3+1/3`，平均 `n_k\approx M/3`"）、`C-149` §4（本档须**撤回**其中"覆盖计数"草图）、`C-147` §1（反射归约）、`E4-ENGINE-4`（卡点逐字）。关键词回查：`好集`=0、`覆盖计数`=0、`有限覆盖论证`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:49 预警）**：**"部分对齐引理"是否只是重蹈 `C-144` §4 的计数覆辙？先用 `(60^\circ,90^\circ)` 压力测试。**
**结论（先行）**：$$\textbf{(一)}\ ⚠️\ \textbf{唐先生预警正确}：\text{压力测试}\ \textbf{决定性失败} —— G_1\cap G_2=\varnothing✓✓$$
$$\qquad G_1(60^\circ)=\{1,5,6,7\},\quad G_2(90^\circ)=\{4,8\},\quad G_1\cap G_2=\varnothing \Longrightarrow \textbf{覆盖计数论证不可能成立}✓✓$$
$$\textbf{(二)}\ ⭐\ \text{但和恰够}（\text{逐}\ k\ \text{和}：0.5,-1.5,-1,0.5,0.5,0,0.5,0.5,-1,-1.5）：$$
$$\qquad \text{机制}＝\textbf{未对齐项贡献}\ 0\ \text{而非}\ -1（\cos(90^\circ k)=0\ \text{当}\ k\ \text{奇}） \Longrightarrow \text{计数界}\ \tfrac32n_k-M\ \textbf{系统性过粗}✓✓$$
$$\textbf{(三)}\ ⭐\ \textbf{新信息＝算术结构}，\text{不是计数}：\text{好集}\ G(\varphi)=\{k:\cos(k\varphi)\ge\tfrac12\}＝\bigcup_n\Big[\tfrac{2\pi n-\pi/3}{\varphi},\tfrac{2\pi n+\pi/3}{\varphi}\Big]$$
$$\qquad \Longrightarrow \text{是}\ \textbf{等差数列型的并}（\text{间距}\ 2\pi/\varphi）;\ \text{计数论证把它们当}\ \textbf{任意子集} \text{用} \Longrightarrow \text{必然失败}✓✓$$
$$\textbf{(四)}\ \text{故}\ \textbf{撤回}\ \text{`C-149` §4／§5 的"覆盖计数"草图}；\ \text{新靶子＝}\textbf{有限维联合不等式}：$$
$$\qquad \min_{\varphi_1,\dots,\varphi_r}\ \max_{k\le5M}\ \sum_lw_l\cos(k\varphi_l)\ \ge\ \tfrac12✓✓$$
$$\textbf{(五)}\ \text{`M=2` 已可拆成}\ \textbf{有限覆盖论证}（\text{本档列出}）；\ \text{网格认证给}\ 0.4738（\text{差} 0.026，\text{需混合法}）✓$$

FREEZE-ACK: 本档即冻结期内的预警验证与草图撤回（依 `§8.1`；不产候选结论）

D0: 本档对象 = **(60°,90°) 压力测试（`G_1\cap G_2=\varnothing`）＋ 撤回覆盖计数草图 ＋ "新信息＝算术结构" ＋ `M=2` 有限覆盖路线** —— 关系 = 验证与撤回，非新机制
D1: 0

# C-150 · **覆盖计数已撤回：`G_1∩G_2=∅`；新信息是算术结构**

> **唐先生 2026-09-19 12:49**：投稿前先确认"部分对齐引理"是否只是重蹈计数覆辙；用 `(60^\circ,90^\circ)` 压力测试 ✓

---

## §1 ⚠️ 压力测试（**决定性**）

$$G_1(60^\circ)=\{k\le10:\cos(k\cdot60^\circ)\ge\tfrac12\}=\{1,5,6,7\}✓$$
$$G_2(90^\circ)=\{k\le10:\cos(k\cdot90^\circ)\ge\tfrac12\}=\{4,8\}✓$$
$$\boxed{G_1\cap G_2=\varnothing}✓✓$$
$$\Longrightarrow\ \textbf{不存在}\ \text{两个簇同时对齐的}\ k \Longrightarrow \text{任何"覆盖计数／并集覆盖"论证}\ \textbf{在本例即不成立}✓✓$$
$$\qquad ⟹\ \textbf{唐先生预警成立}：\text{"部分对齐引理"若走覆盖计数，}\ \text{在}\ \textbf{最简饱和例子} \text{上就已经死了}✓✓$$

## §2 但和恰够：机制是"未对齐项贡献 0，不是 −1"

$$\text{逐}\ k\ \text{的和}：k=1..10:\quad 0.5,\ -1.5,\ -1,\ 0.5,\ 0.5,\ 0,\ 0.5,\ 0.5,\ -1,\ -1.5✓$$
$$\max_k f(k)=0.5\quad(\text{在}\ k=1,4,5,7,8)✓✓$$
$$\qquad k=1：\cos60^\circ=0.5,\ \cos90^\circ=0 \Longrightarrow \text{和}=0.5✓$$
$$\qquad ⚠️\ \text{计数界的错误}：f(k)\ge\tfrac32n_k-M\ \text{假定未对齐项}\ =-1；\ \text{实际}\ \cos(90^\circ k)=0\ (k\ \text{奇})✓✓$$
$$\Longrightarrow\ \textbf{计数界系统性过粗}（\text{这正是}\ \text{`C-144`}\ \text{§4 失败的同源原因}）✓✓$$

## §3 ⭐ 新信息＝**算术结构**（而非计数）

$$G(\varphi)=\Big\{k:\ \cos(k\varphi)\ge\tfrac12\Big\}=\bigcup_{n}\Big[\frac{2\pi n-\pi/3}{\varphi},\ \frac{2\pi n+\pi/3}{\varphi}\Big]✓✓$$
$$\qquad \Longrightarrow \text{单位长度上密度}\ \tfrac13、\ \textbf{间距}\ 2\pi/\varphi \Longrightarrow \text{是}\ \textbf{等差数列型的并}✓✓$$
$$\qquad (60^\circ:\ \text{周期}\ 6，G=\{k\equiv0,\pm1\ (\mathrm{mod}\ 6)\}；\ 90^\circ:\ \text{周期}\ 4，G=\{k\equiv0\ (\mathrm{mod}\ 4)\})✓✓$$
$$\text{计数论证把它当}\ \textbf{任意子集}（\text{只用基数}\ M/5\ \text{或}\ M/3） \Longrightarrow \text{丢掉了}\ \textbf{全部相位信息}✓✓$$
$$\Longrightarrow\ \text{正确靶子}＝\textbf{有限维联合不等式}：$$
$$\qquad \boxed{\min_{\varphi_1,\dots,\varphi_r}\ \max_{k\le5M}\ \sum_l w_l\cos(k\varphi_l)\ \ge\ \tfrac12}✓✓$$

## §4 `M=2` 的有限覆盖路线（本档列出）

$$\text{目标}：\min_{\varphi_1,\varphi_2\in[0,\pi]}\ \max_{k\le10}\Big[\cos(k\varphi_1)+\cos(k\varphi_2)\Big]\ \ge\ \tfrac12✓$$
$$\text{情形 A}：\text{两点都近}\ \pi\mathbb Z\ (\le\pi/6) \Longrightarrow \text{Case A 引理：}f(2)\ge\tfrac32\cdot2-2=1✓✓$$
$$\text{情形 B}：\text{仅一点近}\ \pi\mathbb Z，\text{另一点}\ \varphi_2\in[\pi/6,5\pi/6] \Longrightarrow \text{需}\ \exists k\in\{1,2,3\}:\cos(k\varphi_2)\ge-\cos(k\varphi_1)✓$$
$$\text{情形 C}：\text{两点都在}\ [\pi/6,5\pi/6] \Longrightarrow \text{联合覆盖（有限多段，须逐段核）}✓$$
$$\Rightarrow\ \text{全部化归}\ \textbf{有限个}\ (\text{二维})\ \text{区间覆盖判定}；\ \text{无新的分析难点}✓✓$$

## §5 数值认证现状（诚实）

$$\text{网格}\ 1200\times1200\ \text{上}\ \min g=0.500000\ (\text{在}\ (60^\circ,90^\circ))，\ \text{网格上}\ g<0.5\ \text{的点数}=0✓$$
$$\qquad \text{但}\ \text{Lipschitz}\ L=\sqrt2K=14.1 \Longrightarrow \text{认证误差}\ \le0.0262 \Longrightarrow \text{认证下界}\ 0.4738<0.5✗$$
$$\Longrightarrow\ \textbf{纯网格＋Lipschitz 不够}；\ \text{需}\ \textbf{混合法}：\text{在极小点邻域用}\ \textbf{精确代数}（\text{有理角}），\ \text{其余处用网格＋Lipschitz}✓✓$$

## §6 边界与回查

- ⚠️ §1／§2／§3 为**实际运行 ＋ 本档分析**（`G` 集逐项计算；和表逐项）✓
- ⚠️ §4 的三种情形为**路线草案**（未逐段证）；§5 数值为实际运行 ✓
- ⚠️ **撤回** `C-149` §4／§5 的"覆盖计数"草图（已在原档追加撤回指针）✓
- ⚠️ **不声称** `M=2` 已证；**不声称** 计数路线之外无路 ✓
- **未用** RH；**未改**任何原档（仅追加撤回指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:5x）`[纪律]`（先跑后写）

```
技术词 好集       命中文件数=0 ::  ⟹ 本档新增
技术词 覆盖计数     命中文件数=0 ::  ⟹ 本档新增
技术词 有限覆盖论证  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
