已查地图（**先查后写**）：`C-380-18`（**E 条款注册** ✓✓）、`C-380-17`（**`F_3` = algebraic asset** ✓✓）、`C-380-13`（**sharp 封口** ✓✓）。回查见 §6 ✓

D0: 本档对象 = **C-380-19：`F_3` 的零杠杆／严格切削判定（注册）**，**零计算（登记 ✓）**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（九条 ✓✓）

$$\textbf{① ⭐ 关键纠正（本档核心）}✗✓：\text{在真正的四单位圆节点模型中}\ F_3\ \textbf{本来就是恒等式}✓✓ \Longrightarrow \ \boxed{\mathcal M_4 \subseteq \{F_3 = 0\}}✓✓$$
$$\qquad \Longrightarrow \ \text{若}\ \mathcal M_4\ \text{已是}\ E_0\ \text{的}\ \textbf{精确可行域定义}✓ \ \text{则}\ \boxed{\mathcal F_3 = \mathcal F_0}✓✓$$
$$\qquad \Longrightarrow \ \textbf{不能}把「把\ F_3 = 0\ \text{加进去后数值可行域没变化」}\ \textbf{称为发现}✗✓ \ —— \ \text{它本来就是模型的}\ \textbf{恒等约束}✓✓$$
$$\qquad \textbf{真正的问题必须改成}✓✓：\ \boxed{F_3\ \text{是否能从}\ E_0\ \textbf{原来使用的较弱 relaxation 中恢复出新的约束}？}✓✓$$
$$\textbf{② 因此 E 条款必须做 relaxation 对照}✓✓：\text{设}\ R_0 = \text{目前}\ E_0\ \textbf{实际使用的}、\ \textbf{尚未包含四节点单位圆完整结构} \text{的 relaxation}✓✓$$
$$\qquad \textbf{比较}✓✓：\ \sup_{x \in R_0}T(x)\quad \text{vs.} \quad \sup_{x \in R_0 \cap \{F_3 = 0\}}T(x)✓✓$$
$$\qquad \Longrightarrow \ \text{此时}\ F_3\ \textbf{不是} \text{「重新加入一个本来就成立的恒等式」}✗✓，\ \text{而是在测试}\ \boxed{F_3\ \text{是否给现有}\ E_0\ \text{relaxation 提供新的信息}？}✓✓$$
$$\textbf{③ 三种结果（精确区分）}✓✓：$$
$$\qquad \textbf{A — 真正切削}✓✓：\ \sup_{R_0 \cap \{F_3=0\}}T < \sup_{R_0}T✓ \ \textbf{且} \text{存在可审计的}\ \delta > 0\ \text{使}\ \boxed{T \le C - \delta}✓✓ \Longrightarrow \ \boxed{F_3 = \text{candidate obstruction}}✓✓$$
$$\qquad \textbf{B — } F_3\ \text{在极值点自动成立}✓✓：\ \operatorname{Argmax}_{R_0}T \subseteq \{F_3 = 0\}✓ \Longrightarrow \ \sup_{R_0 \cap \{F_3=0\}}T = \sup_{R_0}T✓✓$$
$$\qquad \qquad \Longrightarrow \ \boxed{F_3\ \text{对当前极值方向}\ \textbf{zero leverage}}✓✓（\textbf{不是}「失败实验」✗✓，\ \text{而是}\ \textbf{明确结论}✓✓）$$
$$\qquad \textbf{C — 更强的投影无效}✓✓：\ \pi_T(R_0) = \pi_T(R_0 \cap \{F_3 = 0\})✓（\pi_T(x) = T(x)✓） \Longrightarrow \ \boxed{F_3\ \text{对}\ E_0\ \text{的目标投影}\ \textbf{完全无效}}✓✓ \ —— \ \textbf{比 B 更强}✓✓$$
$$\textbf{④ ⭐⭐ 特别重要的 sanity check}✗✓：\textbf{必须避免} \text{把「真实四节点模型」}\ \textbf{误当} \text{relaxation}✗✓$$
$$\qquad \text{因}\ F_3 = 0\ \text{是从}\ |e_4| = 1\ \text{与 self-inversive 条件}\ \textbf{推出} \text{的}✓✓；\ \text{若}\ E_0\ \textbf{从一开始} \text{就明确要求}\ |e_4| = 1✓，\ e_3 = e_4\overline{e_1}✓$$
$$\qquad \qquad \Longrightarrow F_3\ \text{加不加入}\ \textbf{当然不会改变} \text{feasible set}✗✓ \Longrightarrow \ \textbf{此时正确结论不是}「F_3 没有 obstruction」✗✓，\ \text{而应是}✓✓：$$
$$\qquad \qquad \boxed{F_3\ \textbf{只是} \text{现有单位圆模型的一个}\ \textbf{派生恒等式}✓ \ —— \ \text{它}\ \textbf{没有} \text{提供超出母约束的新独立信息}}✓✓$$
$$\qquad \qquad \Longrightarrow \ \textbf{这个措辞差别}\ \textbf{很重要}✓✓$$
$$\textbf{⑤ } E_0\ \text{目标固定为唯一对象}✓✓：\text{设目标}\ T = T(p_1, \dots, p_6, \overline{p_1}, \dots, \overline{p_6})✓；\ \text{其余约束记为}\ \mathcal C_0✓；\ \mathcal F_0 = \mathcal M_4 \cap \mathcal C_0✓；\ \mathcal F_3 = \mathcal M_4 \cap \mathcal C_0 \cap \{F_3 = 0\}✓✓$$
$$\textbf{⑥ ⭐ 四项硬验收}✓✓：$$
$$\qquad \textbf{R1}✓✓（\textbf{现在最关键}）：\textbf{明确}\ E_0\ \text{当前 relaxation}\ R_0✓，\ \textbf{不能含糊}✗✓$$
$$\qquad \textbf{R2}✓：\text{证明}\ F_3\ \textbf{是否独立于}\ R_0\ \text{的现有约束}✓✓$$
$$\qquad \textbf{R3}✓：\text{比较}\ \sup_{R_0}T\ \text{与}\ \sup_{R_0 \cap \{F_3=0\}}T✓✓$$
$$\qquad \textbf{R4}✓✓：\text{若无严格下降}✓，\ \textbf{区分}\ \text{zero leverage／projection-equivalent／redundant}✓✓，\ \textbf{不能}笼统写 FAIL✗✓$$
$$\qquad \Longrightarrow \ \textbf{若没有把}\ E_0\ \text{到底在哪个 relaxation 上求极值写清楚}✗，\ \text{任何「}\ F_3\ \text{切掉了多少」的数值都}\ \textbf{没有审计意义}✗✓$$
$$\textbf{⑦ ⭐ 决策树}✓✓：$$
$$\qquad \textbf{若 A}✓：\ \Delta_3 := \sup_{R_0}T - \sup_{R_0 \cap \{F_3=0\}}T > 0✓ \Longrightarrow \ \text{继续}\ C\text{-}380\text{-}20 = \textbf{严格 gap 的解析证明}✓✓$$
$$\qquad \textbf{若 B}✓✓：\ \boxed{F_3\ \textbf{DOWNRANK — zero leverage}}✓✓ \ \textbf{并且不要开}\ F_4✗✓$$
$$\qquad \textbf{若 C}✓✓：\ \boxed{\textbf{SELF-INVERSIVE LOW-DEGREE IDENTITY FAMILY} \longrightarrow \textbf{GAP}}✓✓ \Longrightarrow \textbf{可以直接停止这整个支线}✓✓$$
$$\textbf{⑧ } F_4\ \textbf{暂不碰}✓✓：\text{只有}\ \textbf{证明}\ F_3\ \textbf{有 leverage}\ \text{后}\ F_4, F_5, \dots\ \text{才有意义}✓✓$$
$$\qquad \textbf{否则} \text{很容易重新进入已明确要避免的模式}✗✓：\ \text{非线性恒等式} \to \text{更高阶非线性恒等式} \to \text{越来越漂亮} \to \text{对}\ E_0\ \text{没有切削}✗✓$$
$$\textbf{⑨ 问题重述（本档锁死）}✓✓：\ \boxed{\text{现在真正需要回答的不是「四节点还有什么代数关系？」，\ 而是「四节点代数关系能否改变}\ E_0\ \text{的最优值？」}}✓✓$$

