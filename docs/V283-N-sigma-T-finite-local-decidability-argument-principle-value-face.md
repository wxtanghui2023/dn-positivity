# V283 · **打甲（改造版）：$N_F(\sigma,T)$ 的有限局部可决定性** —— ⭐⭐⭐ **反例与定理两选皆现，但按类分**：抽象类（E1／E2）**可分离（构造性击穿）**；算术类（E4／E5）**不能**，且原因已定位为**两条**（零自由区＝A-leak；计数＝argument principle ⟹ **值面**）⟹ **甲 的正确归宿 ＝ case B（截断显式公式），其实力恰好是档案已审计的预算墙** ⭐⭐⭐⭐⭐

$$\boxed{\textbf{反例侧（E1／E2）}：\text{Beurling 型构造} ⟹ \exists\ \text{同 }S\text{-数据而}\ N(\sigma,T)\ \text{不同} ⟹ \textbf{有限谱压缩在抽象类内被击穿}} ✓✓$$
$$\boxed{\textbf{定理侧（E4／E5）}：\text{无已知分离构造};\ \text{原因二条}：\text{① 零自由区（A-leak）② 计数}\ ＝\ \textbf{argument principle ⟹ 显式公式（值面）}} ✓✓✓$$
$$\boxed{\text{故 甲}\ \textbf{不产生新墙}：\text{它}\ ＝\ \textbf{截断显式公式} ⟹ \text{其实力}\ ＝\ \text{档案已审计的预算墙（0.682 天花板／T² 律／support}>1）} ✓✓✓$$

> 委托 ✓ 唐先生 2026-09-16 11:28：甲**改造**——**不打"整数部分相同"（可能得到恒 0／恒 1 的废指标），也不打 $N_F(T)$ 总计数（可全部横向移动而完全不触及 RH）**；改为打 $$N_F(\sigma,T)=\#\{\rho:\Re\rho>\sigma,\ |\Im\rho|\le T\}$$ 的**有限局部可决定性** ✓✓；并要求 **"先做反例／定理二选一：固定有限 $S,\sigma,T$，到底能不能让 Euler-class 内两个同 $S$-数据对象具有不同的 $N(\sigma,T)$"** ✓；给出四格表（$\sigma>\tfrac12$ vs $\sigma\downarrow\tfrac12$ × $T<\infty$ vs $T=\infty$）与判据（若第一格就已只能依赖完整尾部 ⟹ **甲死**）✓
> 依据 ✓ `V282`（E1–E5／L3*）｜`V258`（值面）｜`V102`／`V162`／`V217b`（预算墙）｜`V172` §5a（A-leak）｜**argument principle／de la Vallée Poussin／Beurling 系统**（经典）✓
> 执行 ✓ 小灵｜**纸面 ✓（零数值 ✓）**｜纪律 ✓ 未用 RH 作推导 ✓；未跑 Lean ✓｜编号 ✓ `V283`（`id_claim.sh` ✓）

---

## §1 ⭐⭐⭐ 第一步：$N(\sigma,T)$ 的**本性**（本档关键）

