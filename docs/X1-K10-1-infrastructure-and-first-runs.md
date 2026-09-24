已查地图：命中（`AMEND-24-reaudit-kill-vs-occupied`）⟹ `X1` 首攻（`K(10,1)<=119`），不开新案
D0: 本档对象 = **`X1` 基础设施（实例／SAT 编码／自校验／独立验证器／贪心＋repair／tabu）** ＋ **首轮实测（132；tabu `k=119` 未覆盖 111→100）** ＋ **算术更正（球大小 11 非 91）** ＋ 下一步
D1: 1（`AMEND-24` 后首个**实际计算**靶；基础设施建成并自校验）
[RESEARCH]

# **`X1 / K(10,1) ≤ 119`：基础设施与首轮**

## §0 算术更正（先纠一处）

```
$$\textbf{先生文中}:\ \text{“每个码字覆盖 }1+10(10-1)=91\ \text{个长度-10 词”}\ \text{与“从 }10^{10}\ \text{个词里挑 }119\ \text{个”}$$
$$\textbf{实际（本项目实例）}:\ \text{空间}=\{0,1\}^{10}\ \text{共 }N=2^{10}=\mathbf{1024}\ \text{词};\ \text{半径 }1\ \text{球}=\{w\}\cup\{w\oplus e_i,\ i=1..10\}\ \text{共 }\boxed{1+10=\mathbf{11}}\ \text{词}$$
$$\qquad \text{故计数下界}=\lceil1024/11\rceil=\boxed{94}\ (\text{非 }94\ \text{以外的值});\ \ 91\ \text{对应的是其它参数空间（非本实例）}$$ ✓
$$\textbf{结论不变}:\ \text{记录区间 }[107,120]\Longrightarrow 119\ \text{仍未被上界证书排除};\ \text{目标}=\text{找 }\boxed{\le119}\ \text{的覆盖码}$$
```

## §1 基础设施（已建成，代码在 `work/k10/`）

```
$$\begin{array}{c|l}
\text{文件}&\text{作用}\\\hline
\texttt{instance\_k10\_r1.json}&\text{实例：}1024\ \text{顶点};\ \text{每顶点可被 }11\ \text{个字覆盖（对称）}\\
\texttt{cover\_search.py}&\text{贪心多起点＋冗余消除＋(1,1)-换位＋delete\&repair};\ \text{含}\ \textbf{独立验证器}\\
\texttt{tabu.py}&\textbf{定长 }k\ \text{tabu}（最小化未覆盖数）—— Honkala–Östergård《Code design》方法族\\
\end{array}$$ ✓
```

## §2 自校验（**先用已知精确值验证编码正确性**）

```
$$\text{SAT 判定“是否 }\exists\ \text{大小}\le K\ \text{的 }Q_n\ \text{半径 }1\ \text{覆盖码”，与 OEIS A000983 已知值对照}:$$
$$\begin{array}{c|c|c|c}
n&K\ (\text{已知精确值})&K\to\text{SAT?}&K-1\to\text{SAT?}\\\hline
4&4&\checkmark\ \text{True}&(\text{未测})\\
5&7&\checkmark\ \text{True}&\checkmark\ \text{False}\\
6&12&\checkmark\ \text{True}&\checkmark\ \text{False}\\
7,8&16,32&(\textbf{仍在跑})&(\textbf{仍在跑})\\
\end{array}$$ ✓✓（\text{编码与判定链路}\textbf{正确}）$$
```

## §3 首轮实测结果

```
$$\textbf{(1) 贪心＋冗余消除＋delete\&repair}:\ \text{从 }\sim148\ \text{降到}\ \boxed{132}\ (\text{验证 }\checkmark\ \text{全覆盖})$$
$$\qquad \text{多起点}:\ 146\to134;\ 148\to132;\ \text{二次起点收敛慢}\Longrightarrow\textbf{朴素局部搜索离记录很远}$$
$$\textbf{(2) tabu（定长 }k=119\text{，目标未覆盖}=0\text{）}:\ \text{运行中};\ \text{18 秒内未覆盖 }111\to\boxed{100}$$
$$\qquad \text{（\textbf{记录}：best-known 上界 }\mathbf{120};\ \text{下界 }107;\ \text{故我方当前 }132\ \text{仍劣于记录}）$$
$$\boxed{\text{结论}:\ \text{链路正确};\ \text{但}\textbf{朴素方法与记录差距大};\ \text{攻 }119\ \text{需更强搜索或更好 warm start}}$$
```

## §4 下一步（三选，代价递增）

```
$$\textbf{(甲) 延长 tabu}:\ k=119\ \text{跑数小时}（4\ \text{核}）;\ \text{成功即新记录};\ \text{失败给 residue（诚实负结果）}$$
$$\textbf{(乙) warm start}:\ \text{取公开 }\mathbf{120}\text{-码（Kamenetsky best-known }n\le11\text{）作参照};\ \text{先复现 }120;\ \text{再测“删一字＋repair”是否可达 }119$$
$$\qquad \text{（注：若 }120\text{-码无冗余字，则 }119\ \text{需\textbf{非包含型}新构造，须全局搜索）}$$
$$\textbf{(丙) 换精确引擎}:\ \text{ILP/CP-SAT（需装 }\texttt{ortools}\text{）求 min set-cover};\ \text{可给较优解但难证最优}$$
【⛔ 纪律】 本轮\textbf{开始实际计算}（照 \textsc{amend-24}）;\ \text{不再输出闸门筛表} ✓
【边界】 记录值取自 OEIS（抽取级）；\ \text{我方数值为本地实测} ✓
