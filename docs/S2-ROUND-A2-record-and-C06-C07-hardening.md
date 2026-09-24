已查地图：命中（`S2-ROUND-A-D03-D04-D06-D07-XG-completion` ＋ `AMEND-18`）⟹ 本档为 Round A-2 记录 ＋ `C06/C07` 硬化，不开新案
D0: 本档对象 = **Round A-2 六条记录（`Mt06,Mt07,Mt08,C06,C07,C09`）** ＋ **`C06`／`C07` 的 `G0→G1/G2` 硬化**（含具体参数格、等价关系、可执行证书）＋ `Zone-B` 口径锁定
D1: 1（首次把 Zone-A 候选从"形态标签"硬化为可执行命题；产出两个 `G1*` 级候选）
[RESEARCH]

# **Round A-2 记录 ＋ `C06`/`C07` 硬化**

## §0 口径锁定与 Round A-2 结果

```
$$\textbf{Zone-B 锁定}:\ \boxed{N=16,\ \texttt{SPEC}=8,\ U_{\rm research}=8};\quad \texttt{SPEC}=\{M01,M02,M06,Au03,Au04,Au05,Au07,Au08\}$$ ✓✓
$$\textbf{D03 的 }\texttt{G0}\ \text{确认}:\ \text{不得把 }STS(v)\le19\ \text{偷塞成原命题窗口};\ \textbf{此纪律对后 6 条一视同仁}$$ ✓✓
$$\begin{array}{c|c|c|l}
\text{ID}&\texttt{G}&\text{暂定 A}&\text{分水岭}\\
\hline
Mt06&\texttt{G0}&A?&\text{automorphism-order distribution 是否已有};\ \text{须锁未完成 }v\\
Mt07&\boxed{\texttt{G1}}&A0?&\text{具体 Ramsey 格是否真 open};\ \text{exact/census 必须分离}\\
Mt08&\texttt{G0}&A?&\text{Tutte collision 是否产生独立结构（非补表）}\\
C06&\texttt{G0}&A?&\text{optimal value 已知但 inequivalent achiever census 未知}\\
C07&\texttt{G0}&A?&\text{covering radius 的参数化与 exact gap}\\
C09&\texttt{G0}&A?&\text{须先定义真正的 spectrum observable}\\
\end{array}$$ ✓✓
$$\text{本轮硬结论}:\ \textbf{6 条中仅 }Mt07\ \text{为硬 }\texttt{G1};\ \text{其余 5 条 }\texttt{G0};\ \textbf{无一条可 }DROP;\ \text{不得为凑 }A\ \text{数而人为补窗口}$$ ✓✓
```

## §1 `C06` 硬化（`G0 → G1*`）

```
$$\mathcal O:\ \text{最优 }q\text{-ary 分组码 }C\subseteq\mathbb Z_q^n,\ |C|=A_q(n,d);\ \text{取}\ \textbf{同构类}\ [C]$$ ✓
$$\text{等价关系}\ \operatorname{Iso}:\ \boxed{\Gamma=(\text{坐标置换})\times(\text{字母表置换})};\ \textbf{线性/非线性分开统计};\ \text{（若走线性码，须另注 monomial 等价）}$$ ✓✓
$$\mathcal I:\ \boxed{E_q(n,d)=\#\{[C]:|C|=A_q(n,d),\ d_{\min}(C)\ge d\}};\qquad \text{可选升级：全部 }[C]\ \text{的构造列表}$$ ✓
$$\mathcal P\ (\textbf{选择规则，使 }\mathcal P\ \text{闭合}):\ \text{取}\ \textbf{最小}(q,n,d)\ \text{使}\ (i)\ A_q(n,d)\ \text{在标准表中有精确值};\ (ii)\ \text{该格的 inequivalent-optimal-code 分类\textbf{未发表}}$$ ✓✓
$$\qquad \text{候选格（须一次点检后择一）}:\ (q,d)=(2,4)\ \text{且 }n\le16;\quad (2,6)\ \text{且 }n\le16;\quad (3,3)\ \text{且 }n\le10$$ ✓
$$\mathcal G:\ \boxed{\text{gap}=E_q(n,d)\ \text{未知而}\ A_q(n,d)\ \text{已知}};\ \text{关闭 }\mathcal G\ \text{只需}\ \textbf{一次定点检索}:\ \text{检索式}\ \texttt{"classification of optimal binary (n,d) codes"}$$ ✓✓
$$\mathcal T:\ \text{canonical augmentation 枚举}\to\ \text{isomorph rejection}\to\ \text{独立距离复核}\to\ \textbf{完备性证书}$$ ✓
$$\text{状态}:\ \boxed{\texttt{G1}^*}\ (\text{窗口与等价关系已闭合};\ \mathcal G\ \text{待一次点检};\ \text{点检为"已发表分类"} \Rightarrow \texttt{DROP})$$ ✓✓
$$\text{暂定 A}:\ \boxed{A0?}\ ——\ \text{优势}:\ \text{optimal value 已知} \Rightarrow \text{gap 极干净};\ \text{风险}:\ \text{若仅"补格"} \Rightarrow A0$$ ✓
```

