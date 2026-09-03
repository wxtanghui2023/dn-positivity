# RCT 四层框架与 Zero-Position Bridge（2026-09-03 终态存档）

## 状态
唐先生主导的 RH 搜索（2026-08-23 起——多日——）到达精确终态：RCT 四层框架——前三层已解决——L4 为开放构造缺口（非已证不存在）。

## RCT 四层
- **L1 定向**：忠实表达实轴左右 ⟹ 线性序（二元定向 + 实轴桥 ⟹ 序——循环序逃不掉桥上的序——不可能三角 A+B+C——）
- **L2 算术序**：(Q,+,×) 中标准序可定义——四平方正锥：x>0 ⟺ x≠0 ∧ ∃a,b,c,d: x=a²+b²+c²+d²（Lagrange——每个正有理数是四平方和——）——"纯算术不能产生序"关闭
- **L3 ZFC 完备化**：(Q,<) 经 Dedekind/Cauchy（幂集——）规范构造 R——唯一——"纯算术不能得到 R"不是 RH 核心障碍
- **L4 Zero-Position Bridge**（唯一未知）：A_ar ⟹(Φ_new) X_A ⊂ R =? {γ: ζ(½+iγ)=0}——Φ 不以 ζ 为输入——不编码零点——不重标——有独立一致性定理

## 循环检测器（审计准则——非存在性证明）
合格候选必须分离两部分：
1. 独立 Φ（A_ar → X_A ⊂ R——不经 ζ——）
2. 独立一致性定理（X_A = Z_ζ——不经解析——）
经 ζ/显式公式/零点计数/解析延拓/已有零点数据的桥 = 循环 = 非新机制

## 关键校正（拒绝过度表述）
- γ_n ∉ Q **未证**——只作 Q-level definability obstruction（(Q,+,×) over Q 可定义集 ⊆ Q——）——不作 Zero-Position obstruction
- "没有已知定理" ≠ "不存在"——L4 是**开放构造性缺口**
- "已知数学无 Bridge" ≠ "RH 超出数学"——**第三种可能开放**：未识别的算术载体 A_ar（非 value functor/orientation/completion/spectral operator/explicit formula/flow/valuation/cohomology/regulator——九类已知接口全排除——但未知载体 + 独立对应定理的空间仍在）
- 已排除：大量已知接口范式——未排除：所有可能接口

## 探索判定史（2026-09-02 至 09-03 主要判死）
- ACD（受限半环等式蕴含深度——）死
- K_∞ 双生成兼容（兼容性定义性——）死
- AXD（τ=min(p,q)——平凡——）死
- ACPC 链（链稀疏退化——κ≈log(1+L₁t) 平凡——）死
- ASC（D_k 系统性反例——75% 负——非矩序列——）死
- Euclidean Cocycle（k=2 W_s(n,m)=F_s(nm)——乘积坍缩——）死
- [A,M] 交换子（单向增——上三角——幂零谱——）死
- affine prime dynamics（CRT 因子化 + 表示论塌缩——）死
- affine word zeta（词非自由——可解群——无闭词——）死
- [Π_Q, U_t]（加法格 Poisson——Q̂=Q 稠密——无素数幂权重——）死
- 谱流（终点=HP + 谱线守恒 + 非自适应——）死
- obstruction→J（Hilbert reciprocity 只给 χ↦χ^{-1}——|·| 需 Archimedean——）死
- DWD^{-1}=1−W（只给 FE 对称——{¼,¾} 反例——非 purity——）死
- purity 载体（Frobenius/HP/Weil——全封——）死
- value functor 四格（离散/Archimedean/p-adic/NA——无第四——）死
- 内在位置/定向（位置依附定位结构——定向⟹序——）死
- Pre-position（规范选择无先例——）开放

## 深层结论
γ_n 的身份由 ζ 定义——独立刻画 + 一致性定理在已知数学中不存在——但这是开放缺口（非 no-go）——L4 是"可以明确验尸的数学接口"

## 文件
本次探索脚本/文档：dn-project/scripts/（acpc_loop_test.py, asc_dk_test.py, euclid_trace_test.py, commutator_trace_test.py, affine_crt_test.py, domain_flow_test.py 等）——dn-project/docs/（各判死文档）
