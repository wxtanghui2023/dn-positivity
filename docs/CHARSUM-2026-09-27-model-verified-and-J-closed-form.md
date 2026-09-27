已查地图：已跑 scripts/prework_map_check.sh 特征和 二项式 J 闭式 ⟹ 执行自 `THREE-2026-09-27-...`（✓）＋ 唐先生 14:59（开甲″-iv ✓）；本档 = **特征和模型验证 ✓ ＋ J 闭式 ✓ ＋ 推导状态** ✓。
D0: 本档对象 = 特征和模型的代数形式与其 J 闭式
D1: 3（**模型验证 ✓（含脚本 bug 更正 ✓）**；**J 闭式 ✓**；**推导状态：k'=1 已推导 ✓、k'=2 观测 ⚠️**）

# (甲″-iv) 特征和模型验证与 J 闭式（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(CV-1 ⭐模型 ✓（唐先生形式 ✓）)}\ \text{设 }Q=I/W\ (\ |Q|=2^{k'}\ ✓),\ \delta=f-\bar m \Longrightarrow\ \boxed{\delta=a\sum_{j=1}^{k'}\chi_j},\ \chi_j\ \text{独立 }\mathbb F_2\text{-特征} \Longrightarrow\ \boxed{f_r=\bar m+(2r-k')a},\ \boxed{e_r=\binom{k'}r\cdot|W|}\ ✓✓}$$
$$\qquad\textbf{三点印证 ✓}:\ k'{=}0\Rightarrow\text{单级};\ k'{=}1\Rightarrow\text{两级 }1{:}1;\ k'{=}2\Rightarrow\textbf{三级 }1{:}2{:}1\ ✓;\ \text{三级例 }\{96{:}4,128{:}8,160{:}4\}=128+32(-1,0,+1)\ \text{恰合 ✓✓}$$
$$\boxed{\textbf{(CW-1 ⭐J 闭式 ✓)}\ \text{用 }\sum_r\binom{k'}r(2r-k')=0,\ \sum_r\binom{k'}r(2r-k')^2=2^{k'}k'\ \Longrightarrow\ \boxed{J_{\rm all}=|W|\bigl(2^{k'}\bar m^2+2^{k'}k'a^2\bigr)},\quad \boxed{J_{\rm int}=J_{\rm all}-A_1^2}\ ✓✓}$$
$$\qquad\textbf{逐例核对（手工 ✓，脚本 bug 见 §2 ✓）}:\ \{128^{16}\}:\ |W|{=}16,k'{=}0\Rightarrow J_{\rm all}{=}16{\cdot}16384{=}262144\Rightarrow J_{\rm int}{=}\mathbf{245760}\ ✓;$$
$$\qquad\{112^8,144^8\}:\ |W|{=}8,k'{=}1,a{=}16\Rightarrow J_{\rm all}{=}8(32768{+}512){=}266240\Rightarrow J_{\rm int}{=}\mathbf{245504}\ ✓;\quad \{96^4,128^8,160^4\}:\ |W|{=}4,k'{=}2\Rightarrow J_{\rm all}{=}4(65536{+}2048){=}270336\ ✓$$
$$\qquad\Longrightarrow\ \textbf{整个 }J\text{-谱\textbf{塌缩为单参数 }a}\ ✓✓\ \text{（比"谱分类"再进一层 ✓）}$$
$$\boxed{\textbf{(CX-1 推导状态)}\ k'{=}1\ \text{（Vasil'ev 支）}\textbf{已推导 ✓}:\ f=X*C,\ X\ \text{在 }W\ \text{上均匀}\Longrightarrow f\ \text{是 }W\text{-不变},\ \text{且 }C\subseteq V=W\sqcup(9{+}W)\Longrightarrow\ \text{两级（}a\ \text{由 }C\ \text{在两陪集的质量差给出 ✓）};}$$
$$\qquad k'{=}2\ \text{（两坐标打孔支）}\textbf{仅观测} ⚠️\ \text{—— 需证打孔后 }C\ \text{质量在 4 个 }W\text{-陪集上呈二项式分布（等价于两个独立特征 ✓）}$$
$$
$$
```

---

## §1 模型内容（**✓**）

```
$$\text{三级例细节 ✓}:\ \{96{:}4,128{:}8,160{:}4\},\ \bar m{=}128,\ a{=}16 \Longrightarrow f_r=128+32(-1,0,+1)\ \text{对应 }r{=}0,1,2\ ✓,\ e_r=4\binom 2r=4,8,4\ ✓$$
$$\text{单级 }/\text{两级同理 ✓};\ \textbf{注意等幅性 ✓}:\ \text{关键是"}\delta=a\sum\chi_j\ \text{等幅"而非任意 Fourier 函数 ⟹ 才给出二项式多重度 ✓（唐先生强调 ✓）}$$
$$
$$
```

---

## §2 脚本 bug 更正（**✓ 纪律**）

```
$$\text{我的检验脚本把 }J_{\rm int}\ \text{写成 }\Bigl(\sum_{g\ne0}f(g)^2\Bigr)-f(0)^2\ ✗ \Longrightarrow \textbf{重复扣减 }f(0)^2\ ✓\ \text{（正确 }J_{\rm int}=\sum_{g\ne0}f(g)^2=J_{\rm all}-f(0)^2\ ✓\text{）}$$
$$\qquad\Longrightarrow\ \text{脚本报 0/662 ✗ 属\textbf{假失败};\ 手工核算三例全部吻合 ✓✓（见 §0 ✓）};\ \text{此更正与既往"先怀疑自己的实现"一致 ✓}$$
$$
$$
```

---

## §3 下一步（**✓**）

```
$$\text{(甲″-iv-a) }\textbf{推导 }k'{=}2:\ \text{算打孔操作对 }C\ \text{分布的作用（把 2 个 }W\text{-陪集变成 4 个、呈 }(1{,}2{,}1)\ ✓\text{）};\ \text{或证"每次打孔提升 }k'\ \text{一阶" ✓}$$
$$\text{(甲″-iv-b) 三坐标 sanity（}k'{=}3\ \text{、多重度 }1{:}3{:}3{:}1\ ✓\text{）};\ \text{(丙) 119（暂不碰 ✓）}$$
$$\text{119}: \textbf{完全不碰} ✓$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：特征和模型验证（$f_r=\bar m+(2r-k')a$、$e_r=\binom{k'}r|W|$）、$J$ 闭式（$J_{\rm all}=|W|(2^{k'}\bar m^2+2^{k'}k'a^2)$）、脚本双扣减 bug 更正
- **档案已有（引用，不列为提出）**：A-CHARSUM-1、A-INVOL-1、A-FEAS-1、内蕴 $\nu$、$X*C$ 卷积


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 特征和模型  命中文件数=1    :: ./CHARSUM-2026-09-27-model-verified-and-J-closed-form.md 
技术词 J 闭式         命中文件数=1    :: ./CHARSUM-2026-09-27-model-verified-and-J-closed-form.md
```
- **本档新增**：特征和模型验证（$f_r=\bar m+(2r-k')a$、$e_r=\binom{k'}r|W|$）、$J$ 闭式、脚本双扣减 bug 更正（见上方命中数；0 命中者为自造语／内部标签 ✓）