## §2 `C07` 硬化（`G0 → G1/G2`）

```
$$\mathcal O:\ \textbf{三选一，不得混}:\ (i)\ R(C)\ \text{（给定码 }C\text{）};\ (ii)\ R_{\min}(q,n,k)=\min_{\dim C=k}R(C)\ \text{（线性）};\ (iii)\ R_{\min}(q,n,M)\ \text{（非线性）}$$ ✓✓
$$\text{本轮锁定}:\ (ii)\ \text{线性};\ q=2;\ \textbf{小区间 }n\le20,\ k\le10$$ ✓
$$\mathcal I:\ \text{精确整数 }R;\ \text{若仅有界则记 }\boxed{L<R<U}\ \text{并\textbf{显式记录 }L,U}$$ ✓
$$\mathcal G:\ \text{覆盖码表（Kéri 型/covering-code tables）给出大量 }(q,n,k)\ \text{的上下界};\ \textbf{缺口＝具体单元 }(2,n,k)\ \text{的 exact }R\ \text{未知}$$ ✓
$$\textbf{与 }D04\ \text{的假重复纪律}:\ D04=\text{packing number};\ C07=\text{covering radius};\ \text{共享"有限组合＋exact 表缺口"}\ \textbf{方法形态}，\text{但 }\boxed{\text{形态重复}\ne\text{数学重复}}$$ ✓✓✓
$$\mathcal T:\ \text{enumerate inequivalent codes}\to\ \text{distance partition}\to\ \text{exact }R\to\ \text{下界证书}\to\ \text{上界构造}\to\ \text{独立复核}$$ ✓
$$\text{状态}:\ \boxed{\texttt{G1}\ \text{（可一步到 }\texttt{G2}\text{）}}\ ——\ n\le20,\ k\le10\ \text{规模可控};\ \text{distance partition 与证书均可机器验证}$$ ✓✓
$$\text{暂定 A}:\ \boxed{A0?}\ ——\ \text{若能给出\textbf{整格规律}（如 }R_{\min}(2,n,k)\ \text{的公式段）\Rightarrow A+;\ \text{若仅补若干格}\Rightarrow A0$$ ✓
```

## §3 下一步（照先生优先序）

```
$$\boxed{C06\rightarrow C07\rightarrow Mt06\rightarrow Mt08\rightarrow C09};\quad \text{本档完成 }C06,C07$$ ✓
$$\text{余下}:\ Mt06\ (\text{须锁未完成 }v\ \text{并查 automorphism distribution 是否已有});\quad Mt08\ (\text{须把 observable 定为最小 Tutte-collision 对});\quad C09\ (\text{须先定义 }\operatorname{Spec})$$ ✓✓
【⛔ 纪律】 零数学计算；`U_{2,3}` 暂停；**不回 RH**；`S3` 冻结；`Zone-B` 口径已锁 ✓
【边界】 §1/§2 的"具体格"须**一次定点核验**后方可固定；文献状态为档级 ✓

## §附 【技术词回查】（补录）
```
技术词 equivalence      命中文件数=34   :: ./kloosterman_fractions.pdf ./V158-spectral-identity-formalization-consistency-soundness-completeness.md ./p49-ab-proofs.md 
技术词 certificate      命中文件数=135  :: ./C3880-standalone-paper-packaging-of-the-cone-separation-assets.md ./C319-directed-recheck-C272-pending-box-set-semantics-GAP-CONFIRMED.md ./C3896-exact-symbolic-T3PASS-certificate.md 
```
