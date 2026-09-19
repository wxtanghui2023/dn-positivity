已查地图（**先查后写**）：`C-147`（负部链 `Q\le(M+\tfrac12)K/2-MS`）、`C-148`（`\delta`-敏感性；DEAD→"差 2×待救"；反例集探测）、`C-143`／`C-146`（`Q_{\min}` 与认证）、`C-144`（Case A）。关键词回查：`锐化链条`=0、`部分对齐`=0、`聚合量不足`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:46「继续」）**：**攻"联合不等式"**：把粗略常数换成**真实量**后，链条还能否闭合？
**结论（先行）**：$$\textbf{(一)}\ ⭐\ \textbf{锐化链条（本档实测）}：CB_{\text{sharp}}:=\tfrac P2+m^-\,N\quad(P:=\sum_{f\ge0}f,\ N:=\sum_{f<0}|f|,\ m^-:=\max|f_{\text{neg}}|)✓✓$$
$$\qquad \text{这是}\ \textbf{有效} \text{条件上界}（0\le f<\tfrac12\Rightarrow f^2\le\tfrac f2;\ f<0\Rightarrow f^2\le m^-|f|）✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{实测：锐化后仍差}\ \approx2\times \Longrightarrow \text{路线}\ \textbf{不能} \text{靠"换更真的常数"救活}✓✓$$
$$\textbf{(三)}\ \text{故}\ \textbf{救活必须靠}\ \textbf{联合结构}（\text{超出聚合量}\ P,N,m^-）\ \text{的新不等式}✓✓$$
$$\textbf{(四)}\ \text{策略处置}：\text{矩量路线}\ \textbf{降级}；\ \text{主攻转}\ \textbf{簇合并归纳（直接攻}\ \max\text{）}✓✓$$

FREEZE-ACK: 本档即冻结期内的链条实测与策略处置（依 `§8.1`；不产候选结论）

D0: 本档对象 = **锐化链条的实测（仍差 2×）＋ "救活必须靠联合结构"的结论 ＋ 策略转向** —— 关系 = 实测与转向，非新机制
D1: 0

# C-149 · **锐化链条仍差 2×；救活必须靠联合结构**

> **唐先生 2026-09-19 12:46**：**「继续」** ✓

---

## §1 锐化链条（把粗略常数换成真实量）

$$\text{`C-147` 的粗略链}：Q\le\Big(M+\tfrac12\Big)\tfrac K2-M\,S\quad(\text{用了}\ \sum_{f\ge0}f<\tfrac K2,\ |f|\le M)✓$$
$$\textbf{锐化版}（\text{用真实的}\ P,N,m^-）：
\qquad Q\ \le\ \tfrac12 P\ +\ m^-\,N\ =:\ CB_{\text{sharp}}✓✓$$
$$\qquad \text{合法性}：0\le f<\tfrac12\Rightarrow f^2\le\tfrac f2\ (\text{紧于}\ f=\tfrac12)；\ f<0\Rightarrow f^2\le m^-|f|\ (\text{紧于}\ f=-m^-)✓$$

## §2 ⭐ 实测（对抗配置处，逐 `M`）

$$\begin{array}{c|r|r|r|r|r|r|r}
M & \max_k f^* & Q & P & N & m^- & CB_{\text{sharp}} & Q_{\min}\\\hline
2 & 0.5000 & 7.75 & 2.50 & 5.00 & 1.50 & 8.75 & 4.94\\
3 & 0.8090 & 17.50 & 4.38 & 9.05 & 2.66 & 26.25 & 9.85\\
4 & 0.8660 & 22.98 & 7.17 & 10.46 & 2.96 & 34.52 & 18.19\\
5 & 1.1674 & 45.55 & 9.08 & 15.22 & 3.73 & 61.29 & 26.95\\
\end{array}✓✓$$
$$\Longrightarrow\ CB_{\text{sharp}}\ /\ Q_{\min}=1.77,\ 2.66,\ 1.90,\ 2.27 \Longrightarrow \textbf{处处}\ \approx2\times \Longrightarrow \textbf{链条不能闭合}✓✓$$
$$\qquad \text{且}\ CB_{\text{sharp}}\ge Q\ \text{处处成立}（\text{合法性验证通过}）✓$$

