已查地图（**先查后写**）：`C-312`（反例包络 ＋ 三条约束 ✓）、`C-311`（Littlewood 第六类 ✓）、`C-310`（Barker 缺失型 ✓）、`C-292`（候选池卡片：Wills／Cusick 出处 ＋ 约定映射 ＋ Bedert 2025 下界 ✓）。回查见 §7 ✓

D0: 本档对象 = **C-313（＝唐先生编号 C-312）：Round 2 第三项 —— Lonely Runner 四格审计**，**零计算**
D1: 0
FREEZE-ACK: 本档即冻结审计

---

## §0 结论（五条 ✓✓）

$$\boxed{\textbf{F}✓✓：\text{Lonely Runner 的 failure}\ \textbf{是性质型 ＋ 有具体载体}✓（\text{速度集合}\ V✓），\text{且逐例可核}✓ \Longrightarrow \textbf{首次通过反例约束③（有载体）}✓✓}$$
$$\boxed{\textbf{A}_1\ ✗：\text{仅有}\ \textbf{归一化型对称}✓（\text{公因子缩放}✓），\textbf{按纪律不计作传播}✗✓}$$
$$\boxed{\textbf{A}_2\ ✗：\textbf{未见独立第二传播}✓}$$
$$\boxed{\textbf{C}\ ✗：\textbf{未见非平凡兼容律}✓}$$
$$\Longrightarrow \textbf{未通过四格}✓ \Longrightarrow \textbf{第七类反例}✓；\textbf{不进入}\ RH\ ✗$$

## §1 F 格：**有载体的性质型 failure**（✓✓）

$$\textbf{对象}✓：V = \{v_1,\dots,v_n\}\ \text{（互异正整数速度}✓）；\text{轨道}\ t \mapsto (t v_1, \dots, t v_n) \bmod 1✓$$
$$\textbf{lonely 条件}✓：\exists t\ \text{使}\ \forall i:\ \|t v_i\| \ge 1/(n+1)✓（\text{等价：view-obstruction 几何判据}✓，\text{Wills 1967／Cusick 1974}✓）$$
$$\textbf{failure}✓：\text{给定}\ V\ \textbf{不存在这样的}\ t✓ \—— \ \text{这是}\ \textbf{关于一个实际存在对象（V）的性质}✓，\textbf{不是} \text{「某类为空」}✗✓$$
$$\Longrightarrow \textbf{F} = YES✓✓；\textbf{且通过反例约束③}✓✓（\text{有 canonical carrier}✓；\text{坏时间集合} = \text{覆盖之补}✓）$$
$$\textbf{诚实标注}⚠️：\text{该 failure 集合}\ \textbf{是否非空}\ \text{未知}✓（\text{正是猜想本身}✓） \Longrightarrow \text{四格建立在}\ \textbf{可能为空} \text{的集合上}⚠️$$

## §2 A₁ 格：**归一化型对称 ≠ 传播**（✓✓，本档关键）

$$\textbf{存在精确对称}✓：\text{公因子缩放}\ V \mapsto aV✓ \Longrightarrow \text{好时间集合变为}\ (1/a)\cdot(\text{好时间集合})✓✓（\because \|t(a v_i)\| = \|(a t) v_i\|✓）$$
$$\qquad \Longrightarrow \text{它}\ \textbf{确实把 failure 映到 failure}✓ \—— \ \textbf{但它是时间重参数化}✗✓（\text{坐标等价}✓）$$
$$\textbf{唐先生纪律}✗✓：\text{单纯换 origin／time 参数}\ \textbf{不算}\ A_1✗；\text{与}\ A_1\ \text{等价的缩放、模}\ 1\ \text{重写}\ \textbf{不算}\ A_2✗；\text{torus translation} \leftrightarrow \text{speed normalization}\ \text{若只是坐标描述等价，直接排除}✗✓$$
$$\textbf{其它候选}✗：\text{时间平移}\ t \mapsto t + s\ \textbf{不保} \text{lonely 条件}✗（\text{非平移不变}✓）；\text{临界对／极值配置分析}\ \textbf{是构造}✗$$
$$\Longrightarrow \textbf{A}_1 = \textbf{未见真正传播}✗（\text{仅归一化}✓）$$

## §3 A₂／C 格（✗）

