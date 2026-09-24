已查地图：命中（`HoG-A1-and-A2-source-check`）⟹ 数据库型批 `A3`，不开新案
D0: 本档对象 = **`A3 Zarankiewicz 表` 定式输出**（记录型入口／owner／在跑路线／`AMEND-21` 主闸） ＋ **`A=0`** ＋ **校准 E5（LANE-A 形态已被工业化）** ＋ 交棒 `A4`
D1: 0（source-level 抽取型，零计算）
[REVIEW]

# **`A3：Zarankiewicz 表`**

## §A3 定式输出

```
$$\textbf{记录型入口数}:\ \mathbf{4}\ \text{类（不混入普通 open problem）}$$
$$\begin{array}{c|l|l|l|l|c}
\#&\text{exact object / parameters}&\text{current record（抽取级）}&\text{在跑路线}&\text{owner}&\text{判定}\\\hline
1& z(n;2)\ (\text{即 }K_{2,2}\text{-free／}C_4\text{-free 二分};&\text{早期：}n\le21\ \text{精确};\ \boxed{\text{Afzaly–McKay 推至 }n\le31}&\text{穷举／SAT（规模大）}&\boxed{\text{是}}\ (\text{Afzaly–McKay})&\boxed{D}\\
2& z(n;3),\ z(m,n;3)\ \text{及不平衡型}& \boxed{\text{2024–2026 年多组持续产出}}:\ \text{Chen–Horsley–Mammoliti（JGT 106(1):81–109, 2024；JCD 32:556–576, 2024）};&\text{SAT／穷举／有限几何构造}&\boxed{\text{是}}\ (\text{多组})&\boxed{D}\\
&& \quad \text{SSRN 文}:\ \boxed{44\ \text{个新精确值}+31\ \text{个改进下界}}\ (z(m,n;3));\ \text{arXiv:2605.01120v3 (2026)}:\ \boxed{3\ \text{新精确值}+41\ \text{下界}}&&&\\
3& z(m,n;s,t)\ \text{一般小格／“前沿切片”}& \texttt{arXiv:2608.08154v1}\ (2026)\ \text{《Exact Zarankiewicz Values on Two Finite Frontier Slices》}&\text{穷举＋证书}&\boxed{\text{是}}&\boxed{D}\\
4& limited augmented Zarankiewicz\ z_L& \text{MDPI Symmetry 18(7):1076 (2026)}:\ 6\times4,\ 5\times3,\ 5\times4\ \text{新精确值};\ 5\times5\ \text{改进下界 15}&\text{构造＋上界论证}&\boxed{\text{是}}&\boxed{D}\\
\end{array}$$ ✓✓
$$\textbf{owner 汇总}:\ \text{Afzaly–McKay};\ \text{Chen–Horsley–Mammoliti};\ \text{Bhan 等 (2026)};\ \text{及独立 SAT 项目（见 §E5）};\ \textbf{无一条为无主记录}$$
$$\boxed{\text{AMEND-21（主闸）= 判除}}\ ——\ \text{计算路线成熟且}\textbf{正在高速产出}（\text{单年数十个新精确值}）\Longrightarrow \text{不因“数学上未完全解决”而生成 A 候选}$$ ✓✓
$$\boxed{\text{A-count} = 0}$$ ✓
```

## §E5 校准（本轮最重要发现）：**LANE-A 形态已被工业化**

```
$$\text{发现}:\ \texttt{metafunctor.com/research/hog}\ (\text{独立研究者，AI 辅助})\ \text{正在做}\textbf{与我方 LANE-A 完全同形}\ \text{的工作}:$$
$$\qquad \text{① SAT 求解（CaDiCaL 与 Kissat 双解一致）产出上界见证};\quad \text{② 见证以 }\texttt{graph6}\ \text{字节精确存储并}\textbf{从零重解重检};\quad \text{③ 存入 }\texttt{House of Graphs};\quad \text{④ 与 OEIS 交叉核（如 A008406 图计数）};$$
$$\qquad \text{⑤ 已产新值}:\ \boxed{\text{sat}(9,C_6)=12,\ \text{sat}(10,C_6)=13}\ (\text{连 }\ n+3\ \text{模式,\ 位于 Lan–Shi 窗口顶端});\ \text{另含 Zarankiewicz 见证}$$
$$\Longrightarrow\ \boxed{\text{E5}:\ \textbf{“dent＋证书＋入库”这一形态本身已被 AI 加速的独立研究者工业化}}$$ ✓✓✓
$$\qquad \text{战略含义}:\ \text{我方 }C07\ \text{式成功所依赖的}\textbf{形态}\ \text{已非稀缺};\ \text{稀缺的是}\boxed{\text{尚未被这条流水线覆盖的具体格}}$$
$$\qquad \text{操作含义}:\ \text{今后凡“记录型”候选，须额外查}\ \boxed{\text{是否存在 AI＋SAT＋入库 型流水线已覆盖该格}}\ (\text{E5 前置问})$$
```

## §交棒

```
$$\text{数据库型批进度}:\ A1\ A=0;\ A2\ A=0;\ \boxed{A3\ A=0}$$
$$\Longrightarrow\ \textbf{照预登记规则}:\ \text{不在 }\ Zarankiewicz\ \text{内部改参数救场};\ \boxed{\text{直接进入 }A4\ (\text{Brouwer 表})}$$
$$\textbf{A4 前置（照先生预登记）}:\ \text{须先做}\ \boxed{\text{identity lock}}\ ——\ \text{编码/设计理论重复率高};\ \text{并叠加 }\boxed{\text{E5 前置问}}$$
【⛔ 纪律】 本轮\textbf{零计算};\ 未决策;\ 未制造候选 ✓
【边界】 全为检索抽取级;\ 未逐格清点 Zarankiewicz 全表;\ 判定基于可识别记录型入口类 ✓
