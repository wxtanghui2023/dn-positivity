已查地图：已跑 scripts/prework_map_check.sh Vasil'ev 实现修正 E3 ⟹ 执行自 `P2-A-STEP1-2026-09-27-...`（✓，**本档对其三处结论作更正** ✓）＋ 唐先生 13:50（锁账、不越 Step 1 ✓）；本档 = **实现 bug 定位与更正 ＋ 已验证的 Vasil'ev 完美码 ＋ E3 判定** ✓。
D0: 本档对象 = Vasil'ev 半码（修正实现）与 P2-A 的 E3 判定
D1: 2（**实现 bug ＋ 三处自我更正 ✓**；**E3 判定：家族外候选 → β-gate 全通过 ✓**）

# P2-A 第二步：Vasil'ev 验证与 E3 判定（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BZ-1 🔴 实现 bug（真凶 ✓）)}\ \text{我此前写第三块为 }(\mathrm{wt}(v)\oplus\lambda(c))\ll 14\ \textbf{未截成单比特} ✗ \Longrightarrow \text{生成字可达 }2^{17} \Longrightarrow \textbf{根本不是 }\mathbb F_2^{15}\ \text{的字} ✗✗}$$
$$\qquad\Longrightarrow\ \textbf{撤回三处} ✗:\ \text{(a) "六形状全失败" ✗};\ \text{(b) "distance-aware 修正项"诊断 ✗（系 bug 产物 ✓）};\ \text{(c) 我对唐先生 }V_{15}\ \text{数据的"不复现"判定 ✗}$$
$$\qquad\textbf{更正后 ✓}:\ \text{形状 A}\ \textbf{确为完美码} ✓;\ |C_1\cap V|=256\ \textbf{与唐先生报告一致} ✓✓\ \text{（其数据原本正确 ✓，是我的实现错了 ✗）}$$
$$\boxed{\textbf{(BZ-2 ✓ 已验证构造)}\ V=\{(\,v,\ v+c,\ |v|\oplus\lambda(c)\,):v\in\mathbb F_2^7,c\in H_7\},\ \lambda(c)=c_0c_1\ (f(0)=0\ ✓)\ \Longrightarrow\ |V|=2048\ ✓,\ \mathfrak B_1(V)=\mathbb F_2^{15}\ ✓\ (\text{掩码 ＋ 暴力双验 ✓}),\ V\ \textbf{非线性} ✓}$$
$$\boxed{\textbf{(BZ-3 ⭐ E3 判定 = 通过（无 collision ✓）)}\ C=(H_{15},0)\cup(V,1)\ \text{经覆盖核验}\ \mathfrak B_1(C)=\mathbb F_2^{16}\ ✓ \Longrightarrow \textbf{NP1CC 确认 ✓✓};\ \text{且 }C\ \textbf{家族外} ✓\ (\text{半码非线性 ✓})}$$
$$\qquad|\mathrm Z|=M=4096\ ✓,\ \text{伙伴对}=2048=M/2\ ✓,\ \nu=\{1:256,\ 2:1792\}\ ✓,\ A_2=1792\ ✓$$
$$\qquad\textbf{E3(i) 星性质 ✓ 通过}（公共坐标 }=\{15\}\ ✓\text{）};\quad \textbf{E3(ii) flatness ✓ 通过}（切片 }\equiv256=\lambda\ ✓\text{）};\quad |S|=7\ ✓$$
$$\qquad\Longrightarrow\ \textbf{P2-A/Vasil'ev-15 = NEGATIVE（该候选未击穿 β-gate ✓）}\ \text{——且此次建立在\textbf{已验证 NP1CC} 之上 ✓✓}$$
$$
$$
```

---

## §1 修正后的双验数据（**✓ 决定性**）

```
$$\begin{array}{c|c|c|c}
\text{形状} & |S| & \text{掩码覆盖} & \text{暴力未覆盖(300 随机目标)}\\
\hline
A\ (v,\ v{+}c,\ |v|\oplus\lambda(c)) & 2048 & ✓ & 0\ ⟹ \textbf{完美 ✓✓}\\
C\ (v{+}c,\ v,\ |v|\oplus\lambda(c)) & 2048 & ✓ & 0\ ⟹ \textbf{完美 ✓✓}\\
G\ (v,\ v{+}c,\ |v{+}c|\oplus\lambda(c)) & 2048 & ✓ & 0\ ⟹ \textbf{完美 ✓✓}\\
B\ (v,\ c,\ |v|\oplus\lambda(c)) & 2048 & ✗ & 121\ ⟹ 非完美 ✗\\
H\ (v,\ c,\ |c|\oplus\lambda(c)) & 2048 & ✗ & 132\ ⟹ 非完美 ✗\\
\end{array}$$
$$\textbf{教训 ✓}:\ \text{"先怀疑自己的实现"在本项目第 12 次应验 ✓；}\textbf{且不得把实现产物升级为诊断/定理} ✓（唐先生 13:50 §3 的告诫完全正确 ✓）$$
$$
$$
```

---

## §2 E3 实验的完整链（**✓ 每一步均有独立核验**）

```
$$\text{(1) 半码}:\ V\ \text{非线性（XOR 不封闭 ✓，实测 }120\times120\ \text{对 ✓）};\ |C_1\cap V|=256\ \Longrightarrow\ \text{Type C 形 ✓（}0<k<2048\ ✓\text{）}$$
$$\text{(2) 组装}:\ C=(H_{15},0)\cup(V,1),\ |C|=4096=\tfrac{2^{16}}{16}\ ✓;\ \text{覆盖核验 }\mathfrak B_1(C)=\mathbb F_2^{16}\ ✓\ \Longrightarrow\ \text{最优 1-覆盖 ⟹ NP1CC ✓}$$
$$\text{(3) 内蕴 }\nu\ \text{（只用 §II 伙伴对划分 ✓）}:\ \nu=\{1:256,\ 2:1792\}\ ✓;\ \text{重量-2 差集 = }\{\{v,15\}:v\in S\}\ ✓\ (|S|=7\ ✓)$$
$$\text{(4) 三道 gate}:\ \text{(i) 星 ✓};\ \text{(ii) flatness（}\equiv256=\lambda=A_2/|S|\ ✓\text{）};\ \text{(iii) }|S|=2^{d'}-1=7\ \Longrightarrow\ d'=3\ ✓$$
$$\Longrightarrow\ \text{与族内 }d'{=}3\ \text{行\textbf{完全一致}}:\ (\lambda,A_2,J)=(256,1792,458752)\ ✓✓$$
$$
$$
```

---

## §3 本轮真正的数学命题（**✓ 可入账**）

```
$$\boxed{\textbf{(BZ-4)}\ \text{首个}\textbf{家族外}（非线性半码 ⟹ 非 Theorem-13 线性形）的已验证 NP1CC，\textbf{仍然满足全部 β-gate} ✓✓}$$
$$\qquad\Longrightarrow\ \text{证据方向}:\ \text{"}\beta\text{-shape 不是线性半码的偶然产物"};\ \text{与 A-P3ALPHA-1（}B\not\Rightarrow q\text{）一致 ✓}$$
$$\qquad\textbf{严格边界 ✓}:\ \text{单例证据 ⟹ \textbf{不得}写成"}\beta\text{-gate 对任意 NP1CC 成立"} ✗\ \text{（那需通用性定理 ✓，仍 OPEN ✓）}$$
$$
$$
```

---

## §4 下一步（**✓**）

```
$$\text{(甲) }\lambda\ \text{参数扫描（唐先生先前提议 ✓）}:\ \text{换不同非线性 }\lambda\ \text{（含 }\lambda\equiv0\ \text{对照 ✓）} \Longrightarrow \text{记录 }(k,\ \mathrm{supp}\,\nu,\ \nu\ \text{取值集}) \Longrightarrow \text{看 gate 是否恒通过 ✓}$$
$$\text{(乙) ENP1CC puncturing（另一族外入口 ✓）};\qquad \text{(丙) 119 主线重定位（你说过暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：实现 bug 定位与三处自我更正、已验证 Vasil'ev 完美码构造、E3 判定（家族外候选通过双 gate）
- **档案已有（引用，不列为提出）**：A-PERFCOND-1、A-ALIGNTHM-1、P2-A 内蕴 $\nu$ 工具、Theorem 13、Type C


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 实现 bug 更正 命中文件数=0    :: 
技术词 家族外候选  命中文件数=1    :: ./P2-A-STEP2-2026-09-27-vasilev-validated-and-E3-negative.md
```
- **本档新增**：实现 bug 定位与三处自我更正、已验证 Vasil'ev 完美码构造、E3 判定（家族外候选通过双 gate）（见上方命中数；0 命中者为自造语／内部标签 ✓）
