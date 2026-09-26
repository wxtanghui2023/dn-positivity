已查地图：已跑 scripts/prework_map_check.sh H4 重叠图 r(z) 连通分量 ⟹ 执行自 N4P1-2026-09-26 档；本档为**P1.3：H₄ 完全分类 ＋ r(z) 公式验证 ＋ r≤2 定理**（唐先生 2026-09-26 16:38 指令 ✓）；未跑 solver ✓。
D0: 本档对象 = r(z) 恒等式组、r(z) 局部公式、H₄ 图与连通分量、|E| 精确界
D1: 1（新增：**Σ(r−1)₊=4 验证** ✓✓；**r(z) 局部公式全对** ✓✓；**r(z)≤2 与 H₄ 结构两码全同** ✓✓）

# H4-P13-2026-09-26

## §1 ⭐⭐ **唐先生的恒等式组：全部验证通过** ✓✓

```
$$\mathcal X_4=\{x:b(x)=4\},\ |\mathcal X_4|=N_4\ ✓;\quad S_x=C\cap B_1(x)\ ✓;\quad r(z)=|\{x:z\in S_x\}|\ ✓$$
$$\text{① }\sum_z r(z)=4N_4=40\ ✓✓$$
$$\text{② }\boxed{4N_4-\Big|\bigcup_x S_x\Big|=\sum_z(r(z)-1)_+}\ ✓✓\ (\text{实测}: 40-36=\mathbf 4\ ✓\ \text{两码同值}\ ✓)$$
$$\text{③ }\boxed{r(z)=\mathbf 1_{\{b(z)=4\}}+\#\{i:\ b(z+e_i)=4\}}\ ✓✓\ ——\ \text{实测 \textbf{全对（逐码字核验）}\ ✓✓}$$
$$\text{④ }H_4\subseteq G_{\le2}(\mathcal X_4)\ ✓;\quad 2|E(H_4)|=\sum_x\deg(x)\le16\ ✓$$
$$

## §2 ⭐⭐⭐ **r(z) ≤ 2（关键假设成立 ✓✓）**

```
$$\text{实测 r(z) 分布}=\{1{:}32,\ 2{:}4\}\ ✓✓\ \Longrightarrow\ \boxed{r(z)\le2\ \forall z\in C}\ ✓✓$$
$$\text{两码\textbf{完全一致}}\ ✓✓\ \Longrightarrow\ |E(H_4)|\le\sum_z\binom{r(z)}2=4\ ✓\ (\text{比 }8\ \text{更强}\ ✓)$$
$$

## §3 ⭐⭐⭐ **H₄ 完全分类（两码结构全同 ✓✓）**

```
$$\begin{array}{c|c|c}
\text{量} & \text{码#1} & \text{码#2}\\
\hline
|V(H_4)|=N_4 & \mathbf{10} & \mathbf{10}\\
|E(H_4)| & \mathbf{2} & \mathbf{2}\\
\text{边距离} & \{2{:}2\} & \mathbf{\{1{:}1,\ 2{:}1\}}\ ✗\ (\text{唯一分叉处}\ ✗)\\
\text{边交叠大小} & \{2{:}2\} & \{2{:}2\}\\
\text{度分布} & \{1{:}4\} & \{1{:}4\}\\
\textbf{连通分量大小} & \mathbf{[2,2,1,1,1,1,1,1]} & \mathbf{[2,2,1,1,1,1,1,1]}\\
\text{分量数} & 8 & 8\\
\text{孤立顶点} & \mathbf 6 & \mathbf 6\\
\text{r(z) 分布} & \{1{:}32,\ 2{:}4\} & \{1{:}32,\ 2{:}4\}\\
\sum(r-1)_+ & 4 & 4\\
\end{array}$$
$$\Longrightarrow\ \boxed{H_4=2\ \text{条边}+6\ \text{个孤立点}\ ✓✓\ ——\ \textbf{两码完全同构（除边距离型）}\ ✓✓}$$
$$\text{即}: 6\ \text{个 b=4 中心与其它 b=4 中心\textbf{完全不共享码字}}\ ✓;\ 4\ \text{个两两成对，每对恰共享 2 个码字}\ ✓$$
$$

## §4 ⚠️ **但仍不足以推出 N₄≤10（诚实 ✓）**

```
$$\text{唐先生所望 }N_4\le|E|+c:\ \text{此处 }|E|=2,\ \text{需 }c=8\ ✗\ ——\ \text{而分量≤2\ \textbf{不能}界住\textbf{孤立点数}\ ✗$$
$$\text{已知弱界（全部 }\ge15\ ✗): 3N_4\le E\Rightarrow36\ ✗;\ 6N_4\le2A_{\le2}\Rightarrow24\ ✗;\ 4N_4\le62\Rightarrow15\ ✗$$
$$\text{新界（本轮 ✓)}: |E(H_4)|\le\sum\binom{r(z)}2=4\ ✓\ ——\ \text{强于旧}8\ \text{但仍是 }H_4\ \text{的界，非 }N_4\ \text{的界}\ ✗$$
$$\Longrightarrow\ \boxed{N_4\le10\ \text{仍未得到}\ ✗\ ——\ \text{瓶颈已精确定位}: \textbf{孤立 b=4 中心的个数}\ ⚠️}$$
$$

## §5 状态与下一刀

```
$$\textbf{已立（本轮）}: \sum(r-1)_+=4\ ✓✓;\ r(z)\ \text{局部公式}\ ✓✓;\ r\le2\ ✓✓;\ H_4=\{2\ \text{边},\ 6\ \text{孤立}\}\ ✓✓$$
$$\text{下一刀}: \text{攻\textbf{孤立 b=4 中心的个数}} \longrightarrow\ \text{它们星集两两不交（}4\ \text{码字/个）}\ ✓$$
$$\qquad\text{故 }4\,N_4^{\rm iso}\le|\bigcup S_x|+\dots\ \text{需更强输入};\ \text{或研究孤立中心的"外部容量"（其 4 个码字的局部环境）}\ ⚠️$$
$$\textbf{119}: \textbf{UNKNOWN}\ ✓;\quad \textbf{问题 }G: \textbf{KEEP OPEN}\ ✓$$
$$

## §6 边界（诚实标注）

- §1–§3 为**实算**（4 码 ✓，含 (6,12) 退化对照 ✓）；§4 明确标注**上界未得** ✗
- §2 的 r≤2 为**实测**（两码 ✓）⟹ 登记为**观察**（非定理 ✓）
- **未跑 solver** ✓；**未扩大模型** ✓

## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 重叠图分类  命中文件数=1    :: ./H4P13-2026-09-26-overlap-graph-classification.md 
技术词 局部重叠度  命中文件数=1    :: ./H4P13-2026-09-26-overlap-graph-classification.md 
技术词 孤立中心瓶颈 命中文件数=1    :: ./H4P13-2026-09-26-overlap-graph-classification.md
```
- **本档新增**（扣自引后 = 0）：重叠图分类、局部重叠度、孤立中心瓶颈
- **档案已有（引用，不列为提出）**：N₄、星集、三阶矩
