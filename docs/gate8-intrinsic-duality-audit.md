# 第⑧关：Intrinsic Duality Audit（对象层，终止性分析）

**日期**：2026-09-10 ｜ 承接 `68e91b9` ｜ 结果：对算术对象，可用的内生自对偶只有两类；一类被你的 req 4 排除，另一类缺几何

---

## 0. 问题（唐先生的七条限制）

是否存在由 $(+,\times,\le)$ 自身生成的非平凡对偶
$$\mathscr D:\mathcal X\to\mathcal X^\vee,\qquad \mathscr D^2\simeq1,$$
且：不预装 ζ／零点／$s\mapsto1-s$；不把 Fourier/Mellin 直接命名为答案；不只是 $n\leftrightarrow x/n$（已死在 1/4 族）；
$$\boxed{\mathscr D\ \text{必须改变【描述方式】，而非仅重排数据}}$$

## 1. 数学事实：自对偶不是稀缺的——它由【极化】被迫产生

梳理被迫出现自对偶的机制，只有有限的几类：
```
(a) 极化/配对    : 存在非退化配对（双线性/二次型）⟹ 结构与其对偶典范同构
(b) Pontryagin   : LCA 群 ⟹ 特征群，典范 D²≅id（【就是 Fourier】）
(c) Stone/Gelfand: 空间 ↔ 代数（布尔代数/分配格/C*-代数）；序–拓扑型
(d) Galois 联络  : 序–代数对应，D² 为闭包算子；D²=id ⟺ 完美对应
(e) Poincaré–Verdier : 光滑射影几何/层论；【不是 Fourier】
(f) Tannakian   : 带纤维函子的范畴 ≅ 群概形表示
```

## 2. 范畴重述（对 req 7 的精确化）

"$\mathscr D$ 改变描述方式" $\iff$ **所涉范畴与其反范畴等价**（contravariant equivalence）。
已知自对偶范畴：有限交换群、有限维向量空间、有限分配格、profinite 群——
$$\boxed{\text{它们全部落在 (b) 或 (c) 类 = Fourier / 序–拓扑型}}$$
⟹ 落在你的 req 4 排除区内。

## 3. 对【算术对象】的两类可用自对偶

```
(I) Pontryagin / 阿代尔自对偶  ⟹ Tate 论文明证：ζ 的泛函方程
    来自 A_ℚ 的 Poisson 求和
    ⟹ 满足 req 1,2,3,5,7，但【违反 req 4（它就是 Fourier）】
    ⟹ 而且它【正是】s↔1−s 的来源

(II) Poincaré–Verdier / 层论对偶  ⟹ 非 Fourier ✓
     但它需要"几何"（光滑射影簇 / ℓ-进上同调）
     char 0 的 Spec ℤ 没有这套几何
     ⟹ 这正是本项目最早的发现：函数域靠 Poincaré 对偶 + Hodge 指标，
       char 0 缺的是这套几何
```

$$\boxed{\text{⟹ 对算术对象，内生自对偶只有这两类：一类是 Fourier（被 req 4 排除，且它已给出泛函方程），}\\
\text{另一类需要缺失的 char 0 几何}}$$

## 4. 第⑧关裁决（按你的终点判据）

```
所有 intrinsic duality ⟶ 要么 Fourier/Pontryagin/Stone（req 4 排除）
                        要么 Poincaré–Verdier（需 char 0 几何 = 已知缺失）
⟹ 【不产生】既非 Fourier、又内生给二阶 global duality 的新对象
⟹ 按你的判据：机制搜索【结束】
```

**并且残余被精确指认为一个【已知研究纲领】而非新机制**：
```
非 Fourier 的唯一落点 = 层/上同调对偶用于算术
= Arakelov / 算术层论 / Connes 算术 site–scaling topos 方向
已知障碍 = quartet 的 C1*（char 0 缺整性/几何），与本项目最早的结论一致
（注：本项目 kill 掉的是该纲领中一个具体的 prolate–Weil 桥，
  不是这套对偶框架本身——框架未被我们审计为死）
```

## 5. 状态

```
机制层（约束/延拓/自对偶的机械构造）: 【结束】
对象层残余                          : 层/上同调对偶用于算术（已知纲领，已知障碍）
新增门槛 P-Dual : 候选必须申报其自对偶属 (a)-(f) 哪一类；
                  (b)/(c) 类一律预筛淘汰（req 4）；(e) 类必须给出 char 0 几何
```

**未写程序。RH 本身未动。**