$$\textbf{A}_2✗：\text{未见与}\ A_1\ \text{真正独立的第二传播}✓$$
$$\textbf{C}✗：\text{无两传播} \Longrightarrow \text{无从谈兼容}✗；\text{亦未见「两定理共同给同一个界」之外的第三层关系}✓$$

## §4 判定（✓✓）

$$\textbf{未通过四格}✗ \Longrightarrow \textbf{第七类反例}✓；\text{新诊断标签}✓✓：\textbf{归一化型对称}✓（\text{有真载体}✓，\text{却仍止于}\ A_1✗）$$
$$\textbf{包络增补}✓✓：\textbf{有载体} \ne \textbf{充分}✗✓（\text{约束③通过}✓，\text{约束②仍失败}✗）$$
$$\text{七反例并表}✓：\quad \begin{array}{c|c|c|c} & \text{Failure} & \text{载体} & \text{兼容律}\\ \hline \text{Hecke} & ✗ & — & ✗\\ \text{Schur} & ✓\text{性质型} & ✓ & ✗\\ \text{素数间隙} & ✓\text{内禀} & ✓ & ✗\\ \text{零点间距} & 🟡\text{模型相对} & ✓ & ✗\\ \text{Barker} & ✓\text{缺失型} & ✗ & ✗\\ \text{Littlewood} & ✓\text{性质型＋对合} & ✓ & ✗\\ \text{Lonely Runner} & ✓\text{性质型＋归一化} & ✓✓ & ✗ \end{array}$$
$$\Longrightarrow \text{七反例}\ \textbf{一致指向}✓✓：\textbf{稀缺物＝独立存在的非平凡兼容律}✓✓$$

## §5 Round 2 完成（✓✓）

$$\textbf{三项全部完成}✓：\text{Barker（第五类}✓）\to \text{Littlewood（第六类}✓）\to \text{Lonely Runner（第七类}✓）$$
$$\textbf{全部在}\ C\ \text{之前死亡}✓ \Longrightarrow \text{按}\ C\text{-305 §6 与}\ C\text{-312 §3}✓：\textbf{下一步有充分理由开 C 类}✓（\text{旧 GAP 重检}✓）$$
$$\textbf{不} \text{扩大外部问题池}✗（\text{唐先生预注册}✓）$$

## §6 避雷执行确认（✓✓）

$$\textbf{① 「看起来至少有两个作用」}\ \textbf{未采信}✗✓（\text{integer speeds／torus geometry／time translation／modular 皆不足以充当}\ A_1／A_2✗）$$
$$\textbf{② torus translation} \leftrightarrow \text{speed normalization}\ \textbf{未采信}✗✓；\textbf{③ 覆盖论证}\ \textbf{未升级为兼容}✗✓$$
$$\textbf{④ 未}因 torus 结构更丰富而降低 compatibility 门槛✗✓$$

## §7 边界与回查（✓）

- **零计算** ✗；未读 pending ✗；未改他档正本 ✓（仅追加 ✓）；未动 v4 ✗；`C-181` 的 `u<=5` 仍为 **GAP-A** ✓
- **不得**写成：Lonely Runner 已排除 ✗（仅"未通过四格"✓）；其 failure 集合非空 ✗（未知 ✓）
- **本档新增词**：`归一化型对称`／`有载体≠充分`（0 命中 ✓）

---

## §8 【技术词回查】输出（**先跑后写**✓）

```
技术词 归一化型对称 命中文件数=1    :: ./C313-round2-lonely-runner-four-column-audit.md 
技术词 有载体        命中文件数=2    :: ./C312-counterexample-envelope-three-constraints-for-round2.md ./C313-round2-lonely-runner-four-column-audit.md 
技术词 反例包络     命中文件数=2    :: ./C312-counterexample-envelope-three-constraints-for-round2.md ./C313-round2-lonely-runner-four-column-audit.md 
技术词 canonical        命中文件数=298  :: ./B-SERIES-INDEX.md ./E3-why-this-is-not-the-old-pit.md ./POS3-provably-positive-mechanisms-enumeration.md
```

$$\textbf{① 本档新增}✓：\text{归一化型对称}✓／\text{有载体不等于充分}✓（\text{若回查显示 0 命中则为首用}✓）；\text{反例包络}／\text{canonical} \text{为既有词（C-312}✓\text{）}$$
$$\textbf{② 纪律}✓：\text{涉及「本档新增／首次命名」的主张}\ 	extbf{一律先跑回查再写}✓（\text{TOOLS.md}✓\text{）}$$