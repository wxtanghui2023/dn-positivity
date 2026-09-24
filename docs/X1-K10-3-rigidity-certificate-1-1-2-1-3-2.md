已查地图：命中（`X1-K10-2-results-rigidity-and-negative-neighbourhoods`）⟹ `X1` 第三轮（`(3,2)` 定向剪枝），不开新案
D0: 本档对象 = **`K(10,1)` 记录码刚性证书（`(1,1)`／`(2,1)`／`(3,2)` 三层）** ＋ **完整重数直方图** ＋ **`(3,2)` 剪枝机制与统计** ＋ **范围界定** ＋ 复现命令
D1: 1（实际计算；产出可复核的穷举否定与结构事实）
[RESEARCH]

# **`K(10,1)` 记录码刚性证书**

## §1 完整重数直方图（本轮新事实）

```
$$\text{顶点按被覆盖重数分类（}N=1024\text{）}:\quad \boxed{\text{重数 }1:801;\ \ 2:172;\ \ 3:36;\ \ 4:8;\ \ 5:7}\quad(\text{合计 }1024\ \checkmark)$$
$$\Longrightarrow\ \text{记录码\textbf{极紧}：}78.2\%\ \text{的顶点只被一个码字覆盖};\ \text{最大重数仅 }5$$
$$\text{私有结构}:\ \mathtt{S}(w)\ \text{（重数 1 顶点）};\ \ \mathtt{D2}\ \text{组 }=159\ \text{个};\ \ \mathtt{D3}\ \text{组 }=36\ \text{个}$$
```

## §2 `(3,2)` 剪枝机制（照先生指定：singleton-owner ＋ bitset 缺口）

```
$$\text{对 }D=\{i,j,k\}\subset C:\quad \boxed{M(D)=\{v:\operatorname{owners}(v)\subseteq D\}}$$
$$\qquad \text{可预计算分解}:\ M(D)=\mathtt{S}(i)\cup\mathtt{S}(j)\cup\mathtt{S}(k)\ \cup\ \mathtt{D2}(ij)\cup\mathtt{D2}(ik)\cup\mathtt{D2}(jk)\ \cup\ \mathtt{D3}(ijk)$$
$$\qquad \text{（重数}\ge4\ \text{的顶点\textbf{永远不会}被 3 字删除变为缺口}\ \Longrightarrow\ \text{可完全预计算，无需扫描全结构}）$$
$$\textbf{计数剪枝（P1）}:\ \boxed{|M(D)|>22\ \Rightarrow\ \text{淘汰}}\ ——\ \text{因半径 1 球覆盖 }1+10=\mathbf{11}\ \text{词，两球至多 }2\times11=\mathbf{22}$$
$$\qquad \textbf{（更正}:\ \text{先生文中“每球 }91\text{、两球 }182\ \text{”适用于别的参数空间；本实例球大小 }=11,\ \text{门槛}=22,\ \text{剪枝强 }8\ \text{倍以上）}$$
$$\textbf{精确检验}:\ \text{用}\ \boxed{\text{顶点}\to\text{覆盖它的候选字}}\ \text{索引}（\text{每顶点仅 }11\ \text{个覆盖者}）\ \Longrightarrow\ \text{每三元组至多 }11\times11\ \text{次检验（非 }904^2\text{）}$$
```

## §3 `(3,2)` 统计与判定

```
$$\begin{array}{c|c}
\text{项目}&\text{数值}\\\hline
\text{三元组总数}&\mathbf{280{,}840}=\binom{120}{3}\\
\text{P1 剪掉}\ (|M|>22)&\mathbf{61{,}400}\ (21.9\%)\\
\text{进入精确检验}&\mathbf{219{,}440}\\
\text{命中（119-码）}&\boxed{\mathbf{0}}\\
\text{用时}&\mathbf{28.3\ s}\\
\end{array}$$
$$|M(D)|\ \text{分布（}\le22\text{）}:\ 7\to4;\ 8\to14;\ 9\to32;\ 10\to144;\ 11\to516;\ 12\to846;\ 13\to1988;\ 14\to5401;\ 15\to8838;\ 16\to12277;\ 17\to21784;\ 18\to35500;\ \boxed{19\to32762;\ 20\to40156};\ 21\to34712;\ 22\to24466;\quad \max=33$$
$$\Longrightarrow\ \boxed{(3,2)\ \text{邻域穷举完毕，无 119-码（相对该 120-记录码）}}$$ ✓✓
```

