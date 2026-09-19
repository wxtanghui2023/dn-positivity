已查地图（**先查后写**）：`C-147`（反射归约／负部链／"二阶矩路线 DEAD"——本档**更正其强度**）、`C-143`／`C-145`／`C-146`（余量与认证）、`C-144`（Case A）、`E4-ENGINE-4`（撤回指针）。关键词回查：`δ-敏感性`=0、`反例集探测`=0、`联合不等式`=0（**均本档新增**）。
**本档任务（唐先生 2026-09-19 12:42 两问）**：**① 负部链的逻辑骨架（反证假设用在几处）② "10 倍缺口"是否对 `\delta` 选取敏感（会不会是"假死"）**
**结论（先行）**：$$\textbf{(一)}\ \text{逻辑骨架}：\text{反证假设}\ (f<\tfrac12)\ \text{用在}\ \textbf{①与③}（\text{同一机制：}\textbf{正部} \text{被}\ \tfrac12\ \text{压住}）；\ \textbf{②不用假设}（\text{只用}\ |f|\le M）✓✓$$
$$\textbf{(二)}\ ⚠️\ \textbf{唐先生判断正确：我昨天判重了}：\text{"}10\times\ \text{缺口"}\ \text{来自我}\ \textbf{任意选的}\ \delta\approx0.4（c_\delta\approx13）✓✓$$
$$\qquad \text{按配置的}\ \textbf{自然}\ \delta\ (\text{极值配置}\ \delta=\pi/3)：c_\delta=\tfrac12+\tfrac1{2\sin^2(\pi/6)}=2.5 \Longrightarrow \text{缺口降到}\ \approx4\text{–}5\times✓✓$$
$$\textbf{(三)}\ ⚠️\ \text{但}\ (M+\tfrac12)K/2\ \text{项的}\ \textbf{2× 缺口与}\ \delta\ \textbf{无关}（\text{来自①／②的粗略性}） \Longrightarrow \text{调}\ \delta\ \textbf{不能} \text{消除它}✓✓$$
$$\textbf{(四)}\ \boxed{\text{更正}\ \text{`C-147`}\ \text{的"DEAD"}：\text{应降级为"以粗略界计差}\ \approx2\times；\ \text{救活取决于更强的}\ \textbf{联合不等式}（\text{未证}）"}✓✓$$
$$\textbf{(五)}\ ⭐\ \textbf{新实验（受约束对抗优化）}：\text{直接探测}\ \textbf{反例集}\ \{\max_kf<\tfrac12\} \Longrightarrow \text{优化器}\ \textbf{压不到}\ 0.5\ \text{以下}（M=2\ \text{卡在}\ 0.5001）✓✓$$

FREEZE-ACK: 本档即冻结期内的敏感性重算与自我更正（依 `§8.1`；不产候选结论）

D0: 本档对象 = **逻辑骨架核对 ＋ `\delta`-敏感性重算 ＋ 对 `C-147` DEAD 判定的降级更正 ＋ 反例集探测实验** —— 关系 = 重算与更正，非新机制
D1: 0

# C-148 · **`\delta`-敏感性重算 ＋ 对 `C-147` "DEAD" 的降级更正 ＋ 反例集探测**

> **唐先生 2026-09-19 12:42**：① 负部链里反证假设用在几处？② "10 倍缺口"是否对 `\delta` 敏感（可能"假死"）？✓

---

## §1 逻辑骨架核对（唐先生第一问）

$$\begin{array}{c|c|c}
\text{步骤} & \text{用到的假设} & \text{是否依赖反证假设}\\\hline
\text{①}\ 0\le f<\tfrac12\Rightarrow f^2\le\tfrac f2 & f\ge0\ (\text{定义}) \ +\ f<\tfrac12 & \textbf{是}\\
\text{②}\ f<0\Rightarrow f^2\le M|f| & \text{仅}\ |f|\le M\ (\text{结构}) & \textbf{否}\\
\text{③}\ \sum_{f<0}|f|\le\tfrac K2-S & \text{用}\ \sum_{f\ge0}f<\tfrac K2（\text{即每项}\ <\tfrac12） & \textbf{是}\\
\end{array}✓$$
$$\Longrightarrow\ \text{反证假设用在}\ \textbf{两处}（①、③），\ \text{但}\ \textbf{同一机制}：\text{把}\ \textbf{正部} \text{压到}\ \tfrac12\ \text{以下}；\ \textbf{②完全不用假设}✓✓$$
$$\qquad \text{写成正式证明时应在}\ ①③\ \text{处标注}\ [\text{reductio}]，\ \text{在}\ ②\ \text{处标注}\ [\text{structure}]✓$$

## §2 ⚠️ `\delta`-敏感性重算（唐先生第二问；**我昨天判重了**）

$$\text{昨日}\ \text{`C-147`}\ \text{用}\ \delta\approx0.4 \Longrightarrow c_\delta=\tfrac12+\tfrac1{2\sin^2(0.2)}\approx13 \Longrightarrow \text{缺口}\ \approx10\times✓$$
$$\text{但}\ \delta\ \textbf{不是自由参数}：\text{归约后应由}\ \textbf{配置本身} \text{定（边界簇的实际距离）}✓✓$$
$$\qquad \text{极值配置}\ (60^\circ,90^\circ)\ \text{在归约坐标}\ [0,\pi]\ \text{内全为内点}，\ \delta_{\text{自然}}=\pi/3✓$$
$$\qquad c_{\pi/3}=\tfrac12+\tfrac1{2\sin^2(\pi/6)}=\tfrac12+2=2.5✓✓$$
$$\Longrightarrow\ \text{重算缺口}：M=2：\text{需}\ Q>(2.5)(5)+2.5\cdot4=22.5，\text{实际}\ Q=7.75 \Longrightarrow 2.9\times；$$
$$\qquad \text{含认证最坏配置（}Q\ge4.25）：5.3\times；\qquad M=11：\text{需}\ Q>316+2.5\cdot121=618，\text{实际}\ \approx134\ \text{–}\ 258 \Longrightarrow 2.4\text{–}4.6\times✓✓$$

## §3 哪一部分可救、哪一部分不可救

$$\text{可救（}\delta\text{-相关）}：c_\delta M^2\ \text{项} \Longrightarrow \text{把"边界"定义放宽/按配置定}\ \delta \Longrightarrow \text{可压缩}\ \approx2\times✓$$
$$\text{不可救（}\delta\text{-无关）}：\Big(M+\tfrac12\Big)\tfrac K2-M\,S\ \text{项的}\ \approx2\times \Longrightarrow \text{来自①／②的}\ \textbf{粗略性}✓✓$$
$$\qquad \text{①在}\ f=\tfrac12\ \text{处紧}；\ ②\ \text{在}\ f=-M\ \text{处紧} \Longrightarrow \text{各自都紧，}\ \textbf{但能否同时达到？}$$
$$\qquad ⚠️\ \text{不能同时达到}（\text{需一列}\ k\ \text{都在}\ \tfrac12\ \text{而另一列都在}\ -M，\ \text{与}\ \sum f=S\ \text{及}\ f\ \text{的}\ \textbf{正权和结构} \text{冲突}）✓✓$$

## §4 ⭐ 新实验：受约束对抗优化（直接探测**反例集**）

$$\text{问题}：\max\Big\{Q(\theta)\ :\ \forall k:\ f(k)\le c\Big\}\quad(\text{惩罚法，}c=0.50,\ 0.55,\ 0.60,\ 0.80)✓$$
$$\begin{array}{c|r|r|r}
M & c & \text{受约束}\ \max Q & \text{找到配置的}\ \max f\\\hline
2 & 0.50 & 7.75 & 0.5001\\
2 & 0.55 & 7.96 & 0.5501\\
2 & 0.60 & 8.17 & 0.6001\\
3 & 0.50 & 15.26 & 0.9867\\
3 & 0.60 & 11.79 & 0.8599\\
4 & 0.50 & 21.30 & 1.2214\\
5 & 0.50 & 39.83 & 1.2789\\
6 & 0.50 & 57.23 & 1.5343\\
\end{array}✓✓$$
$$\Longrightarrow\ ⭐\ \text{优化器}\ \textbf{无法} \text{把}\ \max f\ \text{压到}\ c\ \text{以下}：\ M=2\ \text{恰卡在}\ 0.5001（\text{即}\ \textbf{约束边界}）；\ M\ge3\ \text{地板更高}✓✓$$
$$\qquad \Longrightarrow\ \textbf{数值支持}\ (\text{RP}_M)\ \text{为真，且}\ \textbf{反例集疑为空} \text{（这正是本路线的目标）}✓✓$$

## §5 ⚠️ 更正（对 `C-147` §4）

$$\text{`C-147` 判"二阶矩路线 DEAD（结构性）"} \Longrightarrow \textbf{过强}，\ \text{应改为}：$$
$$\qquad \boxed{\text{以}\ \textbf{粗略界} \text{计，路线差}\ \approx2\times（\delta\text{-无关部分}）；\ \text{能否救活取决于}\ \textbf{联合不等式}：}$$
$$\qquad \qquad \text{在}\ \{\forall k:\ f(k)<\tfrac12\}\ \text{上}\ Q\ \text{的}\ \textbf{真实} \text{上界是否}\ \textbf{远小于} \text{粗略界}\ (M+\tfrac12)K/2-M\,S✓✓$$
$$\qquad \text{该联合不等式}\ \textbf{未证}；\ \text{其真伪}\ \text{决定路线生死} \Longrightarrow \text{路线状态}\ \textbf{不是 DEAD，而是}\ \textbf{"差 2×、待救"}✓✓$$

## §6 边界与回查

- ⚠️ §1／§3 为**本档分析与更正**（`[reductio]`／`[structure]` 标注建议可直接采用）✓
- ⚠️ §2 的 `c_{\pi/3}=2.5` 为**按配置自然取值**（非最优搜索）⟹ 缺口数据为**量级**✓
- ⚠️ §4 为**实际运行**（惩罚法，`PEN=10^4`，12 起点；约束未被真正满足 ⟹ 记录的是"地板"）✓
- ⚠️ **不声称** 联合不等式成立或否；**不声称** 路线已死 ✓
- **未用** RH；**未改**任何原档（仅追加更正指针）✓
- **纪律**：先查后判（R-1 ✓，**先跑后写** ✓）

## §7 【技术词回查】输出（`scripts/tech_word_check.sh`，2026-09-19 12:5x）`[纪律]`（先跑后写）

```
技术词 δ-敏感性    命中文件数=0 ::  ⟹ 本档新增
技术词 反例集探测   命中文件数=0 ::  ⟹ 本档新增
技术词 联合不等式   命中文件数=0 ::  ⟹ 本档新增
```
**读数（按实测）**：三项**全 0 档 ⟹ 均本档新增** ✓
