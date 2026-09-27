已查地图：已跑 scripts/prework_map_check.sh E=285 Boolean-image g T^{-1} mod 11 ⟹ 执行自唐先生 15:45 指令（重审 P0→P3 ✓）；本档 = **E-等价性纠错 ✓ ＋ 新 P1（$g$-形）定理级审计 ✓**。
D0: 本档对象 = (i) $E\ge286$ 之陈述纠错；(ii) $g=11T^{-1}\delta\in\{-1,10\}$ 之可达性
D1: 3（**纠错 ✓（"等价"→"充分"）**；**模 11 定理 $\ker(T\bmod 11)=\mathrm{span}\{\mathbf 1\}$ ✓✓**；**$g$-形 ⟺ 整数松弛 ＋ 二值性 ⟹ 线性内容 = 整数性 ✗**）

# P1 重审：E-纠错与模 11 定理（2026-09-27）

## §0 结论（先给）

```
$$\boxed{\textbf{(OA-1 ✅接受纠错（唐先生 ✓）)}\ \text{我此前写"}"E\ge286\iff\text{119-码不存在"}\ \text{—— }\textbf{"}等价"\ ✗\ \text{用词错误 ✓}}$$
$$\qquad\textbf{正确陈述 ✓}:\ E=\sum_x(b(x)-1)=11|C|-1024\ \text{是 }|C|\ \text{的\textbf{纯函数 ✓}（与覆盖无关 ✓）} \Longrightarrow \boxed{"E\ge286"\iff |C|\ge120}\ ✗\ \text{—— 与"119-码不存在"不是同一命题 ✗}}$$
$$\qquad\textbf{但证明方案仍有效 ✓（改为"充分" ✓）}:\ \boxed{\text{若能从覆盖假设推出 }E\ge286 \Longrightarrow |C|\ge120\ \text{与 }|C|=119\ \text{矛盾 ⟹ 不存在}}\ ✓\ \text{—— 这是\textbf{充分}路线，非等价 ✗}$$
$$\qquad\textbf{档案处置 ✓}:\ \text{已在 `ASSETS-REGISTRY`／后续档中按此口径修正（本档为修正记录 ✓）};\ \text{其余 }\delta\text{-型恒等式（}\sum\delta=285,\ \sum b\delta=4(A_1{+}A_2),\ \sum\delta^2=\cdots\text{）保持不变 ✓}$$
$$\boxed{\textbf{(OB-1 ⭐⭐模 11 定理（本档新 ✓✓）)}\ T=I+\sum_{i=1}^{10}\sigma_i\ \text{被 Walsh 基对角化，特征值 }11-2w\ (w{=}0..10\ ✓);\ \bmod 11\ \text{下}\ 11-2w\equiv-2w\ ✓}$$
$$\qquad\Longrightarrow\ \boxed{\ker\!\bigl(T\bmod 11\bigr)=\mathrm{span}\{\mathbf 1\}}\ ✓✓\ \text{（唯一零特征值 }w{=}0\ ✓;\ 1024\equiv1\bmod11\ \Longrightarrow\ \text{Walsh 基在 }F_{11}\ \text{上仍可逆 ✓）}$$
$$\qquad\Longrightarrow\ \textbf{推论 ✓}:\ \boxed{Tg\equiv 0\ (\bmod 11)\iff g\ \text{各分量同余（}\equiv c\ \text{常数}\ ✓\text{）}}\ ✓✓$$
$$\boxed{\textbf{(OC-1 ⭐}g\text{-形审计（唐先生新 P1 ✓）)}\ \text{由 }f\in\{0,1\},\ b=1+\delta=C_1\ \text{与 }T\mathbf 1=11\cdot\mathbf 1:\ \boxed{f=\tfrac1{11}\mathbf 1+T^{-1}\delta},\ \boxed{g:=11T^{-1}\delta=11f-\mathbf 1\in\{-1,10\}^{1024}}\ ✓✓}$$
$$\qquad\textbf{等价改写 ✓}:\ \boxed{Tg=11\delta,\ \delta\in\mathbb Z_{\ge0}^{1024},\ \sum\delta=285}\ ✓;\ \text{由 (OB-1)：}Tg\equiv0\bmod11\iff g\equiv c\mathbf 1 \Longrightarrow \text{与 }g\in\{-1,10\}\ \text{合起来 ⟺ }f=(g{+}1)/11\in\{0,1\}\ ✓✓}$$
$$\qquad\Longrightarrow\ \boxed{\textbf{线性内容 = }\{f\in\mathbb Z^{1024}:\ Tf\ge1,\ \sum f=119\}\ (\textbf{整数/多重覆盖松弛 ✓})};\ \text{非线性内容 = 二值性 = Booleanity ✓}$$
$$\qquad\Longrightarrow\ \boxed{\text{故 }g\text{-形\textbf{不产生}新必要条件 ✗：其"线性部分"恰是\textbf{整数性}，其余仍是原问题 ✓}}\ \text{（与 A-INCIDENCE-FIX-1 的 Booleanity 等价判同一结论 ✓，本档给出\textbf{模 11 的成因 ✓}）$$
$$
$$
```