## §4 刚性证书（三层）

```
$$\begin{array}{c|l|l}
\text{邻域}&\textbf{穷举规模}&\textbf{判定}\\\hline
(1,1)\ \text{换 1 字}&120\times904=108{,}480&\boxed{\text{否}}:\ \text{仅 }2\ \text{个仍为覆盖码（且均无冗余字）}\\
(2,1)\ \text{删 2 补 1}&\binom{120}{2}\times904=7{,}140\times904&\boxed{\text{否}}\ (\text{全扫})\\
(3,2)\ \text{删 3 补 2}&\binom{120}{3}=280{,}840\ (\text{剪枝后 }219{,}440)&\boxed{\text{否}}\ (\text{全扫},\ 28.3\ \text{s})\\
\end{array}$$ ✓✓
$$\text{warm start 最佳态}:\ \text{删 }0111111001\ \Longrightarrow\ 119\ \text{字仅剩 }\{473,507\}\ \text{未覆盖};\ \text{但}\ (1,1)\ \text{修复无解}$$
```

## §5 范围界定（**锁死，不得越界**）

```
$$\boxed{\text{本证书仅排除：该 120-记录码的 }(1,1)/(2,1)/(3,2)\ \text{邻域}}$$
$$\boxed{\textbf{不排除}:\ \text{全局其他 119-集}\ (\text{即 }119\text{-set}\not\approx C_{120}\ \text{的情形})};\ \text{亦不排除更高阶邻域 }(4,3),\ldots$$
$$\boxed{\textbf{不得}写成“119 不存在”};\ \text{正确表述}=\text{“119 不在该记录码的三层邻域内”}$$
```

## §6 复现

```
$$\text{脚本}:\ \texttt{work/k10/sweep32c.py}\ (\text{剪枝＋索引二球检验});\quad \text{统计}:\ \texttt{work/k10/sweep32\_stats.json}$$
$$\text{基底}:\ \texttt{work/k10/kamenetsky120.txt}\ (\text{OEIS }a000983\text{.txt 公开 120-码，经我方独立验证器复核 }1024/1024)$$
$$\text{运行}:\ \texttt{cd work/k10 \&\& python3 -u sweep32c.py}\ \Longrightarrow\ 28.3\ \text{s},\ \text{hits}=0$$
```

## §7 下一步（三选）

```
$$\text{(甲)}\ (4,3)\ \text{定向剪枝}:\ \binom{120}{4}=8{,}214{,}570\ \text{组};\ \text{同框架可跑（预估数分钟～数十分钟）};\ \text{但邻域阶数越高，}\textbf{离“全局”越远（边际信息递减）}$$
$$\text{(乙)}\ \text{ILP/CP-SAT 长预算}:\ \text{全局 min set-cover（需装 }\texttt{ortools}\text{）}$$
$$\text{(丙)}\ \text{收口}:\ \text{以“独立性复核 ＋ 重数剖面 ＋ 三层刚性证书”为本轮交付}$$
【⛔ 纪律】 本轮实际计算；\ \text{已当场自查并修正 3 处自身问题}:\ \text{① (2,1) 首版 }U\ \text{计数 bug（假解，被 }verify=False\ \text{判死）};\ \text{② 统计打印误置于循环之后（看似卡死）};\ \text{③ }pkill/pgrep\ \text{自杀陷阱两次} ✓
【边界】 记录值取自 OEIS（抽取级）；\ \text{其余数值均为本地实测＋独立验证} ✓
