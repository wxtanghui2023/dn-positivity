已查地图：命中（`LJCR-A5-difference-sets-source-check`）⟹ 判据重审，不开新案
D0: 本档对象 = **判死清单重审（"已做出成果" vs "仅在跑"）** ＋ **误杀清单** ＋ **复活集** ＋ 首攻目标
D1: 0（重审型，零计算）
[REVIEW]

# **判死重审：`achieved` vs `occupied`**

## §1 重审表

```
$$\begin{array}{c|l|l|l}
\text{候选}&\text{我判死的理由}&\text{实际性质}&\text{修正}\\\hline
S1\ \text{诱导饱和 }C_{2t}& \text{2026-08 预印本已构造全部偶环}&\boxed{\text{已做出成果}}&\checkmark\ \text{正杀}\\
K2\ \text{多色三角 Ramsey（渐近）}& \text{2026 AI 证明超指数下界}&\boxed{\text{已做出成果（渐近层）}}&\checkmark\ \text{正杀};\ \text{但}\boxed{\text{小参数恰值层未做出}}\Rightarrow\text{应复活}\\
Mt07\ n\le38\ \text{诸格}& \text{Boza 2026 已解 8 个未知值}&\boxed{\text{已做出成果}}&\checkmark\ \text{正杀（同格）}\\
C06\ \text{已分类之格}& \text{5983 类等已完成}&\boxed{\text{已做出成果}}&\checkmark\ \text{正杀（同格）}\\
\boxed{X1}\ K(10,1)\in[107,120]& \text{三条路线＋在跑 ILP 项目}&\boxed{\text{仅在跑，结果未做出}}&\boxed{\times\ \text{误杀}}\\
\boxed{R(3,10)\in\{40,41\}}& \text{战场拥挤＋纯搜索}&\boxed{\text{未做出}}&\boxed{\times\ \text{误杀}}\\
S2\ A110000\ \text{精确小值}& \text{落入 }p(m,n)\ \text{框架}&\boxed{\text{未做出（仅上界）}}&\boxed{\times\ \text{误杀（框架}\ne\text{成果）}}\\
S3\ \text{moa}(n)\ \text{下一项}& \text{框架已建＋规模型}&\boxed{\text{未做出}}&\boxed{\times\ \text{误杀}}\\
S4\ \text{Barbados}\#24& \text{2026 给出“完整分类”}&\boxed{\text{邻域成果};\ \text{目标（计数/小性）未做出}}&\boxed{\times\ \text{部分误杀}}\\
\text{Zarankiewicz 其余格}& \text{2024–26 产出数十新值}&\text{那些格已做出};\ \boxed{\text{其余格未做出}}&\text{须逐格重判}\\
\text{Brouwer 表其余格}& \text{表龄＋流水线}&\boxed{\text{未做出（且表可能滞后）}}&\text{须逐格重判}\\
\text{LJCR 差集未知参数}& \text{经典路线覆盖“接口”}&\boxed{\text{未做出}}&\boxed{\times\ \text{误杀（接口}\ne\text{成果）}}\\
\end{array}$$ ✓✓
```

## §2 结论

```
$$\textbf{正杀}\ 4\ \text{类};\ \textbf{误杀（或部分误杀）}\ 6\ \text{类}\ \Longrightarrow\ \boxed{\text{池并非空};\ \text{是我把它清空的}}$$ ✓✓
$$\textbf{误杀根因}:\ \text{把}\ \boxed{\text{“有人在做/接口被占”}\ \text{当}\ \boxed{\text{“已做出成果”}}\ \text{用}$$
```

## §3 复活集（按"可产出 ∧ 可验证"重排）

```
$$\boxed{\text{首选 }X1:\ \text{找 }119\text{-word、长 }10\text{、半径 }1\ \text{覆盖码}}\ ——\ \text{开出 } \le119\ \text{即}\ K(10,1)\le119\ \text{新记录};$$
$$\qquad \textbf{证书}:\ \text{显式码集合}\ \Longrightarrow\ \text{覆盖性可由枚举邻域}\ \textbf{秒级独立复核}\ ✓\ （\text{与 }C07\ \text{同形，成本最低、验证最硬}）$$
$$\qquad \textbf{竞争}:\ \text{在跑项目在证“不可行（}\ge120\text{）”──}\textbf{方向相反};\ \text{并不覆盖“存在 }119\text{-码”这一命题};\ \text{记录区间 }[107,120]\ \text{说明 }119\ \text{从未被排除}$$ ✓✓
$$\boxed{\text{次选 }R(3,10):\ \text{构造 }40\ \text{顶点无三角、}\alpha\le9\ \text{图}\ (\Rightarrow R(3,10)\ge41)};\ \text{证书同样秒级可验}$$
$$\text{其余复活项}:\ S2/S3/S4\ \text{精确值层};\ \text{LJCR 未知参数（存在性，证书＝显式差集）};\ \text{Zarankiewicz/Brouwer 逐格重判}$$
【⛔ 纪律】 本档零计算;\ \text{未决策};\ \text{未改交付物类型} ✓
【边界】 重审基于前几轮已取证据;\ \text{未逐格重跑} ✓
