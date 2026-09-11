# SEL1：**selection 原语**审计 —— 你的例子不满足你自己的 §7；谱一半被 AEB1 封死

**依据**：唐先生 2026-09-11 10:53（选择原语拆解；Euclid 型；§7 要求 $D(a,b,c)\mapsto\mathcal A_{a,b,c}$ 改变下一层可行域）｜**约束**：无 $1/2$ 输入；L2 未动
**脚本**：`scripts/SEL1_selection_primitive.py`｜标注：【核验】【推导】【引用】

---

## §0 校准 + Euclid 序列【核验】
```
校准：isprime(2,3,97)=True；(4,91)=False；2·3·5+1=31 ✓
序列（P_0={2}，q=min{prime | N+1}）：q = 3, 7, 43, 13, 53, 5, 6221671  ⟹ 与已知 Euclid–Mullin 一致 ✓
（第 9 项 38709183810571 起需分解天文数字 ⟹ 不可试除，已注明）
```

## §1 你的 §1 反向推导：我接受并给精确形式
$$T(a)\notin\{[a],\chi(a),\operatorname{Tr}(a)\}\ \text{（均先消灭 element-level 信息）}\ \Longrightarrow\ T(a)=\operatorname*{arg\,ext}_b\mathcal C(a,b)$$
$$\boxed{\text{canonical selection} = \text{算术内生的【非对称约束】} + \text{唯一极值解}}$$

## §2 精确形式化：selection **两种类型**（这是本轮的关键区分）
| 类型 | 数学形式 | 是否为你的 §7 所要求 |
|---|---|---|
| **(α) 选择器型** | 状态 ⟹ **唯一值**（函数） | ✗（动作空间不变） |
| **(β) 可行域型** | 状态 ⟹ **允许动作集合**，且集合**改变**（关系/算子） | ✓ |
$$\text{canonical 地"唯一选出"}\iff\text{由【泛性质】确定（伴随/极限/初对象）—— 这是唯一 canonical 的极值来源}$$

## §3 【核验】⭐ 你的 §2 例子**不满足**你的 §7
```
计算显示：Euclid 过程是【一条确定轨道】——每步只有一个动作，且动作【恒定】为"追加 q"
⟹ 允许动作集合【从不改变】⟹ 它属于 (α) 选择器型，不是 (β) 可行域型 ✗
⟹ 按你自己的 §7 判据，Euclid 型【不合格】（这比"退化成 Euclid–Mullin"更精确）
```

## §4 ⭐⭐ 真正的 §7 型动力学必须**分支** ⟹ 然后 AEB1 直接封死**谱那一半**
```
(β) 型要求 |A| > 1（分支）且区域有时【收缩】（否则单调 ⟹ 无边界）
情形 i ：【有限分支】⟹ König（AEB1 Test D：903/903）⟹ 每层可实现 ⟹ 必有无穷线程 ⟹ **无逃逸边界** ✓
情形 ii：【无限分支】⟹ 逃逸可能（AEB1 Test C：S_n={k≥n} ✓），但逃逸要求阶段**非离散**
        而【离散阶段（有限或无限）】⟹ 极限【零维/全不连通】（AEB1 附）⟹ **无 connected 1D 边界** ✓
⟹ **两种情形下，谱参数都【不能】作为边界坐标出现** —— 与分支是否有限无关 ✓✓
```

## §5 canonical "可行域型"结构的来源穷举（对照五条死路）
| 来源 | 判定 |
|---|---|
| congruences / CRT | ✗（AOB5 已判：兼容复形是 flag complex） |
| Diophantine 方程 | ⟹ 算术群 / mutation ⟹ 自守影子 ✗（D2） |
| local–global（Brauer/$\mathrm{Sha}$） | ⟹ L-值测度 ✗（E2/AOB2） |
| valuations / divisor | ✗（E1/D1） |
| cyclotomic / Legendre / Hilbert / Rédei | ⟹ character 箱 ✗（AOB1/AOB2） |
| Massey / 高阶上同调 | ⟹ Tate 对偶 ⟹ L-值 ✗（AOB2） |
| 泛性质闭合（completion / localization / free） | ✗（E1/F1） |
$$\boxed{\text{无 canonical 来源落在五条死路之外 —— 你的 §7 要求目前【无实例】}}$$

## §6 结论：你的架构**把两个问题分开了**（这是真实进步）
```
✅ selection 一半：**可以做出来**（Euclid 型已示范 canonical、element-level 的选择 ✓）
   并且它**天然绕开 AOB3 的共轭类障碍**（因为不是群作用，不存在代表元选择问题）✓✓
✗ spectral 一半：由 AEB1 + König **结构性封死** —— 谱参数不能是边界坐标 ✓
⟹ 净结果：**架构新颖、selection 可建，但 spectral output 仍被拓扑挡死**
   即：你的 §4 判断（"解决 selection 但不解决 spectral localization"）被【结构性证明】而非仅经验判断 ✓
```

## §7 我本轮的错（ERR 纪律）
```
ERR#8：pkill -f 自匹配 —— 命令串含脚本名 ⟹ 杀掉自己的 shell（**重复犯了此前已记录的教训**）
ERR#9：三引号/普通引号混用导致 SyntaxError（脚本第一次没跑起来）
```

## §8 边界
```
· §0 序列与校准为【核验】；§3/§4 为【核验 + 引用（König/零维性）】
· §2/§5/§6 为【推导/结构性】；§5 各行的归属引用本项目已注册结论
· 【未做】未输入 1/2；未构造模型；未改 L2；未声称与 ζ 连接
```

## §9 提交链
```
fe6f981 AEB1 附 → 本篇（SEL1：selection 原语审计 + (α)/(β) 区分 + 谱半封死）
```
