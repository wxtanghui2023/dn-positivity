# D1：prime-history composition 审计（**纯推导，未计算**）

**依据**：唐先生 §20 的两个审计问题｜**约束**：不计算；不输入 $1/2$；不构造模型｜**L2 未动**
**标注**：【推导】= 本文件给出论证；【引用】= 外部标准结果，本轮未验证；【已核验】= 本项目早前轮次已算过

---

## §1 Q1 的第一半：**Euler 化是唯一分解的推论**，不是建模选择【推导】
若尺度是一个真正的 $(\mathbb N,\times)$ 作用：$S_mS_n=S_{mn}$，则由唯一分解
$$S_n=S_{\prod p^{k_p}}=\prod_p S_{p^{k_p}}\qquad\Longrightarrow\ \textbf{必然 Euler 化}$$
$$\boxed{\text{故"避免 Euler 化"}\iff\text{尺度赋值必须依赖【路径】而非终点（非平坦函子）}\iff\Omega\neq1}$$
（与唐先生 §4/§6 一致；此处把"形式"变成"判据"）

## §2 Q1 的第二半：**非交换算子不够**（把 §5/§7 升为命题）【推导】
若基路径范畴仍**交换**（如生成元 $\times p,\times q$ 在基层面交换），则唯一可能的 defect 是 $[A_p,A_q]$ ⟹
整体仍是 $\prod_p(1-A_pp^{-s})^{-1}$ 型**【矩阵 Euler 积】** ⟹ 落回 Dirichlet 类（§14 判死）✓
$$\boxed{\text{关键不在算子层，而在【基层面】的非交换}}$$

## §3 加法×乘法是天然的非交换基 —— 但它**可解**【推导】
$$T_a:x\mapsto x+a,\qquad M_p:x\mapsto px;\qquad T_aM_p-M_pT_a=\text{平移 by }a(1-p)$$
$$\boxed{\text{defect 是【平移】= 阿贝尔}} \Longrightarrow \text{生成群}=\mathrm{Aff}(\mathbb Z)=\mathbb Z\rtimes\mathbb Z^\times\ \text{【亚交换/可解】}$$
（导群 = 平移群（阿贝尔）⟹ 一切高阶 commutator 退化）
$$\boxed{\Longrightarrow\ \text{add}\times\text{mult 路径给出的 defect 是【下中心/可解】的 ⟹ 正是 §7 的陷阱，且在此路线上【不可回避】}}$$
【已核验·本项目】同族结论："仿射/线性 ⟹ $1/2$ 可插入"；"算子复合 ⟹ associator $\equiv0$"

## §4 于是 Q1 收紧为：存在【非可解】的算术路径范畴吗？【推导】
```
天然候选只有两类：
  · Galois 侧：非可解 ✓（但解析影子是 L-函数 ⟹ §14 判死 ✗）
  · 模侧 PSL_2(Z)：非可解 ✓（但其中心对合【就是】FE 的 s↔1−s）
      ⟹ 唐先生 §17 要求"不能从 ζ 的 FE 借来"在此路线上做不到；且 FE 族在本项目已判死 ✗
⟹ **在已审天然类中：不存在不 Eulerize 的 prime-history composition**
   （边界：这是"本次枚举范围内"的结论，非全称不可能）
```

## §5 Q2：什么样的 Ext 能逃出 §14（判据）【推导】
$$\boxed{\text{Ext 必须是【非阿贝尔 }H^1\text{ 的 torsor/可解性陈述】，而不是阿贝尔 }H^2\text{ 的类}}$$
（后者 ⟹ determinant / L-函数 ⟹ §14 判死 ✓）
**但**：即便取非阿贝尔 $H^1$，算术中这类 obstruction 通常由 **Poitou–Tate 型对偶**控制，其解析影子仍落在 L-值上 ⟹ 仍回 §14 ✗
$$\boxed{\Longrightarrow\ \text{逃出 §14 需"其 obstruction 不由带 L-系数对偶定理控制"——目前【无候选】}}$$
（属结构性论证，非定理）

## §6 对你 §9（自对偶 ⟹ $1/2$ 为不动点）的**硬约束**【引用 + 推导】
该机制的**原型正是函数方程**：$\Lambda(s)=\varepsilon\Lambda(1-s)$ ⟹ 中心线 $\Re s=\tfrac12$ **无条件出现**（ζ 自身如此）
**但**【引用，本轮未验证】：存在**具有函数方程却被证明有离轴零点**的经典对象（Epstein $\zeta$ 的 Potter–Titchmarsh 现象）
$$\boxed{\Longrightarrow\ \text{"自对偶}\Rightarrow\text{零点在线上"在一般情况下【是假的】}\ \Longrightarrow\ \text{§9 机制单独【不足】}}$$
任何此类模型必须**显式排除 Epstein 型现象** —— 这是很硬的要求
（精确表述：FE 给的是**临界线**（无条件），不是**零点位置**；这正是 RH 难点所在）

## §7 方法论警示（按本项目已注册纪律）
```
唐先生 §16 的 𝔖_r = (X_r, T_r, Ω_r)、Ω_{r+1} = F(T_r, Ω_r, X_r) 目前是【定义模式】，不是【被生成的对象】
⟹ 与本项目已注册反模式同形（"名字生成 → 漂亮定义 → 结构塌缩"）
⟹ GPS 第一门（G1 原生产生）问"什么【强制】了这个定义"——当前答案是"没有"
   建议：构造之前先回答这一条
```

## §8 综合（对应唐先生 §20）
```
Q1：在已审天然类中 = 【否】
    （Euler 化由唯一分解强制；add×mult 的 defect 可解；Galois/模侧分别落回 L-函数/FE 封闭类）
Q2：逃出 §14 的判据已给出（非阿贝尔 H^1 torsor 且不由 L-系数对偶控制），但【无候选】
⟹ 按 §20 的判死条件：**"任何 composition → Euler/trace/determinant/explicit formula"在已审类中成立**
   ⟹ 这条 arithmetic dynamics 路线【拟判死】
⟹ 保留一条：若出现【非可解基范畴 + 非 L-系数对偶】的对象，则属死路地图【未覆盖区】
```
**边界**：以上为"已审天然类"内的结论；未枚举穷尽，故不写成全称不可能定理