## §1 与既有封口的关系（✓✓）

$$\textbf{已封口}✓✓：C\text{-}380\text{-}12\（\text{等权求和}✓）、C\text{-}380\text{-}13\（\text{单一正三角对偶，sharp}\ 6✓✓）$$
$$\textbf{本档界限}✓✓：\text{R1 未写清}\ \Longrightarrow \ \textbf{不得}进入数值比较✗✓$$

## §2 账本（✓✓）

| 项目 ✓ | 状态 ✓ |
|---|---|
| `C\text{-}380\text{-}13` ✓ | **CLOSED（sharp）** ✓✓ |
| `C\text{-}380\text{-}17` ✓ | **`F_3` = algebraic asset** ✓✓ |
| `C\text{-}380\text{-}18` ✓ | **E 条款注册（表述被本档纠正）** ✗✓ |
| **`C\text{-}380\text{-}19`** ✓ | **NEXT ← 本档注册（R1–R4）** ✓✓ |
| `F_4` ✓ | **封存** ✗✓ |
| `E_0` ✓ | **OPEN** ✓ |
| Bridge A ✓ | **OPEN** ✓ |
| `H = \varnothing` ✓ | **OPEN** ✓ |

## §3 边界（✓✓）

$$\textbf{不得}写成✗：F_3\ \text{已是 obstruction}✗✓；\ F_3\ \text{无 obstruction}✗✓（\textbf{正确}：\text{派生恒等式}✓）；\ \text{可行域已缩小}✗；\ E_0 = \varnothing\ \text{已证}✗✓$$
$$\textbf{诚实标注}⚠️✓：\text{本档}\ \textbf{零计算}✓（注册✓）；\ R_0\ \textbf{未写清}✗✓；\ \text{四结果}\ \textbf{均未取得}✗✓$$

## §4 边界（✓✓）

$$\textbf{零计算}\ ✗（注册档✓）；\ D1 = 0✓；\ \text{未改他档正本}✓；\ \text{未动 v4}✗；\ C\text{-}181\ \text{的}\ u \le 5\ \text{仍}\ \textbf{GAP-A}✓✓$$

## §5 边界（✓✓）

$$\textbf{纪律}✓✓：\textbf{R1 未过不得开数值}✗✓；\ \textbf{R4 不得笼统写 FAIL}✗✓；\ F_4\ \textbf{封存}✓✓$$

## §6 【技术词回查】输出（**先跑后写**✓）＋ 边界

```
技术词 松弛对照     命中文件数=0    :: 
技术词 派生恒等式  命中文件数=0    :: 
技术词 零杠杆判定  命中文件数=1    :: ./C3818-F3-feasible-set-cut-test-for-E0.md 
```
- 运行记录 ✓：`scripts/tech_word_check.sh` ✓