## §3 ⭐ 为何"换更真的常数"救不活（结构性诊断）

$$\text{链条的损失有}\ \textbf{两个独立来源}：$$
$$\qquad \text{(i)}\ \text{把}\ \sum_{f\ge0}f\ \text{用}\ \tfrac K2\ \text{替} \Longrightarrow \text{可由}\ P\ \text{修复（本档已做）}✓$$
$$\qquad \text{(ii)}\ \text{把}\ \sum_{f<0}f^2\ \text{用}\ m^-N\ \text{替} \Longrightarrow \textbf{不可修复}：\text{需}\ \sum f_{\text{neg}}^2\ \text{的}\ \textbf{真实值}，$$
$$\qquad\qquad \text{而它}\ \textbf{不是} \text{聚合量}\ (P,N,m^-)\ \text{的函数} \Longrightarrow \text{必须引入}\ \textbf{联合结构}✓✓$$
$$\Longrightarrow\ \boxed{\text{救活路线}\ \Longrightarrow\ \text{必须证一个}\ \textbf{联合不等式}：\text{在}\ \{\forall k:\ f(k)<\tfrac12\}\ \text{上}\ \sum f^2\ \text{的上界}\ <\ Q_{\min}}✓✓$$
$$\qquad \text{该不等式}\ \textbf{超出} \text{本链的形式}；\ \text{其证明需用到}\ f\ \text{的}\ \textbf{正权和／PSD 结构}✓✓$$

## §4 策略处置

$$\text{①}\ \text{矩量路线}\ \textbf{降级}（\text{不是判死}）：\ \text{其"标准形式"（聚合量 + 粗略／锐化链）}\ \textbf{已穷尽}，\ \text{差}\ \approx2\times✓$$
$$\text{②}\ \text{主攻转}\ \textbf{簇合并归纳}（\text{直接攻}\ \max，\text{不用矩量}）：\ \text{使能工具＝}\text{`C-147` §1 反射归约}✓✓$$
$$\qquad \text{已证的关键情形}：\textbf{单簇}\ (r=1)\ \text{平凡}：f(k)=M\cos(k\varphi) \Longrightarrow \text{引理 C 给}\ \max\ge M/2\ge\tfrac12✓✓$$
$$\qquad \text{待攻核心}：\textbf{部分对齐}（\text{两簇以上的"好 }k\text{"不重合}）——\ \text{例：}\varphi=(60^\circ,90^\circ)\ \text{时}\ k=1\ \text{仅第一簇对齐}，$$
$$\qquad\qquad \text{但}\ \text{和}\ =0.5+0=0.5\ \textbf{恰够} \Longrightarrow \text{证明须精确处理"部分对齐的加和"}✓✓$$

## §5 边界与回查

- ⚠️ §1／§3 为**本档分析与实测**（`[reductio]`／`[structure]` 标注已按 `C-148` 建议）✓
- ⚠️ §2 数值为**实际运行**（Nelder–Mead，20 随机起点 ＋ 3 结构化起点；`Q_{\min}` 为无约束最小值）✓
- ⚠️ **不声称** 联合不等式成立或否；**不声称** 矩量路线已死 ✓
- **未用** RH；**未改**任何原档 ✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §6 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:5x）`[纪律]`（先跑后写）

```
技术词 锐化链条   命中文件数=0 ::  ⟹ 本档新增
技术词 部分对齐   命中文件数=0 ::  ⟹ 本档新增
技术词 聚合量不足  命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓

---

## 【撤回·`C-150`】（2026-09-19 12:5x）

⚠️ §4／§5 的"**覆盖计数**"草图**作废**：
压力测试 `(60^\circ,90^\circ)` 给出 $G_1\cap G_2=\varnothing$（$G_1=\{1,5,6,7\}$，$G_2=\{4,8\}$）
⟹ 不存在两簇同时对齐的 $k$，覆盖计数论证在最简饱和例子上即不成立。
新信息＝**算术结构**（$G(\varphi)$ 是间距 $2\pi/\varphi$ 的等差数列之并），靶子改为有限维联合不等式。
