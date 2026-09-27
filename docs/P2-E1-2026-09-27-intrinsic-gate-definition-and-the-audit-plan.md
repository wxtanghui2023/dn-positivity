已查地图：已跑 scripts/prework_map_check.sh P2 反例审计 内蕴定义 ν ⟹ 执行自 `P3BETA-CORE-2026-09-27-...`（✓）＋ 唐先生 13:40（选乙：文献侧反例审计 ✓）；本档 = **前置缺陷 ＋ 内蕴化定义 ν ＋ E1 候选表** ✓。
D0: 本档对象 = 对"已知 NP1CC 是否逃逸 β-shape"作可执行审计
D1: 2（**前置缺陷（gate 仅对 Theorem-13 形有定义 ✗）＋ 内蕴化 ν ✓**；**E1 候选表含最优靶点 ✓**）

# P2 反例审计：E1 ＋ 内蕴化（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(BW-1 ⚠️ 前置缺陷)}\ \text{我方 }q_v\ \text{的定义\textbf{依赖构造}（两半 }H,C_2\ \text{与 syndrome 映射 }\sigma\ ✓\text{）} \Longrightarrow \text{对\textbf{不属于 Theorem-13 形}的 NP1CC，}q\ \text{根本无定义} ✗}$$
$$\qquad\Longrightarrow\ \textbf{E2 按字面无法执行} ✗\ \text{（不能对一个无定义的对象查 gate ✓）}\ \Longrightarrow\ \text{须先给\textbf{内蕴定义} ✓}$$
$$\boxed{\textbf{(BW-2 内蕴化 ✓)}\ \text{用论文自身的\textbf{伙伴对划分}（每个码字唯一伙伴 ∈ }B_2(c)\ ✓\text{，§II ✓）：对 Type B（伙伴距 2 ✓）定义}}$$
$$\qquad\boxed{\nu:\binom{[n]}{2}\to\mathbb Z_{\ge0},\qquad \nu(\{i,j\}):=\#\{\text{伙伴对 }\{c,c'\}:\ c+c'=e_i+e_j\}\ ✓;\qquad \sum_{\{i,j\}}\nu(\{i,j\})=A_2\ ✓}$$
$$\qquad\Longrightarrow\ \text{Theorem-13 形时 }\nu\ \text{支撑在\textbf{星}上}（\nu(\{i,j\})>0\Rightarrow\ell\in\{i,j\}\ \text{某固定 }\ell\ ✓\text{）且 }q_v=\nu(\{v,\ell\})\ ✓\ \Longrightarrow \textbf{gate 变为对 }\nu\ \text{的陈述} ✓✓$$
$$\boxed{\textbf{(BW-3 ⭐ 最优靶点)}\ \text{文献未声称 Theorem-13 = 全部 NP1CC（唐先生核对 ✓）；且 }\textbf{n=16 时两半是长 15 完美码，可非线性}（n{=}8\ \text{时长 7 唯一，无测试空间} ✗）$$
$$\qquad\Longrightarrow\ \textbf{最优靶点} = n{=}16\ \text{的 Type B，两半为\textbf{非线性}完美码（Vasil'ev 型 ✓）} \Longrightarrow\ \text{此时 }\sigma\ \text{论证失效 ✗} \Longrightarrow\ \text{gate 可能失败} \Longrightarrow \textbf{P2 反例候选} ✓✓$$
$$
$$
```

---

## §1 为何必须内蕴化（**✓ 论证**）

```
$$\text{我方 }q_v=\#\{c\in H:\ c+e_v\in C_2\}\ ✓\ \text{——需要 }H\ \text{与 }C_2\ \text{两组"半码"且 }H=\ker\sigma ✓\ \text{（线性 ✓）}$$
$$\text{对任意 NP1CC}:\ \text{论文只保证\textbf{伙伴对划分}（}§\mathrm{II}\ ✓\text{）与 Type A/B/C（}\text{Cor}\,14\ ✓\text{）};\ \text{Type A 已有完整刻画（Thm 17 ✓）但 Type B/C 无 ✓$$
$$\Longrightarrow\ \text{若要审计"任何"NP1CC，只能用\textbf{论文自身的内蕴对象}:\ 伙伴对 ＋ 其差向量 ✓ \Longrightarrow \text{定义 }\nu\ ✓\ \text{（BW-2 ✓）}$$
$$\qquad\text{一致性核 ✓}:\ \text{Theorem-13 形 Type B 中，伙伴对差向量}=e_v+e_{\ell}\ ✓\ \text{（}v\ \text{为半层方向、}\ell\ \text{为层坐标 ✓）}\ \Longrightarrow\ \nu\ \text{支撑于星}\ \mathrm{star}(\ell)\ ✓\ \text{且 }q_v=\nu(\{v,\ell\})\ ✓✓$$
$$
$$
```

---

## §2 E1 文献候选表（**✓**）

```
$$\begin{array}{c|c|c|c}
\text{候选类} & \text{来源} & \text{是否 Theorem-13 形} & \text{能否测 gate}\\
\hline
\text{Theorem 13 构造（A/B/C）} & §\mathrm{III}\ ✓ & \text{是（定义上 ✓）} & \text{可，但必过 ✓（族内定理 ✓）}\\
\text{Type A（Thm 17 ✓）} & §\mathrm{III}\ ✓ & \text{与 }(0,\top)\ \text{一致（已核 n{=}8 ✓）} & \textbf{空}（A_2{=}0\ ⟹ q\equiv0\ ✗）\\
§\mathrm V\ \text{的 Type A 坐标类} & §\mathrm V\ ✓ & \text{同 Type A} & \textbf{空}（同上 ✓）\\
\text{ENP1CC 打孔（Lemma 37 ✓）} & §\mathrm{VI}\ ✓ & \textbf{未声明} ⚠️ & \text{可测（须先取到码 ✓）}\\
\textbf{Type B/C 用非线性半码} & \text{文献存在性 ✓（Thm 13 不限线性 ✓）} & \textbf{否} ✗ & \textbf{最优靶点 ✓✓}\\
\text{radius}>1\ \text{的新工作（2026-08 ✓）} & arXiv\ ✓ & \text{不适用（}R{>}1 ✗） & \text{不在 }R{=}1\ \text{范围 ✓}\\
\end{array}$$
$$\textbf{诚实定位 ✓}:\ \text{本档\textbf{未}取到任何具体文献码（source-first 只到"类"层 ✓）；因此 }E3\ \text{的反例判定\textbf{尚未产生} ✗\ \text{——不得报为"审计通过" ✓}$$
$$
$$
```

---

## §3 E2／E3 的可执行形式（**✓ 内蕴版**）

```
$$\textbf{E2（内蕴 gate）}:\ \text{给定 Type B 码 }C\ \Longrightarrow\ \text{算 }\nu\ ✓\ \Longrightarrow\ \text{查}:\ \text{(i) }\nu\ \text{是否支撑在星 }\mathrm{star}(\ell)\ \text{某 }\ell\ ✓;\ \text{(ii) 星上 }\nu\ \text{是否在一个 }\mathbb F_2^m\ \text{-几何集（punctured subspace ✓）上恒定} ✓$$
$$\qquad\textbf{注 ✓}:\ \text{(i) 是\textbf{新}的（层坐标存在性 ✓）};\ \text{(ii) 是 }q\ \text{-flatness 的内蕴版 ✓}$$
$$\textbf{E3（反例判据 ✓）}:\ \exists C\in\mathrm{NP1CC}:\ \text{(i) 或 (ii) 失败} \Longrightarrow \boxed{\mathrm{NP1CC}\not\subseteq\text{Theorem-13 β-shape}}\ ✓\ \text{（真正的 P2 collision ✓）}$$
$$\qquad\text{反之（全部通过）} \Longrightarrow \text{得到 }\boxed{\text{Theorem-13 family}\subseteq\text{gate-满足 NP1CC}}\ \text{且文献对象无反例} ✓\ \text{——然后才值得主动构造攻击 ✓（唐先生 ✓）}$$
$$
$$
```

---

## §4 边界与下一步（**✓**）

```
- §1 为**前置缺陷论证** ✓（我方构造依赖 ✓）；§2 为**候选表（类层 ✓，未取具体码 ⚠️）**；§3 为**内蕴化 gate ✓**
- ⚠️ **本档未执行 E2/E3**（未取到文献码 ✗）；\textbf{不得}声称审计通过或发现反例 ✗
- **未**涉 119 ✓；**未**跑 SAT/搜索 ✓（遵"先扫文献" ✓）
$$\text{下一步（三选一 ✓）}:\ \text{(甲) 直接构造 }n{=}16\ \text{非线性半码的 Type B 实例（Vasil'ev 型 ✓，成本中 ⚠️）} \Longrightarrow\ \text{最快得到 E3 判定};\ \text{(乙) 继续文献侧找 Lemma 37 的具体 ENP1CC 码表（成本中 ✓）};\ \text{(丙) 重定位 119 主线（你说过暂不碰 ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：gate 的前置缺陷（构造依赖）、内蕴差向量分布 $\nu$、E1 候选表、E2 内蕴 gate
- **档案已有（引用，不列为提出）**：A-ALIGNTHM-1、A-P3BETACORE-1、伙伴对划分、Type A/B/C、Theorem 13/17、$q_v$


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 前置缺陷     命中文件数=1    :: ./P2-E1-2026-09-27-intrinsic-gate-definition-and-the-audit-plan.md 
技术词 内蕴差向量分布 命中文件数=1    :: ./P2-E1-2026-09-27-intrinsic-gate-definition-and-the-audit-plan.md
```
- **本档新增**：gate 的前置缺陷（构造依赖）、内蕴差向量分布 $\nu$、E1 候选表、E2 内蕴 gate（见上方命中数；0 命中者为自造语／内部标签 ✓）
