# CALIBRATE-K9-b（2026-09-29）—— **$r{=}1$ 第二层仍无条件可行；线性局部账目层\ \textbf{结构封顶}于 $52$；转入有限类型层**

> **性质**：**能力校准链（B 之首刀）**——**不占 C 号** ✓；**不作方向性决策** ✗；空间 B ✓
> **时间**：2026-09-29 14:4x ✓
> **唐先生令**：执行 B；先纠正"任何 LP"之越界表述；第一刀只做 $r{=}1,\ M{=}57..61$ ✓

**已查地图**：`CALIBRATE-K9`（纤维-LP 族）／`DERIVE-107*`✓

D0: 本档对象 ＝ **档案已有**（纤维分解／multiplicity profile——皆经典 ✓）
D1: 0（产出＝**一逻辑纠正之接受 ＋ 一实验 ＋ 一结构性封顶之证明** ⚠️✓）

---

## §0 结论（先给）

$$\boxed{\text{① ✓ 接受纠正}:\ \text{精确表述应为「\textbf{这一族一阶纤维 LP} 只给球界 }52\text{」};\ \textbf{非}\ \text{"任何 LP 皆不能到 }62\text{"}}$$
$$\boxed{\text{② ✓ 实验}:\ r{=}1\ \text{第二层（multiplicity profile）LP}:\ M{=}52\dots62\ \textbf{全部可行}\ (11/11)}$$
$$\boxed{\text{③ ✓✓ 且非技术不足，而是\ \textbf{结构封顶}}:\ 256=|N_1(A)|+|B|-|\cap|\le|N_1(A)|+b;\ \text{用精确 }|N_1(A)|\ \textbf{只会更弱}}$$
$$\boxed{\text{④ ⟹ 按你协议}:\ \text{线性局部账目层\ \textbf{封死}};\ \text{进入\ \textbf{有限类型枚举层}}}$$

## §1 ① 逻辑纠正（**✓ 接受**）

$$\text{我已证者}:\ \text{固定 }r\ \text{之纤维一阶 LP}\ \Longrightarrow\ 10M\ge512\Longrightarrow M\ge52\ (\text{与 }r\ \text{无关})$$
$$\text{我已证者\ \textbf{不包括}}:\ \text{"}57\to62\ \text{不可能来自任何 LP／线性不等式"}✗\ (\text{越界之表述，撤回})$$
$$\textbf{正确版}:\ \boxed{\text{57\to62 \textbf{不能仅}靠一阶纤维 LP 得到}}\ ✓$$
$$\text{更强的 LP 可编码整数性／子空间兼容／不等价分支／局部结构}\ \Longrightarrow\ \text{须查明文献 LP 剪掉了什么、枚举树之状态变量为何}✓$$

## §2 ② $r{=}1$ 之精确结构（**✓ 精确重述**）

$$\mathbb F_2^9=\mathbb F_2^8\times\mathbb F_2;\quad A=\{y:(y,0)\in C\},\ B=\{y:(y,1)\in C\};\ |A|{=}a,\ |B|{=}b,\ a{+}b{=}M$$
$$\text{覆盖}\iff\boxed{N_1(A)\cup B=\mathbb F_2^8\ \wedge\ N_1(B)\cup A=\mathbb F_2^8}\qquad(\text{8-cube 中每字覆盖 }9\ \text{点})✓$$
$$\text{第一层}:\ 256\le9a+b,\ 256\le a+9b\ \Longrightarrow\ M\ge51.2\Rightarrow52$$

## §3 ③ 第二层实验（**✓ 11/11 可行**）

$$\text{变量}:\ a,b,T_0^{(j)},T_1^{(j)}\ (j{=}1..9);\quad \text{约束}:\ a{+}b{=}M;\ \Sigma_jT^{(j)}{=}256;\ T^{(0)}{=}0;\ \Sigma_j jT_0^{(j)}{=}9a{+}b;\ \Sigma_j jT_1^{(j)}{=}9b{+}a$$
| $M$ | $52$ | $53$ | $54$ | $55$ | $56$ | $57$ | $58$ | $59$ | $60$ | $61$ | $62$ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 可行 | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y | Y |

$$\therefore\ \text{加入 fiber 内 multiplicity profile \textbf{不产生任何 gap}}✓$$
$$\text{（二阶一致性}\ \Sigma_j\tbinom j2T^{(j)}=\text{pair-overlap}\ \text{依赖码字距离结构，}\textbf{不可闭式给出}}✓$$

## §4 ④ 结构性封顶（**✓✓ 本档最重要**）

$$256=|N_1(A)\cup B|=|N_1(A)|+|B|-|N_1(A)\cap B|\ \le\ |N_1(A)|+b$$
$$\text{而恒有 }|N_1(A)|\le9a\ (\text{trivial});\quad \text{若用\ \textbf{精确} }|N_1(A)|<9a\ \text{替代},\ \text{则 }b\ \text{之下界\ \textbf{变小}}\Longrightarrow \textbf{更弱}✗$$
$$\therefore\ \boxed{\text{该层可用的\ \textbf{最强}界就是 }9a\Longrightarrow\text{球界 }52}\ ——\ \textbf{方向性论证，非技术不足}✓✓$$
$$\text{（推广至 }r>1:\ \text{求和论证 }\Sigma_u[(10-r)N_u+\Sigma_{v\sim u}N_v]=10M\ \text{恒给 }52✓）$$

## §5 下一步：有限类型枚举层（**按你之执行顺序**）

$$\boxed{\text{fiber LP}\to\text{local multiplicity LP}\to\boxed{\text{finite local types}}\to\text{compatibility enumeration}\to M\le61\ \text{之不可行性}}$$
$$\text{定义局部类型}:\ \tau(F)=(\text{weight dist},\ \text{internal distances},\ \text{boundary coverage},\ \text{multiplicity profile})$$
$$\text{问题转化为}:\ \text{枚举有限个 }\tau\ +\ \text{LP 剪枝}\ +\ \text{fiber compatibility}✓$$
$$\textbf{双侧 benchmark（须分开）}:\quad \text{上界 }62\le K(9,1)\le\mathbf{66}\ (\text{当前我方});\qquad \text{下界 }M\le61\Longrightarrow\bot\ (\text{待证})$$
| 方法 | 当前上界 |
|---|---|
| remove-and-repair | $66$ |
| 下一版结构化搜索 | 待测 |
| 目标 | $\mathbf{62}$ |

## §6 技术词回查（**先跑后写 ✓**）

```
$ bash scripts/tech_word_check.sh "线性局部账目层封死" "方向性封顶" "有限类型层入口"
技术词 线性局部账目层封死  命中文件数=0    ::
技术词 方向性封顶      命中文件数=0    ::
技术词 有限类型层入口    命中文件数=0    ::
```

## §7 边界（硬 ✓）

- **LP 实验（$M{=}52..62$ 全量）＋ 方向性论证 ＋ 精确重述** ✓；**不占 C 号** ✓；**未用 SAT/CP-SAT** ✓
- **撤回**越界表述（"任何 LP"）✓；**不主张** $K(9,1)$ 之值有疑 ✗