$$\text{取矩形}\ R=[\sigma,\sigma+1]\times[-T,T];\qquad \boxed{N(\sigma,T)=\frac1{2\pi i}\oint_{\partial R}\frac{F'}{F}\,ds} ✓✓$$
$$\qquad \frac{F'}{F}=\underbrace{-\sum_p\sum_{k\ge1}(\log p)\,a_p^k\,p^{-ks}}_{\textbf{全素数求和}}\ +\ \underbrace{(\text{极点项})\ -\ (\text{archimedean／}\Gamma\ \text{项})}_{\textbf{archimedean 通道}} ✓✓$$
$$\Longrightarrow \boxed{N(\sigma,T)\ \textbf{本性属值面}：\text{它是"全素数求和 ＋ archimedean 项"的轮廓积分}} ✓✓✓$$
$$\qquad ⚠️\ \text{要点}：\text{卡点}\ \textbf{不是} \text{"尾部自由不可控"}（`V126`-L3），\ \text{而是}\ \textbf{"计数是全局解析操作"}（argument principle）✓✓$$
$$\qquad ⟹ \text{有限局部数据至多给}\ \textbf{截断 ＋ 误差}，\ \textbf{不能} \text{给精确值} ✓$$

---

## §2 ⭐⭐⭐⭐ 二选一（唐先生指令）：**两选皆现，但按类分**

$$\textbf{(A) 抽象类 E1／E2 ⟹ 反例成立（可构造）} ✓✓$$
$$\qquad \text{Beurling 广义素数系统}：\text{令前}\ N\ \text{个广义素数}\ \textbf{≡ 真素数}（\text{则}\ p\in S\ \text{处局部因子与}\ \zeta\ \text{同}）＋ \textbf{尾部工程化} ✓$$
$$\qquad \qquad ⟹ \text{零点星座可被工程（含}\ \tfrac12<\Re s\le1\ \text{区域，乃至}\ \Re s>1）⟹ \exists\ \text{同 }S\text{-数据而}\ N(\sigma,T)\ \text{不同} ✓✓$$
$$\Longrightarrow \boxed{\text{有限谱压缩}\ \textbf{在 E1／E2 内被击穿}};\ \text{但对象}\ \textbf{非算术}（\text{无 FE／非算术素数}）⟹ \text{出类} ⚠️✓$$

$$\textbf{(B) 算术类 E4／E5 ⟹ 定理侧：无已知分离构造} ✓✓$$
$$\qquad \text{本档}\ \textbf{未} \text{找到（也未宣称不存在）同 }S\text{-数据而}\ N(\sigma,T)\ \text{不同的算术对象} ✓$$
$$\qquad ⟹ \text{转而问"为什么不能"（§3）——这正是唐先生设定的第二分支} ✓✓$$

---

## §3 ⭐⭐⭐ 为什么算术类内不能：两条独立原因

$$\textbf{(i) 零自由区（经典，de la Vallée Poussin 型）}：\ \mathrm L(s,\chi)\ \text{在}\ \sigma>1-\frac{c}{\log(q(T+2))}\ \textbf{无零点} ✓✓$$
$$\qquad ⟹ \text{固定}\ (\sigma,T)\ \text{且}\ q\ \text{足够大} ⟹ N(\sigma,T)=0\ \textbf{可证} ⟹ \text{大范围内}\ \textbf{无分离} ✓$$
$$\qquad \qquad ⚠️\ \text{且该输入是}\ \textbf{archimedean／FE 型}（\text{零自由区证明用}\ \Gamma\ \text{因子与凸性}）⟹ \textbf{A-leak}（`V172` §5a）✓✓$$

$$\textbf{(ii) 计数}\ ＝\ \textbf{argument principle ⟹ 显式公式（§1）}：\ \text{精确值需}\ \textbf{全素数求和} ＋ \text{archimedean 项} ✓✓$$
$$\qquad ⟹ \text{有限局部数据只能给}\ \boxed{\text{截断 ＋ 误差}}（＝唐先生四格判据里的 \textbf{case B}）✓✓$$

---

## §4 ⭐⭐⭐⭐ 甲 的正确归宿（本档结论）

$$\boxed{\text{甲}\ \text{落在}\ \textbf{case B}：\text{“有限局部数据}\ \to\ \text{谱定位 ＋ 可证误差”}} ✓✓$$
$$\qquad \text{而 case B 的实力}\ \textbf{恰好就是档案已审计的预算墙}：$$
$$\qquad \qquad \boxed{\text{比例天花板}\ 0.682\ \big|\ \textbf{T}^2\ \text{律／预算越界}\ \big|\ \text{第三矩／高相关需 support}>1（`V102`／`V162`／`V217b`）} ✓✓✓$$
$$\Longrightarrow \boxed{\text{甲}\ \textbf{不产生新墙};\ \text{它是}\ \textbf{"截断显式公式"} \text{的又一名；其实力上限}\ \textbf{已被档案量出}} ✓✓✓$$
$$\qquad ⚠️\ \text{即：}\text{唐先生四格判据的"若第一格就已只能依赖完整尾部 ⟹ 甲死"}\ \textbf{成立}，\ \text{但死法更精确}：$$
$$\qquad \qquad \text{第一格不是"依赖完整尾部"，而是"}\textbf{本性属值面} \text{"} ⟹ \text{连"完整尾部"都不够（还需 archimedean 项）} ✓✓$$

---

## §5 四格表（判定填写）

| | $T<\infty$ | $T=\infty$ |
|:--|:--|:--|
| $\sigma>\tfrac12$ | **第一格**：E1／E2 ⟹ **可分离（构造）**；E4／E5 ⟹ **落值面 ＋ A-leak**（§1§3）⟹ 无分离构造 | **第二格**：$N(\sigma,\infty)$；$\sigma>1$ ⟹ **恒 $0$**（平凡）；$\tfrac12<\sigma\le1$ ⟹ **GRH 型** |
| $\sigma\downarrow\tfrac12$ | **第三格**：临界逼近；同落**值面**（§1） | **第四格**：$\boxed{\mathrm{RH}}$ |

---

## §6 判词 ＋ 边界 ＋ 净产出

$$\boxed{\textbf{V283 判词}：\text{①}\ N(\sigma,T)\ \textbf{本性属值面}（argument principle）;\ \text{② 抽象类可分离（构造），算术类无分离构造};\ \text{③ 第二原因}\ ＝\ \text{零自由区（A-leak）};\ \text{④ 甲}\ ＝\ \text{截断显式公式} ⟹ \text{落已审计预算墙}} ✓✓✓$$

```
① ⚠️ 本档**未**宣称"算术类内不存在同 S-数据而 N(σ,T) 不同的对象" ✗；只报"无已知构造"＋原因定位 ✓
② ⚠️ (A) 依赖 Beurling 系统（引用·经典，未逐条复核）；(i) 依赖 de la Vallée Poussin 型零自由区（引用）⚠️
③ ⚠️ §1 的显式公式展开为**标准恒等式**（本档按标准形式引用，未逐字推导）⚠️
④ ⚠️ §4 的"预算墙"为**引用** `V102`／`V162`／`V217b`（未重算）⚠️
⑤ 未用 RH 作推导 ✓；未跑 Lean ✓；零数值 ✓
```

```
① ⭐⭐⭐ **$N(\sigma,T)$ 的本性**：argument principle ⟹ **全素数求和 ＋ archimedean 项** ⟹ **属值面**；卡点不是"尾部自由"，而是"**计数是全局解析操作**" ✓✓
② ⭐⭐⭐ **二选一：两选皆现** —— E1／E2 **可分离（Beurling 构造，出类）**；E4／E5 **无分离构造** ✓✓
③ ⭐⭐ **算术类内不能的两条原因**：① **零自由区（A-leak）**；② **计数＝显式公式（值面）** ✓✓
④ ⭐⭐⭐ **甲的正确归宿**：**case B（截断显式公式）**，其实力**恰好＝档案已审计预算墙**（0.682／T² 律／support $>1$）⟹ **不产生新墙** ✓✓✓
⑤ ⭐ **四格表填毕**：第一格两分类判定；第二格 $\sigma>1$ 恒 0、$\tfrac12<\sigma\le1$ GRH 型；第三／四格 RH 型 ✓
【下一步（本档不预判，供唐先生选）】
  (甲′) 攻 **case B 的预算天花板本身**（即"0.682／T² 律"是否是硬上限）—— ⚠️ 但注意这正是 `V102`／`V162` 的既有结论范围 ✓
  (乙) 承认第一格属值面 ⟹ 转 §E.4 第二条出路（改变目标）✓
```