## §1 整数松弛的可行性（**✓ 诚实标注**）

```
$$\text{分数松弛（}f\in\mathbb R_{\ge0}\text{）在 }119\ \text{处\textbf{可行 ✓}（}f\equiv 119/1024\Rightarrow Tf=1.278\ge1\ ✓\text{）} \Longrightarrow \text{无阻碍 ✗};\ \text{其最优}=1024/11=93.09\ ✓（档案 M-2A ✓）}$$
$$\text{整数松弛（}f\in\mathbb Z^{1024}\text{）：}\ \textbf{本档不判定其 }119\text{-可行性 ⚠️};\ \text{已知 }K(10,1)\le120\ ✓\ (\text{Östergård/双源 ✓})\ \text{—— 但那是\textbf{无重数}码，非多重覆盖 ✗}$$
$$\qquad\textbf{诚实边界 ✓}:\ \text{若整数松弛在 }119\ \text{不可行 ⟹ 那是\textbf{新结果}（且 ⟹ 不存在 ✓）；但本档\textbf{未}证明其可行或不可行 ⚠️（需计算 ✗）}$$
$$
$$
```

## §2 判定与 P0→P3 重述（**✓ 按唐先生 ✓**）

```
$$\textbf{P0 ✓ 无问题}:\ \text{目标 }K(10,1)\ge120\ \text{（}K\le120\ \text{有历史构造 ✓）};\ \text{尖锐形式}=\text{不存在 }119\text{-cover} ✓$$
$$\textbf{P1（修正后 ✓）}:\ \boxed{\forall C,\ |C|=119\Longrightarrow\exists x:\ b(x)=0}\ \text{（等价：}\nexists C\ \text{with }b\ge1\ ✓\text{）};\ E=285\ \text{只是\textbf{恒等式}，不作 P1（纪要 ✓）}$$
$$\textbf{P2 ✓}:\ 120\text{-构造在档 ✓};\quad \textbf{P3 ✗ 未完成}:\ \text{119 不存在} \iff K{=}120\ ✓$$
$$\textbf{层级图（唐先生 ✓，本档确认 ✓）}:\ \text{profile ⟶ pair-incidence ⟶ triple-incidence ⟶ local/SA}\ \text{全部塌缩 ✓} \Longrightarrow \textbf{残余}=\text{Boolean/整数性（irreducible integrality ✓）}$$
$$\qquad\Longrightarrow\ \textbf{路线 A（Boolean-image 直接数学）}:\ \text{本档证明其\textbf{线性内容}=\text{整数性}} ✗ \Longrightarrow \text{不能独立于此产生必要条件 ✓};\ \textbf{路线 B（高阶 Lasserre/SOS）} = \text{唯一同族残余 ✓}$$
$$
$$
```

## §3 状态（**✓**）

```
$$\boxed{K(10,1)=119\ \text{保持 UNKNOWN};\ \text{路线 A 定理级封口 ✓（第 21 次）};\ \text{未跑 solver ✓};\ \text{不写禁止表述 ✓}}$$
$$\textbf{净收获 ✓}:\ \text{(i) E-陈述纠错 ✓（"等价"→"充分" ✓）；(ii) }\ker(T\bmod11)=\mathrm{span}\{\mathbf1\}\ \text{定理 ✓；(iii) }g\text{-形的线性内容=整数性之证明 ✓（解释了为何 Boolean-image 路线不能独立奏效 ✓）}$$
$$
$$
```

## 【技术词回查】（定稿前逐字输出）

- **本档新增**：$E\ge286$ 陈述纠错（充分而非等价）、$\ker(T\bmod 11)=\mathrm{span}\{\mathbf 1\}$ 定理、$g$-形线性内容=整数性之证明
- **档案已有（引用，不列为提出）**：Booleanity 等价（A-INCIDENCE-FIX-1）、M-2A（LP $1024/11$）、L3B/Level 4、AMEND-35


## 【技术词回查】（定稿前逐字输出）

实跑 `scripts/tech_word_check.sh` 逐字输出：
```
技术词 模 11 定理    命中文件数=1    :: ./P1-REAUDIT-2026-09-27-E-correction-and-the-mod-11-theorem.md 
技术词 整数性        命中文件数=57   :: ./CHAIN-VW-2026-09-27-self-contained-b-le-2-and-full-corollaries.md ./C141-today-net-output-card-2026-09-19.md ./GAP-direct-attack-canonical-form-and-A2-handle.md
```
- **本档新增**：$E\ge286$ 陈述纠错（充分而非等价）、$\ker(T\bmod 11)=\mathrm{span}\{\mathbf 1\}$ 定理、$g$-形线性内容＝整数性之证明（见上方命中数；0 命中者为自造语／内部标签 ✓）
