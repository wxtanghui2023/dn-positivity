已查地图：命中（`OPG-narrow-check-A-equals-zero`）⟹ 数据库型来源批（`A1`/`A2`），不开新案
D0: 本档对象 = **`A1 HoG` 定式输出（条目总数／`R_0\to R_1` 候选数／逐候选／`A-count`）** ＋ **`A2` crossing-number 输出** ＋ 两源 `A=0` ＋ 交棒 `A3`
D1: 0（source-level 抽取型，零计算）
[REVIEW]

# **数据库型来源批：`A1` / `A2`**

## §A1 `HoG-R3-A1`

```
$$\textbf{条目总数}:\ \text{可搜索库}\ \approx\mathbf{22{,}000}\ \text{“interesting”图}\ (\text{HoG 2.0, Coolsaet–D'hondt–Goedgebeur, DAM 325:97–107, 2023});\ \text{另设}\ \boxed{\texttt{meta-directory}}\ =\ \text{按图类组织的}\textbf{完整列表＋生成器}$$
$$\qquad \text{维护方}:\ \text{Ghent（Coolsaet／D'hondt／Goedgebeur）}\ \mathbf{活跃}\ (2026\text{-}09\ \text{仍在更新})$$
$$\textbf{R}_0\to R_1\ \textbf{型候选数}:\ \mathbf{5}\ (\text{见下；均为“记录型入口类”，非全库逐条})$$
$$\begin{array}{c|l|l|l|l|l|c}
\#&\text{exact object / parameters}&\text{current record}&\text{certificate type}&\text{finite verifiability}&\text{active search owner?}&\text{A/W/D}\\\hline
1&\text{SRG}(37,18,8,9)\ \text{完备化}& \text{McKay 数据页}:6760\ \text{图},\ \boxed{\text{“maybe incomplete”}}&\text{显式列表（可验证）}&\text{可（但须穷举生成）}&\boxed{\text{是}}\ (\text{McKay 团队})&D\\
2&\text{hypohamiltonian 小阶完备表（}<18\ \text{顶点已列全）};\ \text{最小平面 hypohamiltonian 图（现 40 顶点）}&\text{完整列表已公开}&\text{显式列表}&\text{可}&\boxed{\text{是}}\ (\text{McKay／Östergård／Zamfirescu})&W/D\\
3&\text{cage 记录（最小 }k\text{-正则、围长 }g\ \text{图）}&\text{多格已定，若干格只有上下界}&\text{显式图＋穷举下界}&\text{可}&\boxed{\text{是}}\ (\text{Exoo／McKay cage 表})&W\\
4&\text{chromatic–girth／4-正则 4-色 高围长记录}&\text{best-known 表（Royle 维护）}&\text{显式图}&\text{可}&\boxed{\text{是}}&D\\
5&\text{反例图库（conjecture counterexamples）}&\text{HoG 收集（仓库型，非记录表）}&\text{显式图}&\text{可}&\text{多为搜索产物}&D\\
\end{array}$$ ✓✓
$$\boxed{\text{A-count} = 0}$$ ✓（\text{四项落在“维护者本人活跃推进”}\Rightarrow W/D;\ \text{一项为仓库型}\Rightarrow D）$$
$$\textbf{口径确认}:\ \text{本表}\textbf{不把“数据库里有 open entry”当候选};\ \text{仅取}\ \boxed{\text{记录型入口类}}\ \text{并逐类判其占有状态}$$
$$\textbf{覆盖边界（诚实）}:\ \text{未逐条枚举 22{,}000 图，亦未逐类清点 meta-directory};\ \text{上表为}\textbf{可识别的记录型入口类}}$$
```

## §A2 `crossing-number 数据库`

```
$$\textbf{对象}:\ \text{rectilinear crossing number}\ \text{rcr}(K_n);\quad \textbf{现行记录}:\ \text{精确值已知 }n\le27\ \text{与 }n=30;\ \boxed{\text{最小未解案例 }n=28:\ \text{rcr}(K_{28})\in\{7233,7234\}}$$
$$\qquad （\text{Schaefer 2026, p.86};\ \text{表见 Ábrego–Fernández-Merchant–Salazar 综述};\ \text{OEIS A014540}）$$
$$\textbf{certificate type}:\ \text{上界＝}\boxed{\text{显式点集（可机器计数交叉）}};\ \text{下界＝abstract order type 枚举／下界不等式（}\text{RCN project}）$$
$$\textbf{finite verifiability}:\ \text{上界可};\ \text{下界需证书型重算}$$
$$\textbf{active search owner}:\ \boxed{\text{是}}\ ——\ \text{Aichholzer 的 }\boxed{\texttt{RCN project}}\ \text{维护 lower bounds＋best known examples};\ \text{且 2026 年专著仍在追踪}$$
$$\textbf{判定}:\ \boxed{\text{W/D}}\ (\text{记录缺口真实};\ \text{但按先生 }A2\ \text{口径“剔除正在推进的经典项”}\Longrightarrow \text{不入选})$$
$$\boxed{\text{A-count} = 0}$$ ✓
```

## §结论与交棒

```
$$\text{数据库型批（已跑）}:\ A1\ \textbf{A=0};\ A2\ \textbf{A=0}$$
$$\Longrightarrow\ \textbf{照先生预登记规则}:\ \text{不在 }HoG/\text{crossing 内部改参数救场};\ \boxed{\text{直接进入 }A3\ (\text{Zarankiewicz 表})}$$ ✓
$$\textbf{两源共同模式（本轮提取）}:\ \text{权威数据库型的“记录”}\textbf{几乎全部由活跃团队自维护}\ \Longrightarrow\ \text{凡记录型入口，}\textbf{先问“谁在推进”}\ (\text{E3/E4 的直接应用});\ \text{本批两源正是由此全灭}$$
$$【⛔ 纪律】 本轮\textbf{零计算};\ \text{未决策};\ \text{未制造候选} ✓
【边界】 全为检索抽取级;\ HoG 未逐条枚举;\ 判定基于可识别入口类 ✓
